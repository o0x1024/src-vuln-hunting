"""Validate all planned0231 reviews before any target/ledger append."""
import ast,json,collections,re
from stage import targets,dbopen
from recover import T,S,A,W,digest
b=json.loads((W/'batch-0231.json').read_text())
assert len(b)==200 and sum(len(r['post_ids']) for r in b)==202
rows=[]
for line in (W/'spec0231.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);rows.append((int(i),d,targets(ts),n))
 assert d in {'new_knowledge','merged','corrected','excluded'} and n.strip()
assert len(rows)==200 and {r[0] for r in rows}==set(range(1,201))
actual=json.loads((W/'media-actual-0231.json').read_text())
new=json.loads((W/'media-new-0231.json').read_text())
assert len(actual)==96 and {(r['name'],r['sha256']) for r in actual}=={(r['name'],r['sha256']) for r in new}
assert len({r['sha256'] for r in actual})==96
known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()}
media=[]
for line in (W/'media-spec0231.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);media.append((int(i),d,targets(ts),n))
 assert d in {'distilled','no_technical_content','insufficient_technical_detail'} and n.strip()
assert len(media)==96 and {r[0] for r in media}==set(range(96))
for r in actual:
 assert r['detail']=='original' and r['viewed_at'] and r['sha256'] not in known
 assert digest((S/'media'/r['name']).read_bytes())==r['sha256']
db=dbopen()
for r in b:assert not db.execute('select 1 from reviews where body_sha256=?',(r['body_sha256'],)).fetchone()
db.close()
fs=next(ast.literal_eval(x.value) for x in ast.parse((W/'native0231.py').read_text()).body if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='facets' for y in x.targets))
assert fs==json.loads((W/'facets0231.json').read_text())
assert len(fs)==522 and len({t for _,t,_ in fs})==522
ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==628 and all(pid in ids for pid in urls)
for f,t,body in fs:
 assert (T/'references'/f).is_file() and ('## '+t) not in (T/'references'/f).read_text()
 assert '/Users/len/x-bugbounty' not in body
c=(T/'references/research/community-distillation.md').read_text()
assert c.count('\n## 首轮提炼范围与未采纳内容\n')==1
print(json.dumps(dict(groups=len(b),posts=202,body_dispositions=dict(collections.Counter(r[1] for r in rows)),media=96,media_dispositions=dict(collections.Counter(r[1] for r in media)),facets=522,topics=len({f for f,_,_ in fs}),batch_bound_URLs=len(urls)),ensure_ascii=False))

for i,dis,ts,note in media:
 if dis=='distilled':
  pid=actual[i]['name'].split('-')[0]
  for target in ts:assert any('references/'+f==target and 'https://x.com/i/status/'+pid in body for f,t,body in fs),(i,target,pid)
print('All distilled image targets bound to exact batch post source')

for i,dis,ts,note in media:
 if dis=='distilled':
  for target in ts: assert any('references/'+f==target and actual[i]['name'] in body for f,title,body in fs),(i,target)
print('Exact filename evidence binding verified')

current=json.loads((W/'media-before-0231.json').read_text())
prior=json.loads((W/'known0231.json').read_text())
assert len(current)==107 and len({r['sha256'] for r in current})==100 and len(prior)==4
observations={actual[i]['sha256']:(dis,ts) for i,dis,ts,note in media}
actual_hashes={r['sha256'] for r in actual}
for r in prior:
 assert r['sha256'] in known and r['sha256'] not in actual_hashes
 old=r['prior'];assert old['sha256']==r['sha256']
 value=(old['disposition'],old['targets'])
 if r['sha256'] in observations:assert observations[r['sha256']]==value
 else:observations[r['sha256']]=value
bound=0
for r in current:
 assert digest((S/'media'/r['name']).read_bytes())==r['sha256']
 dis,ts=observations[r['sha256']]
 if dis=='distilled':
  bound+=1;pid=r['name'].split('-')[0]
  for target in ts:
   assert any('references/'+f==target and r['name'] in body and 'https://x.com/i/status/'+pid in body for f,t,body in fs),(r['name'],target)
assert bound==73
print('All107 current paths rehashed; all73 distilled occurrences including known/duplicate images have exact filename/source/targets')
