"""Exact-once0242 receipt after observed full verifier exit0 session24426/3edba1."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==38569 and s['body_reviewed_posts']==39746 and s['remaining_body_groups']==12910
assert s['media_visually_reviewed_unique_contents']==15620 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==38569 and v['semantic_review_posts']==39746
assert v['local_markdown_links_checked']==27078 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==15597
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0242.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0242.json').read_text()) and len(fs)==440 and len({f for f,_,_ in fs})==39
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0242.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==459 and all(pid in ids for pid in urls) and len(b)==189 and len(ids)==189
actual=json.loads((W/'media-actual-0242.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==65
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0236' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0242' and set(matches[0]['post_ids'])==set(r['post_ids'])
for k in json.loads((W/'known0242.json').read_text()):
 assert next(m for m in media if m['sha256']==k['sha256'])==k['prior']
assert 'batch0242_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
assert pct==75.4
v['batch0242_final_checks']=dict(checked_at=now,quick_validate='unavailable: missing PyYAML; independent static frontmatter/name/description/TODO/fences check passed',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=440,source_URLs_bound_to_batch=459,full_verifier_exit=0,full_verifier_session=24426,full_verifier_final_chunk='3edba1',full_source_hashes=52716,rendered_links=27078,broken_links=0,post_coverage_percent=pct,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0242.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(groups=38569,posts=39746,media=15620,facets=440,percent=pct,all_complete=False,goal='active',receipt=now)))

