"""Exact-once receipt after repaired inline code; full observed final exit0 session72658/7fdf16."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==26260 and s['body_reviewed_posts']==27283 and s['remaining_body_groups']==25219
assert s['media_visually_reviewed_unique_contents']==9044 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==26260 and v['semantic_review_posts']==27283
assert v['local_markdown_links_checked']==5749 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==9021
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0173.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0173.json').read_text()) and len(fs)==9 and len({f for f,_,_ in fs})==8
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0173.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==9 and all(pid in ids for pid in urls) and len(b)==17 and len(ids)==17
actual=json.loads((W/'media-actual-0173.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==7
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0167' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0173' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0173_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
assert pct==51.75
v['batch0173_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=9,source_URLs_bound_to_batch=9,full_verifier_exit=0,full_verifier_session=72658,full_verifier_final_chunk='7fdf16',full_source_hashes=52716,rendered_links=5749,broken_links=0,post_coverage_percent=pct,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0173.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')



v["batch0173_final_checks"]["markdown_formatting_repair"]=dict(failed_session=66116,failed_final_chunk="e6994a",failure="prior0172 handoff code prose looked like Markdown link",repair_chunk="60195b",no_review_ledger_append=True)
(A/"verification.json").write_text(json.dumps(v,ensure_ascii=False,indent=2)+"\n")
prefix = 'CURRENT COMPLETED0173/media0167. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun native/media/body/finish0173.0174/media0168 alreadyPREPARED ONCE, DO NOTprepare/inventory again.\n26260groups27283posts; remaining25219groups25433posts; media9044=5214D2368N1462I, availablehashes9021 inline3/9 priorunavailable20 links5749 broken0. Snapshotc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\n0173 prepare4d0a12 only17groups17posts3991chars because nextbody58236; inventory192d38 sevennew/21missingwaived; all17body59188f, all7originalSHA/timeactual-0173.json andmanualnotes0173.json.9facets8topics9URLs7mappedcorrected10excluded,4D1N2I. Nativebc9137 mediaa5e1c9 body7d20d0 ONCE. Buildc4b596 precheckb2193e. Quickb26d3b/git17d32c/runtime9f4068exit1empty. Full6a668bsession66116FINALe6994aexit1 handoffprior0172 code prose falselylink; repair60195b parentdispatch plain HANDOFF+finish0172 only; rerunfdd1c2session72658FINAL7fdf16 OBSERVEDexit0. Finish0173 receipt verification.json.batch0173_final_checks.\n0173 mechanisms: Host127WordPressmysqlierrornoSSRFbaseline; pathsnotcredentials; XSSMedium4.7vs6.1noallCritical; Gmailnamevsaddressauthentication; notreproducing!=reportcausedfix; onebugconsumerlearning; TelegramGETcurlcallbacknotSSRF/XXE/XSSattributionNOsend; CSPdefaultsrcself scriptsrc fullpolicy/actualbytes; naabutop1000exclude80/443notallports/dashauth. Rank/award/title/course/cover insufficientorN.\nCURRENT0174 PREPARED35206b count160max110000,160groups160posts94848chars first1648874691778555905 last1651635569179467781. Inventory370d31 95paths/95unique1known94new177missingwaived. data0174/actual0174/notes0174/draft0174/helperstores live; no native/media/body append.\nFirst0174body contains58236 mostlyinlinePNGbase64; 194397 decoded/rehashed43433bytes SHAe1545f6c8d48acd5f06b36c5a6c823321fed988a5d20d4b1fa7be8fe677132b9 existingmedia-inline0032 N100x100glassesphoto. body-display-readable-0174.txt preservesALLnaturaltext, replacesonlybinaryURIwithverifiedknownmetadata; originalbody still hashbound intact. inline-reconciliation0174.json actual1known. Knownattached5c05e22594 NATOcover current1649119647390629908-02 prior1592829029807423488. No reledgerofknown.\nALLbody0174 read1–60 435eb3;61–110f4da42; next111–160mustread; then ALL94neworiginalimages <=6percall storemanualnotesbefore nextgroup, actualreturnedbytesSHA/time. No waivedfulltexts/imagesfetch, no sourceexecution/credentials/install/contact/payments/live scans, RTK/no subagents/no memorywrites preserveunrelatedchanges. Memory424–425 actuald62e0c provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\nBuild/precheck plannedallfacets+bodymapped+mediaindividual exactfilename/post; native/media/bodyONCE; quick/git/runtime/fullsameprocessobservedFINALexit0; finishONCE/HANDOFFprepend. Guard all markdown code bracketcall with inline code even HANDOFF because full verifier includes allmd. Templates0173 tinycount17; use0172 160templatefor0174 but actualURLsfacetscountdifferent and base100percent MUSTpreserve.\n\n'
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=26260,posts=27283,media=9044,facets=9,percent=pct,all_complete=False,goal='active',receipt=now)))
