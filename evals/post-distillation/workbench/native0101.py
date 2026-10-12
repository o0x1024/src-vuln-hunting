"""Append this batch's reviewed prose only; source examples are never executed."""
from collections import defaultdict
from pathlib import Path
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
facets=[
('by-type/authn-session.md','Adminer默认凭据与数据库到系统的能力边','''旧帖串联子域发现、目录扫描、Adminer root/root与完整数据库，配图标题称内部访问RCE/P1 Triaged。管理入口存在、凭据被接受、数据库账号权限、可读数据及数据库到操作系统能力必须分别绑定；数据库root名称不等于操作系统root，报告分类也不补执行结果。

以获准配置/既有脱敏记录核对入口暴露、认证来源、真实账号和最小权限，区分匿名、已登录管理员与不应有权限的读者。默认凭据是候选前提，不推广所有部署或以五分钟宣传承诺结果；本批没有登录、运行SQL、导出数据库或尝试系统执行。来源：[保存帖](https://x.com/i/status/1403120079911403522)。'''),
('by-type/authn-session.md','Jira组件枚举与公告更新后的版本和匿名权限','''旧帖将QueryComponentRendererValue!Default.jspa与CVE-2020-36289关联，图含Jira8.14.0、匿名标头及viewHtml用户显示名。返回用户信息与有效用户名判别需已知存在/不存在的合成主体及实际公开策略；Set-Cookie不证明请求先有登录身份，Log In文字也不证明所有请求彻底匿名。

[Atlassian记录](https://jira.atlassian.com/browse/JRASERVER-71559)保留旧描述阈值8.5.13/8.13.5/8.15.1，但明确版本清单为低于8.5.15、8.6.0至8.13.7之前、8.14.0至8.17.0之前，并列修复版8.5.15/8.13.7/8.17.0且提示开启匿名访问时修补实例也可能受影响（2026-10-10核读）。记录版本来源/更新时间/配置，不只用旧描述或页脚认当前漏洞；信息枚举不升级登录/接管，未对实例枚举。来源：[保存帖](https://x.com/i/status/1403213336800497666)。'''),
('by-type/authn-session.md','HTTP成功码中的OTP业务拒绝','''绕过频控标题所配Intruder行均HTTP200、长度536，选中响应却是JSON错误-32000和ErrResetPasswordTooManyRequests。传输完成、业务接收、挑战校验与最终重置/登录能力是不同判据；长度相同不能证明每行内容相同，错误字样也不独立证明计数策略覆盖所有主体。

固定账号/挑战/会话、计数键、窗口、正常业务成功判据与原始结构化错误，分别记未尝试/超时/业务拒绝/通过。只用脱敏历史或隔离合成记录核对判定，不由200认验证码成功，也不执行真实OTP尝试或绕过限额。来源：[保存帖](https://x.com/i/status/1403253252553011205)。'''),
('by-type/mobile-android.md','APKLeaks候选、制品版本与正式资产范围','''APKLeaks图以jq/LinkFinder提取链接并建议添加targetscope及比对旧版本。每个字符串绑定APK哈希、版本/签名、提取位置及解析规则，区分第三方SDK、示例/废弃地址与真正运行时网络消费者；工具名或secret标签不证明凭据有效。

静态找到域名只扩候选，需独立核对当前归属及正式允许资产/动作，不能直接扩大范围。旧版本差异需可信完整制品及归一规则，不把多尺寸同图算独立发现。本批没有下载APK、运行反编译工具、访问候选或复制秘密。来源：[原帖](https://x.com/i/status/1403316204337520647)、[转述](https://x.com/i/status/1403328432939966466)。'''),
('cloud/cloud-misconfiguration.md','跨云实验拓扑与真实访问控制和遥测','''BlueCloud图将Azure/AWS子网、Windows节点、管理端口和Sysmon/Winlogbeat等遥测连接并列。节点/箭头表达设计意图，端口标签不证明实际监听、SG/NSG来源规则、身份权限、隔离或采集到达；公共前端也不说明后端全部公开。

沿获准配置绑定环境/账号、规则方向/源目标/端口、实际管理身份、日志关联及隔离反例，分开部署、可达、认证和遥测观察。共享实验凭据不提供第三方资格，不复制图中密码或部署/连接机器；实验架构不能冒充生产验证。来源：[保存帖](https://x.com/i/status/1403340274932273153)。'''),
('targeted-fuzzing.md','数字候选生成、标准输入与读取完成','''旧例将seq 1 - 1000经管道交给ffuf -w -并替换user/FUZZ。先保留真实生成器argv、数字格式、范围/步长、退出状态和EOF，多出的单独减号不能静默解释成有效范围分隔。生成一千候选与实际发出一千请求、发现一千对象不同。

[ffuf维护者实现](https://github.com/ffuf/ffuf/blob/master/pkg/input/wordlist.go)在readFile的path为减号时读os.Stdin，逐行扫描并加入data列表，返回扫描错误（2026-10-10核读）；stdin支持不保证持续流式/低内存。固定版本、输入哈希/计数、变换、真实插入点与请求预算，权限仍按对象/读者契约核对；只分析文本/自有有限合成记录，未运行来源管线或数字ID探测。来源：[保存帖](https://x.com/i/status/1403601806647832577)。'''),
('by-type/mobile-ios.md','Mach-O规则匹配与真实注入的证据层','''MaliciousBitHunter结构图从FAT/ARM/ARM64、头、加载命令、类/方法/字符串、符号到签名与导入导出，并用CLlocationManager、method_implementation、hooklbs等作规则线索。匹配字符串或显示某结构不证明该架构实际加载、运行时方法替换或恶意行为；图列签名字段也不等于验证通过。

先绑定获准制品哈希、来源/签名身份、架构切片、解析器版本与完整性，和可信同版本基线比较，再用既有受控动态证据定位实际加载/调用。合法SDK、调试符号、未使用字符串和解析失败分别作反例/未知项，不能把未匹配计安全。本批仅审结构图，没有执行应用、动态钩子或签名工具。来源：[保存帖](https://x.com/i/status/1403702804355637249)。'''),
('cloud/container-k8s-security.md','Compose服务声明与主机暴露和配置内容','''旧帖建议留意docker-compose.yml，图列MySQL5.7、phpMyAdmin、WordPress及环境变量、端口、卷、网络，多数值遮盖。文件名候选、HTTP实际返回配置、部署消费者和当前访问能力分开；环境字段名称不证明有效秘密，depends_on不是认证边界。

从获准制品核对插值来源、实际运行环境、容器与主机端口、监听地址、挂载源/目标及公开读者，保留未部署/旧副本/错误页反例。图中容器端口/卷意图不能补当前主机路径或外部可达，遮盖值不恢复。本批未获取真实配置、登录数据库、部署Compose或使用凭据。来源：[保存帖](https://x.com/i/status/1404012291197001735)。'''),
('discovery/records-and-incremental.md','搜索引擎邮件候选与部分失败的分母','''EmailFinder图称Total emails37，同时YandexException因机器人检测而失败。引擎访问完成、解析到字符串、去重后的候选数及当前有效收件地址不同；三个引擎done不能替代失败引擎结果，更不提供全域邮件全集。

保存引擎/时间窗口、查询/来源制品、去重规则、失败/未完成及候选出处，以字符串作线索，不补人员身份、秘密有效性或当前可投递结论。已有索引并不授权联系/猜邮箱；本批未搜索实际目标、发送邮件或绕过机器人检测。来源：[保存帖](https://x.com/i/status/1404201032561971205)。'''),
('by-type/business-logic.md','双优惠券竞争是假设还是原子规则失效','''旧帖提出一单只准一个优惠券却并发取得两个，作者明确说还没在项目发现。可提炼的是权威业务不变量与读条件→写优惠→提交的原子边界，不是一个已确认漏洞；两个请求成功、两条UI提示或两次暂态响应不等于最终双折扣。

在获准隔离合成购物车绑定订单/用户、优惠版本、请求幂等键、并发时序与最终权威总价，先排除本来允许组合优惠、重复重试和回滚。正例需最终持久状态违反同一规则，反例是串行拒绝、原子提交或补偿恢复；仅提出假设也可记录，不购买、耗用真实优惠或制造库存竞争。来源：[保存帖](https://x.com/i/status/1404214249451229184)。'''),
('by-type/info-secrets.md','Django的CSRF拒绝页与DEBUG状态','''旧帖把登录GET200/POST403推广成DEBUG=True泄露管理员邮箱；图一仅Triaged标题，另一响应显示CSRF验证失败和荷兰文“更多信息在DEBUG=True”提示。提示字符串、拒绝理由、实际调试开关及敏感字段是不同观察，HTTP方法差异不补完整debug页或邮箱内容。

[Django5.2设置文档](https://docs.djangoproject.com/en/5.2/ref/settings/#csrf-failure-view)说明CSRF_FAILURE_VIEW处理拒绝且可用403_csrf.html覆盖；[默认view实现](https://github.com/django/django/blob/stable/5.2.x/django/views/csrf.py)分别设置DEBUG与more提示字符串（2026-10-10核读）。版本/实际模板/自定义handler及中间件次序需当前配置，不能从单句提示推开关。HEAD/OPTIONS/TRACE与POST/PUT/DELETE等有不同语义和消费者，图HEAD200/TRACE405也反对所有方法同效；只审既有响应，不向真实登录发方法变异/写操作。来源：[早帖](https://x.com/i/status/1404701480473403396)、[方法帖](https://x.com/i/status/1405106473097519114)。'''),
('by-type/xss.md','failure参数分支与真正的输出消费者','''旧建议将failure从1改0后发现XSS，借Arjun/ParamSpider找隐藏参数。参数名字被发现、服务端接受/类型转换、分支变化、外来值进入输出与浏览器执行是各自一条边；0/1字符串也不能无证据当该实现布尔值或保证相同输出语境。

沿获准调用/路由、普通合成值与默认/缺省分支核对真实契约，排除未知参数被忽略、错误页反射、纯文本与输入被净化。只有分支差而无外来数据到代码消费者仍是线索；执行读者及业务能力另证，不运行来源载荷或全站隐藏参数探测。来源：[保存帖](https://x.com/i/status/1404750164347158528)、[文章预告](https://x.com/i/status/1405158219568148483)。'''),
('by-type/waf-bypass.md','Referer三值的状态差与时点和受保护对象','''403文章图对同一interesting路径放不同Referer，前两次403、另一个子域值200，但响应Date不同且200正文没展示。可见差异不证明严格单变量、同会话、同后端或同对象，Referer也不是可靠登录身份。

在获准既有轨迹绑定时点、原始方法/身份、Host/路由、缓存及真正保护规则，判据是本不应有的敏感读取/操作而非状态或长度。公开fallback、缓存页面、后端继续拒绝均作反例，CSRF来源校验与授权/边缘放行不能混合。只审图和配置，不向全部403发送来源头变异。来源：[保存帖](https://x.com/i/status/1404754967479599107)。'''),
('by-type/info-secrets.md','swap扩展名、系统交换与有限字符串输出','''图把.swap文件、Vim恢复和system memory并列，并建议strings后head。文件扩展名不识别真实格式，编辑器交换缓冲与操作系统虚拟内存交换不是同一制品；strings只见可打印片段，head还截断集合，不能称完整源码或全部秘密。

先核对获准已有字节/头、来源路径/生命周期、格式/版本、哈希和实际公开读者，保留陈旧块、无关二进制和部分恢复的限制。恢复编辑器是额外消费者，不能默认安全打开不可信内容或执行宏/modeline；本批未运行Vim、恢复/删除文件或读取真实内存。来源：[保存帖](https://x.com/i/status/1404796054143385601)。'''),
('discovery/records-and-incremental.md','列表导出的当前行集合与报告正文权限','''Instant Data Scraper图显示Pages scraped1、Rows collected25，尚提示定位Next或开始crawl。Copy ALL指当前工具持有集合，不能由按钮词语称全部HackerOne历史报告；列表标题/金额/作者字段与报告正文、附件及私密权限不同。

以获准导出记录保存起止页/游标、过滤/排序、去重主键、采集时点和失败/未完成，结果绑定实际可访问列表。动态新增/无限滚动和访问拒绝不能记不存在，分页完整也不证明所有正文已读；本批未装扩展、抓取网站或访问私密报告。来源：[保存帖](https://x.com/i/status/1404876157183479820)。'''),
('discovery/passive-and-services.md','名称突变到DNS回答和通配对照','''旧管线dnsgen从subdomains生成名称，再经puredns resolve写valid.txt。突变只是候选，DNS成功回答、通配误报过滤、当前归属、应用服务和正式测试资格不同；valid文件名不证明这五层均成立。

绑定生成器/解析器版本、输入制品、每个查询名/类型/解析器/时间和RCODE/CNAME链，保留随机不存在合成名称的通配对照、错误/超时/未查询分母。共享地址或回答不授权新域名；只读已有结果/隔离离线区域，没有对真实域执行DNS枚举或后续扫描。来源：[保存帖](https://x.com/i/status/1404908020539269126)。'''),
('source-audit.md','服务显示名分块存储与重组执行边','''TChopper概念图将服务显示名、base64片段、CreateService和服务可执行文件消费者串联。显示名是可读数据字段，编码不是加密或执行；写入服务记录、读取片段、可靠排序/重组和启动某个消费者需各自权限及日志。

对获准已有制品/审计记录绑定主体、机器、服务身份、片段长度/顺序/完整性和真正加载内容；缺段、无执行权限或消费者未启动是反例。工具“横移”名称不证明已远程执行，本批未创建/启动服务、构造二进制或运行来源代码。来源：[保存帖](https://x.com/i/status/1404925770053701633)。'''),
('by-type/mobile-android.md','CA转换、设备写入身份与应用信任','''旧图导出Burp DER、转换PEM、计算subject_hash_old，再用样例文件名复制system cacerts并remount/reboot。哈希输出对应文件名需当前证书，不能硬抄示例；主机命令与设备shell权限不同，图中混合调用也不能默认都在已授权root设备上成功。

固定Android/设备版本、真实证书指纹、有效信任库位置、应用网络安全配置/TLS栈、代理链和pinning行为。安装成功、系统信任、应用信任和可见明文分别核对，现代只读分区/有效证书库布局也需实际环境；只审图，不挂载分区、推证书、重启设备或绕过应用校验。来源：[保存帖](https://x.com/i/status/1405160059399671811)。'''),
('experiment-design.md','发现转回归用例与live测试的完成判据','''Ugly Duck宣传五至十分钟把finding转live security test，图仅模糊JSON有firing-range/reflected路径、response和logging条件。声明功能、生成配置、运行隔离fixture与真实环境验证是不同完成状态，文件中path也不补输入/身份或结果。

用自己的合成用例固定制品版本、正常/异常输入、环境/权限、禁止外联条件、正负判据及结构化轨迹，再核对何时判失败/未知。实际获准环境复现还需当前范围及相同根因，不继承任意旧报告目标；时长宣传不替代完成回执，本批未运行源JSON/脚本或live请求。来源：[保存帖](https://x.com/i/status/1405169804986757124)。'''),
('targeted-fuzzing.md','Burp配置库与扫描规则的实际生效制品','''每周词表帖所配图实际是Custom Configuration Libraries，列速度/问题、错误处理、插入点等。保存配置、导入配置、某轮实际使用配置和发现问题不同；标题与图片不匹配时按可见内容分别归档，不补每周词表变更。

固定Burp版本、配置制品hash、有效扫描规则/插入点、身份及请求预算，记录跳过/错误和实际生效设置。图里审计/被动等标签不证明整套运行无主动请求，配置库也不是可读的完整规则集；仅审界面，不导入不可信扩展或启动扫描。来源：[保存帖](https://x.com/i/status/1405177889000132613)。'''),
]
grouped=defaultdict(list)
for f,title,body in facets:
 p=T/'references'/f
 assert p.is_file() and ('## '+title) not in p.read_text(),title
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
print('Added',len(facets),'facets and routes to',len(grouped),'topic files')
