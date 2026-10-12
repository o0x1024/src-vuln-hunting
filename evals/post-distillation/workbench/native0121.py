# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "by-type/xss.md",
    "CRLF 到 HTML 响应消费的两个边界",
    "正文给编码CRLF、响应头及HTML脚本片段，图只给ReflectedXSS accepted邮件。先核输入是否进入真实响应头、解码/CRLF是否合法，再核正文边界、MIME、浏览器上下文和CSP；改变旧X-XSS-Protection字段不自动关闭所有防御。\n\n离线自有合成响应比较普通值、安全拒绝、头部编码和无害HTML标记；只有字符串回显、邮件、错误响应或未被HTML消费者解析为反例。奖励不能补原始交换，也不能由cookie表达式推出可读HttpOnly。\n\n来源：[保存帖1](https://x.com/i/status/1487822309981564929)、[保存帖2](https://x.com/i/status/1488276085460508673)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "后缀与内容类型筛选只产生文件候选",
    "完整httpx链用历史URL、末尾.js、200和application/javascript筛选；另帖targetfile/JSON示例混用cat域名和逻辑or文字，没有完整有效脚本。\n\n静态逐段核stdin/argv、原URL的path/query、当前归属、状态/字节和MIME。自有带版本query、无后缀、第三方、软200及空输入作对照。后缀/声明类型/历史记录不等实际文件或秘密；过滤漏项与命令语法错误需单独记录，不运行归档网络命令。\n\n来源：[保存帖1](https://x.com/i/status/1487838080807538690)、[保存帖2](https://x.com/i/status/1488008369525096454)。"
  ],
  [
    "by-type/authn-session.md",
    "邮箱大小写映射与重置接收者的不同合同",
    "保存的是2/2，声称邮箱大小写变化可把reset token发给另一邮箱；第二示例混入http URL，不能擅自修成一条有效地址。Python upper与casefold具有不同Unicode语义，转换后的相等不等于两接收者身份相同。\n\n静态追原始地址→验证/规范化→账户查找→重置目的地址；仅用自有合成邮箱比较原值、普通大小写、Unicode、拒绝与查找键。接收地址未变、统一验证后的绑定正确、畸形地址被拒或没有投递证据为反例，不发送重置邮件。\n\n来源：[保存帖1](https://x.com/i/status/1487851032315318272)。\n\n语义校核：[Python 字符串方法](https://docs.python.org/3/library/stdtypes.html#str.upper)。"
  ],
  [
    "targeted-fuzzing.md",
    "一份 fuzz 字典不能覆盖所有消费者",
    "正文说一个字典够用，图仅fuzzDicts仓库卡片和stars，没有字典正文。选择输入集应由路由、参数类型、编码层、语法消费者和预算决定。\n\n自有离线样本记录每类输入覆盖/拒绝/缺失，比较无关词与明确合同边界。仓库热度、列表长度、未适配目标或未有消费差异为反例；不把资源链接补成全部字典已理解或所有漏洞可发现。\n\n来源：[保存帖1](https://x.com/i/status/1487852001602174976)。"
  ],
  [
    "by-type/idor-access-control.md",
    "AuthCov 爬行身份与 Authz0 多角色模板",
    "正文保存AuthCov以预定义登录用户进行headless爬行；Authz0以YAML管理URL/roles并复用ZAP/Burp历史、多headers/cookies。两者描述功能，没有运行结果。\n\n离线自有主体/对象/动作矩阵绑定会话、请求、期望权限与实际字段，比较本人/他对象/低角色/无身份。仅爬到URL、模板名称、换cookie失效或正常拒绝为反例；同一身份的爬行覆盖不等跨角色授权已检查，历史请求也不保证当前完整。\n\n来源：[保存帖1](https://x.com/i/status/1487871184687415296)、[保存帖2](https://x.com/i/status/1488210470213496843)。"
  ],
  [
    "by-type/authn-session.md",
    "Kerbrute 帮助页的账户与票据副作用",
    "完整帮助图列USER/users、PASSWORD/passwords、domain/DC IP、threads默认1、结果文件和no-save-ticket；后者说明正确凭据可能保存TGT。没有保存一次实际认证交换。\n\n静态区分账户发现、认证、票据获取和权限，记录输入许可、锁定/速率及保存位置；离线合成合法/错身份/拒绝例。CLI/help、字段名或工具描述不证明认证成功/缺限速，不尝试真实账号、保存票据或运行暴力猜测。\n\n来源：[保存帖1](https://x.com/i/status/1487897047474786319)。"
  ],
  [
    "by-type/xss.md",
    "message listener 正则命中与 DOM sink",
    "正文多次用getJS/httpx正则找addEventListener message；配图是奖励列表或仓库封面，没有真正handler。正则候选可能漏变量、包装器、空白和其他注册形式，也可能匹配注释。\n\n静态追事件origin/source、消息schema、可信窗口关系、字段变换到DOM sink及CSP。自有无外联fixture比较正确来源、错误来源、纯文本及拒绝。只有listener、扫描命中、无危险sink或严格校验为反例；不能将全部message监听当DOM XSS。\n\n来源：[保存帖1](https://x.com/i/status/1487933582354092039)、[保存帖2](https://x.com/i/status/1489122903379812352)、[保存帖3](https://x.com/i/status/1489331257737719817)、[保存帖4](https://x.com/i/status/1491313371647705089)。"
  ],
  [
    "by-type/host-header.md",
    "X-Forwarded-Host 标签缺少反射消费者",
    "保存正文仅称XSS via X-Forwarded-Host，图为通用攻击流程，没有原始头/响应。要区分代理信任、服务端生成字段、HTML反射和浏览器执行。\n\n离线合成头值记录每层转发/覆盖和模板编码，正常值、安全拒绝及纯文本对照。只有标题、无反射、值被可信代理覆盖或安全输出为反例，不能凭通用图认某目标有漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1487975500689842177)。"
  ],
  [
    "discovery/passive-and-services.md",
    "RocketMQ 控制台读字段与管理动作",
    "完整控制台图有DefaultCluster、三个broker、内部地址/10911、V4_3_1、消息TPS/计数及STATUS/CONFIG按钮；Shodan题目建议查console和日志，但图未显示日志正文或配置操作。\n\n静态核资产归属、真实认证角色、字段预期可见范围、请求和消费者；自有只读合成字段与拒绝对照。标题/共享IP、正常管理员视图或仅按钮为反例；内部地址可见不等后台写权限、消息读写或当前版本受影响。\n\n来源：[保存帖1](https://x.com/i/status/1488097638088069125)。"
  ],
  [
    "expert-reasoning.md",
    "缓存报告列表不能补出 CDN 缓存链",
    "图列cache poisoning/deception、Referer storedXSS、token disclosure等报告标题，正文只有三篇外链和总奖金。保存材料未给缓存键、响应或跨用户消费。\n\n离线自有缓存模型分别记录键、可控但未入键的字段、响应可存性和另一个读者，比较冷/热、不同身份及不可缓存结果。标题/总金额、本人缓存、无共享复用或缓存键完整为反例，外链全文按用户口径覆盖而不补造链。\n\n来源：[保存帖1](https://x.com/i/status/1488108514505785349)。"
  ],
  [
    "by-type/info-secrets.md",
    "Segment writekey 与 API key 的能力证据",
    "正文询问JS内Segment writekey/apikey是否可利用；另帖附件仅HardcodedPrivateAPIKEYToken奖励题目，没有材料/服务权限。公开采集标识、查询凭据和管理秘密应按消费者分别判断。\n\n静态绑定来源、环境、有效期、预期公开及允许动作，用自有合成公开/受限字段对照。名称、格式、奖励或无有效权限证据为反例；不调用真实key、写入事件或发送数据。\n\n来源：[保存帖1](https://x.com/i/status/1488165340765126656)、[保存帖2](https://x.com/i/status/1488896481054511104)。"
  ],
  [
    "by-type/xss.md",
    "href 中 javascript scheme 仍需真正导航",
    "正文给href用户输入及javascript scheme，并称open redirect→RXSS，模糊图只见hacked对话框。属性无需破引号只是特定上下文，不能推出所有重定向执行脚本。\n\n静态核URL解析、scheme限制、导航消费者、用户动作、origin与CSP，离线自有纯URL/拒绝/无害导航标记对照。HTTP Location被拒、仅文本、策略阻断或没有真实消费者为反例；模糊弹框不证明接管。\n\n来源：[保存帖1](https://x.com/i/status/1488170820803334145)、[保存帖2](https://x.com/i/status/1488717102923988994)。"
  ],
  [
    "source-audit.md",
    "跨请求复用 RegExp 的 lastIndex 状态",
    "保存2/2称连续两次test能跳过引号。MDN确认g/y标志的同一RegExp对象保存lastIndex；匹配成功向后推进，失败归零。是否跨请求复用对象、初始索引及正则结构仍须代码证明。\n\n自有离线合成字符串比较同实例/新实例、第一次/后续调用与显式归零；记录结果和索引。每请求新建、无g/y、已归零或参数化查询为反例；校验变化不自动SQL注入，还须真实SQL消费者和差异。\n\n来源：[保存帖1](https://x.com/i/status/1488191512974282754)。\n\n语义校核：[MDN RegExp.test](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test)。"
  ],
  [
    "by-type/graphql.md",
    "graphql-path-enum 资源名与 resolver 授权",
    "正文推荐path枚举工具并称上周有帮助，未存查询、schema或结果。路径发现和resolver的主体/对象权限是两层。\n\n离线自有schema保留入口、类型、参数、角色和resolver，比较可达/不可达、合法/错对象。工具链接、禁用introspection、路径存在或正常权限拒绝为反例；枚举结果不等全部API已测试，不安装/运行未存仓库。\n\n来源：[保存帖1](https://x.com/i/status/1488197131814928388)。"
  ],
  [
    "discovery/web-and-api.md",
    "历史 URL 的百分号空格不是 XSS 证明",
    "正文建议wayback列表搜索%20，两个post正文相同。编码空格最多提示输入形态，不给反射或浏览器语法消费。\n\n离线按path/query组件保留原字节和解码次数，再追参数到输出上下文；比较无参数、纯文本、安全编码和实际无害节点。历史URL、关键词、不存在当前入口或无危险sink为反例；不把所有带%20的URL当XSS。\n\n来源：[保存帖1](https://x.com/i/status/1488306826861060096)。"
  ],
  [
    "discovery/passive-and-services.md",
    "密集端口列表与服务作用的区分",
    "图是多个部分遮盖IP重复2052/2053/2082/2083/2086/2087/2095/2096及HTTP端口。正文随机字节送端口的建议不是所存服务证据。\n\n静态核监听、代理/共享网段、实际协议和所属资产，只在自有合成清单做普通/代理/误识别对照。端口开放、重复网段、无banner或正确访问控制为反例，不向真实服务灌随机数据或把端口数量当安全问题。\n\n来源：[保存帖1](https://x.com/i/status/1488387459977302017)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "SuiteCRM Notes 日志与执行身份",
    "终端图声称已登录、Notes植入payload并经localhost/public地址读取passwd样式输出。正文/CVE标签与工具日志不能替代原始请求、权限提升前后及进程身份。\n\n静态追账号角色→Note写/文件存储→解释器消费者→实际能力，自有无敏感标记比较合法Note、拒绝和纯文本。日志自述、passwd中的root条目、localhost演示或未有低权限对照为反例；root账户记录不等执行uid0，不运行工具/植入文件。\n\n来源：[保存帖1](https://x.com/i/status/1488422388991938560)。"
  ],
  [
    "by-type/open-redirect.md",
    "gf redirect 输出和重定向证明分开",
    "完整管线是waybackurls→httpx超时/线程→gf redirect→anew；图实际列多条redirect=no，输出文件却叫vulns。关键词筛选没有展示Location或导航目的。\n\n离线保留原URL和阶段退出/超时、去重库及归属，再核真正跳转消费者，用自有目标/拒绝/相对路径对照。参数名、历史链接、短超时漏检或未有跳转为反例；结果名不改变证据等级。\n\n来源：[保存帖1](https://x.com/i/status/1488455851711029252)、[保存帖2](https://x.com/i/status/1488552263492775937)、[保存帖3](https://x.com/i/status/1488768051453444098)、[保存帖4](https://x.com/i/status/1488847743367929860)、[保存帖5](https://x.com/i/status/1488857275166978048)、[保存帖6](https://x.com/i/status/1489591292279484416)。"
  ],
  [
    "by-type/ssrf.md",
    "开放重定向到 SSRF 的服务端客户端条件",
    "保存正文分别说重定向可能绕IP限制/导致SSRF，外链全文未存。客户端必须是服务器真正取URL的网络消费者，而且后续跳转要抵达本来受限目的。\n\n离线自有合成每跳核scheme/host/解析地址/权限、是否follow及响应归因。只浏览器跳转、停止跟随、每跳拒绝或无服务端连接为反例；重定向存在不自动是SSRF，更不证明内网敏感读取。\n\n来源：[保存帖1](https://x.com/i/status/1488466167685685249)、[保存帖2](https://x.com/i/status/1488497993527353349)、[保存帖3](https://x.com/i/status/1488919765225775109)。\n\n语义校核：[OWASP SSRF 防御](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)。"
  ],
  [
    "by-type/authn-session.md",
    "响应改值、状态码与服务器认证状态",
    "保存线程最后一条列response/status manipulation、parameter pollution、token forging，缺前文和真实交换。四类动作的消费者和权限不同。\n\n离线自有认证状态机比较UI反馈、真实服务器会话、重复参数解析和签名绑定，保存合法/畸形/拒绝对照。客户端变绿、200页面、伪造但未接受token或无状态改变为反例；不能按标签把身份验证绕过算完成。\n\n来源：[保存帖1](https://x.com/i/status/1488506672847142923)。"
  ],
  [
    "by-type/info-secrets.md",
    "AIza 前缀提取不是完整 Google key",
    "完整正文httpx extract-regex仅匹配AIza前缀，然后给scanner外链，没有完整key或权限响应。\n\n静态核匹配长度、材料来源/公开用途、项目环境、限制和真正API动作；离线自有字符串对照完整/前缀/注释/拒绝。200页面、四字符命中、无权限或公开限制有效为反例，不调用真实key或产生费用。\n\n来源：[保存帖1](https://x.com/i/status/1488533268274499586)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Crimson 五十工具与覆盖收据",
    "图把URL/IP/screens、WHOIS/CORS/zonetransfer、portscan、fuzz、JS、SSL、smuggling、SSRF等分三圈；正文说50+工具。图是任务地图，没有每阶段输入/完成结果。\n\n离线将阶段与scope、预算、输入输出和失败收据绑定，比较空输入、跳过和完整产物。工具数/架构图、未运行、失败被吞或越界资产为反例；任务标签不等发现数量。\n\n来源：[保存帖1](https://x.com/i/status/1488584375763492865)。"
  ],
  [
    "by-type/host-header.md",
    "IP source bypass 的 200 和长度差异",
    "图多个自定义IP/Forwarded类头都返回200，长度1345/1967/2316/2345不一，且包括与源IP语义无关的AccessControlAllowOrigin，没有原始基线和正文。\n\n静态追可信代理是否覆盖头、服务实际校验源和受保护动作，离线比较普通头、受信代理和不受信输入。软200、登录页、不同错误长度或头被忽略为反例；状态/长度变化不证明IP限制突破，不尝试真实受限后台。\n\n来源：[保存帖1](https://x.com/i/status/1488621872166092802)。"
  ],
  [
    "discovery/web-and-api.md",
    "Jira 路径清单按消费者分别审查",
    "完整列表含QueryComponent、ViewUserHover、dashboard REST、user picker与编码iframe路径；没有响应或版本实例。\n\n离线记录路由、认证、信息字段、模板上下文与权限合同，比较不存在、公开设计、安全编码/拒绝。默认路径/usernameAdmin/语法含弯引号、产品名或无消费者为反例；不能把路径全标为XSS/泄漏。\n\n来源：[保存帖1](https://x.com/i/status/1488730787021086720)。"
  ],
  [
    "by-type/idor-access-control.md",
    "隐藏参数、搜索和内部 AJAX 的权限合同",
    "正文建议Arjun/搜索、从响应找隐藏参数、internalAJAX访问他用户；图仅privatehiddenaccount/posts和profilepicture的报告标题。UI隐藏与服务器授权不是同一条件。\n\n自有两主体/两对象离线追每入口参数→分支→对象/字段/动作权限，比较合法本人、错对象、无参数与拒绝。参数存在、标题、公开头像、只客户端变化或统一权限正确为反例；不枚举真实私人数据，自动探参也需预算和范围。\n\n来源：[保存帖1](https://x.com/i/status/1488770038601756672)、[保存帖2](https://x.com/i/status/1488896481054511104)。"
  ],
  [
    "reporting.md",
    "Duplicate 与无法共享原报告的记录",
    "正文说很多XSS/IDOR duplicates，图解释previouslysubmitted且原报告含不宜共享信息。重复处理状态既不还原技术机制，也不保证报告人可访问原案。\n\n本地自有记录保留提交时间、实例/根因、证据和平台决定，比较同根因/不同消费者，资料缺失注明。单一平台、私有标签、拒绝共享或无技术交换为反例；不编造原案、不自动换平台或把重复当修复验证。\n\n来源：[保存帖1](https://x.com/i/status/1488838345514168320)、[保存帖2](https://x.com/i/status/1489566646746300416)。"
  ],
  [
    "by-type/mobile-android.md",
    "DIVA 改进计划与 InsecureShop 训练入口",
    "正文一条只是DIVA refinement计划，另一条介绍Kotlin InsecureShop的19+练习，未存实现或完成记录。\n\n把训练目标映射为输入、存储/IPC/WebView/权限等实际消费者和自有离线小样本；版本、环境、合法/拒绝与观察结果分别记。课程/应用名、计划、练习计数或没有运行收据为反例；靶场能力不等真实App漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1488866480355745794)、[保存帖2](https://x.com/i/status/1488905046691569668)。"
  ],
  [
    "experiment-design.md",
    "Flask API 靶场与 Android 取证资源的边界",
    "Fernbach描述以Flask练API OWASP top10，图只是仓库卡片；同帖Androiddiagnostics是独立外链。服务接口实验与设备采集有不同主体、权限和副作用。\n\n离线自有schema/合成采集记录绑定版本、字段、入口、期望行为，分别比较拒绝/空结果/正常。仓库名、top10标签或跨资源标题为反例；不补出未存源码，不安装靶场或连接设备。\n\n来源：[保存帖1](https://x.com/i/status/1489787270408257537)、[保存帖2](https://x.com/i/status/1489830234199265281)。"
  ],
  [
    "by-type/idor-access-control.md",
    "教师用户名前缀触发权限问题的最小对照",
    "附件邮件明确studentusername须以teacherusername开头并加字符；abc/abcX可触发，abc/def不行，修复已部署并请求确认。这是原视频遗漏的必要关系，未存代码和回归结果。\n\n自有合成用户名只改变相等/前缀/无关关系，静态核身份绑定与精确比较，保存角色/对象/动作。名字无关系、完全相等的合法本人、统一严格比较或拒绝为反例；不能认定具体SQL/正则根因或修复已验证，也不发确认邮件。\n\n来源：[保存帖1](https://x.com/i/status/1488896481054511104)。"
  ],
  [
    "by-type/xss.md",
    "og:image 到 SVG 缩略图的二次渲染",
    "正文连续两条说抓取链接metadata并将evilSVG作为缩略图；图保存og:image示例、卡片、遮挡对话框和StoredXSS viaSVGmetadata奖励通知。抓URL、存图和渲染是三段。\n\n静态核URL来源/协议、抓取/转换、存储域/MIME、img或document消费者、CSP及另一读者；离线自有无害SVG比较转码/安全图片/拒绝。只缩略图、img安全模式、本人打开SVG、错origin或无后续读者为反例；奖励不替完整执行链，不抓外部payload。\n\n来源：[保存帖1](https://x.com/i/status/1489128323582095364)、[保存帖2](https://x.com/i/status/1489128808225521664)。"
  ],
  [
    "expert-reasoning.md",
    "Log4j 与 ServiceDesk CVE 资源不是部署证明",
    "完整正文给两个历史CVE/仓库并笼统列版本范围，没有实际部署、配置或消费者。软件组件版本、调用路径和防护条件须独立确认。\n\n离线自有SBOM及配置对照公告适用条件、组件存在/不可达/修复版本。版本口号、工具链接、不同环境或无危险消费者为反例；不把历史RCE标签当当前目标已受影响，不运行归档PoC。\n\n来源：[保存帖1](https://x.com/i/status/1489146773709144066)。"
  ],
  [
    "impact-and-acceptance.md",
    "Pre ATO 的 informative 状态仍缺身份转换",
    "正文仅PreATO closedinformative，未存注册/邮箱验证、身份合并或会话转换。决定状态不能代替账户生命周期机制。\n\n自有离线注册状态机记录验证前后主体绑定、原会话和恢复分支，比较统一验证和拒绝。只有结案标题、无受害者转换或旧会话失效为反例；不从informative推可用ATO，不创建他人账号。\n\n来源：[保存帖1](https://x.com/i/status/1489159777582137345)。"
  ],
  [
    "by-type/host-header.md",
    "重置链接污染到 token 泄露需投递证据",
    "完整笔记建议Host/XForwardedHost/Referer，称nextrequest出现attackerdomain就偷到token。域名进入生成链接仅证明链接控制，仍缺真正邮件、访问者、token位置/可用性。\n\n离线自有合成重置记录比较固定可信baseURL、错来源、token绑定和无投递。域名字符串、自动预取、没有敏感token、未出站或单次失效为反例；不重置他人账户/发邮件，不将下一请求域名等同接管。\n\n来源：[保存帖1](https://x.com/i/status/1489197352518885381)。"
  ],
  [
    "reporting.md",
    "Bad Request 页面与 N A 争议分开",
    "正文称报告N/A并询问公开；图片只有浏览器BadRequest/malformed请求，没有安全交换或技术机制。\n\n离线报告记录原始输入、结果、期望合同、最小比较和处理/披露条件。错误页面、推测无安全团队、状态争议或未有影响为反例；不能从HTTP错误推漏洞，不自动联系/披露。\n\n来源：[保存帖1](https://x.com/i/status/1489203035381325828)。"
  ],
  [
    "by-type/idor-access-control.md",
    "invoice fetch item 的 JSON 与重置链缺口",
    "保存invoice/weakreset→ATO标题，图只有POST dashboard/invoices/fetch-item对象id及200JSON的billing/shipping/user/paid字段，敏感值已遮。没有两主体对照或reset交换。\n\n自有两个合成invoice比较本人合法、他对象和拒绝，固定会话与动作，单独核字段最小披露。合法本人200、仅字段名、标题或无resetconsumer为反例；JSON不证明账户接管，更不证明RCE，不枚举真实账单。\n\n来源：[保存帖1](https://x.com/i/status/1489103691219189761)、[保存帖2](https://x.com/i/status/1489220812762595331)。"
  ],
  [
    "source-audit.md",
    "Heaptrace 的 double free 演示与攻击可达性",
    "完整图C代码malloc后两次free，trace有第二次free警告、doublefree detected和异常退出status6，统计malloc1/free2；这是局部演示。\n\n离线合成调用图核分配/释放所有权、输入可达性、异常处理和真实部署；比较单次释放、安全转移及不可达分支。demo、崩溃、无攻击输入或不同allocator为反例；内存错误不自动RCE，不编译/执行未信任归档代码。\n\n来源：[保存帖1](https://x.com/i/status/1489225759118053389)。"
  ],
  [
    "by-type/ssrf.md",
    "请求走私图的 framing 与连接复用证据",
    "图画前后端同带ContentLength50/TransferEncodingchunked，后端另GETadmin与200/302，没有原始字节、完整chunk终止、配置或连接。另一帖仅headersmuggling外链。\n\n离线自有字节模型记录两parser的边界、实际body长度、合法/拒绝与复用，分header解释和requestframing。示意数字、截断帧、不同连接、服务器一致拒绝或单一200/302为反例；不能凭图认当前走私，不向真实共享连接注入。\n\n来源：[保存帖1](https://x.com/i/status/1489234267687497735)、[保存帖2](https://x.com/i/status/1489816518573670405)。"
  ],
  [
    "scope-and-rules.md",
    "自动化发现范围与测试范围分开保存",
    "正文指出自动枚举会产生outofscope域，并肯定工具能力；资产发现不自动带测试许可。\n\n离线把每阶段候选来源、当前明确归属/规则、过滤理由和实际输入绑定，比较关联域/第三方/允许资产。工具输出、相同品牌、历史scope或未核规则为反例；不能直接把全部发现交给后续主动扫描。\n\n来源：[保存帖1](https://x.com/i/status/1489266272500080650)。"
  ],
  [
    "by-type/ssrf.md",
    "DNS 先校验后再次解析的连接一致性",
    "正文及完整.NET图先Dns.GetHostEntry检查唯一allowlistedIP，sleep1000后WebRequest(url)获取响应。校验值未绑定到连接者，是DNS变化的候选条件；缓存/客户端行为仍须确认。\n\n离线自有解析记录比较不变/变化/多地址/拒绝，核实际连接地址、重试、跳转及TLS hostname/SNI验证。只第一次DNS、连接绑定已验证地址、每跳拒绝或无可控解析为反例；不是看到两API就认SSRF完成，不访问内网或metadata。\n\n来源：[保存帖1](https://x.com/i/status/1489280271640055809)、[保存帖2](https://x.com/i/status/1489280413948596226)。\n\n语义校核：[OWASP 连接到已验证地址](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)。"
  ],
  [
    "hunting-strategy.md",
    "广度工具与深度合同研究的收据",
    "正文建议一边优化工具一边选目标深挖，另帖强调漏洞而非工具。两类工作共享范围和时间预算，需要各自结果。\n\n记录候选来源/失败、优先合同/状态转换及最小对照，离线比较只有广度列表、无证据深挖和已闭合消费者。工具忙、主观信心或没有可验证差异为反例；不把后台运行当已完成，也不据工具身份评估漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1489297862597001219)、[保存帖2](https://x.com/i/status/1490798841867608064)。"
  ],
  [
    "expert-reasoning.md",
    "WMI registry 输出不证明初始授权或 AV 绕过",
    "两图显示命令完成、COMConsumer/EventFilter/Binding清理OK、权限列表及remove registrykey；正文称无需SMB/可绕AV。图没有起始身份、认证交换或安全产品日志。\n\n静态分已有远程执行、输出通道、清理、权限属性和检测结果；自有合成日志核前后状态。程序自述OK、某权限启用、缺检测器证据或已有合法管理员为反例；无需SMB不等无需认证，不执行横向/删注册表。\n\n来源：[保存帖1](https://x.com/i/status/1489346594138951685)、[保存帖2](https://x.com/i/status/1489350441251274752)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Shodan awk 第三字段与 nuclei 指纹等级",
    "完整管线Shodan domain→awk第三列→httpx→nuclei，图包含missingXFrameOptions、Akamai/Cloudflare、S3detect、Pulsepanel、robotstxt等标签及共享CDN。输出结构/主机归属未保存。\n\n离线结构化输入比较缺字段、丢端口、共享CDN和失败，保留每模板版本/匹配原始字段。标签、robots、缺头或登录页为反例；指纹不等可利用漏洞，第三列并非所有版本稳定契约。\n\n来源：[保存帖1](https://x.com/i/status/1489561303580565507)、[保存帖2](https://x.com/i/status/1489695240839589888)、[保存帖3](https://x.com/i/status/1491007448185933827)。"
  ],
  [
    "discovery/passive-and-services.md",
    "site 通配和品牌句子的归属候选",
    "正文给site:target.*及品牌完整句搜关联域，未存当下归属/许可。搜索词只产生候选，可包含旧域、镜像或第三方。\n\n离线保留查询/时间/命中内容、实体归属和当前规则来源，比较官方/镜像/无关结果。品牌相同、搜索排名、WHOIS联系或共享模板为反例，不扩大授权扫描范围。\n\n来源：[保存帖1](https://x.com/i/status/1489605878583992328)、[保存帖2](https://x.com/i/status/1490860571440590850)。"
  ],
  [
    "by-type/info-secrets.md",
    "归档扩展名 grep 不能认当前敏感文件",
    "完整管线wayback保存全集后grep.xls/xlsx/json/pdf/sql/doc/docx/pptx，正则未锚定实际path边界，可能匹配query/子串。没有文件正文和权限。\n\n离线分原URL、时间、path/query、当前字节、预期公开与字段敏感性，以自有公开/不存在/子串对照。历史扩展名、名单、第三方或正常公开文档为反例；不能把所有办公文件/JSON算数据泄露。\n\n来源：[保存帖1](https://x.com/i/status/1489940900167913472)。"
  ],
  [
    "by-type/idor-access-control.md",
    "UUID 可得性与对象授权分开证明",
    "完整tips图列users/all、user/list、users作为可能取得UUID的候选；另一图是1234→1235示意，正文称IDOR难找易利用。随机标识不会替代对象权限，列接口也未必存在。\n\n只用自有两个对象合法取得ID后，离线比较本人、他对象、无身份与统一拒绝；单独记ID来源。公开ID、猜测接口、随机不可得或只有示意为反例；列表可达不自动IDOR，不暴力枚举真实实体。\n\n来源：[保存帖1](https://x.com/i/status/1489941887641399300)、[保存帖2](https://x.com/i/status/1490249356284506115)。"
  ],
  [
    "by-type/file-upload.md",
    "CSV 上传到执行仍需读取应用链",
    "正文说CSVtext upload→RCE并链到恶意软件新闻，保存材料未给上传端、表格解析、外部跳转或执行程序。\n\n静态分上传验收/存储、CSV内容解析、后续读者、公式/链接与权限，自有无害文本与安全消费者对照。标题、下载、纯文本、禁公式或缺后续应用为反例；CSV格式本身不执行任意代码，不补出外链恶意软件链。\n\n来源：[保存帖1](https://x.com/i/status/1490007805532778498)。"
  ],
  [
    "discovery/passive-and-services.md",
    "SIP honeypot 时间窗计数不等当前恶意主体",
    "图SentryPeer SourceIPs一小时窗口、多个IP及一个高计数，另有UA/method/country/number菜单；正文宣称分布式badactors。计数和标签须保留采集范围与归因限制。\n\n离线合成请求核时间窗、重复/重试、来源/代理与去重键，比较正常/空窗/共享地址。高频、历史标签、共享NAT或只有dashboard为反例；不把IP名单认当前已入侵资产，不联系真实号码或运行SIP交互。\n\n来源：[保存帖1](https://x.com/i/status/1490071318804500484)。"
  ],
  [
    "source-audit.md",
    "IDAPython 字节解释与脚本执行权限",
    "图左侧idabytes/heads及XOR字符串代码，右侧IDA数据视图，正文介绍IDA/VSCode执行调试集成；未存连接实现/完整反编译结果。\n\n离线静态核架构、字节边界/编码、key来源、输出和脚本副作用，比较已知合成bytes、错key及越界拒绝。UI并排、局部解密代码或不可读小字段为反例；还原字符串不等漏洞/执行入口，不运行归档脚本。\n\n来源：[保存帖1](https://x.com/i/status/1490297882079076357)。"
  ],
  [
    "by-type/sql-injection.md",
    "SQL concat 到 prompt 的二次语法消费",
    "完整正文concat十六进制HTML/JS与user/database，图URL含UNIONALLSELECT且prompt显示DB字段/cookie，缺原请求基线。SQL表达式输出到HTML/JS是第二个消费者。\n\n静态追查询拼接/绑定→结果字段→模板编码→浏览器事件/CSP；自有无敏感标记比较参数化、纯文本和安全编码。仅query文本、本人console、图源不一致或无SQL差异为反例；XSS不提高SQL权限，不读取真实库/会话或保留秘密值。\n\n来源：[保存帖1](https://x.com/i/status/1490327622110572544)、[保存帖2](https://x.com/i/status/1490545858500509697)。"
  ],
  [
    "reporting.md",
    "报告影响需与实际能力证据相连",
    "正文强调reportimpact而不只名称，文章全文未保存。影响叙述应以主体、对象、动作、违反合同及限制为基础。\n\n用自有合成最小对照记录可复现行为、真实/潜在后果和修复反例，按当前规则提交所需字段。空泛critical、猜测接管、金额或没有证据为反例；标签不能替因果链，也不为追影响扩大测试。\n\n来源：[保存帖1](https://x.com/i/status/1490612401200242688)。"
  ],
  [
    "by-type/ssrf.md",
    "telnet SMTP 会话不能替 SSRF 起始消费者",
    "完整图是telnet本地0/25、Sendmailbanner、HELO/MAIL/RCPT/DATA及acceptedfordelivery；未存通过漏洞的入口、协议转发和真实接收证据。标题SSRF/SMTP/RCE不是一条完整链。\n\n离线分服务端可控网络消费者、可写协议字节、SMTP许可、队列与投递，以自有无发送的合成状态序列核拒绝/接受。直接telnet、localhostdemo、队列接受或无起始交换为反例；连通不等发信/RCE，不向真实SMTP发送。\n\n来源：[保存帖1](https://x.com/i/status/1490586620679966721)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Autorize 长度标签需要原始授权对照",
    "图有Orig/Modif/Unauth长度、Bypassed/Enforced/Isenforced问号，一些原长0；没有会话主体和响应正文。长度分类是启发式。\n\n自有两主体/两对象离线固定请求和会话，核真实字段、动作持久化与期望拒绝，分匿名/低权对照。零长/错误页、动态文本、公开资源、cookie未变或正常拒绝为反例；颜色不证明IDOR，更不证明RCE。\n\n来源：[保存帖1](https://x.com/i/status/1490644520580620296)、[保存帖2](https://x.com/i/status/1490973451254833152)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "多源 JS 管线的覆盖、覆盖写和清理风险",
    "两完整图聚合gau、wayback、gospider，grep.js排jsp/json、sort/uro/anew、anti-burl awk第四列，再LinkFinder/collector/rushSecretFinder；包含错误隐藏、动态bash、通配rm及追加输出。没有完整运行收据。\n\n只静态核逐段stdin/argv、URL/状态字段、query保留、来源scope、失败、去重/缓存与产物版本；离线正常/空/格式变化对照。未保存输出、字段错位、过滤漏项或旧缓存为反例；收集不等秘密有效，不执行动态脚本/删除文件。\n\n来源：[保存帖1](https://x.com/i/status/1490718207585386497)、[保存帖2](https://x.com/i/status/1491057108225503238)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Reverse WHOIS 被误称 reverse DNS 的证据",
    "正文说reverseDNS但实际viewdns链接是reverseWHOIS按邮箱；图2cmdSOA输出域名/共享AppleNS或空值。WHOIS联系、SOA/NS和反向IP解析是不同证据。\n\n离线记录输入、来源/时间、实体、域名与服务托管关系，比较共有provider/无SOA/无关联系。共享NS、电话号码样式域、历史邮箱或空值为反例；关联不证明企业所有，更不授予主动许可。\n\n来源：[保存帖1](https://x.com/i/status/1490726668385796101)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "Instagram 地理标记的历史时间与可见性",
    "图地图弹窗有picturelink、地点、2016timestamp和经纬度；正文说汇总所有geotag输出JSON，没有权限交换。历史照片位置不等当前位置。\n\n离线自有合成公开/私有/去标签照片核可见性、时间、字段最小化和去重；共享地点、旧照片、合法公开或无访问突破为反例，不抓真实个人位置/构建跟踪档案。\n\n来源：[保存帖1](https://x.com/i/status/1490796026961276931)、[保存帖2](https://x.com/i/status/1490999323408015363)。"
  ],
  [
    "by-type/xss.md",
    "document domain 标记与接管证据层级",
    "正文建议document.domain比alert1体现执行域，再升级ATO。域标记只能帮助定位执行上下文，不证明另一读者、身份能力或token可读。\n\n自有无害fixture绑定输入/消费origin/事件/CSP及主体，比较训练页、本人console、安全编码和后续受限消费者。弹框、域字符串、HttpOnly或无状态能力为反例；最小证据足够时止步，不为演示接管修改真实账户。\n\n来源：[保存帖1](https://x.com/i/status/1491030050371686409)。"
  ],
  [
    "by-type/idor-access-control.md",
    "二十位成员 ID 与移除组织 owner 的动作",
    "完整正文改20位alphanumeric成员id可删owner，图P2/1250/Unresolved标题，无前后成员状态。ID复杂度与组织/角色权限无关。\n\n自有合成组织两主体/角色静态核membership与delete合同、最后owner约束和跨组对象，比较本人许可/错组/低权及拒绝。可见ID、按钮、奖励或未有持久化为反例；不删除真实成员，报告未解决不等修复完成。\n\n来源：[保存帖1](https://x.com/i/status/1491058544590077954)。"
  ],
  [
    "by-type/ssrf.md",
    "AutoRepeater 不能替回调主体与请求合同",
    "正文只有用AutoRepeater找SSRF，没有替换规则或响应。重复请求是执行方式，不是消费者证据。\n\n离线自有请求模型固定原参数、每次改动、时间、唯一标记、重试和响应源，比较普通/拒绝/不出站。工具名、重复次数、未归因OOB或浏览器触发为反例；不自动重放真实历史请求。\n\n来源：[保存帖1](https://x.com/i/status/1491067289088987140)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "OTX 第一页 URL list 的分页和材料等级",
    "完整图limit100/page1→jq URL字段，返回example.com样例PDF/admin/login/跟踪query和奇怪信息字段。没有分页总数、当前正文或敏感权限。\n\n离线保存原始页/时间/source、分页完成/失败、path/query和归属，再区分候选文件/当前字节/秘密能力。第一页、样例、历史URL、字符串名字或未下载为反例；不能称全部敏感文件已找，不调用OTX/访问真实秘密。\n\n来源：[保存帖1](https://x.com/i/status/1491073442556579841)、[保存帖2](https://x.com/i/status/1491085963086692352)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "noshell 登录限制与 glob 展开的不同层",
    "正文声称已有commandinjection、账户noshell/WAF后用通配路径，保存拼写/e*c/p*s*we未必匹配期望文件。登录shell限制不自动决定应用进程能否消费命令。\n\n静态追字段→命令构造→shell或argv→glob展开→执行权限/输出，用自有无敏感路径比较literal、空匹配、多匹配和拒绝。拼写错误、无shell、目录受限或无真实输出为反例；不运行归档载荷/读取系统文件。\n\n来源：[保存帖1](https://x.com/i/status/1491086964082511873)。"
  ],
  [
    "by-type/xss.md",
    "Blind XSS fired 邮件与所有表单的范围",
    "正文称developerpanelstoredBXSS并建议每表单都注入，图仅两条截断XSSHunterfired通知，没有payload、主体或浏览器上下文。\n\n离线自有表单按存储/邮件/triager/浏览器消费者绑定唯一标记、时间和读者；普通/安全编码/重复标记/延迟回调对照。通知、扫描器/本人触发、无敏感能力或未经许可表单为反例；不普遍提交载荷、不向外部hunter发数据。\n\n来源：[保存帖1](https://x.com/i/status/1491094277791055872)。"
  ],
  [
    "scope-and-rules.md",
    "平台自身计划与 claim token 标题",
    "正文说找不到项目就测试平台本身，图只是Bugcrowd claimtokenexposed/300奖励标题。平台也是独立项目，须核其当前资产、规则和报告合同。\n\n离线记录当前明确范围、候选材料消费者和自有合成受限/公开值对照。平台身份、赏金图、旧计划或未知权限为反例；不把项目授权扩展到平台、不使用claimtoken。\n\n来源：[保存帖1](https://x.com/i/status/1491115326263947264)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "OAUTHScan 十项检查与协议消费者",
    "正文说扩展含10+OAuth/OpenID检查，图只有仓库卡片；具体规则/版本/结果未保存。\n\n离线自有协议记录client/redirect、state/nonce、code/token绑定与实际分支，合法/错绑定/拒绝对照。工具数、OAuth标签、只UI或无服务端结果为反例；不补出10条未存实现、不安装运行扩展。\n\n来源：[保存帖1](https://x.com/i/status/1491139771607191552)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "EDRHunt 帮助页是本机枚举能力",
    "完整CLI图列services/processes/registry/drivers及all/scan、单项flags；结尾只输入scan，无结果。检测已装软件、其运行状态和实际阻断不同。\n\n离线自有资产清单比较安装/未运行/权限受限/误识别，记录版本和字段来源。帮助页、残留service、进程名或无检测日志为反例；不证明安全软件失效/绕过，不运行设备扫描。\n\n来源：[保存帖1](https://x.com/i/status/1491158609153060864)。"
  ],
  [
    "impact-and-acceptance.md",
    "Grafana 零日措辞与已标 CVE 的状态",
    "正文称两个0day/最快1hour并说每IP，图却列CVE2021-43798、PathTraversal、triagedopen/high。零日标签、已知编号、实例受影响和完成修复不同。\n\n离线核保存时间、产品/版本/路由/消费者、重复根因和当前scope，比较修复实例/不受影响/权限拒绝。triage速度、报告标题、IP数量或未有原始交换为反例；不能当新0day证明或全网IP测试许可。\n\n来源：[保存帖1](https://x.com/i/status/1491184283020857346)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Kafka 叙述与 ZooKeeper 2181 标题分开",
    "正文说KafkaP1，图只有UnauthorizedZooKeeper/2181、P1triaged/stillassessed，没有认证或读写交换。相关组件不能直接互换漏洞证据。\n\n离线自有部署关系分别记录Kafka/ZooKeeper、版本/暴露入口、身份/ACL和最小无副作用能力，正常/拒绝/不关联对照。端口、标题、标签或没有组件消费者为反例，不连接真实协调服务/读取节点或写状态。\n\n来源：[保存帖1](https://x.com/i/status/1491265400474316804)。"
  ],
  [
    "by-type/authn-session.md",
    "个人资料 JSON 与 full ATO 的能力缺口",
    "保存fullATO/RCE宣传，图实际200Successful个人profile含姓名、联系方式、tenant/landlord/status/securityid等已遮字段，没有登录、重置或会话变换。\n\n自有合成两主体静态核对象归属、字段预期可见及访问合同，另建认证转换证据。字段名/本人合法profile、标题、redaction或无身份改变为反例；个人信息可见不等接管，更不等RCE，不复用真实数据。\n\n来源：[保存帖1](https://x.com/i/status/1491386446409703433)。"
  ],
  [
    "by-type/waf-bypass.md",
    "WAF Tester 单上下文与真实规则集",
    "完整图为WAFTester，明确globalHtml/attributeHtml、每次单context限制，弹框显示1；正文怀疑非真实Cloudflare。训练站、真实边缘规则和目标后端上下文须独立绑定。\n\n离线记录实例/规则版本、编码层、输出上下文、请求与浏览器CSP，比较安全编码/阻断/控制变量。训练页、console、规则未知、无原始交换或仅logo为反例；alert不证明所有当前部署可绕。\n\n来源：[保存帖1](https://x.com/i/status/1491390319853973504)。"
  ],
  [
    "reporting.md",
    "管理项目七阶段与成熟度百分比的限制",
    "完整推广图列注册、经理、launch、skills、scantriage、validate、reportremediate七阶段，以及private/public规则和75/100模型宣传。图没有真实测试覆盖/修复回归。\n\n本地自有项目将接收、复现、资格、修复和回归分别绑定证据/时间，记录范围、许可和阶段失败。宣传百分比、邀请人数、支付模型或未有产物为反例；阶段名不证明组织安全成熟，更不证明所有漏洞已修。\n\n来源：[保存帖1](https://x.com/i/status/1489147392402374660)。"
  ],
  [
    "by-type/business-logic.md",
    "负数量负总额和 Paid 发票不等免费完成",
    "保存图片是数量负1、unitprice与total负50000IDR的发票，标Paid/GoPay；没有创建请求、服务端价格计算、库存/账本或交付证据。正文free与RCE标签未建立链。\n\n离线自有订单状态机比较正/零/负数量、服务端重算、拒绝和账本一致性，只用合成金额。客户端发票、显示Paid、退款/测试记录或无持久化为反例；不进行真实购买、支付/退款或推执行权限。\n\n来源：[保存帖1](https://x.com/i/status/1489512080147316740)。"
  ],
  [
    "by-type/xss.md",
    "image URL 弹框与 iframe SSRF 标题",
    "完整图地址含image?url外部图片URL，页面弹框显示短字串，没有保存请求/iframe/服务端抓取。正文把SSRF/XSS/RCE同时标签化。\n\n离线自有请求和DOM模型分别核URL被谁抓取、数据进入何上下文、浏览器origin/CSP和实际无害执行。弹框、本人console、纯图片、无服务端网络或错误消费者为反例；XSS不自动SSRF/RCE，不请求外部payload。\n\n来源：[保存帖1](https://x.com/i/status/1489913389748875268)。"
  ],
  [
    "discovery/passive-and-services.md",
    "GitHub 代码搜索命中与材料生命周期",
    "正文介绍grep.app正则搜索及当时仓库数量，没有具体命中内容、所属项目或有效凭据。历史索引容量不等当前覆盖。\n\n离线自有合成索引保留commit/文件/行、时间、fork/upstream及字段预期可见；比较样例、过期、公开标识与受限材料。搜索命中、来源不明、失效值或无权限consumer为反例，不查询真实秘密/复用key，不能从数量宣称所有仓库已覆盖。\n\n来源：[保存帖1](https://x.com/i/status/1490569524994793474)。"
  ]
]
ids={pid for row in json.loads((W/"batch-0121.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert len(urls)==106 and all(pid in ids for pid in urls)
assert len({title for _,title,_ in facets})==len(facets)
grouped=defaultdict(list)
for f,title,body in facets:
 p=T/"references"/f
 assert p.is_file() and ("## "+title) not in p.read_text(),(f,title)
 grouped[p].append("\n\n## "+title+"\n\n"+body+"\n")
community=T/"references/research/community-distillation.md"
marker="\n## 首轮提炼范围与未采纳内容\n"
c=community.read_text();assert c.count(marker)==1
routes=[]
for f,title,body in facets:
 summary=body.split("\n")[0].split("。")[0]+"。"
 summary=summary.replace("|","｜")
 assert "|" not in summary and "\n" not in summary
 routes.append(f"| {title} | {summary} | [方法条目](../{f}) |")
for p,parts in grouped.items():p.write_text(p.read_text()+"".join(parts))
community.write_text(c.replace(marker,"\n"+"\n".join(routes)+"\n"+marker,1))
print("Added",len(facets),"facets/routes to",len(grouped),"topics;",len(urls),"batch-bound URLs")

