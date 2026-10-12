
"""Exact-once receipt after full verifier observed final exit0 session54589/c163ec."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==21797 and s['body_reviewed_posts']==22750 and s['remaining_body_groups']==29682
assert s['media_visually_reviewed_unique_contents']==6625 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==21797 and v['semantic_review_posts']==22750
assert v['local_markdown_links_checked']==3908 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==6602
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0144.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0144.json').read_text()) and len(fs)==45 and len({f for f,_,_ in fs})==19
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0144.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==66 and all(pid in ids for pid in urls) and len(b)==120 and len(ids)==122
actual=json.loads((W/'media-actual-0144.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==64
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0138' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0144' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0144_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0144_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=45,source_URLs_bound_to_batch=66,full_verifier_exit=0,full_verifier_session=54589,full_verifier_final_chunk='c163ec',full_source_hashes=52716,rendered_links=3908,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0144.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0144/media0138. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0144. Next0145/media0139.\nVerified21,797groups22,750posts43.16%; remaining29,682groups29,966posts; total51,479groups52,716posts. Media6,625=3,699D1,771N1,155I; source52716 availableext6602 inline3/9 priorunavailable20 local3908 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery required. Native independent of archive/currentdir runtime. Shell rtk. No subagents, memorywrites, sourceexecution. Preserve unrelated changes.\n0144 prepare41a052/inventory9ff2f4 SUCCESS ONCE120groups122posts29017chars64newimages129missingwaived. Fullbody da7c7d1–60/a34a3d61–120 actual read. All64images original pixels viewed; binarySHA+realtime persisted beforeledger actual-0144.json;64manualnotes.45facets19topics66URLs66mapped45corrected21merged54excluded;41D11N12I. Buildb9e8f5/precheckc22f8dPASS. Nativeab6978/media0e6d69/bodyfd41a1 SUCCESS ONCE. Quick9fce53valid/git110642pass/runtime9b2307exit1empty. Full e09199session54589 FINALc163ec observedexit0. Normative Fetch turn432view1 and MicrosoftExchange turn431view0 actually read; no waivedarchivefulltext fetched. Finish current script asserts exact artifacts/counts; receipt c163ec.\nNEXT0145/media0139 prepare count250 maxchars65000 and inventory each once; saved fullbodies/meaningfulalts actual read then current images actual view hash/time beforeledger. Bind exactpost URLs and native references. Precheck beforeappend;native/media/bodyrecord each once; quick/git/runtime;fullsameprocess untilobservedexit0;finish exactreceipt. Goalactive until allrequiredcoverage verified.\n\n'
h=W/'HANDOFF.md'; h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=21797,posts=22750,media=6625,facets=45,percent=pct,all_complete=False,goal='active',receipt=now)))
