"""Append manually distilled0112 facets after precheck. Own helper only."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "by-type/authn-session.md",
    "控制台弹窗、designMode 与本机 hosts 的作用域",
    "保存帖把控制台直接调用 alert、开启 designMode 和编辑本机 hosts 当作玩笑演示。\n\n区分研究者本机操作与来自攻击者的输入：记录谁能设置值、谁执行、是否进入其他用户会话及服务端持久状态。仅本机可编辑页面、改解析或运行代码，不能证明远程 XSS、权限提升或目标 DNS 被控制。\n\n来源：[保存帖1](https://x.com/i/status/1446477382907359232)、[保存帖2](https://x.com/i/status/1450027324343308329)、[保存帖3](https://x.com/i/status/1451636107033075712)。"
  ],
  [
    "scope-and-rules.md",
    "历史宽泛范围名单与西班牙语项目规则",
    "阿拉伯语帖列所谓宽范围公司，私有项目 dork 帖只给发现方式；西班牙语直播图展示 Ford 当时的参与规则与响应期。\n\n公司名称、搜索结果、域名归属和旧直播规则是范围线索。具体研究需以当时适用的资产、动作、数据、账号与预算授权为依据；历史资格、生产环境说明、无 VPN 条款和奖励定义均不能自动转成当前授权。\n\n来源：[保存帖1](https://x.com/i/status/1446513173541134359)、[保存帖2](https://x.com/i/status/1446777493743026176)、[保存帖3](https://x.com/i/status/1447690185400012802)、[保存帖4](https://x.com/i/status/1448136525166759938)、[保存帖5](https://x.com/i/status/1449438807472984065)、[保存帖6](https://x.com/i/status/1450873422964088838)。"
  ],
  [
    "by-type/waf-bypass.md",
    "Imperva、Incapsula 与 Cloudflare 载荷的多层解释",
    "保存文本含 javascript URL 空白、事件名实体、Unicode 标识符与 SVG 变体；一张论坛图显示地址含混合 SVG/onload 形态及值为 1 的确认框，其他卡片没有执行回执。\n\n拆开原始字节、代理解码、规则匹配、HTML 解析、事件处理和浏览器执行。确认框至多支持截图中一次浏览器执行观察，不能证明当前 WAF 普遍失效、所有浏览器兼容、零日或 cookie 外传；静态卡片还须保留其未执行边界。仅用无敏感值标记和明确消费者对照。\n\n来源：[保存帖1](https://x.com/i/status/1446579494505091073)、[保存帖2](https://x.com/i/status/1448030029435310080)、[保存帖3](https://x.com/i/status/1449852536480010247)、[保存帖4](https://x.com/i/status/1450592148412411910)、[保存帖5](https://x.com/i/status/1451457844948226059)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "JWT 认证 URL 与 returnto 的重定向链证据",
    "保存 JWT 接管文章的图片只显示含认证值及 returnto 的 GET 和返回同一认证地址的 302。\n\n分别识别 JWT 的用途、接收方和认证状态，记录每跳 Location、最终 origin、允许列表与 URL 解析。返回同一地址并未证明外部跳转、令牌泄露或接管；先区分站内相对地址、错误重试和真正跨信任边界的认证值转发，不保存原始 JWT/cookie。\n\n来源：[保存帖1](https://x.com/i/status/1446745869378744329)。"
  ],
  [
    "by-type/ssti.md",
    "tplmap 的 oscmd 回连与 non-intrusive 标签纠正",
    "图片把带 oscmd 的 tplmap 回连演示标成 non-intrusive。\n\n调用系统命令与向外部地址发送请求属于有副作用动作。模板计算、引擎识别、服务端抓取和系统进程执行应分开证明；回连可能来自浏览器、SSRF 或其他消费端，不能单独判为 SSTI 到 RCE。离线审计调用路径与参数来源，授权验证限自有环境及无害标记。\n\n来源：[保存帖1](https://x.com/i/status/1446802633604444181)。"
  ],
  [
    "by-type/authn-session.md",
    "证书域名不匹配与客户端是否接受错误证书",
    "图片可见 Firefox 拒绝域名不匹配证书，另有一条历史 Medium/Resolved 记录。\n\n核对实际客户端、连接域名、SNI、SAN、证书链及错误处理。浏览器拦截支持证书异常观察，不证明应用接受错误证书或已发生 MITM；若研究移动端/API 客户端，应保留其实际握手及拒绝/接受对照。历史报告状态不替代客户端证据。\n\n来源：[保存帖1](https://x.com/i/status/1446825682173001742)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "500GB RECON 统计与真实资产覆盖",
    "配图是 Windows 网络使用量，九天约 554GB、其中 OpenVPN 约 474GB。\n\n网络流量按接口、进程与时间窗计量，另记录去重资产、请求、有效响应和人工审查数。VPN 总流量可能包含下载或重复传输，不能换算为发现资产或漏洞；保存分母、重试与计量来源，避免用流量总额宣称全量侦察。\n\n来源：[保存帖1](https://x.com/i/status/1446926363177390080)。"
  ],
  [
    "by-type/authn-session.md",
    "账号锁定是否撤销既有会话与恢复窗口",
    "截图描述失败登录锁定会结束受害者所有活动会话，并称永久 DoS。\n\n在自有账号上区分登录入口暂时拒绝、服务端撤销既有令牌、客户端登出及正常过期。记录锁定键、失败窗口、TTL、解锁与恢复方式、会话创建时间和错误状态；缺少恢复窗口不能称永久。随机长字符串与短暂卡顿也不自动证明稳定可用性影响。\n\n来源：[保存帖1](https://x.com/i/status/1446927311161331712)、[保存帖2](https://x.com/i/status/1449150295821492227)、[保存帖3](https://x.com/i/status/1449382979185217541)。"
  ],
  [
    "discovery/passive-and-services.md",
    "BIG-IP 重定向搜索结果与管理接口可达性",
    "Shodan 图按 BIG-IP 重定向标题展示约一万条结果，文字称 CVE-2021-22986。\n\n标题、默认证书与 200 页面仅是产品候选指纹。还需目标范围、具体管理接口、版本、部署边界、认证状态及受影响配置，不能把搜索结果数当作全部可利用实例或未授权 RCE；此保存帖没有实际管理接口对照。\n\n来源：[保存帖1](https://x.com/i/status/1447036513162653698)。"
  ],
  [
    "discovery/web-and-api.md",
    "WordPress 文件清单与 AEM servlet 路由审计",
    "WordPress 帖列管理、配置、包含目录等十二个候选路径，AEM 帖建议寻找其他 servlet。\n\n从已获准的应用路由和配置还原 handler、角色、对象、字段与动作，再比较同一资源在页面、API、导出或 servlet 中的权限。路径存在、备用入口或内部文件名不等于敏感泄露或执行；返回统一页、禁止直读、无敏感值是反例。\n\n来源：[保存帖1](https://x.com/i/status/1447083546921762821)、[保存帖2](https://x.com/i/status/1449127483442286595)。"
  ],
  [
    "by-type/info-secrets.md",
    "Notebook、源码和 URL 中的凭据候选",
    "保存帖给 ipynb 密码搜索方向、源码查找建议，以及 URL 路径含用户名密码的自述；奖励图未展示可验证值。\n\nNotebook 的代码、输出及历史快照均可能保留敏感值；URL 还可能进入日志、历史与引用链。只记录位置、用途、脱敏摘要、归属与公开/示例/过期反例。发现字符串不证明有效凭据，奖励邮件也不证明泄露等级；不复制或使用第三方密码、令牌。\n\n来源：[保存帖1](https://x.com/i/status/1447101455878397956)、[保存帖2](https://x.com/i/status/1447506162048405512)、[保存帖3](https://x.com/i/status/1449040203394473984)、[保存帖4](https://x.com/i/status/1450466178007289872)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "命令注入流水线、Commix 输出与回连截图",
    "一帖串联子域、URL、替换参数与 ffuf；另一图有 Commix 数学探针和 www-data 字样；过滤绕过帖附反向连接截图但未显示进程身份。\n\n保持原始输入、实际参数、编码层、服务端执行点和输出对应关系。单独 uid 文本、扫描结束、外连建立或拼接脚本都可能缺失因果证据；需负例与同一执行端的无害输出对照。截图旧 Python 警告不能作为当前运行建议；不执行保存命令、监听器或扫描链。\n\n来源：[保存帖1](https://x.com/i/status/1447158357547233282)、[保存帖2](https://x.com/i/status/1450511544371060743)、[保存帖3](https://x.com/i/status/1451443062790631462)。"
  ],
  [
    "by-type/xss.md",
    "Nexploit 的 HTMLi 分类与实际 HTML 消费者",
    "图显示 WAVSEP JSP 输入、HTML 标记示例和 127 LFI、20 SQLi、55 HTMLi 等工具数量。\n\n从原始输入到响应上下文、实际 DOM 节点及用户动作逐层确认。HTML 注入可改变链接、表单或页面内容，仍需真实消费端及影响；它不自动等于 JavaScript 执行、WAF 绕过或 RCE。分类数字与工具页面不等于独立已确认漏洞数量。\n\n来源：[保存帖1](https://x.com/i/status/1447171751838953477)。"
  ],
  [
    "source-audit.md",
    "Qu1cksc0pe 静态分析帮助与外部样本上传边界",
    "帮助图列文件、目录、语言、元数据、域名与 VirusTotal 等选项，没有给出样本分析结果。\n\n记录分析文件哈希、版本、解析器、具体命中位置与输出语义，区分帮助、检测签名和真实结论。字符串或恶意标签需上下文与误报对照；外部 API 查询/上传另有数据外发边界，不能依据工具支持而上传私有样本或执行可疑文件。\n\n来源：[保存帖1](https://x.com/i/status/1447173593583046656)。"
  ],
  [
    "by-type/file-upload.md",
    "扩展名、null 与分号变体必须绑定实际文件处理器",
    "保存帖和卡片枚举 PHP/ASP 变体、大小写、null 与分号，阿拉伯语帖把 shell 改为 jpg；另帖泛称未验证上传。\n\n区分名称校验、磁盘名称、平台解析、路由映射、内容识别和最终执行端。扩展名列表、可上传或可访问只支持输入/存储观察；处理器未映射、静态下载、隔离域、版本不支持 null 等是反例。不能由缺少校验直接推出任意代码执行。\n\n来源：[保存帖1](https://x.com/i/status/1447411130264010756)、[保存帖2](https://x.com/i/status/1451494186948104215)、[保存帖3](https://x.com/i/status/1451514923893202950)。"
  ],
  [
    "by-type/idor-access-control.md",
    "json、空 ID 与编码点路径的资源一致性",
    "图片显示相似 GET 的 403 与加 json 后 200；其他帖删对象 ID、改变斜杠、空白或编码点，一张报告图给 util 与编码点前缀的候选管理页面。\n\n固定自有主体、方法、对象与动作，记录原始 request-target、代理归一化、路由、权限决策及最终字段/状态。200 可能是集合入口、公共配置、错误页或不同资源；必须确认同一受保护对象与非所有者可见的敏感值/动作。编码路径中的管理功能名称也不能单凭名字判泄露。\n\n来源：[保存帖1](https://x.com/i/status/1447425088345804800)、[保存帖2](https://x.com/i/status/1448342739444174865)、[保存帖3](https://x.com/i/status/1449617495019634689)、[保存帖4](https://x.com/i/status/1451117857694224385)。"
  ],
  [
    "by-type/csrf.md",
    "CSRF 参数替换与浏览器投递条件",
    "阿拉伯语帖依次建议删除参数、空值、随机长度、其他账号令牌及变更方法；初学文章仅保存标题。\n\n用自有账号验证服务端是否忽略令牌、校验结构或绑定主体/动作，另记录浏览器可发送的方法、编码、cookie、Origin/Referer 与 SameSite。重放器成功或删字段成功不证明跨站投递；必须有实际无害状态改变，缺少登录上下文、方法不可投递或额外挑战均是反例。\n\n来源：[保存帖1](https://x.com/i/status/1447428530065784834)、[保存帖2](https://x.com/i/status/1449555451742466049)。"
  ],
  [
    "by-type/mobile-android.md",
    "Twitter intent 启动输出与崩溃因果",
    "adb 图含 retweet intent 的启动行和较早的解析异常，没有可绑定的应用崩溃栈。\n\n区分 intent 被调度、URI 解析失败、应用 handler 异常与可由其他应用/链接触发的稳定崩溃。记录包/版本、导出边界、冷暖启动、异常进程、时间与无害对照；启动命令及截断 stackTrace 不能直接判 Android RCE 或远程 DoS。\n\n来源：[保存帖1](https://x.com/i/status/1447474740398997510)。"
  ],
  [
    "by-type/csrf.md",
    "Exporter、LazyCSRF 与表单方法覆盖的等价性",
    "Exporter 图提供 clipboard、文件及 XHR/表单生成；LazyCSRF 图把 JSON PUT 请求改成 POST 加隐藏方法字段，并和 Burp 表单比较。\n\n生成文本不证明真实浏览器行为。比较线上请求的 URL、序列化、Content-Type、cookie、Origin、令牌及方法覆盖是否被后端识别；HTML 表单不能任意等价 JSON PUT，隐藏字段也可能无效。保存最终无害状态变化和未覆盖对照，脱敏导出且不执行档案 PoC。\n\n来源：[保存帖1](https://x.com/i/status/1447738688327221251)、[保存帖2](https://x.com/i/status/1447939497413562372)、[保存帖3](https://x.com/i/status/1450571000442195972)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "CDN 原站 IP 候选与直接访问后的权限",
    "保存外链标题称发现原站 IP 可绕过 Cloudflare 并导致 DDoS，图只是 CDN 架构。\n\nIP、DNS 历史或架构只是候选来源；若获准研究，比较正确 SNI/Host 的服务、应用身份验证、原站策略与实际受保护资源。发现地址不证明可直连或访问控制失效，更不证明可用性影响；此档案没有实际原站请求，不开展流量压力测试。\n\n来源：[保存帖1](https://x.com/i/status/1447851450982277122)。"
  ],
  [
    "by-type/authn-session.md",
    "Spring trace 中的 cookie 泄露与 fixation 的区别",
    "保存文本把 trace 记录中的共享父域 cookie 描述为一次点击会话固定，没有保存请求或图片细节。\n\n先确定 trace 访问权限、历史/当前 cookie、Domain/Path/安全属性及对应会话用途。会话固定还要求攻击者能预置已知会话、受害者登录后仍沿用且攻击者可继续使用；拿到已存在会话属于不同机制，父域共享也不自动证明有效。只保存脱敏记录，不使用记录中的会话。\n\n来源：[保存帖1](https://x.com/i/status/1448208604658610181)。"
  ],
  [
    "by-type/authn-session.md",
    "改邮箱后的旧重置链接与对象 ID 绑定",
    "文本描述旧重置链接、登录改邮箱和再次重置；另一图仅有带账号 ID 的密码 POST 和空 Location 的 302。\n\n用自有两账号区分令牌主体、当前邮箱所有权、TTL、一次使用、失效事件、挑战与最终密码状态。本人旧链接可重置本账号不自动构成接管；302 或表单中可改 ID 也不是他人密码已经改变。旧所有者继续拥有有效恢复能力才是需要进一步验证的边界。\n\n来源：[保存帖1](https://x.com/i/status/1448234404791218177)、[保存帖2](https://x.com/i/status/1450297618072948739)。"
  ],
  [
    "reporting.md",
    "厂商复现、未来 CVE 与重复报告的不同阶段",
    "Forti 邮件称已复现并会在修复发布时分配 CVE；其他图有标题 Critical/实际 Medium、滚动修复、不知赏金、重复拒奖及致谢。\n\n分别记录接收、复现、影响评级、已知/重复、修复部署、编号分配、资格和奖励。未来计划不等于已修复或所有实例受影响，标题不是最终评级，重复或无赏金也不消除技术问题；截图不含技术过程时不补写漏洞结论。\n\n来源：[保存帖1](https://x.com/i/status/1446850401618128904)、[保存帖2](https://x.com/i/status/1448247435952852992)、[保存帖3](https://x.com/i/status/1448271709367328775)、[保存帖4](https://x.com/i/status/1448302980474626054)、[保存帖5](https://x.com/i/status/1451049335634812928)、[保存帖6](https://x.com/i/status/1451096454290837505)。"
  ],
  [
    "discovery/web-and-api.md",
    "Piper 的 JWT 格式化与 SPA 端点候选",
    "正文介绍扩展名筛选、提取 SPA/API 路径和 JWT pretty 输出，图片只有仓库概览。\n\n保留响应来源、输入格式、解析器与实际引用位置。格式化 JWT 不证明签名、受众或授权有效，源码字符串不证明端点在线或允许任意方法；提取候选须回到实际应用消费者和获准路径，不把展示功能当成漏洞验证。\n\n来源：[保存帖1](https://x.com/i/status/1448302505700610051)。"
  ],
  [
    "hunting-strategy.md",
    "P4 批量自动化与单目标修复回归的分母",
    "保存帖称可自动化常见 P4 并扫描所有范围内项目，另帖建议对单目标反复找同功能变体。\n\n按当前获准项目、动作和预算建立候选、执行、去重、消费端核对与回归覆盖表。不同项目授权、请求量、认证与报告门槛需独立记录；工具跑完、低评级标签或一次修复不能证明全部功能覆盖或剩余变体无漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1448316299021459456)、[保存帖2](https://x.com/i/status/1448942867217518616)、[保存帖3](https://x.com/i/status/1449127481668083712)。"
  ],
  [
    "by-type/sql-injection.md",
    "PostgreSQL COPY 文件读取与 PROGRAM 执行权限",
    "图片只展示建表、从服务器文件导入及 SELECT 内容，正文把文件读取和命令执行并列。\n\n分开服务端 COPY 文件读写、PROGRAM 与客户端 copy；保存具体数据库版本、SQL 可达性、表权限及数据库进程的文件/执行权限。文件内容出现在表中不证明 PROGRAM 可执行，也不证明 SQLi 到系统 RCE。[PostgreSQL 13 官方说明](https://www.postgresql.org/docs/13/sql-copy.html)分别约束超级用户或相应服务器文件/执行角色。这里仅审查保存会话，不执行数据库语句。\n\n来源：[保存帖1](https://x.com/i/status/1448498378371833857)。"
  ],
  [
    "by-type/idor-access-control.md",
    "S3 时间戳音频名称与二进制内容证据",
    "Turbo Intruder 图展示约五十万请求和三个 200、不同长度的结果，正文声称其中两个是音频；所示响应没有足够的音频解析证据。\n\n预测名称、单个对象读权限与 bucket 列举权限分开判断。确认自有对象的格式、Content-Type/魔数、所有权和设计访问策略；200 文本、错误对象或公开资源均是反例。不能由响应数量推出敏感语音泄露，不枚举第三方时间窗或读取其音频。\n\n来源：[保存帖1](https://x.com/i/status/1448570102157389828)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Nuclei 代理与 Logger 历史的请求对应关系",
    "保存正文提议把 Nuclei 经代理送到 Burp Logger 并筛选。\n\n为获准输入建立扫描版本、配置、请求标识、认证状态、代理实际历史与匹配证据对应表；工具 match、代理可用、请求确实记录和人工确认是不同状态。未通过代理的请求、过滤隐藏、重试及历史旧数据应单独计数，展示日志不等于真实漏洞验证。\n\n来源：[保存帖1](https://x.com/i/status/1448575897452232704)。"
  ],
  [
    "discovery/passive-and-services.md",
    "IPv6 无目标响应与协议层证据",
    "Xmap 图展示网络拓扑、路由器 ICMPv6 不可达与未分配地址处理。\n\n保存探测对象、来源跳点、引用包与具体负响应语义。中间路由器不转发、策略丢弃或无回复不能统一推为目标存活/死亡；网络可达性也不证明应用权限或存在漏洞。TCP/IP 历史演变图只提供背景，不能替代目标请求。\n\n来源：[保存帖1](https://x.com/i/status/1448623134152794113)、[保存帖2](https://x.com/i/status/1450748258280775680)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "Apache 三版本载荷卡片与 2.4.51 修复反例",
    "卡片把编码遍历列入 2.4.49、2.4.50 及 2.4.51，另一个工具图只显示批量生成和连续 HTTP 400。\n\n按版本、Alias 映射、目录权限、归一化和 CGI 条件归档；卡片的 2.4.51 推广缺乏证据。[Apache 官方公告](https://httpd.apache.org/security/vulnerabilities_24.html)记载 41773 仅影响 2.4.49，42013 涉及 2.4.49/50 并历史修复于 2.4.51。400 批量错误与生成数量不证明路径外文件读取或代码执行；这也不是当前升级版本建议。\n\n来源：[保存帖1](https://x.com/i/status/1448031622012575751)、[保存帖2](https://x.com/i/status/1448642634239537158)、[保存帖3](https://x.com/i/status/1450885705912266762)。"
  ],
  [
    "by-type/idor-access-control.md",
    "低高权限 API 矩阵与替换自有账号 ID 的规则",
    "正文建议低权限对高权限端点，卡片指导账号 B 登录后把 URL/正文中的 B 的 ID 替换为自有账号 A。\n\n固定两个获准自有主体、对象、字段与动作，仅替换对象引用并保留调用者认证身份。全局替换可能误改 token、签名、租户或其他标识，从而使请求不可比；按规则范围记录原始及变更字段。确认 A/B 正常访问和 B 对 A 的预期拒绝，奖励截图不替代矩阵结果。\n\n来源：[保存帖1](https://x.com/i/status/1448708808356745224)、[保存帖2](https://x.com/i/status/1450728268647190532)。"
  ],
  [
    "by-type/authn-session.md",
    "OTP 的 400 到 201 与刷新令牌后续用途",
    "图展示六位候选循环、无效 400 后 201 及刷新令牌字段，正文只有测试自述。\n\n区分验证码提交、挑战匹配、重试限制、令牌签发和最终认证能力；固定自有挑战、TTL、账号/设备绑定、作废与挑战重建条件。201 字段不能单独证明完整接管，也不能推导普遍无次数限制；保存脱敏成功/失败语义，不生成或运行枚举循环。\n\n来源：[保存帖1](https://x.com/i/status/1448723839874060301)。"
  ],
  [
    "by-type/authn-session.md",
    "ADCS 正常证书签发与 Golden Certificate 条件",
    "图片展示客户端 CSR、CA、模板、Domain Users 与无需审批的正常签发配置。\n\n还原模板 ACL、EKU、Subject/SAN、签发审批、CA 信任及实际身份映射。正常用户获得允许用途的证书不证明 CA 私钥被控、任意身份认证或 Golden Certificate；这些需要不同权限与证据，不能由工具名称合并。\n\n来源：[保存帖1](https://x.com/i/status/1448774285049352199)。"
  ],
  [
    "by-type/sql-injection.md",
    "Blind SQL 标题与 UNION 版本回显的分类",
    "图片在训练页面 Email 处回显数据库版本，示例属于 UNION 返回值。\n\n按源参数、查询位置、列数/类型、可观察输出及数据库权限记录。可见 UNION 版本回显是带内证据；布尔/时间盲注需另外的可控响应及重复基线。训练站截图不证明真实目标漏洞，更不能由版本字符串推出系统命令执行。\n\n来源：[保存帖1](https://x.com/i/status/1448844254806097923)、[保存帖2](https://x.com/i/status/1449717791733403649)。"
  ],
  [
    "by-type/xxe.md",
    "text/plain 请求中的外部 DTD 与缺失实体定义",
    "请求图含 XML DOCTYPE、远端参数实体及 all/send 引用，没有完整 DTD、响应或回连。\n\n先验证实际服务端 XML 解析器、Content-Type 路由、DTD/外部实体开关及解析日志。DOCTYPE 文本不证明执行，获取 DTD 不等于本地文件读取；未定义实体、忽略 XML、请求未发送是反例。仅记录受控实体解析所需证据，不访问保存远端地址。\n\n来源：[保存帖1](https://x.com/i/status/1448875998808793094)。"
  ],
  [
    "by-type/info-secrets.md",
    "历史网页缓存的版本与私密性判断",
    "两幅图显示过去缓存时间及 MDM 管理页的 CSS/build 等源码引用。\n\n缓存时间、当时公开状态、来源权限、历史与当前构建应分别记录。路径、版本和静态资产标识不等于当前私密数据或可复用会话；旧快照不能证明管理入口仍在线。此项保存的是历史证据，不承诺当前缓存服务可用或恢复外链全文。\n\n来源：[保存帖1](https://x.com/i/status/1448878414094557196)、[保存帖2](https://x.com/i/status/1448917628337082369)。"
  ],
  [
    "by-type/ssrf.md",
    "CVE-2021-40438 的 mod_proxy 版本和消费端",
    "保存帖把 Apache 2.4.48 的 CVE-2021-40438 称为严重 SSRF，未给实际请求回执。\n\n[Apache 官方公告](https://httpd.apache.org/security/vulnerabilities_24.html)说明特制 URI 路径可能使 mod_proxy 转发到远端选择的 origin，历史范围是 2.4.48 及以前并在 2.4.49 修复。先确认模块、转发路径、解析及目标可达性，版本指纹或标题不能证明转发成功、读到内部信息或 RCE；避免把它混同 41773/42013 的遍历配置条件。\n\n来源：[保存帖1](https://x.com/i/status/1448984775306452994)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Shodan 登录指纹与默认凭据尝试的边界",
    "正文串联 SSL 搜索、登录页、公开仓库字符串与默认密码尝试，并自述成果。\n\n将候选归属、当前范围、真实认证系统、账号所有权、角色和结果分开记录。登录页与公开字符串不授权使用第三方凭据；相同用户名或默认密码假设不能代替有效性证据。归档只提炼来源关联与反例，不重放登录或把自述写成已验证接管。\n\n来源：[保存帖1](https://x.com/i/status/1449058767086096388)。"
  ],
  [
    "by-type/cors.md",
    "Burp Origin 替换、项目持久化与浏览器差异",
    "Match/Replace 图展示替换请求 Origin 并保存项目配置。\n\n明确规则匹配范围、开关和实际发送头，用正常/替换/关闭规则三份线报文保持主体与资源一致。研究者代理能伪造 Origin 不等于浏览器允许任意 Origin；CORS 影响还需具体读者、凭据策略和浏览器可读敏感响应，不能仅因代理响应变化判成立。\n\n来源：[保存帖1](https://x.com/i/status/1449339347002613765)。"
  ],
  [
    "by-type/xss.md",
    "资料脚本示意与 HTML 图片的实际读取链",
    "资料注入图把 document.cookie 字样拼进脚本 src 的示意，另一正文描述修改上传字节及 MIME 后访问文件页面。\n\n记录保存字段/文件、最终响应 Content-Type、Content-Disposition、来源域、CSP、真实 DOM 和触发交互。示意字符串不是外传回执，允许 text/html 也不证明被同源活跃文档读取；隔离域、下载响应或转码是反例。HttpOnly、脚本可读范围和受害者可达性决定影响，不读取他人 cookie。\n\n来源：[保存帖1](https://x.com/i/status/1449347705797373952)、[保存帖2](https://x.com/i/status/1449988709898592261)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "数据包嗅探中的 TLS 元数据与应用内容",
    "终端图有 TCP 443 和 UDP 53 的地址、端口与数据包信息。\n\n绑定获准接口、时间窗、进程/连接及去标识化范围。观察 TCP/UDP 元数据不等于获得 TLS 应用明文、用户请求或凭据；TCP 的可靠字节流也不能推广到所有 UDP 流量或业务成功。协议层、网络包与应用记录应分别核对，不捕获无授权第三方流量。\n\n来源：[保存帖1](https://x.com/i/status/1449347965265580032)、[保存帖2](https://x.com/i/status/1449978233294925827)。"
  ],
  [
    "by-type/graphql.md",
    "关闭 introspection 后的查询发现与 resolver 授权",
    "保存帖问 introspection 关闭后还能怎样发现接口，没有给实际查询。\n\n从获准客户端已使用的查询、fragment 和操作名还原可见 schema 线索，分别记录查询合法性及 resolver 的主体、对象和字段授权。关闭 introspection 不等于消除越权或注入，已知合法查询也不等于任意字段可读；不凭问题标题补写攻击回执。\n\n来源：[保存帖1](https://x.com/i/status/1449355902625140744)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "DomainProtect 的 CNAME 候选与真实资源归属",
    "图列 Route53/Elastic Beanstalk 链、四个候选和两个 vulnerable 标签，并建议创建云资源。\n\n保留 zone 权限、当前 alias/CNAME、资源生命周期、提供商错误和被别人绑定的可能性。工具标签不能证明名称仍未绑定、可认领或处于项目范围；创建资源是独立云变更，不能依据输出自行执行。只整理配置与归属证据，不实际认领或部署。\n\n来源：[保存帖1](https://x.com/i/status/1449498925862379522)。"
  ],
  [
    "discovery/web-and-api.md",
    "DorkScout 结果标题与 Dalfox 数据库报错",
    "DorkScout 图是 Hosting Controller 等链接列表，Dalfox 图只命中 OLE DB/MSSQL 报错并结束扫描。\n\n保存检索式、来源时间、真实输入及响应片段语义，再对候选单独做授权及消费者核对。页面标题与列表数不等于受影响系统数，数据库错误可能是无关异常；Dalfox 名称不使该错误自动成为 XSS，finish 也不证明 SQLi、RCE 或覆盖完整。\n\n来源：[保存帖1](https://x.com/i/status/1449710434236383234)、[保存帖2](https://x.com/i/status/1449717791733403649)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "云函数命令参数、调度调用与服务账号凭据类型",
    "图把 Scheduler/PubSub/函数串联，Python 函数直接读请求命令并调用 os.popen，另一图只有 Beanstalk 应用健康页。\n\n区分部署者权限、触发/调用 IAM、请求来源、运行服务账号、出网与具体敏感数据。预置命令处理代码需要先前部署权限，不证明任意云实例本身有漏洞；健康页不是执行回执。[Google 官方认证说明](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads)中的 metadata access token 是短期访问令牌，不能泛称长期服务账号私钥或保证跨服务权限。仅审计保存代码，不部署、调用或外传。\n\n来源：[保存帖1](https://x.com/i/status/1449825332299714562)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Fapro 模拟服务横幅与真实服务指纹",
    "图在 Windows 上列 FTP、MQTT、MySQL 等多个监听地址与端口，工具用于模拟服务。\n\n区分仿真监听器、横幅、协议对话、实际后端软件和权限。开放端口、产品字符串甚至预设弱口令描述都可能来自模拟器；需真实部署及协议语义才能判断漏洞。这里仅记录仿真用途，不启动监听器或把列表算作目标漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1449861466920730625)、[保存帖2](https://x.com/i/status/1450156041270857730)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "shell 的 IFS 和 glob 与 LFI 文件消费端",
    "两段帖给 shell 变量与通配符形态却贴 LFI 标签，另一图只显示 file 参数生成正常 HTML。\n\n先确定输入进入文件 API、include、模板还是 shell。IFS/通配符由相应 shell 消费，单纯文件读取不自动扩展它们；普通 file 参数也不证明任意本地文件可读。记录实际函数、根目录、权限与稳定无害文件对照，不能把命令语法直接命名 LFI 绕过。\n\n来源：[保存帖1](https://x.com/i/status/1450079792645111811)、[保存帖2](https://x.com/i/status/1450806265492516865)、[保存帖3](https://x.com/i/status/1450835749025181699)、[保存帖4](https://x.com/i/status/1451201317842522123)。"
  ],
  [
    "experiment-design.md",
    "Burp 四类功能与代理观察到主动变更的分界",
    "旧卡片列 Proxy、Repeater、Intruder 四模式和 Extender 的历史运行环境。\n\n为已授权实验区分被动捕获、单变量重放、批量候选与扩展代码运行，分别保存输入、动作预算、状态和观察。功能清单不证明目标已验证，扩展支持和旧 Python/JRuby 描述不构成当前安装建议；只有必要的获准最小对照才形成实验结论。\n\n来源：[保存帖1](https://x.com/i/status/1450117074680942593)。"
  ],
  [
    "discovery/passive-and-services.md",
    "被动 DNS 线索、第三方解析器与所有权",
    "正文推荐被动 DNS 两站，另帖想用第三方 hosts 服务更快解析；AXFR 帖循环猜十个 NS 并把带 scheme 的值当域名。\n\nDNS 线索需查询来源、时间、wildcard、权威服务器和资产归属；URL 不是 DNS 名称，猜测 NS 不是实际发现权威 NS。区分被动查询、域传送和第三方服务预算/授权，作者说平台允许自动化不授权所有解析服务或 zone。不加速滥用、不尝试域传送。\n\n来源：[保存帖1](https://x.com/i/status/1450320323891453952)、[保存帖2](https://x.com/i/status/1450512537498361860)、[保存帖3](https://x.com/i/status/1451346048669073412)。"
  ],
  [
    "by-type/idor-access-control.md",
    "x-user-id 与路径 ID 的身份优先级",
    "正文称 401 加用户头后 200，再描述路径用本人 ID、头用他人 ID 的改密请求；图片文档建议 identifyUser 可读取自定义头或认证中间件。\n\n绘制认证主体、网关可信头、后端 identifyUser、路径对象与动作对象的实际优先级；外部可控头须与可信中间件来源分开。文档允许自定义实现不证明部署一定采信攻击者，200 也不证明改密完成。以自有主体的正常/冲突/缺头对照确认业务状态，绝不复制受害者 ID 或令牌。\n\n来源：[保存帖1](https://x.com/i/status/1451376616194539521)。"
  ],
  [
    "by-type/host-header.md",
    "两个 Host 字段的 302 与重置邮件污染",
    "图片里原始 Host 和第二个 Host 并存，响应 Location 指向第二个域名，文字提到方案及转发头。\n\n保留原始线报文、头重复顺序、边缘拒绝/转发及 origin/absolute URL 构建规则。302 支持截图中的响应跳转观察，不证明重置邮件被污染或令牌外传；后者需自有收件地址、生成链接与重置令牌消费对照。不要把带 scheme 的无效 Host 和规范有效域名混为一类。\n\n来源：[保存帖1](https://x.com/i/status/1450772805780443144)。"
  ],
  [
    "source-audit.md",
    "伪代码签名成功与系统信任链",
    "LimeLighter 图明确写 fake cert 并输出 Signed File Created。\n\n分别保存文件哈希、签名结构、证书链、信任根、时间戳、用途及实际系统策略结果。带域名或创建签名文件不证明可信发布者、完整验证通过、SmartScreen/EDR 绕过或权限提升；此档案没有真实信任结果，不下载或执行输出文件。\n\n来源：[保存帖1](https://x.com/i/status/1450797539846918147)。"
  ],
  [
    "by-type/ssrf.md",
    "IMDSv2 工具名与元数据保护的具体边界",
    "保存帖仅介绍 Metabadger 自动化 IMDSv2，没有配置值或 SSRF 回执。\n\n按 EC2 实例、metadata 选项、令牌获取能力、请求方法/头、跳数与实例角色区分保护条件。工具支持 IMDSv2 不证明已启用或阻止所有 SSRF，云厂商之间的 metadata 和凭据类型也不能互换。只列审计边界，不修改实例或访问元数据。\n\n来源：[保存帖1](https://x.com/i/status/1450933458788929536)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "Jira 思维导图与两个 CVE 标题的版本映射",
    "Jira 帖引用 CVE 汇总；另一帖以两个编号并列认证 RCE 与未认证加管理员，但没有保存产品、版本或过程。\n\n先做编号、产品、版本、组件、访问前提与动作的对应表，区分代码执行和账号管理状态变化。汇总图、标签或 CVE 徽标不证明目标装有对应版本；认证前提不能互换，未提供信息不补写利用流程。\n\n来源：[保存帖1](https://x.com/i/status/1450963119501680651)、[保存帖2](https://x.com/i/status/1451092822577254401)。"
  ],
  [
    "by-type/csrf.md",
    "隐藏编辑接口到 CSRF 接管的缺口",
    "正文给找到账号/编辑接口、制作 CSRF、发送受害者的五步自述，配图只有 High 标题。\n\n隐藏接口仍需认证、字段权限、方法与实际用户上下文核对。跨站投递能力、令牌/Origin/cookie 条件和自有账号持久改变分别证明；High 标题、用户可见接口或自己提交成功不是完整接管链。不得向第三方发送 PoC，报告保留缺失步骤而非补写成功。\n\n来源：[保存帖1](https://x.com/i/status/1451167449253089290)。"
  ],
  [
    "by-type/xss.md",
    "邮件 HTML 注入的 mailto 方案与网页脚本差异",
    "卡片先展示 HTTP 链接和删双斜杠，后称换 mailto 可绕过；没有邮件客户端回执。\n\n比较过滤前后字节、HTML 节点、链接 scheme、真实邮件阅读器及点击后的处理端。mailto 可能仅唤起编写邮件，与站内脚本执行或 HTTP 导航不同；可点击链接仍需欺骗/可控内容和用户影响。缺少实际客户端、标签被转义、净化或不触发均是反例。\n\n来源：[保存帖1](https://x.com/i/status/1451181629448155143)。"
  ],
  [
    "by-type/desktop-client.md",
    "ASAN Chrome 启动步骤与堆错误证据",
    "保存正文列本地 HTTP 服务、ASAN Chrome 配置与 PoC 文件名，并自述奖励，没有保存完整 PoC、版本或崩溃栈。\n\n区分页面可加载、protocol handler 触达、特定构建 ASAN 报错、实际 heap 缺陷及可利用条件。启动步骤和奖励金额不能证明堆溢出，更不能推导任意代码执行；保留缺失版本/栈边界，不运行旧浏览器或档案 HTML。\n\n来源：[保存帖1](https://x.com/i/status/1451449019801096197)。"
  ],
  [
    "discovery/passive-and-services.md",
    "PortBender 转发日志与目标漏洞的因果边界",
    "图显示现有 Beacon 内加载模块，把 TCP 445 转到另一端口，并有连接日志。\n\n此操作依赖既有主机执行权限和网络配置；记录原始目的端、转发端、路由/进程及授权。连接接收不证明 SMB 认证、提权或最初入侵路径，转发工具也不是目标自身漏洞。仅整理保存日志，不注入 DLL、开启转发或更改系统端口。\n\n来源：[保存帖1](https://x.com/i/status/1451522238524665860)。"
  ],
  [
    "by-type/authn-session.md",
    "Nuclei token-spray 信息命中与第三方凭据使用",
    "终端图把多个 API 地址和原始 token 放在 info 命中行，正文线程仅保存第一段。\n\n脱敏保留 API 类型、模板版本、匹配条件及响应语义；info 或模板 loaded 数量不等于令牌权限/有效性验证。真实验证须独立授权，仅自有凭据与低影响能力对照；泄露值不授予任何第三方 API/租户访问权。不复制终端秘密，不调用这些 API 或执行保存模板。\n\n来源：[保存帖1](https://x.com/i/status/1451796617971974144)。"
  ],
  [
    "by-type/mobile-android.md",
    "长字段跨 Web 同步到 Android 的可用性链",
    "正文称长字段会使 Android 卡顿或崩溃，线程后续没有保存。\n\n按自有数据的长度/编码、Web 接受、存储、同步、移动读取和渲染逐层记录。资源预算、设备/版本、ANR/崩溃栈、恢复方式与持久状态需分别证明；大字符串、一次卡顿和不在图中的后续步骤不能称稳定跨平台 DoS。保持有界无害样本，不运行失控输入。\n\n来源：[保存帖1](https://x.com/i/status/1451415044416159749)、[保存帖2](https://x.com/i/status/1451818398141194241)。"
  ],
  [
    "by-type/xss.md",
    "图片文件名在元数据、URL 和 HTML 属性中的消费者",
    "正文把事件和标签形态放进 png/svg 文件名，未保存真实服务器输出或浏览器回执。\n\n把名称持久化、编码/规范化、列表文本、属性、链接 URL 与文件内容解析分开审查。同一名称在安全文本、百分号编码 URL 或静态下载中不执行；仅当实际 HTML 消费端将可控名称转为活跃节点/事件时才形成假设，需自有无害 DOM 标记及真实阅读上下文。扩展名本身不证明 XSS。\n\n来源：[保存帖1](https://x.com/i/status/1451822235497418756)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0112.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==113 and all(pid in ids for pid in urls)
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

