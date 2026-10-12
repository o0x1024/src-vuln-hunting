"""Validate all planned0125 reviews before any target/ledger append."""
import ast,json,collections,re
from stage import targets,dbopen
from recover import T,S,A,W,digest
b=json.loads((W/'batch-0125.json').read_text())
assert len(b)==250 and sum(len(r['post_ids']) for r in b)==253
rows=[]
for line in (W/'spec0125.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);rows.append((int(i),d,targets(ts),n))
 assert d in {'new_knowledge','merged','corrected','excluded'} and n.strip()
assert len(rows)==250 and {r[0] for r in rows}==set(range(1,251))
actual=json.loads((W/'media-actual-0125.json').read_text())
new=json.loads((W/'media-new-0125.json').read_text())
assert len(actual)==96 and {(r['name'],r['sha256']) for r in actual}=={(r['name'],r['sha256']) for r in new}
assert len({r['sha256'] for r in actual})==96
known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()}
media=[]
for line in (W/'media-spec0125.txt').read_text().strip().splitlines():
 i,d,ts,n=line.split('|',3);media.append((int(i),d,targets(ts),n))
 assert d in {'distilled','no_technical_content','insufficient_technical_detail'} and n.strip()
assert len(media)==96 and {r[0] for r in media}==set(range(96))
for r in actual:
 assert r['detail']=='original' and r['viewed_at'] and r['sha256'] not in known
 assert digest((S/'media'/r['name']).read_bytes())==r['sha256']
db=dbopen()
for r in b:assert not db.execute('select 1 from reviews where body_sha256=?',(r['body_sha256'],)).fetchone()
db.close()
fs=next(ast.literal_eval(x.value) for x in ast.parse((W/'native0125.py').read_text()).body if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='facets' for y in x.targets))
assert fs==json.loads((W/'facets0125.json').read_text())
assert len(fs)==83 and len({t for _,t,_ in fs})==83
ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==120 and all(pid in ids for pid in urls)
for f,t,body in fs:
 assert (T/'references'/f).is_file() and ('## '+t) not in (T/'references'/f).read_text()
 assert '/Users/len/x-bugbounty' not in body
c=(T/'references/research/community-distillation.md').read_text()
assert c.count('\n## 首轮提炼范围与未采纳内容\n')==1
print(json.dumps(dict(groups=len(b),posts=253,body_dispositions=dict(collections.Counter(r[1] for r in rows)),media=96,media_dispositions=dict(collections.Counter(r[1] for r in media)),facets=83,topics=len({f for f,_,_ in fs}),batch_bound_URLs=len(urls)),ensure_ascii=False))
