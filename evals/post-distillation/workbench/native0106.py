"""Own curated notes for0106. Append once after prevalidation. No source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "by-type/authn-session.md",
    "重置查询后缀与账号限流的最终消费",
    "重置POST图为429，追加查询的Intruder图为200且长度691；API网关轮换出口被称无限代理。HTTP状态、出口IP和真实账号尝试预算是不同观测。\n\n绑定受控账号、恢复挑战、请求规范化后的动作键、服务端计数与最终邮件/密码状态；比较相同挑战的正常和变体输入。缓存命中、统一200错误、挑战轮换或按账号限流均是反例。出口变化不能扩展同一身份额度或当前授权，截图没显示实际邮件送达。\n\n来源：[保存帖1](https://x.com/i/status/1416924025536729089)、[保存帖2](https://x.com/i/status/1417067225870082051)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "SSH代理存活与有效banner及认证收据",
    "Orbitaldump图同时有大量代理连接错误、156个SOCKS4、278个SSH banner、54个live与found1。代理存在、SSH协议可达和登录成功不能相互替代。\n\n分开保存原始输入集合、去重主体、每跳连接失败、banner时点及同次认证最终结果。成功日志需关联实际会话与允许使用的受控身份；只见found计数或旧banner不能补认证权限。不复制或使用截图凭证，不由列表规模推所有输入已验证。\n\n来源：[保存帖1](https://x.com/i/status/1417110791111725058)。"
  ],
  [
    "by-type/request-smuggling.md",
    "TECL分块超时的原始字节与消费者对照",
    "截图畸形分块约60174ms、正常请求65ms，并标possible TECL。一次超时可能来自等待、连接重试或限流，不能单独确认请求走私。\n\n保留原始CRLF、长度/分块字段、连接复用条件、前后端各自消息边界和重复对照。需将延迟定位到特定消费者并区分错误/不完整响应；正常请求也延迟或连接未复用是反例。工具语言和TCP接口不证明所有常规HTTP库均不能实现同样字节。\n\n来源：[保存帖1](https://x.com/i/status/1417151078970404866)。"
  ],
  [
    "by-type/info-secrets.md",
    "认证SMB全文搜索与跳过文件的暴露分母",
    "MANSPIDER图使用admin认证、256线程并跳过大于10MB文件。内容关键词命中只说明该身份看到了匹配文本，未证明未授权暴露或活跃凭证。\n\n记录获准共享、认证主体、文件类型/大小、读取失败、跳过项和匹配上下文；分别判断公开性、受控低权可读性与秘密对应的真实配置权限。模板、示例、过期值与合法管理员读取是反例。线程数不是全文覆盖分母，搜索认证参数不写入案例。\n\n来源：[保存帖1](https://x.com/i/status/1417246793566392333)。"
  ],
  [
    "by-type/idor-access-control.md",
    "组织新增成员与导出私有字段的同意边界",
    "Pokedex示意加入用户后导出私有电话；功能遍历建议用两个用户观察收件箱、邀请与共同业务边。成员关系改变与字段可见性是两次授权消费。\n\n建模发起者角色、目标组织、受控被加入身份、是否需要本人同意及新增后的具体导出字段。合法管理员职责和本人批准可能允许成员操作，却未必允许私有字段；以应用合同和受控双身份最终状态判断，不能把虚构电话示意算真实泄露。\n\n来源：[保存帖1](https://x.com/i/status/1417333683296645121)、[保存帖2](https://x.com/i/status/1420769080861249537)。"
  ],
  [
    "by-type/idor-access-control.md",
    "邀请approve参数与受邀者接受的主体绑定",
    "邀请图把user_email与approve true并列，描述现有用户被添加。客户端批准标志不能代替受邀者本人或合法管理者的授权。\n\n分别绑定issuer tenant、发起actor、受邀受控账号、token的用途/目标/有效期及接受后的权威membership。需核对谁有权批准和最终可用动作；仅发信、界面显示已批准、已有成员或被邀用户未接受均不能补跨主体成功。\n\n来源：[保存帖1](https://x.com/i/status/1417708794566652229)。"
  ],
  [
    "by-type/authn-session.md",
    "模拟身份的actor与subject及退出能力",
    "跨组织target_user和full_access参数图、auth_token改变的建议把模拟身份视作可疑。换发token是正常实现也可能采用的设计，关键是委托权限。\n\n关联原actor、目标subject/tenant、audience、权限范围、期限、审计与退出/撤销；服务端不得仅按客户端required_privileges授予能力。合法同租户管理委托、受限只读token和退出后能力失效是反例，token改变本身不能证明弱算法或接管。\n\n来源：[保存帖1](https://x.com/i/status/1418059170469777411)、[保存帖2](https://x.com/i/status/1418580162757677065)。"
  ],
  [
    "by-type/cors.md",
    "ACAO序列化Origin与带凭据浏览器读回",
    "正文给出裸主机ACAO和ACAC true，另一图201返回组织字段并用星号。响应头出现并不能补真实跨站读回。\n\n在受控浏览器环境记录完整scheme/host/port Origin、凭据模式、Cookie有效条件、预检及实际可读的受保护字段；裸主机不是正常序列化Origin。星号与带凭据响应、服务端JSON可见与脚本读回必须分开；无Cookie、公开数据或浏览器拒绝读回是反例。\n\n来源：[保存帖1](https://x.com/i/status/1417394778208014339)、[保存帖2](https://x.com/i/status/1418510719839002625)。"
  ],
  [
    "by-type/xss.md",
    "百分号解码与JS URI错误处理的实际sink",
    "编码JS URI示例结合析构onerror和throw，另文写prompt却声称alert。输入、解码后的文本与真正运行的函数需要逐层对应。\n\n保存进入URI/HTML/JS的具体消费者、解码次数、过滤后字节、语法上下文和错误处理注册时机；函数名、模态窗口和错误回调不是同一机制。仅有字符串、被当普通文本、scheme不被消费或调用名称不一致都是反例，不以示例补实际Cookie读取。\n\n来源：[保存帖1](https://x.com/i/status/1417105195658514434)、[保存帖2](https://x.com/i/status/1417412355604975621)。"
  ],
  [
    "by-type/waf-bypass.md",
    "不同text与search入口的过滤比较",
    "Cloudflare配图一张text入口被拦截，另一张search路径出现prompt。路径改变可能更换handler、前端代码或规则，不能直接归因相同过滤被绕过。\n\n保持资产、身份、入口、实际输出sink和规则环境一致，保存每步规范化及服务端/浏览器各自响应。先确认同一受保护消费者，再比较变体；不同路由、静态演示或仅浏览器侧构造都是反例。没有真实同入口结果时保留候选等级。\n\n来源：[保存帖1](https://x.com/i/status/1417965150066388997)。"
  ],
  [
    "by-type/xss.md",
    "bogus comment与空HTML注释提前闭合",
    "图片把单连字符形式概括为HTML5注释语法变化。按[WHATWG tokenizer](https://html.spec.whatwg.org/multipage/parsing.html#comment-start-state)，bogus comment和正式注释的开始状态是不同解析分支。\n\n跟踪原始字符、markup declaration分支、bogus/comment-start状态与实际结束符；正式注释起始仍需两个连字符，空注释遇特定结束符可提前闭合。不能凭肉眼认为后续标签都在注释内；无真实输出上下文或只被文本展示是反例。只按规范纠正描述，未运行示例。\n\n来源：[保存帖1](https://x.com/i/status/1417646726412972035)。"
  ],
  [
    "by-type/idor-access-control.md",
    "文件删除success字段与方法授权的最终状态",
    "自有上传455后delete图为200而success0；另帖只给GET他人对象401后建议DELETE，billing GET403/POST200也缺最终内容。HTTP方法与对象权限需分别验证。\n\n在受控对象上关联actor、owner、实际handler、业务success及权威资源状态；读取拒绝不证明写入也拒绝，200也不证明删除成功。自有合法操作、统一失败页与资源未变化是反例，不能扩展为DoS或越权已确认。破坏性最终动作需使用允许的合成对象与可恢复设计。\n\n来源：[保存帖1](https://x.com/i/status/1417759788457336834)、[保存帖2](https://x.com/i/status/1419009336303505412)、[保存帖3](https://x.com/i/status/1419982326230966276)。"
  ],
  [
    "by-type/ssrf.md",
    "图片获取的DNS与HTTP及SMTP协议证据",
    "帖从图片URL回连推到25端口SMTP并建议扫描。DNS解析、HTTP回连和某个端口可连接均未给SMTP命令响应或具体服务身份。\n\n关联受控marker、触发者、时间、实际发起端与协议响应；区分DNS预解析、重定向、错误处理和最终图片消费者。只有DNS、TCP连接或外部检测标签是反例，不能补SMTP会话、内网数据或后续执行；端口候选不扩当前范围与动作许可。\n\n来源：[保存帖1](https://x.com/i/status/1417763344820228096)。"
  ],
  [
    "by-type/business-logic.md",
    "支付Success参数与可信网关回执",
    "把Cancel改Success后页面称已支付的建议缺权威账本。客户端跳转、订单展示与结算是独立状态。\n\n绑定受控订单、金额/币种、网关交易主体、签名回执、服务端查询、幂等键及最终账本/履约。页面改变而账本未付、拒绝不一致签名、合法退款或测试模式是反例；只有客户端success不能认定免费购买，也不开展真实支付。\n\n来源：[保存帖1](https://x.com/i/status/1417791466181599233)。"
  ],
  [
    "by-type/business-logic.md",
    "金额符号与余额预留及并发账本守恒",
    "负金额、超过余额和race建议提供三种输入方向，没有实际交易结果。数量字段与可用余额、已预留额和退款状态共同构成消费合同。\n\n按金额精度、币种、合法范围、余额预留、并发提交的单次消费及退款对账建立不变量；观察同次最终余额、订单和权限。浮点展示、预期拒绝或只是pending不是获利证据。采用受控仿真数据记录时序和失败，不从候选推真实资金变化。\n\n来源：[保存帖1](https://x.com/i/status/1420193626806755329)。"
  ],
  [
    "by-type/business-logic.md",
    "接收者数组的逐项权限与fanout预算",
    "receiverid从单值改数组被描述为发垃圾消息。数组是否允许由API批量用途决定，类型变化本身不构成缺陷。\n\n记录标量/集合schema、每个受控接收者的权限与同意、最大fanout、重复接收者处理和动作计数。合法批量接口是反例；若只检查数组外层而跳过成员授权，需以最终受控动作证明。不发送真实垃圾消息，错误码变化不能补投递结果。\n\n来源：[保存帖1](https://x.com/i/status/1418788645990019074)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "SSRF流水线的输出文件与最终输入集合",
    "长图assetfinder/wayback写urls.txt，gau写1.txt，后续只消费1.txt；还有间隔引用和重定向语法不明确。列出工具不代表各来源已汇合。\n\n按源记录ID、精确文件名、管道边、解析失败、去重键和最终集合hash核对来源保留；保留HTTP200与回连语义的区别。未消费文件、模式标签错配或失败被丢弃都缩小覆盖，不能计全部历史URL已测或盲SSRF已发现。源脚本未执行。\n\n来源：[保存帖1](https://x.com/i/status/1418432696238280708)。"
  ],
  [
    "discovery/web-and-api.md",
    "历史源站IP与301响应头的消费者身份",
    "ViewDNS图含2021/2015历史IP，两个curl301分别带Cloudflare和Varnish。历史地址与头部差异没有展示同次强制IP及TLS/Host绑定。\n\n绑定观察时点、当前资产归属、连接目标、SNI/证书、Host、路径和同一受保护内容；历史转租、共享地址、不同路由和普通重定向是反例。架构图、旧记录与301都不能证当前源站可绕过WAF，Cookie也不补权限。\n\n来源：[保存帖1](https://x.com/i/status/1418450675898322946)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "ASN扫描丢端口与主机协议归一化",
    "ScanApple长图先安装工具再广泛端口扫描，awk提第二列后接httpx和sort。若第二列只保留IP，端口与协议候选会丢失。\n\n使用结构化host/port/protocol/source/time记录，区分扫描输入、可达服务、HTTP转换失败和最终去重项；保留非HTTP服务及原始错误分母。ASN组织归属不证明共享/租户资产许可，安装命令和all ports标题不证真实覆盖，未安装或执行该流水线。\n\n来源：[保存帖1](https://x.com/i/status/1418750657473900544)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "file URL变量文本与实际本地读取者",
    "两图在PHP实验中比较混入变量的file路径和普通passwd路径，并显示array。字符串变形可能发生于不同层，不能仅从输出推远程SSRF。\n\n保留原始输入、真正执行替换的消费者、URI解释、规范化路径及读者权限，比较最终对象是否相同。变量只是字面、应用自行替换、本地训练环境或统一输出均是反例；未见代码时不假定shell插值，也不认定通用过滤绕过。\n\n来源：[保存帖1](https://x.com/i/status/1418849356438917120)。"
  ],
  [
    "source-audit.md",
    "JSP控制字节与AJP映射的源码消费者",
    "两张提示图将mod_proxy_ajp/mod_jk与JSP路径控制字节关联，未给实际源码响应。URL路由、授权检查和后端脚本处理可能采用不同表示。\n\n关联准确版本/配置、原始字节、前端规范化、worker映射、实际文件与后端解析；比较被当静态文本和真正解释执行的结果。普通JSP执行、路由拒绝和无敏感配置是反例；仅标签或历史技巧不证当前部署泄露，也不复制配置秘密。\n\n来源：[保存帖1](https://x.com/i/status/1418900025518829578)。"
  ],
  [
    "by-type/idor-access-control.md",
    "报表生成与PDF存储及下载的租户权限",
    "导出reports/组织参数与PDF用户参数被称BOLA，内部分工被当绕过原因。安全边界在各个实际消费者，而非团队名称。\n\n关联请求actor/tenant、生成任务、查询条件、产物存储键、下载能力和有效期；以受控两身份比对最终私有制品。合法公开报告、同租户允许分享与拒绝错误页是反例，生成时鉴权不自动保证下载时仍绑定主体。\n\n来源：[保存帖1](https://x.com/i/status/1418930621473345542)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "TLS Pass Through与可观察流量的覆盖缺口",
    "帖子为减少代理噪声给提供者域名正则和TLS Pass Through配置。减少解密记录也会改变能够观察的请求内容。\n\n保存匹配主机和规则时点、是否仅隧道转发、当前捕获边界及显式排除项；流量仍发生与代理可见正文分开计数。不能把空日志算无请求，也不能因提供者域名常见就排除目标依赖中的关键流程，配置菜单宣称不是已测覆盖。\n\n来源：[保存帖1](https://x.com/i/status/1419204383288463360)。"
  ],
  [
    "discovery/passive-and-services.md",
    "证书subject搜索与各查询语言的资产归属",
    "FOFA/Shodan字符串把Set-Cookie、证书subject和TARGET组合，两个查询消费者的字段与语法不可直接互换。\n\n保存平台、完整查询、字段解释、观察时点及结果中的host/IP/证书关系，随后按当前规则核实租户归属。共享证书、过期扫描、泛域名与第三方服务是反例；语法看似相似不等于同集合，搜索命中不扩测试范围。\n\n来源：[保存帖1](https://x.com/i/status/1419227144819920899)。"
  ],
  [
    "by-type/ssrf.md",
    "OpenGraph二次图片获取的逐跳scheme合同",
    "正文描述页面先获取HTML，再按og:image生成缩略图，提示file路径。允许外层页面不意味着内层图片URL继承相同安全策略。\n\n逐跳关联原始URL、base/相对解析、重定向、scheme允许集、目标权限、图片解码和最终制品；外层fetch、元数据读取和内层fetch分开。file被拒、只存字符串或缩略图未含目标数据是反例；缺最终输出不能声称本地敏感文件读取。\n\n来源：[保存帖1](https://x.com/i/status/1419298720835784709)。"
  ],
  [
    "discovery/passive-and-services.md",
    "反向RDP转发的既有客户端与出站权限",
    "Rconn图client已有3389、向server1111连出再暴露2222。结构说明反向转发，并不证明对任意内网或防火墙拥有访问能力。\n\n关联获准端点、已运行客户端、已有RDP监听、出站策略、server绑定地址及最终认证主体；NAT穿越和RDP登录权限分别证明。端点未授权、出站拒绝或监听不存在是反例；仅架构图不补程序执行、有效会话或规则绕过。\n\n来源：[保存帖1](https://x.com/i/status/1419420702864777228)。"
  ],
  [
    "by-type/xss.md",
    "jQuery预过滤与option包装的版本分支",
    "截图两个CVE标题重复但内部示例不同；[官方3.5.0说明](https://blog.jquery.com/2020/04/10/jquery-3-5-0-released/)和[3.5.1解释](https://blog.jquery.com/2020/05/04/jquery-3-5-1-released/)分别说明htmlPrefilter正则处理和旧浏览器option包装相关分支。\n\n区分原生innerHTML与jQuery .html/.append的实际消费者，记录真实加载版本、输入来源、预处理和兼容恢复配置。3.5.0修复不能被截图旧编号替代；已修复且未恢复旧行为、普通文本或未走该分支是反例，示例按钮未点击也未执行。\n\n来源：[保存帖1](https://x.com/i/status/1419510462937325572)。"
  ],
  [
    "by-type/csrf.md",
    "密码重置helper表单与浏览器环境的真实状态",
    "重置UI、POST302和Burp生成CSRF HTML使用当前Cookie；另一帖称JWT复制到Cookie后90%可CSRF。都没有给真正跨站浏览器和最终密码状态。\n\n绑定受控第三方origin、Cookie发送条件、SameSite、认证来源、Origin校验、恢复challenge及最终权威状态。助手生成表单、手工带Cookie成功或同站操作不是跨站证明；没有环境凭据、challenge已失效或动作被拒都是反例，不采用90%比例。\n\n来源：[保存帖1](https://x.com/i/status/1419614979880218628)、[保存帖2](https://x.com/i/status/1419687105811394560)。"
  ],
  [
    "source-audit.md",
    "Joomla模板配置与跨版本条目的匹配",
    "Juumla图识别1.5.15却列多条3.x内容，configuration.php-dist标PossibleReadable。识别产品与候选列表不自动匹配受影响版本或活跃秘密。\n\n绑定获准制品/版本、启用功能、真实路由和响应字段；模板文件与实际运行配置分开。默认示例、版本不符和只显示可能可读都是反例；扫描标题、默认凭证列表和奖励邮件不能补最终访问权，不尝试截图凭证。\n\n来源：[保存帖1](https://x.com/i/status/1419647315246297092)、[保存帖2](https://x.com/i/status/1420384846652723205)。"
  ],
  [
    "by-type/host-header.md",
    "loopback解析与自己机器的真实服务身份",
    "两份不同hash图将域名解析127.0.0.1，再比较域名403和IP200。loopback指向请求者所在网络命名空间的本地监听者。\n\n保存解析位置、连接端点、实际服务进程/证书、Host路由和最终对象；确认是否同一获准远程资产。自己机器的不同vhost、不同监听或正常路由是反例，200变化不能补远程越权。不要因截图域名标签将本地结果写成真实站点绕过。\n\n来源：[保存帖1](https://x.com/i/status/1419660307849367555)、[保存帖2](https://x.com/i/status/1419844232320274444)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "SMTP入队与邮件落盘及PHP include的断点",
    "PHP5.1.6实验可读passwd/proc，进程UID100；SMTP图仅250 queued PHP文本。文件读、邮件接收、落盘可读和解释执行是独立能力。\n\n逐段绑定受控输入、实际队列/存储路径、读权限、include消费者和解释器语义；proc里的UID不是root或可写权限。仅passwd读取、SMTP入队、文件未落到可达位置或文本未被解释都是反例，不能补RCE；未发送邮件或运行代码。\n\n来源：[保存帖1](https://x.com/i/status/1419661873541050376)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "ASM数据库差异与定时通知的动作边界",
    "SpiderFoot→SQLite/Datasette→Aquatone/截图→cron新增域名通知的方案同时包含采集、展示和外部发送。工具串联没有证明任何部署已完成。\n\n给观察记录保留来源、身份、时点、稳定键与真实集合差异，区分新发现、移除、失败和重复；截图/数据库接口还有各自访问权限。通知需明确授权和可审阅内容；不把刷新时间当新资产，不创建定时任务或发送消息。\n\n来源：[保存帖1](https://x.com/i/status/1419673864766898180)、[保存帖2](https://x.com/i/status/1420761036899045381)。"
  ],
  [
    "source-audit.md",
    "WordPress安装向导与活跃配置的写入状态",
    "正文从wp-admin403而setup-config step1可达推可创建库和提权。安装页面的可达性与既有配置、数据库写权限和最终管理能力不同。\n\n绑定实际部署状态、已生效配置、向导读写消费者与被允许的受控数据库/账号；只到步骤页、配置已存在、只读文件系统或拒绝配置写入是反例。没有权威状态变化时保留候选，不执行安装、建库或覆盖配置。\n\n来源：[保存帖1](https://x.com/i/status/1419894329447915521)。"
  ],
  [
    "targeted-fuzzing.md",
    "COOK组合与编码变换的候选分母",
    "四张长图展示组排列、范围、日期、空分隔符、大小写/leet/Base64/hash及BasicAuth。候选生成、传输编码和摘要各有不同消费者。\n\n固定输入组、顺序、空值/重复规则、日期范围、每步字节、输出schema与总候选预算；先明确实际字段合同再选择生成维度。笛卡尔积计数、5500sets缓存和工具功能表不是请求覆盖；hash不是可逆编码，生成多不代表有效或已发送。\n\n来源：[保存帖1](https://x.com/i/status/1420004362378629124)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "远程JSON path转basename后的来源丢失",
    "COOK长图每次取远程集合，JSON path经basename、sort去重再smartjoin短文件名候选。相同basename可能来自不同主机和目录。\n\n保存原始来源URL/版本/取回时点、完整path、解析异常及变换映射，展示名不能替代稳定证据键。缓存旧、字段缺失或去重误合并会改变分母；IIS短名候选与真实文件存在分别证明，未取回外链或运行源脚本。\n\n来源：[保存帖1](https://x.com/i/status/1420004362378629124)。"
  ],
  [
    "targeted-fuzzing.md",
    "无效方法与字段错误的解析层归因",
    "建议把age改数组、引入Unicode或改方法，且把http//缺冒号描述成分号问题。原始wire合法性先于应用字段消费。\n\n记录精确字节、传输解析、代理规范化、方法路由、body schema和错误产生位置；用正常受控输入比对。代理直接拒绝、类型错误和普通异常文本都是反例，不能推SQL/XSS消费；不得静默修正载荷再声称原例成功。\n\n来源：[保存帖1](https://x.com/i/status/1420032891283775495)、[保存帖2](https://x.com/i/status/1420033312681250827)。"
  ],
  [
    "reporting.md",
    "历史报告Markdown与新回归收据",
    "旧帖建议Copy Markdown重复报告以检查修复。本地保留历史报告可帮助重建条件，不能代替当前许可和当前结果。\n\n保留旧版本/身份/输入/影响的来源，同时新增当前版本、范围、同次请求响应、最终状态及反例；清理token、Cookie、个人数据。历史标题、Dup聊天、本地DOM改展示和分数差异都不补新漏洞或欺诈结论，不自动提交历史报告或刷POST。\n\n来源：[保存帖1](https://x.com/i/status/1420054205675442183)、[保存帖2](https://x.com/i/status/1419947518293471232)、[保存帖3](https://x.com/i/status/1419973817309487105)、[保存帖4](https://x.com/i/status/1418814628872732675)、[保存帖5](https://x.com/i/status/1419818055002165253)。"
  ],
  [
    "by-type/authn-session.md",
    "SQL截断注册与登录规范化的身份一致性",
    "长邮箱注册图302到back.php，随后200 CSS Library页未显示身份。SQL截断属于存储/比较和唯一性合同问题，不自动等于SQL注入。\n\n比较输入字符/字节长度、存储列长度、SQL模式、collation、唯一约束、注册去重与登录查找的规范化结果；核对最终受控账号身份。严格拒绝、唯一冲突、显示页不含身份和只截UI都是反例；缺实际存储记录不能声称接管。\n\n来源：[保存帖1](https://x.com/i/status/1420063979032891396)。"
  ],
  [
    "by-type/idor-access-control.md",
    "保单HTML属性与私有PDF制品的不同权限",
    "邮件/支付UI、rawHTML GrepExtract和Intruder200展示保单相关字段；字段出现与跨账号私有文档读取不是同一结果。\n\n对受控双方关联保单owner、页面字段公开性、任务与PDF存储键、下载主体和实际制品内容；限制样本并保留失败。只读自有数据、遮挡编号、公开说明和200错误页是反例，不推全部保险记录已泄露或自动下载真实文档。\n\n来源：[保存帖1](https://x.com/i/status/1420275806975062019)。"
  ],
  [
    "source-audit.md",
    "dot HISTFILE的执行语义与只读取证",
    "帖子把dot HISTFILE当快捷查看历史。已核对本机Bash内建help：dot读取并执行指定文件中的命令，不是普通显示文本。\n\n历史内容按未信任数据保留快照、hash与时间，使用只读文本解析器读取；不得source或重放其中命令，也不从记录推当前命令成功。调用帮助不涉及读取用户历史；本轮没有打开个人HISTFILE或执行其内容。\n\n来源：[保存帖1](https://x.com/i/status/1420502171582439427)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "MongoExpress会话与后端数据库认证的分层",
    "MongoExpress图显示admin/config/local/testdb、MongoDB4.4.6、8086以及连接统计。Web界面可能以自身受控凭证访问数据库，不能推出原生MongoDB未认证。\n\n分别记录浏览器/Web账号、管理界面准入、后端连接身份、数据库角色与具体读写动作。库名可见、UI按钮和软件版本都不能补写权；合法管理会话、只读委托和仅公开元数据是反例，不点击写入、删除或导出按钮。\n\n来源：[保存帖1](https://x.com/i/status/1421047723399204869)。"
  ],
  [
    "discovery/passive-and-services.md",
    "433MHz解码校验与发射者身份",
    "rtl433图含2018时点、433.92MHz、Bresser/Nexus温湿度、SNR和checksum。解码成功或校验一致说明格式观测，不提供密码学身份认证。\n\n关联获准接收环境、频段、设备候选、时间、原始帧与校验/测量限制；温湿度值与当前实际物理状态分别判断。旧日志、重放、干扰或仅格式校验都是反例，不推真实位置和当前采集已发生，也不操作无线设备。\n\n来源：[保存帖1](https://x.com/i/status/1421096863948853248)。"
  ],
  [
    "scope-and-rules.md",
    "TXT平台关联与选点快照及第三方令牌归属",
    "DNS TXT平台验证、MoneyScope3196域名/1824TLD/5日数据与第三方Google/FB token的奖励问题分别提供关联、选点或凭证线索。都不能补当前测试许可。\n\n逐资产保存当前规则时点、资产类型、精确匹配/排除、允许动作及凭证audience/scope与所属应用；平台关联不表示私有项目正在开放。旧范围表、共享租户和有效但不属目标的token是反例。曝光与验证使用分开，不由奖励问题推允许登录或数据访问。\n\n来源：[保存帖1](https://x.com/i/status/1420019409591017472)、[保存帖2](https://x.com/i/status/1421147273615003649)、[保存帖3](https://x.com/i/status/1421332549490642944)。"
  ],
  [
    "by-type/xss.md",
    "Akamai ARL上游获取与展示origin的分离",
    "ARL正文路径7/0/33/1d与截图7/100/33/1d不同，另含上游citysearch和SVG候选。CDN获取、缓存与浏览器展示origin是不同权威边界。\n\n保留准确路径参数、上游URL、返回Content-Type、缓存/转换、实际document origin及输入控制者；不能将不同路径当同次PoC。上游自身页面、被当图片/下载或脚本未进入展示消费者是反例，不推广为所有Akamai部署或当前CDN绕过。\n\n来源：[保存帖1](https://x.com/i/status/1421176297548435459)。"
  ],
  [
    "by-type/host-header.md",
    "代理头与方法覆盖的逐消费者信任",
    "长图混列ClientIP/XFF/XOriginalURL、重复Host、absolute URI、http0.9、折行、MethodOverride及Accept路径。它们影响不同解析层，不能作为通用绕过组。\n\n记录原始wire、连接源、可信代理hop、外部头清洗、重复字段合并、方法/路径规范化、授权与最终handler。客户端自报IP不等于可信来源；忽略头、无Override消费者、语法被拒或不同vhost是反例，不能只凭状态变化认定越权。\n\n来源：[保存帖1](https://x.com/i/status/1421235132065779712)。"
  ],
  [
    "source-audit.md",
    "HTTP制品服务与子进程队列的执行证据",
    "LightMe图为脚本服务8080 HTTP200、MAX child-process wait；DNSStager图仅help。生成、可下载和排队不等于制品实际运行或逃逸检测。\n\n给制品记录独立hash、生成环境、传输完成、真正接收者、子进程完成/失败及授权实验效果。HTTP200、ServerStarted和等待日志只属于局部阶段；没有同次执行收据或只有旧控制台是反例，不从混淆/广告推AV绕过。\n\n来源：[保存帖1](https://x.com/i/status/1421232849336905731)、[保存帖2](https://x.com/i/status/1416953552925347844)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0106.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==65 and len(urls)>0
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

