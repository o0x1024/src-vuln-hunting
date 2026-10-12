
"""Exact-once receipt after full verifier observed final exit0 session80034/56da49."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==22230 and s['body_reviewed_posts']==23202 and s['remaining_body_groups']==29249
assert s['media_visually_reviewed_unique_contents']==6858 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==22230 and v['semantic_review_posts']==23202
assert v['local_markdown_links_checked']==4057 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==6835
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0147.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0147.json').read_text()) and len(fs)==54 and len({f for f,_,_ in fs})==29
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0147.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==104 and all(pid in ids for pid in urls) and len(b)==193 and len(ids)==207
actual=json.loads((W/'media-actual-0147.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==87
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0141' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0147' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0147_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0147_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=54,source_URLs_bound_to_batch=104,full_verifier_exit=0,full_verifier_session=80034,full_verifier_final_chunk='56da49',full_source_hashes=52716,rendered_links=4057,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0147.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0147/media0141. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0147. Next0148/media0142.\nVerified22,230groups23,202posts44.01%; remaining29,249groups29,514posts; total51,479groups52,716posts. Media6,858=3,863D1,824N1,171I; source52716 availableext6835 inline3/9 priorunavailable20 local4057 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery/blocker. Native independent of source/currentdir runtime. All shell rtk; no subagents/memorywrites/sourceexecution. Preserve unrelated targetchanges.\n0147 prepare614d7f/inventory2d52be SUCCESS ONCE193groups207posts47873chars first1585903936447332353last1588244505014063104.94paths89unique2known87new223missingwaived. ALL193fullbodies actuald602c2(1–60)/c14b73(61–120)/f6c454(121–180)/7e3e9b(181–193); meaningfulaltsread. ALL87originalimages actual0–86 <=6/call decoded returned binarySHA/time persisted beforeledger actual-0147.json.87manualnotes explicitstored after every batch. No OCR inferred reviews.\n54facets29topics104URLs100mapped52corrected48merged93excluded;59D18N10I. Persist587315;build e79800/precheck f6610d PASS exactimageposttarget source bindings. Nativea631be/media5addc4/body9f048b SUCCESS ONCE. Quickc8b922valid/gitcbca2apass/runtimef9113fexit1emptyexpected. Full031270session80034 then FINAL56da49 observedexit0; source52716 available6835 links4057 broken0 allfalse. Normative0147 empty; no externalfulltexts fetched.\nMechanisms: IDN/HSTS normalization;netrc scanningbounds;CVE/search labelsreconprovenance;XSSpipeline loss;XFFblindbackend;scopehostregex/root/exclusions;reset/historytokenlifecycle;CSPevaluationvsactualexecution;OASToriginalrequest/layers;LFItextmatches;CompanyInfo/allstaffadmin;secretIDvskey/C#wrongMIMEsourcedisclosure;sharefolderpropagation;GraphQLrating;redirectuserinfo/Unicode/CRLFvsnull;CSRFPOSТGET/tokenbinding/browser;AWSmetadatafieldsnotroot;2FAserverprincipal;SQLemail/timing;SSTIengine;rolecookie/proxy/path403;RMIlookupreadObject;captchaCSRFtokensdistinction;Androidstatic/dynamic/logs/hooks;onevariablefuzz;JSubFinderproxyTLSfail;xnLinkFinderdepth/status;company/VTpagination;PHPescapevaluenotactualSQLsink;LinktreejavascriptURI→sameorigintoken;CSRF→XSSneedcrosssiteproof;XSScontext/nulltipnoproof;deleteGETsafety;commandsreadonlyvswrites;grepsecrets;iptablesdirection/state;Azurelistingvsread;inventorydiff;sessionlifecyclemindmap;proccwd/namespace;PressableAPIiderrorsecrets;Host/method/obsfoldparser;JWTnonequestionnotlibraryfact;CIA/statsevidence;RSSXMLnamespaceXSS;NodeInspectorlocalprereqs;XXEexpectwrapper;Jenkinspermissionsvscloudprofiles;Crowdsignalprivatedeletedalteditor;pathdictionaryactionbudget;ActionsRunnerenv→dockerCLI;understandappmodel;RFIconsumer;prototypepollutionownvsinherited/gadget.\nNEXT0148/media0142 boundedprepare count200maxchars48000 or120/30000 (actualcounts authoritative), inventory eachonce. Fullsavedbody/meaningfulalts actualread, then allnewuniqueoriginalpixels <=6/call hash/timebeforeledger. Manually sourceboundfacets/media precheck BEFOREappend. native/media/bodyrecord eachonce;quick/git/runtime;fullsameprocess untilobservedexit0;exactfinish/Handoffprependhistory. Goalactive until allrequiredcoverage complete. Stores data0147/actual0147/notes0147/draft0147/reviewImageBatch0147/bodyReader0147/draftHelper0147/imageHelpers live; load clones always store edits. Templatesbuild/precheck/native/finish0147. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135. No livehandlespending.\n\n\n'
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=22230,posts=23202,media=6858,facets=54,percent=pct,all_complete=False,goal='active',receipt=now)))
