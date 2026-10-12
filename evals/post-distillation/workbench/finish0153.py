
"""Exact-once receipt after full verifier observed final exit0 session10413/14cec7."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==23230 and s['body_reviewed_posts']==24207 and s['remaining_body_groups']==28249
assert s['media_visually_reviewed_unique_contents']==7354 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==23230 and v['semantic_review_posts']==24207
assert v['local_markdown_links_checked']==4379 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==7331
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0153.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0153.json').read_text()) and len(fs)==44 and len({f for f,_,_ in fs})==25
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0153.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==56 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==161
actual=json.loads((W/'media-actual-0153.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==60
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0147' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0153' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0153_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0153_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=44,source_URLs_bound_to_batch=56,full_verifier_exit=0,full_verifier_session=10413,full_verifier_final_chunk='14cec7',full_source_hashes=52716,rendered_links=4379,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0153.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0153/media0147. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0153. Next0154/media0148.\nVerified23,230groups24,207posts45.92%; remaining28,249groups28,509posts; total51,479groups52,716posts. Media7,354=4,183D1,960N1,211I; availableexternal7331 inline3/9 priorunavailable20 links4379 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUserwaiver missingimages/externalfulltexts countcovered nofetch/recovery, no invented reading. Native standalone no source/currentdir runtime dependency. All shell rtk; no subagents/memorywrites/sourceexecution/livecredentialuse/install; preserve unrelatedchanges.\n0153 freshstate720064 confirmed0152final cf2bbe receipt. preparef4dc7e/inventory279f28 SUCCESS ONCE160groups161posts34841chars first1600776893892268032 last1603368351807307781.68paths66unique6known60new173missingwaived.\nALL160completebodies ACTUALLYread6195bc(1-60),26c8eb(61-120),197c82(121-160), meaningfulalts/trailingcaptionsincluded. ALL60newuniqueoriginalimages ACTUALLYviewed0-59 <=6/call returnedbinarySHA/time persisted actual-0153.json beforeledger;60manualnotesstoredaftereachbatch.\n44facets25topics56URLs55mapped44corrected11merged105excluded;34D17N9I. Persistd14bbd/script494054/builda7f1d9/precheck260648PASS exactpostURL/filename/targetbinding. Native96dc86/media56bb32/body531442SUCCESS EACH ONCE. Quickb50af8valid/git024a3cpass/runtime0f7462exit1emptyexpected. Full e34efe session10413 FINAL14cec7 OBSERVEDexit0 source52716 available7331 links4379 broken0 allfalse. Normative0153 empty; no externalarchivefulltext fetched.\nMechanisms:blockedfuzzscope/cost;localXSSfocusvsreflectederrortext;Slackblindcallbackprovenance;ParshuURLcandidatefilters;SQLunfiltered!=syntaxcontrol;OAuthCognitoIDORhypothesismatrix;ThinkPHProute/pearcmdprereqs(noexec);incrementalfeatures/directories;ShodanSimpleHTTPServer/Telnet/Citrix/Jenkins/wpconfigRDPnotpassword;CSRFformgeneratorbrowsercredentials(realrequestnothirdpartyupload);frontdisabledemailserverfieldauth;K8saggregatedAPIhijack/30Xeachhop(client/privilegeprereqs);RocketChatshellopenExternalplatform/config/existingXSS;GSIopensshconfigbanner(notgenericOpenSSH);AzureGraphexistingMSGraphidentity;IBMHTTPXXEcomponentCVEapplicability/notdirectothers;DNSnic/quotedloop/recordtypes/sharedIPscope;checklistArjunparameters/httprobe-notport/Katana-notarchive;emailregexABmatchnotvalidity;IFSglobactualshellconsumer;admin%20state!=permission;HTMLmixedtags/maparea/event/protocolentity(CSP/context);id=-1sentinellist/objectownership;Gitpathsmetadata!=fullsource/secrets;redirecturlURLSearchParamslocationhref;DoHcdbooleanmapping;Pythonuploadsavepathvsreadstrip/HTMLescape/customLogreloadprereq;Log4jpythonHTTPpath/shinputoutputerrors;botpreviouspermutationsprovenance;JSkeycandidatevscredentials;HRSrawbytes/connectionboundariesownfixture;Twittershortlink/BACregressionrewardbeforerepair;Markdownautolinkboundedcomplexity;AuthAnalyzerscopeunticked/SAMEpublicproductnotP1;templatereportversion/requestevidence;ActionscoreexportVariableGITHUBENVdelimiternotElectronruntime;DNSpharmingillustrationnotprovenrebinding;onclickentitysyntax/WAFcandidate;WPsetupwizardnotdatabasecreation;methodoverrideperlayer;NintendoRecommendedattributesnotadminOfficial;RailsSVGattributeReDOSboundedconfigs;Railsmathsvgstyle/selectstyleallconfigurationentrypoints/browserreparse;oldexperiencetime/provenance.\nNEXT0154/media0148 boundedprepare160max40000 actualcounts authoritative;prepare/inventoryONCE. Actualfullsavedbodies/meaningfulalts thenallnewuniqueoriginalpixels<=6/callbinarySHA/timebeforeledger; manualsourceboundfacets/media precheckBEFOREappend; native/media/bodyONCE;quick/git/runtime;fullsameprocessuntilOBSERVEDexit0;exactfinish/HANDOFF prependhistory. GoalactiveuntilALLrequiredcontentcovered. Storesdata0153/actual0153/notes0153/draft0153/reviewImageBatch0153/bodyReader0153/draftHelper0153/imageHelpers live. loadclonesalwaysstoreedits. Templatesbuild/precheck/native/finish0153. No livehandles. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\n\n'
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=23230,posts=24207,media=7354,facets=44,percent=pct,all_complete=False,goal='active',receipt=now)))
