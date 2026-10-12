
"""Exact-once receipt after full verifier observed final exit0 session4180/a42dff."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==22630 and s['body_reviewed_posts']==23604 and s['remaining_body_groups']==28849
assert s['media_visually_reviewed_unique_contents']==7086 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==22630 and v['semantic_review_posts']==23604
assert v['local_markdown_links_checked']==4169 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==7063
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0149.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0149.json').read_text()) and len(fs)==63 and len({f for f,_,_ in fs})==29
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0149.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==115 and all(pid in ids for pid in urls) and len(b)==200 and len(ids)==201
actual=json.loads((W/'media-actual-0149.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==122
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0143' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0149' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0149_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0149_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=63,source_URLs_bound_to_batch=115,full_verifier_exit=0,full_verifier_session=4180,full_verifier_final_chunk='a42dff',full_source_hashes=52716,rendered_links=4169,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0149.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0149/media0143. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0149. Next0150/media0144.\nVerified22,630groups23,604posts44.78%; remaining28,849groups29,112posts; total51,479groups52,716posts. Media7,086=4,016D1,895N1,175I; source52716 availableext7063 inline3/9 priorunavailable20 links4169 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missing images/external fulltexts counts covered; no fetch/recovery/blocker. Native independent of source/currentdir runtime. All shell rtk; no subagents/memorywrites/sourceexecution. Preserve unrelated targetchanges.\n0149 currentpriorstate51df0b;prepare52472e/inventory80f0b9 SUCCESSONCE200groups201posts46433chars first1590900000456081409last1593627593147879425.128paths126unique4known122new216missingwaived. ALL200fullbodies ACTUALLYread1d014e(1–60)/e4d459(61–120)/f94ca0(121–180)/8bf5a7(181–200); meaningfulaltsread. ALL122originalimages ACTUALLYviewed0–121 <=6/call returned binarySHA/time persisted beforeledger actual-0149.json.122manualnotes explicitlystored aftereachimagebatch. No OCR inferred reviews.\n63facets29topics115URLs114mapped62corrected52merged86excluded;77D43N2I. Persist7d665a;scriptbuild47fc67;build5dc4af/precheck64634e PASS exactimageposttargetsourcebindings. Nativec12713/media1b803e/body2fc051 SUCCESSONCE. Quick16311bvalid/git7f7072pass/runtimec3ca10exit1emptyexpected. Fullb868a7session4180 then poll9a83c1 and FINALa42dff OBSERVEDexit0; source52716 available7063 links4169 broken0 allfalse. Normative0149 empty; no externalfulltexts fetched.\nMechanisms: URLfilterloss/CSPXideloutputformat;TLD/policydorkscope;CORSoriginownershipnotcompletechain;OAuthconsentscopeaudience;prototypepollutioninherited/gadgeteval;Shodanalertprovenance;StrutsOGNLactualconsumer/classpath;pathnormalizefrontendbackend;templatevsHTMLcontext;FFUFrawlogsANSI;SQLkeyword/encoding/timing;SBOMreachability;jQueryversionnotPoC;XSSparams/base64/taggedtemplate/redirectURI;Web3ABIblockcontext;zipwrapperinclude;uploadMIMEPUTinterpreter;regexblacklistHTMLscript;selfXSScachedeception;businessmodel/browserproxy/lowreslimits;ClearbitAlgoliaZeroBouncesecretACL;IPorgShodansharedscope;Cookie/2FAlifecycleRESTSOAP;emailseparatorarrayaccountvsdelivery;backupWPpathdictionary;S3CNAME/claimvsYelptemplate;privateenumscriptdependencies/rangeloss;x8reflection/regexfuzzbudget;HTTPconnectionpoolauthority/frames;ReverseSSHInspectorinitialpermission;CI/CDisolatedlab;Redditduplicateemailroleshiddenmembership;redirecthostunescapeddot;SDRofflineframecandidates;WiFihostaptestenvironment;Katananucleiappend/templateevidence;OAuthstateloginredirect;reportstatusdefinitions;resolverupdateatomic;TLSfingerprintsameapplicationrequest;browserDNSrebindprereqs;SOQLactualquery;XXEencodingparserconsistency;HostblindHTMLconsumer;NTLMmetadatanotpassword;shadowdeleteisdestroyingrecoverynotEDRtest;Sawyerhashmethodtypeboundary;deploykeycontextfields;DOMPurifydata-disable-withRails-ujssecondHTML;contactsquickcmdrender;resetuserinfoenumerationvstoken;WARPtrustedSSIDCLIpolicy;eBPFdefensivecomponentsnotimplant;Prefetchhashpath/MemoryDumpintegrity;creatorreadvsrolewrite;SVNBridgememcachedneedsSSRFcontrolledbytes;CSRFheaderGETrealbrowserstate;CPDoSsharedcachekey;XSSscalefilterandskippedmining;defaultcredentialserverprincipal;directoryopensourcevssecrets/scriptPII;PowerHubexistingexec/moduletrust(noAMSIrecipe);phishingarchitectureeventlabeldefense(noemails/payloaddeployment);signaturenamevsvalidchain.\nNEXT0150/media0144 boundedprepare200max48000 (actualcounts authoritative), inventoryeachonce. Fullsavedbody/meaningfulaltsACTUALLYread thenallnewuniqueoriginalpixels<=6/callhash/timebeforeledger. Manuallysourceboundfacets/media precheck BEFOREappend. native/media/bodyrecordeachonce;quick/git/runtime;fullsameprocessuntilOBSERVEDexit0;exactfinish/Handoffprependhistory. Goalactiveuntilallrequiredcoveragecomplete. Storesdata0149/actual0149/notes0149/draft0149/reviewImageBatch0149/bodyReader0149/draftHelper0149/imageHelpers live; loadclonesalwaysstoreedits. Templatesbuild/precheck/native/finish0149. Memory424 provenance01a11e72-23a9-7091-85bd-fb3171d2e135. No livehandlespending.\n\n\n'
h=W/'HANDOFF.md';h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=22630,posts=23604,media=7086,facets=63,percent=pct,all_complete=False,goal='active',receipt=now)))
