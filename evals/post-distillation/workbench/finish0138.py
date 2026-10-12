
"""Exact-once receipt after full verifier observed final exit0 session61577/5a124c."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==20427 and s['body_reviewed_posts']==21308 and s['remaining_body_groups']==31052
assert s['media_visually_reviewed_unique_contents']==5899 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==20427 and v['semantic_review_posts']==21308
assert v['local_markdown_links_checked']==3560 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==5876
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0138.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0138.json').read_text()) and len(fs)==53 and len({f for f,_,_ in fs})==27
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0138.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==105 and all(pid in ids for pid in urls) and len(b)==250 and len(ids)==258
actual=json.loads((W/'media-actual-0138.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==106
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0132' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0138' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0138_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0138_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=53,source_URLs_bound_to_batch=105,full_verifier_exit=0,full_verifier_session=61577,full_verifier_final_chunk='5a124c',full_source_hashes=52716,rendered_links=3560,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0138.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix="CURRENT COMPLETED0138/media0132. ACTIVE goal 完成所有posts内容的提炼. NEVER rerun native/media/record/finish0138. Next0139/media0133. Verified20427groups21308posts40.42%; remaining31052groups31408posts; 5899media=3295D1593N1011I; full source52716 availablemedia5876 links3560 broken0 allfalse. User waiver missing images/external full texts count covered; native standalone no archive/currentdir runtime. Every shell rtk; no subagents/memorywrites/sourceexecution/livehandles. Preserve unrelated changes.\n0138 all250savedbody actualcf2ec0/5721cc/348c15/e161d0, all106neworiginalpixels actual realtimehashbound viewed BEFOREledger; actual0138/notes0138actual.md106. Facets53/27topics/105URLs; 104mapped53corrected51merged146excluded. Media59D40N7I. Persist7a4076/build800be8/precheck6a9f10; nativebf417f/media84d034/bodye3ba80 SUCCESSONCE. Quick2c1451 valid/gita60df9pass/runtime134f4bexit1empty expected. Fulla9de4fsession61577 then FINAL5a124c OBSERVEDexit0. ActualFirebaseprimary417view0 lines83-108 recordednormative0138; Bash417view1failednotreadnotcited. No waivedarchive fulltexts fetched. Ownbuild/precheck/finish0138 templates andlive draft/data/actual/notes/helper available.\nNEXT prepare0139--count250--max-chars65000/inventoryeachsuccessonce; fullbody/meaningfulalts then eachneworiginalimage actual<=6/call hashboundbeforeledger;manualfacets/media/spec; sourcebindingprecheckBEFOREnative;native/media/bodyeachsuccessonce;quick/git/runtime/fullsamehandleobservedexit0;exactfinish/Handoff. Goal remains active until remaining0 and allrequiredmedia/nativeverified.\n\n"
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=20427,posts=21308,media=5899,facets=53,percent=pct,all_complete=False,goal='active',receipt=now)))
