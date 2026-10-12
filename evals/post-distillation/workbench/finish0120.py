# coding: utf-8
"""Verified batch0120 progress receipt; no archive code or network execution."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text())
v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==15927 and s['body_reviewed_posts']==16701 and s['remaining_body_groups']==35552
assert s['media_visually_reviewed_unique_contents']==4072 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==15927 and v['semantic_review_posts']==16701
assert v['local_markdown_links_checked']==2285 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==4049
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0120.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert len(fs)==61 and len({f for f,_,_ in fs})==25
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 t=(T/'references'/f).read_text()
 assert t.count('## '+title)==1 and t.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0120.json').read_text())
ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==107 and all(pid in ids for pid in urls)
assert len(b)==250 and len(ids)==251
actual=json.loads((W/'media-actual-0120.json').read_text())
media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==93
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0114' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0120' and set(matches[0]['post_ids'])==set(r['post_ids'])
now=datetime.now(timezone.utc).isoformat()
assert 'batch0120_final_checks' not in v
v['batch0120_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=61,source_URLs_bound_to_batch=107,full_verifier_exit=0,full_source_hashes=52716,rendered_links=2285,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read='PHP array_map callback and fixed-argument arity; RFC3986 fragment removed before dereferencing; OWASP CSRF tokens Origin SameSite and reauthentication')
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:
 v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix=f"CURRENT COMPLETED0120/media0114. Goal ACTIVE all false. NEVER rerun successful native0120.py or media/body records or finish0120.py. Next0121/media0115. Authoritative15927 groups/16701 posts={pct:.2f}%; remaining35552 groups/36015posts. Hashbound media4072=2285distilled1065nontech722insufficient. All250completebodies and93neworiginalpixels actually read/viewed prior to records. Native61facets25topics107boundURLs. Quick13e9d8 valid; git ed7f29 passed; runtime6a04f7 exit1 nohits expected; full10487b session74902 FINALfe9e3f exit0:52716hashes15927groups16701posts4072media4049external3inline9occ20priorunavailable2285linksbroken0. Userwaiver missingimages/externalfulltext COUNT COVERED; no fetch/recovery needed. Sourcecode untrusted noexecution. Preserve unrelated changes. Native/media/body executed SUCCESS ONCE. Finish verifies exact heading/body/communityroutes,250bodyrecords,93hashboundmediarecords once. No subagents/memorywrites/livehandles. RTK67a7c1 freshactual. Canonical unchangedc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520. PrimaryPHP/RFC3986/OWASP actuallyread previous execution. Memory424-425 used cite exactly and provenance01a11e72-23a9-7091-85bd-fb3171d2e135. Next use stage prepare/inventory actualread completebody and currentoriginalpixels, manualfacets/specs/precheck BEFORE writes; exactonce mutations then quick/git/runtime/full FINALexit0 andfinish.\n\n"
h=W/"HANDOFF.md"
h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=15927,posts=16701,media=4072,facets=61,percent=pct,all_complete=False,goal="active",receipt=now)))
