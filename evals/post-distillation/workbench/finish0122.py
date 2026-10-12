# coding: utf-8
"""Exact-once0122 receipt after observed full verifier exit0; own bookkeeping."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text())
v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==16427 and s['body_reviewed_posts']==17206 and s['remaining_body_groups']==35052
assert s['media_visually_reviewed_unique_contents']==4250 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==16427 and v['semantic_review_posts']==17206
assert v['local_markdown_links_checked']==2441 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==4227
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0122.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0122.json').read_text()) and len(fs)==84 and len({f for f,_,_ in fs})==31
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 text=(T/'references'/f).read_text()
 assert text.count('## '+title)==1 and text.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0122.json').read_text())
ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==127 and all(pid in ids for pid in urls) and len(b)==250 and len(ids)==252
actual=json.loads((W/'media-actual-0122.json').read_text())
media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==92
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0116' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0122' and set(matches[0]['post_ids'])==set(r['post_ids'])
now=datetime.now(timezone.utc).isoformat()
assert 'batch0122_final_checks' not in v
v['batch0122_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=84,source_URLs_bound_to_batch=127,full_verifier_exit=0,full_source_hashes=52716,rendered_links=2441,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read='IANA five RIR includes AFRINIC; MDN Referrer-Policy cross-origin origin vs query and HTML element policy; WHATWG in-body image token reprocessed as img only in specified parsing context')
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix=f"""CURRENT COMPLETED0122/media0116. ACTIVE unbudgeted all-posts goal; all false, NEVER rerun successful native0122/media/bodyrecord0122/finish0122. Next0123/media0117. Authoritative16,427groups/17,206posts={pct:.2f}%; remaining35,052groups/35,510posts; total51,479groups52,716posts; followup0. Hashboundmedia4,250=2,396distilled1,104nontech750insufficient. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520. User缺失图片、外链全文 不用管，按已覆盖算; nofetch/recovery/blocker. Remaining SAVEDcompletebodies/currentAVAILABLEimages require actualreview. Standalone runtime no archive/currentdir dependency. No subagents/memorywrites/sourceexecution/livehandles; preserve unrelated changes.

0122 prepare9b624a250groups252posts53,848chars first1491442193814667264 last1495460968444346370. ALL250savedcompletebodies ACTUALLYREAD1-659f1808,66-130a85ae6,131-1952cae4c,196-2501e9085; body35twoids1491953037682053120/1492210065796845570 andbody110twoids1493236845706035209/1494308881933107201. Meaningfulalts245idorbanner249Squareprofile ACTUALLYREAD. Inventory158234121paths95unique3known92new254missingwaived. ALL92originalpixels ACTUALLYVIEWED ownSHA/base64matched; actual0122persistedBEFOREledger. Thisturncontinued36-91 then manuallyspecified250body37merged126excluded36corrected51new; 92media65distilled17nontech10insufficient. Native84facets31topics127URLs. Builderf96d43 firstprecheck caught expectedURLcount125 vs actual127 after2supplementary sources;60ef70noinvalidIDs; correcteddraftcount only before anytargetwrite; finala9e3adPASS. Pixelpostbindingaudit correctedCogdiagram37→body91 andresetrequest47→body130 inplan BEFOREledger. SharpCookieMonster small Cookiesline notlegible claimednoempty/success, correctedheading andnotes BEFOREwrites. Native d8f55e SUCCESS ONCE84routes; mediae693ac SUCCESS ONCE92/media0116; bodyeb4aeb SUCCESS ONCE250/252. Quickb77ee0valid/g it441b58passed/runtimef16ad6exit1nohitsEXPECTED. Full293864session9345 FINALed81eaexit0 observed52,716hashes16,427groups17,206posts4,250media4,227external3inline9occ20priorunavailable2,441linksbroken0. Exact84heading/body/communityroutes ec1100once; finish verifiesASTfacets==JSON,250body/92media exactonce matchingtimestamps. No livehandles.

