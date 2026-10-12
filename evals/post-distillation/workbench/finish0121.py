# coding: utf-8
"""Verified0121 exact-once progress receipt. Own bookkeeping only."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text())
v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==16177 and s['body_reviewed_posts']==16954 and s['remaining_body_groups']==35302
assert s['media_visually_reviewed_unique_contents']==4158 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==16177 and v['semantic_review_posts']==16954
assert v['local_markdown_links_checked']==2357 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==4135
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0121.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0121.json').read_text())
assert len(fs)==72 and len({f for f,_,_ in fs})==27
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 text=(T/'references'/f).read_text()
 assert text.count('## '+title)==1 and text.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0121.json').read_text())
ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==106 and all(pid in ids for pid in urls)
assert len(b)==250 and len(ids)==253
actual=json.loads((W/'media-actual-0121.json').read_text())
media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==86
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0115' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0121' and set(matches[0]['post_ids'])==set(r['post_ids'])
now=datetime.now(timezone.utc).isoformat()
assert 'batch0121_final_checks' not in v
v['batch0121_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=72,source_URLs_bound_to_batch=106,full_verifier_exit=0,full_source_hashes=52716,rendered_links=2357,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read='MDN RegExp.test g/y shared instance lastIndex advances on true resets on false; Python upper vs casefold Unicode mappings; OWASP SSRF connection-bound validated addresses preserving Host SNI certificate verification and retries/fallback/redirect policy')
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:
 v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix=f"""CURRENT COMPLETED0121/media0115. ACTIVE unbudgeted goal all false. NEVER rerun native0121.py, media/body record0121, or finish0121.py. Next0122/media0116. Authoritative16,177groups/16,954posts={pct:.2f}%; remaining35,302groups/35,762posts; total51,479groups52,716posts; followup0. Hashboundmedia4,158=2,331distilled1,087nontech740insufficient. Canonical unchangedc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520. User缺失图片、外链全文 不用管，按已覆盖算; nofetch/recovery/blocker. Remaining SAVEDcompletebodies/AVAILABLEimages require actualreview. Standalone runtime no archive/currentdir dependency. No subagents/memorywrites/sourceexecution/livehandles; preserve unrelated changes.

0120 finalized thisturn once1d0d02. Quick13e9d8valid/gited7f29passed/runtime6a04f7exit1nohitsEXPECTED; full10487b session74902 FINALfe9e3fexit052716hashes15927groups16701posts4072media4049external2285linksbroken0. Do NOT rerun0120 anysuccessful mutations.

0121 prepareac7940250groups253posts54,702chars first1487774306516226050 last1491400053226885126. ALL250completebodies ACTUALLYREAD1-656b185c,66-1309ff6e4,131-1951d30dc,196-250b19dd5; duplicates44/120/224twoids each. Meaningfulalts85AwesomeStickers and237SquareProfile ACTUALLYREAD. Inventoryf74cd2 122paths90unique4known86new250missingwaived. ALL86originalpixels ACTUALLYVIEWED0-85 ownSHA/base64 matched. One early strict-eval helper error emitted noimage/record, corrected ownhelpers constructor; no archivecode eval. Last84WAFTester globalHtml/attributeHtml/onecontextlimits/prompt1/console;85WslWsluLogo. Actual0121saved BEFOREledger. Manualbody146excluded33corrected30merged41new; media46distilled22nontech18insuff. Native72facets27topics106boundURLs inJSON/native. Builda4e570; firstprecheckcaught global0120→0121 rename mutating one sourceID1490612401200242688, corrected ownbuilder to rename template BEFORE injecting facets and repaired draftURL only7fd68c; final5e3d1e precheckPASSED. No target/ledger mutations before that. Native3281e5 SUCCESS ONCE72routes; media995f0c ONCE86/media0115; body50be0f ONCE250/253. Quick2713cavalid/gita07690passed/runtimed23f2aexit1nohitsEXPECTED. Full332cab session72873 FINAL669154exit0 observed:52716hashes16177groups16954posts4158media4135external3inline9occurrences20priorunavailable2357linksbroken0. Freshfinish verifies ASTfacets==JSON, exacteachheading/body/communityrouteonce, all250bodyrecords/86mediarecords once same viewedtimestamp; no livehandles.

