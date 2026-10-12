"""Exact-once receipt after observed full verifier final exit0, session86904/c8b13f."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==18427 and s['body_reviewed_posts']==19249 and s['remaining_body_groups']==33052
assert s['media_visually_reviewed_unique_contents']==5054 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==18427 and v['semantic_review_posts']==19249
assert v['local_markdown_links_checked']==3073 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==5031
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0130.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0130.json').read_text()) and len(fs)==78 and len({f for f,_,_ in fs})==32
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0130.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==113 and all(pid in ids for pid in urls) and len(b)==250 and len(ids)==253
actual=json.loads((W/'media-actual-0130.json').read_text())
media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==116
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0124' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0130' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0130_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0130_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=78,source_URLs_bound_to_batch=113,full_verifier_exit=0,full_verifier_session=86904,full_verifier_final_chunk='c8b13f',full_source_hashes=52716,rendered_links=3073,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read='MDN Set-Cookie HttpOnly/fetch/CORS/transitionend; HTML fragment navigation; Python string octal escapes; PHP-FPM status fields; EJS tag/data rendering; RFC8259 object name uniqueness')
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)
prefix=f'''CURRENT COMPLETED0130/media0124. ACTIVE unbudgeted goal 完成所有posts内容的提炼; all false. NEVER rerun successful native0130/media/bodyrecord0130/finish0130. Next0131/media0125. Authoritative18,427groups19,249posts={pct}%; remaining33,052groups33,467posts; total51,479groups52,716posts; followup0. Hash-boundmedia5,054=2,813distilled1,305nontech936insuff. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520. Waiver缺失图片、外链全文 不用管，按已覆盖算; nofetch/recovery/blocker. Remaining completeSAVED bodies/currentAVAILABLE images require ACTUALreview. Standalone native references noarchive/currentdirruntime. No subagents/memorywrites/sourceexecution/livehandles; preserve unrelated targetchanges.

0130 prepare dc8f50:250groups253posts54,158chars first1524108644857614340 last1528338331657977857. All250 complete bodies actuallyread untruncated bfbe5b/89b33d/10386a/41c161; meaningfulalts27/31/70/133/188/203read. Inventory266f7e122paths118unique2known116new275missingwaived. All116 new originalpixels0-115 ACTUALLYviewed20calls6/calllast2; ownSHA256decodedbinarymatched +timestampspersisted actual-0130.json BEFOREledger. Manual78facets32topics113batchURLs;99bodygroupmaps=65corrected34merged151excluded; media56distilled23nontech37insuff. Build6195ec/precheck455fe5 PASS; nativeccb23c SUCCESS ONCE78routes; media d29e4a SUCCESS ONCE116/media0124; body8f1692 SUCCESS ONCE250/253. Quick730fd5valid/git80e17apass/runtimeb86a6eexit1nohitsEXPECTED. Full0221d6session86904 FINAL c8b13f OBSERVEDexit0:52716hashes18427groups19249posts5054media5031external3inline9occ20priorunavailable3073linksbroken0. Finish all78headings/body/communityroute and250body116mediaexactonce/timestamps. Receipt {now}. No pendingprocess.

0130methods: scope regex host terminus; profile persistent read identity; concurrent proxy requests receipts; deleted user role/session revocation; Burp export object types; Recon phase contracts/function matrix/filters; SAML signature generation vsacceptance; OTP Host handler/arrays/counter identity; SSP functiontable vsrealcalleeprivileges; Windowsstage/demo limits; reset MIME/parser/recipient/tokenowner/finalstate; Kerberos/AzureAD exchange subjects; SVG/polyglot finite event grammars; secondorder XSS eachsamplewrite-read/macro scope/finalcontext; GraphQL operation vsrequest count; localhostmethod200≠sameactionbypass; M2M machinegrant≠forging/userATO; paramnames≠consumer; faviconsharedhash≠ownership; SOAPserialization/classpath≠gadgetRCE; Authorizationrequestvsresponsecredential; URLpipelinefilterloss; JSONnestedobject/duplicates/typesfinalauth; disclosurepolicy specificbountyvsdetails; Jenkinsconsolelimitedcommand/authunknown; mobilecloudshellfilesnotinstalled/currentfreeguarantee; ratelimitkeynormalization/reset/CAPTCHAserverresult; hiddeninputrequest/navigation; prediction/Runninglabelsnotconfirmation; transitionevent requires real completedpropertychange; HTMLMIMEJSONshape actualDOM/CVEidconflict; privateDSLdependency/executionlogsnotallplannedlevelscomplete; configactivevscomment/environmentconsumer; HttpOnlycookie vsbusinessresponse/sameorigin/CORS prerequisites; Oracleindex/template/registration/userfields finiteauthscope; fragmentfocus browserconditions; Angular string vscompile; JWT offlineentropy/signatureacceptance; editedauthresponse vsserverstate; CRLFtextvsheader/HTML; OTPemaillinkinitialcontrolprereq; SwaggerresourceDOMversion/CSP; CNAMEHostSNIlicense; takeoverinvertedgrep/staleappend; indexcounts/querytruncation/time≠allassets; WHOISorg≠CIDR; trafficOpenAPIobservedvsfullcontract; dompdfremote/PDF/cache/webexecutionstages; Pythonoctal stringvsPyScriptDOM/serverexec; FPMfullmetrics/currentURI/pathnotallroutes/DoS; Lambdaactivations/cost/role/endartifacts; shellglob vsJavafileconsumer vsHTTPquery; filebytes≠include/RCE/hash; EJSdata vscompilesource; CORSrawOriginbrowserconditions/DNSAAAA≠HTTP/rebind/ATO; sqlmapresumedprovenance/customparam≠WPcore; commandUI notJSinitialchain; clienthardcode vsbackendsession/auth; Plexexistingtokenrequired; crawledlinksrelation≠dead/API/scope; labs≠production; resolvedmail≠retest; listenerbind vscallbackroute/TLS/generatedfile≠connected; internettechniquesrequirecurrentscope; historicalCWEmechanismnotcurrentrisk; ports presetfinite; blockeddevice/rolesdocsserverrevocation; httpxstructuredstatusnotarbitrarygrep; Sysmonrelationneedsorigfields. No secret/PII values copied or used.

Primary normative actuallyread400-401: MDN HttpOnly/fetch/CORS/transitionend, HTMLfragment, Pythonoctal, PHPFPM, EJS; RFC8259 previouslyverified. Waived archiveexternalarticles/repos/videos/threads NOTfetched. RTK actual456228 current. Memory relevant actual424-425 prior68b769; finalcitationMEMORY424-425rollout01a11e72-23a9-7091-85bd-fb3171d2e135. No memorywrites.

NEXT0131/media0125: prepare250max65000+inventory; read untruncated completebodies inclmeaningfulalts; originalnewpixels6/call ownbinarySHAactualtimestamps BEFOREledger. Manual facets/body/media specs exactURLsourcebinding. RenameTEMPLATE metadata BEFOREsourceIDs/facets inserted. Precheck BEFOREnative/media/body successonce sequential. Quick/git/runtime allSettledinspectall; fullSAMEhandle FINALexit0; exactonce finish/HANDOFFprepend preservehistory. Nevercomplete until remaining0/native/currentrequiredmedia/fullscopeverified. Allshellcommands startrtk. Functionstores imageHelpers/draftHelper0130/data0130/actual0130/draft0130 persistent;116 actualmedia complete. Safe build/native/precheck/finish0130templates; stage.py bookkeeping/recover.pyconstantshelpers only NEVERrecovermain. No pendingprocesswhenfinalized.

'''
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=18427,posts=19249,media=5054,facets=78,percent=pct,all_complete=False,goal='active',receipt=now)))
