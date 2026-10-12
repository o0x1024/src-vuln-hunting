"""Rebuild local review bookkeeping from saved evidence; never run post text."""
import collections, gzip, hashlib, json, re, sqlite3
from pathlib import Path
from datetime import datetime, timezone
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
S=Path('/Users/len/x-bugbounty'); A=T/'evals/post-distillation'; W=A/'workbench'
IMAGE_PATTERN=r'!\[([\s\S]*?)\]\(((?:\.\./media/|https?://pbs\.twimg\.com/)[^)\n]*)\)'
def digest(b): return hashlib.sha256(b).hexdigest()
def complete_text(tail):
 parts=re.split(r'^## 图片\s*$',tail,maxsplit=1,flags=re.M); body=parts[0].strip()
 if len(parts)==2:
  alts=[m.group(1).strip() for m in re.finditer(IMAGE_PATTERN,parts[1])]
  meaningful=[a for a in alts if a and not re.fullmatch(r'(?:图片\d*|Image\d*|Photo\d*|图像\d*)',a,re.I)]
  if meaningful: body+='\n\n[图片替代文字]\n'+'\n\n'.join(meaningful)
  remaining=re.sub(IMAGE_PATTERN,'',parts[1]).strip()
  if remaining: body+='\n\n[图片区其余文字]\n'+remaining
 return body
def main():
 snapshot=[json.loads(l) for l in gzip.open(A/'snapshot-posts.jsonl.gz','rt')]
 reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
 assert len(snapshot)==52716 and len({r['id'] for r in snapshot})==len(snapshot)
 assert len({r['body_sha256'] for r in reviews})==len(reviews)
 paths=list((S/'posts').glob('*.md')); assert {p.stem for p in paths}=={r['id'] for r in snapshot}
 dbpath=W/'work.sqlite3'; assert not dbpath.exists(), 'Already recovered; reuse existing database'
 db=sqlite3.connect(dbpath); db.executescript('create table posts(id text primary key,document_sha256 text,body_sha256 text); create table bodies(body_sha256 text primary key,body text,first_id text); create table reviews(body_sha256 text primary key,disposition text,note text,targets text,batch text);')
 by_hash=collections.defaultdict(set)
 for r in sorted(snapshot,key=lambda r:(not r['id'].isdigit(),int(r['id']) if r['id'].isdigit() else r['id'])):
  raw=(S/'posts'/(r['id']+'.md')).read_bytes(); assert digest(raw)==r['document_sha256'],r['id']
  parts=re.split(r'^---\s*$',raw.decode(),maxsplit=1,flags=re.M); assert len(parts)==2,r['id']
  body=complete_text(parts[1]); assert digest(body.encode())==r['body_sha256'],('Body differs',r['id'])
  db.execute('insert into posts values(?,?,?)',(r['id'],r['document_sha256'],r['body_sha256']))
  db.execute('insert or ignore into bodies values(?,?,?)',(r['body_sha256'],body,r['id'])); by_hash[r['body_sha256']].add(r['id'])
 for r in reviews:
  assert set(r['post_ids'])==by_hash[r['body_sha256']],r['body_sha256']
  assert all((T/f).is_file() for f in r['targets'])
  db.execute('insert into reviews values(?,?,?,?,?)',(r['body_sha256'],r['disposition'],r['note'],json.dumps(r['targets']),r['batch']))
 db.commit(); db.close()
 # Recover only our saved observation JSON from this task's tool history.
 session=Path('/Users/len/.codex/sessions/2026/10/09/rollout-2026-10-09T10-15-59-01a11e72-23a9-7091-85bd-fb3171d2e135.jsonl')
 observed=None
 for line in session.open():
  q=json.loads(line).get('payload',{}); changes=q.get('item',{}).get('changes',{}); v=changes.get('/tmp/src-post-distillation/media-actual-0097.json')
  if v and v.get('type')=='add': observed=json.loads(v['content'])
 assert observed is not None and len(observed)==42
 for r in observed: assert r['detail']=='original' and digest((S/'media'/r['name']).read_bytes())==r['sha256']
 (W/'media-actual-0097.json').write_text(json.dumps(observed,ensure_ascii=False,indent=2)+'\n')
 report=dict(recovered_at=datetime.now(timezone.utc).isoformat(),source_hashes=len(snapshot),complete_body_hashes=len(by_hash),reviewed_groups=len(reviews),reviewed_posts=sum(len(r['post_ids']) for r in reviews),restored_original_image_observations=len(observed),scope='Only bookkeeping rebuilt; no existing review, topic or source document rewritten; original viewed image hashes revalidated.')
 (W/'recovery.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(report))
if __name__=='__main__': main()
