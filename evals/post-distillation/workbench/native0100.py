"""Append only this task's reviewed prose, without executing source material."""
from collections import defaultdict
from pathlib import Path
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
facets=[
('by-type/sql-injection.md','注释换行、DISTINCTROW与两套词法消费者','''旧帖组合%23、%0A、UNION、块注释及distinctrow，并夹有.0union片段。先保留HTTP原字节→实际解码/规范化→过滤器→数据库查询模板与词法；URL编码文本在未解码阶段并不是数据库注释。注释是否结束、查询是否仍合法、列数/类型及结果消费者均需真实条件。

[MySQL8.4注释说明](https://dev.mysql.com/doc/refman/8.4/en/comments.html)规定#到行末、双横线需后续空白/控制字符、块注释到关闭符；[SELECT说明](https://dev.mysql.com/doc/refman/8.4/en/select.html)将DISTINCTROW描述为DISTINCT同义词（2026-10-10核读相关段落）。这是该方言语义，不是WAF绕过保证或.0union有效性证明。用获准模板/合成普通值核对参数化和两层解释差异，不执行源SQL或导出数据库。来源：[保存帖](https://x.com/i/status/1401103424746229760)。'''),
('by-type/lfi-path-traversal.md','nginx别名替换、目录边界与PHP静态字节','''旧例用/assets../index.php对比/index.php的File not found与source code，建议替换img/js/assets等名称。关键是实际location匹配、alias/root、尾斜线、解码/规范化、文件系统边界及后续handler，不是名字或404指纹。[nginx alias文档](https://nginx.org/en/docs/http/ngx_http_core_module.html#alias)说明替换location并示例URI到文件映射，正则location还涉及捕获（2026-10-10核读alias段）。

由该映射语义推导候选边界：若匹配前缀与实际目录拼接留下上级路径，需核对最终文件位置及拒绝规则；这仍需目标配置/字节证据。PHP文件经静态路径读出与PHP解释执行不同，成功状态不等于源码。优先获准配置和不同内容的合成允许/越界/不存在文件对照，不读取真实源码秘密或向所有nginx404投路径。来源：[保存帖](https://x.com/i/status/1401259603845918722)。'''),
('by-type/cmd-injection-rce.md','shell短路、命令替换与盲观察器','''旧建议在ampersand失败后换管道/逻辑操作符、借命令替换构造DNS、用ping作盲观察。管道、短路与后台分隔影响执行条件/输出，不是同义字符；命令替换还要求真实shell解析，直接argv调用可把字符当普通数据。沿参数位置、引用、调用方式、shell/平台、执行身份及失败路径恢复消费者。

DNS只证相关解析事件，不能把准备读取并外传whoami的字符串当实际结果。ping -c片段的次数/目标位置需该实现合法参数，单次耗时还需排除网络超时/负载；不可默认它提供延时。用获准源码或隔离无外联合成调用解释数据边界，不执行源命令、外传输出或通过真实DNS放大盲证据。来源：[保存帖](https://x.com/i/status/1401440942247354371)。'''),
('discovery/passive-and-services.md','shell伪设备连接与端口开放的观察范围','''Bash图循环254个地址和22/80/443/3306/3389五个端口，并对/dev/tcp重定向写入。每个候选都是主动TCP连接尝试，最多1270个候选不等于1270个已成功执行；实际shell支持、路由/策略、权限、超时和退出状态决定观察。未显示超时并不说明有限时间内一定结束。

连接建立、端口标签、应用协议/身份及漏洞不同；拒绝、超时、伪设备不支持不能统统记closed，更不能推广UDP或所有系统。以已有获准连接日志/隔离合成失败分类核对分母，保留未尝试/错误状态；该私网示例不提供实际地址段授权，本批未执行循环。来源：[保存帖](https://x.com/i/status/1401441368258531330)。'''),
('targeted-fuzzing.md','运行时词表、内存边界与恢复游标','''旧Intruder建议Runtime file用于大词表并保证不崩溃。[PortSwigger payload types](https://portswigger.net/burp/documentation/desktop/tools/intruder/configure-attack/payload-types)说明从运行时文件每行读一个payload，避免完整列表驻内存，因此该类型的payload不能含换行（2026-10-10核读Runtime file段）。这不减少总请求，也不保证响应保存/并发/扩展没有其他内存开销。

固定词表hash、编码/行界、去重/处理规则、实际插入位置和请求预算；检查点绑定制品及已执行游标，文件被改动不能默认为旧轮续跑。需多行候选时选适合的独立表示与消费者，不把显示换行误当一个词项。用自己的有限合成词表核对边界，不加载巨型密码集合或启动真实Intruder攻击。来源：[保存帖](https://x.com/i/status/1401658175716274178)。'''),
('cloud/container-k8s-security.md','RBAC图中的绑定范围与旧PSP准入','''Krane图分Subject、Binding、Role、Rule、namespace/cluster-wide，并列resource的API group/verb/name、non-resource URL及旧PSP属性。先从绑定主体到roleRef及规则恢复当前权限，不能把角色名字或图中相连箭头当实际集群生效。[Kubernetes RBAC说明](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)指出RoleBinding引用同namespace Role或将ClusterRole绑定到该namespace，ClusterRoleBinding用于集群范围（2026-10-10核读相关段落）。

RBAC是否允许具体API动作与工作负载是否通过准入不同；图中privileged false不保证所有有效路径都满足约束。[PSP说明](https://kubernetes.io/docs/concepts/security/pod-security-policy/)记录1.21弃用、1.25移除，当前需绑定实际版本及Pod Security Admission/其他准入实现。资源/非资源路径、名称限制、主体namespace和实时绑定分别核对，只分析获准配置/离线图，不部署Pod、提权或以旧图声称当前防护。来源：[保存帖](https://x.com/i/status/1401664424885342213)。'''),
('by-type/xss.md','其他主体写入将自触发变成跨读者执行','''旧例自存储name XSS，CSRF链未成立，随后通过IDOR修改name并称升级P2。应拆成外来写入权→目标对象/租户绑定→保存字段→其他合法读者→实际输出/执行语境；对象ID可改不说明目标读者必然查看或同一字段被同一消费者渲染。

确认自己以本不应有的权限写入另一合成主体对象，再用获准读者流程区分纯文本、拒绝/清理、自己手动执行及跨主体触发。不能以P5/P4/P2标签补任何边，先前失败CSRF也不自动参与新链。影响跟实际读者身份及受控业务能力，达到最小因果证据即停，不强制串更多问题或操作真实他人资料。来源：[保存帖](https://x.com/i/status/1401786510689533952)。'''),
('by-type/xss.md','冒号前缀的语句标签与URL方案','''旧帖把stop、posting及其他单词后接冒号/调用列为多条XSS载荷。同样字节由JavaScript语句解析器或URL导航消费者处理时含义不同。[ECMAScript Labelled Statements](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-labelled-statements)给出LabelIdentifier冒号LabelledItem语法及语句求值（2026-10-10核读语法/求值段）；换标签名不会凭空建立外来输入到代码的边。

若在href或导航地址中，前缀先参与URL方案解析，任意标签不等于javascript方案；还要实际导航、策略/允许方案及执行语境。只用静态语法/获准合成普通标记区分消费者，不执行这些调用。已有控制台执行与目标外来输入执行分别记，同义标签变体不计独立漏洞。来源：[保存帖](https://x.com/i/status/1401796179252424708)。'''),
('discovery/records-and-incremental.md','favicon候选集、冒号切分与TLS发行者筛选','''F5图从Shodan favicon哈希命中，经grep/cut提host、httpx400并发/四端口及CVE模板，再对独立targets.txt以100并发curl insecure取得issuer并排除root localhost文本。指纹命中是候选，历史搜索不能称所有F5 IP；output.txt、results和targets.txt是否同集合必须有制品/变换证据。

冒号定界切字段可能截断IPv6/端口/结构值，保留完整地址族、协议、端口和原始记录，不把文本行当有效host。TLS关闭验证后的握手/issuer字样不能证明可信身份，排除一个issuer字符串也不证明其余证书可信或产品归属。分别记录每阶段筛选/错误/未完成与总预算，用有限自有合成文本核对解析，不运行Shodan查询、模板或TLS扫描。来源：[保存帖](https://x.com/i/status/1401844465116061697)。'''),
('by-type/host-header.md','来源头的优先序与IP文本比较','''block.php三图展示CLIENT_IP优先于X_FORWARDED_FOR等字段，最后REMOTE_ADDR回退，并将返回字符串严格比较允许IP；随后加XFF与welcome画面。应用选中的字符串、真正连接来源和经可信代理确认的来源不同，任意来头若优先覆盖连接事实便改变该示例的选择器。

沿边缘重写/清除、可信代理名单、多跳解析、字段优先序、地址族及服务端规则核对；单一允许IP文本不是一般CIDR或可靠身份。图中IP Log shows只是echo描述，未显示持久日志写入，拦截待发送也不等于服务器已消费。正常代理、直连拒绝与获准合成对照解释实际权限，不从页面问候推生产敏感数据开放或伪造真实网络身份。来源：[保存帖](https://x.com/i/status/1402145788420050944)。'''),
('by-type/xss.md','JSONP脚本消费与CORS凭据响应头','''旧建议在缺Access-Allow-Credential true时用JSONP取数据；CORS对应响应头实际为Access-Control-Allow-Credentials。fetch/XHR读取、经典script执行与module请求是不同消费者，不能把任意JSON接口变成JSONP。目标需真实返回可执行回调，并在该请求方式下实际带上所需身份和返回敏感内容。

[HTML script说明](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element)区分classic与module，跨来源module要求CORS（2026-10-10核读script属性段）。JSONP还要核对回调名/净化、Cookie/SameSite/第三方策略、Content-Type/nosniff、CSP及跨源资源限制；缺某个CORS头不是所有这些前提的证明。只分析获准脱敏响应/合成公开回调，不加载真实私密JSONP或借挑战链接读他人数据。来源：[保存帖](https://x.com/i/status/1402236597664321543)。'''),
('discovery/passive-and-services.md','PTR、SAN和AAAA到IPv6候选的关联边','''IPv4/IPv6来源图将反向PTR、CT SAN、被动DNS、BGP、注册域、猜地址、P2P及监听并列。域名字符串、证书关联、AAAA回答、路由前缀和当前服务不同；每条边保存来源/时点/地址族/完整前缀与当前归属，PTR或同IP不能自动提供目标资格。

先从获准现有材料恢复有限候选并沿已有IPv6观察能力条目核对环境；IPv4正常不替代IPv6消费者，BGP登记也不授权全部子网。主动DNS/连接、地址猜测、P2P、抓包及外部采集服务分别判断具体范围与预算，不能继承图中大规模猜常见hex或监听建议；IPv6发现扩候选，不自动扩动作授权。来源：[保存帖](https://x.com/i/status/1402295002126946306)。'''),
('discovery/records-and-incremental.md','无头浏览器采集的资源请求与脚本消费者','''page-fetch被描述为加载网页及JS/CSS/图片/XHR并可执行任意JS。URL清单从静态资料而来不使后续浏览器动作被动；导航会按页面逻辑产生额外目的地、脚本执行及身份/状态消费，抓取按钮也不是零副作用保证。

采集前固定制品/配置、初始URL、身份隔离、每种destination/第三方范围及请求/重试预算，记录实际资源轨迹与未观察/阻断/超时。来源标记或过滤日志不能阻止出站，执行-j判断是额外代码消费者。用获准离线制品/隔离无外联页面核对集合，不执行源page-fetch管线或从页面截图声称全站/漏洞完整覆盖。来源：[保存帖](https://x.com/i/status/1402369973830524932)。'''),
('by-type/xss.md','团队名模板、悬停渲染与编译作用域','''旧帖说团队名模板表达式回显为1，悬停图标弹窗，并称CSTI。先定位字段保存/读取、组件模板编译、表达式作用域、事件渲染及执行读者；单次算值和弹窗描述不说明服务端模板执行，更不能由self名称推每个引擎均暴露同一全局对象。

服务端模板渲染、客户端模板表达式及普通文字插值分开，绑定实际框架/制品/模式、净化后值、编译时点及策略。用获准隔离普通标记与不编译数据的反例解释输入是否成为程序，影响仍需真实跨主体读者。无脚本或悬停记录时保留证据缺口，不求值源表达式、访问团队或将CSTI自动标服务器RCE。来源：[保存帖](https://x.com/i/status/1402527470838947844)。'''),
('discovery/web-and-api.md','路由树、父路径与物理文件的不同集合','''旧帖指出/admin/users存在不代表/admin有页面。路由器可将请求分发到单入口，不要求每个路径前缀都是目录或独立路由；父路径404不消除子路由，父目录存在也不保证某个子操作存在/可访问。

以获准路由表、正常业务流和客户端调用记录恢复方法/参数/消费者，分别保留文件映射、静态资源、API和虚拟业务路径。发现/权限均在真正子操作核对，不用截断URL的递归猜测替代路由契约或以相同长度错误页证明新端点。有限合成正常/不存在路径可以解释回退逻辑，无需执行所有父子词表。来源：[保存帖](https://x.com/i/status/1402749647224029185)。'''),
('by-type/xss.md','IDNA主机映射与已取得的JavaScript调用','''日语解说图用anchor设置圈字母HTTP主机，读取a.host得到alert，再通过top的计算属性和tagged template调用；正文代码还带自动链接样式，不能把保存文字与图中语法视为字节完全一致。URL主机映射、字符串值取得、函数引用和JS调用是不同消费者，图为控制台操作，没有外来输入破坏目标数据边界。

[URL Standard IDNA](https://url.spec.whatwg.org/#idna)规定domain parser ToASCII使用Unicode IDNA Compatibility Processing/UTS46（2026-10-10核读当前算法）；不能将所有URL规范化简化成NFKD或推广任意圈字符/浏览器结果。圈主机属性被解析不等于导航/请求已发起，无括号调用语法仍需先有JS执行。只审提供图/规范，不运行表达式或称Twitter已发现XSS。来源：[表达式帖](https://x.com/i/status/1402878611967774722)、[解说帖](https://x.com/i/status/1402881494066946048)。'''),
('by-type/prototype-pollution.md','原型检测标记、否定匹配与失败分母','''旧自动化管线查询中写testparam值exploit/，JS判断却与exploit比较；grep VULNERABLE还会保留NOT VULNERABLE，配图两种输出确实同列。先逐字核对URL生成→实际query解码→属性值→判断→结构化结果，避免正负共享子串。[URL query state](https://url.spec.whatwg.org/#query-state)及编码集合保留查询里的普通斜线语义；图未显示应用额外去尾斜线处理，不能无证据补齐值差异（2026-10-10核读）。

window属性相等仅定位观察，还需排除自身属性/页面预置值，确认原型变化、隔离生命周期及真实gadget读取；污染不自动XSS/RCE。stderr重定向隐藏错误，不能把超时/解析失败计阴性或已完成；grep后的列表也不是有效漏洞数。用自己的有限合成正/负/错误记录核对判定，原来源脚本、无头浏览器/JS和外联请求均未执行。来源：[保存帖](https://x.com/i/status/1402906185301323776)。'''),
('by-type/host-header.md','同IP、DNS与虚拟主机路由的不同事实','''vhost配图说多个名称到同IP意味着在该主机etc/hosts中配置；这推断不成立。名称解析可来自DNS/客户端静态配置等，服务器依据TLS SNI、Host/:authority、端口/代理及具体virtual-host规则选消费者；共享IP不证明同租户或同权限。

固定真正连接目标并记录各层名称、实际后端、默认站点和允许/拒绝响应，核对同IP多个应用的身份/缓存/流隔离。每个新Host或租户仍需正式范围，即使连接IP没变、速率有限也不能自动覆盖第三方。以获准配置/既有日志或合成虚拟主机解释路由，不继承图中任意名字穷举或因作者判断风险低就跳过具体隔离证据。来源：[保存帖](https://x.com/i/status/1402936148578783233)。'''),
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
print('Added',len(facets),'native facets and community routes to',len(grouped),'topic files')
