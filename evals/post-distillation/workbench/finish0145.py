
"""Exact-once receipt after full verifier observed final exit0 session37893/beed43."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==21917 and s['body_reviewed_posts']==22875 and s['remaining_body_groups']==29562
assert s['media_visually_reviewed_unique_contents']==6704 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==21917 and v['semantic_review_posts']==22875
assert v['local_markdown_links_checked']==3958 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==6681
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0145.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0145.json').read_text()) and len(fs)==50 and len({f for f,_,_ in fs})==27
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0145.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==65 and all(pid in ids for pid in urls) and len(b)==120 and len(ids)==125
actual=json.loads((W/'media-actual-0145.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==79
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0139' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0145' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0145_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0145_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=50,source_URLs_bound_to_batch=65,full_verifier_exit=0,full_verifier_session=37893,full_verifier_final_chunk='beed43',full_source_hashes=52716,rendered_links=3958,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0145.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0145/media0139. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0145. Next0146/media0140.\nVerified21,917groups22,875posts43.39%; remaining29,562groups29,841posts; total51,479groups52,716posts. Media6,704=3,757D1,788N1,159I; source52716 availableext6681 inline3/9 priorunavailable20 local3958 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery/blocker. Native independent of archive/currentdir runtime. All shell rtk; no subagents/memorywrites/sourceexecution. Preserve unrelated targetchanges.\n0145 prepare147081/inventory853b69 SUCCESS ONCE120groups125posts26903chars first1581981467130724352last1583718604142362624.89paths80unique1known79new139missingwaived. ALL120fullbodies actualdf14c81–60/e0735861–120; meaningfulaltsread. ALL79originalimages actual0–78 <=6/call returned binarySHA validated and realDate persisted beforeledger actual-0145.json. Notes79 were rebuilt manually from actually viewed semantics after noticing store clone means load(notes).push did not persist; final notes0145.json true79manual observations. No fake OCR verdicts.\n50facets27topics65URLs63mapped49corrected14merged57excluded;58D17N4I. Persistd7506c;buildc380f6/precheckb8d03cPASS all exactimagepostsource bindings. Native270cff/media457028/body969b43 SUCCESS ONCE. Quick195c77valid/git73e47apass/runtime35c9e2exit1emptyexpected. Full4cf9dfsession37893 then FINALbeed43 observedexit0; source52716 available6681 links3958 broken0 allfalse. Normative0145 empty; no externalfulltexts fetched.\n0145 mechanisms: queueframingresponse identity;Go CookieRole/XFFtrust/errornil;Linuxexistingprincipal/PATHconsumers;CRLFdecode/headers;ASPduplicatecomma/WAF/dynamicloader;originIPHostSNI/pathas-isrepair;utmCSSanimationcontext;DNSclaimtimeline;learningauthorizedlabs;KunyuCDNpipelinepassivevsactivebudget;Host403/400/127200JSONrouting;readObjectbeforecast;404DOMvsreflection;filetoken downloadpolicy;emptydeptmanagement;helpdeskfounder/adminlogobjectpermissions;APIpublicdate/PII/TomcatexampleIP;oldfixregressionversion;GraphQLschema≠SQL;vulnerabledepactualreachability;Whoisownershiplimits;ZAPOASTattribution;GUIDtime/tokenbinding;Swaggerrole/downstreammail;currencyquote/settlement;TaxJartokenvsURLidmixedsummaries;localgRPCListenprerequisite;Smokescreenbracketparser;memberinviteadminroles;historicalHOFrewardrules;InviteCSRFbrowservsaccept;removedcommentmessagepermissions;PTracesourcetoassembly;uploadAuthorization/readbackbeforeoverwrite;beginner/scannerduplicatebias;WOTwgetnotanonymous;301%22SQLerror/tamper;Indypackagecompose→shellauth;restrictedglob/context;Tor/timingnetworkcausality;businessinvariants;DatastudioReportIDsharepolicy;localresponsevsserverstate;Krisptrialvspermanent;Trickestpipelinequeues;PHPfilterinclude/encoding;PartyLoudnoiseexperiment;resourceindexnotreading;automationstoragecuratednotifications;cooperation/learningnotrevenuepromise.\nNEXT0146/media0140 prepare count250maxchars65000 or boundedcount120maxchars30000, actual result count matters; inventory eachonce. Fullsavedbody/meaningfulalt actualread then allcurrentnewuniqueoriginalpixels view <=6/call hash/time beforeledger. Manually sourceboundfacets/media then precheck beforeappend. native/media/bodyrecord eachonce;quick/git/runtime;fullsameprocess untilobservedexit0;exactfinish/Handoffprependhistory. Goalactive until allrequiredcoverage complete. Stores data0145 actual0145 notes0145 draft0145 reviewImageBatch0145 bodyReader0145 draftHelper0145 imageHelpers live;load clones so always store edits. Templatesbuild/precheck/native/finish0145. Memory419/424–425 provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\n\n'
h=W/'HANDOFF.md'; h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=21917,posts=22875,media=6704,facets=50,percent=pct,all_complete=False,goal='active',receipt=now)))
