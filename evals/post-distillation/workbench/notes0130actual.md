# 实际审阅记录 0130，尚未写入覆盖台账

0129已最终完成，绝不可重跑native0129/media/bodyrecord0129/finish0129。当前权威18,177组18,996篇36.03%，剩33,302组33,720篇，media4938=2757distilled1282nontech899insuff，links2995，allfalse。0129：native27cb85/media deb261/body fa9345；quick0117e4/git2b8edf/runtimec4f7e1；full78c614 session62171 FINAL bda61e exit0；finishc3dc6c。目标active无预算，未blocked/complete。

0130 prepare dc8f50 250groups253posts54,158chars，first1524108644857614340 last1528338331657977857。inventory266f7e 122paths118unique2known116new275missingwaived。正文全部实际读完：1-65 bfbe5b，66-130 89b33d，131-195 10386a；196-250在多输出exec曾整体截断，已单独完整重读41c161（以41c161为准）。有意义alt27来源信用说明/31波斯语题名/70genericprofile/133scannerascii/188bookmarks/203linkscraper均实际读到。不得声称尚未审阅的内容。

全部116新图片0-115原始像素已实际查看，20calls每6张最后2张。每张返回原始二进制用imageHelpers ownSHA256/base64解码匹配inventory，真实时间戳持久化actual-0130.json，在任何ledger之前；尚无media-actual0130、media/body specs、facets/native/build/precheck/finish0130及ledger追加。Functions stores data0130 {batch250,media116}、actual0130 length116、draft0130空{facets:[],bm:{},ms:{}}；draftHelper0130从0129只改stores名称（aliases内ldap为真实ldap-xpath）。imageHelpers存活。下一步手动按本记录提炼，再规范核验、precheck、每种追加一次、fullverifierfinal0、finish。恢复不要重复prepare/inventory，不必重复原像素；若丢store从actual文件恢复其真实时间戳。

## 图片人工观察（索引对应media-new-0130顺序）

