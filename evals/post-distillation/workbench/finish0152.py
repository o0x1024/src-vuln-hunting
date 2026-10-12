
"""Exact-once receipt after full verifier observed final exit0 session52823/8b724b."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==23070 and s['body_reviewed_posts']==24046 and s['remaining_body_groups']==28409
assert s['media_visually_reviewed_unique_contents']==7294 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==23070 and v['semantic_review_posts']==24046
assert v['local_markdown_links_checked']==4335 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==7271
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0152.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0152.json').read_text()) and len(fs)==61 and len({f for f,_,_ in fs})==25
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0152.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==76 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==161
actual=json.loads((W/'media-actual-0152.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==69
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0146' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0152' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0152_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0152_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=61,source_URLs_bound_to_batch=76,full_verifier_exit=0,full_verifier_session=52823,full_verifier_final_chunk='8b724b',full_source_hashes=52716,rendered_links=4335,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0152.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix=("CURRENT COMPLETED0152/media0146. ACTIVE goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0152. Next0153/media0147.\n"
"Verified23,070groups24,046posts45.61%; remaining28,409groups28,670posts total51,479groups52,716posts. Media7,294=4,149D1,943N1,202I; availableexternal7271 inline3/9 priorunavailable20 links4335 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\n"
"Userwaiver missingimages/externalfulltexts covered nofetch/recovery; standalone native no runtime source/currentdir dependency. All shell rtk; no subagents/memorywrites/sourceexecution/livecredentialuse/install; preserve unrelatedchanges.\n"
"0152 prepare7b6f69/inventory1019c2 SUCCESSONCE160groups161posts33929chars first1598132177580937222 last1600694228438614016.73paths72unique3known69new165missingwaived. All160fullbodies ACTUALLYread abebf5(1-60)/467900(61-120)/67cb7b(121-160), meaningfulalts/trailingcaptions included. ALL69 originalimages ACTUALLYviewed0-68 <=6/call binarySHA/time persisted actual-0152.json beforeledger,69manualnotes.\n"
"61facets25topics76URLs73mapped59corrected14merged87excluded;41D14N14I. Persist09b41c scriptd1b40f build9b72cf precheckad5818. First nativecead1a failed countassert beforemutation; fixed inherited URLguard13f7e5 and precheck9b3604 pass. Native72eb39/media39e93f/body108cd2 SUCCESS EACH ONCE. Quick25e0e2valid/git81820apass/runtimecc2a70exit1emptyexpected. Full1dd297session52823 thenFINAL8b724b OBSERVEDexit0 source52716 available7271 links4335 broken0 allfalse. Normative0152 empty/no externalfulltexts fetched.\n"
"Mechanisms:adminforcedbrowse/serverreadback;Firebaseconfigvsrules;Airflownextnormalization;VCSprompt2ndparse;teamownership/memberremoval;nationalIDobjectmatrix;XSScontext/event/POSTdelivery;headerPOSTSQLdelaycausalbaseline(notdifferentURLs);gauunfurlvariables/structures;commandobfuscationactualshellconsumer;filenamedecoding/storagehandler;pipelineIOcontract;OAuthcallbackstate/delivery;GApostMessageorigin/schema/cookiescope;takeover404/currentbinding;AICVSScorrection;Googleunlinkderivedsessions;richtextpolicy/save-render;clickjackingcriticalaction;TinyFileManagerdefaultdeployment;SSRFIPdoesntexpandscope;Swaggerurl/localversion;httpxCSVfields/errors;curlPUToPOSThandlereuse(noCLI,UAFunproven);Cortexpprof/configauthentication(noDoS);plan/giftentitlementreadback;.netrcEOFboundedparser;secondarycontextnormalization;AIGoerrors/regexnotXSS;WPQueryentry/SQLerror;Gravatarhashprivacy;SVGnewlineexecutionpercontext;programstatsnotauthorization;sensitivefilevscredentials;workflownegativeevidence;desktopAPIserverprincipal;Nucleioldglobnotfindings;EvilTreehits;401to200clientvsbackend;programclosure/reportstate;AirflowBasicdefaultconfig;GETdeleteSQLparameterizationnotCSRF/XFOmeta;scanner000/HTTPstate;naabuNSEcostandexclusions;gospiderqsreplaceencodedcandidateonly;AISolidityproviderpool/assetconstraints;destructivepostcorrection;1xxintermediates;multiauthrole/object;TikTokSellerpermissionwrite;AtlantisUIvsPRexecution;archivedSQLtextnotcurrentinjection;Pylirtlocalsudo/passwdnotpassword;LinkedInrecruiterresumeobjectnotanonymous;Nodeinspectinvalid-octalDNSpremises;IPHostSNIauth;SonyerrorSQLminproof(noDBenumeration).\n"
"Next bounded160max40000prepare/inventoryeachonce; ACTUALLYread savedcompletebody/meaningfulalts; visuallyviewallnewuniqueoriginalimages <=6/call binarySHA/time beforeledger. Facets/manualmediabindexactpostURL/filename/target precheck beforeappend. native/media/bodyonce;quick/git/runtime;fullsameprocessuntilOBSERVEDfinalexit0;exactfinish/HANDOFF prepend. Goal active until ALL required coveragecomplete. Storesdata0152/actual0152/notes0152/draft0152/reviewImageBatch0152/bodyReader0152/draftHelper0152/imageHelpers live; loadclonesstoreedits. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135. No livehandles.\n\n")
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=23070,posts=24046,media=7294,facets=61,percent=pct,all_complete=False,goal='active',receipt=now)))
