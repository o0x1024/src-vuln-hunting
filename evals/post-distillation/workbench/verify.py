"""Verify local source/evidence integrity without executing source material."""
import base64,collections,gzip,json,re,sqlite3
from datetime import datetime,timezone
from urllib.parse import unquote
from recover import T,S,A,W,digest,complete_text
def main():
 snapshot=[json.loads(l) for l in gzip.open(A/'snapshot-posts.jsonl.gz','rt')];status=json.loads((A/'status.json').read_text());old=json.loads((A/'verification.json').read_text())
 canonical=digest(('\n'.join(json.dumps(r,sort_keys=True,separators=(',',':')) for r in snapshot)+'\n').encode());assert canonical==status['post_snapshot_sha256']
 assert {p.stem for p in (S/'posts').glob('*.md')}=={r['id'] for r in snapshot}
 bodies=collections.defaultdict(set);inline=[]
 db=sqlite3.connect(W/'work.sqlite3');db.row_factory=sqlite3.Row
 for r in snapshot:
  raw=(S/'posts'/(r['id']+'.md')).read_bytes();assert digest(raw)==r['document_sha256'],r['id'];text=raw.decode();body=complete_text(re.split(r'^---\s*$',text,maxsplit=1,flags=re.M)[1]);assert digest(body.encode())==r['body_sha256'];bodies[r['body_sha256']].add(r['id'])
  actual=dict(db.execute('select * from posts where id=?',(r['id'],)).fetchone());assert actual==dict(id=r['id'],document_sha256=r['document_sha256'],body_sha256=r['body_sha256'])
  assert db.execute('select body from bodies where body_sha256=?',(r['body_sha256'],)).fetchone()[0]==body
  matches=list(re.finditer(r'data:(image/[^;,\s]+);base64,([A-Za-z0-9+/=]+)',text))
  for n,m in enumerate(matches,1):
   binary=base64.b64decode(re.sub(r'\s+','',m.group(2)),validate=True);inline.append(dict(post_id=r['id'],ordinal=n,mime_type=m.group(1),sha256=digest(binary),bytes=len(binary),document_sha256=r['document_sha256']))
 expected_inline=[json.loads(l) for l in gzip.open(A/'snapshot-inline-media.jsonl.gz','rt')];assert sorted(inline,key=lambda r:(r['post_id'],r['ordinal']))==sorted(expected_inline,key=lambda r:(r['post_id'],r['ordinal']))
 reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()];assert len({r['body_sha256'] for r in reviews})==len(reviews)
 for r in reviews:
  assert set(r['post_ids'])==bodies[r['body_sha256']];v=dict(db.execute('select * from reviews where body_sha256=?',(r['body_sha256'],)).fetchone());assert v['disposition']==r['disposition'] and v['note']==r['note'] and v['batch']==r['batch'] and json.loads(v['targets'])==r['targets'];assert all((T/f).is_file() for f in r['targets'])
 assert db.execute('select count(*) from reviews').fetchone()[0]==len(reviews);assert db.execute('select count(*) from posts').fetchone()[0]==len(snapshot);assert db.execute('select count(*) from bodies').fetchone()[0]==len(bodies)
 media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()];assert len({r['sha256'] for r in media})==len(media);available=0;missing=[];inline_hashes={r['sha256'] for r in inline}
 for r in media:
  assert all((T/f).is_file() for f in r['targets'])
  if r['sha256'] in inline_hashes:continue
  p=S/'media'/r['image_name']
  if p.is_file():assert digest(p.read_bytes())==r['sha256'];available+=1
  else:missing.append(r['sha256'])
 assert set(missing)==set(old['previously_reviewed_media_now_unavailable']),('Reviewed image availability changed',len(missing))
 assert inline_hashes<= {r['sha256'] for r in media}
 links=0;broken=[]
 for p in T.rglob('*.md'):
  if '.git' in p.parts:continue
  prose=re.sub(r'(?ms)^```[^\n]*\n.*?^```[^\n]*$', '',p.read_text())
  prose=re.sub(r'(`+)(?:(?!\1).)*?\1', '',prose,flags=re.S)
  for m in re.finditer(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',prose):
   dest=m.group(1).strip()
   if dest.startswith('<') and '>' in dest:dest=dest[1:dest.index('>')]
   else:dest=re.split(r'\s+[\"\']',dest,maxsplit=1)[0]
   if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',dest) or dest.startswith('#'):continue
   dest=unquote(dest.split('#')[0])
   if not dest:continue
   links+=1
   if not (p.parent/dest).exists():broken.append((str(p.relative_to(T)),dest))
 assert not broken,broken[:10]
 represented=sum(len(r['post_ids']) for r in reviews)
 assert status['body_reviewed_groups']==len(reviews) and status['body_reviewed_posts']==represented and status['remaining_body_groups']==len(bodies)-len(reviews) and status['media_visually_reviewed_unique_contents']==len(media)
 now=datetime.now(timezone.utc).isoformat();result=dict(old)
 result.update(verified_at=now,post_snapshot_sha256=canonical,raw_source_documents_hash_verified=len(snapshot),semantic_review_groups=len(reviews),semantic_review_posts=represented,unique_complete_texts=len(bodies),remaining_text_groups=len(bodies)-len(reviews),semantic_media_contents_reviewed=len(media),all_posts_complete=False,local_markdown_links_checked=links,broken_local_markdown_links=0,raw_source_documents_hash_verified_at=now,local_markdown_links_verified_at=now,reviewed_media_hashes_reverified=available,previously_reviewed_media_now_unavailable=missing,reviewed_inline_media_hashes_reverified=len(inline_hashes),inline_media_occurrences_verified=len(inline),scope='Fresh all raw source IDs/hash/canonical snapshot/complete-body parser hash checks; exact full text ledger and rebuilt SQLite agreement; currently available reviewed media and all inline binary hashes; previous missing reviews retained; local topic targets/Markdown links. Skill validation and whitespace check are separately timestamped. Historical eight research tool tests were not rerun for these prose changes. All content distillation remains incomplete.')
 (A/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');db.close();print(json.dumps(dict(source_hashes=len(snapshot),reviewed_groups=len(reviews),reviewed_posts=represented,media=len(media),available_media_rehashed=available,inline_unique=len(inline_hashes),inline_occurrences=len(inline),prior_missing=len(missing),links=links,broken=len(broken),all_complete=False)))
if __name__=='__main__':main()
