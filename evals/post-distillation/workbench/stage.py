"""This task's bookkeeping only. No post code execution or network access."""
import argparse,collections,json,re,sqlite3
from datetime import datetime,timezone
from pathlib import Path
from recover import T,S,A,W,IMAGE_PATTERN,complete_text,digest
SCOPE='complete saved text including non-generic image alt text and trailing captions; image pixels reviewed separately; missing images and external full text waived by user and count as covered; unavailable unsaved thread continuations are outside saved-post coverage'
ALIASES=dict(xss='by-type/xss',waf='by-type/waf-bypass',sql='by-type/sql-injection',auth='by-type/authn-session',access='by-type/idor-access-control',secret='by-type/info-secrets',ssrf='by-type/ssrf',cmd='by-type/cmd-injection-rce',lfi='by-type/lfi-path-traversal',ssti='by-type/ssti',android='by-type/mobile-android',ios='by-type/mobile-ios',graphql='by-type/graphql',smart='by-type/smart-contract',xxe='by-type/xxe',csrf='by-type/csrf',oauth='by-type/oauth-oidc',host='by-type/host-header',logic='by-type/business-logic',deser='by-type/deserialization-rce',prop='by-type/api-property-pollution',click='by-type/clickjacking',doc='by-type/document-rendering',files='by-type/file-upload',takeover='by-type/subdomain-takeover',redirect='by-type/open-redirect',cloud='cloud/cloud-misconfiguration',container='cloud/container-k8s-security',web='discovery/web-and-api',passive='discovery/passive-and-services',client='discovery/client-and-cloud',records='discovery/records-and-incremental',strategy='hunting-strategy',fuzz='targeted-fuzzing',report='reporting',impact='impact-and-acceptance',scope='scope-and-rules',experiment='experiment-design',expert='expert-reasoning',source='source-audit',business='business-modeling',ldap='by-type/ldap-injection')
def targets(ts):
 out=['references/'+ALIASES[k]+'.md' if k in ALIASES else k for k in ts.split(',') if k]
 assert all((T/f).is_file() for f in out),out
 return out
def dbopen():
 db=sqlite3.connect(W/'work.sqlite3');db.row_factory=sqlite3.Row;return db
def status():
 db=dbopen(); s=json.loads((A/'status.json').read_text()); reviewed={r[0] for r in db.execute('select body_sha256 from reviews')}; groups=collections.defaultdict(list)
 for r in db.execute('select id,body_sha256 from posts'):groups[r['body_sha256']].append(r['id'])
 ledger=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
 assert {r['body_sha256'] for r in ledger}==reviewed and len(ledger)==len(reviewed)
 media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()];assert len({r['sha256'] for r in media})==len(media)
 s.update(updated_at=datetime.now(timezone.utc).isoformat(),body_reviewed_groups=len(reviewed),body_reviewed_posts=sum(len(v) for k,v in groups.items() if k in reviewed),remaining_body_groups=len(groups)-len(reviewed),body_followup_groups=db.execute("select count(*) from reviews where disposition='needs_followup'").fetchone()[0],media_visually_reviewed_unique_contents=len(media),media_review_dispositions=dict(collections.Counter(r['disposition'] for r in media)),all_posts_content_distilled=False,review_scope=SCOPE)
 (A/'status.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');db.close();return s
def prepare(label,count,max_chars=27000):
 db=dbopen();batch=[];size=0;display=[]
 for r in db.execute('select b.* from bodies b left join reviews r using(body_sha256) where r.body_sha256 is null order by length(b.first_id),b.first_id limit ?',(count,)):
  body=r['body'];assert digest(body.encode())==r['body_sha256']; posts=[dict(p) for p in db.execute('select * from posts where body_sha256=? order by id',(r['body_sha256'],))]
  for p in posts:assert digest((S/'posts'/(p['id']+'.md')).read_bytes())==p['document_sha256']
  part=f"\n[{len(batch)+1:03}] ids={','.join(p['id'] for p in posts)}\n{body}\n"
  if batch and size+len(part)>max_chars:break
  batch.append(dict(body_sha256=r['body_sha256'],post_ids=[p['id'] for p in posts],body_chars=len(body)));display.append(part);size+=len(part)
 out=W/('batch-'+label+'.json');assert not out.exists();out.write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n');db.close()
 (W/('body-display-'+label+'.txt')).write_text(''.join(display));return dict(batch=label,groups=len(batch),posts=sum(len(r['post_ids']) for r in batch),chars=size,first=batch[0]['post_ids'],last=batch[-1]['post_ids'])