0 g1 Burp advanced host/IP scope regex，没有host终结边界，domain.*、未转义点/方案片段可误包含相似域；当前规则不是许可，离线正反例核匹配。
1 g5 SpringShell logo nontech；2 g6直播广告 nontech；3 g8付款nontech；4 g16 Cydia欢迎页只有环境界面无ios步骤，insuff；5 g19非技术自助书封面nontech。
6 g22邮件计划修复/报价，未保存deleted-user动作，仅处理状态/影响不能由金额决定（可report方法或insuff）。
7 g26 ConfluenceCVE/P4报告titleinsuff，不把Jira/Confluence混同；8 g28Burp解析器repo题名insuff。
9/10 g31 Zabbix SAML/session/sign终端解码和生成输出、浏览器Cookie页面仍为登录logo，签名生成≠验证成功/权限，HttpOnlySecurecookie不解决签名绑定。不得copytoken或运行。
11 g32CVE triage/pending题名insuff。
12 g33emailverify ratelimit报告题名insuff；正文OTP+Host替代子域，无实际暴力结果，HEAD≠业务、同handler计数键/来源信任/范围，不bruteforce。
13 g34bugradar仓库题名insuff。
14 g36LSA SSP函数指针表，签名/地址≠调用上下文、转储或秘密产物；可source/desktop函数表可达性有限方法，未给完整插件逻辑。
15 g37Laravel issue题名insuff。
16 g38otp JSON数组候选，无响应；数组类型/验证/消费/计数单一请求≠单次验证，无通用bypass。
17 g41重置POST具有path code、Cookie、RequestVerificationToken、Email、Code、Password；请求标量换邮箱≠最终passchanged，token绑定subject+session+finalstate，不copysecret/email/pass。
18 g45AzureAD/Autologon/OnPremAD序列：KerberosTGT/ST/DesktopSSOToken交换；用户枚举/喷洒标题非实际成功。分身份、各消费者、令牌受众/条件，无认证结果。
19 g47完整二阶XSS宏：edit overwritesonlylastpayload，写URL1后顺序读URL2，postrequestmacro scope绑定tools/URL、finalresponse回传。实验每样本写-读-标记隔离，异步/身份/清理、反射≠执行，避免全部写后只读最后。
20 g48Critical500meme/statusinsuff；21 g51byp4xx输出POST200对localhosttest.html，CONNECT400TRACE405、其他无结果；方法变更/HEAD/curl follow与同action权限，200命令打印≠bypass。g50releasefeature命令可结合。
22 g52M2MclientIDsecret认证token再API返回图；clientsecret暴露不能称伪造签名或用户ATO，issuer/aud/scopes/principal。
23 g55faviconhasher URL→hash/date/icon/indexquery；共享icon/哈希碰撞/当前归属，不scopeinherit。
24 g56 SOAP GetMultipleChildren 实体token长序列化样式，Cookie、请求；小文本/截断限制，识别传输字段→实际deserialization consumer/gadgetversion notRCE，别copytoken。
25 g58rewardconfirmationinsuff；正文searchAuthorization用于secret分请求credential与响应泄露，不仅关键词。
26 g67Exceptional pendingtitleinsuff；27 g67Jenkins scriptconsole有限ls.execute.text目录输出，实际commandconsumer需身份/权限/环境，不把公开路径等于匿名；28 g67verifiedreply处理状态，可insuff或report方法不countRCEall。
29 g68Windowsprocessoverwrite PID/section/resume Done+dialog demo，阶段输出支持特定demo notEDR绕过/任意注入权限；不要执行。
30 g70subdomain工具coverinsuff。
31 g73IDORCritical两titleinsuff；32/33 g73reward邮件明确只可sharebounty其它detail需programoperator许可，资料提炼无发布动作，保留现有许可边界，不自动ask审批。
34 g74cloudshellmobiletool文件清单，文件存在≠安装、版本、quota/network/可执行，正文free/lifetime历史claim不做当前推荐，不安装工具。
35 g77LinkedIn宣传nontech。
36 g79fullratelimitlist：headersvariants/duplicateXFF、特殊字符、方法、更换token/cookie、reset解除、CAPTCHA去param；无实测。分来源信任计数key规范化、peraccount/global、success业务状态；100req不是必要或许可，不发100req，不bruteforce。
37 g82hiddeninputredirect表单/URL/javascript examples；hidden只是UI可编辑，不一定更弱；clientredirect vsHTTP Location消费者。
38 g83MLClogonont。
39 g84 BWASP UI预测SQL/XSS,URL和account/HttpOnlyXFO标记；predictable标签不是confirmation；实际响应/dataflow；可experiment/web方法。
40 g85ranknont。
41 g87polyglot图注释引号/comment、detailsopenontoggle、Unicodeconfirm+backticks，finitecontexts/CSP/event条件，notallcontexts。
42 g88NodeShieldlogo nont。
43 g89Shopify客户订单报告题名insuff；44 g90STOKvideocoverinsuff。
45 g93 nestedid/duplicateuser_id/query repeated→200；与g63正文重复键曲引号样例，RFC8259SHOULDunique implementations vary，终端对象/授权不由200判定。
46 g96reconbootrepoinsuff。
47 g97 fullpseudoDSL声明私有tools未发布/pathown易失败；passive工具→scopefilter→DNSbrute/TLScert/CNAME→filter→diff/merge→takeover→resolve/privateIPfilter→httpx→cutURLhostname→nonwebports。保留stagecontracts、canonical identity、passive/active/scope、privateaddresses exclusion要另计覆盖。
48 g97Discordnotif实际25activeunique/98resolved，notification stats≠allcoverage，不要送消息。
49 g97长log parsedvariables/rootoutscopecandidate、generatedUIDs、depends、implicitdefs、acceptedcommands、pyramidlevels0-11、executedsuccess throughlevel6 screenshotcrop；smalltextlimit；工具成功labels≠全部业务/levels11完成。
50 g98ASP.NET/config JSONmultipleDBConnectionStrings（部分commentdev、activeprod、localhost）/identityclientsecret/docdbkey；activevscomment/env/consumer/最小secret证据不copy/use；techwordlists路径≠实际secretendpoint。
51/52 g99sessionInfo/authUser字段及fetchJS片段；HttpOnly不阻止同源业务读取响应，跨origin fetch默认cookie/SOPcors前提；字段值≠reusabletoken/ATO；不copy。
53 g100storedXSScookiesillustrationnont（泛payloadline非具体场景）。
54 g104certnont；55 g109ATOtitleinsuff。
56 g112Oracle用户搜索FirstName a表username/fullname/email rows1-30；用户字段可见与readall/secretpass/current身份分开，部分redacted、不count1000deployments all。
57 g113celebrationmemenont。
58 g117Nuclei actualPOSTadminajax redirectparam，response200text/html carriesescapedJSONstring injectedtag，regexword/statuslabels；正文CVE1597 vsrepo/log1598不一致，严格sourceversions编号不等同；HTMLMIME/JSONescape/DOMcontext需真实解析，不由templatehit证明browserexecution。
59 g119OTPresponsemanip triagedmailinsuff；60 g119CRLFcontentinjection triage说明noXSSlow，可crlf/impact解释文本/HTML/header不同消费者；61 g119XFFOTPtriage明确初始需受害邮箱登录link，roleprereq影响与ratelimit计数，不能mosttimes无条件。
62 g120P3triagedassessedtitlesinsuff。
63 g123historicalURLpipeexcludeext/anew/grep=/urldedupe/gf/qsreplace/airixss，全参数/过滤lostpath，tagreflection≠browserexecution；mergeg60。
64 g124actualuncoversearch→httpx→template resultsOracleRegistration info lots lines，用户注册可用≠读取全部员工/密码；sourceprivacy/multipledeploydistinct/requests/output.
65 g131duplicatemailinsuff。
66 g133Running40m22URLs77params3Highlabels links noHTTPproof，runningnotfinished/labelsnotfindings；ASCIIalt实际读。
67 g146外链DependencyConfusion但图是Shodan448hits SSLscopepartcloudEC2HTTP200，图不支持dependencychain；index/currentservice/certrelation ownership分别记录。
68 g149whoisgreporg姓名/地址/mail butnoinetnum/cidrobject，正文 -h含scheme而图rawhost，organization textnotexactallocatednetblocks，少copyPII不用当前whois发请求。
69 g150bookcover/slide小缩略nont不readbookfull。
70 g157dompdf示意CSS→remotefontPHP→PDF→cacheaccess→RCE；needversion/config remotefetch/persist/executablecache/webservermapping，diagramnotactualexecution。Normative仅primarydocs，不fetchwaivedarticle全文。
71 g158SysmonGraph密集node color无legend/values可读，graphstructure alone no malicious attribution; insuff或records消费者/原events correlation有限方法。
72 g166electronresource repotitleinsuff。
73 g167webinaradvert nont。
74 g168FPMstatusfull pooluptime/acceptedconn/queue/processcount/currentGETURI/scriptpath (redacted)/duration；performance snapshot不是allroutes/DoS，disclosureauth/MIME/scope.
75 g169coursebasicsnont。
76 g175ShadowClonecloudLithops joblogsS3us-east1AWSLambda executor43activation status2%1/43，uploadsmallfunctions skip、startednotcompleted/results；cost/role/outputs，no cloudjobs.
77 g177Burp GET/etc/passwd200textplaintextrootuids/etc entries，file read vsinclude/execute notactualpasswordhash/x entries no plainsecrets；scopeauth/realfileconsumer unknown.
78 g181HPresolvedmailinsuff（文字thankslaptop，无机制）。
79 g185CyphGUIpromotionnont。
80 g186POSTapi/report?tokenandCookie,Origin google.com rawwithoutscheme, CORS ACAOgoogle.com creds true +collaboratorDNSAAAA; CORSheadnotbrowserallowedwithoutvalidorigin/cookie/read, DNS≠rebind/internalHTTP proof，不将标题三类合成证实链。
81 g187reward noemailrate limit150 titleinsuff正文captcha“allmethods”没实际验证。
82–85 g188 fullresourcebookmarkcategorieslinks(smallcrop) onlylinks notarticle mechanisms. insuff all，waived无需follow，没有独立方法自动扩写。
86 g192SQLMap storedsession resumedbooleanblind paramcariGET/MySQL(MariaDBfork)/2dbname partiallyredacted/otherterminalwp prefix entries；WordPress5.9.3coreSQLclaim不能从pluginparam/results版本推断，requestprovenance/resumedstale baseline actualdbnamesnotdumpfullrights。
87 g193testshellaspxprogram/args outputlocalaccountlist success；JS到RCEmissingchain，不补造ashxupload路径/initialidentity。
88 g194visibleJS hardcodedcomparepwd thenwindow.location home.php；clientcheck≠serverauth，不copypassword，后端直接入口测试ownedfixture only。
89 g198PlexGET userwithX-Plex-Tokenrequest→XMLuser/authToken/provider tokens/HttpOnlyCookie，redactedonlyprivacy；existingtokenrequired/returnconsumerpermission notanonymous/fromwaybackATO。
90 g201duplicatesXSS statusesinsuff。
91 g203SniffConUI crawled/internal/externalURLs lists/full alt；linkrelation !=brokenvalidation/clientAPIall/scope; preserve schemehost/crossdomain.
92 g204vAPIlogo nont。
93 g205ATOduplicatetitleinsuff，正文JSON分号无效 duplicateemail schema parse→recipient→token subject→finalstate结合g211/g130/g41。
94/95 g206feedbackandresolveduploadmail仅处理状态，insuff perhapsreportwholeprocess.
96 g207C2cartoonnont。
97 g213labadminaccountsecretlabel/hacked115/congrats; sandboxexerciseonlynoactualproductionATO；secret不copy。
98 g222Octopus listener0.0.0.0 /8088 host10.0.0.1 interval5pathlog.phpSSLfalse + generated file success；bind vs callback route/TLS/生成≠agentconnection perms，不execute。
99 g224talkcovernont。
100 g227cat /??c/p??wd actualshellglobbing→passwdtext；HTTPquery/JavafileRead API不会自动shellglob，图不能证明fileRead.jsp处理?。不要给recipe,区分shell expansion vsfile consumer.
101 g229blogpromo nont。
102 g230zero90daysreportsstatnont；103 g230High7.8misconfig2000 reportinsuff无mechanism。
104 g232 historical2021CWE25full ranks(score/trend/memorybounds/XSS/SQL/auth/secrets/SSRF等等)，useweaknessmechanism taxonomy != currentranking/instancesseverity/solewebonly。primarymitre ifexactuncertain，不fetcharchivefullsource userwaived，但标准分类可独立核.
105 g234httprobeportslarge/xlargecandidateenum；presetversionactualportsnotallprotocol/no live probes.
106 g236appreciationlettermedium wordinginsuff；107/108swagcupenvelopenont。
109 g237googleIPqueryfilter “ignoredsubsequentwords limit32” visible oldsearch warning；truncatedquery conditionsnotallapplied, IP appearance≠ownership/secrets/hiddeneveryasset。No currentGooglelimitgeneralclaim，需要绑定截图时间。
110 g241blocked-device accessesaccounttitleinsuff，device revocation server/session/refresh vslocalUI思路 limitednotconfirm.
111 g242templateOracleEbusinessLoginhighmatchendpoint only；112 samequery964Shodanhits candidatecountnot1000allconfirmed；merge112124106 validactualresultsnotCVES.
113 g244phisherlogonont noimpl。
114 g246httpx -statuscode-title grep '[2' output200lines；regexstructuredstatusfieldcompare/error/pathsoft404 andthreads/serviceidentity;200 != authsuccess不copytargets.
115 g250ARWADfullmindmap WhoisDNSacquisitionroots→active/passive subs→sortfilter→index/http/ports/takeover→content/github/alt/archive/js→fuzz/errors/dirs/template/extension/JSsinks。Diagramonly，不automaticallcoverage or execute;relationshipscope/dataflowtransform/loss/endfunctional matrix.

