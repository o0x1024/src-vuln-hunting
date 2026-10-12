"""Exact-once0123 receipt after observed full verifier exit0."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==16677 and s['body_reviewed_posts']==17458 and s['remaining_body_groups']==34802
assert s['media_visually_reviewed_unique_contents']==4339 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==16677 and v['semantic_review_posts']==17458
assert v['local_markdown_links_checked']==2511 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==4316
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0123.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0123.json').read_text()) and len(fs)==70 and len({f for f,_,_ in fs})==28
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 text=(T/'references'/f).read_text()
 assert text.count('## '+title)==1 and text.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0123.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==115 and all(pid in ids for pid in urls) and len(b)==250 and len(ids)==252
actual=json.loads((W/'media-actual-0123.json').read_text())
media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==89
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0117' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0123' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0123_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0123_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=70,source_URLs_bound_to_batch=115,full_verifier_exit=0,full_source_hashes=52716,rendered_links=2511,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read='MDN HttpOnly direct read vs cookie sending; OpenJDK8u URL url prefix and actual scheme parsing')
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix=f"""CURRENT COMPLETED0123/media0117. ACTIVE unbudgeted all-posts goal; all false. NEVER rerun successful native0123/media/bodyrecord0123/finish0123. Next0124/media0118. Authoritative16,677groups17,458posts={pct:.2f}%; remaining34,802groups35,258posts; total51,479groups52,716posts; followup0. Hashboundmedia4,339=2,448distilled1,131nontech760insufficient. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520. User缺失图片、外链全文 不用管，按已覆盖算; nofetch/recovery/blocker. Remaining SAVEDcompletebodies/currentAVAILABLEimages require actualreview. Standalone runtime no archive/currentdir dependency. No subagents/memorywrites/sourceexecution/livehandles; preserve unrelated changes.

0123 prepare9dd8a0:250groups252posts53,851chars first1495488681012047877 last1499748400203509772. ALL250completebodies ACTUALLYREAD1-65d5baaa/66-13070e763/131-195a95c1a/196-250bc4f10. Meaningfulalts122Writeups150RootUser213/224Squareprofile actuallyread. Two duplicate groups124ids1497529982725369858+1497863415682924545,225ids1499399267890262031+1499730476428259328. Inventory369d91:122paths92unique3known89new250missingwaived. ALL89originalpixels viewed ownSHA/base64matched;0-83priorcontext84-88 currentview thenmediaactualpersisted BEFOREledger. Final5taserSpider/readmeCVEscan/userdetailGET/JSclientsecret/OCRsuccess all reviewed. Own70facets28topics115URLs; manually250rows131excluded41new32corrected46merged;89media52distilled27nontech10insuff. Precheck5a0dbcPASS before mutations. Native54beedSUCCESS ONCE70routes;media cb7bffSUCCESS ONCE89/media0117;body1fd395SUCCESS ONCE250/252. Quick8ff287valid/gitd172bfpass/runtime7431ceexit1nohitsEXPECTED. Full51cd6esession39630 FINALmust be observedexit0:52716hashes16677groups17458posts4339media4316external3inline9occ20priorunavailable2511linksbroken0. FinishassertASTfacets==JSON/every70headingbodyrouteexactonce/all250body89mediaexactonce/timestamps. No handles after fullcomplete.