def inventory(label):
 b=json.loads((W/('batch-'+label+'.json')).read_text());known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()};available={};missing=set()
 for r in b:
  for pid in r['post_ids']:
   for m in re.finditer(IMAGE_PATTERN,(S/'posts'/(pid+'.md')).read_text()):
    ref=m.group(2)
    if ref.startswith('../media/'):
     name=ref[9:];p=S/'media'/name
     if p.is_file():available[name]=dict(name=name,sha256=digest(p.read_bytes()))
     else:missing.add(name)
    else:missing.add(ref)
 unique={}
 for r in available.values():unique.setdefault(r['sha256'],r)
 new=[r for h,r in unique.items() if h not in known]
 for name,data in [('media-before',list(available.values())),('media-new',new),('media-missing',sorted(missing))]:
  p=W/(name+'-'+label+'.json');assert not p.exists();p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 return dict(available=len(available),unique=len(unique),known=len(unique)-len(new),new=len(new),missing=len(missing))
def record(label):
 b=json.loads((W/('batch-'+label+'.json')).read_text()); spec=(W/('spec'+label+'.txt')).read_text();rows=[]
 for line in spec.strip().splitlines():
  n,d,ts,note=line.split('|',3);rows.append(dict(n=int(n),disposition=d,targets=targets(ts),note=note))
 assert len(rows)==len(b) and {r['n'] for r in rows}==set(range(1,len(b)+1));rows.sort(key=lambda r:r['n']);db=dbopen();out=[]
 for item,v in zip(b,rows):
  assert not db.execute('select 1 from reviews where body_sha256=?',(item['body_sha256'],)).fetchone()
  assert v['disposition'] in {'new_knowledge','merged','corrected','excluded','needs_followup'} and v['note'].strip()
  posts=[dict(p) for p in db.execute('select * from posts where body_sha256=?',(item['body_sha256'],))];assert {p['id'] for p in posts}==set(item['post_ids'])
  for p in posts:
   raw=(S/'posts'/(p['id']+'.md')).read_bytes();assert digest(raw)==p['document_sha256'];assert digest(complete_text(re.split(r'^---\s*$',raw.decode(),maxsplit=1,flags=re.M)[1]).encode())==p['body_sha256']
  out.append(dict(body_sha256=item['body_sha256'],post_ids=item['post_ids'],disposition=v['disposition'],targets=v['targets'],note=v['note'],batch='batch-'+label,review_scope=SCOPE,reviewed_at=datetime.now(timezone.utc).isoformat()))
 for r in out:db.execute('insert into reviews values(?,?,?,?,?)',(r['body_sha256'],r['disposition'],r['note'],json.dumps(r['targets']),r['batch']))
 with (A/'reviews.jsonl').open('a') as f:
  for r in out:f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
 db.commit();db.close();return status()
def media(label,media_batch):
 actual=json.loads((W/('media-actual-'+label+'.json')).read_text());new=json.loads((W/('media-new-'+label+'.json')).read_text());assert len(actual)==len(new) and {(r['name'],r['sha256']) for r in actual}=={(r['name'],r['sha256']) for r in new}
 spec={}
 for line in (W/('media-spec'+label+'.txt')).read_text().strip().splitlines():
  i,d,ts,note=line.split('|',3);assert int(i) not in spec;spec[int(i)]=(d,targets(ts),note)
 assert len(spec)==len(actual) and set(spec)==set(range(len(actual)));known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()};out=[]
 for i,r in enumerate(actual):
  assert r['detail']=='original' and r['sha256'] not in known and digest((S/'media'/r['name']).read_bytes())==r['sha256'];d,ts,note=spec[i]
  assert d in {'distilled','no_technical_content','insufficient_technical_detail'} and note.strip()
  out.append(dict(sha256=r['sha256'],example_post_id=r['name'].split('-')[0],image_name=r['name'],disposition=d,targets=ts,note=note,review_scope='entire visible image; small text, crop and redaction limits explicitly retained; no source execution or external destinations',reviewed_at=r['viewed_at'],batch=media_batch));known.add(r['sha256'])
 with (A/'media-reviews.jsonl').open('a') as f:
  for r in out:f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
 return dict(media_added=len(out),dispositions=dict(collections.Counter(r['disposition'] for r in out)))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('command',choices=['status','prepare','inventory','record','media']);p.add_argument('--label',default='0097');p.add_argument('--count',type=int,default=106);p.add_argument('--max-chars',type=int,default=27000);p.add_argument('--media-batch',default='media-0091');a=p.parse_args()
 result={'status':lambda:status(),'prepare':lambda:prepare(a.label,a.count,a.max_chars),'inventory':lambda:inventory(a.label),'record':lambda:record(a.label),'media':lambda:media(a.label,a.media_batch)}[a.command]();print(json.dumps(result,ensure_ascii=False))
