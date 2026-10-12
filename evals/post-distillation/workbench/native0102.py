"""Append manually reviewed batch 0102 mechanisms; never executes archive content."""
from pathlib import Path
from collections import defaultdict
import json,re
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
W=T/'evals/post-distillation/workbench'
facets=[
('by-type/xss.md','ASP.NET URL会话段与ResolveUrl属性输出','''旧图把ASP.NET cookieless会话段、ResolveUrl和生成script src连接起来。[System.Web会话文档](https://learn.microsoft.com/en-us/dotnet/api/system.web.sessionstate.httpsessionstate.iscookieless?view=netframework-4.8.1)说明会话ID可嵌入应用名之后的URL路径；嵌入路径并不独立证明引号逃逸或脚本执行。原图的版本范围只是原帖声明，不能推广所有.NET或Core。

绑定实际框架/会话配置、原始请求路径、URL生成调用、输出原始字节和浏览器属性解析，分开会话识别、链接重写、属性转义及最终读者能力。净化、固定会话格式、无该消费者与纯文本均为反例；本批仅审图和文档，没有运行载荷或启动服务。来源：[保存帖](https://x.com/i/status/1405285718386114562)。'''),
('by-type/authn-session.md','代理路径前缀与后端cookieless路由的保护对象','''同图对/admin与带会话段的路径显示403和200，只能提出代理前缀与后端路由解释不同的候选。200可能是公开fallback、登录页或不同处理器，不能直接计管理员权限绕过。

把原始路径、每层规范化/路由、代理保护规则、后端对象、会话身份和真正敏感动作绑定到同一次轨迹；验证对象授权是否在实际处理器仍执行。会话段的URL嵌入和XSS输出另列机制，不能由某个状态差把两条链互证。未向实例变异路径或访问管理员对象。来源：[保存帖](https://x.com/i/status/1405285718386114562)。'''),
('discovery/passive-and-services.md','回环DNS回答、页面控制与受害本机消费者','''旧纠错帖的127.0.0.1域名与自建localhost页面，只显示作者能控制自己机器上的服务；受害浏览器解析回环地址则指向受害机器。一个DNS回答本身不构成漏洞，也不能据此排除另有本地服务跨边界问题。

分开域名控制、浏览器origin、真正本机监听者、认证/来源校验及谁读到什么能力；自己的echo/本地PHP页和弹窗不替代受害消费者。须有获准既有配置或隔离合成轨迹证明信任跨越，本批没有起服务、触达本机接口或发DNS查询。来源：[保存帖](https://x.com/i/status/1405463614841106433)。'''),
('discovery/records-and-incremental.md','内存制品profile与进程字段的解释边界','''Volatility GUI图显示内存文件、Win7SP1x64 profile和pslist进程行，证明的是一次界面解析观察，不能据进程名称认注入、PPL读取或实时存活。

绑定获准制品的来源/采集时点/哈希、内核与架构、解析器及profile，再区分原始页、解析字段、模型推断和运行时证据。错误profile、截断采集、重复PID及陈旧残留是反例；解析缺项不得记对象不存在。本批没有读取真实内存、运行分析器、结束进程或加载驱动。来源：[保存帖](https://x.com/i/status/1405514636800233483)。'''),
('source-audit.md','CPG建模覆盖与finding到实际消费者的路径','''Joern help.cpg把AST、控制流等组合成可扩展图，并展示cpg.method.l和finding.l。图节点/潜在finding是模型产物，不证明完整源码覆盖、路径可达或可控输入进入实际运行消费者。

保存制品版本/哈希、语言前端、解析失败和未建模文件，沿实际数据流/调用条件/权限核对读写边；跨过程、动态分派、生成代码和运行配置不能由一个列表补齐。正常可信输入、不可达分支、有效净化或无权限作为反例；本批仅读帮助图，没有执行源项目或图查询。来源：[保存帖](https://x.com/i/status/1405877064427786243)。'''),
('by-type/authn-session.md','可选邮箱值、频控键与挑战主体的绑定','''旧帖说忘记密码流程修改可选email会reset频控。可控值变化可能选择新计数键而非清零原键；仍须区分原始字符串、规范化收件地址、账号、挑战/会话与最终重置主体。

在获准合成或既有脱敏记录固定同一主体/窗口/挑战与正常业务判据，核对计数键由谁写、何时检查、是否在最终动作再绑定。数字枚举、200或错误文字变化不证明无限尝试或认证通过；本批没有发送重置邮件、验证码尝试或运行Intruder。来源：[保存帖](https://x.com/i/status/1405881664195031042)。'''),
('by-type/info-secrets.md','source map嵌入源码子集与重建分母','''可读source map不保证整个项目源码。[ECMA-426](https://tc39.es/ecma426/)规定sourcesContent可选且项可为null，sources与sourceRoot还涉及来源URL解析。找到.map、看到文件名、取得嵌入文本与恢复完整构建输入是不同层。

记录地图哈希/构建身份、每项来源名/嵌入状态、URL基准和未保存外部内容，分别计数已读源码、仅名称、缺失/不可解析。嵌入文本也可能旧版、生成内容或第三方库；字符串不证明当前秘密有效。未保存外链按用户覆盖口径处理，同时保留重建限制；没有自动抓取源码、运行构建或使用密钥。来源：[保存帖](https://x.com/i/status/1405890883686309893)。'''),
('by-type/xxe.md','XML签名验证对象、转换链与业务消费对象','''XML导图并列SOAP重放/参数、XPath、实体/DTD/XInclude、签名包装、XSLT及资源耗尽，并注明未必均可利用。按真实消费者拆分：解析器取外部资源、签名验证哪个节点、转换读取/产生什么、业务最终使用哪个对象，不能把所有分支称XXE或RCE。

固定解析/转换版本与配置、外部URI策略、签名引用与验证结果、实际消费节点和资源上限；签名通过不独立证明业务消费的是同一被签对象。无外部解析、固定引用、禁止变换或有限资源为反例。图中攻击名/CVE只是候选入口，本批没有构造XML、读取文件或触达网络。来源：[保存帖](https://x.com/i/status/1405954795421069314)。'''),
('by-type/xss.md','Grafana快照originalUrl从保存到按钮读者','''图中POST /api/snapshots把originalUrl设为JavaScript URL，200返回快照字段，另一图有Open original dashboard按钮和弹窗；创建、持久保存、其他读者读取及实际点击仍需各自关联，不能由两图补跨用户链或全部匿名权限。响应中的删除/访问键不复制。

[维护者PR23254](https://github.com/grafana/grafana/pull/23254)明确快照originalUrl在渲染链接前净化，并列6.7.2里程碑。绑定实际版本/代码、创建者和读者、保存值/渲染值、URL协议策略与真实交互；API返回成功不等于执行。同字段后来的URL欺骗公告不可替代这次XSS根因。本批未创建快照或执行链接。来源：[保存帖](https://x.com/i/status/1406086490648502279)。'''),
('by-type/subdomain-takeover.md','SERVFAIL与REFUSED到遗弃委派的证据距离','''旧图把SERVFAIL/REFUSED及DNS provider清单当接管候选。递归错误可能源于策略、网络、DNSSEC或上游故障，并不独立证明权威委派遗弃、租户资源可分配或攻击者能控制合法域名。

保存已有记录的查询名/类型、解析器、RCODE、时点及权威链，分开临时失败、有效NS归属、服务租户状态与正式允许的认领验证。列表标签和工具“准确”宣传不替当前提供商条件；本批没有枚举、注册域名或申请第三方资源。来源：[保存帖](https://x.com/i/status/1406213934663847937)。'''),
('by-type/xss.md','dangerouslySetInnerHTML命中与外来HTML消费','''搜索dangerouslySetInnerHTML找到的是潜在HTML消费者。[React文档](https://react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html)描述raw HTML/TrustedHTML进入DOM innerHTML；API存在并不证明外来输入、净化失效或可执行浏览器上下文。

沿实际数据源、转换/净化、可信策略、渲染分支和读者身份追踪，保留普通文本输出、可信常量、有效过滤及不被访问的分支作为反例。TrustedHTML类型也需核对实际产生策略，不能仅靠类型名认安全或漏洞。未运行前端代码、提交字段或执行脚本。来源：[保存帖](https://x.com/i/status/1406249885838544901)。'''),
('by-type/ssrf.md','URL下载字节上限与失败清理的权威状态','''旧帖提出50GB下载到约15GB中断且chunk留存，仍缺测量/对象归属，不能从下载功能直接确认SSRF或整机DoS。目的地授权与本地资源生命周期是两个检查面。

核对任务/用户、响应宣称长度与实际流入字节、预分配/流式硬上限、超时/取消、临时对象与配额，逐个观察成功/失败/取消后的权威留存状态。任务失败不证明清理失败，文件存在也可能属正常缓存/其他任务；用有限合成制品和既有日志比较正常清理反例。本批没有下载大文件或耗尽资源。来源：[保存帖](https://x.com/i/status/1406282662843613186)。'''),
('discovery/records-and-incremental.md','多源管线的覆盖写入与实际下游集合','''两张脚本图把发现/解析/HTTP/历史URL/kxss串接。第一张domain_$1与domains_$1等文件名及追加集合不一致；第二张riddler阶段使用单个大于号会覆盖早先追加结果，最后sort去重不能恢复丢失来源。帮助文字用URL作domain输入也需实际argv核对。

按每段输入哈希/行数、退出状态、stdout/stderr、输出路径和覆盖/追加语义记录，区分保存集合与真正被下游读的集合；固定临时路径、未引用变量/非锚定grep和图中可疑缺管道语法均不能静默修复。kxss候选与浏览器执行另证，httprobe也不是纯离线步骤。本批没有执行管线、SQL查询、采集或端口探测。来源：[管线帖](https://x.com/i/status/1406325565104308226)、[多源脚本帖](https://x.com/i/status/1406349724324671492)。'''),
('by-type/idor-access-control.md','用户管理能力与可授角色上限','''User Access读写主体升级admin的描述需拆为允许管理谁、可授什么角色、是否允许自升，以及最终服务端能力。正常用户管理员改普通用户与越过角色上限是不同业务规则，UI可编辑字段不自动证明提权。

从权威RBAC/租户策略建立操作者、对象、旧新角色、委派上限和最终权限矩阵，再绑定服务端写入与后续读者/会话生效。合法委派、请求被拒/回滚、UI假成功或缓存旧角色作反例；本批没有更新用户或取得管理员权限。来源：[保存帖](https://x.com/i/status/1406335865677402120)。'''),
('source-audit.md','内核回调检测链中的PID代际与事件丢失','''FalconEye架构图从内核回调到PID map、hook处理、行为历史及有状态/无状态检测。节点箭头表达设计，不能补回调真实到达、所有进程覆盖或无漏报结论。

核对获准已有事件的进程创建代际、PID复用、时间/顺序、采集失败和存储关联，再区分观测行为、规则命中与恶意判定。合法行为基线、丢事件、晚到与重启均须有独立状态，不能以未告警计安全。本批未加载驱动、注入进程或部署监控。来源：[保存帖](https://x.com/i/status/1406375282295070724)。'''),
('by-type/ssrf.md','方括号重解析声明与URL验证器和连接器差异','''旧node-fetch帖把无协议的方括号字符串写成另一host/path形式，未保存版本或执行轨迹。[Node URL文档](https://nodejs.org/api/url.html)警告legacy url.parse宽松且非标准，并建议WHATWG URL；这不等于确认原例在当前node-fetch必然转换或绕过。

分别保留验证器、实际连接器及跳转处理的版本/输入字节/解析结果，比较scheme、authority、host、port、path与实际解析目的地。解析差只是候选，还需不应访问的目的地和同一请求链；拒绝、同解析或无出网为反例。本批没有执行源JavaScript或发网络请求。来源：[保存帖](https://x.com/i/status/1406634912162123785)。'''),
('by-type/xss.md','Django技术500模板的局部转义与异常前提','''create_user示例路径不是Django通用端点。[Django1.11.5发布说明](https://docs.djangoproject.com/en/5.2/releases/1.11.5/)将CVE-2017-12794绑定到技术500调试模板局部未转义，并要求DEBUG=True；不同于CSRF拒绝页仅显示“更多信息在DEBUG=True”的字符串。

绑定真实版本/调试配置、自定义路由、异常来源、输入如何到错误模板及浏览器读者，不能由路径名或含脚本的查询认当前漏洞。无异常、DEBUG关闭、已修复模板/自定义转义和纯文本为反例。本批没有创建用户、触发服务异常或执行载荷。来源：[保存帖](https://x.com/i/status/1406779605055270914)。'''),
('by-type/lfi-path-traversal.md','设备多斜线路径、固件身份与文件输出解释','''HG659旧图含多斜线/点段路径、curl -k与passwd样式文本。原始路径到真实处理器/文件的变换、设备/固件身份和请求权限仍须分别证明；关闭证书验证还削弱远端身份依据。

从获准已有轨迹保留字节、每层规范化、处理器/固件版本、源文件与输出关联，并比较正常授权路径和拒绝对照。账号样式行不自动是可用密码，系统文件读取也不等于OS命令执行。图中账户行不复制，本批没有执行curl或读取设备文件。来源：[保存帖](https://x.com/i/status/1406782172443287559)。'''),
('discovery/records-and-incremental.md','RDP缓存拼图的缺片、时点与重组推断','''RDP Cache Stitcher图有缺片网格、隐藏已用重复块与自动排列。视觉上合理的拼图可能混合多个时点/会话，不能作为完整单帧屏幕或某个用户动作的直接证据。

绑定获准缓存制品哈希/采集来源、原始块、坐标与可知时间/会话，分开原始观察和算法/人工排列推断；未知缺片、重复、遮盖和无法定位的时点保留为限制。拼出界面不证明点击、认证或服务器状态。本批没有恢复真实缓存或连接RDP。来源：[保存帖](https://x.com/i/status/1406964185204932618)。'''),
('by-type/xss.md','左尖括号后的空格与真实HTML状态机','''旧列表的空格片段`< svg`不能在HTML Data到tag-open语境中直接成为svg起始标记。[WHATWG解析规则](https://html.spec.whatwg.org/multipage/parsing.html#tag-open-state)在此对非字母等分支报错并输出左尖括号，再回Data消费字符；只有真实前置变换或不同语境才可能改变结论。

保留原始字节、解码/过滤每层与浏览器当前状态，不替作者去空格再认原载荷有效。列表其他属性/JS片段各有适用语境，这一个反例既不证全部无效，也不补Cloudflare通用绕过。未运行HTML或脚本。来源：[原列表](https://x.com/i/status/1406997161875673090)、[同文帖](https://x.com/i/status/1407170521368719364)、[纠错帖](https://x.com/i/status/1407289453962579974)。'''),
('by-type/oauth-oidc.md','acr_values请求偏好与实际认证保证','''OIDC图仅有authorize请求的acr_values=otp+password和state。[OIDC Core](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)把acr_values定义为可选、空格分隔的认证上下文偏好，并将对应acr作为Voluntary Claim；请求文字不是已完成OTP/密码或强制二因素的认证结果。

分别绑定RP策略、OP执行的认证流程、实际返回且验证过的身份令牌/上下文，以及最终动作所要求的保证；不能由客户端改请求参数或一张请求图认绕过/安全。缺失/不满足的上下文与普通低保证流程须按权威策略处理，本批没有授权登录或发送OAuth请求。来源：[保存帖](https://x.com/i/status/1407184853255155717)。'''),
('by-type/mobile-android.md','Flutter kernel制品与strings输出的源码分母','''图展示assets/flutter_assets/kernel_blob.bin与strings输出文件output.dart；扩展名并不把可打印字符串重建成完整Dart源码，像素模糊的代码行也不能恢复秘密。[Flutter构建模式](https://docs.flutter.dev/testing/build-modes)区分调试与优化/去调试信息的发布模式，但不能由文件名断言所有制品模式或格式。

绑定获准包哈希/签名/版本、构建模式、架构与实际格式，区分结构解析、字符串片段、生成代码和完整源码集合；发现键名/地址还需真实消费者及当前能力。没有运行strings、反编译、下载应用或调用秘密。来源：[保存帖](https://x.com/i/status/1407266795916972034)。'''),
('by-type/info-secrets.md','Jira自定义字段名披露与dark feature的响应判据','''旧帖QueryComponent!Default.jspa的CVE-2020-14179与Renderer用户枚举不同。[Atlassian71536](https://jira.atlassian.com/browse/JRASERVER-71536)限定自定义字段/SLA名称，列受影响低于8.5.8以及8.6至8.11.1之前；还明确修复不能完全消除此路径，需额外配置，不是只升级即可保证。

核对实际版本、匿名权限和dark feature：public.access.disabled会让匿名请求401，anonymousPreventCfData相关控制可返回200但过滤字段。不能只以状态码认仍泄露，也不把字段名升级为字段值/用户账号/全数据。旧版重写的认证兼容限制另记；本批未访问实例、改配置或重启服务。来源：[保存帖](https://x.com/i/status/1407280181186760707)。'''),
('by-type/subdomain-takeover.md','共享IP未知站点与域名虚拟主机路由','''三图分别为历史A/NS回答、直接IP的Pantheon Unknown site及正确域名的正常HTTPS页面。直接共享IP缺Host/SNI而无租户路由，与域名指向可认领遗弃资源不同；截图没有可接管证据。

保存已有解析/请求的时点、真实hostname、Host/SNI、服务路由及租户归属，分开共享前端、错误页和合法域名的实际响应。IP上的404不能把同IP所有域名扩成范围或接管；正常域名页面也是重要反例。本批没有认领资源、加入Discord或发送协作消息。来源：[保存帖](https://x.com/i/status/1407293388014108677)。'''),
('experiment-design.md','名为unit tests的安全工具与实际状态副作用','''Swift-Attack帮助虽称unit tests，却包含系统/剪贴板/历史/文件采集、网络及模拟动作。测试名称不证明无副作用、隔离或检测有效，工具帮助也不证明各项已实施。

每项先界定自己获准隔离制品、真实调用/权限、网络目的地、修改/留存状态、清理边与前后日志，再用合成正负例约定检测/未知判据。文件采集、会话动作或持久设置不能当普通纯函数测试；本批没有部署工具、获取凭据、执行系统动作或向外传输数据。来源：[保存帖](https://x.com/i/status/1407326584516841472)。'''),
('discovery/passive-and-services.md','前导零DNS标签与有限枚举的实际名称集合','''图用两个1至10循环分别拼disk和disk0，后者会包含disk010，并不等于固定两位十进制格式；disk7与disk07是两个DNS标签，不能先转整数合并。单条回答和其他沉默行也不是全部名称已查询/不存在的证据。

保存精确生成规则、有限名称集合/哈希、每个类型/解析器/时点和实际尝试/失败分母，分别处理通配、陈旧回答、未查询与授权归属。格式扩展增加候选，不证明新名称在范围内；本批仅审图，没有执行循环或DNS查询。来源：[保存帖](https://x.com/i/status/1407341138533654534)。'''),
]
batch=json.loads((W/'batch-0102.json').read_text())
ids={pid for row in batch for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
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