## 正文独立机制提示（250均已读）

1scope regex hostboundary。
14profile store-save-logout-login/otherconsumer roles persistentservervsbrowsercache。
17GNUparallel100 curlproxy -sk discardstdout requestmethodscopeTLS/limit noexecute，Burp捕获receipt≠all.
22deleteduser projectaccess disable superadmin lifecycle revocation/rolestate, screenshotno actions.
27passwordresetbugs只有intro/credit meaningfulalt，新图片没有这组（missingwaived或known2不需新view），仅题名excluded ifnoactualsavedalgorithm。
28BurpprojectexportJSON Audit/proxy/sitemap differentobjects truncation metadata/secret privacy/regexmatchnotall，toolpreviewonly.
30applicationmethodologytechprofiling/CVEmisconfigports/content/spiderJSparams stagedcoverage notguarantee可merge250.
31SAMLsignedsession token notauthconfirmed.
32Shodan facetgroup ranking searchresultsnotcurrentCVE.
33OTPHostaltbackend verifyexacthandler/login counters no bruteforce.
38otp array type;41/130/205/211resetpayloadtypes/tokenobject owner;53threadstep5missing earlier authmethod notinvent。
46SVG slash whitespace attributes仍含onload，“eventsblocked”需具体filter vsbrowser parser，no universalblockedpolicy.
47secondorder macro actualfullimage.
48count800 Critical500titlecontrasts impactnotquantity don't neednewfacet unlessbodycorrection useful.
49GraphQLbatch operationcountperrequest/executioncap/OTP peraccount across batches; no thousands live.
50/51toolsallnon-successcases finite.
52M2Mcredential exchangenotforging.
54top25paramnames toolonly paramsnotvulnconsumer;55faviconimage.
56serializedSOAPinput type/probe≠gadgets availability.
57router twoendpointXSStitle unsavedthreadwaived noactualimage currentnew maybeknown2 titleexcluded.
58Authorizationkeyword requestdefaultcredential vsresponse unintended vsvalidity.
60/123URLpipeentities &gt; vsraw image candidate.
63/93JSON duplicate parseRFC.
64redirectnamesconsumer notallvuln.
66disclosurepolicy question73imagefine.
67console actualcommandoutput limited.
74cloudshellbodyfree/lifetime noverifycurrentrecommend justhistoricalconstraint.
79ratelimitlist fullmanualimage.
82hiddeninputdom→actualrequestmethodconsumer。
84predictiveUI labels.
87polyglotgrammaticalfinite.
94transitionoutline focus alone onlyifendchanged/readactualevent noteverybrowserneedprimaryMDN.
95JSONtypedhtml HTMLparser/escaping actualserverMIME andbrowser differs malformedJSON no universalJSONXSS.
97DSLworkflow fullnotes.
98techspecificconfigsecret.
99HttpOnly/SOP sourcefieldconsumer.
102JSgrafana onlyexternaltitle canexclude.
107URIfragmentautofocus claim actualfocusable matchingID/notfragmentserverside primaryHTML.
110constructorconstructorpayload stringonlymatch reflection !=clienttemplate injection parsecalls.
112/106/124/242 Oraclequery+template/UI read schema mayberegistration legit vsunknownidentity.
114JWT-cracker brute force claim100K offlineentropy/keyformat algo notuniversalfast; no installedtool/docs externalwaived; decode!=validsignature/issuance.
117CVEid1597bodyvs1598repo/image inconsistent don'tnormcurrentCVEclaim.
1193tips images triage prerequisites/textinj corrected.
126/144/235Swagger configUrl externalresource/data toDOM execution version CSP auth scopes; fullarticlewaived, no runparams/URLs.
127dig argURLwrongdomain;CNAMEHTTP Host/SNI routebaseline ownershipnotinherited200。
132response302/403->200 localbypass UI vsserver authorizedstate actual subsequentcheckedstate.
133RunningHigh results.
142takeoversubjack filter grep -v Vulnerable outputinverts label/fileteeappendsoldnotclaimableall.
148auth/rate businessmap login/register/reset/email/feedback currentpolicy minimalcounts。
149WHOIS currentdata notalltargetCIDRs.
151Java gadgetprobe descriptionclasspaths remotequery/callbackcode availabilitynotRCE, noimplementationfullwaivedcanlimited.
152capturesOpenAPIobservedtraffic incomplete schema/security/role/function states infer!=declared exact contract.
157dompdfchain actualdiagram.
160/161PyScript octalescape printvsdisplay auto-render historicalruntime; Pythonlanguageoutput字符串!=HTML browser finalconsumer; no currentPyScriptguarantee.
163/16425SSRFnamedparams only10+5visible missing11-20 waivedunsavedthread noinvent; namesURLconsumer anddifferentredirectfileparameterlikeports.
165root “array” actuallynestedobject root schema notadminrole magically; same2IDs.
168FPMfullimage.
174redirectXSSpayload title missingimageswaived mayknownno mechanismexcluded.
177fileGET result limited.
179OOB6monthsrewardtitle alone no protocolsource evidenceexcluded.
182EJStags 1/3 missingnextsteps; tagsrenderdata vscompiletemplate separateconsumer no universally SSTI.
186CORS/DNS screenshotsplit.
188resources fulltitlesnotfollow.
191indexdorks productsports configrecursionlabels notcurrentcurrentprobe.
192Wordpressversion bodyvsGETcustomparam sqlmapresumed.
193 JS RCE externalarticlebutimageexecution notinitialchain.
194clienthardcode JSauthserver。
198 authenticatedtokens returned response notanonymousarchiveATO.
203 linkscraper internalexternal format.
204ownlabs mimicsAPI top10 completionnotproductionproof.
206reportedresolvedyearlater wait evidence actualretest notshown.
210 inventorythirdparty scopefreshownership.
211 emailmulti syntaxes distinct MIME andparser plusg205invalidsemicolon.
212HTTP methodsheaders classification labs actualproof notchecklist.
219browserinspect sufficienttoolchoice evidenceboundary titlegenericexclude.
222generatedlistenerfile≠activeclient.
225broadinternetlegalsillyidea scopecurrentlicense notworld.
227shellglob vsHTTPfilename.
230newprogramzero90daysstats no prooffirstreport.
232taxonomyweakness mechanisms optionalsourceimpact facetCWE25 many memorytypes notsoleweb.
234presetports;237IPsearch;241deviceblockedtitle only.
243rolesdocs forbidden baseline vsactual enforced serverstate.
245hashtags onlyexcluded.
246structuredstatus200 grep parsing.
250Recongraph wholeflows.

下一批afterfinal0130 expected totals18,427groups19,249posts(36.51%?),remaining33,052groups33,467posts,media5054,availableexternal5031,links2995+Nfacets。不要在0130提交前把这些预期计为完成。
