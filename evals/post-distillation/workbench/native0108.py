"""Append manually distilled0108 facets after precheck. Own helper only."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "by-type/jwt.md",
    "JWT声明生成与验证入口的类型和时间合同",
    "jwtXploiter帮助图列None、HS256、RS256、键文件、声明数值/字符串默认处理、iat/exp/nbf增减及独立verify/find-key选项。帮助参数仅描述工具能力。\n\n把原始令牌、实际算法白名单、验证密钥类型、声明类型、时间基准与服务端最终身份绑定；构造输出与服务端接受分别记录。仅解码、生成成功、时间类型不符或验证仍拒绝是反例，不运行密钥暴力搜索。\n\n来源：[保存帖1](https://x.com/i/status/1426170298567700480)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "厚客户端拦截记录的请求级覆盖",
    "厚客户端捕获图显示Burp拦截login.live.com的POST JSON与登录窗。图片能支持该请求经代理，不给全部进程/协议的流量覆盖。\n\n记录应用进程、网络库、代理路径、TLS信任、具体请求及响应关联；HTTP history出现一条不能推原生后台、其他域或所有登录步骤都被捕获。敏感头/正文不复制；空history、SSL失败或另一个浏览器是反例。\n\n来源：[保存帖1](https://x.com/i/status/1426503872978161667)、[保存帖2](https://x.com/i/status/1430079529171701790)。"
  ],
  [
    "by-type/info-secrets.md",
    "gitconfig远程指针与备份文件内容的分层",
    "gitconfig提示图在remote.origin.url放备份路径；gau过滤.zip的正文则把候选直接叫P1。配置指针和历史URL均未给实际文件内容。\n\n先核对来源仓库/提交、URL主机归属、是否真实文件路径、当前访问合同与最小非敏感样本；正则点未转义、查询里含zip、过期链接、合法公开备份或不可读指针是反例。不能因命中路径就下载整库、保存密码或套严重等级。\n\n来源：[保存帖1](https://x.com/i/status/1426278939899609094)、[保存帖2](https://x.com/i/status/1426508914112221186)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "历史URL流水线的覆盖追加和阶段来源",
    "侦察图串waybackurls、gauplus、sed、grep、sort、anew、wurl与gf；多个阶段输出文件名和覆盖/追加方式不一致，还删中间文件。\n\n为每阶段保留输入hash、来源时间、命令版本、规范化方式、输出与计数；核对200筛选实际消费的是哪个文件。参数/扩展/模式分类只建立候选队列，覆盖文件、混旧追加、错误变量、丢JS或目录匹配是反例，不照图执行清理命令。\n\n来源：[保存帖1](https://x.com/i/status/1426516449741348865)、[保存帖2](https://x.com/i/status/1429033679133630468)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "后利用管理菜单与首次执行因果",
    "Bantam图有www-data、PHP版本与Eval/System/FileBrowser菜单，CamPhish图选择隧道和模板。菜单存在没有说明首次入口、权限绕过或执行结果。\n\n区分初始化/连接/身份/具体操作/最终效果，绑定受控输入与真实输出。只见help、banner、菜单、另一个会话或静态字段是反例，不能推WAF逃逸、首次RCE、摄像头授权绕过；不启动植入器或钓鱼服务。\n\n来源：[保存帖1](https://x.com/i/status/1426668585204736009)、[保存帖2](https://x.com/i/status/1427257501846757383)、[保存帖3](https://x.com/i/status/1427393284138221577)。"
  ],
  [
    "discovery/passive-and-services.md",
    "接口UP状态和证书指纹的观察对象",
    "命令资源图示ip addr筛state UP、跨日志目录tail/xargs、openssl x509指纹。网络接口状态、日志选择与证书制品标识是三个观察对象。\n\n接口UP不能单独确定出站路由；日志需明确路径、排序、时间和权限，复杂管道参数引用须审阅；证书指纹关联制品不自动证明资产归属。缺路由、错选旧日志、同证书复用或空结果是反例，本轮没有执行资源命令。\n\n来源：[保存帖1](https://x.com/i/status/1426732091140579330)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "tko-subs发现模式与占有开关的授权区分",
    "tko-subs帮助列provider CSV、域输入文件、DNS服务器/端口、线程、平台凭证与takeover开关。识别候选和注册/占有外部资源是不同动作。\n\n将scope、DNS记录与时间、provider指纹、可认领条件、发现结果和是否真实认领分别保存；help中出现开关、死DNS、过期指纹或无资格账号是反例。输入域批量化不扩大授权，未使用凭证或触发占有。\n\n来源：[保存帖1](https://x.com/i/status/1426895121451261957)、[保存帖2](https://x.com/i/status/1427305573608042505)。"
  ],
  [
    "by-type/file-upload.md",
    "WebDAV写入与脚本handler执行的两张收据",
    "正文描述WebDAV PUT PHP返回201；另一报告邮件自述PUT上传及反向shell。现有图片没有真实后续命令请求和执行结果。\n\n分记录写权限、保存路径/重命名、取回内容、文件handler/目录规则及受控无害执行标记；201只支持创建语义，静态下载、隔离存储、解释器未映射或只有研究者邮件是反例。固定Basic凭证和执行代码不抄用；不由上传成功补RCE。\n\n来源：[保存帖1](https://x.com/i/status/1426926954138193921)、[保存帖2](https://x.com/i/status/1427999404628320263)。"
  ],
  [
    "by-type/xss.md",
    "JSON源码字符串与真实HTML消费之间的缺口",
    "view-source图显示JSON值里iframe javascript字符串；另一正文把img onerror中的alert(whoami)当反射XSS升RCE。二者未给服务端命令执行链。\n\n绑定响应Content-Type、真实页面读取点、DOM sink、转义/CSP、读者origin及实际浏览器效果。源码中的HTML、纯JSON展示、未定义JS标识符或仅弹窗是反例；whoami在该表达式里是JS变量，不是OS命令，不能补RCE。\n\n来源：[保存帖1](https://x.com/i/status/1427098501545005062)、[保存帖2](https://x.com/i/status/1427305413758701577)。"
  ],
  [
    "by-type/csrf.md",
    "图片触发注销的读者与重复消费条件",
    "保存[1/2]正文提出把注销链接放img src，使组织成员读取后退出。未保存第二段及全员受影响记录。\n\n先确认图片会被实际请求、注销端点是否改变状态、cookie/SameSite/域作用域、受控读者会话及重复渲染；合法本人注销、请求无cookie、GET无副作用或图片被代理拦截是反例。单次退出与持续不可用分开，不由HTML注入推全员DOS。\n\n来源：[保存帖1](https://x.com/i/status/1427143380211957764)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "urlhunter日期关键词与本地NSE目录的能力界限",
    "urlhunter图给关键词文件、日期和输出参数；nscript别名列本地Nmap脚本再grep。一个查询历史索引，一个查询本地文件清单。\n\n保留关键词/日期/索引来源与输出hash；本地脚本路径/安装版本/脚本名另记。文件存在不等于加载、执行或漏洞命中，历史URL不等于实时端点；错误日期、未安装脚本、只匹配名字或过期目标是反例，不运行NSE扫描。\n\n来源：[保存帖1](https://x.com/i/status/1427173323964833793)、[保存帖2](https://x.com/i/status/1427666323102969866)。"
  ],
  [
    "by-type/info-secrets.md",
    "OTX订阅情报API示例与敏感密钥影响",
    "API清单图示OTX subscribed pulses端点、X-OTX-API-KEY、成功结果、Authentication required及64字符regex。截图是示例合同，没有给密钥归属或真实权限。\n\n把provider、端点动作、key权限、资料公开范围和受控最小响应分开；regex命中、示例key、公共威胁情报或未授权错误是反例。不得复制使用图中key或把公共订阅内容直接称敏感泄漏。\n\n来源：[保存帖1](https://x.com/i/status/1427250961144107010)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "OAuth缺email声明后的自填邮箱和保留地址政策",
    "正文描述去Facebook email scope后应用要求自填邮箱，可填原本禁止的admin地址；截图回信称regression并奖励。注册显示邮箱和拥有邮箱/管理员权限不同。\n\n核对授权scope、身份主键、email来源和verified状态、保留地址政策、验证流程及应用实际角色；同名显示、未验证待激活或仍是普通账号是反例。回信证明个案评语，不给管理员权限收据；只以自有身份设计后续验证。\n\n来源：[保存帖1](https://x.com/i/status/1427343103938088967)。"
  ],
  [
    "reporting.md",
    "未回复等待与企业处理流程的证据边界",
    "VDP流程图解释应用、基础设施、VM、SOC和管理团队可能处理报告；正文因4/5天未回复焦虑。一般流程不能补成本案已经进行的活动。\n\n依当前项目沟通渠道与承诺时间保存提交/收件/状态/公开回复，避免从短暂等待推拒绝。内部协调、修复、业务风险、根因及付款属于不同状态；无正式状态或只有通用解释是反例，未发送催促消息。\n\n来源：[保存帖1](https://x.com/i/status/1427352081837461504)。"
  ],
  [
    "by-type/file-upload.md",
    "扩展名与配置文件及编码NUL的不同处理层",
    "后缀图混PHP/ASP源文件、配置、handler扩展；正文另列双后缀、大小写、点/空白、%00与反斜线x00。列表不表示全部服务器同样处理。\n\n标记原始filename、传输编码、解码次数、实际字节、存储重命名和取回handler；文字x00、百分号未解码、被拒NUL、配置不生效或只静态下载是反例。配置文件修改能力与脚本执行另证，不补通用过滤绕过。\n\n来源：[保存帖1](https://x.com/i/status/1426431826013339650)、[保存帖2](https://x.com/i/status/1427894794815250434)、[保存帖3](https://x.com/i/status/1427959268981018634)、[保存帖4](https://x.com/i/status/1428352985176834057)。"
  ],
  [
    "source-audit.md",
    "SGXRay模型反例与实际构建覆盖",
    "SGXRay图从enclave应用构建so，extract-bc取得LLVM输入，再由CLI输出Verified或Error+Counterexample。架构图没有给本次构建/属性/验证输出。\n\n以制品hash、编译选项、IR提取、被验证属性、假设和边界关联结果；Verified只相对模型和已验证条件。无具体属性、模型遗漏、不同构建或只见流程图是反例，未构建或执行源工具。\n\n来源：[保存帖1](https://x.com/i/status/1427755667260117006)。"
  ],
  [
    "by-type/idor-access-control.md",
    "购物车cookie标识与任意用户读写的证据差距",
    "正文称Ud参数导致三百万用户读写；图实际cart view GET带u_ID_COOKIE，返回JSON成功及HTML字段。没有双身份对照或写入收据。\n\n隔离actor cookie、目标对象/owner、字段来源、动作与权威最终状态；仅自有cart、展示字段、多个cookie未隔离、success标签或数字总量是反例。公开标识不等于操作权限，不能由一张GET图补任意写或全部用户数量。\n\n来源：[保存帖1](https://x.com/i/status/1427890986647121922)。"
  ],
  [
    "source-audit.md",
    "PyPI审计warning排名与安装制品的关联",
    "AuraBorealis图有highest warning count、severity、日期变化与单包检查链接。UI展示审计元数据，没有给当前项目装入哪个包/版本。\n\n关联registry/包名/版本/制品hash、扫描规则、警告位置、实际依赖路径和运行可达性；大warning计数、排名变化、同名不同包或未安装版本是反例，不能直接当当前可利用漏洞或恶意包证明。\n\n来源：[保存帖1](https://x.com/i/status/1427982429151764488)。"
  ],
  [
    "by-type/info-secrets.md",
    "Jsleak模式输入与GitSecret分支命中的验证阶段",
    "Jsleak帮助只列JSON输出、模式文件和verbose；GitSecret图选master并打印provider key模式命中。help与匹配结果仍缺有效性和权限。\n\n绑定仓库归属、commit/branch、文件位置、模式版本、最小脱敏片段和业务使用路径；示例字符串、错误provider、旧分支、无调用者或只有help是反例。不复制key、不用key登录；regex命中与真实敏感暴露分阶段。\n\n来源：[保存帖1](https://x.com/i/status/1428118222855942148)、[保存帖2](https://x.com/i/status/1430156518041821186)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "空格过滤候选的shell展开和变量名条件",
    "图建议花括号、Ifs变量和tab形式。去ASCII空格只处理一种字符，实际执行还依shell与参数传递。\n\n先辨明是否经shell、具体解释器、可控位置、变量大小写和内容、词拆分/花括号支持与实际接收字节；原生argv、变量未定义、字面tab文本或不同shell是反例。把候选展开与最终受控无害效果分开，不运行图中命令，也不补跨平台通用RCE。\n\n来源：[保存帖1](https://x.com/i/status/1428247860785598467)。"
  ],
  [
    "by-type/info-secrets.md",
    "GitHub查询类别与拼写以及fresh筛选的漏项",
    "GitHub图在Repositories页对stie.com keyword返回零；另一笔记列org/user/language/NOT及关注fresh。仓库搜索与代码/提交检索不同。\n\n保存实际查询、类别、版本语法、分页、时间窗口、commit和结果hash；修正拼写并明确关键词是否AND/OR，排除式查询也要留未排除对照。零仓库结果不能证无代码泄漏，fresh偏好不能排除旧仍暴露内容，不依据搜索索引授权新资产。\n\n来源：[保存帖1](https://x.com/i/status/1428315335501877250)、[保存帖2](https://x.com/i/status/1430106191645061142)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "PrintNightmare本地样例与远程执行路径的区别",
    "保存alt说明该PowerShell脚本实施LPE；图新建本地管理员、runas及本机whoami/localgroup。上层标签同时提remote，但没有远端请求链。\n\n保留本机主体权限、操作前后组成员/执行身份、具体构建和本地接口；远端连接、服务身份与调用权限另证。只见新账号/回显、未知原始权限或缺远端路径是反例；未执行脚本、创建账号或使用图中密码。\n\n来源：[保存帖1](https://x.com/i/status/1428504202628812803)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "JDWP服务识别成功与信息脚本失败",
    "JDWP图27000 open并识别协议版本，jdwp-info却ERROR；另端口Jetty HTTP401。开放调试服务与已成功执行调试操作并非一回事。\n\n将端口/服务指纹、实际握手、调试权限、错误原因及受控效果分开保存；识别结果、网页401、脚本失败或未经身份/实例关联是反例。标题中的RCE与Shodan候选不补实际命令执行，未连目标调试器。\n\n来源：[保存帖1](https://x.com/i/status/1428688859391426560)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "Selenium已登录资料采集与权限边界",
    "FisherMan日志称hidden mode、logged in、访问profile和收集div选择器。日志未给采集内容或超出可见权限。\n\n绑定自有登录身份、页面/资料可见合同、实际字段与最终记录，公开页面与私有资料读取分开。选择器命中、登录提示、空div或本人可见信息是反例，不补未授权个人资料泄漏，不使用截图账号。\n\n来源：[保存帖1](https://x.com/i/status/1428706950280265731)。"
  ],
  [
    "by-type/host-header.md",
    "Forwarded复合头与403基线的逐字段对照",
    "正文写Forward，截图实际Forwarded的for/by/host同时修改，返回200文章分页；第二图独立CloudFront403错误。两图未绑定相同请求和身份。\n\n先保存同对象/路径/身份基线，再逐字段隔离规范化、信任代理链和路由消费者，比较实际私有数据/动作。不同域/时间/身份、公开文章、一般CloudFront错误或多个变量变化是反例，不能从200推出全子域权限绕过；CORS头另需浏览器上下文。\n\n来源：[保存帖1](https://x.com/i/status/1428723640887959553)。"
  ],
  [
    "source-audit.md",
    "静态零检测与AMSI运行时效果的独立收据",
    "AMSI图含混淆PowerShell反射GetType/GetField/SetValue及0/57静态扫描。静态未命中不说明运行时安全接口行为。\n\n以样本hash、扫描时间/引擎、解释器版本、真实加载路径和运行时受控事件绑定结论；文本文件、未执行片段、未知字段、不同build或无运行日志是反例。不能声称永久undetectable，本轮没有解码后执行或修改系统字段。\n\n来源：[保存帖1](https://x.com/i/status/1428797469232599041)。"
  ],
  [
    "by-type/crlf-response-splitting.md",
    "Unicode编码候选与实际响应分隔字节",
    "正文将UTF8百分号编码序列称CRLF并泛称Java可用。传输编码、解码字符和最终HTTP边界需要逐层区分。\n\n记录原始字节、各层解码/字符转换、header拼接消费者与真实响应边界；只反射Unicode字符、URL编码仍在、标准拒绝换行或内容落正文是反例。不能仅由Java标签/字符串推response splitting，未发送候选。\n\n来源：[保存帖1](https://x.com/i/status/1428815206386479110)。"
  ],
  [
    "discovery/web-and-api.md",
    "JSON字段路径提取与HTTP路由发现的分离",
    "JSON图有address对象和friends数组，工具输出/address等与/friends/1。输出来自JSON结构，没有给对应HTTP路由。\n\n将属性路径、数组索引、资源URL/links字段和已观察请求分别分类，核对提取器的数组覆盖及转义规则；普通个人资料字段、缺数组元素、无请求或404是反例。工具名endpoints不能把所有字段路径计入API资产。\n\n来源：[保存帖1](https://x.com/i/status/1428966231583850500)。"
  ],
  [
    "by-type/info-secrets.md",
    "accesslogs目录与日志中认证资料的分层影响",
    "正文描述/accesslogs/目录索引、日志文件和700用户/管理员密码。没有保存文件内容、字段形式或账号归属证据。\n\n区分目录元数据、可读日志、敏感字段语义、所属业务及时间范围；脱敏最小样本/受控合成记录足以设计验证，原始密码不收集使用。公开合成日志、已脱敏、无真实身份或只有数量叙述是反例，不自动套P1/当前700人。\n\n来源：[保存帖1](https://x.com/i/status/1428978079448375297)。"
  ],
  [
    "by-type/ssrf.md",
    "AutoRepeater全替换的范围和请求因果",
    "两张图配置Request Body Regex Match与Replace All，把URL样式字符串换为OOB地址。配置界面没有给自动重放执行或服务端取回证据。\n\n限定获准端点/方法/会话、非敏感请求及重放预算；核对替换后JSON/XML语法、字段类型和单变量，逐请求使用独立marker。浏览器/预览/安全扫描器回调、只DNS、误替非URL或无对应请求是反例；不由全局替换补自动发现漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1429045628080902144)、[保存帖2](https://x.com/i/status/1430433117991493645)。"
  ],
  [
    "experiment-design.md",
    "表单分页爬取与POST评估任务的终态",
    "Brutus图列scrapethissite多个forms?page_num以及Beginning POST evaluation。抓到候选和任务开始日志不等于检测完成。\n\n绑定范围、每页来源、表单action/method、参数、请求预算、任务游标和终态；去重保留分页关系，主动POST副作用需单独控制。只抓URL、重复分页、任务开始/中断或无响应是反例，不把日志数当漏洞数。\n\n来源：[保存帖1](https://x.com/i/status/1429069389232496641)。"
  ],
  [
    "by-type/authn-session.md",
    "恢复邮箱多值输入的查询和发信绑定",
    "正文列email分隔符和JSON数组；图为旧框架重复参数first/last/list规则。没有账号查询、发信与challenge绑定结果。\n\n在两个自有账号间区分query/form/JSON类型、重复键/数组、验证顺序、账户选择、发信收件人与重置令牌用途；各层同输入一致消费才可判。框架表缺版本/API、只UI接受、发信仍本人或挑战拒绝是反例，不向真实第三方发邮件。\n\n来源：[保存帖1](https://x.com/i/status/1429179741748305930)。"
  ],
  [
    "by-type/authn-session.md",
    "SMB凭证验证与命令执行的动作权限",
    "Keimpxhelp列目标/域/密码/NTLM hash、线程、batch、SMB命令和OS命令列表。接受输入的工具不提供目标权限证明。\n\n以自有测试身份、获准单资产、认证结果和被允许具体动作建立矩阵；认证成功、帮助菜单或admin字符串不能直接推OS命令能力。错误域、限权限会话或无执行receipt是反例；未使用凭证/哈希，也未运行批量登录和命令。\n\n来源：[保存帖1](https://x.com/i/status/1429567620576071686)。"
  ],
  [
    "by-type/ssrf.md",
    "元数据JSON字段与凭证有效性的分层",
    "生产SSRF题的图片显示169.254元数据IAM security-credentials路径及Code、Type、Key、Token、Expiration字段，值均遮掩。能观察字段结构，缺可验证凭证范围。\n\n关联实际server fetch输入、受控URL/重定向、响应来源、身份/实例及敏感字段；HTTP结构、自填页面、未知代理或遮掩值不证明有效key、权限/RCE。只设计合成元数据服务验证，不请求真实云元数据或使用令牌。\n\n来源：[保存帖1](https://x.com/i/status/1429626639110086660)。"
  ],
  [
    "source-audit.md",
    "内存PE导出与样本分析完成的不同产物",
    "ProcessDump图列chrome多个进程和PE/DLL导出文件。文件出现只给产物生成的界面观察。\n\n关联获准进程/时间/位数、读取权限、原始与导出hash、导出完整性及实际分析结论；合法浏览器模块、空/损坏导出、未知进程或仅列表是反例。不能补恶意样本成功恢复、执行或分析完成，未读取真实进程内存。\n\n来源：[保存帖1](https://x.com/i/status/1429794172668633089)。"
  ],
  [
    "reporting.md",
    "鸣谢页面变更与原始贡献证据的留存",
    "图片对比Citrix鸣谢在2021年3月和8月的文字。归档差异显示特定保存页面版本，不给当前官网或技术修复因果。\n\n保存原始提交、收件、报告ID、回复、公开修复公告及页面时间/hash；署名变化、快照缺口或一般感谢不能替代漏洞机制/修复证据。不要从历史截图推现任政策或当前页面状态，本轮未访问外链补全文。\n\n来源：[保存帖1](https://x.com/i/status/1429821829145763842)。"
  ],
  [
    "by-type/sql-injection.md",
    "SQL候选清单的参数类型和零延迟反例",
    "一帖把q引号/数组/注释/concat清单称100%发现SQLi；另一time-based样例sleep(0)。多种输入分别涉及解析类型与DB方言，零sleep不产生预期延迟。\n\n先隔离应用类型解析、SQL构造和方言，采用受控成对真假/非敏感输出或获准小预算时序对照；HTTP错误、数组拒绝、字符串反射、网络抖动和零延迟是反例。未知DB函数和清单命中不补注入成立，未运行SQL或延迟请求。\n\n来源：[保存帖1](https://x.com/i/status/1426615994659844096)、[保存帖2](https://x.com/i/status/1430018495727636483)。"
  ],
  [
    "by-type/ssrf.md",
    "localhost候选写法与实连目的地址的绑定",
    "正文列整数、八进制、hex、短IPv4、DNS别名、IPv6 loopback及未指定地址写法。不同URL/地址解析器不保证同解释。\n\n逐层记录validator、URL parser、DNS、redirect和socket实连地址，比较规范化结果与预期拒绝；字符串合法、DNS变化、未指定IPv6地址或不同解析库是反例。不得把候选表当通用本地绕过，本轮未发本机/内网请求。\n\n来源：[保存帖1](https://x.com/i/status/1430037295911120901)。"
  ],
  [
    "by-type/mobile-android.md",
    "Android代理TLS失败与pinning绕过成功的界限",
    "教程题为Frida/Burp/GenyMotion绕pinning，图却有多域SSL negotiation fatal alert、0请求和手机offline。失败症状不足定位单一原因。\n\n按网络可达、代理路径、CA信任、TLS版本/协议、应用栈、hook加载与实际HTTP记录分阶段；多域同时失败还需独立正常端点对照。空history、offline、只启动hook或未出现请求是反例，不能算绕过完成，未修改设备或运行hook。\n\n来源：[保存帖1](https://x.com/i/status/1430079529171701790)。"
  ],
  [
    "by-type/info-secrets.md",
    "DSStore标题与SymfonyProfiler错误页的组件错配",
    "正文称DSStore/Laravel信息泄漏，保存图为SymfonyProfiler Token not found。页面识别不能补DSStore解析或敏感profiling数据。\n\n分别保存实际组件/版本、具体文件格式和最小内容、profile token语义/可访问数据与权限；错误页、不存在token、不同框架或仅标题是反例，不把随机token当有效会话，不补环境密钥泄漏。\n\n来源：[保存帖1](https://x.com/i/status/1430139414122962947)。"
  ],
  [
    "by-type/file-upload.md",
    "图片魔数和multipart嵌PHP与执行链的缺口",
    "PNG/JFIF hexdumps显示格式头；multipart PUT的file.png/image/png内嵌PHP，仅请求没有响应。JPEG正文FFEE与图FFE0 JFIF不一致。\n\n核对实际制品字节/完整格式、multipart边界、保存改名、内容重编码与取回handler；魔数通过、请求发送、损坏图片或静态下载是反例。文件格式识别和解释器执行是不同合同，未上传或执行代码。\n\n来源：[保存帖1](https://x.com/i/status/1430287600783405061)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "AWS类别表中的对象动作与本机路径区别",
    "正文列S3公开read、认证write、目录路径、POSTpolicy和Lambda；图下半截还出现反向代理/Cognito类别，内容裁切。清单没有具体配置或请求结果。\n\n按资源owner、actor、对象/前缀、read/write/list动作、策略条件、签名与执行消费者建立矩阵；公开预期内容、写入不可执行、对象键中passwd字样或缺实例配置是反例。S3对象路径不自动读取宿主文件，不因top10/P1标签补漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1430494198684262411)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0108.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==58 and len(urls)>0
assert all(pid in ids for pid in urls)
assert len({title for _,title,_ in facets})==len(facets)
grouped=defaultdict(list)
for f,title,body in facets:
 p=T/'references'/f
 assert p.is_file() and ('## '+title) not in p.read_text(),(f,title)
 grouped[p].append('\n\n## '+title+'\n\n'+body+'\n')
community=T/'references/research/community-distillation.md'
marker='\n## 首轮提炼范围与未采纳内容\n'
c=community.read_text();assert c.count(marker)==1
routes=[]
for f,title,body in facets:
 summary=body.split('\n')[0].split('。')[0]+'。'
 assert '|' not in summary and '\n' not in summary
 routes.append(f'| {title} | {summary} | [方法条目](../{f}) |')
for p,parts in grouped.items():p.write_text(p.read_text()+''.join(parts))
community.write_text(c.replace(marker,'\n'+'\n'.join(routes)+'\n'+marker,1))
print('Added',len(facets),'facets and routes to',len(grouped),'topic files; all',len(urls),'source URLs batch-bound')

