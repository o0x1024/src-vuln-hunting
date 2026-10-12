"""Exact-once receipt after full verifier observed final exit0 session13066/7e1c82."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==25763 and s['body_reviewed_posts']==26780 and s['remaining_body_groups']==25716
assert s['media_visually_reviewed_unique_contents']==8788 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==25763 and v['semantic_review_posts']==26780
assert v['local_markdown_links_checked']==5509 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==8765
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0169.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0169.json').read_text()) and len(fs)==96 and len({f for f,_,_ in fs})==36
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0169.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==132 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==166
actual=json.loads((W/'media-actual-0169.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==95
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0163' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0169' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0169_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
assert pct==50.8
v['batch0169_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=96,source_URLs_bound_to_batch=132,full_verifier_exit=0,full_verifier_session=13066,full_verifier_final_chunk='7e1c82',full_source_hashes=52716,rendered_links=5509,broken_links=0,post_coverage_percent=pct,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0169.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

prefix = '''CURRENT COMPLETED0169/media0163. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0169. Next0170/media0164.
Verified25,763groups26,780posts50.80%; remaining25,716groups25,936posts total51,479groups52,716posts. Media8,788=5,067D2,301N1,420I; availableexternal8765 inline3/9 priorunavailable20 links5509 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.
User waiver missingimages/externalfulltexts covered nofetch/recovery/noinventreading; ALLsavedbodies/currentavailableimagesrequired. Standalone no source runtime dependency. RTK shell/no subagents/memorywrites/livecredentials/sourceexecution/install; preserve unrelatedchanges.
0169 prepare4a4e37 inventory0cf111160groups166posts37121chars first1639587578285522949 last1641826778296532993.112paths105unique10known95new173missingwaived. ALLcompletebody actual1–60b171b2;61–110ed4b66;111–160631c75. Known10metadatac77894 JavaURLcontrols/emailreseturl/faviconhash/oldOTP/HPP/two replace diagrams/Hostlocalhost/localhostdirectory/25LFIparameters. All95neworiginal returnedSHA/time actual-0169.json95 notes0169.json95;61D19N15I.96facets36topics132URLs126mapped96corrected30merged34excluded. No externalfulltextfetch normative0169=[].
Manual media0–47 beforecompact;42–47notespersist d69ce4; original48–95 aftercompactcalls complete. Draft2b2c83/build5d2eeb/precheck2a1fff. Nativede8a88/mediaf9a5d6/body486ce1 ONCE. Quickeadd62valid/git0f7e72exit0/runtimeb4347cexit1empty. Full746846session13066 thenFINAL7e1c82OBSERVEDexit0 52716sources25763groups26780posts8788media8765hashes5509links0brokenallfalse.
Principal0169 corrections: client302responsebodyvsserverauth; SQL100percentfalse/quotedemailcontexts; JavaURLcontrols; GitHubsecretsenvironment/permission; fake200lengthfilternotsemantics; resetauthorityboundtoken; MFAresponseUIvsprotectedaction; WAFstatstablevsconsumer; globIFSnotsemanticproof; JiraNucleiversion; OTPchallenge/####notbypass; SVGfiletitleunsaved; DeckselfABobjects; faviconhashdataerrors; Railshistoricalredirect; DropboxBoxsharepurpose; ver_tokenXXXemailmissingdelimiter; browserXMLHttpmissingconstructor/viewsourcefiledesktopnotserverLFI; followcountIntruder403/Repeater20notidempotencyproof; oldendpointpatterns; Duplicateprivacy; CelerCriticaltextHighcardnopermission/valueproof; ThunderCloudhelpnotexecution; Cloudflareverifiedemailoldtokens; Composerdevvsproduction; OneListleakypathsemptycanvasnotwordlistfulltext; AWSsharedrange/certscope; Tomcatmanagernotdefaultcreds; SharepointOnedriveAzureGooglethirdparty/noinfo; JWTkidmissingcomma/incorrectfilekeylookup; CSRFbrowsercookieSameSite; IDORlistGUIDnotdecrypt/200403actualaction/limitedAB; SSTI7x7=49not14 and 81reflectionnotRCE/replayextrarequests; inet_atonvsinet_pton/::80not::1/127networknotation; OSINT3imagesvs6claims/SearchEngine24rolesnotcoverage; Nmapevasionlistsnotpermission; massassignmentpersistentauth; newfeatureincrementalversion; directoryreportnocontent; ASP.NETduplicateparamconsumerorder; suffixgrepnotURLparse; Arjunuserpassnamesnotlogin; readonlylocalcommandsvschmod; LINEfilenametitlelow; errorSQLinotCriticalbydefinition; staffuserdataABtenant; Dalfox100skipcoverage; PyIntelXSlacknocredentialsvalidation/nonotification; ELMAHmediumNucleisyntaxerrorsvsP1cookieclaim; Deciderbuildlogsnotmapping; XMLnamespacelocalhostpromptMIMECSP; /api/su/resetPwdnorequests/ATO; Googlesiteparamcandidates; CloudFlairhistorynorealsource; PHPgadgetrequirescontrolpanelpermissionsHigh; phpMyAdmincase301200nosetupaction; Cmdlistplatformdifferences/downloadchainnotrun; LINEinvalidgroupkeyclientiOSCVE41568LowvsHighhistory; 123toolsactual1–69duplicates; trialexpiresUIvsentitlement; tokenP5thirdpartyscope; document.domainunderscorewithstrictcontextnoDOM; SubfinderpassivevsDNS/ownership; HTTPXgrepclrfmistypenoautofix; SVGdirectpromptnotimgpreview; DNSSERVFAILnotclaimable; Burpdebugflagobservability; LinkedInnewsletterpublicIDprivateSubscribersownership; gitmetadata/staticWPsaveactualsource/smallredaction; replacefirstvsregexg; tinyXSSname/srcdocCSP/strict/frames/polyglotcontexts; undicihostCRLFwirehistorical23936; OpenSSL23919same-threaderrorstacklifecycle; redirectgrepfrequency; AVAXhighwater/rebalanceinvariantnoformula/state/tx/backgroundSSRFirrelevant; S3presignedPOSTnotlongtermsecret; hacktivitycurrentfixregression/authorization; serverinfohighduplicatesidebarnoresponse; MSI882056vs1156019bytesstaticonly; DoSoutofscopeversionattackstartednotimpact; socialbrokenlinknotNextcloudATO; gobusteroutputpathmismatch/cuturl/loopsTLSredirectbudget; HostlocalhostsocketSNIseparate; OTPtrustedproxy/accountchallenge; XLSXparserDTDnotuploadproof; backgroundextensionobservationsnotfullaudit; oldOOSbonusnobroadpermission; FingerprintXlogoNOprotocol; wgetnoparentnotallhostboundaries;25LFIparamnamesnotconsumer; APKpull/decode/rebuild/signingroles; PaddingOracleCBCauthenticationvsoracleclassification; responsesplitvsrequestresponsequeueassociationnootheruserproof. All61D exactfilename/postbound.
NEXT0170/media0164 prepare160max40000ONCE thenactualALLcompletebodies/neworiginalimages<=6/callmanualnotes/returnedSHA/time. Build/precheckbeforeappend;native/media/bodyONCE;quick/git/runtime/fullsameprocessOBSERVEDexit0;finishONCE/HANDOFFprependhistory. Helpersdata0169/actual0169/notes0169/draft0169/reviewImageBatch0169/bodyReader0169/draftHelper0169/imageHelpers/counts0169/normative0169/checks0169 live;loadclonesalwaysstore. Templatesbuild/precheck/native/finish0169. pct=round(100*posts/total,2), NEVERreplace100withURLs. No livehandles. Memory424–425 actual8bf458 provenance01a11e72-23a9-7091-85bd-fb3171d2e135.

'''
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=25763,posts=26780,media=8788,facets=96,percent=pct,all_complete=False,goal='active',receipt=now)))
