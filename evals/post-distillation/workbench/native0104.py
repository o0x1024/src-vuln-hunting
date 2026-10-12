"""Append explicitly reviewed 0104 facets; no source execution."""
from pathlib import Path
from collections import defaultdict
import json,re
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
W=T/'evals/post-distillation/workbench'
facets=[
  [
    "cloud/cloud-misconfiguration.md",
    "AWS地址段匹配与租户及桶地域的分别归属",
    "onaws图把IP匹配到AWS subnet、EC2服务和eu-west-1。此输出只说明该版本数据中的地址段匹配；共享云地址、租户账号、正式测试范围和某个S3桶的地域仍各需对应证据。\n\n保留数据版本/时点、输入域名的解析结果及实际匹配记录，将provider归属作为候选分类。域名多地址、CDN共享或陈旧网段是反例；不能从EC2地域补桶地域或把所有同云地址纳入范围。本次没有解析、扫描或访问云资源。\n\n来源：[保存帖1](https://x.com/i/status/1409788704504225797)。"
  ],
  [
    "targeted-fuzzing.md",
    "机器学习WAF反馈队列的评分与有效变异",
    "WAF-A-MoLE架构图展示mutation pool、priority queue、adapter与Target WAF反馈。低检测分数可能只反映模型特征变化；是否保留原输入语义、经过真实解析、到达目标消费者及发生安全影响是独立结论。\n\n比较时固定输入集合、版本、预算与有效变异分母，记录被拒/无效/未执行分支，并设置语义对照及未参与优化的样本。改变成无害输入、仅适配器误报或离线评分都不能计绕过。本次只分析图，没有运行变异器或WAF探测。\n\n来源：[保存帖1](https://x.com/i/status/1409863312607789056)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "localhost代理开关与实际浏览器流量归属",
    "旧帖将Firefox的network.proxy.allow_hijacking_localhost开关推荐给localhost拦截问题。这是相关浏览器代理配置的线索，不代表原生应用、其他浏览器或所有协议流量都进入代理；当前配置、绕过列表和网络栈仍需核对。\n\n在获准流程中把发出请求的进程、URL、有效代理/PAC与TLS信任条件绑定到实际代理历史。只有页面加载或代理监听成功不能计流量已采集；历史中没有请求也不能当作目标拒绝。不要把单个偏好项视作一键解决方案。本次未改变代理或系统设置。\n\n来源：[保存帖1](https://x.com/i/status/1410005852942221314)。"
  ],
  [
    "by-type/idor-access-control.md",
    "哈希对象ID的字节契约与授权不变量",
    "seq到hashit再ffuf的管线用整数派生候选ID；算法名以外，确切输入字节、换行、字符编码、前导零及输出表现都决定是否对应实际对象。把整行、数字文本或去换行后的文本哈希可能不同。\n\n在既有获准材料中绑定编码前后的受控对象及服务端最终解析值，然后保持主体/动作不变核对所有者或角色规则。编码只改变表示，不能提供对象授权；无法映射、严格格式拒绝或本来公开对象是反例。本次未生成ID集合或运行枚举。\n\n来源：[保存帖1](https://x.com/i/status/1410217894802243589)。"
  ],
  [
    "by-type/api-property-pollution.md",
    "JSON形状、查询操作符与Content-Type消费者",
    "API清单同时推荐数组/对象、布尔/null/数值、重复键、user[]及$ne形状。接受JSON、切换Content-Type和将对象解释为数据库查询操作符不是同一件事；每个值还可能被严格schema拒绝、转换成字符串或直接忽略。\n\n追踪解码后的类型、框架绑定、实际查询构造及授权对象，在相同受控主体/对象下改变一个维度，记录拒绝、忽略和真实语义差异。XML支持不证明DTD处理；路径含竖线也不自动代表Ruby命令执行。旧API/移动入口首先仍受正式范围约束，本次未发变异请求。\n\n来源：[保存帖1](https://x.com/i/status/1410423706799775749)。"
  ],
  [
    "discovery/web-and-api.md",
    "robots文本清洗的误截断与词表原始语义",
    "robots管线图的grep/awk/cut实际生成isallow等词：包含Disallow的注释也被收集，第二字段再无条件删首字符会把字段名而非路径截坏。另一robotstxt/cleanpath/anew示意也需明确stdin究竟是URL还是域名。\n\n保留文件与宿主、User-Agent组、有效指令/注释、原模式及每步输入输出；anew去重不能丢宿主或把共享输出当完整覆盖。先按实际格式验证解析，再作范围内候选词表。已有专题中的robots分组/模式规则适用；BAC确认邮件不补该管线找到的具体漏洞，本次未执行抓取。\n\n来源：[保存帖1](https://x.com/i/status/1410481151433576449)、[保存帖2](https://x.com/i/status/1410661328977600517)、[保存帖3](https://x.com/i/status/1411445636042563587)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "CDX时间戳到重放URL与全文获取的不同阶段",
    "Wayback示意先查询CDX时间戳，再由bash echo组装重放URL。这个后段只输出字符串，即使设置xargs并发也不能计已下载所有历史robots正文；原查询HTTP与重放HTTPS还改变了scheme。\n\n保留原CDX响应格式、源URL/scheme、时间窗、错误/空行及实际输出类型，分开索引结果、生成候选和已获取字节。错误HTML被当时间戳、去重丢归属或历史禁止路径被当当前权限都是反例。未保存全文按用户口径计覆盖，无需补抓；本次没有运行P500管线或访问重放地址。\n\n来源：[保存帖1](https://x.com/i/status/1410540754921918470)。"
  ],
  [
    "by-type/authn-session.md",
    "SSH协议banner与任意公钥认证的证据界线",
    "旧帖把生成密钥、netcat看到SSH2 banner与所谓Race Hazard绕过串在一起。banner只表明协议入口响应，不能证明自生成公钥已写入授权列表、签名挑战通过或获得远端会话。\n\n按保存材料分开主机身份、实际认证方法/允许key、认证完成日志及会话有效主体；正常握手、既有授权key或密码成功都不证明竞态。缺原始认证收据时保留未证声明，不将P1营销文字转成操作指南。本次未创建密钥、连接SSH或登录账号。\n\n来源：[保存帖1](https://x.com/i/status/1410711234962497539)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "DNS载荷参数与线上标签及分片重组预算",
    "DNSteal帮助写payload大小4..240、自选server/target、TcpOnly及延时。工具参数可能是编码前字节、总片长或多个标签组合，源码未保存时不能把240解释成合法单标签。\n\n[RFC1035](https://www.rfc-editor.org/info/rfc1035/)约束单标签至多63 octets及包含长度字段的完整域名至多255 octets。实际构造还须算编码膨胀、根/后缀与序号；绑定分片身份、顺序、重试与校验后才能计合成数据完整到达。仅DNS查询日志不证明文件读取或完整外传，本次未发DNS或采集真实文件。\n\n来源：[保存帖1](https://x.com/i/status/1410723941480419329)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "source配置、保留环境与侦察任务的权限扩大",
    "Lazyrecon图导出存储路径、GitHub token及Discord webhook变量，使用source加载配置，再sudo安装或sudo-E运行通配目标。source会把配置当shell代码，环境保留及提权还可能改变可读数据、外发目的地与动作权限。\n\n对获准工具记录配置字节/来源、真正argv与展开目标、有效身份和下游输出；区分普通数据配置与可执行配置。帮助图不证明安全默认值或已运行，日志/通知也不能复制真实token。本次未加载配置、执行安装或发送webhook。\n\n来源：[保存帖1](https://x.com/i/status/1410950534505324546)。"
  ],
  [
    "by-type/deserialization-rce.md",
    "反序列化标题与PHP命令字段及Node解析栈的分离",
    "同帖的PHP图直接POST cmd并显示www-data输出，未显示序列化对象；Node图出现JSON.parse/unserialize与500 Unexpected end JSON。前者不能由标题改称反序列化漏洞，后者只定位输入/解码候选，尚未补对象构造或危险调用。\n\nCookie图同时Welcome Admin和Please Login，不能计认证完成；扫描图与请求图私网IP/日期不同，需先绑定实例/制品/时点再关联。PHP Content-Length与可见正文不一致也不能静默修成可重放PoC。无原始材料的gadget、root与接管均保留未证，本次未执行代码或复制Cookie。\n\n来源：[保存帖1](https://x.com/i/status/1411248538005082113)。"
  ],
  [
    "by-type/xss.md",
    "reCAPTCHA脚本文本、DOM选择器与可执行上下文",
    "SQLMAP求助图在浏览器显示reCAPTCHA JavaScript文本，包含getElementById的hello选择器与隐藏token字段。参数名/字符串出现在JS或页面、选择器选中元素与攻击者代码执行不同，工具类型标签不能代源/汇分析。\n\n绑定原始响应Content-Type、实际脚本消费者、字符串编码与DOM分支，排除纯文本展示、静态代码或只改变元素选择。sitekey的出现不自动说明秘密泄漏或验证码可绕；第三方脚本本来正常运行也不证明注入执行。本次未运行页面JS、使用验证码key或提交请求。\n\n来源：[保存帖1](https://x.com/i/status/1411268255835062281)。"
  ],
  [
    "by-type/mobile-android.md",
    "二维码文本到scheme分派和WebView权限的链条",
    "两帖QR提示扫码javascript确认，但图没有实际设备或扫码结果。二维码解码出文本、应用接受URL scheme、进入WebView或其他消费者以及执行时origin/原生bridge权限是各自条件。\n\n在获准自有制品中绑定扫码入口、分派策略、实际URL和WebView配置/调用点，记录被当文本、被scheme白名单拒绝、转外部应用及不同origin等反例。不能从可生成二维码认任意Android应用XSS，本次未解码执行二维码或操作设备。\n\n来源：[保存帖1](https://x.com/i/status/1411287363112902656)、[保存帖2](https://x.com/i/status/1645396728357564418)。"
  ],
  [
    "by-type/mobile-ios.md",
    "iOS扫码入口的URL分派与脚本消费者",
    "二维码提示本身不证明iOS扫码应用会导航javascript scheme。先区分扫描器返回文本、调用方URL过滤、打开外部应用以及WKWebView实际导航/脚本消费者，不能借Android推断iOS权限。\n\n仅在获准制品材料中绑定系统/SDK版本、用户交互、实际origin和bridge暴露；文本展示、scheme拒绝或系统外部浏览器是反例。两张同类提示图均已看，仍不补实际设备测试，本次未扫码或执行脚本。\n\n来源：[保存帖1](https://x.com/i/status/1411287363112902656)、[保存帖2](https://x.com/i/status/1645396728357564418)。"
  ],
  [
    "by-type/authn-session.md",
    "省略username与保留Bearer的身份对照",
    "API misconfiguration两图把username改空，但仍保留同一Bearer头；响应数据被黑块遮住。改变一个业务选择字段不等于移除认证，也不足以证明读出全部PII或获得另一账号会话。\n\n绑定Cookie/Bearer及其他有效身份、参数解析后的主体、对象字段与实际响应，不将空字段自动认anonymous。默认返回当前主体、认证header仍生效、字段被忽略和遮挡数据未知是反例。People API Enable卡片同样不证明全组织Directory权限，本次没有用token或枚举用户。\n\n来源：[保存帖1](https://x.com/i/status/1411313443475378176)、[保存帖2](https://x.com/i/status/1411312877479370752)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "phpunit路径与phpinfo响应的版本及执行归因",
    "图请求phpunit eval-stdin路径，带GET正文并显示phpinfo/PHP7.4.20。这是动态执行的候选证据；PHP运行时版本不是phpunit包版本，截图也不补公开无认证、请求未经工具修改或同路径静态页的排除。\n\n用获准已有制品确认实际路由/暴露、包版本/实现、完整身份载体与原始响应来源；将脚本解释、信息输出和操作系统命令权限分开。正常受保护调试页、固定phpinfo或无关运行时版本都是反例。本次未执行PHP、读取配置或复制会话字段。\n\n来源：[保存帖1](https://x.com/i/status/1411517028012158976)。"
  ],
  [
    "by-type/xss.md",
    "document.write标记、同栈重复行与报告状态",
    "DOM Invader图document.write显示三条同栈值，标记位于属性和脚本边界；另一图两报告仍Triaged/Still being assessed。可控值进入汇、实际执行、独立根因数量和最终处理状态不能互换。\n\n绑定原输入、真实输出上下文、变换及消费者调用栈，确认工具未自行补注入，再按根因/对象/读者去重。三条记录可能同一调用，评级不是当前修复重测；只有标记或未经原始链验证的alert图不计完整发现。本次未执行载荷或运行XSS Rush。\n\n来源：[保存帖1](https://x.com/i/status/1411669682017366021)、[保存帖2](https://x.com/i/status/1411972248819306497)。"
  ],
  [
    "by-type/mobile-android.md",
    "DEX内存采集的进程选择与完整性范围",
    "frida-dexdump帮助说明默认前台、未指定PID时可能dump全部进程，并提供spawn、delay和deep选择。这些选项影响采集主体和时点，deep更慢也不代表找回所有有效DEX。\n\n保留获准包/进程PID、启动代际、采集配置、片段字节哈希和后续格式校验；区分未采集、不可读、截断/重复映射与真实不存在。内存片段、完整代码或敏感数据仍需各自证明，不能从工具帮助算移动漏洞已测。本次未运行Frida或导出设备内存。\n\n来源：[保存帖1](https://x.com/i/status/1411675318281199618)。"
  ],
  [
    "by-type/sql-injection.md",
    "H2表单、FILE_READ与自定义alias的分段证据",
    "四图从H2登录模板、自选嵌入库路径/用户名到FILE_READ结果及1.4.196 CALL REVEXEC的uid0输出。表单预填不是连接既有目标库成功；读passwd样式内容不证明JVM以root运行。alias定义/创建路径及同实例关联未保存，不能拼成通用无认证RCE。\n\n[H2 FILE_READ说明](https://h2database.github.io/html/functions.html#file_read)与[CREATE ALIAS说明](https://h2database.com/html/commands.html#create_alias)分别列出管理权限；当前文档用于条件核对，不据此补旧图全部版本。绑定数据库身份、实例/路径、有效权限及函数实现、OS身份和原始结果来源。正常授权管理员或自建本地库是反例，本次没有连接H2、运行SQL或生成alias。\n\n来源：[保存帖1](https://x.com/i/status/1412062699840688133)。"
  ],
  [
    "by-type/authn-session.md",
    "退订能力与完整设置编辑的不同权限",
    "旧提示称退订邮件含目标email可到设置页，且并非所有网站适用。允许一次退订的设计与修改账号全部设置、其他用户数据或会话身份是不同权限；持有某能力令牌也不代表拥有该账号。\n\n沿保存链绑定邮件链接/token、主体、字段/动作及最终持久状态，区分明确允许的免登录退订、只读页面与额外设置越权。改email不产生权威变更、令牌绑定正确或只是公开设置说明是反例。本次未退订、发邮件或修改真实设置。\n\n来源：[保存帖1](https://x.com/i/status/1411934771958083586)。"
  ],
  [
    "by-type/open-redirect.md",
    "DOM URL成员清单与导航及HTML网络消费者",
    "DOM列表把location及其host/path/search等读取成员，与assign/replace/open、srcdoc、AJAX和XHR一起列作open URL参数。它混合输入来源、导航、HTML解析及网络请求，任一名字出现不能统一认开放跳转。\n\n绑定实际赋值/调用及参数来源，再分别判断导航目的地、HTML执行上下文、请求发起origin与返回数据可读性。只读location或请求被浏览器策略拦截是反例。退订重定向帖也缺真实Location/最终目的地，自己的子域不能自动扩大项目范围，本次未跳转或发请求。\n\n来源：[保存帖1](https://x.com/i/status/1412277402177355777)、[保存帖2](https://x.com/i/status/1412662571417489408)、[保存帖3](https://x.com/i/status/1412662574231945225)。"
  ],
  [
    "by-type/authn-session.md",
    "语音信箱接管概念与枚举failure响应",
    "Uber帖声称通过语音信箱取得OTP，图实际是driver RPC手机号输入及Intruder多个200，选中JSON却是failure/Multiple drivers found。这可能是账户枚举候选，不能从状态码或RCE标签认接管已完成。\n\n将号码/账号存在性、OTP投递通道、信箱认证控制、挑战有效期/绑定和最终服务端会话分成证据边。知道某号码对应账户不代表控制信箱，旧token/固定错误也不代表接管。本次不复制手机号/CSRF字段，未枚举、呼叫信箱或提交OTP。\n\n来源：[保存帖1](https://x.com/i/status/1412302374031396864)。"
  ],
  [
    "source-audit.md",
    "ETW服务RUNNING、空日志与检测能力对照",
    "TiEtwAgent图显示服务RUNNING、进程列表和空agentlog，未显示注入事件被记录。进程存在、采集器运行、provider事件到达、判定告警及准确归因是不同层，空日志既不能认检测成功也不能认没有事件。\n\n在获准实验材料中绑定provider/session、进程代际、采集权限/配置、事件丢失与时点，设置合成阳性和正常行为对照，再核对完整收据。没有provider数据、日志路径错误或过滤丢弃都应计未知。本次未注入内存、启动agent或操作进程。\n\n来源：[保存帖1](https://x.com/i/status/1412400033958436873)。"
  ],
  [
    "by-type/idor-access-control.md",
    "JSF选择对象、ViewState与删除后的权威状态",
    "ESET帖称创建受控victim user后替换欢迎消息ID并删除。现存两图是局部ajax请求，涉及selection、ViewState及列顺序/渲染字段，缺完整身份、响应和删除后权威状态；框选数字不直接证明最终对象越权。\n\n将操作者与两主体自建消息、选择器解析值、实际删除授权对象和持久读回绑定，保留不存在对象/正常授权/仅UI消失等对照。局部渲染成功或可改ViewState字符串不代对象授权。本次未重放状态令牌、删除消息或操作用户。\n\n来源：[保存帖1](https://x.com/i/status/1412413763513430022)。"
  ],
  [
    "by-type/authn-session.md",
    "企业邮箱资格与quoted local及投递解析",
    "邮箱图包含大写域、quoted local、comment和SMTP注入声明。语法是否接受、展示规范化后的域、实际投递收件人与企业账号资格是不同条件；将company子串放local part不代表属于企业域。\n\n绑定原始输入、每层解析结果、实际收件路由与资格判断，区分local/domain处理；大写域正常等价不是绕过证据。被严格解析拒绝、正常合法公司地址或只有UI变化都是反例，换行注入仍需真正SMTP消费者。本次未尝试注册、投递或注入邮件。\n\n来源：[保存帖1](https://x.com/i/status/1412418741032390656)。"
  ],
  [
    "by-type/xss.md",
    "DOM Invader合成origin与真实外部发送窗口",
    "DOM Invader介绍和[官方消息设置](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/settings/web-messages)说明工具可修改origin、注入canary及生成消息。这能定位处理器候选，但在工具内接受合成origin不自动证明外部窗口可发送相同事件/数据到相同消费者。\n\n保留原消息与工具变更、event.origin/source/data访问、目标窗口及调用栈，区分读取属性和真正完整验证。在获准自有环境用真实发送origin/窗口能力与严格验证对照判断可达；缺帧能力、源窗口检查拒绝或只本地合成事件是反例。本次未造消息或运行生成PoC。\n\n来源：[保存帖1](https://x.com/i/status/1412426169576787972)。"
  ],
  [
    "by-type/ssti.md",
    "算术模板标记与盲脚本回连的两个消费者",
    "帖将48*53模板候选与盲脚本标签组合。看到回连不能倒推模板求值；看到数字也须排除输入原文、固定文本或其他计算，内网关键端点更需要真实后台读者来源。\n\n给模板输入、求值输出、HTML嵌入与脚本消费者分别保留合成标记/时点，绑定模板引擎、转义上下文和实际读者身份。独立证据成立后再判断链，不能把所有复合字符串称内部SSTI；本次未执行模板、HTML或回连脚本。\n\n来源：[保存帖1](https://x.com/i/status/1412437792118947841)。"
  ],
  [
    "expert-reasoning.md",
    "邮箱字段的多类字符串与消费者路由矩阵",
    "邮箱建议并列XSS、模板/SQL、带外域名、&email参数和通配符。字段相同不代表消费者相同：邮箱语法/投递、HTML展示、模板渲染、查询构造和URL/HTTP请求需要分别追踪。\n\n记录原始与解码/规范化后的值、哪层校验和哪层实际消费，仅对已观察分支提出假设。邮件MX/DNS解析不是HTTP SSRF，百分号作为字面字符不是SQL通配符，参数样式文本也可能只是邮箱字符串。严格拒绝、参数绑定或安全展示是各自反例。本次未发送邮件、触发DNS或执行任何载荷。\n\n来源：[保存帖1](https://x.com/i/status/1412495573127630849)。"
  ],
  [
    "experiment-design.md",
    "AV未检出计数与制品及动态运行的不同证据",
    "Sharperner配图声称2021一次26引擎扫描0检出，并混有广告。无输入制品哈希、引擎/签名配置、扫描完成收据或动态行为，不能推广成普遍隐蔽、运行成功或安全。\n\n比较仅限获准制品与固定采集时点，记录静态/动态阶段、有效引擎分母、失败/未运行和合成对照；0检出与0引擎有效完成不同。旧截图不能补今天结果，扫描未报也不排除恶意行为。本次未生成shellcode、运行二进制或上传扫描服务。\n\n来源：[保存帖1](https://x.com/i/status/1412535955765055493)。"
  ],
  [
    "by-type/authn-session.md",
    "2FA清单的挑战绑定与本地成功标志",
    "十项图混合改response/status、代码重用/跨用户码、重置关闭2FA、缺频控和null码。每项对应不同挑战/状态消费者；本地success=true不能代服务端授权，存在null输入也不证明被接受。\n\n固定受控主体、挑战用途/标识、过期/消费状态、所有身份载体及最终受保护动作，分别判断重复码正常窗口、错误码拒绝、恢复流程批准降级和真实越权。列表不计已成功的十种绕过；已有专题中的响应修改反例适用。本次未猜验证码、禁用2FA或尝试账号恢复。\n\n来源：[保存帖1](https://x.com/i/status/1412622361757581312)、[保存帖2](https://x.com/i/status/1412326524330549251)。"
  ],
  [
    "by-type/authn-session.md",
    "用户名Base64令牌与服务器认证的不可伪造契约",
    "API帖示例把access_token放payment查询串，另图说token仅为用户名Base64。可逆编码不是认证不可伪造性，但示例字面值、长TTL或公开接口仍不能单独认实际可伪造会话/越权。\n\n追服务器是否验证签名/随机能力/状态、绑定的主体/权限/对象及有效期，区分标识符和真正凭证；不要复制示例作真实token。query可能进入日志/历史的风险与实际泄漏还需已有传播链，额外服务器校验或本来公开资源是反例。本次未用token、访问payment或读账号数据。\n\n来源：[保存帖1](https://x.com/i/status/1412688013654585345)。"
  ],
  [
    "by-type/info-secrets.md",
    "Git索引推导对象路径与目录列表和源码完整性",
    "GitDump图逐项Fetching index/refs/logs，Parsing Index后继续objects路径。HTTP目录列表关闭不代表已知文件路径不可读，但这些日志没有响应状态、字节或复原结果，也不能计源码完全泄漏。\n\n绑定获准原始响应与制品哈希，区分真实Git元数据、登录/错误统一页及缺失对象，保留索引指向的对象集合和实际完整性。FETCH_HEAD等文件名命中、root终端提示或Fetching文字不补远端数据读权。本次未下载Git对象、运行dump工具或接触代码中的秘密。\n\n来源：[保存帖1](https://x.com/i/status/1412762403545268224)。"
  ],
  [
    "by-type/sql-injection.md",
    "数据库网络例程与HTTP和目录解析回连的分流",
    "旧SQLi到SSRF帖把Oracle UTL_HTTP.request和MSSQL xp_dirtree共同写作HTTP。例程名与SQL注入存在不证明相同协议、可调用权限或网络请求成功；目录解析产生的名字解析/网络行为不能直接归类HTTP响应读取。\n\n[Oracle19 UTL_HTTP安全模型](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_HTTP.html)要求调用者对应远程主机ACL的connect权限。按实际数据库/主体、例程实现/权限、网络出口及DNS/SMB/HTTP各自收据定位能力；ACL拒绝或仅解析回连是反例。未保存xp_dirtree实现时不补通用协议能力，本次未运行SQL、外联或读取内网数据。\n\n来源：[保存帖1](https://x.com/i/status/1412795100409761792)、[保存帖2](https://x.com/i/status/1412892681710276608)。"
  ]
]
ids={pid for row in json.loads((W/'batch-0104.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==43
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
