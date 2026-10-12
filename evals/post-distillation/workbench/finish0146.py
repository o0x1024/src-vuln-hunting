
"""Exact-once receipt after full verifier observed final exit0 session24978/e1508e."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==22037 and s['body_reviewed_posts']==22995 and s['remaining_body_groups']==29442
assert s['media_visually_reviewed_unique_contents']==6771 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==22037 and v['semantic_review_posts']==22995
assert v['local_markdown_links_checked']==4003 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==6748
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0146.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0146.json').read_text()) and len(fs)==45 and len({f for f,_,_ in fs})==21
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0146.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==60 and all(pid in ids for pid in urls) and len(b)==120 and len(ids)==120
actual=json.loads((W/'media-actual-0146.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==67
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0140' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0146' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0146_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0146_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=45,source_URLs_bound_to_batch=60,full_verifier_exit=0,full_verifier_session=24978,full_verifier_final_chunk='e1508e',full_source_hashes=52716,rendered_links=4003,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0146.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix="CURRENT COMPLETED0146/media0140. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0146. Next0147/media0141.\nVerified22,037groups22,995posts43.62%; remaining29,442groups29,721posts; total51,479groups52,716posts. Media6,771=3,804D1,806N1,161I; source52716 availableext6748 inline3/9 priorunavailable20 local4003 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery/blocker. Native independent of archive/currentdir runtime. All shell rtk; no subagents/memorywrites/sourceexecution. Preserve unrelated targetchanges.\n0146 prepared3d09b/inventory2801e3 SUCCESS ONCE120groups120posts27388chars first1583747377151647746last1585903822291013632.69paths68unique1known67new133missingwaived. ALL120fullbodies actual03ef2d1–60/a15d1a61–120; meaningfulaltsread. ALL67originalimages actual0–66 <=6/call decoded returned binarySHA matched and realDate persisted beforeledger actual-0146.json.67manualnotes stored with explicit store after every batch (load clones, don't push withoutstore). No OCR inferred reviews.\n45facets21topics60URLs60mapped45corrected15merged60excluded;47D18N2I. Persist9e4d93;buildc7fb69/precheck15f1e7PASS all exactimagepostsource bindings. Native12c63c/media9339b1/bodyea76a5 SUCCESS ONCE. Quick973f7cvalid/git7100b1pass/runtimea0b7c3exit1emptyexpected. Fulla663b3session24978 then FINALe1508e observedexit0; source52716 available6748 links4003 broken0 allfalse. Normative0146 empty; no externalfulltexts fetched.\n0146 mechanisms: mobileclientvsserver/staticdynamicdirs;faviconhashownership;Githubextensionkeywords;installedjsonauthorvsadmin;uploadfiledecoder/consumer;VDPlearningbudget;alertpayloadcontext;Wordpressnormalroutes/sensitivefiles/actionsideeffects;reportautomationselfobjects/nobatchvictims;LFIparameterrealconsumer;404takeoverfalsepositive;UA/Referer/DELETE SQLsink;S3CXSSerdetectednotexecution;Jenkinsbuildpermission/templateunknown;recontoolsmethodologyprovenance;RFIreadvsremoteinclude;adminsourceJS/tokenpermissions;Flaskhtml.escape→formattedtemplate→render_template_string/JinjavsSQLmissing;emaildomainroletrust;Informativeemailaffectedprincipal;headlessJS/rolecoverage;cadvisor8080metricsvscontainercontrol;viewertokenbin/delete/versionauthorization;adminOwnerdisableboundary;SwaggerHTMLvsRXSS;communitycompilationscope;OTPlocalresponsevsserverprincipal;ACMEexistingadmin/configconsumers;httpxpathfilterscoverage;fixedcurrencybusinessdecision;SBOMprovidernoresults≠absence;EntropySourcefailurekeybuffer;llhttpemptyheaderLF/obsfold/multilineTErepairbytes;macOSbuildopensslpathsharedhostwrite;forwardIPheadersrateidentity;C2alreadyagentnotinitialRCE;Pingwindowsechoothernetmismatch;PassLockAESmenunotsecure;Waybacktimestampcurrentasset;Shopifyhistoricclaim/restore;crtshffufmultilines/errorsprogress;ViperSIDtaskstatusgraph;sedpathdictionaryloss;LFIpubliccacheheaderskeyproof;JolokiamimeTypeconsumer.\nNEXT0147/media0141 prepare count250maxchars65000 or bounded120maxchars30000 (actualcounts authoritative), inventory eachonce. Fullsavedbodies/meaningfulalts actualread then allcurrentnewuniqueoriginalpixels view<=6/call hash/time beforeledger. Manually sourceboundfacets/media precheck BEFOREappend. native/media/bodyrecord eachonce;quick/git/runtime;fullsameprocess untilobservedexit0;exactfinish/Handoffprependhistory. Goalactive until allrequiredcoverage complete. Stores data0146 actual0146 notes0146 draft0146 reviewImageBatch0146 bodyReader0146 draftHelper0146 imageHelpers live;load clones so always store edits. Templatesbuild/precheck/native/finish0146. Memory419/424–425 provenance01a11e72-23a9-7091-85bd-fb3171d2e135. Previousgoalturn0145progress (native+ledgerverified), current0146progress too. No livehandlespending afterfinish.\n\n"
h=W/'HANDOFF.md'; h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=22037,posts=22995,media=6771,facets=45,percent=pct,all_complete=False,goal='active',receipt=now)))
