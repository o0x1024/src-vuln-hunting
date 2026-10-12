"""Append reviewed prose only; do not evaluate any archived program or payload."""
from collections import defaultdict
from pathlib import Path
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
facets=[
('by-type/cmd-injection-rce.md','动态表达式调用与服务进程身份','''FuelCMS旧帖展示经过编码的PHP表达式、函数名间接调用，以及apache uid/gid48和网络统计输出。沿参数原字节、URL解码、表达式解释器、可调用值选择及最终系统调用恢复链；函数名藏在数据表达式里并不消除执行消费者。输出中的身份要绑定实际目标进程，不能把apache自动提升为root。

区分预先已取得表达式执行、普通返回文本和由未认证外来输入新取得的执行能力；版本、原始处理器与认证条件未显示时仍未知。获准静态调用链或隔离合成不可执行值可判断参数是否始终作为数据，反例是函数选择白名单、无解释器或拒绝表达式。图不是所有FuelCMS版本的PreAuth证明，不求值源表达式、不执行系统命令。来源：[保存帖](https://x.com/i/status/1399433335076687888)。'''),
('by-type/idor-access-control.md','导出任务、格式分支与文件交付的权限','''旧建议强调CSV/PDF下载，另一帖把MEC事件XML下载称P2；文件下载框657KB、PII报告标题或高危标签没有显示私密字段及主体。沿列表筛选→生成请求→异步任务/任务ID→格式序列化→产物存储→下载交付恢复每个身份、租户和对象集合；生成允许与产物读取允许是两条权限判断。

核对各格式是否共享对象过滤和服务端权限，不能从XML一支推所有格式；文件名、大小与成功状态也不证明私密记录泄露。用自有合成对象及获准日志区分公开导出、合法共享、拒绝和跨主体私密字段返回；预签名URL/缓存/旧任务沿原生成主体与有效期核对。无需下载真实客户数据来补影响，最小证据止于不应可见的合成字段/权威权限差异。来源：[导出建议帖](https://x.com/i/status/1399477269714771969)、[事件导出帖](https://x.com/i/status/1400535501233438725)。'''),
('discovery/records-and-incremental.md','匿名统计设置与实际收集和外传','''旧FoxyProxy图中Send Anonymous Usage Statistics已勾，Google同步未勾，发布提示开启；这些分别属于统计、同步和更新入口，不能由一个开关推其他行为。先记录制品/版本、当前配置、实际执行路径、字段、接收方与已有出站回执；匿名名称不证明字段不可关联，截图也不证明真实收集发生。

核对数据是否包含目标URL、请求内容或凭据引用等敏感信息时使用获准脱敏配置/日志，区分设置选择、配置保存、生效和实际发送。取消勾选不能无证据承诺一切跟踪停止，亦不因更新提示存在即称数据泄露。这里仅审旧图，不修改浏览器配置或上传私密HAR。来源：[保存帖](https://x.com/i/status/1399703904028225536)。'''),
('by-type/ssrf.md','回连观察器自测与目标取址的区分','''interactsh0.0.3四窗示例先取观察器地址，再由测试者curl并查看DNS A/AAAA与HTTP事件；这条链能说明某次观察器自测，却不能归因目标服务端取址。每轮把健康检查标记与目标候选标记分开，记录实际发起者、时点、协议及原始事件，排除本机自测、浏览器加载和重放造成的回连。

取址脚本还应核对stdout/stderr的重定向顺序、文件字节和固定列截取规则；截图命令与展示文件不能自动保证一致，固定第16列依赖版本/格式，空值和截断应显式失败。目标HTTP取址、仅DNS解析、返回内容及内网/云权限是分层能力，自测通过不补下一层。只核对已有脱敏日志/合成事件，不启动回连服务、运行curl或访问内网；GNU页面本次获取失败，不将其全文标已核读。来源：[保存帖](https://x.com/i/status/1399723077861265409)。'''),
('by-type/open-redirect.md','双斜线路径、Location与自动跟随的出站','''旧httpx命令将双斜线目标文本放在path并启用follow-redirects/location。请求路径里的字符串、原始响应Location、消费者解析后的目的地址和实际下一跳不同；路径包含主机样式文本不自行证明服务端返回外站导航。保存第一跳状态/原始头、解析基址、每跳目标及真正发起者，再判断允许表和范围。

自动跟随可能产生新的真实出站，应在执行前为每跳约束目的地/方法/头及预算，不能从最终页面逆推所有中间边或将第三方页面当目标内容。正常同源导航、无Location、固定服务器允许目标及不执行导航为反例；令牌带出/账号接管还需独立传递与身份能力证据。本批未运行旧命令或访问候选跳转，旧参数名称不保证当前版本相同。来源：[保存帖](https://x.com/i/status/1399732121879552002)。'''),
('by-type/file-upload.md','multipart路径文本、实际存储与CDN映射','''旧filename包含空格、重复上级路径和jpg后缀，并建议检查Web根目录/CDN。multipart字段名、声明filename、字节内容、规范化路径、存储对象键及对外URL分别记录；空格与解码步骤可能改变实际路径，不能把字符串中出现../当已逃出基目录。

沿实际写入API与最终绝对存储位置核对边界，再判断Web/静态服务/CDN如何映射和分配权限。上传成功不等于写入Web根目录，CDN URL也可能只映射专门对象存储；根URL看不到文件不证明内部写入安全。以已获准源码和隔离合成文件确认允许目录、拒绝越界及公开/私有交付，避免覆盖系统或他人文件。来源：[保存帖](https://x.com/i/status/1399746227286257669)。'''),
('by-type/idor-access-control.md','WordPress数据库准备与配置向导的状态','''旧帖把wp-admin拒绝但setup-config step1表单可见称创建数据库/P1。图只显示DB名、用户名、密码、localhost及表前缀输入。[WordPress安装说明](https://developer.wordpress.org/advanced-administration/before-install/howto-install/)将数据库/用户准备与wp-config.php写入分开，并说明配置向导收集数据库信息写配置（2026-10-10核读相关段落）。

把数据库已存在/权限、配置文件存在/写权限、已安装状态、具体入口校验、安装写表/管理身份和部署所有者分开；默认表单值不是现存有效凭据，入口可见不是任何一项写入完成。用获准源码/离线状态核对各阶段保护和正常未安装用途，再判断是否存在越权配置或再安装能力。不提交向导、覆盖配置或创建数据库来补旧帖结论，版本/主机状态未知保留。来源：[保存帖](https://x.com/i/status/1399809593262358528)。'''),
('targeted-fuzzing.md','批处理父进程、子任务与筛选后的覆盖','''Fuzzy示例分别使用while循环、xargs30、interlace20和200并发流水线，后续jq保留200/403。父任务数不等于每个子工具的请求数或全局并发；实际子配置、同一host汇聚、重试与递归共同决定预算。不同示例不能拼成一个已证乘数，尤其不能从先前另一版本截图继承子进程线程数。

静态核对wordlist.txt与wordlists.txt是否同一制品、真实argv/占位替换、输出命名和追加/去重历史；筛选前的拒绝、失败、其他状态和未完成任务均保留。有限自有合成清单可核对集合，不执行来源扫描/安装命令。200/403只是观察筛选，不是漏洞发现证明，也不能以过滤输出当全部完成。来源：[保存帖](https://x.com/i/status/1399969167436963846)。'''),
('by-type/cmd-injection-rce.md','provider普通JSON与CVE匹配的能力层次','''旧vCenter例展示getClusterCapabilityData的POST和多个false capability字段，另一图显示Nmap VULNERABLE/exploitable与6.5.7.0横幅。普通provider方法响应、插件暴露、产品版本匹配、输入到执行sink及目标进程结果是不同证据；方法可访问不等于任意命令执行。

把实际部署/组件/补丁、身份、方法输入和执行消费者绑定，检测器名称与CVE标签只作候选；原检测脚本未显示时不能代它证明命中条件。root@kali是本机提示符，不能算远端root。正常公开方法、已补丁实现、拒绝危险输入或只返回固定能力数据为反例。仅审提供请求/响应截图，不访问私网vCenter或运行Nmap，未由标题确认任何当前受影响版本。来源：[保存帖](https://x.com/i/status/1400023807327313923)。'''),
('reporting.md','补丁提交、请求复核与发布部署状态','''FireflyIII图片显示维护者提交commit并说should fix，请求在5.5.12发布前验证；NCSC邮件只确认收到并通知负责方。收到报告、开发者判断有效、提交补丁、验证原失败、发布版本和目标已部署是不同状态，奖金/有效标签不能补回归结果。

记录每个状态的来源、时间、制品/commit、原失败入口及谁执行了什么验证。只有提交时明确写待复核；发布存在时仍核对具体部署制品。已获准正常/失败样本和原消费者回归可解释修复是否覆盖共享路径，不为状态核对触发真实写入。PGP文本开头不等于签名已验证，收到确认也无修复时限保证。来源：[保存帖](https://x.com/i/status/1400436424890060800)。'''),
('discovery/records-and-incremental.md','XSSHunter配置、相关密钥与触发事件的来源','''四张旧XSSHunter图分别展示collected pages16、远程script/JavaScript URI候选、Injection Correlation API Key和additional JS链式加载设置、example.com/127.0.0.1触发页。页数是收集项数，通知数/事件数不等于独立漏洞；robots.txt路径中实际Example Domain HTML也不能按路径名认定文件内容。

按每次输入/保存/读者/渲染语境关联独立标记和事件，先排除自测与测试者页面。相关API key与master password用途不同，密钥仅以引用记录，不复制可见秘密。附加远程JS是新增信任/执行消费者，设置存在不证明已保存或触发；事件URL/IP不自动说明特权身份。用既有脱敏回执核对因果，不加载/运行远程脚本、旋转key、删除事件或改变设置。来源：[保存帖](https://x.com/i/status/1400570683671945218)。'''),
('discovery/records-and-incremental.md','Postman响应脚本的额外请求与随机采样','''旧JSONPlaceholder演示在Tests中读取原响应后，随机生成ID并用pm.sendRequest再发GET；213返回404/undefined、105返回200只是两个样本。[Postman说明](https://learning.postman.com/docs/tests-and-scripts/write-scripts/postman-sandbox-reference/pm-send-request/)允许在Pre-request/Post-response脚本异步发请求（2026-10-10核读）。点击一次或执行一个collection项不能按一个HTTP请求计预算。

统计主请求、脚本触发请求及回调/重试分别绑定配置、身份和结果；随机0至999允许重复，实际API对象范围未知时不称全量枚举。公开演示对象200不是IDOR，404及undefined也不证明对象存在或拒绝授权。改为有限自有合成对象集合与预期权限对照来解释计数/覆盖，本批不执行脚本或访问演示站。来源：[保存帖](https://x.com/i/status/1400715015779360770)。'''),
('by-type/idor-access-control.md','User-Agent客户端标签与服务端权限选择器','''旧帖建议将UA改为okhttp/4.1.1以绕过未认证403。该值是客户端可填写标签，不是平台、设备、账号或可信客户端身份证明；服务器若以此选择更宽权限应追到真实规则，而不是从不同状态码推通用绕过。

固定原始主体、Cookie/其他头、资源、方法、时点与缓存，比较同一受保护消费者的正常允许/拒绝及实际字段或能力。404或返回另一个公共响应没有补越权，合法移动端公开契约也可能解释差异。仅用获准日志/源码和合成身份核对选择器，不把UA命中当获取Android身份，也不向所有403端点发包。来源：[保存帖](https://x.com/i/status/1400828226642100225)。'''),
('targeted-fuzzing.md','Nuclei旧速查图的语法、响应序号与组合预算','''旧Template.yml图混有方法、BaseUrl样式、raw Content-Length、Origin、unsafe、request-condition、DSL多响应和clusterbomb/max999。模板名和示意文本不是已验证可执行模板，变量大小写与制品版本先核对。[当前HTTP文档](https://docs.projectdiscovery.io/templates/protocols/http/basic-http)说明变量区分大小写、重定向默认不跟随/可设上限，以及带_n的DSL属性按1起始请求序号取响应，condition可由序号属性自动启用；不能无条件照抄旧开关（2026-10-10核读相关段落）。

[unsafe文档](https://docs.projectdiscovery.io/templates/protocols/http/unsafe-http)将unsafe true绑定rawhttp请求控制；手填Origin不等于浏览器来源。[payload文档](https://docs.projectdiscovery.io/templates/protocols/http/http-payloads)描述clusterbomb尝试全部组合。预算先算各维有限集合乘积，再计多请求、重定向/重试及写动作；999不作为默认许可。DSL的404→200及secret_string匹配要绑定实际响应/身份/字段和正常反例，不能由matcher严重等级确认泄密。本批仅静态审图，不运行原模板、写PUT/DELETE或产生真实请求。来源：[保存帖](https://x.com/i/status/1400869630411948033)。'''),
('by-type/authn-session.md','登录锁定与既有会话失效的可用性契约','''旧帖把锁账号同时销毁sessions称永久DOS/P3。失败计数、锁定窗口/解锁、恢复渠道、凭据或会话代际变化及既有session的有效性应拆成状态迁移；暂时拒绝、自然到期、正常风险保护与不可恢复状态不同。

核对未经认证者能否对指定主体触发状态、重复触发是否延长窗口、合法用户是否可恢复，以及会话消费者是否按该主体/代际正确失效。用获准源码/隔离合成轨迹区分正常锁定保护、错误跨主体影响和持续阻断能力；没有持续条件与恢复证据不称永久。认证次数及锁定独立预算，不为确认阈值猜真实密码、锁真实账号或耗尽恢复渠道。来源：[保存帖](https://x.com/i/status/1401072585756975105)。'''),
('expert-reasoning.md','FAQ类别定义与实际越过的边界','''旧FAQ将IDOR描述为对象引用暴露，将RCE泛化整应用/服务器控制，将SSRF概括为内部资源读写。类别用于选消费者，不替代判据：对象引用可正常公开，需实际不应有的对象/动作能力；解释器执行须界定进程身份、隔离和权限；服务端取址需界定协议、网络可达性、方法和实际返回/状态变化。

XSS跟输入、输出语境、浏览器执行与读者身份，SQL注入跟外来数据如何改变查询语法与数据库作用域。通过“外来输入→真实消费者→违反契约的能力→正常/拒绝反例”检验类别，避免仅凭名称、200或界面字样计漏洞。FAQ展开内容已审，但搜索UI/导出按钮、热度和标签不证明全部索引或所有定义正确；未请求联系人或运行图中代码。来源：[保存帖](https://x.com/i/status/1401092401247047680)。'''),
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