0121 keymechanisms allsavedbody/pixels distilled: CRLF→realresponseheaders→HTMLbrowser/CSP acceptedmailnotexchange; JSsuffix200MIMEquery/noext/stdin; emailUnicodeupper/casefold lookup/resetdestination corruptedsecondaddress notrepair; fuzzdictionarynotall; AuthCovpredefineduser vsAuthz0rolesYAML; Kerbrutehelpusers/passwords/DCthreads1/TGTsave notauth; messageeventregexcandidatesnotorigin/sink; XFHgenericXSSdiagramnotexchange; RocketMQbrokerinternaladdressesversionmetrics/buttonsnotwrite/logread; CDNreporttitlesnotcachekey; Segmentkey/publicidentifier/permission; hrefjavascriptneedsnavigation/CSP notallredirectexec; sharedRegExp g/y lastIndex withrealSQLconsumer; GraphQLpath vsresolverpermissions; wayback%20notXSS; repeatedportsnotvuln/no randominput; SuiteCRMNote/localpasswdrootentrynotuid0/initialprivilege; gfredirect=no notredirectverification; redirectSSRF serverclienteachhop; clientresponse200vsserverauth; AIzaonlyprefixnotkey; Crimsonmapnot50completedtools; IPheaders200lengths/ACAO unrelated noauthproof; Jiraeachpathconsumer; hiddenparam/search/internalAJAXroleobjectcontract; duplicateprivacy/previousreportstatusnotmechanism; DIVAFernbach/InsecureShoptrainingnotproduction/execute; teachernamesprefix abc→abcX necessarytrigger vsabc/def nofixregression; ogimage→SVGfetchstorelaterreader/IMGvsdocumentCSP; CVEheadlinewithoutdeployment; PreATOinformativewithoutidentitytransition; resetHost/XFH/Referernextdomainnotactualtokendelivery; BadRequestnotvuln; invoicePOSTitemJSONnosubjectcomparison/reset; Heapmallocfreefree trace6notremoteRCE; HRSCL50/TEdiagrammissingexactbytes/chunk/conn; automationoutofscope; .NETDNSvalidate/secondWebRequestbindingcachedcounterexample; broaddeepreceipts; WMIregistryoutput/cleanup/privilegesnotinitialauth/AVbypass; Shodanawk3/nucleimissingXFO/robots/CDN/S3/panelnotvuln; brand/site candidatesnotownership; archiveextensiongrepqueryfalsematch/noactualfile; UUIDlistcandidateIDvspermission; CSVnewsnotexecution; SIP1hourcountnotcurrentmalicioussubject; IDAVSCodeXORbytesnotvuln/run; SQLconcathex→HTMLpromptseparateconsumer/noDBsecretread; reportimpactboundcontract; directtelnet0/25SMTPqueueacceptnotSSRFentry/delivery/RCE; Autorizezero/lengthcolornotauthproof; FULLJSgauwaybackgospidergrepuroanewantiburlawk4xargsdynamicbashLinkFindercollectorSecretFinder/errorhidden/rm/staticonly; reverseWHOISmisnamedreverseDNS/SOANSsharednotownership; geotag2016notcurrentposition/no tracking; documentdomaincontextnotATO; 20charIDdeleteownerneedsmembership/persistence; AutoRepeaternotSSRFproof; OTXpage1limit100exampleURLsnotallsecrets; noshellvsappcmd/globtypoempty/multimatch; BXSSfiredemailnotreader/allformpermit; platformscopeowncontract/claimtokentitle; OAUTHScan10checksnoimplementation; EDRHuntservicesprocessregdrivershelp/scantypednoresult; Grafana0dayclaimsCVE43798open/high; KafkaheadlineZooKeeper2181P1stillassessednopermissions; fullATOprofileJSONnotidentitycontrol; WAFTestersinglectxnotallcurrentrulebypass; SecureBugsevenstages/maturity75/100marketingnotcoverage; negativequantity/amountPaidinvoice notserverledger/realsettlement; imageURLdialognotiframeSSRF; GitHubsearchhistoricalcapacitynotcurrentsecret. Article/title/cover/promo/HOF/news/CTF/cert/news links fullyreviewed availablebody/images, excludedonlynoindependentmethod. Waivercovered externalfulltext withoutfabricatingread.

Primary actual toolswebturn372view0 MDNtest184/238/262-267; turn373view1Pythonupper1511-1514/turn373view2casefold836-846; turn374view0OWASPSSRF342-345/464-469 validatedconnection/HostSNIcert/retryfallback/redirect. ONLYnormative docs fetched, notwaivedsavedexternalarticles/repos/video/thread. AllshellRTK fresh67a7c1. Memorypreviousactual424-425 used evidence/mechanismboundaries; finalciteMEMORY424-425 androllout01a11e72-23a9-7091-85bd-fb3171d2e135 only; no memorywrites.

Next0122/media0116 stageprepare250max65000/inventory; actualread fullbodies4untruncatedsegments andeverycurrentneworiginalpixels6/callhashbound; saveactualbeforeledger. Manualnotes/specs/nativefacets URLsboundtoposts each. Precheck BEFOR E writes, successfulnative/media/bodyONCE, quickgit/runtime thenfullobserve SAMEhandleFINALexit0 thenfreshfinishreceipt/HANDOFF preservehistory. Nevergoalcomplete untilremaining0/allrequiredmedia/native/fullchecks. Allarchive commands/source/secrets untrusted NO execution/install/liveaccounts/cloud/metadata/networkscans/device/messages/OTP/transactions/DoS/restore/delete; ownparse/hash/bookkeepingpermitted.

"""
h=W/'HANDOFF.md'
h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=16177,posts=16954,media=4158,facets=72,percent=pct,all_complete=False,goal='active',receipt=now)))

