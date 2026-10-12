
"""Exact-once receipt after full verifier observed final exit0 session52505/3435fc."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==22430 and s['body_reviewed_posts']==23403 and s['remaining_body_groups']==29049
assert s['media_visually_reviewed_unique_contents']==6964 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==22430 and v['semantic_review_posts']==23403
assert v['local_markdown_links_checked']==4106 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==6941
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0148.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0148.json').read_text()) and len(fs)==49 and len({f for f,_,_ in fs})==26
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0148.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==114 and all(pid in ids for pid in urls) and len(b)==200 and len(ids)==201
actual=json.loads((W/'media-actual-0148.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==106
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0142' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0148' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0148_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0148_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=49,source_URLs_bound_to_batch=114,full_verifier_exit=0,full_verifier_session=52505,full_verifier_final_chunk='3435fc',full_source_hashes=52716,rendered_links=4106,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0148.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0148/media0142. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0148. Next0149/media0143.\nVerified22,430groups23,403posts44.39%; remaining29,049groups29,313posts; total51,479groups52,716posts. Media6,964=3,939D1,852N1,173I; source52716 availableext6941 inline3/9 priorunavailable20 links4106 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery/blocker. Native independent of source/currentdir runtime. All shell rtk; no subagents/memorywrites/sourceexecution. Preserve unrelated targetchanges.\n0148 prepare0cb762/inventoryd3d91d SUCCESSONCE200groups201posts42219chars first1588244507698421760last1590899154381078528.115paths113unique7known106new214missingwaived. ALL200fullbodies actuallyread75a817(1–60)/01e742(61–120)/f06c26(121–180)/8ad248(181–200); meaningfulaltsread. ALL106originalimages actual0–105 <=6/call returned binarySHA/time persisted beforeledger actual-0148.json.106manualnotes explicitstored aftereverybatch. No OCR inferred reviews.\n49facets26topics114URLs112mapped48corrected64merged88excluded;76D28N2I. Draftpersistf9bf4f;scriptbuild3c0b21;build471575/precheckc0d2b0 PASS exactimageposttargetsourcebindings. Nativecdcb95/mediad620a5/body617500 SUCCESSONCE. Quick90081dvalid/gitb63aa9pass/runtime45f82dexit1emptyexpected. Full6188f3session52505 then FINAL3435fc OBSERVEDexit0; source52716 available6941 links4106 broken0 allfalse. Normative0148 empty; no externalfulltexts fetched.\nMechanisms: passiveIP/copyright/ASN/deepnameprovenance;foundation/matrix;Cookiefilereadrealresponse;Markdownpreview/movecomplexity;pprofvsarbitraryread;GitLabimportlocalfileprotocol;localDFIR/PREFETCH/RDPpermission;2FAserverstate;recondirectoryscope;TRACEreflectionnotauth;blindXSScallbackconsumer;pipelinesinputtype/filterloss/actionbudget;SQLquerysink/timing;wildcardJSP/Nginxcandidates;CSSpathconsumer;GraphQLregex/batchingbudget;XSSHTML/JS/event/PyScriptcontext;CSRFsessionvsintent;curlCookiecontrolbytes;SSRFneedsseparateshellconsumer;Loggercaptureboundary;git/secrets/fixture;takeoverDNSvsalivefilter;authheaders/session/leadsserverprincipal;GoSSTIengine;fileequalsparser;UnicodeCRLFbytes;codeflags/pathssinks;WARPdevicepolicyallentrances;architecturequestions;Katanaheadlesscoverage;Flinkplanclassload;KafkaJAASJNDI;GrafanaSMTPconfignewline;SQLite/HttpSink/Jolokiachain;malformedJSONnotATO;TinyXSS/SVG/errorcallbackconditions;inventorydiff/Amassformat;localrouterWiFiXSSprereqs;Hostconsumer/victimdevideneed;SelfXSScrosssubject;FFUFkeyword/mode/budget;SSRFIPv6userinfo/finalsocket;fuzzerbenchmark;passwdreporttemplatefalsepositive;uploadMIMEvsinterpreter;GTMpublicIDvssecret;Dalfoxlabelsnotbrowser;WPScanaggressive/passwordactions.\nNEXT0149/media0143 boundedprepare200max48000 (actualcounts authoritative), inventoryeachonce. Fullsavedbody/meaningfulaltsactuallyread thenallnewuniqueoriginalpixels<=6/callhash/timebeforeledger. Manuallysourceboundfacets/media precheck BEFOREappend. native/media/bodyrecordeachonce;quick/git/runtime;fullsameprocessuntilobservedexit0;exactfinish/Handoffprependhistory. Goalactiveuntilallrequiredcoveragecomplete. Storesdata0148/actual0148/notes0148/draft0148/reviewImageBatch0148/bodyReader0148/draftHelper0148/imageHelpers live; loadclonesalwaysstoreedits. Templatesbuild/precheck/native/finish0148. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135. No livehandlespending.\n\n\n'
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=22430,posts=23403,media=6964,facets=49,percent=pct,all_complete=False,goal='active',receipt=now)))
