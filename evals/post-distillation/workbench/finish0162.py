
"""Exact-once receipt after full verifier observed final exit0 session46160/3166d0."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==24670 and s['body_reviewed_posts']==25663 and s['remaining_body_groups']==26809
assert s['media_visually_reviewed_unique_contents']==8147 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==24670 and v['semantic_review_posts']==25663
assert v['local_markdown_links_checked']==4979 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==8124
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0162.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0162.json').read_text()) and len(fs)==73 and len({f for f,_,_ in fs})==26
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0162.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==92 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==165
actual=json.loads((W/'media-actual-0162.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==87
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0156' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0162' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0162_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0162_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=73,source_URLs_bound_to_batch=92,full_verifier_exit=0,full_verifier_session=46160,full_verifier_final_chunk='3166d0',full_source_hashes=52716,rendered_links=4979,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0162.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0162/media0156. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0162. Next0163/media0157.\nVerified24,670groups25,663posts48.68%; remaining26,809groups27,053posts total51,479groups52,716posts. Media8,147=4,682D2,165N1,300I; availableexternal8124 inline3/9 priorunavailable20 links4979 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missingimages/externalfulltexts covered nofetch/recovery/noinventreading; all savedbodies and currentlyavailable images remainrequired. Native standalone no source runtime dependency. RTK shell/no subagents/memorywrites/livecredentials/sourceexecution/install; preserve unrelatedchanges.\n0162 prepare05d3ac inventorya810fd160groups165posts36314chars first1623354665956933634 last1626082627072696321.96paths90unique3known87new174missingwaived. Fullsaved bodies1–60read1fffc1,61–120af76fb,121–160d50593.87neworiginalimagesSHA/time/manualnotes actual-0162.json. Known3metadataf07187:CookieBombDweb,bbFuzzingNthreepaths,encoded403baselineDweb. New87=60D23N4I.73facets26topics92URLs88mapped71corrected17merged72excluded. No waivedfulltextfetched;normative0162=[]; no freshstandardclaimed.\nPersist9e04ef/buildc4cdc0/precheck4459ba exactsource/filename bindingpassed. Native3ae897/media50561a/bodyf9ba10 ONCE. Quick37e052valid/git88f604exit0/runtime8a885aexpectedexit1empty. Full7bf6ea session46160 FINAL3166d0 OBSERVEDexit0 source52716 reviewed24670/25663 media8147 hashes8124 links4979broken0allfalse. Finish0162 receipt seeverification.json; final freshgit required.\nPrincipal0162 corrected boundaries: postMessage targetOrigin vs receiver origin/source and real tokenuse; 2FA localresponse vs serverprotectedaction; Nextcloud validateIPfail/downstreamaccept needsrealconsumer; emailnewline201image timestamp EARLIER than400 requiresID/login proof;403statuspathvariants !=sameprotectedresource; Nmap minratefloor andscriptbudget; Android AESproxy noMACproof/storageIPC consumers; CORSreflection/browserprivatecredentialedread; deletedpollretention needspolicytime; old8x8tenantdeactivate/removedusercookie/calendarOAuthinit/supportticket/invite actualACL/state distinct. All imageobservations boundexactpost/filename. Cover/status/promos excluded with fullbody ledger.\nNEXT0163/media0157 prepare160max40000 actualauthoritative ONCE then fullbodies/allneworiginalpixels<=6/callmanualnotes/returnedSHA/time. BuildprecheckBEFOREappend exactsource/filename; native/media/bodyONCE; quick/git/runtime/fullsameprocessOBSERVEDexit0;finishONCE/HANDOFFprependhistory. Helpers data0162/actual0162/notes0162/draft0162/reviewImageBatch0162/bodyReader0162/draftHelper0162/imageHelpers/counts0162/normative0162/checks0162 storeslive; loadclonesalwaysstore. Templatesbuild/precheck/native/finish0162. Memory424 actuallyread489545 thisgoalturn provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\n\n'
h=W/"HANDOFF.md";h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=24670,posts=25663,media=8147,facets=73,percent=pct,all_complete=False,goal="active",receipt=now)))
