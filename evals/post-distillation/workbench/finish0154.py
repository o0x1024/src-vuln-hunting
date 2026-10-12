
"""Exact-once receipt after full verifier observed final exit0 session47512/1e45bc."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==23390 and s['body_reviewed_posts']==24367 and s['remaining_body_groups']==28089
assert s['media_visually_reviewed_unique_contents']==7436 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==23390 and v['semantic_review_posts']==24367
assert v['local_markdown_links_checked']==4438 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==7413
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0154.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0154.json').read_text()) and len(fs)==59 and len({f for f,_,_ in fs})==23
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0154.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==78 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==160
actual=json.loads((W/'media-actual-0154.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==82
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0148' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0154' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0154_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0154_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=59,source_URLs_bound_to_batch=78,full_verifier_exit=0,full_verifier_session=47512,full_verifier_final_chunk='1e45bc',full_source_hashes=52716,rendered_links=4438,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0154.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0154/media0148. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0154. Next0155/media0149.\nVerified23,390groups24,367posts46.22%; remaining28,089groups28,349posts total51,479groups52,716posts. Media7,436=4,233D1,979N1,224I; availableexternal7413 inline3/9 priorunavailable20 links4438 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUserwaiver missingimages/externalfulltexts countcovered nofetch/recovery no invented reading. Native standalone no source/currentdir runtime dependency. All shell rtk; no subagents/memorywrites/sourceexecution/livecredentialuse/install preserve unrelatedchanges.\n0154 prepare0edbb0/inventoryb5959d SUCCESS ONCE160groups160posts36995chars first1603378320493711360 last1605578663956815874.88paths84unique2known82new172missingwaived. All160fullbodies ACTUALLYread5a0281/cbbcb9/f7a11a incl meaningfulalts/trailingcaptions. All82neworiginalimages ACTUALLYviewed0-81 SHAreturnedbinary/timeactual-0154.json;82manualnotes. Draftsourcebound59facets23topics78URLs74mapped56corrected18merged86excluded;50D19N13I. No normative/externalfulltext fetched.\nPersist57536e scripts5cd8e1 build9fae4c precheck488df7 PASS exactpostURL/filename/targetbinding; native161ee3 media dfab42 record3bd120 SUCCESS EACH ONCE. Quick5d6f6d valid git3893be pass runtime74e54f exit1emptyexpected. Full ecae4f session47512 FINAL1e45bc OBSERVEDexit0 source52716 avail7413 links4438 broken0 allfalse. Finish receipt below required exact once; no live handles.\nMechanisms:NTLMhandshakevsrelay;safeJSkeyloggerentryminimalmarker;randomsamplevsentropy/source;NETONsamplehashenv;multi-stage recon provenance/000vsHTTP/anewnotfullbaseline/slacknotproof;IBMclientIDvssecret;JKreadwriteoperationauth;featuredisablevsrewardfix;WPdebuglogactualnotLFI;AuthAnalyzerSAMEobjectpermission;Akismetwholetransportsecret;Angularactualcompileversion;SquarespaceunclaimedDNS/servicebinding;LFIpubliclistnotauth/file-read-include-exec;guardianemailsnapshot/relationshiptokenrevision;Azureexistingtokenpermissions;localhostfocusnotanyWAF;phoneextnormalizationidentity/OTPkey/multisink SSRFunproven;response302/adminbool/OTPMatchedvsbackend;ZAPcookieexistingidentity;CSRFmethod/anonymoustokencross-sessionrealbrowser/pushStatenooriginchange;OAuthdecodeURIeachhop;archiveHTMLisolation;XMLwrongnamespace/MIMEconsumer;filewordlistsactualcontent;AndroidsystemCAvsappTLS;user_oidcHTTPproviderconfigprivilege/Safarihtmlmetarefresh;UploadscannerHighCertainnotproof;selfXSSchainbridges;PHPInviteLinkrelationalbounds/missingparams/finitecounter/entropy;raceatomicquota/idempotentledger;delaySQLactualcontextboundedbaseline;JSregexcandidatesnotfullroutes;PHPSSRFfixedsubstrvsURLparse/nofollowassumption/GETbeforeisset/curloutput;archivalsecretvalidity;GoerrorJSONshapevsMIME;backuparchiveboundedreadonly;displaynamelengthSQLerrornotSQLi;gospiderpipelineformat/scope/failure;HTTPLootformsideeffects/concurrency/TLS;backticktabmixedcaseconsumer;POSThttpxsideeffects/redirect;Cloudmarefingerprint23%ipnotfound;resetRefererlinkgenerationvsclick/redeem;cmdpipelineUIDgrepnotcausality;SSRFmulti-consumerURLsurfaces;AIactuatorgeneratedpathsnotactual;largepayload408Pumaheadernotorigin;HRSrewardnotrawframes;TaxJarmembercancel/read/linkownrecoverable;stackwordlistsbudget;GrafanasnapshotkeypublicationexpectedCVEonlytitle;GoCloudsproviderfalsevsDNStimeout/ownership.\nNEXT0155/media0149 prepare160max40000 actualauthoritative;prepare/inventoryONCE. Bodiesfullsaved inclmeaningfulalts thenallneworiginalpixels<=6/callSHA/timebeforeledger. Humanfacet/media sourcepostURL/exactfilenameprecheckBEFOREappend;native/media/bodyONCE;quick/git/runtime/fullsameprocessOBSERVEDexit0;exactfinish/HANDOFFprependhistory. GoalactiveuntilALLrequiredcontentcovered. Storesdata0154/actual0154/notes0154/draft0154/reviewImageBatch0154/bodyReader0154/draftHelper0154/imageHelpers live; loadclonesalwaysstore. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\n\n'
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=23390,posts=24367,media=7436,facets=59,percent=pct,all_complete=False,goal='active',receipt=now)))
