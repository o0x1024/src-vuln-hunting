"""Exact-once0124 receipt after observed full verifier exit0."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==16927 and s['body_reviewed_posts']==17711 and s['remaining_body_groups']==34552
assert s['media_visually_reviewed_unique_contents']==4436 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==16927 and v['semantic_review_posts']==17711
assert v['local_markdown_links_checked']==2582 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==4413
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0124.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0124.json').read_text()) and len(fs)==71 and len({f for f,_,_ in fs})==31
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 text=(T/'references'/f).read_text()
 assert text.count('## '+title)==1 and text.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0124.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==116 and all(pid in ids for pid in urls) and len(b)==250 and len(ids)==253
actual=json.loads((W/'media-actual-0124.json').read_text())
media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==97
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0118' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0124' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0124_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0124_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=71,source_URLs_bound_to_batch=116,full_verifier_exit=0,full_source_hashes=52716,rendered_links=2582,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read='RFC8259 repeated object names; RFC7518 none policy and case; Go html/template trust model; Firebase overlapping allow rules; Microsoft WEBSERVICE consumers and NameValueCollection.Get comma joining; Nmap forced rule applicability')
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix=f"""CURRENT COMPLETED0124/media0118. ACTIVE unbudgeted all-posts goal; all false. NEVER rerun successful native0124/media/bodyrecord0124/finish0124. Next0125/media0119. Authoritative16,927groups17,711posts={pct:.2f}%; remaining34,552groups35,005posts; total51,479groups52,716posts; followup0. Hashboundmedia4,436=2,499distilled1,165nontech772insufficient. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520. User缺失图片、外链全文 不用管，按已覆盖算; nofetch/recovery/blocker. Remaining SAVEDcompletebodies/currentAVAILABLEimages require actualreview. Standalone runtime no archive/currentdir dependency. No subagents/memorywrites/sourceexecution/livehandles; preserve unrelated changes.

0124 prepareeae59a:250groups253posts54,389chars first1499755546974760962 last1503744476996640774. ALL250completebodies ACTUALLYREAD1-65824855/66-130012728/131-19554b35e/196-250fbe863. Meaningfulalts34RFC72/73Squareprofile82/94/164/165/209/211Embeddedvideo108BugBountyPrograms225researcherURLactuallyread. Duplicates29ids1500317156495577088+1500493308329553920,150ids1502203242620588036+1586357703164981254,192ids1502853563604938762+1503243222167875586. Inventoryc48bba:131paths103unique6known97new252missingwaived. ALL97originalpixels reviewed SHA256matched and actual timestamps saved BEFOREledger. Own69draftfacets added2SCIMHost201/Domeactivepassive, corrected doc.md draft to existing by-type/document-rendering.md; final71facets31topics116URLs. Manual250rows33new131excluded39merged47corrected;97media51distilled34nontech12insuff. Precheckca1b61PASS before mutations. Native9d90d8SUCCESS ONCE71routes; mediac370f9SUCCESS ONCE97/media0118; body6cb12aSUCCESS ONCE250/253. Quick99b6ecvalid/gitcdc62apass/runtime79431ceexit1nohitsEXPECTED. Fullfe0afasession13947must be observedFINALexit0:52716hashes16927groups17711posts4436media4413external3inline9occ20priorunavailable2582linksbroken0. FinishassertASTfacets==JSON/every71headingbodyrouteexactonce/all250body97mediaexactonce/timestamps. No handles after fullcomplete.

