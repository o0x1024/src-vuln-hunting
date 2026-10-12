
"""Exact-once receipt after full verifier observed final exit0 session82706/5e5ba2."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==22750 and s['body_reviewed_posts']==23725 and s['remaining_body_groups']==28729
assert s['media_visually_reviewed_unique_contents']==7143 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==22750 and v['semantic_review_posts']==23725
assert v['local_markdown_links_checked']==4214 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==7120
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0150.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0150.json').read_text()) and len(fs)==45 and len({f for f,_,_ in fs})==24
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0150.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==57 and all(pid in ids for pid in urls) and len(b)==120 and len(ids)==121
actual=json.loads((W/'media-actual-0150.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==57
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0144' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0150' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0150_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0150_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=45,source_URLs_bound_to_batch=57,full_verifier_exit=0,full_verifier_session=82706,full_verifier_final_chunk='5e5ba2',full_source_hashes=52716,rendered_links=4214,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0150.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix="CURRENT COMPLETED0150/media0144. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0150. Next0151/media0145.\nVerified22,750groups23,725posts45.01%; remaining28,729groups28,991posts; total51,479groups52,716posts. Media7,143=4,052D1,911N1,180I; source52716 availableext7120 inline3/9 priorunavailable20 links4214 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery/blocker. Native independent of source/currentdir runtime. All shell rtk; no subagents/memorywrites/sourceexecution. Preserve unrelated targetchanges.\n0150 prepare0e7758 inventorydc5c2d SUCCESSONCE120groups121posts29256chars first1593657790341427202last1595763762874777601.63paths60unique3known57new128missingwaived. ALL120fullbodies ACTUALLYread d5f871(1–60)/87fc3a(61–120), selectedrecheckefd99b; meaningfulaltsread. ALL57originalimages ACTUALLYviewed0–56 <=6/call returned binarySHA/time persisted beforeledger actual-0150.json.57manualnotes explicitlystored aftereachimagebatch. No OCR inferred reviews.\n45facets24topics57URLs55mapped43corrected12merged65excluded;36D16N5I. Persist0c59a6;scriptbuild0c1d10;build83961e/precheckec1434 PASS exactimageposttargetsourcebindings. Native68f4e6/media63aea5/body9eb743 SUCCESSONCE. Quick4b7269valid/git7379d4pass/runtimed57678exit1emptyexpected. Fullebff2asession82706 then polla4df8b and FINAL5e5ba2 OBSERVEDexit0 source52716 available7120 links4214 broken0 allfalse. Normative0150 empty; no externalfulltexts fetched.\nMechanisms:Hostlocalhostresponseorigin;DoDproject/plotonauxclickeventXSSnotserverRCE;JNDIloggingvsOASTvsexecution;redir.u destinationnotATO;GETcompanydeleteobjectauthorizationreadback/credentialredaction;ExcelXLLprocessconsumerwithouttrustproof;errorUrlMobileTokenbountyhypothesis;Facebookoauthuseridtokenbinding;resetcodeemailbinding;encodedNULtemplateactualparser;OracleTNSreachabilityauthroledistinctions(nocredentialreuse);SoliditytransferFromignoredreturn/mockfalse/revert/NFTatomicity;autoSSRFgeneratedidentifiernotcallback;chatbotDOMclickcrossuser;MLWAFarchitecturevsmeasurablebehavior;accountremovalmailidempotencyboundedtesting;multisourceDNSIP/virtualhostShodanawkformat/provenance/templatescope;ffufmultikeywordmodebudget;FDNS_Astructuredhistoricaloutput;XSScontextlistinvalidjavas-space-cript;GitLabprivatemembershipnotbrokenauthorization;securitypolicydorksnotpermission;NewsletterHTMLescapeJSstringinnerHTMLsecondparse;POST/pathSQLboundedtruefalsebaseline;gitconfiglogsnotfullrepository;fileextensionconsumerimpactnotproof;largePHPlognotsameas10vulns;JWTalgorithm/keytype/JWKS/principal;OAuthredirect/state/scopebinding;APIauthschemenames/IPnotpermissions;CSPthirdparty/anewcompletebaseline;PHPfiltersflagsruntimeconsumer;paymentcurrencyamountunitserverquote;API404negativecase;FastlyPoCnotclaimability;JPEGmetadataactualMIME/DOMconsumer;publicZendeskJSsecretrevocationrole;inspectorDOMeditnotredirectproof;NLPtrainFilestraversaljoblogreadchain;Mattermostpersistedtemplatevsrun/resource/boundedlocalDoS;JSONpolymorphicSpringXMLlifecycleconditions(noexfilcmd);localWappalyzerCLI/fingerprintnotvulnerability;wordlistcountsnotcoverage;Adyennon401/400notkeyvalidityscopecritical;NuvolastaticPassRoleedgesvseffectivepermissions/denytrustSCP.\nNEXT0151/media0145 boundedprepare120max30000 (actualcounts authoritative), inventoryeachonce. Fullsavedbody/meaningfulaltsACTUALLYread thenallnewuniqueoriginalpixels<=6/callhash/timebeforeledger. Manuallysourceboundfacets/media precheck BEFOREappend. native/media/bodyrecordeachonce;quick/git/runtime;fullsameprocessuntilOBSERVEDexit0;exactfinish/Handoffprependhistory. Goalactiveuntilallrequiredcoveragecomplete. Storesdata0150/actual0150/notes0150/draft0150/reviewImageBatch0150/bodyReader0150/draftHelper0150/imageHelpers live; loadclonesalwaysstoreedits. Templatesbuild/precheck/native/finish0150. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135. No livehandlespending.\n\n"
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=22750,posts=23725,media=7143,facets=45,percent=pct,all_complete=False,goal='active',receipt=now)))
