
"""Exact-once receipt after full verifier observed final exit0 session9227/97d923."""
import ast,json,re
from datetime import datetime,timezone
from recover import T,A,W
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==24830 and s['body_reviewed_posts']==25825 and s['remaining_body_groups']==26649
assert s['media_visually_reviewed_unique_contents']==8241 and s['body_followup_groups']==0 and not s['all_posts_content_distilled']
assert v['raw_source_documents_hash_verified']==52716 and v['semantic_review_groups']==24830 and v['semantic_review_posts']==25825
assert v['local_markdown_links_checked']==5055 and v['broken_local_markdown_links']==0 and not v['all_posts_complete']
assert v['reviewed_media_hashes_reverified']==8218
fs=next(ast.literal_eval(n.value) for n in ast.parse((W/'native0163.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
assert fs==json.loads((W/'facets0163.json').read_text()) and len(fs)==76 and len({f for f,_,_ in fs})==29
c=(T/'references/research/community-distillation.md').read_text()
for f,title,body in fs:
 txt=(T/'references'/f).read_text()
 assert txt.count('## '+title)==1 and txt.count(body)==1 and c.count('| '+title+' |')==1,(f,title)
b=json.loads((W/'batch-0163.json').read_text());ids={pid for r in b for pid in r['post_ids']}
urls=[pid for _,_,body in fs for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==100 and all(pid in ids for pid in urls) and len(b)==160 and len(ids)==162
actual=json.loads((W/'media-actual-0163.json').read_text());media=[json.loads(l) for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()]
assert len(actual)==94
for r in actual:
 matches=[m for m in media if m['sha256']==r['sha256']]
 assert len(matches)==1 and matches[0]['batch']=='media-0157' and matches[0]['reviewed_at']==r['viewed_at']
reviews=[json.loads(l) for l in (A/'reviews.jsonl').read_text().splitlines() if l.strip()]
for r in b:
 matches=[m for m in reviews if m['body_sha256']==r['body_sha256']]
 assert len(matches)==1 and matches[0]['batch']=='batch-0163' and set(matches[0]['post_ids'])==set(r['post_ids'])
assert 'batch0163_final_checks' not in v
now=datetime.now(timezone.utc).isoformat()
v['batch0163_final_checks']=dict(checked_at=now,quick_validate='valid',git_diff_check='passed',runtime_source_dependency_scan='no_matches',native_facets_exactly_saved=76,source_URLs_bound_to_batch=100,full_verifier_exit=0,full_verifier_session=9227,full_verifier_final_chunk='97d923',full_source_hashes=52716,rendered_links=5055,broken_links=0,user_waiver_missing_and_external='count_as_covered',primary_normative_read=json.loads((W/'normative0163.json').read_text()),no_waived_archive_fulltexts_fetched=True)
for k in ['static_skill_validation_verified_at','git_diff_whitespace_verified_at','runtime_source_dependency_verified_at','skill_quick_validation_at','git_diff_whitespace_check_at','runtime_source_dependency_check_at']:v[k]=now
(A/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
pct=round(100*s['body_reviewed_posts']/s['total_posts'],2)

prefix='CURRENT COMPLETED0163/media0157. ACTIVE unbudgeted goal 完成所有posts内容的提炼; allfalse. NEVER rerun successful native/media/record/finish0163. Next0164/media0158.\nVerified24,830groups25,825posts48.99%; remaining26,649groups26,891posts total51,479groups52,716posts. Media8,241=4,741D2,192N1,308I; availableexternal8218 inline3/9 priorunavailable20 links5055 broken0. Canonicalc3ba1c34b72295375ce4a5287ee3cc1b3a449702292fd40f2424f41fd78b6520.\nUser waiver missingimages/externalfulltexts covered nofetch/recovery/noinventreading; all savedbodies/currentavailableimagesrequired. Native standalone no source runtime dependency. RTK/no subagents/memorywrites/livecredentials/sourceexecution/install; preserve unrelatedchanges.\n0163 prepare2242ac inventory47d50e160groups162posts36938chars first1626101045028966402 last1628365035201351681.101paths100unique6known94new182missingwaived. Completebodyread1–60actual07b68e,61–120922adf,121–1603ddaf3 untruncated. Known6metadata129d30 exacthash priorD resetURL/auth; duplicatecompanyID/access;suResetPwd/auth/access/source/scope;visualRecon/records/passive;ASPHPP/waf/xss;redirectconsumerdiagram/redirect/xss/web/source. ALL94neworiginalreturnedSHA/time/manualnotes actual-0163.json. New94=59D27N8I.76facets29topics100URLs97mapped73corrected24merged63excluded. No waivedfulltextfetched;normative0163=[] no freshcurrentstandardclaim.\nDraftpersist4fc8f0/adapt25e11c/buildf81c60/precheck3bade1 pass exactfilename/postURL. Native6918b8/media d83b3f/body960722ONCE. Quickc96a90valid/git10caddexit0/runtime49346bexpected1empty. Fullff7d24session9227 polleded05ec confirmedlive thenFINAL97d923 OBSERVEDexit0 52716sources24830groups25825posts8241media8218hashes5055links0brokenallfalse. Finishreceipt currentverification; freshgitrequired.\nPrincipal0163 corrections: .ftpconfigactualcombinedJSnoFTP;S3claimlegacyconsumer/controlseparate;curlHSTSserial/parallelcachedstateshistorical;serviceaccountJWTcode literalinterpolation/unawaitedPromise andIAM;RocketChate2e.updateGroupKeymember/recipient/keybinding;stagepayment/prodproof;XFFtrustedproxy/OTPcount;PhpMyAdminhtaccessAuthNamepromptnotsecret/setupscope;codeplaygroundexecutionneedsandboxboundary;S3read/list/writeindependent;usernameapprovalmassassignment;GitLabordinary/scopedcolorimportdummyAPI+Premium+CSPactualsink;NodeOpenSSLerrorstackfailuretournJWTsignfailnotforgery;prototypegadgetsource/inheritedread/shell,PPFinderundefinedreadandFastifyordinaryfieldmarkerinsufficient;SQLdialect/column/delay;emailverifiedqualificationserver;AIproductlistsnotownership/currentdownload;netcatHTTPbyte/EOF;JWTnotautomaticallyencrypted;SSTInumericMRO/subclassnotuniversal. AllnewDimageexactboundfilename/source. Cover/status/promos excluded with actualbodyledger.\nNEXT0164/media0158 prepare160max40000ONCE thenactualcompletebodies/allneworiginalpixels<=6/callmanualnotes/returnedSHA/time. Build/precheckbeforeappend;native/media/bodyONCE;quick/git/runtime/fullsameprocessOBSERVEDexit0;finishONCE/HANDOFFprependhistory. Helpersdata0163/actual0163/notes0163/draft0163/reviewImageBatch0163/bodyReader0163/draftHelper0163/imageHelpers/counts0163/normative0163/checks0163 live;loadclonesalwaysstore. Templatesbuild/precheck/native/finish0163. FinishtemplateintegerreplacementuseONEPASSregexstandaloneintegers avoidingpreviousbroad ==26 matching25663 etc. Memory424/429actuallyread8006ad provenance01a11e72-23a9-7091-85bd-fb3171d2e135.\n\n'
h=W/"HANDOFF.md";h.write_text(prefix+h.read_text())
print(json.dumps(dict(groups=24830,posts=25825,media=8241,facets=76,percent=pct,all_complete=False,goal="active",receipt=now)))
