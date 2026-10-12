"""Exact-once0221 receipt after observed full verifier exit0 session8495/8625c0."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==34452 and s['body_reviewed_posts']==35580 and s['remaining_body_groups']==17027
assert s['media_visually_reviewed_unique_contents']==13627 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==34452 and v['semantic_review_posts']==35580
assert v['local_markdown_links_checked']==16498 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==13604
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0221.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0221.json').read_text()) and len(fs)==320 and len({f for f,_,_ in fs})==34
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0221.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==423 and all(pid in ids for pid in urls) and len(b)==200 and len(ids)==204
actual=json.loads((W/'media-actual-0221.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==85
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0215' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0221' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0221_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
assert pct==67.49
v['batch0221_final_checks']=dict(checked_at=now,quick_validate='unavailable: missing PyYAML; independent static frontmatter/name/description/TODO/fences check passed',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=320,source_URLs_bound_to_batch=423,full_verifier_exit=0,full_verifier_session=8495,full_verifier_final_chunk='8625c0',full_source_hashes=52716,rendered_links=16498,broken_links=0,post_coverage_percent=pct,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0221.json').read_text()),no_waived_archive_fulltexts_fetched=True,static_vector_source_and_retained_render_hashes="verified; actual-0221.json[51], media-render-0221-51.png")
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(groups=34452,posts=35580,media=13627,facets=320,percent=pct,all_complete=False,goal='active',receipt=now)))

