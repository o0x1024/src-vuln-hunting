"""Checkpoint actual review, not completed distillation or ledger append."""
import json
from recover import W,A,S,digest
a=json.loads((W/'actual-0130.json').read_text())
m=json.loads((W/'media-new-0130.json').read_text())
b=json.loads((W/'batch-0130.json').read_text())
assert len(a)==116 and len({r['sha256'] for r in a})==116
assert [(r['name'],r['sha256']) for r in a]==[(r['name'],r['sha256']) for r in m]
known={json.loads(l)['sha256'] for l in (A/'media-reviews.jsonl').read_text().splitlines() if l.strip()}
for r in a:
 assert r['detail']=='original' and r['viewed_at'] and r['sha256'] not in known
 assert digest((S/'media'/r['name']).read_bytes())==r['sha256']
s=json.loads((A/'status.json').read_text());v=json.loads((A/'verification.json').read_text())
assert s['body_reviewed_groups']==18177 and s['body_reviewed_posts']==18996 and s['media_visually_reviewed_unique_contents']==4938
assert v['batch0129_final_checks']['full_verifier_exit']==0
assert len(b)==250 and sum(len(r['post_ids']) for r in b)==253
prefix='''CURRENT PENDING0130 AFTER COMPLETED0129. Active goal unbudgeted 完成所有posts内容的提炼. Authoritative0129 remains18,177groups18,996posts36.03%, remaining33,302groups33,720posts,4938media,2995links,allfalse. NEVER rerun native0129/media/bodyrecord0129/finish0129. 0129finishc3dc6c full78c614session62171 FINALbda61e observedexit0 quick0117e4valid/git2b8edfpass/runtimec4f7e1nohits.

NEXT finish ALREADY-PREPARED0130/media0124, NOTprepare/inventoryagain. Prepare dc8f50 250groups253posts54,158chars; inventory266f7e122paths118unique2known116new275missingwaived. All250completebodies ACTUALread bfbe5b1-65/89b33d66-130/10386a131-195/41c161196-250;41c161 intentionally reread after global output truncation. Meaningfulalts27/31/70/133/188/203read. All116 NEWoriginalpixels0-115 ACTUALLYVIEWED20calls6/calllast2. OwnSHA256decodedbinarymatched each inventoryhash; actual-0130.json all116 persisted BEFOREanyledger. Disk notes0130actual.md contains detailed human observations for ALL116images and relevantbody mechanisms, including sourcegroupbindings/limits. Can use without repeat pixelviews. Functions data0130/actual0130/draft0130(empty)/draftHelper0130/imageHelpers persistent; from disk recover if needed. No facets/spec/native/build/precheck/media-actual0130 or ledger additions0130 YET. Do NOT count253or116 ascompleted until native+ledger+verifier.

NEXT manualdraft about65-85facets/25-32topics from fullsavedtext+actualimage observations, exactsourceIDs. Distill evidence/mechanisms notauto keywordcategories; titles/bookmarklinks/promos canexcluded covered. Relevantprimarynormativeread separately onlyofficialdocs (SOP/HttpOnly/cookie, JSONdupRFC, HTMLfragmentfocus/transition, Pythonoctalescape/displayruntime, FPMstatus/CWE taxonomy/EJS data-vscompile) asneeded; neverretrieve waived archivearticlefulltext/repos/videos. Preserve secrets and PII: no copying credentials, token/sessionbytes, signedURL secrets, no use/sourceexecution/livehandles/installs/subagents/memorywrites. User缺失图片、外链全文 不用管，按已覆盖算 remains. Standalone targetruntime; preserve unrelated changes. Allshellprefixrtk. Buildrename TEMPLATE metadata before inserting facets+sourceIDs. Precheck exactgroups250posts253media116; eachdistilledimage'sownpostID innativecorrespondingtopic. Native/media(media-0124)/body eachonce sequential; staticquick/git/runtime PromiseallSettledinspectall; fullverifier SAMEhandle observedFINALexit0; exactonce finish/HANDOFFprepend preservehistory. Nevercomplete untilfullscope0remaining,currentavailablemedia/native/integrityproven. Safe0129templates. stage.pybookkeeping/recoverconstantshelpers only neverrecovermain. No processespending.

Memoryactual424-425prior68b769 coverageboundary; finalcitationMEMORY424-425 rollout01a11e72-23a9-7091-85bd-fb3171d2e135. RTK32ef69actualcurrentread. Full0129primarydocs actual396-399; citations preserved in native0129 facets. notes0130actual is reviewcheckpoint, not skillruntime or completedcoverage.

'''
h=W/'HANDOFF.md'
assert not h.read_text().startswith('CURRENT PENDING0130 AFTER COMPLETED0129.')
h.write_text(prefix+h.read_text())
print(json.dumps(dict(authoritative_posts=18996,pending_body_groups=250,pending_posts=253,actually_viewed_pending_images=116,native_pending=True,goal='active',all_complete=False)))
