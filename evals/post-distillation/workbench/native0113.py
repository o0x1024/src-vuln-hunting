import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "scope-and-rules.md",
    "Slack 成员邮箱展示与测试者的工作区权限",
    "图文描述工作区成员邮箱可见性，没有保存当前配置或所有角色结果。\n\n把成员、guest、管理者、UI/API 导出和用户隐私选择作为不同主体与动作。自有允许角色做同数据对照，记录政策时间、可见字段和实际消费者；邮箱公开预期、用户主动公开或合法管理功能是反例。第三方工作区显示邮件不授予测试权，也不能概括为当前 Slack 默认漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1451876063907389446)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "SubCrawl 签名匹配到样本事实的距离",
    "终端列 8 hosts、34 URLs 与两条 CLAMAV Winware 检测，正文称按独特内容签名用于 MISP。\n\n将发现地址、取回内容、哈希、检测器/规则版本、匹配位置和共享输入分层存证。签名命中、文件名或链接数不是确认恶意/独立漏洞数；错误页、演示内容、误报与旧版本样本是反例。不执行样本或上传私有数据。\n\n来源：[保存帖1](https://x.com/i/status/1451884802488033284)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "SysFlow 采集架构的分阶段回执",
    "保存图展示 Collector、Exporter、对象存储、搜索分析等组件。\n\n为事件建立主体/进程、原始时间、采集序列、导出批次哈希、查询条件和结果关联。组件部署、图中连线、存储文件存在与最终查询到事件分别取证；丢弃、重试重复、时间窗口或字段变换可使统计不一致。架构图不能当真实采集证明。\n\n来源：[保存帖1](https://x.com/i/status/1452020640270229512)。"
  ],
  [
    "by-type/idor-access-control.md",
    "消息 DELETE 权限标题与可逆权限核对",
    "通讯概述消息删除接口缺权限并给出大量用户数字，没有保存完整请求/影响统计。\n\n把消息所有者、租户、动作和调用身份分别绑定，检查服务端授权分支与拒绝对照。删除是不可逆动作，本次仅提炼；后续优先查看处理器或使用明确授权的可逆等价动作/一次性实验对象。接口标题和用户总量不证明所有人的消息均可被删。\n\n来源：[保存帖1](https://x.com/i/status/1452229505825841161)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "构建脚本中的已删桶引用与供应链消费者",
    "通讯提到已删除桶仍被构建脚本引用的候选。\n\n追踪引用字符串、资源现有归属、命名可重用条件、构建读取身份、下载内容及完整性验证。旧脚本/不存在桶/相似名称不证明能接管；停止使用、校验哈希、名称不可重用和不同租户命名空间均是反例。只审查已有材料，不创建资源或替换依赖。\n\n来源：[保存帖1](https://x.com/i/status/1452229505825841161)。"
  ],
  [
    "by-type/ssrf.md",
    "SNS InvalidAction 证书回显与 webhook 处理链",
    "保存错误页回显公有 PEM 证书并报 InvalidAction，通讯/标题另称 SNS webhook RCE。\n\n分别定位请求到达、消息解析、证书位置选择、验签、可信数据到后续消费者的流向。公有证书不是私钥，反射错误不是代码执行；未经过实际 webhook 或只到通用 API 错误分支是反例。缺少处理器代码/执行回执，不补写 RCE。\n\n来源：[保存帖1](https://x.com/i/status/1452229505825841161)、[保存帖2](https://x.com/i/status/1452516634489344000)。"
  ],
  [
    "by-type/xss.md",
    "HTML 注入在订单反馈阅读者中的条件",
    "正文自述订单反馈存储 XSS，配图却是 Google Hangouts GET，没有反馈读者或脚本回执。\n\n记录订单阶段、可控字段、存储版本、实际阅读角色、响应上下文和无害 DOM 标记。安全文本/链接、净化后的节点、独立沙盒或只有发送者可见均须纳入反例。配图消费者不同不能与 Alibaba 自述拼成一条已验证链，不复制图中 cookies。\n\n来源：[保存帖1](https://x.com/i/status/1451932492261257222)、[保存帖2](https://x.com/i/status/1452562453498236929)。"
  ],
  [
    "discovery/web-and-api.md",
    "动词探测调试分支与 PHP 状态页的实际处理器",
    "候选包含 Debug=True、server-status、PHP 管理页；Symfony 图仅欢迎页，Tomcat examples 与 manager 是不同路由。\n\n按方法、路径、处理器、认证身份、字段及动作建矩阵，并保持同一对象与请求来源。自有基线对照页面实际内容；200、框架版本、示例页可达和目录路径不等密钥或管理员能力。关闭调试、错误路由、版本伪装、静态示例及独立授权是反例。\n\n来源：[保存帖1](https://x.com/i/status/1451934113590566926)、[保存帖2](https://x.com/i/status/1452862094664155138)、[保存帖3](https://x.com/i/status/1454326952102285315)、[保存帖4](https://x.com/i/status/1455880791959998465)、[保存帖5](https://x.com/i/status/1456692887039746050)。"
  ],
  [
    "by-type/waf-bypass.md",
    "delete alert 与大小写自述的绑定核对",
    "保存正文称删除 alert 再改写调用可突破过滤，没有完整浏览器执行结果。\n\n检查过滤发生层、实际 JS 字节、严格模式、属性描述、全局/局部绑定和继承来源。JS 标识符大小写不能任意互换，删除失败或仍有不同绑定均可能改变结果；无实际解析器/事件/执行回执，不称所有 WAF 绕过，也不运行档案脚本。\n\n来源：[保存帖1](https://x.com/i/status/1452251028934516743)。"
  ],
  [
    "discovery/web-and-api.md",
    "OpenAPI 转换后导入的语法与能力损失",
    "转换图使用 json 扩展名但输出可见 YAML，后续 Parser 列出多个 POST 路径。\n\n记录源/目标规范版本、真实语法、转换工具版本、servers、请求体、安全定义、引用与参数对应关系。导入后按同一方法/路由及身份核对预期定义与产物，文档错位/不支持字段/请求体丢失是反例。表格导入不等实际请求或授权覆盖；不安装转换器或发送请求。\n\n来源：[保存帖1](https://x.com/i/status/1452298996828016640)。"
  ],
  [
    "discovery/web-and-api.md",
    "邮件头候选从地址字符串到 SMTP 的消费层",
    "正文给编码换行与 RCPT 形态的邮件字段，没有发送/收件人变化记录。\n\n分开记录输入编码、解码次数、邮件地址解析、头部构造、MIME 与最终 SMTP 指令。字面反斜杠、拒绝换行、地址被引用或仅显示文本是反例；HTTP Content-Length 不可代替邮件路由证明。使用本地无投递模型/已有处理器证据，本次不寄信或保留真实收件人。\n\n来源：[保存帖1](https://x.com/i/status/1452321357568614416)。"
  ],
  [
    "by-type/ssrf.md",
    "IP 别名候选与真正 URL 解析结果",
    "正文列整数、短 IP、IPv6、userinfo 及信任域置于其他 host/路径的表达式。\n\n在目标实际 URL 解析器中核对 scheme、host、端口、解码/规范化和最终取回身份；允许域按完整规范化名称与点边界检查。无效 IPv6、仅为路径字符串、被拒绝解析或合法独立域名是反例。候选字面形式不证明连到内网，也不访问元数据。\n\n来源：[保存帖1](https://x.com/i/status/1452340514641035271)、[保存帖2](https://x.com/i/status/1452446782487662593)、[保存帖3](https://x.com/i/status/1454412777011879941)。"
  ],
  [
    "source-audit.md",
    "线程堆栈伪装画面与执行地址",
    "ThreadStackSpoofer 图有 ntdll、TOTALCMD 线程模块和地址，没有原始攻击入口或防护判定。\n\n分别记录线程 PC、栈帧、实际模块映射、采样时间、已有权限和显示层生成逻辑。工具改变显示/栈字段不证明执行来自可信模块；缺真实映射、回溯不全或未经过防护均是反例。此图不能推导初始 RCE、提权或通用规避，不执行二进制。\n\n来源：[保存帖1](https://x.com/i/status/1452398024102191116)。"
  ],
  [
    "by-type/file-upload.md",
    "RDF 中 XHTML script 的响应与阅读器",
    "保存 RDF XML 包含 XHTML namespace 和 script 静态内容，没有执行回执。\n\n绑定文件字节、接收处理器、响应 MIME/Content-Disposition、响应 origin、嵌入方式和真实 XML/RDF/浏览器消费者。下载附件、纯数据解析、净化、无脚本沙盒及命名空间不被作为活跃节点是反例。扩展名和标签字节不能单独证 XSS。\n\n来源：[保存帖1](https://x.com/i/status/1452643326960807937)。"
  ],
  [
    "by-type/csrf.md",
    "WordPress 插件自述与核心奖励标题的组件差异",
    "正文称扫描旧插件后利用 CSRF，图则是 WordPress 核心版本 <4.8.5 的奖励标题。\n\n先对应核心/插件包、版本、处理器、登录条件、令牌/Origin 和自有状态变化，独立核对双方来源。核心标题不能证明某插件受影响；扫描器旧版判断、相似路由或不同安装实例是反例。未保存真实浏览器请求，不运行旧 exploit。\n\n来源：[保存帖1](https://x.com/i/status/1452666873779146752)。"
  ],
  [
    "by-type/waf-bypass.md",
    "ASP 重复参数逗号合并与 pointer 事件",
    "正文称重复参数在 ASP 合并成逗号，并组合 pointer 事件，有浏览器限制自述而无完整环境记录。\n\n依次保存查询串、解码顺序、服务器合并结果、HTML 属性字节、JS 解析与事件触发条件。单值消费、数组保持、属性转义、不支持事件或未触发均是反例。逗号出现在响应不等代码执行；版本/规则/浏览器边界不得扩大。\n\n来源：[保存帖1](https://x.com/i/status/1452670575046975498)。"
  ],
  [
    "by-type/idor-access-control.md",
    "LOW 邀请者到 OWNER 的授予能力",
    "正文给 LOW 角色邀请请求内改 OWNER 的自述及奖励，没有持久角色回执。\n\n以邀请者、组织、被邀请的自有实验主体、允许授予上限、token 消费及最终权限分别建账。拒绝、服务器重算角色、仅展示字段或邀请仍待接受是反例。提交 OWNER/200 不证升权；本次不发送邀请/邮件或改变生产角色。\n\n来源：[保存帖1](https://x.com/i/status/1452723004635422722)。"
  ],
  [
    "by-type/authn-session.md",
    "旧 OTP 重登与成功消费后的单次性",
    "帖子称使用某 2FA 码后退出再登录仍可复用，但没有挑战或时间步记录。\n\n记录 OTP 类型、生成时间步、成功消费、挑战主体、认证上下文与最终受保护能力。相同数字出现在新步、备用码或不同验证事务不能直接混为一次重放。RFC6238 要求同一时间步成功接受后不得第二次接受该 OTP；仅审查自有既有记录，不猜码或重放他人因素。[RFC6238](https://www.rfc-editor.org/rfc/rfc6238.html)。\n\n来源：[保存帖1](https://x.com/i/status/1452833522431848453)。"
  ],
  [
    "by-type/deserialization-rce.md",
    "Orion ViewContext JSON 的 Objects 设置与外部来源",
    "ParseViewContext 图设置 TypeNameHandling=1 并反序列化 AlertingActionContext。\n\nJson.NET 官方枚举的 1 是 Objects，Auto 是 4；非 None 处理外部 JSON 应验证输入类型，官方提示自定义 SerializationBinder。继续追 ViewContextJsonString 控制者、签名/保存过程、兼容类型和真实副作用。配置一行、内部可信 JSON 或无可利用兼容类型都不能证 RCE，不构造 gadget。[Json.NET 枚举](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_TypeNameHandling.htm)。\n\n来源：[保存帖1](https://x.com/i/status/1452833644834217986)。"
  ],
  [
    "scope-and-rules.md",
    "VDP 数字快照、dork 与资产过滤器的规则来源",
    "保存统计从 2301 到 2302，并含奖励/名人堂分类；dork、GitHub JSON/jq 和 bbscope 只给发现/过滤线索。\n\n保存官方政策地址、版本时间、资产类型、排除项、wildcard/端口/路径以及允许动作/预算，再将发现资产逐项匹配。分类可重叠、历史条款可变化、工具过滤可丢上下文；命中关键词或输出 in-scope 不能替代当前授权。不下载运行列表脚本或借第三方项目规则授权本次测试。\n\n来源：[保存帖1](https://x.com/i/status/1452847464541614083)、[保存帖2](https://x.com/i/status/1453943225786376211)、[保存帖3](https://x.com/i/status/1455021789986263040)、[保存帖4](https://x.com/i/status/1455218613384777730)、[保存帖5](https://x.com/i/status/1455545996570624002)、[保存帖6](https://x.com/i/status/1455835966963322882)。"
  ],
  [
    "by-type/ssrf.md",
    "IPlogger 管理员阅读与请求源的归因",
    "正文建议引导管理员打开第三方 IPlogger，另一 Lorsrf 图只展示监听服务启动。\n\n安全提炼采用自有批准标记、已有回执与明确阅读上下文，区分浏览器、代理、邮件安全机器人及服务端取回的源身份。监听成功和被访问都不自动证明 SSRF/管理员 IP 泄露；缺关联 ID、共享出口或预览机器人是反例。不联系管理员、寄送链接或收集第三方隐私。\n\n来源：[保存帖1](https://x.com/i/status/1452914602140860421)、[保存帖2](https://x.com/i/status/1453334213193830400)。"
  ],
  [
    "by-type/authn-session.md",
    "验证邮件标志、Origin 回跳与动态 JS 的 OTP",
    "正文分别称改 Origin/Referer 进入 dashboard 和动态 JS 含 OTP；没有完整服务端保护动作。\n\n将未验证账户的有限 UI、pending/verified 标志、客户端可读数据、挑战绑定及服务端最终能力分开。保持自有主体/新会话的有效和无效对照，记录持久结果；只改界面/缓存旧码/允许预验证浏览/服务端仍拒绝均是反例。不能由可见 OTP 或跳转单独认定认证绕过。\n\n来源：[保存帖1](https://x.com/i/status/1452948016059482115)、[保存帖2](https://x.com/i/status/1452948650930294789)。"
  ],
  [
    "by-type/sql-injection.md",
    "扫描器候选、真假条件与时间噪声",
    "正文推荐扫描/引号/真假与延迟检测；MySQL 前缀候选图却仅显示 localhost403。\n\n同参数同身份保存基线、真假条件、返回字段和延迟分布，区分代理/WAF/应用错误与 SQL 消费。稳定非 SQL 错误、缓存、队列、限速或前缀被拒绝是反例。一次500/403、匹配字符串或命令启动不证 SQL 注入；不执行档案 SQL、SQLmap 或高负载计时。\n\n来源：[保存帖1](https://x.com/i/status/1452978615545643010)、[保存帖2](https://x.com/i/status/1452978617437282308)、[保存帖3](https://x.com/i/status/1453335419081293829)。"
  ],
  [
    "by-type/open-redirect.md",
    "并行 HEAD 检测与登录多斜杠的最终 origin",
    "管道替换所有参数后 grep Location，另有登录多斜杠/P4 标题和信任名称路径图。\n\n每个候选保留原参数、替换位置、方法、返回链、URL 解析及最终浏览器 origin；登录 return URL 独立记录解码次数与敏感值。HEAD/GET差异、相对路径、同域字符串、未走登录分支和安全允许域是反例。grep 命中或 triaged 标题不能证明外域跳转及 token 泄露。\n\n来源：[保存帖1](https://x.com/i/status/1453027904405839875)、[保存帖2](https://x.com/i/status/1453292276055252996)、[保存帖3](https://x.com/i/status/1453419305731706881)、[保存帖4](https://x.com/i/status/1454412777011879941)。"
  ],
  [
    "reporting.md",
    "同根因端点、报告阶段与酌情奖励",
    "图包含更早报告重复、同根因其他端点、N/A到Low/High、Pending/Closed及奖励决定，没有相应完整技术链。\n\n以稳定报告ID关联根因、端点变体、证据版本、结单原因、严重性和付款，各字段分别记录时间/来源。重复端点不必是新根因，Closed不必已修复，级别/金额不证明全部影响。不能把状态历史或致谢拼为确认漏洞；保留互相矛盾阶段，不替作者补写重现。\n\n来源：[保存帖1](https://x.com/i/status/1453046077926506497)、[保存帖2](https://x.com/i/status/1453360068225798144)、[保存帖3](https://x.com/i/status/1453755947277422592)、[保存帖4](https://x.com/i/status/1455426761575985152)、[保存帖5](https://x.com/i/status/1455448820746047489)、[保存帖6](https://x.com/i/status/1455556229263073285)、[保存帖7](https://x.com/i/status/1456691022251970565)。"
  ],
  [
    "by-type/idor-access-control.md",
    "发票导出直接引用与二三阶权限链",
    "发票示意图直接将 ID1/2 对应数据库与 exportInvoices；正文另建议二三阶及第三方/隐藏调试。\n\n追自有低/高权限主体的存储引用、队列、worker、渲染与导出消费者，并记录每步实际权限上下文和数据归属。直接取 ID 的图不证明有异步多阶段；合法公共发票、引用在每步重新鉴权或第三方授权边界不同是反例。仅给候选，不读取他人发票或假定第三方可测。\n\n来源：[保存帖1](https://x.com/i/status/1453141260416520194)、[保存帖2](https://x.com/i/status/1453221581044453382)。"
  ],
  [
    "targeted-fuzzing.md",
    "从目标上下文建词表及管道解析损失",
    "正文主张用目标知识建词表，另给 JS/爬虫/ffuf 管道，包含粗略 regex、awk/cut 与全参数替换。\n\n先从实际处理器、源位置、历史记录和字段结构产出候选，标记遗漏/替换位置与有界预算；按结构解析并保留原始URL和身份。简单正则漏模板/转义/符号，跟跳转可能出范围，过滤扩展或500隐藏读者/失败。工具横幅、线程数和200不等覆盖或真实漏洞，不执行扫描。\n\n来源：[保存帖1](https://x.com/i/status/1453258449756827660)、[保存帖2](https://x.com/i/status/1453759254263914500)、[保存帖3](https://x.com/i/status/1454742975456612353)、[保存帖4](https://x.com/i/status/1455889419123281923)。"
  ],
  [
    "by-type/xxe.md",
    "空白编码候选与 DTD 协议支持",
    "图描述内/外实体 SYSTEM 与 file/http/https/gopher，正文提空白/混合编码绕过。\n\n核对真实线缆字节、声明/解码、良构解析、实际库/版本、DTD与实体开关、协议实现及处理身份权限。WAF放行≠实体解析，XML错误、禁用外部实体、不支持scheme或无读权限均是反例。最小核对使用已授权无害标记/已有代码证据，不取文件、外发回调或构造实体资源炸弹。\n\n来源：[保存帖1](https://x.com/i/status/1453261198040961038)、[保存帖2](https://x.com/i/status/1455195626732412937)、[保存帖3](https://x.com/i/status/1455199582518865921)。"
  ],
  [
    "by-type/info-secrets.md",
    "GitHub 关键词、Basic 候选与 API 字典的三层事实",
    "词条含 s3cfg/netrc/gitcredentials/cloud/API 字段；字典给约550格式/response regex，Basic匹配有管理员自述。\n\n分别存源文件版本/位置、值的类型/用途、匹配条件和实际授权能力。占位ACCESS_TOKEN、例子、编码字串、公有配置、失效或限域值是反例；regex/数字/解码本身不证明有效凭据。不复制/解码/试用第三方秘密，合法验证也需另行授权的自有低影响操作。\n\n来源：[保存帖1](https://x.com/i/status/1453331154442997761)、[保存帖2](https://x.com/i/status/1453738771971645447)、[保存帖3](https://x.com/i/status/1453802438578753542)、[保存帖4](https://x.com/i/status/1455131688070107138)、[保存帖5](https://x.com/i/status/1455148088922763264)、[保存帖6](https://x.com/i/status/1456382804539887621)、[保存帖7](https://x.com/i/status/1456625824715575303)。"
  ],
  [
    "by-type/business-logic.md",
    "Referer href 回显与持久修改的实验区别",
    "图展示 Referer 到 href/GoBack，以及200页面；另帖建议刷新检验真实改变。\n\n保持同一对象、身份、动作与初始状态，独立读取持久结果并记录刷新/新会话。导航元数据、提示字符串、乐观UI、缓存或不同处理器返回200都是反例。把头路由/回显/授权/业务状态分别判断，不能从 Content Modified 文案推出越权。\n\n来源：[保存帖1](https://x.com/i/status/1453636718402277380)、[保存帖2](https://x.com/i/status/1455556229263073285)、[保存帖3](https://x.com/i/status/1456866283555725315)。"
  ],
  [
    "discovery/web-and-api.md",
    "SHADOW Swagger 模型到当前 API 能力",
    "图将Swagger路径/参数/模型送到图关系与embedding，没有目标调用证据。\n\n保存文档版本、方法、路径参数、角色、安全定义与实际调用者来源。用已有自有流量核对当前端点及操作语义；弃用文档、示例路径、内部不可达或独立鉴权是反例。模型建议端点不等私有数据可读，未授权第三方API不调用。\n\n来源：[保存帖1](https://x.com/i/status/1453664940137586692)。"
  ],
  [
    "by-type/info-secrets.md",
    "PrettyRecon 错误搜索计数与实际披露字段",
    "图含aws_key 44候选、Whoops4549、500/404与Apache头；Symfony页只是版本/源码目录。\n\n将搜索词、样本响应哈希、响应时间、实际字段、数据归属与权限需求逐项保存。错误样板、字段名未带值、公有版本号、欢迎页和重复响应是反例；404/500、搜索总数与框架路径均不等可用秘密或RCE。不上传/使用疑似密钥。\n\n来源：[保存帖1](https://x.com/i/status/1453749930598690821)、[保存帖2](https://x.com/i/status/1454326952102285315)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "本地 multipart 收文件的权限前提",
    "HTTPUploadExfil 图展示本地 curl 上传、存储与读取示例文件。\n\n绑定发送进程的既有权限、源样本hash、传输接收端、结果hash和来源关联。接收成功只验证复制阶段，不能推导最初入侵、服务器任意读取或凭据提取；本地实验、预置内容、传输截断是反例。本次只提炼，不上传敏感文件或启动监听。\n\n来源：[保存帖1](https://x.com/i/status/1453832659403161602)。"
  ],
  [
    "source-audit.md",
    "VT 低比例与双哈希的样本身份",
    "帖子给同样本MD5/SHA1，图为1/67、AUTOIT标签与单个Adware检测。\n\n保留算法标签、完整样本hash、来源、时间、检测器版本及判定说明；不同算法值不代表两个样本。低比例、名称含Burp、压缩/打包标签既不能证明安全也不能推广到官方软件恶意；误报与过期判定是反例。不下载执行或把私有样本上传公共服务。\n\n来源：[保存帖1](https://x.com/i/status/1453882239167700993)。"
  ],
  [
    "by-type/jwt.md",
    "算法、kid 与密钥选择的独立接受条件",
    "正文列算法选择、非法签名、猜秘密与kid攻击候选，没有保存验签成功链。\n\n追JWT来源、接受的alg/typ/audience/expiry、实际验签钥匙选择和kid消费端路径/远程源。改token后只有UI变化、算法白名单拒绝、kid仅标识可信键或签名失败均是反例。使用自有既有合法/无效对照区分验签与授权，不猜密钥、不取外部JWK或读取文件。\n\n来源：[保存帖1](https://x.com/i/status/1453922337582043139)。"
  ],
  [
    "by-type/authn-session.md",
    "认证 mindmap 变成动作与主体矩阵",
    "保存思维图含登录、注册、重置和2FA支路；替换响应只配High标题，忘密枚举正文建议比较结果。\n\n每支记录输入所有者、挑战/会话、成功消费和最终持久能力；错误渲染、异步时间及服务端回应分别对照。客户端bool、通用200、不同既有会话或邮件发送差异不等认证绕过/身份枚举。仅自有已知账号有界复核，不猜码、批量枚举或寄信。\n\n来源：[保存帖1](https://x.com/i/status/1453999691226443781)、[保存帖2](https://x.com/i/status/1454695010062962689)、[保存帖3](https://x.com/i/status/1454861366674673670)、[保存帖4](https://x.com/i/status/1455914165546078211)、[保存帖5](https://x.com/i/status/1457000786496417793)。"
  ],
  [
    "expert-reasoning.md",
    "技巧帖子与配图矛盾的证据分层",
    "正文提醒Twitter技巧未必正确；本批配图包含消费端不一致和明确Blocked。\n\n先抄出来源主张，再记录实际看到的输入、消费者、权限、结果与反例；区分标题、自述、图中局部观察和完整因果链。把版本/规则/上下文限定写入方法，矛盾保留而非用另一图补齐。已覆盖表示材料处理完，不能转成线上漏洞已验证。\n\n来源：[保存帖1](https://x.com/i/status/1454034644106686465)、[保存帖2](https://x.com/i/status/1452562453498236929)、[保存帖3](https://x.com/i/status/1455737756924071936)、[保存帖4](https://x.com/i/status/1456368204230664202)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "HTTP 版本比特信道与 QR 视频消费者",
    "正文分别用HTTP1.0/1.1表示比特和视频帧QR/AES传指令，图只为梗和三秒QR视频。\n\n分发送者控制、载体编码、传输/代理规范化、receiver解码、身份授权与真实进程执行存证。视频存在、协议字符串或二维码可见不证明命令执行/入侵；无receiver、重编码损坏、协议统一与未通过授权是反例。不解码访问外部命令、部署C2或执行档案。\n\n来源：[保存帖1](https://x.com/i/status/1454059081258389506)、[保存帖2](https://x.com/i/status/1454605421591863300)。"
  ],
  [
    "by-type/xss.md",
    "Lucee missinginclude 路径错误页与实验弹窗",
    "一图为Firefox Lucee5.2.9.31错误页与domain弹窗，另一为自有Neuralegion实验firstname页面rXSS标记。\n\n按应用/构建、输入位置、原始响应、实际DOM、触发事件、阅读者和标记关联分别记录。不同实验不能合并成生产影响；console手输、预置lab、错误分支关闭、路径被转义或沙盒为反例。历史弹窗仅支持其特定观察，不证通用RCE、存储或ATO。\n\n来源：[保存帖1](https://x.com/i/status/1454078934514024454)、[保存帖2](https://x.com/i/status/1455822343125733376)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "daily anew 增量与无条件完成通知",
    "脚本每86400秒跑subfinder/anew，notify在循环内无条件发送。\n\n区分首次全量、去重键、增量输出、阶段失败、执行窗口和通知原因。保留输入版本/产物hash/失败回执并按实际delta核对；空增量仍发完成通知、并发写入或重复历史文件是反例。邮件数与子域条数不是新独立资产或缺陷数，本次不创建定时任务。\n\n来源：[保存帖1](https://x.com/i/status/1452264361754460160)、[保存帖2](https://x.com/i/status/1454644053677535239)。"
  ],
  [
    "by-type/deserialization-rce.md",
    "Django debug 与 Pickle 会话的实际入口",
    "正文给Debug/PickleSerializer候选，未保存目标session配置或受控反序列化输入。\n\n先看实际sessionengine、serializer版本、cookie/服务器存储边界、签名验证、secret来源与调用者。debug开启不直接等于pickle消费，可信服务器存储、不同serializer或签名拒绝为反例。历史类名不证明当前可用或所有Django受影响；不构造pickle或提取秘密。\n\n来源：[保存帖1](https://x.com/i/status/1454661107759689733)。"
  ],
  [
    "discovery/web-and-api.md",
    "main.js 正则与 CDX PHP 历史路径的发现范围",
    "简单斜杠正则和gau/CDX PHP卡片只提供候选；GCP metadata自述配奖励图。\n\n保存源位置/时间、CDX字段结构、完整URL、调用分支与当前归属，标记模板/转义/字符集遗漏。历史存在、扩展为PHP、字符串路径和奖励不能证明当前端点/敏感服务可达；资源转移、死代码、示例和鉴权拒绝是反例。不取metadata或借历史URL授权测试。\n\n来源：[保存帖1](https://x.com/i/status/1454742975456612353)、[保存帖2](https://x.com/i/status/1455587197906608129)、[保存帖3](https://x.com/i/status/1456964593524346883)。"
  ],
  [
    "reporting.md",
    "PeTeReport 数量与 CWE 图的稳定问题标识",
    "图有2products、2reports、5findings、3high及CWE分布；另帖列十大P1类型。\n\n每项稳定ID关联根因、具体触发、受影响角色/字段、证据版本和已证影响，再映射类别/级别。一个问题多类别、多个端点同根因、草稿或汇总重复是反例。CWE图/类别排行/报表数量不证独立确认漏洞，等级需项目规则与实际后果。\n\n来源：[保存帖1](https://x.com/i/status/1454783883124281345)、[保存帖2](https://x.com/i/status/1457004099854077963)。"
  ],
  [
    "source-audit.md",
    "从 CVE 补丁到 elFinder GitLab 的适用条件",
    "正文建议从补丁追小库；elFinder称全旧版受影响，GitLab图只为模块PR/行数。\n\n建立产品、组件、版本/配置、入口、调用者、修复前后信任条件和反例表，检查实际可控输入到危险消费者。补丁/编号/模块被合并不证明当前目标可用；未安装、不同配置、已修复、需要既有权限或版本不连续为反例。缺源码正文不补写链，也不采纳全旧版。\n\n来源：[保存帖1](https://x.com/i/status/1454787269206765582)、[保存帖2](https://x.com/i/status/1455164668964704265)、[保存帖3](https://x.com/i/status/1456282453363019779)。"
  ],
  [
    "by-type/ssrf.md",
    "Windows file 候选与 SMB 认证的不同结果",
    "正文建议file指向VPS、Responder捕获NetNTLMv2再破解，没有实际消费或身份回执。\n\n分别核对平台、file URL/UNC解释、具体服务器读取库、出站SMB/认证策略及请求身份。HTTP取回、纯本地file、禁用SMB/认证、非Windows或低权限匿名是反例。NetNTLMv2响应也不能混称直接取得NT哈希/明文密码。本次不启动Responder、收集哈希、外发诱导或破解。\n\n来源：[保存帖1](https://x.com/i/status/1455181838587240453)。"
  ],
  [
    "experiment-design.md",
    "刷新后权益持久化与竞态标题的验证边界",
    "一帖建议改完刷新，另一只有订阅竞态标题；未保存并发事务顺序。\n\n固定自有对象/初始权益与授权动作，独立读取持久状态，区分乐观UI、缓存、会话和后台计算。竞态另需事务交错、原子性假设与可重复最小差异；一次刷新、订阅后提示或奖励邮件不能证明竞态。仅保存假设/已有记录，不并发支付或制造DoS。\n\n来源：[保存帖1](https://x.com/i/status/1455556229263073285)、[保存帖2](https://x.com/i/status/1456100877492572163)。"
  ],
  [
    "discovery/web-and-api.md",
    "认证扫描器新读者覆盖与会话降级",
    "功能文案提iframe、animation、DOM redirect、SVG和多选等发现能力，未给完整扫描回执。\n\n记录每个入口的动作序列、角色/会话、阅读器、网络回执与最终业务能力，核对全程没有登出或切换身份。未加载frame、隐藏条件未触发、SVG仅下载、缓存/过期session是反例。功能支持与模式数不等目标覆盖；不启动主动扫描或导出凭据。\n\n来源：[保存帖1](https://x.com/i/status/1455671089003212803)。"
  ],
  [
    "by-type/authn-session.md",
    "Flask 用户 ID 修改自述与签名 cookie",
    "正文称改userid可无日志登录，但配图是PDF取回元数据主机名，与会话无关。\n\nFlask默认会话cookie有签名，能读取不等可任意改；需核对实现是否扩展/服务器会话、签名secret、字段绑定、最终主体和保护动作。有效签名拒绝改值、仅显示变化或不同session实现为反例，日志缺失另证。不从PDF图推导认证绕过或尝试cookie。[Flask Sessions](https://flask.palletsprojects.com/en/stable/quickstart/#sessions)。\n\n来源：[保存帖1](https://x.com/i/status/1455737756924071936)。"
  ],
  [
    "by-type/document-rendering.md",
    "PDF metadata 主机名与 Flask GCP 主张分离",
    "PDF图URL含元数据位置与排版参数，页面有AWS样式compute.internal主机名；两个正文分别谈Flask和GCP。\n\n绑定渲染任务、URL消费者、取回身份、返回字段与原始回执。主机名候选最多支持局部取回观察，不证明IAM凭据/云权限，厂商不能互换；预置文本、浏览器本地取回、缓存或模拟响应是反例。不访问元数据或复制敏感字段。\n\n来源：[保存帖1](https://x.com/i/status/1455737756924071936)、[保存帖2](https://x.com/i/status/1455587197906608129)。"
  ],
  [
    "by-type/authn-session.md",
    "隐藏注册到邮箱变更的 verified 主体",
    "保存正文称隐藏signup可进入panel，另线程只到注册自有邮件后改其他邮件；图为修复/分诊邮件。\n\n分注册入口权限、账户角色、pending与verified邮箱、验证挑战收件人/失效、重认证和最终保护能力。允许预激活浏览、服务端保留旧verified主体或未授权邮箱待确认为反例。前两步和修复邮件不证明最终接管，不联系第三方邮箱或发验证信。\n\n来源：[保存帖1](https://x.com/i/status/1455852893039435776)、[保存帖2](https://x.com/i/status/1456982023013285900)。"
  ],
  [
    "by-type/file-upload.md",
    "elFinder cmd=tree 的目录元数据与 OS 命令",
    "赞美课程配本地elFinder2.0.4目录JSON，cmd=tree/target/hash/read/write/name可见。\n\n将应用操作名、对象引用、返回元数据、实际权限检查、文件内容及OS调用分别追踪。tree返回目录/权限声明不等实际文件可写/任意读/执行；本地演示、虚拟文件系统或再次鉴权是反例。不能把cmd字段名当shell入口，本次不访问目录/改文件。\n\n来源：[保存帖1](https://x.com/i/status/1455881504387706889)。"
  ],
  [
    "source-audit.md",
    "LSASS clone dump 完成与凭据解析",
    "日志标LSASS PID、clone handle及dump complete，没有初始权限来源或解析结果。\n\n分进程身份/保护状态、读取权限、采集工具/样本hash、输出完整性和授权解析阶段。日志成功不等取得凭据或提权；错误PID、缺片、无法解密、预置实验和既有管理员权限为反例。本次只读保存截图，不运行dumper、打开真实内存或复制秘密。\n\n来源：[保存帖1](https://x.com/i/status/1455886059011706881)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "ffuf replay-proxy 横幅与捕获事实",
    "管道包含httpx跟跳转/retry/cut和ffuf stdin，横幅示FUZZ、40threads、followfalse与replayproxy。\n\n保存各阶段结构、原URL/重定向范围、参数映射、真实身份、请求预算和proxy history关联。配置代理或横幅出现不等捕获；响应缓存、跳转出范围、字段截断、插件忽略代理均为反例。已有真实流量才能计请求回执，不执行管道/启动扫描。\n\n来源：[保存帖1](https://x.com/i/status/1455889419123281923)。"
  ],
  [
    "by-type/xss.md",
    "application/json 数据块与 HTML 结束标签",
    "AMP图把alert样式字符串放title/docUrl的JSON中，没有执行回执。\n\nWHATWG规定数据块不直接按JavaScript处理，但HTML解析仍需限制script内容中的结束标签序列，且作者脚本可能另消费数据。分别检查原始HTML字节、结束标签安全性与JSON parse后的DOM使用；安全数据存储/文本输出是反例。不能只因type判永无XSS，也不因出现alert判已执行。[WHATWG script](https://html.spec.whatwg.org/multipage/scripting.html#restrictions-for-contents-of-script-elements)。\n\n来源：[保存帖1](https://x.com/i/status/1456138253371854849)。"
  ],
  [
    "source-audit.md",
    "Mekotio 多阶段图的来源与因果回执",
    "图是链接→ZIP→BAT→PowerShell→二次ZIP→AHK/script/DLL→C2，没有每阶段运行日志。\n\n为每个输入/输出hash、调用者权限、实际解释器、下载来源和后续结果绑定证据。架构图、文件名、链尾C2不证明真实感染或防护规避；缺阶段、被阻止、预置文件或正常解释器用途为反例。只分析保存图，不下载恶意文件/解压执行/建立控制端。\n\n来源：[保存帖1](https://x.com/i/status/1456188772182372359)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "root:x grep 与文件列表的真正读者",
    "管道以root:x匹配，另帖列passwd/shadow/SSH/history；Apache历史图有文件内容。\n\n以已授权自有无害标记区分输入反射、静态示例、错误模板与真实文件处理器，记录文件映射、实际服务权限和最小返回。列表不是可读证明，文件读出不等root或代码执行；容器虚拟文件、拒绝访问与固定响应为反例。不读敏感列表或执行历史PoC。\n\n来源：[保存帖1](https://x.com/i/status/1456199035216334848)、[保存帖2](https://x.com/i/status/1456523094126850052)、[保存帖3](https://x.com/i/status/1455376993214623747)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "LDAP poll 快照、uSN 与变更主体",
    "日志有新增CN/RID及office/whenChanged/uSN/description，没有完整审计主体链。\n\n绑定域/服务器、poll时间窗、对象稳定ID、初末快照和源版本；把服务器时间/复制序列与真正变更者分开。复制、不同控制器、缓存或漏poll是反例，属性出现不证明谁修改或初始入侵。不修改/删除LDAP对象或抄出敏感字段。\n\n来源：[保存帖1](https://x.com/i/status/1456233412268855299)。"
  ],
  [
    "by-type/waf-bypass.md",
    "Cloudflare Blocked 图与 default rules 限定",
    "Cloudflare图明确Blocked且alt称只针对default rules，MySQL另一图同样仅403。\n\n保留规则集/版本、规范化字节、失败基线、实际应用读者及独立执行回执。被阻页、不同规则/客户配置、只改状态或未触发事件为反例。缺成功记录不能由配文补成bypass，更不扩大为所有Cloudflare/WAF。\n\n来源：[保存帖1](https://x.com/i/status/1456368204230664202)、[保存帖2](https://x.com/i/status/1453335419081293829)。"
  ],
  [
    "by-type/csrf.md",
    "删除账号 token 建议与不可逆动作边界",
    "正文建议删/换CSRF token，图为奖励和fixing邮件，没有真实跨站请求或删后状态。\n\n先审查处理器、token主体/挑战绑定、Origin/SameSite/cookie及真实浏览器等价性。优先可逆等价动作或明确授权的一次性实验对象；删除需专门明确范围，本次不执行。其他token被拒、未带cookie、仅提示变化或状态不持久为反例，金额不证CSRF成功。\n\n来源：[保存帖1](https://x.com/i/status/1456691022251970565)。"
  ],
  [
    "scope-and-rules.md",
    "Wifite help 的被动与主动无线动作",
    "Wifite2.5.8帮助列deauth、kill进程、无限与WEP/WPA/WPS/PMKID，其他帖仅工具资源。\n\n分别定义允许AP/设备、网络与频段、行为主体、被动接收/主动认证或断联、预算和退出条件。帮助输出不证密码/密钥已获取，工具名不保证仅被动；共享无线环境、第三方设备或默认主动选项为反例。不安装工具、改接口、发deauth或破解。\n\n来源：[保存帖1](https://x.com/i/status/1456845044887949313)、[保存帖2](https://x.com/i/status/1453945941816483846)、[保存帖3](https://x.com/i/status/1456120269051813888)。"
  ],
  [
    "by-type/open-redirect.md",
    "Unicode 域名显示长度与序列化 host",
    "正文称某Unicode显示能缩短域名，配图只有仓库封面，未保存具体字符映射结果。\n\n对同候选记录代码点、浏览器显示、URL序列化host、应用规范化、DNS归属和证书身份；按实际消费者比较允许域与origin。显示长度/视觉相似不等同一host或稳定映射；不同库拒绝/映射不同/确为独立域为反例。缺具体转换不补写必然绕过，不买域或访问候选。\n\n来源：[保存帖1](https://x.com/i/status/1456855615687495681)、[保存帖2](https://x.com/i/status/1454412777011879941)。"
  ],
  [
    "by-type/idor-access-control.md",
    "403 头部候选与同对象授权对照",
    "正文建议localhost头、Referer/UA、方法与参数，其他图仅导航回显和dashboard进入。\n\n固定主体、租户、对象与动作，分边缘路由、错误页面、认证和实际权限，保存持久保护能力差分。200的其他路由、只改href、需要既有admin或公共对象为反例。状态码与localhost字符串不证绕过，本次不猜Authorization、不暴力尝试。\n\n来源：[保存帖1](https://x.com/i/status/1456866283555725315)、[保存帖2](https://x.com/i/status/1453636718402277380)、[保存帖3](https://x.com/i/status/1452948016059482115)。"
  ],
  [
    "by-type/ssti.md",
    "多语法字符串在 SQL HTML 与模板的消费顺序",
    "正文组合SQL引号、SVG/JS与模板乘法，未保存三种实际消费者回执。\n\n为每个可控字段追解码、存储和真正SQL/HTML/客户端或服务端模板读者，分别用无害标记及基线判断。49可能客户端计算/固定内容，原字符串反射、SQL错误或HTML节点不能同时证明三洞。各上下文独立证据和反例，不执行拼接payload。\n\n来源：[保存帖1](https://x.com/i/status/1457002730032144384)。"
  ],
  [
    "by-type/request-smuggling.md",
    "Smuggler No URL 与双端解析证据",
    "终端Smuggler1.1显示ERROR No URL与usage，HTTP2外链未保存正文。\n\n工具可启动/帮助显示与前后端消息边界分歧分开。后者需授权隔离环境的双方协议、连接复用、原始字节、实际解析及关联后续请求；单端错误、无URL、代理统一解析和连接关闭为反例。当前无此链，不运行走私工具/生产混淆请求。\n\n来源：[保存帖1](https://x.com/i/status/1457094053930143748)、[保存帖2](https://x.com/i/status/1456100696466419716)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0113.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==132 and all(pid in ids for pid in urls)
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

