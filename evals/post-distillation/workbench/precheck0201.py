"""Validate all planned0201 reviews before any target/ledger append."""
import ast,json,collections,re
from stage import targets,dbopen
from recover import T,S,A,W,digest
b=json.loads((W/'batch-0201.json').read_text())
assert len(b)==163 and sum(len(r['post_ids']) for r in b)==164
rows=[]
for line in (W/'spec0201.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);rows.append((int(i),d,targets(ts),n))
 assert d in {'new_knowledge','merged','corrected','excluded'} and n.strip()
assert len(rows)==163 and {r[0] for r in rows}==set(range(1,164))
actual=json.loads((W/'media-actual-0201.json').read_text())
new=json.loads((W/'media-new-0201.json').read_text())
assert len(actual)==126 and {(r['name'],r['sha256']) for r in actual}=={(r['name'],r['sha256']) for r in new}
assert len({r['sha256'] for r in actual})==126
known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()}
media=[]
for line in (W/'media-spec0201.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);media.append((int(i),d,targets(ts),n))
 assert d in {'distilled','no_technical_content','insufficient_technical_detail'} and n.strip()
assert len(media)==126 and {r[0] for r in media}==set(range(126))
for r in actual:
 assert r['detail']=='original' and r['viewed_at'] and r['sha256'] not in known
 assert digest((S/'media'/r['name']).read_bytes())==r['sha256']
db=dbopen()
for r in b:assert not db.execute('select 1 from reviews where body_sha256=?',(r['body_sha256'],)).fetchone()
db.close()
fs=next(ast.literal_eval(x.value) for x in ast.parse((W/'native0201.py').read_text()).body if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='facets' for y in x.targets))
assert fs==json.loads((W/'facets0201.json').read_text())
assert len(fs)==249 and len({t for _,t,_ in fs})==249
ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==258 and all(pid in ids for pid in urls)
for f,t,body in fs:
 assert (T/'references'/f).is_file() and ('## '+t) not in (T/'references'/f).read_text()
 assert '/Users/len/x-bugbounty' not in body
c=(T/'references/research/community-distillation.md').read_text()
assert c.count('\n## 首轮提炼范围与未采纳内容\n')==1
print(json.dumps(dict(groups=len(b),posts=164,body_dispositions=dict(collections.Counter(r[1] for r in rows)),media=126,media_dispositions=dict(collections.Counter(r[1] for r in media)),facets=249,topics=len({f for f,_,_ in fs}),batch_bound_URLs=len(urls)),ensure_ascii=False))

for i,dis,ts,note in media:
 if dis=='distilled':
  pid=actual[i]['name'].split('-')[0]
  for target in ts:assert any('references/'+f==target and 'https://x.com/i/status/'+pid in body for f,t,body in fs),(i,target,pid)
print('All distilled image targets bound to exact batch post source')

for i,dis,ts,note in media:
 if dis=='distilled':
  for target in ts: assert any('references/'+f==target and actual[i]['name'] in body for f,title,body in fs),(i,target)
print('Exact filename evidence binding verified')

current=json.loads((W/'media-before-0201.json').read_text())
prior=json.loads((W/'known0201.json').read_text())
assert len(current)==142 and len({r['sha256'] for r in current})==140 and len(prior)==14
observations={actual[i]['sha256']:(dis,ts) for i,dis,ts,note in media}
for r in prior:
 assert r['sha256'] in known and r['sha256'] not in observations
 old=r['prior'];assert old['sha256']==r['sha256']
 observations[r['sha256']]=(old['disposition'],old['targets'])
bound=0
for r in current:
 assert digest((S/'media'/r['name']).read_bytes())==r['sha256']
 dis,ts=observations[r['sha256']]
 if dis=='distilled':
  bound+=1;pid=r['name'].split('-')[0]
  for target in ts:
   assert any('references/'+f==target and r['name'] in body and 'https://x.com/i/status/'+pid in body for f,t,body in fs),(r['name'],target)
assert bound==100
print('All142 current paths rehashed; all100 distilled occurrences including known/duplicate images have exact filename/source/targets')