0124 keymechanisms: snetraInternetDBindexnotactive; Nmap+forcesruleonly; IOCcatalognotextract; ExcelWEBSERVICEWindowsactualcalcnotserverexport; Authz0roleURLcredentialsneedsobjects; BurpBounty2.4rulesversion; extensionmanifest/messageprivilege; charcode2200multipleawards; proddevID1sameidentity; Waybackmp3actualaudioPIIminimum; sdlookupCIDRhttprobeOsmedeusonlyprobe; SYNconceptnotDoS; duplicatephone_noOTPbindingRFC8259parser; AddBankformnotverifiedwrite; reportimpact/PoCattachment; DirtyPipeuidkernelrestorehashnotalldistros; ShodanDBbanner; hourlyGitpushproofnot56commits; randomparentLFIreader; GraphQLhelpnotaudit; vafGET200time61msnotvuln; WindowsfileNTLMconsumer; analyticsIDrelationnotownership; brokenShodanffufsyntax; GeoWiFipartiallookupnotlocationpermission; AndroidWebVieworiginbridge; iOSproxy/pinningactualdecrypt; HRS400InvalidHeadernotrawqueue; Amassmodesversions; MailInjectionall250sameroot; zip/tardorksarchivebytes; OTPVERIFIEDJSONnotserverauth; SASTcounts/catalognotflow; verbosepipelinecontract; FirestorewriteiftrueORnarrowupdate; MOBOTIXhistoricalsnapshot; originHostSNI; ASSAMEEAESupload54%notsecurecomplete; Log4jXFF403notlookup/load/exec; h1/iframedecoding; %00ratekeyidentity; CRLFMIMEheaderbytes; releasesnotguaranteedprobability; JWTNonecase/explicitnonepolicy; partialPIItablesnot5200BAC; privateupto250ticketpending; KYCVDPscope; regex.source/+decode/cookieanalyticsnotauth; LinkFindertextvsAPIconsumer; strcmpblacklisthostvsconnectIP; 25dorksactualquerynames; DomainAlertingwc-lnotnewregistration/notice; ngroktokenprobeunknowncaller; resetURLprefixcanonicalhostname/delivery; GoParseauthorsvsExecuteescapeddata; ASP.NETGetcommajoinAPIversion; PHPpreg_replacebadendingdelimiter→JSstring→innerHTML; JSONparsevsobjecteval; defaultcredentialstitlesnotlogin; WP4.9.9EditorUIvsdisablefunctions; LnkbombrecoveryremovednotNTLMhash; XClientIPtrustproxy; SQLUNIONresponsebaseline; SSRFeveryredirecthop; WP12pathnamesnotread/exec; fakeemailcomposerFromSendunpressednotdelivery/ticket; VMCTFinvariants; assetendpointinputrelations; Rejectedaccessiblevsacceptable; SCIMHost201notpreATO; Dome1.1resolversactive50wildcardIPnotports/scope. Promo/titleonly/external-onlyexcluded noindependentmethod; saved technical claims without exchange corrected/merged as appropriate; waiver notfabricatedread.

Normativeactualread: NmapNSEusage turn379search2; MicrosoftWEBSERVICEturn379search1; RFC8259objects turn379search0/turn380view2/turn381view2; Gohtml/template turn380view0; RFC7518none/case turn380view1/turn381view0/turn381view1; Firebaseoverlappingrules turn382search1; MicrosoftNameValueCollection.Get turn383search0/1/2/10. Waivedexternalposts/repos/videos/threadfulltextnotfetched. RTK9cfa0dactuallyread. Memory52e67f424-425actuallyused; finalciteMEMORY424-425rollout01a11e72-23a9-7091-85bd-fb3171d2e135; no memorywrites.

Next0125/media0119: stageprepare250max65000 andinventory; read4untruncatedcompletebodysegments +meaningfulalts; neworiginalpixels6/call ownSHA/base64bound saveactual BEFOREledger. Manualnative/specs250postURLbinding audit; safebuilder rename TEMPLATEbatchmetadata BEFORE injectingnewfacetsJSON (avoid0121historyURLbug). Precheck BEFOREnative/media/bodywrites eachSUCCESS once. Quick/git/runtime PromiseallSettled inspectevery; fullsamehandle FINALexit0; receipt exactonce/HANDOFFprependpreservehistory. Goal remainsactiveprogress; nevercomplete untilremaining0/allrequiredcurrentmedia/native/fullcheck. Final conciseChinese accurateprogress, missing/externalcovered, allnotcomplete.

"""
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=16927,posts=17711,media=4436,facets=71,percent=pct,all_complete=False,goal='active',receipt=now)))