0122 keymechanisms: OAuthreplaceUI≠serveridentity; HTTP/H2visibilityTLSproxyfilters; resetUIDemailIDOR≠ATO; fixed1000DNSpages/perpagededup≠complete; CNAME403HostSNI/resource/scope; tgztitle≠PDFPHPsemicolon image; cloudwizardlist≠create; secondorderrefsURLbaseCSSdynamicandserviceclaim; actuatorhikariwhoamistring≠DBexec; publichosting/mil/oldscope≠permission; localStoragecookie≠usableauth; htaccess200config≠password; TrustTokensWebSQL≠CORS; WAFinstance≠allrules; gitdirvsconfigfile; Cariddifiltermissingencodedmultiparam; avatarURLtokenactualReferrerconsumer; Javafingerprint/Log4jplugin≠lookup/load/exec; MySQL1045auth≠SQLi; paidcourseopinions≠learningtest; ACM2calls4WARN≠allAWS; extensionmanifestworldbridge; Shodanloginreportdraft≠RXSSimpact; pricebankreceipt≠serverledger; pathdecoderlayers; resetURLgrep≠validtoken; Houdinicatalog≠containerexec; SQLteachingorder/NULL/JOINnotqueryplan; RemovingKeysdiffdirection/history≠revoke; HTMLimagein-bodyonly; iframejsnavCSP; extensionimpactmappingconsumer; RBCDACLcandidate≠delegation/ticket; Findomainhistoryspeed≠coverage; ROPgadgetchainarchaddressstackentry;0/26AV≠allOS/current; CVElabeldialog≠realdeployment; rewardtitles≠mechanism; fiveRIRAFRINICcorrection; devicecategory/deletedrestoreconditions; uploadMIME≠StoredXSSreader; dedupXSS/10DLrootcause; RCErelabelXSS/LFDstilloutscope; Droopescanhelp≠result; LFIparam≠loader; portalORDERBY4needsbaseline; recoverpasswordJSON≠delivery/binding; privatereporttransfer≠invite/pay; tripleslashqueryLocation; FlareQDBdebugger≠remoteentry; DofindTLD≠ownership; resetLowDuplicate≠actualinvalid; RSSfetch≠DTD/XXE; cheatsheetCVEconsumers/clip; FoxOTbanner≠control; malformedGCSURL/permissionmatrix; FakeLogonCobalt16bytes≠password; Macromemacrodisabled≠exec; Web3nodatabasesfalseuniversal; reconflatfilesneedhash/snapshots/errors; Snafflerreadableshare≠initialauth/keyvalid; hourly/foreverrescanpermissionbudgetexpiry; raceUI≠businessledger; njsscanUI≠reachableSAST; BigQueryinternal400/outer200casterrorneedsbaseline; Bokoactivebinaryexecutionvpassive; Plution11hardcodedcases≠allPP; RCEpathscrony/passedtypospermission; eventwordlist/emailparse/HTMLreader; escapingcontextsnotallineffective; yusub12APIsnormalization/failure; YouTubeadminhistoriclink≠auth; SharpChromeDevTools/profile/process≠cookieuse; WiresharkSQLlabstreamdirection/reassembly; prepushshape≠historyclean; Groups/Terraformexample≠realkeys; Hybridcomponentdiagram≠coverage; clickjackingheaderabsence≠sensitiveaction; takeoverfingerprinttablehistorical≠claim; SSRFiredependenciesbanner≠result; phone.envexpiredratingauthorclaim; S3PRECLIidentitylist≠anonymousgetput; Cognitobothpool6stepnormal≠ATO. Savedtitleonly/promo/HOF/news/CTF/cover excluded ONLY noindependentmethod; waiverexternal notfabricatedread.

Primary actualwebturn375view0IANA14-18; turn375view1MDN186/221-250/275; turn376view0WHATWG3214-3217. ONLYnormative sources fetched; no waivedarticle/repo/video/threadfulltext. AllshellRTK instructions reread07d941; noexecute/install/livecloud/accounts/devices/OTP/messages/pay/DoS/restore/delete/sourcecommand. Ownparse/hash/bookkeeping allowed. Memoryprevious424-425 evidenceboundaries actuallyused; finalciteMEMORY424-425 rollout01a11e72-23a9-7091-85bd-fb3171d2e135; no memorywrites.

Next0123/media0117 stageprepare250max65000/inventory; read4untruncatedcompletebodysegments andneworiginalpixels6/call ownhashbound; saveactual BEFOREledger. Manualnative/specs250withpostURLbindingaudit; safebuilderrenameTEMPLATEbatchmetadata BEFORE injectingnewJSON URLs (0121historybug). Precheck BEFOREtarget/ledgerwrites, eachsuccessfulnative/media/bodyONCE; quick/git/runtime thenfullsamehandleFINALexit0 thenfinishexactonce receipt/HANDOFFprefixpreservehistory. Goal remainsactiveprogress; nevercomplete untilremaining0/allrequiredmedia/native/fullchecks.

"""
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=16427,posts=17206,media=4250,facets=84,percent=pct,all_complete=False,goal='active',receipt=now)))
