# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "discovery/records-and-incremental.md",
    "文件系统 Log4j 标签与实际加载组件",
    "图列多个嵌套jar/WAR里的core版本和VULNERABLE标签。文件存在不等于应用实际加载；同归档可能有多个版本、缓存/备份和不同服务。\n\n绑定文件哈希、实际依赖解析、运行类路径、日志实现及受控消息路径，区分API/core和不同漏洞条件。未加载、仅备份、修复回移、不同日志提供者或只有扫描标签为反例，不运行归档检测器或程序。\n\n来源：[保存帖1](https://x.com/i/status/1472797591045906433)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Log4j 训练扫描的 Target Affected 输出",
    "扫描图示localhost训练地址、DNS目标、Waiting和Target Affected；它保存的是扫描器判断和通道信息，未给类加载/命令结果。\n\n固定源请求、唯一无敏感标记、回调时间及解析器到应用的归因；DNS、LDAP、下载、执行分阶段。训练机、共享回调、重放或无执行证据不能扩大成真实目标RCE，不调用归档地址。\n\n来源：[保存帖1](https://x.com/i/status/1472470049629769735)、[保存帖2](https://x.com/i/status/1472903349800423427)。"
  ],
  [
    "scope-and-rules.md",
    "mapcidr 枚举不能扩展主机授权",
    "host-based文章配图仅将/23网段展开为IP列表，未证明每地址当前由目标控制或获准测试。\n\n以当前政策明确的主机/端口为键，CIDR算术、ASN、共用基础设施和应用归属分开；对列举结果只作线索。共享网段、云租户、排除资产或过期政策为反例，不对整网段发探测。\n\n来源：[保存帖1](https://x.com/i/status/1472921253870637057)。"
  ],
  [
    "targeted-fuzzing.md",
    "自定义子域词表与搜索 UI 的覆盖",
    "界面显示Default/上传词表下拉和少量结果；设置入口和表格不证明词表全部执行或DNS可达。\n\n绑定词表版本、候选总数、去重规则、解析器/超时、范围及每项结果；与同预算默认词表比较新增已确认资产。缓存、wildcard、截断列表、相同候选或无当前归属为反例，不运行暴力枚举。\n\n来源：[保存帖1](https://x.com/i/status/1472984908314263553)。"
  ],
  [
    "experiment-design.md",
    "按星期变化的 WAF 现象要控制变量",
    "正文称周三周日不受阻，其余天受阻，没有保存相同时段/身份的原始对照。\n\n时间只能是候选因素，同时固定请求字节、会话、出口、配额、缓存和应用版本，记录拒绝层与受保护操作。限流窗口、维护、出口变化或仅一次状态码不同为反例；不能以日历规律认定绕过或延长未授权测试。\n\n来源：[保存帖1](https://x.com/i/status/1472936944837570560)。"
  ],
  [
    "discovery/passive-and-services.md",
    "证书搜索命中与 origin IP 归属",
    "保存Shodan SSL/CN式和旧origin配置备份路径建议；搜索语法是否有效、证书关联、虚拟主机和当前归属均需证据。\n\n保存查询与结果时间，区分共享证书/CDN/反代、SNI/Host及应用响应身份。共用云IP、旧证书、统一登录页或范围外地址为反例，线索不授权直连源站或读取配置。\n\n来源：[保存帖1](https://x.com/i/status/1472979514196217865)、[保存帖2](https://x.com/i/status/1473069269042749446)、[保存帖3](https://x.com/i/status/1475079254547349507)。"
  ],
  [
    "by-type/business-logic.md",
    "负整数购物车建议与服务端金额不变量",
    "正文只给价格操控视频题名和负整数运算建议，未保存订单/交易交换。\n\n按数量、单价、折扣、税、货币和精度绑定服务端最终订单，保持身份/库存/商品相同，以自有无付款实验比较校验与读回。客户端显示变化、服务端拒负、购物车临时值或未创建权益为反例，不下生产订单。\n\n来源：[保存帖1](https://x.com/i/status/1472982834587389954)。"
  ],
  [
    "by-type/authn-session.md",
    "邀请占用邮箱到注册可用性的状态链",
    "三帖完整保存：攻击者邀请未注册邮箱，收件人不点击邀请而正常注册，出现Email already exist并不能创建账号；正文称奖励100。\n\n机制假设是pending邀请与已验证账号共享唯一邮箱键。自有两账号/邮箱对照无邀请、pending、过期、撤销及接受后注册；绑定持久状态与恢复行为。既有账号、正常合并/恢复、可取消或非持久显示为反例。它证明注册可用性候选，不自动ATO；不邀请或发邮件给真实第三方。\n\n来源：[保存帖1](https://x.com/i/status/1472999288322068486)、[保存帖2](https://x.com/i/status/1472999467817259016)、[保存帖3](https://x.com/i/status/1473000145054846977)。"
  ],
  [
    "by-type/sql-injection.md",
    "username 与 X-Forwarded-For 的不同注入位置",
    "一帖由证书线索到username/sqlmap高风险选项并配Closed Critical标签；另一图标定custom HEADER X-Forwarded-For，74请求及MySQL time-based判断。\n\nURL参数和代理头各自绑定原始请求、真实消费位置、数据库权限和稳定真假/时间对照；标签、74计数、单次延迟、统一响应或代理先处理为反例。数据库枚举/高risk/十线程不能代替范围及预算，不运行工具或延迟查询。\n\n来源：[保存帖1](https://x.com/i/status/1473069269042749446)、[保存帖2](https://x.com/i/status/1474352640981143553)。"
  ],
  [
    "discovery/web-and-api.md",
    "JS grep 的域名正则与实际 URL 边",
    "正文正则和泛称JS可找子域/端点均为静态线索，正则字符类[A-z]及分段结构不能作为所有域名规范验证。\n\n保留原文件/偏移、完整URL解析、拼接变量、真实调用与当前部署版本；测试字符串、注释、第三方服务、语法误命中或未使用分支为反例。候选再绑定资产/权限，不执行JS或按词数认漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1473075645462814720)、[保存帖2](https://x.com/i/status/1473562136173445121)、[保存帖3](https://x.com/i/status/1475126620432191490)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "nuclei 聚类与多等级命中的证据归并",
    "两张图有402聚类/减少369HTTP请求和多个critical/high/medium/info/CVE标签，正文是情绪反应。\n\n保存模板版本、请求/匹配器、原始响应和对象键，聚类优化、检测覆盖、独立机制、验证、等级分开。裁剪目标、指纹/info、重复模板/共享响应或无能力变化为反例，不把列表计作全部漏洞或许可。\n\n来源：[保存帖1](https://x.com/i/status/1473268197382139905)。"
  ],
  [
    "by-type/authn-session.md",
    "替换 2FA 响应与真正的服务端能力",
    "正文建议将403/404/503变200、false变true/error变success，配图实际是200USD处理邮件，未保存服务端验证。\n\n用自有账号先绑定挑战、会话和受保护动作，再比较未经客户端伪造的真实网络请求与持久服务端结果。只显示已登录、本地改UI、后续仍拒绝或邮件另一个问题为反例；不发OTP或接管真实账号。\n\n来源：[保存帖1](https://x.com/i/status/1473343787007361024)。"
  ],
  [
    "reporting.md",
    "Abuse Risk、P4、已修复和奖励的分开记录",
    "图展示Google Abuse Risk转Trust & Safety、Sensitive PHP info page获奖、Closed SQL Critical/未付、Grafana snapshot P1 Triaged、Log4j Medium和Synack四项1760/1408/588/270；这些状态不提供实际机制交换。\n\n每条绑定独立问题ID、提交渠道、处理时间/状态、证据和金额；转组、仍评估、遮挡、重复、未支付或仅标题不能变成最终影响/资格结论。不联系平台、开票或支付。\n\n四张Duplicate Closed图虽等级/旧CVE不同，也只补充去重处理状态；JS key三千金额声明没有有效凭据权限交换。\n\n来源：[保存帖补1](https://x.com/i/status/1475483864323825668)、[保存帖补2](https://x.com/i/status/1474596954361507845)、[保存帖1](https://x.com/i/status/1473026269793198085)、[保存帖2](https://x.com/i/status/1473069269042749446)、[保存帖3](https://x.com/i/status/1473226449121333248)、[保存帖4](https://x.com/i/status/1473343787007361024)、[保存帖5](https://x.com/i/status/1473365966948126729)、[保存帖6](https://x.com/i/status/1473937346064261123)、[保存帖7](https://x.com/i/status/1474295088880697345)、[保存帖8](https://x.com/i/status/1474687966542909440)、[保存帖9](https://x.com/i/status/1475082889955926018)、[保存帖10](https://x.com/i/status/1476116169689993216)。"
  ],
  [
    "targeted-fuzzing.md",
    "仅登录面板词表与隐藏功能假设",
    "正文为仅登录面板提供词表入口；界面可见功能少不代表后台只有认证。\n\n结合JS/路由/正常流确定候选路径，记录词表、方法、身份和soft404/统一登录基线；只有目录计数、统一重定向、范围外路径或缓存为反例，不暴力猜凭据。\n\n来源：[保存帖1](https://x.com/i/status/1473529368714440704)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "S3 ListBucket 拒绝不说明 PutObject 被拒绝",
    "正文分别称ls拒绝、cp上传，图只为Misconfigured s3 bucket Triaged邮件。\n\n[AWS权限文档](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)将ListObjects/ListObjectsV2的ListBucket和上传PutObject分为动作。固定认证主体、bucket/key/prefix与策略条件，分别记录读、列、写和持久读回。已凭据授权写、不同前缀、预签名、未完成上传或只有邮件为反例；不写/删真实桶，不把单动作推导全部权限。\n\n来源：[保存帖1](https://x.com/i/status/1473620224444223490)。"
  ],
  [
    "by-type/ssrf.md",
    "localhost 变体、IPv6 与实际解析层",
    "完整列表含短IPv4、十进制/十六/八进制样式、userinfo、IPv6未指定/缺括号形式；不能都称127.0.0.1等价或对所有解析器有效。\n\n固定方案、原始字节、校验器、DNS/连接解析器与最终地址，在自有无敏感端点比较。解析拒绝、IPv6未指定地址、只客户端、重定向重新校验或无法到达为反例；不把列表当现成内部权限。\n\n来源：[保存帖1](https://x.com/i/status/1473626079520714753)。"
  ],
  [
    "impact-and-acceptance.md",
    "SSRF 的真实影响不由 RCE 标签替代",
    "正文两相同体帖子主张不要报SSRF应升级RCE，另帖询问DNS是否足够；缺少实际第二阶段。\n\n记录服务器请求、网络/文件读、认证上下文和独立能力变化，各阶段用已允许的最小证据支持。DNS解析、阻断出口、无加载能力或只有文章题名为反例；有效受限影响也应如实报告，不为评级执行命令/外发秘密。\n\n来源：[保存帖1](https://x.com/i/status/1473640106741284866)、[保存帖2](https://x.com/i/status/1476408448791289857)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "同一第三方主体连接两个本地账号",
    "保存步骤是provider先连account1再连account2，邮件题名为authorization token misconfiguration/3000；未保存redirect/state/token交换。\n\n绑定issuer+稳定sub与本地账号、当前登录主体、连接/断开和重新登录，用自有账号比较正常重复连接策略及最终权益。合法多账号连接、确认旧绑定、被拒或只邮件为反例；绑定冲突不自动token窃取/ATO，不链接真实第三方账号。\n\n来源：[保存帖1](https://x.com/i/status/1473649582034804743)。"
  ],
  [
    "by-type/ssrf.md",
    "JS 内部 host 和 port 只生成候选",
    "正文建议失败后搜main.js/app.js的localhost/127.0.0.1/host/port；图仅局部JS regex里localhost:53519，没有内部请求读回。\n\n保留代码上下文、部署环境、真实服务消费者及网络位置，将测试/开发配置与运行调用分开。注释、localhost在浏览器、正则验证、服务不存在或无服务器请求为反例，不访问归档内网资源。\n\n来源：[保存帖1](https://x.com/i/status/1473654508521549828)、[保存帖2](https://x.com/i/status/1473654924445511680)。"
  ],
  [
    "by-type/business-logic.md",
    "工作邮箱域名过滤与身份要求",
    "googlemail绕gmail限制是域字符串策略假设，未保存账号创建或权益。\n\n区分字符串denylist、邮箱验证、组织域所有权/SSO和真实受保护功能；自有邮箱仅比较允许/拒绝及最终权限。明确允许个人邮箱、只UI、后台拒绝或无组织权益为反例，不把邮箱别名当企业身份，不注册真实目标。\n\n来源：[保存帖1](https://x.com/i/status/1473669684037767173)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Burp history 与个人 wiki 的可追溯笔记",
    "正文分别强调Repeater/History和持续个人wiki；可复用的是来源、假设与实验的连续记录。\n\n绑定请求/响应身份、环境版本、时间、最小对照和结论状态；在wiki写反例、未验证条件及下次允许动作。只有收藏/工具名、旧结果或脱离主体的截图为反例；保留当前许可，不自动重放历史流量。\n\n来源：[保存帖1](https://x.com/i/status/1473699310999068672)、[保存帖2](https://x.com/i/status/1475523373337874437)、[保存帖3](https://x.com/i/status/1476519652675055618)。"
  ],
  [
    "by-type/info-secrets.md",
    "GitHub Dork Helper 与 Slack webhook 搜索",
    "图是关键词生成器以及54条代码搜索/部分Webhook字符串；命中数字或格式不说明仍有效、归目标或具有读频道能力。\n\n绑定仓库/提交/时间和字段类型，区分测试样例、历史撤销、写入webhook与读取权限；安全报告仅用脱敏上下文。空生成表单、截断字符串、第三方仓库、撤销或不属范围为反例，不使用token或发送Slack消息。\n\n来源：[保存帖1](https://x.com/i/status/1473729425275564042)、[保存帖2](https://x.com/i/status/1475503703855616001)。"
  ],
  [
    "by-type/xss.md",
    "XMB 嵌套 BBCode 到事件属性的消费者链",
    "完整保存嵌套url标签文本，图是localhost私信admin到admin和弹窗1，渲染正文混入onclick片段。\n\n记录BBCode解析、链接构造、属性编码与最终DOM事件，比较普通标签和嵌套标签的自有无副作用输出；受众、存储与触发动作分开。只localhost自投、不同版本、安全序列化或不进入事件上下文为反例，不把CVE题名当所有部署验证，不运行归档脚本。\n\n来源：[保存帖1](https://x.com/i/status/1473739430468980745)、[保存帖2](https://x.com/i/status/1476545420897570816)。"
  ],
  [
    "by-type/waf-bypass.md",
    "JNDI 混淆后的应用校验仍不证明求值",
    "保存AWS PUT/cart同类请求403 ForbiddenException对比400 Envoy返回Required value itemId must contain 6 characters，字符串被反射；另帖只有混合lookup正文。\n\n固定方法/路由/主体和字节，区分边缘拒绝、应用校验、普通反射、lookup、回调和执行。400长度拒绝、字符串原样回显、无logger路径、无独立回调为反例，不调用归档LDAP/公网地址。\n\n来源：[保存帖1](https://x.com/i/status/1472879704692514816)、[保存帖2](https://x.com/i/status/1473777341201625088)。"
  ],
  [
    "targeted-fuzzing.md",
    "curl 子域脚本的超时与状态码边界",
    "完整脚本以词表循环curl半秒timeout，每次睡0.1，1000计数时睡10，并将非000写文件；图有未引用变量和$x=0等可疑重置。\n\n这里只静态读逻辑，000、短超时、协议默认、重定向和状态码必须分别记录，不能把非000当当前资产活跃/有漏洞。变量/路径损失、缓存/wildcard或请求预算不符为反例，不运行脚本或以后台done绕预算。\n\n来源：[保存帖1](https://x.com/i/status/1473816300648554497)。"
  ],
  [
    "by-type/jwt.md",
    "JWT 历史问题类型不能只看 none",
    "正文列none、HS/RS公钥混用及node-jose旧CVE，1/2提示的后续外链按用户口径覆盖；配图仅装饰。\n\n定位真实库版本、允许算法、密钥来源/类型、issuer/audience和最终受保护能力，在自有测试将算法/密钥/声明分别比较。明确允许且其他完整性保护、库拒绝算法混用、未消费token或只CVE列表为反例，不使用归档token。\n\n来源：[保存帖1](https://x.com/i/status/1473828358316343303)。"
  ],
  [
    "by-type/business-logic.md",
    "付款 API amount 的截图与实际权益",
    "Shopify插件题名配付款页146.08SGD与API请求amount/订单字段，但响应面板空，未有支付完成或服务端订单读回。\n\n固定商品、币种、身份和订单ID，区分客户端展示/API请求值、服务器重算、真实支付和最终权益。未发请求、支付服务校验、签名绑定或空响应为反例，不下单/付款或修改生产订单。\n\n来源：[保存帖1](https://x.com/i/status/1473855004184170496)、[保存帖2](https://x.com/i/status/1473903677916123136)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "完整 Log4j 速查卡的通道、变量与权限",
    "卡列控制字符串的headers/输入/文件/EXIF等入口，DNS里的host/Java版本、训练服务/扫描器，以及sys/env变量；还泛称旧版本范围RCE。\n\n记录实际Log4j-core/加载版本、logger路径、lookup/网络/加载条件；DNS变量是信息通道，不能单凭它证明任意命令。API-only、无消息求值、补丁、出口拒绝或训练环境为反例；不发送环境凭据、创建回调或运行样本。训练/历史版本与当前目标独立。\n\n来源：[保存帖1](https://x.com/i/status/1473923526973263872)、[保存帖2](https://x.com/i/status/1475433333416886277)。"
  ],
  [
    "by-type/xss.md",
    "赋值调用与 optional chaining 的演示边界",
    "正文给赋值confirm和注释/optional chaining变体；后图明确在chrome new-tab控制台自行调用alert。\n\nJavaScript语法可执行与应用输入能进入脚本是两件证据，需真实响应/DOM、编码、语法位置和受众；用自有安全标记比较。控制台粘贴、来源遮挡、不支持语法、被转义或无其他读者为反例，不将语法演示叫WAF/XSS成功。\n\n来源：[保存帖1](https://x.com/i/status/1473980395389554691)、[保存帖2](https://x.com/i/status/1475555795995865088)。"
  ],
  [
    "source-audit.md",
    "SeImpersonate 的已获入口与 SYSTEM 后置条件",
    "MultiPotato图先显示SeImpersonate enabled，后创建pipe/duplicate token并报告SYSTEM及本地用户加入管理员。它没有保存初始漏洞入口。\n\n区分已有代码执行主体、可用特权、pipe客户身份、token类型和最终能力，静态记录自有实验的原权限对照；没有该权、客户端未连、令牌不满足或仅菜单为反例，不运行工具/创建账户/修改组。\n\n来源：[保存帖1](https://x.com/i/status/1474126359278538755)。"
  ],
  [
    "by-type/ssrf.md",
    "PII 文章配 OOB 列表的证据错配",
    "正文称数百万投资者/注册信息，图却只有Burp OOB交互三条，目标遮挡，无PII字段或匿名读取。\n\n技术机制按图仅记录通道事件，正文的数量/敏感性需独立对象与受众证据。无关联请求、DNS递归、裁剪或标题错配为反例，不恢复外链全文或放大成数据泄露。\n\n来源：[保存帖1](https://x.com/i/status/1474272305958191108)。"
  ],
  [
    "by-type/graphql.md",
    "批量删除 JSON 与逐对象授权",
    "Phineas正文/flag替代文字配图却是多个数字payload均200和data.BulkDeleteAlertDefinitions，结果是website/alertDefinitions/id/typename嵌套。\n\n绑定实际operation、身份、对象归属和持久状态读回；HTTP200/嵌套对象并不证明成功删除、越权或所有对象有漏洞。错误字段、空列表、合法本人对象或仅响应为反例，不执行批量删除，也不按CTF题名解释此图。\n\n来源：[保存帖1](https://x.com/i/status/1474281187862409219)。"
  ],
  [
    "by-type/sql-injection.md",
    "SQLbit 的布尔真值须保持查询与行号语义",
    "图配置stock中的项作为True判据，展示count14、长度和unicode/行号及商品名；这是工具输出，未保存原始响应。\n\n按固定数据集和稳定真假对照绑定条件、行索引、编码/排序与响应字段。统一200、缓存、分页变化、并发写入或只有工具works为反例，不提取真实数据或运行脚本。\n\n来源：[保存帖1](https://x.com/i/status/1474352878672400386)、[保存帖2](https://x.com/i/status/1474353360039931908)。"
  ],
  [
    "targeted-fuzzing.md",
    "FTP 条件 sed 与参数结构保真",
    "完整正文alt和图将含ftp URL的File/FILE替换path，再grep截至参数等号，丢掉值和余下结构。\n\n保存原URL、条件命中、参数大小写/位置和变异映射，使用解析后的键生成受控候选。主机含ftp但参数非文件、多个参数/编码、片段丢失或重复语义为反例，不把path候选当LFI，不运行归档管线。\n\n来源：[保存帖1](https://x.com/i/status/1474361457265590281)。"
  ],
  [
    "by-type/authn-session.md",
    "Spray365 执行计划与真实认证结果",
    "图仅生成24条计划、随机AD client/endpoint IDs、每次延迟10秒、总240秒，没保存登录结果。\n\n计划与执行/身份/锁定/限流分别记录，随机入口不改变所有账号共享策略或授权范围。未执行、同一计数器、缺主体许可或只有保存计划为反例，不喷洒口令或使用归档列表。\n\n来源：[保存帖1](https://x.com/i/status/1474488690848288776)、[保存帖2](https://x.com/i/status/1474671881399652352)。"
  ],
  [
    "scope-and-rules.md",
    "顶级域枚举与通配政策字面边界",
    "正文假设*.example.*并给tld-scan仓库封面，未有当前政策和命中列表。\n\n将组织名称相似、TLD候选、实际控制与政策列举分别记载；需要明确哪些域/子域/端口纳入，保留排除项。品牌相似、第三方注册、范围歧义或过期政策为反例，不用脚本推导所有TLD授权。\n\n来源：[保存帖1](https://x.com/i/status/1474804831311204353)。"
  ],
  [
    "source-audit.md",
    "NimHollow 图的创建暂停进程与 PE 入口",
    "图只展示injector CreateProcess/CREATE_SUSPENDED、PROCESS_INFORMATION、PEB/TEB及MZ/e_lfanew/EntryPointRva算入口地址，没有实际注入成功。\n\n绑定已有执行主体、进程/架构、访问权限、实际内存/线程消费者；概念布局、架构错配、无法获取句柄或无运行证据为反例，不创建/修改真实进程或运行PoC。\n\n来源：[保存帖1](https://x.com/i/status/1474851083340156929)。"
  ],
  [
    "by-type/authn-session.md",
    "phpMyAdmin root 空密码是待证历史建议",
    "正文只有尝试root/blank建议，未保存版本、初始化方式或登录交换。\n\n面板指纹、配置账号、数据库允许来源和真实成功会话分别记录；旧说明、已改口令、禁账号、统一登录页或无授权为反例，不尝试归档口令。\n\n来源：[保存帖1](https://x.com/i/status/1474857105790226438)。"
  ],
  [
    "discovery/passive-and-services.md",
    "altdns 到 gobuster 的完整候选解析管线",
    "完整卡生成middle-sub词表、sed去.example.com、DNS指定resolver/80线程和screen后台；这些是主动枚举动作。\n\n保留完整域名/标签映射、候选重复、wildcard、resolver时间及实际归属，预算内比较新增已确认资产。sed全局误删、DNS缓存/超时、后台仍发请求或无当前许可为反例；更多子域不自动更多漏洞，不运行命令。\n\n来源：[保存帖1](https://x.com/i/status/1474886800422453251)。"
  ],
  [
    "by-type/info-secrets.md",
    "wp-config.php.save 是配置备份候选",
    "正文给origin IP与wp-config.php.save并称P1，无保存真实文件内容/认证结果。\n\n绑定真实vhost和文件类型、来源/环境、非敏感标记与受众权限；200登录页、备份不存在、空模板、已撤销字段或范围外源站为反例，不读取真实凭据或按P1直接认影响。\n\n来源：[保存帖1](https://x.com/i/status/1475079254547349507)。"
  ],
  [
    "by-type/ssti.md",
    "Velocity 权限提升与 RCE 的不同结果",
    "正文主张Java Velocity SSTI可升权即使无RCE，但未保存对象访问、模板执行或最终权限交换。\n\n识别真实模板引擎/版本、可控制模板边界、暴露对象与受保护状态；无副作用的自有对象对照区分表达式、读取和状态能力。普通文本、客户端模板、权限检查仍在或仅文章标题为反例，不为证明升权修改真实账号。\n\n来源：[保存帖1](https://x.com/i/status/1475111531515990024)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "全端口管线与五类服务命中分开验证",
    "完整正文双编码Carbon内容与两图含rustscan1-65535→grep/tee/sed→httpx→nuclei2.5.4/templates8.7.1、2752模板及Nacos/heapdump/Grafana/mongo-express五标签。历史latest不代表当前。\n\n端口发现、HTTP身份、模板检测和实际权限分别记录；非HTTP端口、行解析损失、未完成扫描、统一响应或多个模板共享根因为反例。不按alive IP自动全端口扫描，不访问秘密/运行高负载或建立回调。\n\n来源：[保存帖1](https://x.com/i/status/1475205809453912068)、[保存帖2](https://x.com/i/status/1475346758838329346)。"
  ],
  [
    "by-type/info-secrets.md",
    "SourceLeakHacker 中断扫描与真实文件类型",
    "图只有根/robots.txt200、七项404、read timeout及Ctrl C等六线程退出；没有源码文件内容。\n\n候选扩展/备份名与实际文件字节、内容类型、身份及运行完成分开。robots公开、soft404、超时/取消或只代码统计为反例，不认所有路径已排查或源码泄露，不运行扫描器。\n\n来源：[保存帖1](https://x.com/i/status/1475228556020101122)。"
  ],
  [
    "by-type/idor-access-control.md",
    "API _id 外键卡与对象关系授权",
    "完整API卡建议以user_id/order_id/product_id找关联接口并复数化规则；命名规则不能保证真实数据库外键/endpoint。\n\n将字段、对象边和真实正常流绑定，再用自有两主体/对象最小对照验证每端权限。复数例外、只字段名、关联对象合法共享、服务器拒绝或未知接口为反例，不全局替换生产流量或批量读取。\n\n来源：[保存帖1](https://x.com/i/status/1475300411254976514)。"
  ],
  [
    "by-type/ssrf.md",
    "metadata 路径出现在 API 请求中的证据范围",
    "银行17问题题名配图是带会话的OData请求、嵌套元数据路径和200JSON，其中代码/key等内容遮挡。不能仅凭路径文本认真实元数据访问、匿名读取或17个独立漏洞。\n\n分别绑定最终服务器请求者、网络目标、IMDS令牌/实例角色、原响应来源与真实受保护能力；普通路径回显、合法登录、环境错配、无二次请求或遮挡为反例，不复制/使用cookie或秘密。\n\n来源：[保存帖1](https://x.com/i/status/1475335781610713090)。"
  ],
  [
    "by-type/info-secrets.md",
    "Drive 下载卡的 shareable link 与下载权限",
    "完整卡从共享链接提取fileID/filename、读取确认页并带cookie，禁证书验证且删除临时cookie文件；没有实际下载结果。\n\n共享可见、下载授权、重定向确认与本地文件完整性分别记录；登录要求、无共享权限、页面而非文件、过期链接或TLS无法验证为反例，不运行命令/获取归档文件或删除用户文件。\n\n来源：[保存帖1](https://x.com/i/status/1475526662489980929)。"
  ],
  [
    "by-type/xss.md",
    "Content-Disposition 文件名到响应头和 HTML",
    "正文称可控文件名进入Content-Disposition后CRLF修改Content-Type到text/html，无保存原始响应或受众。\n\n按字节追踪文件名校验/编码、头序列化、代理/协议处理、最终MIME及内容消费者；自有标记比较拒绝与正常读回。换行拒绝/编码、HTTP2处理、attachment下载、无可控HTML或无其他受众为反例，不把头反射直接认XSS。\n\n来源：[保存帖1](https://x.com/i/status/1475627378827309061)。"
  ],
  [
    "source-audit.md",
    "手绘核心防御图的四条边界",
    "完整手绘图覆盖用户访问的认证/会话/权限；输入拒坏/允许好/净化/安全数据处理/语义/边界/多次验证规范化；错误/审计/告警/响应；管理应用。\n\n用真实功能流把每边界映射到主体、对象、输入及消费者，最小对照定位失效边而非凭术语判漏洞。正确安全处理、层间同义、合法权限或仅地图为反例，不将防御清单当已运行检查。\n\n来源：[保存帖1](https://x.com/i/status/1475719285813174272)。"
  ],
  [
    "by-type/info-secrets.md",
    "API Guesser 格式识别与 token 处理",
    "图是空API key/token表单，正文建议第三方JS网站猜类型；没有识别结果或有效权限。\n\n从公开格式/来源脱敏上下文推断候选类型，真实发行者/作用域/有效性另证；不能上传归档或用户秘密。随机同格式、测试样例、已过期或只有空表单为反例，不使用token/访问识别站点。\n\n来源：[保存帖1](https://x.com/i/status/1475725873575698437)。"
  ],
  [
    "by-type/xss.md",
    "地址栏 javascript 弹窗不证明反射 XSS",
    "两图地址栏是javascript:alert，登录页弹窗及cookie文本；没有保存从服务器/DOM输入到执行的请求。\n\n固定真实来源、注入入口、最终消费者和受众；本人书签/地址栏执行与站点反射分别记录。控制台/地址栏自执行、无可控输入、只有自己的cookie或来源遮挡为反例，不复制/使用cookie或认登录ATO。\n\n来源：[保存帖1](https://x.com/i/status/1475760783233478662)。"
  ],
  [
    "by-type/authn-session.md",
    "Email confirmed 界面与服务端验证状态",
    "标题称邮件验证绕过，图只有Email confirmed成功模态框，未有验证token/绑定或后端读回。\n\n自有邮箱比较未验证与正确/错误/过期token后的真正状态及受保护操作，绑定会话/邮箱/目的。客户端响应替换、固定成功UI、服务器仍拒绝或无原请求为反例，不发送邮件或操作真实账号。\n\n来源：[保存帖1](https://x.com/i/status/1475780324952985600)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "APISIX Dashboard 导出、配置写入与执行分阶段",
    "正文泛称所有<2.10.1，图一是Exists Vuln脚本/登录页，另一为配置JSON中filter_func含os.execute字符串，未有实际执行结果。\n\n[官方历史公告](https://apisix.apache.org/blog/2021/12/28/dashboard-cve-2021-45232/)限定Dashboard2.7–2.10，修复2.10.1；未认证接口可能读写配置，并引出SSRF/代理/执行。Dashboard与网关组件、实际路由/中间件、读配置、可写与真正消费者分别证明。补丁、不同组件、只登录页/字符串或无路由执行为反例，不导出真实秘密、改配置或执行命令。\n\n来源：[保存帖1](https://x.com/i/status/1475799108812419073)、[保存帖2](https://x.com/i/status/1475804838495940609)、[保存帖3](https://x.com/i/status/1476119572822454273)、[保存帖4](https://x.com/i/status/1476221491637280776)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "data wrapper 的构造与 include 消费者",
    "正文alt和完整图展示base64 PHP/phpinfo以及ffuf PHP Version匹配，未保存任何结果且没有FUZZ位置。\n\n[PHP data文档](https://www.php.net/manual/en/wrappers.data.php)列读取与allow_url_fopen/allow_url_include限制；file_get_contents读字符串与include执行不同。绑定真实消费者、配置、编码和无副作用自有标记；被禁、仅文本读取、固定URL单次或匹配历史文本为反例，不运行归档PHP/命令。\n\n来源：[保存帖1](https://x.com/i/status/1475803132659748871)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Referer 403 到 200 需证明同一受保护对象",
    "正文只有敏感站403，加自身Referer变200，未保存内容或身份。\n\n固定Host/SNI/路径、会话、缓存、原字节及实际受保护能力，区别来源提示、WAF路由和服务端授权。200登录页/空响应/缓存、合法本人对象或不同路由为反例；状态码变化不能直接认越权，不访问归档敏感站。\n\n来源：[保存帖1](https://x.com/i/status/1475817334896046089)。"
  ],
  [
    "by-type/sql-injection.md",
    "MySQL 多语句取决于实际调用 API",
    "正文说MySQL通常不能batched而PHP/Python偶有可能；不能据数据库名全局判断。\n\n[PHP mysqli文档](https://www.php.net/manual/en/mysqli.multi-query.php)说明multi_query支持分号分隔的多个查询。实际需绑定驱动版本/模式、调用方法、参数化边界、结果集与数据库权限；正确数据参数、单语句拒绝或无拼接入口为反例。不根据语言名推测所有接口，也不运行堆叠写入/枚举。\n\n来源：[保存帖1](https://x.com/i/status/1475818922536439808)。"
  ],
  [
    "by-type/xxe.md",
    "DOCTYPE 与返回 XML 字段的真正消费阶段",
    "正文建议定义外部实体并在会返回字段引用，没保存解析器或读回。\n\n追踪请求XML的实际解析阶段、DTD/外部实体配置、网络/文件访问及最终响应，用自有无敏感标记比较禁用/允许。仅响应文本、解析器禁DTD、普通转义、无外部访问或只模板为反例，不读取真实文件/发送外部回调。\n\n来源：[保存帖1](https://x.com/i/status/1476054437361684480)。"
  ],
  [
    "source-audit.md",
    "Kiwi 菜单、架构警告与已有控制前提",
    "图是在已compromised主机Meterpreter load kiwi，提示x86载x64，列凭据/DCSync/ticket/LSA/密码/WiFi命令；仅加载菜单没有实际凭据或提权结果。\n\n已有会话、进程架构、系统/目录权限与每命令消费者分别记录；菜单可用、架构错配、无必要权或无真实响应为反例。不运行命令、抓凭据、修改密码/票据或连接域控。\n\n来源：[保存帖1](https://x.com/i/status/1476157298141585408)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "LFI 目录页的 wrapper 与真实包含关系",
    "图定义本地文件包含并列expect/php/filter/proc/fimap/phpinfo目录，仅保存概要不是完整利用步骤。\n\n区分读取、包含、模板和执行的真实消费者及实际wrapper/模块配置；不存在的扩展、仅文本读、权限拒绝或目录标题为反例，不按目录自动认RCE/可读秘密。\n\n来源：[保存帖1](https://x.com/i/status/1476203592440709124)。"
  ],
  [
    "by-type/ssrf.md",
    "Windows file 方案与 NTLM 外发条件",
    "正文建议SSRF到file/VPS获NetNTLMv2，但没有原请求/认证协商。\n\n须有实际服务器端URL/UNC消费者、支持该方案、Windows身份与出站SMB/认证策略；单纯HTTP/DNS回调、禁file/网络或无身份自动协商为反例。读路径、认证握手、凭据材料和后续能力分开，不创建监听/外发或破解真实认证材料。\n\n来源：[保存帖1](https://x.com/i/status/1476423301668999179)。"
  ],
  [
    "by-type/info-secrets.md",
    "CookieExample 与 phpinfo 的服务端回显边界",
    "一图为Servlet CookieExample显示请求cookie，与clickjacking题名错配；另一图info.php显示ci_session并在Storage标HttpOnly true/Secure false。\n\n[PHP官方文档](https://www.php.net/manual/en/function.phpinfo.php)说明phpinfo可包含EGPCS Cookie数据。HttpOnly不阻止cookie随匹配请求送服务器；服务端再输出需单独评估读者。本人看到自己cookie、无法跨主体读取、无利用入口或标题错配为反例。记录cookie类型/属性而不复制值，不推导所有HttpOnly失效或ATO。\n\n来源：[保存帖1](https://x.com/i/status/1476462748359921669)、[保存帖2](https://x.com/i/status/1476518831702953985)。"
  ],
  [
    "by-type/info-secrets.md",
    "favicon 文章链接 fragment 中的 token 暴露",
    "正文保存的文章URL fragment带id_token样式长值。它是归档信息暴露线索，不能凭格式或可解码声明认当前有效/可冒用身份。\n\n只记录参数名、字段类型、URL阶段和传播面，区分日志/历史/客户端fragment/分享与服务端接收；来源、过期、audience、签名验证、真实权限另证。不复制token/PII、不提交验证或访问带值URL。过期/裁剪/仅格式且无消费者为反例。favicon hash线索同样需实际来源/部署与归属，不能按相似图标授予测试范围。\n\n来源：[保存帖1](https://x.com/i/status/1476617665246633987)。"
  ],
  [
    "by-type/host-header.md",
    "未知 Host 的响应变化与真正消费位置",
    "两同正文帖建议先换任意未知Host，没有保存响应或后续消费者。\n\n固定请求方法、路径、主体、连接/SNI与Host，记录代理路由、缓存键、生成链接和真实受保护动作；自有实验比较正常、未知与拒绝。400/421、默认vhost、登录页、不同路由或只状态变化为反例，未知域名不是现成密码重置/缓存影响，不请求归档目标。\n\n来源：[保存帖1](https://x.com/i/status/1476234387620462592)。"
  ],
  [
    "by-type/sql-injection.md",
    "Incapsula SQL 图中的 200 与延迟假设",
    "题名宣称Imperva绕过，图含SQL条件/延迟样式query与200JSON，头有Cloudflare/Incapsula字样；单次工具耗时不能证明指定延迟或真假稳定关系。\n\n绑定实际查询入口、真实防护层、字节/会话和无副作用对照，分别记录边缘接受、数据库语义与可观察数据能力。固定正常JSON、仅200、标题错配、缓存或无时间基线为反例，不运行延迟语料或据此认全部WAF绕过。\n\n来源：[保存帖1](https://x.com/i/status/1473614357019783174)。"
  ]
]

ids={pid for row in json.loads((W/"batch-0117.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert len(urls)==99 and all(pid in ids for pid in urls)
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