0123 keymechanisms: Voltronlocaldebugarch/thread/stopnotremoteentry; SVGescapeandnamespace/CSPactualconsumer; iframejavascriptandESIservervsbrowserstage; cookieanalyticsnotusableauth; configDBAWS/clientorgIdtokenactualsecretpurpose; phpinfo servercookieecho vsHttpOnlyXHRcredentialsSOP/CSPnotdirectread, multipartsuccessnotreader; Gitclone/mirrorrefspec/history; API .json/slash/v2/account/XOriginalURLsameobject; AndroidPOSTuseridreportnotATO; ADBDebugBridge5555notroot; region/rewarddorknoauthorization;48hcontact/publicitynotpolicy; DorkSearchcategorynotquery; NucleiBurpgeneratorGETlocalhostnotmatcher; aquatoneinputvsserviceclaim; bankindexPIIuploaddeletepermissionseparate; CVSS/videoindividualfeedbacknotformula; WinBruteLogonfoundlognotauth; DNSrebindingresolutionvsconnect; redirect25paramsactualnavigation; ignoringallusualsubdomainsmissrisk; GraphQLemptyOTPpartialtrue/errorsnot2FA/RCE; JNDIlistenlinkslookup/load/execute; ownWPcloneversions/roles/config; PublicWWWcachedcodeindex; POSTPUTsameobjectstate; Googlerole/serviceIdconstantsnotassignment; Tomcatrootnamevsuid; ShipmentDetailsUI/APIIDORP3titlesnotauth; NTLMmultipleendpointchallengevslogin; Host302Locationnotreset/cache; dotsemicolonnormalization; Katoolin3titleimagev1.0; XSSlabelsnotexclusive/mutationfiresUIneedsbeforeafterDOM; fullportsneedscopebudget; staging/logcandidateinputformat; GraphQLmindmapschema/actionsrolesmicrotextnotlegible; alreadyrootGiftflagnotentry; DRAKVUFsamplehashPE32process15snotmaliciousness; RCE25/10paramnamesnotsink; nestedimage metadatachainnotheader/fetcher; receivedsubmissionnotclaim/triage; ERBcompiledsourcevsvariable; CSRFreport/loginformXSSidentitybinding; JavaJDK8urlprefixregexvsnewURLHTTPonlynotfilecast; uploadpolyglottwoconsumers; bankJSONverificationStatusnotwrite; Osmedeusdone26/26/paths/privateinstallerdownloadnotreport/install; emptyregistrylistvswrite/deploy; statuscounts/deduprewardsnotrootcause; CAPEstatsnotbehavior; tokenprefix00000007restdifferentnotpredictability; MoodleDBstoredSQL0.00notsecondstage; Searpy202009historicalindex; Gatewayrefresh200GUIwithoutroutewrite/versions/causality; Litefuzzhelp/modes/min/postcmdnotcrash; BuildHackFixRepeatownbusinessinvariants; uncoverIPportsengineidentitynotJira/scope; Ukrainecounts/testingtagsnotpermission; reconappend/overwriteuniq-i semanticfiltercoverage; ProxyEverythingTLS/filter/inputtypeboundaries; malformedCVEgrep onmouse notexecution; taserSpiderP10regexJSsilenterrors/urocollapse; NucleiCVEreadmecriticalnotversion/vuln; vhostHostURLsyntax/statusnotcontent; resetadmintitleGETrestuserviewBearerTEMPnoresponse/reset; OCRsuccess/timeoutnoOCRtext; SQLitale passive acquisition/WHOISnotSQLi; AndroidServerStatusVRTnotATO; Metapicture/videohistoricalbaronly. Promo/titleonly/external-onlyexcluded noindependentmethod; saved technical claims without exchange corrected/merged as appropriate; waiver notfabricatedread.

Normativeactualread ONLY OpenJDKrawURL.java turn377view0/turn378view0lines529-555(urlprefix) and MDNSetCookieturn377view1/turn378view1lines254-257HttpOnlysentXHRfetch. Waivedexternalposts/repos/videos/threadfulltextnotfetched. AllshellRTK instructions07d941lastactualread. Memory424-425mechanism→conditions→minimalcomparison→evidence→counterexample actuallyused; finalciteMEMORY424-425rollout01a11e72-23a9-7091-85bd-fb3171d2e135; no memorywrites.

Next0124/media0118: stageprepare250max65000 andinventory; read4untruncatedcompletebodysegments +meaningfulalts; neworiginalpixels6/call ownSHA/base64bound saveactual BEFOREledger. Manualnative/specs250postURLbinding audit; safebuilder rename TEMPLATEbatchmetadata BEFORE injectingnewfacetsJSON (avoid0121historyURLbug). Precheck BEFOREnative/media/bodywrites eachSUCCESS once. Quick/git/runtime PromiseallSettled inspectevery; fullsamehandle FINALexit0; receipt exactonce/HANDOFFprependpreservehistory. Goal remainsactiveprogress; nevercomplete untilremaining0/allrequiredcurrentmedia/native/fullcheck. Final conciseChinese accurateprogress, missing/externalcovered, allnotcomplete.

"""
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=16677,posts=17458,media=4339,facets=70,percent=pct,all_complete=False,goal='active',receipt=now)))
