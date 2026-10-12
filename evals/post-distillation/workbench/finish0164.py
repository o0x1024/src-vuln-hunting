
"""Exact-once receipt after full verifier observed final exit0 session9227/87465d."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==24990 and s['body_reviewed_posts']==25985 and s['remaining_body_groups']==26489
assert s['media_visually_reviewed_unique_contents']==8328 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==24990 and v['semantic_review_posts']==25985
assert v['local_markdown_links_checked']==5103 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==8305
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0164.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0164.json').read_text()) and len(fs)==48 and len({f for f,_,_ in fs})==28
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0164.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==103 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==160
actual=json.loads((W/'media-actual-0164.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==87
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0158' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0164' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0164_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0164_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=48,source_URLs_bound_to_batch=103,full_verifier_exit=0,full_verifier_session=60861,full_verifier_final_chunk='87465d',full_source_hashes=52716,rendered_links=5103,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0164.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0164/media0158. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0164. Next0165/media0159.\nVerified24,990groups25,985posts49.29%; remaining26,489groups26,731posts total51,479groups52,716posts. Media8,328=4,788D2,210N1,330I; availableexternal8305 inline3/9 priorunavailable20 links5103 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missingimages/externalfulltexts covered nofetch/recovery/noinventreading; ALLsavedbodies/currentavailableimagesrequired. Native standalone no source runtime dependency. RTK/no subagents/memorywrites/livecredentials/sourceexecution/install; preserve unrelatedchanges.\n0164 prepare6f3186 inventoryac45d9 160groups160posts35123chars first1628372029715144704 last1630686057007050752.93paths92unique5known87new175missingwaived. ALLbodyread1–60 actual283ea7,61–1202e2e3b,121–160802884; excludedfullbodyrerereadad2d99. Known5metadata202c13. ALL87neworiginalreturnedSHA/time/manualnotes actual-0164.json. New87=47D18N22I.48facets28topics103URLs98mapped45corrected53merged62excluded. No waivedfulltext fetched;normative0164=[] no currentstandardverificationclaim.\nDrafte9b625/update01e5c0 build1d58b8 precheck8c4379 exactfilename/postURL pass. Native4f7a72/mediae226d8/body63353aONCE. Quickdfd12f valid/git eee9b8exit0/runtimea76bb3expected1empty. Full2d5928session60861 polled1eb413 confirmedlive thenFINAL87465d OBSERVEDexit0 52716sources24990groups25985posts8328media8305hashes5103links0brokenallfalse. Finishreceipt currentverification; freshgit required.\nPrincipal0164 corrections: DNSrebinding tworesponsesnotresolutiontiming; visualscanner syntaxnotcoverage; defaultcredversionconditions; SQLshortXORdialect/timecontrol; emailheadersnotarbitrarycode; S3listmetadata/publicJSnotsecrets/read/write; redirectUrl vsactualreturnUrl andcommahost; base64differentleadingpath43/200; Carnageattemptsnotexecution; JavaRandomconsoleclaimsneedgenerator/state/tokenconsumer/login; Splunkloggedinunknown; jsonspaces inheritedsettings historicalExpress >4.17.3 distinction; JWTeditor vsclaimsrender/signature/origin; AI companyrelationship/apps scope false; GraphQL introspection vsresolver/mailbinding; RFIremoteincludeconfig/oldnullbyte; Stripeacceptdiscountserialduplicate notnecessarilyrace; curl23916decompressenabled/multiheader and23914serial/23915parallel CLI notlibcurl; reportattachmentsvsserver/terminalexecution; Drupalinstall200/notpossibleinstallnotDoS/privilege; POSTXSSaccesskey/onclickinteractionanddomainWAF; CORSvalidorigin/browserreadcredentialresponse; WPloadscripts historicalresourcebound; PCAPGeoIPnotindividual; Nextcloudcronvsperreadexpiry/cache; .bashrcnotalwayshistory/.svnwcdbmetadataNOTallsource; NetlifyJiraregistrationnotpermissions; RPCevm_resetdestructiveonlylocal; session32hexNOTIDOR; APKHunthelpNOTscan; DockerHarborroles; XMLRPCthanksletterNOTSSRF; platformhistoricalscopeeligibilitydifferentassets/time. AllnewDimageboundfilename/post.\nNEXT0165/media0159 prepare160max40000ONCE thenactualALLcompletebodies/neworiginalimages<=6/callmanualnotes/returnedSHA/time. Build/precheckbeforeappend;native/media/bodyONCE;quick/git/runtime/fullsameprocessOBSERVEDexit0;finishONCE/HANDOFFprependhistory. Helpersdata0164/actual0164/notes0164/draft0164/reviewImageBatch0164/bodyReader0164/draftHelper0164/imageHelpers/counts0164/normative0164/checks0164 live;loadclonesalwaysstore. Templatesbuild/precheck/native/finish0164. Build0164template adapted overwrite guard for own derived preappend files; restore assertnotexists for newnative nextbatch. Finishtemplate ONEPASSregexstandaloneintegers. Memory424actuallyread1c5e23 provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\n\n'
h=W/"HANDOFF.md";h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=24990,posts=25985,media=8328,facets=48,percent=pct,all_complete=False,goal="active",receipt=now)))
