"""Validate every0122 planned review before appending. Own bookkeeping only."""
import ast,json,collections,re
from stage import targets,dbopen
from recover import T,S,A,W,digest
b=json.loads((W/'batch-0122.json').read_text());assert len(b)==250 and sum(len(r['post_ids']) for r in b)==252
rows=[]
for line in (W/'spec0122.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);rows.append((int(i),d,targets(ts),n));assert d in {'new_knowledge','merged','corrected','excluded'} and n.strip()
assert len(rows)==250 and {r[0] for r in rows}==set(range(1,251))
actual=json.loads((W/'media-actual-0122.json').read_text());new=json.loads((W/'media-new-0122.json').read_text());assert len(actual)==92 and {(r['name'],r['sha256']) for r in actual}=={(r['name'],r['sha256']) for r in new}
known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()}
media=[]
for line in (W/'media-spec0122.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);media.append((int(i),d,targets(ts),n));assert d in {'distilled','no_technical_content','insufficient_technical_detail'} and n.strip()
assert len(media)==92 and {r[0] for r in media}==set(range(92))
for r in actual:assert r['detail']=='original' and r['sha256'] not in known and digest((S/'media'/r['name']).read_bytes())==r['sha256']
db=dbopen()
for r in b:assert not db.execute('select 1 from reviews where body_sha256=?',(r['body_sha256'],)).fetchone()
db.close()
n=ast.parse((W/'native0122.py').read_text());fs=next(ast.literal_eval(x.value) for x in n.body if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='facets' for y in x.targets))
assert fs==json.loads((W/"facets0122.json").read_text())
assert len(fs)==84 and len({t for _,t,_ in fs})==84
ids={pid for r in b for pid in r['post_ids']};urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==127 and all(pid in ids for pid in urls)
for f,t,body in fs:assert (T/'references'/f).is_file() and ('## '+t) not in (T/'references'/f).read_text()
c=(T/'references/research/community-distillation.md').read_text();assert c.count('\n## 首轮提炼范围与未采纳内容\n')==1
print(json.dumps(dict(groups=len(b),posts=252,body_dispositions=dict(collections.Counter(r[1] for r in rows)),media=92,media_dispositions=dict(collections.Counter(r[1] for r in media)),facets=84,topics=len({f for f,_,_ in fs}),batch_bound_URLs=len(urls)),ensure_ascii=False))

