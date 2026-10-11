# 社区材料的分类提炼

知识正文已直接融入本 skill 的对应专题；本页汇总分类、可执行检查点与去重位置。日常使用按业务线索读取专题即可，不需要原始归档目录、帖子正文、图片、OCR 或检索工具。D 编号仅用于来源追溯，不表示优先级或等级。

## 资产、接口与可观察性

| 编号 | 提炼后的检查点 | 技能内落点 |
|---|---|---|
| D01 | 主机、端口、应用和路径分别确认。首页 404 后，仍可从真实链接、产品文档或源码核对具体业务路径；产品指纹只帮助选择候选。 | [被动与服务发现](../discovery/passive-and-services.md) |
| D02 | 从 JS、历史 URL、source map 和发布材料提取带位置与版本的端点。目录拒绝、文件可读和敏感内容是三个问题，逐项验证。 | [客户端与云资源](../discovery/client-and-cloud.md) |
| D27 | 将截断、缺图、线程/外链未读和观察渠道失效保留为缺口。历史采集状态不代表当前进程状态；日志显示过滤与出站范围控制分开判断。 | [发现记录与增量](../discovery/records-and-incremental.md) |

## 身份、权限与跨端业务

| 编号 | 提炼后的检查点 | 技能内落点 |
|---|---|---|
| D03 | 用主体×对象×操作×字段比较权限。只读成员也检查归档、删除、复制、指派与任务创建；复制的原对象、新对象和继承权限分开确认。 | [访问控制](../by-type/idor-access-control.md)、[属性授权](../by-type/api-property-pollution.md) |
| D04 | MFA 是否完成由服务端受保护能力证明。保留挑战前凭据，对比正常完成会话；代理修改成功字段或状态码只说明客户端被放行。 | [认证与会话](../by-type/authn-session.md) |
| D05 | 用两个独立会话核对改密、退出、撤权后的 access token、refresh token、恢复链接和会话生命周期；排除页面缓存、刷新换新与合法保留策略。 | [认证与会话](../by-type/authn-session.md) |
| D06 | 分别证明凭据有效、主体存在和凭据属于该主体。两个受控提供方身份对照 issuer、subject、audience、发起会话与账号绑定。 | [OAuth/OIDC](../by-type/oauth-oidc.md)、[JWT](../by-type/jwt.md) |
| D07 | 比较 Web、移动端、API 的邮箱规范化、验证和合并规则；用受控邮箱与合成私有资源核对账号 ID 和资源继承，区分合法合并与未经验证的继承。 | [业务建模](../business-modeling.md) |
| D19 | GraphQL 按 resolver、字段和 mutation 覆盖；与等价 REST 入口比较注册、验证、恢复及对象权限。schema 可见性不能代替真实数据或状态证据。 | [GraphQL](../by-type/graphql.md) |
| D20 | 将积分、优惠、订单和支付 token 变体还原为账本约束。跟踪创建、取消、回滚和履约的终态，验证是否实际少付多得，而非只看界面价格。 | [业务逻辑](../by-type/business-logic.md) |
| D21 | 顺序基线后再检查受控竞态窗口，关联操作 ID、余额、核销次数与实际权益；多次成功响应不等于违反一次性或金额守恒约束。 | [竞态](../by-type/race-conditions.md) |

## 浏览器、文件与服务端消费者

| 编号 | 提炼后的检查点 | 技能内落点 |
|---|---|---|
| D08 | 跟随存储字段进入页面、邮件、管理端与设备展示。用唯一无害标记确认写入、持久化、查看角色和渲染上下文；回连、HTML 保留和脚本执行分别归因。 | [XSS](../by-type/xss.md) |
| D09 | 用真实浏览器与两个受控来源确认跨源读取，记录预检、凭据条件和敏感响应。XHR 不是通用预检绕过方式。 | [CORS](../by-type/cors.md) |
| D10 | 先确认服务端消费不同 Content-Type，再验证浏览器能否跨站构造请求、携带身份并造成被禁止的状态变化；代理中的成功不等于 CSRF。 | [CSRF](../by-type/csrf.md) |
| D11 | 实测缓存键与测试资源隔离，用 A 的合成私有标记、B 的独立会话确认跨身份复用。随机 query、HIT 或无痕窗口都不能单独证明隔离或泄露。 | [缓存欺骗](../by-type/cache-deception.md)、[缓存投毒](../by-type/cache-poisoning.md)，复用已有完整方法 |
| D12 | 把 403 变体还原为解析、路由和鉴权假设；核对实际处理器、对象与身份效果，排除公开首页、另一虚拟主机和软错误。 | [WAF 与解析差异](../by-type/waf-bypass.md)、[Host 信任](../by-type/host-header.md)，合并已有方法 |
| D13 | 注入前验证观测渠道和可预测对照，区分应用校验、缓存、错误与实际解释器消费。纠正“7×7 得到 14 即 SSTI”；正确算术同样不自动证明服务端执行。 | [SSTI](../by-type/ssti.md)、[SQL 注入](../by-type/sql-injection.md)、[XXE](../by-type/xxe.md) |
| D14 | 以一次性标记关联 URL 输入、后台任务和请求消费者，逐跳记录重定向；请求来源 IP 相同或不同都不能单独确定 SSRF。 | [SSRF](../by-type/ssrf.md) |
| D15 | 按实际 API 区分目录枚举、本地文件读取与网络路径访问；用自建文件、目录或受控远端对照，不能把回连升级为任意文件读取。 | [路径与包含](../by-type/lfi-path-traversal.md) |
| D16 | 跟踪上传对象到原件、缩略图、转码件、下载与最终渲染，记录身份、来源域、响应头及清理。上传接受与最终消费者影响分开。 | [文件上传](../by-type/file-upload.md) |
| D17 | 分开判断公开标识、有效秘密和实际权限；从 JS/APK/配置中的脱敏指纹查用途与获准最小能力，不从 AccessKeyId 或桶名推导接管。 | [信息与秘密](../by-type/info-secrets.md)、[云 IAM](../cloud/cloud-iam.md) |
| D18 | 悬空 DNS 先核对供应商资源状态、域验证和绑定条件；错误页只产生候选，不能代替可重新注册或绑定的证据。 | [子域接管](../by-type/subdomain-takeover.md)，复用已有方法 |
| D29 | HTTP 日志没有新请求时检查既有 WebSocket 消息、订阅和存储；逐消息核对身份、对象和终态。postMessage 另查 origin、source、frame 与接收 sink。 | [WebSocket](../by-type/websocket.md)、[DOM 消息](../by-type/dom-messaging.md) |

## 客户端、供应链、AI 与合约

| 编号 | 提炼后的检查点 | 技能内落点 |
|---|---|---|
| D22 | 从 Manifest/链接/桥接入口跟到实际能力，区分普通 App/网页与 ADB、root、调试身份。设备名称等字段继续跟到云端后台消费者。 | [Android](../by-type/mobile-android.md) |
| D23 | 依赖混淆核对 manifest、锁文件、registry 与真实安装来源；CI 事件输入跟到插值位置、触发主体和 job 权限。包名空缺和高权限事件名不能替代消费链。 | [CI/CD 与供应链](../by-type/cicd-supply-chain.md) |
| D24 | 关联模型输入、真实工具日志、数据归属与副作用，确认跨过了什么边界。模型宣称执行、打印目录或改变语气不代替工具执行和沙箱逃逸。 | [AI 应用](../by-type/ai-application.md)，合并已有方法 |
| D28 | 输入正向追踪与危险消费者反向追踪在具体符号、参数和转换处汇合；保存鉴权、净化及部署关联，未接通的边仍是缺口。 | [源码审计](../source-audit.md) |
| D30 | 固定二进制哈希、架构、运行条件与攻击身份，缩减到稳定输入，结合栈/诊断证据判断长度、整数、生命周期或共享状态错误；崩溃与控制流影响分开。 | [PC 客户端：原生解析器](../by-type/desktop-client.md) |
| D31 | 固定链、部署、代码与代理实现、调用者及初始资产状态；在获准隔离环境核对权限路径、回调可达性和资产不变量。缺 modifier、外部调用或静态告警都需进一步证明。 | [智能合约](../by-type/smart-contract.md)，新增专题 |

## 推理与交付

| 编号 | 提炼后的检查点 | 技能内落点 |
|---|---|---|
| D25 | 报告连接前提、规则、实际结果与影响。修复复测绑定版本和修复事实；奖金、声望或 resolved 标签不能补齐平台时间线，也不能自动推翻历史重复判定。 | [报告](../reporting.md) |
| D26 | 共享鉴权函数、对象键、解析器或消费者只支持迁移假设；组合链逐边证明前一环输出满足后一环的身份、输入、网络和时序前提。已有成熟结果及时交付。 | [专家式推理](../expert-reasoning.md) |

## 全量逐篇补充

首轮代表性提炼后，继续按完整本地正文逐批复核，包含非通用图片替代文字与图片区补充说明。逐篇处理证据见 [当前进度](../../evals/post-distillation/status.json) 和 [复核记录](../../evals/post-distillation/reviews.jsonl)；这些是审计材料，日常使用知识无需读取它们。未完成部分继续保留，不将机器解析计入语义完成数。

图片内容按 [视觉复核记录](../../evals/post-distillation/media-reviews.jsonl) 独立处理。当前媒体源与早期盘点存在差异，见 [媒体核对](../../evals/post-distillation/media-reconciliation.json)；已缺失的图片及未读内容继续保留缺口，不能按文件大小、头像尺寸或 OCR 结果自动判为无技术内容。早期总量是历史输入口径，不替代当前源核对。

| 补充内容 | 适用检查点 | 落点 |
|---|---|---|
| 响应头与跳转 | 观察 301/302 每一跳的实际响应，分开证明输入反射、新头注入和后续影响 | [CRLF](../by-type/crlf-response-splitting.md) |
| 同名 Cookie | 捕获 Domain/Path、实际顺序及各层选择，不按年龄推断；登录页与 API 入口分开核对保护 | [认证与会话](../by-type/authn-session.md) |
| CSS 与通用载荷误判 | 样式可控、合成值可观察、资源请求和脚本执行分别验证；标签/URL/事件按上下文判断 | [XSS](../by-type/xss.md) |
| 端点引用与描述材料 | 从引用还原有效方法/参数/前置状态，按真实栈补 WADL 等材料，不把空根路径当无 API | [Web/API 发现](../discovery/web-and-api.md) |
| 方法覆盖 | 跟踪传输方法到最终处理器、鉴权与状态；不从覆盖头接受直接推导 PUT/RCE | [API 属性与解析](../by-type/api-property-pollution.md) |
| 邮件与身份 | 认证链接消费、实际 Referer/跳转结果、邮件更新任务所信任的主体分别建模 | [认证](../by-type/authn-session.md)、[业务建模](../business-modeling.md) |
| 标记转换与过滤组合 | Markdown/BBCode、原始文本区和属性上下文跟到实际 DOM；删除与解码先算清中间结果 | [XSS](../by-type/xss.md)、[逐层解析](../by-type/waf-bypass.md) |
| 调试日志与文件回退 | 过滤配置不等于实际日志；随机文件名同内容需排除回退/缓存/路径选择差异 | [信息暴露](../by-type/info-secrets.md)、[文件读取](../by-type/lfi-path-traversal.md) |
| 权限转授 | 管理 B 不自动允许给别人授予 A 的权限，核对发起者、对象范围、可授动作和接收者真实能力 | [访问控制](../by-type/idor-access-control.md) |
| 跨服务失效 | 删除/禁用后逐服务核对旧会话的真实能力、账号关系和失效策略 | [认证与会话](../by-type/authn-session.md) |
| URL 实际主机 | userinfo、解码及规范化逐层核对最终解析结果，允许域字符串不代替主机绑定 | [开放跳转](../by-type/open-redirect.md) |
| 替代表示的权限 | 同一对象的 feed/格式/版本按实际入口比较身份与合成私密标记 | [访问控制](../by-type/idor-access-control.md) |
| 页面与缓存状态 | 提示状态改变可能形成新消费者；304 与缓存正文分开观察，先建立有效响应基线 | [Web/API 发现](../discovery/web-and-api.md) |
| 持久配置与临时文件 | 配置保存后的持续失败、上传搬运前的访问窗口分别以真实状态和恢复/清理结果判定 | [业务状态](../by-type/business-logic.md)、[文件上传](../by-type/file-upload.md) |
| 自动续期与恢复分支 | 固定旧凭据排除自动重登；声明的 Referer/路径不代替服务端流程状态 | [认证与会话](../by-type/authn-session.md) |
| 普通字段进入日志 | 用合成标记检查实际记录和读者，秘密可能误填普通字段但不能据可能性宣称已泄露 | [信息暴露](../by-type/info-secrets.md) |
| MIME、请求缩减与改密入口 | 按真实消费者检查.js响应；缩减请求仍核对身份/终态；资料页改密独立于恢复流程 | [XSS](../by-type/xss.md)、[实验设计](../experiment-design.md)、[认证](../by-type/authn-session.md) |
| 关联资产与失效外部引用 | Analytics/历史路径只补关系；按链接、图片、frame、script判断外部资源控制的实际能力 | [被动发现](../discovery/passive-and-services.md)、[引用接管](../by-type/subdomain-takeover.md) |
| 跳转消费者与中间正文 | fragment跟客户端导航；3xx原始body按每跳身份和受众判定，最终登录页不补前一跳结论 | [开放跳转](../by-type/open-redirect.md)、[信息暴露](../by-type/info-secrets.md) |
| 请求行、Cookie与头检测 | 保存request-target/Host及最终处理器；异常Cookie明确设置主体与恢复；正则匹配不代替真实头边界 | [逐层解析](../by-type/waf-bypass.md)、[会话](../by-type/authn-session.md)、[CRLF](../by-type/crlf-response-splitting.md) |
| 技术图片中的协议与查询 | REST/SOAP同能力对照MFA；动态SOQL跟实际变量与查询，保留教学代码的不一致 | [认证](../by-type/authn-session.md)、[查询输入](../by-type/sql-injection.md) |
| 迟到回调与日志证明 | 回调绑定写入、任务、查看者及版本；无害日志函数不决定是否持久化 | [XSS](../by-type/xss.md) |
| 结算分量与查询成本 | 金额各分量独立核对终态；范围参数用离线或隔离证据分析成本边界 | [业务逻辑](../by-type/business-logic.md) |
| Ruby 方法与版本 | 跟实际接收者、方法及输入消费分支，不从 Rails 指纹推断进程执行 | [命令执行](../by-type/cmd-injection-rce.md) |
| APK 字符串视图 | 字符串命中仅产候选；无命中保留压缩、编译、编码和动态构造的缺口 | [Android](../by-type/mobile-android.md) |
| 地域差异与密码标记 | 网络差异保留身份和缓存对照；密码字段回调跟日志消费者，不推断数据库明文 | [实验设计](../experiment-design.md)、[秘密信息](../by-type/info-secrets.md) |
| 对象别名与凭据角色 | 同一受控对象逐引用分支核对授权；凭据用途由实际身份决定 | [访问控制](../by-type/idor-access-control.md) |
| 敏感字段的替代写入 | 专用改密和资料更新分别核对字段、主体、重新认证与终态；CSRF 另证 | [属性授权](../by-type/api-property-pollution.md)、[CSRF](../by-type/csrf.md) |
| 搜索模式与查询结构 | 通配符扩大结果、对象权限与 SQL 结构注入分别判定 | [SQL 查询](../by-type/sql-injection.md) |
| 观察器与回调通道 | 日志挂接/过滤/版本与受控地址先核对；空日志和失效回调不算目标阴性 | [发现记录](../discovery/records-and-incremental.md)、[实验设计](../experiment-design.md) |
| 共享值放行分支 | 追踪设置主体、部署和规则顺序；公开常量不等于全局 WAF 开关 | [WAF](../by-type/waf-bypass.md) |
| 多消费者与组合输入 | JSON 字段、客户端模板和多反射字段跟到真实编译/渲染；区分客户端与服务端执行 | [XSS](../by-type/xss.md) |
| GET 正文与本地地址 | GET body 按实际网关/框架选值；localhost 按解析与连接主体归因 | [API 解析](../by-type/api-property-pollution.md)、[SSRF](../by-type/ssrf.md) |
| DNS 与注释截图 | 完整 DNS 应答替代行数阈值；注释凭据不证明有效管理员身份 | [被动发现](../discovery/passive-and-services.md)、[秘密信息](../by-type/info-secrets.md) |
| 第三方错误的归属 | 本应用、上游响应和外发请求字段分别追踪，用受控标记核对敏感性 | [信息暴露](../by-type/info-secrets.md) |
| 历史技巧的版本条件 | PHAR 自动恢复变更与实际调用分开；__schema 属于 introspection | [反序列化](../by-type/deserialization-rce.md)、[GraphQL](../by-type/graphql.md) |
| 代入身份与离线 bundle | 代入用户的配置影响保留恢复边界；脚本格式化不证明完整代码恢复 | [业务状态](../by-type/business-logic.md)、[Android](../by-type/mobile-android.md) |
| CSRF 图与告警标签 | 校验存在、Medium/Firm 或弹窗不补实际浏览器/身份/消费者证据 | [CSRF](../by-type/csrf.md)、[验证](../verification.md) |
| 参数名与计数主体 | 编码后的键、规范化账号、代理信任链和真实计数键分别追踪 | [逐层解析](../by-type/waf-bypass.md)、[认证](../by-type/authn-session.md) |
| 设备激活与本地PIN | 激活码绑定账号/设备/确认者；root调试修改本地状态不代替普通身份能力 | [认证](../by-type/authn-session.md)、[Android](../by-type/mobile-android.md) |
| JSONP与脚本外读 | 字段名与真实脚本表示分开，受控外站须实际取得合成私密标记 | [XSSI/JSONP](../by-type/xssi-jsonp.md) |
| 属性可写与身份保证 | schema mutable、客户端写权限、用户API与IAM管理员身份分别核对 | [属性授权](../by-type/api-property-pollution.md) |
| 邮箱变更与撤回副本 | 验证标志绑定实际地址；删除范围涵盖哪些引用/缓存由产品规则决定 | [认证](../by-type/authn-session.md)、[业务状态](../by-type/business-logic.md) |
| ASN与中继分层 | 路由保留前缀/地址族；客户端到中继和中继到peer分别核对 | [被动发现](../discovery/passive-and-services.md)、[请求边界](../by-type/ssrf.md) |
| 授权管理与文档成员 | 角色管理核对可授上限；Office上传跟具体包成员和XML消费者 | [访问控制](../by-type/idor-access-control.md)、[XXE](../by-type/xxe.md) |
| 未验证预注册与合并 | 同邮箱联邦合并后检查旧未验证凭据的实际能力，合法合并作反例 | [业务建模](../business-modeling.md)、[OAuth](../by-type/oauth-oidc.md) |
| 模板链与流水线前提 | 固定运行时类型/方法；发现工具保存每阶段输入、输出与完成状态 | [SSTI](../by-type/ssti.md)、[发现记录](../discovery/records-and-incremental.md) |
| 挑战与秘密候选 | DOM值辨明标识/答案与真实放行；字段名正则不证明秘密已提取 | [认证](../by-type/authn-session.md)、[信息暴露](../by-type/info-secrets.md) |
| 旧确认与MFA配置 | 变更版本绑定旧邮箱令牌；未完成挑战会话能否激活新验证器另证 | [认证](../by-type/authn-session.md) |
| 租户注册与邀请密码 | 注册/邀请绑定允许租户和可授能力，新身份初始化与旧全局凭据更新分开 | [访问控制](../by-type/idor-access-control.md)、[认证](../by-type/authn-session.md) |
| 参数集合与浏览器头 | 比较被验证/消费对象集合；referrer配置跟到实际Referer与有效策略 | [API解析](../by-type/api-property-pollution.md)、[逐层解析](../by-type/waf-bypass.md) |
| 读取、删除与执行 | ZIP包装跟最终文件API；仅删除能力不推执行，Docker概况不推容器或宿主控制 | [文件读取](../by-type/lfi-path-traversal.md)、[对象恢复](../by-type/deserialization-rce.md)、[容器](../cloud/container-k8s-security.md) |
| 正则、TAB与协议标识 | 固定正则修饰符/实体码点/URL规范化；JOSE注册none为小写 | [XSS](../by-type/xss.md)、[JWT](../by-type/jwt.md) |
| 回连、格式化与会话固定 | 接收400与收到标记分开；格式化保留原文件；固定攻击需登录后真实能力 | [XXE](../by-type/xxe.md)、[客户端材料](../discovery/client-and-cloud.md)、[认证](../by-type/authn-session.md) |
| 隐式元数据消费者 | 图片元数据跟实际提取/XML任务；DTD、取址和云权限逐边验证 | [XXE](../by-type/xxe.md)、[SSRF](../by-type/ssrf.md) |
| 构建/监控产物 | Jenkinsfile凭据引用与秘密分开；堆转储只以隔离样例/最小标记核对 | [信息暴露](../by-type/info-secrets.md) |
| 开关与支付终态 | 改开关响应只显UI；卡格式通过与网关、订单、履约分别核对 | [Web采集](../discovery/web-and-api.md)、[业务逻辑](../by-type/business-logic.md) |
| 浏览器取址缓解 | Dangling markup原始字符、元素、版本和最终请求分别记录 | [浏览器输入](../by-type/xss.md) |
| 二次解释与会话循环 | HTML/URL编码分层；XML声明/字节/解码分层；回调循环跟真实Cookie与恢复 | [属性污染](../by-type/api-property-pollution.md)、[XXE](../by-type/xxe.md)、[OAuth](../by-type/oauth-oidc.md) |
| 响应阻断与请求效果 | 嵌入错误与CSRF终态分开；端口规范化保留原表示 | [CSRF](../by-type/csrf.md)、[点击劫持](../by-type/clickjacking.md)、[发现记录](../discovery/records-and-incremental.md) |
| 图片中的能力宣称 | 连接串异常不补因果/凭据权限；multipart字段、文件名与字节分开 | [信息暴露](../by-type/info-secrets.md)、[CSRF](../by-type/csrf.md) |
| 令牌、范围与二进制表示 | 撤销键和已验证对象一致；平台配置核对当前原文；strings仅候选 | [JWT](../by-type/jwt.md)、[范围](../scope-and-rules.md)、[信息暴露](../by-type/info-secrets.md) |

| 确认令牌消费对象 | 签发账号/用途与消费会话及最终绑定对象分别核对 | [认证](../by-type/authn-session.md) |
| AJAX头与异常文件 | 自定义头跟真实预检；损坏样本跟处理任务和恢复，不从工具响应补能力 | [CSRF](../by-type/csrf.md)、[上传](../by-type/file-upload.md) |
| 地址和事件候选 | ::与::1分开；window属性存在不保证元素处理器或事件执行 | [请求边界](../by-type/ssrf.md)、[XSS](../by-type/xss.md) |
| SVG外部引用 | 消费模式与取址主体另证；回连IP不证明真实访问者身份 | [文档处理](../by-type/document-rendering.md) |

| TeX与输出消费者 | 编译读入、排版、PDF链接和阅读器脚本分别核对，宏命令文字不补能力 | [文档处理](../by-type/document-rendering.md) |
| 重装与远程撤销 | 系统恢复/新凭据/本地缓存和原服务器会话分别对照 | [Android](../by-type/mobile-android.md)、[认证](../by-type/authn-session.md) |
| 内联script的两层解析 | HTML结束标签与JS引号分别分析；源码截图不证明执行 | [XSS](../by-type/xss.md) |

| 代理改写与历史客户端 | 规则前后请求/身份保留；旧APK线索跟当前后端契约 | [发现记录](../discovery/records-and-incremental.md)、[Android](../by-type/mobile-android.md) |
| 多处URL消费与短地址 | 每个href/跳转落点分别核对；IPv4部件按真实解析库规范化 | [跳转](../by-type/open-redirect.md)、[SSRF](../by-type/ssrf.md) |
| 标识、身份与订单 | 公共ID不是身份保证；允许公开流程与私人账号能力分开 | [认证](../by-type/authn-session.md)、[访问控制](../by-type/idor-access-control.md) |

| 文件名与长连接 | 内容检查不代替元数据编码；Cookie到期不等于连接撤销 | [上传](../by-type/file-upload.md)、[WebSocket](../by-type/websocket.md) |
| 片段与算法绑定 | 下游URL按解码/拼接/真实请求判断；TLS公钥不自动是JWT验签键 | [SSRF](../by-type/ssrf.md)、[JWT](../by-type/jwt.md) |

| 邮箱语法与代理直通 | RFC/注册/输出各自核对；直通不是出站阻断或已观测正文 | [XSS](../by-type/xss.md)、[发现记录](../discovery/records-and-incremental.md) |
| 数量与员工资格 | 计量精度跟账本/履约；身份声明跟资格验证和权益授权 | [业务逻辑](../by-type/business-logic.md) |
| 删除再注册与字符串比较 | 新身份对象引用跟删除承诺；SQL大小写按类型/排序规则核对 | [认证](../by-type/authn-session.md)、[SQL](../by-type/sql-injection.md) |
| 脚本请求与软件制品 | no-check是请求头；包成员公开性和令牌用途分别核对 | [CSRF](../by-type/csrf.md)、[信息暴露](../by-type/info-secrets.md) |

| 临时凭据与跨站接收器 | 恢复令牌按接口能力核对；回调依赖恢复与私密数据外读分别证明 | [认证](../by-type/authn-session.md)、[XSSI](../by-type/xssi-jsonp.md) |
| 本地页面与枚举差集 | 本机显示不证明远程绑定；差集保留本次未观察到而非删除 | [接管](../by-type/subdomain-takeover.md)、[增量](../discovery/records-and-incremental.md) |
| 邮件、错误页与物流 | 头值消费、跨租户缓存和下游订单授权逐边核对 | [Host](../by-type/host-header.md)、[访问控制](../by-type/idor-access-control.md) |

| 自建页面与过滤缺口 | data脚本需目标投递/来源；放宽过滤不补此前未保存响应 | [XSS](../by-type/xss.md)、[定向Fuzzing](../targeted-fuzzing.md) |
| 存储路由与会话诊断 | SPA片段跟真实请求；路径/列表/凭据接受分别证明 | [客户端](../discovery/client-and-cloud.md)、[信息暴露](../by-type/info-secrets.md) |
| 订阅、链接与对象标识 | 规范化跟队列；提供方/本地链接绑定；高熵ID不代替跨站保证 | [业务](../by-type/business-logic.md)、[OAuth](../by-type/oauth-oidc.md)、[CSRF](../by-type/csrf.md) |

| 嵌入来源与属性顺序 | 外站弹窗与目标执行分开；重复type按真实分词/DOM核对 | [XSS](../by-type/xss.md) |
| 验证令牌与云主体 | 响应取得条件/用途跟收信保证；控制台身份跟单项能力 | [认证](../by-type/authn-session.md)、[云权限](../cloud/cloud-misconfiguration.md) |
| 长度口径与输入配置 | 原始头/解码正文/截断分开；curl配置不是裸URL列表 | [发现记录](../discovery/records-and-incremental.md)、[服务发现](../discovery/passive-and-services.md) |

| 邮件策略与投递角色 | 适用DMARC记录/实际处置另核；回连IP、To和From各自归因 | [邮件关系](../discovery/passive-and-services.md)、[业务](../by-type/business-logic.md) |
| 替换规则与导出授权 | ID变化限制单一动作；查询主体/任务/产物读者逐边核对 | [实验](../experiment-design.md)、[文档导出](../by-type/document-rendering.md) |
| 操作标签与安装状态 | query标签不保证无副作用；向导页面不证明账号创建 | [GraphQL](../by-type/graphql.md)、[认证](../by-type/authn-session.md) |

| 名称匹配与动态跨源参数 | [专题](../by-type/cors.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 发布归档与端点正则的覆盖 | [专题](../discovery/client-and-cloud.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 局部缓解与历史材料 | [专题](../source-audit.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 云搜索密钥的权限与数据范围 | [专题](../by-type/info-secrets.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| PHP禁用函数配置的观察边界 | [专题](../by-type/cmd-injection-rce.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 同邮箱重复注册与凭据更新 | [专题](../by-type/authn-session.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 创建用户与更新角色的独立授权 | [专题](../by-type/idor-access-control.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| XML文本与最终HTML消费者 | [专题](../by-type/xss.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 运算语义与工具任务差异 | [专题](../by-type/sql-injection.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 已引用接口的版本候选 | [专题](../discovery/web-and-api.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |
| 域名输入、跳转与结果归属 | [专题](../discovery/records-and-incremental.md) | 局部观察、真实消费者与反例；不把来源宣称补为已验证漏洞 |

| 跨站检索与错误事件 | [XS-Leaks](../by-type/xs-leaks.md) | 服务端四格对照与外源可观察通道分别证，不能由500/200直接推私密搜索成立 |
| MFA开启前签发的恢复能力 | [专题](../by-type/authn-session.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 双提交值相等与会话绑定 | [专题](../by-type/csrf.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| state全局存在与发起会话归属 | [专题](../by-type/oauth-oidc.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 上传声明与下载响应嗅探 | [专题](../by-type/file-upload.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 嵌入API与响应保密性 | [专题](../by-type/clickjacking.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 空白脚本与编辑器副本 | [专题](../by-type/info-secrets.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 邮件传输解码与链接消费 | [专题](../discovery/passive-and-services.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 图片脱敏与模型准确率 | [专题](../reporting.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 表单与CSV导入的共同数据终点 | [专题](../by-type/xss.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| Cognito标识、临时身份与资源权限 | [专题](../cloud/cloud-misconfiguration.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |
| 端口复查的比较条件 | [专题](../discovery/records-and-incremental.md) | 真实消费者、状态与对照；历史截图不是当前目标执行证据 |

| 主机路径配对与内容去重 | [专题](../discovery/records-and-incremental.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |
| 服务检测与脚本选择 | [专题](../discovery/passive-and-services.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |
| 归档格式与被当成程序执行 | [专题](../by-type/file-upload.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |
| 缓存层的ESI消费者 | [专题](../by-type/ssrf.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |
| 可见第二段文本与实际消息边界 | [专题](../by-type/crlf-response-splitting.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |
| 表示后缀与认证字段暴露 | [专题](../by-type/authn-session.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |
| CSP声明与第三方资源候选 | [专题](../discovery/client-and-cloud.md) | 消费者和原始证据分别核对，截图宣称不补当前漏洞成立 |

| 声明的组织邮箱与已验证资格 | [专题](../by-type/authn-session.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| CSV字段到电子表格公式 | [专题](../by-type/document-rendering.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| CRLF注入与浏览器Origin来源 | [专题](../by-type/cors.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| 长输入异常与原生内存诊断 | [专题](../targeted-fuzzing.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| shell别名的输入边界 | [专题](../discovery/records-and-incremental.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| 路径列表中的不同消费者 | [专题](../by-type/lfi-path-traversal.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| 可选调用与已具备的脚本上下文 | [专题](../by-type/xss.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |
| 主机标签与路由大小写候选 | [专题](../discovery/web-and-api.md) | 真实身份/消费者/语法与历史建议分开，记录反例和缺口 |

| 主机原值与证书记录的解析 | [专题](../discovery/records-and-incremental.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 保存响应与文件数量的覆盖口径 | [专题](../discovery/records-and-incremental.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 包含关键字的正则与实际范围 | [专题](../scope-and-rules.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 文档截图与图片对象的预期读者 | [专题](../by-type/info-secrets.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 指标端点与配置字段名称 | [专题](../by-type/info-secrets.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 文件类型到处理消费者的分支 | [专题](../by-type/file-upload.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 父域Cookie与浏览器存储的不同边界 | [专题](../discovery/client-and-cloud.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 多个参数恢复到同一个HTML属性 | [专题](../by-type/xss.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |
| 扫描器时间差与重放失效 | [专题](../experiment-design.md) | 原始输入、实际消费者与观察口径分别核对，候选不补授权或漏洞回执 |

| 条件分支中的客户端导航 | [专题](../by-type/open-redirect.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| HTTP方法与服务器文件的区别 | [专题](../source-audit.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 密码恢复后的身份保证 | [专题](../by-type/authn-session.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 动作归属与不可否认性 | [专题](../by-type/business-logic.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 支付金额与商品数量的权威绑定 | [专题](../by-type/business-logic.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 替代入口与多个后端的差异 | [专题](../experiment-design.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 第三方发现API的字段与分页 | [专题](../discovery/records-and-incremental.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| script标签中的JSON与可执行程序 | [专题](../discovery/client-and-cloud.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 动态Function与不同邮件模板 | [专题](../by-type/xss.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |
| 图片相关请求中的数据库错误 | [专题](../by-type/sql-injection.md) | 条件分支、权威终态和覆盖缺口分别保留；缺过程的截图不补执行能力 |

| 花括号展开与真实shell调用 | [命令注入](../by-type/cmd-injection-rce.md) | 实际shell/引号/调用边界与回连信息披露独立核对 |

| 记住设备的凭据与因素代际 | [专题](../by-type/authn-session.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 网关重写与后端授权主体 | [专题](../by-type/idor-access-control.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 运维代登功能的授权边界 | [专题](../by-type/idor-access-control.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 品牌跨后缀与字典解析结果 | [专题](../scope-and-rules.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 展示表格与扫描输出的事实层级 | [专题](../discovery/records-and-incremental.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 相对引用、MIME与robots规则 | [专题](../discovery/records-and-incremental.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 工具恢复结果与当前请求证据 | [专题](../by-type/sql-injection.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| JSON数组、CORS与跨站请求的区别 | [专题](../by-type/xssi-jsonp.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| 迟到回连与授权有效期 | [专题](../by-type/xss.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| Git标记、成员可读与源码恢复 | [专题](../source-audit.md) | 来源表示、当前消费与权限边界分开，静态候选保留缺口 |
| SVG的图片与文档消费者 | [SVG的图片与文档消费者](../by-type/file-upload.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 处理指令样式输入与解析器版本 | [处理指令样式输入与解析器版本](../by-type/xss.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 令牌统计与实际接受条件 | [令牌统计与实际接受条件](../by-type/authn-session.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 改密后的并行会话与撤销策略 | [改密后的并行会话与撤销策略](../by-type/authn-session.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 失败响应之后的业务状态 | [失败响应之后的业务状态](../by-type/idor-access-control.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| HEAD与Origin文本匹配的误报 | [HEAD与Origin文本匹配的误报](../by-type/cors.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 深链导航与WebView能力 | [深链导航与WebView能力](../by-type/mobile-ios.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 从JSON字段猜路由的候选层级 | [从JSON字段猜路由的候选层级](../discovery/web-and-api.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 历史JS候选与本地制品命名 | [历史JS候选与本地制品命名](../discovery/records-and-incremental.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| DNS查询名与真实应答 | [DNS查询名与真实应答](../discovery/passive-and-services.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 请求位置、转发头与消费位置 | [请求位置、转发头与消费位置](../by-type/xss.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 发现通知的覆盖与权限 | [发现通知的覆盖与权限](../discovery/records-and-incremental.md) | 已审正文/配图中的条件与误判，保留未验证边界 |
| 隐藏email字段与账号身份变更 | [专题](../by-type/api-property-pollution.md) | 已审来源的实际消费者、身份与结果分层 |
| PoC编码、分支与执行来源审阅 | [专题](../source-audit.md) | 已审来源的实际消费者、身份与结果分层 |
| Go运行时profile与调试入口 | [专题](../by-type/info-secrets.md) | 已审来源的实际消费者、身份与结果分层 |
| 归档高熵URL与持有者能力 | [专题](../by-type/info-secrets.md) | 已审来源的实际消费者、身份与结果分层 |
| 并发增量写入与内容去重 | [专题](../discovery/records-and-incremental.md) | 已审来源的实际消费者、身份与结果分层 |
| JAR提取、筛选与制品保全 | [专题](../source-audit.md) | 已审来源的实际消费者、身份与结果分层 |
| 代理重放也是额外请求 | [专题](../targeted-fuzzing.md) | 已审来源的实际消费者、身份与结果分层 |
| 通配响应与非403的不同含义 | [专题](../targeted-fuzzing.md) | 已审来源的实际消费者、身份与结果分层 |
| 阶段限额与全局预算 | [专题](../scope-and-rules.md) | 已审来源的实际消费者、身份与结果分层 |
| 登录token、拒绝结果与导航 | [专题](../by-type/authn-session.md) | 已审来源的实际消费者、身份与结果分层 |
| 百分号文本、换行与URL规范化 | [专题](../by-type/xss.md) | 已审来源的实际消费者、身份与结果分层 |
| 移动日志与网络响应的观察通道 | [专题](../discovery/records-and-incremental.md) | 已审来源的实际消费者、身份与结果分层 |
| 转换脚本与展示载荷 | [专题](../by-type/sql-injection.md) | 已审来源的实际消费者、身份与结果分层 |
| jQuery组件版本与实际DOM消费者 | [专题](../by-type/xss.md) | 历史方法的版本、解析与覆盖条件 |
| S3命名空间、Region与名称复用 | [专题](../by-type/subdomain-takeover.md) | 历史方法的版本、解析与覆盖条件 |
| DNS进度、成功应答与分母 | [专题](../discovery/passive-and-services.md) | 历史方法的版本、解析与覆盖条件 |
| 脚本链接、字符串与秘密命中 | [专题](../discovery/records-and-incremental.md) | 历史方法的版本、解析与覆盖条件 |
| 服务变化后的复现材料 | [专题](../reporting.md) | 历史方法的版本、解析与覆盖条件 |
| 模板移植与多步提取契约 | [专题](../source-audit.md) | 历史方法的版本、解析与覆盖条件 |
| 挑战验证与内容解析支线 | [专题](../by-type/authn-session.md) | 历史方法的版本、解析与覆盖条件 |
| URL列表工具与导航副作用 | [专题](../discovery/records-and-incremental.md) | 历史方法的版本、解析与覆盖条件 |
| URL片段、指针事件与二次DOM消费 | [专题](../by-type/xss.md) | 已审材料的解析、身份和覆盖条件 |
| 脚本结束标签与输入转换顺序 | [专题](../by-type/xss.md) | 已审材料的解析、身份和覆盖条件 |
| 归档成员名进入网页目录预览 | [专题](../by-type/file-upload.md) | 已审材料的解析、身份和覆盖条件 |
| Actuator可用性、暴露与操作授权 | [专题](../by-type/info-secrets.md) | 已审材料的解析、身份和覆盖条件 |
| Git索引元数据与文件恢复范围 | [专题](../by-type/info-secrets.md) | 已审材料的解析、身份和覆盖条件 |
| PDF提取结果的消费者与覆盖范围 | [专题](../discovery/web-and-api.md) | 已审材料的解析、身份和覆盖条件 |
| 引号包围的JS路径正则仅生成候选 | [专题](../discovery/web-and-api.md) | 已审材料的解析、身份和覆盖条件 |
| security.txt与私有项目邀请 | [专题](../discovery/web-and-api.md) | 已审材料的解析、身份和覆盖条件 |
| 公开表单的回连与模板执行分开 | [专题](../by-type/ssrf.md) | 已审材料的解析、身份和覆盖条件 |
| 隐藏角色字段与实际能力变化 | [专题](../by-type/api-property-pollution.md) | 已审材料的解析、身份和覆盖条件 |
| 历史URL生成词表时保留丢失维度 | [专题](../discovery/web-and-api.md) | 已审材料的解析、身份和覆盖条件 |
| text/plain表单序列化与JSON字段语义 | [专题](../by-type/csrf.md) | 已审材料的解析、身份和覆盖条件 |
| Web设备挑战与API凭据入口 | [专题](../by-type/authn-session.md) | 已审材料的解析、身份和覆盖条件 |
| 从JS词汇批量生成JSON的语义限制 | [专题](../by-type/api-property-pollution.md) | 已审材料的解析、身份和覆盖条件 |
| 跨项目范围导出与私有项上下文 | [专题](../scope-and-rules.md) | 已审材料的解析、身份和覆盖条件 |
| POST改GET与只读查询的证据边界 | [专题](../by-type/graphql.md) | 已审材料的解析、身份和覆盖条件 |
| 访问键、点击与错误处理链的触发条件 | [专题](../by-type/xss.md) | 已审材料的解析、身份和覆盖条件 |
| 实体、标识符转义与带标签模板 | [专题](../by-type/xss.md) | 已审材料的实际消费者与反例 |
| 运算符钩子与函数字符串的固定下标 | [专题](../by-type/xss.md) | 已审材料的实际消费者与反例 |
| 属性中的反斜杠与自动聚焦前提 | [专题](../by-type/xss.md) | 已审材料的实际消费者与反例 |
| 客户端MFA标志与权威账号策略 | [专题](../by-type/authn-session.md) | 已审材料的实际消费者与反例 |
| 第三方创建身份之后的本地重复注册 | [专题](../by-type/oauth-oidc.md) | 已审材料的实际消费者与反例 |
| 删除确认页的关联字段与副作用 | [专题](../by-type/idor-access-control.md) | 已审材料的实际消费者与反例 |
| 邮箱待验证状态与API key数量不变量 | [专题](../by-type/race-conditions.md) | 已审材料的实际消费者与反例 |
| Jenkins脚本控制台与预期管理权限 | [专题](../by-type/cmd-injection-rce.md) | 已审材料的实际消费者与反例 |
| 可执行注释、版本条件与关键字重组 | [专题](../by-type/sql-injection.md) | 已审材料的实际消费者与反例 |
| 网页截图服务的网络与本地文件输入 | [专题](../by-type/document-rendering.md) | 已审材料的实际消费者与反例 |
| 文件名尾部标点与保存后的解释器 | [专题](../by-type/file-upload.md) | 已审材料的实际消费者与反例 |
| 爬虫展示格式与源脚本关系 | [专题](../discovery/web-and-api.md) | 已审材料的实际消费者与反例 |
| CVE编号绑定产品、组件与补丁 | [专题](../source-audit.md) | 已审材料的实际消费者与反例 |
| Shellshock检测脚本的动作与阴性通道 | [专题](../discovery/passive-and-services.md) | 已审材料的实际消费者与反例 |
| Cookie预览值与服务端身份 | [专题](../by-type/authn-session.md) | 已审材料的主体绑定与实际消费者 |
| 邮箱绑定、确认能力与事后导航 | [专题](../by-type/csrf.md) | 已审材料的主体绑定与实际消费者 |
| 删除操作的重新认证与目标绑定 | [专题](../by-type/idor-access-control.md) | 已审材料的主体绑定与实际消费者 |
| 同一文件名的路径、数据库、页面与命令消费 | [专题](../by-type/file-upload.md) | 已审材料的主体绑定与实际消费者 |
| PHP流过滤与包含执行分开 | [专题](../by-type/lfi-path-traversal.md) | 已审材料的主体绑定与实际消费者 |
| 同一脚本中多个参数的词法关联 | [专题](../by-type/xss.md) | 已审来源的解析、权限与覆盖边界 |
| HTML刷新导航与脚本执行的区别 | [专题](../by-type/open-redirect.md) | 已审来源的解析、权限与覆盖边界 |
| fetch作为标签调用的参数与网络条件 | [专题](../by-type/xss.md) | 已审来源的解析、权限与覆盖边界 |
| S3列举、对象读取与sync的权限 | [专题](../cloud/cloud-misconfiguration.md) | 已审来源的解析、权限与覆盖边界 |
| 探测产品、脚本制品与命令题名 | [专题](../source-audit.md) | 已审来源的解析、权限与覆盖边界 |
| 批量替换参数与表达式匹配的归因 | [专题](../by-type/ssti.md) | 已审来源的解析、权限与覆盖边界 |
| 文档跳转后的分享与修订能力 | [专题](../by-type/info-secrets.md) | 已审来源的解析、权限与覆盖边界 |
| 跨来源日志关联与历史事件编号 | [专题](../discovery/records-and-incremental.md) | 已审来源的解析、权限与覆盖边界 |
| 邮件主题的传输、列表与阅读消费者 | [专题](../by-type/xss.md) | 已审来源的解析、权限与覆盖边界 |
| ffuf结构化结果与有损表格转换 | [专题](../discovery/records-and-incremental.md) | 已审来源的结构、执行和统计条件 |
| AAAA发现与IPv6观察能力 | [专题](../discovery/passive-and-services.md) | 已审来源的结构、执行和统计条件 |
| 原生库strings与端点授权线索 | [专题](../by-type/mobile-android.md) | 已审来源的结构、执行和统计条件 |
| Shell展开所依赖的变量与执行上下文 | [专题](../by-type/cmd-injection-rce.md) | 已审来源的结构、执行和统计条件 |
| 外部实体协议与Expect扩展的条件 | [专题](../by-type/xxe.md) | 已审来源的结构、执行和统计条件 |
| 域名按字段排序与注册域语义 | [专题](../discovery/records-and-incremental.md) | 已审来源的结构、执行和统计条件 |
| Firefox历史词表的来源与分母 | [专题](../discovery/records-and-incremental.md) | 已审来源的结构、执行和统计条件 |
| 动态钩子与应用原有加载能力 | [专题](../by-type/mobile-android.md) | 已审来源的结构、执行和统计条件 |
| URL用户信息与后端认证 | [专题](../by-type/ssrf.md) | 已审来源的结构、执行和统计条件 |

| 请求hd与可信组织身份 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [请求hd与可信组织身份](../by-type/oauth-oidc.md) |
| 邮箱投递别名与本地账号策略 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [邮箱投递别名与本地账号策略](../by-type/authn-session.md) |
| OTP代际与限流解锁是独立状态 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [OTP代际与限流解锁是独立状态](../by-type/authn-session.md) |
| CharSequence携带样式的消费边界 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [CharSequence携带样式的消费边界](../by-type/mobile-android.md) |
| 排队闸门与服务端同时消费 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [排队闸门与服务端同时消费](../by-type/race-conditions.md) |
| exec的对象、生命周期与已授予控制 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [exec的对象、生命周期与已授予控制](../cloud/container-k8s-security.md) |
| 域名层数筛选与量词语义 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [域名层数筛选与量词语义](../discovery/passive-and-services.md) |
| 经代理加入URL列表会产生真实请求 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [经代理加入URL列表会产生真实请求](../discovery/records-and-incremental.md) |
| 多人同步流量的共享受众 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [多人同步流量的共享受众](../discovery/records-and-incremental.md) |
| HTTP404与DNS失败的不同通道 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [HTTP404与DNS失败的不同通道](../by-type/subdomain-takeover.md) |
| 空值相等与浏览器可构造请求 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [空值相等与浏览器可构造请求](../by-type/csrf.md) |
| 删除中间标签可能重新组成语法 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [删除中间标签可能重新组成语法](../by-type/xss.md) |
| JSfuck表示与事件属性的语义 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [JSfuck表示与事件属性的语义](../by-type/xss.md) |
| 代理捕获缺口与更换主机的实验变量 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [代理捕获缺口与更换主机的实验变量](../discovery/records-and-incremental.md) |
| 研究检索的查询集合与覆盖 | 完整保存正文及已实际审阅配图的条件化提炼；未执行来源代码/目标动作 | [研究检索的查询集合与覆盖](../hunting-strategy.md) |

| absolute-form与Host的不同消费者 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [absolute-form与Host的不同消费者](../by-type/host-header.md) |
| 创建入口的自然键与租户归属 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [创建入口的自然键与租户归属](../by-type/idor-access-control.md) |
| 事件参数转字符串与定时器消费者 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [事件参数转字符串与定时器消费者](../by-type/xss.md) |
| 公开API集合与实际泄露边界 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [公开API集合与实际泄露边界](../discovery/web-and-api.md) |
| 表示路由的授权与跨站检查 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [表示路由的授权与跨站检查](../by-type/csrf.md) |
| 保存文本中的file地址与真实文件能力 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [保存文本中的file地址与真实文件能力](../by-type/info-secrets.md) |
| 撤销同意后的待兑换code | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [撤销同意后的待兑换code](../by-type/oauth-oidc.md) |
| 文件名展开与IFS依赖 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [文件名展开与IFS依赖](../by-type/cmd-injection-rce.md) |
| 类型转换异常的独立输出路径 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [类型转换异常的独立输出路径](../by-type/xss.md) |
| Lax的顶层导航与方法条件 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [Lax的顶层导航与方法条件](../by-type/csrf.md) |
| 相邻安全公告与扫描器的实际动作 | 完整保存正文/已审配图的条件化提炼，外原研究与规范另标阅读范围 | [相邻安全公告与扫描器的实际动作](../source-audit.md) |

| NAT Slipstreaming网页/ALG线索 | 浏览器输入→网关协议识别→映射→服务能力，绑定版本/网络和ALG前提 | [SSRF](../by-type/ssrf.md) |
| JFrog匿名访问 | 匿名开关与具体仓库/路径/动作权限分开，公开包作反例 | [云配置](../cloud/cloud-misconfiguration.md) |
| view-source:file包装 | 外内层URL校验、实际文件读取主体和调用者能力 | [PC客户端](../by-type/desktop-client.md)、[LFI](../by-type/lfi-path-traversal.md) |
| Unicode RLO与WAF编码 | 字节/码点与视觉排列分开，各层解码及真实消费者对照 | [WAF](../by-type/waf-bypass.md) |
| 证书警告快捷字串 | 本地覆盖前提、证书错误、HSTS状态和具体实现分开 | [实验设计](../experiment-design.md) |
| Sling/AEM端点选择器 | 实际资源结构、selectors/extension/suffix、路由与仓库ACL | [Web/API发现](../discovery/web-and-api.md) |
| favicon哈希发现 | Base64文本与图像哈希/位置/时间分开，匹配只作关联 | [被动发现](../discovery/passive-and-services.md) |
| sed/awk文件转换 | 输出截断、字段/正则损失和原件/派生映射 | [发现记录](../discovery/records-and-incremental.md) |

| 外部平台断链 | 被引用身份/资源生命周期、官方受众与实际消费者，区别DNS接管 | [Web/API发现](../discovery/web-and-api.md) |
| 网段工具Confidence与IPv6总数 | 评分实现/对象类型/父子重复/地址基数，归属和范围独立 | [被动发现](../discovery/passive-and-services.md) |
| Nmap发现控制与端口范围 | -sL/-sn/-Pn真实网络动作及单端口/范围语法 | [服务发现](../discovery/passive-and-services.md) |
| server-status扩展状态 | 产品handler/ExtendedStatus/表示参数/访问者与实际私密字段 | [信息泄露](../by-type/info-secrets.md) |
| runtime分块映射 | ID/名称/publicPath/hash/版本与正常加载记录，无执行的离线解析 | [客户端发现](../discovery/client-and-cloud.md) |
| SSRF流程图的分级与阴性 | 渠道缺失不推出没有影响，每段能力和动作许可分别核对 | [SSRF](../by-type/ssrf.md) |

| SRI元数据集合与脚本消费 | 历史“让hash解析报错即可绕过SRI”的断言要拆成原始integrity字符串、浏览器解析后支持的元数据集合、实际资源字节和加载消费者。 | [方法条目](../by-type/xss.md) |
| WebDAV工具分发与本地执行 | 把远端工具目录映射为本地盘符，只说明获取/寻址方式；目录可见、程序下载、程序实际运行及获得额外权限是不同能力。 | [方法条目](../by-type/desktop-client.md) |
| 代理库钩子与扫描网络栈 | “proxychains加在masscan前即可从Squid扫描内网”缺少真实网络通道证据。 | [方法条目](../discovery/passive-and-services.md) |
| 邮件域、投递链与连接归因 | 邮箱字段首先经过校验、队列和投递组件，域名的DNS解析不等于应用已经直接连接该域的A记录。 | [方法条目](../by-type/ssrf.md) |
| 邮箱字段与供应操作的错误回显 | 邮箱在前端合法，不代表后续provisioning脚本安全；URL解码、邮箱校验、工具参数组装、shell解释和错误渲染各自核对。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 源码映射中的展示与真实执行 | DevTools显示作者源码/TypeScript路径，不意味着浏览器执行了那份展示文件。 | [方法条目](../discovery/web-and-api.md) |
| URL正则与完整地址边界 | grep提取的匹配片段与完整URL分别保存。 | [方法条目](../discovery/records-and-incremental.md) |
| 结构化条件与计数观察 | CTF图中的flag[$regex]是HTTP键名，是否形成结构化查询条件取决于实际参数解析器和查询构造；不能因名字含regex就认定MongoDB、SQL或当前可注入。 | [方法条目](../by-type/nosql-injection.md) |
| 短链接代码与目标权限 | 短链接代码从数字ID转成字母数字串，仍须实际提供商的字母表、大小写、顺序、长度与生成规则；一个计算示例不证明所有短链均顺序可预测。 | [方法条目](../by-type/info-secrets.md) |
| 跨后缀标签迁移与许可范围 | 已提供材料中，同品牌不同地域/后缀的业务标签可生成离线候选，但逐项保留原主机与新后缀，不以全局替换破坏名称或合并所有权。 | [方法条目](../discovery/records-and-incremental.md) |
| 多位置FUZZ与过滤后的观察 | 同一请求在用户名和密码位置重复FUZZ，只改变同一来源值，不等于测试两维所有组合。 | [方法条目](../targeted-fuzzing.md) |
| 营销链接与共享文件角色 | 正常营销邮件中的云盘链接，可作为已获准材料的资源引用；宣传文档公开读取可以是预期行为，full access题述不证明任意主体可删除或替换内容。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Notebook叙述、参数与数据格式 | Jupyter页中描述multi-cloud/subdomain到Excel的能力，应与实际单元格参数、输出格式和已见截图范围逐项比较。 | [方法条目](../discovery/records-and-incremental.md) |

| 原图变体与图片元数据 | 缩略图、裁切图和原图是不同制品；某变体清除元数据，不证明其他变体也清除。 | [方法条目](../by-type/info-secrets.md) |
| 客户端路径合并与实际请求字节 | 历史工具新增--path-as-is，只说明希望保留URL中的点段。 | [方法条目](../discovery/web-and-api.md) |
| 地址表示、未指定地址与解析边界 | 环回地址候选清单先核语法：IPv6主机与端口边界需要正确括号；历史http://0000::1:80不能直接当有效IPv6URL。 | [方法条目](../by-type/ssrf.md) |
| WordPress pingback的历史修复条件 | XML-RPC入口存在、方法名可见和pingback实际发起越界请求是不同能力。 | [方法条目](../by-type/ssrf.md) |
| RPC方法自省与批量调用 | 书页片段展示system.listMethods响应及system.multicall等名称，只证明所示服务暴露这些方法名；不证明敏感方法可匿名执行，也不证明整本书的方法已覆盖。 | [方法条目](../discovery/web-and-api.md) |
| 短链档案的摄取与完成标志 | 档案搜索截图包含下载、解压/解码、删除临时压缩文件、按关键字查询和输出提示，但未展示结果文件内容。 | [方法条目](../discovery/records-and-incremental.md) |
| 首次启用MFA后的已有会话 | 在浏览器A首次启用MFA后，浏览器B旧会话仍有效，只说明已有会话继续工作；先核对产品对首次启用、因素重置、退出全部设备和敏感操作再认证的不同承诺。 | [方法条目](../by-type/authn-session.md) |
| 数值进制还原与属性调用 | 数值经指定进制转成字符串再索引属性，须先还原常量与真正消费者。 | [方法条目](../by-type/xss.md) |
| 业务语言与有限词表派生 | 词表语言按已有产品界面、路由、文档与命名习惯判断，行政/管理等业务词可形成有限翻译候选，但TLD不是语言证明，同一国家也可能多语。 | [方法条目](../targeted-fuzzing.md) |
| 熵阈值过滤与候选损失 | 词表过滤截图给出输入生成器、较小/较大阈值选项及定长候选例子，没有展示熵实现、输入分布或实际结果。 | [方法条目](../targeted-fuzzing.md) |
| 技巧条目与可检索机制 | 收集title/description/trick三字段有助检索，但示例中“同时请求OTP”并未给出主体绑定、竞态窗口、观察或最终身份，不能当已证实手机验证绕过。 | [方法条目](../expert-reasoning.md) |
| 归档库漏洞与实际处理配置 | 历史Drupal公告相关清单含两个CVE编号，但产品名不足以确定依赖版本及部署条件。 | [方法条目](../by-type/file-upload.md) |

| 单次删除与重组后的语法 | 双斜杠及ononerrorerror等旧例子提示单次/顺序替换可能留下另一段语法，但帖子未保存过滤器实现；不能擅自假定所有重复字符串都能绕过。 | [方法条目](../by-type/xss.md) |
| 未验证注册与删除对象的稳定身份 | 不发确认邮件只说明注册验证步骤缺失；同邮箱创建新空账号，不等于原账号被接管或可删除。 | [方法条目](../by-type/authn-session.md) |
| DOM接收点记录与插桩覆盖 | 历史帖子称Untrusted Types记录所有sink；[作者仓库README](https://github.com/filedescriptor/untrusted-types)实际列出导航、已有Trusted Types页面、特定iframe及worker等限制，不能采用“所有”覆盖结论。 | [方法条目](../by-type/xss.md) |
| User-Agent差异与有效配置 | 同一路径在两个工具中显示401与403，可能来自User-Agent等请求变量；历史叙述未给完整请求/响应，不能由状态确认绕过。 | [方法条目](../discovery/records-and-incremental.md) |
| 数组类型与查询格式错误 | 用户名从字符串变成JSON数组后出现MariaDB ER_PARSE_ERROR/1064，只证明该输入触达某错误路径。 | [方法条目](../by-type/sql-injection.md) |
| noscript与净化后的再次解析 | 文件名中的noscript片段不是适用于所有上传表单的通用XSS。 | [方法条目](../by-type/xss.md) |
| 认证值搜索的观察集合与证明 | 只在代理的响应头/正文中搜索某hash而零命中，不能证明它未在别处取得，也不能证明账号接管。 | [方法条目](../by-type/authn-session.md) |
| 更新前值与审计文本的延迟消费者 | 更新事件可能同时记录FROM旧值与TO新值，下一次更新才让上一版本进入审计模板；“至少更新两次”不是所有功能的必要步骤。 | [方法条目](../by-type/xss.md) |
| U+FFFF、字面转义与标签语法 | 帖子里的\uffff文本、实际U+FFFF码点和传输编码字节分别记录。 | [方法条目](../by-type/waf-bypass.md) |
| 反编译匹配行与真正网络消费者 | APK提取图的file:line:match混合文件路径、SDK/广告库、示例域名、网络候选及/proc等本地资源；每一行不是同等的实际API入口。 | [方法条目](../by-type/mobile-android.md) |
| 定时任务、消息与函数的身份链 | 书页片段展示Scheduler→Pub/Sub→函数及HTTP函数示例，只覆盖可见局部，不能当整本云手册或真实部署结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 爬虫动态渲染与无头浏览器出口 | 动态渲染图将普通用户HTML与crawler User-Agent分支分开，后者由服务器启动无头浏览器再跟随页面/重定向。 | [方法条目](../by-type/ssrf.md) |
| 链接属性的分层语法位置 | a标签变形图列出标签/属性分隔、属性值引号、实体与URL内部多个位置，各层不能共享一份“空白都有效”的结论。 | [方法条目](../by-type/xss.md) |
| href与src抽取的引用类型 | curl加文本替换提取href/src，只得到该响应中匹配的属性文本，可能含相对资源、外站、片段、静态文件或重复项；缺匹配不代表不存在DOM生成/API路径，输出行数也不是全部端点数。 | [方法条目](../discovery/web-and-api.md) |

| 行窗口、文件名与采样分母 | sed -n选取1–100行只是从其实际标准输入打印这一窗口；echo subdomain.txt产生文件名文本，并不读取该文件的前100行。 | [方法条目](../discovery/records-and-incremental.md) |
| 方案引用与价格权益的共同绑定 | price不能改但plan_id能改，只说明引用字段可控；不同计划本来可能有不同合法价格/权益。 | [方法条目](../by-type/business-logic.md) |
| 八进制字符串与动态构造消费者 | 旧片段用八进制转义表示属性名和构造器参数；自写离线整数到字符转换核对三组内容为filter、constructor、alert(1)，未求值来源JavaScript。 | [方法条目](../by-type/xss.md) |
| 路径解析差异与两层认证 | ..%3B图组从nginx NOT_LOGIN到Tomcat页面/Manager自己的401，说明应分别追踪入口代理与后端路由/认证。 | [方法条目](../discovery/web-and-api.md) |
| 随机子标签的阴性与父名称候选 | 随机子标签没有A应答，不能推出父名称存在、更不能证明零误报。 | [方法条目](../discovery/passive-and-services.md) |
| 代理全局替换与反射搜索 | Match and Replace图把匹配请求参数替为脚本，再搜索响应；这是主动改写经过代理的流量，不是单纯检索已有反射。 | [方法条目](../by-type/xss.md) |
| 私有资料的替代表示与状态切换 | 资料页设为private不证明源码、feed/atom与SEO head接口也执行同一读者检查；URL参数返回head信息也不自动是SSRF。 | [方法条目](../by-type/idor-access-control.md) |
| HTTP附带IP与DNS观察集合 | [httpx官方选项](https://docs.projectdiscovery.io/opensource/httpx/usage)将-ip定义为展示主机IP；它不保证与独立DNS查询有相同集合/分母。 | [方法条目](../discovery/records-and-incremental.md) |
| 事件名称列表与真实触发路径 | 二十事件图混合加载/错误、聚焦、键鼠、表单和卸载，还含onMoveOn标签；列表中的名字不是浏览器已注册事件或元素支持的证明。 | [方法条目](../by-type/xss.md) |

| 非ASCII标识符、强制转换与动态函数作用域 | 楔形文字示例改变标识符外观，仍依赖布尔/对象到字符串、固定字符下标、属性拼接、constructor与动态函数消费者。 | [方法条目](../by-type/xss.md) |
| 标签中的斜杠、字符实体与真实词法层 | img/**/src等写法须按HTML tokenizer解释，/**/在标签中不是JavaScript注释；[HTML属性名状态及相关状态](https://html.spec.whatwg.org/multipage/parsing.html#attribute-name-state)把斜杠、等号、空白与普通字符分开处理。 | [方法条目](../by-type/xss.md) |
| 目录与扩展名的两个替换维度 | FUZZ.EXT与两份命名词表是两个替换维度，不等同于-e扩展单个FUZZ。 | [方法条目](../targeted-fuzzing.md) |
| 主动TLS指纹与配置聚类 | [JARM作者说明](https://github.com/salesforce/jarm/blob/master/README.md)区分主动服务端探测与被动JA3/S，并说明十组TLS交互的响应进入指纹（2026-10-09核读相关段落）。 | [方法条目](../discovery/passive-and-services.md) |
| Referer的来源结构与附加利用前提 | target.example.evil.example属于evil.example下的名称，把target字串放在路径/查询也不改变来源；分别核对实际URL解析后的scheme/host/port、真实浏览器Referer策略、缺失头处理与服务端允许来源。 | [方法条目](../by-type/csrf.md) |
| 地区视角与受保护API的条件分支 | 某地区看到API开放而另地区阻断，应分别关联出口/地理判定、DNS/路由、边缘规则、真实登录主体、对象权限与操作终态。 | [方法条目](../discovery/web-and-api.md) |
| 邮件回连、来源IP与源站候选 | 恢复邮件投递至受控地址后出现SMTP连接，不自动证明SSRF或暴露应用源站；邮件出站中继、边缘入口和应用消费者可能是不同组件。 | [方法条目](../discovery/web-and-api.md) |
| 注册路径的标识类型与租户成员关系 | 注册路径把公司UUID换成数字并创建到另一公司，先跟真实路由/类型转换、稳定租户解析、邀请或成员资格校验、新账号归属和最终能力。 | [方法条目](../by-type/idor-access-control.md) |
| 静态脚本、SSO入口与另一个API消费者 | 根路径403、应用路径跳SSO和main.js可读可能同时成立；脚本中的IP/端口/API key只是线索。 | [方法条目](../by-type/info-secrets.md) |
| PDF对象边界与脚本和表单动作 | PDF注入图应沿生成库的字符串/annotation URI、括号/反斜杠转义、对象边界、产物与具体阅读器消费者追踪。 | [方法条目](../by-type/document-rendering.md) |
| 插件声明版本与实际部署制品 | WordPress插件readme的Stable Tag可用作源码候选线索，不能独立证明生产正在运行该版本：陈旧readme、自定义补丁、不同部署目录/包与禁用组件均可能造成差异。 | [方法条目](../source-audit.md) |
| 本地枚举的权限位、所有者与扫描窗口 | 文件枚举图混合权限位查找、可执行文件、时间文字筛选、strings/file和下载执行未知脚本；这些输出分别描述元数据/候选，不直接证明root执行。 | [方法条目](../source-audit.md) |
| 邮件与日志的落盘位置和包含消费者 | 邮件内容可能落到mail spool或应用日志时，先记录实际接收/转义、存储文件、写入身份、可读范围及读取或include消费者。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 上传控件类型与服务端取址契约 | 把HTML input的type=file改为url，只改变客户端控件/序列化候选，后端可能仍期待multipart文件、忽略字串或拒绝它。 | [方法条目](../by-type/ssrf.md) |
| 恢复入口的编码、方言与时间对照 | 恢复入口的email类字段也须跟输入→解码→实际驱动/查询构造；%2b到加号的层次、排版弯引号、SQL类型/上下文与数据库方言分别保留。 | [方法条目](../by-type/sql-injection.md) |

| 取消资格、未付款订单与补偿账本 | 取消按钮禁用只是客户端状态；沿订单创建、付款方式、实付金额、取消资格、取消处理器、补偿规则和到账权益追踪。 | [方法条目](../by-type/business-logic.md) |
| 转账符号与成对账本守恒 | 接受负转账并让一侧余额增加，先识别金额类型、货币精度、合法退款或冲正状态、扣款与收款分录及可用余额。 | [方法条目](../by-type/business-logic.md) |
| Firebase产品、资源与规则分别绑定 | Realtime Database、Firestore和Cloud Storage须分别记录产品、项目、资源、实际路径、请求主体及操作规则。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 输入顶级域与递归来源过滤 | company.com和company.org是两个独立输入候选，不能代表公司的全部域名或全部范围。 | [方法条目](../discovery/passive-and-services.md) |
| 扫描器加速声明的相同工作量对照 | 两个版本耗时降低，需同时比较相同输入、目标集合、配置、并发、网络/缓存、重试、实际请求数、错误和输出集合。 | [方法条目](../experiment-design.md) |
| 端口记录降维与后续脚本动作 | 端口扫描结果抽出IP再sort唯一化会丢失IP—端口—协议关系；后续扫描是否恢复正确端口取决于实际参数，不能从主机数推出已覆盖全部开放服务。 | [方法条目](../discovery/records-and-incremental.md) |
| BROWSABLE类别与实际入口解析 | Manifest含BROWSABLE只给出一个intent类别条件；还须检查action、data的scheme/host/path、exported、权限、真实调用方式与最终URL消费者。 | [方法条目](../by-type/mobile-android.md) |
| 反编译字符串提取与有损排除 | APK解包/反编译文本用URL正则、sed和grep-v品牌词，只生成字符串候选。 | [方法条目](../discovery/client-and-cloud.md) |
| 版权年份与部署补丁状态 | 页脚版权年份是展示内容，可能固定、动态或跨部署复用；旧年份不证明软件过期、无人维护或未打补丁。 | [方法条目](../source-audit.md) |
| 冒号文件名、NTFS流与Web映射 | file.php:.jpg等冒号名字须先确认真实操作系统、文件系统、写入API和路径处理。 | [方法条目](../by-type/file-upload.md) |
| Symfony profiler记录与敏感内容边界 | /_profiler入口、索引、单个token记录和真实收集内容分别核对。 | [方法条目](../by-type/info-secrets.md) |
| Go profiler读取与采样成本分开 | /debug/pprof索引、cmdline、heap等profile、CPU采样和trace不是同一内容能力。 | [方法条目](../by-type/info-secrets.md) |
| 特权恢复路由与可预测初始密码 | 普通/api/u/resetPwd与特权/api/su/resetPwd可能分属不同恢复契约。 | [方法条目](../by-type/authn-session.md) |
| 邮件空白规范化与组织资格 | admin@target被拒而带空白的值返回200，应记录请求原字节、解码、去空白/大小写/地址解析、校验时点、存储值和最终验证地址。 | [方法条目](../by-type/authn-session.md) |
| 界面账号与请求凭据主体 | 两个浏览器界面显示不同账号，若请求携带第一账号JWT，服务端按第一账号访问其资源可能完全符合授权。 | [方法条目](../by-type/idor-access-control.md) |
| 错误分支的回调校验与流程图角色 | 无效scope与修改redirect_uri同时发生时，错误落点改变不能直接归因于scope绕过。 | [方法条目](../by-type/oauth-oidc.md) |
| 反射最小长度与检测盲区 | 反射检测的NAME/VALUE类标记、最小长度和参数名/值位置影响候选集合；URL、body、JSON、XML及属性、multipart属性、cookie须各自匹配实际解析/回显消费者。 | [方法条目](../by-type/xss.md) |
| 邮件中的模板字面量与HTML重解析 | email值含<%后邮件显示缺失，先比较保存值、原始MIME、HTML实体/标签、模板引擎输入和最终阅读器。 | [方法条目](../by-type/ssti.md) |
| 额外等号的查询值与执行映射 | file===xx.php按常见首个等号分隔形式得到键file和值==xx.php，不能未经证据把它当file=xx.php。 | [方法条目](../by-type/file-upload.md) |
| 数值实体后的标识符绑定与事件执行 | &#x101;表示U+0101字符ā，不是分号或JavaScript空白。 | [方法条目](../by-type/xss.md) |

| 扩展导入范围与规则快照 | 扩展显示项目或一键Add to scope，只说明导入/匹配能力；同时核对正式规则来源、刷新时点、登录资格、域名/路径/端口排除、速率单位及实际动作。 | [方法条目](../scope-and-rules.md) |
| Windows进程主令牌与线程模拟身份 | Windows的access token描述进程或线程安全上下文，不是Web Bearer字符串。 | [方法条目](../by-type/desktop-client.md) |
| 文件年龄区间与名称数据库时点 | 图中find -mtime NUM被解释成最近最多NUM天并不准确；[GNU年龄区间说明](https://www.gnu.org/software/findutils/manual/html_node/find_html/Age-Ranges.html)按24小时区间取整，0对应不足24小时，1对应24至48小时，+/-和-daystart另有语义（2026-10-09核读官方索引相关摘录）。 | [方法条目](../source-audit.md) |
| 界面校验、序列化与实际请求字段 | 登录框直接输入引号失败而改请求email后出现SQL错误，可能差在前端校验、序列化/编码、字段是否发送、代理改写或服务端路由；不先认定“只有Burp能触发SQLi”。 | [方法条目](../by-type/sql-injection.md) |
| KYC上传件的下游受众与索引副本 | 上传自己的KYC文档后看到存储域名，再搜索到其他文件，需分别确认应用上传权限、对象/租户绑定、存储访问策略、CDN或签名链接、公开索引时间及预期受众。 | [方法条目](../by-type/info-secrets.md) |
| null来源序列化与真实私密读取 | Origin: null不是名为null的可信网站，也不唯一标识某个本地文件。 | [方法条目](../by-type/cors.md) |
| Git reflog、目录403与对象内容 | /.git目录403和某个子文件200可以并存，分别核对目录索引拒绝、路径规则、真实响应类型/内容和预期受众。 | [方法条目](../by-type/info-secrets.md) |
| 反向连接之前的执行前提与出口策略 | 向服务80端口发送字节、在31337监听与目标主动回连是三段不同动作。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Laravel代理可信来源与可信字段 | 历史图正文称X-Forwarded-For，示例实际使用X-Forwarded-Host，须保留字段差异。 | [方法条目](../by-type/host-header.md) |
| 浏览器脚本与本地主机执行的缺失边 | 评论进入网页并在目标origin执行JavaScript，只证明该浏览器上下文的脚本能力；图中紧接“attacker got reverse shell”仍缺从Web脚本到本地进程执行的桥梁。 | [方法条目](../by-type/xss.md) |
| 脚本声明变量与服务端参数契约 | assetfinder/Gau→curl→var正则提取只产生源码声明名候选，不证明它们是URL参数、API输入或可控sink。 | [方法条目](../discovery/client-and-cloud.md) |
| 流水线中间文件、缺项与清理所有权 | 多工具脚本的中间文件须记录来源、创建者、时点、是否覆盖/追加、退出状态和消费顺序；cat缺项或工具失败不能被最后的anew输出掩盖。 | [方法条目](../discovery/records-and-incremental.md) |
| 方法覆盖的处理顺序与JSON请求可构造性 | POST加_method=PUT时，记录传输方法、应用有效方法、覆盖来源/优先级、路由与CSRF/授权中间件执行顺序。 | [方法条目](../by-type/csrf.md) |
| localhost头值与真实连接和路由 | 把Host批量替换为localhost不会把原TCP连接、TLS SNI或真实客户端IP自动变成本地。 | [方法条目](../by-type/host-header.md) |
| 浏览器密码导出与来源归属 | 仓库中的CSV被描述为浏览器保存密码列表，先识别格式、origin条目、用户名/秘密字段、制品时间、提交者与真实管理入口；文件扩展或域名字串命中不证明它是有效凭据导出或当前仍能登录。 | [方法条目](../by-type/info-secrets.md) |

| 已安装WordPress界面与登录URL生成 | 已安装提示与Log In按钮只说明一个可见界面，不证明找到了隐藏登录地址或已获认证。 | [方法条目](../by-type/authn-session.md) |
| 原始响应、页面源码与回连观察通道 | 界面没有显示结果时，先核对原始响应、HTML源码/嵌入序列化数据及解码层，不能据可见DOM就认定blind SSRF。 | [方法条目](../by-type/ssrf.md) |
| 旧报告关闭状态与当前同缺陷复测 | closed、duplicate、已修复和当前仍可复现是不同记录。 | [方法条目](../reporting.md) |
| 全局代理设置与实际应用网络路径 | ADB修改global http_proxy属于设备状态写入，不是读取流量或授予测试许可。 | [方法条目](../by-type/mobile-android.md) |
| 有效TrustManager与主机名校验分支 | 空checkServerTrusted或异常被吞掉是证书链验证候选，但要先确认该TrustManager被实际连接工厂/网络库使用，而非死代码/调试分支。 | [方法条目](../by-type/mobile-android.md) |
| 只交密码时的主体选择与验证器绑定 | 删除用户名/邮箱后只凭密码返回某个账号，需要追踪主体选择发生在哪一层、匹配记录的稳定ID、口令验证器/盐与KDF、查询顺序及会话签发绑定。 | [方法条目](../by-type/authn-session.md) |
| 图表模糊显示与数据受众阈值 | CSS blur、锁图标和成绩阈值属于显示与产品资格线索，先检查客户端已有数据、实际响应受众、服务端资格校验和产品承诺。 | [方法条目](../by-type/idor-access-control.md) |
| GET403与空POST404的竞争解释 | 来源所称403bypass的截图实际是GET返回403、带Content-Length:0的POST返回404；方法和头同时改变了两个变量。 | [方法条目](../by-type/idor-access-control.md) |
| Apache协议端口虚拟主机与目录索引 | HTTPS域名403变为HTTP/IP目录列表200同时改变协议、端口、主机名/SNI及可能的后端。 | [方法条目](../discovery/web-and-api.md) |
| 历史证书数据集合差与当前新增资产 | 比较三月数据与五月CT查询时，先保存各自来源、查询条件、时间窗口/时间字段、分页完整性、通配符与域名规范化、重复证书去重和失败项。 | [方法条目](../discovery/records-and-incremental.md) |
| 源站Host路由与限流执行面 | 历史xmlrpc/pingback找到源地址之后修改Host的叙述，还缺实际TCP目的地、TLS SNI、代理路由、后端身份和限流执行位置。 | [方法条目](../by-type/host-header.md) |
| 剪贴板接收者、同步与命令字节 | grep输出送到xclip/pbcopy改变了数据接收者；本机复制也可能进入剪贴板历史、同步服务、其他应用或后续粘贴位置。 | [方法条目](../discovery/records-and-incremental.md) |

| 两套API的令牌受众与只读契约 | 开发者API和应用内部API即使属于同一公司，也应分别关联发行者、令牌类型/受众、scope或角色、租户、对象和允许操作。 | [方法条目](../by-type/authn-session.md) |
| 正则模式输入与匹配输入的资源复杂度 | ReDoS候选需关联实际正则、引擎/版本、匹配模式、攻击者可控字符、长度限制/超时、调用线程与共享资源。 | [方法条目](../source-audit.md) |
| 联邦登录缺失邮箱时的本地主体映射 | 第三方身份没有email字段时，区分字段缺失、null、空字符串、权限未授予和未经验证地址；每一层规范化结果都应关联可信issuer/subject和本地稳定账号ID。 | [方法条目](../by-type/oauth-oidc.md) |
| 指针捕获事件与真实触发前提 | gotpointercapture/lostpointercapture不是onclick的同义词；事件属性可写、元素实际捕获/释放指针与脚本在目标来源执行分别记录。 | [方法条目](../by-type/xss.md) |
| 文档编辑邀请令牌与搜索索引受众 | 邀请他人编辑文档的URL可能是受保护能力，也可能是公开分享或仅邀请标识。 | [方法条目](../by-type/info-secrets.md) |
| Jira分享仪表盘、过滤器与问题正文 | 热门/搜索仪表盘、过滤器列表、项目键、用户枚举和问题正文是不同对象及授权契约。 | [方法条目](../by-type/idor-access-control.md) |
| Jira集合图中的Confluence组件归属 | “Unauthenticated JIRA CVEs”图同时列XSS、SSRF、元数据/用户枚举、模板和路径分支，不是单一组件的通用攻击链。 | [方法条目](../source-audit.md) |
| HttpOnly会话值在CSRF字段的第二副本 | HttpOnly限制脚本通过Cookie接口读值，不承诺同一秘密从未出现在HTML、JSON或其他字段。 | [方法条目](../by-type/authn-session.md) |
| 扫描器检测与数据库取证动作分界 | 从历史URL模式筛选到SQLmap检测，再到读取banner/current user/database/hostname是不同阶段和动作。 | [方法条目](../by-type/sql-injection.md) |
| PHP查询返回false与结构注入证据 | 源站IP加Host并关闭TLS校验后出现mysql_fetch_array期望resource却收到boolean，说明消费链得到不符合预期的值；不能仅由这条警告证明输入控制SQL结构或已取到数据。 | [方法条目](../by-type/sql-injection.md) |
| 同源示意图的箭头与浏览器读取 | 协议/主机/有效端口共同决定普通Web URL来源，路径差异本身不改变origin。 | [方法条目](../by-type/cors.md) |
| 认证fuzz的会话来源与角色基线 | 将auth Cookie加入dirsearch/wfuzz/ffuf只改变请求身份，不保证有效会话、正确租户/角色或完整认证覆盖。 | [方法条目](../targeted-fuzzing.md) |

| 尾斜线规范化与授权处理器一致性 | 角色受限令牌访问普通路径被拒、加尾斜线返回200，是路由与授权边界不一致的候选。 | [方法条目](../by-type/idor-access-control.md) |
| 原先self-XSS的条件变化与再次审查 | 旧报告因只有自身输入/自身执行而关闭，后来CSRF保护或受众发生变化，应按当前消费者重新打开分支。 | [方法条目](../by-type/xss.md) |
| Cisco历史扫描结果与Web服务文件系统 | 按组织字符串从Shodan选到Cisco候选，再显示MayBeVuln和OEM路径，仍需关联正式资产范围、当前ASA/FTD版本、AnyConnect/WebVPN配置及真正响应内容。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 认证方法清单的不同抽象层 | Basic是凭据传输方案，Cookie/session涉及会话承载与生命周期，JWT是一种令牌格式，OAuth描述授权委托及协议角色；它们可组合而不是互斥的同层认证选择。 | [方法条目](../by-type/authn-session.md) |
| 限流计时锚点与拒绝后的窗口 | 来源以Forbidden的视频时间加30秒推断下一次允许时间，又用X-Forwarded-Host或X-Client-IP在较早视频时刻收到OTP。 | [方法条目](../by-type/authn-session.md) |
| base元素、相对表单目标与独立CSP指令 | HTML注入能够影响base元素时，先关联有效的首个href、已有文档基址、相对form action、脚本提交方式和最终解析地址。 | [方法条目](../by-type/csrf.md) |
| JS完整路径提取与片段词表的损失 | 从静态JS中提取引号内斜线路径，再按第1到第8层切分、过滤扩展/关键词、写入去重词表，得到的是片段候选；它与完整API路径、完整URL或浏览器实际调用清单不同。 | [方法条目](../discovery/records-and-incremental.md) |
| 媒体解码器的HLS引用与嵌套消费者 | 上传清单把FFmpeg/HLS、SSRF与本地文件泄露放在一起，需要展开实际链路：上传对象→内容识别/转码器→播放列表解析→嵌套资源URL/协议→进程网络与文件权限→输出制品/返回受众。 | [方法条目](../by-type/file-upload.md) |
| Zip Slip与zip包装包含的不同边界 | 来源上传清单把zip包装访问归档成员标成Zip Slip，应纠正为两类消费者：Zip Slip涉及解压时归档成员路径逃出预期目录；zip包装则涉及运行时文件读取/包含如何定位归档和成员。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 批量密码输入与会话续期的计数粒度 | password数组是否被接受，需要分清类型验证、逐元素秘密比较、实际尝试次数和请求/账号/设备/挑战计数。 | [方法条目](../by-type/authn-session.md) |
| Sentry filepath字段到制品消费者 | 事件堆栈中的filepath可能只是显示元数据，也可能被符号解析、源码制品查找、debug renderer或其他任务用来定位资源。 | [方法条目](../by-type/ssrf.md) |
| URL模式去重与不同业务对象保留 | 来源示例将三种page值和三种id值的六条URL缩成两个代表项，属于参数结构归类，不能证明页面、照片或授权上下文等价。 | [方法条目](../discovery/records-and-incremental.md) |
| Spring ALPS与JSON Schema元数据的消费者 | 来源将ALPS拼成APLS，并给出Accept application/schema+json及localhost示例路径。 | [方法条目](../discovery/web-and-api.md) |

| Android堆转储的身份、时点与秘密消费者 | 源图将进程列表中的PID传给am dumpheap，再pull一个hprof文件；只能证明该图所示采集动作和输出文件，未展示其中存在密码、算法密钥或可用凭据。 | [方法条目](../by-type/mobile-android.md) |
| CONNECT隧道目标与上游代理归因 | CONNECT图返回200 Connection established，需要关联研究者配置的上游代理、实际请求接收方、隧道目标及目标回连；不能把自身代理的正常行为记成应用SSRF。 | [方法条目](../by-type/ssrf.md) |
| X-Original-URL与前后端授权目标一致性 | 外部路径被拒、入口根路径加X-Original-URL后200，是不同组件使用不同有效目标的候选。 | [方法条目](../by-type/idor-access-control.md) |
| 联邦个人资料进入另一应用的存储渲染 | 第三方账号的显示名/username进入登录后的应用，属于跨系统数据输入，不能因为来自受信身份提供方就假定字段已适合HTML/属性/脚本语境。 | [方法条目](../by-type/xss.md) |
| 私有线程评论与通知中的读写授权 | 对私有线程可评论和对另一账号项目可查看，是不同对象/动作。 | [方法条目](../by-type/idor-access-control.md) |
| 逐跳Connection字段移除与安全上下文 | hop-by-hop是逐连接控制语义，需画出每个代理收到/移除/新增的字段及后端消费。 | [方法条目](../by-type/request-smuggling.md) |
| 正确OTP对照后的旧会话污染 | 响应修改示例先提交正确OTP取得valid，再提交错误OTP并把invalid改成valid。 | [方法条目](../by-type/authn-session.md) |
| 表达式完成值、导航文档与dump输出 | 来源把可选链findIndex调用dump后拼HTML称作Firefox无需document.write的写DOM方法。 | [方法条目](../by-type/xss.md) |
| 布尔盲注分治的稳定判定与工作量 | 分治加速依赖真实、稳定的真假观察器及可按条件划分的有限候选空间；每次可靠判定将候选区间缩小，和逐值猜测的请求需求不同。 | [方法条目](../by-type/sql-injection.md) |
| 错误响应缓存与CPDoS的共享受众 | CPDoS首段描述通过缓存内容导致资源不可用，但缺少实际触发条件。 | [方法条目](../by-type/cache-poisoning.md) |
| 上传URL抓取与公开热链接的访问者 | 上传清单提到URL取回和IPlogger观察访问者，应区分服务端下载/转码、自身浏览器预览、公开页面保留外链和之后访问者加载，以及安全扫描器取回。 | [方法条目](../by-type/ssrf.md) |
| 禁用2FA动作与后续登录条件 | 禁用2FA的CSRF需关联真实设置动作、浏览器可构造请求、自动会话、CSRF/来源防护、再认证要求、绑定主体与权威配置变化。 | [方法条目](../by-type/csrf.md) |
| 批量SQL错误关键字的未知状态 | 来源流水线替换所有query值、并发请求后grep syntax或mysql，并把没有命中写成Not Vulnerable。 | [方法条目](../discovery/records-and-incremental.md) |

| OTP字段省略的输入强制转换与认证分支 | GraphQL登录去掉错误OTP后“登录成功”的声明，需要区分字段/参数省略、显式null、空字符串、变量缺失与默认值。 | [方法条目](../by-type/graphql.md) |
| 删除字面关键词与传输层空格还原 | 删除javascript字面文本可使包在标签名和事件属性中的文本重新拼成HTML语法；核对删除大小写、次数、递归、转义/解码顺序及最终HTML tokenizer输入，不能只看过滤前字符串。 | [方法条目](../by-type/xss.md) |
| 全局属性枚举下标与with作用域 | 源控制台图中Firefox下标5、Chrome153和Safari5880各自调用弹窗，说明相同数字并无跨浏览器函数身份保证；另一图下标6/7展示不同结果。 | [方法条目](../by-type/xss.md) |
| 二阶查询的独立观察页面与代理改写 | 二阶SQL涉及植入/保存输入与后来检索/报表消费者。 | [方法条目](../by-type/sql-injection.md) |
| 客户端DNS观察与实际应用请求者 | 客户端DNS代理只能提供被观察的名称查询，关联应用/进程身份、查询时点、解析器/缓存、后台进程、记录类型和网络配置。 | [方法条目](../discovery/client-and-cloud.md) |
| 离线重启的应用挑战与服务端因素状态 | 源图叙述断网、强制停止、重启、恢复网络后没有再次显示2FA。 | [方法条目](../by-type/mobile-android.md) |
| 集合差分、人工选择与通知提交点 | 来源四张终端技巧图分别演示stdin减旧集合、xor对称差、交集及方向性差集；新减旧、旧减新与两边独有项含义不同。 | [方法条目](../discovery/records-and-incremental.md) |
| 文本扩展宏的实际命令与配置版本 | espanso的短词扩展可缩短输入，但源图只有空终端/视频预览，未展示:ht定义或展开结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 删除图片的保留契约与可访问副本 | 已删除图片仍可用旧地址读取，应核对当前产品/隐私承诺、删除生效时点、允许保留窗口、软删除/备份、CDN缓存与原始/缩略派生副本。 | [方法条目](../by-type/file-upload.md) |
| 图片元数据的来源、派生制品与隐私受众 | EXIF可能承载拍摄位置等元数据，不能假定每张图都有IP或秘密。 | [方法条目](../by-type/file-upload.md) |
| 空文件名IO错误与对象反序列化消费者 | 空文件名导致java.io栈错误，只能定位某个文件/IO处理路径；java.io包名不证明该入口调用对象反序列化或存在可用gadget链。 | [方法条目](../by-type/deserialization-rce.md) |
| 会话变量复用的写入者与认证读取者 | Session Puzzling/Variable Overloading首段列出可能绕过认证/MFA或提权，但没给具体流程。 | [方法条目](../by-type/authn-session.md) |
| 媒体类型过滤后的解析错误与实体能力 | 源图application/xml返回403、改Content-Type为*/*后400并输出Failed to parse XML。 | [方法条目](../by-type/xxe.md) |
| 改密缺少当前密码与CSRF因素的分别归因 | 改密时同时移除当前密码和CSRF token产生的结果，不能区分重新认证缺失与跨站请求防护缺失。 | [方法条目](../by-type/csrf.md) |

| 百分号主机文本到域名解析的顺序 | 源文用百分号编码的Unicode句号/ASCII域名宣称多个浏览器可打开；需要分开记录原始地址、host提取、百分号到UTF-8字节解码、域名映射、实际目的地及展示文本。 | [方法条目](../by-type/open-redirect.md) |
| 兼容规范化产生路径分隔符的Host-Split候选 | 源文将iOS13Memo链接中的℅转换称NKFD，正确形式名为NFKD。 | [方法条目](../by-type/mobile-ios.md) |
| 图片注释中的程序文本与真正解释器 | exiv2/exiftool将PHP片段置于图片注释，只说明可写入某个元数据位置；JPEG/PNG正常解码不会因此成为PHP执行。 | [方法条目](../by-type/file-upload.md) |
| 文件填充、检查范围与源站完整字节 | 大量换行填充后追加程序片段的声明，需要核对WAF检查字节数/截断与超限策略、传输编码/解压、请求总长度、源站收到内容和真正解释器。 | [方法条目](../by-type/waf-bypass.md) |
| 标准输入路径与可重复读取的文件契约 | /dev/stdin可作为部分工具的输入路径，但是否存在以及程序如何打开/读取依赖当前系统和工具实现。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史Angular文件与当前CSP允许的脚本消费者 | 在历史索引找到旧Angular文件，只形成曾有资源线索；需关联当前可达且实际相同版本的内容、script-src/nonce/hash/strict-dynamic等有效策略、页面上下文及触发的具体库行为。 | [方法条目](../by-type/xss.md) |
| 秘密正则与possible-Creds标签的实际语义 | 来源regex表按前缀/字符类分类，输出图出现大量Twilio标签，另一图possible_Creds却是password输入UI、函数名和字段赋值。 | [方法条目](../by-type/info-secrets.md) |
| GraphQL错误分层与私密内容受众 | 畸形/意外输入的错误可能来自文档语法、schema/变量校验、resolver或下游异常，各自消费与受众不同。 | [方法条目](../by-type/graphql.md) |
| HTTP分类图与具体状态的缓存语义 | HTTP分类图只帮助初步解释状态，200不表示业务授权/终态/全部数据均正确，4xx也不说明请求失败之前没有副作用；3xx不是每种都进行URL跳转。 | [方法条目](../discovery/web-and-api.md) |
| 同页Referer放行与补丁保护的业务对象 | 自设Referer指向被拒页面后规则放行，提示补丁可能依赖客户端可提供的来源文本。 | [方法条目](../by-type/waf-bypass.md) |
| 错误XML中的存储名称与对象权限 | URL末尾%C0导致XML URI中露出bucket名称的声明，需要区分原字节、UTF-8/路径规范化拒绝、错误生成组件、后端存储前缀和当前实际bucket归属。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 盲请求耗时与端口状态推断的观察器 | 公开表单的耗时差可能来自DNS、连接/读取超时、重试、队列、缓存、扫描器或后台任务，不能直接给端口标开放/关闭。 | [方法条目](../by-type/ssrf.md) |
| 无头截图的渲染动作、参数与采集状态 | 无头浏览器截图会加载/渲染目标，可能执行脚本、跟跳转和使用浏览器身份，不能当纯文本读取URL。 | [方法条目](../discovery/records-and-incremental.md) |

| HTTP/0.9请求与客户端接受无头响应 | 源帖把请求行的版本文字改为HTTP/0.9并称200成功，但这不是规范的Simple-Request。 | [方法条目](../discovery/web-and-api.md) |
| JWT结构图的编码、验签者与声明名称 | 三段HS256图只描述一种JWS，不能推广为所有JWT。 | [方法条目](../by-type/jwt.md) |
| Electron可执行文件签名与外部应用归档 | 有效exe签名只覆盖其签名对象，应用启动后实际加载的app.asar、未打包模块、备用目录和更新来源需单独追踪。 | [方法条目](../by-type/desktop-client.md) |
| OpenSSH账号枚举与RCE声明纠正 | 源帖把CVE-2018-15473标成OpenSSH RCE。 | [方法条目](../discovery/passive-and-services.md) |
| CGI头到环境变量再到Bash启动解析 | 旧jarrewrite截图在User-Agent置函数形式字符串，响应出现文件内容与CGI Usage；方法应追到HTTP头映射的环境变量、实际CGI调用、Bash版本/启动函数导入与进程身份，而不是把静态文件名或头反射直接标命令注入。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 邮箱更新碰撞与登录可用性契约 | 两个账号邮箱改成同值后登录报错，先区分产品是否允许多账号共用收件箱、唯一登录键规范化、verified状态、数据库约束与稳定主体选择。 | [方法条目](../by-type/authn-session.md) |
| 双栈地址排序、连接尝试与耗时归因 | telnet图显示先尝试两个IPv6地址、随后IPv4连接，但没有每阶段时长、DNS日志或HTTP结果，不能直接说IPv6导致所有工具卡顿。 | [方法条目](../discovery/records-and-incremental.md) |
| 读取聊天标识与写入聊天消息的链条 | 跨站能读chat sessionId与借此发消息是两个消费者。 | [方法条目](../by-type/cors.md) |
| 编码字符串到计时器或HTML写入消费者 | 源polyglot把\x28/\x29标Unicode，实际是两位十六进制转义；[MDN词法说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#hexadecimal_escape_sequences)将它与\u形式区分。 | [方法条目](../by-type/xss.md) |

| 账号到期、会话有效与项目写入权益 | 账号或套餐到期后仍能创建/编辑项目，先明确到期的是身份、会话还是付费权益，以及读、写、续费、导出各动作的契约。 | [方法条目](../by-type/business-logic.md) |
| JavaScript恢复接口与未加引号的iframe拼接 | Linkfinder列出viewUserInfo及userId，只恢复客户端接口候选，服务端是否按当前主体校验对象仍需独立证据。 | [方法条目](../by-type/xss.md) |
| 下划线主机名的解析层与同源边界 | 带下划线的域名候选和HTTP400截图不能证明SOP被绕过。 | [方法条目](../by-type/host-header.md) |
| 协商诊断表示与连接器异常中的秘密 | Accept的JSON/JavaScript媒体偏好可能使某处理器选择更详细的错误表示，但[RFC9110 §12.5.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-12.5.1)定义的是表示偏好及q权重，不保证一定返回栈、版本或秘密。 | [方法条目](../by-type/info-secrets.md) |
| 转发字段角色与逐跳可信选择 | Host覆盖清单混列X-Forwarded-For、Proto、Host、Server和自定义Override；名称相似不能认定它们都覆盖URL主机。 | [方法条目](../by-type/host-header.md) |
| JavaMelody监控读者与管理动作分离 | 监控页面出现CPU、内存、HTTP/JDBC统计及版本升级横幅，说明当前观察者看到这些内容；浏览器可能已有身份，不能直接称匿名访问，更不能由只读统计断言可删除数据。 | [方法条目](../by-type/info-secrets.md) |
| Pimcore路由导出与JSONP回调的真实信息 | 客户端路由文件暴露后台路径和参数可用于恢复接口，但路径列表不等于后台私密记录或未授权动作。 | [方法条目](../discovery/web-and-api.md) |
| 历史2to3提示与迁移后运行时契约 | 安装2to3再转换脚本的旧提示只能描述部分语法迁移，不证明工具现在可用或转换后语义正确。 | [方法条目](../discovery/records-and-incremental.md) |
| Nmap分片、诱饵与FTP辅助连接的不同条件 | 旧“绕防火墙”命令混用-f、-A、-T1、-sS和--script，连写也可能改变实际参数；慢速不等于绕过，-A包含多种检测动作。 | [方法条目](../discovery/passive-and-services.md) |
| 地图API密钥的平台限制与计费能力 | 移动包中的地图key与网页Referer规则不一定适用同一平台。 | [方法条目](../by-type/info-secrets.md) |
| 地图URL签名端点的委托能力 | 返回含client及signature的Street View URL，只证明签名结果被返回，不说明URL signing secret已泄露，也不证明请求被提供者接受或计费。 | [方法条目](../discovery/web-and-api.md) |

| Druid请求配置与服务端JavaScript执行保证 | Druid sampler图在嵌套transform/filter中加入JavaScript、java.lang.Runtime调用和enabled字段，并展示带外请求/文件样式正文；实际链须绑定同一请求、服务端表达式消费者、运行身份与回连来源。 | [方法条目](../by-type/cmd-injection-rce.md) |
| PHP源码参数提取的词法、引用与数据流 | 针对$_GET的grep/sed串先核对shell引用与正则语法：未正确保护的$可能参与变量展开或正则锚定，混合引号、字符类和多行排版也可能改变模式。 | [方法条目](../discovery/client-and-cloud.md) |
| 临时HTTP服务的文档根与外部读者 | 从home目录启动HTTP服务并开放互联网，会把进程可见文件和服务配置作为新的发布边界；index图列出.bash_history、.ssh、.config、工具配置等只是名称，文件是否可读及真正内容仍需区分。 | [方法条目](../by-type/info-secrets.md) |
| 测试支付响应与生产订单的环境绑定 | 测试卡号通过前端校验或网关返回模拟成功，不能证明真实付款，也不能直接命名缺乏反欺诈。 | [方法条目](../by-type/business-logic.md) |
| 购物篮库存预占的归属、期限与释放 | 加购物篮使全局可售数量减少，可能是正常限时预占，也可能违反库存策略；不付款和金额奖励不足以证明DoS。 | [方法条目](../by-type/business-logic.md) |
| Lync发现链接到NTLM目标信息 | lyncdiscover XML中的root/user/xframe链接及originalDomain是发现元数据；后续NTLM目标信息的NetBIOS domain/computer、DNS domain/computer/tree和build又是另一协议层。 | [方法条目](../discovery/passive-and-services.md) |
| 同一会话字段的流程用途混用 | Cookie认证思维图中的Session Puzzling提示服务端会话字段可能被多个流程复用。 | [方法条目](../by-type/authn-session.md) |
| 带外事件、通知生成与邮件投递分层 | XSS Hunter告警进spam的旧提示涉及观察器可靠性。 | [方法条目](../discovery/records-and-incremental.md) |
| PHP动态可调用表达式与版本语义 | 旧图把system文字拆分/加注释、字符串调用、裸常量和$_GET键都列为可行过滤绕过；每种须先能进入PHP表达式求值，而不是普通模板文字、参数值或仅命令参数。 | [方法条目](../by-type/cmd-injection-rce.md) |

| 图片导入的本地来源到公开派生文件 | 图片导入入口接收picUrl并返回媒体ID，另一列表把ID映射到公开uploads路径，最后响应出现数据库配置文本，是三个需独立绑定的消费阶段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 文本载荷字典的后缀与预览消费者 | 将字典生成器的标准输出重定向为xss.doc只改变名称，不创建有效Word文档。 | [方法条目](../by-type/file-upload.md) |
| SMTP调试接收与真实邮件投递 | 旧命令用smtpd.DebuggingServer监听0.0.0.0:25，并建议Docker发布25端口。 | [方法条目](../discovery/passive-and-services.md) |
| 站内消息副本与邮箱所有权挑战 | 页面要求确认邮箱，而My Messages列出Confirm your email address时，只说明站内有通知记录。 | [方法条目](../by-type/authn-session.md) |
| 评论仓库配置与OAuth应用权限 | Gitalk配置图列clientID/clientSecret/repository/owner/admin，密钥被遮盖；评论仓库和可初始化Issue的名单是应用配置，不能独立证明认证提供商将令牌限制在该仓库。 | [方法条目](../by-type/oauth-oidc.md) |
| 已有执行权限与实例元数据是两条证据链 | 旧帖先假定reverse shell，再给metadata/latest路径；已有RCE、运行环境身份和云资源权限必须分别证明，不由Linux或AWS字样推出EC2/实例角色。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 过长UTF-8字节与页面显示字符 | GlassFish旧正文显示À®等字符，原图请求目标却显示%c0%ae重复路径；页面Unicode显示、原始C0 AE字节及百分号请求目标不是同一表示。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 旧授权类型选择图与当前安全要求 | 旧流程图按machine/user、web/native/browser及first/third party选择Client Credentials、Code、Implicit或Password grant，描述的是历史分类而非当前通用配置建议。 | [方法条目](../by-type/oauth-oidc.md) |

| 抓取后的JSON响应契约与可见性 | 导入功能只展示合法JSON而对无效JSON报错时，拆开URL/目的地校验、实际抓取、响应字节、JSON解析、字段schema和最终展示。 | [方法条目](../by-type/ssrf.md) |
| Lambda调用回执与实际执行消费 | 旧Lambda图把同步描述为主线程A完成再B开始、异步画为事件请求、流处理画为队列拉取。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| S3兼容端点与逐操作身份 | 旧八步清单只有第一条指定HTTP自定义endpoint，后续省略；9000端口及AWS CLI字样不能证明是Amazon S3或任何特定产品。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| UserInfo声明与ID Token的主体绑定 | OIDC简介图把ID Token说成可用access token从UserInfo得到，应纠正消费对象：UserInfo返回用户claims，通常为JSON，协商后也可为签名/加密JWT；JWT外观不使其自动成为ID Token。 | [方法条目](../by-type/oauth-oidc.md) |
| 登录启发式的阴性与真实入口 | haslogin输出对一些网站标NoLogin、对另一些给signin路径，只证明工具的未知启发式在一次输入/页面上未命中。 | [方法条目](../discovery/web-and-api.md) |
| 事件属性名与净化变换的阶段 | 事件属性ASCII大小写、百分号解码和HTML字符引用属于不同阶段。 | [方法条目](../by-type/xss.md) |
| HTTP片段与ZIP成员分隔符 | PHP ZIP包装语法中的#分隔归档与成员，而浏览器HTTP URL里的裸#开启客户端片段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 子域Cookie范围与服务端第二副本 | 接管验证页面用domain最后两个标签设Cookie，再声称能显示HttpOnly值；拆开浏览器允许的Domain、实际Cookie头、服务器反射副本与DOM显示。 | [方法条目](../by-type/authn-session.md) |
| Datadog客户端标识与管理凭据 | 发现DATADOG_CLIENT_TOKEN和DATADOG_APPLICATION_ID字段时，先判断实际SDK与API消费者，不能只因token/key名字便认定敏感凭据。 | [方法条目](../by-type/info-secrets.md) |

| 否定状态的false、null与空数组 | 把banned从false改为null或空数组，不只是变布尔值：字段缺省、JSON null、数组、合法布尔、schema拒绝、默认值及持久化清除是不同分支。 | [方法条目](../by-type/api-property-pollution.md) |
| ASPXAUTH名称与跨应用票据信任 | 另一个站点也使用ASPXAUTH或同一ASP.NET应用，不保证它能签发目标接受的票据。 | [方法条目](../by-type/authn-session.md) |
| Windows UNC与远程URL开关的边界 | Windows文件API可以把UNC路径定位到网络共享；它与http等URL包装不是同一消费者。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 高权限备份对符号链接的定位 | Node靶场拓扑图写直接备份root目录失败、备份指向它的symlink成功，仅提供路径检查与实际打开对象可能不同的线索，未给备份程序实现、有效身份或原始输出。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Windows批处理的解释器与逐行URL契约 | 旧图把amass/waybackurls/findstr/sort与cmd风格for /f、%%s、@echo off、pause混在同一段；先确定实际解释器、命令解析与各工具版本，不能由Windows标题保证所有行在同一shell成立。 | [方法条目](../discovery/records-and-incremental.md) |
| 词表占位符替换后的实际请求 | 内置词表含{KNOWNFILE}或{domain}时，源图建议Intruder Payload Processing的Match/replace。 | [方法条目](../targeted-fuzzing.md) |
| LIKE下划线模式与SQL语法注入分开 | “SQL请求中_像正则.”应限定在实际LIKE模式，不能推广到等号、标识符或所有查询。 | [方法条目](../by-type/sql-injection.md) |
| 日志参数、生成脚本与日志查看器 | console.log接收字符串/值并输出，不会仅因日志里没有显示引号就重新解析其中的脚本。 | [方法条目](../by-type/xss.md) |

| Jira用户悬浮资料与枚举版本校正 | 旧帖把CVE-2020-14181的7.13分支阈值写成7.13.6；[Atlassian官方记录](https://jira.atlassian.com/browse/JRASERVER-71560)明确为7.13.16，另列8.0.0至8.5.7之前、8.6.0至8.12.0之前，并绑定Jira Server/Data Center的ViewUserHover.jspa（2026-10-09核读）。 | [方法条目](../by-type/authn-session.md) |
| 协议方案、TLS入口与认证消费者 | HTTPS超时、改HTTP后200可能表示该端口只提供明文HTTP、TLS终止点不同或协议不匹配，不能直接称“私密开发入口的认证被绕过”。 | [方法条目](../discovery/web-and-api.md) |
| Airflow连接密文、配置密钥与DAG源码 | Airflow连接表中的密码、fernet_key配置、DAG里的硬编码数据库参数和执行日志不是同一种保护范围。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 数据库校验错误与初始化副作用 | 数据库连接的“验证”可能已经进入驱动、连接参数和初始化消费者，后续返回400/SQL语法错误不能证明此前无副作用。 | [方法条目](../source-audit.md) |
| 镜像仓库目录、清单与层表示 | /healthz不是Docker Registry V2的通用匿名授权证明。 | [方法条目](../cloud/container-k8s-security.md) |
| py2app制品层级与字节码版本 | py2app应用可同时含Mach-O启动/扩展、Python源码、依赖归档和字节码；[维护者实现说明](https://py2app.readthedocs.io/en/latest/implementation.html)列出Resources里的启动脚本/主脚本、Python依赖zip及Mach-O依赖，历史目录名不能硬套当前制品。 | [方法条目](../source-audit.md) |
| 兼容规范化与相似斜线的区别 | 看起来像ASCII的字符不一定由NFKC统一替换。 | [方法条目](../by-type/xss.md) |
| 编码井号、保存文件名与URL片段 | 旧图的example.jpg%23.html是文件名建议，不是实际处理结果。 | [方法条目](../by-type/file-upload.md) |
| referrer元数据与真实请求头 | HTTP头拼作Referer，但HTML元数据名是referrer。 | [方法条目](../by-type/csrf.md) |
| 跨参数脚本拼接、行注释与调用 | 多个查询字段被原样串进同一个JavaScript字符串时，应审完整生成脚本，不能逐参数看关键词是否放行。 | [方法条目](../by-type/xss.md) |

| 金额保护值与数量的语义绑定 | “amount由随机hash保护，quantity从1改2即可两件一价”首先是业务字段绑定假设，不是密码学破译。 | [方法条目](../by-type/business-logic.md) |
| AEM查询结果序列化与仓库权限 | QueryBuilder可定位节点并选择输出属性，入口可达、节点可读和私密属性返回是三层证据。 | [方法条目](../by-type/info-secrets.md) |
| 链接noreferrer与导航操作的限制 | rel=noreferrer是链接注解，referrerpolicy=no-referrer是来源策略，不能把它们都写成HTTP头值。 | [方法条目](../by-type/csrf.md) |
| F5管理入口的认证边与执行边 | [F5原始缺陷记录951705](https://cdn.f5.com/product/bugtracker/ID951705.html)将CVE-2021-22986绑定iControl REST的未认证远程命令执行（2026-10-09核读标题/产品段，未称全部版本公告已读取）。 | [方法条目](../source-audit.md) |
| data脚本地址的逗号与反斜杠文本 | 源帖在HTML的script src属性写字面反斜杠x2C；[HTML双引号属性规则](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(double-quoted)-state)不会像JavaScript字符串解析器那样把它转换成逗号。 | [方法条目](../by-type/xss.md) |
| HTML image兼容名与元素上下文 | 黑名单没列image并不意味着它是完全无关的新标签。 | [方法条目](../by-type/xss.md) |

| 带外工具的回连接收者与结果归因 | 运行带外工具前，先静态追踪接收地址的来源、默认值、配置覆盖、生成载荷、各重定向/第三方服务与最终传输。 | [方法条目](../source-audit.md) |
| phpMyAdmin配置向导与数据库权限 | phpMyAdmin登录页与setup配置向导属于不同消费者。 | [方法条目](../by-type/authn-session.md) |
| 百分号编码的十六进制大小写 | [RFC3986§2.1](https://www.rfc-editor.org/rfc/rfc3986.html#section-2.1)规定百分号编码中A–F与a–f等价（2026-10-09核读），所以%3C与%3c在对应百分号解码后表示同一字节。 | [方法条目](../by-type/waf-bypass.md) |
| 正则校验与最终解析器的差分判据 | 差分检查先定义应保持一致的具体性质，例如正则接受的地址是否被实际URL消费者解析成预期scheme/host/端口，而不是要求两个实现对所有输入输出相同。 | [方法条目](../targeted-fuzzing.md) |
| GitLab个人与项目snippet的可见性 | /-/snippets可提供代码片段发现线索，存在入口和可读公开代码不自动是秘密泄露或critical。 | [方法条目](../source-audit.md) |
| Windows文件名末尾句点与实际存储接口 | “Windows自动去掉末尾句点”需要限定路径命名空间和实际API。 | [方法条目](../by-type/file-upload.md) |
| Intruder反射匹配的配置与观察边界 | Grep-payloads勾选只表示工具按配置发现请求标记的响应匹配。 | [方法条目](../targeted-fuzzing.md) |

| 数值字符引用的前导零与缺失分号 | HTML数值字符引用与URL百分号解码分别发生。 | [方法条目](../by-type/xss.md) |
| Unicode码点窄化与HTTP控制字节 | %E5%98%8A经正确百分号到字节、UTF-8解码对应U+560A，不等于LF；离线仅对单字符编码观察到UTF-8字节E5 98 8A，显式取码点低8位才得到0A。 | [方法条目](../by-type/waf-bypass.md) |
| 令牌换发入口的验签与签发主体 | 换发/生成JWT的入口也可能先消费旧票据，不因其他业务接口严格验签就获得安全保证。 | [方法条目](../by-type/jwt.md) |
| 邮箱大小写与订阅权益的稳定身份 | 小写地址登录成功、大写变体另注册后显示verified/paid，至少涉及注册唯一键、登录查找、验证主体和订阅查找四个消费者。 | [方法条目](../by-type/authn-session.md) |
| 秘密扫描器的合成语料与漏项评估 | 泄漏样本仓库能帮助评估扫描器，但名称叫leaky-repo不保证每个值都安全、撤销或可使用，也不证明样本覆盖当前项目。 | [方法条目](../by-type/info-secrets.md) |
| URL内容监控的身份、阈值与差异制品 | 监控图里的interval、tolerance=50、keywords、Cookie和View Changes说明多个观察配置，不给出50的算法/单位或完整工具实现。 | [方法条目](../discovery/records-and-incremental.md) |
| Burp站点树的JS筛选与采集遗漏 | Site map选Script MIME及.js后缀只得到已有采集集合经过过滤的视图。 | [方法条目](../discovery/client-and-cloud.md) |
| 响应头注入与HTML正文消费的分界 | %0A表示LF一个字节，CRLF是一对字节；[RFC9112§2.2](https://www.rfc-editor.org/rfc/rfc9112.html#section-2.2)描述行终止的CRLF与接收方可识别单LF的宽容处理，[§11.1](https://www.rfc-editor.org/rfc/rfc9112.html#section-11.1)将响应拆分绑定请求数据解码后进入响应字段/协议流（2026-10-09核读）。 | [方法条目](../by-type/request-smuggling.md) |

| 门户CNAME客户端提示与服务端域绑定 | 历史Freshdesk帖声称改管理门户响应可绕过客户端CNAME校验，截图仅展示门户表单与代理中响应；没有最终绑定、公共DNS或另一租户实际控制证据。 | [方法条目](../by-type/subdomain-takeover.md) |
| Amass来源列表与凭据可用性 | enum -list -config的旧截图列出Data Source、Type与Available星号；它直接证明当时工具展示了来源列表，不证明所有API key通过实时认证、额度足够或能返回目标数据。 | [方法条目](../discovery/passive-and-services.md) |
| object的data资源与执行文档身份 | object data中的data:text/html;base64值先经过资源URL解析与解码，再由实际嵌入消费者处理；Base64不是净化或权限来源。 | [方法条目](../by-type/xss.md) |
| XML命名空间与浏览器的文档消费者 | .xml后缀或application/xml不保证内容只作为无活动文字。 | [方法条目](../by-type/xss.md) |
| EKS配置链、Secret列表权限与终端表示 | 旧图从AWS临时凭据、集群名称与update-kubeconfig走到kubectl get secrets，但没有最终API响应。 | [方法条目](../cloud/container-k8s-security.md) |
| SSO登录提示与已验证会话主体 | 旧图以阻断/删除Cookie、改saml?login邮箱后“登录另一账号”的流程描述风险，未提供SAMLResponse、实际IdP认证与SP会话证据。 | [方法条目](../by-type/saml-sso.md) |
| 内省类型种类与查询字段的匹配 | GraphQL手写笔记里的Schema/Type/TypeKind/Field/InputValue/EnumValue/Directive是模型线索，不是完整查询；名称需按实际内省元字段和类型处理。 | [方法条目](../by-type/graphql.md) |
| CDN路径命名候选与失效子域的独立状态 | 目标子域标签与已见CDN脚本路径的对应，可形成有依据的少量邻近文件候选；记录页面引用、构建版本、路径模板及哪些片段来自推导。 | [方法条目](../discovery/client-and-cloud.md) |
| 云名称可用性脚本的实际提交对象 | Azure CloudApp检查截图读入azure.list筛出.cloudapp.net，但可见片段随后提交固定name的JSON，没有把$list逐项注入请求或展示可用性响应。 | [方法条目](../by-type/subdomain-takeover.md) |

| API二次URL构造的路径与分隔符 | 历史图把外层API路径中的编码斜杠/井号导向内部路径，称Second Order Path Traversal；这是二次URL构造与路由的候选，不直接证明文件系统遍历或认证绕过。 | [方法条目](../discovery/web-and-api.md) |
| Java mTLS的本机身份材料与远端信任 | 来源列出ClientKeyStore/ClientTrustStore，建议改truststore与代理证书做流量检查；材料角色不能混为一个认证开关。 | [方法条目](../by-type/authn-session.md) |
| 可选链、括号分组与模板标签调用 | 可选调用、取属性后的模板标签调用和间接eval有不同语义。 | [方法条目](../by-type/xss.md) |
| 表单表示转换与百分号字段语义 | 旧图从application/x-www-form-urlencoded改为multipart/form-data，前后仍是POST；不能称作HTTP方法变化。 | [方法条目](../by-type/waf-bypass.md) |
| 支付回调的签名比较与权威订单匹配 | 历史PHP图拼接merchant_id、transaction_id、摘要后的秘密、金额、币种及status，再以==比较md5sig，另比较收款邮箱；正文只讲获利故事，图中TODO也不是已运行履约证据。 | [方法条目](../by-type/business-logic.md) |
| 代理自动改写的启用状态与TLS直通缺口 | 历史Burp Match and Replace截图显示请求/响应规则，但多项启用框未勾选；列出规则不证明它们作用于所观察请求。 | [方法条目](../discovery/records-and-incremental.md) |
| 用户名命中与自然人身份关联 | Maigret/UserRecon截图的相同handle、Found标签和资料链接只生成关联候选；重名、软404、旧页面、平台别名及工具判断规则都可能造成误关联。 | [方法条目](../source-audit.md) |

| 导出后缀拼接与HYPERLINK的值及链接 | 旧图声称CSV导出给可疑输入追加-1会阻止公式，而加字符串拼接可恢复HYPERLINK；这是最终单元格表达式候选，未给实际导出字节、软件版本或点击记录。 | [方法条目](../by-type/document-rendering.md) |
| 无逗号表达式的方言与结果形状 | 历史图列出LIMIT替代、SUBSTR的FROM/FOR形式及派生表JOIN，不能仅按字符限制认这些表达式在全部数据库等价。 | [方法条目](../by-type/sql-injection.md) |
| 认证查询结果与独立密码比较 | 教育图的authenticate伪代码先按username拼查询取password，再把$result与md5(password)比较；它没有说明db.execute返回标量、行集、游标还是错误，亦未展示绑定主体的会话。 | [方法条目](../by-type/sql-injection.md) |
| 注入时序与结果观察通道分开建模 | 旧SQL类型图把Second Order或Out Band放同一框，但二次注入描述存储后再被不安全查询消费的时序，带外描述结果经另一通道观察；两者可以组合，也各自独立。 | [方法条目](../by-type/sql-injection.md) |
| 顺序GUID的生成条件与对象授权 | 旧图按前三个NEWSEQUENTIALID例子建议首个十六进制字节加一；样例序列不能推广所有GUID或持续相同增量。 | [方法条目](../by-type/idor-access-control.md) |
| 仓库索引排序、模式过滤与账户额度 | GitDorker旧功能图声称recently indexed/Best Match、过滤test/example以及30次请求乘独立账户token。 | [方法条目](../discovery/passive-and-services.md) |

| JWT格式属性与浏览器凭据运输 | 格式、密码学保护、长度与浏览器运输条件分别核对。 | [方法条目](../by-type/jwt.md) |

| 缓存命中信息与缓存失效权限 | 历史帖把X-Cache: HIT和X-Cache-Hits: 50直接关联到未经认证的cache purge；这两个观察没有给清除请求、权限检查或失效结果，不能从命中计数推断清除能力。 | [方法条目](../discovery/web-and-api.md) |
| 所有参数同时替换与裸键的变换契约 | 旧图脚本对query按&分段，再用正则去掉等号及后续值并拼触发字符串，示例把多个字段包括commit同时改成FUZZ。 | [方法条目](../targeted-fuzzing.md) |
| 随机对象码的样本数与结果分类器 | 旧Turbo Intruder图以两大写字母和四数字再洗牌生成账号码，range(1,10000)描述至多9999个循环位置，不代表9999个不同对象；随机抽样可重复，正文声称几百次后返回账号资料也没有给完整执行日志。 | [方法条目](../targeted-fuzzing.md) |
| 路径星号与真正路由及授权消费者 | 旧图仅称/secret返回404而/secret/*返回200并揭示端点；未给两次请求、所选处理器或私密资源。 | [方法条目](../discovery/web-and-api.md) |
| CRUD业务动作与真实API方法 | 由DELETE /api/item/32推POST /api/item、GET /api/item/33及SET更新，是候选模式而非该服务契约；32和33也不是同一对象的对照。 | [方法条目](../discovery/web-and-api.md) |
| 正则生成的正例与真实接受边界 | 来源建议网站按regex生成列表以加快分析；生成器输出仅是该实现选择的一组字符串，不能证明生产校验器接受、完整覆盖或没有绕过。 | [方法条目](../targeted-fuzzing.md) |
| 恢复链接的可逆表示与账号绑定 | 恢复token末尾等号不能独立证明Base64或任何特定格式；即便离线解出自有邮箱，也只证明该表示含身份字段，不证明其是全部授权凭据、无签名、可修改或可接管。 | [方法条目](../by-type/authn-session.md) |

| 重定向日志筛选器的条件与观察缺口 | 旧Logger++图用scope、302、GET及query/body中URL样式正则筛日志，随后建议爬整站与Fuzz；筛选结果只是选中的既有记录。 | [方法条目](../by-type/open-redirect.md) |
| 地址表示换算与来源笔误 | 旧帖写169.259.169.254等于2851449342，四段写法的259超出八位组范围，且整数按32位四个八位组展开是169.245.169.254；不能静默改为常见元数据地址再称来源已证明等价。 | [方法条目](../by-type/ssrf.md) |
| 数组拼接字符串与管道后的解释器 | 旧片段用数组skid与索引s拼字符后把标准输出管给$0。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 数据库中凭据表示与恢复令牌的不同能力 | 旧帖建议SQL注入无法“解密密码哈希”就转取重置token，并称常未加密或盐弱。 | [方法条目](../by-type/sql-injection.md) |
| 文件后缀筛选所在阶段与敏感内容判据 | 旧流水线把历史URL收集、去重/隐藏图片、HTTP探测、grep后缀和追加输出相连；后缀筛选发生在探测后，不能把全量网络行为描述成只读搜索。 | [方法条目](../discovery/records-and-incremental.md) |
| 主机文本后缀与URL路径追加 | 来源对subfinder每行用sed在末尾加dashboard再交给httpx，却未加路径分隔符。 | [方法条目](../discovery/web-and-api.md) |
| 招聘技术要求与已部署组件 | 招聘JD列语言、框架、云技能可作为有日期和部门背景的技术候选，不能认定每个站点当前运行这些组件。 | [方法条目](../discovery/passive-and-services.md) |
| 本机IPC与DNS轨迹的观察层 | IPCDump旧图混合unix-dgram到/run/systemd/notify的WATCHDOG=1与loopback-udp上ping/systemd-resolve的DNS字节。 | [方法条目](../discovery/passive-and-services.md) |
| 协作空间导出日志与凭据作用域 | SlackPirate旧图持有token、称非admin但可dump用户/access日志，查S3/credential/key、提取消息URL并下载5个文件；“attempting find”与条件文字“If any”不证明每类秘密真实命中，文件名passwordsecret也不证明内容有效。 | [方法条目](../discovery/client-and-cloud.md) |

| 二进制保护标签与实际内存能力 | 旧OverRide训练图显示Partial RELRO、No canary found、NX enabled、No PIE和文件路径；另帖概括地址泄漏/部分覆盖可败ASLR。 | [方法条目](../source-audit.md) |

| 方法提示注释与实际请求方法 | 旧Burp历史图的Method列为GET，而Comment分别写PUT、POST或POST PUT DELETE PATCH；另一HEAD行与这些注释不是同一操作。 | [方法条目](../discovery/web-and-api.md) |
| 固定列提取、删行与下游输入形状 | 旧链用gospider输出的awk第5列、Shodan输出第3列、sed删前4行、code-200及等号筛选，再交给探测/注入工具。 | [方法条目](../discovery/records-and-incremental.md) |
| 图片加载、Referer与恢复权限的分段证明 | 旧帖把可存储img src、OOB回连与零交互账号接管相连。 | [方法条目](../by-type/authn-session.md) |
| 浏览器容器与可比较的CSRF主体 | 旧帖称Chrome里失败可转Firefox Multi-Account Containers。 | [方法条目](../by-type/csrf.md) |
| 客户端captcha标志与服务端受保护动作 | 旧CAPTCHA图由robot错误变成invalid email/password，提交文字含captcha_presented=false，但g-recaptcha-response仍可见。 | [方法条目](../by-type/authn-session.md) |
| POST正文候选与路径发现的不同位置 | 旧vaf图固定jsonplaceholder/posts、method POST、正文title字段占位，候选index/main/register/login/api均显示201与长度33至38。 | [方法条目](../targeted-fuzzing.md) |
| 社交网页搜索路径与Graph API契约 | 旧图标题写Facebook Search Graph API，却列/search/UserID/...、2019事件及fb://profile等网页/应用导航形状。 | [方法条目](../discovery/client-and-cloud.md) |
| 相同爬虫设置下的输入变化与增量 | 旧笔记以相同Burp配置重新crawl寻找新端点，另建议通知机器人、模板扫描与分布式工作。 | [方法条目](../discovery/records-and-incremental.md) |

| 多主机循环的输入单位、输出归属与总预算 | 旧FFUF片段以for i in $(cat hosts)逐个加/FUZZ，每次用相同ffuf.txt，筛200/非零长度并自动校准。 | [方法条目](../targeted-fuzzing.md) |
| JSON转换后的去重单位与JS发现覆盖 | 旧haktrails→httpx→getJS --complete图出现重复api_dynamic.js/api_static.js，另一链先tojson再anew，展示带引号/逗号的列表片段。 | [方法条目](../discovery/records-and-incremental.md) |
| 候选去重的原顺序与资源上限 | 旧Duplicut图称sort -u导致probabilistic ordering loss、awk关联数组会OOM。 | [方法条目](../discovery/records-and-incremental.md) |
| 无地址答案的CNAME与过期注册域线索 | 旧puredns帖称有有效CNAME但没有IP仍保留，可发现指向过期域。 | [方法条目](../by-type/subdomain-takeover.md) |
| APK凭据字段与STS主体的有限结论 | 旧图在反编译strings.xml显示aws_access_key/aws_secret_key标签，另一图配置凭据后GetCallerIdentity返回user/sqs_queue_consumer样式ARN。 | [方法条目](../by-type/info-secrets.md) |
| ID的标量、数组、嵌套对象与通配消费者 | 旧API图把id标量改数组/嵌套对象、URL重复id和user_id星号并列为401/403后绕过招式。 | [方法条目](../by-type/api-property-pollution.md) |
| 扫描器版本提示、条件建议与实际检查结果 | 旧Nginxpwner图显示current1.19.6/latest1.19.9并给Exploits/ Shellcodes No Results，随后说如果工具显示nginx.conf可能没有root directive。 | [方法条目](../source-audit.md) |
| 重复返回参数与多层编码的实际导航消费者 | 旧/login例同时给两个ReturnUrl和双百分号编码值，另一例用title闭合、编码属性/实体、location/hash片段宣称Access Denied bypassed。 | [方法条目](../by-type/xss.md) |

| 有效验证码与被验证手机号的挑战绑定 | 旧两种语言的图先给自有手机号的有效验证码，再建议改MobileNo并转发，另一状态图称2FA Bypass/Low。 | [方法条目](../by-type/authn-session.md) |
| 分页上限与实际资源成本 | 旧API图以limit=100改极大数字称可能Layer7 DoS。 | [方法条目](../targeted-fuzzing.md) |
| Swagger文档来源与元数据链接消费者 | 旧图用url参数加载外部定义，将termsOfService及contact.url/email都写成javascript字符串。 | [方法条目](../by-type/xss.md) |
| HEAD筛头的匹配、缺失与请求失败 | 旧headerFilter/headerMatch用xargs -P40把域名插进bash -c，curl -I --silent后tac两次再grep -q；负向函数把未匹配行打印为域。 | [方法条目](../discovery/records-and-incremental.md) |
| 邮件模板变更与同一输入的求值观察 | 旧图把两个日期的邮件展示名中{{7*7}}与49并排，正文称等待模板变动得到SSTI。 | [方法条目](../by-type/ssti.md) |
| 多API凭据、监控配置与外送副作用 | 旧Findomain例把同源多key用逗号配置，并列Postgres连接、Discord/Slack webhook、Telegram、threads/rate_limit、timeouts、随机目标及exclude_sources。 | [方法条目](../discovery/records-and-incremental.md) |
| 窗口名称、子框架编号与srcdoc策略 | 旧TinyXSS图把top[0].name、contentWindow.name、top.name、srcdoc外部script、eval(name/URL)分成数种场景。 | [方法条目](../by-type/xss.md) |
| PHP参数名转换与不完整百分号编码 | 旧帖说PHP替换空格、ASPX删掉后面不是两个数字的百分号。 | [方法条目](../by-type/waf-bypass.md) |
| 邮箱确认票据跨用途与换邮箱后的恢复状态 | 旧帖把确认链接verifyemail路径改reset-password称成功；另一帖认为改邮箱后旧重置链接还能改密必是bug。 | [方法条目](../by-type/jwt.md) |
| 关键词筛选与凭据字段的语义分类 | 旧Cookie IDOR正则找admin/user等与id/name/token相连，使用弯引号、未转义点和未锚定匹配；另称Top10的Burp清单实际列11种文字。 | [方法条目](../discovery/records-and-incremental.md) |
| 抽象攻击仿真中的owned与真实系统证据 | 旧CyberBattleSim图的attack/print_all_attacks输出将节点标owned/discovered，关系分KNOWS/REMOTE_EXPLOIT/LATERAL_MOVE，并展示模拟CachedCredential、SSH标签与奖励说明。 | [方法条目](../source-audit.md) |
| 代理请求脚本与变换前后的证据 | 旧帖建议每个HTTP请求/响应运行Python脚本以编码/加密输入、签名或处理弱CAPTCHA。 | [方法条目](../discovery/records-and-incremental.md) |

| 重复等号与文件参数消费者 | 旧帖把file=rce.php改为file===rce.php，声称WAF由阻断变200。 | [方法条目](../by-type/waf-bypass.md) |
| 匿名评论内容与作者关联的可见性 | 旧帖称六位UID可取用户全部评论，包含匿名与非匿名评论。 | [方法条目](../by-type/idor-access-control.md) |
| 登录字段由POST正文移到查询串 | 旧帖将登录POST改GET并把user/pass放查询串，配图另展示输入片段和两个遮盖主机的弹窗。 | [方法条目](../discovery/web-and-api.md) |
| HTML输入名称提取与表单契约 | 旧流水线并发200次curl后用grep筛input、匹配双引号name并去重。 | [方法条目](../discovery/records-and-incremental.md) |
| PTR候选、地址去重与虚拟主机丢失 | 旧例扩展一个/16逐地址PTR，再用未转义品牌正则筛名字、正向解析、删列仅留IP并HTTP探测。 | [方法条目](../discovery/passive-and-services.md) |
| 抓包、流记录与图描述的格式边界 | 旧例从已有pcap筛TCP且目标端口80，接argus/ra、排序去重，再送dot生成PNG；中间含省略号，转换细节未完整给出。 | [方法条目](../discovery/records-and-incremental.md) |
| Basic凭据的组装与编码层次 | 旧Intruder图将用户名与口令列表用冒号组合、Base64处理并关闭URL编码，属于凭据候选生成流程，不证明任一身份已认证。 | [方法条目](../by-type/authn-session.md) |
| ASPX错误源行、类型转换与短路语义 | 旧错误页显示System.FormatException、promotions_details.aspx第14行、Request的DetID/PID/ID片段、整数转换与渲染栈；路径/主机有遮盖且源行右侧截断。 | [方法条目](../by-type/info-secrets.md) |
| 代理总开关与匹配规则是否实际生效 | 旧FoxyProxy图一张选择Burp for all URLs，另一张规则页提示只有Patterns and Order模式才采用规则；白名单为全部URL而无黑名单。 | [方法条目](../discovery/records-and-incremental.md) |
| 两个账号重放与真正跨站CSRF边界 | 旧图先从A捕获关闭2FA请求，再关闭标签保持B登录，在新标签提交PoC看B是否关闭。 | [方法条目](../by-type/csrf.md) |
| 音频元数据中的XML与升级后失效的防护 | [Sonar原始分析](https://www.sonarsource.com/blog/wordpress-xxe-security-vulnerability/)将CVE-2021-29447绑定WordPress5.7.1之前、PHP8及媒体上传权限：WAVE的iXML块经getID3进入SimpleXML，LIBXML_NOENT显式启用实体替换；旧代码在PHP8跳过实体加载禁用，默认安全假设与显式flag发生冲突。 | [方法条目](../by-type/xxe.md) |
| 社交页面不可用与可重新控制 | 旧对照图一边说内容可能只对小组可见/可见性已改变/已删除，另一边说链接可能损坏或页面移除；正文将左归IP地区阻断、右归可接管。 | [方法条目](../by-type/subdomain-takeover.md) |
| 收集模式与自动扫描模式的副作用 | 旧APSoft图将Scanner、URL grabber、Grab url and scan分开，列SQL/XSS/LFI和搜索来源；3klcon画面虽称中小范围，却还列端口、秘密、接管、桶和CVE扫描。 | [方法条目](../discovery/records-and-incremental.md) |
| 脚本字符串反射与自动Vulnerable标签 | 旧图把历史URL全部query值替换成script字符串，curl返回后grep文字就打印Vulnerable；同时有Failed writing body。 | [方法条目](../by-type/xss.md) |
| Firebase探索工具与真实数据权限 | 旧Baserunner帖宣称未认证读写、全库导出、跨权限写和UI隐藏集合。 | [方法条目](../discovery/client-and-cloud.md) |
| 非十六进制百分号片段的来源错误 | 旧编码帖将%2s/%2u称为角括号的URL编码，另一些重定向例写$2f%2f；这些字节必须按原样保留。 | [方法条目](../by-type/waf-bypass.md) |

| IFS、工作目录与路径通配的环境依赖 | 旧无空格载荷使用IFS、第九位置参数、PWD后缀删除和路径通配去读取系统文件；另一图显示相似请求与passwd格式响应。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 无限重连脚本与可终止动作 | 旧Bash循环每五秒尝试建立FIFO并连接nc/交互shell。 | [方法条目](../discovery/records-and-incremental.md) |
| 自动求值标记与完整模板消费链 | 旧线程1/3用50并发curl跟随重定向，grep check-ssti49就输出VULNERABLE；正文没提供完整sstipatterns或后两段，转发又把引号/换行改成弯引号和字母n。 | [方法条目](../by-type/ssti.md) |
| 2FA启用、预认证会话与挑战更新 | 旧2FA图把发送/刷新/验证限额、OTP跨用户/跨动作复用、启用后旧会话、改密/关2FA、答案泄露和本地响应改写混在一起。 | [方法条目](../by-type/authn-session.md) |
| Flutter流量与泛用TLS钩子的观察缺口 | 旧图代理中有Dart/2.10的GET，旁边泛用Android脚本多数pinning类not found，仅显示TrustManagerImpl bypass。 | [方法条目](../by-type/mobile-android.md) |
| 分号路径段与代理到容器的规范化顺序 | 旧图把/portal/..;/manager/html在前层称普通目录，在Tomcat称父目录，另见/sol/..;/manager/status、HTML403和根路径404。 | [方法条目](../by-type/waf-bypass.md) |
| Tomcat状态页与管理接口的权限分层 | 旧图状态页有JVM/连接器统计，manager/html却403；错误页还列manager-gui/script/jmx/status及CSRF说明。 | [方法条目](../by-type/idor-access-control.md) |
| 跳过预解析与浏览器实际连接 | 旧Findomain4.3.0图接外部HTTP筛选器，再用--no-resolve截图，另给Findomain单独流程。 | [方法条目](../discovery/records-and-incremental.md) |
| 联系人导入与手机号到稳定账号的关联 | 旧图给联系人管理流程：加入手机号后重定向到另一接口，其参数giver_id声称关联该号码所属账号。 | [方法条目](../by-type/info-secrets.md) |
| AFL计数、唯一崩溃与独立根因 | 旧Privoxy研究正文称六项漏洞，配图AFL++显示56总crashes、1unique、246timeouts/14unique、1401paths及运行时间。 | [方法条目](../targeted-fuzzing.md) |
| public与private路由名及真实配置受众 | 旧线程从/application/properties/public换private，称免认证返回私人属性。 | [方法条目](../by-type/info-secrets.md) |
| 盲XSS候选字段与真实后续读者 | 旧列表将review/contact、password、地址、付款姓名和User-Agent列作盲XSS入口。 | [方法条目](../by-type/xss.md) |
| SSRF导图中的协议、读取与元数据能力 | 旧Search&Destroy图并列URL解析/地址表示、重定向、DNS、schema及文件/云/内网/XXE/XSS等分支。 | [方法条目](../by-type/ssrf.md) |
| 用户态隐藏与观察器可信边界 | 旧r77图展示文件管理器、TaskManager、注册表变量及TCPView，正文声称隐藏进程/文件/连接。 | [方法条目](../expert-reasoning.md) |

| 日志写入、文件读取与解释执行的三段条件 | 旧帖把User-Agent写入访问日志，再通过文件包含参数调用PHP片段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| AEM点号路径与Sling资源分解 | 旧两行示例同时把/node改成/nod并改变点号串后称JSON绕过；这些变化不能证明命中同一资源，更不能把省略样式点串恢复成确定selector数量。 | [方法条目](../by-type/waf-bypass.md) |
| WEB-INF部署描述符与可下载制品的范围 | 旧图/assets/../settings.py返回404而/assets../settings.py列200，另有原始GET /sf//../WEB-INF/web.xml及XML响应。 | [方法条目](../by-type/info-secrets.md) |
| 创建对象时指定另一所有者 | 旧线程修改Base64形式user_id后称为User2创建Goal，报告截图补充GraphQL入口和triaged标签。 | [方法条目](../by-type/idor-access-control.md) |
| 验证码过期后的拒绝分支与替代恢复因素 | 旧步骤称等待OTP过期后任意值均通过，另列null、000000、备份码、密码恢复、点击劫持和重复提交。 | [方法条目](../by-type/authn-session.md) |
| 为列表行补scheme的输入类型契约 | 旧sed把https://添加到每行开头。 | [方法条目](../discovery/records-and-incremental.md) |
| 未取得邮箱claim时的手工回填与资格判定 | 旧线程仅保存步骤6至8：社交授权不给email权限，产品随后要求填写company email并接受任意声明，称资格校验绕过。 | [方法条目](../by-type/oauth-oidc.md) |
| 全局false替换与角色字段的不同消费者 | 旧Burp图对Response body作字面false→true，关闭Regex match，另一后台清单把Cookie/请求参数、响应标志和roleid写入并列。 | [方法条目](../by-type/idor-access-control.md) |
| 浏览器JavaScript控制台与操作系统shell | 旧JSshell图有SVG/SCRIPT/IMG/BODY片段、循环附加document子节点、localhost连接，cookie输出foo=bar、pwd输出hook.html、domain输出example.com。 | [方法条目](../by-type/xss.md) |
| Bash网络重定向扫描的有限矩阵与阻塞 | 旧图双重循环仅含地址末段1至254及22、80、443、3306、3389五个端口，共1270候选，不是完整子网全部端口。 | [方法条目](../discovery/records-and-incremental.md) |
| SQL、XSS与模板polyglot的独立判据 | 旧图把一个含引号、svg事件与双花括号算式的字符串分别标SQL Injection Test、XSS Test和SSTI/CSTI。 | [方法条目](../experiment-design.md) |
| GraphQL搜索输入到NoSQL操作符的边界 | 旧GraphQLmap图的doctors search参数内含lastName/$regex并返回Admin记录，随后显示nosqli及未输入的Query提示。 | [方法条目](../by-type/graphql.md) |
| 前端配置里的候选秘密与版本扫描的证据层级 | 旧打包JS图展示prod/dev数据库、Azure、Dropbox、Vimeo、Google和其他集成的配置字段，许多数值被遮盖。 | [方法条目](../source-audit.md) |
| Burp扩展清单与自动化动作的证据保全 | 旧三栏cheatsheet覆盖快捷键、编码、Collaborator协议、参数发现、变换告警、版本扫描、请求走私、日志、高速请求、SAML/JWT/多角色对照和REST API。 | [方法条目](../discovery/records-and-incremental.md) |
| 工具报错、命令输出与实际执行身份 | 旧struts-pwn终端图有-c id、ChunkedEncodingError/IncompleteRead、随后uid=1001(tomcat)和Done。 | [方法条目](../by-type/cmd-injection-rce.md) |

| 防火墙阻断规则集合与有效流量决策 | 旧PowerShell片段仅筛FwPolicy2.rules中action为0的规则，再显示name/applicationname/localports；这是规则集合的部分视图，不是当前所有被阻端口。 | [方法条目](../discovery/passive-and-services.md) |
| 拼写建议、词典替换与过滤后语法重组 | 旧帖和图把scrpt/confrm纠正为script/confirm，并称PHP pspell_suggest能绕WAF。 | [方法条目](../by-type/xss.md) |
| 事件名中的百分号、NULL与最终HTML属性 | 旧XSS图建议on%00error，并列其他标签/事件、prompt/confirm和多重编码。 | [方法条目](../by-type/waf-bypass.md) |
| 禁止重定向后的页面与真实后台能力 | 旧帖称No-Redirect老Firefox扩展加猜后台URL可接管，图仅有username/logout/companies/上传与Save表单。 | [方法条目](../by-type/idor-access-control.md) |
| 多请求链的凭据来源与消费代际 | 旧AuthMatrix图用链从不同Request抽JSESSIONID、app_sessionId、token、隐藏app_processorId，并将用户名/密码/OTP替换到后续请求，矩阵正则只看302/200。 | [方法条目](../experiment-design.md) |
| 非root注入Gadget与被改变的APK | 旧帖frida-non-root将Gadget注入APK并要求更新/res。 | [方法条目](../by-type/mobile-android.md) |
| 递归目录脚本的聚合负载与失败覆盖 | 旧“without killing host”脚本图含ffuf400线程、递归深度10、0.6至1.2延迟、多扩展，过滤500/501/502并按末段清洗名写JSON。 | [方法条目](../targeted-fuzzing.md) |
| shell快捷函数中的Markdown链接与累积输出 | 旧.bashrc图把crt.sh/anubis URL写成`[URL](URL)`的Markdown样式，reconjs又向js.txt/AliveJs.txt累积追加并从antiburl输出取第四列。 | [方法条目](../discovery/records-and-incremental.md) |
| 表单中间件、GET副作用与XS-Search | 旧帖指GraphQL中间件可能接受表单POST、GET mutation和XS-Search。 | [方法条目](../by-type/graphql.md) |
| 编辑器交换文件的生命周期与原文恢复范围 | 旧图Vim打开/var/www/html/index.php，目录出现.index.php.swp，curl输出12288字节后cat显示b0VIM8.0及零散PHP文本。 | [方法条目](../by-type/info-secrets.md) |
| 跨子域令牌复用与受众设计 | 旧帖建议在主站签发token后拿到全部子域尝试。 | [方法条目](../by-type/authn-session.md) |
| Cloud Shell容量与研究工具环境的使用约束 | 旧帖以5GB/每周50小时建议用Google Cloud Shell做recon。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| XML-RPC错误响应中的实体展开证据 | 旧Burp图GET含XML methodCall/DTD外部实体，响应200的methodResponse却是fault，faultString出现“No such service”及账号样式文本。 | [方法条目](../by-type/xxe.md) |
| 静态扫描的命中位置与独立漏洞数量 | 旧Php_Code_Analysis终端声称total17，列SQLi5/XSS3/command1/LFI1/SSRF1/upload1/host1/deserialization4，部分命中只是mysqli_query/UPDATE或变量位置，文件与路径右裁剪。 | [方法条目](../source-audit.md) |
| 账号测试导图中的动作分类与身份污染 | 旧裁剪导图并列登录后资料/邮箱/密码/CSRF、文件上传/EXIF、删除/重认证、代登/会话替换、错误/用户名枚举、TLS、限额/字典、2FA本地响应改写。 | [方法条目](../expert-reasoning.md) |

| PDO数据参数与动态排序标识符 | 旧帖说PDO不能绑定列名/ORDER BY列。 | [方法条目](../by-type/sql-injection.md) |
| 关闭内省后的候选schema与模型完整性 | clairvoyance旧宣传称内省关闭仍可输出供Voyager/InQL使用的JSON。 | [方法条目](../by-type/graphql.md) |
| 批处理中的挑战身份与验证次数 | 旧帖将单包多邮箱/密码及全部2FA值直接称限流绕过。 | [方法条目](../by-type/graphql.md) |
| 对话框、动态求值与文档写入的不同消费者 | alert关键词被过滤后改confirm/prompt/eval/write，只是候选调用名称改变；这些API不具有相同参数、返回值或安全作用域。 | [方法条目](../by-type/xss.md) |
| 字符串替换回调与已取得的JavaScript执行 | 旧帖把replace传入alert函数称“在RegExp中执行”。 | [方法条目](../by-type/xss.md) |
| 旧百分号u表示与Unicode外观和HTML标签开头 | 旧ASP span示例把%u003C、%u3008和%uFF1C并列。 | [方法条目](../by-type/waf-bypass.md) |
| 自动化文字命中与服务端取址的因果 | 旧1/4脚本把参数替换为云metadata hostname路径，grep到compute.internal便标VULNERABLE；2/4改为interactsh标记。 | [方法条目](../by-type/ssrf.md) |
| 多阶段URL流水线的集合、解析与总量 | SSRF组合图串枚举→httpx活性筛选→gau/wayback→URL去重→参数替换→curl/ffuf，分别列500、30或200等并发。 | [方法条目](../discovery/records-and-incremental.md) |
| 站点树过滤、任务暂停与观察分母 | 旧Burp图显示only parameterized、hide not-found，4xx/CSS/图片/二进制被隐藏，only in-scope没有勾选，且task execution paused/site map will not be populated。 | [方法条目](../discovery/records-and-incremental.md) |
| 系统代理协议选择与项目scope和制品身份 | 桌面测试旧帖建议OS proxy/Burp scope/pinning patch；图里macOS只勾HTTP到本机8080，HTTPS未勾，并有local/link-local bypass，另一图是Burp advanced scope的Any协议、单host与空Port/File。 | [方法条目](../by-type/desktop-client.md) |
| Rails历史指南与实际许可字段的绑定 | 旧帖链接Rails3.2.9并称mass assignment仍普遍存在，accepted/奖金图缺字段与版本，不能推广当前所有Rails。 | [方法条目](../by-type/api-property-pollution.md) |
| 申请状态字段与审批转换的权威结果 | pending0→1或PENDING→Accepted只是字段候选，不同产品枚举/状态含义不同。 | [方法条目](../by-type/api-property-pollution.md) |
| APK中的Firestore线索与主动规则检查 | FireStorePwn示例图先反编译APK、从Manifest/strings/smali取项目与Tweets集合，再提示查询费用、询问permission checks并显示readable/not writable。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| IMAP凭据工具中的配置、连接与认证失败 | IMAPLoginTester截图把invalid email、missing config、IPv6代理不支持、超时与Login FAILED放在同一输出，最后working logins0/4。 | [方法条目](../by-type/authn-session.md) |
| Windows工具图中的跳转、执行与横向权限 | HookDump图列ntdll函数/JMP地址，但没有基准字节、模块归属、权限/系统版本；跳转存在不独立证明恶意hook或保护可绕过。 | [方法条目](../expert-reasoning.md) |

| 动态表达式调用与服务进程身份 | FuelCMS旧帖展示经过编码的PHP表达式、函数名间接调用，以及apache uid/gid48和网络统计输出。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 导出任务、格式分支与文件交付的权限 | 旧建议强调CSV/PDF下载，另一帖把MEC事件XML下载称P2；文件下载框657KB、PII报告标题或高危标签没有显示私密字段及主体。 | [方法条目](../by-type/idor-access-control.md) |
| 匿名统计设置与实际收集和外传 | 旧FoxyProxy图中Send Anonymous Usage Statistics已勾，Google同步未勾，发布提示开启；这些分别属于统计、同步和更新入口，不能由一个开关推其他行为。 | [方法条目](../discovery/records-and-incremental.md) |
| 回连观察器自测与目标取址的区分 | interactsh0.0.3四窗示例先取观察器地址，再由测试者curl并查看DNS A/AAAA与HTTP事件；这条链能说明某次观察器自测，却不能归因目标服务端取址。 | [方法条目](../by-type/ssrf.md) |
| 双斜线路径、Location与自动跟随的出站 | 旧httpx命令将双斜线目标文本放在path并启用follow-redirects/location。 | [方法条目](../by-type/open-redirect.md) |
| multipart路径文本、实际存储与CDN映射 | 旧filename包含空格、重复上级路径和jpg后缀，并建议检查Web根目录/CDN。 | [方法条目](../by-type/file-upload.md) |
| WordPress数据库准备与配置向导的状态 | 旧帖把wp-admin拒绝但setup-config step1表单可见称创建数据库/P1。 | [方法条目](../by-type/idor-access-control.md) |
| 批处理父进程、子任务与筛选后的覆盖 | Fuzzy示例分别使用while循环、xargs30、interlace20和200并发流水线，后续jq保留200/403。 | [方法条目](../targeted-fuzzing.md) |
| provider普通JSON与CVE匹配的能力层次 | 旧vCenter例展示getClusterCapabilityData的POST和多个false capability字段，另一图显示Nmap VULNERABLE/exploitable与6.5.7.0横幅。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 补丁提交、请求复核与发布部署状态 | FireflyIII图片显示维护者提交commit并说should fix，请求在5.5.12发布前验证；NCSC邮件只确认收到并通知负责方。 | [方法条目](../reporting.md) |
| XSSHunter配置、相关密钥与触发事件的来源 | 四张旧XSSHunter图分别展示collected pages16、远程script/JavaScript URI候选、Injection Correlation API Key和additional JS链式加载设置、example.com/127.0.0.1触发页。 | [方法条目](../discovery/records-and-incremental.md) |
| Postman响应脚本的额外请求与随机采样 | 旧JSONPlaceholder演示在Tests中读取原响应后，随机生成ID并用pm.sendRequest再发GET；213返回404/undefined、105返回200只是两个样本。 | [方法条目](../discovery/records-and-incremental.md) |
| User-Agent客户端标签与服务端权限选择器 | 旧帖建议将UA改为okhttp/4.1.1以绕过未认证403。 | [方法条目](../by-type/idor-access-control.md) |
| Nuclei旧速查图的语法、响应序号与组合预算 | 旧Template.yml图混有方法、BaseUrl样式、raw Content-Length、Origin、unsafe、request-condition、DSL多响应和clusterbomb/max999。 | [方法条目](../targeted-fuzzing.md) |
| 登录锁定与既有会话失效的可用性契约 | 旧帖把锁账号同时销毁sessions称永久DOS/P3。 | [方法条目](../by-type/authn-session.md) |
| FAQ类别定义与实际越过的边界 | 旧FAQ将IDOR描述为对象引用暴露，将RCE泛化整应用/服务器控制，将SSRF概括为内部资源读写。 | [方法条目](../expert-reasoning.md) |

| 注释换行、DISTINCTROW与两套词法消费者 | 旧帖组合%23、%0A、UNION、块注释及distinctrow，并夹有.0union片段。 | [方法条目](../by-type/sql-injection.md) |
| nginx别名替换、目录边界与PHP静态字节 | 旧例用/assets../index.php对比/index.php的File not found与source code，建议替换img/js/assets等名称。 | [方法条目](../by-type/lfi-path-traversal.md) |
| shell短路、命令替换与盲观察器 | 旧建议在ampersand失败后换管道/逻辑操作符、借命令替换构造DNS、用ping作盲观察。 | [方法条目](../by-type/cmd-injection-rce.md) |
| shell伪设备连接与端口开放的观察范围 | Bash图循环254个地址和22/80/443/3306/3389五个端口，并对/dev/tcp重定向写入。 | [方法条目](../discovery/passive-and-services.md) |
| 运行时词表、内存边界与恢复游标 | 旧Intruder建议Runtime file用于大词表并保证不崩溃。 | [方法条目](../targeted-fuzzing.md) |
| RBAC图中的绑定范围与旧PSP准入 | Krane图分Subject、Binding、Role、Rule、namespace/cluster-wide，并列resource的API group/verb/name、non-resource URL及旧PSP属性。 | [方法条目](../cloud/container-k8s-security.md) |
| 其他主体写入将自触发变成跨读者执行 | 旧例自存储name XSS，CSRF链未成立，随后通过IDOR修改name并称升级P2。 | [方法条目](../by-type/xss.md) |
| 冒号前缀的语句标签与URL方案 | 旧帖把stop、posting及其他单词后接冒号/调用列为多条XSS载荷。 | [方法条目](../by-type/xss.md) |
| favicon候选集、冒号切分与TLS发行者筛选 | F5图从Shodan favicon哈希命中，经grep/cut提host、httpx400并发/四端口及CVE模板，再对独立targets.txt以100并发curl insecure取得issuer并排除root localhost文本。 | [方法条目](../discovery/records-and-incremental.md) |
| 来源头的优先序与IP文本比较 | block.php三图展示CLIENT_IP优先于X_FORWARDED_FOR等字段，最后REMOTE_ADDR回退，并将返回字符串严格比较允许IP；随后加XFF与welcome画面。 | [方法条目](../by-type/host-header.md) |
| JSONP脚本消费与CORS凭据响应头 | 旧建议在缺Access-Allow-Credential true时用JSONP取数据；CORS对应响应头实际为Access-Control-Allow-Credentials。 | [方法条目](../by-type/xss.md) |
| PTR、SAN和AAAA到IPv6候选的关联边 | IPv4/IPv6来源图将反向PTR、CT SAN、被动DNS、BGP、注册域、猜地址、P2P及监听并列。 | [方法条目](../discovery/passive-and-services.md) |
| 无头浏览器采集的资源请求与脚本消费者 | page-fetch被描述为加载网页及JS/CSS/图片/XHR并可执行任意JS。 | [方法条目](../discovery/records-and-incremental.md) |
| 团队名模板、悬停渲染与编译作用域 | 旧帖说团队名模板表达式回显为1，悬停图标弹窗，并称CSTI。 | [方法条目](../by-type/xss.md) |
| 路由树、父路径与物理文件的不同集合 | 旧帖指出/admin/users存在不代表/admin有页面。 | [方法条目](../discovery/web-and-api.md) |
| IDNA主机映射与已取得的JavaScript调用 | 日语解说图用anchor设置圈字母HTTP主机，读取a.host得到alert，再通过top的计算属性和tagged template调用；正文代码还带自动链接样式，不能把保存文字与图中语法视为字节完全一致。 | [方法条目](../by-type/xss.md) |
| 原型检测标记、否定匹配与失败分母 | 旧自动化管线查询中写testparam值exploit/，JS判断却与exploit比较；grep VULNERABLE还会保留NOT VULNERABLE，配图两种输出确实同列。 | [方法条目](../by-type/prototype-pollution.md) |
| 同IP、DNS与虚拟主机路由的不同事实 | vhost配图说多个名称到同IP意味着在该主机etc/hosts中配置；这推断不成立。 | [方法条目](../by-type/host-header.md) |

| Adminer默认凭据与数据库到系统的能力边 | 旧帖串联子域发现、目录扫描、Adminer root/root与完整数据库，配图标题称内部访问RCE/P1 Triaged。 | [方法条目](../by-type/authn-session.md) |
| Jira组件枚举与公告更新后的版本和匿名权限 | 旧帖将QueryComponentRendererValue!Default.jspa与CVE-2020-36289关联，图含Jira8.14.0、匿名标头及viewHtml用户显示名。 | [方法条目](../by-type/authn-session.md) |
| HTTP成功码中的OTP业务拒绝 | 绕过频控标题所配Intruder行均HTTP200、长度536，选中响应却是JSON错误-32000和ErrResetPasswordTooManyRequests。 | [方法条目](../by-type/authn-session.md) |
| APKLeaks候选、制品版本与正式资产范围 | APKLeaks图以jq/LinkFinder提取链接并建议添加targetscope及比对旧版本。 | [方法条目](../by-type/mobile-android.md) |
| 跨云实验拓扑与真实访问控制和遥测 | BlueCloud图将Azure/AWS子网、Windows节点、管理端口和Sysmon/Winlogbeat等遥测连接并列。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 数字候选生成、标准输入与读取完成 | 旧例将seq 1 - 1000经管道交给ffuf -w -并替换user/FUZZ。 | [方法条目](../targeted-fuzzing.md) |
| Mach-O规则匹配与真实注入的证据层 | MaliciousBitHunter结构图从FAT/ARM/ARM64、头、加载命令、类/方法/字符串、符号到签名与导入导出，并用CLlocationManager、method_implementation、hooklbs等作规则线索。 | [方法条目](../by-type/mobile-ios.md) |
| Compose服务声明与主机暴露和配置内容 | 旧帖建议留意docker-compose.yml，图列MySQL5.7、phpMyAdmin、WordPress及环境变量、端口、卷、网络，多数值遮盖。 | [方法条目](../cloud/container-k8s-security.md) |
| 搜索引擎邮件候选与部分失败的分母 | EmailFinder图称Total emails37，同时YandexException因机器人检测而失败。 | [方法条目](../discovery/records-and-incremental.md) |
| 双优惠券竞争是假设还是原子规则失效 | 旧帖提出一单只准一个优惠券却并发取得两个，作者明确说还没在项目发现。 | [方法条目](../by-type/business-logic.md) |
| Django的CSRF拒绝页与DEBUG状态 | 旧帖把登录GET200/POST403推广成DEBUG=True泄露管理员邮箱；图一仅Triaged标题，另一响应显示CSRF验证失败和荷兰文“更多信息在DEBUG=True”提示。 | [方法条目](../by-type/info-secrets.md) |
| failure参数分支与真正的输出消费者 | 旧建议将failure从1改0后发现XSS，借Arjun/ParamSpider找隐藏参数。 | [方法条目](../by-type/xss.md) |
| Referer三值的状态差与时点和受保护对象 | 403文章图对同一interesting路径放不同Referer，前两次403、另一个子域值200，但响应Date不同且200正文没展示。 | [方法条目](../by-type/waf-bypass.md) |
| swap扩展名、系统交换与有限字符串输出 | 图把.swap文件、Vim恢复和system memory并列，并建议strings后head。 | [方法条目](../by-type/info-secrets.md) |
| 列表导出的当前行集合与报告正文权限 | Instant Data Scraper图显示Pages scraped1、Rows collected25，尚提示定位Next或开始crawl。 | [方法条目](../discovery/records-and-incremental.md) |
| 名称突变到DNS回答和通配对照 | 旧管线dnsgen从subdomains生成名称，再经puredns resolve写valid.txt。 | [方法条目](../discovery/passive-and-services.md) |
| 服务显示名分块存储与重组执行边 | TChopper概念图将服务显示名、base64片段、CreateService和服务可执行文件消费者串联。 | [方法条目](../source-audit.md) |
| CA转换、设备写入身份与应用信任 | 旧图导出Burp DER、转换PEM、计算subject_hash_old，再用样例文件名复制system cacerts并remount/reboot。 | [方法条目](../by-type/mobile-android.md) |
| 发现转回归用例与live测试的完成判据 | Ugly Duck宣传五至十分钟把finding转live security test，图仅模糊JSON有firing-range/reflected路径、response和logging条件。 | [方法条目](../experiment-design.md) |
| Burp配置库与扫描规则的实际生效制品 | 每周词表帖所配图实际是Custom Configuration Libraries，列速度/问题、错误处理、插入点等。 | [方法条目](../targeted-fuzzing.md) |

| ASP.NET URL会话段与ResolveUrl属性输出 | 旧图把ASP.NET cookieless会话段、ResolveUrl和生成script src连接起来。 | [方法条目](../by-type/xss.md) |
| 代理路径前缀与后端cookieless路由的保护对象 | 同图对/admin与带会话段的路径显示403和200，只能提出代理前缀与后端路由解释不同的候选。 | [方法条目](../by-type/authn-session.md) |
| 回环DNS回答、页面控制与受害本机消费者 | 旧纠错帖的127.0.0.1域名与自建localhost页面，只显示作者能控制自己机器上的服务；受害浏览器解析回环地址则指向受害机器。 | [方法条目](../discovery/passive-and-services.md) |
| 内存制品profile与进程字段的解释边界 | Volatility GUI图显示内存文件、Win7SP1x64 profile和pslist进程行，证明的是一次界面解析观察，不能据进程名称认注入、PPL读取或实时存活。 | [方法条目](../discovery/records-and-incremental.md) |
| CPG建模覆盖与finding到实际消费者的路径 | Joern help.cpg把AST、控制流等组合成可扩展图，并展示cpg.method.l和finding.l。 | [方法条目](../source-audit.md) |
| 可选邮箱值、频控键与挑战主体的绑定 | 旧帖说忘记密码流程修改可选email会reset频控。 | [方法条目](../by-type/authn-session.md) |
| source map嵌入源码子集与重建分母 | 可读source map不保证整个项目源码。 | [方法条目](../by-type/info-secrets.md) |
| XML签名验证对象、转换链与业务消费对象 | XML导图并列SOAP重放/参数、XPath、实体/DTD/XInclude、签名包装、XSLT及资源耗尽，并注明未必均可利用。 | [方法条目](../by-type/xxe.md) |
| Grafana快照originalUrl从保存到按钮读者 | 图中POST /api/snapshots把originalUrl设为JavaScript URL，200返回快照字段，另一图有Open original dashboard按钮和弹窗；创建、持久保存、其他读者读取及实际点击仍需各自关联，不能由两图补跨用户链或全部匿名权限。 | [方法条目](../by-type/xss.md) |
| SERVFAIL与REFUSED到遗弃委派的证据距离 | 旧图把SERVFAIL/REFUSED及DNS provider清单当接管候选。 | [方法条目](../by-type/subdomain-takeover.md) |
| dangerouslySetInnerHTML命中与外来HTML消费 | 搜索dangerouslySetInnerHTML找到的是潜在HTML消费者。 | [方法条目](../by-type/xss.md) |
| URL下载字节上限与失败清理的权威状态 | 旧帖提出50GB下载到约15GB中断且chunk留存，仍缺测量/对象归属，不能从下载功能直接确认SSRF或整机DoS。 | [方法条目](../by-type/ssrf.md) |
| 多源管线的覆盖写入与实际下游集合 | 两张脚本图把发现/解析/HTTP/历史URL/kxss串接。 | [方法条目](../discovery/records-and-incremental.md) |
| 用户管理能力与可授角色上限 | User Access读写主体升级admin的描述需拆为允许管理谁、可授什么角色、是否允许自升，以及最终服务端能力。 | [方法条目](../by-type/idor-access-control.md) |
| 内核回调检测链中的PID代际与事件丢失 | FalconEye架构图从内核回调到PID map、hook处理、行为历史及有状态/无状态检测。 | [方法条目](../source-audit.md) |
| 方括号重解析声明与URL验证器和连接器差异 | 旧node-fetch帖把无协议的方括号字符串写成另一host/path形式，未保存版本或执行轨迹。 | [方法条目](../by-type/ssrf.md) |
| Django技术500模板的局部转义与异常前提 | create_user示例路径不是Django通用端点。 | [方法条目](../by-type/xss.md) |
| 设备多斜线路径、固件身份与文件输出解释 | HG659旧图含多斜线/点段路径、curl -k与passwd样式文本。 | [方法条目](../by-type/lfi-path-traversal.md) |
| RDP缓存拼图的缺片、时点与重组推断 | RDP Cache Stitcher图有缺片网格、隐藏已用重复块与自动排列。 | [方法条目](../discovery/records-and-incremental.md) |
| 左尖括号后的空格与真实HTML状态机 | 旧列表的空格片段`< svg`不能在HTML Data到tag-open语境中直接成为svg起始标记。 | [方法条目](../by-type/xss.md) |
| acr_values请求偏好与实际认证保证 | OIDC图仅有authorize请求的acr_values=otp+password和state。 | [方法条目](../by-type/oauth-oidc.md) |
| Flutter kernel制品与strings输出的源码分母 | 图展示assets/flutter_assets/kernel_blob.bin与strings输出文件output.dart；扩展名并不把可打印字符串重建成完整Dart源码，像素模糊的代码行也不能恢复秘密。 | [方法条目](../by-type/mobile-android.md) |
| Jira自定义字段名披露与dark feature的响应判据 | 旧帖QueryComponent!Default.jspa的CVE-2020-14179与Renderer用户枚举不同。 | [方法条目](../by-type/info-secrets.md) |
| 共享IP未知站点与域名虚拟主机路由 | 三图分别为历史A/NS回答、直接IP的Pantheon Unknown site及正确域名的正常HTTPS页面。 | [方法条目](../by-type/subdomain-takeover.md) |
| 名为unit tests的安全工具与实际状态副作用 | Swift-Attack帮助虽称unit tests，却包含系统/剪贴板/历史/文件采集、网络及模拟动作。 | [方法条目](../experiment-design.md) |
| 前导零DNS标签与有限枚举的实际名称集合 | 图用两个1至10循环分别拼disk和disk0，后者会包含disk010，并不等于固定两位十进制格式；disk7与disk07是两个DNS标签，不能先转整数合并。 | [方法条目](../discovery/passive-and-services.md) |

| 重置验证码状态差与仍被拒绝的并发声明 | 重置密码图中一行200/较长响应和多数422，只显示HTTP差异，选中面板还是请求；另一Apple图的UI与JSON明确Too many incorrect verification codes/hasError true。 | [方法条目](../by-type/authn-session.md) |
| 扫描skip配置与发现和验证的不同分母 | Dalfox管线提示保存输出并使用skip/onlydiscovery选项提速。 | [方法条目](../discovery/records-and-incremental.md) |
| 可编辑响应标志与最终持久写权限 | xx_update_xx=false改true能启用编辑的描述，首先证明的是可控客户端分支候选。 | [方法条目](../by-type/idor-access-control.md) |
| CVE标题、info级登录页匹配与执行漏洞 | Nuclei2.3.8图把CVE-2017-7692 RCE写入标题，但实际输出Squirrelmail Login、info等级及login.php URL。 | [方法条目](../targeted-fuzzing.md) |
| 参数形状矩阵与解析后的授权对象 | IDOR导图并列重复HTTP参数、重复JSON键、数组/对象包裹、路径/方法/Content-Type、UUID/数字ID、API版本与移动入口。 | [方法条目](../by-type/idor-access-control.md) |
| 组织关键词到ASN列表的格式和共享归属 | 旧amass管线把org输出按逗号取首列，再用xargs按逗号拆ASN并发调用；结尾还含可疑孤立引号。 | [方法条目](../discovery/passive-and-services.md) |
| APK URL正则排除与候选来源的保全 | apktool后正则提URL、删引号并排除google/github等词的管线，得到的是某一规则筛后的字符串集合。 | [方法条目](../by-type/mobile-android.md) |
| CI lint远程include的校验失败与取址副作用 | 旧GitLab请求对CI lint提交远程include，响应invalid YAML引用该URL，旁图有A/AAAA/HTTP事件。 | [方法条目](../by-type/ssrf.md) |
| eval异常通道中的示例输出与执行身份 | Python图以NameError显示eval调用，再以KeyError内uid字符串示意子进程结果；前段变量名还不一致，属于待核的示例材料，不能用绘制的Traceback替代原始执行轨迹。 | [方法条目](../by-type/cmd-injection-rce.md) |
| PassiveScan回调与扩展额外发出的请求 | 403 Directory Bypasser说明PassiveScan默认触发自动扫描，图High/Certain和多个路径200来自扩展自身标签。 | [方法条目](../discovery/records-and-incremental.md) |
| Cisco SAML字段与特定VPN界面的浏览器读者 | 保存请求写SAMLResponse并配/+CSCOE+/saml/sp/acs页面弹窗，仍需原始POST响应、字段到输出上下文、实际设备/用户界面和交互条件关联。 | [方法条目](../by-type/xss.md) |
| Azure管理面枚举与匿名Blob数据面的证据 | BlobHunter图先显示登录主体及两个subscriptions，第一段报告21个storage accounts、2个PUBLIC containers，第二段还在检查。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 同名URL数组拼接与校验和连接的解释分歧 | 原图将重复url参数变数组，再示意逗号拼接与@用户信息产生另一个主机，作者明确不是通用技巧。 | [方法条目](../by-type/ssrf.md) |
| S3历史ACL清单的资源层与READ_ACP语义 | Pastebin图的bucket_exists、AuthUsers/AllUsers及READ/READACP是旧扫描标签，还有NoSuchBucket异常与后行黏连，不能认当前所有资源或全部对象暴露。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Autorize长度判定、公开流量与有效主体隔离 | Autorize图含Bypassed/Is enforced?、长度对比及analytics/OPTIONS等公共流量，并显示临时Cookie配置。 | [方法条目](../by-type/idor-access-control.md) |
| 凭据API hook声明与调用和权限前提 | SharpHook帮助列mstsc/runas/powershell多进程与本地文件输出，说明的是意图和参数。 | [方法条目](../source-audit.md) |
| 网络诱饵事件到poisoner检测的归因 | HoneyCreds图显示SMB/HTTP客户端、诱饵配置、发送事件和Poisoned response日志。 | [方法条目](../experiment-design.md) |
| DWR参数类型、延时文本差异与实际测量 | 图DWR请求的string参数含pg_sleep(1)，正文却写pg_sleep(10)并使用曲引号/长破折号；这些原字节不能静默转换成ASCII后称原PoC有效。 | [方法条目](../by-type/sql-injection.md) |
| 文件泄露模板命中与统一错误页反例 | 私有InterestingLeaks模板图短时输出大量htaccess/htpasswd等路径及Low等级，但未展示matcher源码或实际正文。 | [方法条目](../targeted-fuzzing.md) |
| S3列举的截断信息与HTML对象浏览器origin | ListBucketResult图有MaxKeys1000、IsTruncated false和images/零字节marker，屏幕下部仍裁切；服务响应的集合边界与截图可见集合不同，目录样式键也不是可浏览真实文件夹。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| heap快照变化、地址复用与内存损坏判据 | Heappy图将多个snapshot、next/prev_size等字段和注释并列，可视地址/值变化不证明越界写、UAF或任意写能力。 | [方法条目](../source-audit.md) |
| 实验VPC图的路由、VPN路径与未部署节点 | AWS实验图的public路由指IGW、private仅local，另列WireGuard、SG端口及NACL标签。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 全局头替换的注入出处与盲通知去重单位 | 旧建议在Burp Match/Replace把盲XSS放UA/Referer，另一图称22次执行、Resolved及旧VRT版本。 | [方法条目](../discovery/records-and-incremental.md) |
| robots注释、User-Agent分组与路径模式来源 | 图中grep Disallow把#注释也收到集合，且去掉User-Agent分组、Allow和原URL。 | [方法条目](../discovery/web-and-api.md) |
| 代理修改响应与服务端反射的证据边 | 旧一分钟XSS步骤混写intercept response和在request尾加HTML。 | [方法条目](../by-type/xss.md) |

| AWS地址段匹配与租户及桶地域的分别归属 | onaws图把IP匹配到AWS subnet、EC2服务和eu-west-1。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 机器学习WAF反馈队列的评分与有效变异 | WAF-A-MoLE架构图展示mutation pool、priority queue、adapter与Target WAF反馈。 | [方法条目](../targeted-fuzzing.md) |
| localhost代理开关与实际浏览器流量归属 | 旧帖将Firefox的network.proxy.allow_hijacking_localhost开关推荐给localhost拦截问题。 | [方法条目](../discovery/records-and-incremental.md) |
| 哈希对象ID的字节契约与授权不变量 | seq到hashit再ffuf的管线用整数派生候选ID；算法名以外，确切输入字节、换行、字符编码、前导零及输出表现都决定是否对应实际对象。 | [方法条目](../by-type/idor-access-control.md) |
| JSON形状、查询操作符与Content-Type消费者 | API清单同时推荐数组/对象、布尔/null/数值、重复键、user[]及$ne形状。 | [方法条目](../by-type/api-property-pollution.md) |
| robots文本清洗的误截断与词表原始语义 | robots管线图的grep/awk/cut实际生成isallow等词：包含Disallow的注释也被收集，第二字段再无条件删首字符会把字段名而非路径截坏。 | [方法条目](../discovery/web-and-api.md) |
| CDX时间戳到重放URL与全文获取的不同阶段 | Wayback示意先查询CDX时间戳，再由bash echo组装重放URL。 | [方法条目](../discovery/records-and-incremental.md) |
| SSH协议banner与任意公钥认证的证据界线 | 旧帖把生成密钥、netcat看到SSH2 banner与所谓Race Hazard绕过串在一起。 | [方法条目](../by-type/authn-session.md) |
| DNS载荷参数与线上标签及分片重组预算 | DNSteal帮助写payload大小4..240、自选server/target、TcpOnly及延时。 | [方法条目](../discovery/records-and-incremental.md) |
| source配置、保留环境与侦察任务的权限扩大 | Lazyrecon图导出存储路径、GitHub token及Discord webhook变量，使用source加载配置，再sudo安装或sudo-E运行通配目标。 | [方法条目](../discovery/records-and-incremental.md) |
| 反序列化标题与PHP命令字段及Node解析栈的分离 | 同帖的PHP图直接POST cmd并显示www-data输出，未显示序列化对象；Node图出现JSON.parse/unserialize与500 Unexpected end JSON。 | [方法条目](../by-type/deserialization-rce.md) |
| reCAPTCHA脚本文本、DOM选择器与可执行上下文 | SQLMAP求助图在浏览器显示reCAPTCHA JavaScript文本，包含getElementById的hello选择器与隐藏token字段。 | [方法条目](../by-type/xss.md) |
| 二维码文本到scheme分派和WebView权限的链条 | 两帖QR提示扫码javascript确认，但图没有实际设备或扫码结果。 | [方法条目](../by-type/mobile-android.md) |
| iOS扫码入口的URL分派与脚本消费者 | 二维码提示本身不证明iOS扫码应用会导航javascript scheme。 | [方法条目](../by-type/mobile-ios.md) |
| 省略username与保留Bearer的身份对照 | API misconfiguration两图把username改空，但仍保留同一Bearer头；响应数据被黑块遮住。 | [方法条目](../by-type/authn-session.md) |
| phpunit路径与phpinfo响应的版本及执行归因 | 图请求phpunit eval-stdin路径，带GET正文并显示phpinfo/PHP7.4.20。 | [方法条目](../by-type/cmd-injection-rce.md) |
| document.write标记、同栈重复行与报告状态 | DOM Invader图document.write显示三条同栈值，标记位于属性和脚本边界；另一图两报告仍Triaged/Still being assessed。 | [方法条目](../by-type/xss.md) |
| DEX内存采集的进程选择与完整性范围 | frida-dexdump帮助说明默认前台、未指定PID时可能dump全部进程，并提供spawn、delay和deep选择。 | [方法条目](../by-type/mobile-android.md) |
| H2表单、FILE_READ与自定义alias的分段证据 | 四图从H2登录模板、自选嵌入库路径/用户名到FILE_READ结果及1.4.196 CALL REVEXEC的uid0输出。 | [方法条目](../by-type/sql-injection.md) |
| 退订能力与完整设置编辑的不同权限 | 旧提示称退订邮件含目标email可到设置页，且并非所有网站适用。 | [方法条目](../by-type/authn-session.md) |
| DOM URL成员清单与导航及HTML网络消费者 | DOM列表把location及其host/path/search等读取成员，与assign/replace/open、srcdoc、AJAX和XHR一起列作open URL参数。 | [方法条目](../by-type/open-redirect.md) |
| 语音信箱接管概念与枚举failure响应 | Uber帖声称通过语音信箱取得OTP，图实际是driver RPC手机号输入及Intruder多个200，选中JSON却是failure/Multiple drivers found。 | [方法条目](../by-type/authn-session.md) |
| ETW服务RUNNING、空日志与检测能力对照 | TiEtwAgent图显示服务RUNNING、进程列表和空agentlog，未显示注入事件被记录。 | [方法条目](../source-audit.md) |
| JSF选择对象、ViewState与删除后的权威状态 | ESET帖称创建受控victim user后替换欢迎消息ID并删除。 | [方法条目](../by-type/idor-access-control.md) |
| 企业邮箱资格与quoted local及投递解析 | 邮箱图包含大写域、quoted local、comment和SMTP注入声明。 | [方法条目](../by-type/authn-session.md) |
| DOM Invader合成origin与真实外部发送窗口 | DOM Invader介绍和[官方消息设置](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/settings/web-messages)说明工具可修改origin、注入canary及生成消息。 | [方法条目](../by-type/xss.md) |
| 算术模板标记与盲脚本回连的两个消费者 | 帖将48*53模板候选与盲脚本标签组合。 | [方法条目](../by-type/ssti.md) |
| 邮箱字段的多类字符串与消费者路由矩阵 | 邮箱建议并列XSS、模板/SQL、带外域名、&email参数和通配符。 | [方法条目](../expert-reasoning.md) |
| AV未检出计数与制品及动态运行的不同证据 | Sharperner配图声称2021一次26引擎扫描0检出，并混有广告。 | [方法条目](../experiment-design.md) |
| 2FA清单的挑战绑定与本地成功标志 | 十项图混合改response/status、代码重用/跨用户码、重置关闭2FA、缺频控和null码。 | [方法条目](../by-type/authn-session.md) |
| 用户名Base64令牌与服务器认证的不可伪造契约 | API帖示例把access_token放payment查询串，另图说token仅为用户名Base64。 | [方法条目](../by-type/authn-session.md) |
| Git索引推导对象路径与目录列表和源码完整性 | GitDump图逐项Fetching index/refs/logs，Parsing Index后继续objects路径。 | [方法条目](../by-type/info-secrets.md) |
| 数据库网络例程与HTTP和目录解析回连的分流 | 旧SQLi到SSRF帖把Oracle UTL_HTTP.request和MSSQL xp_dirtree共同写作HTTP。 | [方法条目](../by-type/sql-injection.md) |

| BOF模块枚举与句柄及系统调用权限 | FindObjects配图FindModule枚举clr.dll与多个PID。 | [方法条目](../source-audit.md) |
| 容器发行版与linuxkit内核及宿主身份 | Docker图同时出现Ubuntu18.04.2、Tomcat6文件、CentOS4.9/glibc2.3.4及4.9.125-linuxkit内核。 | [方法条目](../cloud/container-k8s-security.md) |
| API key跨管理员披露与角色降级后的权限版本 | 帖叙述管理员B读取管理员A的Base64 key，B降为User仍能用该key；High/Resolved标题没有具体响应。 | [方法条目](../by-type/authn-session.md) |
| 失效社交链接的用户名分配与官方信任链 | 旧Instagram/YouTube链接帖提出第三方用户名重新分配。 | [方法条目](../by-type/subdomain-takeover.md) |
| 恢复能力跨邮箱变更与2FA状态的身份绑定 | 密码重置自动进入Dashboard、邮箱变更后旧重置链接有效及认证不只login的帖子，应追恢复能力实际授权的账户与状态转换。 | [方法条目](../by-type/authn-session.md) |
| 移动预验证登录与Web验证合同的最终动作 | 帖声称Web先验证邮箱而移动端能先登录且响应含PII。 | [方法条目](../by-type/authn-session.md) |
| 函数别名逗号表达式与弹窗图的消费者证据 | 函数别名和逗号表达式建议依赖实际JS变量绑定、执行上下文及消费者；帖子称五个XSS却仅四张裁切弹窗，没有输入或调用栈。 | [方法条目](../by-type/xss.md) |
| XML resolver到调试服务的协议与执行边界 | 保存叙述把XML resolver、gopher和Java的TelnetDebugging串成RCE。 | [方法条目](../by-type/xxe.md) |
| 文本列提取与累计字典的原始记录合同 | hakrawler输出筛script取第二列、将转义点转换为换行后sort -u再tee -a、Cewl/cut管道都依赖具体输出格式；片段还含弯引号和间距问题。 | [方法条目](../discovery/records-and-incremental.md) |
| 重复注册与已完成状态的单次消费 | 重复signup叙述称触发四个ATO，但未保存四条链。 | [方法条目](../by-type/business-logic.md) |
| GetBucketAcl读权与Owner字段及对象访问 | S3 owner建议提供ACL查询候选。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| XML字段输入的解析层与数据库查询消费者 | productId放SQL表达式的图没有响应，另图用弯引号可能使XML本身错误；XML只是输入容器，不能由标签名归为XXE。 | [方法条目](../by-type/sql-injection.md) |
| ADB代理intent与有效网络及应用流量 | ProxySetter命令给的是代理配置意图，没有设备端生效及实际流量收据。 | [方法条目](../by-type/mobile-android.md) |
| GNU parallel字段重组与输出碰撞的覆盖分母 | 图中parallel按列重组目标、只取URL字段1和3，10个jobs运行Nuclei并用同字段命名输出；severity只保留critical/high/medium。 | [方法条目](../discovery/records-and-incremental.md) |
| JWT工具valid input与服务端算法和key合同 | HS256菜单和valid input表示工具接受了格式，不表示服务器验证了签名。 | [方法条目](../by-type/jwt.md) |
| 客户端filter移除与真实租户查询边界 | 帖将Grafana/Elastic查询称GraphQL并建议删filter/filterid，声称约30%能读额外数据。 | [方法条目](../by-type/idor-access-control.md) |
| AEM JSON元数据与完整私有内容和性能分开 | 图中.json包含sling OrderedFolder、dam相关及示例主题元数据，URL遮挡，帖提节时但缺前后图和耗时。 | [方法条目](../by-type/info-secrets.md) |
| 未验证邮箱预占2FA与锁定造成的恢复状态 | 未验证邮箱先注册再设2FA可能阻碍邮箱所有者恢复，另帖称IP block/用户lockout/captcha总应启用。 | [方法条目](../by-type/authn-session.md) |
| 设备名进入后台读者与2FA动作的独立关系 | Android/iOS设备名BXSS建议把改设备名与所有应用开启2FA连在一起。 | [方法条目](../by-type/mobile-android.md) |
| Laravel env默认值与活跃凭证的配置证据 | env图有localhost、空APP_KEY、默认样式数据库字段和遮挡mail，但缺取得文件的原始HTTP来源。 | [方法条目](../by-type/info-secrets.md) |
| AXFR训练zone的记录类型与公开性和范围 | DNSrr图给zonetransfer.me的AXFR记录，含TTL与NS/A/AAAA/PTR/HINFO。 | [方法条目](../discovery/passive-and-services.md) |
| API错误变体的schema认证与代理层归因 | 建议把数字改字符串、去字段、损坏JSON和删header/Cookie以寻找错误。 | [方法条目](../by-type/info-secrets.md) |
| KeyCredentialLink写入与实际证书映射及TGT | Whisker图显示属性更新、证书生成和提示下一步运行Rubeus；该阶段尚未证明目标身份成功获票或可用权限。 | [方法条目](../by-type/authn-session.md) |
| DOM书签span采集的集合类型与虚拟列表覆盖 | 书签console片段直接对getElementsByTagName返回集合用forEach且打印所有span。 | [方法条目](../discovery/records-and-incremental.md) |
| 邮件双斜线处理后的mailto消费者与HTML注入 | email HTML图显示双斜线处理后mailto scheme，第二哈希图内容相同。 | [方法条目](../by-type/xss.md) |
| RFD文本响应到下载名称和打开程序的消费链 | messagehistory TXT图含JS/PHP样式文字，但缺完整Content-Type、Content-Disposition、下载名与实际打开程序。 | [方法条目](../by-type/document-rendering.md) |
| SQLi读权限到页面写入和存储脚本的独立能力 | 图在正常static_pages_content字段旁标Inject Stored XSS，未展示真实注入。 | [方法条目](../by-type/sql-injection.md) |
| curl http_code的000与首跳和错误丢失 | shell循环打印http_code却压掉stdout/stderr，URL未引用且未跟随跳转。 | [方法条目](../discovery/records-and-incremental.md) |
| WordPress候选路径与插件名称及攻击计数 | wp-config备份/debug.log路径、Wpscvn的WP4.9.8和插件名只是候选层。 | [方法条目](../targeted-fuzzing.md) |
| YApi mock返回passwd文本与动态求值及文件读取 | YApi mock路径图显示passwd样式文本，缺实际输入、求值调用和命令结果来源。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 用户名保留名与路由优先级及安全handler | index.php作用户名后profile位于对应路径的叙述涉及命名空间与路由优先级。 | [方法条目](../by-type/business-logic.md) |
| CDN WAF子网列表的更新时间与租户归属 | YAML子网工具声称每日00UTC更新并覆盖CDN/WAF。 | [方法条目](../discovery/passive-and-services.md) |
| bbscope混合资产类型与public-only及当前规则 | bbscope图带public-only而结果混合域名、仓库、包和移动应用，token不复制。 | [方法条目](../scope-and-rules.md) |
| 分页终止与后台线程及CSV完整性 | H1 CSV图显示NEXT_PAGE、getScope、Thread.start、写文件及public skip，截图外的join/异常处理未知。 | [方法条目](../discovery/records-and-incremental.md) |
| 分号路径的授权检查与实际路由消费者 | 帖称admin/index.jsp403而加分号变200，Go403Bypass图13路径403/404、9头全403。 | [方法条目](../by-type/idor-access-control.md) |
| Nexpose SQLi恢复缓存与产品版本及当前响应 | sqlmap图显示resumed旧session、已有Cookie、PostgreSQL11.7和Nexpose<=6.6.48标签。 | [方法条目](../by-type/sql-injection.md) |
| 盲SQL总查询耗时与HTTP500的时序证据分母 | 盲SQL图212次查询、3460.94秒、24个HTTP500及遮挡currentDB/stored logs。 | [方法条目](../discovery/records-and-incremental.md) |
| Windows缓解支持表与实际架构及启用配置 | 旧Win7/8缓解表列SafeUnlink、NX、SMEP和参考材料。 | [方法条目](../source-audit.md) |
| 跨租户邀请的issuer目标与接受后成员状态 | 叙述User1 Org1把邀请orgid改Org2并带Org2邮箱，Critical/Resolved标题没有具体接受结果。 | [方法条目](../by-type/idor-access-control.md) |
| SQL拼接方言模式与注释原始字节 | SQL方言帖将MySQL双竖线写拼接并说块注释通常不工作。 | [方法条目](../by-type/sql-injection.md) |
| Cilium架构图与有效eBPF策略及身份覆盖 | Cilium图从Pod/CNI到kernel eBPF并标policy/logging/metrics，说明架构分层，未给当前部署、附着点、身份标签或有效规则。 | [方法条目](../cloud/container-k8s-security.md) |
| Intruder处理菜单与变换顺序及实际wire字节 | Burp图处理规则菜单Hash高亮、payload/request计数0、URL encode勾选。 | [方法条目](../targeted-fuzzing.md) |

| 重置查询后缀与账号限流的最终消费 | 重置POST图为429，追加查询的Intruder图为200且长度691；API网关轮换出口被称无限代理。 | [方法条目](../by-type/authn-session.md) |
| SSH代理存活与有效banner及认证收据 | Orbitaldump图同时有大量代理连接错误、156个SOCKS4、278个SSH banner、54个live与found1。 | [方法条目](../discovery/records-and-incremental.md) |
| TECL分块超时的原始字节与消费者对照 | 截图畸形分块约60174ms、正常请求65ms，并标possible TECL。 | [方法条目](../by-type/request-smuggling.md) |
| 认证SMB全文搜索与跳过文件的暴露分母 | MANSPIDER图使用admin认证、256线程并跳过大于10MB文件。 | [方法条目](../by-type/info-secrets.md) |
| 组织新增成员与导出私有字段的同意边界 | Pokedex示意加入用户后导出私有电话；功能遍历建议用两个用户观察收件箱、邀请与共同业务边。 | [方法条目](../by-type/idor-access-control.md) |
| 邀请approve参数与受邀者接受的主体绑定 | 邀请图把user_email与approve true并列，描述现有用户被添加。 | [方法条目](../by-type/idor-access-control.md) |
| 模拟身份的actor与subject及退出能力 | 跨组织target_user和full_access参数图、auth_token改变的建议把模拟身份视作可疑。 | [方法条目](../by-type/authn-session.md) |
| ACAO序列化Origin与带凭据浏览器读回 | 正文给出裸主机ACAO和ACAC true，另一图201返回组织字段并用星号。 | [方法条目](../by-type/cors.md) |
| 百分号解码与JS URI错误处理的实际sink | 编码JS URI示例结合析构onerror和throw，另文写prompt却声称alert。 | [方法条目](../by-type/xss.md) |
| 不同text与search入口的过滤比较 | Cloudflare配图一张text入口被拦截，另一张search路径出现prompt。 | [方法条目](../by-type/waf-bypass.md) |
| bogus comment与空HTML注释提前闭合 | 图片把单连字符形式概括为HTML5注释语法变化。 | [方法条目](../by-type/xss.md) |
| 文件删除success字段与方法授权的最终状态 | 自有上传455后delete图为200而success0；另帖只给GET他人对象401后建议DELETE，billing GET403/POST200也缺最终内容。 | [方法条目](../by-type/idor-access-control.md) |
| 图片获取的DNS与HTTP及SMTP协议证据 | 帖从图片URL回连推到25端口SMTP并建议扫描。 | [方法条目](../by-type/ssrf.md) |
| 支付Success参数与可信网关回执 | 把Cancel改Success后页面称已支付的建议缺权威账本。 | [方法条目](../by-type/business-logic.md) |
| 金额符号与余额预留及并发账本守恒 | 负金额、超过余额和race建议提供三种输入方向，没有实际交易结果。 | [方法条目](../by-type/business-logic.md) |
| 接收者数组的逐项权限与fanout预算 | receiverid从单值改数组被描述为发垃圾消息。 | [方法条目](../by-type/business-logic.md) |
| SSRF流水线的输出文件与最终输入集合 | 长图assetfinder/wayback写urls.txt，gau写1.txt，后续只消费1.txt；还有间隔引用和重定向语法不明确。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史源站IP与301响应头的消费者身份 | ViewDNS图含2021/2015历史IP，两个curl301分别带Cloudflare和Varnish。 | [方法条目](../discovery/web-and-api.md) |
| ASN扫描丢端口与主机协议归一化 | ScanApple长图先安装工具再广泛端口扫描，awk提第二列后接httpx和sort。 | [方法条目](../discovery/records-and-incremental.md) |
| file URL变量文本与实际本地读取者 | 两图在PHP实验中比较混入变量的file路径和普通passwd路径，并显示array。 | [方法条目](../by-type/lfi-path-traversal.md) |
| JSP控制字节与AJP映射的源码消费者 | 两张提示图将mod_proxy_ajp/mod_jk与JSP路径控制字节关联，未给实际源码响应。 | [方法条目](../source-audit.md) |
| 报表生成与PDF存储及下载的租户权限 | 导出reports/组织参数与PDF用户参数被称BOLA，内部分工被当绕过原因。 | [方法条目](../by-type/idor-access-control.md) |
| TLS Pass Through与可观察流量的覆盖缺口 | 帖子为减少代理噪声给提供者域名正则和TLS Pass Through配置。 | [方法条目](../discovery/records-and-incremental.md) |
| 证书subject搜索与各查询语言的资产归属 | FOFA/Shodan字符串把Set-Cookie、证书subject和TARGET组合，两个查询消费者的字段与语法不可直接互换。 | [方法条目](../discovery/passive-and-services.md) |
| OpenGraph二次图片获取的逐跳scheme合同 | 正文描述页面先获取HTML，再按og:image生成缩略图，提示file路径。 | [方法条目](../by-type/ssrf.md) |
| 反向RDP转发的既有客户端与出站权限 | Rconn图client已有3389、向server1111连出再暴露2222。 | [方法条目](../discovery/passive-and-services.md) |
| jQuery预过滤与option包装的版本分支 | 截图两个CVE标题重复但内部示例不同；[官方3.5.0说明](https://blog.jquery.com/2020/04/10/jquery-3-5-0-released/)和[3.5.1解释](https://blog.jquery.com/2020/05/04/jquery-3-5-1-released/)分别说明htmlPrefilter正则处理和旧浏览器option包装相关分支。 | [方法条目](../by-type/xss.md) |
| 密码重置helper表单与浏览器环境的真实状态 | 重置UI、POST302和Burp生成CSRF HTML使用当前Cookie；另一帖称JWT复制到Cookie后90%可CSRF。 | [方法条目](../by-type/csrf.md) |
| Joomla模板配置与跨版本条目的匹配 | Juumla图识别1.5.15却列多条3.x内容，configuration.php-dist标PossibleReadable。 | [方法条目](../source-audit.md) |
| loopback解析与自己机器的真实服务身份 | 两份不同hash图将域名解析127.0.0.1，再比较域名403和IP200。 | [方法条目](../by-type/host-header.md) |
| SMTP入队与邮件落盘及PHP include的断点 | PHP5.1.6实验可读passwd/proc，进程UID100；SMTP图仅250 queued PHP文本。 | [方法条目](../by-type/lfi-path-traversal.md) |
| ASM数据库差异与定时通知的动作边界 | SpiderFoot→SQLite/Datasette→Aquatone/截图→cron新增域名通知的方案同时包含采集、展示和外部发送。 | [方法条目](../discovery/records-and-incremental.md) |
| WordPress安装向导与活跃配置的写入状态 | 正文从wp-admin403而setup-config step1可达推可创建库和提权。 | [方法条目](../source-audit.md) |
| COOK组合与编码变换的候选分母 | 四张长图展示组排列、范围、日期、空分隔符、大小写/leet/Base64/hash及BasicAuth。 | [方法条目](../targeted-fuzzing.md) |
| 远程JSON path转basename后的来源丢失 | COOK长图每次取远程集合，JSON path经basename、sort去重再smartjoin短文件名候选。 | [方法条目](../discovery/records-and-incremental.md) |
| 无效方法与字段错误的解析层归因 | 建议把age改数组、引入Unicode或改方法，且把http//缺冒号描述成分号问题。 | [方法条目](../targeted-fuzzing.md) |
| 历史报告Markdown与新回归收据 | 旧帖建议Copy Markdown重复报告以检查修复。 | [方法条目](../reporting.md) |
| SQL截断注册与登录规范化的身份一致性 | 长邮箱注册图302到back.php，随后200 CSS Library页未显示身份。 | [方法条目](../by-type/authn-session.md) |
| 保单HTML属性与私有PDF制品的不同权限 | 邮件/支付UI、rawHTML GrepExtract和Intruder200展示保单相关字段；字段出现与跨账号私有文档读取不是同一结果。 | [方法条目](../by-type/idor-access-control.md) |
| dot HISTFILE的执行语义与只读取证 | 帖子把dot HISTFILE当快捷查看历史。 | [方法条目](../source-audit.md) |
| MongoExpress会话与后端数据库认证的分层 | MongoExpress图显示admin/config/local/testdb、MongoDB4.4.6、8086以及连接统计。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 433MHz解码校验与发射者身份 | rtl433图含2018时点、433.92MHz、Bresser/Nexus温湿度、SNR和checksum。 | [方法条目](../discovery/passive-and-services.md) |
| TXT平台关联与选点快照及第三方令牌归属 | DNS TXT平台验证、MoneyScope3196域名/1824TLD/5日数据与第三方Google/FB token的奖励问题分别提供关联、选点或凭证线索。 | [方法条目](../scope-and-rules.md) |
| Akamai ARL上游获取与展示origin的分离 | ARL正文路径7/0/33/1d与截图7/100/33/1d不同，另含上游citysearch和SVG候选。 | [方法条目](../by-type/xss.md) |
| 代理头与方法覆盖的逐消费者信任 | 长图混列ClientIP/XFF/XOriginalURL、重复Host、absolute URI、http0.9、折行、MethodOverride及Accept路径。 | [方法条目](../by-type/host-header.md) |
| HTTP制品服务与子进程队列的执行证据 | LightMe图为脚本服务8080 HTTP200、MAX child-process wait；DNSStager图仅help。 | [方法条目](../source-audit.md) |

| Gopher预制字节与数据库握手的协议条件 | SSRF提示图给MySQL Gopher示例但明确truncated，描述SHOW DATABASES而无实际响应。 | [方法条目](../by-type/ssrf.md) |
| 人脸检测截图与隐私变换效果的评价 | Ruse宣传改变照片以阻识别，图片却是Original和FaceDetected，含landmark和概率。 | [方法条目](../experiment-design.md) |
| APK发布版本与签名及变体覆盖 | dapk图5页138 releases只显示四个版本下载行。 | [方法条目](../by-type/mobile-android.md) |
| 参数发现的heuristic与差异因子 | Arjun图一张v2beta列url/page/filter及httpcode/body因子，一张2.1显示8个heuristic名。 | [方法条目](../discovery/web-and-api.md) |
| 用户集合与版本及单对象的公开字段合同 | v3/v4 users集合被拒，而编号对象返回id/name/username/Public_email。 | [方法条目](../by-type/idor-access-control.md) |
| 移除数字路径段与斜线规范化的同对象条件 | 原路径含数字段返回403，移除该段并用双斜线或反斜线后称200。 | [方法条目](../by-type/idor-access-control.md) |
| 域名与范围IP交集的时点和共享租户 | 建议大IP范围内找公司域名并取落在in-scope地址的交集。 | [方法条目](../scope-and-rules.md) |
| mutation输入subValues与返回resolver的字段权限 | 低权创建Value时加入subValues空数组，据称响应暴露管理员隐藏子值，卡片只写mutation且对象名遮挡。 | [方法条目](../by-type/graphql.md) |
| InfluxDB查询错误到HTML提示的输出消费者 | InfluxDB UI1.0/Server1.0图包含查询语法错误、反射和alert，数据库语句未成功。 | [方法条目](../by-type/xss.md) |
| 移动账户数据的编码外壳与XML实体读者 | 交通App图从账户ChangeMyData入口到text/plain编码请求，响应text/html内呈XML与passwd行。 | [方法条目](../by-type/xxe.md) |
| 代理替换JSON与末端扩展日志的原始收据 | MatchReplace图启用UA/Referer/body与escapedJSON载荷，另一帖要求Logger++置最后。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史SQL快照日历与实际内容暴露 | Google SQL候选后查询Wayback图为四次capture，日期2017至2021，没有显示SQL全文。 | [方法条目](../by-type/info-secrets.md) |
| 仓库关键词与提供者标记的活跃配置证据 | Git-Secret图选master并检查README/apikeys等，输出Google/AWS标记。 | [方法条目](../by-type/info-secrets.md) |
| HTTPS代理hook定义与插件注册及实际wire | Proxverter图定义request hook并启动127.0.0.1:8081 HTTPS，未展示插件注册或客户端链路。 | [方法条目](../source-audit.md) |
| 研究服务器目录索引与历史命令的秘密层级 | WEBrick索引图列bash_history/.ssh、工具目录和大小，历史命令截图含扫描/删除等文本。 | [方法条目](../by-type/info-secrets.md) |
| LAPS的LDAP认证主体与密码读取ACL | SharpLAPS图给认证参数并显示masked密码输出。 | [方法条目](../by-type/info-secrets.md) |
| 认证状态机的挑战输入输出与合法转移 | Raider介绍将每步视作state，带Cookie/header/CSRF输入输出。 | [方法条目](../by-type/authn-session.md) |
| 联系表单延迟后台消费的时间和读者身份 | 叙述联系表单两日后后台触发BXSS且截图含支持数据。 | [方法条目](../by-type/xss.md) |
| 支付确认重放与单次交付账本 | 图片描述数字商品一次支付后重放确认请求可多次获得产品，奖卡称无限。 | [方法条目](../by-type/business-logic.md) |
| RSS订阅保存与后台feed获取的回连归因 | 正文只说profile关联RSS feed并发现盲SSRF，卡片称内网发现。 | [方法条目](../by-type/ssrf.md) |
| 多个登录注册入口的同身份策略矩阵 | dork图列login/signup/dashboard等，称各入口保护可能不同。 | [方法条目](../by-type/authn-session.md) |
| API hash解析名称与动态调用的分层 | IDA图显示hash映射LoadLibrary、VirtualAlloc和WinHttp函数，API Monitor图却No process monitored。 | [方法条目](../source-audit.md) |
| jpeg.php声明与保存位置及解释器消费 | 上传图filename为jpeg.php且MIME image/jpeg，另一图UI只列两个SVG名。 | [方法条目](../by-type/file-upload.md) |
| 单字符端点模式与ID关键词的候选限制 | 提取端点的regex在slash后字符类没有重复量词，不能覆盖多字符路径；另例默认grep查id模式，被称最简单IDOR。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史JS子串过滤与当前源码集合 | gau图按.js子串过滤并排除.jsp/.json，使用追加输出；JS列表不证明当前响应是JavaScript。 | [方法条目](../discovery/records-and-incremental.md) |
| 来源开关与队列inactive的结果完整性 | Sigurlfind3R help列include/exclude/use/list sources，WARCannon图DeployYES但JobINACTIVE和0Messages。 | [方法条目](../discovery/records-and-incremental.md) |
| 证书issuer字段与id查询的标识合同 | crt.sh图取JSON issuer_ca_id后接id查询并grep SHA1。 | [方法条目](../discovery/records-and-incremental.md) |
| PDF打印页脚URL标识与能力传播 | 打印PDF页脚显示Booking对象路径，正文把GUID或token统一视作危险。 | [方法条目](../by-type/info-secrets.md) |
| PHP非严格比较的操作数与版本边界 | 缺严格比较提示需核实真实类型。 | [方法条目](../by-type/authn-session.md) |
| cookieless会话路径到输出属性的消费链 | ASP.NET图A路径含引号/事件样文本并有alert1，另图只列ArchivedMedium报告。 | [方法条目](../by-type/xss.md) |
| 域名JSON提取与重复DNS行的观察身份 | Anubis regex列表末尾带大括号，sonarbyte图重复api/根域/www，RapidDNS主页给大总量。 | [方法条目](../discovery/passive-and-services.md) |
| JS字符串转义与实体URI的解析顺序 | productId单引号示例用编码空白换行及find(alert)，embed和formaction示例使用HTML实体。 | [方法条目](../by-type/xss.md) |
| Base64文本与eval消费者的语法有效性 | SVG/eval/atob片段被称绕过，但只读解码其字节为XSS haxor，没有可用JS表达式。 | [方法条目](../by-type/xss.md) |
| HTTP方法矩阵的同资源与最终权限 | legacy图GET/HEAD403、POST/OPTIONS200，其他方法405/501/400。 | [方法条目](../by-type/idor-access-control.md) |
| 银行响应RC与PIN的权威后端状态 | 两图分别RC0109 BLOCKED和RC0102成功并提示建立PIN。 | [方法条目](../by-type/authn-session.md) |
| Nexus3.14版本边界与读取和执行能力 | 帖称小于3.14.0，但图Server3.14.0-04。 | [方法条目](../source-audit.md) |
| ProxyShell模板命中与RCE链的独立验证 | Nuclei2.2.0图一规则标CVE34473/critical并列多个URL，未给matcher或有效载荷结果。 | [方法条目](../source-audit.md) |
| 同一消息在Web与iOS WebView的渲染差异 | 正文称消息过滤后Web未触发，却在iOS App WebView触发。 | [方法条目](../by-type/mobile-ios.md) |
| profile图片UUID与聊天内容对象权限 | 聊天机器人帖从profile图片UUID改用户聊天请求而称管理员聊天披露，卡片无内容。 | [方法条目](../by-type/idor-access-control.md) |
| 游戏双会话与评论删除的关系权限 | 游戏建议两个自有账号隔离会话交换user/object参数；评论图六步叙述公开comment ID后可删除。 | [方法条目](../by-type/idor-access-control.md) |
| TinyXSS长度与浏览器和能力条件矩阵 | TinyXSS图列15样例与script/style/eval/frames、name/URL控制、innerHTML及浏览器标签。 | [方法条目](../by-type/xss.md) |
| Ghost授权CodeInjection与支持聊天注入的边界 | LiveChat HTML注入标题配Ghost CodeInjection设置图，说明主题header/footer用于插入代码。 | [方法条目](../by-type/xss.md) |
| DOM导航与文档解析及XHR的不同sink | 所谓15个DOM重定向参数混location属性、assign/replace/open、srcdoc、Ajax和XHR。 | [方法条目](../by-type/open-redirect.md) |
| Karton产物hash与静态动态任务的队列合同 | Karton图区分producer/classifier/unpacker、动态dump、静态配置、报告消费者。 | [方法条目](../source-audit.md) |
| Digest降Basic的challenge与凭证作用域 | 正文称SSRF诱导Digest降Basic泄漏API凭证。 | [方法条目](../by-type/ssrf.md) |
| 组织成员信息与员工email字段的恢复能力 | 邀请用户进入组织后可见信息被称IDOR，经理员工接管标题图却仅email输入/返回不同。 | [方法条目](../by-type/authn-session.md) |

| JWT声明生成与验证入口的类型和时间合同 | jwtXploiter帮助图列None、HS256、RS256、键文件、声明数值/字符串默认处理、iat/exp/nbf增减及独立verify/find-key选项。 | [方法条目](../by-type/jwt.md) |
| 厚客户端拦截记录的请求级覆盖 | 厚客户端捕获图显示Burp拦截login.live.com的POST JSON与登录窗。 | [方法条目](../discovery/client-and-cloud.md) |
| gitconfig远程指针与备份文件内容的分层 | gitconfig提示图在remote.origin.url放备份路径；gau过滤.zip的正文则把候选直接叫P1。 | [方法条目](../by-type/info-secrets.md) |
| 历史URL流水线的覆盖追加和阶段来源 | 侦察图串waybackurls、gauplus、sed、grep、sort、anew、wurl与gf；多个阶段输出文件名和覆盖/追加方式不一致，还删中间文件。 | [方法条目](../discovery/records-and-incremental.md) |
| 后利用管理菜单与首次执行因果 | Bantam图有www-data、PHP版本与Eval/System/FileBrowser菜单，CamPhish图选择隧道和模板。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 接口UP状态和证书指纹的观察对象 | 命令资源图示ip addr筛state UP、跨日志目录tail/xargs、openssl x509指纹。 | [方法条目](../discovery/passive-and-services.md) |
| tko-subs发现模式与占有开关的授权区分 | tko-subs帮助列provider CSV、域输入文件、DNS服务器/端口、线程、平台凭证与takeover开关。 | [方法条目](../by-type/subdomain-takeover.md) |
| WebDAV写入与脚本handler执行的两张收据 | 正文描述WebDAV PUT PHP返回201；另一报告邮件自述PUT上传及反向shell。 | [方法条目](../by-type/file-upload.md) |
| JSON源码字符串与真实HTML消费之间的缺口 | view-source图显示JSON值里iframe javascript字符串；另一正文把img onerror中的alert(whoami)当反射XSS升RCE。 | [方法条目](../by-type/xss.md) |
| 图片触发注销的读者与重复消费条件 | 保存[1/2]正文提出把注销链接放img src，使组织成员读取后退出。 | [方法条目](../by-type/csrf.md) |
| urlhunter日期关键词与本地NSE目录的能力界限 | urlhunter图给关键词文件、日期和输出参数；nscript别名列本地Nmap脚本再grep。 | [方法条目](../discovery/records-and-incremental.md) |
| OTX订阅情报API示例与敏感密钥影响 | API清单图示OTX subscribed pulses端点、X-OTX-API-KEY、成功结果、Authentication required及64字符regex。 | [方法条目](../by-type/info-secrets.md) |
| OAuth缺email声明后的自填邮箱和保留地址政策 | 正文描述去Facebook email scope后应用要求自填邮箱，可填原本禁止的admin地址；截图回信称regression并奖励。 | [方法条目](../by-type/oauth-oidc.md) |
| 未回复等待与企业处理流程的证据边界 | VDP流程图解释应用、基础设施、VM、SOC和管理团队可能处理报告；正文因4/5天未回复焦虑。 | [方法条目](../reporting.md) |
| 扩展名与配置文件及编码NUL的不同处理层 | 后缀图混PHP/ASP源文件、配置、handler扩展；正文另列双后缀、大小写、点/空白、%00与反斜线x00。 | [方法条目](../by-type/file-upload.md) |
| SGXRay模型反例与实际构建覆盖 | SGXRay图从enclave应用构建so，extract-bc取得LLVM输入，再由CLI输出Verified或Error+Counterexample。 | [方法条目](../source-audit.md) |
| 购物车cookie标识与任意用户读写的证据差距 | 正文称Ud参数导致三百万用户读写；图实际cart view GET带u_ID_COOKIE，返回JSON成功及HTML字段。 | [方法条目](../by-type/idor-access-control.md) |
| PyPI审计warning排名与安装制品的关联 | AuraBorealis图有highest warning count、severity、日期变化与单包检查链接。 | [方法条目](../source-audit.md) |
| Jsleak模式输入与GitSecret分支命中的验证阶段 | Jsleak帮助只列JSON输出、模式文件和verbose；GitSecret图选master并打印provider key模式命中。 | [方法条目](../by-type/info-secrets.md) |
| 空格过滤候选的shell展开和变量名条件 | 图建议花括号、Ifs变量和tab形式。 | [方法条目](../by-type/cmd-injection-rce.md) |
| GitHub查询类别与拼写以及fresh筛选的漏项 | GitHub图在Repositories页对stie.com keyword返回零；另一笔记列org/user/language/NOT及关注fresh。 | [方法条目](../by-type/info-secrets.md) |
| PrintNightmare本地样例与远程执行路径的区别 | 保存alt说明该PowerShell脚本实施LPE；图新建本地管理员、runas及本机whoami/localgroup。 | [方法条目](../by-type/cmd-injection-rce.md) |
| JDWP服务识别成功与信息脚本失败 | JDWP图27000 open并识别协议版本，jdwp-info却ERROR；另端口Jetty HTTP401。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Selenium已登录资料采集与权限边界 | FisherMan日志称hidden mode、logged in、访问profile和收集div选择器。 | [方法条目](../discovery/client-and-cloud.md) |
| Forwarded复合头与403基线的逐字段对照 | 正文写Forward，截图实际Forwarded的for/by/host同时修改，返回200文章分页；第二图独立CloudFront403错误。 | [方法条目](../by-type/host-header.md) |
| 静态零检测与AMSI运行时效果的独立收据 | AMSI图含混淆PowerShell反射GetType/GetField/SetValue及0/57静态扫描。 | [方法条目](../source-audit.md) |
| Unicode编码候选与实际响应分隔字节 | 正文将UTF8百分号编码序列称CRLF并泛称Java可用。 | [方法条目](../by-type/crlf-response-splitting.md) |
| JSON字段路径提取与HTTP路由发现的分离 | JSON图有address对象和friends数组，工具输出/address等与/friends/1。 | [方法条目](../discovery/web-and-api.md) |
| accesslogs目录与日志中认证资料的分层影响 | 正文描述/accesslogs/目录索引、日志文件和700用户/管理员密码。 | [方法条目](../by-type/info-secrets.md) |
| AutoRepeater全替换的范围和请求因果 | 两张图配置Request Body Regex Match与Replace All，把URL样式字符串换为OOB地址。 | [方法条目](../by-type/ssrf.md) |
| 表单分页爬取与POST评估任务的终态 | Brutus图列scrapethissite多个forms?page_num以及Beginning POST evaluation。 | [方法条目](../experiment-design.md) |
| 恢复邮箱多值输入的查询和发信绑定 | 正文列email分隔符和JSON数组；图为旧框架重复参数first/last/list规则。 | [方法条目](../by-type/authn-session.md) |
| SMB凭证验证与命令执行的动作权限 | Keimpxhelp列目标/域/密码/NTLM hash、线程、batch、SMB命令和OS命令列表。 | [方法条目](../by-type/authn-session.md) |
| 元数据JSON字段与凭证有效性的分层 | 生产SSRF题的图片显示169.254元数据IAM security-credentials路径及Code、Type、Key、Token、Expiration字段，值均遮掩。 | [方法条目](../by-type/ssrf.md) |
| 内存PE导出与样本分析完成的不同产物 | ProcessDump图列chrome多个进程和PE/DLL导出文件。 | [方法条目](../source-audit.md) |
| 鸣谢页面变更与原始贡献证据的留存 | 图片对比Citrix鸣谢在2021年3月和8月的文字。 | [方法条目](../reporting.md) |
| SQL候选清单的参数类型和零延迟反例 | 一帖把q引号/数组/注释/concat清单称100%发现SQLi；另一time-based样例sleep(0)。 | [方法条目](../by-type/sql-injection.md) |
| localhost候选写法与实连目的地址的绑定 | 正文列整数、八进制、hex、短IPv4、DNS别名、IPv6 loopback及未指定地址写法。 | [方法条目](../by-type/ssrf.md) |
| Android代理TLS失败与pinning绕过成功的界限 | 教程题为Frida/Burp/GenyMotion绕pinning，图却有多域SSL negotiation fatal alert、0请求和手机offline。 | [方法条目](../by-type/mobile-android.md) |
| DSStore标题与SymfonyProfiler错误页的组件错配 | 正文称DSStore/Laravel信息泄漏，保存图为SymfonyProfiler Token not found。 | [方法条目](../by-type/info-secrets.md) |
| 图片魔数和multipart嵌PHP与执行链的缺口 | PNG/JFIF hexdumps显示格式头；multipart PUT的file.png/image/png内嵌PHP，仅请求没有响应。 | [方法条目](../by-type/file-upload.md) |
| AWS类别表中的对象动作与本机路径区别 | 正文列S3公开read、认证write、目录路径、POSTpolicy和Lambda；图下半截还出现反向代理/Cognito类别，内容裁切。 | [方法条目](../cloud/cloud-misconfiguration.md) |

| 脚本与爬虫候选流水线的来源和字段保持 | JSSpider图含同脚本重复及第三方域；gospider串联grep状态、awk第五列、qsreplace和dalfox的文字没有真实漏洞结果。 | [方法条目](../discovery/web-and-api.md) |
| MFA重发动作和预启用状态的分层 | 正文把resend请求POST改DELETE后删除2FA设置称绕过；图报告仍为P3 New。 | [方法条目](../by-type/authn-session.md) |
| 方法脑图节点与实际验证产物的对应 | 两份Frogy图把域/subdomain/app/IP/cert、端口/OSINT、扫描工具和手工unexpected/extra/less/sequential input组合。 | [方法条目](../hunting-strategy.md) |
| WebSocket消息中的身份字段与握手授权 | 两张WebSocket测试图分别出现SessionID/customerLogout以及customerProfileChanged、目的用户名；缺握手cookie、Origin和实际授权主体。 | [方法条目](../by-type/authn-session.md) |
| 站点摘要中的状态指纹和真实内容覆盖 | goverview图给HTTP200、时间、8322长度、checksum、CSP和favicon指纹。 | [方法条目](../discovery/web-and-api.md) |
| 供应链图中源码构建和制品的八个边界 | SLSA图列A至H：不当源码、源码管理、后续修改、构建平台、依赖、CI绕行、仓库和消费者的风险点。 | [方法条目](../by-type/cicd-supply-chain.md) |
| 云身份字段与本地文件标题的证据错配 | 一帖列crossdomain、SVG、文件处理与元数据候选，两图显示云IAM credential JSON；标passwd的图仍给元数据URL和Code/Type/Token/Expiry结构。 | [方法条目](../by-type/ssrf.md) |
| 代码与情报索引的类型时间和授权边界 | grepgithub半百万仓库宣传、Phonebook域/URL结果及多站代码查询图都给索引线索。 | [方法条目](../discovery/passive-and-services.md) |
| 权限关系图中的可能路径与实际动作 | adalanche图为2targets、19 possible pwns、7users、1group、0computers，未给每条边真实动作结果。 | [方法条目](../by-type/idor-access-control.md) |
| Profiler候选路径与可读性能数据的分离 | SymfonyProfiler图列app_dev及_profiler等候选路径和Open instances，没有保存有效profile数据。 | [方法条目](../by-type/info-secrets.md) |
| Webhook校验解析和取回解析的时刻区别 | 正文描述Webhook域名先正常解析后变127地址/端口21并出现内部error，缺具体socket取回证据。 | [方法条目](../by-type/ssrf.md) |
| Host变体中的请求目标和代理消费者 | 十种变体图含Host前缀/空白/重复、absolute URI、空行、XFH、另一host/端口/IP；反向代理图仅internet→proxy→server结构。 | [方法条目](../by-type/host-header.md) |
| 认证头长度与资源耗尽的因果对照 | 正文用Basic/NTLM约20与约二百万字符比较3秒和3分钟，自述未给服务资源、队列或重复测量。 | [方法条目](../experiment-design.md) |
| OAuth清单按发行传输和消费阶段重排 | 完整清单图列access/refresh token、code、泄漏、scope、redirect、CSRF、replay、credential等；另一正文把请求body含token直接列问题。 | [方法条目](../by-type/oauth-oidc.md) |
| iOS采集层与哈希输出选项的证据合同 | MEAT帮助分别列logical AFC jailed和filesystem path，以及md5/sha1和输出选项。 | [方法条目](../by-type/mobile-ios.md) |
| PHP参数名称折叠与原始字节保留 | 正文列点/空格/account方括号等；图显示account_id与未闭合account[id输入折叠后只留一个_GET值，缺PHP版本。 | [方法条目](../by-type/api-property-pollution.md) |
| 分享与提案发送之间的跨动作能力合同 | 正文把POST shares替为data_requests/id/send_proposal，界面原先不显示发送能力；图只是报告triaged。 | [方法条目](../by-type/idor-access-control.md) |
| 重定向端点与脚本scheme消费的两段保存线程 | 保存1/2给external-link.jspa url候选，保存2/2自述javascript对话框成功，没有执行origin/浏览器图。 | [方法条目](../by-type/open-redirect.md) |
| unescape百分号算法与源码词法转义的区别 | 两帖把百分号tab和反斜杠x/u写法归为unescape自动转换。 | [方法条目](../by-type/xss.md) |
| 扫描进度更新与误报质量验证的不同收据 | HawkScan1.9 changelog列百分比、行数、实时error、json/csv/txt和降低误报的描述；trick3st图20 running但只有2成功节点。 | [方法条目](../discovery/records-and-incremental.md) |
| 可写注册表和检测红标到特权消费的缺口 | Reg1c1de帮助列HKLM可写、属性与日志；BeaconEye图仅两红色进程/monitoring2。 | [方法条目](../source-audit.md) |
| 恢复令牌返回端点与重置消费的同一绑定 | 正文写resetPassword，而图为getPasswordToken username后JSON id/token/stamp；没有认证上下文或实际重置终态。 | [方法条目](../by-type/authn-session.md) |
| GraphQL批量能力与逻辑操作预算 | 正文推荐BatchQL的batch、CSRF和introspection；另帖Graphw00F仅指纹标题。 | [方法条目](../by-type/graphql.md) |
| 模板引用输出与模板检测命中的分离 | wmn图按Nuclei template ID产生四个引用URL，没有HTTP匹配请求或漏洞结果。 | [方法条目](../reporting.md) |
| 2FA秘密可读与认证后的持续用途 | 正文引用旧VRT下2FA秘密仍可获得的P4分类，以及gauth_token泄漏标题；没有当前规则或令牌内容/消费证明。 | [方法条目](../by-type/authn-session.md) |
| 通配符DNS过滤的随机对照和空输入风险 | massdns/wildcard文字使用dig样例含http前缀、egrep排除和共享IP；缺实际解析收据。 | [方法条目](../discovery/passive-and-services.md) |
| 修改签名文件的工具自述与平台验证 | SigFlip图给msbuild、输入/输出SHA1不同、padding/optional header及signed标志，没有Windows独立签名验证。 | [方法条目](../source-audit.md) |
| WEB-INF配置内容与标题拼写的实际读边界 | 正文路径写.EB-INF而图为WEB-INF/web.xml，可见JavaEE/Spring配置；另帖Confluence特殊路径只列pom/seraph/decorators候选。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 合法sudo与页面指纹不替代首次执行 | SSH key RCE题图显示admin、sudo密码提示后root；Confluence检测图只GET doenterpagevariables并grep form action后标Vulnerable。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 报告编号错配与debug摘要的最小事实 | Mailru正文报告号与图1083543不同；图resolved/critical摘要列AWS、SMTP、DB、Django等类别，未展示原始秘密。 | [方法条目](../reporting.md) |
| 结构字段进入可调用消费者的因果链 | locale JSON含system/id的图与Includes标签中的uid1000/www-data响应关联；未保存受控基线或处理实现。 | [方法条目](../by-type/api-property-pollution.md) |
| 每日资产差异与漏洞差异的版本绑定 | UML图为daily cron：scope输入、多工具、dedup、每日log、与前日比对、DB及带auth的web查看。 | [方法条目](../discovery/records-and-incremental.md) |
| 文件移除成功响应与对象终态 | removefiles图提交file_id并得到HTTP200 success_0，正文称IDOR/DoS。 | [方法条目](../by-type/idor-access-control.md) |
| Windows路径读取与远程include的不同消费者 | LFI→RFI图片以Windows PHP/SMB share和allow_url_include/fopen禁用为提示；可见路径只有单前导反斜杠。 | [方法条目](../by-type/lfi-path-traversal.md) |
| accepted金额和发现难易的独立事实 | Google图显示accepted但奖励稍后；Synack500图题为Blind SSRF internal port scan，缺端口技术证据；重定向自述1150条无查询数据。 | [方法条目](../impact-and-acceptance.md) |
| 邮件标识中的换行候选与真正输出字节 | 用户名拼接正文列百分号0a再0d及链接文字，顺序为LFCR，没有实际生成消息或header结果。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 注入技术菜单远程管理与实际执行动作 | GoPurple帮助列13种技术且server8000无incoming；SharpStrike图显示WMI/CIM主机身份与进程表；Penelope图已有PTY后的脚本/文件操作。 | [方法条目](../source-audit.md) |
| S3对象清单中的文件名与敏感读取分层 | S3图列versions、gz、signature和工具zip等键，正文建议AWS/recon命令；未保存内容、下载权限或秘密字段。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| JWT算法文字与密钥信任来源的校正 | JWT图把HS256写为symmetric encryption，并列alg None/RS与HS、kid、jku/jwk/x5u/x5c等候选。 | [方法条目](../by-type/jwt.md) |
| 数量小数与计价交付合同的同一口径 | 正文用quantity从1变0.1、234变23.4说明逻辑问题，没有计量单位、订单或交付收据。 | [方法条目](../by-type/business-logic.md) |
| 邀请预占和真正加入组织的状态门 | 一帖邀请未注册邮箱会自动建team；另一org/team邀请图企业回复只发email、无法join组织。 | [方法条目](../by-type/business-logic.md) |
| IIS配置可下载与实际秘密字段的区别 | web.config图为200 application/octet-stream及enableVersionHeader=false、removeServerHeader=true；正文称影响低无奖但修复。 | [方法条目](../by-type/info-secrets.md) |
| 旧请求再登录后的cookie冻结对照 | 正文称logout/password reset后旧profile edit失效，登录后旧请求又成功，没有保存重放所用cookie。 | [方法条目](../by-type/authn-session.md) |
| 历史URL退出截图的独立无会话验证 | 正文建议收集认证后的历史URL，logout后用aquatone；没有保存实际私有响应。 | [方法条目](../by-type/idor-access-control.md) |
| 电子签名文档在各读者和存储阶段的origin | 电子签名图从APP发文档到recipient签名再到多云存储；payload图列事件属性、实体、引号及localStorage读取，未保存真实sink。 | [方法条目](../by-type/document-rendering.md) |
| 表单线索转测试参数的类型和副作用合同 | 正文建议HTML input属性/data schema用于ffuf/jaeles；另一每API都fuzz观点配白皮书封面。 | [方法条目](../targeted-fuzzing.md) |
| 邮箱旧验证链接与对象版本和用途的绑定 | 正文描述未验证账号改邮箱、验证新邮箱后使用旧验证link导致删除；图只有250奖励。 | [方法条目](../by-type/authn-session.md) |
| 公开转私有后的关注关系终态 | 正文为A follow B→unfollow→B改private→重放旧follow，称200再次关注；图只是250奖励。 | [方法条目](../by-type/idor-access-control.md) |
| 图片URL的浏览器嵌入与后台取回区分 | 正文问网页接收任意图片URL能做什么，没有保存backend取回请求。 | [方法条目](../by-type/ssrf.md) |
| 恢复客户端参数构造与服务端挑战绑定 | Android Java图向auth/flashcall_account_recovery构造cuid、encrypted_phone_numbers和cli等字段，缺服务端回复/校验。 | [方法条目](../by-type/mobile-android.md) |
| MFA提示与最终认证会话的不同阶段 | TrevorSpray图两账号、1 valid，并提示MFA in use，缺最终会话或资源访问。 | [方法条目](../by-type/authn-session.md) |
| MinIO目录视图与默认凭证有效性的分开确认 | 正文提默认帐号和非标准端口；图9000/minio/cdn显示目录/PNG、1.61GB，没有认证方式。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 历史漏洞分类映射与任务覆盖矩阵 | OWASP图展示2017→2021分类映射和统计；图片描述历史版本而无资产实际测试。 | [方法条目](../hunting-strategy.md) |
| 限流候选变换与同一逻辑身份计数 | rate poster列session/IP/cache/429及X头、空白、UA、cookie/编码等；没有真实计数日志。 | [方法条目](../by-type/authn-session.md) |

| 反射扫描HTML标签分类与浏览器执行证据 | Reflector2.5图列POST200、Reflected Yes、script HTML tag、Vulnerable Yes或Maybe，并显示两个奖励条目。 | [方法条目](../by-type/xss.md) |
| 域枚举帮助函数与具体对象查询产物 | EDD帮助列function、domain、computer/group/process/user、share/search、输出和threads5，help后打印done。 | [方法条目](../discovery/passive-and-services.md) |
| 路径反斜杠触发PCRE构造错误的定位 | 两图URL包含反斜杠，分别出现PCRE不支持escape及No ending delimiter错误，未保存实现。 | [方法条目](../source-audit.md) |
| 百分号hex大小写和实际换行消费者 | 正文建议百分号0A改0a避403；没有真实响应分隔结果。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 递归页面搜索中的匹配层和链接范围 | WWWGrep帮助可按literal/regex、case、header、HTML、JS、text/comments搜索，并区分root或any链接递归，另有代理/auth与separator。 | [方法条目](../discovery/web-and-api.md) |
| API Gateway域发现与端点认证合同 | 正文把execute-api通配域搜索后fuzz称No auth required；没有具体route/stage或私有对象结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| WindowsADS候选的文件流与目录消费者 | 两张不同尺寸卡列ASP文件::$DATA与admin目录$INDEX_ALLOCATION，未保存响应。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 搜索工具版本更换后的输入输出合同 | pagodo2.0图改搜索库、字典返回、原生HTTP/SOCKS、min/max等待和固定all_dorks文件，移除旧依赖/UA禁用。 | [方法条目](../discovery/records-and-incremental.md) |
| 路径大小写分号与限流键的规范化一致性 | 正文称加分号只在Java可绕限流，并建议端点大小写变化避forbidden。 | [方法条目](../by-type/authn-session.md) |
| Grafana错误页返首页与后端权限分离 | 正文叙述403目标某JS路径为Grafana404，点home后正常，无保存会话/私有API数据。 | [方法条目](../by-type/idor-access-control.md) |
| 历史默认帐号表与部署身份的独立确认 | 正文列多个产品默认帐号密码，无实际目标/版本/登录收据。 | [方法条目](../by-type/authn-session.md) |
| 官方功能教程到业务假设的版本对应 | 正文建议成熟公司教程发现未用功能；另一图反思盲改请求转为理解资产连接。 | [方法条目](../business-modeling.md) |
| Flashcall返回映射与恢复终态的同一挑战 | Facebook图请求should_use_flash_call及cli字段，回包出现code_length和flash_call_cli_filter_map，缺新密码或最终会话。 | [方法条目](../by-type/authn-session.md) |
| 票据输出与ACL修改和权限恢复的区别 | targetedKerberoast终端显示认证上下文和长票据样式串，微小字段没有可靠全读；缺ACL修改/恢复日志。 | [方法条目](../source-audit.md) |
| 挑战规则的读者域和浏览器矩阵 | 0921页面规则指定该域、Chrome/Firefox、域对话框、非selfXSS/MITM和时间范围。 | [方法条目](../by-type/xss.md) |
| 反编译HTTP注解与动态路由和真实请求 | jadx grep图列GET/POST注解、路径变量和动态{url}，方法名涉及app/store；正文只按Java文件搜注解。 | [方法条目](../by-type/mobile-android.md) |
| 成员移除与旧编辑添加动作的撤销边界 | 正文叙述admin移除成员后旧请求仍编辑/新增文件；奖邮件标题却为removed customers add reports on data_requests。 | [方法条目](../by-type/idor-access-control.md) |
| fileURL问号解码与shell文字的不同解释器 | 保存多帖候选含问号、百分号双编码、变量和命令替换样式，未给consumer或结果。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Jira功能路径dork与实际CVE条件 | 正文用ContactAdministrators路径dork称RCE，未保存版本、配置、输入或执行结果。 | [方法条目](../discovery/passive-and-services.md) |
| ASN和归档URL模板的执行与范围输入 | 模板商店图列ASN network/subdomain、archiveURLs、JS credentials、redirect、port/S3/fuzz等动作卡。 | [方法条目](../discovery/records-and-incremental.md) |
| 事件属性中的脚本加载与分类标签错配 | 正文onfocus接jQuery.ajax dataType script；图Search输入却分类Stored，triaged high但无执行/持久化截图。 | [方法条目](../by-type/xss.md) |
| 支付回调页与账单结算交付的一致性 | 图建议取Success/Referer/Callback里payment/hash URL重新打开，称支付成功，没有backend账单证据。 | [方法条目](../by-type/business-logic.md) |
| FirebaseURL和HTML数据库字样的公开配置边界 | 一帖Wappalyzer/source找到Firebase db URL；另一MongoDB pass放HTML文字无实际字段图。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 多源枚举退出成功与缺失模块的实际覆盖 | OneForAll0.2dev图因缺APIkey跳过多个模块；0.3dev图有404/500、DNS/wildcard流程、只port80、2alive和csv overwrite，最终exit0。 | [方法条目](../discovery/records-and-incremental.md) |
| multipartHTML输入与取回读者合同 | 图只给cat.html、text/html和h1 test的multipart请求；正文列黑白名单与Exif类别，没有上传响应。 | [方法条目](../by-type/file-upload.md) |
| 本地污染fixture与控制台主动原型写的差别 | Plution图对本地fixture输出Vulnerable；JSPanda图控制台直接defineProperty Object.prototype后显示CLOSURE_BASE_PATH Polluted。 | [方法条目](../by-type/prototype-pollution.md) |
| 文档同屏计算器与文档触发的进程因果 | CVE40444标题的图仅Word页面、坏图像和Calculator窗口，缺文档触发或父子进程。 | [方法条目](../by-type/document-rendering.md) |
| 并发ping日志与主机存活的协议边界 | 两帖把254个ping后台任务追加文件称全部alive探测，未给wait/任务结果；端口表和网络工具图只是协议类别。 | [方法条目](../discovery/passive-and-services.md) |
| 信任链内证据与范围外资产的授权分开 | 正文建议scope外XSS用于scope内CORS，开放RDP推整subnet/VPS，政府清单推可猎目标；另帖自述FacebookSSRF禁止提升RCE。 | [方法条目](../scope-and-rules.md) |
| 恒真表达式相同响应的零信息反例 | 正文称正常username和附恒真式返回同内容就确认SQLi，缺恒假和查询构造。 | [方法条目](../by-type/sql-injection.md) |
| 历史JS取回到秘密模式扫描的阶段连接 | 图gau先cut query、regex选JS/JSON，fff保存200，再遍历gf _secrets模式；未显示gf从哪个目录/流读取。 | [方法条目](../by-type/info-secrets.md) |
| Drupal模块目录和配置字段的不同敏感度 | 卡片给extension/services、sync目录和swiftmailertransport路径；正文>=8隐藏内容推荐没有配置响应。 | [方法条目](../by-type/info-secrets.md) |
| 证书内网名称和组件产品名单的资产归属 | 正文用证书internal CN和reversewhois找名称；OMIGOD完整alt列Azure Automation/Update/OMS/Log Analytics/Configuration/Diagnostics/Container Insights。 | [方法条目](../discovery/passive-and-services.md) |
| 代理拼接的地址顺序与身份消费者 | XFFor图把实际client与自填IP拼数组并称backend读取第二项，正文无最终免费权益证明；Apple图用XFHost影响302Location。 | [方法条目](../by-type/host-header.md) |
| 上游身份邮箱到下游显示sink的完整类型链 | 正文称提供者允许特殊邮箱，用其登录别的服务可能XSS，未保存具体字段/DOM。 | [方法条目](../by-type/xss.md) |
| 竞态标题与逐帖日期提取代码的错配 | Race adduser帖子图实际遍历Twitteruser_timeline，用第一条created_at决定时间窗，再抽整个response的expandedURL。 | [方法条目](../discovery/records-and-incremental.md) |
| Manifest静态声明与运行组件权限的独立证据 | jadx图app-debug manifest列targetSDK25、网络/storage/calendar、singleInstance及receiver exported=false；另图历史MobileTop10分类。 | [方法条目](../by-type/mobile-android.md) |
| NTLM触发制品生成与实际reader回包 | 图为模板目录、localhost file shortcut及现代格式Created/OPEN/BROWSE说明，多个旧格式被skip。 | [方法条目](../source-audit.md) |
| 已有执行会话与脚本打包产物的两种收据 | InlineExecuteAssembly图已有beacon打印Seatbelt LastShutdown；PS2EXE图编译HelloWorld.exe及config，未见新exe运行。 | [方法条目](../source-audit.md) |
| 日志字符串到可解释包含文件的完整前提 | 彩色/黑白LFI图示include输入、日志污染、error log再include和shell/DoS后果，均为概念链。 | [方法条目](../by-type/lfi-path-traversal.md) |
| PHP输入过滤与进程交互wrapper的能力区别 | 正文把php file、filter、input等混成LFI→RCE。 | [方法条目](../by-type/lfi-path-traversal.md) |
| CDX重复URL与独立有效密钥计数 | CDX图original/collapseurlkey列多次相似api-key query且含test字样；正文声称10k premiumkeys但没独立有效性证据。 | [方法条目](../by-type/info-secrets.md) |
| metrics拒绝与私人红队Critical标签的独立判断 | GC周期/metrics报告图NA closed，正文归因名气；私人红队奖表把default password/BAC/weakpolicy/redirect/phpmyadmin exposure都标Critical。 | [方法条目](../impact-and-acceptance.md) |
| 工具UA识别和公开目录的执行授权界限 | 正文建议改第三方工具UA；另有GitHubAction批扫、多种网络工具及开放主机玩笑。 | [方法条目](../scope-and-rules.md) |
| internal候选路由和HTTP方法的对象合同 | 正文internal路由403→200和POST改GET只有状态建议，无具体私有对象响应。 | [方法条目](../by-type/idor-access-control.md) |
| 错误页逆图搜索的框架候选和部署验证 | 正文从error截图逆图搜索发现框架，没有保存实际版本/组件证据。 | [方法条目](../discovery/web-and-api.md) |
| 自操作XSS到其他读者以及客户端取回的边界 | 正文selfXSS加CSRF、缺X-XSS-Protection会变严重，又以window.location去自有server称XSPA。 | [方法条目](../by-type/xss.md) |
| 网络工具图的观察层与配置副作用 | 整张图列ping/curl、DNS/whois、SSH复制、抓包、route/IP、ARP、VPN/firewall、TLS、性能和namespace等。 | [方法条目](../discovery/passive-and-services.md) |
| 词种扩增数量与候选预算的关系 | Weakpass图两个seed生成432个大小写/后缀候选；正文Haptyc列Sniper/Clusterbomb/Batteringram/Pitchfork。 | [方法条目](../targeted-fuzzing.md) |
| 通知和邀请发送的业务动作配额 | 两100奖励邮件标题分别提无限admin creation/daily notification及employee invitation emailbomb；OTP图只phone/SMSformat字段。 | [方法条目](../by-type/business-logic.md) |
| 协议URI初始argv与后续启动参数的两次消费 | WorkSpaces图版本3.1.6.2064初始ProcessStart，--uri内含编码空格及gpu launcher候选，未显示calc子进程；two-tier图只架构。 | [方法条目](../by-type/desktop-client.md) |
| creator邮箱字段路径与订阅者列表声称的区别 | VoiceCreator图文字称可列subscriber邮箱，query实际指向publications.creator.email_settings.confirmed_email.email_address，没有response。 | [方法条目](../by-type/graphql.md) |
| 符号码元生成与片段调用终态的分离 | 代码图从第21行起，用类型强转和字符串索引拼constructor/Function/alert字样；标题称无字母数字括号调用，缺最终调用片段。 | [方法条目](../by-type/xss.md) |
| shell提示符外观与实际执行身份 | 正文建议exportPS1为井号提高impact，是显示层反讽，没有uid/权限变化。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 客户端路径规范化的真实wire对照 | 正文称curl/browser会去点段而Python原样，并给urllib示例，未保存实际请求。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 认证前后矩阵与跨客户端同邮箱身份 | 一帖建议先preauth场景；另一保存1/2为Web上传私有文档后Android同邮箱不同密码注册，缺续文/最终文档读取。 | [方法条目](../by-type/authn-session.md) |

| 前缀过滤重定向与斜杠消费者对照 | 截图称正常绝对URI返回403，前置斜杠后绕过；另两帖列三斜杠、无双斜杠scheme与反斜杠组合，没有Location或最终目的地。 | [方法条目](../by-type/open-redirect.md) |
| 文档安全警告检索转为具体实现假设 | 正文替代文字与截图给grep-HanriEC2检索deprecated、unsafe、must not及common pitfall等词，并保留两行上下文。 | [方法条目](../source-audit.md) |
| 多字典URL拼接的输入契约与CSV解析 | ffuf帖给URL与FUZZ两个字典、200筛选、CSV输出后awk取第三列；Haklistgen图只是人物词汇文本，Bopscrk图为歌词短语1342经长度过滤1202。 | [方法条目](../targeted-fuzzing.md) |
| 侦察流水线的阶段产物与路径展开 | 正文串subfinder、httprobe与aquatone，自述210个子域并把输出路径写为波浪号紧接工具名。 | [方法条目](../discovery/web-and-api.md) |
| 上传导图中的解析消费者与触发条件 | 三张导图副本列后缀/MIME/魔数、WindowsADS、图片SVG/GhostScript、音视频ffmpeg/HLS、XML/OOXML/ODF、ZIP链接和配置文件分支。 | [方法条目](../by-type/file-upload.md) |
| 业务功能的端点操作身份矩阵 | 作者自述连续35份业务报告并建议查不同端点，没有保存报告原文。 | [方法条目](../by-type/business-logic.md) |
| SSH反向隧道转代理的两端角色 | 正文在本地向VPS建-R8080到本地127.0.0.1:8080的SSH隧道，再于VPS用本地回环端口代理。 | [方法条目](../discovery/web-and-api.md) |
| 侦察数据库配置中的端点身份和TLS校验 | BBRF示例含VPS CouchDB、用户名/口令占位、通知字段并设置ignore_ssl_errors true；ELK帖只述收集和可视化。 | [方法条目](../discovery/records-and-incremental.md) |
| SAML浏览器往返的SP与IdP信任边界 | 图画SP产生请求、浏览器转IdP认证、IdP响应经浏览器送ACS再登录，没有签名检查实现。 | [方法条目](../by-type/saml-sso.md) |
| 社交登录共享信息提示与真实授权范围 | 邮件图称登录Rell并共享name and profile picture，可Edit Settings；不是数据库或API响应。 | [方法条目](../by-type/oauth-oidc.md) |
| 分号路径上的认证授权与应用状态差异 | 截图同一JWT在Settings路径收到401，标为FORBIDDEN；加入分号后200且JSON出现权限字段true，路径和数据部分打码。 | [方法条目](../by-type/authn-session.md) |
| 报告质量与公开信息的可识别组合 | 正文强调准确可复现无偏报告；另一帖提醒程序名、细节和客户引用组合可能识别目标。 | [方法条目](../reporting.md) |
| 漏洞分类导图转为功能和信任边界路线 | Web导图列注入/SSRF/IDOR/缓存/竞态等，另图列侦察分支和为何构建网站、测试145项目但未展开。 | [方法条目](../hunting-strategy.md) |
| MFA导图中界面修改与服务端授权的分离 | 导图把successfalse改true、401改200、Referer、直接访问、旧会话、备用码、重用和跨账号OTP均列绕过，还建议大量重复请求。 | [方法条目](../by-type/authn-session.md) |
| 跨字段拼接与终端HTML上下文 | 图把firstname末尾img开标签与lastname属性/事件合并成页面弹窗。 | [方法条目](../by-type/waf-bypass.md) |
| 项目搜索结果与当前明确授权 | 正文给bugbounty相关Google查询，Chaos图按bountytrue和平台筛URL后下载/解压/删除zip；discloseio帖给历史2297等政策计数。 | [方法条目](../scope-and-rules.md) |
| 空间搜索的证书域名与HTTP响应角色 | C2搜索图有IP、证书签发者/受体域名和IIS8.5、404/Content-Length0；cero帖建议所有IPv4或云范围取证书。 | [方法条目](../discovery/passive-and-services.md) |
| 网页技术指纹库与实际漏洞的验证差距 | WebStor图把DNS传送/端口/HTTP响应和Wappalyzer导入数据库，再按名称regex取URLs/IPs；Cariddi自述130kURL十分钟50目标。 | [方法条目](../discovery/records-and-incremental.md) |
| 限流验证与猜测凭据的动作边界 | 正文问限流在范围但密码暴力不在范围如何判断；SharpSpray图只有AD/Csharp/LDAP标题。 | [方法条目](../by-type/authn-session.md) |
| 库存功能命令输出与受控输入因果 | 图片显示库存POST表单storeId后附命令片段，200返回Linux uname样式文本，像实验室页面。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 注册查询参数进入meta属性的浏览器读者 | 阿拉伯语帖述拦注册请求改payload与cookie，图显示registerdo参数闭合meta og:url属性并形成script，另图浏览器弹出cookie样式值。 | [方法条目](../by-type/xss.md) |
| 点击链接混合编码的上下文与浏览器条件 | 图片标题声称Akamai全部浏览器有效，包含实体/控制字符的hrefjavascript与点击文本并把location发送到外站。 | [方法条目](../by-type/waf-bypass.md) |
| 无效UTF8触发旧登录页的版本和回退路径 | cPanel帖有loginuser事件payload，图SEC596描述无效UTF8触发LegacyLogin输出编码不足，列修复11.98.0.8和11.94.0.16。 | [方法条目](../by-type/xss.md) |
| XML候选位置与实际DTD外部实体配置 | 正文列SVG/sitemap/SAML/HTML/SOAP/XMLAPI；上传图还有OOXML/ODF。 | [方法条目](../by-type/xxe.md) |
| 公开邮箱候选与泄漏凭据的事实边界 | Zen图描述找GitHub用户邮箱，正文把员工邮件/泄漏和credentialstuffing连在一起，未保存有效凭据。 | [方法条目](../by-type/info-secrets.md) |
| Base64身份token与对象级授权并非等同 | IDOR漫画示范改Base64token内id读取他人记录并说弱session/不应使用用户输入；小副本正文仍可辨但细节有限。 | [方法条目](../by-type/idor-access-control.md) |
| API密钥签发对象与权限证明 | 保存1/2描述生成密钥需user_id及email；Ghost图仅列adminAPI路径200，没显示密钥字段和低权identity。 | [方法条目](../by-type/idor-access-control.md) |
| 模型预测口令与认证结果的区别 | SharpML图从共享文件数据/规则与AD用户输入模型，再产用户口令对并连接Login，未给实际认证结果。 | [方法条目](../by-type/authn-session.md) |
| S3词典枚举的Host与资源权限分离 | 正文ffuf原请求Host带http scheme，过滤404400并建议300线程；无实际桶响应。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| PKINIT与ADCS图示的具体证书身份 | PKINIT终端显示请求并保存TGT，ADCS图只有Root/SubCA颁发/安装关系；Kekeo图画AS/TGS/AP往返。 | [方法条目](../by-type/authn-session.md) |
| 受理修复署名和奖励评估的不同终态 | Apple图分别写reviewinvestigating、无法再复现/署名询问和possible rewardevaluation；另图功能问题不是安全漏洞，Crowdin礼盒。 | [方法条目](../reporting.md) |
| 下载文件完整性与被替换执行链 | 帖子称未完整性校验使替换exe执行，奖励图只给No secure integrity check of downloaded file200。 | [方法条目](../by-type/desktop-client.md) |
| 系统代理CA与捕获请求的不同收据 | Proxverter图列importcert、setsysproxy、engage、delsysproxy，使用回环8081和is_https。 | [方法条目](../discovery/client-and-cloud.md) |
| 银行业务三类假设与权威交易状态 | 正文列篡改支付通信、回调未校验、虚拟卡号可预测，没有完整通信；付款测试图述误用真卡而扣款。 | [方法条目](../by-type/business-logic.md) |
| HTTP方法和状态码的具体语义与应用动作 | 方法图列GETHEADPOSTPUTDELETECONNECTOPTIONSTRACE，状态图把3xx全概括为跳到不同资源。 | [方法条目](../discovery/web-and-api.md) |
| Flexbe模板命中与可认领服务条件 | 图仅示nuclei2.3.4加载一模板并命中flexbe takeover high，正文指向模板PR和issue。 | [方法条目](../by-type/subdomain-takeover.md) |
| CSV导出中的公式解释与后续程序执行 | 正文把上传/导出CSV直接称RCE，替代文字只是服务广告，未保存公式。 | [方法条目](../by-type/document-rendering.md) |
| fileURL由哪个服务端消费者处理 | 正文列file路径/多斜杠与ssrfphp参数并说可读服务器文件，未给响应。 | [方法条目](../by-type/ssrf.md) |
| OTP请求控制字段与挑战最终状态 | 注册OTP图只有POST请求，result_ids指otpdiv、dispatch标verifyregister及OTP字段，没有响应或已验证状态。 | [方法条目](../by-type/authn-session.md) |
| 反汇编system导入与可达命令边界 | r2图从afl usefulFunction到反汇编/bin/ls/systemcall，再看system导入跳转；efi图为仿真SMIhandlerreturned记录。 | [方法条目](../source-audit.md) |
| 历史CVE热度与具体漏洞影响分离 | 9月CVE曲线列多个编号，未定义纵轴采样；正文说not all bugs critical，另GoogleForms称低影响intended。 | [方法条目](../impact-and-acceptance.md) |
| 侦察自动通知的阶段完成与证据保留 | Morya正文称bash侦察加Discord通知，AttackSurface图DiscoveryDB→Nmap→各模块→ReportAlert循环。 | [方法条目](../discovery/records-and-incremental.md) |
| OAST服务配置和目标回调的来源绑定 | 正文称interact旧域变化并给带空格的aliasnuclei参数，另一图把iframe样式插入请求但200长度0。 | [方法条目](../by-type/ssrf.md) |
| 少见漏洞的消费者跨层路线 | 保存列表1到4为HTTP2smuggling、OfficeXMLXXE、PDF生成XSS→SSRF、SVGXSS，后续未保存。 | [方法条目](../hunting-strategy.md) |
| WordPress用户路径拼接与数据公开性 | 正文awk把每行域名追加wpjsonwpv2users；方括号是帖子包装，未给返回内容。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 车辆工具菜单中的观察与发送动作 | CarPunk菜单分CANinterfaceupdown、sniffrecordplay，没有操作结果。 | [方法条目](../by-type/automotive-security.md) |
| Apache旧版本路径规范化与CGI条件 | 旧图分别见2.4.49读取passwd、2.4.48返回400，另图2.4.50本地CGI500后临时marker文件出现，以及49/50响应daemonuid。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 批量路径脚本的原始字节和响应特征误判 | 正文sed给目标追加cgi编码点段，再httpxmatchroot；没有运行收据。 | [方法条目](../targeted-fuzzing.md) |
| 缓存激活和邀请链接的对象生命周期 | 正文称cachedactivationreset可攻破，另帖从档案发现上千projectteaminvites并自述非成员可加入。 | [方法条目](../by-type/authn-session.md) |
| 原型污染库定位与gadget分开的数据库复用 | 图DetectionSelenium/extension/CodeQL→关键词/断点/阻断JS定位库→sourcegadget，再存librarygadget库和被动regex检索。 | [方法条目](../by-type/prototype-pollution.md) |
| BBCode转换后的HTML与原文属性界面 | 正文提醒BBcode可有XSS，但外链实现未保存；另帖lng值闭title后iframe，未给响应。 | [方法条目](../by-type/xss.md) |
| UNION适用查询位置与独立返回证据 | 正文仅说明SELECT可UNION两结果；另帖问时间盲注扩展，无具体请求。 | [方法条目](../by-type/sql-injection.md) |
| 页面源码凭据线索与真实保密边界 | 正文称敏感credential奖励并建议源码，图仅确认修复/奖金额打码。 | [方法条目](../by-type/info-secrets.md) |
| 编码绕过卡的各层解释规则 | 正文列case和percent，图片再列Unicode/HTML混合编码、注释、doubleencode、通配符、垃圾/换行及未初始化变量。 | [方法条目](../by-type/waf-bypass.md) |
| 注册XSS与CRLF头写入的独立消费者 | 正文payload拼script和字面反斜杠r/n再SetCookie，没给原始响应头；AWSWAF卡混杂percent控制字节/事件/atob。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 改邮箱token的主体绑定与session假设 | 正文自述自有账号改自有邮箱链接被受害者打开后改受害者邮箱，并归因token不绑session。 | [方法条目](../by-type/authn-session.md) |
| 重置主体参数与返回token能力的拆分 | multipart图password/password2/id/action仅请求；另一正文改GETuseridreset取token并称cookieeditor登录，未给响应终态。 | [方法条目](../by-type/authn-session.md) |
| 邮箱验证码字段的JSON标量与数组类型 | 图PUTmailverify把code标量换成多项数组，200响应含id/token，未保存最终verified状态。 | [方法条目](../by-type/api-property-pollution.md) |
| HostURL生成与限流身份键分别验证 | 正文把XFHostresetpoisoning、XFFloopback、null和case统称限流；reset图只见改Host请求。 | [方法条目](../by-type/authn-session.md) |
| cookie弹窗的脚本上下文与接管能力 | Huawei协作帖图片只有裁剪地址栏与cookie弹窗，没有输入/响应上下文。 | [方法条目](../by-type/xss.md) |
| 平台邮箱别名与软件演示访问授权 | 正文称用bugbounty平台邮件别名使厂商以为企业请求演示。 | [方法条目](../scope-and-rules.md) |
| 隐蔽通道生成文件与命令实际执行的区别 | CovertTube图运行generatevideo，输入命令并列出outputavi，未保存上传/接收端/执行收据。 | [方法条目](../discovery/client-and-cloud.md) |

| 控制台弹窗、designMode 与本机 hosts 的作用域 | 保存帖把控制台直接调用 alert、开启 designMode 和编辑本机 hosts 当作玩笑演示。 | [方法条目](../by-type/authn-session.md) |
| 历史宽泛范围名单与西班牙语项目规则 | 阿拉伯语帖列所谓宽范围公司，私有项目 dork 帖只给发现方式；西班牙语直播图展示 Ford 当时的参与规则与响应期。 | [方法条目](../scope-and-rules.md) |
| Imperva、Incapsula 与 Cloudflare 载荷的多层解释 | 保存文本含 javascript URL 空白、事件名实体、Unicode 标识符与 SVG 变体；一张论坛图显示地址含混合 SVG/onload 形态及值为 1 的确认框，其他卡片没有执行回执。 | [方法条目](../by-type/waf-bypass.md) |
| JWT 认证 URL 与 returnto 的重定向链证据 | 保存 JWT 接管文章的图片只显示含认证值及 returnto 的 GET 和返回同一认证地址的 302。 | [方法条目](../by-type/oauth-oidc.md) |
| tplmap 的 oscmd 回连与 non-intrusive 标签纠正 | 图片把带 oscmd 的 tplmap 回连演示标成 non-intrusive。 | [方法条目](../by-type/ssti.md) |
| 证书域名不匹配与客户端是否接受错误证书 | 图片可见 Firefox 拒绝域名不匹配证书，另有一条历史 Medium/Resolved 记录。 | [方法条目](../by-type/authn-session.md) |
| 500GB RECON 统计与真实资产覆盖 | 配图是 Windows 网络使用量，九天约 554GB、其中 OpenVPN 约 474GB。 | [方法条目](../discovery/records-and-incremental.md) |
| 账号锁定是否撤销既有会话与恢复窗口 | 截图描述失败登录锁定会结束受害者所有活动会话，并称永久 DoS。 | [方法条目](../by-type/authn-session.md) |
| BIG-IP 重定向搜索结果与管理接口可达性 | Shodan 图按 BIG-IP 重定向标题展示约一万条结果，文字称 CVE-2021-22986。 | [方法条目](../discovery/passive-and-services.md) |
| WordPress 文件清单与 AEM servlet 路由审计 | WordPress 帖列管理、配置、包含目录等十二个候选路径，AEM 帖建议寻找其他 servlet。 | [方法条目](../discovery/web-and-api.md) |
| Notebook、源码和 URL 中的凭据候选 | 保存帖给 ipynb 密码搜索方向、源码查找建议，以及 URL 路径含用户名密码的自述；奖励图未展示可验证值。 | [方法条目](../by-type/info-secrets.md) |
| 命令注入流水线、Commix 输出与回连截图 | 一帖串联子域、URL、替换参数与 ffuf；另一图有 Commix 数学探针和 www-data 字样；过滤绕过帖附反向连接截图但未显示进程身份。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Nexploit 的 HTMLi 分类与实际 HTML 消费者 | 图显示 WAVSEP JSP 输入、HTML 标记示例和 127 LFI、20 SQLi、55 HTMLi 等工具数量。 | [方法条目](../by-type/xss.md) |
| Qu1cksc0pe 静态分析帮助与外部样本上传边界 | 帮助图列文件、目录、语言、元数据、域名与 VirusTotal 等选项，没有给出样本分析结果。 | [方法条目](../source-audit.md) |
| 扩展名、null 与分号变体必须绑定实际文件处理器 | 保存帖和卡片枚举 PHP/ASP 变体、大小写、null 与分号，阿拉伯语帖把 shell 改为 jpg；另帖泛称未验证上传。 | [方法条目](../by-type/file-upload.md) |
| json、空 ID 与编码点路径的资源一致性 | 图片显示相似 GET 的 403 与加 json 后 200；其他帖删对象 ID、改变斜杠、空白或编码点，一张报告图给 util 与编码点前缀的候选管理页面。 | [方法条目](../by-type/idor-access-control.md) |
| CSRF 参数替换与浏览器投递条件 | 阿拉伯语帖依次建议删除参数、空值、随机长度、其他账号令牌及变更方法；初学文章仅保存标题。 | [方法条目](../by-type/csrf.md) |
| Twitter intent 启动输出与崩溃因果 | adb 图含 retweet intent 的启动行和较早的解析异常，没有可绑定的应用崩溃栈。 | [方法条目](../by-type/mobile-android.md) |
| Exporter、LazyCSRF 与表单方法覆盖的等价性 | Exporter 图提供 clipboard、文件及 XHR/表单生成；LazyCSRF 图把 JSON PUT 请求改成 POST 加隐藏方法字段，并和 Burp 表单比较。 | [方法条目](../by-type/csrf.md) |
| CDN 原站 IP 候选与直接访问后的权限 | 保存外链标题称发现原站 IP 可绕过 Cloudflare 并导致 DDoS，图只是 CDN 架构。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Spring trace 中的 cookie 泄露与 fixation 的区别 | 保存文本把 trace 记录中的共享父域 cookie 描述为一次点击会话固定，没有保存请求或图片细节。 | [方法条目](../by-type/authn-session.md) |
| 改邮箱后的旧重置链接与对象 ID 绑定 | 文本描述旧重置链接、登录改邮箱和再次重置；另一图仅有带账号 ID 的密码 POST 和空 Location 的 302。 | [方法条目](../by-type/authn-session.md) |
| 厂商复现、未来 CVE 与重复报告的不同阶段 | Forti 邮件称已复现并会在修复发布时分配 CVE；其他图有标题 Critical/实际 Medium、滚动修复、不知赏金、重复拒奖及致谢。 | [方法条目](../reporting.md) |
| Piper 的 JWT 格式化与 SPA 端点候选 | 正文介绍扩展名筛选、提取 SPA/API 路径和 JWT pretty 输出，图片只有仓库概览。 | [方法条目](../discovery/web-and-api.md) |
| P4 批量自动化与单目标修复回归的分母 | 保存帖称可自动化常见 P4 并扫描所有范围内项目，另帖建议对单目标反复找同功能变体。 | [方法条目](../hunting-strategy.md) |
| PostgreSQL COPY 文件读取与 PROGRAM 执行权限 | 图片只展示建表、从服务器文件导入及 SELECT 内容，正文把文件读取和命令执行并列。 | [方法条目](../by-type/sql-injection.md) |
| S3 时间戳音频名称与二进制内容证据 | Turbo Intruder 图展示约五十万请求和三个 200、不同长度的结果，正文声称其中两个是音频；所示响应没有足够的音频解析证据。 | [方法条目](../by-type/idor-access-control.md) |
| Nuclei 代理与 Logger 历史的请求对应关系 | 保存正文提议把 Nuclei 经代理送到 Burp Logger 并筛选。 | [方法条目](../discovery/records-and-incremental.md) |
| IPv6 无目标响应与协议层证据 | Xmap 图展示网络拓扑、路由器 ICMPv6 不可达与未分配地址处理。 | [方法条目](../discovery/passive-and-services.md) |
| Apache 三版本载荷卡片与 2.4.51 修复反例 | 卡片把编码遍历列入 2.4.49、2.4.50 及 2.4.51，另一个工具图只显示批量生成和连续 HTTP 400。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 低高权限 API 矩阵与替换自有账号 ID 的规则 | 正文建议低权限对高权限端点，卡片指导账号 B 登录后把 URL/正文中的 B 的 ID 替换为自有账号 A。 | [方法条目](../by-type/idor-access-control.md) |
| OTP 的 400 到 201 与刷新令牌后续用途 | 图展示六位候选循环、无效 400 后 201 及刷新令牌字段，正文只有测试自述。 | [方法条目](../by-type/authn-session.md) |
| ADCS 正常证书签发与 Golden Certificate 条件 | 图片展示客户端 CSR、CA、模板、Domain Users 与无需审批的正常签发配置。 | [方法条目](../by-type/authn-session.md) |
| Blind SQL 标题与 UNION 版本回显的分类 | 图片在训练页面 Email 处回显数据库版本，示例属于 UNION 返回值。 | [方法条目](../by-type/sql-injection.md) |
| text/plain 请求中的外部 DTD 与缺失实体定义 | 请求图含 XML DOCTYPE、远端参数实体及 all/send 引用，没有完整 DTD、响应或回连。 | [方法条目](../by-type/xxe.md) |
| 历史网页缓存的版本与私密性判断 | 两幅图显示过去缓存时间及 MDM 管理页的 CSS/build 等源码引用。 | [方法条目](../by-type/info-secrets.md) |
| CVE-2021-40438 的 mod_proxy 版本和消费端 | 保存帖把 Apache 2.4.48 的 CVE-2021-40438 称为严重 SSRF，未给实际请求回执。 | [方法条目](../by-type/ssrf.md) |
| Shodan 登录指纹与默认凭据尝试的边界 | 正文串联 SSL 搜索、登录页、公开仓库字符串与默认密码尝试，并自述成果。 | [方法条目](../discovery/passive-and-services.md) |
| Burp Origin 替换、项目持久化与浏览器差异 | Match/Replace 图展示替换请求 Origin 并保存项目配置。 | [方法条目](../by-type/cors.md) |
| 资料脚本示意与 HTML 图片的实际读取链 | 资料注入图把 document.cookie 字样拼进脚本 src 的示意，另一正文描述修改上传字节及 MIME 后访问文件页面。 | [方法条目](../by-type/xss.md) |
| 数据包嗅探中的 TLS 元数据与应用内容 | 终端图有 TCP 443 和 UDP 53 的地址、端口与数据包信息。 | [方法条目](../discovery/records-and-incremental.md) |
| 关闭 introspection 后的查询发现与 resolver 授权 | 保存帖问 introspection 关闭后还能怎样发现接口，没有给实际查询。 | [方法条目](../by-type/graphql.md) |
| DomainProtect 的 CNAME 候选与真实资源归属 | 图列 Route53/Elastic Beanstalk 链、四个候选和两个 vulnerable 标签，并建议创建云资源。 | [方法条目](../by-type/subdomain-takeover.md) |
| DorkScout 结果标题与 Dalfox 数据库报错 | DorkScout 图是 Hosting Controller 等链接列表，Dalfox 图只命中 OLE DB/MSSQL 报错并结束扫描。 | [方法条目](../discovery/web-and-api.md) |
| 云函数命令参数、调度调用与服务账号凭据类型 | 图把 Scheduler/PubSub/函数串联，Python 函数直接读请求命令并调用 os.popen，另一图只有 Beanstalk 应用健康页。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Fapro 模拟服务横幅与真实服务指纹 | 图在 Windows 上列 FTP、MQTT、MySQL 等多个监听地址与端口，工具用于模拟服务。 | [方法条目](../discovery/passive-and-services.md) |
| shell 的 IFS 和 glob 与 LFI 文件消费端 | 两段帖给 shell 变量与通配符形态却贴 LFI 标签，另一图只显示 file 参数生成正常 HTML。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Burp 四类功能与代理观察到主动变更的分界 | 旧卡片列 Proxy、Repeater、Intruder 四模式和 Extender 的历史运行环境。 | [方法条目](../experiment-design.md) |
| 被动 DNS 线索、第三方解析器与所有权 | 正文推荐被动 DNS 两站，另帖想用第三方 hosts 服务更快解析；AXFR 帖循环猜十个 NS 并把带 scheme 的值当域名。 | [方法条目](../discovery/passive-and-services.md) |
| x-user-id 与路径 ID 的身份优先级 | 正文称 401 加用户头后 200，再描述路径用本人 ID、头用他人 ID 的改密请求；图片文档建议 identifyUser 可读取自定义头或认证中间件。 | [方法条目](../by-type/idor-access-control.md) |
| 两个 Host 字段的 302 与重置邮件污染 | 图片里原始 Host 和第二个 Host 并存，响应 Location 指向第二个域名，文字提到方案及转发头。 | [方法条目](../by-type/host-header.md) |
| 伪代码签名成功与系统信任链 | LimeLighter 图明确写 fake cert 并输出 Signed File Created。 | [方法条目](../source-audit.md) |
| IMDSv2 工具名与元数据保护的具体边界 | 保存帖仅介绍 Metabadger 自动化 IMDSv2，没有配置值或 SSRF 回执。 | [方法条目](../by-type/ssrf.md) |
| Jira 思维导图与两个 CVE 标题的版本映射 | Jira 帖引用 CVE 汇总；另一帖以两个编号并列认证 RCE 与未认证加管理员，但没有保存产品、版本或过程。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 隐藏编辑接口到 CSRF 接管的缺口 | 正文给找到账号/编辑接口、制作 CSRF、发送受害者的五步自述，配图只有 High 标题。 | [方法条目](../by-type/csrf.md) |
| 邮件 HTML 注入的 mailto 方案与网页脚本差异 | 卡片先展示 HTTP 链接和删双斜杠，后称换 mailto 可绕过；没有邮件客户端回执。 | [方法条目](../by-type/xss.md) |
| ASAN Chrome 启动步骤与堆错误证据 | 保存正文列本地 HTTP 服务、ASAN Chrome 配置与 PoC 文件名，并自述奖励，没有保存完整 PoC、版本或崩溃栈。 | [方法条目](../by-type/desktop-client.md) |
| PortBender 转发日志与目标漏洞的因果边界 | 图显示现有 Beacon 内加载模块，把 TCP 445 转到另一端口，并有连接日志。 | [方法条目](../discovery/passive-and-services.md) |
| Nuclei token-spray 信息命中与第三方凭据使用 | 终端图把多个 API 地址和原始 token 放在 info 命中行，正文线程仅保存第一段。 | [方法条目](../by-type/authn-session.md) |
| 长字段跨 Web 同步到 Android 的可用性链 | 正文称长字段会使 Android 卡顿或崩溃，线程后续没有保存。 | [方法条目](../by-type/mobile-android.md) |
| 图片文件名在元数据、URL 和 HTML 属性中的消费者 | 正文把事件和标签形态放进 png/svg 文件名，未保存真实服务器输出或浏览器回执。 | [方法条目](../by-type/xss.md) |

| Slack 成员邮箱展示与测试者的工作区权限 | 图文描述工作区成员邮箱可见性，没有保存当前配置或所有角色结果。 | [方法条目](../scope-and-rules.md) |
| SubCrawl 签名匹配到样本事实的距离 | 终端列 8 hosts、34 URLs 与两条 CLAMAV Winware 检测，正文称按独特内容签名用于 MISP。 | [方法条目](../discovery/records-and-incremental.md) |
| SysFlow 采集架构的分阶段回执 | 保存图展示 Collector、Exporter、对象存储、搜索分析等组件。 | [方法条目](../discovery/records-and-incremental.md) |
| 消息 DELETE 权限标题与可逆权限核对 | 通讯概述消息删除接口缺权限并给出大量用户数字，没有保存完整请求/影响统计。 | [方法条目](../by-type/idor-access-control.md) |
| 构建脚本中的已删桶引用与供应链消费者 | 通讯提到已删除桶仍被构建脚本引用的候选。 | [方法条目](../by-type/subdomain-takeover.md) |
| SNS InvalidAction 证书回显与 webhook 处理链 | 保存错误页回显公有 PEM 证书并报 InvalidAction，通讯/标题另称 SNS webhook RCE。 | [方法条目](../by-type/ssrf.md) |
| HTML 注入在订单反馈阅读者中的条件 | 正文自述订单反馈存储 XSS，配图却是 Google Hangouts GET，没有反馈读者或脚本回执。 | [方法条目](../by-type/xss.md) |
| 动词探测调试分支与 PHP 状态页的实际处理器 | 候选包含 Debug=True、server-status、PHP 管理页；Symfony 图仅欢迎页，Tomcat examples 与 manager 是不同路由。 | [方法条目](../discovery/web-and-api.md) |
| delete alert 与大小写自述的绑定核对 | 保存正文称删除 alert 再改写调用可突破过滤，没有完整浏览器执行结果。 | [方法条目](../by-type/waf-bypass.md) |
| OpenAPI 转换后导入的语法与能力损失 | 转换图使用 json 扩展名但输出可见 YAML，后续 Parser 列出多个 POST 路径。 | [方法条目](../discovery/web-and-api.md) |
| 邮件头候选从地址字符串到 SMTP 的消费层 | 正文给编码换行与 RCPT 形态的邮件字段，没有发送/收件人变化记录。 | [方法条目](../discovery/web-and-api.md) |
| IP 别名候选与真正 URL 解析结果 | 正文列整数、短 IP、IPv6、userinfo 及信任域置于其他 host/路径的表达式。 | [方法条目](../by-type/ssrf.md) |
| 线程堆栈伪装画面与执行地址 | ThreadStackSpoofer 图有 ntdll、TOTALCMD 线程模块和地址，没有原始攻击入口或防护判定。 | [方法条目](../source-audit.md) |
| RDF 中 XHTML script 的响应与阅读器 | 保存 RDF XML 包含 XHTML namespace 和 script 静态内容，没有执行回执。 | [方法条目](../by-type/file-upload.md) |
| WordPress 插件自述与核心奖励标题的组件差异 | 正文称扫描旧插件后利用 CSRF，图则是 WordPress 核心版本 <4.8.5 的奖励标题。 | [方法条目](../by-type/csrf.md) |
| ASP 重复参数逗号合并与 pointer 事件 | 正文称重复参数在 ASP 合并成逗号，并组合 pointer 事件，有浏览器限制自述而无完整环境记录。 | [方法条目](../by-type/waf-bypass.md) |
| LOW 邀请者到 OWNER 的授予能力 | 正文给 LOW 角色邀请请求内改 OWNER 的自述及奖励，没有持久角色回执。 | [方法条目](../by-type/idor-access-control.md) |
| 旧 OTP 重登与成功消费后的单次性 | 帖子称使用某 2FA 码后退出再登录仍可复用，但没有挑战或时间步记录。 | [方法条目](../by-type/authn-session.md) |
| Orion ViewContext JSON 的 Objects 设置与外部来源 | ParseViewContext 图设置 TypeNameHandling=1 并反序列化 AlertingActionContext。 | [方法条目](../by-type/deserialization-rce.md) |
| VDP 数字快照、dork 与资产过滤器的规则来源 | 保存统计从 2301 到 2302，并含奖励/名人堂分类；dork、GitHub JSON/jq 和 bbscope 只给发现/过滤线索。 | [方法条目](../scope-and-rules.md) |
| IPlogger 管理员阅读与请求源的归因 | 正文建议引导管理员打开第三方 IPlogger，另一 Lorsrf 图只展示监听服务启动。 | [方法条目](../by-type/ssrf.md) |
| 验证邮件标志、Origin 回跳与动态 JS 的 OTP | 正文分别称改 Origin/Referer 进入 dashboard 和动态 JS 含 OTP；没有完整服务端保护动作。 | [方法条目](../by-type/authn-session.md) |
| 扫描器候选、真假条件与时间噪声 | 正文推荐扫描/引号/真假与延迟检测；MySQL 前缀候选图却仅显示 localhost403。 | [方法条目](../by-type/sql-injection.md) |
| 并行 HEAD 检测与登录多斜杠的最终 origin | 管道替换所有参数后 grep Location，另有登录多斜杠/P4 标题和信任名称路径图。 | [方法条目](../by-type/open-redirect.md) |
| 同根因端点、报告阶段与酌情奖励 | 图包含更早报告重复、同根因其他端点、N/A到Low/High、Pending/Closed及奖励决定，没有相应完整技术链。 | [方法条目](../reporting.md) |
| 发票导出直接引用与二三阶权限链 | 发票示意图直接将 ID1/2 对应数据库与 exportInvoices；正文另建议二三阶及第三方/隐藏调试。 | [方法条目](../by-type/idor-access-control.md) |
| 从目标上下文建词表及管道解析损失 | 正文主张用目标知识建词表，另给 JS/爬虫/ffuf 管道，包含粗略 regex、awk/cut 与全参数替换。 | [方法条目](../targeted-fuzzing.md) |
| 空白编码候选与 DTD 协议支持 | 图描述内/外实体 SYSTEM 与 file/http/https/gopher，正文提空白/混合编码绕过。 | [方法条目](../by-type/xxe.md) |
| GitHub 关键词、Basic 候选与 API 字典的三层事实 | 词条含 s3cfg/netrc/gitcredentials/cloud/API 字段；字典给约550格式/response regex，Basic匹配有管理员自述。 | [方法条目](../by-type/info-secrets.md) |
| Referer href 回显与持久修改的实验区别 | 图展示 Referer 到 href/GoBack，以及200页面；另帖建议刷新检验真实改变。 | [方法条目](../by-type/business-logic.md) |
| SHADOW Swagger 模型到当前 API 能力 | 图将Swagger路径/参数/模型送到图关系与embedding，没有目标调用证据。 | [方法条目](../discovery/web-and-api.md) |
| PrettyRecon 错误搜索计数与实际披露字段 | 图含aws_key 44候选、Whoops4549、500/404与Apache头；Symfony页只是版本/源码目录。 | [方法条目](../by-type/info-secrets.md) |
| 本地 multipart 收文件的权限前提 | HTTPUploadExfil 图展示本地 curl 上传、存储与读取示例文件。 | [方法条目](../discovery/records-and-incremental.md) |
| VT 低比例与双哈希的样本身份 | 帖子给同样本MD5/SHA1，图为1/67、AUTOIT标签与单个Adware检测。 | [方法条目](../source-audit.md) |
| 算法、kid 与密钥选择的独立接受条件 | 正文列算法选择、非法签名、猜秘密与kid攻击候选，没有保存验签成功链。 | [方法条目](../by-type/jwt.md) |
| 认证 mindmap 变成动作与主体矩阵 | 保存思维图含登录、注册、重置和2FA支路；替换响应只配High标题，忘密枚举正文建议比较结果。 | [方法条目](../by-type/authn-session.md) |
| 技巧帖子与配图矛盾的证据分层 | 正文提醒Twitter技巧未必正确；本批配图包含消费端不一致和明确Blocked。 | [方法条目](../expert-reasoning.md) |
| HTTP 版本比特信道与 QR 视频消费者 | 正文分别用HTTP1.0/1.1表示比特和视频帧QR/AES传指令，图只为梗和三秒QR视频。 | [方法条目](../discovery/records-and-incremental.md) |
| Lucee missinginclude 路径错误页与实验弹窗 | 一图为Firefox Lucee5.2.9.31错误页与domain弹窗，另一为自有Neuralegion实验firstname页面rXSS标记。 | [方法条目](../by-type/xss.md) |
| daily anew 增量与无条件完成通知 | 脚本每86400秒跑subfinder/anew，notify在循环内无条件发送。 | [方法条目](../discovery/records-and-incremental.md) |
| Django debug 与 Pickle 会话的实际入口 | 正文给Debug/PickleSerializer候选，未保存目标session配置或受控反序列化输入。 | [方法条目](../by-type/deserialization-rce.md) |
| main.js 正则与 CDX PHP 历史路径的发现范围 | 简单斜杠正则和gau/CDX PHP卡片只提供候选；GCP metadata自述配奖励图。 | [方法条目](../discovery/web-and-api.md) |
| PeTeReport 数量与 CWE 图的稳定问题标识 | 图有2products、2reports、5findings、3high及CWE分布；另帖列十大P1类型。 | [方法条目](../reporting.md) |
| 从 CVE 补丁到 elFinder GitLab 的适用条件 | 正文建议从补丁追小库；elFinder称全旧版受影响，GitLab图只为模块PR/行数。 | [方法条目](../source-audit.md) |
| Windows file 候选与 SMB 认证的不同结果 | 正文建议file指向VPS、Responder捕获NetNTLMv2再破解，没有实际消费或身份回执。 | [方法条目](../by-type/ssrf.md) |
| 刷新后权益持久化与竞态标题的验证边界 | 一帖建议改完刷新，另一只有订阅竞态标题；未保存并发事务顺序。 | [方法条目](../experiment-design.md) |
| 认证扫描器新读者覆盖与会话降级 | 功能文案提iframe、animation、DOM redirect、SVG和多选等发现能力，未给完整扫描回执。 | [方法条目](../discovery/web-and-api.md) |
| Flask 用户 ID 修改自述与签名 cookie | 正文称改userid可无日志登录，但配图是PDF取回元数据主机名，与会话无关。 | [方法条目](../by-type/authn-session.md) |
| PDF metadata 主机名与 Flask GCP 主张分离 | PDF图URL含元数据位置与排版参数，页面有AWS样式compute.internal主机名；两个正文分别谈Flask和GCP。 | [方法条目](../by-type/document-rendering.md) |
| 隐藏注册到邮箱变更的 verified 主体 | 保存正文称隐藏signup可进入panel，另线程只到注册自有邮件后改其他邮件；图为修复/分诊邮件。 | [方法条目](../by-type/authn-session.md) |
| elFinder cmd=tree 的目录元数据与 OS 命令 | 赞美课程配本地elFinder2.0.4目录JSON，cmd=tree/target/hash/read/write/name可见。 | [方法条目](../by-type/file-upload.md) |
| LSASS clone dump 完成与凭据解析 | 日志标LSASS PID、clone handle及dump complete，没有初始权限来源或解析结果。 | [方法条目](../source-audit.md) |
| ffuf replay-proxy 横幅与捕获事实 | 管道包含httpx跟跳转/retry/cut和ffuf stdin，横幅示FUZZ、40threads、followfalse与replayproxy。 | [方法条目](../discovery/records-and-incremental.md) |
| application/json 数据块与 HTML 结束标签 | AMP图把alert样式字符串放title/docUrl的JSON中，没有执行回执。 | [方法条目](../by-type/xss.md) |
| Mekotio 多阶段图的来源与因果回执 | 图是链接→ZIP→BAT→PowerShell→二次ZIP→AHK/script/DLL→C2，没有每阶段运行日志。 | [方法条目](../source-audit.md) |
| root:x grep 与文件列表的真正读者 | 管道以root:x匹配，另帖列passwd/shadow/SSH/history；Apache历史图有文件内容。 | [方法条目](../by-type/lfi-path-traversal.md) |
| LDAP poll 快照、uSN 与变更主体 | 日志有新增CN/RID及office/whenChanged/uSN/description，没有完整审计主体链。 | [方法条目](../discovery/records-and-incremental.md) |
| Cloudflare Blocked 图与 default rules 限定 | Cloudflare图明确Blocked且alt称只针对default rules，MySQL另一图同样仅403。 | [方法条目](../by-type/waf-bypass.md) |
| 删除账号 token 建议与不可逆动作边界 | 正文建议删/换CSRF token，图为奖励和fixing邮件，没有真实跨站请求或删后状态。 | [方法条目](../by-type/csrf.md) |
| Wifite help 的被动与主动无线动作 | Wifite2.5.8帮助列deauth、kill进程、无限与WEP/WPA/WPS/PMKID，其他帖仅工具资源。 | [方法条目](../scope-and-rules.md) |
| Unicode 域名显示长度与序列化 host | 正文称某Unicode显示能缩短域名，配图只有仓库封面，未保存具体字符映射结果。 | [方法条目](../by-type/open-redirect.md) |
| 403 头部候选与同对象授权对照 | 正文建议localhost头、Referer/UA、方法与参数，其他图仅导航回显和dashboard进入。 | [方法条目](../by-type/idor-access-control.md) |
| 多语法字符串在 SQL HTML 与模板的消费顺序 | 正文组合SQL引号、SVG/JS与模板乘法，未保存三种实际消费者回执。 | [方法条目](../by-type/ssti.md) |
| Smuggler No URL 与双端解析证据 | 终端Smuggler1.1显示ERROR No URL与usage，HTTP2外链未保存正文。 | [方法条目](../by-type/request-smuggling.md) |

| 并行枚举脚本的阶段产物与失败回执 | 保存脚本把域名枚举、历史URL、参数加工和多个扫描器串接；另帖把admin=true加工后交给不匹配的管道。 | [方法条目](../discovery/records-and-incremental.md) |
| Shodan 服务指纹与凭据主张的分离 | 帖子列MongoDB、FTP、Jenkins、Telnet、SNMP及RDP查询，并把一段RDP响应前缀标为密码。 | [方法条目](../discovery/passive-and-services.md) |
| 反汇编 INT3 分支与调试检测结论 | IDA图可见比较、条件跳转及INT3，但未保存执行路径与异常处理。 | [方法条目](../source-audit.md) |
| localhost 头与双斜线路由的同对象对照 | 正文提出X-Client-IP localhost；图把带对象ID的users路由403与省略对象ID后的另一users路由200并列，另帖切换Zabbix dashboard动作。 | [方法条目](../by-type/idor-access-control.md) |
| 源码敏感词与可用秘密的证据界限 | 候选包括dockercfg、私钥、FuelPHP profiler配置、门户JSON、Azure JS字段及两条被遮挡的ASIA匹配；Stacs图只是封面。 | [方法条目](../by-type/info-secrets.md) |
| Kunyu 与 Gotanda 的查询入口不是资产结果 | Kunyu帮助列hash、fingerprint、WHOIS及搜索模式；Gotanda菜单列IP、ASN、证书、URL和第三方查询入口。 | [方法条目](../discovery/passive-and-services.md) |
| 按位并行盲注的字符模型与稳定 oracle | 图有14行提取日志和7线程ASCII示例；另一卡片称检查多种参数形态即可100%找SQL注入。 | [方法条目](../by-type/sql-injection.md) |
| 多等号与上传扩展名的实际消费者 | 帖子建议文件名参数额外等号、PHP改phtml；Fuxploider图在localhost实验环境列12请求及phpinfo正则命中。 | [方法条目](../by-type/file-upload.md) |
| 批量 Git 更新与克隆的逐仓库状态 | 更新图同时出现非仓库、非目录、本地修改导致中止和已更新；ghorg图列69个仓库并显示Success。 | [方法条目](../discovery/records-and-incremental.md) |
| GraphQL 七类标签与具体执行边界 | 正文列注入、认证授权、业务逻辑和拒绝服务等类别，没有某个resolver的请求回执。 | [方法条目](../by-type/graphql.md) |
| 奖励与 Triaged 邮件的证据阶段 | 图中有Duplicate Closed、Still being assessed、P1/P4、高危标签及多份奖励；目录递归帖的750美元由两份不同金额图组成。 | [方法条目](../reporting.md) |
| JWT 在线解码与验证边界 | 帖子推荐在线JWT解码器，未保存签名校验或受保护操作。 | [方法条目](../by-type/authn-session.md) |
| 双引号反斜杠与 JavaScript 语法的消费顺序 | 帖子列双引号逃逸、globalThis、正则source、call/apply与HTML数字实体编码，没有真实浏览器成功回执。 | [方法条目](../by-type/xss.md) |
| ENS 名称与客户端校验后的存储读者 | 正文把ENS名称、绕过前端校验的字段、后台读取UA/IP及邀请邮件HTML作为入口，图片多为封面或报告标题。 | [方法条目](../by-type/xss.md) |
| Cloudflare Blocked 图的失败基线 | 配文声称Cloudflare新绕过，实际截图明确Blocked。 | [方法条目](../by-type/waf-bypass.md) |
| 分两步保存的中间状态与故障范围 | 作者称组名保存两步中断后刷新崩溃，图仅有DoS标签、500分类及分级奖励。 | [方法条目](../by-type/business-logic.md) |
| NTLM Type1 到 Type3 与真正的模拟权限 | RottenPotato图展示DCOM/SSPI握手；Nosferatu图仅见LSASS模块列表中一个非标准DLL。 | [方法条目](../by-type/authn-session.md) |
| 学习计划的反馈节奏与独立实验 | 手写图强调基础、Bash、自动化、CTF、周计划与专注；两组重复正文强调方法需适合环境。 | [方法条目](../hunting-strategy.md) |
| PAN-OS 版本分布与 CVE-2021-3064 适用性 | Shodan图计84632项且包含PAN-OS 9.1等版本；另帖扫描命令与新闻提到走私加溢出链。 | [方法条目](../source-audit.md) |
| 二维码公共视频通道的既有接收者 | 图显示YouTube公开QR视频1或3秒，正文提到多个云服务控制通道。 | [方法条目](../discovery/records-and-incremental.md) |
| 从 URL 与子域提取词表的结构损失 | 管道把URL标点转换为换行去重；PyIntruder图选参数标记、1到100、10线程与编码模式；子域图用tok加工后从ffuf展示文本切字段。 | [方法条目](../targeted-fuzzing.md) |
| 历史 origin 候选与 Host TLS 应用身份 | 一图在IP显示Angular/IIS并标50% sure，另一域名HTTPS图显示Akamai；证书CN与Cloudmare只是候选来源。 | [方法条目](../by-type/waf-bypass.md) |
| Boofuzz reset 与进程崩溃的关联证据 | 图列RUNNING、连接重置和监视进程的segfault代码；Hyenae仅显示菜单。 | [方法条目](../experiment-design.md) |
| 旧 Mongo ObjectID 结构与对象权限 | 保存newsletter按时间、机器、PID、计数器解释ObjectID，未保存当前驱动生成器或越权响应。 | [方法条目](../by-type/idor-access-control.md) |
| Base64 与 NAT 转发各自需要的消费者 | 正文提出base64让XXE/SSRF白名单失效、SSRF到NAT转发；另一命令只替换URL参数为回调地址，没有发送阶段。 | [方法条目](../by-type/ssrf.md) |
| 新密码接口的 ID 旧密码与挑战绑定 | 一图显示新密码POST的ID、existing encrypted password注释与200 code0；重置帖只保存accepted标题与两次奖励图。 | [方法条目](../by-type/authn-session.md) |
| OSI 示意图与实际跨层攻击链 | 示意图把攻击名分到七层，混列ARP、MITM、DoS、钓鱼和应用漏洞。 | [方法条目](../discovery/passive-and-services.md) |
| 虚拟机与 Kubernetes 安装回执的状态分层 | Windows实验图有ISO下载、KVM/VNC及驱动准备；Kubeapplier列30/30 Applied与黑名单，Kubernetes Goat图为实验目录。 | [方法条目](../cloud/container-k8s-security.md) |
| javascript URL 跳转与最终脚本来源 | DOM帖子只有accepted标题；NASA图分别展示HTML标题及域名弹窗。 | [方法条目](../by-type/xss.md) |
| 本地 xhr 页面与跨站写入的独立条件 | 截图只有本地文件页面与sessionid弹窗；另一帖将JSON改成urlencoded以避免preflight。 | [方法条目](../by-type/cors.md) |
| 数据库 root 到 Web 执行仍有多道权限 | 帖子直接从数据库root及outfile推断PHP shell或Windows IIS执行。 | [方法条目](../by-type/sql-injection.md) |
| 注销后的返回页面与新网络请求 | 正文把注销后Back看到敏感页面解释为缓存漏洞，未保存网络请求或会话验证。 | [方法条目](../by-type/authn-session.md) |
| phpinfo profiler 与目录清单的可见内容 | 图包含开发环境DB字段、Mongo URI、FuelPHP配置与目录文件名；有些值被遮挡，有些确实可见。 | [方法条目](../by-type/info-secrets.md) |
| WHOIS 外范围线索与供应商授权边界 | 图明示只有政策允许all org-owned assets时扩展；另一帖建议从外范围找内范围线索，招聘邮件说可能明年开展合作。 | [方法条目](../scope-and-rules.md) |
| Azure 审计查询的时间窗与完整性 | 截图连接Exchange Online并配置6小时、12间隔、1000聚合条目，没有查询结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 访问日志 200 筛选与 robots 的候选保真 | 日志管道grep 200后切引号字段，robots管道裁掉首字符；ffuf图显示普通页面与config长度差异。 | [方法条目](../discovery/web-and-api.md) |
| Stripe 测试接受与生产履约状态 | 原帖建议在生产结算尝试测试卡，配图为表情图，没有交易/订单证据。 | [方法条目](../by-type/business-logic.md) |
| ChopChop 的插件等级与响应证据 | 完整alt解释工具，图有Git exposed High、gitconfig路径、插件和修复建议。 | [方法条目](../discovery/web-and-api.md) |
| 低权限重放管理员新增动作 | 正文先捕获管理员请求再换非管理员；图题为ManageOrgAccounts升为admin与奖励。 | [方法条目](../by-type/idor-access-control.md) |
| CSP 图表的 fetch fallback 与 Report-Only | 两张完整CSP图把default-src和各种指令并列，并简化为允许/禁止资源。 | [方法条目](../by-type/xss.md) |
| Blind XSS 通知数量与实际后台读者 | 图为XSS Hunter的30/70 notifications及payload fired标题；正文猜登录UA被管理员页面消费。 | [方法条目](../by-type/xss.md) |
| IP Rotate 与高并发建议不能突破授权 | 帖子推广换IP绕过封禁、Fuzz everything及5000线程递归；另一帖主张所有子域进入HTTP前都需指定DNS链。 | [方法条目](../scope-and-rules.md) |
| S3 AccessDenied 与各动作权限 | 帖子从AccessDenied推测仍可找敏感脚本；另帖声称任意上传但未保存脚本全文或写入回执。 | [方法条目](../by-type/info-secrets.md) |
| Newsletter 的 race 名称与 TOCTOU 状态 | 完整newsletter提ConcreteCMS上传及Palo走私/溢出，底部ResourceSpace内容被裁切，没有具体竞态回执。 | [方法条目](../by-type/race-conditions.md) |
| Telerik rau 编码命中与真实处理器 | 正文把路径中一个字符百分号编码后得到200称为upload绕过，未保存上传或执行结果。 | [方法条目](../by-type/waf-bypass.md) |
| 登录 Help 到独立 IT 服务的访问边界 | 图仅显示Okta登录帮助里的IT ticket入口；配文称可自注册再读资料。 | [方法条目](../by-type/authn-session.md) |
| iOS 思维导图的客户端与服务端权限 | 完整图列本地文件、备份/日志、Keychain、URL schemes、WebView、认证、第三方库与通信，资源卡标July2020。 | [方法条目](../by-type/mobile-ios.md) |
| 合约五阶段审计与业务不变量 | 完整图从非代码信息、代码检查、漏洞思路、手动审计到工具验证，列transfer/send/delegatecall/selfdestruct等函数候选。 | [方法条目](../by-type/smart-contract.md) |
| PPScan 到 XSS 的 gadget 缺口 | 正文说ppmap把prototype pollution升级为XSS，图片为工具封面。 | [方法条目](../by-type/prototype-pollution.md) |
| NS 异常与二阶断链的实际消费 | 图有.cd的NS dig记录与扫描全TLD主张，另帖建议broken link checker找二阶接管。 | [方法条目](../discovery/passive-and-services.md) |
| 设置接口的属性映射与持久权限 | 正文建议在设置POST里加入页面/请求没有映射的字段，没有实际持久差分。 | [方法条目](../by-type/api-property-pollution.md) |
| nginx 分块初始化与历史 WAF 读者 | 保存图包含content_length_n置零、chunk-size大小写处理片段及一次blocked/另一次用户字段响应；附件列表本身没有全文。 | [方法条目](../by-type/waf-bypass.md) |
| 过滤器漏检与双端消息边界的不同证据 | newsletter讲Palo链，nginx文章图说明WAF可能未检查body，没有前后端连接关联记录。 | [方法条目](../by-type/request-smuggling.md) |
| 进程树 伪造日志与 LSASS 模块的可信来源 | MSTIC图有explorer/iexplore/msiexec及PID/命令；伪造日志帖只有封面，RegistryRecon只有菜单，SillyRAT列listener与Active session。 | [方法条目](../discovery/records-and-incremental.md) |
| phpLDAPadmin anonymous 选项与目录可读范围 | 正文称anonymous checkbox可读并分级high，图片只有triaged邮件。 | [方法条目](../by-type/ldap-xpath.md) |
| PDO prepare 内的字符串拼接不是参数绑定 | 代码图在getUserEmail把userid拼入SQL字符串再交给prepare，没有参数占位符。 | [方法条目](../source-audit.md) |
| 多解析器答案选择与子域去重 | 卡片把多个DNS resolver结果交jq的answers[0].name再anew，另一卡用展示文本取存活子域。 | [方法条目](../discovery/passive-and-services.md) |
| Metabase GeoJSON 的版本与文件读者 | 图有nuclei单模板命中、浏览器passwd样式内容及一串遮挡URL列表，没有全部目标的请求身份与完整回执。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 弹窗后的影响推导与受保护能力 | 帖子鼓励从XSS弹窗继续探索，没有后续权限链。 | [方法条目](../impact-and-acceptance.md) |
| WordPress 检查清单的检测与认证分层 | 完整卡片列header、xmlrpc、wp-cron、版本、主题插件、备份、用户枚举与口令爆破，并把random user agent称防火墙绕过。 | [方法条目](../discovery/web-and-api.md) |
| 4-ZERO-3 SQLi help 与执行结果 | 帮助图增加SQLi模式并用2xx至5xx着色，没有SQL求值或成功权限回执。 | [方法条目](../by-type/waf-bypass.md) |

| prepare 拼接示例的调用者约束 | 帖子指出prepare里的ID字符串拼接可能仍有SQL注入，未提供调用者/执行回执。 | [方法条目](../source-audit.md) |
| 目录尾斜线与上传执行链的阶段 | 正文从folder403和folder/200直接跳到unrestricted upload与RCE，没有上传或执行回执。 | [方法条目](../by-type/idor-access-control.md) |
| sed 全替换 URL 值与参数身份 | 图用正则把长URL各等号后的片段改成FUZZ，bhedak帖把多语法字符串送管道，SSRF候选grep参数词表。 | [方法条目](../targeted-fuzzing.md) |
| GeoJSON 文件文本与自动化确认节点 | 图片有Metabase浏览器文件样式内容及Trickest ListTargets→meg→ConfirmCVE工作流，局部输出可见；另有批量root:x匹配命令。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 自带参数在 Request.Form 异常页中的读者 | BYOP图有新增参数的POST、500 potentially dangerous Request.Form错误及浏览器弹窗；另帖说UA引号报错就有发现。 | [方法条目](../by-type/xss.md) |
| nuclei OOB 日志 MISSING 与告警附件 | 图有重复oob-header-based-interaction:dns、top-xss-params含格式化MISSING及Findomain邮件/扫描标签，附件未保存全文。 | [方法条目](../discovery/records-and-incremental.md) |
| 线程劫持示意与初始进程访问权限 | 配图只有目标线程与恶意进程示意，未见handle、权限、线程状态或执行日志。 | [方法条目](../source-audit.md) |
| 枚举 fingerprint 与资源认领权限 | 脚本串subfinder/assetfinder/amass/subjack；另一帖把Subzy候选直接导向新GitHub仓库/custom domain连接。 | [方法条目](../by-type/subdomain-takeover.md) |
| Swagger 标签下的反斜线路径与真实处理器 | Repeater图显示特殊反斜线路径、200 text/html和文件样式内容，配文称浏览器不适用并叫Swagger UI LFI。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Deep Dive 的可检验问题与覆盖边界 | 正文主张停留更久、不同入口/方法及从工具转影响；自动化图建议按web截图识别。 | [方法条目](../hunting-strategy.md) |
| 注销残留的 localStorage 与服务端会话 | 正文称注销后会话不失效，另一帖具体称localStorage里PII仍被其他人读取并获P4；未存具体字段/主体。 | [方法条目](../by-type/authn-session.md) |
| VictoriaMetrics 菜单与具体监控数据 | 图列vmui、targets、metrics、tsdb、top_queries和active_queries入口，没有每一入口实际返回数据。 | [方法条目](../discovery/web-and-api.md) |
| 监控 SQL 命中与数据库身份回显 | 一图在XML节点url里出现root@localhost、joomla、5.5.68-MariaDB，另图为CVE标签/union字符串。 | [方法条目](../by-type/sql-injection.md) |
| RMI 蜜罐警告与工具输入不可信 | 正文提醒1099 RMI可能是anti-ysoserial蜜罐，另帖提醒fake tips；外链未保存方法。 | [方法条目](../scope-and-rules.md) |
| 版本冻结口号与可重复的软件基线 | 图列Burp Professional v2020.2.1，正文称从不更新最稳定，另帖建议检查不同浏览器版本。 | [方法条目](../discovery/records-and-incremental.md) |
| 报告邮件的准确主张与阶段标签 | 图有6个月54次提交、P2奖励、Critical Triaged、P1 New、gruntfile P3未解决、邮件与HoF；一封模板将login clickjacking直接称ATO。 | [方法条目](../reporting.md) |
| Apple PII 弹窗与跨服务影响的范围 | 截图在500 JBoss异常页显示accountSummary/purchaseHistory样式弹窗且部分字段被遮挡，正文声称多个Apple服务。 | [方法条目](../impact-and-acceptance.md) |
| 完整 recon 导图的横向纵向与主动边界 | 多张完整图包含IP/ASN、收购/WHOIS、证书、子域、JS、历史URL、GitHub、VHOST、CMS、WAF、端口及fuzz；AssetDiscovery卡区分横向、被动/主动纵向和web端口。 | [方法条目](../discovery/passive-and-services.md) |
| Whoc runtime 图与容器初始权限 | 图示runtime执行/proc/self/exe，容器再打开、execve上传进程并发送fd，未存真实文件内容/运行日志。 | [方法条目](../cloud/container-k8s-security.md) |
| RapidDNS HTML 切字段的归属保真 | RapidDNS管道靠td/a与斜线字段取域名；另帖列加密货币program dorks。 | [方法条目](../discovery/passive-and-services.md) |
| 跨字段拆分属性的最终 HTML 结构 | 图把q与color两个字段分开，使最终img示意出现额外属性并标Filter Bypassed，没有真实浏览器回执。 | [方法条目](../by-type/xss.md) |
| Zero Click 名称与注册 email 页面 | 正文称Zero Click ATO，图只有完成注册的邮箱表单。 | [方法条目](../by-type/authn-session.md) |
| 百分号十六进制说明与实际解码次数 | 正文把多层百分号字符串解释成SQL/注释，却有数字与引号对应不准确的说明，没有数据库响应。 | [方法条目](../by-type/sql-injection.md) |
| Nanobrok 管理画面的设备与初始连接 | 图显示Genymobile设备、Android10、emulator、无线信息/日志与no locations found，未见注册或权限取得过程。 | [方法条目](../by-type/mobile-android.md) |
| APISIX public 与 protected 基线 | 保存图只有public服务数据与protected403，文章主题是request_uri路径遍历及GitHub错误用法，没有成功越权图。 | [方法条目](../by-type/idor-access-control.md) |
| FCKeditor 目录指纹与 phpinfo 路径清单 | 正文列FCKeditor connectors与四条phpinfo候选，XAMPP图把setup路径称AuthBypass；phpinfo帖配图只有付款。 | [方法条目](../discovery/web-and-api.md) |
| Burp Intercept 等待与真实 HTTPS 捕获 | 有人问CA下载问题，另一条提醒打开Burp后等待可能因Intercept。 | [方法条目](../discovery/records-and-incremental.md) |
| 整数算术比较与方法切换的 consumer 差分 | 正文建议整数用数学对照而非直接引号，另一帖GET换POST，binary search帖仅外链；HoF图不含查询。 | [方法条目](../by-type/sql-injection.md) |
| 动态 DNS 目录与不同语言的配置字段 | 正文称动态DNS索引可浏览家用文件、不同语言找credential、GET参数可能敏感；图邮件明确凭据仅test环境/internal VPN且P4。 | [方法条目](../by-type/info-secrets.md) |
| OTP requires_2fa 替换与后端验证状态 | 正文改requires_2fa为null；一张OTP图只有长captcha表单请求，响应操作卡主张将paywall状态改200。 | [方法条目](../by-type/authn-session.md) |
| JS grep 281 行不是 281 条当前 API | JS图从httpClient.get切文本得到281行和含模板变量的接口，gf图筛siteKey有linker warning。 | [方法条目](../discovery/web-and-api.md) |
| Nginx Microsoft Apache 横幅不等漏洞版本 | 帖子列Nginx1.14.0、Microsoft10.0、Apache2.4.41作为unique vulnerable候选，没有组件配置和实际根因。 | [方法条目](../source-audit.md) |
| 4-ZERO-3 Forbidden 帮助与 4xx 结果 | 两图为工具帮助，列头、方法、路径、编码、代理/UA等模式和输出选项，没有实际保护能力差分。 | [方法条目](../by-type/waf-bypass.md) |
| DetectionLabELK 的采集检测存储三阶段 | 架构图从Windows/DC事件、beats、osquery/Velociraptor/Sysmon/Suricata/Zeek至ELK，并列RDP/SSH/web发布端口。 | [方法条目](../cloud/container-k8s-security.md) |
| FirstBlood 标题中的预约与身份不变量 | 完整报告目录含X-SITE-REQ、预约ID、doctor/patient、disabled email、同用户名覆盖与注册ATO，只有标题/等级。 | [方法条目](../by-type/idor-access-control.md) |
| Redux AJAX 信息与 secret 哈希的不同能力 | 一图返回WordPress插件/版本JSON；另一完整说明将CVE38314关联Redux/Gutenberg插件、可推导AJAX action、外部verify和合并secret的md5，附代码。 | [方法条目](../by-type/info-secrets.md) |
| Frida 练习变量与服务器保护能力 | 正文列修改硬编码变量、函数返回、实时变量和PIN爆破，图是教程封面与资源索引。 | [方法条目](../by-type/mobile-android.md) |
| href 字符实体的准确拼写与 URL 规范化 | 正文给Tab/colon/NewLine候选，但示例含tap以及文字NewLIne等不一致拼写，未存浏览器回执。 | [方法条目](../by-type/xss.md) |
| AEM setPreferences 错误 MIME 与未完成执行 | 图有setPreferences后缀变化、4xx响应、text/javascript及Invalid keymap文字，h1样式字符串未显示成HTML；正文承认无法绕Content-Type。 | [方法条目](../by-type/xss.md) |
| title noscript 图中的解析模式 | 图建议闭合title或noscript逃逸并混写unscript，没有当前页面/执行记录。 | [方法条目](../by-type/xss.md) |
| Origin ACAO 精确差异与浏览器读权限 | 片段先列wwwx.in精确匹配，再列evil.ie与evilx.ie不一致同时ACAC true，没有浏览器响应读取。 | [方法条目](../by-type/cors.md) |
| 数字实体括号与奖励金额的解码层 | 正文列数字实体编码的SVG函数括号，图片只有两项XSS重新分级各1000及两项信息泄露合计250；另帖为偏好payload。 | [方法条目](../by-type/xss.md) |
| 平台协作设置与数据分享授权 | 正文列Friends/Anyone及AddCollaborator，图片为封面，没有实际policy或权限授予记录。 | [方法条目](../scope-and-rules.md) |
| Base64 FROM_URL 与 Continue 按钮消费者 | 完整图有activationKey/LANGUAGE/FROM_URL、Base64注入片段和点击Continue步骤，第二图为fixed/sw ag邮件。 | [方法条目](../by-type/xss.md) |
| 报告润色工具与秘密字段的最小共享 | 帖子推荐QuillBot写报告/改标题，未存自动化实现。 | [方法条目](../reporting.md) |
| Actuator Logview 的 base 与 filename 读者 | 图是localhost:8887日志view、filename/base参数及文件样式内容，文章题为CVE21234；未存版本/远程身份。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 未闭合资源属性与 dangling markup 的请求证据 | 完整示意将未闭合img src包裹后续CSRF/email文字并标exfiltrated，没有实际浏览器出站回执。 | [方法条目](../by-type/xss.md) |
| DNS 重绑定的两次解析与 IMDSv2 条件 | 正文称从外部URL到EC2 metadata全内容；另帖说every EC2都有credentials，IPv6卡列IPv4-mapped地址，没有请求回执。 | [方法条目](../by-type/ssrf.md) |
| Markdown 多行和引用链接的同一 URL 校验 | 正文提Multi-line与reference style链接造成两种Markdown XSS，没有保存源码/渲染回执。 | [方法条目](../by-type/xss.md) |
| 两百万线程玩笑与分布式 fleet 的预算 | 正文给ffuf两百万线程并配BOOM，Axiom图创建三台fleet并成功selected，另帖要求portscan everything。 | [方法条目](../scope-and-rules.md) |
| git 目录 403 与子文件的最小内容 | 图把.git403与config/logs HEAD200并列，无真实文件内容；正文给批量path检测。 | [方法条目](../by-type/info-secrets.md) |
| Crawpy 的过滤词数与被排除读者 | 图列GET、50 semaphore、follow false、php/html扩展、过滤9/83词及若干200/301/302/400。 | [方法条目](../targeted-fuzzing.md) |
| embed image 与完整 SSRF 导图的消费阶段 | embed图只有1500美元accepted；完整SSRFMindmap列URL/Unicode/IP别名、DNS pin/rebind、redirect、file/rendering/proxy、scheme、内网和metadata。 | [方法条目](../by-type/ssrf.md) |
| Firebase REST PUT 回显与允许写入范围 | 图为一个Firebase用户路径PUT JSON及200相同字段，没有后续读取/规则/认证结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| vCenter provider logo 列表与 file 协议假设 | 正文给版本和provider-logo fileURL，图仅httpx v1.1.0的遮挡列表，没有每项原始响应或部署版本。 | [方法条目](../by-type/lfi-path-traversal.md) |
| ClusterFuzzLite CI 红灯与可归因 crash | 截图PR称Add a crash to do_stuff_fuzzer，All checks failed/Fuzzing failing，未存栈/case或诊断详情。 | [方法条目](../experiment-design.md) |
| OAuth 完整导图的 code grant 与撤销不变量 | 完整图含code复用/跨client、state、redirect URI/mobile scheme/open redirect/Referer、clientsecret/token、grant错配、refresh竞争及evil app revoke。 | [方法条目](../by-type/oauth-oidc.md) |
| SageMaker Self XSS 到 CSRF 的用户动作缺口 | 图片只有同notebook域的Start Attack链接和Jupyter/SageMaker页签，正文称instance takeover链。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| DLL Scanner Trusted Directory 字符与 24/192 | 终端显示system与fake directory字面差异、多个exe→DLL Vulnerable及24/192计数，没有独立加载/提升回执。 | [方法条目](../source-audit.md) |
| paywall 200 修改与服务器订单权益 | 响应截获卡称改支付HTTP状态为200可到下一步或完全绕逻辑，没有订单/权益回执。 | [方法条目](../by-type/business-logic.md) |
| PDF creator 执行主张与服务器取资源 | 正文称自动PDF里的JS会由creator执行导致SSRF，未存实际引擎/配置/网络回执。 | [方法条目](../by-type/document-rendering.md) |
| GitLab 旧默认口令与 root 菜单观察 | 三条帖子建议同一旧默认口令，图只有Administrator @root菜单；CredzCheckr为工具介绍。 | [方法条目](../by-type/authn-session.md) |
| Rate limit 图的限额主体与客户端通道 | 完整卡列forwarded来源头、控制字符、Web/Android/iOS、UA/cookie变化，没有实际限额/请求对照。 | [方法条目](../by-type/authn-session.md) |
| 不可编辑 dropdown 的请求值与真实存储 | 图为Feature request下拉菜单与Submit，正文建议拦截改成XSS/BXSS值。 | [方法条目](../by-type/xss.md) |
| 有 token 的 CSRF 假设与 critical 标签 | 正文建议有token也继续、emailchange，图却含H2RCE P1 New与另单CSRF Critical Triaged；无浏览器跨站证据。 | [方法条目](../by-type/csrf.md) |
| diodb 2304 总数与权限字段的交叉分布 | 三帖同组列2304、goodfaith158、authorization239、bounties379、swag42，字段可能重叠。 | [方法条目](../scope-and-rules.md) |
| Toutatis cookie 图与个人信息访问者 | 图只有Instagram cookie面板/圈出session项，没有邮箱/电话号码返回，正文称工具可提个人信息。 | [方法条目](../by-type/info-secrets.md) |
| KitHunter 关键词命中与真实数据消费者 | 图中 KitHunter 按标签/关键词扫描解包内容，出现 Google exit、header/href 和追踪标签等命中；未给出可达漏洞或真实用户数据传输证据。 | [方法条目](../source-audit.md) |
| 网络命令速查卡的行为与授权边界 | 完整速查卡包含接口/IP/MAC、DNS/WHOIS/证书、抓包、ARP、远程捕获、扫描脚本与 shell 等不同动作；工具将脚本标为 safe 或列出高发送速率，不代表目标授权或无副作用。 | [方法条目](../scope-and-rules.md) |

| 上传 iframe 与元数据请求发起者 | 帖子将未过滤iframe的HTML上传直接连到AWS元数据；关键前提是实际服务器渲染器发请求。 | [方法条目](../by-type/ssrf.md) |
| GitLab 搜索命中与历史口令建议 | 正文列旧root/admin口令并建议按org/title查GitLab；仅保存历史建议，未有实际登录交换。 | [方法条目](../by-type/authn-session.md) |
| HPP 速查图的解析器与消费者差异 | 完整HPP图比较重复q的首项/末项/合并及客户端链接、付款网关两个消费者。 | [方法条目](../by-type/api-property-pollution.md) |
| Grafana 插件路径与代理规范化的历史条件 | 保存图中部分遮挡请求返回passwd样式文本，另一图可见插件路径/200文本；nuclei high标签单独保留。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 隐藏 JS 变量提取管线的结构损失 | 图按var正则、cut、sort从JS采集参数，再交给扫描器；另一完整卡用注释、URL、/api和普通单词匹配。 | [方法条目](../discovery/web-and-api.md) |
| 负数反应值与计数不变量 | 正文将like从1改为-100，图只有triaged负计数标题，未见持久状态或计数请求响应。 | [方法条目](../by-type/business-logic.md) |
| 金额、RCE 标签与修复受理的独立记录 | 本批图含Critical RCE标题、30日4275及200待付、Google遮挡奖励、100欧Medium/250美元Low/500USDC入账/200USDT修复、1000美元首位有效及282币约202美元；不是同一技术链或通用等级。 | [方法条目](../reporting.md) |
| 情报关系图的资产键与主动动作 | 完整关系图连接公司/ASN/网络/域名/主机/服务/路径/邮箱/账号和漏洞，含WHOIS、证书、DNS、扫描及密码暴力等性质不同的边。 | [方法条目](../discovery/passive-and-services.md) |
| IP 转发标题与证书绑定证据 | 相关文章标题称iptables/IP forwarding绕过SSL pinning，现有图仅VirtualBox GooglePixel PoweredOff和硬件/磁盘配置，无TLS验证代码或握手。 | [方法条目](../by-type/mobile-android.md) |
| APK 正则命中 Google Maps key 的边界 | 完整卡从APK目录按AIza格式grep，只显示提取命令，无实际key返回。 | [方法条目](../by-type/info-secrets.md) |
| 按业务语言选择词表的假设 | 正文称Heridas指wounds，西班牙词表找到usuarios并泄露员工信息，没有保存原始权限请求。 | [方法条目](../discovery/passive-and-services.md) |
| Host FUZZ 虚拟主机与实际路由身份 | 正文ffuf Host候选含有不规范URL空格，未保存成功响应。 | [方法条目](../by-type/host-header.md) |
| LinkFinder 端点与六百美元权限案例 | 保存正文只有LinkFinder ^/参数、端点/Access control声明和600奖励，未给对象、身份或响应。 | [方法条目](../by-type/idor-access-control.md) |
| SMBeagle 共享发现与有效读写主体 | 完整流程图分本机接口/netstat与白黑名单、445测试、共享枚举、UNC/本地根与文件权限、输出CSV/PDF/Elastic；没有实际文件结果。 | [方法条目](../discovery/web-and-api.md) |
| PHP echo 正则候选到输出上下文 | 正文grep匹配echo与GET/REQUEST/POST仅定位可能热点，未保存实际源码命中。 | [方法条目](../source-audit.md) |
| 自动轮换会话后的请求主体保真 | Burp Session Handling tracer图显示cookies replacement与check session issued request，localhost回执细节为空。 | [方法条目](../by-type/authn-session.md) |
| 反编译 SQLite 凭据示例与真实可读性 | VSCode DIVA样例可见SQLite创建user/password列、INSERT拼接和saved toast，右侧代码截断。 | [方法条目](../by-type/mobile-android.md) |
| Tarian 的注册、同步与检测动作 | 完整架构图含CLI/UI注册、config/analytics DB、RBAC/dex/openEBS、sidecar同步、已知威胁动作/自毁pod、未知变化告警、社区数据和FluentBit聚合。 | [方法条目](../cloud/container-k8s-security.md) |
| Log4j DNS 回调的归因与可提交证据 | Canary回执明确source IP指DNS服务器；另图有DNS/AAAA、hostName/header/java.version组成域名，正文警告云服务回调及缺变量。 | [方法条目](../discovery/records-and-incremental.md) |
| Log4j 旧 JVM 阈值不能定义全部漏洞条件 | 正文“只查Java版本/不低于阈值就换目标”把远程类加载条件等同整个风险；图11.0.3仅来自一次DNS字段。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Canary 创建表单与已观测通道 | 三图依次为DNS token创建表单、lookup示例、DNS triggered回执；创建/生成字符串不是实际测试，回执也只说明标注的通道。 | [方法条目](../discovery/records-and-incremental.md) |
| Log4j 列表管线与有效输入归因 | 保存管线使用sed去scheme、xargs shell/httpx多header和bbrf列表；实际图一轮显示Targets does not seem vulnerable，下一轮Waiting，不能把等待/阴性自动扩成全列表。 | [方法条目](../targeted-fuzzing.md) |
| 重复 Host 与重置链接的信任来源 | 帖子同时列两个Host并追加X-Forwarded-Server/Host等，没有生成重置链接的证据。 | [方法条目](../by-type/host-header.md) |
| Host 端口声明与缓存故障的可观察范围 | 正文将Host写成含scheme的:22并声称DOS，附图却是数个奖励/等级邮件，没有全局持久故障证明。 | [方法条目](../by-type/host-header.md) |
| Nmap XML 到 Searchsploit 的候选关联 | 正文版本扫描导出XML再匹配潜在利用，仅展示命令，没有目标响应或实际利用。 | [方法条目](../discovery/records-and-incremental.md) |
| 全局 Match and Replace 与信息字段外发 | 完整Burp规则把User-Agent替换lookup，编辑框含env:user；已有代理配置不证明所有流量已测试，也不能让归档串外发用户名。 | [方法条目](../targeted-fuzzing.md) |
| ADenum 的已认证 LDAP 枚举 | 原图命令提供用户/密码并显示Successfully Authenticated with LDAP及Domain Admin列表，SSL connect FALSE；不是无凭据进入域。 | [方法条目](../source-audit.md) |
| Log4j 两阶段图与实际可达执行链 | 两份完整图先用户输入→日志→LDAP响应reference/codebase/factory，再下载类；另一图还示意serializedData和不同防护点。 | [方法条目](../by-type/cmd-injection-rce.md) |
| SVG 上传请求与真正脚本消费者 | 图可见image/svg+xml请求体及脚本，未展示存储后读取/执行；正文SVG结束标签亦不完整。 | [方法条目](../by-type/xss.md) |
| Struts 日期异常到日志调用的边 | 源图片段getDateHeader If-Modified-Since异常后LOG.warn写入原始header；示例localhost不证明所有Struts/生产部署使用易受影响日志组件。 | [方法条目](../source-audit.md) |
| bhedak Windows 替换输出的语义保真 | 完整Windows图将多个URL参数值替换hello，含%20与80端口；工具改Python regex不自动保证与sed全部等价。 | [方法条目](../targeted-fuzzing.md) |
| Pitchfork 的同步位置与回调字段 | 三图有Pitchfork、101 payload/request count、header名与lookup内同步标记，以及DNS标注X-Forwarded-For和11.0.10。 | [方法条目](../targeted-fuzzing.md) |
| Solr action 字符串与 400 拒绝基线 | 实际图/solr/admin/cores action lookup返回400及SolrCore Initialization Failures invalid core；正文另列collections和ReverseShell链，无实际执行回执。 | [方法条目](../by-type/cmd-injection-rce.md) |
| POST 与 GET 参数的动作等价前提 | 正文建议把POST参数当GET尝试，未保存结果。 | [方法条目](../targeted-fuzzing.md) |
| FiddleZAP Magecart 标签与静态脚本关系 | 图标High Magecart FakeClicky，显示正常外观Google标签及atob和document.write构造脚本；只有静态响应与工具标签，没有实际数据发送。 | [方法条目](../source-audit.md) |
| Findomain validate 清洗与资产可达性 | 图从混有波浪/斜线/逗号/下划线前缀的列表筛出域名；发布性能声明没有基准结果。 | [方法条目](../discovery/passive-and-services.md) |
| Haptyc 范围标记与请求变异边界 | 图只标出GET account的[radamsa]和[end]以及输入区，未显示响应或失败样本。 | [方法条目](../targeted-fuzzing.md) |
| Imperva 标题与 Cloudflare SQL 错误图的错配 | 正文称Incapsula/Imperva，图响应却标Cloudflare并暴露MySQL语法和查询片段；不能从配图确定WAF产品或完整绕过。 | [方法条目](../by-type/waf-bypass.md) |
| Dalfox URL 过滤、去重与 blind 受众 | 完整卡gau/subs、HTTPS、扩展grep、含等号、uro、Dalfox deep-domxss/multicast/blind串，是候选管线无成功回执。 | [方法条目](../targeted-fuzzing.md) |
| Telerik rau 百分号变化仍需实际处理能力 | 正文显示AkamaiGhost阻断与r%61u200，未有响应体、组件版本或上传执行结果。 | [方法条目](../by-type/waf-bypass.md) |
| AngularJS 版本输出与服务端模板的区别 | SSTI-XSS-Finder图显示AngularJS1.7.2/1.5.3及按版本推荐表达式，没有真实模板输入、渲染和弹窗。 | [方法条目](../by-type/ssti.md) |
| 反斜线数字引号实体与弹窗的上下文 | 正文字符串混反斜线、数字引号实体和confirm；图只弹窗1且origin遮挡，没有完整注入位置。 | [方法条目](../by-type/xss.md) |
| Oracle 延迟建议与稳定时间判据 | 正文列DBMS_PIPE RECEIVE_MESSAGE及十秒参数，涉及login/signup/forget，没有实际执行/耗时对照。 | [方法条目](../by-type/sql-injection.md) |
| 语言 cookie 文件返回与读取权限 | 图language/lang请求cookie s_language有遍历，200 octet-stream长度38返回root行敏感部分已遮挡；只支持这次历史文件内容读取，非OS root。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 403 页面和下载对话框不足以确认泄露 | 现有图是Forbidden页面叠浏览器下载对话框，目标与文件名遮挡，无响应headers/内容。 | [方法条目](../by-type/file-upload.md) |
| SeaweedFS Filer 目录及 shell 文件名 | 完整Filer图可见Upload入口和jsp/php/jars、命令样式文件名，只有列表/尺寸/时间，没有文件读取或执行。 | [方法条目](../by-type/info-secrets.md) |
| Jira CVE 卡混入 Confluence macro 的纠正 | 完整卡列12项历史SSRF/XSS/用户枚举/信息/模板/遍历，并将tinyMCE macro preview/WidgetConnector CVE-2019-3396放在Jira标题下。 | [方法条目](../discovery/records-and-incremental.md) |
| 五千二百 PII 声明与脱敏表格范围 | 正文称JS线索找到5.2k PII/权限缺陷；两表可见customer/supplier、地址/电话字段和受理High通知，表只部分行且脱敏，没有请求/身份对照。 | [方法条目](../by-type/idor-access-control.md) |
| 反斜线等价性须绑定实际 URL 解析器 | 正文将backslash解析差异连到redirect/SSRF，未给具体两个消费者及结果。 | [方法条目](../by-type/ssrf.md) |
| diodb 2305 更新与重叠政策字段 | 历史目录本批2305、good-faith158、authorization239、bounties380、swag42，比前批总数/奖金项增加一，但字段非互斥。 | [方法条目](../scope-and-rules.md) |
| deep recon 与多 CVE 等级的证明边界 | 正文列AWS takeover High、两个CVE Critical/Medium及Rxss Medium，建议deep recon+nuclei；没有完整技术对照。 | [方法条目](../discovery/records-and-incremental.md) |
| JWT none 与应用预期验证的差异 | 保存正文只到第一条none/改claim步骤，未保存其余两技巧或实际响应。 | [方法条目](../by-type/jwt.md) |
| PII 与 admin 搜索式的实际受众 | 两个Google式包含site、phone/email/name/admin/login和排除项，未保存结果；｜及大小写/引号的实际查询语义需结果确认。 | [方法条目](../discovery/passive-and-services.md) |
| CVE Trends 热度与历史风险等级 | 图聚合Twitter/NVD/GitHub、日期/CVSS/EPSS/受众，45046显示历史LOW3.7；当前Apache公告已列CRITICAL9.0，不沿用旧图评级。 | [方法条目](../discovery/records-and-incremental.md) |
| 版权表单 blind XSS 与创作者能力链 | 正文称假版权通知触发创作者blindXSS/ATO，图只1632奖励及禁止未经许可披露弱点的历史通知，没有真实接收者/会话能力。 | [方法条目](../by-type/xss.md) |
| Log4j 混淆接受与 JNDI 求值分阶段 | 保存图中GET旧混淆403、另一混淆400含Envoy上游；POST旧串403、新串200空数组，正文又称旧方案已补。 | [方法条目](../by-type/waf-bypass.md) |
| MySQL 时序与 swap-case/comment 的假设 | 正文XOR条件/时间与大小写注释改形只有载荷/声称，缺保存可用响应。 | [方法条目](../by-type/sql-injection.md) |
| View source 的 username/password 字段类型 | 正文仅称查看源码搜索username找到网址和账号/密码，缺实际字段上下文或认证成功。 | [方法条目](../by-type/info-secrets.md) |
| file 方案的多层解码与变量语法 | 保存一组file URL问号/双编码/点段及br/u/te变量形式，没有实际解析器或响应，不能默认执行shell展开。 | [方法条目](../by-type/lfi-path-traversal.md) |
| JNDI 蜜罐记录与 IP 声誉归因 | 图只有IP reputation输入页和自动加黑的蜜罐描述，无实际日志行/目标命中。 | [方法条目](../discovery/records-and-incremental.md) |
| Flywheel Oops 页面与可声明性 | 图是Flywheel未设置正确站点提示及域名管理示意，没有账号声明/绑定成功。 | [方法条目](../by-type/subdomain-takeover.md) |
| Sudomy 速度建议与请求预算 | 完整卡称低requests/sec时用Sudomy省时间，命令却含httpx/dnsprobe/webanalyze等动作；不能把“别人已侦察”推导为全部被动或不计请求。 | [方法条目](../discovery/passive-and-services.md) |
| Firebase 公共规则图与 REST 权限范围 | 早图为标题封面，后完整Rules图显示根read/write true及公共警告；未给实际部署项目/REST请求和持久数据。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 快速响应的三个范围外问题 | 正文明确三问题全部out of scope，即使安全团队响应快也不能推导赏金资格。 | [方法条目](../scope-and-rules.md) |
| XSSR 发现标签与实际浏览器执行上下文 | 保存图同时出现XSS FOUND标签及查询页弹窗；弹窗显示一次浏览器执行，查询和来源部分裁剪，仍不能直接证明其他主体读取或受保护能力。 | [方法条目](../by-type/xss.md) |
| 用户信息响应、会话 cookie 与可读主体 | 保存响应是200，含basicInfo及角色/部门/经理/工时休假字段，多项为空，同时有HttpOnly会话cookie及Access-Control-Allow-Origin星号；未保存未认证对照或跨源脚本读回。 | [方法条目](../by-type/info-secrets.md) |

| 文件系统 Log4j 标签与实际加载组件 | 图列多个嵌套jar/WAR里的core版本和VULNERABLE标签。 | [方法条目](../discovery/records-and-incremental.md) |
| Log4j 训练扫描的 Target Affected 输出 | 扫描图示localhost训练地址、DNS目标、Waiting和Target Affected；它保存的是扫描器判断和通道信息，未给类加载/命令结果。 | [方法条目](../discovery/records-and-incremental.md) |
| mapcidr 枚举不能扩展主机授权 | host-based文章配图仅将/23网段展开为IP列表，未证明每地址当前由目标控制或获准测试。 | [方法条目](../scope-and-rules.md) |
| 自定义子域词表与搜索 UI 的覆盖 | 界面显示Default/上传词表下拉和少量结果；设置入口和表格不证明词表全部执行或DNS可达。 | [方法条目](../targeted-fuzzing.md) |
| 按星期变化的 WAF 现象要控制变量 | 正文称周三周日不受阻，其余天受阻，没有保存相同时段/身份的原始对照。 | [方法条目](../experiment-design.md) |
| 证书搜索命中与 origin IP 归属 | 保存Shodan SSL/CN式和旧origin配置备份路径建议；搜索语法是否有效、证书关联、虚拟主机和当前归属均需证据。 | [方法条目](../discovery/passive-and-services.md) |
| 负整数购物车建议与服务端金额不变量 | 正文只给价格操控视频题名和负整数运算建议，未保存订单/交易交换。 | [方法条目](../by-type/business-logic.md) |
| 邀请占用邮箱到注册可用性的状态链 | 三帖完整保存：攻击者邀请未注册邮箱，收件人不点击邀请而正常注册，出现Email already exist并不能创建账号；正文称奖励100。 | [方法条目](../by-type/authn-session.md) |
| username 与 X-Forwarded-For 的不同注入位置 | 一帖由证书线索到username/sqlmap高风险选项并配Closed Critical标签；另一图标定custom HEADER X-Forwarded-For，74请求及MySQL time-based判断。 | [方法条目](../by-type/sql-injection.md) |
| JS grep 的域名正则与实际 URL 边 | 正文正则和泛称JS可找子域/端点均为静态线索，正则字符类[A-z]及分段结构不能作为所有域名规范验证。 | [方法条目](../discovery/web-and-api.md) |
| nuclei 聚类与多等级命中的证据归并 | 两张图有402聚类/减少369HTTP请求和多个critical/high/medium/info/CVE标签，正文是情绪反应。 | [方法条目](../discovery/records-and-incremental.md) |
| 替换 2FA 响应与真正的服务端能力 | 正文建议将403/404/503变200、false变true/error变success，配图实际是200USD处理邮件，未保存服务端验证。 | [方法条目](../by-type/authn-session.md) |
| Abuse Risk、P4、已修复和奖励的分开记录 | 图展示Google Abuse Risk转Trust & Safety、Sensitive PHP info page获奖、Closed SQL Critical/未付、Grafana snapshot P1 Triaged、Log4j Medium和Synack四项1760/1408/588/270；这些状态不提供实际机制交换。 | [方法条目](../reporting.md) |
| 仅登录面板词表与隐藏功能假设 | 正文为仅登录面板提供词表入口；界面可见功能少不代表后台只有认证。 | [方法条目](../targeted-fuzzing.md) |
| S3 ListBucket 拒绝不说明 PutObject 被拒绝 | 正文分别称ls拒绝、cp上传，图只为Misconfigured s3 bucket Triaged邮件。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| localhost 变体、IPv6 与实际解析层 | 完整列表含短IPv4、十进制/十六/八进制样式、userinfo、IPv6未指定/缺括号形式；不能都称127.0.0.1等价或对所有解析器有效。 | [方法条目](../by-type/ssrf.md) |
| SSRF 的真实影响不由 RCE 标签替代 | 正文两相同体帖子主张不要报SSRF应升级RCE，另帖询问DNS是否足够；缺少实际第二阶段。 | [方法条目](../impact-and-acceptance.md) |
| 同一第三方主体连接两个本地账号 | 保存步骤是provider先连account1再连account2，邮件题名为authorization token misconfiguration/3000；未保存redirect/state/token交换。 | [方法条目](../by-type/oauth-oidc.md) |
| JS 内部 host 和 port 只生成候选 | 正文建议失败后搜main.js/app.js的localhost/127.0.0.1/host/port；图仅局部JS regex里localhost:53519，没有内部请求读回。 | [方法条目](../by-type/ssrf.md) |
| 工作邮箱域名过滤与身份要求 | googlemail绕gmail限制是域字符串策略假设，未保存账号创建或权益。 | [方法条目](../by-type/business-logic.md) |
| Burp history 与个人 wiki 的可追溯笔记 | 正文分别强调Repeater/History和持续个人wiki；可复用的是来源、假设与实验的连续记录。 | [方法条目](../discovery/records-and-incremental.md) |
| GitHub Dork Helper 与 Slack webhook 搜索 | 图是关键词生成器以及54条代码搜索/部分Webhook字符串；命中数字或格式不说明仍有效、归目标或具有读频道能力。 | [方法条目](../by-type/info-secrets.md) |
| XMB 嵌套 BBCode 到事件属性的消费者链 | 完整保存嵌套url标签文本，图是localhost私信admin到admin和弹窗1，渲染正文混入onclick片段。 | [方法条目](../by-type/xss.md) |
| JNDI 混淆后的应用校验仍不证明求值 | 保存AWS PUT/cart同类请求403 ForbiddenException对比400 Envoy返回Required value itemId must contain 6 characters，字符串被反射；另帖只有混合lookup正文。 | [方法条目](../by-type/waf-bypass.md) |
| curl 子域脚本的超时与状态码边界 | 完整脚本以词表循环curl半秒timeout，每次睡0.1，1000计数时睡10，并将非000写文件；图有未引用变量和$x=0等可疑重置。 | [方法条目](../targeted-fuzzing.md) |
| JWT 历史问题类型不能只看 none | 正文列none、HS/RS公钥混用及node-jose旧CVE，1/2提示的后续外链按用户口径覆盖；配图仅装饰。 | [方法条目](../by-type/jwt.md) |
| 付款 API amount 的截图与实际权益 | Shopify插件题名配付款页146.08SGD与API请求amount/订单字段，但响应面板空，未有支付完成或服务端订单读回。 | [方法条目](../by-type/business-logic.md) |
| 完整 Log4j 速查卡的通道、变量与权限 | 卡列控制字符串的headers/输入/文件/EXIF等入口，DNS里的host/Java版本、训练服务/扫描器，以及sys/env变量；还泛称旧版本范围RCE。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 赋值调用与 optional chaining 的演示边界 | 正文给赋值confirm和注释/optional chaining变体；后图明确在chrome new-tab控制台自行调用alert。 | [方法条目](../by-type/xss.md) |
| SeImpersonate 的已获入口与 SYSTEM 后置条件 | MultiPotato图先显示SeImpersonate enabled，后创建pipe/duplicate token并报告SYSTEM及本地用户加入管理员。 | [方法条目](../source-audit.md) |
| PII 文章配 OOB 列表的证据错配 | 正文称数百万投资者/注册信息，图却只有Burp OOB交互三条，目标遮挡，无PII字段或匿名读取。 | [方法条目](../by-type/ssrf.md) |
| 批量删除 JSON 与逐对象授权 | Phineas正文/flag替代文字配图却是多个数字payload均200和data.BulkDeleteAlertDefinitions，结果是website/alertDefinitions/id/typename嵌套。 | [方法条目](../by-type/graphql.md) |
| SQLbit 的布尔真值须保持查询与行号语义 | 图配置stock中的项作为True判据，展示count14、长度和unicode/行号及商品名；这是工具输出，未保存原始响应。 | [方法条目](../by-type/sql-injection.md) |
| FTP 条件 sed 与参数结构保真 | 完整正文alt和图将含ftp URL的File/FILE替换path，再grep截至参数等号，丢掉值和余下结构。 | [方法条目](../targeted-fuzzing.md) |
| Spray365 执行计划与真实认证结果 | 图仅生成24条计划、随机AD client/endpoint IDs、每次延迟10秒、总240秒，没保存登录结果。 | [方法条目](../by-type/authn-session.md) |
| 顶级域枚举与通配政策字面边界 | 正文假设*.example.*并给tld-scan仓库封面，未有当前政策和命中列表。 | [方法条目](../scope-and-rules.md) |
| NimHollow 图的创建暂停进程与 PE 入口 | 图只展示injector CreateProcess/CREATE_SUSPENDED、PROCESS_INFORMATION、PEB/TEB及MZ/e_lfanew/EntryPointRva算入口地址，没有实际注入成功。 | [方法条目](../source-audit.md) |
| phpMyAdmin root 空密码是待证历史建议 | 正文只有尝试root/blank建议，未保存版本、初始化方式或登录交换。 | [方法条目](../by-type/authn-session.md) |
| altdns 到 gobuster 的完整候选解析管线 | 完整卡生成middle-sub词表、sed去.example.com、DNS指定resolver/80线程和screen后台；这些是主动枚举动作。 | [方法条目](../discovery/passive-and-services.md) |
| wp-config.php.save 是配置备份候选 | 正文给origin IP与wp-config.php.save并称P1，无保存真实文件内容/认证结果。 | [方法条目](../by-type/info-secrets.md) |
| Velocity 权限提升与 RCE 的不同结果 | 正文主张Java Velocity SSTI可升权即使无RCE，但未保存对象访问、模板执行或最终权限交换。 | [方法条目](../by-type/ssti.md) |
| 全端口管线与五类服务命中分开验证 | 完整正文双编码Carbon内容与两图含rustscan1-65535→grep/tee/sed→httpx→nuclei2.5.4/templates8.7.1、2752模板及Nacos/heapdump/Grafana/mongo-express五标签。 | [方法条目](../discovery/records-and-incremental.md) |
| SourceLeakHacker 中断扫描与真实文件类型 | 图只有根/robots.txt200、七项404、read timeout及Ctrl C等六线程退出；没有源码文件内容。 | [方法条目](../by-type/info-secrets.md) |
| API _id 外键卡与对象关系授权 | 完整API卡建议以user_id/order_id/product_id找关联接口并复数化规则；命名规则不能保证真实数据库外键/endpoint。 | [方法条目](../by-type/idor-access-control.md) |
| metadata 路径出现在 API 请求中的证据范围 | 银行17问题题名配图是带会话的OData请求、嵌套元数据路径和200JSON，其中代码/key等内容遮挡。 | [方法条目](../by-type/ssrf.md) |
| Drive 下载卡的 shareable link 与下载权限 | 完整卡从共享链接提取fileID/filename、读取确认页并带cookie，禁证书验证且删除临时cookie文件；没有实际下载结果。 | [方法条目](../by-type/info-secrets.md) |
| Content-Disposition 文件名到响应头和 HTML | 正文称可控文件名进入Content-Disposition后CRLF修改Content-Type到text/html，无保存原始响应或受众。 | [方法条目](../by-type/xss.md) |
| 手绘核心防御图的四条边界 | 完整手绘图覆盖用户访问的认证/会话/权限；输入拒坏/允许好/净化/安全数据处理/语义/边界/多次验证规范化；错误/审计/告警/响应；管理应用。 | [方法条目](../source-audit.md) |
| API Guesser 格式识别与 token 处理 | 图是空API key/token表单，正文建议第三方JS网站猜类型；没有识别结果或有效权限。 | [方法条目](../by-type/info-secrets.md) |
| 地址栏 javascript 弹窗不证明反射 XSS | 两图地址栏是javascript:alert，登录页弹窗及cookie文本；没有保存从服务器/DOM输入到执行的请求。 | [方法条目](../by-type/xss.md) |
| Email confirmed 界面与服务端验证状态 | 标题称邮件验证绕过，图只有Email confirmed成功模态框，未有验证token/绑定或后端读回。 | [方法条目](../by-type/authn-session.md) |
| APISIX Dashboard 导出、配置写入与执行分阶段 | 正文泛称所有<2.10.1，图一是Exists Vuln脚本/登录页，另一为配置JSON中filter_func含os.execute字符串，未有实际执行结果。 | [方法条目](../by-type/cmd-injection-rce.md) |
| data wrapper 的构造与 include 消费者 | 正文alt和完整图展示base64 PHP/phpinfo以及ffuf PHP Version匹配，未保存任何结果且没有FUZZ位置。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Referer 403 到 200 需证明同一受保护对象 | 正文只有敏感站403，加自身Referer变200，未保存内容或身份。 | [方法条目](../by-type/idor-access-control.md) |
| MySQL 多语句取决于实际调用 API | 正文说MySQL通常不能batched而PHP/Python偶有可能；不能据数据库名全局判断。 | [方法条目](../by-type/sql-injection.md) |
| DOCTYPE 与返回 XML 字段的真正消费阶段 | 正文建议定义外部实体并在会返回字段引用，没保存解析器或读回。 | [方法条目](../by-type/xxe.md) |
| Kiwi 菜单、架构警告与已有控制前提 | 图是在已compromised主机Meterpreter load kiwi，提示x86载x64，列凭据/DCSync/ticket/LSA/密码/WiFi命令；仅加载菜单没有实际凭据或提权结果。 | [方法条目](../source-audit.md) |
| LFI 目录页的 wrapper 与真实包含关系 | 图定义本地文件包含并列expect/php/filter/proc/fimap/phpinfo目录，仅保存概要不是完整利用步骤。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Windows file 方案与 NTLM 外发条件 | 正文建议SSRF到file/VPS获NetNTLMv2，但没有原请求/认证协商。 | [方法条目](../by-type/ssrf.md) |
| CookieExample 与 phpinfo 的服务端回显边界 | 一图为Servlet CookieExample显示请求cookie，与clickjacking题名错配；另一图info.php显示ci_session并在Storage标HttpOnly true/Secure false。 | [方法条目](../by-type/info-secrets.md) |
| favicon 文章链接 fragment 中的 token 暴露 | 正文保存的文章URL fragment带id_token样式长值。 | [方法条目](../by-type/info-secrets.md) |
| 未知 Host 的响应变化与真正消费位置 | 两同正文帖建议先换任意未知Host，没有保存响应或后续消费者。 | [方法条目](../by-type/host-header.md) |
| Incapsula SQL 图中的 200 与延迟假设 | 题名宣称Imperva绕过，图含SQL条件/延迟样式query与200JSON，头有Cloudflare/Incapsula字样；单次工具耗时不能证明指定延迟或真假稳定关系。 | [方法条目](../by-type/sql-injection.md) |

| 密码重置令牌与路径用户的交叉绑定 | 五步图用A生成重置链接，再改路径user_id成B，声称B密码可变；公开profile仅用于定位ID，不是绕过证据。 | [方法条目](../by-type/authn-session.md) |
| diodb 历史百分比的重叠分类 | 2021末统计2306项目、158goodfaith6.9%、239authorization10.4%、380bounties16.5%、42swag1.8%。 | [方法条目](../scope-and-rules.md) |
| LFI 批量管线的关键词确认边界 | 完整gau/gf/qsreplace/xargs/curl管线以root:x打VULNERABLE，带200threads及P25；其他帖用httpx多slashdot200/root匹配和ffuf。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Frogy 的多源、解析、站点计数分层 | 图先列CHAOS/Amass/Wayback/BufferOver/证书等源各自计数，再列15唯一子域、11解析域、114活网站、21登录入口和CSV产物。 | [方法条目](../discovery/records-and-incremental.md) |
| 延迟 OOB 事件与机器人归因 | 正文报告5–10分钟后来自四AWS地址/旧Chrome的blindSSRF与XSSHunter回调，没有执行记录。 | [方法条目](../by-type/ssrf.md) |
| S3 匿名列举与签名身份的动作差异 | 正文声称普通ls失败而no-sign-request可列。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| CTF 服务指纹的证据与移植范围 | 图显示nmap实验地址22SSH/OpenSSH8.2、80Apache2.4.41及Linux线索，是一次实验的服务枚举。 | [方法条目](../discovery/passive-and-services.md) |
| 订阅注册的枚举与消息副作用 | 正文讨论subscribe-page spam/user-enumeration，没保存真实交换。 | [方法条目](../by-type/authn-session.md) |
| Osmedeus 工作区与模块级结果 | 两图保存general/quick工作区创建时间、summary/logfile及fingerprint/ipspace/portscan/probing/screenshot/spider/sto/subdomain产物入口。 | [方法条目](../discovery/records-and-incremental.md) |
| 浏览器独立 profile 与 Burp 请求生命周期 | Firefox另建profile可隔离cookie/插件/proxy/CA和角色基线；另一帖图Proxy截住POST而Repeater空白Target not specified，没有保存已知修复。 | [方法条目](../experiment-design.md) |
| 被遮挡的 WAF 变体与执行现象 | 普通script关键词被blocked，另一截图alert3且关键变体被遮挡。 | [方法条目](../by-type/xss.md) |
| APISIX 配置导出与配置执行的不同能力 | 图GET/apisix/admin/migrate/export没有可见Cookie，200JSON包含routes/plugins/upstream/脚本字符串。 | [方法条目](../by-type/idor-access-control.md) |
| RiotPot 的诱捕交互强度与真实服务 | 图将packet capture/noise filter、attack database、low-interaction模拟与host/cloud可插拔高交互容器关联，列HTTP/SSH/Telnet/MQTT/CoAP/AMQP/Modbus等。 | [方法条目](../discovery/passive-and-services.md) |
| GROUP_CONCAT 的行关系与输出限制 | 技巧图把username和password分别GROUP_CONCAT，声称更低噪声；多行数据聚合不减少读取敏感数据，也可能丢失两列行对应。 | [方法条目](../by-type/sql-injection.md) |
| 正常功能使用到可证伪的漏洞假设 | 正文提醒先脱离终端理解应用。 | [方法条目](../business-modeling.md) |
| 搜索分类、项目集合与 IP 建议的范围边界 | LeakIXcountry/highseverity查询、MoneyScope/rescope/bbscope集合和“扫IP别扫域名”都是发现/工具选择信息；共享IP、证书或wildcard候选不自动属于授权。 | [方法条目](../scope-and-rules.md) |
| Grafana plugin 遍历的实际返回内容 | 两图使用public/plugins/alertGroups多级路径，分别200textplain/passwd和grafana.db片段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 账号验证单请求与邮件用户探测的差别 | GitHub图只有account_verifications请求含launch_code，没有15k阈值/后续响应；msmailprobe图只有identify/onprem/O365 userenum帮助和线程参数。 | [方法条目](../by-type/authn-session.md) |
| hostname 能回显而 passwd 不回显的竞争解释 | 提问说JavaXXE只读hostname，没保存解析器/原始XML/权限或错误。 | [方法条目](../by-type/xxe.md) |
| subjack 输出被 grep 反向过滤 | 完整subfinder/httpx/subjack管线末尾grep-v Vulnerable会排除含Vulnerable的行；输出文件名takeover不改变实际过滤语义。 | [方法条目](../by-type/subdomain-takeover.md) |
| 分享预览 picture 参数与 ImageTragick 标题 | 截图保存分享对话picture URL参数和图片预览、文章开头历史介绍；没有完整命令/解析链。 | [方法条目](../by-type/file-upload.md) |
| RPC 业务依赖不等于无法设防 | RPCFirewall示意把RPC/SMB/TCP与DC必须开放放一边、RDP3389/WSMAN5985/6可过滤放另一边，这是拓扑概括。 | [方法条目](../scope-and-rules.md) |
| 多份 High 报告与扫描扩大建议 | ApacheSSRF三同题High列表没有原请求/不同根因；正文说内网扫端口升High/Critical不能作通用规则。 | [方法条目](../impact-and-acceptance.md) |
| git 目录列举与 EC2 接管标题 | .git索引图可见HEAD/config/index/objects/refs等名称，正文标题说AWS/EC2接管；缺恢复内容、有效权限和实际状态。 | [方法条目](../by-type/info-secrets.md) |
| PDF 中 HTML 资源加载与元数据前提 | 线程称把HTML放PDF后访问metadata；没有保存实际renderer、加载请求或认证条件。 | [方法条目](../by-type/document-rendering.md) |
| 堆快照字符串与旧新 JS 差异 | 一图Chromeheap snapshot grep/api/company65行与十个路径；另一图旧新main.js经beautify再diff，curl-ks且归档时间串异常。 | [方法条目](../discovery/client-and-cloud.md) |
| Termux 源查询、配置目录与完成状态 | 正文pkg insta拼写，图实际install findomain5.1.1随后16源查询进度；amass enum-list-config只列参数/key名称。 | [方法条目](../discovery/passive-and-services.md) |
| Osmedeus YAML 的阶段、预算与证据清理 | CLI图general/exclude/vuln/cidr/domains/wordlists/threads40/concurrency2；完整general图十模块，subdomain图required、timeout3h、subthreads50、多源并行、stderr重定向、Append/SortU、metabigor及postrun清理。 | [方法条目](../discovery/records-and-incremental.md) |
| X-Forwarded-For 与实际限速身份 | Django图有XForwardedFor127.0.0.2、200/SetCookie，另一图只画多次失败→Too many requests，alt也只有主题。 | [方法条目](../by-type/authn-session.md) |
| PHP 备份扩展与 WordPress 配置字段 | wp-config.php受限而_orig或/blog/wp-config.php.bkp可读的图片包含DB字段和认证salt/key。 | [方法条目](../by-type/info-secrets.md) |
| 词典生成与 tracking comp 的结构保留 | 完整字典管线抓URL抽token/lowercase/sort/追加，另管线tr删除标点；tracking图把comp=muse/nodeweb变目录。 | [方法条目](../discovery/web-and-api.md) |
| RMI、JMX 与 SSRF 的实际协议消费者 | 几个标题建议SSRF接JavaRMI/JMX，没有原始连接或方法结果。 | [方法条目](../by-type/ssrf.md) |
| 视频取回与重定向链的每跳验证 | 图片列HTTP客户端是否跟随、redirect gadget、原SSRF是否能正确到gadget；图api/get_video=ID→vimeo，再用redirect?url→301/302→example响应。 | [方法条目](../by-type/ssrf.md) |
| 变更后的复查与非破坏能力证明 | Arabic正文建议系统变更/改进/新增后复查；另线程提醒不能覆写生产关键文件。 | [方法条目](../experiment-design.md) |
| 可读取 token 与上传延迟图片错配 | 正文建议页面取得未绑定CSRF token；所附图却是upload fileName包含sleep15、单次15.3秒与200HTML，并未保存token跨会话动作。 | [方法条目](../by-type/csrf.md) |
| XMLRPC 入口、技能曲线与提交资格 | 两图是停止提交XMLRPC.php报告和技能成长meme，缺具体能力与实际统计；不能扩成所有XMLRPC安全/不收。 | [方法条目](../reporting.md) |
| copy 事件改写剪贴板的执行边界 | 图JS在copy事件setData把显示内容换成curl外部脚本再管道sh，并附换行，preventDefault覆盖默认复制。 | [方法条目](../discovery/client-and-cloud.md) |
| 生物认证 boolean 与服务器凭据 | 正文建议Objection把本地False改True，没有实际服务端动作。 | [方法条目](../by-type/mobile-ios.md) |
| JSON 正常出口与 HTML 错误出口 | 两图正常请求API query中SQL后附HTMLonclick标记，错误页显示SQLsyntaxerror和alert287719；正文说异常改text/html，alt为scanner截图。 | [方法条目](../by-type/xss.md) |
| JWT 可解码性与声明可信度 | 正文将JWT定义为可验证/可信compactJSON；格式可读或可解码不说明此实例经过正确验证。 | [方法条目](../by-type/jwt.md) |
| 多斜杠读取图与 NGINX 默认结论错配 | 题名称mergeSlashes NGINX RCE，但实际图200passwd、Server Jetty和ramda_repository_session；httpx图则只列200/root命中。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 按 403、404、200 分工具的失真 | 正文给大范围策略：403fuzz、404接管、200截图。 | [方法条目](../discovery/web-and-api.md) |
| 支付 tampering 的订单与权益不变量 | 保存帖建议检查gateway flows/tampering，没有订单或后端结果。 | [方法条目](../by-type/business-logic.md) |
| postMessage 出站追踪与被改写 CSP | 三图分别outgoing info记录CSRF/origin*与stack、headless模板改响应CSP为宽松unsafeinline/unsafeeval，以及入站DOMXSS/出站泄露分类。 | [方法条目](../by-type/xss.md) |
| 编码反斜杠的验证与消费次序 | 技巧图用%5c混入含白名单后缀的URL，称绕过regex。 | [方法条目](../by-type/open-redirect.md) |
| 反代分号路径到管理认证窗 | 四图Apache首页403、test路径Tomcat404、manager的Apache403、test;../manager/html出现Basic认证窗。 | [方法条目](../by-type/idor-access-control.md) |
| Unicode 显示相似与实际标识符 | Homoglyph工具可产生视觉相似文字，线程未存注册/登录比较。 | [方法条目](../by-type/authn-session.md) |
| 创建 SCRIPT 需要先有 JavaScript 消费入口 | 正文createElementSCRIPT+src+append加载外部代码，图有alertOPENBUGBOUNTY；创建元素自身需要已有JS控制/可达代码入口。 | [方法条目](../by-type/xss.md) |
| cut 固定分隔与追加去重的身份损失 | 两图用slash/colon截hostname并剥443末四字符、首四字符；另帖anew去重追加。 | [方法条目](../discovery/records-and-incremental.md) |
| 配置和私钥搜索词只是发现线索 | 四dork涉及tcpconfig/certserverkey/admin下载/WebServers.xml；未存命中内容或访问条件。 | [方法条目](../by-type/info-secrets.md) |
| RCLocals 环境清单与持久化命题 | 图RCLocals2.0列GPG key身份及installed packages/版本/时间，没有启动配置写入或执行结果。 | [方法条目](../source-audit.md) |
| geojson 的 file 读取与 HTTP SSRF 分层 | 图片geojson?url=file:///etc/passwd返回文本含metabase用户，另一帖子转发同图。 | [方法条目](../by-type/ssrf.md) |
| 移动测试比例与 Android 目录的边界 | 正文说40%项目有mobile及web3smartphone，图只是AndroidGuide目录（存储/crypto/local auth/network/platform/build/tamper）。 | [方法条目](../scope-and-rules.md) |
| SQL 语法错误与真正认证结果 | auth bypass问题所附图显示MySQL near OR1=1# and password语法错误，缺正常查询和登录后状态。 | [方法条目](../by-type/sql-injection.md) |

| fragment 训练样例与 HTTP 参数的区别 | 正文把查询串/hash加123与XSS相连，alt和图片显示训练文档页面onclick及alert。 | [方法条目](../by-type/xss.md) |
| SourceMapping 的路由状态与源码可见性 | 图列atutor8080源码路径、200/500和计数；Shuji正文只是sourcemap提取工具。 | [方法条目](../source-audit.md) |
| MovableType handler 解码、加载失败与执行阶段 | 保存图是mt.handler_to_coderef XMLRPC请求，含编码内容，响应Failed loading package中有passwd字段。 | [方法条目](../by-type/cmd-injection-rce.md) |
| URL 被写成 Python 脚本名的管线校验 | 两完整管线写python3加HTTP URL形式，另有50并发、paramspider/hakcheckurl及数字状态排除。 | [方法条目](../discovery/records-and-incremental.md) |
| 组织搜索到 ASN 的聚合与共享网络 | 完整amass组织搜索、ASN处理/逗号合并及xargs P3查询链，将组织→ASN→网络资源作为发现路径。 | [方法条目](../discovery/passive-and-services.md) |
| authorization_code 字样与可用授权码 | 正文建议在JS搜authorization_code，没有保存一次真实授权响应或可兑换材料。 | [方法条目](../by-type/oauth-oidc.md) |
| PasteMonitor 的 SES URL 命中与秘密认定 | PasteMonitor正文描述Pastebin API、词表、每日通知，图只是amazonaws SES URL命中，另一帖复用同图。 | [方法条目](../by-type/info-secrets.md) |
| devnet 宣传和 SSL 公司名的许可边界 | devnet SOL/Discord宣传、Shodan SSL公司字符串、200/login和默认密码故事均没有保存当前资产政策与受保护动作。 | [方法条目](../scope-and-rules.md) |
| 截图相似与同一代码库的验证距离 | 正文用标题/截图聚类找interesting domains，另帖正常漫游、JS与功能性分析仅保存1/2。 | [方法条目](../discovery/web-and-api.md) |
| Burp Bounty 2.3 的匹配点与规则来源 | 两图保存2.3变更：Intruder only points、raw请求修复、编码器、private collaborator及扫描菜单，另一图列七个CVE profiles。 | [方法条目](../targeted-fuzzing.md) |
| Automation 只读角色与角色管理的持久化证据 | 正文说文档角色readonly但写API可调用，图题Operator manageAutomationconfig；另一帖移除disabled后更新role并成为Admin，550邮件声称内部复现。 | [方法条目](../by-type/idor-access-control.md) |
| 安全完成率与组件易利用口号的校正 | 100%安全宣传、Jira easy及NoSQL everywhere/easy没有保存部署条件或原始比较；标题/课程完成不能证明漏洞存在或全系统无漏洞。 | [方法条目](../expert-reasoning.md) |
| anew 仅新名称循环遗漏已知资产变化 | 完整while循环每小时subfinder→anew→httpx→nuclei→notify，anew之后只送新名称。 | [方法条目](../discovery/records-and-incremental.md) |
| 客户端 JSON 改为 admin 与认证权威 | 两帖完整status0→1/user_typeadmin故事发生在错误凭据响应之后，附图只有P1 Unresolved标题。 | [方法条目](../by-type/authn-session.md) |
| GUID 删除、改密与 email 查对象的不同契约 | 三图分别是acID/Delete POST、两账户GUID改密草图和email查询UUID/手机号/历史的200 JSON。 | [方法条目](../by-type/idor-access-control.md) |
| WannaRace 页面到并发不变量的最小实验 | 靶场图显示voucher、balance、buy和reset，没有保存并发请求或双兑付结果。 | [方法条目](../by-type/business-logic.md) |
| Autorize 结果必须绑定身份和业务状态 | 正文反对手动测试并称半自动插件找两IDOR，没有保存主体/对象/动作及差异交换。 | [方法条目](../by-type/idor-access-control.md) |
| SVG animate 改 href 的交互前提 | 完整SVG animate/xlinkhref片段带实体编码javascript，另帖有十进制/十六进制与前导零变体。 | [方法条目](../by-type/xss.md) |
| APK 解密到 GitLab 权限链的逐段身份 | 两长图叙述APK→.jsc→XXTEA→JS→IP/端口→GitLab自注册/枚举/绕限/管理员→源码，续图再写Redis/管理登录/RCE，缺每段原始交换。 | [方法条目](../by-type/mobile-android.md) |
| log.txt、Yii 配置与公开字段的秘密门槛 | 正文给枚举/fuzz/login日志三步，图仅triaged PII标题；Yii图含被遮蔽的DSN/password/OAuth/CRM/payment/telegram字段；wp-json users正文说会引出猜密。 | [方法条目](../by-type/info-secrets.md) |
| 邮件缺 DMARC 标签与实际投递的区分 | SpoofThatMail图25/35标签含NoDMARC与willbespam；Espoofer图分MUA、SMTP envelope/receiver、DNS、SPF senderIP、DKIM签名和DMARC对齐，还有重放/客户端路径。 | [方法条目](../by-type/authn-session.md) |
| 扩展 contentScripts 域匹配不等于扩展 XSS | 正文认为Chrome扩展匹配的域都在scope，奖项图仅critical DOM题名。 | [方法条目](../discovery/client-and-cloud.md) |
| NGINX Plus 上游 API 的读写执行层级 | Parser图经编码路径到api2/http/upstreams/servers，显示id/server/weight/fail等字段，没有写入/认证的完整交换。 | [方法条目](../by-type/idor-access-control.md) |
| Grafana constructor 字符串的语法与上下文 | 保存snapshot/dashboard constructor表达式与alert片段引号不完整，未保存对应版本、入口解析或执行交换。 | [方法条目](../by-type/xss.md) |
| NOSCRIPT、title 与 innerHTML 的解析分层 | 正文完整h1/NOSCRIPT/p/title/外部script组合，另帖说innerHTML插script不执行但事件属性仍可能运行。 | [方法条目](../by-type/xss.md) |
| 五个标题在一报告中的根因分组 | 图一个标题列information/SSRF/git/debug/metrics，状态Unresolved accepted；另一帖强调报告给triage/QA/dev/security看且从零复现。 | [方法条目](../reporting.md) |
| server-status 的访客数据与最小标记 | 图监控工具卡片写clients及requested URLs，正文称据此找五漏洞，没有保存五个交换。 | [方法条目](../by-type/info-secrets.md) |
| WiFi 测试框架的驱动和观察接口 | 图hostap扩展经ethernet/wpaspy到解释器/testcase和monitor接口，是测试架构而非攻击结果。 | [方法条目](../experiment-design.md) |
| OpenDreambox WebAdmin 错误、字段和 uid 的证据 | 完整插件/shodan/script cmd正文和多图中有pipe输入、passwd字段及Permission denied，另一图id输出uid0，转帖复用。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 后台捕获与目录列表的语义筛选 | 正文正常漫游时Burp后台捕获、ffuf/ferox产200/403列表；FOFA 401/Basicrealm图给大量IP统计。 | [方法条目](../discovery/web-and-api.md) |
| Token Spray 工具与密钥动作的最小范围 | Token Spray/Guesser提示在两帖出现，图片只有105奖励。 | [方法条目](../by-type/info-secrets.md) |
| 没有专用 HTTP 栏位时保存原始交换 | 表单图有URL、Markdown description及附件/字符限制，没有单独HTTP请求栏目。 | [方法条目](../reporting.md) |
| message.data 到 document.write 的接收契约 | spotcode图监听message并直接document.write(data)，可见代码没有origin/source判断，但未存真实页面/策略和发送者可达性。 | [方法条目](../by-type/xss.md) |
| CTF user/root 截图与初始入口分离 | Momentum2图是uid1000athena/userflag与uid0/rootflag末端终端，正文alt明确User/Root；Insomnia CTF alt却配另一WP SQL语法错误图。 | [方法条目](../reporting.md) |
| SSRF 输入不会自行成为 shell 命令 | 保存帖把SSRF到RCE与反引号、curl取passwd/写文件表达式相连，另帖2/2说shell值未转义而前段未存。 | [方法条目](../by-type/cmd-injection-rce.md) |
| SSH key API 的 token 与二次因子保护 | 图是Get SSH keys API AuthorizationToken/API_KEY文档，正文说没有OTP/2FA，并未保存一次未授权交换。 | [方法条目](../by-type/authn-session.md) |
| AD CVE 号不一致时停止补全链 | 正文写42287但外链写42278，只有资源标题，没有版本、前提、交换及权限结果。 | [方法条目](../expert-reasoning.md) |
| Scemu 仿真和既有 CLR 模块的执行边界 | Scemu图是x86 call EAX到MessageBoxA的仿真输出；InjectAssembly图已有CobaltStrike session、FindModule/clr.dll及PID。 | [方法条目](../source-audit.md) |
| HTTP_HOST Notice 的文件路径披露范围 | PHP图三个文件/行号的UndefinedIndexHTTPHOST Notice和PageNotFound，重复帖复用同图，没有源码文件全文。 | [方法条目](../by-type/info-secrets.md) |
| 编码 SVG 与 selfcomment 的实例级复现 | 正文有CF/WordFence7.5.7二次编码SVG/fragment，另组两帖同完整selfcomment/domainalert字符串但图片不同：blocked与alert。 | [方法条目](../by-type/waf-bypass.md) |
| 公开订单号与订单详情授权 | 完整正文说Twitter公开订单号可追踪并看到姓名/地址/商品，但缺原始响应和访问合同。 | [方法条目](../by-type/idor-access-control.md) |
| Osmedeus CIDR YAML 的依赖、预算和完成收据 | 保存完整四模块portscan→screen→vuln→dirb YAML，portscan参数含65535ports/rate20000/tthreads3/nmthreads30/scr5及HTTP timeout；CLI图仅启动。 | [方法条目](../discovery/records-and-incremental.md) |
| username 进入 img alt 的属性逃逸边界 | 图保存username引号/onload进入img alt的代码/呈现，正文称stored XSS，重复帖子复用。 | [方法条目](../by-type/xss.md) |
| Python 绝对 filename 与完整路径点号筛选 | 代码os.path.join(BASE_DIR,uploads,filename)后对整个file_path.find('.')判断，再openread返回image/png；绝对组件可能丢弃先前基址，筛点却可能因BASE_DIR自身有点而拒绝一切。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Content-Type 接受与服务器解释器消费 | 正文说双扩展没成功、改ContentType为image/jpeg后执行，但没有保存接受、落盘位置和解释器调用的交换。 | [方法条目](../by-type/file-upload.md) |
| 数值地址、userinfo 与 unspecified 的解析差异 | 两完整列表有127.1、整数/hex/octal、白名单userinfo、IPv6及0.0.0.0/0/[::]，某些写法无括号或不是loopback。 | [方法条目](../by-type/ssrf.md) |
| Kerberos 缓存和 Windows token 的已有身份 | 票据图list/export TGT/LDAP及两kirbi旧时间，TokenUniverse图FullAccess句柄、Primary/Medium/Limited且accesscontrol项未启用。 | [方法条目](../by-type/authn-session.md) |
| 客户端 localhost 字串到服务器网络消费者 | 图SearchSources中搜localhost/127/internal/local等，正文“discover”，没有实际服务器请求。 | [方法条目](../by-type/ssrf.md) |
| LeakIX 历史严重性与新闻变化的范围确认 | 图closedcritical Log4j/Jira/PaloAlto，正文Google Alerts推荐盯项目新闻；另一帖diodb2307按不同字段给比例。 | [方法条目](../scope-and-rules.md) |
| 枚举器相串与 wayback 参数裁切的覆盖损失 | 完整subfinder｜assetfinder｜httpx不保证两源并集；wayback/gf/sed'=.*'裁切再sort/tee/dalfox会丢后续参数和值。 | [方法条目](../discovery/records-and-incremental.md) |
| OUTFILE 写入、文件范围与 Web 执行 | 完整OUTFILE示例带畸形PHP标签/curlyquotes，正文未存数据库权限、保存成功及web消费者。 | [方法条目](../by-type/sql-injection.md) |
| 混杂 file 与 manlist 片段不能拼成同一利用链 | 图把geojson file://读取及cgi-bin/manlist section<h1/script片段并列，正文说完美工作；缺统一实例/请求/权限对应。 | [方法条目](../expert-reasoning.md) |
| iptables DROP 截图与连接时序的因果界定 | 终端图已有SSH到vm2/student后出现INPUT/OUTPUT DROP文字，却未保存hook、接口、状态或命令返回后的流量序列。 | [方法条目](../source-audit.md) |
| PHP PATHINFO_EXTENSION 与带点拒绝列表 | 附件代码denylist含.php等，pathinfo(PATHINFO_EXTENSION)结果不含前导点，字符串比较错位；另有orig..筛选后public上传move。 | [方法条目](../by-type/file-upload.md) |
| mt_rand 无扩展存储与覆盖、访问契约 | 另一附件代码拒orig含..，用mt_rand构造无扩展public目标并move。 | [方法条目](../by-type/file-upload.md) |
| APISIX 固定端口标签与不同 IP 的拼链 | 正文Shodan后固定9000，批量图又有9001/default/no/vul标签；一图lsbrelease输出CentOS后SSH是另一IP且先失败。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 只阻断 Collaborator 域名的修复反例 | meme对比修代码和阻断collab域；阻断观测通道可能只消除回调，没有改变输入到网络/代码消费者的真实边界。 | [方法条目](../expert-reasoning.md) |
| VPN 或代理不会给出测试身份保证 | 正文称总应VPN/proxy避免IDS/admin，没有保存网络/识别比较，也没有因此获得权限。 | [方法条目](../scope-and-rules.md) |
| Maven Path.resolve 后再 URI.resolve 的两类语义 | 完整Java图groupId替点成路径、artifact/version/jar名经Paths.resolve/normalize后toString，再BASE_URI.resolve供OkHttp使用；另一正文说absoluteURI会取参数。 | [方法条目](../source-audit.md) |
| Driftwood 本地解锁与远端身份授权 | 图加密privatekey的passphrase破解和GitHubUsername JSON，正文只有工具推广，缺当前远端认证及权限交换。 | [方法条目](../by-type/info-secrets.md) |
| tld_scanner 参数与工具菜单的分类作用 | 正文完整tld_scanner参数且明确自行核belongsorg；DorkHelper/Investigator全菜单包括配置/DB/日志/登录/备份/源码、员工、历史、S3及多搜索源，卡片没有探测结果。 | [方法条目](../discovery/passive-and-services.md) |
| sort-u 合枚举源后保留来源和失败 | 完整正文与文字图sort-u合Amass/Sublist3r，只显示唯一集合。 | [方法条目](../discovery/records-and-incremental.md) |
| API、config 和内部路径词表的候选边界 | 两帖子同完整词表含api/access/token/json/admin/aws.js/config/v1至多版本、dashboard/oauth/url/uri/auth/internal/dev。 | [方法条目](../discovery/web-and-api.md) |
| proc 与 K8s 路径表的命名空间和读权限 | 完整路径表有proc/cwd/index.php/main.py/motd/net/UDP/ARP/self/environ及k8s serviceaccount。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Tomcat 404 版本不能证明 PUT 写入和执行 | CVE2017-12617求助只配Tomcat8.5.23和/_ui/responsive/common/js/404 banner，没有PUT/落盘/执行交换。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 厂商内部复现与修复中的不同报告状态 | PreATO邮件声称内部verified并workingfix，角色更新奖励也声称可内部复现；AppleHoF只写serverconfigurationissue addressed，无对应技术交换。 | [方法条目](../reporting.md) |

| polyglot 的外观、格式和消费者判断 | 正文把polyglot定义为看似A而实际也符合B的文件，视频正文未保存。 | [方法条目](../by-type/file-upload.md) |
| Collaborator 多面板 DNS 事件的关联键 | 自建Collaborator帖子图是五个客户端面板的DNS查询/payload/时间，没有HTTP正文或真实触发主体。 | [方法条目](../by-type/ssrf.md) |
| 常见端口表与实际服务识别的距离 | 图给FTP20/21、SSH22、Telnet23、SMTP25、DNS53、HTTP80、POP3 110和HTTPS443，只是常见服务关联，不包含某个目标的探测。 | [方法条目](../discovery/passive-and-services.md) |
| LFI 重复 dot、双编码和分隔符的消费者 | 完整图给重复dot、双URL编码、%00与%5C变体，并自注sometimes且不知原因，没有保存实际读取交换。 | [方法条目](../by-type/lfi-path-traversal.md) |
| OAuth 注册分支移除当前密码后的改密保护 | 完整正文说普通改密要求当前密码，OAuth注册后同动作不用当前密码并声称CSRF，没有保存跨站请求和持久化结果。 | [方法条目](../by-type/csrf.md) |
| 权限清单必须拆成主体、对象和动作 | 图片清单并列path traversal、authorization schema、vertical/horizontal、missingauth与IDOR；另外只有低权限附件accepted标题。 | [方法条目](../by-type/idor-access-control.md) |
| Burp 参数筛选会隐藏非参数对象入口 | 资源帖实际图框出HTTP history的Show only parameterized requests，框内未勾；正文链接未保存。 | [方法条目](../discovery/records-and-incremental.md) |
| Wireshark 描述与 Tenable 菜单不对应 | 两正文介绍流量关联TI/资产/漏洞插件，唯一新图片却是Tenable Vulnerability Detail/List/Summary菜单，缺插件实现和原始流量。 | [方法条目](../expert-reasoning.md) |
| Shopify HTML 编辑器未保存状态的执行边界 | 正文称admin/product XSS resolved/high/1000，图为Unsaved changes编辑器中的img事件属性，没有显示保存成功、DOM执行或另一主体读者。 | [方法条目](../by-type/xss.md) |
| proc、home 用户路径与挂载的读权限 | 完整清单有cmdline/mounts/sched_debug/motd/mysql配置、home用户history/SSHkey，另一帖列cwd源码、net视图/environ及K8s serviceaccount。 | [方法条目](../by-type/lfi-path-traversal.md) |
| self 注释、iframe 训练和 top 属性解码 | 正文保存self/bracket/comment编码、iframe+/ON/onload及top属性hexescape对照；图WAF Tester明确globalHTML/attribute、单context限制，另一图只有alert。 | [方法条目](../by-type/waf-bypass.md) |
| extensive 与 quick CIDR 工作流的覆盖差异 | 完整YAML图extensive/general/domain有subdomain→probing→screenshot→sto/fingerprint→spider/archive/ipspace→vulnscan，并extensive分支portscan/dirbscan/pvulnscan；quick CIDR/cidrfile/forceparams固定HTTP端口子集，只portscan/screenshot/vulnscan/dirb。 | [方法条目](../discovery/records-and-incremental.md) |
| Pwndora 扫描范围、超时和端口子集 | CLI图start/end IPv4、range文件、threads默认50、socket timeout0.5、top20与all1000、HTTP screenshot及Wappalyzer更新，没有运行结果。 | [方法条目](../targeted-fuzzing.md) |
| Postman 搜索、contact JS 与 Algolia 标识 | 图建议公共Postman按scope域搜索，但所示只是example/RAML/demo；正文另说contact JS可能SMTP秘密和AlgoliaAPPID/APIKEY，未存实际材料权限。 | [方法条目](../by-type/info-secrets.md) |
| 六项 OTP 清单中的客户端和服务端边界 | 正文两列表把响应/状态改写、码泄露、JS分析、复用与限速同称bypass；图仅401 InvalidOTP/successfalse。 | [方法条目](../by-type/authn-session.md) |
| DoD header 接收口号与默认密码速查 | 两帖说DoD只接受server在header，repo图只有简介；默认凭据repo和大公司允许bruteforce/P2高奖泛称也无当前政策。 | [方法条目](../scope-and-rules.md) |
| Grafana 原始 request-target 含井号的层级差异 | 保存Raw HTTP/2图的plugins/welcome路径确含literal #及dot段，响应200有passwd字段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| XSS、任意写和 Laravel 标签到 RCE 的缺口 | XSS→RCE图只indexphpalert1，Meta预告明确任意写转RCE是应用特定，LaravelIgnition图仅low报告列表和maybeRCE。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 二阶 SQL 的空白页面与错误差异 | 正文仅线程1说应用二阶blindSQL页面始终空白，只有查询错误时不同，未保存发行/存储/二次查询交换。 | [方法条目](../by-type/sql-injection.md) |
| Symfony Profiler 的路径、变量与配置文件 | 正文说debug/profiler enabled，实际图参数路径下ExceptionController/200/headers及phpinfo服务器变量，数值多遮蔽。 | [方法条目](../by-type/info-secrets.md) |
| 平台注册清单和 HoF 的历史契约 | 平台图按公开注册/邀请列网站，是历史分类；FlexLists HoF图明确无bounty并列排除项，NoRateLimit标题没有因子/动作证据。 | [方法条目](../scope-and-rules.md) |
| S3 链接、unclaimed 标题与资源接管 | 正文只建议检查所有S3链接，200奖励邮件题名unclaimed bucket on login页，没有实际引用、归属、注册可能/控制后的消费证据。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| git 与 svn 清单中的元数据和源码区别 | 完整词表包含HEAD/index/logs、attributes/config/keep/modules/review及svn entries/ignore，另一帖仅git/svn/env，报告1/2还要求客户/用户影响。 | [方法条目](../source-audit.md) |
| Second-Order depth 与 ripgen 生成候选 | help图SecondOrder depth1/threads10/repeat headers/insecure/output/target，ripgen卡片domainpermutation，Freshdesk只有signupform。 | [方法条目](../by-type/subdomain-takeover.md) |
| curl 转换 PoC 时保持交换语义 | 图片curlPOST XMLRPC/ContentType/data转Python requests.post，另有logo；转换界面没有执行/响应结果。 | [方法条目](../reporting.md) |
| Whatfiles 和 FACT 的观察权限与采集收据 | Whatfileshelp新命令或attachPID须root、log/stdout/debug；FACTUI targets/UUID/disks/partition/mount/collectedtime及capture/ingest按钮。 | [方法条目](../source-audit.md) |
| email UserProfile 与随机 username 回退的比较 | 完整正文称枚举email再读取profile，图GETUserProfiles带Authorization并返回多字段；另一帖username null→xyz得到随机profile，缓存只是作者疑问。 | [方法条目](../by-type/idor-access-control.md) |
| ffuf 必用与详细解释的验证关系 | 正文alwaysffuf及理解core/不用花哨one-liner建议，只是方法取向，无实际端点/结果。 | [方法条目](../expert-reasoning.md) |
| Twitter 和 BlackHat 资料检索的可信度 | 图保存list/min_faves/filterlinks/SSRF/Latest查询样式，正文BlackHat site/intext/topic/filetypepdf；YouTube概览声称快速critical，没有实际漏洞链。 | [方法条目](../discovery/passive-and-services.md) |
| Http2Smugl help 到协议转换边界的距离 | 图help仅detect/request/completion/connect-to/timeout10s，正文说H2→H1转换可导致smuggling，另一帖只是相同工具链接。 | [方法条目](../discovery/web-and-api.md) |
| GET map 控制 array_map 的 callable | 完整PHP图input来自GET map，再array_map(input,[0,23,454,234])。 | [方法条目](../source-audit.md) |
| 任意收件人 OTP 数量与身份完成分层 | 完整正文求给任意email含未注册者无限发OTP定级，另一帖NoRateLimit HoF和大公司bruteforce口号都缺实际验证。 | [方法条目](../by-type/authn-session.md) |
| 弱候选保留状态不预先证明连链 | 正文建议记录selfXSS等暂时不能利用的候选，以便后来寻找连接。 | [方法条目](../discovery/records-and-incremental.md) |
| api file 的 path 与 type 提示不是读取证明 | 正文链接显示api/file?path=config/products/crystals/ruby.jpg&type=image/jpg并问问题，未保存请求/响应或loader实现。 | [方法条目](../by-type/lfi-path-traversal.md) |
| POST XSS 加 CSRF 不自动成为 stored | 完整正文写POSTXSS=P5、加CSRF=storedP3，图只是triaged/stillassessed标题。 | [方法条目](../by-type/xss.md) |
| PTY、TERM 和 stty 改变交互而非权限 | 完整正文给pty.spawn、TERM、挂起/stty raw/fg序列，未保存环境/控制流或执行结果。 | [方法条目](../source-audit.md) |
| SQL 百分之百口号与完整 alt 的类型变体 | 正文及有意义alt保留引号/反引号/反斜线/注释、q[]/q=[1]、OR、括号、函数样式等变体，图仅SQL封面。 | [方法条目](../by-type/sql-injection.md) |
| subjs 双 tee、uniq 与跨域资源证据 | 完整管线subjs后两次tee写同一js_url、uniq及stderr重定向，图实际列分析/营销/CDN资源和带query版本JS；另一帖bash后写HTTP脚本名，实际JSFScan图是本地启动和19/19links/LinkFinder队列。 | [方法条目](../discovery/records-and-incremental.md) |
| AWS 数据库标题与 SSH 日志图的字段归因 | 帖子标题千开放AWS数据库/RCE/K8s，图却Kibana sshd invaliduser/kex/closed日志，process.cmd部分accepted不等认证成功。 | [方法条目](../by-type/info-secrets.md) |
| file hosts 地址与 PHP DB 定义的对应缺口 | 图片地址栏写file:///etc/hosts但页面展示PHPheader/DBdefine/include，值全部遮蔽，正文只有不披露感叹。 | [方法条目](../by-type/info-secrets.md) |
| WebSocket 握手和消息生命周期的覆盖 | 正文指出WebSockets与HTTP不同、工具支持较少和规模发现困难，外部talk后续未存。 | [方法条目](../discovery/web-and-api.md) |
| vCenter header 端口对照的连接消费者 | 两图同GET vropspluginui getvcdetails且带session/多个headers，vcIP一图127.0.0.1:22返回500/UnrecognizedSSLplaintext，另一127.0.0.1:2返回Connectionrefused。 | [方法条目](../by-type/ssrf.md) |
| 复杂功能先拆合同而非按复杂度判漏洞 | 正文建议复杂站先用access/logic/auth强项建立信心，另一条直接complex=lesssecure。 | [方法条目](../hunting-strategy.md) |
| IDOR 入口比例不能当当前漏洞概率 | 正文列REST/query/body/GraphQL/PUT/header/cookie/querylanguage，图REST31.8%、GET25.8%、POST21.2%、GraphQL9.1%等，没有样本分母，类别也可能重叠。 | [方法条目](../by-type/idor-access-control.md) |
| Abuse Risk 分流和奖励资格分开记录 | Googlebot通知identifiedAbuseRisk/triagedTrustSafety，并说稍后回应；它描述处理队列，不提供漏洞机制、最终受理或奖金承诺。 | [方法条目](../reporting.md) |
| Burp 仍开启与页面等待的诊断顺序 | meme把页面不加载归因BurpProxy仍开，没有实际网络日志。 | [方法条目](../experiment-design.md) |
| 长密码报告的不同项目与资源成本证据 | 保存两完整图分别Imgur resolved/medium/250与Asana同类标题N/A；前者文字声称72/48常见限制但没有哈希成本/服务指标，目标/环境/政策不同。 | [方法条目](../impact-and-acceptance.md) |
| SSRF 图的可读、盲连接和协议前提 | 完整图分environment、canreadresponses、URL/header/webhook/PDF/document入口、ftp/dict/gopher/file/ldap、跳转/数值地址及internalservices/metadata。 | [方法条目](../by-type/ssrf.md) |
| Gh-Dork valid cache 和覆盖输出的完整性 | CLI图wordlist、users/org/repo、validitems缓存和outputdir会覆盖内容；正文另一帖仅工具链接，未存一次搜索结果。 | [方法条目](../discovery/records-and-incremental.md) |
| html 路径到标题投影的后端消费者 | 完整正文path后缀.html含UNION投影，四图title显示DBuser/db/version、再列schema字段与账号hash。 | [方法条目](../by-type/sql-injection.md) |
| Osmedeus chunk 首块不是全部完成 | 两个原图chunk-parts20：域名单10139行首块509、CIDR116行首块7，skip-subdomain后probing/65kportscan启动，没有全部块收据。 | [方法条目](../discovery/records-and-incremental.md) |
| Google Sites ListScripts 的标识和能力层级 | 图POST某site的gateway/ListScripts而Referer是另一site，带cookie/token，响应privateScript name/id/service/function；正文7500IDOR/RCE标签没有下一能力交换。 | [方法条目](../by-type/idor-access-control.md) |
| Combobulator 公共同名包与依赖解析 | 图四Maven包publicprovider、包龄/versions4of4计数，未保存真正应用resolve、下载或运行；重复帖尾部whitecheckmark不是结果。 | [方法条目](../source-audit.md) |
| SSL 发现到负载均衡后台的身份和等级 | 完整五步SSLTarget→EC2 internal login→Okta/auth→默认账号→LBdashboard，图只是厂商valid/4.6medium/500邮件；缺原始登录/角色/后台动作。 | [方法条目](../scope-and-rules.md) |
| Mininode 粗细依赖图与动态消费者 | 架构图Parser→Valuebinding→Loaddependencybuilder/Callgraphbuilder→Reducer输出reducedapplication，蓝/红粗细两种路径，无具体裁剪结果。 | [方法条目](../source-audit.md) |
| opaque after 参数与 Java RCE 标签的缺口 | JavaRCE帖子图片只有GET api/v1/list size25/after不透明值、placeholder cookie和常规headers，没有响应、解码格式或执行消费者。 | [方法条目](../source-audit.md) |
| PDF iframe 的 file 与 HTTP 网络消费者 | 完整tips图HTML注入到PDFgenerator iframe/cloudmetadata，正文另给filepasswd。 | [方法条目](../by-type/document-rendering.md) |
| 公共表单回调到 SSTI 还需模板消费者 | 完整正文及alt建议公共form收到request后trySSTI，未保存模板表达式/计算结果和真正出站发起者。 | [方法条目](../by-type/ssrf.md) |
| sudo 跑未读代码的假设不能当工具方法 | meme声称50行太长直接sudo，另一帖给畸形HTTP脚本名。 | [方法条目](../source-audit.md) |
| JS 后缀、状态和 MIME 三重筛选的漏项 | 完整gau→grep.js$→httpx200/contenttype→grepapplicationjavascript图列workerjs，查询版本/noext/错MIME可能漏，软200或第三方资源也可能进列表。 | [方法条目](../discovery/records-and-incremental.md) |
| Amass CIDR 到 nuclei 管线的 stdin 和地址键 | 完整链Amass loopback/21→subfinder文件输出→rustscan filearg/全端口→grepOpen/sed→httpx→nuclei。 | [方法条目](../discovery/records-and-incremental.md) |

| CRLF 到 HTML 响应消费的两个边界 | 正文给编码CRLF、响应头及HTML脚本片段，图只给ReflectedXSS accepted邮件。 | [方法条目](../by-type/xss.md) |
| 后缀与内容类型筛选只产生文件候选 | 完整httpx链用历史URL、末尾.js、200和application/javascript筛选；另帖targetfile/JSON示例混用cat域名和逻辑or文字，没有完整有效脚本。 | [方法条目](../discovery/records-and-incremental.md) |
| 邮箱大小写映射与重置接收者的不同合同 | 保存的是2/2，声称邮箱大小写变化可把reset token发给另一邮箱；第二示例混入http URL，不能擅自修成一条有效地址。 | [方法条目](../by-type/authn-session.md) |
| 一份 fuzz 字典不能覆盖所有消费者 | 正文说一个字典够用，图仅fuzzDicts仓库卡片和stars，没有字典正文。 | [方法条目](../targeted-fuzzing.md) |
| AuthCov 爬行身份与 Authz0 多角色模板 | 正文保存AuthCov以预定义登录用户进行headless爬行；Authz0以YAML管理URL/roles并复用ZAP/Burp历史、多headers/cookies。 | [方法条目](../by-type/idor-access-control.md) |
| Kerbrute 帮助页的账户与票据副作用 | 完整帮助图列USER/users、PASSWORD/passwords、domain/DC IP、threads默认1、结果文件和no-save-ticket；后者说明正确凭据可能保存TGT。 | [方法条目](../by-type/authn-session.md) |
| message listener 正则命中与 DOM sink | 正文多次用getJS/httpx正则找addEventListener message；配图是奖励列表或仓库封面，没有真正handler。 | [方法条目](../by-type/xss.md) |
| X-Forwarded-Host 标签缺少反射消费者 | 保存正文仅称XSS via X-Forwarded-Host，图为通用攻击流程，没有原始头/响应。 | [方法条目](../by-type/host-header.md) |
| RocketMQ 控制台读字段与管理动作 | 完整控制台图有DefaultCluster、三个broker、内部地址/10911、V4_3_1、消息TPS/计数及STATUS/CONFIG按钮；Shodan题目建议查console和日志，但图未显示日志正文或配置操作。 | [方法条目](../discovery/passive-and-services.md) |
| 缓存报告列表不能补出 CDN 缓存链 | 图列cache poisoning/deception、Referer storedXSS、token disclosure等报告标题，正文只有三篇外链和总奖金。 | [方法条目](../expert-reasoning.md) |
| Segment writekey 与 API key 的能力证据 | 正文询问JS内Segment writekey/apikey是否可利用；另帖附件仅HardcodedPrivateAPIKEYToken奖励题目，没有材料/服务权限。 | [方法条目](../by-type/info-secrets.md) |
| href 中 javascript scheme 仍需真正导航 | 正文给href用户输入及javascript scheme，并称open redirect→RXSS，模糊图只见hacked对话框。 | [方法条目](../by-type/xss.md) |
| 跨请求复用 RegExp 的 lastIndex 状态 | 保存2/2称连续两次test能跳过引号。 | [方法条目](../source-audit.md) |
| graphql-path-enum 资源名与 resolver 授权 | 正文推荐path枚举工具并称上周有帮助，未存查询、schema或结果。 | [方法条目](../by-type/graphql.md) |
| 历史 URL 的百分号空格不是 XSS 证明 | 正文建议wayback列表搜索%20，两个post正文相同。 | [方法条目](../discovery/web-and-api.md) |
| 密集端口列表与服务作用的区分 | 图是多个部分遮盖IP重复2052/2053/2082/2083/2086/2087/2095/2096及HTTP端口。 | [方法条目](../discovery/passive-and-services.md) |
| SuiteCRM Notes 日志与执行身份 | 终端图声称已登录、Notes植入payload并经localhost/public地址读取passwd样式输出。 | [方法条目](../by-type/cmd-injection-rce.md) |
| gf redirect 输出和重定向证明分开 | 完整管线是waybackurls→httpx超时/线程→gf redirect→anew；图实际列多条redirect=no，输出文件却叫vulns。 | [方法条目](../by-type/open-redirect.md) |
| 开放重定向到 SSRF 的服务端客户端条件 | 保存正文分别说重定向可能绕IP限制/导致SSRF，外链全文未存。 | [方法条目](../by-type/ssrf.md) |
| 响应改值、状态码与服务器认证状态 | 保存线程最后一条列response/status manipulation、parameter pollution、token forging，缺前文和真实交换。 | [方法条目](../by-type/authn-session.md) |
| AIza 前缀提取不是完整 Google key | 完整正文httpx extract-regex仅匹配AIza前缀，然后给scanner外链，没有完整key或权限响应。 | [方法条目](../by-type/info-secrets.md) |
| Crimson 五十工具与覆盖收据 | 图把URL/IP/screens、WHOIS/CORS/zonetransfer、portscan、fuzz、JS、SSL、smuggling、SSRF等分三圈；正文说50+工具。 | [方法条目](../discovery/records-and-incremental.md) |
| IP source bypass 的 200 和长度差异 | 图多个自定义IP/Forwarded类头都返回200，长度1345/1967/2316/2345不一，且包括与源IP语义无关的AccessControlAllowOrigin，没有原始基线和正文。 | [方法条目](../by-type/host-header.md) |
| Jira 路径清单按消费者分别审查 | 完整列表含QueryComponent、ViewUserHover、dashboard REST、user picker与编码iframe路径；没有响应或版本实例。 | [方法条目](../discovery/web-and-api.md) |
| 隐藏参数、搜索和内部 AJAX 的权限合同 | 正文建议Arjun/搜索、从响应找隐藏参数、internalAJAX访问他用户；图仅privatehiddenaccount/posts和profilepicture的报告标题。 | [方法条目](../by-type/idor-access-control.md) |
| Duplicate 与无法共享原报告的记录 | 正文说很多XSS/IDOR duplicates，图解释previouslysubmitted且原报告含不宜共享信息。 | [方法条目](../reporting.md) |
| DIVA 改进计划与 InsecureShop 训练入口 | 正文一条只是DIVA refinement计划，另一条介绍Kotlin InsecureShop的19+练习，未存实现或完成记录。 | [方法条目](../by-type/mobile-android.md) |
| Flask API 靶场与 Android 取证资源的边界 | Fernbach描述以Flask练API OWASP top10，图只是仓库卡片；同帖Androiddiagnostics是独立外链。 | [方法条目](../experiment-design.md) |
| 教师用户名前缀触发权限问题的最小对照 | 附件邮件明确studentusername须以teacherusername开头并加字符；abc/abcX可触发，abc/def不行，修复已部署并请求确认。 | [方法条目](../by-type/idor-access-control.md) |
| og:image 到 SVG 缩略图的二次渲染 | 正文连续两条说抓取链接metadata并将evilSVG作为缩略图；图保存og:image示例、卡片、遮挡对话框和StoredXSS viaSVGmetadata奖励通知。 | [方法条目](../by-type/xss.md) |
| Log4j 与 ServiceDesk CVE 资源不是部署证明 | 完整正文给两个历史CVE/仓库并笼统列版本范围，没有实际部署、配置或消费者。 | [方法条目](../expert-reasoning.md) |
| Pre ATO 的 informative 状态仍缺身份转换 | 正文仅PreATO closedinformative，未存注册/邮箱验证、身份合并或会话转换。 | [方法条目](../impact-and-acceptance.md) |
| 重置链接污染到 token 泄露需投递证据 | 完整笔记建议Host/XForwardedHost/Referer，称nextrequest出现attackerdomain就偷到token。 | [方法条目](../by-type/host-header.md) |
| Bad Request 页面与 N A 争议分开 | 正文称报告N/A并询问公开；图片只有浏览器BadRequest/malformed请求，没有安全交换或技术机制。 | [方法条目](../reporting.md) |
| invoice fetch item 的 JSON 与重置链缺口 | 保存invoice/weakreset→ATO标题，图只有POST dashboard/invoices/fetch-item对象id及200JSON的billing/shipping/user/paid字段，敏感值已遮。 | [方法条目](../by-type/idor-access-control.md) |
| Heaptrace 的 double free 演示与攻击可达性 | 完整图C代码malloc后两次free，trace有第二次free警告、doublefree detected和异常退出status6，统计malloc1/free2；这是局部演示。 | [方法条目](../source-audit.md) |
| 请求走私图的 framing 与连接复用证据 | 图画前后端同带ContentLength50/TransferEncodingchunked，后端另GETadmin与200/302，没有原始字节、完整chunk终止、配置或连接。 | [方法条目](../by-type/ssrf.md) |
| 自动化发现范围与测试范围分开保存 | 正文指出自动枚举会产生outofscope域，并肯定工具能力；资产发现不自动带测试许可。 | [方法条目](../scope-and-rules.md) |
| DNS 先校验后再次解析的连接一致性 | 正文及完整.NET图先Dns.GetHostEntry检查唯一allowlistedIP，sleep1000后WebRequest(url)获取响应。 | [方法条目](../by-type/ssrf.md) |
| 广度工具与深度合同研究的收据 | 正文建议一边优化工具一边选目标深挖，另帖强调漏洞而非工具。 | [方法条目](../hunting-strategy.md) |
| WMI registry 输出不证明初始授权或 AV 绕过 | 两图显示命令完成、COMConsumer/EventFilter/Binding清理OK、权限列表及remove registrykey；正文称无需SMB/可绕AV。 | [方法条目](../expert-reasoning.md) |
| Shodan awk 第三字段与 nuclei 指纹等级 | 完整管线Shodan domain→awk第三列→httpx→nuclei，图包含missingXFrameOptions、Akamai/Cloudflare、S3detect、Pulsepanel、robotstxt等标签及共享CDN。 | [方法条目](../discovery/records-and-incremental.md) |
| site 通配和品牌句子的归属候选 | 正文给site:target.*及品牌完整句搜关联域，未存当下归属/许可。 | [方法条目](../discovery/passive-and-services.md) |
| 归档扩展名 grep 不能认当前敏感文件 | 完整管线wayback保存全集后grep.xls/xlsx/json/pdf/sql/doc/docx/pptx，正则未锚定实际path边界，可能匹配query/子串。 | [方法条目](../by-type/info-secrets.md) |
| UUID 可得性与对象授权分开证明 | 完整tips图列users/all、user/list、users作为可能取得UUID的候选；另一图是1234→1235示意，正文称IDOR难找易利用。 | [方法条目](../by-type/idor-access-control.md) |
| CSV 上传到执行仍需读取应用链 | 正文说CSVtext upload→RCE并链到恶意软件新闻，保存材料未给上传端、表格解析、外部跳转或执行程序。 | [方法条目](../by-type/file-upload.md) |
| SIP honeypot 时间窗计数不等当前恶意主体 | 图SentryPeer SourceIPs一小时窗口、多个IP及一个高计数，另有UA/method/country/number菜单；正文宣称分布式badactors。 | [方法条目](../discovery/passive-and-services.md) |
| IDAPython 字节解释与脚本执行权限 | 图左侧idabytes/heads及XOR字符串代码，右侧IDA数据视图，正文介绍IDA/VSCode执行调试集成；未存连接实现/完整反编译结果。 | [方法条目](../source-audit.md) |
| SQL concat 到 prompt 的二次语法消费 | 完整正文concat十六进制HTML/JS与user/database，图URL含UNIONALLSELECT且prompt显示DB字段/cookie，缺原请求基线。 | [方法条目](../by-type/sql-injection.md) |
| 报告影响需与实际能力证据相连 | 正文强调reportimpact而不只名称，文章全文未保存。 | [方法条目](../reporting.md) |
| telnet SMTP 会话不能替 SSRF 起始消费者 | 完整图是telnet本地0/25、Sendmailbanner、HELO/MAIL/RCPT/DATA及acceptedfordelivery；未存通过漏洞的入口、协议转发和真实接收证据。 | [方法条目](../by-type/ssrf.md) |
| Autorize 长度标签需要原始授权对照 | 图有Orig/Modif/Unauth长度、Bypassed/Enforced/Isenforced问号，一些原长0；没有会话主体和响应正文。 | [方法条目](../by-type/idor-access-control.md) |
| 多源 JS 管线的覆盖、覆盖写和清理风险 | 两完整图聚合gau、wayback、gospider，grep.js排jsp/json、sort/uro/anew、anti-burl awk第四列，再LinkFinder/collector/rushSecretFinder；包含错误隐藏、动态bash、通配rm及追加输出。 | [方法条目](../discovery/records-and-incremental.md) |
| Reverse WHOIS 被误称 reverse DNS 的证据 | 正文说reverseDNS但实际viewdns链接是reverseWHOIS按邮箱；图2cmdSOA输出域名/共享AppleNS或空值。 | [方法条目](../discovery/passive-and-services.md) |
| Instagram 地理标记的历史时间与可见性 | 图地图弹窗有picturelink、地点、2016timestamp和经纬度；正文说汇总所有geotag输出JSON，没有权限交换。 | [方法条目](../discovery/client-and-cloud.md) |
| document domain 标记与接管证据层级 | 正文建议document.domain比alert1体现执行域，再升级ATO。 | [方法条目](../by-type/xss.md) |
| 二十位成员 ID 与移除组织 owner 的动作 | 完整正文改20位alphanumeric成员id可删owner，图P2/1250/Unresolved标题，无前后成员状态。 | [方法条目](../by-type/idor-access-control.md) |
| AutoRepeater 不能替回调主体与请求合同 | 正文只有用AutoRepeater找SSRF，没有替换规则或响应。 | [方法条目](../by-type/ssrf.md) |
| OTX 第一页 URL list 的分页和材料等级 | 完整图limit100/page1→jq URL字段，返回example.com样例PDF/admin/login/跟踪query和奇怪信息字段。 | [方法条目](../discovery/records-and-incremental.md) |
| noshell 登录限制与 glob 展开的不同层 | 正文声称已有commandinjection、账户noshell/WAF后用通配路径，保存拼写/e*c/p*s*we未必匹配期望文件。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Blind XSS fired 邮件与所有表单的范围 | 正文称developerpanelstoredBXSS并建议每表单都注入，图仅两条截断XSSHunterfired通知，没有payload、主体或浏览器上下文。 | [方法条目](../by-type/xss.md) |
| 平台自身计划与 claim token 标题 | 正文说找不到项目就测试平台本身，图只是Bugcrowd claimtokenexposed/300奖励标题。 | [方法条目](../scope-and-rules.md) |
| OAUTHScan 十项检查与协议消费者 | 正文说扩展含10+OAuth/OpenID检查，图只有仓库卡片；具体规则/版本/结果未保存。 | [方法条目](../by-type/oauth-oidc.md) |
| EDRHunt 帮助页是本机枚举能力 | 完整CLI图列services/processes/registry/drivers及all/scan、单项flags；结尾只输入scan，无结果。 | [方法条目](../discovery/client-and-cloud.md) |
| Grafana 零日措辞与已标 CVE 的状态 | 正文称两个0day/最快1hour并说每IP，图却列CVE2021-43798、PathTraversal、triagedopen/high。 | [方法条目](../impact-and-acceptance.md) |
| Kafka 叙述与 ZooKeeper 2181 标题分开 | 正文说KafkaP1，图只有UnauthorizedZooKeeper/2181、P1triaged/stillassessed，没有认证或读写交换。 | [方法条目](../discovery/passive-and-services.md) |
| 个人资料 JSON 与 full ATO 的能力缺口 | 保存fullATO/RCE宣传，图实际200Successful个人profile含姓名、联系方式、tenant/landlord/status/securityid等已遮字段，没有登录、重置或会话变换。 | [方法条目](../by-type/authn-session.md) |
| WAF Tester 单上下文与真实规则集 | 完整图为WAFTester，明确globalHtml/attributeHtml、每次单context限制，弹框显示1；正文怀疑非真实Cloudflare。 | [方法条目](../by-type/waf-bypass.md) |
| 管理项目七阶段与成熟度百分比的限制 | 完整推广图列注册、经理、launch、skills、scantriage、validate、reportremediate七阶段，以及private/public规则和75/100模型宣传。 | [方法条目](../reporting.md) |
| 负数量负总额和 Paid 发票不等免费完成 | 保存图片是数量负1、unitprice与total负50000IDR的发票，标Paid/GoPay；没有创建请求、服务端价格计算、库存/账本或交付证据。 | [方法条目](../by-type/business-logic.md) |
| image URL 弹框与 iframe SSRF 标题 | 完整图地址含image?url外部图片URL，页面弹框显示短字串，没有保存请求/iframe/服务端抓取。 | [方法条目](../by-type/xss.md) |
| GitHub 代码搜索命中与材料生命周期 | 正文介绍grep.app正则搜索及当时仓库数量，没有具体命中内容、所属项目或有效凭据。 | [方法条目](../discovery/passive-and-services.md) |

| details toggle 与 JavaScript 字符串须绑定真实解析上下文 | 正文提供details/open/ontoggle与字符串闭合型片段，完整图另有模糊cookie弹框，只能辨认分析cookie样式字串，没有完整请求响应和其他实际读者。 | [方法条目](../by-type/xss.md) |
| OAuth match replace 响应与服务端身份绑定 | 保存正文称改变OAuth响应即可绕过，没有授权码交换、token或服务端身份状态。 | [方法条目](../by-type/oauth-oidc.md) |
| HTTP 与 HTTP2 捕获的可见性边界 | 正文建议Wireshark发现Burp未显示的HTTP/HTTP2问题，另一帖称Logger人工分析发现4项HRS与2项SSRF。 | [方法条目](../discovery/records-and-incremental.md) |
| 密码重置区用户ID与邮箱暴露须分开验证 | 正文建议更改用户ID；两张完整图片分别是用户详情IDOR150与重置区邮箱暴露200的奖赏通知，没有重置执行链。 | [方法条目](../by-type/idor-access-control.md) |
| 固定一千页 DNS 查询与有限分页证据 | 保存完整循环固定1至1000页，URL与POST字段给同一域查询，跟随跳转、忽略TLS校验，按页grep并sort-u。 | [方法条目](../discovery/passive-and-services.md) |
| 403 与 CNAME 切换需要证明同一资产同一权限 | 正文声称403后改用CNAME可获得SQLite，完整图只建议查CNAME再访问可能200；没有403/200交换、数据库字节或身份对照。 | [方法条目](../discovery/web-and-api.md) |
| tgz 标题与 PDF PHP 分号文件名图片不一致 | 正文称tgz上传RCE，完整图实际为multipart文件名shell.pdf;.php、application/pdf及含密码检查和cmd执行的PHP文本；没有上传响应、存储路径、下载或解释器执行。 | [方法条目](../by-type/file-upload.md) |
| Osmedeus 云向导配置与实际资源操作分离 | 保存正文与两图为4.0.2历史发行说明、新DNS/anew及云向导选择Linode/DigitalOcean、默认镜像/规格/区域、掩码token与YAML覆盖，再校验或列SSH镜像等信息。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 第二阶资产采集先解析依赖再判断接管 | 完整图用BeautifulSoup收集HTML/JS/CSS中src/href的script/img/audio/video/svg，绝对URL抽域送takeover模板，相对URL用于词表。 | [方法条目](../by-type/subdomain-takeover.md) |
| Actuator connection test query 字符串不等已执行 | 完整图JSON列出admin/actuator/env、found true和spring.datasource.hikari.connection-test-query，其值含CREATE ALIAS/Java Runtime及CALL whoami，部分表达式形状不完整。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 搜索公开托管平台与在范围内漏洞是两条判断 | 保存帖推荐Trello、Zoom、Pastebin、.mil dorks、奖励检索与历史政府范围列表，另称排除类型中能找到允许的XSS。 | [方法条目](../scope-and-rules.md) |
| localStorage 与 Cookie 弹框需到实际权限影响 | 正文称反射XSS读取localStorage可升级高危；另一帖鼓励进一步影响，图片在搜索URL中含img/onerror并显示可读cookie。 | [方法条目](../impact-and-acceptance.md) |
| phpMyAdmin htaccess 下载与认证配置泄露 | 完整图GET phpmyadmin/.htaccess返回200 octet-stream，正文出现deny from all、Basic/AuthName、authuserfile路径和Limit规则，另有allow from all；可见cookies不是可复用授权。 | [方法条目](../by-type/info-secrets.md) |
| Trust Tokens 本地存储画面不证明 CORS 读取 | 正文称CORS已解决，完整图是DevTools本地Trust Tokens发行者与WebSQL数据库表，未显示Origin、CORS响应头或跨站读取。 | [方法条目](../by-type/cors.md) |
| Akamai SVG 与 Cloudflare 编码片段的单实例边界 | 一张完整搜索页图显示svg/onload弹框，正文标Akamai；另一帖提供Cloudflare编码片段，均未保存完整边缘请求、规则版本和后端字节。 | [方法条目](../by-type/waf-bypass.md) |
| git 目录拒绝与 config 文件权限分别建模 | 完整图强调.git为目录而config为文件，正文把403目录与可读config作发现技巧，并称GitHub部署经常如此。 | [方法条目](../by-type/info-secrets.md) |
| Cariddi grep uro Dalfox 管道的过滤损失 | 保存完整管道先 intensive 爬取，再用后缀排除与简单问号参数字符正则、sort、uro并交Dalfox。 | [方法条目](../targeted-fuzzing.md) |
| 自托管头像与 URL token 的 Referrer 消费者 | 正文假设头像是攻击者托管且页面URL有token，没有保存图片请求或泄露值。 | [方法条目](../by-type/authn-session.md) |
| Java 指纹到 Log4j 回连须保留每一层证据 | 保存完整图片包括Wappalyzer Java指纹、1至9步骤、Burp历史插件安装、爬取/主动扫描/Collaborator与混淆ldap/rmi示例，没有保存回连。 | [方法条目](../by-type/cmd-injection-rce.md) |
| phpMyAdmin HY000 1045 是认证错误线索 | 完整图phpMyAdmin输入单引号后mysqli::real_connect提示HY000/1045 Access denied与无法连接MySQL，没有SQL语法结果。 | [方法条目](../by-type/sql-injection.md) |
| 图示与动手偏好需要可验证学习产物 | 正文偏好图解和例子，完整图反对付费课程/导师并强调无出售秘密；另有五次理解应用与HTTP/SSL基础建议。 | [方法条目](../hunting-strategy.md) |
| CloudSploit ACM WARN 与有限收集范围 | 完整图显示跳过AWS分区设置、只测ACMCertificateValidation、收集2个API调用后四项邮箱验证WARN表格，没有全云扫描或漏洞利用。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| content script manifest 与页面通信权限边界 | 完整图把manifest content_scripts/permissions与DevTools扩展和top执行上下文放在一起，保存内容没有具体message桥/sink或越权动作。 | [方法条目](../discovery/client-and-cloud.md) |
| Shodan login 标题与反射 XSS 草稿证据 | 正文从http.title login候选到高危RXSS，完整图为倾斜报告草稿含编码img片段与cookie影响说法，未展示可读完整响应、其他读者或会话有效性。 | [方法条目](../discovery/passive-and-services.md) |
| 电影价格一美元说法与银行收据不能连成结算链 | 保存阿拉伯正文称改变端点响应可让票价变一美元；图片只有银行支付记录，未展示端点请求、服务端重算或交付。 | [方法条目](../by-type/business-logic.md) |
| 路径编码候选要定位具体规范化消费者 | 正文列favicon路径、png加编码片段、点段、调试参数及URL/双重编码/换行实体形式，没有保存成功响应。 | [方法条目](../discovery/web-and-api.md) |
| 重置 URL 搜集链不证明有效 token 或接管 | 完整图从subfinder经少数端口、HTTPS优先探活、gau搜reset/token/password，再xargs/curl跟随跳转与grep表单提示输出CHECK。 | [方法条目](../by-type/authn-session.md) |
| Houdini Docker 工具目录与运行环境是两项证据 | 完整图仅目录、标签、搜索、RAUDI更新/star与工具名，没有image digest、容器权限、执行结果或漏洞证明。 | [方法条目](../discovery/records-and-incremental.md) |
| SQL 语句学习表与真实查询消费者分开 | 完整SQL图列SELECT/FROM/WHERE/JOIN/CASE/NULL/LIKE、DDL/DML、聚合GROUP/HAVING/ORDER/LIMIT与COMMIT/ROLLBACK，JOIN图和教学逻辑顺序没有漏洞交换。 | [方法条目](../by-type/sql-injection.md) |
| Removing AWS keys 提交信息与 diff 方向矛盾 | 完整历史diff标题说Removing AWS keys，但可见新增行含凭据形式而删行是占位值；不抄录字面key。 | [方法条目](../by-type/info-secrets.md) |
| HTML image 改写不能推广为任意标签过滤绕过 | 正文称所有标签被过滤时用image，没有保存真实输出。 | [方法条目](../by-type/xss.md) |
| HTML 注入到 javascript iframe 需要独立导航证据 | 正文把HTML注入升级RXSS并给iframe javascript样式，后续评论未保存按豁免覆盖；没有实际DOM/CSP/导航结果。 | [方法条目](../by-type/xss.md) |
| 按扩展名推影响应改为消费者检查表 | 保存完整列表将asp/aspx/php、svg/gif、csv/xml/avi、html/js、png/zip/pdf直接对应webshell/XSS/SSRF/XXE/LFI/DoS。 | [方法条目](../by-type/file-upload.md) |
| RBCD GenericWrite 图是候选 ACL 路径 | 完整图列父子/森林双向trust、三个域对象数量与九条GenericWrite/GenericAll候选边，没有已修改委派、service ticket或代码执行。 | [方法条目](../by-type/idor-access-control.md) |
| Findomain 历史 beta 标志与吞吐不等覆盖 | 完整7.0 beta2图列异步resolver/HTTP替换、no-resolve/状态标志修复、默认线程与Rust最低版本变更；后帖称900 HTTP/s、1532 DNS/s。 | [方法条目](../discovery/records-and-incremental.md) |
| Exrop 标题与 ROPgadget 输出先核架构和入口 | 完整图片实际是ROPgadget v5.2生成write-what-where、syscall参数、int0x80与pack形式的链，不是保存的完整Exrop执行。 | [方法条目](../source-audit.md) |
| FUD 与跨系统说法不能从一次零检出推出 | 完整图片2022样本扫描0/26、引擎清洁列表与哈希，没有各系统运行行为；正文却称所有OS包含Mac。 | [方法条目](../experiment-design.md) |
| phpMyAdmin CVE 标题弹框与实际入口链 | 完整图是phpMyAdmin CVE-2022-23808标题页面上的XSS对话框，没有输入、响应、版本验证或真实部署资产。 | [方法条目](../by-type/xss.md) |
| 奖赏通知与漏洞机制分离并保留隐私 | 完整图分别为BlindXSS60通知、单次搜索alert(0)与多报告标题/状态/奖金；正文另有Host Header ATO P1和full SSRF一万元说法，没有完整机制链。 | [方法条目](../reporting.md) |
| RIR 四选项遗漏 AFRINIC 与资产归属边界 | 保存问题称四个RIR，选项D列APNIC/LACNIC/ARIN/RIPE NCC但遗漏AFRINIC。 | [方法条目](../discovery/passive-and-services.md) |
| 设备资料类别与已删除文件可恢复的条件 | 两张完整图列密码/银行卡/SSN/联系人/最近文件/网页历史cookie、通话短信、当前位置及照片导航历史等位置，并称删除文件在覆盖前都可恢复。 | [方法条目](../discovery/client-and-cloud.md) |
| 头像 Content Type 绕过与 Stored XSS 奖赏题目 | 正文称改上传Content Type即被接受，完整图只是Stored XSS on profile picture450通知。 | [方法条目](../by-type/file-upload.md) |
| 两个 XSS 入口同 profile 影响应按根因去重 | 正文询问两个XSS入口能否再次用profile取数证明ATO，另一帖询问十处目录列举分开提交。 | [方法条目](../reporting.md) |
| 被排除 RCE 改叫 Stored XSS 或 LFD 不扩大许可 | 保存完整片段通过shell写HTML至公开目录或cat系统文件，建议RCE超出范围时改叫Stored XSS/LFD。 | [方法条目](../scope-and-rules.md) |
| Droopescan help 指示能力而非扫描结果 | 完整图仅help，scan为CMS扫描、stats为能力/状态，还有debug/quiet与Drupal/SilverStripe示例。 | [方法条目](../discovery/records-and-incremental.md) |
| 路径类参数到 include read 消费者的分层 | 正文解释include可能输出文件、用cd类比路径穿越并列action/dir/page/folder/document/layout参数；没有服务端真实包含或文件字节。 | [方法条目](../by-type/lfi-path-traversal.md) |
| portal searchitem ORDER BY 错误须结合对照 | 完整图在POST portal.php searchitem中加入ORDER BY4，响应显示Unknown column '4' in 'order clause'；请求存在历史PHPSESSID但不复制/重放。 | [方法条目](../by-type/sql-injection.md) |
| recover_password email 请求与重置身份状态 | 完整图仅POST /api/recover_password JSON含被遮蔽email、同origin与cookie，未保存响应、投递、token绑定或最终提交。 | [方法条目](../by-type/authn-session.md) |
| 转移到私有项目的沟通状态与奖金完成分开 | 完整图沟通说工作中要转移到有奖金的项目，平台staff已转移，作者再问邀请；侧栏High7.5/Triaged Open，未显示接受邀请、bounty发放或付款完成。 | [方法条目](../reporting.md) |
| 三斜杠加 query 的 404 到跳转要核 Location | 正文称同三斜杠外域路径不带query为404，附query则跳转；奖赏图250通知且要求披露细节需项目许可，没有原始Location/重定向链。 | [方法条目](../by-type/open-redirect.md) |
| FlareQDB 断点读取输出不是任意代码执行 | 完整图历史Windows终端显示调试命令在地址处读取ebp偏移字符串并反复打印输入，缺完整程序、架构/符号和漏洞入口。 | [方法条目](../source-audit.md) |
| Dofind TLD 拼接输出与注册所有权分开 | 完整图显示加载1489条域候选，把目标名接多种后缀并打印，正文给工具链接。 | [方法条目](../discovery/passive-and-services.md) |
| Password reset link not expire 的低危重复状态边界 | 完整图报告题目重置链接不失效，Closed/Duplicate、Low、奖金0。 | [方法条目](../by-type/authn-session.md) |
| 外部 RSS 订阅到 Blind XXE 不可跳过 XML 消费者 | 保存正文建议寻找外部RSS订阅并称Blind XXE，没有DTD配置、外部实体解析或实际回连。 | [方法条目](../by-type/xxe.md) |
| cheatsheet 可见 CVE 片段先绑定实际解释器 | 完整图列Imagick标SSRF但片段含命令拼接形状、Shellshock CGI请求头/反向shell及Heartbleed工具/Metasploit引用，右端裁切保留限制。 | [方法条目](../source-audit.md) |
| Niagara Fox banner 的监控线索与 OT 行为边界 | 完整历史图在1911/tcp返回Niagara Fox/应用版本、Java VM与QNX/主机标识，没有控制操作或漏洞。 | [方法条目](../discovery/passive-and-services.md) |
| GCS 缺斜杠示例先纠正 URL 语法与读取权限 | 正文示例把storage.googleapis.com与target name直接相连，不能静默视为合法bucket URL；没有实际列表/对象内容。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| FakeLogonScreen Beacon 截图不证明凭据取得 | 完整图Cobalt Strike显示powershell进程中的会话与任务become interactive、发送16bytes，没有伪登录界面、输入密码或凭据结果。 | [方法条目](../by-type/authn-session.md) |
| Excel 宏被禁用与读写工具标题分开 | 完整图Excel output2.xls打开decoy sheet，黄色条明确Macros disabled并有Enable Content按钮，单元格诱导开启；没有宏代码、启用事件或执行结果。 | [方法条目](../by-type/document-rendering.md) |
| Web3 不需要数据库的断言不能代替架构核验 | 完整图文章片段称DApps不需要数据库/后端是合约，于是SQLi、上传与服务端RCE不会带到Web3。 | [方法条目](../by-type/smart-contract.md) |
| recon 摘要与可回溯原始资料须一起设计 | 完整聊天图强调把信息摘要存flat files、记录数据重新取得出处，例如百万历史记录提取域有100/0端点，不存全部重复资料；聊天关于异常模式仍是提问。 | [方法条目](../discovery/records-and-incremental.md) |
| Snaffler share 规则命中与有效秘密分开 | 完整图从AD列10台电脑、创建任务、发现readable shares再规则匹配web.config，打印validation/decryption形式材料。 | [方法条目](../by-type/info-secrets.md) |
| 每小时与永续 rescan 的范围和终止条件 | 完整Osmedeus图提供每60分钟命令及完成即再次永续运行两种模式，没有授权期限、并发/失败预算或终止。 | [方法条目](../discovery/records-and-incremental.md) |
| 竞态结果以业务不变量与账本核实 | 正文提醒Intruder/Turbo表可能遗漏成功，应查网页最终结果；网页也可来自缓存或异步状态，二者均未保存本案交换。 | [方法条目](../by-type/business-logic.md) |
| njsscan clone upload 界面不证明 SAST 数据流 | 完整图nodejsscan界面仅git Clone与Upload Scan入口、版本信息和recent scans，无代码、规则或结果。 | [方法条目](../source-audit.md) |
| BigQuery INT64 错误泄露需要请求响应与最小对照 | 完整图请求logtype含UNION及CAST project_id AS INT64，HTTP200内JSON statusCode400/stateFAILED/invalidQuery，错误可见Bad int64 value与被遮蔽标识。 | [方法条目](../by-type/sql-injection.md) |
| Boko passive 与 active dyld 检查的执行差异 | 完整help列运行进程/已安装/指定应用、输出log/CSV、SIP disabled筛选、passive classic检查与active执行主二进制设置DYLD_PRINT_RPATHS。 | [方法条目](../discovery/client-and-cloud.md) |
| Plution 十一案例不能等于所有原型污染 | 完整正文称headless Chrome用硬编码payload检测十一种已列案例，没有具体目标的数据传播或实际sink。 | [方法条目](../by-type/prototype-pollution.md) |
| RCE 后路径列表包含拼写与隐私风险条件 | 正文列var/log、var/spool/crony、etc/cron.*、etc/group、etc/passed、var/log/btmp。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 事件 handler 词表与 email 字段须核展示消费者 | 正文推荐生成on事件词表；完整email图列包含script的三个地址形式并称fuzz可能代码注入，工具图只是repo卡片。 | [方法条目](../by-type/xss.md) |
| Escape the Escape 需要区分输入校验与输出编码 | 正文泛称输入escaping可被escaped，没有语言/上下文或编码过程。 | [方法条目](../by-type/xss.md) |
| yusub 十二 API 汇总输出不是全域覆盖 | 保存正文称收集十二个API，完整图从两个示例输入输出许多域形状行，部分看似email/端口/特殊格式，没有API成功状态或所有权证据。 | [方法条目](../discovery/passive-and-services.md) |
| YouTube 教程说明中的 admin 入口只是公开线索 | 完整图视频说明展示远程控制面板教程、firmware3更新与admin面板/info链接，关键名称被遮挡，无HTTP响应、身份或权限结果。 | [方法条目](../discovery/passive-and-services.md) |
| SharpCookieMonster 本地 Chrome 启动与 cookie 结果限制 | 完整图工具使用用户临时Chrome目录，DevTools监听本机端口并寻找process、取URL、杀进程，最后出现Cookies字样但具体内容受分辨率限制，旁边shell仅能见到进程/链接信息。 | [方法条目](../by-type/authn-session.md) |
| Wireshark Follow HTTP Stream 是离线 SQL 痕迹证据 | 完整图SQL_Lab.pcap的Follow HTTP Stream列input UNION信息表查询与许多表名反复出现，界面标一client/server pkt及45kB conversation，未见完整请求权限和基线。 | [方法条目](../by-type/sql-injection.md) |
| Talisman pre push 形状检测与全历史泄露边界 | 正文描述pre-push检查可疑outgoing changeset，没有规则/版本、命中结果或全历史扫描。 | [方法条目](../by-type/info-secrets.md) |
| Google Groups key 检索与 Terraform 示例凭据区别 | 正文给Google Groups公司名/密钥关键词；完整图是创建AWS Access Keys后写Terraform provider的历史示例，部分字面值被遮挡。 | [方法条目](../by-type/info-secrets.md) |
| Hybrid 框架架构图与实际测试覆盖分开 | 完整图连IntelliJ/GitHub Actions、Java Gradle Selenium4、Grid/BrowserStack浏览器节点，Docker Kafka/LocalStack/Jenkins/ZAP/SonarQube与报告界面。 | [方法条目](../experiment-design.md) |
| 缺响应头的 clickjacking 通知不是敏感动作证明 | 完整奖赏图写lack of sensitive headers leads clickjacking300，正文建议检查每个项目，没有响应/CSP、可嵌入页面或动作结果。 | [方法条目](../by-type/clickjacking.md) |
| Can I Take Over 表格指纹是历史候选名单 | 完整图列Acquia/Akamai/ELB/Cloudfront等Not vulnerable、Agile/Anima/S3等Vulnerable、Fastly Edge case及错误字串/讨论链接；没有当前服务注册政策或目标资源归属。 | [方法条目](../by-type/subdomain-takeover.md) |
| SSRFire 依赖与 callback 配置不等自动发现完成 | 完整终端图仅启动命令与banner，要求ffuf/gau/qsreplace路径、可选openredirex、setup依赖和询问是否子域检查。 | [方法条目](../discovery/records-and-incremental.md) |
| 手机发现 env 过期 key 与 P4 P5 是案例状态 | 正文称手机看到目录列表和.env AWS key，报告DL P5/SDE P4因过期，没有保存文件、当前key状态或权限验证。 | [方法条目](../by-type/info-secrets.md) |
| S3 PRE 列表不等匿名对象读取或写入 | 完整图仅aws s3 ls某dev bucket及许多PRE前缀，未显示CLI身份/配置、匿名参数、对象读取或写入。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Cognito 双池流程图不证明 zero click 接管 | 两张完整图画login→User Pool/第三方登录→JWT→Identity Pool token exchange→临时AWS credentials→S3，共六步。 | [方法条目](../by-type/oauth-oidc.md) |

| Voltron 调试器画面须绑定架构和当前停点 | 完整画面包含反汇编、寄存器、栈与GDB的argc/strcmp、sleep和循环示例；这说明本地调试状态，没有远程漏洞入口。 | [方法条目](../experiment-design.md) |
| SVG 未编码尖括号须追到实际 HTML 消费者 | 正文称关闭SVG的右尖括号被转义而尾部左尖括号未处理，另一帖提供编码SVG并声称除Firefox外可用；未保存原始响应、完整DOM和浏览器版本。 | [方法条目](../by-type/xss.md) |
| iframe javascript 与 ESI 注释要分清不同解析阶段 | 完整浏览器图有十六进制编码的iframe javascript属性与空白prompt；正文还有fo<!--esi-->cus/a<!--esi-->lert变体。 | [方法条目](../by-type/waf-bypass.md) |
| document.cookie 弹框要证明实际可用权限 | 完整图显示问卷分数参数、注入片段及cookie弹框，可以辨认分析类cookie等字串，没有其他读者或可用会话证据。 | [方法条目](../impact-and-acceptance.md) |
| 词表命中 config.json 与真实秘密暴露分层 | 完整图有config.json连接串UID/password、数据库/服务器和AWS/S3字段；另一组JS图有crypt.secret、document token加密注释及demoConfig的orgId/token/restUri/searchHub。 | [方法条目](../by-type/info-secrets.md) |
| phpinfo 服务端回显与 HttpOnly 读取限制分开 | 完整图phpinfo的$_COOKIE/ci_session与DevTools HttpOnly=true/Secure=false并列；另一图JS用带凭据同步XHR读取info.php，再按HTTP_COOKIE索引截取与base64；multipart另有外部script，JSONsuccess=true。 | [方法条目](../by-type/xss.md) |
| Git clone 与 mirror 的引用覆盖范围需列清 | 正文提示普通clone与mirror可能暴露范围不同，没有保存具体引用集合、敏感提交或服务端权限。 | [方法条目](../source-audit.md) |
| 路径后缀和账户标识变体须保留对象同一性 | 正文列PHP/ASP候选和API的.json、?、斜杠、v2、账户路径、X-Original-URL；另称网站/users/reports/settings拒绝而API子域200。 | [方法条目](../discovery/web-and-api.md) |
| 手机 POST userid 到接管仍缺执行消费者 | 正文说手机登录POST能控制userid、网页没有并需用户交互；完整图只有Android误配置报告Medium5.4/1000奖励状态，没有请求、响应或被接管会话。 | [方法条目](../by-type/idor-access-control.md) |
| nrich Shodan ADB 与来源归属边界 | 正文介绍IP标准输入获取Shodan metadata，另将5555端口ADB banner称Android Root Bridge并联系ETH挖矿速度；没有设备权限与shell结果。 | [方法条目](../discovery/passive-and-services.md) |
| 奖励与地区 dork 搜索不能扩展项目许可 | 保存正文按奖励政策、地区/行业关键词及域检索，有拼写/语法差异，没有当前项目条款与实际授权。 | [方法条目](../scope-and-rules.md) |
| 四十八小时未回应不是统一升级披露时限 | 正文建议等48小时后追问并借社交媒体/大客户催促，没有项目协议和报告状态上下文。 | [方法条目](../reporting.md) |
| DorkSearch 分类 UI 与可用搜索结果分开 | 完整图显示漏洞公告、错误、秘密文件、登录、设备等dork类别，没有查询文本、命中内容或资产归属。 | [方法条目](../discovery/web-and-api.md) |
| Nuclei Burp 生成器与可验证模板分开 | 两张完整Burp图在Nuclei页展示localhost:8081的GET /，无响应/匹配器结果；正文鼓励编写目标相关模板。 | [方法条目](../discovery/records-and-incremental.md) |
| aquatone takeover 输入与服务归属独立判断 | 正文给带http scheme的-d示例，但没有DNS、服务专属错误、当前可注册状态或受控内容。 | [方法条目](../by-type/subdomain-takeover.md) |
| 银行文档被索引与上传删除权限分别验证 | 正文问被Google索引的银行PII照片/存折、上传和删除如何影响，没有保存文件正文、访问身份或操作结果。 | [方法条目](../by-type/info-secrets.md) |
| 视频和 CVSS 好评不能充当统一奖励公式 | 完整图报告质量反馈给CVSS与视频不同分值并有奖励时间线；正文强调攻击者视角。 | [方法条目](../reporting.md) |
| WinBruteLogon 的 found 输出与真实认证分离 | 完整help列username/domain/wordlist及线程/verbose，示例打印本机Visitor、10001候选、2线程和OK found password。 | [方法条目](../by-type/authn-session.md) |
| DNS rebinding 要比较解析检查和实际连接地址 | 正文称被阻断SSRF可尝试DNS rebinding并找到两项，没有DNS时序、地址校验或连接结果。 | [方法条目](../by-type/ssrf.md) |
| 二十五个 redirect 名称不等重定向消费者 | 完整词表含next/url/target/destination/redirect_uri/returnTo/checkout_url/continue等，另一图是Message参数与hacked弹框，未有Location或外部导航。 | [方法条目](../by-type/open-redirect.md) |
| 忽略已被工具发现的子域会遗漏重要旧资产 | 正文建议amass/subfinder扫到的全部忽略去找新目标；其他帖描述被动数据源与工具比较，没有覆盖、时效或风险结果。 | [方法条目](../hunting-strategy.md) |
| GraphQL 空 OTP 成功字段不能直接证明 2FA 绕过 | 完整图POST /graphql有遮蔽token、空otp_code及六位verification_code；HTTP200 JSON同时有was_successful=true与errors.edges。 | [方法条目](../by-type/graphql.md) |
| JNDI server 监听和生成链接不等目标类加载执行 | 完整图是本地JNDI工具java参数与open Calculator示例，HTTP/RMI/LDAP监听及输出url，并注释历史JDK trustURLCodebase要求；没有目标lookup/加载/执行。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 复制 WordPress 插件搭建练习不能代替目标复现 | 正文建议识别站点插件后自建相同WordPress再测试，并称总能找到XSS；没有目标版本、设置、输入或其他读者。 | [方法条目](../experiment-design.md) |
| PublicWWW 代码索引与当前完整站点不同 | 正文介绍从HTML/JS/CSS文本搜索并导出网站列表，没有目标命中与当前代码。 | [方法条目](../discovery/passive-and-services.md) |
| POST 改 PUT 的方法差异须跨同一权限边界 | 正文称修改HTTP方法可出IDOR，没有实际交换或对象变更。 | [方法条目](../by-type/idor-access-control.md) |
| 混淆 Google 服务 ID 不等管理员角色已赋予 | 完整片段有SERVICE_ADMIN_ROLE、Services Administrator及APPADMIN/VIEWDLPRULE、遮蔽serviceIds，没有ID映射、请求、角色赋予或权限结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Tomcat 凭据中的 root 字符串不等系统 root | 正文描述历史演练从公网Tomcat root/root到AD，没有保存认证/进程身份和跨域授权链。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 管理员页面 UI 不证明访问控制已绕过 | 完整图实际Shipment Details界面和物流历史；另有SelfXSS Duplicate Closed及APIIDOR P3/850报告，双重复正文称v1拒绝v2允许。 | [方法条目](../by-type/idor-access-control.md) |
| NTLMRecon 多端点认证 challenge 与登录不同 | 完整终端列43种候选端点，EWS的NTLM、ActiveSync Basic realm、PowerShell Kerberos与Rpc Basic并保存CSV；没有凭据认证、授权读取或执行。 | [方法条目](../discovery/passive-and-services.md) |
| Host 进入 SilverStripe Location 与重置毒化分开 | 完整GET /admin/pages带Host bing.com及cookie，响应302 Location包含该Host，另有控制器、locale HttpOnly和CSP。 | [方法条目](../by-type/host-header.md) |
| 点路径与分号路径须核前后端规范化差异 | 完整tip写/image/../secretfolder和/image/..;/secretfolder并要求首目录存在，没有实际403/200、规范化后的对象或服务响应。 | [方法条目](../by-type/waf-bypass.md) |
| Katoolin3 标题与 v1.0 安装菜单不是同一版本证据 | 完整图是Katoolin v1.0列330工具、仓库更新、类别、菜单与帮助，正文称Katoolin3。 | [方法条目](../discovery/records-and-incremental.md) |
| 反射存储 DOM 和 self 标签不是互斥四类 | 正文将XSS分四种，另一帖声称mutation XSS，图仅XSS Hunter fires列表、受害URI/IP、缩略图与操作按钮，没有变异前后解析字节。 | [方法条目](../by-type/xss.md) |
| 全端口建议仍需服务和预算覆盖证据 | 正文建议先全端口再Nuclei，没有保存端口范围、扫描错误、服务确认或项目许可。 | [方法条目](../targeted-fuzzing.md) |
| staging 与 log 关键词只生成历史候选 | 正文把Subfinder带http域输入、grep staging与Google日志搜索串联，没有DNS、响应或日志内容；另有被动recon文章标题。 | [方法条目](../discovery/passive-and-services.md) |
| GraphQL 思维图把 schema 和动作候选分开 | 完整图可辨端点/Playground/Schema、基础/深层introspection、类型/字段/参数、query/mutation、用户/权限及商业逻辑；部分微小叶子字不可辨。 | [方法条目](../by-type/graphql.md) |
| 已经 root 的 CTF flag 不能补全初始入口 | 完整图训练Gift主机root提示符、列user.txt与flag，并有Root and User Flag alt；未保存取得root的方法。 | [方法条目](../experiment-design.md) |
| DRAKVUF 样本元数据和进程树不是恶意结论 | 完整报告有PE32+ x86-64 Windows样本、哈希、约15秒运行以及系统/测试进程树，没有完整API行为、网络或恶意因果。 | [方法条目](../discovery/client-and-cloud.md) |
| 二十五个 RCE 参数名称仍缺命令执行 sink | 完整词表含cmd/exec/command/ping/query/code/func/load/process/read/module/payload/run/print等，另一图列前十项。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 嵌套 image URL 到元数据仍缺请求身份 | 正文从localhost image?url嵌套到云元数据并声称header/WAF变体，没有保存HTTP链、header内容或返回字段。 | [方法条目](../by-type/ssrf.md) |
| 提交收据与邮件 claim 不等分诊完成 | 完整图提示submission received，并要求邮件关联finding；没有已认领、分诊、有效性或支付。 | [方法条目](../reporting.md) |
| Ruby ERB 的字符串数据与模板代码执行边界 | 正文描述用户输入ERB表达式进入模板渲染，没有完整模板、环境或实际结果。 | [方法条目](../by-type/ssti.md) |
| CSRF 接管标题仍需浏览器凭据和状态绑定 | 完整图只有CSRF导致ATO的P2 Triaged/仍评估状态；另一帖是RXSS窃取登录表单接管文章标题。 | [方法条目](../by-type/csrf.md) |
| Java URL 的 url 前缀须按实际 JDK 解析 | 完整代码先用^[a-z]+:检查scheme并只拒绝file；另一图JDK1.8.0_261的new URL(url:http://example.com)交HttpURLConnection GET读到Example Domain。 | [方法条目](../by-type/ssrf.md) |
| polyglot 上传需要两个真实格式消费者 | 正文声称始终使用polyglot且多数目标适用，没有文件、上传回应或浏览器/服务端解释结果。 | [方法条目](../by-type/file-upload.md) |
| bankVerificationStatus JSON 与可变更权限不同 | 完整JSON有币种INR、测试银行/账号字段、active=false、bankVerificationStatus=1、isSystemAccount=false和空documentFileHandle，未保存POST、身份/所有权或实际变更。 | [方法条目](../by-type/idor-access-control.md) |
| Osmedeus report done 与 installer 下载各自有限 | 完整图有4.0.3历史更新、workspace flow done/fast26/26与各报告路径，以及premium/Linux64强制下载说明；未读报告对象、没有完整安装结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 空 Docker registry 匿名可见不等可利用写入 | 正文称私人registry空且无需认证可上传，询问怎么利用，没有目录对象、push权限、镜像或消费者。 | [方法条目](../cloud/container-k8s-security.md) |
| 多报告和重复状态不能替代独立根因计数 | 完整图有Sony Medium5.3、Ubisoft混合P1/P3/P4 Triaged、NotApplicable、Duplicate、High Duplicate Closed、两P5 Informational及OAuth925支付。 | [方法条目](../reporting.md) |
| CAPE 仪表盘容量指标不证明样本行为覆盖 | 完整仪表盘显示任务/样本数、Top20、running3/pending0和时间/容量估算，没有单样本过程或检测证据。 | [方法条目](../discovery/client-and-cloud.md) |
| 重置 token 公共前缀不能证明可预测 | 完整tip给两个32位十六进制示例，共享00000007前缀，其余部分明显不同；不足以支持只差末字符或下一token可猜。 | [方法条目](../by-type/authn-session.md) |
| Moodle 第二阶存储到 SQL 执行须分别留证 | 完整MySQL图select mdl_badge_criteria_param返回field_lastname行，value含id条件及SLEEP(5)字串，本次select显示0.00sec。 | [方法条目](../by-type/sql-injection.md) |
| Searpy 历史搜索输出与当前漏洞分开 | 完整图是2020-09-14的Searpy2.3更新及Google inurl:php?id结果URLs，没有当前状态、范围或SQL执行。 | [方法条目](../discovery/passive-and-services.md) |
| Gateway refresh 图片需补 route 写入与执行链 | 完整图localhost:9000的POST /actuator/gateway/refresh带RewritePath表达式及Runtime open Calculator、HTTP200和计算器GUI；正文标CVE-2022-22947，没有此前route注册、真实部署和权限。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Litefuzz help 的模式和后处理不能算崩溃 | 完整help包含local/server/client、迭代/超时/mutator、crash/temp目录、minimize/superminimize、TLS/attach、postcmd、ReportCrash/memdump及禁用选项，没有crash样本和复现。 | [方法条目](../targeted-fuzzing.md) |
| Build Hack Fix Repeat 要保留业务不变量 | 正文建议自行做注册、登录、用户/管理员与数据库练习再攻击、修复和重复，没有已测应用或产物。 | [方法条目](../experiment-design.md) |
| uncover 多引擎 IP 端口命中不能归并成同一资产 | 完整图uncover0.0.1以jira字词给Shodan/FOFA/Censys结果，其中同IP不同端口及重复引擎记录；没有当前Jira响应、所有权或漏洞。 | [方法条目](../discovery/passive-and-services.md) |
| 战时项目计数和 testing tag 仍须明确授权 | 完整图是Ukraine相关项目views/reports/hackers计数与profile alt；另帖列third-party security testing字样。 | [方法条目](../scope-and-rules.md) |
| recon 管道覆盖和 tee overwrite 需要可复核计数 | 完整管道聚合subfinder/amass/assetfinder、httprobe、wayback、hakrawler、paramspider并排除后缀；另一正文waybackurls和gau分别tee到同一文件可能覆盖，sort uniq-i可能合并大小写语义不同URL。 | [方法条目](../discovery/records-and-incremental.md) |
| Proxy Everything 与拿到所有参数的说法有边界 | 正文建议Burp全代理、Ctrl-R和获取所有参数，没有TLS解密条件、请求保留/过滤或结果。 | [方法条目](../discovery/records-and-incremental.md) |
| CVE 单行 grep onmouse 不证明事件可执行 | 正文给形状不完整的while read/curl --insecure /admin/module.php示例并grep onmouse后打印vulnerable，没有响应上下文、CSP或浏览器结果。 | [方法条目](../by-type/xss.md) |
| taser Spider 与 uro 的过滤损失须量化 | 完整taser图从subdomain经httpx和xargs-P10 PythonSpider，再正则抽JS并把错误重定向/dev/null，结果含/maps/api/js和chunk.js；正文uro删除boring/duplicate。 | [方法条目](../discovery/records-and-incremental.md) |
| CVE critical 和 readme 命中仅是扫描线索 | 完整Nuclei图片只有CVE-2020-35489/http/critical及contact-form-7/readme.txt路径，没有请求、响应、实际版本和触发漏洞。 | [方法条目](../by-type/cmd-injection-rce.md) |
| vhost Host authority 格式和状态码不能混同 | 正文ffuf把http://FUZZ放进Host并按多个状态码保留，没有完整交换和服务内容。 | [方法条目](../discovery/web-and-api.md) |
| 重置管理员标题的用户详情 GET 不构成重置证据 | 完整图只有GET /rest/user/view/54191、遮蔽BEARER TEMP token与同站Origin/Referer，未保存响应、重置提交、被选身份或新会话。 | [方法条目](../by-type/authn-session.md) |
| OCR Recon 的 success timeout 与语义提取分开 | 完整终端以Sign关键词运行OCR Recon，显示www.amazon.com success与youtube timeout，没有图像、识别文字、坐标或页面类别。 | [方法条目](../discovery/records-and-incremental.md) |
| SQLi tale 的被动资产清单与注入确认分开 | 保存正文第一部分描述根域、收购关系、Wiki/Crunchbase/WHOIS和子域工具，未保存SQL查询、错误或注入响应。 | [方法条目](../discovery/passive-and-services.md) |
| Android Server Status 奖赏标题不能继承接管影响 | 保存手机快速P4正文与完整图是Apache Server Status、via127.0.0.1、Unresolved/accepted valid issue和历史VRT1.10.1。 | [方法条目](../impact-and-acceptance.md) |
| Meta 图片视频项目的奖励门槛只适用于所述上下文 | 完整回信称已知多个报告低于该项目奖励门槛，并说明只涉图片/视频、项目关闭且未写敏感XSS影响。 | [方法条目](../impact-and-acceptance.md) |

| snetra nrich InternetDB 的 CVE 输出须保留索引身份 | 正文称stdin IP扫描端口/漏洞；完整图实际列hostname、端口、CPE与历史CVE，另有dnsx解析第二列、移除方括号、sort-u后交nrich。 | [方法条目](../discovery/passive-and-services.md) |
| Nmap 加号强制脚本只改变 rule 适用条件 | 正文建议--script +http-methods解决不运行；没有具体拒绝原因、脚本版本或执行结果。 | [方法条目](../targeted-fuzzing.md) |
| IOC Parser 支持类型目录与提取正确性分开 | 完整图列ASN、IPv4/IPv6、URL/domain、email、MD5/SHA1/SHA256/filename、MAC、MITRE ATT&CK IDs/YARA，描述blog/PDF/CSV、defang和whitelist，没有提取样本/结果。 | [方法条目](../discovery/records-and-incremental.md) |
| Excel WEBSERVICE 的执行者决定是否服务端抓取 | 完整tip有WEBSERVICE公式，并声称只对Windows servers有效，未显示导出文件、计算触发或请求。 | [方法条目](../by-type/document-rendering.md) |
| Authz0 的 URL role credential 矩阵仍需对象结果 | 正文介绍自动授权工具按URLs、roles和credentials发现未授权，完整图只是logo，没有具体用例和结果。 | [方法条目](../by-type/idor-access-control.md) |
| Burp Bounty 自动更新要保留检查时规则版本 | 完整2.4.0changelog写profiles/rules、扩展自动更新、Collaborator替代host、Variations/Request passive修复，没有安装或扫描结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 扩展代码审阅从 manifest 到特权消息消费者 | 正文给CRXcavator、manifest与读代码三步，没有具体扩展版本、结果或漏洞。 | [方法条目](../source-audit.md) |
| 字符码片段不完整与二千二百奖励归属冲突 | 正文将onmouseover与不完整with/String/eval/fromCharCode片段描述为POST并获2200；完整图是CSRF端点1800和两项RXSS50/350，总和2200。 | [方法条目](../by-type/xss.md) |
| prod dev 与 ID1 差异须保持资源和身份一致 | 完整文字tip描述prod/profile常规邻近ID与1失败，dev邻近ID仍失败而dev/profile/1称可读admin用户名、邮箱、角色；没有实际请求响应，P2/700是作者记录。 | [方法条目](../by-type/idor-access-control.md) |
| Wayback mp3 候选与录音敏感字段的最小证据 | 完整tip称从Wayback发现mp3，姓名式文件名和听到姓名、号码、地址、超过900用户，未保存实际音频/HTTP权限对照。 | [方法条目](../by-type/info-secrets.md) |
| CIDR sdlookup 到 Osmedeus urls 启动只到 probe 阶段 | 完整图从CIDR经sdlookup-open、httprobe-c100、tee得到多http/https IP端口，再启动Osmedeus4.0.3 urls/probe，未显示后续扫描结果。 | [方法条目](../discovery/records-and-incremental.md) |
| SYN 半连接原理图不等目标资源已耗尽 | 完整图表示多SYN、服务端SYN-ACK等待第三次握手、正常用户请求后服务不可用，没有真实目标、测量或配置。 | [方法条目](../experiment-design.md) |
| 重复 phone_no 的 OTP 交付和身份绑定须同源 | 正文两次JSON都重复phone_no并声称短信到攻击者号码但会话为受害者，没有保存短信、解析后对象或会话。 | [方法条目](../by-type/authn-session.md) |
| Add Bank 表单字段不等验证绕过 | 完整图是Add Bank/UPI、姓名/银行/确认账号/IFSC、Cheque或statement照片与JPG/PNG最大5MB，没有保存提交、bank verification或另一个主体。 | [方法条目](../by-type/business-logic.md) |
| 影响补充和漏附件应绑定具体报告证据 | 正文要求按功能写影响并避免漏PoC；两张完整邮件说明clarification后RXSS由P3升P2，另有Email code bypass500奖励但无机制。 | [方法条目](../reporting.md) |
| DirtyPipe 本机 uid 变化不证明所有发行版适用 | 两图分别显示改passwd后新名字rootz与另一VM运行dirtypipe2后uid1000到uid0；后者有hijack/drop/restore日志。 | [方法条目](../experiment-design.md) |
| 数据库 banner dork 与敏感数据访问分开 | 正文列MongoDB/mongo-express、MySQL3306、elastic9200、PostgreSQL5432、ProFTPD21等搜索词，另有Free Shodan Tips标题，没有真实权限响应。 | [方法条目](../discovery/passive-and-services.md) |
| 小时 Git recon 归档要区分快照和发布完成 | 正文按/platform/company/domain/amass.json分层并给每小时git add/commit/push；完整图private repo按平台文件夹、有56commits，没有cron/推送回执。 | [方法条目](../discovery/records-and-incremental.md) |
| random 目录再返回的 LFI 状态码需真实文件消费者 | 正文列大小写api/bEtA、....//与../../etc/random/../passwd，称403变200；没有文件字节、真实文件系统或路径规范化记录。 | [方法条目](../by-type/lfi-path-traversal.md) |
| GraphQL Cop help 和十项检测说法不是审计完成 | 完整图GraphQL Cop1.0帮助只有目标URL/path、JSON输出和版本；正文后称约十种DoS/CSRF/info leak检测，repo卡没有具体规则。 | [方法条目](../by-type/graphql.md) |
| vaf GET 时间和长度输出不能继承漏洞判断 | 完整vaf1.8.0图在[]标记URL使用wordlist/.html后缀，reflex与URL encode为false，输出index.html200/1256/61ms；正文描述计时和显示优化。 | [方法条目](../targeted-fuzzing.md) |
| Windows file URL 到 NTLM 需要系统消费者与身份 | 正文建议SSRF指向file URL并运行Responder接收NetNTLMv2再破解，实际保存图片为meme，视频未保存按豁免。 | [方法条目](../by-type/ssrf.md) |
| 唯一 analytics ID 关联网站不等相同所有权 | 正文列分析ID站点，Synapsint图列Domain/IP/IPv6/ASN/SSL、Analytics/AdSense/email/phone、Bitcoin/CVE；没有实际query或来源结果。 | [方法条目](../discovery/passive-and-services.md) |
| 损坏的 Shodan ffuf 行先验证文本契约 | 保存串有favicon hash分离、awk中81/$2字形、while read do形状和mc200选项缺失，未有运行结果。 | [方法条目](../discovery/records-and-incremental.md) |
| GeoWiFi 多库部分命中不等当前位置或路由器权限 | 完整图有遮蔽BSSID/OUI TP-Link、多个提供者not_found、OpenWiFi部分坐标和JSON/map输出路径，没有采集时间或现场证明。 | [方法条目](../discovery/passive-and-services.md) |
| WebView 可加载 URL 与桥接特权须分层 | 保存正文只有WebView checklist主题和任意URL影响方向，没有WebView代码、配置、加载来源或JS bridge。 | [方法条目](../by-type/mobile-android.md) |
| iOS 测试主题清单与可解密流量证据分开 | 正文列架构、样例app、proxy/jailbreak、检测/pinning与敏感暴露方向，没有证书、配置、请求响应或绕过结果。 | [方法条目](../by-type/mobile-ios.md) |
| Invalid Header 图片需要原始连接队列证据 | 完整Burp请求有GET /404、单独0和另一个GET /buy，render视图出现400 Invalid Header及文字403，缺完整framing头和连接时序。 | [方法条目](../by-type/request-smuggling.md) |
| Amass intel enum track db 的历史示例不等当前覆盖 | 三图列org/CIDR/ASN/whois、active/brute、API config/resolvers/maxqueries、track/db/show/names和viz，未写实现版本、来源响应、结果或diff。 | [方法条目](../discovery/records-and-incremental.md) |
| 同一 Mail Injection 多端点的奖励仍按根因归并 | 正文建议同问题多找端点；完整回信250奖励覆盖最近essentially same issue的全部tickets，无邮件注入输入/解析机制。 | [方法条目](../reporting.md) |
| zip tar 备份名与受限档案字节分开 | 正文建议搜索zip/tar，dorks另含日志、email.xls、id_rsa和database.sql.zip；完整图只HIGH500奖赏/付款信息，没有档案内容。 | [方法条目](../by-type/info-secrets.md) |
| VERIFIED 响应字段与服务端会话创建分开 | 完整图OTP POST及HTTP200 JSON有VERIFIED/userId/token，多数关键值像素化；正文称Response Manipulation接管，没有修改前后、真实响应来源或最终身份。 | [方法条目](../by-type/authn-session.md) |
| SAST 分类统计和规则目录不能代替可达 flow | Scanmycode WebGoatPHP图55critical/1minor及code/file/XSS/key/entropy等分类；Codecat0.56图JavaScript规则目录有CSRF/SCE/XSS/SSRF/DOM/XMLHttpRequest等，没有具体代码或确认结果。 | [方法条目](../source-audit.md) |
| verbose recon 到 Nuclei CVE 的 stdout 契约 | 正文和完整图amass-passive-v接httpx-verbose再交nuclei cves路径，声称很快找已知漏洞，没有输出或每步错误。 | [方法条目](../discovery/records-and-incremental.md) |
| Firestore 无条件 write 使更窄 update 条件失去限制 | 完整v2规则在posts/comments递归路径allow read,write if true，又有update要求author/comment与已有字段相同，未保存实际部署和写入。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| MOBOTIX 搜索街景截图不证明当前设备公开权限 | 完整Shodan图有历史时间、IP/主机/地区、MOBOTIX200和街景截图，没有当前请求、设备所有者或认证策略。 | [方法条目](../discovery/passive-and-services.md) |
| 历史 DNS 找 origin IP 要核 Host SNI 同一性 | 正文称Incapsula后通过viewdns.info找到origin IP，没有DNS记录、连接或后端权限响应。 | [方法条目](../discovery/web-and-api.md) |
| ASSAMEE AES 名称与半程上传不能证明保密完整 | 完整图菜单upload/download/package、遮蔽API key、archive、AES-256-CBC密码提示及54%传输，没有IV/完整性、完成收据或解密回读。 | [方法条目](../discovery/records-and-incremental.md) |
| Log4j XFF 表达式和 403 要分 lookup 执行证据 | 完整图是vcenter SAMLRequest、X-Forwarded-For中的JNDI/hostName/Java版本表达式与403 Forbidden，正文有Google1337奖励标题。 | [方法条目](../by-type/cmd-injection-rce.md) |
| h1 百分号编码与 iframe 实体要追完整解码层 | 正文给h1混合大小写/百分号属性与iframe javascript实体，声称Cloudflare或括号过滤可绕，未保存响应/DOM；括号变体仍含一个字面右括号。 | [方法条目](../by-type/waf-bypass.md) |
| 百分号零空字符与 rate limit 计数键分开 | 正文建议%00用于认证的No Rate Limit bypass，完整回信是认证bypass High/P2和凭证奖励，无具体输入、计数或身份消费者。 | [方法条目](../by-type/authn-session.md) |
| CRLF MIME 片段须证明字节进入响应头边界 | 完整保存片段含CRLF、X-XSS-Protection、text/html及脚本/cookie，没有HTTP回应；同正文两条post IDs。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 新功能和 release 页是变化线索而非更高漏洞概率保证 | 正文称新功能发现概率always更高，建议观察release页，没有对比样本、版本差异或确认结果。 | [方法条目](../hunting-strategy.md) |
| JWT None 大小写和无签名许可要按验证器确认 | 正文称None标准算法并给alg:None与is_admin=true空签名片段，没有验证器、应用策略或受限权限结果。 | [方法条目](../by-type/jwt.md) |
| 客户供应商表截图不证明五千二百条越权 | 完整图只有两小表的客户/供应商姓名、地址/电话部分遮蔽，正文称BAC泄露5.2k，未有endpoint、身份对照、全量或数据来源。 | [方法条目](../by-type/info-secrets.md) |
| 私项目沟通应关联 ticket 且待支付不等已支付 | 完整回信说愿付up to250、要求PayPal信息，提醒ticket外沟通可能遗漏；正文称Open Redirect到StoredXSS私项目，未保存链。 | [方法条目](../reporting.md) |
| KYC 背景检查和 VDP 资格不是资产授权替代 | 正文建议完成KYC/背景检查、读规则、从VDP和旧报告开始；另有未回应/不支付但修复的个案说法，未有当前规则或证据。 | [方法条目](../scope-and-rules.md) |
| regex source 拼接与 cookie 弹框仍依赖 reader | 正文有regex.source组合事件调用、window括号属性和十六进制al\x65rt，Microsoft图弹框可辨MUID/MC1 GUID其余模糊，另仅RXSS Medium5.4状态。 | [方法条目](../by-type/xss.md) |
| LinkFinder 的 JS 文本 endpoint 与实际可达 API 分开 | 正文介绍从JavaScript提取endpoints及参数，没有输入JS、调用图或执行结果。 | [方法条目](../discovery/client-and-cloud.md) |
| strcmp 黑名单比 hostname 与连接 IP 会留下不同边界 | 完整演示slide画域名到169.254.169.254并写Bypassing strcmp，正文称读AWS metadata，但无DNS回应、实际抓取和字段。 | [方法条目](../by-type/ssrf.md) |
| 二十五项 XSS dork 图实际为 query 字段名 | 完整图列q/s/search/id/lang/keyword/page/year/email/type/name/month/immagine/url/key/begindate/enddate等25参数形状，未有搜索引擎语法或命中结果。 | [方法条目](../targeted-fuzzing.md) |
| DomainAlerting 日期文件行数不等新注册域覆盖 | 完整图有日期目录、domain-names.txt的wc-l计数与head三行，正文说按关键词每日注册提醒，没有注册权威数据、查询条件或通知。 | [方法条目](../discovery/records-and-incremental.md) |
| 回连 token 和自动探测要核真正产生者 | 正文称redirecturl回连带token/param0，完整图ngrok/Python HTTP日志出现一条含query的GET和.env/git/svn/robots等404；未有身份、token用途/权限或真实用户导航。 | [方法条目](../by-type/open-redirect.md) |
| 重置 URL 前缀接受须核解析后 hostname 与交付 | 完整文字故事给正常email/url重置链接、改google后host为空、再用target.com.evil.com被拼入邮件；未保存完整请求/邮件字节或新会话。 | [方法条目](../by-type/authn-session.md) |
| Go define template 是模板源码权限而非数据转义绕过 | 正文给define/T1/template与script字面量并称Go SSTI/XSS bypass，没有引擎、Parse/Execute调用或输出。 | [方法条目](../by-type/ssti.md) |
| ASP NET 重复参数的拼接分隔符决定解析结果 | 完整tip分两段同名parameter并声称ASP.NET/IIS无分隔拼成svg事件，没有HTTP/实际API或响应。 | [方法条目](../by-type/waf-bypass.md) |
| preg_replace delimiter 错误要分结果与两次消费者 | 完整训练图preg_replace提示No ending delimiter并显示源码：处理GET payload后进入JS name单引号，再拼到greeting.innerHTML。 | [方法条目](../by-type/xss.md) |
| JSON 字符串变对象只有代码消费者才会执行表达式 | 完整图是单引号/name/alert(document.domain)片段，正文称JSON string变object初始化执行，但没有语法上下文或eval/JSON.parse消费者。 | [方法条目](../by-type/xss.md) |
| test test 与 token secret 题目仍缺身份结果 | 正文称默认test/test与endpoint token-secret，完整图只有两个Medium标题，没有登录交换、端点字段或权限。 | [方法条目](../by-type/authn-session.md) |
| WordPress Editor 菜单缺失不等 PHP 功能被绕过 | 完整图对比WordPress4.9.9普通主题/插件Editor与所谓our application没有Editor，正文是disable_functions到remote shell文章标题，没有PHP配置、请求或shell结果。 | [方法条目](../source-audit.md) |
| Lnkbomb 创建 recovery 和 removed 日志不证明 NTLM 获取 | 完整图打印在网络share创建.url、生成.recovery并随后removed，没有文件hash/目录确认、读者打开、挑战响应或破解结果。 | [方法条目](../discovery/client-and-cloud.md) |
| X Client IP 回环字段要核代理信任边界 | 正文建议403增加X-Client-IP:127.0.0.1，无保存回应或网络身份。 | [方法条目](../by-type/idor-access-control.md) |
| Spotify UNION 与返回数据库字串仍需基线归属 | 完整BurpPOST adminajax图body含UNION ALL SELECT/from information_schema.schemata，响应track_streams类JSON末有sys/wordpress；未保存正常基线、身份/权限和任意查询范围。 | [方法条目](../by-type/sql-injection.md) |
| 单次双次跳转都必须重核最终目的地址 | 正文给一层PHP Location到回环和第二层再跳第一层，称同样可到元数据，没有实际抓取/重定向处理和结果。 | [方法条目](../by-type/ssrf.md) |
| WordPress 十二端点名不等可读配置或执行能力 | 正文列wp-includes目录、index、login、opml、activate、blog-header、cron、links、mail、xmlrpc、settings、trackback，未有请求、权限或输入消费者。 | [方法条目](../discovery/web-and-api.md) |
| 支持邮件 From 到 ticket 账号必须验证身份来源 | 完整图仅fake-mail composer的From victim、To support、plaintext、附件与Send按钮；正文称创建受害ticket和5000奖励，没有发送/交付/ticket或敏感动作。 | [方法条目](../by-type/authn-session.md) |
| 虚拟机破坏和 CTF 练习需明确要验证的不变量 | 正文主张新Linux VM动手至坏以及boot-to-root CTF可建立方法，没有实际问题、对照或验证产物。 | [方法条目](../experiment-design.md) |
| 子域 endpoint 参数三个阶段要保留关系和未知 | 正文给三类recon目标、SingleFile保存页资源与Osmedeus可组合基础的主张，没有具体采集结果/流程验证。 | [方法条目](../discovery/passive-and-services.md) |
| 拒绝表 accessible 与 acceptable 不是同一理由 | 正文抱怨2000报告website not acceptable/cannot reproduce；完整表实际Website is not accessible及Can't reproduce vulnerability，未有原始复现或资格政策。 | [方法条目](../reporting.md) |
| SCIM 创建响应不能直接继承 Host Header pre ATO 结论 | 保存正文称Host Header Injection导致preATO；图片可辨SCIM users POST携带不同Host并返回201及用户JSON。 | [方法条目](../by-type/host-header.md) |
| Dome active passive 解析命中要保留模式与 wildcard 边界 | Dome卡片本身没有实现；另一保存图可辨1.1版本、active模式50线程、resolvers和wildcard check，active/passive found域名IP列表。 | [方法条目](../discovery/passive-and-services.md) |

| Burp Sniper 单密码位置和 spray 会话基线分开 | 保存Burp图是wp-login POST、Sniper一个密码位置及现有Cookie/CSRF字段，正文另列spraying/session/revalidation/SSL主题；界面未开始运行。 | [方法条目](../targeted-fuzzing.md) |
| DirtyPipe 手机演示要核内核构建与有效 uid | 正文称Pixel6/S22受影响，但保存图只有手机和sh5.1提示，无可辨型号、内核构建、有效uid或完整步骤。 | [方法条目](../by-type/mobile-android.md) |
| X Client IP 回环线索要跟随入口与后端同资源 | 正文重复127.0.0.1头绕403提示，没有保存响应。 | [方法条目](../by-type/idor-access-control.md) |
| 自动属性 XSS 的 Collaborator token 不等账号接管 | 正文将HTML属性注入、无交互与criticalATO关联；图有DNS/HTTP交互及GET t参数，token大部遮蔽。 | [方法条目](../by-type/xss.md) |
| IDA 二进制补丁 UI 要绑定字节与重定位 | Patching图可辨call exit、地址和机器字节，保存正文只工具简介。 | [方法条目](../source-audit.md) |
| password 弱密码报告文字仍需真实认证身份 | 2500故事图写password和dashboard/projects及登录附件，但账号和URL遮蔽、未保存认证交换。 | [方法条目](../by-type/authn-session.md) |
| Git 敏感路径清单要分元文件和可恢复对象 | 清单包括gitHEAD/index/logs与gitattributes/gitkeep/modules/review、svnentries/ignore；它们敏感程度不同。 | [方法条目](../by-type/info-secrets.md) |
| WMEye 项目创建日志和横向执行分开 | 图可辨目标IP/用户名凭据输入、连接及ShellcodeProjectcreated日志，正文描述WMIEventFilter/MSBuild横向移动；缺远端实际执行或对象访问。 | [方法条目](../discovery/records-and-incremental.md) |
| innerText 写入文本不能代替所有上下文防护 | 正文建议innerText代替innerHTML且不要eval/newFunction，又将HTML编码表述为总能缓解。 | [方法条目](../by-type/xss.md) |
| Osmedeus 模块工具表不是各阶段成功回执 | 图列subdomain/probing/SSame/spider/fingerprint/sto/ipspace/vulnscan/portscan/dirbscan及各工具；另一图只有厂商logo。 | [方法条目](../discovery/records-and-incremental.md) |
| Git 删除 secret 文件仍需历史与撤销证据 | Git图说明提交删除后旧history仍可见、需要revoke/rotate，并用SolarWinds故事示意。 | [方法条目](../by-type/info-secrets.md) |
| CORS 读权限与 CSRF 状态修改是两个门 | 正文称攻击域带credentials可造成CSRF，但无保存浏览器请求或修改结果。 | [方法条目](../by-type/csrf.md) |
| 公司名反向 WHOIS 与版权模板需要独立归属证据 | PrettyRecon结果列域名/创建日期/registrar，菜单明示maynotowned；另一图建议copyright/disclaimer/favicon关联域。 | [方法条目](../discovery/passive-and-services.md) |
| Recon 小中范围流程须先约束 seeds 与账号 | 四图Before公司/范围/多账号/业务政策→After子域ASN服务目录，frameworkv2把ASN收购、证书、Git/JS、HTTP、端口与扫描连接；small指定域，medium宣称所有subs。 | [方法条目](../discovery/records-and-incremental.md) |
| HTTP 方法矩阵要保持对象与业务不变量 | 正文建议GETPOSTPUTDELETEPATCH和INVENTED，未有结果。 | [方法条目](../discovery/web-and-api.md) |
| Astra 检测类别介绍不证明 API 检查覆盖 | 正文列SQLi/XSS/CSRF/unlimitedusage/JWT，图片仅仓库卡。 | [方法条目](../targeted-fuzzing.md) |
| Form feed 原字节与推文替代点必须区别 | 正文明确0x0c且提醒•只是平台不能显示时的替代点；图只有JSFiddle封面。 | [方法条目](../by-type/waf-bypass.md) |
| SQL 候选管道的 sqli 文件名须一致 | 正文五步sublist3r→httpx→waybackurls→gf输出sqli，最后sqlmap读sqli.txt；输入文件已不一致，tee-a也混旧结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 改密码 token 检查不当必须落到服务端结果 | 正文称CSRF致ATO，图仅passwordchangeP3Triaged；未保存token检查或改密交换。 | [方法条目](../by-type/csrf.md) |
| Nmap verbose 发现行不能套用 grepable 格式解释 | 正文awk按Discoveredopenport取末字段和第四字段，图又描述-oG；这两种格式不能混作同一契约。 | [方法条目](../discovery/records-and-incremental.md) |
| visualRecon 固定 foo 目录与多源去重须可复核 | 图中mkdirfoo/cd、sublist3r输出subs、assetfinder追加、sort-u再probeaquatone；没有运行回执。 | [方法条目](../discovery/records-and-incremental.md) |
| svg on onload 图片只证明保存的有限浏览器现象 | 同源帖对比scriptblocked与svgononload弹domain，另有marqueeonstart/animateonbegin；图缺请求链、规则和版本。 | [方法条目](../by-type/waf-bypass.md) |
| freq 标签及 h1 字符串匹配要分反射和执行 | wayback→gf→uro→qsreplace→freq图有Vulnerable/Not标签；另一行把端口/协议/每等号改写后httpx匹配h1字符串。 | [方法条目](../by-type/xss.md) |
| 正常 signup 与 OAuth signup 需要同一身份状态比较 | 正文提醒两入口注册不同，图只有WeakRegistration150奖励。 | [方法条目](../by-type/oauth-oidc.md) |
| Censys 证书 names 查询要保留历史与租户关系 | 正文给services.tls.certificates.leaf_data.names查询并称更多子域，无保存结果。 | [方法条目](../discovery/passive-and-services.md) |
| 图片 filename 返回 passwd 字节与 MIME 标签分开 | 保存GETimagefilename点目录到passwd及200响应ContentTypeimagejpeg，正文外链只目录穿越标题；另一tpl请求也返回passwd文本。 | [方法条目](../by-type/lfi-path-traversal.md) |
| phpMyAdmin setup 空 servers UI 不足以定 critical | 图可辨setupoverview、noconfiguredservers和SaveLoadDelete按钮，没有版本、后端操作或DB权限。 | [方法条目](../discovery/web-and-api.md) |
| PHP 短标签绕过上传过滤仍受解释器条件约束 | 正文把正常php标签阻断、短标签放行称CloudflareRCE绕过，没有保存上传/执行响应。 | [方法条目](../by-type/file-upload.md) |
| 2FA 类别清单不等各入口共享验证边界 | 列bruteforce/OAuth/race/reset/response manipulation，未有具体流程。 | [方法条目](../by-type/authn-session.md) |
| 删除 API 路径租户段的 200 不等同一对象越权 | 多帖api数字users403变api双斜杠/反斜杠200，另列json、问号、斜杠、v2、accountdetail和OriginalURL。 | [方法条目](../by-type/idor-access-control.md) |
| S3 read write delete 标签需要各自对象回执 | S3Sec图只是三个标注bucket位置，没展示对象内容、写入或删除回应。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| JFScan 全端口结果的 403 标题不等业务授权 | JFScan1.0.3图有全端口、自定义resolver、10threads、nmapXML，几个80/443openOpenResty403及Cloudflare400；无整体结束状态。 | [方法条目](../discovery/passive-and-services.md) |
| JSON CSRF 的 simple complex 示例还缺语法和凭据条件 | simple图设置textplain却未withCredentials；complexapplicationjson设置withCredentials。 | [方法条目](../by-type/csrf.md) |
| O365 valid email 输出须有响应差异和归属 | Oh365UserFinder1.0.0列valid/invalid并称发现3个登录账号，未保存验证API交换。 | [方法条目](../by-type/authn-session.md) |
| Avatar deleteImage 的 JS id 消费者不能确证删除越权 | Avatarjs显示deleteAvatar把id放FormData、POSTUser/deleteImage、parseJSON和msg.success判分支；没有后端授权或删除结果。 | [方法条目](../by-type/idor-access-control.md) |
| 重置十三类清单要转为交付绑定与生命周期实验 | 图列rate/expiry/email/referer/token response/跨账号token/selfXSS/poisoning等，重复图片排版不同；无具体结果。 | [方法条目](../by-type/authn-session.md) |
| vaf fuzz 位置介绍与参数覆盖结果分开 | 正文只描述Nim跨平台fuzzer可URL/POST自定义wordlist，无运行日志。 | [方法条目](../targeted-fuzzing.md) |
| cdn proxy 建站副本不能继承生产 CDN WAF 结论 | 正文声称工具创建禁用CDN/WAF的目标副本，没保存实现或同站证据。 | [方法条目](../discovery/web-and-api.md) |
| VPS 与 wordlist 环境笔记不能预设内存总是瓶颈 | 保存笔记列Ubuntu2vCPU4GB/60GB、16GB笔记本、128GB桌面及下载旧工具词表；价格和主张仅历史。 | [方法条目](../experiment-design.md) |
| 短暂子域覆盖要记录来源时间和遗漏原因 | 正文批评单脚本/证书库遗漏短暂子域，提多scraping/brute/permutation/reverseSSL。 | [方法条目](../discovery/passive-and-services.md) |
| Intruder null payload 重发不证明请求并发重叠 | 正文建议nullpayload发送同请求测race，没有调度、时序或业务结果。 | [方法条目](../by-type/race-conditions.md) |
| Findsecret 正则目录要核分组语义与 secret 目的 | 图有JSON规则authbasic/bearer/HTTPuserpass/AWSclientid/keys/ARN/secret；部分前缀组合与字符类/组语义容易误配。 | [方法条目](../by-type/info-secrets.md) |
| signup 重定向后 CSV 候选与注册 PII 字节分开 | 正文signup→signup/→csvfuzz→signup/signup.csv称全部注册PII；图仅P1TriagedDuplicate。 | [方法条目](../by-type/info-secrets.md) |
| 重复 company_id 管理员添加须核实际 JSON 解析 | 图正常company_id自己、构造重复company_id另一值，声称添加admin即可storetakeover；没有HTTP请求、响应或角色结果。 | [方法条目](../by-type/api-property-pollution.md) |
| API mindmap 要把文档对象与实际消费端连接 | 图含版本v1v2v3、RESTSOAPGraphQL、WADLWSDL/公开文档、认证ID、比较文档、行为映射、objects/actions/端点和BurpPostmanSoapUIfuzz路径；小字保持限度。 | [方法条目](../discovery/web-and-api.md) |
| CSRF checklist 的双提交修改要核攻击者 cookie 控制 | 图列GETPOST、空缺token、同长变字、重用、decode、double submit cookie+param、跨账号token。 | [方法条目](../by-type/csrf.md) |
| 五十 seeds 的 validated 说法要展开验证谓词 | 日记称hunter.sh50seeds输出dedupvalidatedsubs并启动contentdiscovery，先最隐蔽seed；无实际结果。 | [方法条目](../discovery/records-and-incremental.md) |
| checkLink localhost 管道 id 返回须有执行因果 | 图可见checkLink的url编码localhost与管道id，200JSONstatuserror/message有uid0字符串；另一文章截图catIFS与回连passwd行。 | [方法条目](../by-type/cmd-injection-rce.md) |
| curl grep URL 提取不能代替 HTML 或 JS 解析 | 图输出有w3namespace、external库、截断CSS参数和目标URL，正文regex仅限定字符类。 | [方法条目](../discovery/records-and-incremental.md) |
| Actuator env 双斜杠 200 还需环境字段证据 | 正文单斜杠403/双斜杠200，图仅像素化env页面；不能读出密钥或用户。 | [方法条目](../by-type/idor-access-control.md) |
| phpPgAdmin 与 bash history 明文要分读暴露和登录能力 | 图phpPgAdmin显示postgres身份/测试DB，bashhistory可见psql连接用户名密码；缺未认证基线及因果登录交换。 | [方法条目](../by-type/info-secrets.md) |
| RFC diff errata 是实现假设来源而非漏洞证明 | 正文建议SecurityConsiderations、旧RFC、Rfcdiff和Errata，无具体规范差分。 | [方法条目](../source-audit.md) |
| 证据补充能改变影响判断但不能凭数据量升严重度 | 正文称足够数据/客户影响低可升高，另图有validhighesttier1000并请求invoice；三P2Unresolved各2500合7500。 | [方法条目](../reporting.md) |
| M1 Android Studio ARM 下载项不等测试环境就绪 | 保存图2021.1.1.22包列表含MacARM和hash，正文说M1配置困难；无安装或代理证据。 | [方法条目](../by-type/mobile-android.md) |
| staging 域 env 泄露到 production 的链须独立归属 | 正文水平recon→stg域→GitHubenv→developer凭据→production，无保存搜索/secret/登录交换。 | [方法条目](../by-type/info-secrets.md) |
| 多斜杠 next 要核解析后的实际导航 origin | 两个正文给next多斜杠evil字符串，没有实际Location或导航。 | [方法条目](../by-type/open-redirect.md) |
| manage admin 参数改变状态须核服务器赋权 | manage.php403→admin1参数200提示，无保存响应。 | [方法条目](../by-type/idor-access-control.md) |
| currency_code 改币种必须同时核价格与结算单位 | 正文USD300改PKR300称被扣更低价值，无保存订单/支付回执。 | [方法条目](../by-type/business-logic.md) |
| AD Explorer snapshot 对话框不证明完整图已导入 | 图snapshotpath空、throttle100%；正文描述解析给BloodHound和全对象NDJSON。 | [方法条目](../discovery/client-and-cloud.md) |
| Osmedeus cloud chunk 调度要有每片与合并回执 | 图4.0.3、63600行、chunk3、三instance、其中SSHrefused后日志继续running与UIreport；没有全部完成或合并。 | [方法条目](../discovery/records-and-incremental.md) |
| Amass 到 Nmap 仍需域输入和解析服务边界 | 正文一句quickscan所有发现子域，无图或运行结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 应用 DoS 类别要对应成本曲线和可恢复边界 | 图列长password/comment/uploadname、xmlrpcbrute、imagesize、cookiebomb/pixelflood、noratelimit/loadscript/cachepoisoning。 | [方法条目](../experiment-design.md) |
| IPv6 unspecified 与 loopback 不应混成同一绕过 | 两个正文列http[::]:80及未加括号0000::1:80，没有保存fetch结果。 | [方法条目](../by-type/ssrf.md) |
| DNS hierarchy 图需区别委派权与缓存解析 | 图root→TLD→zone举例，正文无查询。 | [方法条目](../discovery/passive-and-services.md) |
| Wayback 敏感 URL 历史版本与现有泄漏分开 | 两个正文把404config.js交waybackurls-getversions称可返回旧文件；图仅LowInfoDisclosure标签。 | [方法条目](../by-type/info-secrets.md) |
| 历史 url 参数筛选只定位潜在 fetcher | assetfinder→waybackurls→grepurl=被称五分钟SSRF，未有实现或交换。 | [方法条目](../by-type/ssrf.md) |
| 隐藏 Signup 的员工角色须独立验证邮箱与功能 | 保存图描述internalportal无signup链接，手改Signup用公司格式邮箱未验mail/admin可employee登入，列共享存储团队PII但admin失败。 | [方法条目](../by-type/authn-session.md) |
| register 页猜密主张要验证是否共享认证计数 | 图称login限速可去register猜密码，通常没保护；无实际请求/身份。 | [方法条目](../by-type/authn-session.md) |
| Spring routing expression 错误栈和计算器不能确证 RCE | 图本机POSTlocalhost带spring.cloud.function.routing-expression，返回500SpelEvaluationException，背景源码和已开calculator；正文是SPEL0day标题。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 文件尾分号斜杠要核 ACL 与 reader 路径一致 | 正文三项奖励并称semicolon/slash内容发现常有效，没有真实例子。 | [方法条目](../by-type/idor-access-control.md) |
| 引用 value 中实体解码不直接重开 HTML 标签 | 正文inputsearch的value含quot/lt/imggt，询问绕过；没有后续DOM消费者或执行。 | [方法条目](../by-type/xss.md) |
| composer lock 版本公开与可利用泄漏需分开 | 正文问为什么informative，图只是标题，没保存lockfile实际字段。 | [方法条目](../reporting.md) |
| Te Cl 错 chunk 六十秒延迟只能作为 desync 候选 | RequestSmuggler图打印possibleTeCl、wrongchunk60174ms对usual65ms，显示ContentLength/TransferEncoding转义文本；无原始连接复用/队列差异。 | [方法条目](../by-type/request-smuggling.md) |
| 弱 JWT hash 猜测与服务端签名政策分开 | 正文描述HashCat找hash后重新设计token即可authenticated，无token算法/验证响应。 | [方法条目](../by-type/jwt.md) |
| Collaborator ping 与内部扫描成功都需独立影响证据 | 正文回连后建议内网port/assets/file/LFI，另一帖称192168范围有效而localhost/rebind不行；图只P2Triaged。 | [方法条目](../by-type/ssrf.md) |
| Findomain ports NULL 和截图文件名不是内容检查 | 图列域IPURL端口或NULL及jpeg目录，正文仅集成能力和Discord推广。 | [方法条目](../discovery/records-and-incremental.md) |
| dnsgen anew 和 tee append 取决于记录身份定义 | 正文一律建议anew替tee-a，没有输入/版本/结果。 | [方法条目](../discovery/records-and-incremental.md) |
| Ostorlab 多 agent install scan 命令未到运行结果 | 图只多agentOpenVAS/Nmap/Tsunami/Nuclei和install/scan一个IP行，无输出；正文称可扩展分布式平台。 | [方法条目](../discovery/records-and-incremental.md) |
| Rivals follow 422 中用户字段与三百五十万泄漏分开 | Yahoo故事称350万，图实际followPOST422notallowed、body仍嵌user/phone/provider/认证metadata等多字段，部分请求身份遮蔽。 | [方法条目](../by-type/info-secrets.md) |
| unsubscribe 历史链接要核接收身份与订阅状态 | 正文邮件子域→Wayback称其他付费用户取消P3，图只TripAdvisorfooter。 | [方法条目](../by-type/business-logic.md) |
| 本地工具 help 文件与零检测标签须保留独立证据 | PSRansom图help描述加解密/C2key/plaintext，Shellcode图本机HelloWorldMessageBox，LsassDump图Administrator、dmpfile/Defenderenabled与0of26，Nimcrypt图下载行/旧定义。 | [方法条目](../experiment-design.md) |
| Microsoft seller users JSON 的角色字段不证明跨租户读权限 | 保存图partner站点GET seller路径users，响应含sellerId/email/roles/roleAssignments和部分principalId；大量Cookie遮蔽。 | [方法条目](../by-type/idor-access-control.md) |
| apiUrl 空响应与 DNS HTTP 回连必须追唯一产生者 | 保存图apiUrl含Collaborator地址、服务200但ContentLength0，旁列DNS/HTTP并显示AAA查询；未有内部内容。 | [方法条目](../by-type/ssrf.md) |

| 深挖与 recon 建议要匹配各自输入和停止条件 | 帖子提醒不同猎人方法有不同前提。 | [方法条目](../hunting-strategy.md) |
| 端口开放到 SMB 路径还需服务和权限链 | 波斯语正文与图片提出端口发现、识别服务、再调查 SMB，图片只课程海报。 | [方法条目](../discovery/passive-and-services.md) |
| Android 五项检查应分客户端入口与服务端状态 | 正文列导出 Activity、硬编码 token/password、SQLite 敏感数据、旧版本绕过和不失效 API 会话。 | [方法条目](../by-type/mobile-android.md) |
| 双斜杠和反斜杠 200 需要核同租户同对象 | 正文把 tenant users 403 与删去数字段、双斜杠或反斜杠的 200 比较，未保存完整响应。 | [方法条目](../by-type/idor-access-control.md) |
| 注册报错页泄露配置要逐字段确定秘密用途 | 注册截图实际是 Laravel 栈与环境配置，列数据库、邮件、Redis、AWS、JWT 和第三方字段，大部分值遮蔽；与正文内部域邮箱注册和用户名 XSS 是不同线索。 | [方法条目](../by-type/info-secrets.md) |
| Socid 页面标识提取的认证输入与输出分开 | 保存 help 列 URL、文件、cookies、cookie-jar、activation；工具声称支持 102 网站，但没有实际提取结果。 | [方法条目](../discovery/passive-and-services.md) |
| SQL 实验列表可以组织证据类型不能替代解题 | 图片可读 WHERE、登录、UNION 列数/文本/多值、数据库版本与内容、布尔/错误/时间、OOB 与外带等实验标题和 Solved。 | [方法条目](../by-type/sql-injection.md) |
| 反连演示的 loopback 身份只证明本地两端 | 保存图片是本地监听、127.0.0.1 连接与 whoami 输出 peter，正文仅反向 shell 生成器简介。 | [方法条目](../experiment-design.md) |
| 默认凭据候选须有产品部署和认证权限依据 | 正文分别提到 WordPress 用户名枚举、品牌默认密码及 RabbitMQ guest；截图有网络设备设置 UI，却没有默认凭据认证前后对照。 | [方法条目](../by-type/authn-session.md) |
| Jenkins 解密能力描述需区分输入材料和凭据验证 | 正文称工具支持旧/新密码格式、SecretBytes、用户 hash 与 token，未保存实现或可读输出。 | [方法条目](../by-type/info-secrets.md) |
| 人工 recon 日志要保留发现与待验证的状态差异 | 正文分别写百站中的少量候选、/api2/admin 数据线索，以及 Grafana 默认凭据、git 暴露与尚在调查的 SQL 参数；没有原始交换。 | [方法条目](../discovery/web-and-api.md) |
| Windows hosts 路径与 LFI 奖励标签分开保存 | 正文列 Windows hosts 路径变体，图片只 LFI 到系统文件、P1、未解决和奖励。 | [方法条目](../by-type/lfi-path-traversal.md) |
| CNAME 候选提取与原站 Host SNI 访问分阶段 | 图片命令从 httpx 403 中取主机，再 dig 短输出，输出中也混有 404、200、302；正文称原站绕过。 | [方法条目](../by-type/host-header.md) |
| OWASP Top 10 SAST 宣传需要对应规则与流分析 | 保存预览只描述 Insider 面向 OWASP Top 10，星数和贡献者不是检测证据。 | [方法条目](../source-audit.md) |
| SAML 插图中的断言响应与实际信任验证分开 | 三张图介绍多应用单点登录、XML 断言及浏览器中转 IdP/SP，最后画 SP 向 IdP 查询验证；它是概念示意，不是每个 SAML 部署固定在线回查步骤。 | [方法条目](../by-type/authn-session.md) |
| 报告 API 中 weakness ID 与模拟提交需可追溯 | 图片补充了模板 Markdown 疑问、模拟报告无法删除，以及通过网站过滤 URL 找 weakness ID 的历史经验。 | [方法条目](../discovery/records-and-incremental.md) |
| Spring routing expression 与 Framework 绑定漏洞独立核验 | 本批混称 SpringShell、Core 和 Cloud Connector；图片实际有 Function 3.1.6 routing-expression、500 后本机标记文件出现、只请求无响应，以及另一些 JSP/目录输出。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 404 与 takeover 接受邮件仍需独立可接管条件 | 正文称 11 个模板命中或建议检查 404；图片只接受邮件。 | [方法条目](../by-type/subdomain-takeover.md) |
| SSRF 搜索截图中的路径变体和 bearer 转发需逐跳追踪 | 图片实际显示历史帖子：/adminapi/ 与 /adminapi、追加邮件样式域的 URL、声称 https SSRF 泄 bearer，另有只能访问外部的 SSRF；正文只推荐搜索词。 | [方法条目](../by-type/ssrf.md) |
| 清单中的低优先级类型仍要转成可证伪假设 | 正文提醒 CSRF 等检查，另一图列 CORS、Host、SMTP、点击劫持、越权、SSRF、XSS、SSO state、限流等，并混入大量 cookie DoS 建议。 | [方法条目](../hunting-strategy.md) |
| GlobalProtect 历史 CVE 标题与处置变化不等 PoC | 正文用登录路径、Shodan 字段和版本描述，图片出现 Not applicable、Triaged、Duplicate、Unresolved 及不同年份 CVE 标题。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 手机号验证奖励文字只提供时序攻击方向 | 图片邮件称手机号验证绕过难以核验、涉及 timing attack、升级 P2 并邀请复测，没有并发请求或验证状态。 | [方法条目](../by-type/race-conditions.md) |
| 修复复测应绑定同一报告和新增根因 | 正文称复测时发现新问题，图只两笔奖励。 | [方法条目](../reporting.md) |
| gau qsreplace 打印回连候选并未触发 SSRF | 正文流水线到替换 URL 参数后结束，没有发出最终请求的阶段；大量线程和统一替换也抹掉参数上下文。 | [方法条目](../by-type/ssrf.md) |
| 图片渲染和 KYC 管理员 XSS 需要实际读者链 | 正文有图片渲染、KYC 总会成功和 XSS 到管理员凭据说法；图片只文章标题、状态、管理员 XSS 标题及回复认可，没有真实 source/sink 或认证消费者。 | [方法条目](../by-type/xss.md) |
| 路径引号与块注释片段应保留编码和消费者 | 一图地址栏含编码 script 与弹窗，另一图是带引号、alert、块注释和编码空格的 GET 路径，未保存对应 HTML/JavaScript 源。 | [方法条目](../by-type/xss.md) |
| Shodan 登录线索到 sqlmap 导出缺独立基线 | 重复正文给证书/employee portal 搜索与高风险 sqlmap 数据枚举命令，未保存实际请求或结果。 | [方法条目](../by-type/sql-injection.md) |
| Smap 服务表中的 open 来自历史索引需要注明 | 图片 Smap 以 Nmap 样式打印端口和版本，正文说明它使用 Shodan，另一图只是 Nmap/Shodan 标签。 | [方法条目](../discovery/passive-and-services.md) |
| 信息泄露实验标题提供五类分支检查 | 图片列错误信息、debug 页、备份源码、信息泄露中的认证绕过和版本历史。 | [方法条目](../by-type/info-secrets.md) |
| 登录 JSON 多字段不证明全部用户 PII 可读 | 图片可读 login 路径和 city、电话字段名、role、用户 ID、账户状态与课程信息，大部标识遮蔽，未显示换对象基线。 | [方法条目](../by-type/info-secrets.md) |
| JS 路径正则的输入格式和同文件 tee 风险 | 图片补足两种方法：第一条从历史 URL 文本匹配 src、强制 https、忽略 TLS 后解析响应；第二条 grep JS.txt 再 tee JS.txt。 | [方法条目](../discovery/client-and-cloud.md) |
| 穿越实验列表的六类解析边界分开 | 图片实际列普通穿越、绝对路径、非递归剥离、多余 URL 解码、前缀校验与 null byte 扩展名校验。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Autocomplete off 讽刺文章不能成为 critical 依据 | 正文明确讽刺并建议不报告，不能把标题 CRITICAL 当漏洞评级。 | [方法条目](../impact-and-acceptance.md) |
| 枚举提供者配置与历史发布能力需要分开统计 | 正文是 Findomain 历史版本的 PG TLS/no-discover 与 Amass 部分 API、付费密钥经验。 | [方法条目](../discovery/records-and-incremental.md) |
| Unicode 域名显示长度与实际 ASCII 主机须分开 | 正文称 Unicode 域名可成为两三个 ASCII 字母，未给字符串实例。 | [方法条目](../by-type/host-header.md) |
| AutoElevate SYSTEM 图必须保留已有管理员前提 | 正文说 ADMIN 到 SYSTEM，图有最初有限权限表、工具行、Administrator 窗口和 nt authority system。 | [方法条目](../experiment-design.md) |
| 席位许可竞争标题未提供资源耗尽过程 | 图片只有 High Race Condition Ending User License Available Seats 邮件标题。 | [方法条目](../by-type/race-conditions.md) |
| 终止卡住的子工具不应默记扫描完成 | 正文建议用进程工具终止卡住的模块以继续框架，未提供运行日志。 | [方法条目](../discovery/records-and-incremental.md) |
| FINAPI Android 凭据标题和银行元数据不能互证 | 正文是 plaintext OAuth credentials 标题，图片实际仅 banks JSON、supportedDataSources、location、test/support 标志和时间。 | [方法条目](../by-type/info-secrets.md) |
| httpx 标题技术栈视图是入口筛选不是漏洞验证 | 图片明确给 title、tech detection、status、server 概览，正文只是 200 的比喻。 | [方法条目](../discovery/web-and-api.md) |
| Subdomains wrapper 开关需要逐阶段覆盖状态 | help 可读 passive sources、semi-active、字典、置换、DNS、reverse DNS、active 与 setup 开关。 | [方法条目](../discovery/records-and-incremental.md) |
| Electron 内容加载与支付 postMessage 标题须追权限消费者 | 正文只不安全加载和 DOM/postMessage XSS 标题，未保存处理代码或窗口配置。 | [方法条目](../by-type/xss.md) |
| Jeeves 延时参数与五秒十秒 payload 不一致需核实 | 本批有 sleep5 配 payload-time10、sleep10 配10，以及称 time-based 却不含明显延时表达式的字符表；无测量响应。 | [方法条目](../by-type/sql-injection.md) |
| 公司邮箱来源可作出处线索不等账户授权 | 正文建议查看 hunter.io 邮箱来源，没有具体证据。 | [方法条目](../discovery/passive-and-services.md) |
| 重置邮件头污染必须把请求账户与 token 主体对齐 | 正文从自己的邮箱发请求，改 Host/Referer/Origin，却声称受害者收到邮件点击后泄 token；图片只有 ATO 复测奖励与关闭状态。 | [方法条目](../by-type/host-header.md) |
| Service Bus 队列传输示意不证明 Azure 授权漏洞 | 图片实际是 CobaltBus server/client、入出队列、专属 beacon 队列和 named pipe/目标进程，正文仅 C2 工具说明。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 伪 TCP 与 ICMP 传输图应限定网络与证据阶段 | Phantun 图有 UDP→伪 TCP、TUN、SNAT/DNAT 和 conntrack；ICMP 图只有 staging/下载命令及脚本名，没有接收字节。 | [方法条目](../discovery/passive-and-services.md) |
| 存档 join 链接和私人笔记需要能力 token 生命周期 | 图片实际报告文字称存档项目 join 链接与用户笔记，另两图是奖励/状态；未保留真正授权交换。 | [方法条目](../by-type/authn-session.md) |
| airixss stdout 确认须追实际浏览器解析 | 正文历史 URL→gf→uro→httpx→替换 SVG→工具 grep 标签，没有 DOM 与执行记录。 | [方法条目](../by-type/xss.md) |
| 历史 redactor 补丁线索应绑定提交和漏洞消费者 | 正文描述 GitLab reference_redactor 补丁、过去复现和 bypass，未保存 diff 或实际结果。 | [方法条目](../source-audit.md) |
| Prometheus 路径标签应去聚合并保留敏感范围 | 两张图片有 path、status_code、le bucket、count/sum 等重复指标，路径包括 CI、phpMyAdmin、debugbar、query；正文还提 kubemetrics。 | [方法条目](../discovery/web-and-api.md) |
| 现场采集 UI 应保留案件元信息与采集项目清单 | Live Forensicator 图有案件号、地点、设备描述、输出目录以及网络、账号、程序、系统、进程任务的 Gathering 行。 | [方法条目](../discovery/records-and-incremental.md) |
| RCE 参数清单只有八个名字不能补成二十五个 | 正文标题声称 25 参数但保存正文只有 cmd、exec、command、execute、ping、query、jump、code。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 取证 artifact 文件名列表不等实际解析覆盖 | 图片列 antivirus、cloud_services、config_files、containerd、docker、file_systems、hadoop、java、kubernetes、linux、macos、shell 等 YAML 文件名，没有内容。 | [方法条目](../discovery/records-and-incremental.md) |
| admin true 的发现故事缺服务端角色变化证据 | 正文从历史 admin dork、blackadmin.php 到 admin=true 声称面板可用，没有原请求/身份响应。 | [方法条目](../by-type/idor-access-control.md) |
| HaxUnit 图中串联工具需留阶段来源与范围门槛 | 三个不同 hash 图片展示 Sonar 跨 TLD、DNS 字典/解析、subfinder、gau、反向 DNS、Shodan、naabu、httpx 再到 nuclei/Acunetix。 | [方法条目](../discovery/records-and-incremental.md) |
| X Forwarded For 回环头的缓存 200 不是权限绕过证明 | 图片请求含 127.0.0.1，响应 200 JSON 且 public cache、X-Cache HIT，未保存不带头的同对象对照。 | [方法条目](../by-type/idor-access-control.md) |
| TruffleHog 主动验证宣传不意味着没有误报 | 正文一项描述能力，另一项说主动验证就无 FP，未保存 credential 类型、实际请求或结果。 | [方法条目](../by-type/info-secrets.md) |
| 证书后缀索引与军方地址没有测试许可关系 | 正文给含 .mil 的 Shodan 搜索描述，没有实际资产或授权证据。 | [方法条目](../scope-and-rules.md) |
| 代理导入与响应归档要保留身份和时间版本 | 正文半段建议把子域导入 Burp，另一帖请求历史 HTTP 响应；没有后续步骤或新 SSRF 实现。 | [方法条目](../discovery/records-and-incremental.md) |
| 邮箱确认链接未绑定发起账户可更新点击者账户 | 图片保存了完整叙述与步骤：A 在自己账户发起邮箱改到 C，链接送达 C，却在 B 已登录上下文消费时改变 B 的邮箱；原因是 token 未绑定账户。 | [方法条目](../by-type/authn-session.md) |
| 多语言备份词表须保留语言和具体文件角色 | 正文列 db/database、德语 datenbank、西语/法语/葡语变体和压缩扩展名。 | [方法条目](../targeted-fuzzing.md) |
| 二级跳转 query 传播需要每跳实际 Location | 正文描述 company 把 query 带到第三方，再借第三方 open redirect 到控制域，示例域拼写也不一致。 | [方法条目](../by-type/open-redirect.md) |
| 参数污染到授权码泄露标题应分三条信任边 | 正文只有 pollution→redirect→OAuth code 的文章标题，没有参数顺序或消费者。 | [方法条目](../by-type/oauth-oidc.md) |
| 计划任务工具 help 的 create run delete 不是无权横移 | 两幅 help 列 create/delete/run/query/queryfolders/move、远程主机、用户名与不同触发条件；move 说明会自动建、运行、删除。 | [方法条目](../discovery/records-and-incremental.md) |
| KNX 硬件接线图与总线数据解码证据分开 | 图片实际标出 Raspberry Pi、KNX Pi HAT、USB adapter、电源、变压器、执行器和传感器，正文称导出 Wireshark 兼容数据。 | [方法条目](../discovery/passive-and-services.md) |
| 版本发布卡的 vuln 更新 flag 不能推全部扫描重跑 | 正文与图片是 Osmedeus 4.1.0 重构和更新 flag，图片说明截断于 only。 | [方法条目](../discovery/records-and-incremental.md) |
| Informative 仍可获酌情奖励不能反推评级改变 | 图片邮件明确奖励来自报告澄清和研究努力且不能保证经常如此，另图仍 Informative、None0.0、50 bounty。 | [方法条目](../impact-and-acceptance.md) |
| 老目标发现故事只影响调查优先级不证明具体入口 | 正文称许多发现来自旧目标及计划介绍任意用户登录，未保存后续链。 | [方法条目](../hunting-strategy.md) |
| HCL threat model 交互图的资产分类要连接安全边界 | 图片交互可读项目范围、名称、链接、负责人、是否面向 Internet、规模、资产分类与 use case，输出仍在输入中。 | [方法条目](../business-modeling.md) |
| origin 相等检查后的 innerHTML 仍须验证消息主体 | 图片代码实际为 onmessage、读取 e.data、严格比较 e.origin 与 window.origin，然后 render 类型直接赋 innerHTML。 | [方法条目](../by-type/xss.md) |
| Lambda URL OOB listener 标题只说明观测服务方向 | 正文称 Lambda function URL 与通知服务，外链实现未保存。 | [方法条目](../by-type/ssrf.md) |
| 入门路线图的基础学习与有效发现需分阶段 | 仅标签正文的图片实际列网络端口/协议/握手、Linux 权限、编程、HTML/CSS/JavaScript、漏洞类型和记录/搜索。 | [方法条目](../hunting-strategy.md) |
| 新增范围域名应以范围快照和历史去重对齐 | 正文建议关注项目新域名，图片只是第三方 token 泄露奖励。 | [方法条目](../discovery/records-and-incremental.md) |
| CVE PoC 索引名称需绑定公告和实现 provenance | 正文只 find-gh-poc 工具简介与 GitHub 链接，无保存代码。 | [方法条目](../source-audit.md) |
| 隐藏文件内核模块生成 help 未给模块生效证明 | 图片 Casper-Fs help 描述 YAML rules、隐藏和读写删除保护，并显示缺少 rules 参数错误。 | [方法条目](../source-audit.md) |
| OWASP 年份分类迁移图不能作为当前风险排名 | 图片是 2017 到 2021 分类对应，新列 insecure design、software/data integrity 和 SSRF，未给实际漏洞。 | [方法条目](../expert-reasoning.md) |
| 访问控制实验标题提供角色对象动作三轴 | 图片列隐藏后台、角色/用户 ID 参数、个人资料修改、重定向数据、密码字段、IDOR、URL/方法/多步/Referer 检查。 | [方法条目](../by-type/idor-access-control.md) |
| Recon 证书的训练范围可记但不替实际覆盖 | 证书文字列目录/虚拟主机、DNS 与 git 信息检索挑战，正文称徽章完成。 | [方法条目](../hunting-strategy.md) |

| 复制开发代码后的权限差异要追服务端消费者 | 正文从开发者复制代码推测多个入口会共享 broken ACL，配图仅报告状态。 | [方法条目](../by-type/idor-access-control.md) |
| Spring4Shell 检查器的 400 只能提示绑定路径 | 图片保存对 class.module.classLoader.URLs 索引的请求及把 HTTP 400 标为 vulnerable 的脚本，背景有绑定异常。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Jhaddix recon 图的公司种子需要归属核验 | 完整图从收购、ASN、反向 WHOIS、证书及页面/JS 链接扩展种子，再枚举、变形、解析子域。 | [方法条目](../discovery/passive-and-services.md) |
| Recon 流程中的探测和口令尝试应各有入口条件 | Jhaddix 图同时列出端口、服务识别、截图、接管检测与 Brutespray。 | [方法条目](../targeted-fuzzing.md) |
| 自动化 recon 的合并节点要记录阶段产物 | Jhaddix 提到 Interlace/自动化；Trickest 示意图显示两枚举器合并后交给 httprobe；机器人截图按子域、Wayback、KXSS 宣告完成并发布报告地址。 | [方法条目](../discovery/records-and-incremental.md) |
| 请求速率与奖金说明不能替代账户影响证据 | 奖励邮件可见每秒请求、服务器响应及可能导致暴力尝试的说明，其余细节遮挡。 | [方法条目](../experiment-design.md) |
| 极短 PHP shell 仍依赖解释器和执行上下文 | 正文保存短 echo 标签与反引号消费 GET 输入的 PHP 片段。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Linux 速查表要区分观察与环境修改 | 图片混列目录/文件、进程、网络、压缩和权限命令，也含根目录删除的玩笑说明。 | [方法条目](../source-audit.md) |
| HTTP pipeline 的时序线索要排除队列与连接混杂 | 中文正文谈非 HTTP/2 的 pipeline 用于放大时序信号，没有保存完整请求或测量。 | [方法条目](../experiment-design.md) |
| DOM Invader canary 应串起 source 到 sink | 图片给出 Chromium 中开启 DOM Invader、更新 canary、遍历功能、查看反射和 source/sink 的流程。 | [方法条目](../by-type/xss.md) |
| HTML 注释提取先确认工具究竟消费什么输入 | 正文和图片保存 URLs.txt 接 html-tool comments 再用正则抽取 URL 的管道，提到注释中 endpoint、参数或凭据。 | [方法条目](../discovery/web-and-api.md) |
| 页面所有链接依赖静态源码与动态 DOM 的边界 | 正文列 Chromium 扩展与 FindAllLinks 脚本，没有保存其实现。 | [方法条目](../discovery/client-and-cloud.md) |
| 创造性和系统化要落实为可证伪假设 | 正文强调 creative、systemizing、persistence、ethics；另帖称任意程序短期内必有漏洞。 | [方法条目](../hunting-strategy.md) |
| 重复 Host 的解析异常仍需密码重置消费者链 | 正文把两个带 http:// 的 Host 字段作为重置接管技巧，没有保存生成邮件或 token 兑换。 | [方法条目](../by-type/host-header.md) |
| RapidDNS 与 Uncover 输出应保留查询来源和格式 | RapidDNS 截图有缺参数错误及子域名称输出；Uncover 截图用多个搜索引擎得到带提供方标签的 IP:port。 | [方法条目](../discovery/passive-and-services.md) |
| 筛选 JavaScript URL 要保留查询和结构化响应 | 正文先用 gau 与 .js 结尾过滤，再以 200 和 application/javascript 选择结果。 | [方法条目](../discovery/client-and-cloud.md) |
| JS 链接管道不能把 URL 当成本地文件名 | 保存脚本逐行读取输入后执行 cat $line，再 grep 引号中的路径并写 manyjslink.txt。 | [方法条目](../discovery/client-and-cloud.md) |
| 定制 wordlist 应保留词语的页面和参数上下文 | 文字把带 scheme 的输入交给 subfinder，图片用裸域名；管道通过 httpx/hakrawler 和分隔符拆词。 | [方法条目](../targeted-fuzzing.md) |
| 头像 UID 的对象越权与属性绑定需要分别证明 | 正文建议把头像请求 parent uid 换成另一用户，再通过加参数寻找 mass assignment，没有保存完整交换。 | [方法条目](../by-type/idor-access-control.md) |
| Secret 检测器数量与 P1 宣传都不决定实际权限 | 正文把大量 TruffleHog 检测器和 P1 联系起来；另组以 password 与多厂商品牌组合成搜索 dork。 | [方法条目](../by-type/info-secrets.md) |
| 用户编辑的 XSS、CSRF 与认证缺失要分别建模 | 正文描述管理用户编辑参数、unsanitized 与 unauthenticated crafted web request，混列 XSS/CSRF，没有保存请求。 | [方法条目](../by-type/authn-session.md) |
| Base64 文件下载证据不能改称云 SSRF | 图片保存 download 路径中标注为 Base64 的文件名及 attachment filename=passwd 的文件内容，正文外链标题谈云 SSRF。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 重置邮件头中的发送 IP 不保证是 Web 源站 | 图建议从重置邮件取发送源 IP，再访问该 IP 并声称绕过所有 WAF。 | [方法条目](../discovery/passive-and-services.md) |
| 旧 APK 的接口线索需与服务端当前入口对照 | 图用旧/新版客户端是否含 login_insecure 说明移除前端入口后后端可能仍在。 | [方法条目](../by-type/mobile-android.md) |
| 漏洞大图应按边界检索而非套用全部标签 | 完整思维图混列服务器配置、注入、认证/会话、敏感数据、CSRF、访问控制、XSS、密码学，以及移动存储/传输、硬化和隐私。 | [方法条目](../expert-reasoning.md) |
| Linux LFI 路径表要匹配实际进程的文件权限 | 图片列 /etc 配置、/proc 信息、日志及用户点文件；正文另表有 /etc/passed 和 /var/spool/crony 等拼写。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 历史 VDP 规则截图只说明当时的约束 | 图中 VDP 规则限定不伤害、不扰乱、不泄露非公开数据、测试自有或有许可账号，并要求及时报告且不继续利用。 | [方法条目](../scope-and-rules.md) |
| 多斜杠 traversal 要区分观察到的文件字节与 Nginx 根因 | 截图确实显示多斜杠/父目录片段的请求与 passwd 风格响应，正文归因于 mergeslash。 | [方法条目](../by-type/lfi-path-traversal.md) |
| LDAPShell 的名称不能代替目录 ACL 利用链 | 正文介绍 AD ACL abuse 工具，三组图片仅同类装饰图，没有目录请求或 ACL 结果。 | [方法条目](../by-type/ldap-xpath.md) |
| 接管拒绝中的关键问题是可声明性 | 反馈可见报告被拒绝，因为研究者不能成功 claimed；后来接受邮件的具体原因遮挡。 | [方法条目](../by-type/subdomain-takeover.md) |
| 可预测 ID 和增加参数只是候选对象线索 | 正文列 profile/reset/folder ID、数字 ID 和对随机参数加一的技巧。 | [方法条目](../by-type/idor-access-control.md) |
| OOB 回调之后不能直接推出内部文件读取 | 重复帖建议回调 ping 后做内部端口、资产和文件；另一图用 SVG 参数、httpx 和截图自动找 SSRF。 | [方法条目](../by-type/ssrf.md) |
| 代理路径返回外部页面还需确定取回主体 | 正文把 WCM proxy 的 500 改成外部主机后 200；配图浏览器 URL 下能看到外部页面内容。 | [方法条目](../by-type/ssrf.md) |
| Flutter TLS 验证源码不是 pinning 绕过完成证据 | 图片展示证书链存在性、verify store、主机名及 verify callback 设置的源码，正文提到 Ghidra 修改二进制。 | [方法条目](../by-type/mobile-android.md) |
| 公开员工数据索引不是已暴露的秘密或入侵许可 | 正文宣称 Insiders 为多家公司的员工资料归档，图只有仓库预览。 | [方法条目](../discovery/client-and-cloud.md) |
| Dismap 的协议响应里可能已经包含拒绝信息 | 两张图显示 NBNS、SMB/RDP、HTTP/Tomcat/WebLogic 指纹，同时 Redis 为 protected mode 拒绝、MySQL 不允许该来源连接。 | [方法条目](../discovery/passive-and-services.md) |
| Resend SMS 的 DELETE 差异需核二次认证状态 | 正文声称把重发 SMS 的 POST 换 DELETE 就能禁用 2FA，没有保存完整交换。 | [方法条目](../by-type/authn-session.md) |
| LFI 管道的 root:x 字符串需要文件消费者对照 | 保存一行从 URL 归档/gf/参数替换到并行 curl，以 grep root:x 就输出 VULN 的流程。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 扫描器清单应映射到可观察检查能力 | 正文按 web、infra、CMS、API、specialized 列工具；另组写代理/枚举/nmap 多 agent 安装命令。 | [方法条目](../targeted-fuzzing.md) |
| 损坏社交链接与可控品牌入口要分步核验 | 正文把 SocialHunter 的 broken links 与 profile hijack 联系，没有保存声明过程。 | [方法条目](../by-type/subdomain-takeover.md) |
| 能做什么应回答已观察的受限状态 | 正文提醒发现问题后应问能造成何种影响；奖励金额争议与 triage 状态图没有补充技术链。 | [方法条目](../impact-and-acceptance.md) |
| POST 换 GET 的反射需核 handler 和执行位置 | 正文称 signup 的 productID 在 POST 被阻挡，改 GET 后出现反射型 XSS，没有保存完整页面。 | [方法条目](../by-type/xss.md) |
| 模板字面量和图片事件片段仍受最终语法约束 | 正文建议转义/模板字面量绕过括号，截图显示 redirect 参数与页面中直接显示的 image/onmouseover 字符串。 | [方法条目](../by-type/xss.md) |
| 历史 URL grep 的命中要解析回具体字段 | 正文替代文字与图保存 admin/login/staging、多个扩展和 env 等 grep，再写入 interesting_paths_exts.txt。 | [方法条目](../discovery/records-and-incremental.md) |
| 公开搜索 dork 和无奖励投稿都不等于测试许可 | 正文给 .mil 注册查询，也建议没有 program 时一律报告到 contact us。 | [方法条目](../scope-and-rules.md) |
| XSS 一行管道的过滤器同时定义了遗漏范围 | 两组正文及图片串 Wayback/anew/等号筛选/gf/nilo/gxss/dalfox，并跳过 DOM mining、若干检查及 302/404/403。 | [方法条目](../by-type/xss.md) |
| 改响应 isAdmin 与添加朋友按钮都需独立状态核验 | 正文以 isAdmin false→true 说明访问控制；反馈截图指出改响应后按钮出现，但刷新后消失、没有真正成为朋友。 | [方法条目](../by-type/authn-session.md) |
| Android 抓到 HTTPS 请求要说明代理和信任条件 | M1 模拟器截图显示应用登录与 Burp 截获的 HTTP/2 表单请求，但没有响应或配置细节。 | [方法条目](../discovery/client-and-cloud.md) |
| Burp 编解码扩展要区分初始与最后处理阶段 | 完整图显示请求/响应进入多个扩展、编辑器、Logger 和网络前后的顺序，processHttpMessage、processProxyMessage 及 first/last extension 各有位置。 | [方法条目](../source-audit.md) |
| Forgot password 的数字参数尚不是账户接管 | 图片显示 forgotPassword 的 admNoVal 查询参数和 Cookie；另一组仅个人资料页面，没有返回或兑换结果。 | [方法条目](../by-type/authn-session.md) |
| Web 传感器图表计数不能替代漏洞实例 | 两张 Melody 图呈现来源/语言/HTTP 等计数与 payload 排名，细节有缩小限制，没有目标的业务状态。 | [方法条目](../discovery/records-and-incremental.md) |
| DumpXSS 的 Found 输出仍需浏览器执行证据 | 终端图有 XSS Found 与含 image/onerror 的 URL，报告列表只是 rXSS 标题；正文强调输入文件和输出功能。 | [方法条目](../by-type/xss.md) |
| Origin null 不是单一可信来源的身份 | 正文建议 data 协议制造 Origin null 来绕过 CSRF 校验。 | [方法条目](../by-type/csrf.md) |
| HTTPS FUZZ 端口模板只覆盖其协议假设 | 正文用 1..65535 接 ffuf 的 HTTPS target:FUZZ，把输出当成端口扫描。 | [方法条目](../discovery/passive-and-services.md) |
| 注入分类必须说明语言、解析器和执行 sink | 正文混列 SQL、XML、OS、SSTI，以及 DOM-based SQL/XPath/JSON、SSL Injection 等名称。 | [方法条目](../expert-reasoning.md) |
| phpinfo 候选要确认正文而不是只有 200 | 正文把带 scheme 的地址给 subfinder，httpx 请求 info.php 并只筛 200。 | [方法条目](../by-type/info-secrets.md) |
| 扫描器 localhost 的归属取决于执行主体 | 正文主张任何扫描范围始终包含 127.0.0.1。 | [方法条目](../scope-and-rules.md) |
| 重置 JSON 的 Url 参数需追链接到 token 绑定 | 正文保存 email 与 Url 字段并称可接管，没有生成邮件或兑换结果。 | [方法条目](../by-type/host-header.md) |
| HTTP 状态速查表不提供权限或完成状态证明 | 图片有常见状态列表，其中把 306 写成 Switch Proxy。 | [方法条目](../experiment-design.md) |
| 公司 recon 图应保存不同类型的关联边 | 图从 Company 分 CIDR 和 Domains，经子域、DNS、指纹、内容、JS；IP 再关联端口、ASN 和 GeoIP。 | [方法条目](../discovery/passive-and-services.md) |
| AD CS 模板 ACL 的单条属性写权需限定效果 | 截图为 cert template ACL，圈出 Domain Users 对 ms-PKI-OID-User-Notice 的 WriteProperty，其他可见项有 Enrollment 等权限。 | [方法条目](../by-type/ldap-xpath.md) |
| 数字实体 SVG 事件片段要核最终解析与事件 | 正文称 SVG/onmouseover 中数字实体编码绕过 Cloudflare，没有保存防护版本或执行结果。 | [方法条目](../by-type/waf-bypass.md) |
| Findomain 告警邮件的 severity 仍是工具标签 | 正文列端口、截图、DNS/fuzz 和通知功能；两封图只有 nuclei high/low/critical 提示与未发现变形子域说明。 | [方法条目](../discovery/records-and-incremental.md) |
| SSH 速查表需区分连接、复制与配置生效 | 图列 ssh/scp、服务启停、密钥生成/发送及 sshd 配置，含端口、认证、MaxStartups/MaxAuthTries/MaxSessions 等项。 | [方法条目](../source-audit.md) |
| HRS 写入 Cookie 的 ATO 主张需要队列和身份链 | 正文说 HTTP request smuggling 可把 cookies 写进评论导致 mass ATO，图只有标题和 P2 Unresolved。 | [方法条目](../by-type/request-smuggling.md) |
| 加载器 help 与防护状态图不证明 EDR 绕过 | Shhhloader 图片仅 CLI 参数说明；EDRSandblast 图片仅 Windows 系统信息中的 VBS/Credential Guard/完整性状态。 | [方法条目](../by-type/desktop-client.md) |
| Prototype pollution 到 XSS 或 RCE 需要具体 gadget | 正文比较 prototype pollution 与 XSS/RCE 难度，没有对象流或样本。 | [方法条目](../by-type/api-property-pollution.md) |
| Weird ERC20 目录只能提示核验合约交互假设 | 正文推荐历史 ERC20 示例仓库，但没有保存合约实现或测试。 | [方法条目](../by-type/smart-contract.md) |
| ATO 技术名称清单要连接到认证消费者 | 正文列 CSRF、XSS、IDOR、OAuth、secrets、逻辑、smuggling、Host 等，末尾 CRLF 字样截断。 | [方法条目](../by-type/authn-session.md) |
| SQL 自动化管道必须绑定同一个候选产物 | 正文把 gf sqli 输出存为 sqli，却从 sqli.txt 读入另一工具。 | [方法条目](../by-type/sql-injection.md) |
| Self stored XSS 嵌入 file iframe 不自动成为 LFI | 正文建议从 self stored XSS 引入本地 passwd iframe 来升级 LFI，没有保存渲染结果。 | [方法条目](../by-type/document-rendering.md) |
| 7zip 帮助交互的提权标题仍缺权限前后对照 | 正文称 Windows 7zip 21.07 拖放到帮助窗口可提权，外链全文未保存。 | [方法条目](../by-type/desktop-client.md) |
| Shodan 产品版本命中不等于受影响构建 | 两张图从 nginx 产品查询缩小到版本，正文推荐进一步查 CVE。 | [方法条目](../discovery/passive-and-services.md) |
| 子域扫描二十秒的主张要分速度与有效覆盖 | 正文声称一千子域很快完成，图只保存域名列表，没有测量区间或解析结果。 | [方法条目](../experiment-design.md) |
| 证书域名递归扩展需去重和限制关联跳数 | 图示从子域收集 TLS 证书名称，再对新域名重复查询，形成多跳关联图。 | [方法条目](../discovery/passive-and-services.md) |

| 从 GitHub 线索到数据库界面需保留权限链 | 正文称 recon、目录与 GitHub 线索带来数据库控制；图可见 phpMyAdmin 的表与操作列表。 | [方法条目](../by-type/info-secrets.md) |
| Shell 别名隐藏的网络与权限前提 | 图中 alias 包含 sudo VPN、403 脚本、容器运行及端口发布、字典路径。 | [方法条目](../experiment-design.md) |
| 活动类型在范围内与奖励资格分别核验 | 历史截图把 social engineering、phishing 等列入活动类型，同时说明外部表单场景不奖励。 | [方法条目](../scope-and-rules.md) |
| 登录注册覆盖要按功能状态建立输入模型 | 正文建议重定向到登录后找注册入口、收集参数、再寻找注入，并声称能保证发现漏洞。 | [方法条目](../hunting-strategy.md) |
| 凭据文件名清单需要映射真实消费者 | 正文列 npm、Docker、SSH、数据库、FTP 与恢复码等文件名和关键字，其中有拼写不完整的线索。 | [方法条目](../by-type/info-secrets.md) |
| AD 多模块启动日志要按模块记录完成状态 | linWinPwn 图显示域/DC 输入、LDAP bind、用户枚举，以及部分模块需要凭据。 | [方法条目](../by-type/ldap-xpath.md) |
| admin 文本匹配必须核验受限功能 | 保存命令在多个 Web 端口请求 admin 路径并匹配 admin 文本。 | [方法条目](../discovery/web-and-api.md) |
| crt.sh 别名及组织关联不能直接继承种子范围 | 证书图同时含 CN、Matching Identities 与跨域名称；正文另列收购、LinkedIn、Shodan 等关联来源。 | [方法条目](../discovery/passive-and-services.md) |
| 聚合奖励项目通配符只产生政策候选 | 正文把汇总的 wildcard 去前缀后交给发现、探测与 takeover 工具，另用搜索语法查 bounty/security.txt。 | [方法条目](../scope-and-rules.md) |
| 模板字面量要检查插值语法而非只检查引号 | 保存片段在 Unicode 转义多类字符的模板字面量中使用 ${...}。 | [方法条目](../by-type/xss.md) |
| onclick 的 HTML 实体需沿两层解析核验 | 正文用 &apos; 描述 onclick 字符串上下文，未保存最终页面。 | [方法条目](../by-type/xss.md) |
| 删除响应 CSP 后的 XSS 观察要标明实验改动 | 正文建议在 Burp 响应里删除 CSP 再确认 XSS。 | [方法条目](../experiment-design.md) |
| 收集请求和响应参数后按消费者分配候选 | 正文建议记录正常使用过程中的请求与响应参数，再交叉尝试。 | [方法条目](../discovery/web-and-api.md) |
| 服务商名称命中与子域可认领性分别证明 | 正文把指向某平台的子域概括为可 takeover，没有保存当前资源状态。 | [方法条目](../by-type/subdomain-takeover.md) |
| KrbRelay 的协议操作清单不是成功中继证据 | help 图列 LDAP、SMB 与 HTTP 操作，并含 SPN、SSL、会话和 COM 参数。 | [方法条目](../by-type/ldap-xpath.md) |
| 字典词与扩展名的组合必须落到正确路径 | 正文列 API、token、config 等候选词；图片示例在 signup 路径下添加 csv 扩展，称发现文件。 | [方法条目](../targeted-fuzzing.md) |
| 给 URL 列表追加 FUZZ 需识别查询和分隔符 | 截图以文本替换给每行追加路径占位符。 | [方法条目](../targeted-fuzzing.md) |
| 原入口的重定向与目标不可用分别留证 | 正文讨论发现后目标不可访问且重定向到另一范围内资产的情况。 | [方法条目](../reporting.md) |
| SQL 候选追加文件需防止混入旧批次 | 正文通过发现与历史 URL 筛选把候选追加到文件，再读取该文件进行后续验证。 | [方法条目](../by-type/sql-injection.md) |
| 移动端和 Web 同一业务应比较服务端状态 | 正文建议跨端比较相同功能，图仅有 blind stored XSS 的报告标题。 | [方法条目](../by-type/idor-access-control.md) |
| ADReaper 帮助页的枚举类别不等于权限结果 | 图列 users、groups、SPN、GPO、trust、计算机及数据库等参数，命令以 help 状态结束。 | [方法条目](../by-type/ldap-xpath.md) |
| 私有 JS 可见性与其中接口的授权分别检查 | 正文称私有 JavaScript 含可访问 API，但没有保存接口交换。 | [方法条目](../by-type/info-secrets.md) |
| 影响说明和引用报告都需落到本次证据 | 正文建议先描述影响，另帖称引用历史报告能提高奖励。 | [方法条目](../reporting.md) |
| Smap 的索引输出要保留时间与数据来源 | 图以 Nmap 风格列端口和服务，但正文称数据来自 Shodan。 | [方法条目](../discovery/passive-and-services.md) |
| 学习案例应复现因果条件并限定实验环境 | 正文列智能合约学习、独立做题和重现漏洞报告，并有无论什么漏洞都重现的建议。 | [方法条目](../hunting-strategy.md) |
| 自动化发现与手工业务判断分别衡量覆盖 | 正文强调适合自己的方法与自动化辅助。 | [方法条目](../hunting-strategy.md) |
| 反射流水线的过滤和替换要保留原参数身份 | 正文串联历史 URL、扩展过滤、去重、全参数替换与反射筛选。 | [方法条目](../by-type/xss.md) |
| DOM 调试和目录发现需分别记录观察对象 | 保存正文把 DOM Invader 与 Burp History 后的目录 fuzz 作为方法，仅保存部分步骤。 | [方法条目](../discovery/web-and-api.md) |
| 社交登录的可解码字段不等于可信身份声明 | 正文把 signature 可解码与邮箱修改联系到接管；图仅是社交认证 POST，含 provider、邮箱和 social_media_id。 | [方法条目](../by-type/oauth-oidc.md) |
| JavaScript 字符串转义要检查反斜杠与闭合字节 | 正文给出带反斜杠、引号和注释尾部的片段，称部分字符已编码或转义。 | [方法条目](../by-type/xss.md) |
| 绝对路径及 null byte 片段取决于最终文件 API | 正文分别建议绝对路径与 %00 加扩展名，没有保存运行时或文件读取结果。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 攻击时间线示意要连接实际文件与进程事件 | Ma2tl 图给出特定旧 macOS 环境的下载、伪装、执行和持久化顺序。 | [方法条目](../by-type/desktop-client.md) |
| 弱口令主张要限定登录消费者和实际权限 | 正文建议某组短凭据或品牌相关口令，图只有 admin 报告标题与状态。 | [方法条目](../by-type/authn-session.md) |
| Burp 速查表中的编辑转换与测试能力分开 | 两页图列导航、编辑器编码、Collaborator、参数发现、扫描、JWT/SAML 与角色比对等功能。 | [方法条目](../source-audit.md) |
| Burp REST 的定义列表、任务提交与状态分别留证 | 速查表区分知识库定义 GET、scan 的 URL 输入 POST 与按任务编号查询。 | [方法条目](../discovery/records-and-incremental.md) |
| 开发文档线索需核对实际部署的动作与入口 | 正文建议从开发文档挖功能、接口和输入。 | [方法条目](../discovery/web-and-api.md) |
| 扫描器的路径披露标签需回到响应原文 | 图显示 File path disclosure 与服务器目录字符串，旁边列各路径状态和响应长度。 | [方法条目](../by-type/info-secrets.md) |
| transitionend 片段需要实际过渡完成条件 | 图为自定义元素、outline transition、tabindex 与 transitionend 处理器，没有执行画面。 | [方法条目](../by-type/xss.md) |
| HTML 表单注入到 token 外送需要表单归属链 | 正文给出 form 与 textarea 片段，含弯引号和不完整 action，但没有最终 DOM。 | [方法条目](../by-type/csrf.md) |
| SVG 混合大小写和 Unicode 片段要按解析层核验 | 图片在 SVG 事件、伪属性、混合大小写与 JavaScript 标识符转义之间加注释。 | [方法条目](../by-type/waf-bypass.md) |
| 开放重定向需证明超出实际允许目的地 | 概念图从可信站点指向另一站点；另帖只称可到几个知名域而其他域被拒。 | [方法条目](../by-type/open-redirect.md) |
| eBPF 明文观察要说明进程与 TLS 边界 | eCapture 图把用户态应用/库与内核探针、网络路径关联。 | [方法条目](../by-type/desktop-client.md) |
| 301 和回连地址不是请求走私边界证据 | Turbo Intruder 图有状态与耗时列表，选中请求仅普通 GET，响应为含回连地址的重定向。 | [方法条目](../by-type/request-smuggling.md) |
| 旧版 API 发出的管理员令牌仍需验证消费者 | 截图比较两个 API 版本，一个返回认证失败，旧版返回 admin_token；部分请求信息被遮挡。 | [方法条目](../by-type/authn-session.md) |
| 收藏工具仓库与执行可信度分别管理 | 正文说收藏和回顾 GitHub 工具。 | [方法条目](../source-audit.md) |
| Burp 与 ZAP 功能映射按操作证据核对 | 图将历史、站点树、scope/context、拦截、重复请求、fuzzer、爬虫与扫描等对应。 | [方法条目](../source-audit.md) |
| 发现到截图的工具链要保留阶段输入身份 | 正文列历史 URL、子域发现、HTTP 探测和截图工具的管道。 | [方法条目](../discovery/records-and-incremental.md) |
| href 上下文中的整段 anchor 不是通用逃逸 | 正文展示 href 属性与完整带事件 anchor，未说明原属性如何闭合。 | [方法条目](../by-type/xss.md) |
| 技术指纹到已知漏洞须核适用构建与配置 | 简图直接从技术/版本到 POC 和利用；另帖建议优先看旧站点和特定语言。 | [方法条目](../hunting-strategy.md) |
| 目录重定向后 404 需比较路由规则 | 正文从带斜杠重定向推测隐藏目录，没有实际目录内容。 | [方法条目](../targeted-fuzzing.md) |
| 管理界面发现与具体 WSO2 漏洞分别判定 | 正文用 Shodan 产品线索、CVE 题名和管理页面模板指向 WSO2。 | [方法条目](../discovery/web-and-api.md) |
| 反射定义必须连接即时响应中的脚本消费者 | 正文解释 reflected XSS 是输入经不安全响应处理返回；配图是梗图。 | [方法条目](../by-type/xss.md) |
| 标为 test 的仓库秘密仍需核用途和范围 | 正文建议验证组织仓库中标为测试的秘密。 | [方法条目](../by-type/info-secrets.md) |
| 提醒上次关注时间不等于完成测试覆盖 | skeleton 图显示自上次查看目标以来的天数。 | [方法条目](../discovery/records-and-incremental.md) |
| NTDS 取证建议应限定必要性与证据最小化 | 正文建议在作业中复制目录数据库，没有具体事件或批准范围。 | [方法条目](../by-type/info-secrets.md) |
| ASN 到证书名流水线需保留网络与字段边界 | 图把 CIDR 探测、证书模板和固定列 cut、去括号与分割串联。 | [方法条目](../discovery/passive-and-services.md) |
| git-dumper help 不证明仓库可恢复 | 截图仅有 URL、DIR、并发、超时、代理和请求头等 help 参数。 | [方法条目](../by-type/info-secrets.md) |
| 未发现漏洞的报告要描述方法和覆盖限制 | 正文询问没有发现漏洞时如何报告。 | [方法条目](../reporting.md) |
| 错误日志的会话片段要核有效性和归属 | 正文建议查看访问不存在 favicon 后 error.log 中的会话信息。 | [方法条目](../by-type/info-secrets.md) |
| 恶意文件扫描器的路径与更新参数分开核验 | 图片只展示扫描器 help，含目录路径及引擎更新参数。 | [方法条目](../by-type/file-upload.md) |
| 正反向代理图不能推导匿名或加密保证 | 海报比较用户到代理的出口地址，以及反向代理到多个内部服务，并声称代理不能加密。 | [方法条目](../discovery/web-and-api.md) |
| 注册重复身份、长输入和展示注入须分别验证 | 正文并列重复注册、十万字符的字段输入与用户名 XSS。 | [方法条目](../by-type/authn-session.md) |
| SQL 条件拼接示例需确认输入确实进入语法 | 正文将 teacherId 的布尔条件与 SELECT 拼接展示。 | [方法条目](../by-type/sql-injection.md) |
| 双斜杠状态变化要证明同一受限处理器 | 正文称 login 路径 403，而双斜杠得到 200。 | [方法条目](../by-type/authn-session.md) |
| 粘贴站点和格式正则只提供秘密候选 | 正文列品牌关键字及 token 格式正则，没有保存结果。 | [方法条目](../by-type/info-secrets.md) |
| 重复投票参数需对照投票规则与持久状态 | 图片文字步骤描述复制多个选项参数、追加到一次投票后看到多个投票，并在刷新和另一浏览器中保持。 | [方法条目](../by-type/business-logic.md) |
| 逐参数替换输出保持其他参数与来源不变 | 图展示两个查询参数轮流被替换为编码字符串，另一参数保持原值。 | [方法条目](../targeted-fuzzing.md) |
| 不可见管理界面的 stored XSS 仍需回连主体 | 正文声称输入在不可见后台触发会更严重，没有载荷或实际回连记录。 | [方法条目](../by-type/xss.md) |
| 项目下载 IDOR 的报告标题需对象权限证据 | 正文称多个入口的项目下载越权，图片仅报告列表与严重度。 | [方法条目](../by-type/idor-access-control.md) |
| 插件 fuzz 的 fopen 告警需区分路径和网络消费者 | 图可见插件警告、服务器路径、URL 输入与域名解析失败，并有 active installs 标记。 | [方法条目](../by-type/file-upload.md) |
| JavaScript URL 筛选需核查询后缀和命令形状 | 正文含域名空格、拆开的选项以及 .js 正则筛选；另帖用宽泛匹配。 | [方法条目](../discovery/web-and-api.md) |
| 源码与黑盒功能发现要连接同一业务消费者 | 正文强调结合代码与黑盒，以及优先研究独有功能。 | [方法条目](../source-audit.md) |
| 404 主机上的文档线索可指向另一协议入口 | 正文称长 PDF 导向 JNLP 和 Java 产品登录，再称弱凭据带来设备管理权限。 | [方法条目](../discovery/client-and-cloud.md) |
| 管理设备数量不能替代管理员动作边界 | 同一正文把管理界面与近九千设备全控制联系起来，没有具体设备操作证据。 | [方法条目](../by-type/idor-access-control.md) |
| 大小写与拼写路由变化须对照同一限流动作 | 正文把不同 casing 与拼写的注册路径作为 rate limit 线索。 | [方法条目](../by-type/business-logic.md) |
| CRLF 设置跨子域 Cookie 需要响应和域作用域链 | 正文把某子域响应拆分、另一子域的 Cookie XSS 串到接管；图仅严重度变化。 | [方法条目](../by-type/crlf-response-splitting.md) |
| Cookie XSS 加 autocomplete 不自动泄漏凭据 | 正文在重定向到登录和启用自动填充后直接声称 ATO。 | [方法条目](../by-type/authn-session.md) |
| CSRF 修改资料后需验证存储和受害者渲染 | 保存步骤把 CSRF 改 profile name、切换 beta/重定向和 stored XSS 相连。 | [方法条目](../by-type/csrf.md) |
| 支付网关跳转前的步骤不证明低价购买成立 | 正文只保存加购物车、选择支付方式和跳转第三方网关三步，后续未保存。 | [方法条目](../business-modeling.md) |
| 额外等号导致状态变化要核参数实际解析 | 正文比较参数值前额外等号时的 403 与 200。 | [方法条目](../by-type/waf-bypass.md) |
| IDA 函数颜色与危险调用候选需追实际数据流 | VulFi 图可见函数类别颜色、函数列表与 start 附近汇编，没有实际缺陷证明。 | [方法条目](../source-audit.md) |
| SQLMap 数据库名称输出仍需绑定注入请求 | 图显示查询输出长度及多个数据库名称；正文给出发现与筛选后交给工具的流程。 | [方法条目](../by-type/sql-injection.md) |
| 特定 CRS 和字符变换主张缺少原始链时不泛化 | 正文声称修改 LiteSpeed/ModSecurity CRS 与字符组合可绕过，实际片段留在未保存评论。 | [方法条目](../by-type/waf-bypass.md) |
| 第三方脚本信任关系不自动继承测试许可 | 正文称攻击第三方脚本可得到两家奖励，没有具体授权或请求。 | [方法条目](../scope-and-rules.md) |
| 邀请角色参数要约束到邀请者的有效权限 | 正文称拥有 Add member 权限的用户修改邀请 role 为 Owner；图仅 P1 New，仍在评估。 | [方法条目](../by-type/idor-access-control.md) |
| 仿登录页和文档下载需区分诱导界面与执行结果 | O365-Doppelganger 图显示类似登录界面和打开政策文档的确认窗口，没有凭据流或执行结果。 | [方法条目](../scope-and-rules.md) |
| 混合内容处理与事件触发按实际浏览器核验 | 历史正文把 Chrome/Firefox 的事件差异概括为固定规律，未保存版本与对照。 | [方法条目](../by-type/xss.md) |
| 命令行 XSS 二分标签不能取代浏览器确认 | 截图在历史 URL、查询去重和多参数替换后打印 Vulnerable/Not Vulnerable，没有浏览器执行画面。 | [方法条目](../by-type/xss.md) |
| BITB 中仿地址栏不能证明真实浏览器来源 | 图片把两个相似 Facebook 窗口标为 phishing 与 real，但没有真实顶层来源或凭据交换。 | [方法条目](../scope-and-rules.md) |
| 上传脚本到 LFI 后还需文件解释消费者 | 正文用上传 PHP 片段声称 LFI 可变 RCE，没有实际读取或执行结果。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 内存事件时间线要保留证据源和因果限制 | RipRaw 相关图为云节点内存界面，含矿工引用、SSM 进程事件和部分命令日志。 | [方法条目](../by-type/desktop-client.md) |
| URL 分类器的 0.89 accuracy 不证明 XSS | 图列两类 precision、recall、F1 与 1,923 个样本，正文称按 URL 词汇预测风险。 | [方法条目](../experiment-design.md) |
| 开放端口管道交给 HTTP 工具前先核协议 | 正文从端口扫描 stdout 筛 Open，经文本替换交给 HTTP 探测和模板工具。 | [方法条目](../discovery/records-and-incremental.md) |
| 挑战页观察不能证明所有防护部署可绕过 | 正文以所有 Under Attack/Rate limiting 站点为概括，图仅浏览器挑战等待页。 | [方法条目](../by-type/waf-bypass.md) |
| 302 响应体中的命令结果应与输入和身份绑定 | 两张请求/响应图在 auth 用户字段引入动态求值，并以另一个参数选择不同命令；302 响应体分别含进程身份和目录清单，第三张只为报告邮件。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 异常分支的参数名输出需要独立 HTML 编码 | CTF 源码图的正常分支对某参数值调用 html.escape，异常分支把请求参数名拼接后直接放入 HTML。 | [方法条目](../source-audit.md) |
| 特殊 IP 表示应在实际 URL 消费者中规范化 | 正文把短 IPv4、数值进制、0 与 IPv6 未指定地址列为回环绕过。 | [方法条目](../by-type/ssrf.md) |
| 公开 S3 搜索结果要核归属和具体访问能力 | 正文只推荐公开 bucket 搜索站点，没有对象或响应。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Jira CVE 的通用评分与平台优先级分别说明 | 一张图仅 P5 报告，另一张历史 NVD 条目说明特定 Jira 版本的文件读取，CVSS 5.3 与低机密性影响。 | [方法条目](../impact-and-acceptance.md) |

| 历史 URL 管道的候选过滤与浏览器执行分层 | 正文串接 URL 收集、参数去重、替换全部参数和反射检测，最后按标签过滤。 | [方法条目](../by-type/xss.md) |
| CDN 地址过滤要记录被排除的服务面 | 正文介绍过滤 CDN 地址以减少探测，图仅工具仓库题名。 | [方法条目](../discovery/passive-and-services.md) |
| 下载接口读取与文件解释执行分别证明 | 正文把下载参数发现和本地文件读取相连。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 源码未反射时追导航后的 DOM 消费者 | 正文建议在重定向后寻找源码不可见的 XSS，附图只有报告标题。 | [方法条目](../by-type/xss.md) |
| 代码搜索与检测规则自身命中不能证明秘密有效 | 保存材料包含 Git 搜索、Gitleaks 命中、Burp 令牌规则和 age 密钥正则测试；其中显示源文件位置和测试样本。 | [方法条目](../by-type/info-secrets.md) |
| PHP echo 正则只能定位待追踪输出 | 正文以搜索 echo 与 GET/POST/REQUEST 的组合定位 XSS。 | [方法条目](../source-audit.md) |
| Cognito 用户令牌与 AWS 资源权限的交接边界 | 图把 User Pool 令牌、Identity Pool、临时 AWS 凭据和云服务连成流程。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 弱口令案例的身份与影响不能由标签推断 | 正文声称固定管理凭据迅速获得高等级报告，图只有报告标题。 | [方法条目](../by-type/authn-session.md) |
| text/plain 表单的最终字节与服务端接受条件 | 图把 JSON 片段放进表单字段名和值，以容纳 text/plain 序列化产生的等号。 | [方法条目](../by-type/csrf.md) |
| 路径变体返回成功要核最终受限处理器 | 图列扩展名、分隔符、空白编码与斜杠等变体，并用状态码标示结果。 | [方法条目](../by-type/idor-access-control.md) |
| 对象标识编码与版本切换仍需统一授权 | 图还列接口版本、多个 ID、Base64 标识和邮箱替代。 | [方法条目](../by-type/idor-access-control.md) |
| 移动资源和文档中的 API key 要按服务限制评估 | 图显示 APK 资源 XML 中的 Google Maps key，正文另建议收集文档令牌。 | [方法条目](../by-type/info-secrets.md) |
| 离线参数文本匹配与数据库执行是两种证据 | 图中的模板对文件文本匹配常见参数名和数字形式，正文称无需请求即可寻找 SQL 注入。 | [方法条目](../by-type/sql-injection.md) |
| 协作回调邮箱需绑定发送者与具体业务动作 | 保存线程首段建议把地址中的域换成协作回调域。 | [方法条目](../by-type/info-secrets.md) |
| 备份读取到高权限会话必须逐层绑定身份 | 截图可见备份组身份、远端注册表材料读取、后续凭据处理和远程 SYSTEM 输出。 | [方法条目](../by-type/desktop-client.md) |
| 端点数量不能直接当作发现概率 | 正文把成功机会等同于发现的端点数量。 | [方法条目](../experiment-design.md) |
| 用户编辑功能按字段权限和对象权限交叉检查 | 保存文字讨论用户信息查看与修改，图仅视频封面。 | [方法条目](../by-type/idor-access-control.md) |
| 内存转储完成与秘密解析完成分别记录 | 图可见转储文件下载完成及签名恢复、解析工具提示，没有后续解析产物。 | [方法条目](../by-type/desktop-client.md) |
| LDAP 过滤表达式必须与 SQL 片段分开解析 | 保存列表混合星号、括号、NUL 表示及 SQL 风格字符。 | [方法条目](../by-type/ldap-xpath.md) |
| 浏览器 Python 运行时不等于服务端命令执行 | 图通过脚本资源和 py-script 展示浏览器端 Python 内容，正文把 HTML 注入描述为 RCE。 | [方法条目](../by-type/xss.md) |
| 重定向响应中的 Cookie 需核实际浏览器处理 | 正文询问 301 中设置 Cookie 是否可行，没有保存完整响应或浏览器结果。 | [方法条目](../by-type/crlf-response-splitting.md) |
| API 同一功能的 XML JSON GET 表达按消费者核验 | 图列 MISP/STIX 功能的路径参数、重复 XML 元素、JSON ID 数组和 POST 标签过滤。 | [方法条目](../discovery/web-and-api.md) |
| 主机提权清单从环境事实到具体条件 | 完整图把 OS、应用服务和网络枚举分组，包含版本、进程、用户、配置与敏感文件线索。 | [方法条目](../by-type/desktop-client.md) |
| 计划任务与服务配置的可写性需对应执行主体 | 主机清单包含启动项、服务、计划任务和配置检查。 | [方法条目](../source-audit.md) |
| 网络主机清单要绑定命名空间与观测渠道 | 图列网卡、路由、DNS、监听端口、进程和流量观测。 | [方法条目](../discovery/passive-and-services.md) |
| URL 的 fragment 与服务器收到的路径分开 | 图以含原始井号的 URL 展示所谓 Nginx 绕过和状态码。 | [方法条目](../by-type/waf-bypass.md) |
| Polyglot 的注释引号与事件语法按有限上下文验证 | 正文和图分别展示不同复合 XSS 字符串，图对注释、引号、标签闭合、事件及 Unicode 标记作注释。 | [方法条目](../by-type/xss.md) |
| Recon 流程图按每阶段输入输出建立覆盖记录 | 图串接代码搜索、域名源、存活探测、端口、截图、目录、参数与模板工具。 | [方法条目](../hunting-strategy.md) |
| 关联数据到主动测试之间保留归属和范围判断 | Recon 与 OSINT 图把证书、网络索引、组织收购、邮箱和代码关系连成资产线索。 | [方法条目](../scope-and-rules.md) |
| 固件快照模糊测试要保存可重复的崩溃条件 | 图显示固件快照恢复和 AFL 输入命令，没有崩溃结果。 | [方法条目](../experiment-design.md) |
| 修复声明与同条件复测分别记证据 | 正文建议重查已关闭问题；图包含已移除文件访问的回复和团队确认修复的说法。 | [方法条目](../reporting.md) |
| 泄漏句柄的对象权限与工具动作分别判断 | 图的帮助包含研究、自动操作、挂起类型和命令选项。 | [方法条目](../by-type/desktop-client.md) |
| Newman 报告泄露请求结构但未必泄露有效权限 | 图可见登录请求字段、若干请求头、耗时、响应大小和测试通过统计。 | [方法条目](../by-type/info-secrets.md) |
| Mochawesome 测试源码与交易完成分开 | 图展示商品、变体、随机邮箱地址、结账点击和最终 thank_you URL 断言，且有超时失败。 | [方法条目](../by-type/info-secrets.md) |
| 弹窗截图只支持对应上下文中的有限执行观察 | 几张图分别展示浏览器弹窗与部分 URL，有的图可见闭合标签和事件片段，有的只可见弹窗；正文还声称多个漏洞或 ATO。 | [方法条目](../by-type/xss.md) |
| LDAP 通道架构不等于 LDAP 注入或链路已运行 | 图用两个网络区段和目录服务连接说明跨区通信概念。 | [方法条目](../by-type/ldap-xpath.md) |
| Burp 请求头替换先核匹配谓词与真实流量 | 图中规则使用锚定的 User-Agent 正则和外部脚本替换内容。 | [方法条目](../experiment-design.md) |
| AWS 策略文档与主体有效权限分别核验 | 图分别显示云 API 动作名称日志和读取 AWS 管理策略的 Allow 通配文档。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 工具集合更新与多节点环境要固定具体版本 | 保存材料介绍模板集合发布和周期性重建工具环境，没有执行结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 索引发现到 SQL 实验要保留原始请求身份 | 正文把 SSL 索引发现、管理入口和数据库枚举命令相连。 | [方法条目](../by-type/sql-injection.md) |
| 自制 302 响应按报文完整性和跟随主体核验 | 正文以监听器拼接 302、Location 和本机地址，没有保存完整请求结果。 | [方法条目](../by-type/open-redirect.md) |
| 币种切换要核金额单位与最终履约 | 正文用两种币种相同数值说明支付差异，并给出历史汇率估计。 | [方法条目](../by-type/business-logic.md) |
| 安全邮件平台注册资格与发送权限分开 | 保存线程首段描述注册邮件安全门户并声称可发送到任意对象。 | [方法条目](../by-type/authn-session.md) |
| 工作流输出清理与域名置换保留原候选 | 图的发布记录提到输出清理、通知和替换生成，正文提出置换生成仍有遗漏。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史搜索运算符按查询语义和索引边界记录 | 完整旧版搜索表覆盖精确短语、排除、OR、站点、标题、URL、文件类型和数字区间等类别。 | [方法条目](../discovery/passive-and-services.md) |
| 产品搜索特征与具体 CVE 可利用性分开 | 正文以产品路径和搜索特征寻找 BIG-IP 候选，没有对应实例的版本与补丁证据。 | [方法条目](../by-type/waf-bypass.md) |
| 容器工具帮助可运行与产物生成成功分别记录 | 图可见容器已存在、帮助输出，以及文件或 MIME 相关命令缺失和后续工具用法信息。 | [方法条目](../experiment-design.md) |
| 返回外部页面内容仍需确认实际请求消费者 | 图显示带 Cookie 的 POST 请求和 Example Domain 页面内容，正文称 Full SSRF。 | [方法条目](../by-type/ssrf.md) |
| 重定向参数中的模板代码文本不等于执行 | 保存 URL 含编码后的 PHP 模板式字符串，没有执行输出。 | [方法条目](../source-audit.md) |
| 重置邮箱数组要核令牌所属账户与接收规则 | 正文把邮箱字段从标量改成含两个地址的数组并声称账户接管，没有保存完整结果。 | [方法条目](../by-type/authn-session.md) |
| Prometheus 指标标签不能代替完整 API 定义 | 正文把 /actuator/prometheus 的暴露称为全部 API 定义。 | [方法条目](../discovery/web-and-api.md) |
| 掩码邮箱与电话片段只能约束候选集合 | 图显示重置页面的掩码邮箱和部分电话号码，正文介绍预测完整地址的工具。 | [方法条目](../by-type/info-secrets.md) |
| 异步导出在创建读取下载各阶段保持对象权限 | 图明确描述导出模块让另一服务端组件读取原本不可访问的产品数据。 | [方法条目](../by-type/idor-access-control.md) |
| 邮件头中的服务器地址不能直接认作 Web 源站 | 图从邮件 Received 字段取得地址，正文将邮件注册与源站发现相连。 | [方法条目](../by-type/waf-bypass.md) |
| 生成器参数与建立会话的执行结果分开 | 图是包含平台、架构、连接方式、证书和后续命令选项的帮助。 | [方法条目](../experiment-design.md) |
| 奖励政策搜索结果不授予当前测试许可 | 正文列搜索 bug bounty、security.txt 和奖励的查询。 | [方法条目](../scope-and-rules.md) |
| 请求补充复现材料不等于所有报告已确认 | 图中的回复要求针对具体问题提供详细步骤、PoC 和截图，正文引用较大的问题数量。 | [方法条目](../reporting.md) |
| 索引快照差异要核时间与数据覆盖变化 | 保存材料包含两帖，图对比保存的 Shodan JSON、IP、端口与 CVE 标记。 | [方法条目](../discovery/records-and-incremental.md) |
| GraphQL 用户响应要核解析器身份与字段权限 | 图显示 getUser 请求、转发地址头和 200 用户 JSON，部分内容遮挡。 | [方法条目](../by-type/idor-access-control.md) |
| WP-Cron 正常任务触发与资源耗尽分开 | 正文声称 wp-cron 普遍可导致严重性能问题，图是报告和奖励说法，没有请求成本证据。 | [方法条目](../discovery/web-and-api.md) |
| 重定向循环脚本需保留原跳与解析后的目标 | 正文脚本替换 URL 参数、跟随 HEAD 重定向并匹配 Location 文本，存在变量与引用边界问题。 | [方法条目](../by-type/open-redirect.md) |
| 配置文件覆盖到代码执行取决于实际生命周期消费者 | 正文把上传任意 JSON、覆盖包配置和运行脚本相连。 | [方法条目](../by-type/file-upload.md) |
| SSRF 输入位置覆盖要追实际网络请求构造 | 正文列路径、Host、请求头、请求体和查询参数等位置。 | [方法条目](../by-type/ssrf.md) |
| 静态 URL 提取记录匹配范围与实际字符串来源 | 图用 grep 提取包内 URL，正文和图的参数、引号及字符集合有差异。 | [方法条目](../discovery/client-and-cloud.md) |
| 修改本地响应需证明后续服务端操作改变 | 正文声称改响应里的 ID 可撤回另一用户任务。 | [方法条目](../by-type/idor-access-control.md) |
| 安全头缺失按具体浏览器消费者评估 | 图列 CSP、X-Content-Type-Options、HSTS、Access-Control-Allow-Origin 与框架头缺失，没有原始响应。 | [方法条目](../discovery/web-and-api.md) |
| 扫描运行状态与各项结果完成分别记录 | 图仍显示 Running 和用时，同时列若干低等级项目。 | [方法条目](../experiment-design.md) |
| Actuator env 暴露需核脱敏和访问主体 | 正文只有环境端点的线索，图是题名，没有实际字段值。 | [方法条目](../by-type/info-secrets.md) |
| SQL 字符列表按方言绑定类型和差分证据 | 保存列表混合不同数据库延时语法、引号编码、布尔条件及 LDAP 片段。 | [方法条目](../by-type/sql-injection.md) |
| 多跳 HTTP 头处理不能简化成单个地址头绕过 | 截图包含多个认证、转发和连接相关字段，响应有进程身份结果；其他正文将其简化成单个头或不完整命令。 | [方法条目](../by-type/waf-bypass.md) |
| 接管严重性由可认领资源和业务消费者确定 | 正文把子域接管概括为几乎总是高等级，图是广告内容。 | [方法条目](../impact-and-acceptance.md) |
| 解析器数量不能代替当前解析质量证据 | 正文介绍数量很大的解析器集合，图只是仓库标题。 | [方法条目](../discovery/passive-and-services.md) |
| 重写请求头的最终路由仍需统一权限判断 | 图通过 X-Original-URL 改变后端目标并展示不同响应状态。 | [方法条目](../by-type/idor-access-control.md) |
| Referer 变化与权限结果用单变量对照 | 图的另一例同时出现路径与 Referer 变化，并用 200 表示结果。 | [方法条目](../by-type/idor-access-control.md) |
| 远程响应控制台按任务对象和文件产物核权限 | 图含代理在线、离线或无效状态，以及多个已下载文件的路径和大小。 | [方法条目](../by-type/desktop-client.md) |
| 重复键数组与查询参数需核各层有效对象标识 | 图将对象 ID 改成嵌套值、重复 JSON 键或重复查询参数，并展示状态差异。 | [方法条目](../by-type/idor-access-control.md) |
| 操作录像需和最小 HTTP 证据共同绑定 | 正文列录屏工具安装方式，没有漏洞过程。 | [方法条目](../reporting.md) |

| Burp 主机范围正则要核名称终点和相似域 | 图中的高级范围规则用宽泛域名片段匹配主机，缺少名称终点约束。 | [方法条目](../scope-and-rules.md) |
| 个人资料持久化要区分服务端保存与本地残留 | 正文描述修改个人资料后退出、重新登录仍触发的场景。 | [方法条目](../by-type/xss.md) |
| 并发 curl 丢弃输出时仍需逐请求完成凭据 | 正文把大量并发请求送入代理，并关闭证书校验、丢弃终端输出。 | [方法条目](../experiment-design.md) |
| 删除成员后核项目权限和既有会话撤销 | 正文声称已删除用户仍可访问项目并改变管理员状态，图片只有计划修复与金额。 | [方法条目](../by-type/idor-access-control.md) |
| Burp 导出对象要区分审计发现代理记录与站点地图 | 正文介绍解析项目导出数据，图片仅仓库题名。 | [方法条目](../discovery/records-and-incremental.md) |
| Recon 流程图的节点需要对应功能覆盖与输入输出 | 完整图串联根域来源、主动/被动子域、排序过滤、HTTP/端口、接管候选、归档、JS 和内容发现；正文另给技术识别到参数分析的顺序。 | [方法条目](../hunting-strategy.md) |
| SAML 会话签名产物与服务端身份接受分别取证 | 图显示会话数据解码、签名生成和 Cookie 页面，但浏览器仍展示登录界面。 | [方法条目](../by-type/saml-sso.md) |
| OTP 的 Host 变体必须到达同一验证处理器 | 正文建议替代后端主机及 HEAD 请求，图片是邮件验证限流报告题名。 | [方法条目](../by-type/authn-session.md) |
| LSA SSP 函数表只能定位调用边界 | 图是 Windows LSA SSP 函数指针表，正文称其可用于密码材料观察。 | [方法条目](../source-audit.md) |
| Windows 函数入口和进程演示的权限条件要保留 | 一图给 LSA SSP 接口，另一图展示进程写入、创建 section、恢复执行以及特定演示窗口。 | [方法条目](../by-type/desktop-client.md) |
| OTP 数组输入应按实际候选消费次数计数 | 图片把标量 OTP 改成 JSON 数组，未展示响应。 | [方法条目](../by-type/authn-session.md) |
| 重置邮箱变体要贯通解析收件人令牌主体与消费 | 保存请求包含路径验证码、Cookie、防伪字段和邮箱，其他正文列重复字段、括号、逗号及数组变体，其中一个 JSON 片段本身语法无效。 | [方法条目](../by-type/authn-session.md) |
| Azure AD 登录图按每次令牌交接记录身份 | 图连接 Kerberos TGT、服务票据、Autologon、DesktopSSOToken 和 Azure AD；正文题名另称枚举及喷洒。 | [方法条目](../by-type/authn-session.md) |
| SVG 和多语法片段需回到实际事件及解析上下文 | 正文用斜杠和空白改变 SVG 标签，但仍包含事件属性；另一图注释引号、注释边界、details 开启事件及 Unicode 字符串。 | [方法条目](../by-type/xss.md) |
| 二阶 XSS 宏要每个样本完成写入再读取 | 完整宏图说明写入 URL1 后读取 URL2，编辑覆盖会只保留最后一个样本，并把后置宏响应交回检测工具。 | [方法条目](../experiment-design.md) |
| 后置读取响应不是二阶 XSS 执行证据 | 图展示宏将最终响应供检测工具分析。 | [方法条目](../by-type/xss.md) |
| GraphQL OTP 批处理按业务操作数约束 | 正文建议将多个 OTP 尝试放在一个 GraphQL 请求内，未给验证结果。 | [方法条目](../by-type/graphql.md) |
| 方法切换的成功状态需绑定原受限动作 | 工具正文介绍多方法尝试，实际终端在 localhost 静态路径上显示 POST 200、CONNECT 400、TRACE 405。 | [方法条目](../by-type/idor-access-control.md) |
| M2M 客户端凭据交换要保留机器主体 | 图明确由 client ID 和 client secret 换访问令牌，再访问 API。 | [方法条目](../by-type/oauth-oidc.md) |
| 参数名字只产生候选还需定位具体消费者 | 正文列 XSS、跳转和 SSRF 常见参数；SSRF 列表只保存部分序号，未保存段落按用户口径覆盖。 | [方法条目](../targeted-fuzzing.md) |
| favicon 哈希检索需保留共享图标的误归属 | 图把图标 URL 转换成哈希、日期和索引查询。 | [方法条目](../discovery/passive-and-services.md) |
| SOAP 序列化字段与 Java 类探测不能直接推出 RCE | SOAP 图片包含实体令牌、Cookie 和长序列化样式字段；另一正文介绍类路径探测工具。 | [方法条目](../by-type/deserialization-rce.md) |
| Authorization 关键词需区分请求凭据与意外返回 | 正文建议在流量中搜索 Authorization，图片仅赏金确认。 | [方法条目](../by-type/info-secrets.md) |
| URL 管道每次筛选需记录丢失的候选 | 图和正文将扩展名过滤、等号筛选、去重、参数分类、全参数替换与反射标签检测串联。 | [方法条目](../discovery/records-and-incremental.md) |
| 嵌套对象重复键和重复查询要核最终授权值 | 图展示 nested ID、重复 JSON 字段与重复查询，正文把嵌套对象误称 root 数组，并用状态码代表结果。 | [方法条目](../by-type/idor-access-control.md) |
| 披露许可应按具体细节与允许范围记录 | 奖励邮件允许分享赏金，但要求其他漏洞细节先获项目方同意，正文也讨论报告可见性。 | [方法条目](../reporting.md) |
| Jenkins 控制台目录输出需保留既有身份条件 | 图展示脚本控制台执行目录列举并返回结果，其他图仅题名和处理状态。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 云端移动终端文件清单不代表工具可运行 | 图显示移动端云 shell 中多个工具文件，正文声称免费和长期可用。 | [方法条目](../experiment-design.md) |
| 限流清单要区分计数身份输入规范化与流程重置 | 完整图列头字段变体、重复转发地址、字符、方法、Cookie 更换、重置与验证码参数，正文覆盖登录、注册、重置和反馈。 | [方法条目](../by-type/authn-session.md) |
| 隐藏字段仍需追实际请求与跳转消费者 | 图列 hidden 输入和多种 URL 写法，正文认为隐藏重定向字段更容易出现问题。 | [方法条目](../by-type/open-redirect.md) |
| 预测面板和 Running 扫描不能计为确认发现 | 图分别显示预测 SQL/XSS 标签，以及仍在 Running 的扫描、URL/参数数量和 High 标签。 | [方法条目](../experiment-design.md) |
| 焦点触发的 CSS transition 需发生真实属性变化 | 正文用 outline 和 transition 组合声称可触发脚本。 | [方法条目](../by-type/xss.md) |
| HTML 类型的 JSON 外形响应要核实际解析上下文 | 正文建议修改 JSON 内容，图中的历史模板响应为 text/html，包含转义的 JSON 外形字符串及检测标签。 | [方法条目](../by-type/xss.md) |
| 私有 Recon DSL 的依赖图与阶段完成状态分开记录 | 完整脚本图描述被动收集、过滤、DNS/TLS/CNAME、差分合并、接管候选、解析、HTTP 和非 Web 端口，日志含变量、UID、依赖与多层计划。 | [方法条目](../discovery/records-and-incremental.md) |
| 过滤私网地址和归并域名需另记被排除的覆盖面 | 脚本图在解析后过滤私网地址，并从 URL 提取主机再做其他服务探测。 | [方法条目](../scope-and-rules.md) |
| 连接配置中的注释活动项与环境权限要分开 | 图展示多个数据库连接配置、身份客户端秘密及文档数据库 key，部分为注释或不同环境。 | [方法条目](../by-type/info-secrets.md) |
| HttpOnly 不阻止同源脚本读取业务响应字段 | 图展示 sessionInfo/authUser 响应和 fetch 片段，正文将其称为 HttpOnly 场景中的令牌取得。 | [方法条目](../by-type/xss.md) |
| 用户接口返回身份字段要核访问主体和复用条件 | sessionInfo 图显示认证用户字段；Plex 图则在请求中已携带 X-Plex-Token，响应含用户与认证字段。 | [方法条目](../by-type/info-secrets.md) |
| Oracle 注册入口索引模板标签与实际用户字段分层 | 材料包括产品搜索、注册模板命中与搜索用户的界面；界面确实展示部分姓名、用户名和邮箱，另图是大量索引候选。 | [方法条目](../discovery/web-and-api.md) |
| 片段导航的焦点条件须绑定元素和浏览器状态 | 正文声称 URL 片段配合焦点事件无需交互可触发。 | [方法条目](../by-type/xss.md) |
| Angular 字符串命中与模板表达式执行分别取证 | 正文给出 constructor 表达式并按页面字符串搜索，未展示完整执行链。 | [方法条目](../by-type/xss.md) |
| JWT 破解速度说法不能替代密钥熵与验证语义 | 正文介绍历史破解器并给速度数值，没有当前环境结果。 | [方法条目](../by-type/jwt.md) |
| CVE 编号不一致的模板命中需保留来源冲突 | 正文与仓库/终端图片使用不同编号，图显示特定请求和响应。 | [方法条目](../discovery/records-and-incremental.md) |
| 本地修改认证响应不能证明服务端已授予身份 | 正文建议把失败响应换成成功值或状态，图有 OTP 报告处理通知。 | [方法条目](../by-type/authn-session.md) |
| CRLF 内容注入需区分正文与响应头消费者 | 处理回复明确该案例是内容注入且未展示 XSS，并按较低等级处理。 | [方法条目](../by-type/crlf-response-splitting.md) |
| OTP 案例的邮箱登录链接前提不能省略 | 另一处理回复指出测试流程先需要邮箱中的登录链接，正文概括为通用绕过技巧。 | [方法条目](../impact-and-acceptance.md) |
| Swagger configUrl 的外部数据需追到实际 DOM 使用 | 正文描述从 configUrl 加载外部配置并触发 XSS，未保存文章全文。 | [方法条目](../by-type/xss.md) |
| CNAME 关系不改变请求 Host 与 TLS 身份 | 正文把 DNS 查询与另一个域名的 HTTP 状态相连，并含将 URL 当 DNS 名的写法。 | [方法条目](../discovery/passive-and-services.md) |
| 接管标签过滤反向与追加文件会污染候选 | 正文管道使用反向筛选 Vulnerable 标签并追加文件。 | [方法条目](../by-type/subdomain-takeover.md) |
| 索引候选数量与长查询截断不代表资产完整发现 | 图分别显示产品/证书服务命中和旧搜索界面的词数截断警告；正文另列产品及端口条件。 | [方法条目](../discovery/passive-and-services.md) |
| WHOIS 组织字段不能推出确切分配网段 | 图的过滤输出是组织、地址和邮件，没有网络分配字段，正文服务器参数写法与图不同。 | [方法条目](../discovery/passive-and-services.md) |
| 流量生成 OpenAPI 只反映已观察功能 | 正文介绍将 mitmproxy 流量转成规范。 | [方法条目](../discovery/web-and-api.md) |
| dompdf 字体缓存示意链需逐段证明消费者条件 | 图把远程 CSS、字体下载、PDF 生成、缓存访问和 RCE 相连，未给实际执行结果。 | [方法条目](../by-type/document-rendering.md) |
| 渲染器写入缓存与 Web 服务解释执行是两层权限 | 字体图将保存到缓存的内容与后续浏览器访问相连。 | [方法条目](../by-type/file-upload.md) |
| Python 八进制字符串与 PyScript 页面渲染分层 | 正文用 Python 转义字符串及 print/表达式描述页面执行，没有当前运行证据。 | [方法条目](../by-type/xss.md) |
| PHP-FPM full 状态页暴露的是具体运行快照 | 图可见 pool、连接/队列、进程数量、当前 URI、脚本路径与耗时。 | [方法条目](../by-type/info-secrets.md) |
| FPM 状态指标不能当完整 API 清单 | full 状态图展示部分 worker 当前请求、路径和性能值。 | [方法条目](../discovery/web-and-api.md) |
| Lambda 批量任务日志需保留角色成本与结束状态 | 图显示 Lithops/AWS Lambda 作业、对象存储区域、43 个激活及 1/43 的进度。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 分布式扫描的激活计数需与产物逐一对账 | 云任务图展示调度器和部分进度。 | [方法条目](../discovery/records-and-incremental.md) |
| 文件返回字节与 shell 通配展开不能混作同一链 | 一图显示 GET 文件路径得到 passwd 文本；另一图是 shell 中通配符展开后 cat 的结果，正文将其联系到 Java 读文件接口。 | [方法条目](../by-type/lfi-path-traversal.md) |
| EJS 模板源码与传入数据的求值边界要分开 | 正文只保存 EJS 标签相关讨论的第一部分。 | [方法条目](../by-type/ssti.md) |
| CORS 响应需用浏览器实际 Origin 与凭据条件核对 | 图中的手工 Origin 和允许来源都是无方案的 google.com，并设置允许凭据，未显示真实浏览器可读结果。 | [方法条目](../by-type/cors.md) |
| DNS AAAA 回调只证明对应解析观察 | 另一图显示 DNS AAAA 回调，正文将 SSRF、DNS 重绑定与接管放在一起。 | [方法条目](../by-type/ssrf.md) |
| sqlmap 恢复会话与 WordPress 核心归因分开 | 终端明确恢复已保存的注入会话，显示自定义 GET 参数、布尔盲注标签、MySQL/MariaDB 与有限数据库名；正文称 WordPress 5.9.3 核心漏洞。 | [方法条目](../by-type/sql-injection.md) |
| 命令页面输出不能补出从 JavaScript 到 RCE 的入口 | 图展示 ASPX 页面中的程序、参数与账户列表结果，外链全文未保存。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 客户端硬编码比较需追后端受限入口 | 图中 JavaScript 比较固定口令后导航到另一页面。 | [方法条目](../source-audit.md) |
| 前端登录跳转不是服务端会话建立 | 硬编码检查图只显示浏览器条件判断和导航。 | [方法条目](../by-type/authn-session.md) |
| Plex 用户响应需保留请求已携带令牌的前提 | 图的用户接口请求已带 X-Plex-Token，随后响应用户和认证信息，正文概括为从历史记录接管。 | [方法条目](../by-type/authn-session.md) |
| 链接抓取的内外关系不代表失效验证或许可 | SniffCon 图列已爬取、内部与外部链接，替代文字补充工具功能。 | [方法条目](../discovery/web-and-api.md) |
| 实验室题目完成不能替代生产环境证据 | 正文介绍 API 练习与基础方法，图是实验室成功和管理员标记。 | [方法条目](../experiment-design.md) |
| 已解决邮件仍需同条件复测支撑修复结论 | 保存图片只有反馈及一年后解决通知，未给原请求与复测过程。 | [方法条目](../reporting.md) |
| 监听绑定地址与回连地址需分别解释 | 图展示 0.0.0.0 监听、具体回连地址、HTTP 路径、间隔、SSL 关闭和文件生成成功。 | [方法条目](../experiment-design.md) |
| 广泛互联网技巧仍需落在当前许可资产 | 正文提出面向大量互联网目标的做法，没有具体项目许可。 | [方法条目](../scope-and-rules.md) |
| 历史 CWE 排名应作为机制分类而非当前严重性 | 图片是 2021 年 CWE Top 25，含内存边界、身份授权、数据注入等不同机制。 | [方法条目](../impact-and-acceptance.md) |
| 端口预设只定义一次候选集合 | 图介绍 httprobe 的 common/large/xlarge 端口预设。 | [方法条目](../discovery/passive-and-services.md) |
| 设备封禁与角色文档需落到服务端状态 | 正文分别描述封禁设备后访问与文档中的角色限制，图只有报告题名。 | [方法条目](../by-type/authn-session.md) |
| httpx 成功筛选应解析状态字段而非任意文本 | 图使用文本 grep 筛选 2 开头状态并显示 200。 | [方法条目](../discovery/web-and-api.md) |
| Sysmon 关系图需回事件字段才能解释行为 | 图是密集事件关系节点，未提供完整可读字段和图例。 | [方法条目](../discovery/records-and-incremental.md) |

| 放行页面与脚本执行需要分别观察 | 两图分别展示被阻断页面与变更查询后正常首页，未展示反射或脚本执行。 | [方法条目](../by-type/waf-bypass.md) |
| 未发布功能可见要核服务端动作而非界面开关 | 正文询问未发布功能是否算漏洞，另一图链接摘要提到用 match/replace 显示隐藏功能。 | [方法条目](../by-type/idor-access-control.md) |
| 上传文件名按后续消费者拆开核对 | 正文把文件名中的路径、SQL、HTML 和 shell 片段连接到不同缺陷。 | [方法条目](../by-type/file-upload.md) |
| 工具的流行程度不能代替方法适配与证据 | 正文认为热门工具使发现趋同，并建议学习工具而非跟随多数。 | [方法条目](../hunting-strategy.md) |
| Recon 管道需核工具输入类型与输出是否进入合并 | 正文将根域收集、HTTP、模板、截图和归档连接；部分命令把 URL 当域名，或用管道连接未必消费 stdin 的收集器。 | [方法条目](../discovery/records-and-incremental.md) |
| CNAME 链与可注册域名仍需核受影响消费者 | 终端展示多级 CNAME，正文建议检查目标域是否可购买。 | [方法条目](../by-type/subdomain-takeover.md) |
| 证书 WHOIS 和 Analytics 关联需保存来源区别 | 图列证书、反向 WHOIS、Analytics 标识的相关域发现，并同时出现不同版本标记。 | [方法条目](../discovery/passive-and-services.md) |
| 合并文件名不一致会静默漏掉子域来源 | 脚本图收集多个来源，另一脚本把 subfinder 输出追加到不同单复数文件名，最后只整理其中一个文件。 | [方法条目](../discovery/records-and-incremental.md) |
| wc 文件总行数不能代表唯一发现数 | 终端对多个收集文件与合并文件计数并打印总数。 | [方法条目](../experiment-design.md) |
| 双斜杠状态差异需核规范化后的同一入口 | 正文展示登录路径 403 与双斜杠路径 200。 | [方法条目](../by-type/idor-access-control.md) |
| 反向 IP 与云提供商网段不自动属于租户 | 正文建议由 IP 索引与 BGP 查询寻找资产，图显示长搜索查询遭截断。 | [方法条目](../discovery/passive-and-services.md) |
| 严重性处理状态与奖励规则分别记录 | 一图同时显示 Critical 与 Informative Closed，其他回复确认问题但按特定历史奖励规则不给金钱奖励。 | [方法条目](../impact-and-acceptance.md) |
| CSRF 生成器产生表单还需真实跨来源业务结果 | 图展示由代理请求生成表单、Test in browser 和本地 burpsuite 展示 URL。 | [方法条目](../by-type/csrf.md) |
| 协议分析漏洞扫描和日志检索应按任务分工 | 图将多个工具概括成网络安全工具，混用了扫描与日志搜索描述。 | [方法条目](../experiment-design.md) |
| 生产 bundle 与 sourcemap 需保留版本及代码归属 | 正文介绍分析 Webpack 产物、读取 JS 和通过 sourcemap 获取源码，没有完整外链实现。 | [方法条目](../source-audit.md) |
| 结账画面金额与实际结算参数分别证明 | 图在外部 PoC 页面显示结账界面、金额、币种和修改按钮文字，未给最终交易记录。 | [方法条目](../by-type/business-logic.md) |
| 版本控制路径和代码搜索关键词仅定位待核内容 | 正文列 Git/SVN 文件路径及配置、passwd、shadow 等搜索条件。 | [方法条目](../by-type/info-secrets.md) |
| 邮箱确认与二次验证必须约束同一服务端动作 | 正文建议通过 API 使用未确认邮箱账户，或用 DELETE 绕过敏感操作的 2FA。 | [方法条目](../by-type/authn-session.md) |
| ZIP 上传与 PHP 包含需核同一可达文件消费者 | 正文提出由 ZIP 上传连接 LFI 与执行，未展示请求或结果。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 多头回调标记需绑定来源与实际交互协议 | 图在多个头分别放入不同外部标记，未展示对应回调结果。 | [方法条目](../by-type/ssrf.md) |
| 本地响应和错误码变化还需服务端状态核对 | 正文泛称请求/响应修改可造成严重问题，另建议替换改密响应或修改错误码。 | [方法条目](../by-type/authn-session.md) |
| 交易示意中的诱导点击需核身份与防伪绑定 | 银行交易图把诱导链接、已登录交易页与转账结果相连。 | [方法条目](../by-type/csrf.md) |
| 双扩展名上传不保证服务器按脚本解释 | 图示文件名从双扩展名变成脚本文件并产生连接，未展示保存和处理配置。 | [方法条目](../by-type/file-upload.md) |
| 命令图的 shell 拼接与独立参数调用分别核对 | 图由应用输入连接命令分隔与后续连接，没有实际请求结果。 | [方法条目](../by-type/cmd-injection-rce.md) |
| root 对象形态与空数组不是通用认证身份 | 图显示嵌套 root 对象中的认证字段、响应数据和 Cookie，正文另称空数组绕过。 | [方法条目](../by-type/authn-session.md) |
| 算术结果需排除客户端模板及普通计算接口 | 正文列不同算术表达式、方法和大量 SSTI 数量，没有响应证据。 | [方法条目](../by-type/ssti.md) |
| HTTP 差分模糊测试需记录每跳消息边界 | 正文介绍基于语法的请求走私差分工具，未保存论文或实现全文。 | [方法条目](../by-type/request-smuggling.md) |
| PII 的 OCR 和分类命中需回可见原图核实 | 正文介绍用 OCR 和 CNN 搜索证件、照片与签名。 | [方法条目](../by-type/info-secrets.md) |
| localhost 插件命令输出不能推广到所有 WordPress | 三段保存正文给相同插件路由与命令输出，显示 www-data 主体。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 归档 URL 主机提取应保留端口与原始引用 | 图用 CDX 提取域名，一份输出含端口，另一份用 sed 删除协议、路径和 www。 | [方法条目](../discovery/passive-and-services.md) |
| 复测批准和删除记录仍需同条件独立证据 | 回复分别说明复测奖励及删除 NetDB 记录，其他邮件只称已解决。 | [方法条目](../reporting.md) |
| 错误页版本信息与可利用缺陷分别证明 | 邮件明确描述 400 页面出现 Nginx 版本并称重复，未保存实际错误响应。 | [方法条目](../by-type/info-secrets.md) |
| Cognito 挑战响应字段需由服务端绑定身份 | 图展示 RespondToAuthChallenge、client ID 与 ChallengeResponses，字段大量遮挡，没有响应。 | [方法条目](../by-type/authn-session.md) |
| JS 美化差分需同时保存原字节与获取条件 | 图介绍变更监控、消息通知和美化 diff。 | [方法条目](../discovery/records-and-incremental.md) |
| OTP 的 domain 参数受理不等于已发生跳转 | 两图显示 OTP 生成请求中有 domain，响应仅 JSON success 和空 data，没有 Location 或最终落地页。 | [方法条目](../by-type/open-redirect.md) |
| 历史默认凭据清单需核自有部署配置和实际角色 | 图分别是默认凭据报告题名与 Tomcat 清单，正文声称 dev 用户有高权限。 | [方法条目](../by-type/authn-session.md) |
| Recon 数据库与 Repeater 分组需绑定身份和副作用 | 正文建议数据库整理和 CLI/消息入口，图是端点树及含会话、防伪和验证码的重置请求，未给响应。 | [方法条目](../discovery/records-and-incremental.md) |
| 片段取值与 auxclick 需保留交互和脚本策略 | 正文把片段字符串与 SVG auxclick 处理器连接，并称某次 WAF 放行。 | [方法条目](../by-type/xss.md) |
| 历史 CVE 片段要保留中间解释器与配置条件 | 图截取 ImageMagick 图形片段、CGI/Bash 示例及 TLS 缺陷章节，部分内容裁剪，标题混有 SSRF 与命令消费者。 | [方法条目](../source-audit.md) |
| 子域图的主动被动分类应按真实网络动作 | 完整脑图将词表、置换和虚拟主机列主动，但在被动分支也列端口、HTTP 和爬虫；正文另称证书一次收集全部子域。 | [方法条目](../scope-and-rules.md) |
| Nmap 选项图需绑定版本权限和额外探测 | 旧脑图列扫描方式、发现、时序和输出，将 -A 简化成操作系统检测。 | [方法条目](../experiment-design.md) |
| 扫描输出文件需保留格式运行边界与结束状态 | 正文介绍日志输出，图列 normal/XML 等格式、追加与恢复。 | [方法条目](../discovery/records-and-incremental.md) |
| 子域清单与 S3 桶命名不是同一种对象 | 正文将子域枚举文件直接交给桶扫描工具，并建议下载内容。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 转发地址限流差异需固定账户处理器和时间 | 图对比 429 与设置转发头后 200，响应称邮件已发送；部分字段遮挡，用户名/路径等对照不完整。 | [方法条目](../by-type/authn-session.md) |
| XML 实体进入错误页时失败状态仍可能泄露字节 | 图中的外部实体进入响应 schema 字段，503 错误信息和 HTML 标题含 passwd 文本。 | [方法条目](../by-type/xxe.md) |
| URL 片段聚焦需核匹配元素与真实事件 | 图把片段 ID 与 input 焦点处理器相连。 | [方法条目](../by-type/xss.md) |
| 重置令牌边界需保留发行消费重发与并发状态 | 正文列移除、空值、过期、数组和并发条件，另一段仅提示收到代码及重发。 | [方法条目](../by-type/authn-session.md) |
| 延时语法需绑定数据库方言与稳定对照 | 正文分别以十秒页面响应称注入、以及 PostgreSQL 延时函数替代其他语法。 | [方法条目](../by-type/sql-injection.md) |
| 字典生成数量与 WAF 选项不是实际绕过结果 | 图展示 LFI 字典、深度和 WAF 勾选，以及编码注意事项，输出称有 889 项。 | [方法条目](../targeted-fuzzing.md) |
| 代理请求转 JavaScript 后要重新核浏览器限制 | 图的扩展菜单可将所选实验室请求复制成 JavaScript。 | [方法条目](../experiment-design.md) |
| SSH 隧道示意需保留入口出口与许可 | 图将本地客户端经 SSH 中转到另一服务，未展示真实连接结果。 | [方法条目](../discovery/client-and-cloud.md) |
| 配置 IP 与出站地址需要核真实请求生产者 | 正文概括 Cloudflare 入站/出站差异，并建议从 htaccess 内容抽地址再验证。 | [方法条目](../discovery/passive-and-services.md) |
| SOME 窗口关系需核调用时来源和具体动作 | 完整图描述开启窗口、原窗口导航到目标、另一窗口经回调引用 opener 的 DOM 方法；正文提到同域或子域部署。 | [方法条目](../by-type/xss.md) |
| 特权候选标记需核文件权限及真实执行条件 | 正文列自动提权工具，另一段搜索 root 所有且有 SUID 位的文件。 | [方法条目](../source-audit.md) |
| 图片尺寸资源影响需按解码预算分段评估 | 正文建议上传极大像素图片并称 DDoS，没有运行证据。 | [方法条目](../by-type/file-upload.md) |
| Windows 命令会话不证明域管理员控制 | 图显示 handler、一次 Windows 命令会话和应用配置目录，正文称三小时域管理员。 | [方法条目](../impact-and-acceptance.md) |
| 管理配置界面需核主体与持久动作权限 | 图可见 Web 防火墙服务配置和端口，正文外链称从 JS 得到管理面板。 | [方法条目](../by-type/idor-access-control.md) |
| Ruby Kernel 是语言模块不是操作系统内核 | 正文将 Kernel open、动态 send 和多种反序列化列为 Rails RCE 方向，图片只是文章封面。 | [方法条目](../source-audit.md) |
| 序列化 Cookie 与 dump 题名不能证明秘密或 RCE | 一图只显示 API 请求的认证标志和长 data Cookie，正文另称 Java dump 暴露秘密；另一正文列多种 Ruby 解析器。 | [方法条目](../by-type/deserialization-rce.md) |
| PostgREST 文档中的 RPC 需核实际数据库角色权限 | 图显示 Swagger 文档、版本字符串、绑定地址、根描述接口与一项 RPC 的参数 schema。 | [方法条目](../discovery/web-and-api.md) |
| 高频参数名字不等于当前 XSS 风险 | 图列 25 个查询参数并引用历史来源，没有具体响应。 | [方法条目](../by-type/xss.md) |
| 用户更新接口要分请求材料与非预期响应字段 | 正文建议查看更新用户数据的接口，图仅奖励题名。 | [方法条目](../by-type/info-secrets.md) |
| 例外奖励不能作为漏洞成立的通用依据 | 回复明确称并非真正漏洞，但决定例外奖励。 | [方法条目](../reporting.md) |
| 范围字符串与模糊条目需按资产和动作解释 | 正文区分通配域与单个域，并询问未明确列入或排除的条目。 | [方法条目](../scope-and-rules.md) |
| 分号路径变化需核路由规范化和响应媒体类型 | 正文给 Nginx/Tomcat 路径转换，另称给 JSON 端点附 HTML 后缀可在 Firefox 执行。 | [方法条目](../discovery/web-and-api.md) |
| 选择器截图需绑定页面状态与原始响应 | 正文介绍按 CSS 选择器截图，未保存实现全文。 | [方法条目](../reporting.md) |
| 代理解压视图需保留原字节及变换说明 | 图片在链接清单中实际给 gzip/deflate 解压选项提示，并以历史默认状态说明。 | [方法条目](../discovery/records-and-incremental.md) |
| headless 模板版本命中与浏览器执行证据分层 | 图显示 localhost 的 headless 模板命中、引擎/模板版本及另一图的发布清单。 | [方法条目](../experiment-design.md) |

| 浏览器凭据告警、仓库命中与配置文件来源 | 扩展告警、仓库搜索和通用正则只提供候选。 | [方法条目](../by-type/info-secrets.md) |
| URL 前缀与问号、反斜杠的解析分歧 | 把受信域拼到另一域的 URL 中时，分别观察校验器和实际请求客户端解析的 scheme、authority、host、userinfo、path、query。 | [方法条目](../by-type/ssrf.md) |
| 前台 products 与 API products 的授权对照 | 前台拒绝而 API 返回 200 是调查入口。 | [方法条目](../by-type/idor-access-control.md) |
| 隐藏查询参数发现之后验证消费者 | 参数发现工具给出的名字需要逐项与无参数基线比较，确认解析位置、重复值规则、是否真正影响业务或仅被反射。 | [方法条目](../targeted-fuzzing.md) |
| IDA 函数过滤作为审计入口 | 函数大小、字符串引用、字节模式、立即数与代码模式可以组合或反向过滤，缩小候选函数集。 | [方法条目](../source-audit.md) |
| 勒索软件模拟截图的进程与结果边界 | 模拟器截图出现伪装进程启动、影子副本删除与文件加密日志。 | [方法条目](../experiment-design.md) |
| Linux 证据采集的输入、用户和类别覆盖 | 采集前限定目标文件系统、输入位置、用户及证据类别；记录工具版本、采集时间、文件系统兼容性、输出位置、哈希与失败项。 | [方法条目](../discovery/records-and-incremental.md) |
| Origin 相似度阈值与真实归属 | 反代源站候选的相似度阈值越宽松，候选和误报都可能增加。 | [方法条目](../discovery/passive-and-services.md) |
| 从保存流量生成 API 描述的覆盖边界 | 先确认实际截获了请求和响应，再保存 flows 并记录采集账户、功能操作和时间窗口。 | [方法条目](../discovery/web-and-api.md) |
| DLL 搜索失败日志到实际加载边界 | 进程监视器中的 DLL 搜索记录与 NAME NOT FOUND、PATH NOT FOUND 是路径线索。 | [方法条目](../by-type/desktop-client.md) |
| 容器攻击链逐阶段证明权限跨越 | 将文件上传、主机提权、容器环境探测、逃逸、集群访问和持久化拆成独立阶段。 | [方法条目](../cloud/container-k8s-security.md) |
| 硬编码凭据训练的代码与容器层区分 | 训练示例把硬编码口令定位到代码、容器和不同云平台。 | [方法条目](../by-type/info-secrets.md) |
| 自动化机器人参数与日志中的令牌边界 | 机器人配置依赖会话标识和访问令牌，命令可能经过 GET 请求。 | [方法条目](../by-type/info-secrets.md) |
| script 字符串、结束标签与 URI 编码的不同消费者 | 先定位输入是在 JavaScript 字符串、表达式还是 HTML script 元素文本中，再记录引号、反斜杠和结束标签分别经过哪层转义。 | [方法条目](../by-type/xss.md) |
| 非 HTTP 客户端经 Burp 中转的协议一致性 | 框架图将原生客户端、监听端、HTTP 中转、Burp、目标 relay 和服务端连接起来。 | [方法条目](../by-type/desktop-client.md) |
| HTTP 速查图的注册状态与业务结果 | 速查图混用了标准状态、未分配号码和实现专有号码；例如 103 的注册语义为 Early Hints，不能沿用图中的 Checkpoint。 | [方法条目](../discovery/web-and-api.md) |
| 工具脑图转为阶段、输入与验收结果 | 脑图的词表、信息收集、Web 扫描及 Android/iOS 工具按任务分阶段使用：每阶段明确输入来源、适用协议、账户上下文、主动或被动动作与预期输出。 | [方法条目](../hunting-strategy.md) |
| 带命令样式输入的 PDF 响应不能单独证明 RCE | 截图中查询输入含命令样式片段，响应是 200 与 PDF 数据。 | [方法条目](../by-type/sql-injection.md) |
| 爬虫与扫描流程中的请求范围和隐私 | 将目录枚举、子域爬取、扫描和个人信息验证拆开，在每个发起网络请求的阶段检查目标、方法与当前规则。 | [方法条目](../scope-and-rules.md) |
| 搜索引擎的服务候选与实时资产边界 | Shodan、Censys、FOFA 或类似索引返回的是某次观测的主机、端口和服务。 | [方法条目](../discovery/passive-and-services.md) |
| 白名单重定向链中的参数编码层次 | 第一跳认可受信域时，第二跳仍可能根据另一个参数导航。 | [方法条目](../by-type/open-redirect.md) |
| 奖金、证书、收购关系和雇佣身份不能扩展授权 | 获奖或历史报告接收不意味着范围外资产被允许测试；收购、子公司、证书与 DNS 关系也需要对照当前程序规则。 | [方法条目](../scope-and-rules.md) |
| 脚本目录、漏洞库更新与实际执行版本 | 区分仅更新漏洞库、加载脚本以及清理重装：目录里有 CVE 文件或更新成功不等于扫描时已选中并执行。 | [方法条目](../hunting-strategy.md) |
| AD 关系图的会话来源与路径可信度 | MemberOf、AdminTo 和 HasSession 关系表达不同权限和观察事实。 | [方法条目](../experiment-design.md) |
| 密码学题目先辨识编码、哈希与加密模型 | XOR、古典替换、散列、分组或流密码以及 RSA 依赖不同输入和验证条件。 | [方法条目](../source-audit.md) |
| OSI 速查不替代实际协议与认证边界 | 分层图用于组织帧、网络、传输和应用观察，但不宜把 SSH、TLS、API 和 socket 固定塞进单一层后推导漏洞。 | [方法条目](../discovery/web-and-api.md) |
| 过滤差异与事件脚本的实际执行条件 | HTML 标签别名、实体解码、事件属性、JavaScript 转义和属性访问语法都要在对应消费者里核对。 | [方法条目](../by-type/xss.md) |
| 改密成功界面与认证前置条件 | 改密页面显示成功、同时显示 Log in 或要求旧密码，都不能单独证明匿名改密。 | [方法条目](../by-type/authn-session.md) |
| Confluence 结果头、模板输出与历史版本证据 | 截图分别展示自定义响应头中的运行身份、Windows 工具用法、进程信息和扫描模板匹配。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 源码暴露覆盖多种版本控制元数据 | Git、SVN、Mercurial、Bazaar、Darcs 和 BitKeeper 的目录名可作为泄露候选。 | [方法条目](../by-type/info-secrets.md) |
| CRLF 扫描配置与 HTTP 头的真实变化 | 截图只有 target、GET、线程、超时及验证开关等配置，没有注入结果。 | [方法条目](../by-type/crlf-response-splitting.md) |
| Android Intent 的组件选择与 exported 边界 | SEND、EXTRA_TEXT 和 MIME 类型描述消息用途，不会自动让 Intent 成为显式；显式 Intent 需要指定组件。 | [方法条目](../discovery/client-and-cloud.md) |
| 登录时序差异先证明账号存在性 | 靶场截图显示存在与不存在用户名耗时不同。 | [方法条目](../by-type/authn-session.md) |
| JS 推导后台路由与管理界面的权限验证 | 客户端路由或命名模式、wp-admin 可打开和管理界面扫描器命中只定位入口。 | [方法条目](../by-type/idor-access-control.md) |
| 注释登录线索与 sqlmap 恢复结果分开 | 页面注释可暴露输入位置，但是否进入数据库仍需实际请求对照。 | [方法条目](../by-type/sql-injection.md) |
| 历史 CVE 报告标题不能证明当前实例 | 历史服务索引与某份报告的 CVE/RCE 标题可以提供研究线索，但缺少当前产品、受影响版本、配置和具体结果。 | [方法条目](../reporting.md) |
| 另一页面令牌与当前操作授权的不同职责 | 先识别令牌承担 CSRF、会话还是能力授权，并记录签发身份、用途、生命周期与绑定对象。 | [方法条目](../by-type/idor-access-control.md) |
| 多个子域同一 CVE 的报告归并 | 同一 CVE 在三个域出现时，先判断是否同一部署、共享根因、相同配置和共同修复。 | [方法条目](../reporting.md) |
| SSH pivot 图中的每一跳访问范围 | 隧道图连接网关、跳板和内网设备，只说明预想路径。 | [方法条目](../scope-and-rules.md) |
| 第三方公开索引与敏感文件的读取边界 | 公司关键词可以搜索代码分享、文档、SaaS、存储和开发平台中的相关资料，目录索引与备份文件名也能提示泄露。 | [方法条目](../discovery/passive-and-services.md) |
| 2FA 候选归入服务端认证状态与绑定 | 直接访问下一步、复用验证码、重置流程、代码泄露、响应修改及限流差异分别对应不同假设。 | [方法条目](../by-type/authn-session.md) |
| Django debug 场景先确认版本与输出消费者 | 将用户名放入脚本样式内容只是输入；先确认历史漏洞涉及的 Django 版本、debug 状态及错误页面实际输出位置，再判断内容是否进入可执行 HTML。 | [方法条目](../by-type/xss.md) |
| 云攻击模拟按权限、资源、观测与回滚拆解 | 技术列表把 IAM、EC2、S3、CloudTrail 等动作映射到不同战术。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 主机标签边界不能用字符串前缀判断 | 以完整解析后的 hostname 判断域名关系，不能因 URL 开头含目标域名就视为可信。 | [方法条目](../by-type/ssrf.md) |
| RS256 与 HS256 混淆的密钥类型和算法约束 | RS256 用私钥签名、公钥验证，不能把“获取公钥”描述为获取签名秘密。 | [方法条目](../by-type/jwt.md) |
| 多等号参数差异需要确认最终文件值 | 图片把 file= 与 file=== 的不同结果称为 WAF 绕过。 | [方法条目](../by-type/waf-bypass.md) |
| 构建与测试系统从接收代码到产物权限 | 按幻灯片的问题追踪代码进入方式、构建或测试执行环境、可控配置、产物保存、发布方式及读取权限。 | [方法条目](../source-audit.md) |
| 时间扫描与代理复核需要同请求基线 | 单行脚本把总耗时超过阈值直接标为 SQLi，会混入网络、连接建立、队列和普通慢请求；HEAD 与真实 GET/POST 处理还可能不同。 | [方法条目](../by-type/sql-injection.md) |
| 激活重发与用户详情的对象归属对照 | 重发激活路径中的数字与用户详情 ID 都应绑定请求者权限。 | [方法条目](../by-type/idor-access-control.md) |
| 上传图片与文档的元数据泄露验收 | 对自有样本先记录 GPS、设备信息、作者等元数据，再比较上传后下载原件、缩略图和转换文档。 | [方法条目](../by-type/info-secrets.md) |
| 子域流水线先过滤范围再进入主动阶段 | 保留被动来源、解析器、词表与源记录，按明确域名标签匹配范围并去除排除项，再进行 DNS、TLS、HTTP 与端口等主动步骤。 | [方法条目](../discovery/passive-and-services.md) |
| DNS 隧道图与实际查询证据 | 示意图展示客户端、递归 DNS、权威侧与返回数据，但 DNS 请求和回调不自动等于数据窃取。 | [方法条目](../discovery/records-and-incremental.md) |
| 失效社交链接的可能接管与平台绑定 | 爬虫的 Possible Takeover 只表明链接异常。 | [方法条目](../by-type/subdomain-takeover.md) |
| 靶场扫描结果按证据类型复核 | 扫描结果表含反射、XSS、SQLi、HTTP/DNS 外部交互、依赖和 TLS 等项目，各项需要不同确认方式。 | [方法条目](../experiment-design.md) |
| WordPress 插件本地执行结果的范围 | 保存帖含本地插件路由请求与 www-data 身份结果，属于特定插件环境的执行线索。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 可控子域 XSS 到凭据 CORS 读取的逐段条件 | 链条要求脚本能在受信子域实际执行，受保护接口认可该实际 Origin，浏览器发送相应凭据，并允许脚本读取响应。 | [方法条目](../by-type/cors.md) |
| 登录错误响应中的可控数据库内容 | 保存截图把输入与数据库 duplicate entry 错误联系起来。 | [方法条目](../by-type/sql-injection.md) |
| 重复 user_id 的解析顺序与授权一致性 | 分别比较单个 ID、两个不同 ID 与交换顺序，记录网关、授权层和业务查询最终选取的值或列表。 | [方法条目](../by-type/idor-access-control.md) |
| Pulse 文件遍历响应与密码披露的边界 | 截图返回的是 passwd 风格账号与 UID/shell 记录。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 浏览器弹窗能证明当前执行但不能自动证明存储链 | 弹窗显示 Cookie 样式文本，只能在排除人工执行、扩展或固定弹窗后支持当前页面脚本执行。 | [方法条目](../by-type/xss.md) |
| 分布式抓包的接口、过滤与接收端溯源 | 架构图将多个 sensor 的接口与 BPF 过滤结果发送到 receiver 并写入文件。 | [方法条目](../discovery/records-and-incremental.md) |
| API 令牌变更的 CSRF 与最终凭据状态 | 敏感端点候选需在真实跨站浏览器上下文核对请求方法、Cookie/SameSite、反伪造令牌、Origin/Referer 与服务器认证。 | [方法条目](../by-type/csrf.md) |
| 链接数量上限与并发事务不变量 | 服务器最多允许创建固定数量链接时，以串行基线和最小并发对照检查“校验数量—写入”是否原子执行。 | [方法条目](../by-type/business-logic.md) |
| 被阻断的 HTML 上传不能证明云对象覆盖 | 图片请求把 HTML 内容放入 multipart file，响应是 WAF 阻断页。 | [方法条目](../by-type/file-upload.md) |
| Login CSRF 与 self-XSS 的跨用户触发链 | 组合链应证明登录 CSRF 能把受害测试浏览器切换到攻击者自有账户，并让已存在的输入在该浏览器自动到达执行点。 | [方法条目](../by-type/xss.md) |
| URI 规范化到 Tomcat manager 的逐层对照 | 截图出现带路径片段的 manager/status 页面及 JVM 信息。 | [方法条目](../by-type/idor-access-control.md) |
| 黑盒测试前明确身份、业务和动作边界 | 仅得到网站地址时，先取得可测试域名/应用与环境、许可方法、排除对象、测试账户及角色、限速窗口、数据处理和联系人。 | [方法条目](../scope-and-rules.md) |
| 个人检查表与待处理问题的证据状态 | 检查表按资产、角色、业务操作与漏洞假设记录已验证、未验证及阻塞条件。 | [方法条目](../hunting-strategy.md) |
| HTTP 工具输出与访问密钥正则的匹配位置 | 截图流水线对候选文件路径和 AKIA 样式标识进行搜索，但默认静默 URL 输出未必包含响应正文，嵌套 echo 也未必按预想生成每个目标的备份文件名。 | [方法条目](../by-type/info-secrets.md) |
| SQL shell 与 OS shell 的不同前置权限 | 工具选项只表达请求能力：先确认真实注入、数据库类型和当前身份，再分别验证数据库查询权限与操作系统执行链所需配置。 | [方法条目](../by-type/sql-injection.md) |
| SPA DOM 扫描的会话、路径序列与实际 sink | 帮助页提供 Cookie、HTTP 认证、初始序列、存储、代理、排除 URL、超时和检查类型等配置。 | [方法条目](../by-type/xss.md) |

| 工具清单按研究阶段选择并保留输入输出 | 截图及正文列出发现、参数、代理、口令与扫描工具名称。 | [方法条目](../hunting-strategy.md) |
| 历史 URL 到 SQL 候选的流水线保持当前证据 | 截图串联子域发现、历史 URL、去重、SQL 参数筛选和自动探测。 | [方法条目](../by-type/sql-injection.md) |
| 蜜罐收到漏洞载荷不等于被测产品成功执行 | 截图左侧产品版本、右侧接收的编码请求说明该观察点收到一种输入。 | [方法条目](../experiment-design.md) |
| Web 配置读取区分路径规范化与命令执行 | 图片显示含多斜杠路径的请求返回 WEB-INF 配置 XML 与过滤器映射。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Docker 列表可读与宿主机控制分阶段验证 | 截图中的容器 JSON 含容器标识、镜像与命令字段，只支持列表信息可读这一观察。 | [方法条目](../cloud/container-k8s-security.md) |
| JWT 修改算法和 kid 必须对应实际验证器 | 保存正文提出修改 alg、角色字段及 kid。 | [方法条目](../by-type/jwt.md) |
| PUT 成功状态与上传文件执行分开举证 | 正文把 PUT 的 403 到 201 与脚本上传关联。 | [方法条目](../by-type/file-upload.md) |
| 隐含 user_id 与多值参数按实际授权消费者检验 | 正文列出数组、对象、重复参数与隐藏 JSON user_id，另图只显示调查/修复/奖励状态。 | [方法条目](../by-type/idor-access-control.md) |
| 事件日志存储与后续加载执行属于不同阶段 | 图片显示事件源写入多条事件和二进制字段。 | [方法条目](../by-type/desktop-client.md) |
| 响应篡改实验保存原始流量及后续服务端结果 | 保存步骤介绍 Burp 匹配替换；图片同时修改真假字段并添加环回地址相关请求头，另一图片只显示物流详情页面。 | [方法条目](../experiment-design.md) |
| 邮件冒名的最终收件证据与域策略独立记录 | 正文强调邮件进入收件箱，图片只有题名与奖励邮件。 | [方法条目](../by-type/authn-session.md) |
| 备份与 env 索引命中先验证实际暴露内容 | 截图包含多端口备份候选的 200 和搜索引擎 env 摘要。 | [方法条目](../by-type/info-secrets.md) |
| sleep 探针跳转到登录页不能证明时延 SQL 注入 | 图片里的探针返回登录跳转和一次耗时。 | [方法条目](../by-type/sql-injection.md) |
| 科学计数输入关注金额和数量解析不变量 | 正文给出科学计数表示。 | [方法条目](../by-type/business-logic.md) |
| 历史参数筛选保留真正的前端输入消费者 | 图片把历史 URL、等号筛选、静态后缀过滤与参数替换串联。 | [方法条目](../by-type/xss.md) |
| 连接载荷生成不等于目标执行或网络可达 | 图片是多种编码、反向及绑定连接的生成器帮助。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 导入功能按预览与最终消费链检查验证一致性 | 正文指出导入入口可能缺少其他入口的校验。 | [方法条目](../by-type/file-upload.md) |
| 主机和参数笛卡尔组合保持逐请求范围 | Intruder 图片展示主机与参数两个位置的组合。 | [方法条目](../targeted-fuzzing.md) |
| 邮箱动作与代理地址限流使用相同服务端动作对照 | 正文分别涉及邮箱变更缺少限流和 X-Forwarded-For 伪造。 | [方法条目](../by-type/authn-session.md) |
| 跳过双因素提示检查服务端认证阶段 | 正文称跳过提示后登录成功。 | [方法条目](../by-type/authn-session.md) |
| 发布路线与修复公告作为版本化研究假设 | 正文建议关注浏览器新功能与修复数量。 | [方法条目](../hunting-strategy.md) |
| 维护者邮箱域失效不自动等于软件供应链接管 | 正文提出注册失效邮箱域再走账户重置的链条。 | [方法条目](../by-type/subdomain-takeover.md) |
| phpMyAdmin setup 的可见表单与配置写权限分开 | 截图显示 setup 索引命中和添加服务器表单，包括连接方式字段。 | [方法条目](../by-type/idor-access-control.md) |
| 证书 CN 与索引 IP 只构成归属候选 | 正文将 Shodan 证书 CN 查询、IP 探测与目录筛选组合，另图只有 SQL dump 报告状态。 | [方法条目](../discovery/passive-and-services.md) |
| 重置用户参数与令牌兑付主体必须一致 | 正文称重置 user 参数可导致接管。 | [方法条目](../by-type/authn-session.md) |
| 历史路由与隐藏参数发现按当前请求补全 | 正文将历史 URL 收集和隐藏参数工具并用。 | [方法条目](../discovery/web-and-api.md) |
| 申诉与重新提交用当前根因和新增影响支撑 | 正文及图片涉及优先级变化、调解、范围拒绝、点击劫持不奖励与 Git 报告重评。 | [方法条目](../reporting.md) |
| 云交互 Shell 中的本地 root 不等于云项目控制 | 截图显示环境内提权及容器相关结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 移动报告将客户端控制与服务端影响分开 | 一张图片给出移动报告结构：静态/动态分析、调试、代理、证书固定、本地数据及重打包等。 | [方法条目](../discovery/client-and-cloud.md) |
| 子域关键词优先级不代表真实风险与归属 | 图片列举环境、管理、运维、测试等名称关键词用于筛选。 | [方法条目](../discovery/passive-and-services.md) |
| 侦察图与分布式任务保留全局范围及阶段产物 | 侦察图含注册、ASN、并购、搜索、链接、仓库、DNS、端口与截图；正文提到把工作分配到多台实例。 | [方法条目](../hunting-strategy.md) |
| 隐藏头反射与缓存污染分别证明消费者及共享复用 | 正文把隐藏请求头、反射、XSS 和缓存污染串联。 | [方法条目](../by-type/xss.md) |
| 代理历史词表与注释抽取保留来源边界 | 图片显示代理扩展菜单，正文介绍从流量生成词表和提取响应注释。 | [方法条目](../discovery/records-and-incremental.md) |
| 盲注回调按字段与处理者归属区分 | 正文提到联系/反馈/举报字段与独立回调服务。 | [方法条目](../by-type/xss.md) |
| 编码属性与 fragment 使用完整浏览器解析链 | 正文/图片包含编码属性、片段输入与注释边界载荷。 | [方法条目](../by-type/xss.md) |
| 登录后 return URL 按实际解析结果限制目标 | 正文列出多种 return URL 形式，图片显示登录后 JavaScript URL 的执行观察。 | [方法条目](../by-type/open-redirect.md) |
| 公开地址与服务索引分清采集、指纹和漏洞 | 图片分别显示公开 IP 分析工具帮助、网络设备索引和 RPC 服务数量。 | [方法条目](../discovery/passive-and-services.md) |
| NSE 类别并集与请求预算不能误读为全部 safe | 正文和图片用 default,safe,discovery 加 Web 端口与快速时序。 | [方法条目](../discovery/passive-and-services.md) |
| PE 证书区域藏数据与可信加载路径独立审计 | 图片描述将编码数据放入 PE 证书相关区域并由测试加载器读取/解码/执行。 | [方法条目](../by-type/desktop-client.md) |
| Firebase 下载能力、规则和扫描判定分层检查 | 正文含下载 token/媒体访问与匿名读写论断；图片实际显示 APK 反编译发现实例后给出 Secure 判定。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 限流路径后缀变化必须仍命中同一账户动作 | 图片对 accounts.json 和追加后缀比较 429/200。 | [方法条目](../by-type/authn-session.md) |
| IPv4 另类表示按最终客户端与网络出口归一 | 正文列出十六进制、八进制、缩写及协议变体。 | [方法条目](../by-type/ssrf.md) |
| 重置链接 Host 污染以最终邮件 URL 与令牌绑定为证据 | 正文提出通过 Host 影响重置邮件。 | [方法条目](../by-type/authn-session.md) |
| JNDI 元数据回调与任意代码执行分别定级 | 正文展示通过目录服务回调携带环境属性的思路。 | [方法条目](../by-type/deserialization-rce.md) |
| Flink 双编码路径读取记录每层解码和实际文件正文 | 图片以日志路径与编码片段构造候选并筛选类似账号行。 | [方法条目](../by-type/lfi-path-traversal.md) |
| GIF 标记与上传脚本执行取决于响应和打开方式 | 图片示例本地文件前缀与回调记录，正文涉及上传。 | [方法条目](../by-type/file-upload.md) |
| 失效社交链接需证明注册及现存信任关系 | 图片只显示某账号不存在，正文将其关联链接劫持。 | [方法条目](../by-type/subdomain-takeover.md) |
| jQuery HTML 转文本前的解析阶段仍需审计 | 正文用先 .html(text) 再 .text() 的例子。 | [方法条目](../by-type/xss.md) |
| curl 状态尺寸表保留重定向与结构化字段 | 截图以请求状态、大小和 URL 生成逗号表。 | [方法条目](../discovery/records-and-incremental.md) |
| 镜像环境变量泄露按配置与历史层分别追溯 | 正文涉及容器构建变量、配置键与云凭据线索。 | [方法条目](../by-type/info-secrets.md) |
| 默认凭据截图要以最终服务端会话权限判断 | Axis2 登录 POST 图片有默认账号字段、200 和会话 Cookie，未显示受保护管理动作。 | [方法条目](../by-type/authn-session.md) |
| Java 表达式环境回显与错误页关联实际求值 | 截图的编码表达式之后，服务端错误正文出现环境变量样式数据。 | [方法条目](../by-type/ssti.md) |
| Microsoft 服务指纹建立端点与版本置信度 | 图片输出 Exchange/ADFS 的版本、域及 EWS/Autodiscover 等端点，另有未发现服务。 | [方法条目](../discovery/client-and-cloud.md) |
| 修复回归使用相同原始输入并补充消费者边界 | 正文建议重测旧报告，图片分别给出认可与初步修复通知。 | [方法条目](../experiment-design.md) |
| 端口发现结果只描述本次探测集合 | Naabu 图片列出一个域解析到的 IP 及四个开放端口。 | [方法条目](../discovery/passive-and-services.md) |
| Swagger 配置接口输出按字段能力与读取权限定级 | 截图记录 GET Logging 端点 200 返回配置，含存储连接字符串及账户键字段。 | [方法条目](../by-type/info-secrets.md) |
| PHP 调试信息候选避免状态码和限流假阳性 | 正文以索引和路径探测寻找 PHP 信息页。 | [方法条目](../by-type/info-secrets.md) |
| 搜索引擎模糊发现保留索引边界及后续动作 | 正文描述用搜索引擎/字典发现子域、文件和目录，图片只有工具标识。 | [方法条目](../discovery/passive-and-services.md) |
| LDAP 特殊字符根据过滤器与 DN 消费者验证 | 正文列出通配、括号及空字符相关字符串。 | [方法条目](../by-type/ldap-xpath.md) |
| 自动秘密发现与类型猜测不作为凭据有效性证明 | 工具描述涵盖爬取、填表、触发调试页与匹配秘密，另一截图把同一字符串匹配到多个服务。 | [方法条目](../by-type/info-secrets.md) |
| 主题 Ajax 参数反射要补足真实响应与浏览器触发 | 图片显示主题密码流程的 Ajax POST，其中 redirect_to 含 HTML 输入，但响应窗为空。 | [方法条目](../by-type/xss.md) |
| SCCM 管理点发现不等于主站点与控制权限 | 图片输出管理点、注册表查询失败及可能寻找主站点的提示。 | [方法条目](../discovery/client-and-cloud.md) |
| 无线工具菜单与射频验证范围分开记录 | 图片只列无线工具模式与网卡状态，没有报文、关联或认证结果。 | [方法条目](../discovery/client-and-cloud.md) |
| 邀请与可预测标识区分公开查询和私有用户字段 | 正文关联团队邀请及可预测标识，图片只有用户信息披露奖励标题。 | [方法条目](../by-type/idor-access-control.md) |
| 上传文件名的百分号与扩展名按最终存储解释 | 正文给出后缀/文件名变体及编码换行。 | [方法条目](../by-type/file-upload.md) |
| 外部协作服务命令通道示例不证明初始入侵 | Trello C2 图片显示操作端、代理编号与命令输出。 | [方法条目](../by-type/desktop-client.md) |
| 域名许可与 IP 其他端口授权分别读取 | 正文问范围内 Web 域解析 IP 的其他管理端口是否可测试。 | [方法条目](../scope-and-rules.md) |
| 自动工具结果之外建立主体对象动作矩阵 | 正文指出工具可能遗漏认证授权问题。 | [方法条目](../business-modeling.md) |
| 历史重定向参数与生成器结果只是候选 | 正文串联历史 URL、在线状态筛选及重定向参数工具，另帖提到生成器。 | [方法条目](../by-type/open-redirect.md) |

| 离线与 CI 秘密扫描的规则数量及输入边界 | ggshield 卡片标注的支持类型数与保存正文不一致，数量应随工具版本、规则集和扫描模式记录，不能当作发现了相同数量的有效凭据。 | [方法条目](../by-type/info-secrets.md) |
| TLS 证书与服务搜索结果用于候选资产归属 | tlsx 的保存输出提供 TLS 版本、密码套件及证书摘要；SAN/CN、同一 IP 的服务和搜索平台的 ssl/status 条件可用于补充候选关系。 | [方法条目](../discovery/passive-and-services.md) |
| 修改密码的旧密码校验与登录限流分别核查 | 保存帖提出从修改密码功能检查当前密码尝试次数。 | [方法条目](../by-type/authn-session.md) |
| CSP 审计输出需要回到实际响应与浏览器执行边界 | Lighthouse 保存图片列出 base-uri 缺失、host allowlist 等风险，cspparse 图片则只展开 connect-src。 | [方法条目](../by-type/xss.md) |
| postMessage 的接收来源、窗口身份与数据消费者 | 保存图显示 window.open 后通过通配 targetOrigin 发送消息，应提炼为跨窗口信任边界核查。 | [方法条目](../by-type/xss.md) |
| 加载器及 C2 演示先区分已有执行权与初始入侵 | Nim 加载器保存图展示 AMSI/ETW 修改、系统调用、内存写入、线程和 PE 入口计算等自报日志；Nim C2 图展示已有 agent 的回环连接、命令、文件和截图能力。 | [方法条目](../by-type/desktop-client.md) |
| 查询值替换与重定向候选保留原始 URL 结构 | 保存的 qsreplace 对比说明，替换全部参数会改变与目标字段无关的业务条件；正则、sed 和 awk 重建 URL 还可能丢失重复参数、顺序、编码及片段。 | [方法条目](../by-type/open-redirect.md) |
| DNS 威胁清单按控制面、数据面与资源影响拆解 | 保存图混列域名控制、DNS 缓存、隧道、资源耗尽以及 TCP 洪泛和僵尸网络，应按被影响的边界整理。 | [方法条目](../discovery/passive-and-services.md) |
| 响应词数筛选不能替代 JSON 解析和业务判定 | 保存帖用极少词数筛选 JSON 响应。 | [方法条目](../targeted-fuzzing.md) |
| 反射标记先定位 HTML 与脚本的逐层消费者 | 保存帖覆盖事件属性、title/meta、输入 value、script 结束标签、CTF 表达式及 javascript URL 等上下文。 | [方法条目](../by-type/xss.md) |
| JWT 解码、密钥强度与服务端授权分别建立证据 | 保存图把 Base64 解码、HMAC 弱密钥离线检查、修改 token 和发送请求放在一条流程中。 | [方法条目](../by-type/jwt.md) |
| Firebase 客户端配置、数据规则与路径访问分开核查 | 保存正文指出 init.js/init.json 与数据 .json 路径可提供配置和资源线索。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| AD 强制认证与 ACL 路径保留对象及权限条件 | DFSCoerce 图片中 RPC 返回访问拒绝而监听端仍收到认证，说明返回码与认证副作用需要独立记录。 | [方法条目](../discovery/client-and-cloud.md) |
| 公开索引、前端源码与相似框架路径只产生秘密候选 | 保存帖包含 API-key 搜索词、源码管理接口线索、敏感文件检索及 bootstrap.cache 等相似站点路径。 | [方法条目](../by-type/info-secrets.md) |
| 回调来源、协议消费与延迟都需要服务端归属证据 | 保存的 httpx 重定向跟随可由本地客户端自行触发 Interactsh 回调，必须先排除本地探测器、浏览器、预取或代理。 | [方法条目](../by-type/ssrf.md) |
| 历史 Angular 表达式载荷必须绑定模板编译与版本 | 保存图片涉及历史 Angular 1.4 至 1.5.8 的表达式、charAt 原型变化和动态脚本组合。 | [方法条目](../by-type/xss.md) |
| CGI 扫描状态过滤要保留真实业务响应 | Scout 保存结果包括大量 302，正文也列出重复参数方向。 | [方法条目](../discovery/web-and-api.md) |
| ETW、进程识别与 Burp 工程文件保留观测窗口 | ETW 图片列出 provider、opcode、进程过滤及 PID、线程和时间；EmoCheck 图列出检测名、进程路径与导出记录。 | [方法条目](../discovery/records-and-incremental.md) |
| 调试开关、扩展名与新接口各自验证服务端权限 | 保存正文提出 debug 参数、js/json 后缀和 img/services 到 subscription 的路由差异。 | [方法条目](../by-type/idor-access-control.md) |
| Tomcat examples 表单 XSS 的历史版本条件 | 保存 Nuclei 图片显示 examples JSP 路径命中，正文给出搜索标题与历史 CVE。 | [方法条目](../by-type/xss.md) |
| 防护清单按具体数据流与边界验证 | 保存的两张防护图涉及序列化、PDF、上传、文件写入、字符串拼接、堆栈泄漏以及语言、框架、ORM、网络分隔和 WAF。 | [方法条目](../source-audit.md) |
| 注册与邀请邮件中的 HTML 内容和脚本执行分开 | 保存正文及 OneNote 分享输入、邀请邮件的红色 h1 图片说明用户名或留言可能进入邮件 HTML。 | [方法条目](../by-type/xss.md) |
| 历史 URL 管道在去重与活跃访问前保留来源 | 保存流程组合 subfinder、waymore、gau、unfurl、httprobe、aquatone 及 shell 函数。 | [方法条目](../discovery/web-and-api.md) |
| MFA 反向代理演示区分会话转发和协议认证边界 | 保存图把凭据、一次性码和会话 cookie 经中间代理转发。 | [方法条目](../by-type/authn-session.md) |
| 前端对象 ID 与订单查询接口需要真实所有者对照 | 保存 Shopify 图片显示页面内 application/json 状态和带 shopify_customer_id 的请求；订单图则显示前端要求订单号与邮箱，而查询 API 返回配送地址等字段。 | [方法条目](../by-type/idor-access-control.md) |
| 前端配置中的公开标识和私密能力按类型区分 | 保存图片包含 OAuth client ID、Stripe 发布密钥及分析 SDK 写入标识等客户端配置。 | [方法条目](../by-type/info-secrets.md) |
| Gallia 车辆与设备测试保留传输类型和物理副作用 | 保存架构图覆盖 scanner、transport、配置、日志/数据库及硬件电源管理。 | [方法条目](../discovery/client-and-cloud.md) |
| WSUS 信任链核查区分更新来源、审批与客户端执行 | 保存拓扑展示 Microsoft Update、网络边界、更新服务器和客户端。 | [方法条目](../discovery/client-and-cloud.md) |
| Solidity 扫描结果绑定源码版本与部署实例 | 保存图包含源代码目录、扫描规则和高熵检测计数。 | [方法条目](../source-audit.md) |
| 工具清单按输入输出、身份和阶段组成覆盖矩阵 | 保存内容列出被动发现、抓取、参数、协议、漏洞及浏览器扩展等工具。 | [方法条目](../hunting-strategy.md) |
| HTTP 状态与 API 术语清单回到当前服务契约 | 保存状态图将 103 写成 Checkpoint 并列出若干非标准码，应以注册表纠正：103 是 Early Hints，122 位于未分配范围；其他非标准状态需保留实现语境而非当作通用协议定义。 | [方法条目](../discovery/web-and-api.md) |
| 搜索模式、WHOIS 与公开代码关系需要资产归属确认 | 保存 Google 通配 site 查询、Amass reverse WHOIS 和“每个资产都有 GitHub”建议。 | [方法条目](../discovery/passive-and-services.md) |
| 云资源枚举保留身份、区域、服务与分页缺口 | awsEnum 保存图显示 profile、region、EC2 和 JSON 输出。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 数据库错误与时间载荷用重复基线证明真实查询消费 | 保存内容有 SLEEP 参数、约六秒响应、INSERT 外键错误及历史 WordPress 计时脚本。 | [方法条目](../by-type/sql-injection.md) |
| 进程注入演示必须保留现有系统权限前提 | Dlinject 保存图显示库构造函数打印消息和 PID，原进程仍运行。 | [方法条目](../by-type/desktop-client.md) |
| 根路径跳转、robots 与框架路径不能代替子路由检查 | 保存图对比根路径 302 和子路径敏感文件 200；正文补充 robots.txt、框架管理路径及分隔符候选。 | [方法条目](../discovery/web-and-api.md) |
| 源码 JSON 中的失效链接先确认实际使用与信任 | 保存正文只描述页面源码 JSON 里有 broken link，没有后续消费和可接管证据。 | [方法条目](../by-type/subdomain-takeover.md) |
| 路径候选与登录错误参数需要确认文件消费者 | 保存帖列出路径分隔、编码及空字节候选，另帖描述从登录错误找到 filename 参数后检查 LFI。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 高并发 DNS 枚举保留解析器与未完成覆盖 | aiodns 保存图以高并发对字典进行解析并显示发现数量。 | [方法条目](../discovery/passive-and-services.md) |
| 多主题技巧图把每种消费者与成功条件独立验证 | 四张保存图跨数据库函数、表单、渲染器、Markdown、资源预算、HTTP、缓存、文件方法、URL、token、代码托管和认证。 | [方法条目](../experiment-design.md) |
| 方法覆盖头先证明实际后端方法和文件状态 | 保存图中直接 PUT 返回 403，GET 携带方法覆盖头返回 200。 | [方法条目](../by-type/file-upload.md) |
| 历史报告回归先刷新授权和部署条件 | 保存正文建议对历史已报告问题重新测试。 | [方法条目](../experiment-design.md) |
| 接管候选管道区分旧输出、指纹与可控制性 | 保存 shell 管道将结果追加到文件后继续连接后续工具；stdout 已重定向可能使后续阶段没有实际输入，追加还会混入历史候选。 | [方法条目](../by-type/subdomain-takeover.md) |
| README 凭据与数据库界面分别记录权限事实 | 保存图出现数据库管理界面和数据库列表，正文把 README 凭据作为来源线索。 | [方法条目](../by-type/info-secrets.md) |
| 上传变体分别核对请求、WAF、保存和最终消费 | 保存帖建议扩展名、魔术字节、MIME 与 cookie 变化，Cloudflare 图片中的 multipart 请求携带 PHP 命令载荷但被 403 阻断。 | [方法条目](../by-type/file-upload.md) |
| 移动 SSL unpin 与 root 工具只说明受控设备条件 | 保存正文列出 root、调试与 SSL unpin 工具。 | [方法条目](../discovery/client-and-cloud.md) |
| 个人信息与付款功能覆盖采用获授权测试数据 | 保存正文提醒高风险功能可能只在填入 PII/PFI 后出现。 | [方法条目](../business-modeling.md) |
| 盲 XSS 自动化保留载荷归属与真实后续处理器 | 保存 SXSS 帮助页只展示提取、生成和检测命令，另一管道在历史 URL 请求的 User-Agent 注入外部脚本。 | [方法条目](../by-type/xss.md) |
| Burp 模板生成与快捷键操作保留选择范围和副作用 | 保存 Nuclei Generator 界面只提供二进制位置、保存路径、作者及窗口选项。 | [方法条目](../discovery/records-and-incremental.md) |
| 披露项目数据库将授权、善意条款与奖励分开 | 保存的 disclose.io 历史统计将 Good-faith、Authorization、Bounties 和 Swag 分列，说明这些不是同一政策字段。 | [方法条目](../scope-and-rules.md) |
| 导出 PDF 中的云字段不能直接证明元数据 SSRF | 保存图在本地 PDF 中显示类似云身份及会话字段，但没有完整请求、元数据地址、出口或有效权限的来源证据。 | [方法条目](../by-type/document-rendering.md) |
| SQL 注入到 Web 执行链分阶段确认有效权限 | 保存 sqlmap 输出显示数据库写入 stager 后经 Web 触发，最终用户是 www-data。 | [方法条目](../by-type/sql-injection.md) |
| 请求走私工具列表只提供协议边界选择线索 | 保存正文按 HTTP、H2C、WebSocket 和 HTTP/2 列工具，图片仅为 h2csmuggler 封面。 | [方法条目](../by-type/request-smuggling.md) |
| 与分诊协作以范围、根因和最小复现建立共识 | 保存帖包含历史 accepted、duplicate 和 out-of-scope 统计及与分诊合作的建议。 | [方法条目](../reporting.md) |
| 语言切换核查路由、模板与权限的一致性 | 保存正文只提出换语言可能引入新问题，奖励截图的技术字段被遮盖。 | [方法条目](../discovery/web-and-api.md) |
| 浏览器 PoC 先证明跨站自有会话的真实状态变化 | 保存正文询问生成 CSRF PoC 后测试和发送的含义。 | [方法条目](../by-type/csrf.md) |

| 视频与调解材料保留同一请求和真实影响 | 保存帖对比 N/A 与 Triaged 状态，调解图展示影响说明、重新打开及严重性从 Critical 调为 Medium。 | [方法条目](../reporting.md) |
| 简单 HTML 标记用于定位消费者而非确认所有漏洞 | 保存技巧图把无害下划线标记投入输入并显示格式化结果。 | [方法条目](../by-type/xss.md) |
| 订单页面的参数与 HTML 响应不等于私人 API 数据 | 保存图中订单页面 GET 带订单号、邮箱和会话，返回 200 HTML。 | [方法条目](../by-type/idor-access-control.md) |
| 多源子域发现按来源、解析与归属组成候选集合 | 保存图和正文组合子域工具、搜索服务、版权、公司名、邮箱、DNS 与 RNN 预测。 | [方法条目](../discovery/passive-and-services.md) |
| 奖励通知中的公开披露许可与技术发现分开 | 保存奖励邮件明确将赏金金额与漏洞细节披露分开，图片没有展示项目越权的实际请求。 | [方法条目](../scope-and-rules.md) |
| CSRF 决策图需要真实浏览器发送和服务端状态证据 | 保存流程图覆盖移动入口、cookie、token 缺省、跨会话 token、可预测性、JSON、简单内容类型以及 CORS。 | [方法条目](../by-type/csrf.md) |
| 扫描管道的反射命中与浏览器执行保持独立 | 保存管道包括 nuclei 模板、kxss、历史 URL、cleanP/injectP、uro、qsreplace 和 httpx 标记匹配。 | [方法条目](../by-type/xss.md) |
| 页面提示与属性绕过回到原始字符及最终 DOM | 保存图可见浏览器提示，正文包含反射标记、脚本语法平衡、属性内角括号编码以及使用 Inspect 与页面源码的建议。 | [方法条目](../by-type/xss.md) |
| 片段与百分号编码变化不能作为通用 URL XSS 绕过 | 保存正文把编码 javascript 形式和追加井号后的未编码形式进行对比，两者同时改变了编码和片段。 | [方法条目](../by-type/xss.md) |
| 后执行工具及 postMessage 的数据能力以无害标记确认 | toxssin 保存图显示 handler 请求、来源和已有活动会话，正文另建议通过 window.opener 与通配 postMessage 发送 localStorage。 | [方法条目](../by-type/xss.md) |
| HTML 与 CSS 注入的影响需要可达业务链 | 保存图显示标题大小变化以及未证明身份窃取的影响主张，正文询问如何提高 HTML/CSS 注入影响。 | [方法条目](../impact-and-acceptance.md) |
| 授权相关输入的 SQL 错误要绑定真实来源字段 | 保存图片的请求为登录相关 GET 与 cookie，错误正文展示用户名条件、数据库名称和 SQL 语法错误；文章标题提到 Authorization token，但图中不能建立同名头到查询的完整映射。 | [方法条目](../by-type/sql-injection.md) |
| 默认凭据清单只形成配置核查项 | 保存正文枚举大小写、空值和常见管理员凭据。 | [方法条目](../by-type/authn-session.md) |
| APK 静态提取绑定应用包和规则版本 | APKLeaks 2.2.0 帮助图展示输入文件、输出位置、自定义模式和 JSON。 | [方法条目](../discovery/client-and-cloud.md) |
| 无头截图保留页面来源与脚本访问范围 | 保存图展示 nuclei 对单 URL 和列表使用 headless screenshot 模板。 | [方法条目](../discovery/records-and-incremental.md) |
| 隐藏字段与特殊路径重定向先证明实际导航 | 保存正文涉及隐藏 URL 字段、特殊点号路径及重定向参数与 RXSS 组合。 | [方法条目](../by-type/open-redirect.md) |
| CVE 模板与引用记录保留历史版本及证据层级 | 保存 nuclei 输出以 CVE 标签和 medium 列出多条 Scorm/player 路径；另一保存图列出 Known 的历史版本、Host Header Injection 描述与参照文章。 | [方法条目](../discovery/records-and-incremental.md) |
| 社区模板归集与扫描数据库保留可追溯来源 | cent 保存图展示多仓库克隆和去重，dbns 正文只说明 Postgres 集成。 | [方法条目](../discovery/records-and-incremental.md) |
| 公开 cookie 与第三方 passkey 线索不能直接复用会话 | 保存正文建议把公开 cookie 加入每次请求并关注第三方 pass key。 | [方法条目](../by-type/authn-session.md) |
| S3 列举到第三方密钥权限按每步证据拆解 | 保存正文描述子域发现、S3 列表、读取 JS 中的第三方 Authorization key 和访问员工信息，图片只显示接受状态。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 路径与路由别名的 40X 差异须确认同一业务权限 | 保存内容包含 bypass-url-parser 的线程、超时、header 与 spoof-IP 帮助，WordPress wp-json/rest_route 别名及 login 双斜杠对比。 | [方法条目](../discovery/web-and-api.md) |
| 模板指纹决策树需要排除客户端计算并限制能力结论 | 保存思维图从算术、字符串及闭合条件到 Smarty、Mako、Jinja/Twig 等候选，再列函数、扩展、自有对象、循环、变量和文件/执行能力。 | [方法条目](../by-type/ssti.md) |
| 缓存端口污染与可用性影响用受控复用证明 | 保存正文描述用端口改变与缓存污染产生临时 DoS，但没有保存完整请求链。 | [方法条目](../discovery/web-and-api.md) |
| CGI 命令参数与 uid 文本匹配先确认消费者 | 保存单行命令为历史路径和参数发送请求，再按 uid= 筛选响应。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 大体积错误页作为调试泄漏候选而非评级 | 保存正文描述 400/500 页面包含 DB、SMTP、AWS、IP 或源码，并建议检查较大错误正文。 | [方法条目](../by-type/info-secrets.md) |
| 共享 VHOST 或环境不自动扩展范围和影响 | 保存正文声称 sister domain/VHOST 的漏洞会自动影响范围内域名，应纠正为两个独立判断：该资产与动作当前是否授权，以及现有证据是否确实跨越共享环境的隔离边界。 | [方法条目](../scope-and-rules.md) |
| 多领域扫描目录按实际入口与证据能力选择 | 保存目录列智能合约、移动包、二进制、隐私、子域、数据库、认证、IoT、XSS、源码和持久威胁等类别。 | [方法条目](../hunting-strategy.md) |
| 范围正则要按 URL 组件验证根域与子域 | 保存正文对比匹配点号前缀和斜杠或点号前缀的 Burp Scope 表达式。 | [方法条目](../scope-and-rules.md) |
| 付款沙箱与测试链必须确认当前环境和资产许可 | 保存正文建议在 staging/test 环境使用付款沙箱或加密货币 testnet。 | [方法条目](../business-modeling.md) |
| CVSS 的 PR 记录利用前权限并注明评分版本 | 保存正文争议是 IDOR 要求认证后 PR 能否为 None。 | [方法条目](../impact-and-acceptance.md) |
| credential_process 配置写入到执行需实际消费链 | 保存的 AWS 文档图说明 credential_process 由所选配置驱动外部程序，读取 stdout 的 JSON 凭据并以非零退出码报告失败。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 修改 JWT 角色字段必须保持合法格式与验证链 | 保存正文用 user/role 字段变更提出管理员假设，其中示例并非完整合法 JSON。 | [方法条目](../by-type/jwt.md) |
| ID 筛选与形状变化分开验证资源所有者 | 保存脚本用 grep 找 ID，两个图中的正则有位置及字符类问题，且星号允许空匹配；追加文件又可能包含旧结果。 | [方法条目](../by-type/idor-access-control.md) |
| JavaScript 抓取结果区分资源标识、配置与秘密 | Pinkerton 保存图列出少量 JS 资源及 AWS URL、Access Key ID 和 Firebase URL 候选。 | [方法条目](../by-type/info-secrets.md) |
| 目录枚举帮助页只定义输入与操作模式 | ZenBuster 帮助图包含 URL/IP、HTTPS、端口、字典、目录扩展名、输出与详细模式。 | [方法条目](../discovery/web-and-api.md) |
| 错误页内的文件正文与路径规范化分别核查 | 保存 ThinkPHP 图展示含父目录的 errorfile 参数和错误页中的 passwd 样式内容；另一正文提到 Windows 空格规范化但没有保存具体例子。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 无 DNS 的 VHOST 发现保持 Host、基线与范围关联 | 保存 ffuf 图先对不存在的 Host 获取长度 612 基线，再按该长度过滤，得到 dev 候选。 | [方法条目](../discovery/web-and-api.md) |
| OOB 回调记录与扫描器漏报独立核查 | 保存 Interactsh 图列出 DNS/HTTP、时间、请求及 favicon 的浏览器头，正文提到静态托管可配合 XSS/XXE；Freddy 正文则说明历史 DNS 回调未形成报告的问题。 | [方法条目](../discovery/records-and-incremental.md) |
| ThinkPHP 历史调用图保留输出来源和部署条件 | 保存请求包含路由到函数调用及系统信息消费者，错误页面中显示 Windows 系统信息。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 历史子域下载与服务指纹不能直接确认接管 | 保存 SecurityTrails API 示例只展示带 key 的子域请求，正文建议将当前和历史名称送入 subzy。 | [方法条目](../by-type/subdomain-takeover.md) |
| phpMyAdmin setup 可达性与配置写入权限分开 | 保存正文给出 setup/index.php，图片仅为未认证可达的报告标题。 | [方法条目](../by-type/authn-session.md) |
| 大小写变化的限流候选对照规范化后的账号 | 保存奖励标题提到登录大小写导致限流差异和 ATO，但没有完整请求链。 | [方法条目](../by-type/authn-session.md) |
| 表单注入的动作、来源与 token 消费逐项确认 | 保存正文提出表单 action、同站 cookie 和 CSRF token 的影响方向。 | [方法条目](../by-type/xss.md) |
| 在线 SQL 沙箱采用独立示例并注明方言 | 保存正文列在线查询沙箱。 | [方法条目](../by-type/sql-injection.md) |
| 奖励资格时间线与漏洞复现及修复分开 | 保存正文描述报告提交、项目后来加入奖励范围和修复状态迁移。 | [方法条目](../reporting.md) |
| 第三方登录建议先识别真实信任与主体绑定 | 保存正文建议应用采用另一服务登录时读取其文档，外链案例全文未保存。 | [方法条目](../by-type/oauth-oidc.md) |
| 增量子域观察按真实差异保存而非重复通知 | 保存正文提出脚本获取新子域、定时处理并发出通知。 | [方法条目](../discovery/records-and-incremental.md) |
| SSRF 管道结束于 URL 改值只能算候选生成 | 两张保存图把子域发现、httpx 活跃筛选、wayback 历史、等号筛选与 qsreplace 串接，最终没有向目标发送改值请求。 | [方法条目](../by-type/ssrf.md) |

| 事件属性、搜索页和弹窗分别绑定解析上下文 | 保存正文给出 div/onmouseover 与 img/onerror 片段，本地图片展示搜索页叠加弹窗。 | [方法条目](../by-type/xss.md) |
| 子域来源扩展与公司关联按证据组成资产候选 | 保存表格比较 Subfinder 默认、all 和多个 API 来源的历史名称数量与耗时；另帖列出收购、ASN、WHOIS、搜索服务、端口、目录与代码库线索。 | [方法条目](../discovery/passive-and-services.md) |
| 接受、严重性和奖金分别记录来源证据 | 保存的 Google 工单图展示类型、严重性及接受状态变化，另一封邮件只展示已决定奖励和付款登记流程。 | [方法条目](../reporting.md) |
| 浏览器调试网络观察保留请求与响应原始证据 | cdb 保存图给出终端网络列表和请求/响应面板，正文说明使用 Chrome DevTools Protocol。 | [方法条目](../discovery/web-and-api.md) |
| 登录错误信息先验证差异而非扩大口令尝试 | WordPress 图区分 admin 的密码错误，Django 样式登录图只提示 staff 账号或密码不正确。 | [方法条目](../by-type/authn-session.md) |
| ASM 工具链保存阶段输出与增量差异 | Proteus 标题卡及保存正文组合 Subfinder、DNSX、HTTPX、Nuclei、Notify 与 Axiom。 | [方法条目](../discovery/records-and-incremental.md) |
| 模式发现和扩展加载分别核查完成状态与权限 | 保存正文描述 GraphCrawler 收集查询、变更、认证和猜测模式；InQL 图片显示加载进度及空 Output/Errors，并未显示加载完成。 | [方法条目](../by-type/graphql.md) |
| SQL 文件读取受数据库角色与服务器文件边界限制 | 保存帖的 MySQL 示例 SELECT * LOAD_FILE(...) 语法不正确：LOAD_FILE 是表达式函数，查询形式应是 SELECT LOAD_FILE(...)。 | [方法条目](../by-type/sql-injection.md) |
| 回调 URL 外观与实际 OAuth 接收方分开验证 | 正文给出 userinfo 中看似目标域名以及在恶意主机路径中放目标域名的候选。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存书目目录仅用于组织测试维度 | 已保存目录可见认证、会话、访问控制、输入边界与规范化、错误/审计，以及 HTTP、编码、序列化、内容及参数映射。 | [方法条目](../business-modeling.md) |
| 编码混淆载荷按实际解码链与消费者验证 | 保存帖组合 fieldset、NUL 表示、混合大小写事件属性、Unicode 转义函数名以及不含尖括号的编码片段；Akamai 图只有页面及 200 网络记录。 | [方法条目](../by-type/waf-bypass.md) |
| 隐藏参数先确认输入位置和独立消费者 | 保存正文描述 text.php、Arjun 隐藏参数和引号尝试。 | [方法条目](../discovery/web-and-api.md) |
| 时间和数据库错误信号保留阴性对照 | 保存 Burp 图展示 sleep 表达式与一次约 38.5 秒响应；Oracle 图展示输入片段、错误栈和 SYS 字样。 | [方法条目](../by-type/sql-injection.md) |
| 最小可逆状态变化与分诊结果分开 | 保存工单图确认 PoC 后要求恢复变更，作者回复已经恢复，随后标题和严重性调整。 | [方法条目](../experiment-design.md) |
| 对象、父子关系和动作需两账号真实状态对照 | 图片包含编辑/删除/更新 IDOR 票据列表；另一图给出两账号 AccountOpeningWizard、PlanId 和 ContactId 的联系人流程，collections/set 图则只展示请求。 | [方法条目](../by-type/idor-access-control.md) |
| Amass 速查按阶段与历史版本使用 | 保存速查图列出 intel、enum、viz、track、db、dns，以及组织/ASN、证书、被动来源、配置、关系展示和增量跟踪。 | [方法条目](../discovery/passive-and-services.md) |
| 客户端角色字段不能替代服务器权限验证 | 保存图用 Viewer/Editor/Admin、cookie 中两位角色串与改为 11 的示例说明提权候选。 | [方法条目](../by-type/idor-access-control.md) |
| 模拟器未实现行为与目标漏洞分开 | RESim/Simics 保存图出现设备型号、内核启动以及未实现寄存器/字段日志。 | [方法条目](../experiment-design.md) |
| 范围、披露渠道、技术确认与奖金分别核查 | BMW 保存邮件对一个 out-of-scope 发现给出酌情奖金，同时说当时不能确认；VDP/private BBP 正文则表达同范围但无奖金的不满。 | [方法条目](../scope-and-rules.md) |
| CVSS 版本向量与先决权限逐项给出证据 | 保存图显示 CVSS 3.1 的输入及 7.7 向量，另一正文称快速免费注册就应为 PR None。 | [方法条目](../impact-and-acceptance.md) |
| 邮件 HTML 渲染和浏览器脚本执行分别确认 | 保存邮件图片只展示回信中的 HTML 大图，正文谈到邮箱模板注入及潜在误导。 | [方法条目](../by-type/xss.md) |
| CDX 路径查询保留历史时间与归并策略 | 正文给出 CDX 查询中的路径、original 字段、statuscode 200 过滤与 collapse=urlkey。 | [方法条目](../discovery/passive-and-services.md) |
| 可达性筛选保留协议、失败和重定向语义 | LiveTargetsFinder 图分别生成 alive 域/IP/URL、SQLite 与 massdns/masscan/nmap 原始输出；s1c0n 图则出现 open ports 和 FAIL MAYBE HOST DIED；并发 curl 图包含 200、重定向、401 和 403。 | [方法条目](../discovery/records-and-incremental.md) |
| 管理 REST 错误指纹只用于候选识别 | F5 保存图访问管理认证路径，按 resterrorresponse 文本贴出 iControl REST API exposed 标签；正文和图片中的 shell 流程还存在语法问题。 | [方法条目](../discovery/web-and-api.md) |
| 配置与备份候选按实际文件和秘密用途验证 | 正文列出备份、数据库、配置、文本和 class 后缀，目录图展示 /old/configs/ 下的文件及空 config.php，另一帖声称工具和页面源码中找到口令。 | [方法条目](../by-type/info-secrets.md) |
| 分号路径变化核查规范化与真实保护动作 | 保存正文把普通路径 403 与前置分号参数路径 200 对比。 | [方法条目](../by-type/idor-access-control.md) |
| 竞争条件以业务不变量和提交结果验证 | 正文把竞争描述为两个过程在过期初始条件上执行，并以银行转账举例。 | [方法条目](../by-type/business-logic.md) |
| 断链域名提取需处理后缀、超时与实际消费者 | 保存脚本用 blc、ENOTFOUND、末两域标签和 WHOIS free 文本寻找断链候选；输出只展示一个 FOUND。 | [方法条目](../by-type/subdomain-takeover.md) |
| 移动及网页实验记录实际环境与许可 | Corellium 图片展示越狱 iPhone XS、iOS 14.4.1 和设备控制台；在线测试资源图按安全、移动、API、网页、自动化和性能分类。 | [方法条目](../experiment-design.md) |
| 自动复现需仍可审查输入、结果与清理 | 保存工单图片只给出 python3 exploit.py、附件数量和 Triaged/High 状态。 | [方法条目](../reporting.md) |
| 主域深入测试以业务模型和停止条件组织 | 正文建议在安全较好的目标上深入理解业务，另帖展示主域工单位置。 | [方法条目](../hunting-strategy.md) |
| 文件时间线与审计日志保留关联强度 | modDetective 图按日期显示 mtime 路径，Laurel 正文只描述把 audit 日志变成易处理的形式。 | [方法条目](../discovery/records-and-incremental.md) |
| 网络搜索速查先确认检索后端和时间 | Shodan Snippets 图列出查询、监控、下载和主动扫描等不同任务，另一帖标题称 Shodan 但图片明确给出 Netlas 的 geo/tag/certificate.validity/http.favicon.hash_sha256 等语法和 2022 日期。 | [方法条目](../discovery/passive-and-services.md) |
| 执行身份与反向连接前提分开证明 | 浏览器截图显示参数相关 id 输出及 www-data 身份；反向 shell 图列出 Bash、Netcat/FIFO、Python、Perl 和 PHP 执行入口，末尾 PHP 片段还被截断。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 反射管线和 DOM 执行验证分别计账 | 保存图片组合子域工具、HTTP 可达性、历史 URL、gf、qsreplace、curl grep 或 kxss，并将它们标为 DOM/XSS。 | [方法条目](../by-type/xss.md) |
| 客户端响应改写和弹窗缺失不能决定漏洞成立 | 正文询问自己改响应后产生 XSS，并把 Chrome 92 起跨源弹窗限制说成永久结论。 | [方法条目](../by-type/xss.md) |
| 详细错误页面按最小泄漏与输入类型评估 | PHP 保存错误图暴露版本、路径、调用栈与 JSON 解码后访问 Email 属性的片段。 | [方法条目](../by-type/info-secrets.md) |
| WebSocket 跨站验证保留握手与真实消息权限 | 视频帧包含 WebSocket onopen、send、onmessage 示例和跨站劫持解释。 | [方法条目](../by-type/csrf.md) |
| 依赖混淆候选需绑定真正的解析和安装流程 | 图片用 HTTPX 获取 package.json/package-lock.json，再交给 confused 工具。 | [方法条目](../source-audit.md) |
| SSRF 地址变体先核查实际解析与出口约束 | 保存正文列出十六进制/整数/零地址和未加方括号 IPv6 片段；思维图还列协议、重定向、短地址和内部网段。 | [方法条目](../by-type/ssrf.md) |
| 盲 XSS 通知需绑定字段与真实下游展示 | 保存正文建议大量 User-Agent 请求，图片仅显示 XSS Hunter 通知标题。 | [方法条目](../by-type/xss.md) |
| 多词表组合先计算实际请求数 | ffuf 图为 URL 中 WORD、SPECIAL 和 FUZZ 分别命名词表并使用 clusterbomb。 | [方法条目](../targeted-fuzzing.md) |
| URL 收集保留污染输入和主动检查边界 | collector 图展示 pull/check、threads、with-subs、loadfile 和 outfile，并输出正常 URL、编码空白、历史载荷以及 .idea 路径。 | [方法条目](../discovery/web-and-api.md) |
| CORS 告警和真实浏览器非公开读取分开 | CORScanner 图列 reflect_origin、trust_any_subdomain、https_trust_http 和 credentials 标志；另一组图给出 withCredentials 的 XHR 与弹窗中的会话数据，且请求设置自定义 API 头。 | [方法条目](../by-type/cors.md) |
| 容器对照用于定位工具环境差异 | 正文建议 dirsearch 出问题时尝试容器版本。 | [方法条目](../experiment-design.md) |
| SVG 的图像和文档消费上下文分开 | 正文在 SVG 中放外部 script 引用作为 Blind XSS 候选。 | [方法条目](../by-type/file-upload.md) |
| IPv6 名称解析链须满足同网段和认证前提 | Pretender 保存图依次展示 Router Advertisement、DHCPv6 配置偏好 DNS、名称请求/响应及后续 SMB relay。 | [方法条目](../discovery/client-and-cloud.md) |
| APK 文本端点抽取保留工件与漏检边界 | 保存正文以 apktool 解包后用正则抽取 URL 并排除公共域字符串。 | [方法条目](../discovery/client-and-cloud.md) |
| favicon 匹配需保留哈希算法与归属对照 | favrecon 标题卡和正文提出用 favicon 查相关服务。 | [方法条目](../discovery/passive-and-services.md) |
| 人员选择端点先区分公开用途和私有字段 | 正文声称 Weaver OA /UserSelect/ 可未认证取得信息。 | [方法条目](../by-type/idor-access-control.md) |
| 二次验证阶段以服务器身份和受保护状态为准 | 正文建议直接请求下一端点或更改 Referrer，OTP 图片只显示部分遮挡手机号及四个输入框，后帖声称完整十位号码但没保存方法。 | [方法条目](../by-type/authn-session.md) |
| 证书和历史 DNS 只生成关联及原站候选 | 保存正文通过证书 Common Name/组织名、Shodan/Censys、SPF/TXT 和历史 DNS 寻找相关资产或原站 IP。 | [方法条目](../discovery/passive-and-services.md) |
| 托管域引用与资源可认领性分开 | 保存正文写 azurewebsites.com 子域引用并链接历史接管文章。 | [方法条目](../by-type/subdomain-takeover.md) |
| 云实验镜像启动不等于资源部署与测试完成 | TerraformGoat 保存图展示 aliyun 0.0.4 镜像拉取、run 和 exec 后提示符。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 爬取与改值管线仅产生 SSRF 输入候选 | 正文组合 hakrawler 深度 5、等号筛选和 qreplace 结尾，没有向修改后的 URL 发请求。 | [方法条目](../by-type/ssrf.md) |
| 隐藏端点和参数发现保持方法与内容类型 | 保存图从 JS Miner/Burp Spider、代码搜索、CDX/Wayback 获取候选，再经代理观察和 Arjun 的 GET、POST、JSON、XML 寻参；正文建议重点看注册页面。 | [方法条目](../discovery/web-and-api.md) |
| 前端凭据候选按用途和当前权限边界处理 | 保存奖金图声称 JavaScript 文件泄漏 API key，正文有“找到 token 就到处试”的建议。 | [方法条目](../by-type/info-secrets.md) |
| 多类思维图转换为消费者和状态边界实验 | 保存图列出缓存/CPDoS、头部、方法、CRLF、上传、XSS、重置、IDOR、CSRF、DoS、403 与 2FA 等分支。 | [方法条目](../experiment-design.md) |
| URL 模式筛选保留原始来源与排除理由 | Parshu 标题及正文描述类似 gf 的正则过滤。 | [方法条目](../discovery/records-and-incremental.md) |
| 查询解码与导航协议检查需覆盖真实语法 | 保存本地页面图通过 URLSearchParams 取得 redirectURL，正则只检查含有类似冒号/双斜线的片段，随后赋给 location.href；另一图中编码 U+2028 的 javascript URL 出现 confirm 弹窗。 | [方法条目](../by-type/xss.md) |
| 临时凭据字段截图不补出 SSRF 或权限链 | Slack 保存图显示名为 awskeys.xlsx 的上传内容，含被遮挡的 AccessKeyId、SecretAccessKey、Token 和 2019 过期时间。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 参数名称和类型变化按实际解析器对照 | 保存技巧图把 parameter、parameter[] 和 parameter[id] 作为候选。 | [方法条目](../targeted-fuzzing.md) |
| 扫描器能力数量与可执行操作预算分开 | scan4all 卡声称大量 PoC、密码尝试、指纹、协议和端口规则。 | [方法条目](../targeted-fuzzing.md) |
| 图片地理信息以实际元数据与隐私意图评估 | exifLooter 卡宣称所有图片 URL/目录地理信息并可关联地图。 | [方法条目](../by-type/info-secrets.md) |
| 搜索索引命中先最小确认 Elasticsearch 权限 | 正文通过搜索服务、9200 端口和目标关键字寻找 Elasticsearch，并建议转储全部内容。 | [方法条目](../by-type/info-secrets.md) |

| 验证账户资料编辑要比较入口一致性和服务端不变量 | 保存正文描述认证账户的姓名、出生日期在普通编辑页受限，却可通过注册入口修改。 | [方法条目](../by-type/business-logic.md) |
| OTP窗口与本地响应改写必须回到服务端认证状态 | 图片提供删除验证码字段、改响应、不同验证方式和计时窗口等候选线索；另一正文将自改响应为500泛称高成功率。 | [方法条目](../by-type/authn-session.md) |
| 姓名进入邮件HTML时先证明渲染与可信内容混淆 | 正文将姓名字段中的图片标记带入邮件，并询问能否提高影响；保存字符串含不完整的URL格式。 | [方法条目](../by-type/xss.md) |
| 对象标识与版本字段差异需要身份和对象读回对照 | 保存内容包括路径ID与查询ID的403/200差异、相邻消息的401/200截图，以及删除版本字段后422消失。 | [方法条目](../by-type/idor-access-control.md) |
| XSS工具与编码候选按输入到消费位置逐层核对 | 保存清单混合抓历史参数、扫描器、静态分析及编码技巧。 | [方法条目](../by-type/xss.md) |
| 检索披露政策与管理员入口后要另行确认测试范围 | 搜索正文给出管理员入口和披露政策关键词。 | [方法条目](../scope-and-rules.md) |
| 域名候选生成先校验域名与URL输入约定 | 保存图片用sed为词表加域名再交给探测器，正文提到向域名枚举工具传入含协议的URL。 | [方法条目](../discovery/passive-and-services.md) |
| 目录索引与调试页只提取最小暴露证据 | 图片分别显示Apache目录索引和phpinfo字段，正文列出Git/SVN元数据路径。 | [方法条目](../by-type/info-secrets.md) |
| 熟悉功能与新增变化要转化为可复核的工作假设 | 保存正文强调深度熟悉一个项目、关注新功能和减少低收益工具折腾；配图主要是奖励和状态。 | [方法条目](../hunting-strategy.md) |
| Unicode换行候选必须追踪实际响应头字节 | 正文把一组多字节百分号编码作为CRLF候选。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 侦察流程图中的阶段和工具不能替代资产证据 | 保存ARWAD流程图混合组织资料、域名、HTTP、端口、接管、内容、Git、JS及历史记录。 | [方法条目](../discovery/passive-and-services.md) |
| VLAN跳跃概念须绑定实际交换网络和隔离条件 | 保存内容区分交换机伪装和双标签思路。 | [方法条目](../discovery/client-and-cloud.md) |
| 客户端角色参数与转发IP声明要验证服务端信任链 | 正文分别提出把console角色参数改成admin和堆叠localhost转发头。 | [方法条目](../by-type/idor-access-control.md) |
| 训练目录和容器桥接图要转成可重置的隔离实验 | 保存目录列出训练站点，WebSploit图把Web和API靶场放在不同Docker桥接子网。 | [方法条目](../experiment-design.md) |
| 上传清单需分开后缀校验内容识别和执行处理器 | 保存的部分清单包含双后缀、大小写、子串匹配、SVG、MIME与魔数，底部未保存部分按用户要求计覆盖。 | [方法条目](../by-type/file-upload.md) |
| 会话管理界面与RCE示意图必须明确已有执行前提 | Kage图片显示生成器、处理器与会话字段，另一图片是命令执行概念图。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 第三方枚举界面要同时记录覆盖和目标数据披露 | 图片展示聊天机器人工具菜单和第三方子域查询的私密扫描选项。 | [方法条目](../discovery/passive-and-services.md) |
| 标签闭合与事件属性候选要追踪持久化消费上下文 | 保存图片列出不同标签闭合，正文给出h1事件及重复的img事件字符串。 | [方法条目](../by-type/xss.md) |
| Salesforce接口工具的帮助页只说明可用检查入口 | Cirrusgo帮助截图列出目标、应用、检查、请求头与代理等选项。 | [方法条目](../discovery/web-and-api.md) |
| 移动取证面板的告警和流量必须与采集条件一起解释 | PiRogue图片展示设备、流、域名、字节数和告警面板。 | [方法条目](../discovery/client-and-cloud.md) |
| LFI参数名词表只提供入口优先级 | 保存图片列出page、file、path、template等候选名称。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 数学表达式示意要排除客户端计算和固定输出 | 图片以模板表达式输出49解释SSTI，未给出真实响应或引擎。 | [方法条目](../by-type/ssti.md) |
| NDA网络来源与自定义头要求须保留规则版本 | 正文提醒项目可能增加NDA、VPN或自定义头要求。 | [方法条目](../scope-and-rules.md) |
| 混淆脚本先静态追踪字符串构造和真实DOM写入 | 保存图片包含属性索引、隐式字符串转换、递增操作和innerHTML构造，末尾有注释中的alert。 | [方法条目](../by-type/xss.md) |
| 历史反序列化通告需区分写文件与可执行落点 | 保存Full Disclosure目录和SoListingTabs通告片段描述数据库、会话及Twig文件系统对象链。 | [方法条目](../by-type/deserialization-rce.md) |
| 接管扫描器的Confirmed标签仍需独立资源控制证据 | DNS Reaper图片以未注册CNAME给Confirmed、不可解析给Potential。 | [方法条目](../by-type/subdomain-takeover.md) |
| 从GET改为POST要核对处理器解码和浏览器执行 | 图片声称URL编码阻止XSS时改用自动提交POST。 | [方法条目](../by-type/xss.md) |
| JavaScript跳转列表要追踪具体导航调用和允许协议 | 保存正文罗列JavaScript样式的跳转字符串。 | [方法条目](../by-type/open-redirect.md) |
| 网络索引与连接快照的结果必须保留来源和时效 | 图片给出Censys服务标题查询、Shodan ASN导出、搜索来源目录及Windows连接快照；正文介绍基于Shodan的端口或子域工具。 | [方法条目](../discovery/passive-and-services.md) |
| 自动化误报要以控制组和实际反馈校准 | 正文用多次误报概括自动化无用。 | [方法条目](../experiment-design.md) |
| 表单SQL检测先排除登录失败与通用错误页 | Logsensor和SQLiDetector卡片分别宣称POST表单、长度或错误正则检测。 | [方法条目](../by-type/sql-injection.md) |
| 盲XSS通知需要最小标记关联持久输入和实际消费者 | 保存图片显示前端prompt、通知邮件、回调列表及带有打码字段的渲染页面。 | [方法条目](../by-type/xss.md) |
| 索引到默认登录页仍须许可和有效角色核验 | 正文提到端口检索和默认凭据，图片只有备份及管理员访问的P1标题。 | [方法条目](../by-type/authn-session.md) |
| 转发头字典要区分代理信任问题与服务端真实取址 | 保存图片混合转发IP、端口、协议、原始URL及错拼头。 | [方法条目](../by-type/ssrf.md) |
| 编码JSON与缓存SQL输出须用新鲜配对证据确认 | 图片显示URL与Base64包裹的JSON搜索值，以及约5.66秒和703毫秒的对照；另图显示SQLmap已恢复旧缓存且数据库计数失败。 | [方法条目](../by-type/sql-injection.md) |
| 管理员文件编辑功能先判断预期权限与最小落点 | 保存图片显示Pimcore服务端文件浏览器编辑public/index.php，正文称本地或演示凭据可令测试安全。 | [方法条目](../by-type/file-upload.md) |
| 过滤器放行要与最终事件属性消费分别验证 | 正文比较onxxx被403而xxx得到200，配图列出声称绕过Cloudflare的实体、属性、srcdoc和脚本协议候选。 | [方法条目](../by-type/waf-bypass.md) |
| 清理与时间戳工具只能作为证据完整性风险线索 | 保存帮助页包含痕迹清理、ETW绕过和时间戳改写选项。 | [方法条目](../discovery/records-and-incremental.md) |
| 已确认漏洞可生成规则但需验证组织实际调用链 | 保存图片强调理解项目编程模式后用Semgrep寻找同类问题，正文涉及命令注入和缺少认证模式。 | [方法条目](../source-audit.md) |
| 404产品指纹与扩展名枚举应回到具体输出上下文 | 保存正文描述从404和PHP产品指纹到扩展路径、参数及路径XSS的发现顺序，图片只有奖励。 | [方法条目](../by-type/xss.md) |
| 命令引号和防护告警差异不能证明通用规避 | 保存正文声称给certutil名字加引号绕过某防护产品，未提供完整环境证据。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 令牌验证和Cookie传输应分开检查 | 保存图对比会话查找和令牌验证，正文题名涉及JWT技术。 | [方法条目](../by-type/jwt.md) |
| Origin前后缀候选必须证明浏览器读取真实保护数据 | 正文提醒CORS前后缀匹配，图片是Prefix match奖励标题。 | [方法条目](../by-type/cors.md) |
| 公开报告附件目录只作为来源索引 | 保存图片展示漏洞类别文件夹，正文介绍公开PoC视频下载工具。 | [方法条目](../reporting.md) |
| AWS训练首页只支持学习范围不能替代云权限证据 | 同组两条保存图片均为flAWS首页，说明AWS配置陷阱和可只读提示的训练方式。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 依赖混淆线索必须绑定实际解析规则和构建 | 保存图展示内部旧包与外部新包竞争，另一正文说JS工具帮助发现依赖；奖励配图没有解析细节。 | [方法条目](../source-audit.md) |
| HttpOnly不能保护服务端另行返回的可读令牌副本 | 保存正文指出XSS可调用返回会话令牌的端点，图片显示认证用户接口JSON中包含与Cookie相似的认证字段。 | [方法条目](../by-type/authn-session.md) |
| 缓存指令含义与真实共享缓存行为必须分别核对 | 保存正文称有no-cache、private仍发现缓存污染。 | [方法条目](../discovery/web-and-api.md) |
| 同意字段与删除申请要验证后台状态和申请人身份 | 保存正文分别提出移除同意字段，以及未认证DSAR表单可能导致账户删除。 | [方法条目](../by-type/business-logic.md) |
| Host头问题需要追踪URL构建及真实消费方 | 正文仅命名Host header漏洞并强调扫描后人工验证，图片只有奖励。 | [方法条目](../discovery/web-and-api.md) |
| 开放管理员注册页与菜单可见仍需有效权限证据 | 保存图片显示/admin/register.php和注册表单，另图显示Hello test菜单及路径扫描。 | [方法条目](../by-type/idor-access-control.md) |
| Cookie结构差异要核对服务端身份及签名约束 | 正文从两个账户的Cookie差异推测权限并提出拼接。 | [方法条目](../by-type/authn-session.md) |
| 路径词表组合先做本地展开和请求预算 | 保存正文介绍路径生成工具。 | [方法条目](../targeted-fuzzing.md) |
| Cognito注册请求只能作为身份绑定检查入口 | 保存图片是SignUp请求中的Username与用户属性，没有响应。 | [方法条目](../by-type/authn-session.md) |
| 退出后本地存储残留与服务端会话撤销分别核对 | 正文和奖励题名指出退出后localStorage保留用户集合。 | [方法条目](../by-type/info-secrets.md) |
| VBA分阶段写入代码的宣称需与静态依赖和遥测区分 | 保存片段下载到临时文本再调用移动命令，并关闭证书检查、依赖未展示的执行函数；注释声称防护绕过。 | [方法条目](../source-audit.md) |
| XSS探测流程应保留单变量过滤与消费证据 | 保存图片建议先试无害HTML、残缺标签、编码控制字符和黑名单变体。 | [方法条目](../by-type/xss.md) |

| 短链接跳转后的目的地址必须重新核验 | 保存正文描述封禁元数据URL后用短链接绕过，图片只显示短链生成；另一图强调影响受服务器实际网络能力约束。 | [方法条目](../by-type/ssrf.md) |
| SQL阶段清单需要查询上下文与数据库文件权限边界 | 图片把报错、列数、UNION、库信息和LOAD_FILE并列。 | [方法条目](../by-type/sql-injection.md) |
| 组织ASN和证书枚举需要校验实际参数与来源 | 保存图片提供Amass组织转ASN、高DNS预算及并行调用，Cert4Recon图只有未指定目标的帮助，正文将Smap称为Nmap替代。 | [方法条目](../discovery/passive-and-services.md) |
| XSS流水线的中间结果必须保留原始输入和消费证据 | 保存正文和图片将爬虫、历史URL、过滤、去重及Dalfox/Nuclei连接，另用正则找message监听器。 | [方法条目](../by-type/xss.md) |
| 修复后的IDOR复测要保持原始证据和当前许可 | 保存图显示同一更新帖子问题及两次修复绕过题名。 | [方法条目](../by-type/idor-access-control.md) |
| 本地注入与反向会话演示要明确已有执行权限 | Nim图片显示进程打开、内存写入和线程创建；Hoaxshell图片先生成载荷并等待已有执行，再展示身份、系统和防护进程。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Grafana面板可见须核对实际身份与数据访问 | 保存图片显示登录样式的仪表盘管理页及历史版本，正文只有写作宣传。 | [方法条目](../by-type/idor-access-control.md) |
| 范围聚合工具与政策搜索都需要回到原始规则 | 正文给出Goodfaith过滤公共范围和历史披露数据库统计，图片列出政策与奖励检索词。 | [方法条目](../scope-and-rules.md) |
| 方法切换与存储XSS链必须分别验证跨站写入和消费 | 保存正文列出CSRF方法、令牌、会话及Cookie条件，并提出POST改GET将self-XSS转为有效问题；图片仅有CSRF存储XSS题名。 | [方法条目](../by-type/csrf.md) |
| 渗透测试是否覆盖用户业务风险取决于明确目标 | 保存问题把账户接管与业务逻辑和系统访问相比较。 | [方法条目](../business-modeling.md) |
| 共享分析代码和内部域名仅是组织关联候选 | 图片显示公开Analytics标识与多个关联域名，正文建议以内部域名扩展代码或情报检索。 | [方法条目](../discovery/passive-and-services.md) |
| 代码与搜索关键词须区分真实秘密和公开标识 | 保存图提供文件名、令牌关键词及搜索结果，报告截图只有秘密泄露题名。 | [方法条目](../by-type/info-secrets.md) |
| 历史URL和服务索引不能直接升级为实时漏洞清单 | 正文移除协议后收集历史URL，以证书主体搜索到IP并串联探测与扫描；图片列出数据库、SSH、FTP、邮件和管理页指纹。 | [方法条目](../discovery/passive-and-services.md) |
| IIS的WebDAV路径只能作为功能发现假设 | 正文建议IIS上检查WebDAV目录。 | [方法条目](../discovery/web-and-api.md) |
| 新功能与期限应形成有限可验证的工作单元 | 保存正文提醒老项目关注新增功能，并谈没有期限导致目标模糊，奖励图未提供过滤机制。 | [方法条目](../hunting-strategy.md) |
| 支持工单归属要核对注册邮箱验证和消息路由 | 正文指出从自有注册邮箱向支持系统发送邮件，检查未验证注册邮箱与工单关联。 | [方法条目](../by-type/authn-session.md) |
| 复测和追问节奏应尊重明确停止条件 | 保存报告截图明确要求停止测试，另一正文建议每日催问。 | [方法条目](../reporting.md) |
| 流量筛选示意图不能证明当前防护规避 | RedGuard图以IP、时间、黑名单和请求检查区分不同来源并连接C2。 | [方法条目](../discovery/client-and-cloud.md) |
| SVG事件与表情候选需要实际解码和插入上下文 | 图片展示SVG候选与弹窗，另有localhost表情乱码加img事件；正文给出不同事件字符串。 | [方法条目](../by-type/xss.md) |
| 结账页脚本影响只用自有假数据评估 | 正文因alert受限而声称记录结账输入。 | [方法条目](../by-type/xss.md) |
| 411与TE候选不能独立证明请求解析分歧 | 正文询问加入Transfer-Encoding后出现411，另一条只引用TE混淆训练。 | [方法条目](../by-type/request-smuggling.md) |
| 索引展示源代码密钥需最小打码证据而非复用 | 保存图片确实显示PHP客户端构造中的认证字段及历史网络索引。 | [方法条目](../by-type/info-secrets.md) |
| 扫描模板的非破坏性宣称需核对实际动作 | J2EEScan图、Nuclei输出与批量CVE命令提供候选路径、规则标签、端口和并发值。 | [方法条目](../experiment-design.md) |
| 改邮箱与外部登录接口要验证身份绑定及会话结果 | 图片分别显示带认证头的邮箱修改成功，及provider、邮箱、验证字段和返回令牌的外部登录请求。 | [方法条目](../by-type/authn-session.md) |
| Firebase配置中的标识与数据授权是不同边界 | 保存图片是客户端Firebase配置，未提供数据库规则或数据响应。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| VLAN双标签工具帮助只提供隔离实验参数 | 保存帮助列出接口、本地及目标VLAN、两端IP，正文只有工具介绍。 | [方法条目](../discovery/client-and-cloud.md) |
| 侦察API清单需记录数据来源与实际使用约束 | 保存表格列公司、价格或免费、联系方式及工具使用，但字段很少。 | [方法条目](../discovery/passive-and-services.md) |
| 自动安全修复界面要核对写权限与实际变更 | 保存StepSecurity图显示公开仓库输入、登录、修复预览和创建PR按钮。 | [方法条目](../source-audit.md) |
| 限流与输入扫描须保持账户和时间窗口边界 | 正文包含SQL词表造成生产账户锁定的例子、X-Forwarded-Host限流候选及WP登录无速率限制被评Critical的宣称。 | [方法条目](../by-type/authn-session.md) |
| 产品ID与价格字段需要服务端业务不变量对照 | 保存图片只显示POST中的PID和金额占位符。 | [方法条目](../by-type/business-logic.md) |
| 静态查询容器输出须绑定源版本和实际覆盖 | CodeQL Docker图展示语言、源码路径、挂载、查询套件、输出与覆盖旧数据库选项。 | [方法条目](../source-audit.md) |
| 目标词表与环境名称扩展先计算候选和预算 | 正文提出自建子域词表、由prod猜测stage等环境及目标专属词表，但未保存续篇。 | [方法条目](../targeted-fuzzing.md) |
| 403与路径附加变体需要证明同一受保护资源 | 正文以env加路径尾段声称绕过，配图是奖励，工具卡片只有目录扫描宣称。 | [方法条目](../by-type/idor-access-control.md) |
| 训练题目目录须绑定版本与自有业务不变量 | 保存DeFi与PHP练习页列出独立挑战、命令入口、修复、本地或管理员限制及不同哈希类型。 | [方法条目](../experiment-design.md) |
| 已有cmd处理器输出不等于特定CVE的完整证明 | 保存图片访问cmd.jsp并显示命令表单与文件名，正文以历史Zimbra编号归因。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 移动插桩面板要明确设备权限与调试监听 | AndroidBud图展示Frida和LLDB启动停止、全地址监听及shell进程输出。 | [方法条目](../discovery/client-and-cloud.md) |
| SQL候选排序和单次延迟需要分开验证 | 保存的流水线把子域、历史 URL、去重、问号筛选和前 20 条串接到 SQL 测试；参数排名工具展示 page_id，另图展示 localhost 上已登录 WordPress 请求的排序参数及一次约 10 秒响应。 | [方法条目](../by-type/sql-injection.md) |
| Gadget枚举需要二进制版本与控制流前提 | Ropr 帮助页展示 ROP、JOP、syscall、范围、raw 和去重等枚举选项。 | [方法条目](../source-audit.md) |
| Shell字符变体必须绑定实际解析过程 | 保存图列出引号、通配符、空变量、反引号及命令替换等绕过候选，还混有相对路径读取。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 报告模板要填写可复现的证据而非只复制栏目 | 图中报告模板包含 Summary、Steps、Materials 和 Impact。 | [方法条目](../reporting.md) |
| XML外部实体候选需证明解析器与文件对应关系 | 保存截图展示 XML-RPC 请求、DOCTYPE 的 SYSTEM 文件候选和部分被遮挡响应，正文声称获取高权限哈希。 | [方法条目](../by-type/xxe.md) |
| 重定向工具选项要分别验证URL消费与响应头 | Oralyzer 帮助页展示目标列表、CRLF、自定义载荷、代理和历史来源等选项，并提示部分选项不能同时使用。 | [方法条目](../by-type/open-redirect.md) |
| 开发目录命中需用最小私有对象确认 | exos 截图把 .git、.hg 等目录列为 Found 或 Manual check，展示多个命中和待复核项。 | [方法条目](../by-type/info-secrets.md) |
| 多功能工具菜单需要逐项确定输入输出语义 | Hunter-Toolkit 图列出编码、散列、端口和 Whois 等菜单，并将 MD5 标作 Encryption。 | [方法条目](../experiment-design.md) |
| JAR文件名候选须核对实际加载内容 | look4jar 展示包含版本样式和通用名称的 JAR 候选列表，正文关联 Log4j RCE。 | [方法条目](../source-audit.md) |
| 历史压缩包候选与当前信息披露要区分 | 正文建议从 Wayback URL 中筛选 zip，截图仅展示厂商关于已保存信息移除的回复。 | [方法条目](../by-type/info-secrets.md) |
| 文件参数与固定遍历路径需要路由及内容对照 | 一帖建议浏览器遍历后查看 Burp history/logger 的 file 参数，另一帖把多个端口、固定下载日志路径和敏感文件匹配串为一行。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 重复参数和截断的Jira载荷不能直接证明反射执行 | 保存正文给出 Wallboard URL，包含重复 dashboardId 与被截断的 cyclePeriod 脚本候选。 | [方法条目](../by-type/xss.md) |
| 对象校验位置与实际读取对象必须一致 | 截图提出路径对象经过校验、查询参数对象被实际读取的错位；另一帖描述 CSV 下载链接将 ID 6 改为 5 后获得其他用户信息。 | [方法条目](../by-type/idor-access-control.md) |
| DNS接管工具的签名命中只形成候选 | DNSReaper 截图展示签名总数，以及 unregistered、unresolved 等确认或潜在分类。 | [方法条目](../by-type/subdomain-takeover.md) |
| HTTP探测筛选应保留结构化状态与每跳来源 | 保存一行把 HTTPX 的跟随跳转、状态、vhost、并发及排序输出接到 grep、cut 和空白删除。 | [方法条目](../discovery/passive-and-services.md) |
| 资产自动化要记录阶段覆盖和变化来源 | 正文列出子域、DNS、端口、HTTP、模板和通知工具，声称可构建零成本 ASM。 | [方法条目](../discovery/records-and-incremental.md) |
| 严重性沟通应给出向量依据并区分奖励 | 截图展示严重性及奖励调整，正文强调 CVSS 对该报告奖励的影响，未提供评分版本、完整向量或具体利用条件。 | [方法条目](../impact-and-acceptance.md) |

| 限流绕过要证明同一窗口中的服务端计数 | 保存图显示大量 200 错误密码响应，另帖在 Pitchfork 中同时改变 Host 与密码，返回相同的 400；还有正文用 X-Forwarded-For 声称操纵限流。 | [方法条目](../by-type/authn-session.md) |
| 邀请邮件与支持页面弹窗需要区分渲染器 | 正文把公司名称中的输入带入邀请邮件，截图弹窗来源是临时邮箱站点；另一帖在自有账户的支持页看到弹窗。 | [方法条目](../by-type/xss.md) |
| 优惠兑换应核对代码的主体与使用次数 | 保存正文描述同一 Pro Plan 代码在两个账户分别兑换。 | [方法条目](../by-type/business-logic.md) |
| 密码重置字段更换必须验证令牌绑定和最终登录 | 截图只展示重置表单中的令牌、邮箱、密码及确认字段，正文声称改邮箱后改了另一账户密码；奖励邮件提供处理状态。 | [方法条目](../by-type/authn-session.md) |
| 文件名与秘密关键词检索只生成归属候选 | 图列出配置、数据库、VPN、历史文件及 API/token/password 关键词，正则仓库卡片未保存实际规则。 | [方法条目](../by-type/info-secrets.md) |
| 邮箱样式载荷要核对校验器和后续消费 | 图片将 XSS、模板表达式、SQL、地址字面量和重复参数候选统称有效邮箱。 | [方法条目](../experiment-design.md) |
| 按需部署的云训练环境要核对隔离与清理 | HazProne 帮助展示 start/stop、quest 和 AWS profile，宣传按需部署易受攻击资源。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 索引输出转扫描时保留字段与范围 | 保存图把 Shodan 输出第二字段去括号后送入 HTTP 探测端口 3000 和 Grafana 模板，另一图显示 197 行、IP/域名及 None。 | [方法条目](../discovery/passive-and-services.md) |
| 服务索引与常用端口不能替代实时资产对照 | 正文和图给出 DNS 查询结果、RDP/VNC/Samba/FTP/打印机的 banner 检索、子域枚举及常见端口列表。 | [方法条目](../discovery/passive-and-services.md) |
| 新增数据源和图标哈希要保留来源差异 | 保存图列出多种 Amass 数据源及旧的费用标签，另一图显示 favicon hash 查询；正文也建议换搜索引擎找遗漏。 | [方法条目](../discovery/passive-and-services.md) |
| 源代码压缩包和备份后缀需确认最小私有内容 | 保存内容包含 html.zip、SQL/sqlite 备份名称，以及受保护配置路径改为 .bkp 返回 200 的候选。 | [方法条目](../by-type/info-secrets.md) |
| 历史提交发现的密钥不能直接复用 | 图建议检查 Git 旧提交，正文补充不同分支并介绍密钥验证工具。 | [方法条目](../by-type/info-secrets.md) |
| Base64解码应保留原始字节与实际工具约定 | 截图展示把文本经管道送入 base64 解码。 | [方法条目](../experiment-design.md) |
| 源站IP候选需保持同一应用与访问条件 | 保存正文从历史 DNS、证书或直接 IP 提出源站及 403 绕过候选。 | [方法条目](../by-type/waf-bypass.md) |
| 设备密码字段匹配要确认型号与访问边界 | 正文把固定管理路径、多个端口与 syspasswd 字串串接成探测流水线，并关联一个 Wavlink 型号。 | [方法条目](../discovery/client-and-cloud.md) |
| 面板指纹与管理动作权限须独立核对 | 一帖用 Hello from Rasa 识别服务并声称可更新或删除模型；其他保存图只展示 Grafana 面板及 phpMyAdmin 报告回执。 | [方法条目](../by-type/idor-access-control.md) |
| 方法覆盖头不能直接升级为命令执行 | 正文声称在仅允许 GET/POST 的服务增加 X-HTTP-Method: PUT 可获得 RCE。 | [方法条目](../discovery/web-and-api.md) |
| 历史CVE批量命中需复核实例与浏览器消费 | 保存正文和模板输出把 logout_redirect.do 的 sysparm_url 候选标为 ServiceNow XSS/CVE，报告列表又包含重复与不受理状态。 | [方法条目](../by-type/xss.md) |
| SQL测试要绑定查询位置而非参数清单 | 正文建议遍历参数、使用 SQL 在线实验及定制自动工具，保存图列出 GET 参数的布尔、报错、时间、UNION 和数据库名日志。 | [方法条目](../by-type/sql-injection.md) |
| 端点词表和输出文件需保持原始origin | 图将子域探测结果逐个交给 API 词表，并仅用域名命名输出；另图从已收集名称生成 token 词表，正文补充 .srv.js 和空格长度候选。 | [方法条目](../targeted-fuzzing.md) |
| 带外模板要用独立标记确定触发类型 | 正文列出参数、头及整请求三类 interaction 模板，并将命中与 blind RCE、SSRF、XSS 并列。 | [方法条目](../experiment-design.md) |
| 混合XSS载荷需还原解码和HTML修复过程 | 正文包含多种标签闭合、注释、编码、事件和 JavaScript 片段，图只有报告状态。 | [方法条目](../by-type/xss.md) |
| 历史WAF载荷需要双重对照 | 正文称某些编码和注释片段可绕过 Cloudflare 或 Akamai。 | [方法条目](../by-type/waf-bypass.md) |
| 重定向转XSS须证明目的地址的实际消费 | 保存文章开头仅说明用户可控跳转目的地址，正文另列控制字符和 JavaScript 协议候选。 | [方法条目](../by-type/open-redirect.md) |
| SVG动画事件候选须核对实际插入方式 | 正文和图展示 SVG animate 的 onend 候选及浏览器弹窗。 | [方法条目](../by-type/xss.md) |
| 候选受限时保留失败条件再换入口 | 正文描述特殊字符被编码，虽插入 script 却无法闭合，最后在另一参数找到 XSS。 | [方法条目](../hunting-strategy.md) |
| 浏览器历史与笔记要绑定真实请求状态 | 正文要求检查 Burp history 并强调做笔记。 | [方法条目](../discovery/records-and-incremental.md) |
| 聊天附件的存储路径与可执行处理必须分开证明 | 保存报告描述通过聊天上传 ASPX、在 attachments 路径访问，并展示目录列表；另列 SVG 存储 XSS。 | [方法条目](../by-type/file-upload.md) |
| 漏洞链不能自行扩展项目授权范围 | 正文称严重的范围外报告也可接受，另一帖描述范围外子域接管再加入 XSS 仍被判 Informative，披露数据库只有历史聚合统计。 | [方法条目](../scope-and-rules.md) |
| 训练环境的PHP包装器结果不能直接推广 | lfimap 截图来自低安全级别 DVWA，列出文件、data、input 等包装器、POST 变体及反向会话，还显示未提供 cookie 的警告。 | [方法条目](../by-type/lfi-path-traversal.md) |
| GraphQL批量请求应核对每个操作的计数与授权 | 正文提示 GET 与 batch queries，外链标题将批量与密码、MFA 和对象枚举并列。 | [方法条目](../by-type/graphql.md) |
| 格式后缀与权限图需要同一对象的角色对照 | 保存图建议两个角色访问同一支付信息路径，将 302 的普通入口追加 .json；另图只是 allow/deny 的对象归属示意。 | [方法条目](../by-type/idor-access-control.md) |
| 签名交易请求先保持业务与身份条件有效 | 保存图展示购买请求中的 amount、price_id、总价、存取账户 ID 及签名相关字段，响应为 400 转换错误。 | [方法条目](../by-type/business-logic.md) |
| 退订状态要对照地址绑定与授权规则 | 正文声称能取消任意用户邮件通知，截图只有感谢回执。 | [方法条目](../by-type/idor-access-control.md) |
| 登录响应中的个人字段须区分枚举与数据越权 | 图片展示按名称变化的 Intruder 响应和多项个人字段，正文仅关联登录 IDOR。 | [方法条目](../by-type/idor-access-control.md) |
| API分类与历史版本要变成具体不变量 | 图片列出缓存、令牌、JWT、授权、限流、race、XXE、Content-Type、方法和注入，并给出 v1/v2/v3 与年份路径候选。 | [方法条目](../discovery/web-and-api.md) |
| SOAP训练方法清单应分别验证读写和解析 | Erlik 截图列出创建、读取、运行文件、反序列化、日志、用户及查询方法和实验输出。 | [方法条目](../experiment-design.md) |
| 历史漏洞分类时间线只用于组织假设 | 保存图展示多个历史 OWASP Top 10 版本与不同类别名称。 | [方法条目](../experiment-design.md) |
| 测试框架的创建读回示例要区分真实与模拟 | Karate 图展示 API、浏览器、mock、适配器、报告与断言结构，示例先 POST 并核对 201、非空 ID 和名称，再按 ID GET。 | [方法条目](../experiment-design.md) |
| 无线去认证工具属于有副作用的隔离实验 | Autodeauth 帮助展示注入接口、SSID/MAC 白名单黑名单、发送数量、间隔及随机化，默认数量很高。 | [方法条目](../discovery/client-and-cloud.md) |
| 重复报告回执不能证明协作者泄露了方法 | 保存回执说明问题先前提交及项目限制，正文归因于协作者披露方法。 | [方法条目](../reporting.md) |
| 弱JWT秘密候选需证明签名验证与受保护消费 | 正文称开发者使用常见秘密导致 JWT 可被破解，外链词表未保存。 | [方法条目](../by-type/jwt.md) |
| CMS指纹需要核对实际版本与可达配置 | 正文建议通过 CMSeeK 识别 WordPress 或 Drupal。 | [方法条目](../source-audit.md) |
| 截图超时调整需保留失败原因和浏览器状态 | 图给出 Aquatone 的 HTTP、扫描和截图超时以及分辨率选项，声称避免截图失败。 | [方法条目](../discovery/passive-and-services.md) |
| SYSDATE时间候选要验证语义和延迟对照 | 保存请求使用 NOW、SYSDATE、条件和 SLEEP，图显示一次约 20 秒响应。 | [方法条目](../by-type/sql-injection.md) |
| 命令替换与带外响应需要直接因果关联 | 图中的请求包含命令替换样式输入，响应为 302，备注声称得到了 hostname，却未展示完整回调。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 服务器取址证据须排除客户端与代理直接请求 | 正文描述 proxy.stream 的 origin 参数及绝对 URL 请求，图同时变更多个带外头并显示 Collaborator 200；另一图仅是打码的元数据样式响应。 | [方法条目](../by-type/ssrf.md) |
| Referrer与登录路径定位不等于认证绕过 | 正文用自定义 Referer 和取响应头的请求关联一个登录页披露 CVE，未保存对应响应。 | [方法条目](../by-type/authn-session.md) |
| file协议载荷必须绑定实际渲染环境 | 保存内容用 object、XMLHttpRequest 和 iframe 声称 XSS 可读服务器文件，部分片段还含畸形标签或额外文本。 | [方法条目](../by-type/document-rendering.md) |
| XSS升级标题需要逐跳补齐权限证据 | 正文将 XSS 与 CMS 命令、恶意软件下载及 AWS SSRF 并列，图片只保存研究封面，未保存完整链条。 | [方法条目](../by-type/xss.md) |
| 简历上传目录要核对公开意图与最小对象 | 正文给出 WordPress 职位插件上传目录检索并关联 CVE。 | [方法条目](../by-type/info-secrets.md) |
| AD权限图须对应实际DACL与有效身份 | Aced 截图把多个主体用 AllExtendedRights、GenericAll、ForceChangePassword 和 AdminTo 连成链。 | [方法条目](../source-audit.md) |
| 代理会话示意图要保留已有执行前提 | 图展示 Cobalt Strike 的已有 beacon 与反向代理命令，正文强调 Chisel 的 XOR 包装。 | [方法条目](../by-type/cmd-injection-rce.md) |
| CIDR候选不能从通配域名范围自动推导 | 保存内容强调通配域名之外可关注 CIDR，图片只有培训封面。 | [方法条目](../scope-and-rules.md) |
| 密码重置混合清单需拆开实际消费边界 | 保存图用密码重置和 CRLF 标题，却继续列 UNION、数据库信息、文件权限及文件函数。 | [方法条目](../by-type/authn-session.md) |
| 浏览器Hook演示不替代初始XSS证据 | Toxssin 图展示已加载 handler 后的会话、按键、表单及响应日志。 | [方法条目](../by-type/xss.md) |
| 人工子域检查需要保留已查入口与证据 | 正文建议人工逐一检查子域并宣称 DOM-XSS，未保存具体数据流。 | [方法条目](../by-type/xss.md) |
| 奖励关键词检索必须回到原始项目规则 | 保存图通过 security-program、report、reward 等检索词寻找项目。 | [方法条目](../scope-and-rules.md) |
| 包上传的编码路径需逐层验证写入边界 | GitLab 保存图描述项目令牌、Maven 路径中的编码斜杠和遍历片段，随后声称写入 SSH 配置并登录。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 安全信誉结果不证明DNS接管条件 | 保存图只有 VirusTotal 的历史 URL 状态和未被安全厂商标记结果，正文宣称子域枚举到接管。 | [方法条目](../by-type/subdomain-takeover.md) |

| 包内URL与子域正则须保留解析遗漏 | 保存图用 grep 字符类提取 app 包中的 URL，又把子域正则与 google_maps_api_key 赋值匹配混列。 | [方法条目](../discovery/client-and-cloud.md) |
| 跨Web与移动入口检查同一IDOR修复边界 | 保存建议在 Web IDOR 修复后检查 iOS/Android 同类功能。 | [方法条目](../by-type/idor-access-control.md) |
| 嵌套对象ID替换须核对父子归属与操作 | 图中 accountsboard 路由替换 userid 后均返回 200；正文还声称 companyid/namespacepid/analyticid 的 DELETE 能删除个人分析数据。 | [方法条目](../by-type/idor-access-control.md) |
| 重复注册返回UUID只证明标识线索 | 图给出重复注册的 409 和 ref UUID。 | [方法条目](../by-type/idor-access-control.md) |
| 上传扩展和图片多态要沿完整消费链判断 | 图列 PHP/ASP/JSP/ColdFusion 后缀、大小写、双后缀、NUL、空格、CRLF、尾点/斜杠等候选，正文另提扩展黑名单和图片多态。 | [方法条目](../by-type/file-upload.md) |
| 上传文件名和SVG脚本要区分各消费者 | 上传清单含文件名中的标签、SVG script/onload 及 window.location。 | [方法条目](../by-type/xss.md) |
| 上传文件名路径需证明实际读写落点 | 图建议把遍历片段放入上传文件名，但把 passwd 路径后再接文件名并不能证明读取。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 文件名SQL线索不能由一次长延迟确定 | 清单在文件名中放置 sleep 表达式。 | [方法条目](../by-type/sql-injection.md) |
| 文件名命令候选依赖实际shell消费 | 正文声称 whoami 失败但加入 shell 分隔符后出现 www-data，上传清单另给文件名延时命令和 ImageTragick 模板。 | [方法条目](../by-type/cmd-injection-rce.md) |
| URL取图须区分服务器抓取与访客浏览器 | 图把 Upload from URL 与访客 IP logger 并列。 | [方法条目](../by-type/ssrf.md) |
| SVG外部实体候选须定位服务端XML解析器 | 图显示 SVG SYSTEM 实体及展开用法，另一帖仅 XXE 拼图插画。 | [方法条目](../by-type/xxe.md) |
| WordPress路径清单要校对路由和公开预期 | 保存图与正文列 wp-config、wp-content/uploads、wp-json、登录、注册、xmlrpc、cron 等路径，列表还有重复项及未证实的文件名。 | [方法条目](../discovery/web-and-api.md) |
| DNS证书索引和WHOIS聚合需保留原证据 | dig+grep+head1会丢掉多A、AAAA、CNAME和错误；tlsx、Netlas、wtfis、WebOSINT及Infoooze聚合证书、DNS、Whois、IP、信誉与历史源。 | [方法条目](../discovery/passive-and-services.md) |
| 组织文件关键词和仓库流水线须验证归属 | 图列 client_secret、连接串、数据库口令、gh/npm/oauth token、LDAP、私钥及配置/历史文件等检索候选，GitHub流水线还有脚本URL与协议过滤不一致问题。 | [方法条目](../by-type/info-secrets.md) |
| PHP登录SQL拼接与密码比较要分别审计 | 保存代码将 username 拼入 SELECT，取首行 password 后与 md5(password) 严格比较。 | [方法条目](../by-type/sql-injection.md) |
| 事件属性与编码变体需区分放行和实际执行 | 保存正文给 pointerenter、换行/CR、cookie/globalThis、实体/Unicode和SVGOnly/onload等候选，图片包括阻挡页、遮挡确认框及正常首页；img style dataSVG 片段还存在解析上下文疑点。 | [方法条目](../by-type/waf-bypass.md) |
| 方法变化和构造器载荷仍须证明初始XSS入口 | 正文建议GET不反射时换POST，又给hash/eval及Object.prototype扩展和Function构造器字符串变换。 | [方法条目](../by-type/xss.md) |
| AngularorderBy表达式须区分客户端和服务器 | 正文把 Angular orderBy 载荷称SSTI，保存图只有遮挡浏览器提示。 | [方法条目](../by-type/ssti.md) |
| 默认日志文件名不代表对外暴露 | 正文建议 /logs/error_log，图片则为Apache编译信息中的默认相对日志路径、HTTPD_ROOT及模块/配置。 | [方法条目](../by-type/info-secrets.md) |
| 人工浏览与持续投入需记录实际覆盖 | 保存正文强调浏览器操作、持续研究少数项目和区分普通bug与安全问题。 | [方法条目](../hunting-strategy.md) |
| 子域接管模板加载不等于可控制资源 | 正文建议嵌套子域检查，图给chaos/DNS/HTTP/nuclei链但只显示模板Loaded；奖励邮件没有DNS条件。 | [方法条目](../by-type/subdomain-takeover.md) |
| 面板端口和HTTP版本差异须核对同一处理器 | 正文提空白页的非标端口/302目录以及去掉头改HTTP/1.0；图片仅cPanel登录页和Lync403基线。 | [方法条目](../discovery/web-and-api.md) |
| LDAP主机名回调只证明被观察到的求值层 | 正文给包含hostname的LDAP/OOB候选。 | [方法条目](../by-type/deserialization-rce.md) |
| 历史URL筛选和自动检测必须保留原请求 | Swagger词表、subfinder/wayback/gau/gf/sed/qsreplace/ffuf/dalfox/sqlmap及GitHub触发流水线只产生候选。 | [方法条目](../targeted-fuzzing.md) |
| 多服务口令与限流检查须定义每账户预算 | TheSprayer图列域/DC、已有策略查询凭据、连续/Force及剩余次数选项，另帖强调限流不只邮件短信，BruteX仅功能卡。 | [方法条目](../by-type/authn-session.md) |
| 产品指纹与探测输出只是发现记录 | Shodan菜单、httpx status/title/length、SubEvil协议过滤、HTTPFY、Hawk及Subfinder/Wappalyzer显示产品、服务、来源或正在枚举。 | [方法条目](../discovery/passive-and-services.md) |
| SMB递归示例须区分凭据权限和读取失败 | 图展示已有域用户及管理员访问SYSVOL、递归目录、AccessDenied与八个文件下载。 | [方法条目](../by-type/idor-access-control.md) |
| 合约提现外部调用前后须检查状态不变量 | 图中withdraw先检查余额，外部call后才扣账，提示回调可重入的窗口。 | [方法条目](../by-type/business-logic.md) |
| 目录日志建图须保留查询身份与证据缺口 | BOFHound正文介绍日志转BloodHound图，ADSearch图展示已有凭据LDAPS与SPN及限定cn/DN/groupID查询。 | [方法条目](../discovery/records-and-incremental.md) |
| 代理头盲注延迟需核对数据库语义和重复对照 | 正文在X-Forwarded-For使用MySQL时间函数，另一帖在X-requested-with给WAITFOR延迟却称毫秒，图仅404及约19.698秒总耗时。 | [方法条目](../by-type/sql-injection.md) |
| 重置OTP和2FA清单必须证明挑战与最终身份 | 保存图在响应JSON显示OTP字段，正文又提启用2FA后secret、修改重置JWT邮箱及多收件人/bcc/重复email参数、注册/改密/改邮箱。 | [方法条目](../by-type/authn-session.md) |
| 社交注册和账号链接须核对服务端可信身份 | ATO清单建议修改socialsignon的email、去掉scope后手填邮箱、电话号码注册再链接既有邮箱。 | [方法条目](../by-type/oauth-oidc.md) |
| 开源奖励与公开数据集不能扩展资产许可 | 正文提Google OSS奖励项目和公开侦察数据集。 | [方法条目](../scope-and-rules.md) |
| 票据工具和补丁建议需核对前提与当前状态 | noPac图已有域账户、机器账号修改、票据及清理失败，Coercer仅含认证材料的banner，WESNG为systeminfo/CVE数据过滤帮助。 | [方法条目](../source-audit.md) |
| DNS变化须比较校验地址与实际连接地址 | 正文建议重绑定DNS。 | [方法条目](../by-type/ssrf.md) |
| 多搜索引擎并发须核对查询保密与独立结果 | TRIFECTA仅说明一个词可在十二个搜索引擎单独或并行查询。 | [方法条目](../discovery/passive-and-services.md) |
| 登录跳转参数须核对真正导航和信息携带 | 正文描述登录期间开放重定向，图仅奖励通知。 | [方法条目](../by-type/open-redirect.md) |
| Pcap IP地理导出需保留时间与元数据限制 | IPGeo图过滤私网后对公网地址分析并导出。 | [方法条目](../discovery/records-and-incremental.md) |
| HTTP与浏览器爬取队列需证明各阶段完成 | Darc图将hostname/requests/selenium队列、cache检查、解析/保存/提交、robots/sitemap/hosts及数据库/API回写连接。 | [方法条目](../discovery/records-and-incremental.md) |
| 多云资源清单需核对凭据身份和分页 | Cloudlist正文介绍多provider资产收集。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 缺少安全响应头需证明具体浏览器影响 | 正文讨论缺少header应否报告。 | [方法条目](../impact-and-acceptance.md) |
| 本地靶场shell画面不能补造SQL或上传入口 | PostgreSQL训练图有登录页面与本地os-shell，Zimbra图则先用admin凭据登录再上传JSP并回显。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 反Frida端口检查只是本地检测条件 | 保存建议默认27042端口检测可能通过换端口规避。 | [方法条目](../discovery/client-and-cloud.md) |
| Schema路径和工具评分不能代替字段授权 | GraphCrawler图显示mutation读取错误、十二queries、零敏感项、_service授权及三条CoreVideo路径。 | [方法条目](../by-type/graphql.md) |
| 内核调试环境须匹配符号与真实隔离边界 | like-dbg图显示ARM64源码、反汇编、线程和SIGINT调用栈，正文称Docker部署调试内核。 | [方法条目](../cloud/container-k8s-security.md) |
| 斜杠遍历和非标端口文件显示需定位处理器 | 保存Nginx图给重复斜杠/..路径及passwd响应，另一图浏览器8085显示文件，SwaggerUI正文则给混合斜杠遍历候选。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 大小写展开必须在校验和存储两端一致 | 正文指出JavaScript把ß变为SS。 | [方法条目](../experiment-design.md) |
| 域名字典组合须核对规模和合法性 | 图用comb将词表与rootdomain做点分组合，或gee占位替换并去重，Gorilla正文介绍字典变异。 | [方法条目](../targeted-fuzzing.md) |
| shell生成器输出不证明输入可执行 | GSHELL/Shelly图展示IP、port、语言、bind/reverse方向和base64/URL等编码模板。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 现成会话和分阶段加载须标明初始执行前提 | BlackHeart监听、TCP后门主动启动、DFShell已建立fifo会话、BeatRev分阶段解密/内存加载、Gohide本机隧道和NimRunPE本地映射PE等都依赖预先执行权限；Pyramid/Connect仅功能介绍。 | [方法条目](../source-audit.md) |
| 本地提示和shell配置替换不等于无前提提权 | ForceAdmin正文依赖反复UAC提示，Sudo-Stealer图在.zshrc重定义sudo并委派另一程序，EyeBinder图列Run as Administrator/Defender exclusions选项。 | [方法条目](../by-type/desktop-client.md) |

| WordPress公开元数据与私有调试文件分开确认 | 保存图片把 debug.log、配置备份、用户 REST、注册和 xmlrpc 混列。 | [方法条目](../by-type/info-secrets.md) |
| 免括号语法候选仍依赖具体脚本消费者 | 保存内容从 img 属性、SVG、tagged template、onerror、隐式转换到免括号清单。 | [方法条目](../by-type/xss.md) |
| 报表file URI与插件下载参数各自核对读取边界 | rwservlet 图中 URLPARAMETER 的 file URI 对应文件正文，BackupBuddy 图中下载参数返回附件和文件格式内容；编码路径穿越图也显示文件读取。 | [方法条目](../by-type/lfi-path-traversal.md) |
| CVE管道命中须在范围和模板请求之间设证据边界 | 保存 subfinder/httpx/nuclei 和编排图只说明发现与模板串联，部分示例用 9500 线程或只匹配 200/文件字符串。 | [方法条目](../targeted-fuzzing.md) |
| Aura风险分与PyPI相似包只生成审计候选 | 图片同时显示单文件污点/URL 命中和 requests 相似包元数据差异。 | [方法条目](../source-audit.md) |
| 打印服务与令牌工具须补齐初始权限和触发前提 | SpoolTrigger 图含服务加载路径和 SYSTEM 输出，JuicyPotato 图为旧 Windows/SeImpersonate 环境，Coercer 需既有认证，SharpImpersonation 只列进程令牌。 | [方法条目](../by-type/desktop-client.md) |
| 现成Shell菜单不构成最初RCE路径 | Mango 菜单列用户、服务、任务和本地目录，RCE 后路径建议涉及日志/账号/计划任务。 | [方法条目](../source-audit.md) |
| 浏览器扩展按身份隔离和真实请求检验 | 保存工具矩阵包括代理切换、历史 URL、组件识别、容器账户和临时邮箱；Firefox 推荐还含翻译。 | [方法条目](../experiment-design.md) |
| Teams GIF演示需要区分显示内容与本地命令来源 | GIFShell 图片仅显示聊天 GIF、PowerShell 文本和本地服务演示。 | [方法条目](../by-type/desktop-client.md) |
| 搜索查询与实际回跳目标不能混同 | DuckDuckGo 示例是编码查询参数，Google dork 的负 inurl 条件会排除包含指定词的结果。 | [方法条目](../by-type/open-redirect.md) |
| OAuth外部redirect示意要绑定客户端与实际授权响应 | 图片的 response_type=token 概念箭头没有真实完整会话。 | [方法条目](../by-type/oauth-oidc.md) |
| cachebuster改变缓存状态也可能改变实验变量 | 每次递增随机参数可能避开某层缓存，也可能影响签名、路由、参数校验或缓存 key 归一化。 | [方法条目](../experiment-design.md) |
| security.txt联系渠道和公开项目标签不授予测试权限 | /.well-known/security.txt 可提供联系或政策线索；disclose 类目录的 good faith、bounties、swag 等只是索引标签。 | [方法条目](../scope-and-rules.md) |
| 客户端在范围外时不能借最终范围内消费者扩张授权 | 保存说法包含所有项目都会排除 SSO，以及从 OOS Android 输入触发范围内 XSS 的建议。 | [方法条目](../scope-and-rules.md) |
| 无线接口菜单和IQ波形区分被动采集与主动修改 | Tsu-Fi 图片列接口切换、监听模式、IP 转发、Ettercap 和 WPS，Sniffle 显示固件加载，FISSURE 显示 IQ 波形。 | [方法条目](../discovery/client-and-cloud.md) |
| PHPwrapper特性表不是任意文件读到RCE的通用桥 | Liffy 图混列 data/expect/input/filter、CGI environ、日志污染和绝对/相对路径。 | [方法条目](../by-type/lfi-path-traversal.md) |
| kubectl秘密读取需按当前RBAC及响应最小化 | 保存建议仅围绕 kubectl get secrets。 | [方法条目](../cloud/container-k8s-security.md) |
| 403工具卡不能替代拒绝原因和最终业务权限 | nomore403/DontGo403 只有工具介绍。 | [方法条目](../by-type/idor-access-control.md) |
| 静态页面与JavaScript仍可形成真实API入口线索 | 静态页面没有表单不代表没有后端；结合保存建议的 JS、历史 URL、截图和目录线索，记录文件/脚本版本、字段、路由和调用位置，再在明确范围内与实际客户端请求对照。 | [方法条目](../discovery/web-and-api.md) |
| 子域到自动化流程必须保留每阶段来源与失败 | 保存方法图覆盖 seeds、收购/ASN/Whois/证书、JS、子域排列、端口、指纹、截图、takeover 和编排。 | [方法条目](../discovery/records-and-incremental.md) |
| 子域排列与单IPv4管道不能代表全部解析覆盖 | 图片分别展示子域计数、altdns、AORT --all、dnsenum Alive 和 dig 正则加 head -1。 | [方法条目](../discovery/passive-and-services.md) |
| 404及takeover指纹须与实际资源绑定条件复核 | 保存脚本把 404 和 can-i-take-over 风格指纹当检查步骤。 | [方法条目](../by-type/subdomain-takeover.md) |
| 临时目录HTTP服务要核对监听范围与上传权限 | Swego 图片在 localhost 暴露目录列表、上传、新目录和 ZIP 下载。 | [方法条目](../by-type/file-upload.md) |
| 网站词表与OWA包装器需固定账号和失败预算 | CeWL/词表是候选生成，OWA 包装器截图因密码列表不可访问直接中止。 | [方法条目](../by-type/authn-session.md) |
| 目录递归与后缀组合应按整个队列计预算 | ffuf 图显示 301 添加递归任务后找到 .bak 200；ferox 图只给调用参数，shell 函数还未正确引用输入。 | [方法条目](../targeted-fuzzing.md) |
| 给请求加标签头会改变被观测实验 | 为了在代理中找回请求而加入 X 头，可能改变缓存 key、签名、WAF 或应用行为。 | [方法条目](../discovery/records-and-incremental.md) |
| XLL加载提示与Excel进程属性分开证明执行 | 一张图显示 Excel 从临时目录加载 XLL，另一张明确因缺签名禁用并要求用户启用。 | [方法条目](../by-type/desktop-client.md) |
| GraphQL批处理按逻辑操作而非HTTP包数检查限流 | CrackQL 宣传涉及批量破解、2FA、IDOR；只有工具能力声明。 | [方法条目](../by-type/graphql.md) |
| Webhook与PDF及邮箱域回调要定位真正消费者 | 保存清单包含 URL 参数、HTML/PDF 外部资源、文档下载、注册邮箱域。 | [方法条目](../by-type/ssrf.md) |
| PDF外部资源与文档URL导入分步确认 | PDF/HTML 预览图片建议测试外部资源和将上传改 URL 下载。 | [方法条目](../by-type/document-rendering.md) |
| UserAgent时间SQL候选需区分函数时钟与网络等待 | 保存 XOR/IF/SLEEP 候选依赖 User-Agent 被拼入数据库表达式，奖励图没有完整复现。 | [方法条目](../by-type/sql-injection.md) |
| 产品版本接口与漏洞影响应分开判断 | 保存 POST GetProductVersion 建议与 75 美元奖励图。 | [方法条目](../by-type/info-secrets.md) |
| 复现争议按完整环境与根因证据沟通 | 截图包含无法复现、跨网络影响问题、补充视频、Triaged 到 Duplicate 变更；关键正文遮盖。 | [方法条目](../reporting.md) |
| CIA影响应落在受保护对象和最终状态上 | 保存三页分别解释保密、完整、及时可靠访问。 | [方法条目](../impact-and-acceptance.md) |
| 静态特征动态日志和模型分数保存各自证据来源 | 图中 PE/Android 特征、YARA、LOKI 与沙箱模型分别输出能力标签、置信度和分数。 | [方法条目](../source-audit.md) |
| Registry Run自动分类须复核ACL与真实登录触发 | PersistenceSniper 图把有效签名音频程序 Run Key 标为 System。 | [方法条目](../by-type/desktop-client.md) |
| GitHub配置字段关键词须回到发行提交和有效边界 | Redis/Slack/SSH/Stripe/Jenkins 关键词图和 YAML 建议只是定位配置候选。 | [方法条目](../by-type/info-secrets.md) |
| JWT前缀和可解码内容不能说明加密或认证有效 | ey 开头仅常见 JSON 编码线索，并非 JWT 必须的固定前缀。 | [方法条目](../by-type/jwt.md) |
| 登录CookiePath不能解释Jetty目录列表的权限 | 保存登录请求有已有会话，302 返回新 JSESSIONID 且 Set-Cookie Path=/，随后带该新会话 GET /oauth/ 返回目录列表。 | [方法条目](../by-type/authn-session.md) |
| USB进程附加与APK重签名改变本地验证前提 | Medusa 图片已在 USB 设备附加进程读取 ELF，APKLab 图显示重打包后的 AndroidDebug 签名。 | [方法条目](../discovery/client-and-cloud.md) |
| 地址变体清单必须绑定最终连接解析器 | 图把 127/IPv6 变体称 CIDR，并对 userinfo、fragment、反斜线给固定库解析结论。 | [方法条目](../by-type/ssrf.md) |
| massassignment角色变化需检查真实写入对象 | 低代码应用标题声称从参数赋值提升租户管理员，但全文未保存。 | [方法条目](../by-type/idor-access-control.md) |
| Oracle条件错误候选需以可观测真假分支确认 | 保存 DECODE/SUBSTR 与除零候选是数据库表达式假设。 | [方法条目](../by-type/sql-injection.md) |
| PHP顺序替换黑名单须模拟最终SQL字节 | 挑战截图先读取 GET q，再逐项 str_replace 加反斜线，最终拼接到单引号 category 查询。 | [方法条目](../by-type/sql-injection.md) |
| SQL挑战的无结果反射还有独立HTML消费者 | 同一 PHP 截图在无结果分支反射 q。 | [方法条目](../by-type/xss.md) |
| OpenAPI负向生成需标明实际契约与状态副作用 | CATS 名称和工具介绍只提供测试生成线索。 | [方法条目](../targeted-fuzzing.md) |
| Bitbucket公共仓库和Git错误须分别归因 | 公共仓库列表是正常指纹；archive 请求图一例显示带疑似执行身份的 Git 错误，另一例为 InvalidRefName。 | [方法条目](../by-type/cmd-injection-rce.md) |
| CSP阻断与另一浏览器弹窗必须保留同源条件 | 一图有 SVG onload DOM 节点，另一图是项目以 CSP 阻断关闭，第三图另浏览器 alert 6。 | [方法条目](../by-type/xss.md) |
| prototype转换效果仍须证明不受信输入进入该链 | 保存脚本已直接处于 JavaScript 执行环境并修改 prototype。 | [方法条目](../source-audit.md) |
| 选择功能假设与练习环境要按证据收益控制投入 | 保存建议涉及熟悉技术、优先上传/PDF/注册/恢复等功能、掌握工具和 CTF 练习。 | [方法条目](../hunting-strategy.md) |
| 虚拟主机实验单变量区分Host路径和SNI | 示例同时在 URL 路径及 Host 放 FUZZ，并把 DNS 内网 IP 加列表。 | [方法条目](../discovery/web-and-api.md) |
| 协议信息功能不能默认包含踢人或代理捕获 | Minecraft 工具帮助混合端口、server/player/mods/listening 查询、kickall/循环踢人和代理捕获。 | [方法条目](../scope-and-rules.md) |
| Tor配置完成与恢复文字需要实际网络状态对照 | Neutron 图修改 DNS/Tor/iptables 并显示出口 IP，另图称还原完成。 | [方法条目](../experiment-design.md) |
| 登录和注册回跳应各自验证当前修复状态 | 奖励邮件区分已修复 sign-up 和未知 sign-in 回跳。 | [方法条目](../by-type/open-redirect.md) |
| 付费内容访问先确定订单权益和被访问对象 | 保存故事声称免费获得付费产品，图片仅奖励邮件。 | [方法条目](../by-type/business-logic.md) |
| 盲XSS通知计数不能替代输入到消费者归因 | XSS Hunter 列表仅显示 fired 通知和数量。 | [方法条目](../by-type/xss.md) |
| 邮件触发限流用最小自有次数验证 | 正文建议改包后重复 50 次，图为 Email-triggering NoRateLimiting/P4。 | [方法条目](../by-type/authn-session.md) |
| 自定义CA与OCSP设置不能证明pinning绕过 | Burp 扩展图只显示监听端口与默认/自定义 CA，Start 尚可点击。 | [方法条目](../by-type/desktop-client.md) |
| 溢出实验的崩溃阈值偏移与执行证据不能跨环境拼接 | 三图为 2000 字节 crash、1978 offset/跳转/坏字符参数和另地址 vulnserver 反连。 | [方法条目](../targeted-fuzzing.md) |
| 匿名AD绑定成功不代表枚举模块全部成功 | LinWinPwn 图用匿名/空密码模式，DNS 与 BloodHound 模块提示需要凭据，LDAP bind OK 后才尝试目录读取。 | [方法条目](../by-type/ldap-xpath.md) |

| Leonidas 部署链与测试资源必须分别核对权限 | Leonidas 架构把 CI/CD、Lambda、测试资源和 SIEM 连接起来。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 上传后果按实际消费者验证而非扩展名分类 | 上传清单把 SVG、GIF、CSV、XML、AVI、ZIP、PDF/PPTX 和脚本扩展名关联到多种风险；报告截图还提到表单处理人接收 disallowed 文档。 | [方法条目](../by-type/file-upload.md) |
| 移除 Bearer 的方法差异要读回对象状态 | 保存帖建议移除 token 后比较 DELETE/PUT/GET，配图只有奖励。 | [方法条目](../by-type/idor-access-control.md) |
| Bitbucket archive 候选不能省略 repository read 前提 | CVE-2022-36804 帖称 pre-auth，截图展示 archive 请求及本地临时文件操作参数，没有响应或文件结果。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Gallia 电源控制和协议请求分开定义实验范围 | Gallia 图包含数据库、日志、配置、用户输入、scanner/transport 与 hardware power supply。 | [方法条目](../experiment-design.md) |
| Triaged 与 duplicate 状态保留裁决和复现边界 | 奖励、duplicate 和长时间 pending 的帖子不能替代技术证据。 | [方法条目](../reporting.md) |
| 多搜索来源的空结果不代表资产不存在 | 帖子建议 Google 无结果时换 Bing，并列出多个引擎。 | [方法条目](../discovery/passive-and-services.md) |
| ffuf 部分进度与 200/301 只用于候选筛选 | 截图的 GET FUZZ 结果有 admin.php 301、index.html 200，进度尚未完成。 | [方法条目](../targeted-fuzzing.md) |
| 侦察到 CVE 模板的流水线需要产品和请求证据 | Amass→httpx→nuclei CVE-2022-26134 卡只有命令没有输出；RCE 模板目录还混有 API exposure、备份和 source map 项。 | [方法条目](../discovery/web-and-api.md) |
| file URI 与多斜线路径要定位真实读文件消费者 | 保存正文显示 file URI 下载候选被 WAF 阻止，另图显示多斜线/点段路径返回账户文件风格文本且 Server 为 Apache。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 域前置扫描 HIT 需要 SNI Host 和上游行为对照 | WSee 输出包含超时、404/501/502 和两条 HIT。 | [方法条目](../discovery/web-and-api.md) |
| 目标派生备份名与本地解压目录不能直接认定泄露 | 保存帖列域名派生归档后缀，配图本地 WordPress 目录含配置、安装器、备份和日志。 | [方法条目](../by-type/info-secrets.md) |
| Dalfox discovery 与浏览器及 blind 验证分开 | Dalfox 选项图区分 selected parameters、only-discovery、DOM/headless 和 blind。 | [方法条目](../by-type/xss.md) |
| Karma 的证书 ASN CDN 关联不能定义授权范围 | Karma 帮助根据证书 CN、ASN、favicon、CDN、产品/CVE 和 leaks 形成关联，还支持无限结果。 | [方法条目](../discovery/passive-and-services.md) |
| HTTP 端口和跳过 TLS 校验保留不同含义 | 帖子建议总 fuzz 80、cariddi 加 insecure、以及 CDN 开放端口疑问。 | [方法条目](../discovery/web-and-api.md) |
| 元数据目录响应与服务端请求来源分别证明 | 截图 POST 表单 url 指向元数据路径，200 正文列目录名。 | [方法条目](../by-type/ssrf.md) |
| 非法头的缓存 HIT 需要干净请求受到污染的证据 | Akamai 卡示意非法头返回 400、Server-Timing 为 HIT。 | [方法条目](../discovery/web-and-api.md) |
| CSRF 生成器保留中文编码及浏览器凭据条件 | LazyCSRF 与 Burp 图对比中文姓名字段，原请求含同源头、会话和 authenticity_token。 | [方法条目](../by-type/csrf.md) |
| SPF DMARC 记录检查与实际邮箱身份分开 | Spoofy 帖描述依据域名 SPF/DMARC 判断 spoofable，未展示发送或接收结果。 | [方法条目](../by-type/authn-session.md) |
| https 字串存在与无条件前缀不是同一过滤 | 保存帖一方面说在值前加 https://，另一方面提供含 https:// 字串的 javascript 表达式，两者不能无条件同时成立。 | [方法条目](../by-type/xss.md) |
| 侦察平台计数和队列要保留阶段输入及失败 | WARF 图按子域、目录、Wayback、JS、secret 和 LinkFinder 统计；SubCrawl 图有文件/情报/Kafka 输入、处理/存储及 MISP 导出。 | [方法条目](../discovery/records-and-incremental.md) |
| Logger token 过滤仍需保留原始请求和响应 | Logger 图示 Response.body CONTAINS token，正文/alt 描述 API 过滤合集。 | [方法条目](../discovery/records-and-incremental.md) |
| GitHub AWS 和连接字段检索只形成待核实候选 | 关键词图列 access_key、SecretAccessKey、DB_PASSWORD、connectionstring、token 等。 | [方法条目](../by-type/info-secrets.md) |
| TCP shell 和 PTH 演示保留既有执行及身份前提 | PSAsyncShell 帮助明确客户端/监听模式及明文 TCP，依赖已能运行 PowerShell 和网络连接；PTH 截图传入 hash，经过 SMB 认证、DuplicateTokenEx 后以 impersonated token 启动进程。 | [方法条目](../by-type/desktop-client.md) |
| 功能笔记要区分状态机前提与未验证想法 | 保存帖建议记参数、endpoint、功能、角色和以后再看项，并尝试跳过流程步骤。 | [方法条目](../business-modeling.md) |
| 旧客户端升级提示与服务端权限边界分开 | 保存帖仅描述旧版要求更新，现存图是 Android 桌面，没有绕过细节。 | [方法条目](../by-type/desktop-client.md) |
| Schema valid 与基线工具不能替代安全措施验证 | MOSP 图展示 JSON/schema 编辑与标准映射，Debian CIS 帖仅宣传基线工具。 | [方法条目](../source-audit.md) |
| 演示 token 和缓存账户接管标题不等于泄露链 | 保存正文提演示页面，图片仅 Web Cache Deception triaged 标题。 | [方法条目](../discovery/web-and-api.md) |
| 正则 authority 黑名单与真实连接解析需要一致 | 保存 Flask 代码仅用正则取协议和 authority，字面阻止 localhost/127.0.0.1 后 requests.get，再 base64 渲染结果。 | [方法条目](../by-type/ssrf.md) |
| Source map 先核对实际引用及内容再审计 source | 去 min 加 map 只是名称猜测，优先核对 sourceMappingURL、真实版本、map 格式、sources/sourceRoot/sourcesContent 及加载地址。 | [方法条目](../discovery/client-and-cloud.md) |
| AEM 参数名中的编码冒号按每层解码比较 | AEM 例子比较 form 字段 param:body 与 param%3Abody。 | [方法条目](../by-type/waf-bypass.md) |
| JWT none 和算法混淆验证服务端允许集合及 key 绑定 | JWT 图把解码、签名和资源访问连成流程，并描述 none 与把公钥当 HMAC 密钥的候选。 | [方法条目](../by-type/jwt.md) |
| Burp scope 正则按 host protocol port 与排除字段验证 | 帖子给 .*\.target\.com$，图中的 Burp 列表明确 protocol、host、port、file 与排除规则分开。 | [方法条目](../scope-and-rules.md) |
| Cookie 审计分离字段消费者与服务端信任 | Cookie 思维图包含组织/role/user_id、失效、fixation、flags、重复参数、反序列化和注入。 | [方法条目](../by-type/authn-session.md) |
| 汇编克隆得分要回到可达输入与基本块语义 | Kam1n0 图展示 REST/MVC access filter、共享资源缓存、符号与 ML 模块，另图标记重命名、插入和 CFG 配对，结果页给分类/克隆百分比。 | [方法条目](../source-audit.md) |
| 模拟协议和 honeypot 事件不认定生产漏洞 | FaPro 协议日志与 OWASP Honeypot 图分别展示口令/命令尝试、启动模块、IP/端口分布和日志分页。 | [方法条目](../discovery/records-and-incremental.md) |
| Domain Protect DNS 观测 通知与接管动作分开 | 图示跨账户 AssumeRole→Organization→目标 Route53，再写 DynamoDB/SNS 并通知 Slack，还单独有 takeover Lambda。 | [方法条目](../by-type/subdomain-takeover.md) |
| SVG background image 先确定浏览器还是后端消费者 | 保存问题明确 SVG 被放进 background-image url，XSS/SSRF 尝试未成功。 | [方法条目](../by-type/file-upload.md) |
| PUT 写入 文件 listing 与执行 handler 分别证明 | 保存帖把 PUT enabled 关联 RCE，图只显示 uploads listing 与脚本文件名。 | [方法条目](../by-type/file-upload.md) |
| WP XML-RPC 用户候选与 XSPA 操作按功能逐项验证 | WPXSPA 帖列 user enumeration、brute force、DoS 与 xmlrpc 能力。 | [方法条目](../discovery/web-and-api.md) |
| 网页 sign in 与 GitLab API 原始资源分别验证 | 保存报告截图显示网页跳转登录，但 /api/v4/projects 返回内部项目信息并列 source 可读路径。 | [方法条目](../by-type/idor-access-control.md) |
| 词汇变换百万字典不构成认证测试授权 | Psudohash 示例从词汇生成大小写/符号/数字/padding 超百万候选并提示大小。 | [方法条目](../by-type/authn-session.md) |
| 集成 Jira title 的渲染到 POST 链保留缺失 gadget 边界 | 报告截图摘要描述 Jira issue title 缺 HTML 编码，HTML/CSS 注入经 gadget/浏览器行为升级 POST，保存内容没有具体 gadget。 | [方法条目](../by-type/xss.md) |
| OAuth 授权响应 回调和资源权限分别绑定 | 保存帖列 redirect/XSS/CSRF 外链，图画授权请求、code、token 和资源服务器。 | [方法条目](../by-type/oauth-oidc.md) |
| ACAC true 单一响应头不能认定 CORS 数据泄露 | 保存 Yelp 报告图将 ACAC true 视为风险但状态为 Informative。 | [方法条目](../by-type/cors.md) |
| Password autocomplete 功能与独立攻击前提分开 | 保存报告称 autocomplete enabled，状态 Informative，摘要依赖设备被控制或额外 XSS。 | [方法条目](../by-type/authn-session.md) |
| mDNS 设备和服务广播只说明当前局域网可见信息 | SpyCast 图显示私网设备、型号/TXT、地址、服务和端口。 | [方法条目](../discovery/passive-and-services.md) |
| id 字串和 profile link 标题不能替代 A B 对象授权 | IDOR 图用 grep id 数字筛选 URL，另报告摘要称可修改他人 profile links。 | [方法条目](../by-type/idor-access-control.md) |
| DSAR 删除流程从匿名受理到最终身份验证逐阶段核对 | DSAR 提示仅请求删自有测试账户。 | [方法条目](../by-type/business-logic.md) |
| Wildcard 路由 重复参数及修复分支分别读最终导航 | Flickr 摘要称未匹配路由原本用于 404，另帖提出重复 next、多次编码以及 failed 分支修复后再绕过。 | [方法条目](../by-type/open-redirect.md) |
| noscript 解析模式与 WAF 事件词不能生成通用绕过 | noscript 候选依赖 HTML parser 的 scripting 模式、上下文与后续重新解析；[HTML noscript 规范](https://html.spec.whatwg.org/multipage/scripting.html#the-noscript-element)说明其解析会随模式变化。 | [方法条目](../by-type/xss.md) |
| POST 时间候选先验证条件和抖动再限制工具动作 | 帖子用 NOW/SYSDATE 条件与 20 秒 SLEEP 后将请求交 SQLmap --dbs；保存文本还带非 ASCII 引号/命令格式错误。 | [方法条目](../by-type/sql-injection.md) |
| 密码策略必须校验服务端接受的最终值 | Cloudflare 摘要指出改请求可绕前端策略，修复对齐后端；Nextcloud 摘要指出 HIBP 检查后 str_shuffle 可能改变最终值且示例复现依赖改随机源代码。 | [方法条目](../by-type/authn-session.md) |
| 外部账号改名后绑定以稳定身份和实际权限判断 | TikTok/Instagram 摘要称 username 改后 profile 链接未更新。 | [方法条目](../by-type/oauth-oidc.md) |
| DLL Hijack found 需要真实搜索路径和目录权限 | DLLirant 图标出 signed x64 程序、mpclient 导出测试和代理生成，只有消息框不够。 | [方法条目](../by-type/desktop-client.md) |
| CIDR PTR Shodan 和组织字串保留资产关联链 | CIDR 查询帖、Shodan dork 图和 spk→PTR→根域→Subfinder JSON 图把组织/IP/AS/证书/title 关联为候选。 | [方法条目](../discovery/passive-and-services.md) |
| ProxyNotShell 的 IIS 404 matcher 不能确认 Exchange SSRF | 保存帖把 ffuf autodiscover 命中 IIS Web Core 的 404 称 vulnerable，截图跟跳转、线程 5000 且只列 404。 | [方法条目](../by-type/ssrf.md) |
| 目录 403 与子文件读取是不同授权对象 | 保存帖说 /logs 403 而 /logs/user.txt 返回 PII。 | [方法条目](../by-type/idor-access-control.md) |
| XSS shell 流水线先修正输入和保留请求语义 | 保存 XSS automation 管道存在域名/列表输入混淆与未配对引号，不运行原命令。 | [方法条目](../by-type/xss.md) |
| Burp 扩展名称和 passive 标签不代替动作审核 | 帖列 Autorise、Upload Scanner、Param Miner，并称隐藏参数/缓存分析 passive。 | [方法条目](../targeted-fuzzing.md) |
| Rails Accept 文件泄露按 render file 条件判断且读取正文 | 保存截图含点段 Accept 候选，404 正文却有账户文件风格内容；另图 Rails 识别只有 50% sure。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 无用户名随机口令响应要排除环境内已有认证 | 保存帖声称随机密码且空 username/email 可 ATO，没有身份结果。 | [方法条目](../by-type/authn-session.md) |
| cmd code ping 参数名只是 sink 审计候选 | 保存帖给 cmd/code/execute/feature/ping/load/process/req/query 名称清单。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Deadfinder 404 死链不自动证明可控内容或接管 | 保存 sitemap 图列少量 404。 | [方法条目](../discovery/web-and-api.md) |
| 邮件 iframe 假设要确定实际渲染和过滤消费者 | 保存问题只询问 email iframe，没有示例响应。 | [方法条目](../by-type/xss.md) |
| 企业邮箱字符串与 SSO 组织权限不得直接等同 | 邮箱注册/企业 SSO 提权卡只给假设。 | [方法条目](../by-type/authn-session.md) |

| UUID 泄漏与 IDOR 入口矩阵分别核对对象权限 | UUID难猜不替代授权。 | [方法条目](../by-type/idor-access-control.md) |
| 字符索引形式的安全头要追溯生成与浏览器处理 | 响应截图把头文本拆成0、1等数值字段和单字符值。 | [方法条目](../by-type/xss.md) |
| 参数与授权工具按实际重放副作用划分 | Param Miner、Autorize、InQL名称清单只提供工具候选。 | [方法条目](../discovery/web-and-api.md) |
| Jira QueryComponent 页面区分公开项目与私有元数据 | 保存截图称/secure/QueryComponent!Default.jspa可匿名查看问题与项目名。 | [方法条目](../by-type/info-secrets.md) |
| PHP 路径过滤必须在分隔符转换后核对最终文件 | 挑战源码先循环删除../再OSPath转换斜杠，随后include("home/"+输入)；转换可重新引入点段，home前缀不保证目录边界。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 日志追加到 include 的执行链保留每个前提 | 同一PHP挑战把原始lang追加到logs/log.txt。 | [方法条目](../by-type/cmd-injection-rce.md) |
| refresh SSO JWT 与 authType null 是不同认证候选 | 保存清单列refresh、SSO、CMS、示例JWT和authType=null。 | [方法条目](../by-type/authn-session.md) |
| 角色邀请的接受与降级必须使旧授权失效 | Reddit Talk报告摘要指出speaker/host offer接受或降级后仍可复用。 | [方法条目](../by-type/business-logic.md) |
| WordPress 集合与单项作者入口复核同一可见性规则 | 图片列wp-json用户集合、单项、rest_route和author入口。 | [方法条目](../by-type/info-secrets.md) |
| 混淆字符必须跨传输和解析层验证真实执行 | top属性十六进制字符串、百分号编码和Sucuri分数字符片段属于上下文候选，按保存原文保留实际字节。 | [方法条目](../by-type/waf-bypass.md) |
| OTP 限制按账户与挑战状态核对 | Cloudflare历史摘要称失败多次仍可猜OTP，后以限制2FA尝试修复。 | [方法条目](../by-type/authn-session.md) |
| 盲 XSS 追踪提交字段到异步渲染消费者 | 归档给User-Agent替换、signup/demo表单、邀请用户名/mention和票务摘要。 | [方法条目](../by-type/xss.md) |
| 固定 URL 前缀加 endpoint 仍需验证最终 authority | localhost/test截图把endpoint由/adduser改成@attacker.com/adduser，正文声称后端拼接固定网址；没有实际响应或连接证据。 | [方法条目](../by-type/ssrf.md) |
| SQL 扫描器比较要隔离旧 session 和网络失败 | Ghauri图片有时间注入、旧session恢复、库名提取及尚在测试的输出；sqlmap图片同时有301、随机UA、WAF、超时、显著延迟和403。 | [方法条目](../by-type/sql-injection.md) |
| 会话低影响项组合需证明连接处的权限 | P5/P4/P3混成P1示意只有组合主张。 | [方法条目](../by-type/authn-session.md) |
| jQuery UI 选项注入按初始化与后续事件分开验证 | 保存卡列position.of、dialog.closeText、tooltip/title与dialog/title等历史消费者。 | [方法条目](../by-type/xss.md) |
| 代理与后渗透工具保留初始执行及身份前提 | Java字节码客户端、GC2 Sheets/Drive、REAVE ESXi、Gofrette回连、ReverseSSH及DonPAPI属于不同已有执行/凭据上下文。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 请求转模板和 matcher 改写必须保留真实语义 | Burp图片只见localhost基线与Nuclei入口，另一帖仅建议word转DSL，没有完整模板。 | [方法条目](../targeted-fuzzing.md) |
| Git 元数据泄漏区别于正常公开 ignore 文件 | Git/SVN字典混有HEAD/config/index/logs和gitignore等普通公开内容。 | [方法条目](../by-type/info-secrets.md) |
| CodeQL 查询贡献奖励与实际应用漏洞分开记录 | Python邮件、Java路径/regex及C++证书主机名卡片是查询贡献奖励，未保存查询源或真实应用数据流。 | [方法条目](../source-audit.md) |
| 删除考核结果复测必须绑定自有对象并读回 | LinkedIn报告摘要以profileId和skill构造DELETE目标，公开UUID不授予删除权限。 | [方法条目](../by-type/idor-access-control.md) |
| 报告聚合保持 finding 与原始证据对应 | PeTeReport示例把产品、报告、finding与CWE等级聚合。 | [方法条目](../reporting.md) |
| DNS 验证与实际连接分别绑定解析结果 | LINE历史摘要称参数DNS验证可绕过，没有具体请求。 | [方法条目](../by-type/ssrf.md) |
| 多归档索引的 EVERYTHING 不等于完整覆盖 | waymore卡列多个索引，正文建议根域取所有内容。 | [方法条目](../discovery/records-and-incremental.md) |
| 密钥字段搜索保留仓库范围与可用性边界 | GitHub字段、文件后缀、多语言关键字与JS/JSON候选只能发现文本；图片一行重叠，不还原不可读字符。 | [方法条目](../by-type/info-secrets.md) |
| Connection 指定字段要比对各 hop 的真实分帧 | Akamai历史截图开头解释逐跳头和Connection字段，正文后续未保存。 | [方法条目](../by-type/request-smuggling.md) |
| 依赖混淆从 resolver 选择到下游消费者逐段证明 | POC安装说明与OAST curl回连没有构建选择链。 | [方法条目](../source-audit.md) |
| 历史 win.ini 读取摘要不能替代当前路径实证 | Sony报告摘要把win.ini读取关联到CVE2018-1271，没有完整请求或部署版本。 | [方法条目](../by-type/lfi-path-traversal.md) |
| crossdomain URL 的读取取回与渲染分成独立链 | Sony摘要把url参数关联LFI、EC2元数据和外部SVG取回后的反射XSS。 | [方法条目](../by-type/ssrf.md) |
| findusers 排序白名单的类型问题要追到 SQL sink | ImpressCMS截图仅见POST groups进入函数、user_sort经in_array映射白名单与默认uname，user_order后续截断。 | [方法条目](../by-type/sql-injection.md) |
| GitHub 导入的 JSON 方法映射要追到后续调用 | GitLab截图描述Sawyer将JSON键映射Ruby方法，报告声称Redis命令注入；代码下部与完整调用链未保存。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 接管候选必须核对服务状态与可申领权限 | subfinder/subzy流水线与Azure cloudapp.net约三日释放说法都是历史候选。 | [方法条目](../by-type/subdomain-takeover.md) |
| all 扫描要展开协议端口与误判条件 | zBuster帮助中的all明确不含目录探测；Nmap图片为TCP SYN全端口，跳过探活/DNS、低重试与RST限制设置，并警告closed可能变filtered。 | [方法条目](../discovery/passive-and-services.md) |
| 403 转 404 先排除身份时间与边缘状态变化 | 多次发送XSS后状态从403变404不能证明绕过或漏洞消失。 | [方法条目](../experiment-design.md) |
| OSINT 工具结果保持来源和身份歧义 | Vichiti菜单混合WHOIS、定位、URL展开、端口扫描等；Nexfil同名profile返回列表并有超时/DNS设置。 | [方法条目](../discovery/passive-and-services.md) |
| 收据成功模板要排除跨请求残留对象状态 | 图示合法id返回success、另一id先error，再接合法请求后也success。 | [方法条目](../by-type/idor-access-control.md) |
| Cloudfox all checks 保留区域权限错误与缓存来源 | 截图在assumed-role下列inventory、instances、secrets、IAM模拟等，同时存在任务失败、部分结果和缓存说明。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 历史 URL 到主动扫描之间增加范围与队列校验 | XSS管道和目录扫描建议把所有存活子域送入探测。 | [方法条目](../targeted-fuzzing.md) |
| 缓存扫描器标题不替代 key 隔离证据 | Web Cache Scanner图片只有名称，没有真实检测细节。 | [方法条目](../experiment-design.md) |
| PHP 扩展黑名单需要真实处理器和存储证据 | Laravel历史PR截图只显示补充扩展名，正文按PHP7/8列黑名单。 | [方法条目](../by-type/file-upload.md) |
| 邮件头解析保留信任边界与链接错配 | HeadMail图片展示本地文件解析Received-SPF、sender和Content-Type，正文仓库URL却指向缓存扫描器。 | [方法条目](../by-type/info-secrets.md) |
| SQL 片段按查询上下文与方言做最小对照 | 保存帖子包含引号/注释、布尔值、ORDER BY、UNION和id数组等片段，速查图还列不同数据库拼接方式。 | [方法条目](../by-type/sql-injection.md) |
| 搜索注册入口与 GraphQL 错误保持索引边界 | register关键词结果可只是FAQ；GraphQL错误码可指鉴权拒绝或持久查询缺失，Censys title也只是一种索引字段候选。 | [方法条目](../discovery/web-and-api.md) |
| ServiceStack metadata 与真实业务权限分开审计 | ResourceRequest页面列路径、方法、参数/响应类，metadata列XML/JSON/SOAP、XSD/WSDL操作。 | [方法条目](../discovery/web-and-api.md) |
| 分布式 SSH 尝试保留连接失败与认证结果区别 | OrbitalDump截图用多个代理进行口令尝试，混合连接错误和成功标签。 | [方法条目](../by-type/authn-session.md) |
| 旧 API 与相邻子域各自核对当前策略 | v3转v1和app/dashboard/api相邻配置只是发现假设。 | [方法条目](../by-type/idor-access-control.md) |
| CLI 文件路径警报核对调用者与真实写入语义 | Hyperledger截图的os.Args[3]经resultPipeName进入os.OpenFile，标志为APPEND｜WRONLY；这是可见写消费者，不能照报告文字称已读任意文件。 | [方法条目](../source-audit.md) |
| ACME challenge 文本先核对预期公开用途 | 截图仅well-known/acme-challenge路径与遮盖字符串。 | [方法条目](../by-type/info-secrets.md) |
| 功能清单按对象角色状态和消费者建模 | 脑图与organization/export/view/subuser/share等清单用于建立业务候选，不从功能名自动判定XSS/IDOR/SQL/SSRF。 | [方法条目](../business-modeling.md) |
| DNS MX 与 zone IP 不扩大主动网络范围 | DNS/MX/zone关联只是候选与历史来源。 | [方法条目](../discovery/passive-and-services.md) |
| 自动化与手工并行保持请求和状态归因 | 后台自动化同时手工测试时，为每个逻辑操作记录身份、对象、时间、标记及来源，按目标合并速率与请求预算。 | [方法条目](../experiment-design.md) |
| 跳转候选按真实解析结果而非字符串特征判定 | 保存图列redirect/next、userinfo、斜杠、百分号、控制字符等，资源清单不是每个payload实测。 | [方法条目](../by-type/open-redirect.md) |
| 移动客户端 pinning 结果绑定具体 build 与端点 | 旧iOS/Android版本建议只提供候选。 | [方法条目](../discovery/client-and-cloud.md) |
| 迁移 step2 不能代替对前序身份与对象的校验 | Liberapay截图称POST migrate?step=2可跳过前序，任意email_address与username组合返回主邮箱。 | [方法条目](../by-type/business-logic.md) |
| Flask 字符删除不能覆盖 HTML script 与 DOM 两层 | 挑战源码在/profile取name、删除单引号后格式化到script中的JavaScript字符串，随后innerHTML追加。 | [方法条目](../by-type/xss.md) |
| APK 字符串 URL 管道保留构建与调用上下文 | 保存apktool/grep管道混用package名与文件输入，正则可能截断query、Unicode和复杂路径，广泛排除Google/GitHub也可能隐藏自有Firebase/OAuth配置。 | [方法条目](../discovery/client-and-cloud.md) |
| ASN route 查询保留多 origin 与 IPv6 缺口 | 保存RADB管道用首个origin与route提取，whois主机文字混有http://。 | [方法条目](../discovery/passive-and-services.md) |
| Salesforce debug shell 页面不证明服务端执行权限 | 图片显示soap/ajax/22.0/debugshell.html的空编辑框，没有执行或返回。 | [方法条目](../discovery/web-and-api.md) |
| 安装与管理端点区分配置可见和状态修改 | 正文列adminconsole/install.htm，图片只是修改admin/DB配置的P1标题。 | [方法条目](../discovery/web-and-api.md) |
| localhost Host 差异核对路由与授权来源 | 保存帖只有403后换Host的线程开头，后续未保存。 | [方法条目](../discovery/web-and-api.md) |
| 条件重写与宏保留修改前后的实际请求 | Reshaper题名提及规则/宏没有完整配置。 | [方法条目](../experiment-design.md) |
| 带外参数发现分开 DNS HTTP 与消费来源 | lorsrf正文和卡片把SSRF与out-of-band resource load列为候选。 | [方法条目](../by-type/ssrf.md) |
| 研究收益比较保留时间预算与可验证假设 | 研究竞争天平把复杂冷门与易懂热门内容比较，未给收益数据。 | [方法条目](../hunting-strategy.md) |
| ProxyNotShell 的 IIS 404 不能作为漏洞确认 | 保存ffuf流水线以IIS Web Core/404为vulnerable，另帖URL中断行。 | [方法条目](../by-type/ssrf.md) |
| 项目响应时长与投入期限记录实际条件 | 保存帖建议快确认/支付项目并坚持超过一月。 | [方法条目](../hunting-strategy.md) |
| ASP.NET 指纹不构成 SQL 注入证据 | 保存帖建议看到ASP.NET就用sqlmap，图片大部分正文被侧栏遮盖。 | [方法条目](../by-type/sql-injection.md) |

| 布尔登录与路径错误注入按消费者做对照 | SQLbit仅自动化简介，登录片段与组织API extractvalue截图缺实际响应。 | [方法条目](../by-type/sql-injection.md) |
| wpeprivate 的 302 与敏感文件可读分开判断 | 保存帖称_wpeprivate目录P1，图仅标题。 | [方法条目](../by-type/info-secrets.md) |
| WAF 归一化和 HTML 字符引用需要真实字节证据 | 正文只给filter collision/normalization名称与SVG事件字符引用片段。 | [方法条目](../by-type/waf-bypass.md) |
| 用户名存在与公开反馈 UUID 不证明接管 | username_exist请求及反馈PUBLIC评论响应只能说明可见入口/标识候选，遮盖内容不能恢复。 | [方法条目](../by-type/idor-access-control.md) |
| TLS 套件枚举绑定主机 SNI 时间与握手条件 | CipherScan截图列协议、套件、PFS、曲线、证书信任与OCSP等。 | [方法条目](../discovery/passive-and-services.md) |
| IDOR 清单按真实解析和对象矩阵拆分 | 保存清单覆盖URL/头/body、重复参数、通配符、版本/扩展、方法、Referer、UUID、导出与跨请求状态。 | [方法条目](../by-type/idor-access-control.md) |
| 盲 XSS 管道修正输入类型与异步来源边界 | subfinder输入写成http://target.com，gau后grep &会遗漏单参数/POST/无query入口。 | [方法条目](../by-type/xss.md) |
| CORS 批量管道须验证浏览器实际共享的认证响应 | 保存命令用target=$(curl...)后grep未连接变量，curl -I仅取头且语法残缺，不执行。 | [方法条目](../by-type/cors.md) |
| 公司名和 Web3 私钥关键字只形成代码候选 | 公司名language:python结果与ETH/BSC/privateKey/hardhat字段搜索需绑定获准owner/repo、来源时间及代码上下文。 | [方法条目](../by-type/info-secrets.md) |
| 跨移动入口到缓存 XSS 要验证每个消费者 | 正文称网站WAF拦截、移动入口写username、xss.css被缓存，图仅Triaged通知。 | [方法条目](../by-type/xss.md) |
| 验证码缺失与方法类型变化按服务端挑战校验 | 清单建议改变方法/JSON、置空或查看源码。 | [方法条目](../by-type/authn-session.md) |
| Cognito token 签发和资源授权独立核对 | 图仅User Pool认证取token后访问自有资源，未保存misconfiguration。 | [方法条目](../by-type/authn-session.md) |
| 误构建源码公开需确认 artifact 与预期边界 | Cloudflare摘要称backend代码公开并修复，未见具体文件。 | [方法条目](../by-type/info-secrets.md) |
| dashboard 标识发现与 profile 修改独立读回 | MTN步骤称dashboardData返回email/id，再修改userProfile请求的id/email影响另一账户。 | [方法条目](../by-type/idor-access-control.md) |
| 启动脚本到 central config 保留实际可见范围 | run/startup/entrypoint文件名只是探测候选，JSON图含安全开关、TTL、ActiveMQ与遮盖凭据。 | [方法条目](../by-type/info-secrets.md) |
| Autodiscover 协议响应不单独确认 ProxyNotShell | Acronis历史报告把404与Outlook ActiveSync JSON当41040证明，裁决记录不替代可复现机制。 | [方法条目](../by-type/ssrf.md) |
| 多层 API 版本路径先确认真实路由 | 版本目录组合只提供候选。 | [方法条目](../discovery/web-and-api.md) |
| Linkpop 回归与 self XSS 按新旧存储值和消费者验证 | 截图有旧name残留blindscript、onboarding前几步及addlink javascript输入。 | [方法条目](../by-type/xss.md) |
| 学习闭环把实验条件和负例写进笔记 | 图示视频/书→Labs→Notes→writeups/code review/练习。 | [方法条目](../hunting-strategy.md) |
| Fortinet 端口到模板管道保留范围与原始验证 | 图片给子域/多个端口送入模板与多条40684命中，没有模板内容和响应。 | [方法条目](../targeted-fuzzing.md) |
| shellcode 与 C2 演示不证明通用免杀或初始入口 | 图片为已有本地exe执行后回连、Defender设置、ClamAV分段扫描与C2监听。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 账户信息 CSRF 到恢复流程逐步绑定真实身份 | my-account.cfm摘要称CSRF更新信息后password reset接管，code未保存。 | [方法条目](../by-type/csrf.md) |
| VendorId PII 报告保留未验证 ATO 状态 | 作者明确未测多功能/ATO且PoC遮盖。 | [方法条目](../by-type/idor-access-control.md) |
| EditUserProfile 邮箱冲突序列核对密码写入对象 | 截图自有A/B序列混合邮箱冲突、userId替换、恢复A字段再以B邮箱/A密码登录。 | [方法条目](../by-type/authn-session.md) |
| 公开注册到用户目录要核对新增角色权限 | OA_HTML注册/本地登录/vacation rules搜索用户摘要属于注册资格与目录权限两阶段。 | [方法条目](../by-type/idor-access-control.md) |
| ESI 头字段再渲染与 HttpOnly 保护边界分开验证 | 图中ms字段调用ESI读取HTTP头，另title消费者反射XSS。 | [方法条目](../by-type/xss.md) |
| 意外访问申请邮件保留不可复现的来源状态 | 报告自述未知何因加入收件组、不知复现且未获得实际访问。 | [方法条目](../by-type/info-secrets.md) |
| 下载 URL 从参数到网络消费者与目录结果逐段确认 | SSRF保护清单列hostname、redirect、rebind；image downloader图片只见前端urlParam/decodeURI，另一download-url图返回元数据键目录。 | [方法条目](../by-type/ssrf.md) |
| 操作图和时间线保留 task 与结果身份关联 | RedEye截图呈现任务、日志、beacon边与ATT&CK标签。 | [方法条目](../discovery/records-and-incremental.md) |
| Netlify 误配置摘要保留申领条件的证据缺口 | 历史8x8摘要称Netlify目标可接管后修复，无DNS或申领过程。 | [方法条目](../by-type/subdomain-takeover.md) |
| 侦察产物和脑图不能代替执行覆盖 | 状态桶、GAU/dnsIP/JS/secrets文件名和域→端口→dorks→JS→fuzz→手工图描述流程。 | [方法条目](../discovery/records-and-incremental.md) |
| profile 多版本返回字段按发布和验证状态核对 | 图称发布profile版本切换，verified/requested版本API额外返回email。 | [方法条目](../by-type/info-secrets.md) |
| git config 到源码与凭据影响分别证明 | 截图有git/config、remote及部分文件名，称gitdumper拿完整仓库。 | [方法条目](../by-type/info-secrets.md) |
| Zabbix 原生脚本 API 按调用角色和执行目标审计 | 保存帖称创建执行script可影响server和受监控主机，图仅文档封面。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 企业邮箱子串与组织成员资格分别验证 | 图建议company.com后拼外域并观察SMTP。 | [方法条目](../by-type/authn-session.md) |
| KnoXSS 流水线避免把候选拼成 shell 指令 | awk把发现URL拼成curl文本再交sh，输入引号或命令字符可改变生成内容，且请求可能向外部服务上传目标。 | [方法条目](../targeted-fuzzing.md) |
| 默认文档凭据需要当前 principal 与权限证据 | 正文称Censys4200发现Write管理台并凭默认文档密码登录，图只界面版本。 | [方法条目](../by-type/authn-session.md) |
| 403 写请求还要从独立会话读回最终状态 | 保存帖提示PUT/DELETE/PATCH/POST即使403也核对UI。 | [方法条目](../by-type/idor-access-control.md) |
| 项目选择把角色场景与实际响应样本分开 | 功能多、角色多、兴趣、响应快与奖金额是选择偏好。 | [方法条目](../hunting-strategy.md) |
| 多斜杠与编码遍历必须确认最终规范路径 | 保存片段含重复点段、多斜杠、绝对前缀与百分号反斜杠。 | [方法条目](../by-type/lfi-path-traversal.md) |
| JS 到云凭据再到 RCE 的每段保留权限前提 | 初学者图串联隐藏JS、外AWS、admin、SSRF、凭据、bucket、私有API与RCE，无请求。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 共享收短信服务不能证明号码控制权 | 保存帖只有公共接收短信链接。 | [方法条目](../by-type/authn-session.md) |
| Markdown 表单注入与脚本执行分开保留消费者 | GitHub截图显示Markdown里登录表单/input/button/textarea，没有提交或执行证据。 | [方法条目](../by-type/xss.md) |
| 业务请求顺序实验定义状态机与停止条件 | 正文建议改参数/头/Cookie、跳步、重放与省略，未保存第二部分。 | [方法条目](../by-type/business-logic.md) |
| NIN 验证中的手机 OTP 绑定和最终状态独立证明 | 截图只有进入流程、输入手机号/NIN与发送OTP摘要，后续绕过未保存。 | [方法条目](../by-type/authn-session.md) |

| 走私队列示意需落到实际分帧和响应归属 | 两张图描述前端/后端不同队列与未结束请求拼接、响应串到下一请求，但没有原始报文。 | [方法条目](../by-type/request-smuggling.md) |
| Go role Cookie 与转发地址不得代替受信身份 | 可见Go示例将role Cookie与X-Forwarded-For直接用于admin判断，按冒号切分与127.0.0.1/localhost比较；还未检查Cookie错误即取Role.Value，普通HTML在权限判断前输出。 | [方法条目](../by-type/authn-session.md) |
| Linux 提权清单绑定已获会话和实际执行身份 | 截图列系统/挂载/软件/进程/cron/服务、PATH、环境、sudo/SUID/capabilities/ACL等类别。 | [方法条目](../by-type/cmd-injection-rce.md) |
| CRLF 编码变体核对最终头边界 | 图片为换行、回车及多重百分号编码的Set-Cookie清单，没有响应。 | [方法条目](../by-type/crlf-response-splitting.md) |
| ASP 重复参数拼接和动态脚本载入逐层验证 | 正文展示重复id被逗号拼接成HTML/JS，另示例在img事件中动态创建script；作者已标明依配置而异。 | [方法条目](../by-type/waf-bypass.md) |
| 下线域名和源站直连是不同修复验证路径 | 正文称站点下线后通过索引IP仍能读文件，图一仅DNS失败，图二直IP路径-as-is/k请求200及脱敏文件格式。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 营销参数的 CSS 动画事件按实际模板验证 | Shopify摘要显示utm_source输入尝试结束属性、设置animation-name与animationstart；未保存完整DOM/执行环境。 | [方法条目](../by-type/xss.md) |
| 自定义接管页面需要 DNS 和申领时间线支撑 | 截图仅自定义PoC页面/遮盖域名与店铺，没有原DNS、供应商资源或申领过程。 | [方法条目](../by-type/subdomain-takeover.md) |
| 学习路线以机制和授权实验检验进步 | 图列计算机基础、网络/Linux/Web语言、编程与靶场，并强调实践。 | [方法条目](../hunting-strategy.md) |
| 资产管道区分索引查询和主动验证预算 | Kunyu帮助列Host/Web/Icon/Cert/Domain查询、HostCrash与AliveScan；另一图把subfinder/dnsx/cf-check送naabu再httpx。 | [方法条目](../discovery/passive-and-services.md) |
| Host 变化的配置响应比较须追踪真实路由 | 三图分别原Host403、无Host400和127.0.0.1返回JSON头200，配置正文未显示，HTTP2伪头信息不全。 | [方法条目](../by-type/info-secrets.md) |
| 反序列化类型转换发生在对象读取之后 | 截图概述readObject在最终类型检查前可能执行对象逻辑，条件包括实际不可信字节进入反序列化及可达类路径。 | [方法条目](../by-type/deserialization-rce.md) |
| 404 中的执行现象先定位反射与 DOM 消费者 | 截图可见404消息、损坏图片及alert遮盖，但不足定位是服务端反射还是DOM插入。 | [方法条目](../by-type/xss.md) |
| 下载 token 与文件下载政策单独核对 | Lark摘要明确已知有效file token后可直URL下载。 | [方法条目](../by-type/idor-access-control.md) |
| 空部门参数不能默认为跨部门管理权限 | Lark摘要称有管理用户section权限的角色把department_id置空后能将用户加到部门范围之外。 | [方法条目](../by-type/idor-access-control.md) |
| 组织管理角色仍需 helpdesk 与日志对象授权 | Lark摘要分别为团队创始人兼另一helpdesk管理员可读无权ticket图像，以及低权限角色可读admin日志。 | [方法条目](../by-type/idor-access-control.md) |
| 匿名 API 与示例服务按实际字段可见性判影响 | 图摘要涉及未登录获得TikTok创建日期、SAM system accounts中的邮箱/IP/组织地点/身份提供者信息、Tomcat示例披露内部IP。 | [方法条目](../by-type/info-secrets.md) |
| 旧报告回归复测记录修复版本与新消费者 | 正文及图建议重访旧报告，IDOR多次修复绕过只作示例。 | [方法条目](../discovery/records-and-incremental.md) |
| GraphQL schema 可见不等于 SQL 注入 | 正文标题SQLi但图实际为__schema和types/fields返回，未见数据库sink或结果。 | [方法条目](../by-type/graphql.md) |
| 易受攻击依赖须证明应用内可达影响 | 保存帖要求不能仅因库被标为有漏洞就报告可利用。 | [方法条目](../impact-and-acceptance.md) |
| Whois 数据服务作为关联线索保留来源限制 | 保存帖列Whois服务索引，无实际查询结果。 | [方法条目](../discovery/passive-and-services.md) |
| ZAP 与 OAST 的关联须落到原始操作 | 正文只说明给ZAP加入interactsh，无集成配置。 | [方法条目](../targeted-fuzzing.md) |
| 时间型 GUID 候选与恢复令牌可用性分阶段确认 | 正文声称近似生成时间可缩小v1 GUID猜测空间，但未保存工具实现或真实恢复请求。 | [方法条目](../by-type/authn-session.md) |
| Swagger 管理 API 按角色和下游消费者核对 | 正文分别声称公司邮件API支持HTML/XSS/附件和admin接口可读PII，图只奖励/Duplicate元数据。 | [方法条目](../by-type/idor-access-control.md) |
| 订单币种参数要核对服务端结算与权限授予 | 截图描述orders/new?p=214增加cur=usd后界面同数值不同币种，状态为Informative。 | [方法条目](../by-type/business-logic.md) |
| TaxJar 恢复 token 与 URL 账户对象不能错配 | 同图供应商称reset token未正确绑定URL account ID，作者称Accountant Access POST账户编号与email替换；保存材料不足还原两叙述如何串联。 | [方法条目](../by-type/authn-session.md) |
| 本地 gRPC Listen 的安全边界保留本机前提 | Stripe-cli摘要说明daemon暴露本地无认证gRPC，另一已安装应用可调用Listen得到当前账户webhooks；供应商保留本机妥协/物理或中间人前提。 | [方法条目](../by-type/desktop-client.md) |
| 双层括号过滤差异需要统一解析与连接对象 | Smokescreen历史摘要指出deny_list处理只剥一组括号，双括号绕过，历史修复剥全部。 | [方法条目](../by-type/ssrf.md) |
| 成员自邀管理员须核对角色授予权限 | TaxJar current_user_data摘要称member可邀请自己成为admin。 | [方法条目](../by-type/idor-access-control.md) |
| 历史无奖励邮件不替代当前项目范围规则 | 截图显示Telekom历史报告被确认但不符当时奖励条件，可列HOF；正文用户名玩笑不代表项目整体无价值。 | [方法条目](../scope-and-rules.md) |
| Create Invite CSRF 区分发送和实际加入团队 | Lark摘要称诱导用户运行PoC可触发邀请，缺表单/token/cookie细节。 | [方法条目](../by-type/csrf.md) |
| 撤销文档成员后 message API 权限需重新评估 | Lark摘要指出撤成员后仍通过message API读评论。 | [方法条目](../by-type/idor-access-control.md) |
| 源码和汇编步进对应当前执行路径 | PTrace图展示C变量、factorial及汇编步进。 | [方法条目](../source-audit.md) |
| File Uploaded 不证明未认证或任意覆盖 | 图为multipart destination=gallery/与poc.txt，含Authorization并回200 File Uploaded，标题宣称认证绕过与任意覆盖。 | [方法条目](../by-type/file-upload.md) |
| 初学类别和扫描器重复率是选择偏好 | 正文建议先看IDOR/访问控制/业务逻辑，同时覆盖更广；另作者将低重复率归因少用自动扫描。 | [方法条目](../hunting-strategy.md) |
| 代理容器的 wget 成功不证明无追踪 | WOT终端仅wget跟随跳转并保存页面，未见代理出口或DNS路径。 | [方法条目](../discovery/passive-and-services.md) |
| 301 正文中的 MariaDB 错误按编码和上下文比较 | 保存正文比较单/双引号与%22，图中301正文含WordPress数据库语法错误，另sqlmap有tamper未纳入所示payload警告。 | [方法条目](../by-type/sql-injection.md) |
| POOL_UPGRADE package 到 shell 的验证链需完整 | Hyperledger indy摘要给package→check_upgrade_possible→curr_pkg_info→get_curr_info→compose_cmd dpkg -s→run_shell_command路径。 | [方法条目](../by-type/cmd-injection-rce.md) |
| shell 词绕过依赖真实展开和执行上下文 | printf管道多次sh示例以及restricted shell图列glob、引号、反斜杠、变量、替换和history；部分截图右/底截断。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 代理与时间阈值变化不能代替盲注因果对照 | 正文建议sqlmap受阻后Tor/proxy和time-sec=10，但无原始请求/响应。 | [方法条目](../by-type/sql-injection.md) |
| 理解应用落实到业务不变量和消费者 | 保存帖只有理解应用建议。 | [方法条目](../business-modeling.md) |
| 报告 ID 与返回 shareable 配置分别核对权限 | Datastudio图显示sourceReportId指向B并返回reportConfig/viewMode/name/page值，认证和共享前提未完整保存。 | [方法条目](../by-type/idor-access-control.md) |
| 本地响应修改须验证独立服务端终态 | 正文仅说Burp修改响应令人满意。 | [方法条目](../experiment-design.md) |
| 试用绑卡绕过与永久付费权益分开验证 | Krisp标题为完全支付绕过，但供应商摘要只说明business trial未强制绑卡。 | [方法条目](../by-type/business-logic.md) |
| 图形化 Text4shell 流水线保留队列与回连来源 | Trickest图将targets经gau/静态扩展过滤/get-all-urls，同callback生成payload后qsreplace/ffuf，未见源码模板或执行结果。 | [方法条目](../targeted-fuzzing.md) |
| PHP filter 链须到实际 include 和可用编码器 | 保存图只有php require filter的iconv/base64长串，横向裁切，资源/完整输出未见。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 模拟浏览请求不证明隐私保护效果 | PartyLoud图用URLlist/blocklist生成HTTP请求并检查curl等依赖。 | [方法条目](../experiment-design.md) |
| 资料导航与实际学习覆盖各自留记录 | Cheatsheet按资源/漏洞类型导航、CTF资源目录及BountyGuide项目方/研究者分栏，仅说明材料入口。 | [方法条目](../hunting-strategy.md) |
| 自动化存储与通知按候选和实证分级 | 笔记建议可搜索存储、按日批次、精筛通知、工具包装和变化检测。 | [方法条目](../discovery/records-and-incremental.md) |
| 学习习惯与合作条款不能保证一年收入 | 12months笔记的100%赚钱、自动化时间越多收入越高属宣称，不采纳因果保证。 | [方法条目](../hunting-strategy.md) |

| 移动检查目录分别验证客户端与服务端边界 | 截图列Android/iOS静态逆向、动态、网络/服务端及root/pinning检查和MobSF，底部截断。 | [方法条目](../discovery/client-and-cloud.md) |
| favicon 哈希关联仍需独立资产归属 | 图片用favicon哈希查Shodan等索引，结果显示IP和Web响应。 | [方法条目](../discovery/passive-and-services.md) |
| GitHub 扩展搜索区分配置索引和真实秘密 | 图列env/cfg/json/pem/ppk/sql等后缀与private/client_secret关键词。 | [方法条目](../by-type/info-secrets.md) |
| installed.json authors 不是目标管理员证明 | 截图引用vendor/composer/installed.json作者字段，将第三方维护者信息称admin，最终Informative。 | [方法条目](../by-type/info-secrets.md) |
| 上传清单按校验存储和消费者分段验证 | 图列扩展/双后缀/regex/大小写、SVG、Content-Type、magic bytes与尺寸，底部nullbyte部分未全存。 | [方法条目](../by-type/file-upload.md) |
| VDP 和学习安排按目标与可测证据选择 | 正文用初学/中级/高级谈VDP价值，另提工作学习时间与靶场资料。 | [方法条目](../hunting-strategy.md) |
| 单一 alert 样式不能代表输入上下文覆盖 | 正文批评到处重复script/alert，续篇未保存，图只Stored XSS裁决元数据。 | [方法条目](../by-type/xss.md) |
| WordPress 文件与路由候选先验证实际入口 | 两张保存图列wp-json、uploads、login、config、cron、xmlrpc等并重复signup，部分候选写法不全。 | [方法条目](../discovery/web-and-api.md) |
| 自动化 PoC 要便于复核并保留真实前提 | 截图只有运行遮盖Python脚本、输入email、Random/EmailSpecific与massscale描述，无源码或结果；另一帖仅报告生成器链接。 | [方法条目](../reporting.md) |
| LFI 参数名称只是消费者假设 | 图给file/download/path/include/page/conf等25名，没有请求结果。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 404 接管指纹与可申领条件分别记录 | 作者明确SubOver/指纹表称可接管而实际无法，图为Cargo404历史标签。 | [方法条目](../by-type/subdomain-takeover.md) |
| 头字段与 DELETE 注入核对实际数据库消费者 | 正文提醒User-Agent/Referer及DELETE方法，截图奖励列表无原始请求。 | [方法条目](../by-type/sql-injection.md) |
| 扩展 detected 输出仍需实际浏览器执行证据 | S3C窗口列POST/GET/hidden参数测试和detected链接，没有DOM或执行截图。 | [方法条目](../by-type/xss.md) |
| Jenkins 构建触发候选先审计权限和任务配置 | 保存帖称nuclei命中Git Plugin缺权限检查，可触发已配置仓库任务，但作者仍求PoC。 | [方法条目](../by-type/idor-access-control.md) |
| 侦察工具和脑图每阶段绑定来源与执行结果 | 列表/Methodology图涵盖种子、ASN、reverseWhois、证书/JS、子域/变化、端口/服务、GitHub、截图、接管和自动化。 | [方法条目](../discovery/records-and-incremental.md) |
| 本地遍历读取与远程文件解释分开确认 | RFI图先画../到本地文件，再画远程PHP URL，缺实际环境。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 源码凭据与 token 响应保持实际权限缺口 | 正文称admin源码命令泄露和JSdev超级账户，图只有裁决元数据、JSON.stringify username/password/post片段及A1token.jsp遮盖access_token。 | [方法条目](../by-type/info-secrets.md) |
| HTML escape 不替代动态模板源隔离 | Flask片段把search先html.escape，MySQL_Get失败时将值百分号插进HTML字符串后render_template_string。 | [方法条目](../by-type/ssti.md) |
| 邮箱域名和员工角色授予需要受信证明 | 正文建议注册目标域邮箱获得员工权限，未说明邮箱所有权或验证。 | [方法条目](../by-type/authn-session.md) |
| Informative 裁决围绕受影响身份补最少证据 | 图说明行为仅涉及注册邮箱且注册需邮箱验证，作者认为高危/未看视频，未保存实际机制。 | [方法条目](../impact-and-acceptance.md) |
| 无头爬虫与 JS 链接解析覆盖真实交互条件 | 正文提Wapiti历史无头/认证改进与ZAPAjaxSpider、Jsparser/Linkfinder比较，无实测。 | [方法条目](../discovery/web-and-api.md) |
| 公开 cAdvisor 指标与容器控制分开证明 | 图摘要指出cAdvisor8080公开性能/资源指标，作者称连续监控发现，没有完整响应或监控配置。 | [方法条目](../cloud/container-k8s-security.md) |
| 文件 token 权限须覆盖回收站和历史版本 | Lark摘要分别为viewer已知folder token永久删除admin回收站内容，以及只获某版本查看权却读取旧版本。 | [方法条目](../by-type/idor-access-control.md) |
| 管理角色对 Owner 的禁用需确认产品边界 | Linktree摘要称admin可永久使Owner无法访问，图没有请求或恢复步骤。 | [方法条目](../by-type/idor-access-control.md) |
| Swagger 的 HTML 注入与脚本执行分层保留 | 两图分别供应商确认RXSS摘要与HTML injection摘要，另一弱点标签写DOMXSS但没有真实执行。 | [方法条目](../by-type/xss.md) |
| 社区 tips 汇编保留出处和遗漏范围 | BookTips导读明确按分类汇编社区帖子、可能漏项并链接原帖。 | [方法条目](../discovery/records-and-incremental.md) |
| OTP valid 响应修改需要真实会话终态 | 图列自有正确/错误OTP响应code valid/invalid，再把invalid改valid称登录，没有服务端证据。 | [方法条目](../by-type/authn-session.md) |
| ACME 菜单与证书更新任务保留既有权限前提 | WinACME图为Windows/IIS管理员运行菜单、证书创建/更新与计划任务状态。 | [方法条目](../discovery/passive-and-services.md) |
| httpx path 与状态过滤不代表完整目录覆盖 | 图把domains与path wordlist交httpx并过滤400/403/404，没有输出或版本说明。 | [方法条目](../targeted-fuzzing.md) |
| 固定币种价格差先核对定价政策 | PortSwigger历史报告以不同币种固定价格与当时汇率差称套利，图中供应商明确商业决策并Informative。 | [方法条目](../by-type/business-logic.md) |
| SBOM 无命中保留提供者与组件匹配缺口 | Bomber图为0.1.1、Go25包、OSV提供者无命中，并明确不能证明无漏洞。 | [方法条目](../source-audit.md) |
| 随机源失败必须连到密钥输出消费路径 | Node历史摘要称SecretKeyGenTraits::DoKeyGen忽略EntropySource返回，熵初始化失败可能不写buffer或写弱值，图未存完整源码/复现。 | [方法条目](../source-audit.md) |
| 空头与折叠 TE 回归按字节和代理差异确认 | Node历史图涉及空header后的单LF引出Transfer-Encoding、obs-fold及multi-line TE修复不完整；后两图请求/测试代码未保存完整。 | [方法条目](../by-type/request-smuggling.md) |
| 构建遗留 OpenSSL 路径连接共享主机写权限 | Node18macOS摘要称启动会读构建者/home/iojs/build下openssl.cnf，攻击前提为共享主机能创建该路径。 | [方法条目](../source-audit.md) |
| 转发 IP 头是否影响限额需核对受信来源 | 正文列X-Forwarded/Client/Remote/Originating-IP等候选，没有实测。 | [方法条目](../by-type/authn-session.md) |
| C2 界面区分既有 agent 和初始执行证明 | Heroinn图显示Linux/Windows agent、whoami、进程/crontab与文件传输，没有安装/初始入口过程。 | [方法条目](../discovery/records-and-incremental.md) |
| Ping sweep 输出地址必须对应实际发送目标 | 正文Bash广播式后台ping，Windows命令ping 172.21.10网段却echo另一192.168.1地址。 | [方法条目](../discovery/passive-and-services.md) |
| 密码管理菜单和 AES 名称不证明存储安全 | PassLock图仅list/new/show/generate/move/path与部分process error。 | [方法条目](../by-type/authn-session.md) |
| 历史文件提取绑定快照来源和当前状态 | 土耳其文正文说明工具从Wayback取旧文件，无实现/结果。 | [方法条目](../discovery/records-and-incremental.md) |
| Shopify 历史申领摘要不替代当前资源验证 | Gymshark截图称未申领Shopify子域、作者临时申领并密码保护PoC，原DNS/完整申领步骤缺失。 | [方法条目](../by-type/subdomain-takeover.md) |
| crt.sh 到 ffuf 管道保留多值输入和每任务错误 | 正文crt.sh JSON name_value加https、去重、xargs送ffuf，图并发40而正文70，多个任务全Errors且进度100%。 | [方法条目](../targeted-fuzzing.md) |
| Viper 图与模块日志分别证明会话和执行状态 | 图有LABadmin/root、SID/route/reverse连接、模块选择、sysinfo与端口结果。 | [方法条目](../discovery/records-and-incremental.md) |
| URL 路径字典保留解析前后的信息损失 | 图用sed去query/fragment/部分分隔后切路径词并anew去重，未存输出。 | [方法条目](../targeted-fuzzing.md) |
| 遍历读取与 public 缓存标签分别验证 | 图为长点段到文件路径，带遮盖Cookie并返回200/unknown type/public cache与脱敏文件格式。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Jolokia 错误路径与 mimeType 消费者独立确认 | 图述旧1.3.5在read路径输入SVG事件并mimeType=text/html，只有摘要/版本缩图，未见完整响应和执行。 | [方法条目](../by-type/xss.md) |

| IDN 点归一化与 HSTS 主机缓存必须共用规范形式 | 归档 curl 报告描述 IDN 字符 U+3002 被转为 ASCII 点，但 HSTS 检查与实际请求对主机规范化顺序不同，可能使已缓存 HTTPS 主机仍走 HTTP。 | [方法条目](../discovery/client-and-cloud.md) |
| netrc 无空白输入检查的是扫描边界与终止条件 | 保存报告指出 curl .netrc 内容不含 ISSPACE 判断为真的字符时，parsenetrc 的扫描可能越界读并发生单字节越界写，长度及内存状态影响表现。 | [方法条目](../source-audit.md) |
| 资产搜索界面与自动 recon 宣传属于有时效的候选来源 | Netlas 保存图展示响应头、证书、IP/端口与 CVE 标签；ReconFTW 图仅展示仓库概要及自动采集宣传。 | [方法条目](../discovery/passive-and-services.md) |
| XSS 流水线的过滤损失与浏览器入口必须分开记录 | 保存命令组合历史 URL、gospider、gf、qsreplace、dalfox/nuclei；grep 200、awk 第五列、grep 等号、sed 截断到等号与扩展名黑名单都依赖输出格式，可能丢失多参数、非 200、路径输入及 JS/SVG/PDF 等资源。 | [方法条目](../by-type/xss.md) |
| XFF 盲 XSS 候选须绑定后台渲染而非仅外部交互 | subfinder/gau/bxss 示例把脚本放入 X-Forwarded-For，并引用远端脚本域；域输入不应直接混用完整 URL。 | [方法条目](../by-type/xss.md) |
| Burp 主机正则和程序范围导入需验证根域及排除项 | 保存正文介绍项目 JSON 范围配置，图展示 Scope 的协议、Host/IP、Port、File 独立字段，主机示例 .*\.target\.com$ 不含根域本身。 | [方法条目](../scope-and-rules.md) |
| 重置链接复用与历史敏感 URL 是不同生命周期问题 | 正文把密码重置链接重复使用和历史 URL 中的令牌/密钥并列。 | [方法条目](../by-type/authn-session.md) |
| CSP 策略评估结果需结合可控输入与实际指令生效 | CSP Evaluator 截图含 unsafe-inline/unsafe-eval、主机白名单、缺 object-src 及未知指令等样例告警；正文列 JSONP、固定 nonce、上传同源文件及 Angular 场景。 | [方法条目](../by-type/xss.md) |
| 自动替换 OAST 的确认单位是原请求和实际交互层级 | AutoRepeater 正则将 URL 替换为 Taborator 占位符并把回调关联原请求；正文/截图还含仅 DNS、Referer、IPv6 及多协议候选。 | [方法条目](../by-type/ssrf.md) |
| 历史 LFI 批扫的 root 文本匹配只是文件读取候选 | 图片展示 gau/gf/qsreplace 将参数替换为文件路径，再并行 curl 并 grep root:x。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Company Info 权限不应隐式授予全员群管理 | Lark 保存报告明确：受邀管理员仅拥有 Company Info 权限，却可编辑、访问和删除 all-staff 群设置。 | [方法条目](../by-type/idor-access-control.md) |
| 公开凭证索引及错误 MIME 源码暴露先识别实际秘密类型 | API Key Leaks 图是多供应商凭证目录；另图 image/jpeg 响应返回 C# WebHandler 源码；公开 Production 配置图含被遮挡/编码的用户名密码。 | [方法条目](../by-type/info-secrets.md) |
| 共享邀请不得把目录级权限扩展到其他用户结构 | Lark 报告描述非 Primary admin 因被邀请查看/修改文件夹而可访问其他用户目录结构。 | [方法条目](../by-type/idor-access-control.md) |
| GraphQL introspection 的分级须落到可访问数据和操作 | 正文讨论 introspection 被不同平台评级，图片只有修复及奖励邮件。 | [方法条目](../by-type/graphql.md) |
| 重定向候选应比较解析后的最终主机而非 Location 子串 | 保存资料含外部 redirect 的 url/urlHash 请求、HEAD grep Location 流水线及反斜杠、Unicode 点、userinfo @、%23、%00、%0d%0a 等候选。 | [方法条目](../by-type/open-redirect.md) |
| CSRF 方法和令牌变异要验证浏览器发送及真实状态变化 | 正文给 POST→GET、空/缺失/改单字符/长度、帐号 A/B 令牌与 null Origin/data URI 候选；保存跨 Origin 认证 POST 图却返回 410 Access Denied。 | [方法条目](../by-type/csrf.md) |
| 元数据凭证字段暴露不能直接写成云 root 控制 | 截图返回 AWS-HMAC、AccessKeyId、SecretAccessKey、Token、Expiration 等字段，标题宣称 SSRF→root。 | [方法条目](../by-type/ssrf.md) |
| 2FA 判断以服务器受保护操作和因子绑定为准 | 正文及十条清单涵盖帐号/组织 2FA、JS/响应泄露、code 复用与跨用户绑定、重置降级、禁用 CSRF、null/000000 和状态篡改。 | [方法条目](../by-type/authn-session.md) |
| 邮箱与时间盲注候选仍需证明输入到查询的语法影响 | 邮箱引号 local-part 可容纳特殊字符，错误提示/参数数组变异可揭示解析差异；MySQL timing 图给 IF/LIKE/now/sysdate/SLEEP 与 ｜｜、&& 变体。 | [方法条目](../by-type/sql-injection.md) |
| 模板表达式算术只是引擎求值的分层标记 | 正文以 {{7*7}} 和强执行表达式作 SSTI 候选。 | [方法条目](../by-type/ssti.md) |
| 角色 Cookie 与路径变体须追踪代理和应用各自的授权 | 保存正文提出 role=ADMIN、X-Forwarded-For loopback/localhost、X-Original-URL 及路径大小写、点/斜杠/分号变体。 | [方法条目](../by-type/idor-access-control.md) |
| Java RMI lookup 响应 readObject 是需审计的反序列化入口 | 图片代码显示 lookup 将名称 writeObject 给远端，取返回流时 readObject 后强转 java.rmi.Remote。 | [方法条目](../by-type/deserialization-rce.md) |
| 验证码、CSRF 令牌和限流身份应按消费者分别验证 | 正文 captcha tips 与 _RequestVerificationToken 示例混杂：POST/GET、删值、旧值、JSON 格式、改单字符及 X-Forwarded-For 等头。 | [方法条目](../by-type/authn-session.md) |
| Android 静态检查、日志和 hook 应与服务端安全边界分层 | mindmap 列 Manifest 的 exported/debug、框架/混淆、secret/preferences/logs、WebView/intent/broadcast、crypto 与 root/pinning；日志图包含连接/installer，hook 图含 su/magisk、TrustManager、BiometricPrompt。 | [方法条目](../discovery/client-and-cloud.md) |
| 参数名和值的定向变异须保持请求语义和证据上下文 | 正文建议在 Burp 检查参数、Cookie、UA、Referer、头、方法及错误反馈，再分别变参数名与值。 | [方法条目](../targeted-fuzzing.md) |
| JS 收集与代理重放须先确认 TLS 和实际保存内容 | JSubFinder 配图展示 proxify 监听与 replay 命令，但 TLS 日志连续 unknown certificate。 | [方法条目](../discovery/client-and-cloud.md) |
| 端点提取应保留深度、状态和实际资源消费关系 | xnLinkFinder 保存图以深度 2 枚举 URL、JS 和语言路径，显示 200、404、405。 | [方法条目](../discovery/web-and-api.md) |
| 公司关联和单页子域索引均不能当作完整授权资产集 | 正文建议父子公司调查，VirusTotal 示例取 UI 子域接口 limit=40 后用正则排序。 | [方法条目](../discovery/passive-and-services.md) |
| 过滤返回值未流入最终 SQL 仍留下原始字符串 sink | 组108保存图片实际为 PHP：id/stock 用 intval，color 取原 GET；real_escape_string 的返回值只赋给数组元素，而 SELECT 仍插入原 $color。 | [方法条目](../by-type/sql-injection.md) |
| 社交链接脚本协议可绕过 cookie 读取限制转向同源令牌接口 | Linktree 报告描述 SocialIcon URL 未校验而允许 javascript URI；HttpOnly 无法直接读 cookie，但脚本可带现有 cookie 请求同源 /api/token 取得 accessToken。 | [方法条目](../by-type/xss.md) |
| CSRF 到反射 XSS 须证明跨站表单响应中的可执行上下文 | MTN 截图显示 CFID 的 POST 值包含 HTML 事件标记，但 Origin 为目标同源。 | [方法条目](../by-type/csrf.md) |
| 编码、script 边界及事件属性要回到实际 HTML 上下文 | 材料包含 terminalId 反射到 script 双引号、路径 URL 编码脚本、混合大小写闭合及 input value 后的 onfocus/autofocus；另正文建议 %00 分隔事件名，图本身未显示 null 字节。 | [方法条目](../by-type/xss.md) |
| 删除业务端点的 SQL 候选不得以破坏性重放补证 | 保存图是 GET /account/user_group.php?task=delete&groupID=27，响应空且未显示 SQL payload 或时序。 | [方法条目](../experiment-design.md) |
| 命令备忘录应拆成离线处理、只读检查和状态修改 | 长图含编码/十六进制、计数排序、lsof/fuser、压缩、guestmount -ro、证书与 protobuf，以及安装、创建用户、authorized_keys、文件属性和载荷下载。 | [方法条目](../experiment-design.md) |
| grep 敏感字段模式只生成需脱敏的本地候选 | 图片提供 email/IP/密码/hash/卡号/证件/URL 正则，存在长度、大小写、锚点、转义及多协议差异。 | [方法条目](../by-type/info-secrets.md) |
| 防火墙命令清单需审计方向、规则顺序及默认策略 | iptables 图先 flush/delete-chain，再允许 loopback、established、部分 SSH/HTTP/DNS，INPUT DROP 而 FORWARD/OUTPUT ACCEPT。 | [方法条目](../cloud/container-k8s-security.md) |
| Azure 容器列举与 blob 读取是独立授权动作 | 正文简写 comp=list，图显示 EnumerationResults 的 ContainerName、Blobs Name/Url/ETag/Size/ContentType。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 资产库存增量需保存版本差分和授权核对结果 | Github hostnames diff 展示新增域，正文建议每日提交和监控。 | [方法条目](../discovery/records-and-incremental.md) |
| 会话安全图的局部节点应转成生命周期对照 | 局部 mindmap 可读会话固定、token 随机性/静态性、网络泄漏和登录/退出/到期状态，同时展示 CSRF 与 SQL 操作类别。 | [方法条目](../by-type/authn-session.md) |
| proc self cwd 只在实际进程和命名空间里解释相对路径 | Linux 目录图可作为配置/数据/临时/虚拟文件系统候选，正文提出 /proc/self/cwd 访问当前应用目录。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 对象 ID 越权与错误页秘密泄漏可能走同一更新入口 | Pressable 报告描述把 application[id] 换成第二帐号 ID 后迁移 API application，再只保留 id 与 authenticity_token 触发 Name required 错误页并返回目标 Client ID/Secret。 | [方法条目](../by-type/idor-access-control.md) |
| Host 与方法覆盖变体需保留完整字节及每层路由决定 | 正文列 Method Override、PUT、absolute-form GET、Host 不一致、重复 Host/折行及相关工具字典。 | [方法条目](../by-type/request-smuggling.md) |
| JWT none 问题先确认验证端接受算法的实际条件 | 保存正文仅询问为何有人会接受 none，没有服务或实现细节。 | [方法条目](../by-type/jwt.md) |
| 影响分类和个人报告数量不替代可验证的因果链 | 正文以机密性/完整性/可用性标签和个人 Burp Repeater 记录数量介绍经验。 | [方法条目](../impact-and-acceptance.md) |
| 第三方评论 RSS 需对来源标题按 XML 上下文编码 | IntenseDebate 报告将自有博客 title 经评论传播到平台 comments.rss，未编码标题含 XHTML 命名空间 script。 | [方法条目](../by-type/xss.md) |
| Node Inspector 任意求值必须先满足进程调试访问前提 | Jscythe 图显示发现进程、SIGUSR1、获取 loopback /json 的 WebSocketDebuggerUrl、连接并发送载荷与 Calculator 现象。 | [方法条目](../by-type/desktop-client.md) |
| expect URI 的执行能力取决于 XML 外部解析器和 wrapper | 正文把 expect://id 用作 XXE 候选。 | [方法条目](../by-type/xxe.md) |
| Jenkins 控制台执行身份与云 profile 泄漏需分别定界 | 保存图为 Jenkins node script 页面，Result 显示 jenkins uid 与多组 AWS profile 凭证字段，值部分遮挡。 | [方法条目](../by-type/info-secrets.md) |
| private 和 deleted 对象也需限制插件编辑器的替代读入口 | Crowdsignal 报告指出其他用户通过插件 editor 读取 private/deleted poll 的 questions/answers，但不是 results。 | [方法条目](../by-type/idor-access-control.md) |
| CVE 路径字典命中须确认消费者、请求副作用和真实配置 | LeakyPaths 图介绍 CVE、配置和隐藏 API 路径清单，但未保存具体字典正文或响应。 | [方法条目](../discovery/web-and-api.md) |
| Actions Runner 的环境输入需跨过 docker CLI 编码边界审计 | 保存 GitHub 报告说明 runner 为 job/service/container actions 直接调用 docker CLI，环境变量编码缺陷可让不可信输入逃逸进调用参数。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 理解业务和整理资料应产出可验证的对象与状态模型 | 正文强调理解应用、读 scope、手工识别入口、记录以及整理各类资源。 | [方法条目](../hunting-strategy.md) |
| 远端资源读取与服务器 include 必须按消费者区分 | 正文只介绍远端文件包含的动态内容场景，未保存后续细节。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 原型链属性探针需排除 own property 并关联实际 gadget | 图片流水线用 __proto__[testparam] 查询与 page-fetch 检查 window.testparam 等于标记。 | [方法条目](../discovery/web-and-api.md) |

| IP、旧页面、深层子域和 ASN 都是需核对的资产候选 | 保存材料展示 HostHunter 的 IP→域名输入、版权文本搜索旧页面、corp/internal/dev 命名、assetfinder→dnsgen→puredns→httpx 变异流程及 ASN 输出改名。 | [方法条目](../discovery/passive-and-services.md) |
| 入门目录与主站清单应转成可核验的业务矩阵 | 保存图从 HTTP、Cookie、MIME、编码、SOP 等基础概念延伸至认证/OTP、角色、上传、API、支付、缓存、竞态及移动端；一张小图细小节点受分辨率限制，葡语图强调持续学习与休息。 | [方法条目](../hunting-strategy.md) |
| Cookie 文件路径示意需要原始消费者与文件来源证据 | 保存 Cookie:usid 示例含目录遍历，但一图只有200与省略号，另一图把 passwd 样式行放进 Server 头；另一个界面显示路径框及 root:x:0:0 等账户条目，缺完整 HTTP 交互。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Markdown 预览与移动动作可能共用高复杂度解析器 | 保存 GitLab 报告描述畸形 issue 描述让 preview 与 move_issue 消耗 CPU 并达到约60秒超时。 | [方法条目](../experiment-design.md) |
| Profiling 调试端点暴露与任意文件读取应分别证明 | InfluxDB 保存图列 debug/pprof 的 goroutine、heap 等路径，报告以 file disclosure 命名但图未给返回。 | [方法条目](../by-type/info-secrets.md) |
| 仓库导入的 URL 校验应在本地协议进入 git 前完成 | GitLab BulkImports 保存链为 httpUrlToRepo→oauth2 字串替换→UrlBlocker.validate!→fetch_as_mirror，报告指出校验未限制 scheme 可让 file 协议导入本地仓库。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 已有本地身份、取证或代理权限不能当成初始提权入口 | Linux 备忘录可读系统/内核/用户、服务、配置、cron 和网络基线；PrefetchHashCracker 只输出路径候选；内存取证日志包含管理员采集、哈希、profile 及加密；RDP BOF 示例依赖已有 beacon、token 或 Kerberos 身份切换会话。 | [方法条目](../discovery/client-and-cloud.md) |
| 2FA 复用、备用码和响应变异必须落到服务器因子状态 | 保存21项清单含状态/响应变异、code 复用及 A/B 绑定、backup 生成、reset/OAuth 降级、禁用 CSRF、旧会话、未验证邮箱与 JSON 数组；OTP 配图仅为 intercept off 页面。 | [方法条目](../by-type/authn-session.md) |
| Recon 目录的资产归属与授权边界需要独立复核 | 保存目录/图连结范围、收购、ASN/IP、根域、证书透明度、DNS、端口、供应商/CDN/S3、页面和 JS。 | [方法条目](../scope-and-rules.md) |
| TRACE 头回显与真正的权限或跨站影响需要分层 | 保存 Burp 图为 TRACE 请求与200响应，疑似回显头但部分小字/脱敏不可读；正文称403相关荣誉。 | [方法条目](../discovery/web-and-api.md) |
| 盲 XSS 接收记录应关联精确请求和后台浏览器消费者 | 保存帖子讨论历史 XSS Hunter 下线与自托管 ezXSS，图为演示报告列表；另帖称主题反馈隔天回调以及 admin login 的 UA 盲 XSS，后者仅猜测后台日志。 | [方法条目](../by-type/xss.md) |
| 工具流水线的输入类型、过滤损失与动作预算须可追溯 | 保存链包含 Burp JS 集合→LinkFinder、subfinder/httpx 多端口→Katana→sqlmap/nuclei、UA/XFF/Referer 候选及 unfurl/grep 参数筛选。 | [方法条目](../discovery/web-and-api.md) |
| SQL 示意分类与一次六秒错误须关联真正查询语法 | 保存图以 userid=199 or 1=1 拼入 SELECT 展示逻辑变化；另图 ASP 登录含编码 WAITFOR DELAY，500响应约6465毫秒。 | [方法条目](../by-type/sql-injection.md) |
| 通配式路径和 Nginx 标签需要真实文件调用证明 | 保存 fileRead.jsp 示例把路径部分改为问号并由406变200；另一图 httpx 匹配 root 文本称 Nginx traversal，但缺 alias 配置和完整返回。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 主题 CSS 路径拼接只是客户端消费链的一个阶段 | Acronis 图显示 color_scheme 拼进 /mc/theme.PARAMETER.css 并发起客户端 GET/加载 CSS。 | [方法条目](../by-type/xss.md) |
| GraphQL 正则提取和遗漏 batching 都需回到实际执行预算 | 保存 nestle 输出通过 query/mutation 正则与 sed 换行抽取，依赖命名与嵌套格式；另一帖说安全指南遗漏 batching，未保存指南正文。 | [方法条目](../by-type/graphql.md) |
| 反射、特殊标签和隐藏参数要绑定实际 HTML 或脚本上下文 | 保存例子有 market description 的 iframe/javascript、Harvard 登录弹窗、onpointerenter 逗号表达式、py-script 转义文本、SVG/style/data 与 Param Miner 隐藏参数反射进 JS。 | [方法条目](../by-type/xss.md) |
| 合法会话与邮箱校验不能证明跨站请求符合用户意图 | 保存 deleteUser POST 带 csrf 参数且跨站 Origin 返回 success；PHP 改邮箱代码用 session/UserCheck/validateemail/EditUser，没有独立 CSRF、Origin 或方法校验。 | [方法条目](../by-type/csrf.md) |
| Cookie 控制字节可跨共享 jar 影响后续请求格式 | curl 保存报告描述低于32的控制字节进入 Cookie，后续对同域/相关服务的请求可能被400拒绝。 | [方法条目](../discovery/client-and-cloud.md) |
| SSRF 升级为命令注入需要另一个真实执行消费者 | 正文声称某些 SSRF 可成为命令注入，完整写在未保存外链。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Logger 过滤与导出应保留捕获集合和丢失边界 | Logger++ 图列工具来源过滤、CSV、regex、columns、highlight/tag/grep 与 liveview。 | [方法条目](../discovery/records-and-incremental.md) |
| 源码目录、历史配置和测试 fixture 需要实际秘密分类 | 保存提示为 HTTP80 的 /.git 根跳转HTTPS404而 /.git/config 返回200，以及 GitHub .env/.netrc/.npmrc/.pgpass 等文件名；Yelp 图的 mesos-secrets 位于 itest_dockerfiles 且报告 Informative。 | [方法条目](../by-type/info-secrets.md) |
| 存活过滤与退役 S3 引用不能替代可认领证明 | 保存 httpx→逗号拼接→subzy hidefails 链会忽略不响应域名并隐藏失败；S3 例称退役且无用户数据，缺 DNS/认领交互。 | [方法条目](../by-type/subdomain-takeover.md) |
| 信任头、Session 名和 lead 对象都需要服务器主体对照 | 保存 X-Custom-IP-Authorization:127.0.0.1 将删除请求401变302，另一帖替换 User Session 声称读取管理员数据；TikTok 平台摘要称 Get Leads 的 sec_user_id 可能揭示邮件/手机号，历史时间线曾Informative后重开。 | [方法条目](../by-type/idor-access-control.md) |
| Go 模板定义文本需区分模板编译与 HTML 输出编码 | 正文给 define/template 插入 script 的 Go 例子，未给真实目标或响应。 | [方法条目](../by-type/ssti.md) |
| file=== 与双扩展名差异先定位参数解析层 | 正文称 file=shell.php、php.jpg、php5 被403而 file===shell.php 变200，未给上传响应和存储位置。 | [方法条目](../by-type/file-upload.md) |
| Unicode 字节候选不能直接当成 CRLF 换行 | 正文称 UTF-8 %E5%98%8A%E5%98%8D 可用于 Java CRLF；缺实际输入、响应和字符转换链。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 路径清单、Cookie flags 和复杂函数应追踪到实际安全消费者 | 正文列 post-RCE 的 log/cron/group 等路径且 /etc/passed 为拼写疑点，另帖只保存 Missing Cookie Flags 与复杂函数两个审计点。 | [方法条目](../source-audit.md) |
| 设备策略锁定要覆盖断网、快捷动作和 profile 生命周期 | WARP 历史报告分别描述同时关蜂窝/Wi-Fi、Quick Action Disable WARP 和删除 VPN profile 绕过 Lock Zero Trust；归档各有修复版本说明。 | [方法条目](../discovery/client-and-cloud.md) |
| 架构五问应定位意图授权、缓存边界和信息流 | 保存正文以 CSRF、缓存、信息流、认证和文档五个问题审视应用。 | [方法条目](../business-modeling.md) |
| Headless、JS、robots 和 sitemap 扩展的是候选集合 | 保存 Katana 循环按域分组显示深度、headless、JS、robots/sitemap 参数及实验 URL，公告列爬取模式与输出过滤。 | [方法条目](../discovery/web-and-api.md) |
| Flink jar plan 的类加载前提和租户权限需要分开审计 | 保存报告称 GET jars/{jarid}/plan 可使用 classpath 类及参数，并在特定租户/SQL job 场景存在执行链。 | [方法条目](../source-audit.md) |
| Kafka connector 的 JAAS 配置可把配置写权引向类加载 | 保存图描述 MySqlConnector 的 producer sasl.jaas.config 被设为 JndiLoginModule 后进入 LDAP/反序列化路径；末端被截断。 | [方法条目](../by-type/deserialization-rce.md) |
| SMTP 密码换行只有进入配置语法后才可能改变 renderer 参数 | Grafana 保存图描述租户 API 的 SMTP password 含换行，被写入配置后影响 rendering_args 再作用于 renderer。 | [方法条目](../by-type/crlf-response-splitting.md) |
| SQLite 写文件、HttpSink 和 Jolokia 加载属于不同权限阶段 | 保存链组合 Kafka Jdbc 的 SQLite 写入、HttpSink 访问 localhost 与未保护的 Jolokia DiagnosticCommand/jvmtiAgentLoad，再宣称 JVM agent 执行。 | [方法条目](../by-type/ssrf.md) |
| 畸形 JSON 加隐藏字段不能以200推定帐号接管 | 保存两个版本的示例在请求中加 email/password/token 并称200可ATO，但文本语法不像合法 JSON，缺真实后端身份结果。 | [方法条目](../by-type/authn-session.md) |
| 短载荷、错误回调和 WAF 品牌标签都依赖解析上下文 | 保存表和说明包含 TinyXSS 的 inline/eval/external/frame/browser 条件、SVG 大小写/假属性/Unicode标识/注释与 tagged template、throw/onerror/Errorname/eval 以及脚本上下文建议。 | [方法条目](../by-type/xss.md) |
| 周度资产增量和 Amass 文本映射需保存来源与格式约束 | 正文介绍定期盘点域名及新域重词表，图仅为 accepted 的 SwaggerUI 题名；另帖说 Amass→awk 整理 IP，未保存视频。 | [方法条目](../discovery/records-and-incremental.md) |
| 路由器本地脚本字段不证明无需网络或认证的 XSS | 保存页面地址为本地10.0.0.1，无线配置脚本的 wlanPara 数组含密码类字段与弹窗，正文称无需网络。 | [方法条目](../discovery/client-and-cloud.md) |
| Host 注入影响必须有受害者可达链和真正主机消费者 | 保存报告泛述 vhost/XFH，PoC为部分 GET/Host，平台标 Informative 并要求访问受害设备。 | [方法条目](../discovery/web-and-api.md) |
| Self-XSS 的标签输入仍需证明另一主体自然触达 | 保存 suggest tag 图含脚本输入，服务方摘要说仅影响自己。 | [方法条目](../by-type/xss.md) |
| FFUF 多主机与多字典需明确组合模式、错误和筛选基线 | 保存 for循环对 hosts 跑词表，以及 HOST/FUZZ 多字典示意，过滤200/302/401、线程40，过程7/7且无匹配；多字典 -w 的关键词顺序需隔离核对。 | [方法条目](../targeted-fuzzing.md) |
| 回环地址变体必须比较校验主机和最终连接地址 | 保存清单含127多种形式、userinfo @、fragment #、IPv6 ::1以及未括号IPv6；标题称CIDR但没有前缀。 | [方法条目](../by-type/ssrf.md) |
| 本地 fuzzer 吞吐比较须有版本、真值集和功能等价条件 | 保存表以 localhost、同词表、10线程、7秒超时、若干状态过滤比较 Dirsearch/FFUF/Feroxbuster/Gobuster 的req/s与Great/Good标签，缺版本、资源与命中真值。 | [方法条目](../experiment-design.md) |
| 报告模板、严重度与 passwd 题名不能代替实际响应 | Reddit 保存图给 /etc%2fpasswd URL并声称密码哈希，但步骤/附件仍是模板占位，状态Not-applicable。 | [方法条目](../reporting.md) |
| 上传声明 MIME 与存储后的解释器是不同校验边界 | 保存 multipart 图的文件名为PHP、Content-Type:image/png，字节实际含HTML/PHP命令执行，另帖仅题名 file upload content-type bypass。 | [方法条目](../by-type/file-upload.md) |
| Tag Manager 容器是前端线索源而公开 ID 不是凭证 | 保存图从 HTML 的 GTM ID 定位 gtm.js，规则字符串包含子域和产品路径。 | [方法条目](../by-type/info-secrets.md) |
| 爬取到 Dalfox 的触发标签仍需浏览器执行对照 | 保存命令用 Katana/qurl→Dalfox，图为教学站cat参数，包含反射、SQL错误、found DOM Object/Triggered 与PoC URL。 | [方法条目](../by-type/xss.md) |
| WPScan 的枚举、主动探测和口令动作应各自限定预算 | 保存命令包含 aggressive、token、密码词表和50线程，未展示目标结果。 | [方法条目](../targeted-fuzzing.md) |

| URL 去杂与文本提取应量化丢弃的安全入口 | 保存 grep 反向正则、数字/blog/docs 排除、Xidel XPath、nuclei Cloudflare 最后一列及 CSP 正则提域，另链 append wayback/hakrawler/gau/Katana 后 sed/扩展名筛选。 | [方法条目](../discovery/web-and-api.md) |
| 通配 TLD 搜索和披露 dork 只找到待读政策候选 | 正文 *.target.* 搜索与长图 security.txt/.well-known/disclosure/bounty/地区/平台 dork 可以发现相似名字及政策页。 | [方法条目](../scope-and-rules.md) |
| 过期或可购买 Origin 不自动完成 CORS 读取链 | 正文仅保存步骤4–6，称一个域可买但昂贵，图为 Dell 奖励通知。 | [方法条目](../by-type/cors.md) |
| OAuth 同意、scope、token 受众与资源权限是不同决定 | 保存 AAD/Graph 图分开 owner→client 同意、授权服务器发 token、client 向资源服务器携带 token 与 API 暴露 scope。 | [方法条目](../by-type/oauth-oidc.md) |
| 原型污染标记到 eval 必须包含真实继承关系和 gadget | DOM Invader 图显示 GTM eval 文本包含 canary/prototypepollutionsequence；Plution 图在本地解析器实验页给 Vulnerable 标签。 | [方法条目](../discovery/web-and-api.md) |
| Shodan 告警导入要保留源时间与字段变更 | ShoMon 图为 TheHive 的 ShodanAlert，含 IP、端口、ASN/org、hostnames、来源timestamp 与 Recursion enabled。 | [方法条目](../discovery/records-and-incremental.md) |
| Struts 表达式头候选先确认类名与真实 OGNL 消费者 | 正文给 Content-Type 中表达式访问响应对象并添加算术结果头，类路径拼写可疑且无实际响应。 | [方法条目](../source-audit.md) |
| 路径变体要比较前置路由与后端规范化的同一对象 | 保存图列编码点/斜线、分号/矩阵参数、反斜线、空/控制/无效字节及查询/片段候选，并称 Nginx 前置 Tomcat。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 花括号内的 SVG 文本不能混同模板求值和 XSS | 正文把转义 SVG 放入 {{ }} 并称 SSTI via XSS，没有引擎、渲染结果或执行记录。 | [方法条目](../by-type/ssti.md) |
| FFUF 清理进度与 ANSI 文本不可丢掉错误和原始输出 | 保存命令合并 stdout/stderr、追加文件并 sed 去进度/ANSI。 | [方法条目](../discovery/records-and-incremental.md) |
| SQL 编码、运算与时间候选需保留查询语法和基线 | 保存 MySQL SLEEP/IF/XOR/subquery/注释/编码列表、OR/null/算术/｜｜ 变体及“单引号未报错”提示。 | [方法条目](../by-type/sql-injection.md) |
| SBOM 与库版本匹配必须落到部署和可达代码 | Bomber 图对721个npm包报14个候选，列包/版本/CVE/严重度/license并提示不同提供商结果不同；另一帖仅问 jQuery2.2.4 的PoC。 | [方法条目](../source-audit.md) |
| 参数名、Base64 与无括号脚本都要追踪浏览器解释层 | 保存查询参数名字表、constructor tagged template、HTML注释/script组合、message Base64、隐藏参数及 redirectUrl/returnPath 的 javascript 候选。 | [方法条目](../by-type/xss.md) |
| JSON-RPC 解码应绑定 ABI、合约与块上下文 | Web3 Decoder 图把 eth_call 的 data/to/latest 及result解释为 balances(address[],address[])→uint256[]。 | [方法条目](../discovery/web-and-api.md) |
| zip wrapper 升级要证明上传路径进入语言 include | 保存示意上传ZIP含PHP，然后 page 使用 zip 协议指向归档成员。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 上传与 PUT 的安全边界包含真实类型、存储和解释器 | 保存 Academy multipart 声明image/png但含PHP、WebDAV201/BasicAuth示意、Tomcat /files/ PUT 声称及完整上传图的扩展/MIME/元数据/预览/ZIP/OOXML/配置路径。 | [方法条目](../by-type/file-upload.md) |
| 替换关键词后拼 script 的缺陷是代码上下文信任 | 代码示例把search值替换 prompt/confirm/print及部分符号后拼 <script> 再送 jQuery .html。 | [方法条目](../by-type/xss.md) |
| Self-XSS 借静态后缀缓存影响他人需证明同一缓存键 | 保存示意 /my_profile 不缓存而 /my_profile/xss.css 返回同页面可能缓存；另帖仅有 cache poisoning→stored XSS 外链。 | [方法条目](../by-type/xss.md) |
| 浏览器代理与思维图应产出对象状态证据而非工具数量 | 保存正文强调浏览器/代理与手工理解，图仅能读到低分辨率 pentest 主枝，另帖只存 read source 第一条与新版续篇标题。 | [方法条目](../hunting-strategy.md) |
| 密钥验证应先识别权限并避免消费他人真实秘密 | 保存 Clearbit 示例请求涉及联系人查询，Algolia /keys 图列 search/add/delete/settings/browse等ACL，ZeroBounce 历史URL包含email/api_key。 | [方法条目](../by-type/info-secrets.md) |
| 组织名和端口搜索不能把共享基础设施变为授权资产 | 保存 dig→ipinfo→grep org 与 Shodan MySQL/SSH/nginx/Jenkins 查询，另帖赞快速技术/子域检测。 | [方法条目](../discovery/passive-and-services.md) |
| Cookie、2FA 和限速必须分别验证服务端生命周期 | 保存 Cookie 图列fixation、puzzling、weak、flags、反序列化/注入等候选；2FA图列旧/跨主体/跨动作OTP、refresh/SMS/verify预算、旧会话、重置/禁用/API版本；REST/SOAP示例语法不完整。 | [方法条目](../by-type/authn-session.md) |
| 邮箱分隔符与数组要比较帐号选择和消息投递的解析结果 | 正文列逗号、空格、管道及数组email，未给响应/邮件。 | [方法条目](../by-type/authn-session.md) |
| 备份与 WordPress 路径清单需按具体消费者验证 | 保存 .env/.git、webdav、backups、volume/VM、robots/sitemap/策略/.well-known 与 WordPress login/config/uploads/wp-json/xmlrpc/cron等候选，包含重复及可能非标准名字。 | [方法条目](../discovery/web-and-api.md) |
| S3 DNS 与模板式认领截图的证据强度不同 | Equifax 保存报告给 dig CNAME 到 S3 website 并声称可服务自有内容；Yelp图为Not-applicable、泛化模板与“hacked”页面，缺DNS/资源归属。 | [方法条目](../by-type/subdomain-takeover.md) |
| 枚举示范脚本的私人依赖和范围损失需先暴露 | 保存脚本自述私有工具/路径未公开、可能失败，从被动域名与范围过滤到DNS爆破/证书/CNAME、合并、接管、解析、去私IP、HTTP与非web端口扫描。 | [方法条目](../discovery/web-and-api.md) |
| 隐藏参数与正则生成词表需验证消费者并控制组合上界 | x8图只展示词表长度、GET/POST进度、size与reflects email，SuperTruder正文称可用正则生成词表。 | [方法条目](../targeted-fuzzing.md) |
| 跨站连接复用的安全决定要绑定池键与每条消息 | HTTP story 图为连接复用教学时间线，关联HTTP1.1走私与HTTP2/3污染，HTTP3在图上为历史TBD。 | [方法条目](../by-type/request-smuggling.md) |
| 反向 SSH 与 Inspector 示例均有已有执行或连接权限前提 | Reverse SSH 图是human/client/server连接拓扑，Jscythe 图显示发SIGUSR1、loopback /json、WebSocket调试及Calculator。 | [方法条目](../by-type/desktop-client.md) |
| CI/CD 实验环境架构应定义每阶段的可信输入 | CI/CD Goat 图列 Gitea→Jenkins→agent/LocalStack/LIGHTTPD及CTFd。 | [方法条目](../experiment-design.md) |
| 同邮箱多角色邀请不能绕开成员列出和撤销 | Reddit保存报告描述同一email可在同组织被多次邀请为不同角色，形成隐藏admin，owner在members看不到也无法移除。 | [方法条目](../by-type/idor-access-control.md) |
| URL 主机中的正则点应按字面或结构化解析 | PHP代码在GETlogout中用 /^https:\/\/auth.domain.com\/.*$/ 校验redirect_to后Location301，主机点没有转义。 | [方法条目](../by-type/open-redirect.md) |
| 射频帧结构候选与无线测试框架需有隔离观测条件 | FISSURE图列preamble次数、packet统计、位切片、字段偏移/entropy及X10设备gallery；Wi-FiFramework图连hostap extension、wpaspy、testcases与Ethernet/Monitor接口。 | [方法条目](../discovery/client-and-cloud.md) |
| Katana 接 nuclei 需保持批次、模板和真实响应关联 | 保存管道httpx→alive文件→Katana→endpoint文件→nuclei，包含排版的双长横及append旧文件；图只显示dot-env模板标签。 | [方法条目](../discovery/web-and-api.md) |
| OAuth state 被当跳转地址须验证业务消费者和登录前提 | Acronis保存报告的authorize请求保持本地redirect_uri而state为外站，注释要求先登录，缺完整最终交互。 | [方法条目](../by-type/open-redirect.md) |
| 报告分流和改评级应以完整证据与项目规则解释 | 正文把Not Applicable等同出scope、Informative等同无影响、Duplicate等同已处理，图另有none→P2变化。 | [方法条目](../reporting.md) |
| DNS resolver 更新应先生成并验证再替换旧基线 | 保存脚本先删旧名单并隐藏错误，再从公共源以40线程验证写回同路径。 | [方法条目](../discovery/passive-and-services.md) |
| TLS 指纹变化与应用授权要用同一请求对照 | 正文称Burp扩展替换HTTP/TLS栈以改浏览器指纹，缺具体实现/运行结果。 | [方法条目](../by-type/waf-bypass.md) |
| DNS 重绑定必须满足解析变化和本地服务的实际前提 | 图示域先A公网TTL120后A127.0.0.1，浏览器稍后同域XHR并外传。 | [方法条目](../discovery/client-and-cloud.md) |
| SOQL 注入的对象查询上下文不能套全套 SQL 字典 | 保存Apex表单输入拼SELECT User WHERE Email后Database.query，示意变量名及邮箱解释有不一致。 | [方法条目](../by-type/sql-injection.md) |
| XML 编码变异需让预过滤和解析器看到同一语义 | 保存iconv脚本展示UTF7/16/16BE外部parameter entity，但声明与正文分开echo可能形成无效流。 | [方法条目](../by-type/xxe.md) |
| Host 中的 HTML 片段只有经过后台渲染才可能盲执行 | 正文将img片段置于forgot_password Host，缺响应/渲染位置。 | [方法条目](../by-type/xss.md) |
| NTLM challenge 元数据不等通过认证或获得密码 | 正文称IIS403后/testauth返回WWW-Authenticate，图为SSPDecoder的target/computer/domain/DNS/tree/timestamp字段全遮挡。 | [方法条目](../by-type/info-secrets.md) |
| 删除卷影快照是破坏恢复能力而非 EDR 验证 | 正文把vssadmin删除全部shadows当“有EDR时尝试”，没有效果记录。 | [方法条目](../discovery/client-and-cloud.md) |
| 外部 hash 转方法对象会改变调用方对类型的假设 | GitLab导入图说明Octokit/Sawyer::Resource把hash键变对象方法，to_s/length例子可被数据值替换，下游id调用被截断。 | [方法条目](../source-audit.md) |
| 模板中已编码 fullname 不保护同一行其他字段 | deployKeyRowHtml图片把key.title、avatar_url、isActiveClass插进HTML标签/属性，fullname另有escape调用。 | [方法条目](../by-type/xss.md) |
| 净化后保留的 data 属性可能被另一个库二次解释 | 保存v-safe-html报告称DOMPurify删data-remote/url/type/method却保留data-disable-with，Rails-ujs后续当HTML展示，CI job名经错误消息传递且style/class可遮罩引导点击。 | [方法条目](../by-type/xss.md) |
| 联系人名字经 quick command 建议框需要再次编码 | 保存GitLab报告按group启用CustomerRelations→contact firstname/lastname→project issue /add_contacts或/remove_contacts建议框触发。 | [方法条目](../by-type/xss.md) |
| 重置页用户信息枚举与 token 控制是不同影响 | 保存reset链接userid与token，两个页面userid不同显示username/email和一次性说明，正文称15连续请求后阻断并以Nullbyte/IP rotate绕过。 | [方法条目](../by-type/idor-access-control.md) |
| 锁定 WARP 的信任 SSID 配置也需同一策略执行 | 保存摘要称add-trusted-ssid让锁定client断开、ZeroTrust策略未强制。 | [方法条目](../discovery/client-and-cloud.md) |
| eBPF 主机组件架构只能在已有权限前提下解释 | TripleCross图列tracepoints/XDP/TC、userprocess、共享maps、网络和C2组件。 | [方法条目](../discovery/client-and-cloud.md) |
| Prefetch 路径候选与内存采集完成必须有不同证据 | Prefetch图输入exe/hash/bodyfile/mount并返回候选路径；CollectMemoryDump图列多采集后端、pagefile、32GB哈希/9.86GB归档与完成耗时，另图仅87%进度。 | [方法条目](../discovery/client-and-cloud.md) |
| Creator 的读权限和角色写权限应分别覆盖所有接口 | 正文保存owner/creator两角色：creator本不允许PII却读取所有邮件，再按creator UUID把自身角色改account manager，缺中间请求。 | [方法条目](../by-type/idor-access-control.md) |
| SSRF 到 SVNBridge 反序列化需要控制实际缓存字节 | GitHubEnterprise保存摘要将SSRF、可控被反序列化数据、memcached/SVNBridge与潜在RCE连接，列历史修复版本但无具体入口/gadget。 | [方法条目](../by-type/deserialization-rce.md) |
| 移除 CSRF 头或 GET 创建都需要真实跨站状态证明 | 正文称删anti-csrf header仍有响应；AppSearch图描述GET find_or_create创建curations和登录后另一tab/HTMLPoC。 | [方法条目](../by-type/csrf.md) |
| 错误响应污染缓存须验证键合并、共享命中与恢复 | 正文示例正常q=10返回200不cache、变化q导致503cache、正常q再503，图仅维护错误页。 | [方法条目](../discovery/web-and-api.md) |
| 反射筛选和跳过 mining 会限制规模化 XSS 的覆盖 | 保存subfinder→httpx→Katana→Gxss100→Dalfox且跳过bav/mining/grepping，转述帖仅重复标题。 | [方法条目](../by-type/xss.md) |
| 登录页公开或默认凭证的有效性须用自有主体验证 | 正文有default组合/复制登录页凭证声称，图为GlobalProtect triaged状态与Elastic报告登录rundeck后500、version/path/class。 | [方法条目](../by-type/authn-session.md) |
| 目录公开源与脚本邮件名单需按真实敏感性定界 | 8x8摘要称cobbler/cblr公开Spacewalk源码且无敏感信息，另图script块含部分遮挡的邮件名单，正文称loadbalancer/shallowcopy/cache链。 | [方法条目](../by-type/info-secrets.md) |
| 下载执行界面和模块 help 不证明越过主机权限 | PowerHub UI展示远端DownloadString/IEX和反射选项，终端只加载SharpHound并显示help。 | [方法条目](../by-type/desktop-client.md) |
| 代理钓鱼架构与事件标签应分开于真实会话控制 | Evilgophish图包含代理、legitimate site、cookie/token/credential路径及事件库，另一图为空campaign，livefeed标sent/opened/clicked/submitted/captured并遮挡秘密。 | [方法条目](../by-type/authn-session.md) |
| 签名者名称必须与证书链和文件完整性一起判断 | Mangle图显示exe的Digital Signatures带厂商名字，但详情明确cannot verify或signature not valid。 | [方法条目](../by-type/desktop-client.md) |
| 内外网取资源示意必须定位真正后端消费者 | autoSSRF图示content URL从网站请求内部admin并回传。 | [方法条目](../by-type/ssrf.md) |

| Host 改写到 localhost：敏感响应与后台路由分开核验 | 保存正文明确把 Host 从目标域名换成 localhost 并声称看到敏感信息；1593673512576847875-02.jpg 只保存严重度/接受标签。 | [方法条目](../by-type/info-secrets.md) |
| DoD 的 project 与 plot：事件触发和浏览器执行边界 | 1593674835904847876-02.jpg 和 1593674945254621187-02.jpg 分别保存 project、plot 参数插入 h1/onauxclick 的报告，要求右键等事件。 | [方法条目](../by-type/xss.md) |
| JNDI 表达式与回连：日志消费、网络交互、执行三级证据 | 1593675056475000833-02.jpg 保存 URL 参数中的 JNDI LDAP 表达式和 hostName 回连主张。 | [方法条目](../by-type/deserialization-rce.md) |
| redir.html 的 u 参数：跳转目的地与账号影响分层 | 1593690282809237505-02.jpg 保存 redir.html 查询中 u 指向其他来源的报告文字。 | [方法条目](../by-type/open-redirect.md) |
| 公司删除 GET 的对象授权：标识替换之后必须读回 | 1593690392955863043-02.jpg 保存 Vendor/Companies/Delete/{id} 的 GET 请求和替换末尾 ID 步骤。 | [方法条目](../by-type/idor-access-control.md) |
| Excel 启动 XLL：进程命令行只证明消费入口 | 1593778585537458176-03.png 的进程属性显示 Excel.exe 接收临时解压目录中的 HelloWorldXll.xll。 | [方法条目](../by-type/desktop-client.md) |
| errorUrl 与 MobileToken：奖励邮件仅保留链条假设 | 1593849100469866496-02.jpg 的奖励邮件称 errorUrl 开放重定向泄漏 MobileToken。 | [方法条目](../by-type/open-redirect.md) |
| Facebook 账号绑定的 userid 与 oauth token 必须属于同一主体 | 保存请求形状为 oauth={token}&userid=本账号&email=本邮箱，帖文建议替换 userid。 | [方法条目](../by-type/oauth-oidc.md) |
| 重置代码与 email：改目标字段后的真实身份核验 | 1593947246378291204-02.jpg 的示意图保持 code 不变而替换 email，声称重置另一个用户。 | [方法条目](../by-type/authn-session.md) |
| 编码 NUL 的模板表达式：先确定解码与求值上下文 | 1593951117490225157-02.png 可见编码 NUL 包裹 constructor 表达式及 alert 1；正文把正常双括号失败与插入 %00 后成功相比。 | [方法条目](../by-type/xss.md) |
| Oracle TNS 可达、认证结果与角色权限必须分开 | 1593955785754562560-02.png 展示 WODAT 发现监听端口、多个 ORA-01017 拒绝及一项认证成功。 | [方法条目](../discovery/passive-and-services.md) |
| Solidity transferFrom 返回值与 NFT 交付状态的原子性 | 1593980414791647234-02.jpg 中 initiatePayment 验证赢家后调用 sendPayments，USDT.transferFrom 返回值未被处理便发出 paymentMade，NFT 交付代码省略。 | [方法条目](../by-type/business-logic.md) |
| autoSSRF 打印 OOB 标识：生成载荷与收到请求不是同一证据 | 1593996108207984642-02.jpg 仅显示 URL 查询输入及生成的一条 OOB 标识。 | [方法条目](../by-type/ssrf.md) |
| 聊天机器人号码输入：HTML 消费、点击条件与跨用户送达 | 1594007870005190656-02.jpg 保存把 onclick 按钮输入聊天号码字段的报告。 | [方法条目](../by-type/xss.md) |
| MLWAF 蜜罐分流图：架构设计与可测效果分开 | 1594020177967910918-02.jpg 显示用户/攻击者经 MLWAF 分流到网站或交互蜜罐，并汇入 ELK。 | [方法条目](../by-type/waf-bypass.md) |
| 移除账号通知：副作用幂等与节流单独验证 | 1594264894353858561-02.jpg 的 Weblate 报告称移除账号请求可重复触发大量邮件，并建议高次数重放。 | [方法条目](../by-type/business-logic.md) |
| 多来源域名到 IP 再到模板：保存每个阶段的对象与失败 | 正文给出多来源域名→DNS IP→端口/HTTP→私有字典，另一帖给出 Shodan 文本第 3 列→httpx→nuclei 的管线。 | [方法条目](../discovery/web-and-api.md) |
| ffuf 双关键字：URL 与路径的组合模式和预算 | 保存例子用 URL 与 FUZZ 两个字典关键字组合目标和路径。 | [方法条目](../targeted-fuzzing.md) |
| FDNS_A 历史记录解析：字段、错误与归属核验 | 帖文把 FDNS_A 数组按逗号切第二列去重来取子域名。 | [方法条目](../discovery/passive-and-services.md) |
| 短 XSS 列表必须先匹配最终 HTML、JS 与 URL 上下文 | 保存正文列出 HTML 标签、属性聚焦事件、script 结束、JS 字符串及 javascript URL 等不同输入形状。 | [方法条目](../by-type/xss.md) |
| GitLab listrepo 的 private 可见性：凭据许可与越权分开 | 1594382564361314304-02.jpg 的 SCMKit 截图用账号密码列出仓库名称、可见性和 URL，包括 private/internal。 | [方法条目](../by-type/idor-access-control.md) |
| 安全策略搜索词：候选页面与授权依据之间的核验 | 1594567906947256321-02.jpg 给出 security.txt、responsible disclosure、reward、平台及机构等搜索词。 | [方法条目](../scope-and-rules.md) |
| Newsletter 的 HTML 转义再入 innerHTML：跨解析阶段审计 | 1594646225415970817-03.jpg 中 PHP htmlspecialchars 的结果嵌入 JS 字符串，随后拼接 Welcome HTML 并赋值 innerHTML，@ 个数检查仅校验形状。 | [方法条目](../by-type/xss.md) |
| POST 参数与 URI 路径的延时主张：三段对照而非评级 | 正文分别保存嵌套 SLEEP 的 POST 参数与 URI 路径 XOR/条件延时表达式；1594685055242469376-02.png 只显示 SQLi 被 triaged 的时间线。 | [方法条目](../by-type/sql-injection.md) |
| Git 配置和日志路径：暴露片段与完整仓库重建分开 | 保存正文点名 .git/config、logs/HEAD、logs/refs 等路径，1594777753911496717-02.jpg 只有名人堂和表情图。 | [方法条目](../by-type/info-secrets.md) |
| 扩展名影响表：文件类型只确定候选消费者 | 帖文把 ASP/PHP、SVG、CSV、XML、PDF、图片、压缩包等扩展名直接对应 RCE/XSS/SSRF/XXE/DoS。 | [方法条目](../by-type/file-upload.md) |
| 大型 PHP 错误日志：大小和行数不是漏洞数量 | 1594813795196608513-02.png 可见约 2.98 GB 日志、约三千万行及被遮挡的 PHP 错误。 | [方法条目](../by-type/info-secrets.md) |
| JWT 检查表：算法策略、密钥类型与服务端主体分层 | 正文列 none、泄漏/弱秘密、未校验、过期、客户端生成、RS→HS 与 JWKS 冒用；1595046632894111745-02.jpg 还列算法固定、密钥和生命周期。 | [方法条目](../by-type/jwt.md) |
| API 清单的 redirect、state 与 scope：字段存在不代表绑定 | 1595046632894111745-02.jpg 列 redirect_uri 服务端校验、code 响应、state 与 scope。 | [方法条目](../by-type/oauth-oidc.md) |
| API 认证方式清单：JWT 名称与 IP 白名单不代替权限 | 1595046632894111745-02.jpg 建议禁用 Basic 并用 JWT、限制登录重试和私有 API 的 IP/host。 | [方法条目](../by-type/authn-session.md) |
| CSP 域名与 anew：关系线索、新增记录和完整运行 | 1595005075717591041-02.jpg 给出 CSP 提取工具入口；1595395884384223232-02.jpg 展示 subfinder→httpx→csprecon→anew 的新增域名管线。 | [方法条目](../discovery/records-and-incremental.md) |
| PHP 黑盒过滤特征：相似输出不等于同一安全策略 | 1595052119908057090-02.jpg 对比 htmlentities、filter_var 和多种历史 sanitizer 的输出，并把可保留反斜杠、单引号或再次 URL 解码等情况列为风险。 | [方法条目](../by-type/xss.md) |
| 固定数值改币种：价格、金额单位与履约一致性 | 帖文建议不改 price 而改 currency，并保留相同数值。 | [方法条目](../business-modeling.md) |
| user/1 成功而 user/2 为 404：负例与越权证据分开 | 正文明确一个用户路径返回 PII，另一个及其版本/控制字符变体均为 404。 | [方法条目](../by-type/idor-access-control.md) |
| Fastly 题名和自定义页面：可控内容与可认领条件分开 | 1595159709136330753-02.png 保存 redacted 域名下的 PoC 页面及 resolved 奖励标签，正文只给 Fastly 子域接管题名。 | [方法条目](../by-type/subdomain-takeover.md) |
| JPEG 元数据 XSS 题名：实际响应类型和预览消费者 | 1595297466295156737-02.jpg 保存 JPEG 后缀 URL 上的浏览器 alert 与聊天预览；两个帖子都仅链接元数据 XSS 文章。 | [方法条目](../by-type/file-upload.md) |
| 公开 JS 的 Zendesk token：暴露、权限和修复范围分层 | 1595339486443016192-02.jpg 的双方摘要称公开 JS 含 Zendesk API token 与关联邮箱，导致多个支持门户管理权限，后续移除/弃用 token 并调整权限。 | [方法条目](../by-type/info-secrets.md) |
| 本地检查器改 img：自改 DOM 不构成开放重定向 | 1595339597512318982-02.jpg 的 AMBER informative 报告要求在浏览器检查器修改 img 的 onerror 后导航。 | [方法条目](../experiment-design.md) |
| NLP trainFiles 路径：后台任务读取与日志暴露链 | 1595424432000049152-03.png 的 JSON trainFiles 指定上级路径到 etc/passwd；1595424432000049152-04.png 的 finetune 日志出现对应系统账号样式及解析长度警告。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Mattermost 大字段：写入成本、延迟消费者和恢复路径 | 1595447529717604352-02.jpg 称 playbook 大模板保存后要运行才触发资源问题；1595447641101541377-02.jpg 称自动回复大字段的用户 patch 产生更新成本。 | [方法条目](../by-type/business-logic.md) |
| JSON 类型选择到 Spring XML：类实例化与生命周期消费者 | 1595484816623173632-02.jpg 展示 JSON 指定 FileSystemXmlApplicationContext，再引用含 ProcessBuilder 生命周期的 XML。 | [方法条目](../by-type/deserialization-rce.md) |
| Wappalyzer 批处理：本地 CLI、结构化结果与指纹证据 | 正文误把 python3 的脚本位置写成 URL；1595506987852521472-02.jpg 则显示本地 main.py 和技术名称结果。 | [方法条目](../discovery/web-and-api.md) |
| 目录与文件词表生成：数量、分组与目标预算 | 1595510733743468544-02.png 展示 filename/directory、common/extra、PHP/dotted 等词表生成计数。 | [方法条目](../targeted-fuzzing.md) |
| Adyen 的非 401：返回码不能替代密钥有效性与权限 | 正文称非 401 即秘密有效并可操作私有环境；1595538689794650112-02.png 实际仅显示 redacted x-api-key 和 400 Resource not found。 | [方法条目](../by-type/info-secrets.md) |
| Nuvola 的 PassRole 图：静态边与有效云权限之间 | 1595666023021158400-03.jpg 把 PassRole、CreateAutoScalingGroup、CreateLaunchConfiguration 与多个角色画成图；1595666023021158400-02.jpg 只是 logo。 | [方法条目](../cloud/cloud-misconfiguration.md) |

| Octopii 的输入支持：扫描结果与 PII 暴露证据分开 | 1595767763447910401-02.png 的帮助界面显示本地路径或 URL，且 URL 只支持 S3/开放目录；没有检测结果或准确率。 | [方法条目](../by-type/info-secrets.md) |
| 重置邮件 Host 投毒：链接来源与代码消费者绑定 | 正文给出替换 Host 后检查重置邮件链接的思路。 | [方法条目](../by-type/authn-session.md) |
| S3 命令表混合读写：先确定身份与具体权限 | 1595837676728782848-02.jpg 同列 ACL、列举、移动/上传和删除命令。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| CGI 与 Bash 函数环境：入口、解释器和权限分别确认 | 保存正文给出 Shellshock 风格的 User-Agent 函数定义及读取文件/反向连接命令。 | [方法条目](../by-type/cmd-injection-rce.md) |
| X-Cache 与 unkeyed input：共享存储和独立读取两段证明 | 1595839217275666432-02.jpg 建议从 X-Cache Hit/Miss 和 Paraminer 寻找不入缓存键的 header/cookie/参数。 | [方法条目](../discovery/web-and-api.md) |
| 内容类型与 SameSite：浏览器可发送请求和状态变化为准 | 1595842027832610816-02.jpg 称 JSON/text/plain 失败而 form-urlencoded 成功；1597980588362895361-02.jpg 则仅检查 SameSite 属性，报告为 not-applicable，并提到 None 缺 Secure 时被拒绝。 | [方法条目](../by-type/csrf.md) |
| script 文本终止与字符串转义：两套解析器分开观察 | 1595842546395410432-02.jpg 把引号、script 结束标签和反斜杠作为测试方向，但例子部分缺变量名；另帖称必须先结束原 script 才执行。 | [方法条目](../by-type/xss.md) |
| Recon 总表：公开线索、主动交互与许可范围分层 | 1595843621580079104-02.jpg 汇总 IP/域名/邮箱/平台/服务/组织联系人等来源，并列 DNS、搜索、网站、ping、traceroute、SMTP 等方法。 | [方法条目](../discovery/passive-and-services.md) |
| 用户编号与邮件列表：存在性、对象归属和限量对照 | 一帖保存 user/1 返回 PII 而 user/2 与变体为 404；另一帖声称递增 ID 可枚举全部邮件，但缺端点和结果。 | [方法条目](../by-type/idor-access-control.md) |
| httpx→Katana→模板：追加文件中的运行边界 | 1595855922265751552-02.jpg 把 alive.txt、endpoints.txt 用追加方式串入模板。 | [方法条目](../discovery/records-and-incremental.md) |
| SQL 思维图：观察通道、查询上下文与权限能力分开 | 1595980200894164992-02.jpg 列 union/error、HTTP/DNS、time/boolean、filesystem/OS/UDF、clauses/stack/second-order。 | [方法条目](../by-type/sql-injection.md) |
| RedirectUrl 完整替换失败：保留负例并定位规范化规则 | 正文明确重置请求中的 RedirectUrl 换完整 URL 未成功。 | [方法条目](../by-type/open-redirect.md) |
| 词表仓库截图：按 API、路径、文件和 header 消费者选子集 | 1596053934447394816-02.jpg 与 1596393048770240512-02.png 仅保存 403、admin、API action/object、配置、备份、CGI、Git 等词表名称。 | [方法条目](../targeted-fuzzing.md) |
| OTP 响应 Valid 与 InValid：前端放行与后端验证分开 | 1596079403737710593-02.png 的 Comparer 只显示 returnValue 差异，两边封套均为 SUCCESS 且 action ID 不同。 | [方法条目](../by-type/authn-session.md) |
| 公开仓库与连接串正则：命中、归属和秘密消费者三级核验 | 正文建议先看 dotfiles/shell 仓库并给 SSH/FTP 连接串正则；1596805258206150657-02.jpg 汇总配置/历史/秘密文件名与关键词，1597228825540055040-02.png 的搜索结果含示例风格连接串，1596104334999175168-02.jpg 仅为公开仓库工具卡。 | [方法条目](../by-type/info-secrets.md) |
| Nextcloud 通知的文件名、会话名与状态：富文本资源和代码执行分层 | 1596110894244700163-02.jpg 保存文件重命名进入桌面通知；1596186565226684424-02.jpg 保存群会话名进入通话弹窗；1596186678732984322-02.jpg 保存 Full Name/Status 中 img 进入 Windows 客户端。 | [方法条目](../by-type/desktop-client.md) |
| WODAT 标签与数据库认证：成功会话不代表管理角色 | 1596134108920438785-02.jpg 显示 TNS 监听、多个 ORA-01017 及一项认证成功，并将 SYSDBA/SYSOPER 标成 potential/manual confirm。 | [方法条目](../discovery/passive-and-services.md) |
| 历史 checkout URL 与 view-source：遮罩不代替服务端数据裁剪 | 正文称归档发现 orders/uuid 页面，界面遮罩但源代码仍含地址、订单和邮箱。 | [方法条目](../by-type/info-secrets.md) |
| Concrete CMS 远程文件导入：扩展检查与响应可读性分开 | 1596201899103068160-02.jpg 称远程上传要求 200/后缀，私有 IP 可通过，PATH_INFO 风格的脚本路径后接图片/HTML 后缀，结果被保存供下载。 | [方法条目](../by-type/ssrf.md) |
| 旧子域与参数反射：优先级线索不代替 XSS 证明 | 两帖给出业务/应用了解→旧子域→私有参数词表→反射/XSS 的序列；1596214043215556608-02.jpg 只有报告列表和 High 标签。 | [方法条目](../hunting-strategy.md) |
| DNS Rebind 摘要：检查时地址和连接时地址绑定 | 1596217122564329473-02.jpg 称远程导入通过 DNS rebind 访问云元数据，并列三份未保存附件。 | [方法条目](../by-type/ssrf.md) |
| 额外 header 触发导航：攻击者可控条件与 canonical URL | 1596217238893334530-02.jpg 的摘要称额外请求头造成导航，且提到 MITM、走私/头注入或反向代理是前置条件；工作人员问是否配置 canonical URL，截图无答案。 | [方法条目](../by-type/open-redirect.md) |
| 停用账号后资料仍公开：登录状态与数据生命周期策略 | 1596413780170350593-02.jpg 称 DOMAIN/u/USERID 的资料停用后仍可读，而用户不能清除或修改，工作人员确认资料也应停用。 | [方法条目](../by-type/idor-access-control.md) |
| circle×folder 推荐查询：组合规模、取消与资源预算 | 1596413885606760448-02.jpg 的历史 Nextcloud 报告将圈子与分享文件夹组合关联到推荐接口的数据库循环。 | [方法条目](../by-type/business-logic.md) |
| 混合编码载荷表：规范化等价性要在实际消费者确认 | 1596469132543037441-02.jpg 混列 BOM/URL 编码、Unicode/数字地址表示、HTML 事件、JS 编码与命令替换，部分行被裁切。 | [方法条目](../by-type/waf-bypass.md) |
| curl HTTP proxy 清理：释放所有权与协议错误路径 | 1596481996720570368-02.jpg 保存历史 curl HTTP proxy/dict 组合下 Valgrind Invalid free 和 cleanup 栈。 | [方法条目](../source-audit.md) |
| curl PUT 后 POST：方法状态和数据缓冲生命周期一起重置 | 1596482107529895938-02.jpg 的摘要称顺序复用使预期 POST 仍为 PUT，并读 READDATA 而非 POSTFIELDS，可能触及旧/已释放缓冲。 | [方法条目](../source-audit.md) |
| 名称黑名单与 file URL：字符串过滤不等于网络或文件边界 | 1596483954550669312-02.jpg 用 localhost 与另一个域名的示意对比称访问内文档；另帖只保存 file URL 被 WAF 阻断。 | [方法条目](../by-type/ssrf.md) |
| 规模 SQLi 管线：候选筛选、输入引用和验证预算 | 1596486675546443776-02.jpg 的流程从域名/HTTP/爬虫追加 URL，经 gf 到高 risk、current-db 扫描。 | [方法条目](../by-type/sql-injection.md) |
| 数值 site 搜索词：文本索引不能替代 IP 解析或授权 | 1596488447941828609-02.png 把多项数值 wildcard site 词拼接，含 256。 | [方法条目](../discovery/passive-and-services.md) |
| SharePoint 挂载异常日志：连接秘密与日志读取权限 | 1596497326859747331-02.jpg 称错误配置挂载导致连接凭据明文写入 Nextcloud 日志，影响需先取得日志。 | [方法条目](../by-type/info-secrets.md) |
| httpx 超时 10 与 30 的行数：未响应候选要保留 | 1596551278410072064-02.png 的两个 timeout 设置给出 147/230 行。 | [方法条目](../discovery/records-and-incremental.md) |
| 浏览器 JS 中 SSH 配置：公开字段、真实秘密与使用权限分层 | 1596721530255593473-02.png 与 1597061426686078976-02.jpg 可见 bundle 中内外部地址、用户名和 password 样式字段。 | [方法条目](../by-type/info-secrets.md) |
| 奖励邮件中的 MobileToken：导航与 token 消费者不省略 | 1596750626888642560-02.jpg 的邮件称开放重定向泄漏 MobileToken，参数/目标已遮挡。 | [方法条目](../by-type/open-redirect.md) |
| WordPress users 公开作者：字段敏感度不能继承 Critical 标签 | 1596751276804657153-02.jpg 指向 users REST 接口，称可见用户名/作者，内嵌 JSON 很小难辨。 | [方法条目](../by-type/info-secrets.md) |
| NLP trainFiles 再次出现的请求图：路径输入不代替读取证据 | 1596830709209264128-03.jpg 只有 JSON trainFiles 上级路径和被遮挡认证信息，没有对应任务日志。 | [方法条目](../by-type/lfi-path-traversal.md) |
| rate-limit 帖的 202 列表：入队接受与副作用完成区分 | 1596948034302414848-02.jpg 只显示多行相似长度的 202 和随机样式输入，无请求细节及邮件/业务结果。 | [方法条目](../by-type/business-logic.md) |
| Recon 工具职能表：按输出对象组织流程 | 1597081015989989376-02.jpg 将工具分为域名、DNS、端口、HTTP、截图、历史 URL、爬虫、目录、指纹、秘密及模板；另帖列框架和发现工具。 | [方法条目](../discovery/web-and-api.md) |
| Amass 数据源清单：互补来源与限额、失败记账 | 1597114427417165824-02.png 列多家历史数据源并标免费/试用。 | [方法条目](../discovery/passive-and-services.md) |
| Shodan dork 的 RDP 字节：协议特征不代表密码 | 正文把 telnet/root 字样、Citrix 标题、RDP 二进制、Jenkins 200 和 WP 配置说明作为搜索词，其中 RDP 标为密码。 | [方法条目](../discovery/passive-and-services.md) |
| 单任务积分并发：实际记账、日上限和兑换价值 | 正文称一个任务并发可重复得分；1597185627983781888-02.jpg 的评审因日上限和积分兑换率将影响收窄为 Medium。 | [方法条目](../by-type/business-logic.md) |
| KubeEye 架构的 OPA 与节点日志：规则发现和有效权限分开 | 1597221269505712128-02.png 显示节点日志/Problem/Condition Manager，经 API server 对 RBAC、workload、node 使用 OPA 规则审计。 | [方法条目](../cloud/container-k8s-security.md) |
| 返回 session 的 Origin 反射示例：浏览器读取和真实身份均需证据 | 1597231588118450178-03.jpg 把请求 Origin 原样写入 ACAO、credentials=true，并返回 id/name/email/session；GetCredentials 是固定对象示意。 | [方法条目](../by-type/cors.md) |
| EvilTree 关键词命中：可访问文件、内容确认与跳过项 | 1597232430737391619-02.png 显示本地目录树、keyword 命中 creds.csv 及多个 access error。 | [方法条目](../source-audit.md) |
| 图片文件名进入 HTML：后缀与展示字段的上下文不同 | 1597299060704411649-02.jpg 给出含引号/标签/事件的 .jpg 名称。 | [方法条目](../by-type/file-upload.md) |
| Django locale 当正则：输入可达性和复杂度要一起证实 | 1597302967547432961-02.jpg 的历史报告称 locale 在国际化 URL 中被作正则，并列旧分支修复版本。 | [方法条目](../source-audit.md) |
| curl verbose 的 CSP 提取：先解析响应头再抽域名 | 正文管线用 curl verbose 输出再以行首 content-security-policy 匹配；verbose 常含前缀且头名大小写/HTTP 版本可变，应核对实际字节，避免锚点静默漏掉所有头。 | [方法条目](../discovery/records-and-incremental.md) |
| campaign balance 与 history：认证会话仍需每个广告账号授权 | 一帖称归档发现 balance/history 泄露；1598041148337098754-02.jpg 保存 campaignManagerAccounts/{campaignId}/accountCredits 的历史报告，步骤替换 campaign ID，但图未给实际 JSON。 | [方法条目](../by-type/idor-access-control.md) |
| Electron showWindow 改成 exec：本地可写前置条件不能省略 | 1597481408402161665-02.png 的源码片段按平台启动终端，调用 child_process.exec，并出现开发工具配置。 | [方法条目](../by-type/desktop-client.md) |
| 公开 JS、币种地址与 API key：不把公开性本身判为秘密泄露 | 1597559979866820609-02.jpg 的 not-applicable 报告列 JS chunks 和 coin 配置地址，却没有具体秘密或受限消费者，引用另一份支持门户 token 报告。 | [方法条目](../by-type/info-secrets.md) |
| 邮箱形状注入矩阵：接受语法与下游消费者分开 | 1597579677786574848-02.jpg 将 XSS、模板、SQL、SSRF、参数/邮件头输入称为全部有效邮箱。 | [方法条目](../targeted-fuzzing.md) |
| RapidDNS 域名、IP 与范围入口：总记录数不代表目标完整 | 1597599227450130436-02.jpg 是历史查询入口，列 domain/keyword/IP/range 及 IPv6/CIDR 例子。 | [方法条目](../discovery/passive-and-services.md) |
| 三种被动枚举到 anew：原始来源与已完成基线分开保存 | 1597602194165215232-02.jpg 把 Amass、Subfinder、Assetfinder 合并到同一 domain.txt。 | [方法条目](../discovery/records-and-incremental.md) |
| CORS 加方法覆盖头：读取策略与真实动作仍是两道边界 | 正文主张 CORS 端点加 HTTP override 可扩展访问、绕过 CSRF/XST，但没有请求或结果；1597629835781689344-02.jpg 只是人物画。 | [方法条目](../by-type/cors.md) |
| Dovetale 创作者申请：审核者渲染与旧对象加载前提 | 1597650772929519616-02.jpg 描述创作者姓名字段保存后由品牌管理员审批，包含 object/scriptlet 形状及付费订阅前置条件。 | [方法条目](../by-type/xss.md) |
| pending review CSV 导出：登录身份不等于组织资产权限 | 1597678098153193473-02.jpg 的报告称任意登录用户可通过 organization handle 下载 pending review CSV。 | [方法条目](../by-type/idor-access-control.md) |
| 视频发送文本的 stored XSS 摘要：消费者和会话影响分层 | 1597708447105126400-02.jpg 的双方摘要只说给朋友发送视频时的文本存在载荷，可能会话劫持，没有代码或 DOM。 | [方法条目](../by-type/xss.md) |
| etc/passwd 报告模板：URL 和哈希主张不足以证明读取 | 1597844949051269121-02.jpg 只有编码路径、未填步骤和“发现密码哈希”的模板，没有响应或字段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| ShareFinder 调用已有代理：执行前提、共享 ACL 与编码 | 正文以 powershell-import/psinject 调用共享发现脚本并写 ASCII 文件。 | [方法条目](../source-audit.md) |
| Base64 身份图示：token 完整性和对象授权分别核验 | 1597961148338520065-02.jpg 图示客户端改 Base64 ID 后服务端信任，随后把 IDOR 都归因弱 session、反对任何用户输入。 | [方法条目](../by-type/idor-access-control.md) |

| 历史保存帖0152：管理员路径发现与低权限动作读回 | 先用自有管理员账户列出功能和实际请求，再用自有普通账户逐一检查相同动作的服务端权限。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0152：访谈笔记中的功能建模与端点发现 | 保存的访谈图把子域、历史 URL、JS 端点与登录/注册/每个功能的手工检查结合。 | [方法条目](../hunting-strategy.md) |
| 历史保存帖0152：Firebase 公共配置与数据库授权分开 | apiKey、databaseURL 等前端配置出现并不自动等于秘密泄漏或可写数据库。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 历史保存帖0152：Airflow 登录 next 的规范化边界 | 历史报告提示 next 参数中斜杠/反斜杠的服务器判定与浏览器最终 URL 可能不同。 | [方法条目](../by-type/open-redirect.md) |
| 历史保存帖0152：VCS 元数据进入 shell prompt 的二次解析 | 保存图展示 Git/SVN 分支元数据进入 vcs_prompt、PS1/.bash_prompt 后发生再次命令替换的思路。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 历史保存帖0152：团队成员移除同时绑定团队与用户 | 团队移除动作不能只检查发起者是某处的成员：需要发起者在目标团队的权限、被移除用户与该团队的关系及动作规则。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0152：成功页消息标识与敏感对象读取 | 正文把 success 页的 message 数字标识与身份证信息暴露关联，截图没有实际字段。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0152：混合标签与事件载荷需回到具体渲染上下文 | 正文列出混合多标签的 polyglot、details/open/ontoggle、SVG animate/onbegin、SVG onload 等字串。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0152：长延时与不同目标不是 SQL 因果对照 | UA/Header 或 POST 参数可进入日志、查询或后续后台处理，先找真实 SQL 消费者。 | [方法条目](../by-type/sql-injection.md) |
| 历史保存帖0152：从历史 URL 提取词表保留结构与变量边界 | 保存脚本用 gau→unfurl→sed 生成域名、参数键和路径词表。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0152：shell 混淆字串的消费者与展开前提 | 变量拼接和 glob 可以改变 shell 看到的字串，但只有外部输入实际进入会解析这些语法的 shell 调用时才有关。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 历史保存帖0152：文件名改写需证明保存路径与处理器 | 正文声称扩展名斜杠、空白及 CRLF 可使上传名称被截断。 | [方法条目](../by-type/file-upload.md) |
| 历史保存帖0152：XSS 流水线输出契约与跳过步骤 | curl/参数发现/waybackurls/过滤/awk/dalfox 的图把多个文件和列格式串接，却有缺少输出参数、sort 输入与输出混淆及按第二列提取 URL 的问题。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0152：OAuth 回调与状态逐个边界核验 | 图列出开放重定向回调、路径规范化、伪子域、HTML/referrer、state 和 client_secret。 | [方法条目](../by-type/oauth-oidc.md) |
| 历史保存帖0152：统计 postMessage handler 的来源与动作权限 | Shopify 历史截图描述 checkout→主站的消息转发及 GA 调用。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0152：404 与旧归档不是服务可认领证明 | 历史 Kajabi/Oberlo 报告给出域名接管标题、归档 PoC 和清理 DNS 建议；另一正文提醒404与接管不等价。 | [方法条目](../by-type/subdomain-takeover.md) |
| 历史保存帖0152：AI 评分解释和虚构争论不能充当规范 | 两张 AI 输出分别解释 CVSS 与编造研究者/triager 争论，包含可疑指标、自注册与权限混淆及互相矛盾的推理。 | [方法条目](../impact-and-acceptance.md) |
| 历史保存帖0152：解绑外部身份后的既有会话生命周期 | Shopify 历史链以先取得账户访问、绑定 Google 并建立会话为前提，之后受害者解绑但会话仍有效。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0152：外部身份解除关系与登录授权状态 | 身份关系被删除、外部提供商令牌被撤销以及本应用会话失效是三个状态。 | [方法条目](../by-type/oauth-oidc.md) |
| 历史保存帖0152：富文本策略变更与保存后渲染路径 | 两个帖子保存同一 Shopify /admin/product、/admin/collections 报告。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0152：点击劫持删除账户需独立交互证据 | 正文与图片只有删除账户点击劫持奖励标题。 | [方法条目](../by-type/csrf.md) |
| 历史保存帖0152：文件名载荷清单先定位下游消费者 | 保存列表混合路径穿越、SQL 延时、HTML/脚本和 shell 字串，甚至 document.comain 拼写错误。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0152：Tiny File Manager 默认配置与管理服务暴露 | MTN 历史报告写到跳转后发现文件管理器并用默认配置登录，声称可修改/上传/删除但未展示操作。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0152：SSRF 源地址线索不扩展测试授权 | 正文建议从 SSRF 看到的出站 IP 转向同网段其他 IP。 | [方法条目](../scope-and-rules.md) |
| 历史保存帖0152：Swagger 文档加载参数与本地管理端渲染 | Acronis 历史截图在本机安装管理端并给出 Swagger url 指向外部页面的路径，未展示完整执行。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0152：httpx 文本转 CSV 保留字段与引用 | 正文把 httpx 的状态、标题、服务器、IP 和重定向文本用 sed 改成逗号分隔。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史保存帖0152：libcurl PUT→POST 的复用状态与回调所有权 | 截图明确同一 libcurl handle 先 PUT 后 POST，设置 POSTFIELDS 后仍意外调用 READFUNCTION。 | [方法条目](../source-audit.md) |
| 历史保存帖0152：Cortex 观测端点认证和信息暴露边界 | Shopify 历史摘要确认 Cortex 误暴露且加认证修复，列出 config、pprof 与 cmdline。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 历史保存帖0152：订阅参数变更需对照服务端有效权益 | plan_type、gift_code 的提示只能产生业务假设；图片是 Business Logic Errors/High/Triaged 标签，没有参数、计费或权益读回。 | [方法条目](../by-type/business-logic.md) |
| 历史保存帖0152：netrc 末行解析的长度与文件控制前提 | 历史 .netrc 报告描述末行非空白字串且无换行触发栈边界读取，在特定路径可能写零越界。 | [方法条目](../source-audit.md) |
| 历史保存帖0152：服务端二次请求的路径和查询解释差异 | 正文列出编码、分号、NUL、反斜杠、通配符及 ?&# 等 secondary context 候选。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0152：AI Go 扫描代码的错误路径与判定失真 | 图中代码 GET 固定 URL，用正则对响应正文匹配后输出有/无 XSS，缺少输入、反射位置、渲染及执行关联；ioutil 未导入，错误后继续访问响应也需修正。 | [方法条目](../source-audit.md) |
| 历史保存帖0152：WP_Query 错误截图绑定调用入口 | 本机 WordPress admin-ajax 请求的 query vars 与返回 SQL 语法错误支持调查输入→查询结构的关系。 | [方法条目](../by-type/sql-injection.md) |
| 历史保存帖0152：头像邮箱摘要的隐私候选与字典验证 | Gravatar 图将头像路径摘要与邮箱候选匹配关联；摘要不是可任意逆转的加密，匹配依赖候选空间与规范化。 | [方法条目](../by-type/info-secrets.md) |
| 历史保存帖0152：换行 SVG 弹窗证据只属于保存上下文 | 正文有换行与 tagged-template 风格 SVG 字串，图片可见 URL 片段与弹窗。 | [方法条目](../by-type/waf-bypass.md) |
| 历史保存帖0152：项目选择指标不能替代逐项范围核验 | 宽范围、处理快、公平、新项目等偏好可影响优先级，正文的 safe harbor/奖励/认证数量只是旧快照。 | [方法条目](../scope-and-rules.md) |
| 历史保存帖0152：敏感文件发现与凭据有效性分开 | subfinder/dirsearch 找到 Accesses.txt 的文字没有实际内容证据。 | [方法条目](../by-type/info-secrets.md) |
| 历史保存帖0152：切换目标之前保留已测面与负证据 | 无发现后换目标或休息可用于工作节奏，但不能把时间耗尽当作测完所有功能。 | [方法条目](../hunting-strategy.md) |
| 历史保存帖0152：桌面配置行为回到 API 与真实服务器身份 | Windows 应用“使用管理员账户更新配置”及 .NET 反编译登录 API 的正文是线索。 | [方法条目](../by-type/desktop-client.md) |
| 历史保存帖0152：Nuclei 年份 glob 是选择条件而非检测结论 | 旧版截图通过路径 glob 选年份模板并列出已加载规则。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0152：目录正则秘密扫描区分命中与消费者 | EvilTree 图显示本地配置树的 db_passwd 字串。 | [方法条目](../by-type/info-secrets.md) |
| 历史保存帖0152：将401改200只改变客户端观察 | 正文说 Node 登录失败后把响应401改200出现管理界面，图片只有高危报告标题。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0152：项目关闭与报告状态是不同生命周期 | 正文描述项目关闭时仍有 triaged/unresolved 报告。 | [方法条目](../reporting.md) |
| 历史保存帖0152：Airflow Basic 认证与默认配置归类 | 正文用 Basic header 访问 pools 的例子先检查实际认证方式、初始化配置和服务端角色。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0152：代码题中 SQL 参数化与删除请求来源分离 | 代码图的 DELETE SQL 使用占位符，但 /delete 为 GET 路由，csrf/session/id 来自服务端读取 Cookie 后的 user 对象，没有可见独立请求令牌校验。 | [方法条目](../by-type/csrf.md) |
| 历史保存帖0152：框架防护配置核对实际 HTTP 响应 | 代码题把 X-Frame-Options 放进 HTML meta，却未设置同名响应头。 | [方法条目](../discovery/client-and-cloud.md) |
| 历史保存帖0152：批量状态输出区分传输失败与 HTTP 响应 | 状态扫描器图输出000与200/301/403等；000只可作为工具的失败/未得响应标记，需回到退出码和错误详情。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史保存帖0152：端口扫描排除项与后续脚本行为 | naabu 一行排除80/443并转交 nmap 的版本、默认和 vuln 脚本，设并发50，但无结果。 | [方法条目](../discovery/passive-and-services.md) |
| 历史保存帖0152：爬虫替换参数列表不等于 XSS 已运行 | gospider、文本过滤、qsreplace 生成查询候选，图显示双重编码 SVG URL 而无响应/执行。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0152：AI AMM 示例的身份键与资产账本约束 | Solidity 图片中 provider 以 msg.sender 单键存储、pool 以 token 对存储；公开 sender 的散列比较不独立证明资产来源，数值 liquidity 增减也不证明代币转入。 | [方法条目](../by-type/business-logic.md) |
| 历史保存帖0152：破坏性操作不是漏洞证明的必要步骤 | 保存正文直接建议删除管理员家目录或禁用 SSH。 | [方法条目](../scope-and-rules.md) |
| 历史保存帖0152：1xx 中间状态与最终结果区分 | 正文列出100/101/102/103。 | [方法条目](../discovery/web-and-api.md) |
| 历史保存帖0152：匿名与多个用户的差异测试 | anonymous/john/root 的提示可形成自有测试身份矩阵：固定同一对象与动作，比较匿名、对象所有者、同角色另一用户和高权限用户的真实响应与状态。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0152：销售平台权限对象写入与职责边界 | TikTok Seller 历史摘要指出 POST IDOR 可改 Finance Specialist 角色权限，但没有完整请求。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0152：Atlantis 可达界面与 PR 执行权限分层 | 历史 Atlantis 服务暴露摘要注明未披露敏感信息、限制访问后修复。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 历史保存帖0152：归档 URL 内 SQL 文本与当前执行区分 | 截图中的 Wayback/CDX 片段包含用户计数与 metrics 查询文本。 | [方法条目](../by-type/info-secrets.md) |
| 历史保存帖0152：本地响应采集清单与读取权限来源 | Pylirt 图在 sudo 下读取本机 IP 和 /etc/passwd 的用户/服务账号清单；这里不是密码散列文件或远程取数。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史保存帖0152：简历下载的招聘身份与对象关系 | LinkedIn 历史摘要说招聘者缺少相应权限仍可下载简历，并记载当年修复及无滥用证据。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0152：Node inspect 地址分类与浏览器 DNS 解释 | 保存报告中非法八进制形态1.09.0.0被浏览器按 DNS 名称解析，检查器保护的地址分类与浏览器解释可能不同。 | [方法条目](../by-type/desktop-client.md) |
| 历史保存帖0152：IP 入口和虚拟主机认证不共享假设 | 正文提示查看 IP 入口的认证。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0152：登录请求错误型 SQLi 的最小证明 | Sony 历史摘要描述捕获登录请求、工具识别错误型 SQLi并枚举数据库名，没有请求和错误细节。 | [方法条目](../by-type/sql-injection.md) |

| 历史保存帖0153：被阻断的 fuzz 先核对规则与成本 | 正文只有如何绕过项目封禁的问题，没有技术解法。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0153：本机事件弹窗与错误页文字分级 | 教程封面可见本机查询、焦点事件与弹窗，但不包含完整渲染代码或接收者；另一图仅错误页显示被改写文字。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0153：盲 XSS 通知绑定唯一实验标记 | Slack 的 XSS-Hunter 消息与裁切 URL 可作回调线索。 | [方法条目](../experiment-design.md) |
| 历史保存帖0153：参数过滤工具保留候选分类语义 | Parshu help 以漏洞名称分类历史 URL，未展示任何检测结果。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0153：SQL 数据可达不是注入判据 | 科普图把未过滤输入进入数据库当作原因，应回到查询语法和数据边界：合法绑定参数本来就会到数据库，过滤也不能证明不可信值不会改变查询结构。 | [方法条目](../by-type/sql-injection.md) |
| 历史保存帖0153：账户与云身份假设绑定实际功能 | 正文优先看OAuth、Cognito/AWS、IDOR和提权。 | [方法条目](../hunting-strategy.md) |
| 历史保存帖0153：ThinkPHP 路由与 pearcmd 链的适用前提 | 正文给旧版本阈值和 think_lang 路径拼接/pearcmd 请求。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 历史保存帖0153：功能与目录更新的增量检查 | 长期关注同一程序、发现新增功能及回访目录可减少重复摸索。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史保存帖0153：Shodan 指纹与敏感内容假设分开 | SimpleHTTPServer、Telnet root字串、Citrix、Jenkins状态和wp-config片段是索引线索，不保证有秘密或授权缺失；RDP握手字节尤其不等于密码。 | [方法条目](../discovery/passive-and-services.md) |
| 历史保存帖0153：生成 CSRF 表单仍需浏览器认证与读回 | 工具图只有合成请求和空白PoC区域。 | [方法条目](../by-type/csrf.md) |
| 历史保存帖0153：前端禁改字段与后端字段授权 | 教学图把禁改邮箱补到POST参数，另正文声称响应操控可接管管理员但无实证。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0153：聚合 API 控制后的重定向客户端边界 | Kubernetes 历史报告先控制 metrics-server 镜像或 kube-system 匹配标签的pod，再返回30X，使调用客户端转向内部端点。 | [方法条目](../cloud/container-k8s-security.md) |
| 历史保存帖0153：桌面外部打开 API 的平台与调用权限 | Rocket.Chat 历史摘要把 openInternalVideoChatWindow URL 交给 shell.openExternal，需禁用内置视频窗口或特定Mac构建，并可能依赖已有XSS调用Desktop API。 | [方法条目](../by-type/desktop-client.md) |
| 历史保存帖0153：GSI OpenSSH 配置条件不能由版本指纹替代 | 报告抄录旧GSI-OpenSSH/Fedora/PermitPAMUserChange配置与错误密码描述，却未展示目标配置或登录实证，critical文字和平台Low不一致。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0153：MS Graph 枚举具有现有 token 前提 | AzureGraph help 要求有效 MS Graph token/refresh token。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 历史保存帖0153：IBM 服务指纹到 XXE 必须核验组件 | 两个帖子把 IBM HTTP server版本、搜索CVE、拿公开exploit直接测其他服务器串联。 | [方法条目](../by-type/xxe.md) |
| 历史保存帖0153：DNS 信息发现按记录对象与授权归属 | nic前缀只能作为旧域名信息线索，不保证各TLD都有同一入口；DNS图里的单引号循环不会执行dig替换。 | [方法条目](../discovery/passive-and-services.md) |
| 历史保存帖0153：方法清单按输入输出与消费者选用 | 25项检查及自动工具图可整理为资产发现→功能与身份→具体消费者→实证。 | [方法条目](../hunting-strategy.md) |
| 历史保存帖0153：邮箱正则匹配与地址有效性分开 | 题目中的锚定正则对给出的a/b可匹配，对缺少点后后缀或只有1字母后缀的c/d不匹配。 | [方法条目](../source-audit.md) |
| 历史保存帖0153：IFS 与 glob 展开依赖真实 shell 消费者 | 保存文字和Burp图使用变量、环境字串和glob代替被禁字符，响应呈passwd形式。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 历史保存帖0153：编码空白后的200不等于管理权限 | 教学图中/admin为302而%20变体为200，只有状态没有正文或服务器动作。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0153：标签结束与映射链接的解析交互前提 | 正文混合标签结束字串、map/area javascript链接和字符实体前缀。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0153：负数标识可能进入集合分支 | id=-1 的大 JSON 可提示sentinel/list或过滤失效，图只见部分空值/遮盖字段。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0153：Git 路径暴露与仓库恢复范围 | 正文列.git/config、refs、logs和packed-refs；图片仅P1标题。 | [方法条目](../by-type/info-secrets.md) |
| 历史保存帖0153：redirect_url 导航到协议消费者 | 代码图从URLSearchParams取redirect_url，非空直接赋location.href。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0153：布尔参数文本与协议语义一致性 | Cloudflare历史DoH摘要描述cd的0/false未落实预期DNSSEC校验。 | [方法条目](../by-type/business-logic.md) |
| 历史保存帖0153：上传写路径与分享读路径不能分别放宽 | Python代码图上传直接拼f.filename保存，而分享读只删斜杠；HTML escape保护输出字串，不能约束文件系统路径。 | [方法条目](../by-type/file-upload.md) |
| 历史保存帖0153：Log4j 一行脚本先验证本地执行契约 | bbrf→httpx→xargs sh-c 的正文把python脚本位置写成http URL；python3不会因此下载执行该脚本。 | [方法条目](../targeted-fuzzing.md) |
| 历史保存帖0153：历史排列候选保存来源与去重 | 正文说机器人用此前结果做排列。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史保存帖0153：JS 中 key 关键词不是秘密判据 | 正文奖励后的key关键词建议只能产生候选。 | [方法条目](../by-type/info-secrets.md) |
| 历史保存帖0153：请求边界差异与连接复用共同证明 | 手绘示意前代理Content-Length、后端Transfer-Encoding及后续带cookie请求。 | [方法条目](../by-type/request-smuggling.md) |
| 历史保存帖0153：回归修复与奖励状态分别验证 | Twitter旧短链报告提串联重定向/表意句号回归，BAC奖励邮件明确修复仍在进行、之后才邀请复测。 | [方法条目](../reporting.md) |
| 历史保存帖0153：Markdown autolink 复杂度受配置与输入约束 | 历史cmark-gfm摘要指autolink扩展的多项式复杂度和当时修复版本。 | [方法条目](../by-type/document-rendering.md) |
| 历史保存帖0153：Auth Analyzer 相同响应仍需对象权限模型 | 工具图显示两会话SAME/DIFFERENT及Cookie替换，范围限制未勾选；另图是Juice Shop目录产品JSON。 | [方法条目](../by-type/idor-access-control.md) |
| 历史保存帖0153：模板名与实际检测证据一起保存 | 分享使用的Nuclei模板可提高复核，但还需模板内容版本、引擎、输入/过滤、身份、请求与实际响应及失败/跳过记录；模板存在或标签不能替代结果。 | [方法条目](../reporting.md) |
| 历史保存帖0153：GitHub Actions exportVariable 的文件协议边界 | Electron网站报告实际讨论@actions/core把不可信值写入GITHUB_ENV，固定分隔符使值跨变量边界。 | [方法条目](../source-audit.md) |
| 历史保存帖0153：DNS 目标替换示意不补足重绑定链 | 保存图初始pharmer地址后切真实地址、script/iframe示意，缺少TTL、逐次解析、同源读取与浏览器防护实证。 | [方法条目](../discovery/client-and-cloud.md) |
| 历史保存帖0153：实体与 Unicode 拼接先检查真实 DOM | 正文onclick含globalThis、实体、Unicode和字符串拼接，但字串闭合/调用形式本身需核验。 | [方法条目](../by-type/waf-bypass.md) |
| 历史保存帖0153：WordPress 安装向导可达与初始化动作分开 | /wp-admin403而setup-config.php可访问可能只是不同路由，不保证可创建数据库或提权。 | [方法条目](../by-type/authn-session.md) |
| 历史保存帖0153：HTTP method override 按层解释实际动作 | 帖子仅讨论方法覆盖头是否应限制，没有具体应用行为。 | [方法条目](../discovery/web-and-api.md) |
| 历史保存帖0153：推荐比赛属性属于服务端可信字段 | MK8DX历史创建API的attributes数组未验证，可使用户比赛进入Recommended靠近官方条目。 | [方法条目](../by-type/business-logic.md) |
| 历史保存帖0153：SVG 属性 ReDoS 核对正则与配置 | 旧Rails PermitScrubber摘要指特定SVG属性净化路径的回溯复杂度。 | [方法条目](../source-audit.md) |
| 历史保存帖0153：净化器标签组合与所有配置入口回归 | Rails历史图有svg+style/math+style允许组合保留危险结构，以及select/style在class属性与sanitize参数两种配置路径，补丁只处理一条。 | [方法条目](../by-type/xss.md) |
| 历史保存帖0153：旧经验保存证据等级与适用时间 | 阅读资深研究者旧帖可以发现思路，但经验名望不证明当前版本、政策或payload有效。 | [方法条目](../source-audit.md) |

| AD FS 的 NTLM 握手不能替代中继成立证据 | 保存图仅示 Negotiate、Challenge、Authenticate 三段正常握手。 | [方法条目](../by-type/authn-session.md) |
| JS keylogger 演示应缩减到无敏感数据的入口验证 | 图中实验脚本收到示例按键，只证明已加载脚本能观察输入，未展示攻击者控制入口或另一主体执行。 | [方法条目](../experiment-design.md) |
| SecRandomCopyBytes 输出采样与随机源审查分工 | 帖子建议将随机输出交给 Sequencer 做样本分析。 | [方法条目](../by-type/authn-session.md) |
| NETON 沙箱汇总中的样本和环境必须可追溯 | 保存图聚合 IP/ASN、时间、文件哈希、模块、主机信息及虚拟机检查。 | [方法条目](../discovery/records-and-incremental.md) |
| 侦察流水线在每个阶段保留输入输出与失败状态 | 几张图分别展示子域发现→DNS/HTTP 探测→扫描通知、多来源合并→URL 收集，以及 DNS、端口、截图、历史 URL、爬虫和模板工具分类。 | [方法条目](../discovery/records-and-incremental.md) |
| IBM 客户端标识和秘密字段需分别判断用途 | 正文只列 X-Ibm-Client-ID 与 X-Ibm-Client-Secret 字段名及外链。 | [方法条目](../by-type/info-secrets.md) |
| JK status 的 dump 与控制参数需按操作权限审查 | 保存正文将 jk_status 的 cmd=dump 与 opt=0 联系到读写状态，图片只有 P2/Triaged 标题。 | [方法条目](../by-type/idor-access-control.md) |
| 功能下线、奖励、受理状态和修复需各自记录 | 保存对话中报告者追问阻塞，回应称功能对所有账户消失；另有 Not Applicable 后奖励积分，以及 Azure 奖励邮件。 | [方法条目](../reporting.md) |
| WordPress debug.log 的实存日志与泛化文件读取分开 | 保存日志出现 PHP fatal error、插件路径和堆栈，是具体日志暴露线索。 | [方法条目](../by-type/info-secrets.md) |
| Auth Analyzer 的 SAME 标签回到对象和动作比较 | 矩阵把不同角色响应标为 SAME，但相同状态、长度或正文不等于越权。 | [方法条目](../by-type/idor-access-control.md) |
| Scscanner 的 000 与 AllJobsDone 都要拆解 | 保存截图将 000、301、200、403、404 放在同一结果列，并示 301 过滤后仅两条 URL 及 AllJobsDone。 | [方法条目](../discovery/records-and-incremental.md) |
| 把秘密从 Akismet 子域移到请求体仍需检查整条传输链 | 图示 API key 原先在主机名中，修改为请求体。 | [方法条目](../by-type/info-secrets.md) |
| AngularJS CSTI 的版本表达式以实际编译入口为界 | 正文列若干版本的表达式，图片仅显示测试标记弹窗。 | [方法条目](../by-type/xss.md) |
| Squarespace 未认领页面只是域名接管候选 | 截图显示 Domain Not Claimed/404，与正文 CNAME/服务绑定假设组合。 | [方法条目](../by-type/subdomain-takeover.md) |
| 公开 LFI 链接清单与实际读取证据不能混同 | Sony 摘要列路径/参数及 passwd、proc/version，另一图为第三方 URL 列表，未展示完整读取响应。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 监护人邮件确认令牌绑定到签发时的地址和关系 | 截图展示改成自有邮箱取得令牌、未点击再改回另一地址的思路，缺最终令牌使用和关系完成结果。 | [方法条目](../by-type/authn-session.md) |
| AzureGraph 帮助页的令牌前提与权限输出分开 | 图示工具需要 MSGraph/refresh token，并有用户、设备等查询接口。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| localhost 的 focus 弹窗不能保证绕过任意 WAF | 图为 XSS 教学封面及本地 contenteditable/autofocus/onfocus 标记。 | [方法条目](../by-type/xss.md) |
| 电话参数归一化后身份、投递和 OTP 限速键应一致 | 图中 phone-context/ext 变体指向同一投递号码，却以整串输入计 OTP 限速。 | [方法条目](../by-type/authn-session.md) |
| phone-context 与 ext 进入不同消费者时分别定向验证 | 保存图把电话参数关联 HTML、参数解析、SQL、模板和 URL 消费者。 | [方法条目](../targeted-fuzzing.md) |
| 篡改 302、权限布尔或 OTP 提示先核对服务端授权 | 保存例子包括将 302 改 200 并移 Location、permissions 中 admin 标记/编号修改，以及 OTP 页面显示 Matched。 | [方法条目](../by-type/authn-session.md) |
| ZAP Ajax crawler 的登录 Cookie 只建立既有会话 | 帖子描述用手工 Cookie 让 Ajax crawler 进入已有登录状态。 | [方法条目](../discovery/client-and-cloud.md) |
| 方法切换、匿名 token 与 CSRF 链都需要真实浏览器对照 | 正文列 POST→GET、移除 token 及 CSRF 可到创建管理员/改账号的链；图片另称匿名 token 可复用于任意受害者，并展示截断表单。 | [方法条目](../by-type/csrf.md) |
| 重定向 URI 多层编码需逐层标注解析结果 | OAuth 幻灯片展示编码路径、点段和 fragment 中 code 的候选。 | [方法条目](../by-type/oauth-oidc.md) |
| 历史响应文件先当不可信内容进行隔离阅读 | 帖子建议人工用浏览器查看 waymore 保存响应补充 URL 解析结果。 | [方法条目](../discovery/client-and-cloud.md) |
| XML 文件扩展名与命名空间均不能独立确认 XSS | 保存正文/图将脚本放在 XML 前缀标签内，命名空间写作 http://w3.org/1999/xhtml；另图有 localhost 弹窗但无原始头。 | [方法条目](../by-type/xss.md) |
| 敏感文件词表按真实内容和公开预期筛选 | 正文列 .pnp、.DS_Store、.env、npm/yarn 日志、.firebase、.vscode、authDump、sampleemployees、web.config 等路径。 | [方法条目](../by-type/info-secrets.md) |
| Android 系统 CA 截图与应用 HTTPS 解密之间仍有边界 | 两张图显示模拟器系统信任 PortSwigger CA，并未展示应用流量。 | [方法条目](../discovery/client-and-cloud.md) |
| user_oidc 的 HTTP provider 配置先审查谁能设置和秘密如何传输 | 截图显示容器/管理配置中 provider URL 及 client secret，秘密传输结果未完整保存。 | [方法条目](../by-type/oauth-oidc.md) |
| user_oidc 的 Safari 分支要跟踪 HTML meta refresh 消费者 | 代码截图通过 UA 含 Safari 且不含 Chrome 选择 DataDisplayResponse，把 URL 拼接到 HTML meta refresh。 | [方法条目](../by-type/xss.md) |
| Upload Scanner 的 High/Certain 结果回到文件处理链复核 | 帖子称将请求发送给扩展即可发现 RCE/XXE/XSS，图中只见实验路径的 SVG XXE/SSRF High/Certain 告警及上传页面。 | [方法条目](../by-type/file-upload.md) |
| self-XSS 升级链逐个证明跨主体传递 | 正文把缓存投毒、复制 iframe、Cookie 自动登录列为升级方向。 | [方法条目](../by-type/xss.md) |
| InviteLink 的整数边界要满足有序区间和有限循环 | PHP 图把 from/to 转整数，允许 from 在 0..16、to 仅 <=64，循环从 from 到不等于 to。 | [方法条目](../source-audit.md) |
| InviteLink 的长度区间与随机目的需要一起审查 | 同一代码按 to-from 次从小写字母表抽取字符，允许区间时实际长度可能很短，并使用 rand。 | [方法条目](../by-type/authn-session.md) |
| 免费交易配额的并发结果以已接受事务账本为准 | 正文声称 15 次免费交易变成 200 次，图片只有奖励及会修复。 | [方法条目](../by-type/business-logic.md) |
| 延时 SQL 候选必须匹配数据库和真实语法消费者 | 正文有 JSON 形式 SLEEP(20)，图列多种引号/括号和 MSSQL WAITFOR(5) 组合。 | [方法条目](../by-type/sql-injection.md) |
| JS 路径正则提取的结果保持为有限候选 | 正文管道只匹配双引号中的有限字符路径，再排序去重。 | [方法条目](../discovery/web-and-api.md) |
| PHP 固定 substr URL 校验与真实 authority 解析必须一致 | 保存代码只检查前五字符为 https、固定偏移 8 长度 22 的文本匹配，再交 cURL；注释末尾字符与代码偏移不一致。 | [方法条目](../by-type/ssrf.md) |
| PHP SSRF 题目的缺参分支和 cURL 输出单独检查 | 代码先访问 $_GET[url] 再判断 isset，可能触发缺参数警告；curl_exec 的输出方式也需与 CURLOPT_RETURNTRANSFER 配置核对。 | [方法条目](../source-audit.md) |
| Wayback 中的登录信息以历史有效性与最小披露报告 | 正文讲 php/admin 历史照片中发现凭证并声称登录，没有保存完整原请求或现时权限证据。 | [方法条目](../by-type/info-secrets.md) |
| Go 错误消息的 JSON 外形不保证浏览器以 JSON 解析 | 图片中 invalid license 回显带事件标签并出现域名弹窗，缺真实响应头/原请求。 | [方法条目](../by-type/xss.md) |
| admin.tar.gz 候选先确认归档字节而非报告标题 | 正文称敏感备份，图只有 admin source code zip file/Triaged。 | [方法条目](../by-type/info-secrets.md) |
| displayname 长度触发 SQL error 与 SQL 注入分开 | 保存报告标题将缺长度校验关联 SQL error，状态为已解决、低等级 DoS，未给实际语句/响应。 | [方法条目](../source-audit.md) |
| gospider 到 Dalfox 的文本管道保留解析和授权边界 | 保存管道串联爬深/并发、媒体黑名单、other-source、code-200 grep、awk 字段和 qsreplace。 | [方法条目](../discovery/records-and-incremental.md) |
| HTTPLoot 爬虫默认并发和表单提交需显式配置 | 帮助图给并发 180、深度 3、表单字段随机填充、提交表单、并行 15、TLS 校验和域外爬取开关。 | [方法条目](../targeted-fuzzing.md) |
| 混合大小写、制表符和反引号字符串按真实 URL 消费者检验 | 正文说直接 javascript 字符串失败后尝试大小写及 ASCII tab 变体，图片仅奖励邮件。 | [方法条目](../by-type/xss.md) |
| httpx 的 POST 登录探测与跟随跳转并非纯存活检查 | 正文将 admin/login POST、100 线程、重定向和标题去重连接。 | [方法条目](../targeted-fuzzing.md) |
| Cloudmare 的相似度和云 IP 标签只辅助归属调查 | 保存输出有子域、CDN 地址、解析错误、misconfigured 候选，最后比较页面 23% 相似且报告 IP not found。 | [方法条目](../discovery/passive-and-services.md) |
| 重置链接与 Referer 泄漏要分清生成阶段和访问阶段 | 正文说修改 forgot-password 请求 Referer 指向回调后可窃取重置链接。 | [方法条目](../by-type/authn-session.md) |
| URL 批量替换与 uid grep 不能代替命令注入数据流 | 保存管道经过 httpx/gau/qsreplace/ffuf、重放代理和 uid 文本匹配，包含需核实的引号与字段格式。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Webhook、上传处理和链接展开分别追踪实际请求者 | 正文枚举 webhook、URL 上传、link expansion、代理为候选。 | [方法条目](../by-type/ssrf.md) |
| AI 生成 actuator 替代路径作为带来源的候选词 | 图中 AI 建议 management/monitoring/admin/system 路径及配置属性，未展示真实部署。 | [方法条目](../discovery/web-and-api.md) |
| 大请求的 408 和 Server 头不能确定 WAF 后真实源站 | 正文说大 payload 引发 400 后露出真实服务器，图实际为 GraphQL POST 的 HTTP/2 408 和 Puma 版本头。 | [方法条目](../discovery/web-and-api.md) |
| HRS 奖励和 CL-/H2.CL 题目仍缺原始解析链 | 四张图为奖励及数据外流标题，其中两项 CL- 后截断，未给帧。 | [方法条目](../by-type/request-smuggling.md) |
| TaxJar 成员取消订阅与订阅信息读取是两个权限动作 | 保存报告摘要给出成员能看到订阅细节并取消账号，已解决/Medium/$500。 | [方法条目](../by-type/idor-access-control.md) |
| TaxJar 连接账号的角色授权和最终关联分别检查 | 摘要说成员可查看已连接账号并新增购物车，提 GET /auth/[CARTS-NAME]?authenticity_token=0。 | [方法条目](../by-type/idor-access-control.md) |
| 按技术选目录词表仍需版本、负对照和请求预算 | 帖子列 php/aspx/java 不同词表，未保存外链全文。 | [方法条目](../discovery/web-and-api.md) |
| Grafana snapshot 的 key 占位符与公开快照预期分开 | 正文给 api/snapshots/:key，图仅 CVE2021-39226/P2/Triaged 标题。 | [方法条目](../by-type/idor-access-control.md) |
| GoClouds 的提供商分类与 DNS 失败分开保存 | 截图按域名和地址族输出云服务 false/AWS true，另有 DNS timeout。 | [方法条目](../discovery/records-and-incremental.md) |

| HttpOnly 与 XSS 所处同源请求权限不能混同 | 正文把无法读 Cookie 时寻找 CSRF token 联到 ATO，奖励图的金额也与正文不同。 | [方法条目](../by-type/csrf.md) |
| 设备码授权审查绑定发起客户端与用户所见目的 | QR/MFA 更新邮件只是设备授权诱导示意。 | [方法条目](../by-type/oauth-oidc.md) |
| 搜索减词和扩展名筛选保留未过滤基线 | 保存搜索分别加 site、减 www/shop 等词和 ext:php，另结果只是截断 IP/地理 JSON。 | [方法条目](../discovery/web-and-api.md) |
| 重复的 AD FS 三段图只支持认证链建模 | 本组两帖同正文带正常 NTLM Negotiate/Challenge/Authenticate 图。 | [方法条目](../by-type/authn-session.md) |
| 云分类输出中的 false 与解析超时保持不同结果 | GoClouds 图中输出 IPv4/IPv6、AWS true/其他 false，并有 DNS timeout。 | [方法条目](../discovery/records-and-incremental.md) |
| Shodan Grafana 与 SSL Facet 线索按实际资产核验 | 正文用 org、Grafana title、SSL Facet 和默认词表找候选，图仅有版本区间 XSS 奖励题目或 InfoDisclosure 标题。 | [方法条目](../discovery/web-and-api.md) |
| 子域排列与 takeover 一行工具保留候选状态 | 正文串联三类枚举并追加同一 FILE、随后 subjack；另建议 a1/a2/a3 域名序列。 | [方法条目](../discovery/records-and-incremental.md) |
| 服务台开放注册与内部请求权限分开检查 | 正文说 atlassian servicedesk 有时开放 signup。 | [方法条目](../by-type/idor-access-control.md) |
| JS 与代码搜索的 AWS/Jira/Okta 秘密先确认作用和授权 | 正文从 JS、view-source 避免前端跳转及组织密码词搜索寻找秘密，图仅 AWS key 标题。 | [方法条目](../by-type/info-secrets.md) |
| 跨服务凭证复用需要服务范围与角色独立证据 | 保存叙述从低权限 Jenkins 凭证转到 Jira，图片只有 P1 portal 标题。 | [方法条目](../by-type/authn-session.md) |
| 以被保护资产和验证问题组织学习与手工探索 | 图片指南强调 HTTP/JSON/DNS 基础、耐心、CTF 到工程视角，正文说明确目的后使用工具和逐项操作页面。 | [方法条目](../hunting-strategy.md) |
| 备份与 WordPress 词表由目标证据缩到有限集合 | 帖子提域名动态词表、WordPress endpoints 并问最佳词表。 | [方法条目](../targeted-fuzzing.md) |
| 网络 API 模拟以合成数据验证可观测性 | NetLlix 图列 Wininet/WinHTTP、C#、raw socket、PowerShell 到 HTTP 服务的不同调用路径。 | [方法条目](../experiment-design.md) |
| URL 导入 XML 的取回阶段与解析阶段分别确认 | 保存叙事是新子域→vhost→/file JSON URL→远端 XML，随后显示文件行；并说明升级未获允许而停止。 | [方法条目](../by-type/ssrf.md) |
| URL 取回后的 XML 实体权限以自有标记文件验证 | 同一图给外部实体声明和读取结果摘要。 | [方法条目](../by-type/xxe.md) |
| 虚拟主机发现固定连接目标并独立记录 Host 与 SNI | ffuf 简述虚拟主机无需对应 DNS，和图中新子域后的 vhost 查找形成候选方法。 | [方法条目](../discovery/web-and-api.md) |
| 字符变体和 tagged template 分别通过实际解析层验证 | 正文列混合大小写、ASCII tab、实体、混合标签与反引号调用，图片只有弹窗或本地效果。 | [方法条目](../by-type/xss.md) |
| 聊天脚本与 Cookie 外传描述缩到入口和跨主体证据 | 正文用脚本发出 document.cookie 声称 ATO，未保存实际响应/执行链。 | [方法条目](../by-type/xss.md) |
| Flask 片段先分清运行错误和潜在对象授权缺口 | 图只 import flask 却使用未定义的 Flask，database 也未给实现，按所示不能直接推定可运行服务。 | [方法条目](../source-audit.md) |
| UUID 可发现性与对象授权分别建模 | 保存图一张公开作者 userId 链接、一张截断 my-account UUID 请求，另 Flask 图直接查询指定对象。 | [方法条目](../by-type/idor-access-control.md) |
| 302 注入图先保留原始分帧字节再讨论脚本执行 | 图为 Pretty 显示的 302、Content-Length:0、Location、Set-Cookie 及脚本行，正文询问为何无弹窗。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 重复点斜线与 zip wrapper 需区分读取和执行消费者 | 正文重复点斜线 path 候选，另图示 zip 成员作为 PHP include 路径。 | [方法条目](../by-type/lfi-path-traversal.md) |
| JSON/IF/REGEXP SQL 图的语法和结果类型先在夹具检查 | 两图展示 JSON 聚合/嵌套、条件和正则，但包含参数形状需核对及 JSON_OBJESELECT 重复/截断文字。 | [方法条目](../by-type/sql-injection.md) |
| Omise 调试日志的 Authorization sink 在所有处理器去敏 | 保存代码将 self.api_key 作为 logger.debug 的参数，图建议启用 debug 重现。 | [方法条目](../by-type/info-secrets.md) |
| postMessage 到 autolink 的信任检查与 href 编码分开 | 截图显示 autolink 用正则匹配文本后拼接 a href，描述消息可达 challenge，完整输入/消息检查未保存。 | [方法条目](../by-type/xss.md) |
| GHES Pages 的仓库写权限不自动授权每个页面动作 | 报告摘要给组织仓库 write 主体通过 API 创建/删除 Pages 的历史权限缺陷和修复版本。 | [方法条目](../by-type/idor-access-control.md) |
| 组织 owner 管理成员与更改全局登录邮箱是不同权限 | TaxJar 摘要说 owner 可改同组织成员 email，进而关联恢复账号，修复限制该操作。 | [方法条目](../by-type/authn-session.md) |
| dataset owner 的两段名字在拼接边界做文本编码 | 摘要将 first/last name 拼成 owner 字段，某些普通用户仅 self-XSS，enterprise 共享场景可能跨成员。 | [方法条目](../by-type/xss.md) |
| 协作 UI 自动发 POST 需核查消息的主体和操作权限 | 保存摘要描述同算法伙伴经协作 UI 被驱动发请求，仅完整展示 Build Algorithm 与 validate 路由，第二功能不在截图。 | [方法条目](../by-type/idor-access-control.md) |
| WebSocket 协作输出仍需按浏览器 HTML 边界编码 | 两摘要涉及调试 watched expression 输出与 TogetherJS 协作消息，前者 Python 输出被作为 HTML，后者 HTTP 层编码/403 与 WebSocket 处理不同。 | [方法条目](../by-type/xss.md) |
| Host 路由到不同子域与后台 SSRF 分别证明 | 报告摘要把 Host 操作称 SSRF 并声称可访几个子域，缺实际 Host、SNI、连接地址及服务端发起请求。 | [方法条目](../by-type/host-header.md) |
| HSTS 的 IDN 缓存键与真实连接主机使用同一规范化结果 | 保存 curl 历史摘要描述字符经 IDN/Nameprep 映射成点，而 HSTS 写入用转换前主机，导致后续请求未匹配；示例出现明文端口尝试。 | [方法条目](../discovery/client-and-cloud.md) |
| 上传 SVG 的消费者决定脚本是否可达 | 保存 SVG 示意带脚本，alert(Hacked) 的变量也未定义，检测库识别 SVG 不证明执行。 | [方法条目](../by-type/file-upload.md) |
| 修复声明、Confirmed 阶段与付款分别留时间和证据 | CERT 信称相信已修复并欢迎反馈、另有新报告即修复的争议与 Confirmed 阶段截图。 | [方法条目](../reporting.md) |
| SQL 注入最小证明不以破坏性动作或 RCE 为默认目标 | 正文一项鼓励 PostgreSQL 升级，一项反对 DROP/UPDATE/DELETE 测试。 | [方法条目](../by-type/sql-injection.md) |
| 新增子域端口与枚举来源按增量基线对账 | 正文提新增子域端口、Shodan 后全端口扫描、排列组合及 Sublist3r，图列旧 Subfinder 来源和端口清单。 | [方法条目](../discovery/records-and-incremental.md) |
| docker-compose 泄露的秘密与数据库网络可达独立报告 | 保存 Acronis 历史对话说公开配置有 MySQL 凭证，但服务不对公网可达，仍给低等级奖励。 | [方法条目](../by-type/info-secrets.md) |
| open redirect 链需要实测授权结果在哪一跳交付 | 图把 return_to、redirect_uri 和 CDN 跳转连到盗 OAuth token，未给最终授权响应。 | [方法条目](../by-type/oauth-oidc.md) |
| API key scope 空集合不能被默认为主体的全部权限 | 图叙 Viewer 对 viewer/admin scope 被拒绝，却以 [] 创建全权 key 再提升角色，缺原始完整响应。 | [方法条目](../by-type/idor-access-control.md) |
| blind XSS 回调唯一标记绑定触发入口和观察来源 | 正文用 contact/name 和第三方平台描述触发，另推荐新平台。 | [方法条目](../by-type/xss.md) |
| 产品名输入与下载页渲染分别保存编码证据 | 一图产品名显示含 %00 的事件字符串，另一保存页面有按钮及确认窗，未给原始头/DOM/另一用户。 | [方法条目](../by-type/xss.md) |
| setup 可见与默认密码登录的权限结果分别验证 | 正文 phpMyAdmin setup 与 Kanboard 某端口默认密码，图只有两个 P1/Triaged 题目。 | [方法条目](../by-type/authn-session.md) |
| shell 片段先用合成字面值检查 argv 和输出状态 | 截图 qsreplace 使用弯引号，导致 < 被 shell 解释而报错；正文另给 find -exec 模板。 | [方法条目](../discovery/records-and-incremental.md) |
| PHP 重置令牌的安全空间取决原始 9000 个输入 | 完整图以 random_int(1000,9999) 后 MD5 生成 reset hash，只有 9000 种可能；哈希长度和随机 API 名称不能增加原始空间。 | [方法条目](../by-type/authn-session.md) |
| PHP 改密与令牌清除在同一原子边界完成 | 图用 UPDATE password=? WHERE resethash IS NOT NULL AND email=? AND resethash=?，成功后另调用 resetHash(NULL) 清票；passwd 未见 password_hash 处理。 | [方法条目](../source-audit.md) |
| Blind IDOR 的 200 之后追踪邮件、短信和导出归属 | 正文把 userID 变更后无正文泄露但通知泄 PII 的情况称 Blind IDOR，截图仅 schedule 请求、200 与截断 disposition。 | [方法条目](../by-type/idor-access-control.md) |
| 外部域名清单与已接受报告不能代替当前范围 | 正文建议问范围并发布政府域名仓库，图片多项历史 Accepted/P1。 | [方法条目](../scope-and-rules.md) |
| 多参数测试先隔离单变量再验证交互 | 正文比较两个参数同时放 payload 与分别替换。 | [方法条目](../experiment-design.md) |
| 404 的 UA 日志链按真正进程消费者建立因果 | 保存图请求 UA 含命令，返回普通 404；另一图回调 HTTP POST 有文件样式文本。 | [方法条目](../by-type/cmd-injection-rce.md) |
| JS 中的 S3 地址与 users.csv 读取权限各自确认 | 正文从 main.js 找 bucket，称只读开放 users.csv 泄 PII，无保存完整数据。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 403 辅助工具与自动表单爬虫都先明确无副作用边界 | 图分别只有 inside403 的工具宣称和 HTTPLoot 帮助，后者默认并发 100、深度 3、随机长度/固定表单值；默认与其他截图不同，需绑定版本。 | [方法条目](../targeted-fuzzing.md) |
| URL grep 分类的反向过滤与凭证识别分别校验 | 法文清单按扩展名、redirect 词、表单、wp、邮箱/JWT/base64 和 debug/admin 过滤；某处 -v 反而排除想找的词，反光/裁剪字不补全。 | [方法条目](../discovery/web-and-api.md) |
| Login CSRF 的自动提交示例仍需证实实际会话切换 | 图片有固定测试账户隐字段、pushState、提交后立即跳 account，action 弯引号和立即导航都可能改变行为。 | [方法条目](../by-type/csrf.md) |
| self-XSS 与登录 CSRF 链中的每个主体变化需独立证据 | 保存正文声称 self name→login CSRF→stored XSS，图只模板和遮挡来源弹窗。 | [方法条目](../by-type/xss.md) |

| 编码对象标识与通配选择器分别验证授权 | 保存案例把 user_id 做 Base64 后可解码改写，另一个示意使用带 userId 的编码 JSON。 | [方法条目](../by-type/idor-access-control.md) |
| 管理后台默认配置的证据与部署边界 | 保存帖提到通用管理面板和 Apollo 的默认账号情形，图片只给报告题名或项目界面。 | [方法条目](../by-type/authn-session.md) |
| 登录 CSRF 与自操作脚本链需要会话切换证据 | 保存正文将 self XSS 与 login CSRF 串联，相关图片的二进制哈希已有实际审阅记录。 | [方法条目](../by-type/csrf.md) |
| HTTP 与原始套接字示意应保存可观测阶段 | NetLlix 图展示 HTTP 与原始套接字两类数据传输通路。 | [方法条目](../experiment-design.md) |
| 扫描版本与失败记录决定候选是否可复核 | 保存图片出现 Nuclei 2.8.2/2.8.3、模板 9.3.2/9.3.3、加载模板数、去重目标数、速率和参数发现；单一 CVE 模板的 critical 命中、IIS 错误页或 Autodiscover 路径都只产生候选。 | [方法条目](../targeted-fuzzing.md) |
| 公开作者信息与私密用户字段的区别 | 保存 WordPress REST users 报告只有高危/解决状态，未展示受限字段与身份对照。 | [方法条目](../by-type/info-secrets.md) |
| 秘密遮罩不能只绑定已执行任务 | 保存 Airflow 情形描述连接秘密先在模板中被渲染，任务受历史依赖失败而尚未执行，秘密仍可能进入展示路径。 | [方法条目](../by-type/info-secrets.md) |
| 预约字段到邮件协议的多层数据流 | 保存截图从预约 JSON 的 displayName/email/description 指向 BookingService.php 和下方 SMTP 片段，裁切不足以证明完整链。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 协议失败后的资源所有权与重试生命周期 | curl/telnet/smb 的历史摘要提到代理 CONNECT 502 后的 use-after-free，但没有保存完整源码和内存诊断。 | [方法条目](../source-audit.md) |
| 过期分支也必须保留签名和授权校验 | 保存 JWT 摘要称 exp 过期时走到校验旁路，缺少实际实现和请求。 | [方法条目](../by-type/jwt.md) |
| 证书警告与停止发送凭据是不同结果 | 保存 nextcloudcmd 历史情形涉及自签 CA、未启用显式信任选项而证书失败后继续同步。 | [方法条目](../by-type/desktop-client.md) |
| 动态广播接收器的实际发送者边界 | 保存 Talk Android 摘要指出 registerReceiver 未配置 broadcastPermission。 | [方法条目](../by-type/mobile-android.md) |
| 修复状态需要原案例和同根因入口回归 | 保存案例出现 component 报告被接受、工单已解决但作者称仍未修复，以及“修复/奖励后重试”的建议。 | [方法条目](../reporting.md) |
| 源码测试凭据与生产消费者必须分开确认 | 保存图片有 uid/32 位十六进制字符串及 HTML 注释中的假站测试凭据；正文另提开发 Basic Auth、仓库/容器配置和生产环境复用。 | [方法条目](../by-type/info-secrets.md) |
| 闭合标签组合依赖实际解析上下文 | 保存图给大量闭合标签接 SVG 的组合，只适用于具体注入点的解析状态。 | [方法条目](../by-type/xss.md) |
| 历史 URL 到 JS 扫描字典的格式契约 | 保存命令把 gau、waybackurls、排序、wordlistgen 和 cut 串起来，另以 JavaScript MIME 条件将 URL 送入 exposures 模板。 | [方法条目](../discovery/web-and-api.md) |
| 提供商分类不能代替资产与扫描范围判断 | 保存 subfinder→解析筛选→cf-check→naabu→HTTP 探测链，以及 Cloudflare 前先过滤的建议。 | [方法条目](../discovery/passive-and-services.md) |
| 同名桶与遗留 DNS 的接管前提 | 保存 S3 摘要提到遗留 DNS 指向已不存在的同名桶，再创建名称并展示内容；没有完整地区和控制平面证据。 | [方法条目](../by-type/subdomain-takeover.md) |
| 个人简介中的脚本字面显示不能证明执行 | 保存简介截图显示脚本字符串，却没有执行效果；正文的 ATO 外链未保存。 | [方法条目](../by-type/xss.md) |
| 多跳链接与 Unicode 主机名各自规范化 | 保存 Twitter 内部跳转→analytics 链示例提到类似点号字符和 URL 编码触发白名单分歧。 | [方法条目](../by-type/open-redirect.md) |
| 原始 Location 与解码后的记录不得混写 | 保存 Python 2 示例读 Location 后调用 unquote_plus；加号在普通 URL 中可能是字面字符，不能默认采用表单空格语义。 | [方法条目](../discovery/records-and-incremental.md) |
| 整数地址的解析结果与 HTTP 可达性分开验证 | 保存图示 ping 将整数表示解析为回环，curl 另例返回 301；这不单独证明应用 SSRF。 | [方法条目](../by-type/ssrf.md) |
| 登录功能排除条款须绑定具体动作和版本 | 保存计划截图列出 web application login functions，拒绝回复称登录后的功能被排除；缺整份有效政策和上下文。 | [方法条目](../scope-and-rules.md) |
| 404 与占位文本过滤必须有保留样本 | 保存十条技巧提到真实后台登录页返回 404，另有“Will be right back”占位文本过滤命令和手工目录练习。 | [方法条目](../targeted-fuzzing.md) |
| 本地文件前缀检查与规范路径可能不同 | 保存技巧中直接绝对路径被拒绝，指定本地前缀后加父目录段却被接受；需比较原始字节、解码次数、路径合并/规范化、实际打开对象及权限，而非只看字符串起始部分。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 组织注册标识的类型与租户绑定必须一致 | 保存技巧将注册组织 UUID 换为数字表示后声称用户被放入另一组织。 | [方法条目](../by-type/idor-access-control.md) |
| JSON 转 XML 仅改变解析入口 | 保存技巧将改密码请求从 JSON 转成 XML 后接受，随后声称 XXE；200 只能说明某一请求被处理。 | [方法条目](../by-type/xxe.md) |
| API 描述与恢复入口不等于文件读到执行链 | 保存技巧出现 application.wadl、受保护操作与一个返回 200 的忘记/重置入口，后称 LFI、日志凭据与 RCE，但没有完整链的请求和权限。 | [方法条目](../discovery/web-and-api.md) |
| Twig 算术与可调用函数不是同一能力 | 保存密码模板技巧声称输入算术后输出计算值，再讨论未定义过滤器回调和 map 函数路径。 | [方法条目](../by-type/ssti.md) |
| 管理 UI 与文本 API 需要一致的授权和路由语义 | 保存 Tomcat 技巧涉及带特殊分隔段的路径、manager/html 被拦而 manager/text 可达，再通过部署功能声称执行。 | [方法条目](../by-type/idor-access-control.md) |
| 方法替换与 token 七候选都要核对浏览器状态 | 保存十条技巧和独立帖把 POST/PUT/PATCH 变 GET、参数移到查询并删除 X-CSRF 头，以 200 声称绕过；七项清单还包括缺失/字符变更/跨账号复用 token、弱生成/可猜以及 XSS 获得 token。 | [方法条目](../by-type/csrf.md) |
| APK 静态端点候选需要实际服务端 sink | 保存技巧将 APK 当压缩包查看端点，再称 HTTP 头触发盲 SQL。 | [方法条目](../discovery/client-and-cloud.md) |
| 路由别名按根因与消费者归并 | 保存技巧称同一日历功能通过多个路径别名触发 XSS 并得到多笔报告，但别名文字与完整影响未保存。 | [方法条目](../discovery/records-and-incremental.md) |
| URL 参数闭合脚本与 DOM 执行应按具体 sink 对照 | 保存 tab 参数截图有编码引号/空格和弹窗，JetBlue vsid 历史摘要给闭合脚本的表达式并显示 High 改为 Low；两者均未保存完整 sink。 | [方法条目](../by-type/xss.md) |
| 标签管理容器 ID 用于关联代码而非证明秘密 | 保存图说明从 HTML 中的 GTM ID 关联额外 JavaScript，并审阅候选域、路径和秘密；相关两图哈希已有实际审阅记录。 | [方法条目](../by-type/info-secrets.md) |
| 嵌入外部文档不自动执行于父页面 | 保存 embed src 提问、可信 iframe 域内重定向的建议与密码对话框图片，未给完整浏览器链。 | [方法条目](../by-type/xss.md) |
| 初始化端点与数据库备份是独立暴露面 | 保存正文提到 phpMyAdmin scripts/setup.php、WordPress install.php 与 MySQL 备份；图片仅报告题名或付款。 | [方法条目](../by-type/idor-access-control.md) |
| 重复对象键与全局替换会制造不同鉴权值 | 保存 IDOR 图给同名 user_id 的两个顺序和数组表示，另一技巧建议 Burp 全局 ID 替换。 | [方法条目](../by-type/idor-access-control.md) |
| 减站点和多引擎结果需要可复核集合 | 保存搜索结果使用 site 域约束、减去常见子站点，并建议多搜索引擎。 | [方法条目](../discovery/web-and-api.md) |
| CSP 评估器只产生策略候选 | 保存示例策略 script-src self 与某允许域、img-src 通配，评估器提示 host 白名单、缺失 object-src 和 Trusted Types；没有具体注入 sink 或实测绕过。 | [方法条目](../by-type/xss.md) |
| 长密码的输入边界与成本要测量而非猜测 | 保存 Nextcloud 管理员建用户的长密码报告描述无长度上限、Low 状态和一串输入，未保存耗时/资源测量。 | [方法条目](../by-type/authn-session.md) |
| 预览衍生内容也要执行分享与水印策略 | 保存 Nextcloud 步骤为分享文件夹后关闭 Allow download，收件者仍获取 preview；Collabora 展示带水印的文档，但预览可给不带水印的第一页。 | [方法条目](../by-type/idor-access-control.md) |
| 退出会话必须撤销信令与已建立媒体授权 | 保存 Nextcloud Talk 案例限定 HPB 和 guest：访客被移除后他人 UI 不再显示该访客，而原连接仍存在，再开始通话时仍自动连接。 | [方法条目](../by-type/authn-session.md) |
| 历史下载地址、目录与代码托管内容都先限量核对 | 保存帖提到历史 requests/PDF、JS 指向 S3 users CSV、目录索引和 pastebin/jsfiddle/codebeautify/codepen 搜索。 | [方法条目](../by-type/info-secrets.md) |
| 数字零与字符串 token 的类型边界 | 保存技巧提出 JSON 数字 0 与 PHP 松散比较碰撞。 | [方法条目](../by-type/csrf.md) |
| 品牌域搜索与通配政策不能混为一谈 | 保存帖建议从 *.target.* 搜新 TLD；品牌字符串匹配可能返回其他组织或未获授权域。 | [方法条目](../scope-and-rules.md) |
| SVG 主动文档导航与服务器重定向不同 | 保存 SVG 使用 onload 修改 window.location 指向示例域。 | [方法条目](../by-type/open-redirect.md) |
| 扩展名分隔符必须记录真实文件名字节 | 保存清单将空字节、换行、分号、Unicode、百分号表示和反斜线转义混列在扩展名之间。 | [方法条目](../by-type/file-upload.md) |
| 国际化邮箱的恢复标识与收件者必须一致 | 保存同形 IDN 邮件提示将外观近似域名用于密码重置，但没有请求或投递证明。 | [方法条目](../by-type/authn-session.md) |
| 响应协商与错误内容只说明对应输入的结果 | 保存建议改变 Accept 以获得 JSON/JS、版本/栈/路由，以及发送非法 Content-Type 找隐藏端点。 | [方法条目](../discovery/web-and-api.md) |
| 依赖参数的递归搜索要有限且可解释 | 保存示意先发现 ID，再在有效 ID 上发现 method，最后枚举 method 值。 | [方法条目](../targeted-fuzzing.md) |
| PingBack 端点存在与真实出站是不同证据 | 保存 WordPress xmlrpc.php/PingBack 提示没有实际请求和回调。 | [方法条目](../by-type/ssrf.md) |
| SQL 注释与大小写是语法候选而非绕过结论 | 保存图片将关键字大小写和注释混合用于 SQL 注入。 | [方法条目](../by-type/sql-injection.md) |
| 序列化 DOM 与模板标签调用不能凭外形判断 | 保存一例 XMLSerializer 序列化 document 后找关键词，另一例 document.createElement 模板标签构造 script 并把插值给 append。 | [方法条目](../source-audit.md) |
| 盲回调需绑定具体输入实例而非通知数量 | 保存 Blind XSS manager 有域、URL、hash 和多种上下文候选；另一截图只是 XSSHunter 邮件通知列表。 | [方法条目](../by-type/xss.md) |
| 地址栏显示与连接 origin 应分别记录 | 保存 2017 Tor/Firefox ESR 52.4 情形涉及 Armenian U+0578 和 punycode 地址外观分歧，平台标为 Informative；不能据此称当前浏览器仍受影响。 | [方法条目](../by-type/desktop-client.md) |
| 导出对象权限和导出字段权限必须独立验证 | 保存 PDF export 示例在 JSON 中既改 ids 为另一用户，又把 fields 扩大到邮箱/哈希列，随后声称完整任意数据库读。 | [方法条目](../by-type/idor-access-control.md) |
| 部署介质加密与任务凭据可读性是不同边界 | 保存 PXEThief 输出显示 Media Variables/Policy 解密、Task Sequence XML 和网络文件夹、Windows 设置、命令任务、Network Access Account 字段。 | [方法条目](../by-type/info-secrets.md) |
| URL 参数修改器需要明确输入输出与状态边界 | 保存 Paramix 说明从 stdin 读 URL 列表、stdout 返回参数变体，没有实现与实测。 | [方法条目](../discovery/records-and-incremental.md) |
| 多响应和证书线索需要身份与时间基线 | 保存实验建议查看每个响应、视觉与证书线索，多次请求推测负载均衡并检查 DNS/区域传输。 | [方法条目](../discovery/records-and-incremental.md) |
| Slack 字段名、服务域与秘密资源段分别判断 | 保存检索建议包括 webhooks、xoxp/xoxb、API/hash/id 和 language:shell，截图只有 Alertmanager slack_api_url 指向 hooks.slack.com 且其余被遮挡。 | [方法条目](../by-type/info-secrets.md) |
| CSV 单元格解释与客户端执行需要不同证据 | 保存报告路径是 client management→client name→导出 CSV，包含 DDE 命令示例和旧 CVE 引用，未保存真实执行结果。 | [方法条目](../by-type/document-rendering.md) |
| 隔离演练的会话归属和服务器同步要有边界 | 保存 Villain 截图展示监听、Windows 会话、systeminfo 输出与另一服务器同步，正文只有工具发布信息。 | [方法条目](../experiment-design.md) |
| 语言词典生成要保留文本而非执行 shell 片段 | 保存 dict 英法字典脚本使用 shell 分词、按用户词串 grep 和删除前缀；会损失空格、词形、Unicode 或把词当正则。 | [方法条目](../targeted-fuzzing.md) |
| 搜索历史的保存与再渲染是独立边界 | 保存帖建议搜索项后来显示在历史中时检查 HTML、重定向和所谓 DDOS。 | [方法条目](../by-type/xss.md) |
| IP 列表折叠只能表示同一个授权集合 | 保存 IP 转 CIDR 提问和 ASN 查询页面，没有真实结果。 | [方法条目](../scope-and-rules.md) |
| 示例 DAG 的触发权限与 shell 插值链 | 保存 Airflow 历史报告描述 <2.4.0、UI 能触发示例 DAG 的用户，2.3.3 BashOperator 片段将手工 run_id/dag_run 放入 bash_command。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 清洗器允许标签组合与不完整修复要分别回归 | 保存 Rails Html Sanitizer 两摘要分别涉及 select+style、不完整修复，以及 math+style 或 svg+style，历史文字同时写 ALL 与 fixed 1.4.4。 | [方法条目](../by-type/xss.md) |

| 数据主体请求的执行身份不能只来自匿名表单 | 保存 DSAR 示意建议检查匿名表单提交删除测试账户后是否未经验证处理。 | [方法条目](../by-type/authn-session.md) |
| 扫描报告导出端点需要协议与历史身份 | 保存 Nessus XML→HOST:PORT/IP:PORT 工具说明，没有解析实现。 | [方法条目](../discovery/records-and-incremental.md) |
| 负数对象标识与集合权限要独立比较 | 保存 localhost users/-1 示意返回 users 数组，其中含 admin/isAdmin；宣传图不是实际受限数据回读。 | [方法条目](../by-type/idor-access-control.md) |
| 邮件记录发现的主机不自动属于输入域的测试范围 | 保存 ExchangeFinder 先读 MX，再访问 mail 主机/OWA，并打印 Exchange 2016 CU22/Nov21 SU 与 IIS 10.0。 | [方法条目](../discovery/passive-and-services.md) |
| 提交和分支候选应保留秘密来源与消费者 | 保存建议审阅组织/开发者公开仓库、提交和不同分支，图列 ETH/BSC/MAINNET private-key、hardhat.config.js 与排除 process.env 的检索。 | [方法条目](../by-type/info-secrets.md) |
| 数据库错误、发现路径与崩溃宣称不是同一个原语 | 保存单引号无响应而加斜线出现 MySQL 语法错、404 后发现 gallery 登录，以及长十六进制输入被称为 buffer overflow/firewall crash。 | [方法条目](../by-type/sql-injection.md) |
| 配置生成器可见、可保存与可应用须分开留证 | 保存 phpMyAdmin 3.3.10.4 setup/index.php?page=config 显示带测试 verbose 的生成配置及 Download/Save，正文从 Shodan/Censys、服务指纹与 PHP 字典发现它。 | [方法条目](../by-type/idor-access-control.md) |
| 恢复邮件解析与账号选择必须指向同一主体 | 保存完整恢复候选含重复 email、CRLF/cc、逗号/空格/管道分隔、缺域/TLD 和 JSON 数组。 | [方法条目](../by-type/authn-session.md) |
| 设备 APK 获取要绑定包标识和签名版本 | 保存 ADB 导出 APK 的说明和使用示例，脚本全文未保存。 | [方法条目](../by-type/mobile-android.md) |
| 版本库、日志和调试文件的返回真实性与最小读取 | 保存 .git/.svn 元数据候选、.git/config 拼接并筛 200 的命令、logs 目录显示 error.log 2.2G，以及 info.php 的 Linux 版本片段。 | [方法条目](../by-type/info-secrets.md) |
| 注册触发的 DNS SMTP HTTP 回调先确认消费者 | 保存同一个 token 在多时刻产生 DNS、SMTP 与 HTTP 记录，正文提到云 IP 和 python-requests。 | [方法条目](../experiment-design.md) |
| 混合探针要拆成解析上下文的独立假设 | 保存混合引号、SVG 与模板算术的字符串被标为 XSS+SQLi+CSTI/SSTI，另建议向每个参数都注入。 | [方法条目](../experiment-design.md) |
| HTML 注入影响证明无需真实登录诱导 | 保存建议以登录表单跳外域来提高 HTML injection 接收率，但没有真实消费者与影响证据。 | [方法条目](../reporting.md) |
| 批量侦察的输出文件必须保留完整入口身份 | 保存 subfinder→httpx→unfurl 域→ffuf、katana/gf→sqlmap，以及 sequential parffuf 的阶段说明。 | [方法条目](../discovery/records-and-incremental.md) |
| 资料字段的视觉覆盖与脚本模板要分开判断 | 保存 firstname/surname/info 的 style 固定覆盖和 mouseover 事件，以及 constructor 模板表达式。 | [方法条目](../by-type/xss.md) |
| JS 关键词命中与公共库术语分别归类 | 保存 Nuclei 2.8.2/模板 9.3.4/单模板 2355 目标的 info Found_Token 输出，许多来自 jQuery、Drupal、Matomo、CLDR 等公共库，仅列 key/pass/token/client_id 等词；另文给 authorization/authentication/password/value 关键词。 | [方法条目](../by-type/info-secrets.md) |
| 百分号和空白字符必须追踪到最终脚本上下文 | 保存 RXSS 片段含百分号编码、实体、大小写变化、iframe/javascript 与 SVG，以及 script 名称中的 tab/newline；WebPuff URL 摘要还有多层编码和新 IP。 | [方法条目](../by-type/xss.md) |
| 源码与历史参数跨入口复用要有字段语义 | 保存从公共 PHP 仓库取 GET/POST/header/routes、证书名字/目标词典/JS 端点/URL 参数提取，以及 xnLinkFinder 和隐藏表单字段的建议。 | [方法条目](../discovery/web-and-api.md) |
| 预览格式识别必须约束转换器的资源访问 | 保存 Nextcloud HEIC 预览调用 Imagick 的历史报告，文件名 test.heic 实为 SVG 并用 xlink 引用本地 PNG；转换器支持多格式会跨过扩展名假设。 | [方法条目](../by-type/document-rendering.md) |
| 产品路径和公开报告索引只产生带时间的候选 | 保存 inurl:/content/dam ext:txt 用于找 AEM，及 site:openbugbounty.org/inurl:reports/intext:目标域查旧 XSS/redirect。 | [方法条目](../discovery/web-and-api.md) |
| PHAR 包装器与元数据反序列化触发点应分别审计 | 保存正文只有 phar:// 与 PHP 反序列化到 RCE 的入口线索，BlackHat 2018 封面没有完整链。 | [方法条目](../by-type/deserialization-rce.md) |
| 原始路径与重写头必须在同一授权对象上比较 | 保存 GET /admin 被拒与 GET /test 携 X-Original-URL:/admin 返回 200 的示意。 | [方法条目](../by-type/idor-access-control.md) |
| 禁用控件不代表所有事件上下文不可到达 | 保存 disabled input 上的 beforecopy/beforecut 示例声称在 Chrome 可用，没有保存版本或触发录像。 | [方法条目](../by-type/xss.md) |
| 畸形媒体类型的解释必须用真实字节与消费者 | 保存 Content-Type 示例把 text/plain 参数、逗号、text/html 和其他值放进一行，不能直接当合法列表。 | [方法条目](../by-type/document-rendering.md) |
| 十阶段侦察必须保留每种可达性的含义 | 保存图列资产来源/子域、DNS 解析、HTTP/端口、全端口扫描、目录、技术识别、JS、历史 URL、搜索/仓库及模板/参数变体十阶段。 | [方法条目](../discovery/records-and-incremental.md) |
| iOS 静态检查按具体数据消费者建模 | 保存图的静态项包括 React/Flutter 生态、混淆、client ID/token/key/password/device UUID、MD5/SHA-1、SQL/反序列化、WebView JS/debug/证书错误、URI handler、备份/日志、检测/pinning、资源/权限/第三方库、Info.plist、Universal Links、UIActivity/UIPasteboard、扩展/键盘及 ATS。 | [方法条目](../by-type/mobile-ios.md) |
| iOS 动态检查分清设备解锁与服务端权限 | 保存图的动态项是模拟器日志、越狱/pinning/TouchID/FaceID、隐藏功能、键盘缓存、截图、URL schemes/deep links、运行时/WebView、输入/访问、存储/加密与复制粘贴；工具仅是观察手段。 | [方法条目](../by-type/mobile-ios.md) |
| 后端不支持安全选项时不能静默当作已生效 | 保存 libcurl 构建为 libssh 后忽略 SSH_HOST_PUBLIC_KEY_SHA256 的历史报告，摘要明确该选项文档要求 libssh2。 | [方法条目](../source-audit.md) |
| 下载文件的安全性贯穿打开到后续使用 | 保存共享可写临时目录、可预测文件名的符号链接重定向写入与关闭后替换内容，摘要称是 curl 调用使用问题，另指出 file 上传读源同类边界。 | [方法条目](../source-audit.md) |
| 公开 API 控制台与私有方法授权各自验证 | 保存 DERIBIT testnet 控制台明确只用 testnet keys，且当前无 token，私有方法需另认证。 | [方法条目](../by-type/idor-access-control.md) |
| DNS 指向、租户绑定与邮件能力需要独立证据 | 保存 Node.js/Cloudflare CDN 情形声称未绑定子域可由 GitHub 账号添加，另帖提 MX misconfiguration/email takeover，但没有完整绑定/邮件回读。 | [方法条目](../by-type/subdomain-takeover.md) |
| API 文档版本和实际请求映射须同时保留 | 保存完整图先辨 API 版本、开源/定制、REST/SOAP/GraphQL、WADL/WSDL 与公开/本地文档，再映射 GET/POST/PATCH/PUT/DELETE、body/header 和 Swagger 等界面。 | [方法条目](../discovery/web-and-api.md) |
| API 编码主体与登录流程不等同授权能力 | 保存 API 图列 cookie/header 认证、OTP、JWT、加密/编码/序列化状态值和用户名/ID 哈希。 | [方法条目](../by-type/authn-session.md) |
| API 模糊测试按对象动作与合法前置状态限定 | 保存图将 endpoints、objects、methods/actions 作为三类点，词典来自公开/本地文档、历史、JS、组织仓库、开源实现和通用词表。 | [方法条目](../targeted-fuzzing.md) |
| Schema 可见与数据对象权限是不同边界 | 保存 API 图列 introspection、可视化和查询枚举，用于理解 GraphQL 结构，不能推出“数据库每个查询都可访问”。 | [方法条目](../by-type/graphql.md) |
| XSS 后的事件与 OAuth 链需要实际授权回流 | 保存帖把 HttpOnly、改邮箱需当前密码与 OAuth+event listener 联为“最容易 ATO”，但未保存监听类型和授权流程。 | [方法条目](../by-type/oauth-oidc.md) |
| 并发加入要以成员唯一性与统计不变量验证 | 保存 CTF group/join 摘要描述同一用户被记录多次并影响统计，旧同根因曾修后轻微改实现复发。 | [方法条目](../by-type/business-logic.md) |
| 重复、奖励与公开范围互不替代 | 保存 Duplicate 回复称原报告可能含私人/额外漏洞信息而不添加新研究者，Reddit 通知只准分享金额、细节需运营方明确许可。 | [方法条目](../reporting.md) |
| 延迟语法需要方言与计时负例 | 保存 WAITFOR DELAY 列多个引号/括号/分号、IF 和畸形百分号/弯引号变体，未保存响应。 | [方法条目](../by-type/sql-injection.md) |
| 消息通知入口也必须经过本地应用锁 | 保存 Talk Android 15.0.2 RC1 情形为 A 在 web 发消息、B 已登录手机并开 passcode，点通知进入内容。 | [方法条目](../by-type/mobile-android.md) |
| 字段长度错误必须绑定实际字段与持续影响 | 保存报告先说 display name/username 无上限，步骤却是 Deck Add Boards name，返回 500 后称 DoS。 | [方法条目](../targeted-fuzzing.md) |
| 默认账号端口与面板数据权限都须独立确认 | 保存文字给测试账号和 8080 面板，图只有 P1/Triaged 与客户信息题名。 | [方法条目](../by-type/authn-session.md) |
| 附件删除必须验证父卡片与文件关系 | 保存 Deck 1.8.0 请求实际是 DELETE，描述却称 POST，路径含 card ID、attachment 和 file 类型/ID。 | [方法条目](../by-type/idor-access-control.md) |
| 改密码时缺失旧密码不能静默退为无需再认证 | 保存故事称错误旧密码被捕获后删除该字段而改密成功，没有完整请求。 | [方法条目](../by-type/authn-session.md) |
| 公开用户 UUID 不能作为跨站请求的秘密 | 保存故事将用户 UUID 放在公开 URL/搜索结果却用作 CSRF 防护，并与删除旧密码组合。 | [方法条目](../by-type/csrf.md) |
| 发现 AWS 密钥与证明权限不能以弹窗代替 | 保存 Trufflehog API key 发现弹窗和 enumerate-iam 验证说明，没有保存密钥对或权限结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| MFA 超时与并发失败不得提交认证终态 | 保存 TikTok 摘要说两步验证随机 timeout 与快速多次错误尝试可能旁路，明确先要邮件/密码或手机/验证码；视频全文未保存。 | [方法条目](../by-type/authn-session.md) |
| 计划搜索目录的标签不是完整有效授权 | 保存 Firebounty 目录有域名/标题、奖励/HOF、scope 类型、undefined/security.txt 和创建/更新时间。 | [方法条目](../scope-and-rules.md) |
| Origin 反射要核对浏览器实际读取与私密数据 | 保存历史 CORS 请求在 /wp-json 送非本域 Origin，响应 ACAO 回显，credentials 头与后续效果裁切。 | [方法条目](../by-type/cors.md) |
| 多次反射的组合解析应覆盖跨片段状态 | 保存图分别给单输入反射两次的 script/comment 跨越，以及两输入在 HTML 属性引号中拼成事件的示意。 | [方法条目](../by-type/xss.md) |
| 缓存状态与错误响应的头部生产者需要留证 | 保存 Pingora 摘要限定 cached file、畸形 Range、REVALIDATED、实际经过代理且源接受 Range，并称已移除代理响应泄露。 | [方法条目](../by-type/info-secrets.md) |
| 深链到认证 HTTP 请求不能直接拼接外部参数 | 保存 Windows Nextcloud Desktop 3.6.1 摘要描述点击 nc 深链后发送任意 POST/body，旧修复又引入 CSRF，示例还涉及 OCS 路由、用户字段、日志/token 路径段。 | [方法条目](../by-type/desktop-client.md) |
| 共享权限报告的计数与有效操作必须相互核对 | 保存 PowerHuntShares 展示 computers/shares/share ACL 的 read/write/high-risk 比例、名称和创建时间。 | [方法条目](../by-type/idor-access-control.md) |
| 钱包锁定状态应覆盖所有视图和签名句柄 | 保存 Hiro 扩展两份 popup，一处锁定后另一处仍可访问，作者称可交易但未保存完整视频。 | [方法条目](../by-type/authn-session.md) |

| 畸形媒体类型的响应声明与请求解析表须分开验证 | 保存正文给出响应 Content-Type 多值声明，保存表格却比较请求 form、JSON 与 application/x-www-form-urlencoded;/json 的解析。 | [方法条目](../by-type/waf-bypass.md) |
| BlindF 奖励帖只支持盲执行候选而非必须提取 Cookie | 保存帖声称仅 cookie extractor 成功但没有载荷或消费端截图。 | [方法条目](../by-type/xss.md) |
| 侦察导图中的证书、DNS、端口和虚拟主机是不同证据层 | 图将在线枚举、字典、DNS数据、证书/反查等来源汇入域名，再分为证书检查、DNS解析、IP端口及HTTP、vhost、Wayback路径。 | [方法条目](../discovery/passive-and-services.md) |
| SVG 事件读取 URL fragment 后 eval 的客户端执行链 | 保存示例为 SVG onload 调用 eval(location.hash.slice(1))，fragment 再创建外部 script。 | [方法条目](../by-type/xss.md) |
| Nextcloud deck 引用缓存须在命中路径重新校验用户 | 保存报告描述 ReferenceManager 的 cachePrefix 与用户无关：User1先访问卡片并分享引用，知道 board/card ID 的其他用户可能读到缓存数据。 | [方法条目](../by-type/idor-access-control.md) |
| Node inspector 的 macOS 特殊地址与 local 解析属于版本回归条件 | 截图历史摘要把路由IP修复遗漏关联到 macOS 对0.0.0.0及 ComputerName.local 的解析行为。 | [方法条目](../by-type/desktop-client.md) |
| JavaScript 历史 URL 收集的后缀过滤会遗漏带查询资源 | 保存管道 gau/waybackurls 后按 .js$ 筛选并 anew。 | [方法条目](../discovery/client-and-cloud.md) |
| GHES App scoped token 提权摘要要求已有安装权限 | 保存摘要要求拥有安装 GitHub App 的管理权限，风险是受限 user-to-server token 被错误授权为管理员/组织Owner，不能提炼为匿名提权。 | [方法条目](../by-type/oauth-oidc.md) |
| of-CORs 工具公告不能把网络可达性等同浏览器跨源读取 | 正文只有typosquatting、内网CORS与回传工具的能力声明，未保存实现。 | [方法条目](../by-type/cors.md) |
| 支付设置 JSON 后缀示意只能引出处理器鉴权差异 | 该帖复用已实际审查的admin/user支付设置.json 302→200图片。 | [方法条目](../by-type/idor-access-control.md) |
| MX 工具的 reclaim 日志包含实际注册副作用 | 图中 mx-takeover 使用Mailgun API、16并发和WHOIS，输出 Possible Takeover、reclaimed及domain already exists。 | [方法条目](../by-type/subdomain-takeover.md) |
| usid Cookie 名称不能决定文件读取语义 | 正文只声称Cookie本地文件读，没有保存请求或路径。 | [方法条目](../by-type/lfi-path-traversal.md) |
| database.php.orig 的源码泄漏与浏览器 view-source 分工 | 截图显示.orig备份响应含DB hostname、database、username、password变量，值遮挡。 | [方法条目](../by-type/info-secrets.md) |
| 走私类型图的核心是双方消费的实际字节边界 | 图包括CL.0、CL-CL、CL-TE、TE-CL、TE-TE，分别描述零/忽略长度、重复长度优先与transfer编码识别差异。 | [方法条目](../by-type/request-smuggling.md) |
| 漏洞报告入口 dork 只发现候选政策页面 | 保存查询组合submit vulnerability report、powered by bugcrowd/hackerone并排除news和.de。 | [方法条目](../scope-and-rules.md) |
| APK file 模板匹配 URL 与 Email 需要区分业务及依赖来源 | 图为解包APK静态匹配，路径含libflutter、AndroidX、Room、strings.xml，结果为Email/URL/Firebase info。 | [方法条目](../by-type/mobile-android.md) |
| JSON Unicode 的两张 403 图只能支持过滤层响应差异 | 明文候选返回CloudFront HTML403，编码候选仍403但为JSON UNKNOWN_USER。 | [方法条目](../by-type/waf-bypass.md) |
| GitHub OrgKey 与 UserKey 报告标题不足以确定组合权限 | 帖与图仅描述OrgKey/UserKey/access token泄漏后读取员工或执行API，值和操作细节未保存。 | [方法条目](../by-type/info-secrets.md) |
| robots.txt 扫描报告的 Not-applicable 状态提示内容证据门槛 | 保存图只提供robots语法及索引建议，未给敏感响应，状态Not-applicable。 | [方法条目](../impact-and-acceptance.md) |
| 名字分别过滤后拼接成 HTML 属性必须按最终上下文处理 | 保存两字段示例拼成IMG和onmouseover，后图有xxs弹窗但目标域遮挡。 | [方法条目](../by-type/xss.md) |
| 密码重置帖中的双邮箱正文不是合法 JSON | 原帖写email键后两个未加引号逗号值，不是有效JSON，不能复制成可复现ATO。 | [方法条目](../by-type/authn-session.md) |
| EAR 图实际展示客户端跳转后的初始页面响应 | 图声称EAR但示意admin页面200加载后转/login，view-source仍见内容。 | [方法条目](../source-audit.md) |
| Fuzzable 函数评分须经可达性和崩溃归因验证 | 保存图列函数、地址、评分，11个符号分析、8个跳过。 | [方法条目](../targeted-fuzzing.md) |
| Mattermost Windows 重装保留会话要与卸载及撤销承诺比较 | 截图步骤先正常登录，再卸载重装自动恢复。 | [方法条目](../by-type/desktop-client.md) |
| SSRF 管道候选与 MicroStrategy 专用模板适用性需分离 | 保存图将assetfinder→HTTP探测→gau→gf ssrf送特定模板或10并发curl经代理，并建议Collaborator。 | [方法条目](../by-type/ssrf.md) |
| Markdown 输出保留 IMG 却删除 onerror 是当前反例 | 保存git mode请求包含img onerror，返回HTML保留img src和样式却没有事件属性。 | [方法条目](../by-type/xss.md) |
| WordPress aiowps 文本索引只是配置泄漏定位候选 | 正文重复给出"aiowps_remove_wp_generator_meta_info" filetype:txt及CVE-2022-4346声明，没有保存实际文件或版本验证。 | [方法条目](../by-type/info-secrets.md) |
| 后台代理历史必须区分捕获、等待转发与真实响应 | 获奖帖建议Burp后台运行；Caido图显示跨域多端口Forward队列及Drop/Forward。 | [方法条目](../discovery/records-and-incremental.md) |
| 边做边学应以可观察输入输出和技术模型组织 | 保存帖主张按需学习、输入产生异常输出和理解目标技术，不能继承99.99%成功等夸张概率。 | [方法条目](../hunting-strategy.md) |
| 钱包交易可视化的链上关联不能确定现实身份 | 保存图只示Bitcoin交易与两个发送地址。 | [方法条目](../discovery/passive-and-services.md) |
| GCP SSH 用户名与公钥拼接需检查元数据写入边界 | 图显示ssh.cloud.google的newLinuxUsername值混入编码公钥并带行结束符，未保存授权请求或后端结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| One-liner 的多扫描器并发必须隔离目标和观察证据 | 截图说明rush20工作者SQLmap、Dalfox管道、重定向Location和CRLF；独立工具可能再开并发，应统一总请求预算并按资产/会话/参数保存输出。 | [方法条目](../targeted-fuzzing.md) |
| One-liner 的 Swagger、Host 与 CSP 地址都是候选来源 | 保存另一页包括swagger paths、Host fuzz、recon.dev、跟重定向仅200筛选、历史参数反射和IP映射。 | [方法条目](../discovery/web-and-api.md) |
| AEM Sling 端点清单需按 selector、深度和权限建模 | 保存列表覆盖/system/console、crx/crxde logs、JCR versionStorage、profile、OSGi配置、content query、tidy/infinity、feed及replication/cloudservices。 | [方法条目](../discovery/web-and-api.md) |
| VuCSA 厚客户端练习需要协议和服务端授权证据 | 图明确Java/JavaFX非HTTP实验应用，分类包括buffer over-read、command、SQL、enumeration、XML、水平和垂直访问控制。 | [方法条目](../by-type/desktop-client.md) |
| VuCSA XML 练习中的实体和 XInclude 属于不同解析开关 | 保存XML页提示entities和XInclude可用于实验，但图中只有正常storage request/response。 | [方法条目](../by-type/xxe.md) |
| 高级 IDOR 预览中的负数 sentinel 需证明实际集合授权 | 此帖图片复用此前实际核读的localhost/users/-1管理员集合示意。 | [方法条目](../by-type/idor-access-control.md) |
| Cognito Identity Pool 公共标识与匿名角色权限要分开 | 保存图从bundle定位identityPoolId、userPoolId、clientId和region，并声称匿名临时凭据访问AWS服务。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Cognito SignUp API 开放只在管理员建号业务中构成候选 | 图前提是应用不提供自注册且应由管理员开户，却未禁用SignUp API。 | [方法条目](../by-type/authn-session.md) |
| Cognito 可写用户属性须追踪 AppClient 至服务端权限消费者 | 图列标准attributes并提出提权。 | [方法条目](../by-type/authn-session.md) |
| Cognito email 更新与验证完成需要同一版本状态 | 图展示应用UI禁改email，但本人access-token可调用update-user-attributes。 | [方法条目](../by-type/authn-session.md) |
| ownCloud 外部文件 Activity 的 URI 路径必须约束应用内部存储 | 保存摘要针对ReceiveExternalFilesActivity、第三方组件上传和android.intent.extra.STREAM，指出路径验证不足可读写internal storage。 | [方法条目](../by-type/mobile-android.md) |
| Kubernetes 工具清单覆盖不同审计层而非可运行扫描计划 | 正文只有kube-hunter、kubeaudit、KubiScan、kubesploit、kubernetes-rbac-audit、peirates链接。 | [方法条目](../cloud/container-k8s-security.md) |
| Algolia 发现器输出三字段不能证明 Admin API Key | 正文JS收集去重后运行工具，图只见algoliaIndex、algoliaAppId、algoliaApiKey，值遮挡。 | [方法条目](../by-type/info-secrets.md) |
| Base64 data URI 只承载 PoC 不保证真实浏览器 CSRF | 正文Burp生成HTML→Decoder Base64→data:text/html打开，图为生成入口；另一图localhost GET发送成功。 | [方法条目](../by-type/csrf.md) |
| 上传校验五项需要覆盖处理前后及目标文件身份 | 正文列类型、大小、服务端处理、防覆盖和上传后校验。 | [方法条目](../by-type/file-upload.md) |
| Mattermost deleted_at 输入引起的是频道渲染生命周期异常 | 截图描述发消息时JSON added deleted_at>0、pending_post_id唯一，查看或切换频道白屏，刷新可复现；历史CVE-2021-37863。 | [方法条目](../by-type/business-logic.md) |
| Osmedeus YAML 工作流应锁定阶段输入与实际副作用 | 正文只说明可自定义YAML工作流和签名，并未给流程文件。 | [方法条目](../targeted-fuzzing.md) |
| DNS 重绑定 SSRF 需要确认校验与连接使用不同解析结果 | 正文声称公开IP A换至EC2 metadata B后读到内容，未有原始响应；不要重放该地址。 | [方法条目](../by-type/ssrf.md) |
| 平面备份、导图和表格需要共享稳定证据标识 | 正文按小/大目标建议flat files备份、Xmind、表格。 | [方法条目](../discovery/records-and-incremental.md) |
| Salesforce 密码搜索帖未保存的 2FA 续篇不能补为绕过 | 正文只给GitHub搜索target.my.salesforce.com password，并说登录要求2FA，续篇未保存。 | [方法条目](../by-type/info-secrets.md) |
| Mitaka refang 与第三方检索必须保留原始 IoC | 正文及图为IP/domain/URL/hash右键检索Censys、Shodan等。 | [方法条目](../discovery/passive-and-services.md) |
| chaos 至全端口探测的耗时图不能替代范围与性能预算 | 图把chaos域名结果送naabu -ports full再httpx，多个80/443及非标准端口，约1m29；正文另列Nmap/Naabu/Masscan/Rustscan。 | [方法条目](../discovery/passive-and-services.md) |
| IBM 低中危报告状态不能保证私邀或当前接受口径 | 正文声称大范围及5至10分钟找到漏洞，图仅IBM Tokens & Secrets的Low Triaged和Medium Resolved。 | [方法条目](../scope-and-rules.md) |
| ZoomEye 聚合应保留服务类别与历史 banner 时间 | 正文site:[target].com并进入aggregation，图列Apache、Exchange SMTP、OpenSSH、cPanel、Dovecot、Exim及2023 banner。 | [方法条目](../discovery/passive-and-services.md) |
| Host 提示图复用应追踪具体头被哪一跳消费 | 此帖复用已实际审查的Host/转发/IP头提示图；各头名称并非同义。 | [方法条目](../by-type/host-header.md) |
| AVIator 界面可辨认样本用途却不证明免杀有效 | 保存图列AES/IV、shellcode输入、架构和线程/进程注入选项，是二进制生成工具界面；未保存实现、检测对照或运行证据。 | [方法条目](../source-audit.md) |
| 邮箱连续变更后旧验证令牌不能恢复过期绑定 | Mattermost截图描述从A改B获验证链接，后改C并验证C，旧B链接仍能改变账户绑定。 | [方法条目](../by-type/authn-session.md) |
| 邀请链接展示邮箱与 token 的权威主体不得错配 | 保存图为 signup_user_complete 的d参数含email/display_name/name，t为邀请token；删空email后的完整接管步骤未见。 | [方法条目](../by-type/authn-session.md) |
| 邀请撤回、提醒重发和消费需使用同一有效状态 | 标题讲撤销后Reminder，截图实际描述没有取消邀请入口且旧邮件可加入，二者证据不能混合。 | [方法条目](../by-type/authn-session.md) |
| 邀请邮件自定义 message 的 HTML 注入与 ATO 应分开 | Mattermost图给guest邀请自定义message插入a/input并在邮件呈现，另一帖只有email-template外链题名。 | [方法条目](../by-type/xss.md) |
| Swagger 外部 configUrl 与旧版 HTML 呈现需要 sink 证据 | 保存JourneyAPI图主要timeline，InDesign标题含configUrl={site}，未见完整配置及执行。 | [方法条目](../by-type/xss.md) |
| SICOM console 路径可达要比较未认证实际功能 | 正文Shodan ssl/org筛选并访问/~sicom/mgrng/index.phpa，图只有报告title与severity。 | [方法条目](../by-type/idor-access-control.md) |
| 归档重定向管道需保持完整 URL 并逐参数对照 | 一帖修改redirectTo由linkedin至自定义外部域，另一管道gau→tee -a archive→gf→cut冒号→qsreplace→httpx Location。 | [方法条目](../by-type/open-redirect.md) |
| 子域词表小写去重适用于 DNS 标签但不替代路径字典 | 正文说明合并SecLists/Assetnote子域词表为小写并排序，未保存下载内容。 | [方法条目](../targeted-fuzzing.md) |
| Kscan 私网截图仅支持服务指纹候选 | 图显示/24资产SSH、SMB、FTP、HTTP与多产品识别，没有漏洞复现。 | [方法条目](../discovery/passive-and-services.md) |
| HaE 正则高亮只提高候选可见度 | 正文说明自定义regex匹配高亮，没有规则实现。 | [方法条目](../discovery/records-and-incremental.md) |
| ffuf mc all 与 ac 校准不能保证隐藏端点都被保留 | 正文ffuf -mc all -ac配OneListForAll，未保存实际命中。 | [方法条目](../targeted-fuzzing.md) |
| 账号删除后公开 profile 残留需要按数据与时间比较 | 正文建议删号后查公开profile，截图只有报告标题与奖励。 | [方法条目](../by-type/info-secrets.md) |
| XSSHunter Discord 通知需要绑定输入和实际执行来源 | 图为W3Schools tryit的payload fired通知，不能作为真实目标漏洞；Discord只为通知渠道。 | [方法条目](../by-type/xss.md) |
| GraphQL 风险清单需按 resolver 数据流而非类别名确认 | 正文列normalization、DoS、SQLi、auth、introspection、CSRF及errors。 | [方法条目](../by-type/graphql.md) |
| PURGE 管理方法是否失效缓存需真实前后证据 | 保存Yelp图声称匿名PURGE，实际可见部分仅GET200、AmazonS3/varnish和cache hits，状态Informative。 | [方法条目](../discovery/web-and-api.md) |
| KAYAK deeplink 摘要只给历史会话泄漏风险与版本 | 图称Android161.1恶意deeplink可窃session，161.2初修；未保存handler或URI链。 | [方法条目](../by-type/mobile-android.md) |
| GraphQL aggs 必须在聚合前应用相同可见性约束 | 保存报告search与opportunities_search的aggs参数/返回字段可暴露private program handles。 | [方法条目](../by-type/graphql.md) |
| 任意搜索参数生成 hidden input 时 name 与 value 都是不可信 | 图描述主搜索附加任意参数后生成hidden input的name/value，未见完整后续执行片段。 | [方法条目](../by-type/xss.md) |
| Shodan 服务 dorks 与 favicon 指纹不决定目标归属 | 正文给mongo-express cookie/200、MySQL3306、Elasticsearch9200、PostgreSQL5432、BIG-IP标题、favicon和UA标识。 | [方法条目](../discovery/passive-and-services.md) |
| 钱包抓取声称与截图的固定 SFTP 文件读取不是同一能力 | 图中Paramiko代码要求显式SSH主机/用户名/密码，只读取固定路径.dat，不含发现钱包、提取seed或无凭据远程访问。 | [方法条目](../source-audit.md) |
| 信息泄漏定义需要落到未经授权的具体字段和消费者 | 保存正文定义敏感信息被未授权方访问，但未保存areas续篇。 | [方法条目](../by-type/info-secrets.md) |
| WordPress 视频截图的扫描和密码字典不能证明 Blind SSRF 或 DoS | 图列WPScan API情报/用户枚举、密码字典和wp-cron/DoS工具，却没有DNS重绑定解析或耗尽证据。 | [方法条目](../impact-and-acceptance.md) |
| 历史参数热度词表需要保留目标上下文和低频样本 | 正文与图为gau→unfurl参数→按流行度排序的定制字典。 | [方法条目](../targeted-fuzzing.md) |

| 泄漏入口关闭与凭据失效分别确认 | 帖子提示已泄漏凭据可能在修复后仍有效。 | [方法条目](../by-type/info-secrets.md) |
| 限流变体必须保持业务身份与计数器对象 | 保存图片列出 IP 头、User-Agent、cookie 和编码变体，但这些输入未必参与限流计数。 | [方法条目](../by-type/authn-session.md) |
| SQL 自动检测的错误与时序输出保留候选级别 | Ghauri 图含 MSSQL 参数 id 的布尔/时间检测与数据库枚举提示；SQLiDetector 使用 14 个载荷和 152 个错误模式。 | [方法条目](../by-type/sql-injection.md) |
| 登录参数的反射需要定位实际语法上下文 | 图片中的 admin 登录 perspective 参数与正文中的 GlobalProtect user 参数都提供了候选入口；保存材料未建立通用的执行结论。 | [方法条目](../by-type/xss.md) |
| GraphQL 目录转换为解析器和操作权限检查表 | 保存目录和正文覆盖查询/变更、参数、变量、内省、错误、数据库注入和鉴权。 | [方法条目](../by-type/graphql.md) |
| GraphQL 分页与放大量以实际资源预算核验 | 目录提到 pagination、wildcards、较少输入、DoS 和 amplification，但没有实测阈值。 | [方法条目](../by-type/graphql.md) |
| 授权请求字段与服务端授予能力分开审计 | 截图包含 authorize 的 clientId、PKCE S256、scope、nonce 和 cookie，正文强调服务端验证 token；未保存取得管理员能力的响应。 | [方法条目](../by-type/oauth-oidc.md) |
| 多次解码的 DOM 字符数据与再次解析边界 | 正文声称 %26lt; 先变成 &lt; 再成为 <。 | [方法条目](../by-type/xss.md) |
| 已有 Aliyun 凭据的列桶与对象权限分离 | 正文与替代文字明确先配置 aliyun 凭据，再用 oss ls 列可访问桶及桶内容；截图有 Size、ETag 与 Region。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 排除 CDN 标签不能确立端口探测归属 | 帖子将 cf-check 输出接入 naabu，保存图仅是封面，没有工具实现。 | [方法条目](../discovery/passive-and-services.md) |
| 角色矩阵以动作和对象所有权建立双向对照 | 图片用 Admin、HR、Printer 与 No/Only own/Yes 描述读、编辑、删除、创建文档和打印动作。 | [方法条目](../by-type/idor-access-control.md) |
| Katana 字段提取与浏览器爬取的来源记录 | 保存命令使用 js-crawl、深度 5、headless 和 field endpoint 接入 anew。 | [方法条目](../discovery/client-and-cloud.md) |
| E2E 标题与 Axios 回调图的消费者证据分层 | 截图有 Axios 的 url/baseURL、headers、withCredentials，以及 DNS/HTTP Collaborator 记录。 | [方法条目](../by-type/ssrf.md) |
| 范围确认前置到盲回调与每个后续动作 | 正文描述深挖后才发现域名超范围或项目停止，另一帖的盲 XSS 通知明确来自超范围域名。 | [方法条目](../scope-and-rules.md) |
| URL 变体按实际消费者的解析结果比较 | 保存清单混合斜杠、反斜杠、userinfo、注释、控制字符编码和全角斜杠。 | [方法条目](../by-type/open-redirect.md) |
| favicon 相似性、IP 归属和端点响应三段核验 | 图中以 Shodan org 与 favicon hash 得到 IP:port，再用 ffuf 及 Spring Boot 词表保留 200。 | [方法条目](../discovery/passive-and-services.md) |
| 敏感路径字典按技术、权限和响应证据缩小 | 保存词表包含 API/admin、环境配置、数据库备份、phpinfo、package、Swagger/WADL 和版本路径；另帖建议在子域复查。 | [方法条目](../by-type/info-secrets.md) |
| JS 端点到未授权模块需验证对象与操作 | 正文链为 JSLinkfinder→排序→FFUF→发现未授权模块，但没有请求和对象证据。 | [方法条目](../by-type/idor-access-control.md) |
| 云存储 dork 的公开资料反例与索引语法 | 保存正文和替代文字包含 s3.amazonaws.com、blob.core.windows.net、googleapis.com、drive.google.com 的 site 条件，部分正文还嵌入 http://，需先核对检索语法。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Shodan 子域候选保留索引时间与 API 额度 | shosubgo 图展示返回域名以及 API credit 余额，密钥已遮挡。 | [方法条目](../discovery/passive-and-services.md) |
| 注入转发头的 301 输出不能确认服务器请求 | 保存工具图批量显示头变体与 Code 301。 | [方法条目](../by-type/ssrf.md) |
| 并发 curl 的响应数与业务原子性分别验证 | 命令用 100 次循环和 xargs -P 25，curl 跟随重定向且丢弃正文，只保留状态码和大小。 | [方法条目](../by-type/business-logic.md) |
| S3 指纹、列表和匿名读写分成不同候选 | 正文宣传 S3Scanner 与导出内容；另一图用 httpx 的 AmazonS3 标识或 AccessDenied 筛选。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| ASP.NET 重复参数的过滤和聚合行为需同版本对照 | 已核读的重复图片声称将 XSS 字符串拆为多个同名参数，ASP/IIS 在应用侧拼接。 | [方法条目](../by-type/waf-bypass.md) |
| 重置邮件 URL 的选择器与授权 token 分离 | 已核读的重复图片描述 email/url 基线、改变 host 后为空以及目标域后缀进入重置邮件，但没有邮件交付或接管交换。 | [方法条目](../by-type/authn-session.md) |
| 预发布注册、邮箱验证与管理员资格的身份边界 | 已核读的重复图片叙述 stage 注册未验证邮箱，使用 maintainer 邮箱取得 admin 并声称可见大量 PII；没有实际请求/响应。 | [方法条目](../by-type/authn-session.md) |
| WordPress pingback 的两 URL 与请求阶段区分 | 保存 XML 为 pingback.ping 并含两个 URL。 | [方法条目](../by-type/ssrf.md) |
| Grafana avatar 历史 DoS 字符串保留版本和故障证据 | 正文给出 Grafana 7.0.1 的 avatar 路径及 printf/this.Url 模板样式，但没有请求结果。 | [方法条目](../discovery/web-and-api.md) |
| SQL 风格参数名与查询值按真实解析链追踪 | 一帖把含 sleep 的字符串放在 name[...] 参数名，另一帖出现 q=SELECT…WHERE board.id 的请求值。 | [方法条目](../by-type/sql-injection.md) |
| gf 候选链保留查询参数和每阶段真实输入 | 已核读重复图片将 gau、去 query、正则、fff 200 输出和 gf_secrets 连成链，但末段循环没有明确目录/stdin 绑定。 | [方法条目](../by-type/info-secrets.md) |
| 信用卡 canary 的告警与实际资金行为区分 | 保存截图介绍唯一卡号、拒绝所有交易并告警的 canary。 | [方法条目](../discovery/records-and-incremental.md) |
| 遍历以允许文件根和实际消费者为边界 | 正文把越出 web root 定义为遍历，图示用 file=../etc/passwd。 | [方法条目](../by-type/lfi-path-traversal.md) |
| zip wrapper 的读取与 PHP 解释执行前提 | 正文及已核读重复图片将上传 zip、zip:// 与 LFI→RCE 联系起来。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 历史报告数量不能代替增量资产和方法复查 | 正文以旧项目已有 1600 多报告仍可获奖为例，保存图片仅有报告标题、状态和奖励，未提供漏洞实现。 | [方法条目](../hunting-strategy.md) |
| JavaScript 变量名不是已接受的 GET 参数 | 图中链路采集 URL、取响应、用正则抓 var 声明，再追加 =xss 构造请求。 | [方法条目](../discovery/client-and-cloud.md) |
| 静态 fuzz 排名保留跳过项和版本语境 | Fuzzable 图含 fuzz-friendly、risky sinks、loops、cyclomatic complexity 和 coverage；两次分析有不同 skipped 数及排名。 | [方法条目](../targeted-fuzzing.md) |
| 相同会话标识图必须补足获取与生命周期前提 | 保存图用相同 PHPSESSID 表示攻击者取得会话，但没有展示如何取得。 | [方法条目](../by-type/authn-session.md) |
| HTML 内容控制与脚本执行及钓鱼影响分层 | 保存图描绘 HTML 注入后的伪登录表单，只说明内容控制的一种可能影响。 | [方法条目](../by-type/xss.md) |
| 本地 shell 展开不是远程命令注入证据 | 教材图展示应用输入进入 shell，另一图用引号、反斜杠、ANSI-C/十六进制及 glob 在本地读 passwd 并出现目录错误。 | [方法条目](../by-type/cmd-injection-rce.md) |
| GitHub 搜索命中需核对组织归属和秘密用途 | 正文给出 payments/config_formal.json 路径、Code/Recently Indexed 筛选；已核读 GitHound 图强调人工确认。 | [方法条目](../by-type/info-secrets.md) |
| 成功 compose 页面须补足跨站浏览器与终态 | 两张保存图仅显示 localhost GET compose 成功，正文则给出一般 CSRF 定义。 | [方法条目](../by-type/csrf.md) |
| 客服盲 XSS 从采样标记到真实 sink 与披露权限 | 正文建议在联系表单/客服中到处投送，截图的奖金邮件却明确限制公开漏洞细节。 | [方法条目](../by-type/xss.md) |
| Base64 文件参数比较必须保持同一规范路径 | 正文的原始 f=etc/passwd 与编码 f=L2V0Yy9wYXNzd2Q= 并不只差编码：后者解码为带前导斜杠的 /etc/passwd。 | [方法条目](../by-type/lfi-path-traversal.md) |
| sed 与 gron 的离线数据变换保留原始结构 | 保存教程覆盖 sed 的替换、捕获组、global 与锚点，以及 gron 展开 JSON 路径再重建。 | [方法条目](../discovery/records-and-incremental.md) |
| 反馈链接的 scheme、导航与 opener 分别检查 | Slack 图展示反馈 POST、crumb 与 path 字段的 javascript/外部链接候选，window.opener 后续代码未完整保存。 | [方法条目](../by-type/xss.md) |
| 实验室单一上下文训练与真实项目授权衔接 | 正文建议选一种 Web Security Academy 主题、完成实验、理解答案并构建工具或应用；图为未编码 HTML 反射实验入口，没有实际解答。 | [方法条目](../hunting-strategy.md) |
| 响应链接与截断 bookmarklet 的静态候选清洗 | LinksDumper 图同时出现相对端点和 Textarea/body/head 等 HTML 碎片；bookmarklet 只保存 script 标签枚举与正则开头，横向代码截断。 | [方法条目](../discovery/client-and-cloud.md) |
| IP、Host 和 Proto 转发头按信任链与消费者分流 | 两张图混合 XFF、X-Real-IP、CF/Fastly、X-Host、Forwarded-Host/Server/Proto 和多个 Host 变体。 | [方法条目](../by-type/host-header.md) |
| JS 文件名、注释与运行时密钥来源分级 | 保存 JS 词表含 config/credentials/secrets/session/crypto/hash/salt/nonce/permission，另一图有 FETCHBUCKETS、objId 与空的 accesskey/secretkey，遮盖值位于注释。 | [方法条目](../by-type/info-secrets.md) |
| 历史调解建议转为有证据的报告时间线 | 正文说报告四个月后才被 triage，并建议经平台支持调解；图只有严重性/状态列表，没有漏洞实现。 | [方法条目](../reporting.md) |
| IPv4 映射 IPv6 必须先统一地址族再判断范围 | 保存摘要描述 ::ffff:127.0.0.1 和 ::ffff:10.0.0.1 在历史 Go 判断链中的问题。 | [方法条目](../by-type/ssrf.md) |
| Wayback 私有报告表单索引不授予项目资格 | 正文与图以平台域名的历史 URL 找 /rd 表单和 UUID。 | [方法条目](../scope-and-rules.md) |
| AppLocker Allow 事件需要主体、模式和拒绝对照 | 保存图显示脚本 8005、DLL 8002 等 Allow 事件，未展示时间、用户、规则或 audit/enforce 模式。 | [方法条目](../by-type/desktop-client.md) |
| 子域枚举参数与采集来源不能互换 | 保存图列 subfinder all、amass passive/norecursive 配置和 assetfinder subs-only。 | [方法条目](../discovery/passive-and-services.md) |
| 模板算术指纹与危险能力不能连跳 | 保存脑图从 7*7、闭合形式及 Smarty/Mako/Jinja/Twig 识别，延伸到对象、函数、文件/RFI/RCE。 | [方法条目](../by-type/ssti.md) |
| Theia WebView 的 postMessage 接收链保留截断限制 | 保存 Theia/CVE-2021-41038 图包含启用 WebView 的条件、window.open/postMessage、channel/content/args/options，但未保存完整 sink 与校验。 | [方法条目](../by-type/xss.md) |
| Notebook 域名可见性与编辑权限分别验证 | 另一保存图描述 notebook 子域经 Referer 或 viewer 可见，并声称 viewer 能成为 editor。 | [方法条目](../by-type/idor-access-control.md) |
| XSS 变体清单以语法上下文和编码阶段拆分 | 保存 26 条清单混合 onclick、SVG、onerror、百分号/实体/TAB、javascript、iframe srcdoc、多反射和模板表达式。 | [方法条目](../by-type/xss.md) |
| 失效社交链接的可认领性与受信任展示分开 | 正文说支持页的 Facebook/社交链接失效，建议建账户并证明影响；图只见奖励。 | [方法条目](../by-type/subdomain-takeover.md) |
| 侦察脑图按证据来源和阶段预算落地 | 已核读重复脑图将域来源、子域、HTTP/端口、关键词、dork、Wayback、JS secret、fuzz 与手工串联。 | [方法条目](../discovery/records-and-incremental.md) |
| AD 账户风险指标与有效凭据权限分层 | DC-Sonar 图含域/用户、reused passwords、weak/no-expire 与时间字段，但没有密码/hash 来源或实际权限。 | [方法条目](../by-type/desktop-client.md) |
| 盲回调面板的容量与客户端 IP 来源核验 | 正文报告大量 fires 时页面不加载及 IP 一直为 127.0.0.1。 | [方法条目](../discovery/records-and-incremental.md) |
| OPRF 退化随机值先在协议实现和自有样本中约束 | 保存挑战说明使用易猜/很小的 OPRF 值，例子为零，导致离线攻击，并强调安全随机数。 | [方法条目](../by-type/authn-session.md) |
| byp4xx 线程模式与限速模式按实际选项核验 | 正文描述 Go、文件输入和 goroutine/semaphore，保存帮助明确启用 threads 会关闭 rate limit，rate 模式单线程、默认 5 请求每秒。 | [方法条目](../targeted-fuzzing.md) |
| CORS 响应读取权限与服务认证分开建模 | 保存正文定义以响应头指定允许来源，图只有封面。 | [方法条目](../by-type/cors.md) |
| 旧子域列表与模板 Loaded 都只是接管候选 | 一帖建议复用旧子域清单，已核读重复图是 chaos→dnsprobe→httprobe→nuclei takeover，只有 Loaded 输出。 | [方法条目](../by-type/subdomain-takeover.md) |
| CMS 扫描版本、公开文件与旧 CVE 候选分级 | 正文及替代文字列 WordPress/Joomla/Drupal/Moodle，图为本地 WordPress 4.9.1 的旧扫描结果，含安全头、xmlrpc、公开 README/LICENSE、用户名及 EDB 候选。 | [方法条目](../discovery/web-and-api.md) |
| GitHub App 的仓库 scope 与组织 Project V2 权限分离 | 保存摘要描述 Scoped-User-To-Server token 可操作 GraphQL 组织用户/项目等非仓库资源，同时明确仓库内容、issues/pulls 不受同一问题影响。 | [方法条目](../by-type/oauth-oidc.md) |
| 盲 XSS 扩展的改头范围与变换来源显式记录 | 图中扩展为 OFF，可添加不存在的头，并对 User-Agent、Referer、XFF、Origin 做编码和随机化。 | [方法条目](../by-type/xss.md) |
| 好友可见视频的投票动作继承对象访问资格 | 保存摘要声称知道 vote_id 就能对 Friend Only 视频投票。 | [方法条目](../by-type/idor-access-control.md) |
| Drive 关键词采集保留每个响应的独立出处 | 保存脚本将多个 curl 响应追加到同一文件，再搜索 drive.google、docs.google 与 document/spreadsheets 路径；命中示例是 /uc?export=view&id= 引用。 | [方法条目](../discovery/records-and-incremental.md) |
| BlueHound 逻辑路径与网络和会话前提交叉验证 | 图列 Logical Paths、Network Enabled Paths、域管理员会话、Kerberoastable 用户、Crown Jewels 与 Ransomulator。 | [方法条目](../by-type/desktop-client.md) |
| 历史 JSP 登录线索与时间差需当前消费者对照 | 正文链为 dork→JBoss→Wayback CDX→JSP 登录→username 的 WAITFOR delay。 | [方法条目](../by-type/sql-injection.md) |
| 邀请表角色空值和取消动作按租户状态验证 | 保存图只有 Email/User Access/Expires/Cancel Invite，部分角色栏为空，没有跨对象请求。 | [方法条目](../by-type/idor-access-control.md) |
| JS 词表的 POST 探测需真实方法、正文和错误页基线 | 正文建议从 JS 取端点、随意构造 POST 参数再交 dirsearch；图用 raw 请求、25 线程、147 条词表并排除 300–599，只展示 200/长度。 | [方法条目](../targeted-fuzzing.md) |
| 双因素重试不能把待验证会话提升为已认证 | 保存 9to5Google/Newswav/pplware 段落描述 TikTok Android/Web 多次重试后跳过第二因素；Android Police 仅有标题且称已修复。 | [方法条目](../by-type/authn-session.md) |

| 数字零地址的解析和连接语义按实际栈验证 | 保存图声称 http://0 在 Linux 被解析为 0.0.0.0 并访问本机，其他表示被拒而该形式返回 200。 | [方法条目](../by-type/ssrf.md) |
| Jira 信息接口的匿名权限与未保存执行链分离 | 保存 Jira 摘要列 project categories、resolutions 和 usernames 的未认证可见性，标记 JRASERVER-73060/CVE-2020-14179，并声称另外两个服务可组合至内网 RCE。 | [方法条目](../by-type/info-secrets.md) |
| 搜索执行叙述与异源 cookie 影响分别核验 | 保存报告写搜索栏插入 script 后弹窗，并声称可借其他站点 CORS 获取 cookie/token。 | [方法条目](../by-type/xss.md) |
| prefixRank 属性事件候选需实际 DOM 和交互条件 | 图有表单 POST customer.cfm、prefixRank 参数及 accesskey/onclick 片段，包含被遮挡目标及会话。 | [方法条目](../by-type/xss.md) |
| xAPI 的 file 查询与浏览器可发请求条件分开 | 报告标题写 URL path，但保存 URL 为 statements?file=…，并要求添加 Basic Authorization 和 X-Experience-Api-Version:1.0.1。 | [方法条目](../by-type/xss.md) |
| Memory 隐私写动作以稳定所有权为授权边界 | TikTok Now Android 摘要称可修改他人 Memory 的 Who Can View。 | [方法条目](../by-type/idor-access-control.md) |
| Ads 输出编码根因与 WAF 或接管声称分层 | TikTok Ads 保存摘要明确为用户输入反射缺少适当 HTML escaping/output encoding，称 2022-09-07 已修复；另一叙述称 Akamai 绕过与任何账户接管。 | [方法条目](../by-type/xss.md) |
| 身份资料变更使验证资格绑定到资料版本 | EXNESS 图描述验证后 /kyc_back/api/v2/surveys/personal_info 可改 Name、DoB、Address，GUI 却禁止。 | [方法条目](../by-type/business-logic.md) |
| 身份文档与申报资料的对应关系独立检查 | 同一截图还描述使用不对应姓名/地址的文档完成验证，与验证后资料可改是两个问题。 | [方法条目](../by-type/business-logic.md) |
| 过期社交链接的修复回执不证明外部资源认领 | 8x8 摘要称发现过期社交链接并修正，标题写 Instagram takeover，但图没有可认领证明。 | [方法条目](../by-type/subdomain-takeover.md) |
| SSTImap 请求选项与文件或 shell 能力分别限界 | 保存 SSTImap 1.0.2 帮助列 URL、交互、marker、data/header、engine/technique 及文件和 shell 选项，没有实际检测输出。 | [方法条目](../by-type/ssti.md) |
| 侦察搜索名录按数据类型与第三方提交边界分类 | 保存脑图把证书、服务、代码、攻击面、威胁情报、邮箱及 Wi-Fi 搜索混列，例如 crt.sh、Shodan/Censys、grep.app、urlscan 与 hunter。 | [方法条目](../discovery/passive-and-services.md) |
| CMS 与查询参数 dork 只产生有范围的索引候选 | 保存清单包含 admin-ajax、Drupal/user、Joomla/login 以及 q/s/search/query/lang/keyword；图片命中博客和 Yahoo，而非证明当前组件或 XSS。 | [方法条目](../discovery/web-and-api.md) |
| 邮箱注释语法与注册资格使用同一规范身份 | 正文混括号注释、分号、加号和白名单域名，注册图仅显示非 WUR 邮箱被拒绝。 | [方法条目](../by-type/authn-session.md) |
| 邮箱模糊输入按独立 sink 分解检查问题 | 图将邮箱的 HTML/引号/注释、模板算术、SQL、回调域、重复字段及 CRLF/RCPT TO 混在一起。 | [方法条目](../source-audit.md) |
| 多工具侦察管线保留输入类型与单次快照 | 图链为 subfinder/amass→tee -a→filter-resolved→指定 HTTP 端口→Wayback→kxss。 | [方法条目](../discovery/records-and-incremental.md) |
| 上传文件名的路径、SQL、HTML 与 shell 消费者分流 | 图把目录片段、SQL 延迟、SVG 事件和 shell 分隔符放在文件名。 | [方法条目](../by-type/file-upload.md) |
| PHP raw-byte 短码需要解释执行与输入来源前提 | 正文称 19 字节非字母数字 reverse shell，图只见原始字节、变量/参数与反引号的短码示意及 id 注释。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 第三方代码托管和文档扩展检索保留公开用途反例 | 保存 dork 联合 paste/code/trello 平台与目标关键词，另帖列 doc/docx/ppt/csv 等扩展。 | [方法条目](../by-type/info-secrets.md) |
| absolute-form 与 Host 的重置邮件 authority 一致性 | 图中正常 origin-form 请求生成本站重置 URL，改变 Host 为外域后 404；absolute-form 指向本站而 Host 外域的组合则声称产生外域邮件链接。 | [方法条目](../by-type/host-header.md) |
| 被过滤函数名与实际执行 sink 不可混同 | 正文建议 alert 被拦后用 confirm/prompt/eval/write。 | [方法条目](../by-type/xss.md) |
| OWA 工具的 401 与空值错误保留为失败证据 | 保存 MailSniper/PowerShell 图要求凭据，返回 HTTP 401 并出现 null method 错误，没有成功会话。 | [方法条目](../by-type/authn-session.md) |
| 账户接管清单以邮箱验证和稳定主体建模 | 已核读重复图片及两张新图列重置多 email/bcc/重复字段或响应 token、社交登录手填邮箱、修改密码/邮箱、重复注册/手机关联邮箱。 | [方法条目](../by-type/authn-session.md) |
| 成员移除后邀请复用需证明重新授予能力 | 三帖组成创建组织→邀请自有用户并接受→管理员移除→再打开旧邀请链接。 | [方法条目](../by-type/idor-access-control.md) |
| 强制解码 YARA 匹配保留原始字节与偏移 | Yaralyzer 图对 53 字节、1195–1250 偏移的匹配展示 raw/HEX、多编码置信度、强制解码和 UTF-16/32 失败。 | [方法条目](../discovery/records-and-incremental.md) |
| ASP 仅拒绝 asp 后缀不能代表安全上传 | 保存 C# 代码使用 HasFile、GetExtension/ToLower，仅拒绝 .asp，其余直接 SaveAs 到 uploads。 | [方法条目](../by-type/file-upload.md) |
| 上传保存路径、覆盖与错误回显单独核验 | 同段代码将用户 FileName 与 MapPath 目录 Path.Combine 后 SaveAs，并把 ex.Message 回显。 | [方法条目](../by-type/file-upload.md) |
| Loofah SVG data MIME 案例保留版本和配置条件 | 保存摘要列 Loofah >=2.1.0 且 <2.19.1、CVE-2022-23515，并称升级 >=2.19.1；特定配置可经 SVG use 绕过 HTML sanitize。 | [方法条目](../by-type/xss.md) |
| PHP 源码返回以内容而非 200 或版本指纹确认 | 三张图展示 phpinfo.php 后附第二 GET/空行，响应 19 字节为 PHP 原文而非执行结果，Connection:close。 | [方法条目](../by-type/info-secrets.md) |
| PHP 复用请求状态的扩展名与路径必须同代际 | 保存根因说明第二请求 vpath=/、无 index 时 request.ext=NULL，但 request.path_translated 仍指向第一请求 PHP 文件；扩展名检查第二请求，而静态读取打开第一请求路径，is_static_file=1 导致返回源码。 | [方法条目](../source-audit.md) |
| 结构化范围提取保留规则与提交资格两条维度 | 图用 HackerOne API 的 handle/structured_scopes、eligible_for_submission 和 eligible_for_bounty，再把 asset_identifier/instruction 拼接、去引号、转小写和抽域。 | [方法条目](../scope-and-rules.md) |
| JS 秘密字段名与公开标识、占位及受众区分 | 图列 config/credentials/auth_tokens/access_tokens/certificates/nonce 等路径，正文另给 accessToken、oauth_token 关键词。 | [方法条目](../by-type/info-secrets.md) |
| 默认账户提示先对应组件和真实服务能力 | 正文分别给 guest/guest 与 Maximo SaaS 文档中的默认集成账户，保存图只有报告列表。 | [方法条目](../by-type/authn-session.md) |
| PDF 与打印导出继承原业务对象的权限 | 正文给 /node/<id>/printable/pdf，另一图描述 printApplication?id 换顺序编号后返回他人申请信息。 | [方法条目](../by-type/idor-access-control.md) |
| JWT 与故意脆弱 API 的训练保持实验边界 | 正文提到 JWT 实验与 Capital 的故意脆弱 API/CTF。 | [方法条目](../hunting-strategy.md) |
| Xssor 的反射检查与浏览器执行分别确认 | 正文说明 Go 版 Xssor 检查载荷在源码的反射，并强调速度与重复 URL 跳过；后帖只是发布 writeup。 | [方法条目](../by-type/xss.md) |
| 登录、筛选和重置输入先追踪实际查询构造 | 正文列 login/filter/forgot-password 入口和 Shodan 线索，另帖给 SQL 注入定义，但没有具体原始请求。 | [方法条目](../by-type/sql-injection.md) |
| 关联子域与公开报告状态不能覆盖范围排除 | JetBlue 图给 logoff 的 redirecturl 候选，并保存回复：未明确列入范围的 connected services 不授权，报告被设为 Informative。 | [方法条目](../scope-and-rules.md) |
| 车机键盘快捷键的可用性只在隔离台架验证 | 正文提到某些 HU 因 CTRL+ALT+DEL 关闭，但未给车型、版本、连接条件或响应。 | [方法条目](../by-type/desktop-client.md) |
| 理解修复须说明改变的安全不变量和反例 | 正文强调不了解修复就不了解漏洞。 | [方法条目](../experiment-design.md) |
| 报告接收、重复判定与奖励资格分开记录 | 四封保存历史回信分别欢迎报告但不提供报酬/感谢信、仅高质量报告考虑认可，以及两个 duplicate/已跟踪回复。 | [方法条目](../impact-and-acceptance.md) |
| 历史 JS 搜集与实际秘密验证保留同一出处 | 正文链为 Wayback/gau→httpx 选 JS→人工/模板/浏览器扩展，图仅有严重性、评分和 Closed 流程。 | [方法条目](../discovery/client-and-cloud.md) |
| 字典生成比例不代表技术覆盖或命中质量 | 正文称字典 70% 来自 ChatGPT、30% 来自他人，图仅为仓库卡，没有保存词条。 | [方法条目](../targeted-fuzzing.md) |
| compose 的 GET 成功页不证明跨站会话操作 | 保存图是 localhost compose GET 的 msg/rID/action/confirm/csrf=1 与成功提示，没有跨站浏览器、cookie 或终态。 | [方法条目](../by-type/csrf.md) |
| 已有 forwarded shell 会话与获取执行入口分离 | DFShell 帮助称连接/FIFO 已建立，列枚举、host/port scan、文件上下传、提权与退出删文件，终端为 www-data。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 控制字符与双向文本按解码后的消费者分别判断 | 正文列 %0a%0d、%09、%00、%e2%80%ae。 | [方法条目](../by-type/waf-bypass.md) |
| 从 httpx IP 到全端口扫描保留归属和格式边界 | 图将 httpx -ip 输出用 awk/sed 取第二字段去括号，再逐项 sudo masscan 0–65535，未显示速率与范围检查。 | [方法条目](../discovery/passive-and-services.md) |
| 反射参数候选与对象选择器的服务授权分开 | 正文说手工找到多个 IDOR，并用 Reflection 扩展发现更多参数，图只有奖励。 | [方法条目](../by-type/idor-access-control.md) |
| uploads 索引和 backup 线索不自动代表私密内容 | 正文建议检查 wp-content/uploads 与 backup zip/tar，图只有敏感文件标题/High。 | [方法条目](../by-type/info-secrets.md) |
| OpenSSH 枚举脚本全命中需已知不存在对照 | 保存图把 CVE-2018-15473 工具的多个 found 与 OpenSSH 8.4p1/Debian 指纹放在一起，还提示 OS 猜测条件不佳。 | [方法条目](../by-type/authn-session.md) |
| 弹窗和 javascript 书签排除本地主动执行反例 | 一图只有页面 alert1，另一回复解释地址栏/书签执行 javascript 与 void(0)。 | [方法条目](../by-type/xss.md) |
| 敏感业务流程用合成测试资料发现接口 | 图建议使用所有功能，尤其要求 PFI/PII/银行卡的功能，可能出现漏测 API。 | [方法条目](../discovery/web-and-api.md) |
| 嵌入 URL 的回调文本必须绑定真正 shell 来源 | 正文在 URL 后放反引号 whoami，图有 DNS/HTTP HEAD 及 uid/gid/groups 字符串，格式与正文示例并不一致。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 多步表单的状态与反射请求逐步绑定 | 正文建议从真实表单流程开启 Intercept，到出现反射的请求再修改，图只见代理输入片段。 | [方法条目](../by-type/xss.md) |
| SOA 与 NOERROR 空答案不能作为子域存活判据 | 保存 dig A 的 unc.mil 为 NOERROR、ANSWER0 和 authority SOA，www 则返回 CNAME→CDN→A。 | [方法条目](../discovery/passive-and-services.md) |
| SVG 从 data 到 blob 的 origin 与打开方式分离 | Shopify 摘要称富文本 data SVG 被转成 blob，修复避免该转换；报告明确普通 img 不运行其中脚本，而打开图片后会执行。 | [方法条目](../by-type/xss.md) |
| Windows 绝对路径响应需核对实际文件系统与预期受众 | 两张 cloudbrowser 图对 /c:/Windows/.../hosts 与 setup.etl 返回 200、默认 HOSTS 样例及二进制正文，标题却直接归因 IIS。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Importer 共享会话不得扩大另一应用的员工权限 | 保存步骤为自有 Shopify admin 装 Judge.me 与 AliExpress Importer，新增评论，给 staff 仅 importer 权限，再打开 importer 建立 Judge.me session 并访问评论入口；后续 URL/结果裁切。 | [方法条目](../by-type/idor-access-control.md) |
| 公开资料 data HTML 链接的执行与站点权限分层 | 图在产品描述放 data:text/html;charset=utf-7;base64 链接，称点击后运行；Base64 是编码，声明 charset 不保证浏览器采用它。 | [方法条目](../by-type/xss.md) |
| 邮件预览的嵌入策略与 self-XSS 跨用户条件分离 | 图描述 image URL 引号/事件产生 self-XSS，应用的 CSP/X-Frame-Options 策略限制外部嵌入，另称 full mail preview 可加载 iframe；后半受害者链未保存。 | [方法条目](../by-type/xss.md) |
| 允许富文本与持久 HTML 控制先说明受信任边界 | Judge.me 图给 public profile recommendations 描述可存 HTML，作者明确无法执行 JavaScript，报告 Informative。 | [方法条目](../by-type/xss.md) |
| 所谓 SSRF 头清单按地址、站点、协议和路径消费者分组 | 两图混合 Base/Http/Proxy URL、Client/Real/Forwarded IP、Host、Scheme、Port、Original/Rewrite URL 与自定义鉴权头。 | [方法条目](../by-type/host-header.md) |
| 扩展与 private 关键词不等于仓库访问或密钥有效性 | 图列 pem/ppk、SQL dump、JSON/YAML 服务关键词、ICA Password、license、client_secret，还重复 ppk。 | [方法条目](../by-type/info-secrets.md) |
| 无敏感影响反馈保留证据缺口而非通用结论 | 保存 Informative 回复说明该报告未见影响安全/完整性的敏感信息，但未给资源细节。 | [方法条目](../impact-and-acceptance.md) |
| 相同 cookie 指纹不证明应用或会话同一性 | 正文建议用 cookie 找相似站点以识别应用，没有保存工具或结果。 | [方法条目](../discovery/client-and-cloud.md) |
| JSON 与表单编码差异不能代替 CSRF 状态验证 | 图把 application/json 称为普通 HTML form content type，应纠正：原生表单的 enctype 为 urlencoded、multipart 或 text/plain；application/json 不属于 CORS 安全列表，普通跨源脚本设置它通常需预检。 | [方法条目](../by-type/csrf.md) |
| 扫描跳过修复公告与告警邮件不证明全量覆盖 | 正文提到 Nuclei v2.8.5 target-skipping 修复，Findomain 两邮件只有 low/critical/high 标签和未保存附件，称无 permutation 新子域。 | [方法条目](../discovery/records-and-incremental.md) |
| BFF 路径规范化需避免多变量对照和文件读推断 | Starbucks 图先是含 users/me 的路径及回退片段得 403，另一例去掉 users、插 web 后返回 JSON Not Found/errorCode404。 | [方法条目](../by-type/waf-bypass.md) |
| OAuth 授权说明与页面身份认证标题分开 | 正文自身定义 OAuth2 为客户端代表用户访问资源的授权框架，封面却写 Authentication。 | [方法条目](../by-type/oauth-oidc.md) |
| Forwarded Host 反射须跨越可信代理和 HTML 编码两边界 | 正文在 X-Forwarded-Host 放引号及事件示意。 | [方法条目](../by-type/xss.md) |
| 跨第一方登录流的主体与会话状态逐步绑定 | 保存 FB/Meta/Oculus 链以 FB 已登录、Oculus 未登录开始，提到 logout/login CSRF 再走第一方 OAuth。 | [方法条目](../by-type/oauth-oidc.md) |
| 嵌套 redirect_uri 与 fragment token 的转交链单独核验 | 同图为 response_type=token、内外 redirect_uri，称 fragment token 经论坛 openredirect 外泄。 | [方法条目](../by-type/oauth-oidc.md) |
| 修改登录响应为 200 后必须确认服务端订单授权 | 正文声称改 4xx 登录响应为 200 后访问所有用户订单，未保存交换。 | [方法条目](../by-type/idor-access-control.md) |
| AWS WAF 的声明前缀样例保留具体解析和版本条件 | 正文称在 script 前加 <! 即可绕过 AWS WAF，没有请求、规则或响应。 | [方法条目](../by-type/waf-bypass.md) |
| 邮箱文本进入 HTTP 或 SMTP 语法需要独立证据 | 保存混合清单把 Content-Length/CRLF 和 RCPT TO 放进邮箱文本。 | [方法条目](../by-type/crlf-response-splitting.md) |

| 管理端入口的路径与代理身份差异须回到同一业务动作 | `/admin%20`、`%09`、`;` 路径、重写头、X-Real-IP/X-Forwarded-For 以及 IP/CNAME、HTTP/HTTPS 变体只是代理和应用解释不一致的候选。 | [方法条目](../by-type/idor-access-control.md) |
| 项目调试文件与编辑器交换文件需验证真实内容归属 | 保存帖列 `.pnp/.pnp.js`、`.DS_Store`、`.env`、npm/yarn/debug 日志、`.firebase/.vscode`、authDump/data 系列 JSON、员工 CSV 和 web.config，另称 wp-config.php 404 而 .swp 200。 | [方法条目](../by-type/info-secrets.md) |
| 压缩上传到 PHP 包含解释之间存在两道独立边界 | 图示先把 PHP 放进 ZIP 上传，再让 `page` 指向 `zip://` 本地 ZIP 和 `%23` 成员分隔。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 历史 URL 和搜索索引中的 token 线索仍需验证用途与访问边界 | Drive 截图是历史 folders 链接、usp 分享参数和检索错误；Sorare 截图只有 `site:... inurl:token` 搜索起点，确认链接复用步骤未保存，作者还承认误改他人资料。 | [方法条目](../by-type/info-secrets.md) |
| 盲 XSS 面板应保留事件来源并拆开附加扫描结论 | XSS Hunter 保存面板显示 AWS 标识、CORS `*`、Git 配置片段、Browser Time 和 iframe=false；这些属于一个采集事件的多个线索。 | [方法条目](../by-type/xss.md) |
| 正则黑盒模糊测试须跟踪验证与规范化的先后顺序 | REcollapse 的保存正文只说明用黑盒正则模糊测试发现验证/规范化问题，没有工具内部算法或样本结果。 | [方法条目](../targeted-fuzzing.md) |
| 前端角色枚举只是查找服务端授权校验的起点 | 注册响应里 ROLE_USER 与 JS 中可能出现的角色名称，只能帮助定位属性和业务动作。 | [方法条目](../by-type/idor-access-control.md) |
| 旧 Swagger UI 的 configUrl 消费者需与普通链接导航区分 | Jamf Pro 历史截图指出 classicapi/doc 的旧 Swagger UI 可消费 configUrl=data:text/html;base64 并声称出现 alert 或钓鱼页，摘要称 2022 已移除入口。 | [方法条目](../by-type/xss.md) |
| 多入口二步验证应共用服务端认证状态与凭据生命周期 | TikTok 历史摘要称登录后回跳 UK Seller URL 可绕 2FA；另一清单列响应/状态码、direct、Referer、开发入口、XFF、session 权限、token 重用/共享、OTP 回显、CSRF/clickjacking、任意输入。 | [方法条目](../by-type/authn-session.md) |
| LFI 管道的 root:x 命中须绑定单个请求与文件消费者 | 保存管道 gau→gf lfi→qsreplace→25 路 curl，并把 stderr 合并后 grep root:x。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 外部渗透清单须把授权范围与具体动作逐项绑定 | 表格列 ROE、范围 IP/客户范围、kickoff、扫描、泄漏数据库、员工资料、门户枚举、手工测试、工具结果验证、密码喷洒、外转内、旧修复及 cleanup，状态全部 Outstanding。 | [方法条目](../scope-and-rules.md) |
| 图标哈希只产生服务候选而非漏洞实例 | Shodan/Zoomeye 的图标哈希及 favfreak 可以帮助聚合同类页面；保存帖没有实际版本、引用 exploit 或成功结果。 | [方法条目](../discovery/passive-and-services.md) |
| 越范围资产的漏洞链须在触碰新边界前重新核授权 | 保存帖把 out-of-scope takeover→ATO 与 3000 奖励连写，没有链条请求。 | [方法条目](../scope-and-rules.md) |
| 待验证邮箱更改后旧链接不能验证新地址 | 保存的四段流程为注册邮箱 A→重发激活链接→通过“邮箱错误”更改为 B→点击先前寄到 A 的链接，却声称 B 已验证。 | [方法条目](../by-type/authn-session.md) |
| 云评估与认证前后工具必须对应真实身份和资源 | AWS 图只是 VPC 公私网、实例与 S3 关系，O365 DRAFT 工具表分 recon、audit/review、phishing、authentication attacks、post-authentication。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 重定向白名单应约束整条实际跳转链 | 保存帖建议快速托管“redirection machine”并使用 DNS payload，没有实际服务器或输入输出。 | [方法条目](../by-type/open-redirect.md) |
| 将不完整提示转为一个可证伪的实验假设 | 正文批评误导/不完整 tips，图列半懂、一次学全部、追奖励、易放弃和与他人比较。 | [方法条目](../experiment-design.md) |
| 认证 SQL 片段需匹配真正查询结构与数据库方言 | 保存帖给 Oracle DUAL 的 AND/UNION/null,user 片段，另一帖仅称 SQLi auth bypass。 | [方法条目](../by-type/sql-injection.md) |
| HSTS 的主机状态键应在存取时采用相同规范化 | CVE-2022-43551 历史截图说明 curl 的 IDN 字符如 U+3002 转换为 ASCII 点，HSTS 存 IDN encoded、查 IDN decoded 导致后续 HTTP 没升级。 | [方法条目](../by-type/host-header.md) |
| 登录查询接口的账户资料字段应在授权前最小化 | 保存截图的 POST /auth?subdomain=test&commonLoginQuery=true 只见 login JSON，响应给 is_confirmed、email_contact、姓名、country、MFA/require_pass 等字段，access_token 等为空，Host 等已遮蔽。 | [方法条目](../by-type/authn-session.md) |
| 共享 Analytics 标识和反向 DNS 只提供待核资产关联 | UDON 正文用 Google Analytics ID 关联域名，另一帖给 IP 反向查询网站。 | [方法条目](../discovery/passive-and-services.md) |
| 域名标签层级统计不能依赖未转义点的正则 | 图示 grep -P 用 `[a-z0-9]+.` 重复匹配二至四级；`.` 未转义，会接受非点分隔并遗漏连字符、大写或 IDN 表达。 | [方法条目](../discovery/passive-and-services.md) |
| 路径反射命中须核最终来源和真实浏览器上下文 | 图片脚本对路径后缀和假查询参数 curl -L 并 grep xss，示例目标与第二个 PoC 域名还不一致。 | [方法条目](../by-type/xss.md) |
| 默认凭据候选必须分清产品识别、真实登录与角色能力 | PeopleSoft 正文给三组默认凭据，图是 Nuclei 2.7.7/模板 9.1.9 的 PSADMIN 命中；Tomcat 历史报告声称 6.0.35 的 manager/html 可用默认凭据并附小图。 | [方法条目](../by-type/authn-session.md) |
| 源代码秘密扫描应绑定实际文件输入与匹配规则 | 正文将 git clone stdout 管到 nuclei 本地目标，截图复用 Gitleaks 文件位置匹配。 | [方法条目](../by-type/info-secrets.md) |
| 模板与 XSS 混合字符串要按不同解释器逐段定位 | 正文字符串混合 `<%= 7*7 %>`、关闭标签、SVG 事件及跨行邮箱。 | [方法条目](../targeted-fuzzing.md) |
| ffuf 结果应从结构化字段提取并保存原始记录 | 正文 `cat * ｜ jq ｜ grep url ｜ cut` 会混入不同格式、过滤有效 FUZZ 文本、误取代理 URL 或日志并丢失状态/长度/方法/请求标识。 | [方法条目](../discovery/records-and-incremental.md) |
| 命令混合字符串的 DNS、延迟与文件写入证据应分开 | 图片组合 Unix/Windows ping、echo 写临时文件、dig 到共享回调域和 sleep 21。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 浏览器扩展的代理与身份隔离会改变实验环境 | 完整图片表包括 FoxyProxy、containers、PwnFox、Cookie Editor、Hackbar、修改 header 及识别/打开链接工具；PwnFox 列 toolbox injection 和 security header remover。 | [方法条目](../experiment-design.md) |
| 合并域名后批量 curl 应保留每条响应的身份与来源 | 图示 subfinder→assetfinder/anew→domain.txt→xargs sh -c curl -L，所有输出混在终端。 | [方法条目](../discovery/records-and-incremental.md) |
| 新域名扫描流程的提交点应区分完成、失败与配置变化 | 保存流程下载 CHAOS 新/更新项目，比较 master 域名，仅 new→tmp→Nuclei→Telegram→加入 master；无 new 也发通知。 | [方法条目](../discovery/records-and-incremental.md) |
| 双账户响应相同必须排除公共对象与共同拒绝 | Auth Analyzer 图把 A/B Cookies 放入工具、重复每 endpoint，声称 same=same 即奖励；手验被列在最后。 | [方法条目](../by-type/idor-access-control.md) |
| 缓存污染定义必须补齐缓存键与另一访问者取值 | 保存正文只给 unauthorized content 被当正常内容服务的定义，续篇未保存。 | [方法条目](../discovery/web-and-api.md) |
| DNS 解析器的完整率应由样本和错误状态验证 | 正文声称提供 resolver 文件能改善 10–30%，没有测量样本。 | [方法条目](../discovery/passive-and-services.md) |
| Activity 的可调用性与每个 WebView 消费者要逐项核验 | 图从 Manifest/Activity 指向 exported、permissions、auth、DeepLinks/WebView，并列 JS、loadUrl/loadData、JavascriptInterface、content/file 访问配置。 | [方法条目](../by-type/mobile-android.md) |
| WebView 文件与脚本能力须证明不可信内容实际可达 | 将 allowUniversalAccessFromFileURLs、JS 开关、loadUrl/loadData、JS interface、content access 分成能力、来源和消费者。 | [方法条目](../by-type/mobile-android.md) |
| XXE 的回显、外部 DTD、错误与 XInclude 是不同通道 | 完整图分别列 DOCTYPE 文件实体、SSRF/OAST、参数实体及外部 DTD、错误信息引入不存在文件、复用本地 DTD、XInclude 与 SVG 上传。 | [方法条目](../by-type/xxe.md) |
| 远程连接日志应按时间、会话和主机关联后再解释 | 保存表给 RemoteConnectionManager 1149 的 authentication succeeded，以及 LocalSessionManager 24/25 的断开/重连，跨 2019/2022 多 IP。 | [方法条目](../discovery/records-and-incremental.md) |
| 路径中看似外部 URL 的重定向须核解析后的目的地 | JetBlue 历史报告示例 movi 域路径带 `_https@google.com`，声称 Chrome 直接导航而 Firefox 先提示；图没有完整原始 Location。 | [方法条目](../by-type/open-redirect.md) |
| 模型给出的编码绕过建议必须经过真实解析链对照 | 两张历史聊天图仅因提示是否提 H1 私邀而给泛化编码/混淆建议或拒答。 | [方法条目](../by-type/waf-bypass.md) |
| 程序排除项与第三方集成影响应读取精确上下文 | 保存政策截图列第三方低影响可拒、SPF/DMARC、静态 clickjacking、匿名/登录退出 CSRF、无利用证明的旧库、旧浏览器/物理访问、工具报告/扫描禁令、非敏感 cookie flags、公开 robots、无 PoC SSL 及社工等排除。 | [方法条目](../scope-and-rules.md) |
| 字典命中的状态码需与软404和训练目标分开 | Wordlists 图片是 testphp.vulnweb 的 .idea、admin、cart 等 200/301/404/403，banner 遮住部分结果。 | [方法条目](../targeted-fuzzing.md) |
| 双编码路径需证明每层解码后都约束同一允许根 | 正文与图给 `/images/.%252e/` 重复到 etc/passwd，返回 root/bin/daemon 等文件样式；没有正常/单编码对照、最终服务器路径或调用。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 邮件冒用的投递结果、对齐验证与账户接管分开举证 | 正文声称 admin 子域缺/错 DMARC 可把 support/admin From 送到 inbox；图只 P4 Unresolved Duplicate 零奖励。 | [方法条目](../by-type/authn-session.md) |
| 静态堆报告须核所有权与实际控制流的可达性 | Heap Detective 图把 malloc/free 行、taint、loop 及 memory leak/double free 标到 samples，代码有 realloc、free、NULL 等局部片段。 | [方法条目](../source-audit.md) |
| 模型生成的目录列表不能当服务器执行证据 | 两张所谓 ChatGPT RCE 图片只是“the output of command”叙述与含 root/www、wp-admin/config-sample、cms 的目录文本。 | [方法条目](../experiment-design.md) |
| 邮件连接参数的 SSRF 分阶段验证协议与前置认证 | Nextcloud Mail 2.0.1 历史图分别是 POST /apps/mail/api/accounts 的 imapHost，先过正确 IMAP 才检查 smtpHost，以及已加邮箱后 PUT /apps/mail/api/sieve/account/5 的 sieveHost；截图多个 body/response 被裁切。 | [方法条目](../by-type/ssrf.md) |
| 业务认领流程需验证最终授予结果而非中间电话提交 | Yelp 保存摘要直接否认“替换 phone 就能认领任意商户”：号码内部验证，流程最终失败，报告 Not-applicable 虽保留 High7.5 标签。 | [方法条目](../by-type/business-logic.md) |
| XSS 影响需由真实执行身份和可访问能力限定 | 保存正文给可窃敏感信息/代操作的概念，图只 Day22 标题。 | [方法条目](../by-type/xss.md) |
| 更改 Content-Type 的 success 不等浏览器跨站 CSRF | 图声称 JSON body 在 text/plain 被 Cors origin not allowed 拒绝，而 form-urlencoded 返回 success 就 High。 | [方法条目](../by-type/csrf.md) |
| 静态 HTTP 服务命令只说明已有执行环境的服务能力 | 图是 Python2/3、Ruby、PHP -S 和 nc 的本地监听示例，正文却称运行 hosted server RCE。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 子域组合生成速度不能替代 DNS 与活服务覆盖 | mksub 图 500 词深度2产生250500行，time 重定向 /dev/null 报 0.67real/0.83user/1.09sys。 | [方法条目](../discovery/passive-and-services.md) |
| 限流头的变化须确认权威计数键与总尝试预算 | 正文称 X-Host 127.0.0.1 再轮换 .2/.3 可绕限流。 | [方法条目](../by-type/authn-session.md) |
| JS 正则提取的路径必须绑定调用代码与实际参数 | 正文 regex 及图输出 cart/confirmed/order、means-of-payment、stripe/publishable-key、account/edit/user/{6}。 | [方法条目](../discovery/client-and-cloud.md) |
| 依赖混淆候选须确认实际包解析与构建边界 | Hyperledger 报告说 package.json 依赖 aries-bifold 在公共 npm 不存在，作者明确没上传包、仓库 scope 不明确，状态 Informative0。 | [方法条目](../source-audit.md) |
| 定点插入扫描必须固定基线和自动改写字段 | Intruder 图把 GET search 的 test 设一处 § 插入点，并勾 Update Host to match target；没有扫描结果。 | [方法条目](../targeted-fuzzing.md) |
| 模板注入应区别模板源拼接与数据参数渲染 | 保存正文只有“把模板代码放进模板”定义和外链。 | [方法条目](../by-type/ssti.md) |
| 移动静态审计与被动 JS 规则需验证规则覆盖和数据流 | APKHunt 图片只有 MASVS static analyzer logo；Semgrepper 只有 Burp 集成说明和 stars/forks。 | [方法条目](../source-audit.md) |
| 旧依赖报告需分清实际 lock 来源与可达漏洞条件 | moment-timezone 图称修复0.5.35将 FTP换HTTPS，同时展示 lock 为0.5.35与HTTPS；Flysystem 图列历史race版本及CVE但只异常类 CorruptedPathDetected。 | [方法条目](../source-audit.md) |
| 多服务 token 测试前需核变量输入和凭据分发边界 | 保存正文/图将单 token 与 token 文件都传 nuclei -var token=...；只有 README 链接，文件如何逐行载入并未保存。 | [方法条目](../by-type/info-secrets.md) |
| 来历不明的工具应从来源和执行边界评估而非版本宣传 | 帖批评 cracked tools 可能让本机变远程节点，图片广告正文/链接卡版本还不同。 | [方法条目](../experiment-design.md) |

| postMessage 发出的 token：接收窗口控制先于通配符判断 | 保存截图中服务端页面以 window.parent.postMessage({token:…}, "*") 向父窗口发送 token；另一张图展示 alert 中的 token JSON。 | [方法条目](../by-type/authn-session.md) |
| 盲 XSS 回调收集：数据保管与有效事件去重 | 保存帖讨论第三方 XSS Hunter 与自建 VPS，配图展示 cookie、referrer、User-Agent、origin、浏览器时间和截图等回调字段。 | [方法条目](../reporting.md) |
| 跨资产复用一个发现：同一根因与独立授权边界 | 保存帖将 exposed Git、Django debug、Swagger UI 放在持续检查其他基础设施的经验中，另有 reconFTW/Osmedeus 以及构建工具清单。 | [方法条目](../hunting-strategy.md) |
| 自动化未命中后的手工检查：从 redirect 假设补齐输入链 | 保存正文给出 CVE-2023-0748 和先自动化、无结果再手工的经验，图片仅是 huntr/CVE 通知。 | [方法条目](../experiment-design.md) |
| 历史 URL 到 redirect 候选：保留参数和消费者 | 保存帖把 waybackurls 的结果交给 gf redirect，再用 tee -a 汇集。 | [方法条目](../by-type/open-redirect.md) |
| FiveM NUI 弹窗截图：执行上下文和持久化证据分开 | 现有图片显示 nui://easy-chat 中两个 alert 场景及 XSS Hunter 通知计数，正文称 stored XSS。 | [方法条目](../by-type/xss.md) |
| S3 搜索结果：桶归属和对象权限分别核验 | 正文建议在 s3.amazonaws.com 下带目标域名搜索。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 图片的物理信息泄露：从可见线索到隐私影响 | “spot the bug” 配图以丢失钥匙海报把钥匙、住所和在家时段等线索放在同一处。 | [方法条目](../discovery/passive-and-services.md) |
| 2FA 本地响应改写与空验证码：以服务端受保护操作确认 | 保存帖分别建议把 4xx 响应改成 200，另一个仅给出空验证码获奖文章标题。 | [方法条目](../by-type/authn-session.md) |
| Web shell 与后门菜单：既有执行权不能倒推入口 | C99Shell 页面列出文件、命令、上传、FTP 等能力，另图展示 PowerShell 后门获取 OS、BIOS、文件、公共 IP 的菜单。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 密码重置超长输入：限制位置与资源消耗要独立证明 | 保存帖称 Nextcloud 可重置很长密码及超长输入导致服务器问题，图片只有裁剪的历史报告/低级别 DoS 摘要。 | [方法条目](../by-type/authn-session.md) |
| 修复即刻复测：同一原始条件加最小旁路变化 | 正文建议在报告 resolved 后马上复测，图片展示奖励和状态。 | [方法条目](../reporting.md) |
| 缓存工具 FALSE 输出：阴性覆盖只绑定当前探针 | FockCache 图片列出 X-Forwarded-Host 和 Scheme 等探针的 FALSE 结果。 | [方法条目](../discovery/web-and-api.md) |
| doc URL 返回 Apache server-status：回显 SSRF 与云影响拆开 | 图片显示 GET /view_postdocument.php?doc=http://localhost/server-status 返回 Apache 状态文本，涉及服务版本、prefork 和回环地址。 | [方法条目](../by-type/ssrf.md) |
| GTFO sqlite3 条目：可用能力取决于已有权限 | 截图列出 sqlite3 的 .shell、文件写入和 .import 以及 sudo/SUID 条件。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 协议处理器与 WMI 启动：监听器启动不是执行链闭合 | 正文提出注册协议处理器再由 WMI 启动，截图只有反向 TCP listener STARTED。 | [方法条目](../by-type/desktop-client.md) |
| Cookie bomb：输入变大和会话可用性之间的边界 | 正文把参数中的逗号扩展与 cookie header 限制联系起来，复用图片显示 Cookie 过大导致 400。 | [方法条目](../discovery/web-and-api.md) |
| 移动端 admin 标记变更：客户端显示与后端授权拆开 | 保存标题称把 admin 从 0 改成 1，图片只有文章封面。 | [方法条目](../by-type/authn-session.md) |
| Nextcloud IP 策略：验证失败后跳过拒绝与下游解析差异 | 可见源码片段先以 filter_var 验证 IP，再检查私网/保留地址及 100.64/10、192.0/24 等范围。 | [方法条目](../by-type/ssrf.md) |
| Jitsi Windows 历史 URL scheme：参数构造决定命令边界 | 图片描述 Jitsi Windows launchbrowser 在历史提交前存在 URL scheme 命令注入并关联 CVE-2022-43550；展示 High、奖励与 retest 状态。 | [方法条目](../by-type/desktop-client.md) |
| Nextcloud nc 链接到本地文件：文件选择与执行结果分开 | 现有源码截图出现 QtConcurrent 处理后以 QDesktopServices::openUrl(QUrl::fromLocalFile(foundFiles.first())) 打开文件，历史报告关联 CVE-2022-41882。 | [方法条目](../by-type/desktop-client.md) |
| 重复前导斜线的 partner API：先核验同一资源和授权状态 | 保存帖及截图把标准 partner autorebate 路径的 403 与重复前导 // 的 POST /api/v2/autorebates/groups/ 请求并列。 | [方法条目](../by-type/idor-access-control.md) |
| 购物数量负值：服务端订单不变量优先于小计显示 | 正文描述 50 与 49 的商品及 quantity=-1 得到 subtotal=1 的情境。 | [方法条目](../by-type/business-logic.md) |
| 加密移动 API 双代理：观测层转换与服务端校验边界 | 保存图描述客户端密文先进入 mitmproxy 解密，再送到 Burp 编辑明文，再由另一 mitmproxy 加密并送服务端，正文提到硬编码 key/IV。 | [方法条目](../by-type/mobile-android.md) |
| 报告附件公布：视频里未公开材料也属于披露面 | 保存报告摘要称公开的复测视频附件包含另三个未公开报告的名称、项目或严重性信息。 | [方法条目](../by-type/info-secrets.md) |
| WHOIS 大网段与顺序 IP：服务商范围不等于目标资产 | 图片以 Amazon 107.20/14、AT&T 107.224/11 等 WHOIS 范围说明连续 IP，另帖给出收集脚本链接。 | [方法条目](../discovery/passive-and-services.md) |
| GET id 的 MySQL SLEEP 候选：延迟需重复对照与方言确认 | 保存正文给出在 GET id 中使用 XOR/SELECT SLEEP(9) 的时间盲注探针。 | [方法条目](../by-type/sql-injection.md) |
| 公开粘贴和格式化站点：搜索片段不能代替保密性判断 | 保存帖列举 pastebin、codebeautify、jsfiddle、codepen 等域限定搜索，现有图显示 XML/JSON viewer 结果含订单或联系字段。 | [方法条目](../by-type/info-secrets.md) |
| Nmap 速率与扫描类型：预算约束到每类实际请求 | 三页图含目标文件/随机目标/排除项、SYN/connect/UDP/ACK、服务和 OS 探测、NSE、超时、并发、重试及 min/max-rate。 | [方法条目](../discovery/passive-and-services.md) |
| 浏览器插件清单：把输入辅助与代理捕获覆盖分开 | 保存正文/图列出十三种 Firefox 插件，重复帖子保留为同一候选清单。 | [方法条目](../discovery/client-and-cloud.md) |
| URL 消费者清单：文件输入、SVG 与元数据各有独立前提 | 正文建议从一切可输入 URL 的功能，以及 file 输入改 URL、SVG image/xlink、ImageMagick 等寻找 SSRF；另一帖询问 AWS URL 403。 | [方法条目](../by-type/ssrf.md) |
| Apache server-status：内部状态字段到外部读者的可见性 | 图片展示历史 Apache server-status 的 PID、CPU、回环地址、vhost 和请求行，正文提到可能含敏感信息。 | [方法条目](../by-type/info-secrets.md) |
| Users 到 Subcomments 的 API 图：每条边都绑定归属关系 | 保存帖以 Users→Posts→Comments→Subcomments 描述对象关系。 | [方法条目](../business-modeling.md) |
| AI 生成 dork：语法、索引和目标归属三次过滤 | 保存图片宣称十条新颖 dork 但只展示前四条，涉及 WP xmlrpc、vBulletin 版本、Cloudflare/server 字样和 Git HEAD。 | [方法条目](../discovery/passive-and-services.md) |
| SSTI 定义纠偏：模板编译点不同于生成 HTML | 保存正文以不安全生成 HTML 描述 SSTI，图片为 Day27 文章封面。 | [方法条目](../by-type/ssti.md) |
| 403 路径变体：状态码差异必须落到同一受保护资源 | 保存帖出现 lyncdiscover 403 绕过题名、amass/搜索发现建议，现有图列出 secret 为 403、secret/、secret/.、//secret//、./secret/./ 为 200；已复用的 lyncdiscover 图仅显示编码路径仍 403。 | [方法条目](../by-type/idor-access-control.md) |
| 正常登录跳转：可控目的地和跨源边界分别验证 | 正文描述开放重定向，图片只显示 dashboard→login 的正常路由。 | [方法条目](../by-type/open-redirect.md) |
| dirsearch 大字典与线程数：候选扩展不能替代服务证据 | 保存帖给出 200 threads、-e * 和 CombinedWordlist。 | [方法条目](../targeted-fuzzing.md) |
| Origin 反射清单纠偏：浏览器可读私有数据才是确认点 | 图片把 Origin 中带 slack、前后缀相似域、任意域或子域获反射列为漏洞，其中若干示例缺少 scheme。 | [方法条目](../by-type/cors.md) |
| Android 存储与备份：路径名只是暴露候选 | 现有攻击图列出文件路径/XML、外部存储、Firebase 配置、SQLite 以及备份/共享路径。 | [方法条目](../by-type/mobile-android.md) |
| Android 硬编码 key 与 IV：保密性和伪造性要分开 | 攻击图含 CBC、静态 IV、硬编码 key、XOR 及 API 共享 token。 | [方法条目](../by-type/mobile-android.md) |
| Android IPC 与 WebView：入口导出和数据消费者逐段检查 | 保存图及教程题目涉及 Intent/filter、BroadcastReceiver、ContentProvider、WebView、deep link、ADB 和 SDK/插件。 | [方法条目](../by-type/mobile-android.md) |
| HTML 到 URL 到 JavaScript：绕过载荷依赖分层解析位置 | anchor 示例图标注空白、实体和 scheme 等六处变异，另帖给出注释、onmouseover、SVG 与编码混合的 polyglot 文本。 | [方法条目](../by-type/xss.md) |
| PHP 与参数搜索：索引关键词仅建立待测入口 | 保存 dork ext:php inurl:& site:target[.]com 可用于收集有参数样式的 PHP 候选。 | [方法条目](../discovery/passive-and-services.md) |
| JSON 数组登录尝试：认证消费者和请求计数独立核验 | 正文建议在 username/password 中放列表，以单次 POST 尝试多组凭据；图只有奖励/验证状态。 | [方法条目](../by-type/authn-session.md) |
| 旧已解决报告再检：复用根因而不是状态标签 | 保存帖建议从 Hacktivity、OpenBugBounty、Twitter、Medium 的旧报告中查找旁路。 | [方法条目](../hunting-strategy.md) |
| 注册 email 尾换行：规范化冲突必须以账户归属确认 | 现有两图分别是已有 email 返回 400 “exists”，以及 JSON email 加换行返回 201、返回值去掉换行。 | [方法条目](../by-type/authn-session.md) |
| Hunter 查询字段：检索运算与资产结论拆开 | 图列 IP、domain、suffix、HTTP、product/version、location、certificate、JARM、favicon、ASN 等字段，以及 ==、=、!=、!==、and/or。 | [方法条目](../discovery/passive-and-services.md) |
| secret regex 搜索与 Validating 状态：匹配不等于有效凭据 | 保存帖称 secrets DB 有 1600 余 regex，另一帖建议一天多次 GitHub 搜索并配 Validating Access Token 状态图。 | [方法条目](../by-type/info-secrets.md) |
| 历史 Splunk raw server-info：路径存在与敏感字段披露分开 | 图给出 /en-US/splunkd/__raw/services/server/info/server-info?output_mode=json，正文关联旧版本和 CVE-2018-11409、license key。 | [方法条目](../by-type/info-secrets.md) |
| 删除 poll 后数据保留：接口权限和公开策略同时核验 | 历史摘要称 Twitter 已删除的 poll 在 UI 消失后仍可经 API 访问并超过声称的保留期限。 | [方法条目](../by-type/info-secrets.md) |
| 重定向转 XSS/ATO 的编码候选：每次转换单独留证 | 保存文本包含普通 javascript、百分号、HTML 实体及嵌套编码 URL 候选。 | [方法条目](../by-type/open-redirect.md) |
| 一次性优惠码竞态：限制一与实际兑换次数之间的原子边界 | Stripe Promo TEST 图片显示 redemption limit 1 及历史 TOCTOU 摘要。 | [方法条目](../by-type/business-logic.md) |
| 参数污染和方法隧道：解析选择与授权消费者需对应 | 保存帖提出 parameter pollution、verb tunneling 的练习方向。 | [方法条目](../discovery/web-and-api.md) |
| IPv4 缩写：只验证实际网络栈支持的等价形式 | 保存图举 1.0.0.1→1.1、127.0.0.1→127.1、192.168.0.1→192.168.1。 | [方法条目](../by-type/ssrf.md) |
| 剪贴板分块与 OCR 文件传输：传输准确性不等于权限绕过 | Invoke-Transfer 帮助图含约 120KB 分块、剪贴板、Guacamole、base64 合并及 OCR，并标注 Win10 OCR 不精确。 | [方法条目](../by-type/desktop-client.md) |
| uat 子域置换：环境命名不能代替漏洞证据 | 正文建议 permutation 添加 uat，并称找到的环境很脆弱。 | [方法条目](../discovery/passive-and-services.md) |
| ZAP AJAX 爬虫进程：启动证据不能说明登录态与覆盖 | 截图显示 ZAP AJAX、geckodriver 和 Firefox 的进程/资源，正文介绍组合。 | [方法条目](../discovery/client-and-cloud.md) |
| SQL 引号再拼接：恢复响应只是可疑解释差异 | 正文提出单引号报错后尝试相邻字符串、｜｜ 或 +，若原响应恢复则可能 SQL 注入。 | [方法条目](../by-type/sql-injection.md) |
| debug.log 报告通知：实际字段决定泄露边界 | 图片仅显示历史 WordPress debug.log full-path 报告 resolved 通知。 | [方法条目](../by-type/info-secrets.md) |
| Triage Wizard HTML 测试：扩展特权和网页 origin 区分 | 正文/图建议开启 HackerOne Triage Wizard Chrome extension，进入指定 security/bugs 查询的报告页后点 View Triage Questionnaire Beta，声称注入 HTML 可能 XSS。 | [方法条目](../by-type/xss.md) |
| Nuclei 排序输出：模板严重性不能代替目标影响 | 图片把 missing CSP 标 critical、SSL issuer 标 high、NS/WAF 项标 medium，并含多个目标/协议/实验项。 | [方法条目](../impact-and-acceptance.md) |
| 租户停用后 users roles：生命周期状态参与授权 | 8x8 历史摘要称自有 tenant 停用后仍可 GET /api/v1/users/UUID/roles。 | [方法条目](../by-type/idor-access-control.md) |
| 移出 workspace 后旧 cookie：会话撤销和对象权限同步 | JaaS 历史报告描述管理员邀请用户、用户加入执行动作并保存 cookie、管理员移除、旧 cookie 仍可读写 workspace。 | [方法条目](../by-type/authn-session.md) |
| Rooms 无权限成员启动 calendar OAuth：init 与授权效果拆开 | 保存 8x8 历史摘要给出 /meet-external/spot-roomkeeper/v1/calendar/auth/init 和指向 rooms/add 的 successRedirectUrl，嵌入页同时提示没有 Rooms 权限。 | [方法条目](../by-type/oauth-oidc.md) |
| 工单接口的内部 agent 数据：角色和字段双重边界 | 历史 8x8 摘要称 /api/v2/support/requests/<ticketnumber> 可见内部代理数据，已修复 ACL。 | [方法条目](../by-type/idor-access-control.md) |
| 管理员邀请代发：发起者、显示署名和接收权限分别验证 | 保存历史摘要含 POST /api/v1/users/<UserID>/invites 冒用另一管理员发邀请，以及受限 User Management 角色邀请管理员。 | [方法条目](../by-type/idor-access-control.md) |
| wp-config.php.bk 字典候选：下载内容和备份归属决定风险 | 正文列出 wp-config.php.bk 作为 wordlist 项。 | [方法条目](../by-type/file-upload.md) |
| 代理工具界面：一条真实流量确认每层操作 | Caido 图展示 scope、history、request/response，example.com favicon 请求返回 404，并有 intercept/replay 等入口。 | [方法条目](../discovery/client-and-cloud.md) |
| 三字符密码挑战：搜索空间和服务端限制决定实际工作量 | 正文称三字母密码 brute force 两天，属于挑战描述。 | [方法条目](../by-type/authn-session.md) |
| 考试 foothold/escalation/exfil 分类：分阶段保存独立证据 | 保存正文把 Burp 考试学习分为 foothold、escalation、exfil，图片只是学习仓库卡片。 | [方法条目](../hunting-strategy.md) |
| 公开 CTF 帖给出的 IP/flag 指令：来源提示不扩大授权 | 保存正文是公开 IP 挑战及 flag/私信规则。 | [方法条目](../scope-and-rules.md) |
| HTTPS 链接改成 HTTP：本地改写与服务端协议授权拆开 | 正文建议从 https 换 http，图是 Burp Response modification rules 中 Convert HTTPS links to HTTP 复选框。 | [方法条目](../discovery/web-and-api.md) |

| .ftpconfig 路径却返回 JavaScript：内容识别先于扩展名影响 | 现有图的 URL 以 combined.js/.ftpconfig 结尾，返回 core_informations.js、API base path 和 sf Angular 模块数组，没有 FTP 主机、用户名或口令。 | [方法条目](../by-type/info-secrets.md) |
| 遗留 S3 静态网站依赖：名称占用和消费者信任各自核验 | Tendermint 历史报告描述 us-west-1 的 tendermint-packages 静态网站桶未占用，并叙述同名建桶、开启静态网站可接管；正文称其他区块链项目的代码仍引用它。 | [方法条目](../by-type/subdomain-takeover.md) |
| curl HSTS 状态共享：串行多请求和并行持久化分开 | 两张历史摘要分别描述 CVE-2023-23914：同次 curl 调用先 HTTPS 再 HTTP，而内存 HSTS 没有在下一请求正确沿用；CVE-2023-23915：--parallel 多站点后 hsts.txt 仅保留一站条目。 | [方法条目](../discovery/client-and-cloud.md) |
| Shodan 证书与标题筛选：从归属候选到 Swagger 消费者 | 正文用 ssl:"Company Inc" 加 http title 筛选，再 fuzz 发现 swagger-ui 并尝试历史 XSS 仓库；另一帖称深 Shodan 发现无认证 dashboard。 | [方法条目](../discovery/passive-and-services.md) |
| IDOR 候选：对象引用、主体资格与操作结果三个条件 | 正文称 IDOR “无需技能且高奖励”，另帖建议扫描或手工查 missing authorization。 | [方法条目](../by-type/idor-access-control.md) |
| 服务账号私钥示意：JWT assertion、token 交换和 IAM 权限分层 | 图片用 jose/RS256 和 PKCS8 私钥占位生成含 kid、iss、scope、aud、iat、exp 的 assertion，再拟向 Google token endpoint 交换 access token 并访问 Firestore。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| MISP 属性导出：情报类型和资产测试资格拆开 | 保存题名说明 MISP-Extractor 从实例取 IP、URL、hash 类属性，图片是装饰。 | [方法条目](../discovery/records-and-incremental.md) |
| 远程 LastBootUpTime：管理查询成功不等于漏洞入口 | 正文建议循环 wmic /node 查询 OS LastBootUpTime。 | [方法条目](../by-type/desktop-client.md) |
| recon 与 kxss 命中：反射位置必须落到浏览器执行上下文 | 正文给出常见闭属性 script 载荷及 GET 参数中的单引号减法 confirm 候选，并提到 kxss；图片只有 triaged/duplicate/收件或验证通知。 | [方法条目](../by-type/xss.md) |
| 上传类型限制：接受文件、可取回与执行三次确认 | 正文概述未充分验证上传及 Upload_Bypass_Carnage；图片是 Day31 封面和 shell.PhP6.PhP6 等双扩展尝试、nc 仅监听。 | [方法条目](../by-type/file-upload.md) |
| AI JavaScript 审计意见：原始可达数据流决定真假 | 现有 ChatGPT 图列 hardcoded access_token、/login 字符串 SQL、req.param 到 res.redirect、无验证、事件监听“不必要”和 Sequelize storage 路径。 | [方法条目](../source-audit.md) |
| HoaxShell 演示：生成器、监听、会话和初始入口分别留证 | 保存替代文字是独立 listener 集成介绍，图片展示 cmd-curl listener9001、Session established 及 Windows hostname 返回，另图为 RevShells 的回环地址生成器。 | [方法条目](../by-type/cmd-injection-rce.md) |
| E2E 群密钥更新：加密强度不能替代更新 API 授权 | Rocket.Chat 历史摘要描述 e2e.updateGroupKey 更新 rocket_subscription 的 E2EKey，用户 public_key 以 RSA 包装 room-key，再用 AES 保护聊天消息。 | [方法条目](../by-type/idor-access-control.md) |
| 多层 HTTP 基础架构：拒绝与解析结果绑定实际处理层 | 保存图画 client→firewall→load balancer→多个 web servers→database。 | [方法条目](../discovery/web-and-api.md) |
| Joomla public=true 检测：200 和关键词只提供候选 | 保存 YAML 以 GET /api/index.php/v1/config/application?public=true，AND 匹配 password/application/200，另两帖给 httpx 路径请求及只匹配 200 的链。 | [方法条目](../by-type/idor-access-control.md) |
| 反射未闭合转盲回调：触发页面和敏感能力仍要确认 | 正文建议把无法完整利用的 RXSS 换成盲 XSS 载荷，图只裁剪 cookie 与浏览器 User-Agent 字段。 | [方法条目](../by-type/xss.md) |
| 模板表达式与 auxclick：客户端解释器和交互条件先于 WAF 标签 | 正文给 Angular 风格构造器/charAt/$eval 表达式，以及 details 的 onauxclick confirm 示例；图片只有两个 WAF-bypass 报告状态和 Akamai 页面地址栏候选。 | [方法条目](../by-type/xss.md) |
| 响应 regex 秘密候选：公开 key、样例与有效凭据分开 | SecretFinder 图标注 google api 为 Information/Tentative 并要求手工确认，Burp regex 图选择 response body、未勾 In-scope only，结果含 Google Maps apiKey 和 clientSecret 模板字样。 | [方法条目](../by-type/info-secrets.md) |
| SSL stripping 与 HSTS：明文入口和策略状态决定降级可能 | 图画用户到中间人为 HTTP、中间人到服务为 HTTPS，正文是 HSTS/SSL strip 主题。 | [方法条目](../discovery/client-and-cloud.md) |
| 整批 Burp 请求加 header：作用域与方法覆盖逐条核验 | CustomHeader 图片按行设置字段和值，并用 checkbox 选择 GET/PUT/DELETE/TRACE 等，显示 TRACE enabled。 | [方法条目](../discovery/client-and-cloud.md) |
| stage 测试卡请求到生产：环境绑定与支付结算来源检查 | 正文叙述 stage 子域用测试卡升级，再带 tokens 的请求移到 prod 获一年 premium。 | [方法条目](../by-type/business-logic.md) |
| X-Forwarded-For 限流假设：可信代理链与账号计数分开 | 两帖声称 X-Forwarded-For:127.0.0.1 可绕 login/OTP 限制。 | [方法条目](../by-type/authn-session.md) |
| 默认口令列表：型号、构建和出厂状态是验证前提 | 保存图混列 Cisco、Citrix、OPNsense、Dell iDRAC、Juniper、pfSense、SAP、Tomcat、UniFi、WebLogic、Zabbix、Windows、Splunk、PRTG、Raspbian 等示例，正文给第三方查询站。 | [方法条目](../by-type/authn-session.md) |
| 403 Bypasser 帮助页：算法和受保护资源需要实际证据 | 图只有 403-bypass.py 的 --help、URL/PATH 参数及示意调用。 | [方法条目](../by-type/idor-access-control.md) |
| 重复对象参数：first/last/list 解析要对应实际授权对象 | 正文提示多处 ID 只改一处可能绕过，已复用图片是重复 company_id JSON 添加管理员的文字示意。 | [方法条目](../by-type/idor-access-control.md) |
| 子域优先与 CeWL 词表：由业务内容缩小有授权候选 | 正文建议主域竞争多转向子域并用 CeWL 做词表。 | [方法条目](../hunting-strategy.md) |
| claim 前加 @：用户信息解析与资源唯一性须闭合 | 图片示意 subdomain 已被占用，而 @subdomain 可注册，解释可能是 @ 用户信息分隔引起解析差异。 | [方法条目](../by-type/subdomain-takeover.md) |
| phpMyAdmin .htaccess 返回：可见配置与认证秘密区分 | 图片 GET /phpmyadmin/.htaccess 携带多项 cookie，返回 200 application/octet-stream，body 含 deny from all、AuthType Basic、AuthName、AuthUserFile /home/.passwd 与 Require user admin。 | [方法条目](../by-type/info-secrets.md) |
| 代码练习执行与沙箱越界：环境变量不是 S3 访问证明 | Meta Careers 图展示提交 PHP 调用 system 读取 /proc/12/environ，console 有 Lambda 函数/运行接口/region 等元数据。 | [方法条目](../by-type/cmd-injection-rce.md) |
| S3 ls、cp 与 sync：列举、上传和读取互不推导 | 图文字叙述历史 URL→JS→linkfinder 发现桶，ls 成功，cp 本地 note 上传 AccessDenied，sync 下载并称敏感文件。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 二次用户名修改：额外字段与次数审批限制同时验证 | 图说用户名只允改一次，第二次需管理员，编辑 profile 请求额外加 user[username]=testing 后可再次改。 | [方法条目](../by-type/business-logic.md) |
| POST 改 GET 与 _escaped_fragment_：渲染路线变化单独验证 | 图片文字称 id 从 POST 改 GET 后 XSS，另说 _escaped_fragment_ 参数可解除阻断。 | [方法条目](../by-type/xss.md) |
| 把单一发现写成模板：相同根因和阴性对照先于数量 | 正文建议用自定义 Nuclei 模板检查其他子域，宣称三十余发现，图是多个 XSS 报告标题。 | [方法条目](../hunting-strategy.md) |
| SVG 载荷与脚本内反射：浏览器版本和周围字节决定解析 | Safari 图给 SVG/a/onload，另一正文给 SVG script xlink:data 示例并说明后续 script 块影响闭标签，第三帖称已在 script 内应从 d=document 开始并讨论 path/query 引号编码。 | [方法条目](../by-type/xss.md) |
| AI 生成 XSS PoC：从 alert 到影响必须保持原始利用条件 | 保存正文列描述 prompt、导出 JSFiddle、托管和引入外部脚本再扩大 alert 的流程，未保存 prompt/code。 | [方法条目](../reporting.md) |
| chaos→naabu→httpx：保留 Host、端口和共享基础设施归属 | 图展示子域枚举、全端口探测到 HTTP 服务列表，含 80/443 及多个非标准端口。 | [方法条目](../discovery/passive-and-services.md) |
| CSP allowlist 检查：允许域不等于允许攻击者脚本 | 保存正文建议检查 google/google-analytics 等 allowlist，图示 default-src example.com 阻止外部 script。 | [方法条目](../by-type/xss.md) |
| workspace 邀请跳过接受：管理员权限与受邀者同意分开 | Slack 历史摘要说管理员能用 email 加入未接受邀请用户，绕过“接受后才能成为成员”的流程。 | [方法条目](../by-type/idor-access-control.md) |
| 私有视频缩略图：派生资源继承原对象可见性 | TikTok 历史摘要限定 friends/followers only、排除 only me，且要求已知或可猜 video_id。 | [方法条目](../by-type/idor-access-control.md) |
| 加密库线程错误栈：失败残留影响下一个操作 | Node.js 历史摘要称至 19.2.0 的 OpenSSL error stack 未清，在同线程证书验证失败后 JWT 签名可能错误失败，关联 CVE-2023-23919 与 X509Certificate::CheckPrivateKey/ClearErrorOnReturn。 | [方法条目](../source-audit.md) |
| 密码重置五项候选：收件人、令牌主体与邮件 origin 各自绑定 | 图列重复 email、数字 code 猜测/IP 轮换、自有 reset token 用于另一账户、Host 改变重置链接及 timestamp/userID/email 推测 token。 | [方法条目](../by-type/authn-session.md) |
| 导入 label color 与 scoped label：同一修复覆盖两种消费者 | GitLab 历史报告以外部 GitHub 导入 labels.color 未净化为入口；图说明 GitHub 正常不能任意 color，因此需要受控 dummy API、可达服务、api-scope PAT 和 namespace，后续摘要称 15.3.2 修复漏掉 Premium scoped label（名称含 ::）。 | [方法条目](../by-type/xss.md) |
| 目录枚举投入时间：区分新路径、软 404 与受保护内容 | 正文建议花时间 dir bruteforce，图片只有 P4/Unresolved/奖励。 | [方法条目](../targeted-fuzzing.md) |
| card.xq id 的 HTML 与脚本候选：界面注入和执行结果分开 | 历史图给 /card.xq?id 参数，编码字符串闭 title 后写 body/form，form action 指向外源，另一行是 script alert 候选；图同时提到 jQuery1.11.3。 | [方法条目](../by-type/xss.md) |
| jadx 静态还原：输出要回到实际 APK 与动态消费者 | 现有 Session03 图示 jadx -d 指定输出路径及 GUI 反编译，正文列静态/动态分析。 | [方法条目](../by-type/mobile-android.md) |
| 测试目录与编号：覆盖表要写完成状态及证据限制 | Voorivex guide 图介绍九类测试及十五 extra，可见 fingerprint、搜索/元文件/注释/错误栈、敏感路径、索引、local storage、部署/admin/backup/header、注册/锁定/remember/cache 等目录。 | [方法条目](../hunting-strategy.md) |
| 跨重复编码 header 的资源上限：总量不能按单项重置 | curl CVE-2023-23916 历史摘要说明多个 Transfer-Encoding/Content-Encoding header 中每个 encoding 分配 buffer，单 header 的层数有限而 header 数量没有合并限额。 | [方法条目](../discovery/client-and-cloud.md) |
| DotGit 面板候选：仓库对象恢复需独立确认 | 图片 DotGit 显示 Total found:0 却有三个遮挡 URL 的下载按钮。 | [方法条目](../by-type/info-secrets.md) |
| 漏洞管理 UI：严重性、证据和风险接受状态独立保存 | Faraday 图以示例站点展示 SQLi、明文 password、RXSS 标签、严重性筛选和 Risk-Accepted。 | [方法条目](../reporting.md) |
| prototype additionalArgs gadget：污染源到继承读取再到 shell | 代码图从 obj.additionalArgs 取数组，把项包进单引号拼到 cmd 后调用 exec。 | [方法条目](../source-audit.md) |
| PP Finder hooks 与 Fastify marker：undefined 读取不是污染确认 | PP Finder 图称用 TypeScript AST 注入 undefined 属性读取 hooks 并替换原 JS，输出 express/qs 位置；另一图 Fastify4.13.0 POST 普通 JSON content-type 后响应含 polluted=true。 | [方法条目](../source-audit.md) |
| SQL 载荷合集：方言、列类型和延迟对照分别确认 | 保存正文混有布尔/注释/ORDER BY、MSSQL waitfor、MySQL SLEEP 及 POST polyglot、十五列 UNION 和 GROUP_CONCAT。 | [方法条目](../by-type/sql-injection.md) |
| 未验证 email 的 cookie：页面门槛与服务器资格分开 | 正文建议拿 unconfirmed 账号 cookie 发送验证后请求，图只有 Verify your email 界面。 | [方法条目](../by-type/authn-session.md) |
| rpcping 与认证响应诱导：已有 shell 不等于取得明文密码 | 正文从非管理员主机 shell 提出 Inveigh 配 rpcping 的候选。 | [方法条目](../by-type/desktop-client.md) |
| WordPress users、CORS 和 xmlrpc：三个独立消费者逐项判断 | 正文称 /wp-json/wp/v2/users/<id> 公开所有用户字段、CORS misconfiguration 和 xmlrpc vulnerability，却无响应。 | [方法条目](../discovery/web-and-api.md) |
| 拿到 CSRF token 后：获取条件和会话绑定仍决定是否可伪造 | 正文问“有 token 是否仍 CSRF”。 | [方法条目](../by-type/csrf.md) |
| Reverse IP 输出：共址、历史解析和同主体归属区分 | 图的 reverse-ip.py 示例对一个域的 IPv4/IPv6 列出数百关联域并导出文件。 | [方法条目](../discovery/passive-and-services.md) |
| Go 小工具目录：可复用模板先核对输入输出与副作用 | 保存正文推荐 goHackTools 作为自建模板，图目录跨 DNS/MX/HTTP headers/comments/文件/地理信息、经典 cipher/base64、Shodan、代理与 tunnel/shell、密码/扫描/SYN flood 等。 | [方法条目](../hunting-strategy.md) |
| CSS 注入到服务端取资源：渲染消费者是链的关键 | 保存帖标题称 CSS injection→local file read/SSRF→internal API，但全文未保存。 | [方法条目](../by-type/ssrf.md) |
| jwt-cracker 与 JWT 标准描述：验签、密钥与授权三层区分 | 正文提供 jwt-cracker 的 alphabet/maxLength 接口，另称 JWT 安全传输 JSON，图片只有 JWT 封面。 | [方法条目](../by-type/jwt.md) |
| 从 Angular JavaScript regex 提取路径：字符串候选不等于所有 API | 保存 one-liner 以 curl 后路径 regex 和 sort -u 提取字符片段。 | [方法条目](../discovery/web-and-api.md) |
| netcat 单连接循环响应：HTTP 字节与工具退出语义核验 | 图片循环构造 HTTP/1.1 200、wc -c 的 Content-Length、cat index.html，再 nc -l -p8080 并重启循环。 | [方法条目](../experiment-design.md) |
| 四类重定向消费者：最终导航和脚本 scheme 分别验证 | 复用图片归纳 Location、Refresh、meta 与 JavaScript 重定向。 | [方法条目](../by-type/open-redirect.md) |
| visualRecon 多源追加：增量名单与来源不能被目录污染 | 已复用 visualRecon 图组合 sublist3r/assetfinder，固定目录 cd、追加 subs、sort-u、httprobe 和 aquatone。 | [方法条目](../discovery/records-and-incremental.md) |
| ASP.NET/IIS 重复参数：拼接方式需要实测而非技术栈猜测 | 保存正文及复用图片声称 HTTP parameter pollution 可把 XSS 碎片拼接绕过滤。 | [方法条目](../by-type/waf-bypass.md) |
| 重置邮件 URL 污染：页面跳转与已交付令牌分开 | 已复用图片文字描述改变重置 URL host、空值及 target.com.evil.com 等候选，但没有真实邮件交付或 ATO。 | [方法条目](../by-type/authn-session.md) |
| SMTP 源码与 mysql.env：字段可见、秘密有效和权限范围分开 | PHPMailer 图含 SMTPAuth/TLS587、遮挡 host/Username/Password 及 SMTPDebug3；另图浏览器 mysql.env 可见连接/数据库/root 用户与 password 字段。 | [方法条目](../by-type/info-secrets.md) |
| phpMyAdmin setup 的 Critical 标签不能覆盖范围与真实能力 | 正文称 phpmyadmin/setup 被 out of scope/Informative 关闭，图列表却标 unauthenticated setup 为 Critical。 | [方法条目](../scope-and-rules.md) |
| 普通与特权 resetPwd 路由：恢复主体资格不能只靠后缀 | 复用历史八步图从 /api/u/resetPwd 到 /api/su/resetPwd，涉及用户名固定后缀和可预测密码叙述。 | [方法条目](../by-type/authn-session.md) |
| Firefly 行为反馈：新响应先去噪再追踪消费者 | 图流程 configure input/request template/payload tamper/filter→行为验证→memory storage→fuzz engine→new behavior 收集/display/output。 | [方法条目](../targeted-fuzzing.md) |
| xargs 批量 xray：URL 是数据、报告输出须每目标隔离 | 保存命令把 urls.txt 的行插入 sh -c 字符串，选 cmd-injection/sqldet/xss 插件并固定 vuln.html。 | [方法条目](../discovery/records-and-incremental.md) |
| 超长前缀绕 WAF：总请求预算与检测截断位置对应 | 正文建议 POST/PUT/PATCH 参数前加 8KB–10MB 无用字符。 | [方法条目](../by-type/waf-bypass.md) |
| introspection 转 Postman 请求：schema 存在与对象权限分开 | 正文建议把 GraphQL introspection 结果交给 Postman 构造 queries。 | [方法条目](../by-type/graphql.md) |
| AI 产品选靶列表：推测、采用数据与范围授权不得混同 | 四图 ChatGPT 列 Web 应用、MFT、VPN 产品并建议 IBM ID/license 到 Fix Central 下载；含类别重叠和被裁剪列表。 | [方法条目](../hunting-strategy.md) |
| Python 模板类索引读取：引擎可达与类表顺序各有前提 | 正文 POST desc 里含 __class__.__mro__[2].__subclasses__()[40] 读取文件的历史候选及示意 cookie。 | [方法条目](../by-type/ssti.md) |
| 三阶段 XSS 示意：用户浏览器能力不自动成为系统控制 | 图画攻击者输入代码、页面返回给用户，再写攻击者获得用户数据或系统控制。 | [方法条目](../by-type/xss.md) |

| 子域候选生成、DNS记录与持续监控的覆盖边界 | assetfinder/subfinder 输出合并去重再送接管检测器，只构成候选发现链；名称命中或服务指纹不证明资源可认领。 | [方法条目](../discovery/records-and-incremental.md) |
| 可视化扫描模块中的请求、匹配和跟随重定向语义 | 可视化模块展示路径、请求头、payload和never/relative/always重定向选项；语法验证只排除格式错误，不等于漏洞语义正确或与Nuclei执行器一致。 | [方法条目](../targeted-fuzzing.md) |
| DNS rebinding 的解析检查与连接目标时序证据 | 保存卡片描述先解析为公有地址通过黑名单，再解析到元数据地址；另图分别出现Invalid IP address和EC2ws元数据JSON。 | [方法条目](../by-type/ssrf.md) |
| 从前端脚本和旧版 API 发现后台功能的证据链 | 阅读已授权应用的JS可找未被字典猜出的路由、管理/支持功能与旧版API。 | [方法条目](../discovery/web-and-api.md) |
| 默认凭据清单必须落到产品版本与部署条件 | 默认账号表属于候选，不是任何同品牌产品都存在的有效凭据；记录产品、版本、首次安装/已修改状态及对应服务。 | [方法条目](../by-type/authn-session.md) |
| 输入长度与编码变化下的 SQL 延时探针 | 保存帖给出短XOR/sleep表达式并提到XML编码，只有候选语法没有后端成功响应。 | [方法条目](../by-type/sql-injection.md) |
| 邮件头注入需区分头字段拼接与普通邮件正文 | 保存正文把邮件注入笼统写成向邮件服务器发送恶意代码，但没有具体例子。 | [方法条目](../by-type/crlf-response-splitting.md) |
| AWS 访问控制清单与 S3 列举报告的不同边界 | AWS清单列S3权限、CloudFront/S3接管、计算应用、主机网络加固与服务凭据提权，作为独立审查维度。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 重定向参数转脚本执行的参数名与解码差异 | 正文先写redirectUrl，截图实际是returnUrl，复现必须以实际请求字段为准；保存的//evil,org含逗号也不能当有效攻击域名。 | [方法条目](../by-type/open-redirect.md) |
| 从参数反射、JWT 解码到浏览器执行的分层判据 | pagenum截图可见参数闭合JS字符串并使用数组索引/call调用，另图弹窗1；该实例支持该JS上下文执行，不能把表达式套到HTML属性或JSON。 | [方法条目](../by-type/xss.md) |
| 编码和后缀变体测试必须先保证基线语义一致 | base64截图的etc/passwd与解码后/etc/passwd有前导斜线差异，403变200混入路径变量，不能直接归因base64绕过。 | [方法条目](../by-type/waf-bypass.md) |
| 对象权限、注册用户标识与会话秘密的区分 | 浏览器view-source可辅助找对象字段，IDOR必须证明当前身份没有对目标对象的授权；报告P3标签不能补足请求。 | [方法条目](../by-type/idor-access-control.md) |
| Java Random 重置令牌预测需验证生成器与完整消费链 | PoC控制台声称恢复种子并预测下一令牌、尝试密码，但没有HTTP交换或成功登录证据。 | [方法条目](../by-type/authn-session.md) |
| 互联网服务索引、Argo 与 Splunk 信息响应的认证上下文 | Shodan结果提供服务候选并可能陈旧，必须核对归属、当前暴露及授权范围。 | [方法条目](../by-type/info-secrets.md) |
| 服务端原型污染 JSON spaces 探针的版本与归因限制 | 截图文章以__proto__写json spaces使响应JSON缩进改变，代码经app.get读取settings继承值；这是污染入口→继承读取→序列化行为变化的特定链。 | [方法条目](../source-audit.md) |
| 将 CVSS、EPSS、已利用清单与资产上下文分开排序 | 保存正文的工具把NIST CVSS、FIRST EPSS、CISA已利用清单组合，图中还有OpenVAS资产统计。 | [方法条目](../hunting-strategy.md) |
| 工具目录与侦察链按输入输出职责选择 | 社区目录和工具清单可用于候选选型：Amass/Subfinder等发现名称，Gau/Hakrawler等找URL，httpx探活，Nmap查服务，ffuf定向字段测试，Aquatone辅助截图；Uncover/Gotator等按实际版本输出另核对。 | [方法条目](../hunting-strategy.md) |
| Frida 与代理证书准备不等于 Android 解密成功 | 教程图片展示adb推送frida-server与权限设置、导出Burp DER并按脚本约定命名；这是准备步骤，没有启动server、进程连接、hook命中或代理解密证明。 | [方法条目](../by-type/mobile-android.md) |
| 旧 JWT 刷新与新 token 主体绑定 | 复用图片展示JWT历史故事中的旧token刷新与账户主体关系，属于候选链。 | [方法条目](../by-type/jwt.md) |
| IMDSv2 SSRF 标题不能由付款回执补足 | 正文提到经EC2元数据的SSRF/IMDSv2，现有图只是付款通知。 | [方法条目](../by-type/ssrf.md) |
| GraphQL 范围、模式发现与邮件流程授权分开确认 | 帖子声称范围外GraphQL发邮件可批量ATO，图只有P1接受/升严重性通知；另有introspection和自动化外链与logo。 | [方法条目](../by-type/graphql.md) |
| 主应用深挖与广域侦察的成本分配 | “侦察陷阱、只挖主应用”是方法偏好，不是停止资产发现的普适结论。 | [方法条目](../hunting-strategy.md) |
| 远程文件包含样例依赖 include sink 与历史配置 | 图片只有page参数远程URL、单/双编码和空字节变体。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 代码仓库令牌与环境变量泄露的权限证据 | 员工公开仓库、主组织仓库和getEnvVars仅是发现位置候选。 | [方法条目](../by-type/info-secrets.md) |
| 费用优惠重复消费是幂等状态缺失，不必需要竞态 | Stripe公开报告图片描述20,000费用优惠的接受操作调用30次应用30份，并明确说竞态不必要。 | [方法条目](../by-type/business-logic.md) |
| 历史 curl 多头压缩链的总额度限制 | CVE-2023-23916截图说明解压链上限按每个header计数，多个Content-Encoding/Transfer-Encoding可能绕过总体限制而造成大量内存或错误；每次传输要启用默认关闭的自动解压。 | [方法条目](../discovery/client-and-cloud.md) |
| 历史 curl CLI 顺序与并行 HSTS 的两种状态错误 | CVE-2023-23914描述同一CLI命令顺序多URL没有携带首HTTPS响应形成的HSTS状态；23915描述--parallel多传输缓存被最后完成传输覆盖，后续早期主机HTTP不再升级。 | [方法条目](../discovery/client-and-cloud.md) |
| 报告附件不限制扩展名与支持人员打开文件的执行边界 | 公开报告图片称附件扩展/大小未验证，提出支持人员打开恶意文件的影响；这与文件在服务器作为脚本执行是不同链。 | [方法条目](../by-type/file-upload.md) |
| Drupal install.php 可达与重安装保护分开验证 | 截图报告返回200，同时承认安装流程不可继续，却推测重安装、DoS和PluginNotFoundException提权。 | [方法条目](../discovery/web-and-api.md) |
| POST 与跨站触发 XSS 的交互和域名边界 | 公开POST报告fld_displaytype经字符串闭合进入accesskey/onclick，正文称另一域名未被WAF覆盖；必须核对真实响应上下文、点击/快捷键交互及受影响域名在范围内。 | [方法条目](../by-type/xss.md) |
| CORS 反射 origin 与带凭据敏感读取的浏览器对照 | CORS应结合SOP理解：服务端许可哪些origin读取响应；不是任何跨站请求都被禁止。 | [方法条目](../by-type/cors.md) |
| WordPress load-scripts 聚合端点的资源上限审查 | CVE-2018-6389历史报告把大量注册JS聚合到load-scripts.php，推测重复加载导致资源消耗；截图没有可用性和负载曲线。 | [方法条目](../discovery/web-and-api.md) |
| AI 生成公司与移动应用清单只能作为待核验候选 | 截图的母子公司推理反向、应用重复且iOS ID前后不同；没有权威所有权或商店开发者核验。 | [方法条目](../scope-and-rules.md) |
| WebSocket 双向连接不等于每条消息已授权 | 已保存正文把WebSocket定义为客户端与服务器的持久双向通信；封面与外部writeups没有更多步骤。 | [方法条目](../discovery/web-and-api.md) |
| 源站、调试日志与 SVN 元数据的实际内容边界 | 失效子域的源站IP仍可能响应，但IP需归属和范围核对，TLS/vhost返回通用页面不能算目标恢复。 | [方法条目](../by-type/info-secrets.md) |
| 项目选择需按资产资格和处理记录，不按截图奖励差价 | 截图里Chainlink历史计划合约/Explorer/Faucet有资格，主站和通配不奖励；另一平台快照含主站且奖励表不同。 | [方法条目](../scope-and-rules.md) |
| Nextcloud 消息过期的可见性与 cron 依赖 | CVE-2023-26041公开报告标题明确cron配置不当，步骤设置消息60/120秒过期、等待再打开会话。 | [方法条目](../by-type/business-logic.md) |
| PCAP GeoIP 分析输出与真实位置之间的距离 | IpGeo图片展示读取pcap、剔除地址、逐IP分析和export成功，未展示导出结果或定位准确性。 | [方法条目](../discovery/passive-and-services.md) |
| 状态、补充信息和重复结论必须按时间保存 | 正文时间线提交后提供视频、补充信息，最终Duplicate，说明先确认/triaged也可能变更。 | [方法条目](../reporting.md) |
| 公开服务台与 CMS 自注册入口的角色和数据授权 | Jira UsersAPI文档提示权限、登录页signup与Netlify CMS公开注册都是授权模型核对线索。 | [方法条目](../by-type/idor-access-control.md) |
| JSON-RPC 调试管理方法应与普通查询隔离 | IOVLabs2018报告以eth_blockNumber读块号再调用evm_reset，正文称挂起、504和退回块0；截图只有最初查询响应片段。 | [方法条目](../discovery/web-and-api.md) |
| 登录与 OTP 限流的计数主体和业务后果 | 正文对无限尝试/绕过限流笼统给Low，但严重性要结合操作类型、凭据熵、计数键、重置/登录结果及其他防护。 | [方法条目](../by-type/authn-session.md) |
| APKHunt 静态 MASVS 线索与动态权限确认 | 帮助图说明APKHunt单APK/目录与日志选项、Linux及jadx/dex2jar/go/grep依赖，没有扫描结果。 | [方法条目](../by-type/mobile-android.md) |
| 镜像扫描、仓库管理与漏洞验证的职责区分 | Docker帖子列Trivy、Clair、Harbor、Grype、Dagda等仓库；这些项目角色不同，Harbor包含仓库管理与集成扫描能力，不能全部视为同一种独立扫描器。 | [方法条目](../cloud/container-k8s-security.md) |
| XML-RPC pingback 入口与 SSRF 出站能力的分离 | 正文提到WordPress XML-RPC pingback，图片是CSIRT感谢信而无方法调用或出站响应。 | [方法条目](../by-type/ssrf.md) |
| Blind stored XSS、CSRF 与 ATO 的独立触发链 | 联系表单blind stored XSS与电商CSRF ATO标题没有保存外链步骤。 | [方法条目](../by-type/csrf.md) |
| 注销、密码重置与客户端响应篡改的服务端确认 | logout invalidation、reset poisoning和OTP response manipulation保存为题名或简短描述。 | [方法条目](../by-type/authn-session.md) |
| 第三方服务识别与搜索引擎比较保留未知项 | 保存帖建议识别第三方应用/服务节省时间，具体指示器的续篇未保存；Shodan用于扩展服务候选，GNOD用于比较搜索引擎。 | [方法条目](../discovery/passive-and-services.md) |

| 协作介绍、业务反例与思路恢复的记录方式 | 合作时说明可贡献的技能/时间和期待的互补能力，比只说noob更能形成具体任务；这是保存帖的协作建议，不代表授权他人测试。 | [方法条目](../hunting-strategy.md) |
| 命令注入示意中的 shell 消费与进程权限 | 教学图把表单输入连接full system control并列多个OS，未展示实际shell调用。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 数据库错误、扫描初始阳性与最终误报结论分开 | Incapsula相关图先见SQL Server ODBC11未闭合引号/语法错误，Burp标SQL injection；sqlmap随后明确false positive/unexploitable和notinjectable。 | [方法条目](../by-type/sql-injection.md) |
| Dashboard 索引与默认 admin 候选的身份边界 | 保存Shodan ssl target/title dashboard查询只是证书/标题候选，admin:admin需落到具体产品、版本、初装或未改配置。 | [方法条目](../by-type/authn-session.md) |
| 401/403 返回变化与真实授权绕过的区别 | 保存正文将401概括为凭据缺失/无效、403为权限不足，并把所有绕过标High；真实服务还可能因网关/WAF/匿名策略返回相同代码。 | [方法条目](../by-type/idor-access-control.md) |
| XMLParser 教学图不能替代实际库版本与实体行为 | 图混合xml.etree.ElementTree/fromstring、XMLParser、defusedxml及文件实体读取示意，正文指CVE-2021-29410但没有受影响代码/版本日志。 | [方法条目](../by-type/xxe.md) |
| 登录源码、搜索路径与配置文件曝光的敏感性确认 | 登录页源码与GitHub扩展名/regex搜索可找候选，但公开前端API标识不必是秘密；API key/GIPHY权限只见报告标题。 | [方法条目](../by-type/info-secrets.md) |
| 不可信 PHP unserialize 调用与 gadget 触发之间 | 表情图给unserialize($_GET[param1])，外链源码未保存。 | [方法条目](../by-type/deserialization-rce.md) |
| Google Home 历史账号绑定场景的同网与安装前提 | 保存图片场景要求受害者安装恶意Android app，同LAN经mDNS发现Google Home，并称两HTTP请求把攻击者账号链接设备；未展示两请求或音频证据。 | [方法条目](../by-type/iot-security.md) |
| ffuf 路径输出的筛选与 JSON 提取误差 | 图脚本遍历hosts后仅匹配200、过滤1行、自动校准，再以grep/cut取JSON url；没有实际结果。 | [方法条目](../targeted-fuzzing.md) |
| 文件参数、Web 配置和 proc cmdline 的独立读取证据 | get_file.php图片从视频路径尝试系统路径、遍历，再.htpasswd/.htaccess，只有称成功的文字无响应；文件存在、基目录、权限和读取/包含sink都需确认。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 发票备注 HTML 表单与浏览器自动填充的交互条件 | Stripe历史报告图片描述memo插入透明输入表单及按钮，已有保存凭据可能自动填充后经GET提交。 | [方法条目](../by-type/xss.md) |
| Nextcloud 再分享权限不得扩大原分享下载能力 | NC25/CVE-2023-25821截图链为user1给user2可再分享但不可下载，user2给user3后PUT下游share更改下载权限。 | [方法条目](../by-type/idor-access-control.md) |
| 混合命令便笺先按权限、目的与输出敏感性拆分 | 现有图混合日志观察、SMB/SID枚举、进程/转储/strings、SSH转发、Web配置/组文件、WP扫描与PHP序列化载荷，还有禁用防护和凭据工具命令。 | [方法条目](../experiment-design.md) |
| Wireshark 显示过滤图用于证据定位而非证明解密 | 导图按帧/Ethernet/ARP/IP/ICMP/TCP/UDP/HTTP/TLS等分组并列逻辑/比较操作；细字段需按实际版本与流量类型核对，不全量照抄小字。 | [方法条目](../discovery/passive-and-services.md) |
| WAF 429 和重置邮件限流分别记录计数与副作用 | 正文观察同IP10秒10请求后429，只说明该窗口/操作被阻断，429期间枚举结果不能当不存在；减速和有限窗口复测须符合范围。 | [方法条目](../by-type/authn-session.md) |
| 低代码连接身份、应用操作人和审计主体的三层边界 | 图片保存低代码十类历史风险目录，具体例子是全部查询使用开发者数据库身份、员工表单写个人邮箱，以及管理员运行app导致开发者权限提升。 | [方法条目](../business-modeling.md) |
| 请求观察、JS 路径正则与新增域名只产出候选 | 观察页面请求/第三方服务器，读取JS路径并跟踪最近新增域名可发现入口；JSFinder Find50URL图片与Angular正则提取不是漏洞证明。 | [方法条目](../discovery/web-and-api.md) |
| 登录注销 rurl 与转 XSS 的两个验证层 | Expedia历史报告提到rurl，图片默认logout1请求、响应底部仅200，没有改参跳转结果；其他转XSS外链全文未保存。 | [方法条目](../by-type/open-redirect.md) |
| document.write 和 URL hash eval 的源到 sink 条件 | document.write静态写入脚本只是演示，漏洞需不可信source进入sink；SVG onload→eval(location.hash.slice(1))再append外部script也先依赖允许SVG事件/JS执行。 | [方法条目](../by-type/xss.md) |
| 移动 deeplink 授权码劫持须闭合 PKCE 兑换绑定 | Shop/Outlook历史摘要说明恶意app同自定义scheme可截取code，工程师加PKCE缓解。 | [方法条目](../by-type/oauth-oidc.md) |
| Android 回调 intent 路由与 OAuth 会话各自验证 | 移动回调审查先确认自定义scheme/intentfilter、系统实际解析到哪一测试app及App Link验证，再确认OAuth交易绑定。 | [方法条目](../by-type/mobile-android.md) |
| iOS 自定义 URL scheme 与授权码消费者的分离 | 历史Shop报告把iOS Xcode登记scheme与Android intent并列；自定义scheme声明不是唯一所有权保证，但是否劫持要看实际系统路由/用户选择、Universal Link验证和交易上下文。 | [方法条目](../by-type/mobile-ios.md) |
| 模板库、模块分类与移动管道的匹配证据 | Nuclei/ Vidoc仓库封面和模块库显示分类/数量，不给规则语义；Termux图显示Katana0.0.3→Nuclei2.8.9的模板/目标计数和CVE命中。 | [方法条目](../targeted-fuzzing.md) |
| Nextcloud 登录流 v2 的授权诱导与 token 轮询边界 | 报告图片state为Informative，而转发正文只强调Medium；真实处理状态不能删掉。 | [方法条目](../by-type/desktop-client.md) |
| 共识 liveness 描述必须绑定协议和故障阈值 | 保存帖给PoS/DPoS liveness denial定义、宣称High但无具体协议或步骤。 | [方法条目](../by-type/smart-contract.md) |
| 客户端免费转付费展示与服务端权益状态分开 | 保存帖声称响应篡改从免费功能提升到付费计划，外链没有保存过程。 | [方法条目](../by-type/business-logic.md) |
| 宽范围项目预设与授权边界仍须逐请求核验 | Caido帖子提出每计划独立project、scope preset与replay集合，有助将请求和证据组织到对应范围。 | [方法条目](../scope-and-rules.md) |
| AI 故意脆弱示例需要逐标签验证并隔离运行 | 正文建议模型生成DOMXSS等练习，图片document.write拼prompt确有输入sink候选，但redirect_url固定example.com只附query，不能标开放重定向；abc123是示意字符串，不是现实API秘密。 | [方法条目](../by-type/ai-application.md) |
| 邮件未验证能进面板与真实业务资格的区分 | Stripe历史截图说明classic注册未验证可进dashboard但只能testdata，真实invoice/payment受限；Connect部分只见authorize起始，后文裁切不能补成功链。 | [方法条目](../by-type/authn-session.md) |
| Blind XSS 页面秘密检测扩展的回连和数据最小化 | 正文称XSSHunter fork集成Trufflehog、750余检测类型、完整截图与通知；图片只有仓库封面。 | [方法条目](../by-type/xss.md) |
| HTTP 请求走私需证明前后端解析分歧和连接关联 | 保存定义指出代理/服务器解释HTTP请求不同，封面不含载荷。 | [方法条目](../by-type/request-smuggling.md) |
| Docker 基线检查、监测与逃逸工具列表的角色拆分 | 列表含docker-bench/CIS/Lynis/Wazuh以及botb/Gorsair/ccat/deepce等外链，没有实际规则输出。 | [方法条目](../cloud/container-k8s-security.md) |
| Hook URLSearchParams.get 的执行路径与 DOM XSS 判据 | Eval Villain图示hook URLSearchParams.get得到参数名和stack，亦列eval/HTML/定时器等hook；优点是找被当前页面执行路径读取的名称。 | [方法条目](../by-type/xss.md) |
| Rocket.Chat 管理员原型污染与托管宿主权限边界 | CVE-2023-23917历史摘要明确原型污染到RCE在admin账户下，用户能自建云server当admin，可能影响云基础设施；没有source/gadget代码。 | [方法条目](../by-type/prototype-pollution.md) |
| SSRF 图谱按输入入口、解析目标与协议消费者拆分 | 大图给文件/HTML/PDF/图片渲染、ffmpeg/M3U8、XXE/SVG、URL上传/preview/callback和代理头等入口候选。 | [方法条目](../by-type/ssrf.md) |
| SSRF scheme、文件与云元数据的运行时前提 | 图列HTTP/HTTPS、FTP/SFTP、file、Java jar/netdoc、gopher/ldap与UNC/NetNTLM等；消费者是否支持scheme、网络策略和操作系统权限必须逐项确认，不能套任意URL字段。 | [方法条目](../by-type/ssrf.md) |
| 短链历史、证书 JSON 与参数采集的一致性 | waybackurls短链→httpx location只输出历史候选/导航目标，官方专用短域仍可能跳第三方；先核对范围、时间和最终host，不声称必有秘密。 | [方法条目](../discovery/records-and-incremental.md) |
| 预登录 XSS 改写表单的本地证据和用户提交前提 | 正文用querySelector(form)修改method为GET、action指向外部，图片依次显示错误页、带script的error参数与输入框、本地127.0.0.1 HTTP server收到演示用户名/密码查询。 | [方法条目](../by-type/xss.md) |
| CRLF 文本视图与 hop-by-hop Location 消费链 | Akamai图片只解释CRLF分头及空行分正文，虽然UI标HTTP/2，线上HTTP/2头帧不等于该HTTP/1风格文本。 | [方法条目](../by-type/crlf-response-splitting.md) |
| shop 字典候选、模板命中与域绑定所有权 | 正文建议将shop加DNS字典，图片页面写Subdomain Takeover PoC。 | [方法条目](../by-type/subdomain-takeover.md) |
| Argo CD 分片 reconciliation 必须执行命名空间限制 | CVE-2023-22736历史摘要描述sharding启用时controller忽略Application namespace glob，argocd-*限制下other命名空间对象被reconcile；只有对象更新触发，攻击者需能更新Application。 | [方法条目](../cloud/container-k8s-security.md) |
| WAF 变体分类与实际语言语义分开验证 | 卡片列大小写、URL/Unicode/HTML、混合/双编码、注释、glob、垃圾字符、CRLF和未初始化变量；正文把WAF称应用层过滤并标Low。 | [方法条目](../by-type/waf-bypass.md) |
| 账户 ID 改邮箱到重置接管的主体绑定链 | 保存帖步骤为注册两账户、设置里替换ID/邮箱、邮箱改变后重置；图片仍Pending-program-review/Critical，未展示请求或登录。 | [方法条目](../by-type/idor-access-control.md) |
| 安全响应头按资源与浏览器行为验证，缺头不等于漏洞 | 两页表列nosniff、旧X-XSS-Protection、XFO/CSP、HSTS、Referrer-Policy等。 | [方法条目](../discovery/web-and-api.md) |
| no-cache、no-store 与内容下载策略的独立含义 | 表中Cache-Control区分no-cache重用前验证和no-store不存储；Content-Disposition控制inline/attachment，CORP限制跨origin资源消费。 | [方法条目](../by-type/cache-deception.md) |
| 自定义 X 头、压缩与 CORS 方法声明不是安全授权 | 表将X-*、Content-Encoding、ACAO/ACAM与多种攻击相连，不能据标签推因果。 | [方法条目](../by-type/cors.md) |
| Word RTF 字体表 PoC 的生成数据与利用结论分离 | 保存Python表达式生成RTF fonttbl，range(0,32761)写大量编号字体项并称CVE-2023-21716；没有解析器栈、崩溃或执行记录，代码未在本轮运行。 | [方法条目](../by-type/document-rendering.md) |
| 报告数量、历史战绩与状态变化保留原始口径 | 60条/8项目、45余XSS/33triaged、13条无奖励及历年click-ATO都是作者叙述，不提供独立复现或成功率分母。 | [方法条目](../reporting.md) |

| Spring 页面识别与工具写入日志的证据差距 | 普通登录页无法识别Spring/Tomcat版本；Spring4Shell脚本打印修改日志路径、写webshell的成功信息仍只是工具自报。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Stripe 历史对象输入与已知密码的条件链 | 历史报告将对象输入异常、MySQL查询语义和登录认证组合，前提是使用MySQL且已知库中一个有效密码，可来自自注册账户。 | [方法条目](../by-type/sql-injection.md) |
| 组织与管理控制台指纹是服务候选 | Shodan的org/http.title及WSO2、RocketMQ等控制台关键词只用于定位候选服务。 | [方法条目](../discovery/passive-and-services.md) |
| 历史 URL 到 XSS 工具链须保留每个过滤阶段 | wayback/gau→gf→去重→参数替换→反射检查→Dalfox/Gxss等是候选流水线。 | [方法条目](../by-type/xss.md) |
| JSON 修改密码与 HTML 表单序列化的边界 | 去掉enctype后HTML表单默认application/x-www-form-urlencoded；HTML实体在属性中解码，不把email/new_password自动转换为JSON。 | [方法条目](../by-type/csrf.md) |
| 文本正则与子域标签层级只能做候选整理 | 简短URL正则缺连字符、端口、百分号、片段等合法结构；com后缀的grep标签数也不是注册域/公共后缀识别。 | [方法条目](../discovery/passive-and-services.md) |
| SAML 的 XML 解析与签名绑定需分别核对 | 实体及XML属性是解析候选，签名绕过则取决于验证的节点与最终消费的断言是否同一个对象。 | [方法条目](../by-type/saml-sso.md) |
| Pages 符号链接读取需限定实际租户边界 | 历史Cloudflare Pages摘要称构建脚本可借宽泛文件权限与符号链接读取配置/环境，但明确仅限同一用户站点变量。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 单次 SLEEP 时延与 SQLSTATE 不等于布尔盲注 | 图片给含SLEEP(5*2)的表单请求、SQLSTATE[21000]和约10.4秒耗时。 | [方法条目](../by-type/sql-injection.md) |
| 特殊字符引起的错误须回到功能语义 | 先理解字段预期类型、状态及业务操作，再一次只改变一个字符或编码，记录解析层、状态码、响应内容及服务端影响。 | [方法条目](../experiment-design.md) |
| 邮箱评论与引号语法不能代替下游注入证明 | 邮箱输入可能经过引号、括号评论和规范化再进入不同消费者。 | [方法条目](../discovery/web-and-api.md) |
| 搜索词拆分仍可能保留 SQL 表达式语义 | 历史H1 CVE搜索报告描述空白拆词后未额外消毒，真假布尔条件对应正常结果/无结果。 | [方法条目](../by-type/sql-injection.md) |
| 对象删除与图片覆盖必须绑定操作人及资源所有者 | GraphQL DeleteStorySnaps的variables.ids及上传图片文件名/id都是对象引用候选。 | [方法条目](../by-type/idor-access-control.md) |
| 奖励、报告关闭与实际修复是独立状态 | 图片显示项目在修复仍需时间时关闭报告并奖励，后续还请求帮助验证。 | [方法条目](../reporting.md) |
| 搜索与默认内容路径须区分公开设计和暴露 | Dork菜单、云存储/Drive/Googleapis搜索及Drupal/node数字路径只形成候选。 | [方法条目](../discovery/web-and-api.md) |
| 历史 DNS 与证书 IP 不自动绕过 Cloudflare | 旧A记录、证书CN关联IP可提示候选源站，但可能过期、复用或第三方资产。 | [方法条目](../discovery/passive-and-services.md) |
| 聚合项目清单与 shell 一行脚本不能替代授权 | 公开全部program域名的仓库不是授权政策；按具体项目当时政策、排除、速率和资格再生成目标。 | [方法条目](../scope-and-rules.md) |
| PII 与密钥检测的匹配规则需要可核验证据 | DataSurgeon/Bearer/NoseyParker的文本、目录或git历史扫描声明只构成工具线索。 | [方法条目](../by-type/info-secrets.md) |
| 客服固定密码重置需验证身份核验与生命周期 | 图述支持Telegram渠道按用户ID给统一固定密码，机制候选是客服重置未核验身份且密码可预测/共享。 | [方法条目](../by-type/authn-session.md) |
| SecurityTrails 子域 API 结果要验证结构和后缀 | 历史图以jq读取.subdomains[]后拼目标后缀；先检查HTTP/API错误、配额、返回schema和空列表，再按相对/完整域形式规范化并保存原始来源时间。 | [方法条目](../discovery/passive-and-services.md) |
| 数量为小数须匹配商品计价与履约规则 | 数量1报价234而0.1报价23.4仅说明乘法计价。 | [方法条目](../by-type/business-logic.md) |
| 自动 recon 的密钥与接管标签均需人工确认 | 正文Gank而窗口kold-recon的名称差异保留。 | [方法条目](../by-type/subdomain-takeover.md) |
| 搜索筛选参数 XSS 的弹窗与账户影响分级 | 历史USDoS segFilter报告有候选URL及嵌入弹窗图，Resolved/Medium4.7。 | [方法条目](../by-type/xss.md) |
| 历史优惠券和到期套餐须验证资格与最终订单 | Wayback coupon URL及89.99减29.70/45/9的报价只提供不同优惠候选，图为试用结束应付款。 | [方法条目](../by-type/business-logic.md) |
| npm 静态资源接管与供应链影响应分两段验证 | 正文assets.npm.com与图assets.npmjs.com不同；面板High/Resolved约2000和aws-bucket模板通知只是历史记录。 | [方法条目](../by-type/subdomain-takeover.md) |
| SSRF 影响不能由漏洞标签统一定为 High | 输入URL触发服务器请求是机制候选，需固定源字段、解析/重定向/DNS规则、协议和出网身份，用受控接收器与禁止目标对照定位实际请求。 | [方法条目](../by-type/ssrf.md) |
| Mail OAuth 设置中间态的明文存储窗口 | 历史Nextcloud Mail CVE-2023-23944摘要指XOAUTH2设置期间密码列临时明文，完成后存加密access token，平常密码也加密。 | [方法条目](../by-type/info-secrets.md) |
| 范围快照和 API 导出须保留政策时间与例外 | 历史H1变更页分别显示资产最大严重度、in-scope和bounty；API wildcard导出/grep清单会遗漏政策文字、排除、资格和动态变化。 | [方法条目](../scope-and-rules.md) |
| StackOverflow 名称不是 SQL 注入结论 | 原帖把SQLi与StackOverflow关联但没有请求、后端查询或技术链。 | [方法条目](../by-type/sql-injection.md) |
| Spring suffix 路由与容器 URL 约束不一致 | 图中Tomcat web.xml仅约束/adminURL及/adminURL/，Spring suffix匹配让/adminURL.PTSWARM映射相同控制器；图对照403与200 Hello Admin。 | [方法条目](../by-type/idor-access-control.md) |
| 浏览器 file 导航与服务器文件读取属于不同主体 | view-source:file之类浏览器本地导航依赖页面origin、导航触发及客户端策略；它并未要求远端服务器读取文件。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 备份路径与目录索引要落到实际非公开内容 | admin.tar.gz、BackupBuddy local-download参数及目录列表只提示读取面。 | [方法条目](../by-type/info-secrets.md) |
| 依赖混淆须追踪私有名称到真实构建消费者 | 被截断的创建私有包建议不足以说明哪个registry、namespace、解析优先级、lockfile或构建执行。 | [方法条目](../discovery/client-and-cloud.md) |
| 复用漏洞模式需要逐目标独立消费者验证 | 从已验证案例抽出可控字段、消费者、信任边界与最小对照，再映射其他许可应用，记录每个新目标的前提差异与失败原因。 | [方法条目](../hunting-strategy.md) |
| Grafana CVE 标识不一致先保留来源差异 | 正文CVE-2021-43789而仓库卡/链接是43798，不能合并成已确认漏洞标识。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Spark doAs 候选需要权限与实际消费者条件 | 原帖doAs中的命令替换及sleep只给候选输入，没有配置、认证/代理身份或回包。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 自建落地页与链接注入需证明上游信任链 | 自己控制的404页面可演示落地视觉，但不能证明源站开放重定向；DOM链接或PDF超链接注入也须实际渲染/用户动作/最终导航证据。 | [方法条目](../by-type/open-redirect.md) |
| 参数反射识别与脚本执行是两道验证 | 参数发现/反射工具须保留请求、输出位置、编码和DOM消费路径，比较无特殊标记及等价编码。 | [方法条目](../by-type/xss.md) |
| 子域枚举后的排列不能计为已发现资产 | subfinder/amass/findomain与gotator/dnsgen/altdns分别是枚举与名称生成阶段。 | [方法条目](../discovery/passive-and-services.md) |
| 命令参数词表和严重度标签只形成候选 | cmd/exec/ping/query/code/arg/module等名称不能判定执行函数。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 签发端漏验可能把无效 JWT 换成可信 token | 图述APK暴露generateJwtToken入口，用Auth-Token去签名、改user id后换出他人JWT，而其他入口仍正确验签。 | [方法条目](../by-type/jwt.md) |
| XSS 混合载荷应按语法与事件拆分验证 | 候选含SVG/xlink、实体、URL换行、大小写、pointermove和auxclick，需要逐项记录WAF解码与浏览器上下文。 | [方法条目](../by-type/waf-bypass.md) |
| Windows Runner 环境值空字节的权限前提 | 历史GHES CVE-2023-22381摘要要求已有权限控制一个GitHub Actions环境变量值且使用Windows runner，解析空字节可能注入其他环境项；图列3.4.15/3.5.12/3.6.8/3.7.5修复及3.8前范围。 | [方法条目](../cloud/container-k8s-security.md) |
| Hydrogen 的店铺与 GitHub 连接授权需共同绑定 | 历史报告前提为店铺安装Hydrogen、受害者连接含私有仓库的GitHub账户，开发攻击店可查询他人仓库。 | [方法条目](../by-type/idor-access-control.md) |
| WAF 指纹工具只能识别候选防护层 | WAFW00F的名称/输出用于定位防护候选，必须保存原始HTTP证据、CDN/代理链及版本假设。 | [方法条目](../by-type/waf-bypass.md) |
| 前端 env 的写入 key 与服务端秘密要分类 | REACT_APP前缀说明可能被打包到客户端，PostHog/Segment写入key与Stripe publishable key通常承担不同功能。 | [方法条目](../by-type/info-secrets.md) |
| APKHunt 帮助与 MASVS 标题不等于审计完成 | 图显示-p单APK、-m目录、-l日志，Linux验证及jadx/dex2jar/go/grep依赖。 | [方法条目](../by-type/mobile-android.md) |
| 反序列化标题下误贴的 HRS 定义须纠正 | Day53封面写不安全反序列化，但正文是前后HTTP服务器处理请求不同的解释，属于请求走私机制。 | [方法条目](../by-type/deserialization-rce.md) |
| 隐藏 scope 标签不能保护后端跨项目查询 | 历史H1报告称external/invite-only页面无scope tab但追加policy_scopes可见全部项目范围。 | [方法条目](../by-type/idor-access-control.md) |
| 年度 CWE 数量不能直接转成当前狩猎概率 | 2022统计图示CWE20014813、CWE795433、设计5178、访问控制1744、重定向1279；先标记时间、数据集、报告/漏洞口径、去重及分母。 | [方法条目](../hunting-strategy.md) |
| ffuf 循环变量与输出身份必须对应真实目标 | 图循环i从web-server文件读取却ffuf用$1/FUZZ，脚本位置参数并非当前循环URL。 | [方法条目](../targeted-fuzzing.md) |
| 邮箱作为 Cookie JWT 标识仍须可信验证 | 原帖Toyota提到邮箱与JWT Cookie而现有图只是Logo，没有token内容、验签或请求。 | [方法条目](../by-type/jwt.md) |
| 搜索服务类别不能自动变为授权资产 | 技术、证书、文件、代码、相机和PII搜索平台分别提供不同索引视图。 | [方法条目](../discovery/passive-and-services.md) |
| 公开 DLL 中初始化账号不等于现存超级管理员 | 图有195KB DLL下载及.NET Configuration反编译，CreateApplicationUser使用硬编码密码并AddToRole SuperAdmin，前面先检查用户是否存在。 | [方法条目](../by-type/info-secrets.md) |
| OTX 历史关联 URL 与敏感标签分别核验 | AssociatedURLs数量/100条边界属于历史索引视图，需确认分页、时间、归属、当前权限与非公开文档响应。 | [方法条目](../by-type/info-secrets.md) |
| 遗留第三方 widget 的资源接管须追踪浏览器消费 | 历史H1 /resources代理Uberflip，旧/read/page_widget/数字ID跨客户存在，有HTTP资源被混合内容挡住，另有HTTPS脚本；标题称删除S3桶导致storedXSS。 | [方法条目](../by-type/subdomain-takeover.md) |
| GraphQL schema 和控制台发现须连接 resolver 权限 | graphql/altair/playground、debug及旧版本提示可发现入口，内省有多种查询形态但不能把“两版本”当通用标准。 | [方法条目](../by-type/graphql.md) |
| 文件名变体与载荷类型应映射到具体消费者 | 双扩展/大小写、路径、SQL、SVG及shell文本只是文件名/内容候选；图中的工具遍历PHP变体和nc监听无连接。 | [方法条目](../by-type/file-upload.md) |
| XSS 工具清单需要按观察角色使用 | Firebug/JMeter等与专用XSS扫描工具用途不同，不能23个名字都当有效扫描器。 | [方法条目](../by-type/xss.md) |
| 新子域通知需要可恢复的证据基线 | Bankai历史消息和监控视频封面只显示新候选域，未展示Python实现。 | [方法条目](../discovery/records-and-incremental.md) |
| 连续等号改的是参数值而非等价请求 | file=shell.php与file===shell.php通常把额外等号纳入值，不能假设业务语义一致。 | [方法条目](../discovery/web-and-api.md) |
| 笔记组织应让候选与证据可独立追溯 | 图示Found vulnerabilities、Annotations及Exploration Map层级。 | [方法条目](../discovery/records-and-incremental.md) |
| 表达式被删除和版本敏感对象链不是 SSTI 确认 | aaaa{{8*8}}bbbb变aaaabbbb说明删除/过滤，不是计算64；Flask链config.items()[4]依赖旧Python容器可索引与对象顺序，Python3 dict_items通常不可下标，固定MRO/subclasses索引也不稳定。 | [方法条目](../by-type/ssti.md) |
| gau 选项和历史 URL 输出要保留版本与语义 | --subs等选项可能随版本，记录实际工具版本/帮助、provider、目标、输出schema及错误。 | [方法条目](../discovery/passive-and-services.md) |
| 剪贴板分块传输依赖既有会话与允许通道 | Invoke-Transfer帮助述Windows10+、120KB分块延时、Guacamole模式、base64合并及OCR；适用既有RDP/Citrix/VNC等剪贴板会话。 | [方法条目](../by-type/desktop-client.md) |
| CVE 题名和格式错误表达式不补成复现 | TabShell/Text4Shell帖子仅给题名/候选，Text4Shell字符串Runtime.get.Runtime()形态及URL里的$cmd存在语法/插值不明。 | [方法条目](../by-type/cmd-injection-rce.md) |
| textarea 与 srcdoc 需要确认具体解码和嵌套上下文 | textarea结束标签及iframe srcdoc涉及不同HTML文本/属性与嵌套文档消费者。 | [方法条目](../by-type/xss.md) |
| 重置多收件人与账户 token 绑定分别验证 | 图中JSON email转义换行连两个受控地址且两个收件箱同时间收到Password Reset，支持收件人解析线索。 | [方法条目](../by-type/authn-session.md) |
| TV 名称到 Web 登录页需界定触发人和会话 | 图片电视名称含script字符串，手机Netflix域弹窗1，提示设备元数据进入网页呈现路径。 | [方法条目](../by-type/iot-security.md) |
| Google hd 选择提示必须与组织授权解耦 | 改OAuth URL的hd参数可能更改账号选择提示，hd不是可信授权输入。 | [方法条目](../by-type/oauth-oidc.md) |
| 默认凭据线索和后台标题不能自动定 Critical | Shodan指纹、8888端口、登录页及Critical后台列表没有完整登入/管理操作证据。 | [方法条目](../by-type/authn-session.md) |
| 参数名与数组键需验证查询构造消费者 | parameter[]=123或parameter[id']=123可能改变框架解析类型/键；正文另给SQLServer WAITFOR样式嵌套键，但没有回包。 | [方法条目](../by-type/sql-injection.md) |
| Ajax spider 的浏览器数量不等于应用覆盖 | ZAP Ajax spider可通过渲染补充客户端路由，但乱码结果可能来自字符集、认证失效、资源加载或抓取范围。 | [方法条目](../discovery/web-and-api.md) |
| server-status 影响按实际非公开字段判定 | TD历史/server-status截图含当前/重启时间、uptime、负载及访问/流量计数，Resolved/Medium5.3。 | [方法条目](../by-type/info-secrets.md) |

| MySQL 报错、缓存恢复与取库失败须分开记录 | 单引号触发PDO prepare SQLSTATE42000/MySQL1064及execute on boolean，可定位查询或错误泄露候选；不能直接判P1/取库。 | [方法条目](../by-type/sql-injection.md) |
| 枚举工具集合应按来源与验证阶段拆分 | subfinder/assetfinder/amass/findomain/历史URL/GitHub等是候选来源，gotator是生成，DNS与httpx/httprobe是解析/服务验证，Nuclei是模板判别。 | [方法条目](../discovery/passive-and-services.md) |
| 随机内容去重需防止吞掉业务差异 | Afuzz正文称过滤随机内容与冗余结果，但没有配置或输出。 | [方法条目](../targeted-fuzzing.md) |
| 版权、国家后缀与 S3 搜索命中须核对归属 | 版权句、target.com.*和S3关键词检索只提示可能相关页面。 | [方法条目](../discovery/passive-and-services.md) |
| HTML 与 URL 变体须验证每层解码及事件 | 大小写、换行、双编码、嵌套移除、HTML实体、select/noembed/script及a标签6个变异点都依赖具体WAF和HTML/URL/JS消费者。 | [方法条目](../by-type/waf-bypass.md) |
| CCAI iframe 导航与共享聊天 origin 要分别证明 | 保存文章图述agent的cobrowseDomain进入iframe位置允许javascript URL且缺embedding保护；client聊天属性/Waiting message进入HTML，SDK共享websdk.ujet.co origin并信任Cobrowse/window.opener形成跨站聊天候选。 | [方法条目](../by-type/xss.md) |
| 公开报告的视频附件也需核对其他资产披露 | 历史H1报告1886143描述公开视频暴露另一公司未修复漏洞类型和subdomain，Low3.8/500/Resolved。 | [方法条目](../reporting.md) |
| 401 与 403 变体必须访问同一受保护资源 | 转发IP/重写路径头只有后端可信配置存在时才影响身份或路由；点段/分号/编码/方法/IP/虚拟主机要比较访问检查与handler的实际规范化。 | [方法条目](../by-type/idor-access-control.md) |
| 邮箱合法语法与最终 HTML 消费者分别核对 | 引号/括号评论和带HTML字样的邮箱可能通过校验后在资料页/邮件模板显示。 | [方法条目](../by-type/xss.md) |
| MFA 客户端开关不能决定服务端认证阶段 | 图对比mfa:null/code空到dashboard与mfa:true到authenticate，声称篡改后绕过。 | [方法条目](../by-type/authn-session.md) |
| Joomla public 标志与配置端点需绑定实际授权 | 帖子给CVE-2023-23752及/api/index.php/v1/config/application?public=true候选，没有组件版本/认证模式/回包。 | [方法条目](../by-type/idor-access-control.md) |
| debug 尾斜杠可能暴露不同访问检查路径 | 正文/debug为Basic401而/debug/200；现有图分别Basic挑战与ZoneInfo/instance输入页。 | [方法条目](../by-type/idor-access-control.md) |
| SSTI 的确认与评级依赖引擎和权限 | 用户输入成为模板source/指令而非普通数据才是机制；固定引擎、版本、sandbox、输入入口与渲染身份，以受控常量表达式/文字对照确认计算和实际能力。 | [方法条目](../by-type/ssti.md) |
| 测试支付模式须与生产权益和结算分开验证 | Stripe/Adyen历史测试卡列表仅是沙箱资源，经验图付款576后UpgradeSuccessful并未证明live/test模式、服务器结算或持久权益。 | [方法条目](../by-type/business-logic.md) |
| GraphQL 提取工具与 schema 公开不等于授权缺陷 | Graphicator帮助有目标header/file、proxy/Tor、insecure、multi/no-cache等配置，影响请求身份/TLS/缓存须固定记录。 | [方法条目](../by-type/graphql.md) |
| 响应 cid 篡改需证明服务端实际身份改变 | 登录返回status success/cid1后客户端改为0的描述，只说明客户端数据可改。 | [方法条目](../by-type/authn-session.md) |
| 上传文件名的注入候选必须落到具体消费者 | 路径、SQL延时、SVG和shell字样进入文件名可能分别影响存储路径、查询、下载HTML呈现或系统命令。 | [方法条目](../by-type/file-upload.md) |
| 业务逻辑测试先明确正常规则与状态模型 | 依据已保存正文先整理应用文档/商业模型、正常角色、资源与交易状态，再对每一步输入和状态转换写出预期不变量。 | [方法条目](../business-modeling.md) |
| heartbeat 扩展 grep 不能给出 Heartbleed 阴性 | 图一行把openssl s_client输出grep heartbeat id15，任何未命中都打印safe。 | [方法条目](../experiment-design.md) |
| iOS AES hook 失败要定位运行时实际调用点 | 正文只是Frida hook crypto/AES三天失败求助，没有代码或异常。 | [方法条目](../by-type/mobile-ios.md) |
| UDP discovery challenge 必须绑定实际源地址 | 历史RSKJ协议摘要称Pong仅验check却未绑定Ping同一来源，伪造源被加入连接后FindNode诱发更大Neighbors响应到第三方。 | [方法条目](../by-type/smart-contract.md) |
| grep URL 字符集缺项会让发现结果不完整 | 示例regex仅HTTP/HTTPS及少量字母数字符号，缺端口、百分号、片段等；shell引号/尾星号也需输入契约明确。 | [方法条目](../discovery/web-and-api.md) |
| stdin 串联工具须保存阶段身份与失败输出 | httpx/Nuclei读stdin能连接候选→服务→模板阶段，仍需固定版本、目标范围、schema、错误/超时和输出来源绑定。 | [方法条目](../discovery/records-and-incremental.md) |
| redirect_uri javascript 弹窗需定位导航消费者 | 图中浏览器参数为javascript字样并弹窗，但源域遮蔽、缺HTTP/DOM处理。 | [方法条目](../by-type/xss.md) |
| 参数词表与后缀拼接不代替完整跳转链 | next/url/redirect/return等25项是候选路径/参数不是搜索dork；历史JetBlue url报告Critical被调Low，缺Location/视频。 | [方法条目](../by-type/open-redirect.md) |
| FortiNAC PoC 默认 cron 副作用不是审计确认 | 帖子明示默认CVE-2022-39952脚本写cron建立反向shell，仓库卡无版本/入口/响应。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 后门帮助界面须分清已有执行权限与入口 | 有意义alt称PowerShell生成器支持设备载荷和每次build签名变化；图有listen.py私网listener、已有Admin提示及系统/网络/文件能力。 | [方法条目](../by-type/desktop-client.md) |
| 客户端模板插入输入不必然执行框架表达式 | CSTI前提是输入进入客户端框架编译/表达式求值，而非普通DOM文本或已处理数据。 | [方法条目](../by-type/xss.md) |
| 搜索提醒和 CT 监控保存候选变更契约 | Google Alerts图是indexof/contentdam/默认页等检索提醒，CertWatcher仅CT/YAML DSL题名。 | [方法条目](../discovery/records-and-incremental.md) |
| JS endpoint extractor 的全部与一秒声明需限定 | EndExt仓库卡只称Go提取possible endpoints，无parser/schema或样例结果。 | [方法条目](../discovery/web-and-api.md) |
| 代码签名扫描标签不等于文件恶意判定 | CertVerify历史引擎333签名、16文件中5标infected，需要二进制hash、证书主体/链、验证时间、吊销/泄露依据及规则版本。 | [方法条目](../discovery/client-and-cloud.md) |
| APK 关键词命中须区分练习数据与真实秘密 | accesskey/admin/AES/API/password/pinning/token/TrustManager等grep只定位代码。 | [方法条目](../by-type/mobile-android.md) |
| 远程 ZIP 目录与部分读取需确认对象边界 | remotezip候选依赖Range及ZIP中央目录/压缩和服务器支持，原帖无运行回包。 | [方法条目](../by-type/info-secrets.md) |
| 回访旧报告需确认新参数是否改变根因 | 将历史暴露路径加入候选词表时保留来源版本、路由/角色及接受状态，用新旧参数与正常/拒绝对照验证实际消费者和权限差异。 | [方法条目](../discovery/records-and-incremental.md) |
| alg none 与 claim 篡改要经过服务端验签和授权 | JWT header/claims可在客户端改动，真实缺陷要服务器接受未签名/算法不匹配并将其作为可信主体。 | [方法条目](../by-type/jwt.md) |
| 账户邮箱修改到重置接管需验证连续身份绑定 | 自有A/B账户验证A会话仅替换B id/email是否持久改B地址，再独立确认reset token绑定B、投递到受控地址、兑换后的B身份和原会话策略。 | [方法条目](../by-type/idor-access-control.md) |
| KCP ghost TLS 包要区分长度、复用与会话隔离 | 历史Tor Snowflake摘要称KCP收到其他会话TLS包，图建议ReadFrom(buf)后打印整个buf。 | [方法条目](../by-type/info-secrets.md) |
| 评级申诉要用能力证据支持每个条件 | 图从Medium6.7调High7.6/8.9，计算器向量是申诉者选择，缺XSS→ATO链。 | [方法条目](../impact-and-acceptance.md) |
| EC2 后续 shell 工具依赖既有云权限 | EC2StepShell题名声称公私EC2高权限shell，没有凭据/策略/命令结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 反射检查管道的文件与端口覆盖要独立核对 | 复用已核验图包含passive枚举、resolved过滤、httprobe81/8080/8443、wayback/kxss，domain/domains文件名不一致及追加旧数据。 | [方法条目](../by-type/xss.md) |
| OOB 菜单没有 callback 归属与漏洞确认 | OutBandit选择OS/技术/SQLi/cmd/XXE/SSTI/SSI/deser/SMTP等只设置候选，listener仍空。 | [方法条目](../experiment-design.md) |
| TLS Pass Through 降噪同时造成 HTTP 证据盲区 | 对google/gstatic/mozilla/googleapis/pki正则透传只影响Burp代理观察，TLS不解密时不能检索其请求/响应。 | [方法条目](../discovery/web-and-api.md) |
| 混合遍历词表中的文件与命令消费者分开 | Windows路径、斜杠编码、超长UTF8、cmd.exe参数及换行cat/实体候选依赖OS、URL解码与最终文件/命令处理器。 | [方法条目](../by-type/lfi-path-traversal.md) |
| wget 保存 Cookie 须先验证登录序列与身份 | 原帖命令被断行、选项单横形态/username冒号及form语义不明，没有登录回包。 | [方法条目](../by-type/authn-session.md) |
| 本地 PHP 后门执行不证明防火墙绕过 | 图PHP7.3.6由sudo在127.0.0.1启动，参数选system/id得到uid0；是已具本地root权限后的演示。 | [方法条目](../by-type/cmd-injection-rce.md) |
| URL token 与只读 key 的信息影响须按类型限定 | JWT可能可读claims而非加密，URL会进入历史/日志/Referrer；API只读权限也可能含非公开数据。 | [方法条目](../by-type/info-secrets.md) |
| Nacos 固定 token 模板须验证鉴权配置与反例 | 图GET namespaces携固定accessToken，仅200/namespaceShowName/configCount三个匹配，声明0.1.0至2.2.0范围未核证。 | [方法条目](../by-type/jwt.md) |
| 重入与静态告警要落到状态更新和调用权限 | 重入依赖外部调用回调在状态/余额更新前重入同或相关函数，效果可能资产重复转出或状态不变量破坏，不是所有重复调用均DoS/Critical。 | [方法条目](../by-type/smart-contract.md) |
| 模型报告与 curl 转换须回对原始证据 | GPT_Vuln-analyzer仅说Nmap→模型报告，curl转换只给提示与尾部JSON图。 | [方法条目](../by-type/ai-application.md) |
| BROWSABLE activity 还需验证 exported 与 URL 策略 | AndroidManifest BROWSABLE是深链接候选，核对exported/permission、action/data scheme/host/path及运行时Intent/嵌套URL处理。 | [方法条目](../by-type/mobile-android.md) |
| ImageMagick PNG 转换导出本地文件不是直接 RCE | 历史CVE-2022-44268摘要称旧ImageMagick在resize时将本地文件十六进制嵌入输出，tEXtprofile用于元数据排查；sidebar RFI与摘要localfile差异需保留。 | [方法条目](../by-type/file-upload.md) |
| curl User-Agent 与查询文字不能证明 shell 执行 | 正文反引号whoami及root子域claim缺日志；另一图DNS/HTTP callback GET查询用户名文本、curl7.84.0箭头标RCE。 | [方法条目](../by-type/ssrf.md) |
| Wappalyzer 并行指纹输出要绑定配置和目标 | 正文python3 http://main.py异常而图为本地main.py analyze；parallel50示例输出Akamai/Apache/Ubuntu/Laravel/Envoy等只指纹。 | [方法条目](../discovery/passive-and-services.md) |
| GitHub 文件名和词检索须保留 repo commit 来源 | 配置/历史/数据库/私钥文件名、API/token/password关键词只形成候选，target,com拼写差异及域关键词不保证组织归属。 | [方法条目](../by-type/info-secrets.md) |
| CSV 的 S3 上传与应用导入是两个信任阶段 | TaxJar历史图前置双账号、攻击者上传CSV，显示S3 multipart POST但签名字段与后续import裁切。 | [方法条目](../by-type/csrf.md) |
| 重置后会话撤销应比对原令牌实际权限 | 图仅Failure to invalidate session on reset/change标题、P4/unresolved/duplicate。 | [方法条目](../by-type/authn-session.md) |
| 扫描器与 Burp 扩展要按角色验证可见边界 | 15工具混模板、Web扫描、攻击框架、库识别、exploit搜索及爬虫；Autorize/AuthMatrix权限比较、BurpBounty profile、ActiveScan扩展、BrokenLink等也功能不同。 | [方法条目](../discovery/web-and-api.md) |
| 多层 API 版本路径仍需真实路由与权限对照 | /api/v1/0.0.1/users等只是候选版本结构。 | [方法条目](../targeted-fuzzing.md) |
| Werkzeug console 可见与调试执行能力分开 | 正文声称debug及console执行os.listdir，图只有PythonDebugger P1/Resolved标题。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 编码 CSS 后缀到缓存 XSS 要证明独立读者 | self email XSS→.css被挡→%2ecss200/cached需要缓存键、解码/路由、内容类型、存储资格及身份差异。 | [方法条目](../by-type/cache-deception.md) |
| EJS gadget 题名不足以证明污染到执行 | SSPP→EJS RCE外链仅题名，需分别确认可控对象合并/原型写入、受影响属性实际消费、EJS版本/配置和生成代码权限。 | [方法条目](../by-type/prototype-pollution.md) |
| Duplicate 判断须按首报时间与根因证据核对 | 邮件只称多份same issue和多个asset，正文自称首报但没有时间线/原始根因。 | [方法条目](../reporting.md) |
| Airflow Basic 默认凭据是配置与有效身份问题 | 帖子/api/v1/pools加Basic header只是默认凭据候选，没有回包。 | [方法条目](../by-type/authn-session.md) |
| WiFi capture 导入的零错误不等完整正确 | wifi_db图将已有csv/kismet等capture导SQLite，MACvendor远程DNS失败后copylocal fallback，按文件errors0。 | [方法条目](../discovery/records-and-incremental.md) |
| 奖励资格、测试范围和接受类型必须分开 | not eligible to bounty不等out of scope；资产可测性、测试方法许可、奖励资格及漏洞接受规则应分别核对。 | [方法条目](../scope-and-rules.md) |
| phpinfo 的环境字段要验证暴露身份与真实用途 | phpinfo可能泄露env，而已核验图是dev/APPSECRET/SQLite/Mailer样例。 | [方法条目](../by-type/info-secrets.md) |
| 去点域名需要真实浏览器 Origin 和可读响应 | wwwTarget.com式候选可能利用substring/regex origin检查，须核对真实可控注册域、scheme/port及浏览器Origin，记录ACAO/ACAC、Cookie/SameSite和跨站脚本能读的非公开内容。 | [方法条目](../by-type/cors.md) |
| Basic 邀请成员需校验请求者角色与受邀租户 | thread仅保存signup为admin/invite为basic及新成员邮件称Account2邀请，中段缺失。 | [方法条目](../by-type/idor-access-control.md) |
| 上传 XSS 必须确认保存和访问时的呈现上下文 | 正文仅提示upload检查，机制需输入文件名/内容在预览/下载/后台被当HTML/SVG等执行。 | [方法条目](../by-type/file-upload.md) |
| Amass 数据库与 track 参数要核对运行版本 | enum -nf用于整合候选及track的历史行为需按实际版本/帮助核验；uniq只处理相邻重复，track -d带http://形态不应当标准域输入。 | [方法条目](../discovery/records-and-incremental.md) |
| ProxyNotShell 的 404 IIS 指纹只能定位候选 | ffuf/autodiscover候选并跟随重定向匹配IIS Web Core，不足以证明CVE-2022-41040。 | [方法条目](../by-type/ssrf.md) |
| Sqoop libjars 的执行前提是连接配置与 MR 消费 | 历史CVE-2023-25693摘要<3.1.1、SqoopHook._prepare_command从Connection libjars传-libjars，让MR task classpath加载Jar。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 服务端验证字段可写需证明持久状态和受限能力 | 实际图片为注册email_verified:false→新增email_verified:true→响应true，但user/organization id不同，is_admin两图原本都true。 | [方法条目](../by-type/idor-access-control.md) |
| 重置收件人变体与 token 暴露各自取证 | 逗号/bcc/重复参数是邮箱解析候选，响应token泄露是另一阶段。 | [方法条目](../by-type/authn-session.md) |
| option 与 item 变更需证明合法商品与最终履约 | 图仅POST变更option_id/item_id、购物车FREE/0.00及High7.7/TriagedOpen。 | [方法条目](../by-type/business-logic.md) |
| CRLF 汉字字节映射与响应头须按真实序列判定 | 图标准%0D%0A400，E5988D/E5988A汉字UTF8百分字节被称GBK可过，文字200而实际图HTTP1.1 301和单独Set-Cookie marker。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 自动 token 替换不能污染身份与重试边界 | ATOR图正常token直发，错误后登录提取并替换pattern/area，新token更新内存；30/59分钟仅示例。 | [方法条目](../by-type/authn-session.md) |
| 云 IP 工作流与相似网页匹配不能授予扫描许可 | 图AWS地址范围→EC2→CIDR/批次→80/443端口→HTTP候选，再以Host/标题及Levenshtein匹配源站。 | [方法条目](../discovery/passive-and-services.md) |
| ffufr 固定 HTTP 和递归须限定输入与预算 | bash函数wordlist/$1、http://$2/FUZZ及recursion缺quote、HTTPS/端口/basepath和递归预算/输出身份。 | [方法条目](../targeted-fuzzing.md) |
| 目录索引与递归下载须确认实际非公开内容 | 图为localhost Apache/PHP目录，secret/priv/edit/config.php只是名称。 | [方法条目](../by-type/info-secrets.md) |
| IPv4 短写形式依赖校验与请求解析器一致性 | 1.1/127.1/192.168.1的inet兼容解读随库/URL标准而异。 | [方法条目](../by-type/ssrf.md) |
| TLS 证书读取需显式 SNI 与链验证状态 | ssl.create_default_context及server_hostname提示SNI和默认链校验，原代码缩进缺失且未运行。 | [方法条目](../discovery/passive-and-services.md) |
| 重定向升级链应逐个验证新的信任消费者 | OAuth token流、SSRF跟跳转、CRLF/JavaScript导航都有不同前提。 | [方法条目](../by-type/open-redirect.md) |
| BIO_new_NDEF 失败清理 UAF 需定位实际流式调用 | 历史OpenSSL CVE-2023-0215摘要：callerBIO前加ASN1 filter，invalidCMSrecipient等失败释放filter返回NULL却链留悬指针，后续BIO_pop造成UAF通常crash；涉及CMS/SMIME/PKCS7流式API而非普通TLS全部路径。 | [方法条目](../source-audit.md) |
| 盲 XSS 面板的 admin 地址与遥测 Cookie 不等角色证据 | 面板列admin URI/referrer、Mac UA/GPU、遥测session Cookie、NRBA sessionStorage和DOM片段；这些字段可能客户端自报，不保存真实值。 | [方法条目](../by-type/xss.md) |
| RCE 参数词表只生成消费者候选 | 图片列出 cmd、exec、query、code、arg、module 等 25 个参数名。 | [方法条目](../by-type/cmd-injection-rce.md) |

| Burp 请求变体、重放与差异比较分别承担什么 | 阿拉伯语正文分别介绍Intruder变体枚举、Repeater单次修改、Comparer比较和Sniper逐位置变更。 | [方法条目](../discovery/web-and-api.md) |
| A 与 MX 记录的发现用途不能互换 | 保存正文说明A关联主机IPv4，MX提供邮件交换路由。 | [方法条目](../discovery/passive-and-services.md) |
| 重复 Pending 行只提出竞态与幂等性候选 | 列表中同一名称/站点在同分钟出现多条Pending，但没有原始并发请求、请求ID、重试或业务唯一性规则。 | [方法条目](../by-type/business-logic.md) |
| 环回地址族过滤要与实际连接目的地核对 | 正文以127.0.1.2说明127/8环回候选，不能把只拦单一127.0.0.1视为完整限制。 | [方法条目](../by-type/ssrf.md) |
| Cognito 认证概念图没有给出接管错配 | 图仅有认证获取token再访问自有资源的流程，正文外链标题声称完整ATO，保存部分没有具体UserPool/AppClient配置或跨用户请求。 | [方法条目](../by-type/authn-session.md) |
| 域内共享枚举需要以 ACL 与访问身份确定影响 | FindUncommonShares图发现753台计算机和默认/backup/communication等共享名称。 | [方法条目](../discovery/client-and-cloud.md) |
| GitHub 关键词命中到有效秘密还有环境与权限边界 | 图以目标域名加CLIENT_SECRET、PASSWORD、APIKEY、TOKEN、JDBC、JIRA、AWS等关键词筛选，另一正文只称critical仓库。 | [方法条目](../by-type/info-secrets.md) |
| gf 筛选的是候选参数而不是重定向或 SSRF 结论 | cat targets｜gf redirect示例输出redirect/next，但没有响应。 | [方法条目](../targeted-fuzzing.md) |
| Headers 正则耗时应落到可控输入和资源预算 | 保存报告图说明undici5.13 Headers.set/append的headerValueNormalize正则，对重复制表符的大本地字符串计时约几秒，历史Low3.1。 | [方法条目](../experiment-design.md) |
| ICU 环境覆盖与提升权限进程的初始化边界 | Node忽略NODE_ICU_DATA而下游ICU仍处理ICU_DATA，图讨论setuid等较高权限启动及已有icu-data-dir能力。 | [方法条目](../source-audit.md) |
| 全角尖括号候选必须检查存储与输出的真实规范化 | 正文声称某些ASP.NET/SQLServer路径把全角尖括号规范化。 | [方法条目](../by-type/xss.md) |
| API 版本后缀候选保留相同对象和身份 | 已审阅复用图列getUserFUZZ的V1/V2/Beta后缀，没有完整真实端点或返回对象。 | [方法条目](../by-type/idor-access-control.md) |
| Intruder 提取反射后仍需最终 DOM 与事件证据 | 图中部分script已实体转义，img事件串原样突出，正文描述GrepExtract选反射。 | [方法条目](../by-type/xss.md) |
| 管理员登录页 XSS 不自动获得管理员权限 | 保存TD报告描述win进入popupLogin.jsp并跳出引号，附cookie弹窗示意及历史Medium4.7。 | [方法条目](../by-type/xss.md) |
| Multipart 部分计数与临时文件生命周期决定资源风险 | Django24580报告图说明无限empty/filepart在请求结束前保留临时文件，导致FD/内存耗尽，并以DATA_UPLOAD_MAX_NUMBER_FILES限制数量；版本边界为历史材料。 | [方法条目](../experiment-design.md) |
| Wayback 到 Dalfox 的贪婪截断会改变参数结构 | 保存管线按gf xss筛选，sed s/=.*/=/从首个等号后删掉全部剩余内容，可能丢后续参数和值。 | [方法条目](../by-type/xss.md) |
| 失效社交或商店链接要证实原链接与可认领标识 | Instagram图是遮挡账户和自行写入的BrokenLinkhijack文字，外链GooglePlay404题名没有保存全文。 | [方法条目](../by-type/subdomain-takeover.md) |
| XXE 影响从解析器功能和外部实体消费者推导 | 保存正文给出外部实体干扰XML处理的定义及泛Critical标签，没有DTD配置或请求。 | [方法条目](../by-type/xxe.md) |
| Shodan FTP 与登录关键词保留 banner 时效和资产归属 | 图以230、anonymous、guest、vsftpd2.3.4、org/country/port词组搜索，部分语法未经验证。 | [方法条目](../discovery/passive-and-services.md) |
| 隐藏 OPTIONS 流量只是工作台显示过滤 | 截图用OPTIONS /负向且大小写敏感的文字过滤，未启regex。 | [方法条目](../discovery/records-and-incremental.md) |
| 分字段输入必须在真实合成位置形成相同上下文 | 图把img/src、onerror与事件值拆到First/Middle/Last，另一图仅有persistent通知标题及奖励。 | [方法条目](../by-type/xss.md) |
| Netify 的关联情报与实际捕获流量分开记录 | 资源图列Application/Platform/Network/Protocol lookup及DPIAgent/API/DataFeeds，正文说明DPI情报涉及域名、IP、CDN、协议。 | [方法条目](../discovery/passive-and-services.md) |
| Android 工具词表按源码、运行与组件验证分工 | 正文重复Dex2JAR并列JADX/JD-GUI/ByteCodeView、Baksmali/ApkTool、Drozer、AndroGuard、QARK/AndroBugs、AppMon/MobSF。 | [方法条目](../by-type/mobile-android.md) |
| 付款与欺诈争议保留实际权益和项目政策 | 截图显示High8.3后改Low/fraud并奖250，正文称企业功能付费绕过，没有订单原始证据。 | [方法条目](../impact-and-acceptance.md) |
| X-Original-URL 差异要先确认是否到达相同处理器 | 正文GET /api/getUser403而根路径加X-Original-URL:/api/GetUser200，路径大小写已不同。 | [方法条目](../by-type/idor-access-control.md) |
| 归档秘密扫描的 verified 选项不默认离线 | 图TruffleHog filesystem扫描waymore目录并only-verified/concurrency2输出，未见命中，版本语法不能直接当当前接口。 | [方法条目](../by-type/info-secrets.md) |
| 尺寸、元标签与上传后的渲染消费者分别验证 | convert -resize1044x1044通常保持比例，不能从命令名认定严格方形；exiftool写-All示例含不可靠续行及主动脚本。 | [方法条目](../by-type/file-upload.md) |
| GSS 委派等级变化必须参与连接池复用判定 | 两份curl27536图指出CURLOPT_GSSAPI_DELEGATION遗漏匹配，较宽always连接在后来none/policy请求下仍被复用。 | [方法条目](../source-audit.md) |
| FTP 账户与安全选项是连接复用的身份边界 | curl27535图列FTP_ACCOUNT、ALTERNATIVE_TO_USER、SSL_CCC、USE_SSL遗漏比较；332要求account后alice连接被bob请求复用的演示。 | [方法条目](../source-audit.md) |
| SFTP 波浪号前缀替换与路径校验的先后次序 | curl27534图说明仅独立首元素~应映射home，但错误地转换~2或~a..前缀，后者可成为../路径。 | [方法条目](../by-type/lfi-path-traversal.md) |
| TELNET IAC 注入是协议协商而不是操作系统命令 | curl27533图说明TTYPE/XDISPLOC/NEW_ENV未转义IAC0xff可逃逸子协商，tcpdump示意相应字节。 | [方法条目](../source-audit.md) |
| 默认账户猜测不能与限速或旁路报告混归因 | 正文建议admin邮件/口令并称三次325，图分别为认证尝试限制不足与AlternatePath认证绕过，只有Medium/Closed类别和奖励。 | [方法条目](../by-type/authn-session.md) |
| MFA、OAuth 配置与账户占位用身份生命周期判别 | 正文仅记录2FA报告被改为OAuthMisconfiguration/AccountSquatting，缺具体流量。 | [方法条目](../by-type/oauth-oidc.md) |
| PDF 内弹窗与宿主页面 XSS 的来源边界 | 图只有pdf.js /xss2/弹窗和PDF上传题名，正文外链文件未获取。 | [方法条目](../by-type/file-upload.md) |
| 实体指数展开风险与外部实体读取分开验证 | BillionLaughs正文说明XML实体指数展开，Critical为泛标签。 | [方法条目](../by-type/xxe.md) |
| OData 字符串拼接同时涉及查询语法与 URL 参数边界 | 正文后端拼filter=id eq引号包围不可信输入，单引号可能改变OData表达式，&可能改变URL参数分隔；两者层次不同。 | [方法条目](../discovery/web-and-api.md) |
| phpMyAdmin 安装路径匹配与数据库 root 权限分开 | 正文把pma/setup/index.php扩展到admin前缀并称两个发现，图P1/New还在评估。 | [方法条目](../by-type/idor-access-control.md) |
| 联合查询模板与文件上传线索不能拼成已证 SQL 链 | 正文保存15列UNION和固定schema hex/元数据聚合串，另一正文只到发现unrestrictedupload的首帖，没有后续SQL消费者。 | [方法条目](../by-type/sql-injection.md) |
| ffuf replay-proxy 需要计入额外请求与身份保持 | 复用已审阅图示matched请求发往Burp，回放是额外请求，可能与扫描请求cookies/headers不同。 | [方法条目](../targeted-fuzzing.md) |
| phpinfo 接受与计划下线不能代替修复复核 | 保存正文只称phpinfo，图反馈接受且拟明天下线、未修复前open，没有具体环境值。 | [方法条目](../by-type/info-secrets.md) |
| Android 搜索命中要区分消息服务凭据与公开配置 | BeVigil图搜索APA91b找到反编译源码Authorization:key和FirebaseMsgAPIKey字段。 | [方法条目](../by-type/info-secrets.md) |
| Datadog env.json 线索按 API 权限与资产范围闭合 | 正文从子域/证书IP/ffuf到env.json及Datadogkey，再读文档示影响，没有实际键/请求。 | [方法条目](../by-type/info-secrets.md) |
| 密码确认步骤的限速与登录认证分别审计 | Nextcloud25820图需要先注册验证再进入安全设置，生成backupcode/删除/资料更改要求再次password，错误403与正确200作为oracle。 | [方法条目](../by-type/authn-session.md) |
| 混淆输出只证明表示变化不能证明规避能力 | PSObfuscation图片展示编码字符串与表达式，没有原始内容、等价结果或防护前后对照。 | [方法条目](../source-audit.md) |
| 403 工具题名与命令帮助仍需相同资源授权结果 | byp4xx正文只给工具调用格式，复用图是仓库卡，无模板/实际输出。 | [方法条目](../by-type/idor-access-control.md) |
| CI 配置与服务器源码文件按实际内容确定泄漏 | 正文建议.gitlab-ci.yml并称DB密码，图server.js/package-lock报告P3Duplicate但无文件内容。 | [方法条目](../by-type/info-secrets.md) |
| SSRF 参数候选不是服务端网络消费者证据 | 所谓25dorks实为dest/redirect/uri/path/host/port等参数名，缺fetch或回连。 | [方法条目](../by-type/ssrf.md) |
| 允许富文本也要检查不同字段与 iframe 使用点 | 正文提出Title+iframe，图只有基本XSS Medium4.3状态。 | [方法条目](../by-type/xss.md) |
| JS 归档提取令牌保留原 URL 和回放请求来源 | 图gau后js正则/ffuf200回放至Burp再被动提取accessToken/access_token，正则与占位词可能不完整。 | [方法条目](../by-type/info-secrets.md) |
| Docker 工具和宿主逃逸题名按能力边界组织 | 正文列secret-diver、imgcrypt、confine、Falco及若干DockerWriteup链接，只有资源名称。 | [方法条目](../cloud/container-k8s-security.md) |
| 撤销成员后的邀请令牌应同时失效于租户状态 | 正文建议移除用户后消费旧邀请，图valid通知仍说评级可变/修复待定。 | [方法条目](../by-type/idor-access-control.md) |
| HTTP 500 与一次十五秒耗时不够确认时间 SQLi | 图multipart字段中XOR/now/sysdate条件sleep15，响应500且br内容显示乱码，总时间15367ms。 | [方法条目](../by-type/sql-injection.md) |
| 删除反馈的 Blind XSS 需要后台消费与回连归因 | 正文建议删除/停用账号后的反馈输入，图只有P2Triaged题名。 | [方法条目](../by-type/xss.md) |
| 授权码泄漏链在 redirect 路径与统计消费者分别闭合 | pixiv图通过redirect_uri路径规范化到攻击者商品页，再由其GA配置获取query中的code。 | [方法条目](../by-type/oauth-oidc.md) |
| 修饰器和奖励时间问题由状态与输入控制确定影响 | 正文只说无控制modifier、validator错误timestamp导致epoch计算；修饰器名称并非唯一授权方式。 | [方法条目](../by-type/smart-contract.md) |
| PE 静态布局可视化不自动判定恶意或漏洞 | PortEx截图提供section entropy、raw/virtual地址与size的结构图。 | [方法条目](../discovery/client-and-cloud.md) |
| Connection 提名字段在多跳代理中可能删除可信头 | 图Proxy1加X-Important-Header却透传客户端Connection对该字段的提名，Proxy2删除后Backend缺头。 | [方法条目](../discovery/web-and-api.md) |
| GitHub SSO 后 Jenkins 构建能力需核对授权配置 | 图GitHub登录Jenkins页和构建console的ls/pwd/id，执行身份uid1000jenkins。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 子域截图发现需要可访问性和后续证据链 | 正文subfinder→httprobe→aquatone仅保存首帖约210子域与截图发现线索。 | [方法条目](../discovery/records-and-incremental.md) |
| Security Lab 查询贡献不是产品漏洞复现证据 | 保存题名涉及Beego RequestBody source、shutil.unpack_archive/TarSlip、PAM和类似CVE5123查询；图是issue链接、状态与奖励，无query源码。 | [方法条目](../source-audit.md) |
| 历史 URL 中 PII 的公开性、时效和数量分开证实 | 正文称WebArchive某端点有3000邮箱与部分姓名地址，图仅Low/Triaged。 | [方法条目](../by-type/info-secrets.md) |
| AWS WAF 前缀候选仍须同语义执行对照 | 正文建议在script前添<!，没有规则ID/实际响应。 | [方法条目](../by-type/waf-bypass.md) |
| SSH 协议位掩码比较遗漏密钥隔离检查 | curl27538图把SCP｜SFTP组合位掩码与单协议用==比较导致分支不进，建议按位&；同host/username及其他复用条件相同而key不同才构成候选。 | [方法条目](../source-audit.md) |
| 只读令牌返回成员信息不等授予成员角色 | Sanity图同Bearer GETprojects列members和Administrator/Editor角色描述，再GETprojects/users返回姓名/email/loginprovider字段，正文称标准请求起初无敏感数据。 | [方法条目](../by-type/info-secrets.md) |
| 多份奖励通知不能推断同一缺陷与沟通因果 | 正文称200，图片有150时间线及另一2FA报告50，合计可解释声明但目标与关联被遮。 | [方法条目](../reporting.md) |
| WP Engine 未关联站点与 CNAME 不自动等可接管 | 图SiteNotAvailable称未关联active站点，digNOERROR同时有CNAME/A且未知解析器、TTL0；价格页只显示付费条件。 | [方法条目](../by-type/subdomain-takeover.md) |
| 跨线程共享 HSTS 的释放边界区别于头配置 | curl27537图讨论多handle跨线程共享HSTS数据无mutex导致doublefree/UAF。 | [方法条目](../source-audit.md) |
| 爬虫与子域工具比较以可解释覆盖衡量 | GoSpider正文说明链接跟随/结构化保存/并发，工具比较帖子只有外链题名。 | [方法条目](../discovery/passive-and-services.md) |
| Portainer 到 Docker API 的题名保留每一步权限 | 保存材料只有2018报告/2023披露题名及Critical500状态，无SSRF入口或DockerAPI请求。 | [方法条目](../cloud/container-k8s-security.md) |
| HTML 注入与 DOM XSS 的评级记录不能替代消费者 | 两份Uber图分别HTMLinjection和DOMXSS题名，含历史评级调整/奖励但没有参数或DOMsource/sink。 | [方法条目](../by-type/xss.md) |
| WebSocket Origin 与成员消息授权分开验证 | Mattermost图只有2017报告/2023披露题名与CriticalCSRF状态。 | [方法条目](../by-type/websocket.md) |
| 标签层数过滤不能支持越深越易受攻击 | 复用图grep -P按com结尾筛至少2/3/4标签，不完整域名语法且不识别公共后缀/连字符。 | [方法条目](../discovery/passive-and-services.md) |
| 密码重置污染需比较路由 authority 与邮件 URL 来源 | 图originform改Host被404拒绝，absoluteform保留target路由却evilHost生成污染链接，为示意。 | [方法条目](../by-type/host-header.md) |
| Exchange 历史 PoC 链接不能证明现有部署状态 | 正文只有CVE41040历史PoC/视频链接，未保存版本、认证和实际入口结果。 | [方法条目](../by-type/ssrf.md) |
| 退出后历史页面显示与会话仍有效分别检查 | 正文以logout后alt-left可见旧页判bug，未区分浏览器bfcache、HTTPcache或新服务器请求。 | [方法条目](../by-type/authn-session.md) |
| JavaScript 变量词表不是后端参数契约 | 图grep var提取并sed拼接URL/GET参数，未引号curl与文本规则不能正确处理JS语法、query和编码。 | [方法条目](../targeted-fuzzing.md) |
| 证书匹配与页面标题只建立来源关联候选 | 转载图ssl:target/http.title/loginerrorIP，再确认归属后dirsearch找配置。 | [方法条目](../discovery/passive-and-services.md) |
| security.txt 与安全港资源不能自动授予测试许可 | 正文资源建议用safe-harbour发现项目，仅有外链。 | [方法条目](../scope-and-rules.md) |
| 路径词表按解码层、版本与文件消费者归类 | 图包含单/双编码、所谓UTF8实为overlong编码、nullbyte/截断、filter/zlib/zip及后门制作。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 参数字典频率排序仍保留目标上下文与低频项 | 复用图gau→unfurl→filter/popularity。 | [方法条目](../targeted-fuzzing.md) |
| PDF 空响应的 scheme 候选不能取代实际资源结果 | 正文FILE/fIlE/fifilele/FiFilele/%66ile/转义变体混合大小写、字符串替换和多层解码。 | [方法条目](../by-type/document-rendering.md) |
| Nginx 扫描工具题名没有给出配置缺陷 | 正文Nginxpwner功能宣传，图目录空终端，没有模板/版本/输出。 | [方法条目](../discovery/web-and-api.md) |
| CDN 引用里的内部主机名需要独立归属与可达证据 | 图枚举自有CDN域后用Shodan http.html搜索dev-int主机引用。 | [方法条目](../discovery/passive-and-services.md) |
| 多仓库同步审计要固定版本与本地范围 | Starhook正文只称同步远程仓库组到localhost，无配置/实际结果。 | [方法条目](../source-audit.md) |
| 负数量在结算出现仍需服务端订单与履约一致性 | 正文quantity=-1购物车不显示变化但finalcheckout显示，图只accepted标题。 | [方法条目](../by-type/business-logic.md) |
| SVN 元数据到源码读取保留实际内容和路径边界 | 正文dirsearch排除500/403找到.svn，用extractor筛database.php，未保存输出。 | [方法条目](../by-type/info-secrets.md) |
| XML-RPC 接口启用与认证或资源缺陷分开 | 报告图列发布/修改/删除/上传/评论功能及pingback/bruteforce泛风险，没有无权限操作结果。 | [方法条目](../discovery/web-and-api.md) |
| localStorage 门控需区分展示限制与服务端授权 | 图称正确密码后localStorage flag=true，手工改并reload可见PII。 | [方法条目](../by-type/authn-session.md) |
| 公开注册页面的军种参数反射按事件上下文确认 | 两份报告图NextRequestAccount.action militarybranchGET加换行/onmouseover，正文称登录前注册可达。 | [方法条目](../by-type/xss.md) |
| HAProxy stats 可见后按实际字段与控制动作定影响 | 图描述1024/haproxy-status与?stats外部可达，没有统计截图或管理动作。 | [方法条目](../by-type/info-secrets.md) |
| WordPress load-scripts 聚合数量与实际资源损耗分开 | 6389图列大量registeredJS load字段并称未认证资源消耗，缺版本/计时/CPU或可用性结果。 | [方法条目](../experiment-design.md) |
| MediaWiki 安装重启按钮与重装状态分开验证 | 图mw-config/index.php免认证显示restartinstallation按钮，未见动作成功/配置变化。 | [方法条目](../by-type/idor-access-control.md) |
| downloadForm 文件读声明不扩展成 SSH 接管 | 图filename../下载etc/hosts，文把斜线误称backslash，passwd被拦且id_rsa/SSH仅假设。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 邮件正文预览的双层编码还需要真实 DOM 解析 | 图PreviewLetterhead.aspx emailbody需先注册登录，HTML实体后再URLencode混合大小写script声明；不验证email不等免登录。 | [方法条目](../by-type/xss.md) |
| Joomla 扫描声明保留 web-service 权限验证 | 正文只称23752扫描器对webservice不当访问控制，无工具输出/入口版本。 | [方法条目](../by-type/idor-access-control.md) |
| 响应 admin 字段回传需追到持久权限与主体 | 正文把响应中admin:false加入请求并改true，响应仍true，没有受保护动作。 | [方法条目](../by-type/idor-access-control.md) |
| 反斜杠与 at 符号的 whitelist 差异需实际目的地 | 图proxy将backslash转slash后与白名单验证解析不同，声称callbackHTTP与metadata地址404，无响应对照。 | [方法条目](../by-type/ssrf.md) |
| 训练环境文件返回不能当真实目标发现 | 图page../etc/passwd实际HTTP200系统账户行，Apache/PHP旧版且cookie security=low显示训练环境特征。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 邮箱验证 token 必须绑定预期账户和邮箱 | 正文建议替换verificationURL的email参数，图只有绿色VerifiedUI。 | [方法条目](../by-type/authn-session.md) |
| CRLF 泛定义须落到响应协议与注入位置 | 保存Day68正文仅称响应中注入不希望数据，封面无具体header/原始字节。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 聊天室补全接口需要校验目标 room 的成员权限 | Nextcloud图三个自有用户demo/demo1/hacker：前二在room，hacker非成员调用autocomplete itemTypecall/itemId与requesttoken。 | [方法条目](../by-type/idor-access-control.md) |

| GTM 标识关联候选需要归属和时效核验 | 保存正文与 BuiltWith 图以 Google Tag Manager 标识找关联站点。 | [方法条目](../discovery/passive-and-services.md) |
| QR 文件转移工具描述不证明隔离边界已穿越 | 正文描述二进制转二维码影片再视觉重组。 | [方法条目](../discovery/client-and-cloud.md) |
| 302 响应里的后台正文与客户端状态改写分开判断 | speakerkit 示例说明跳转响应正文可能仍含后台内容。 | [方法条目](../by-type/idor-access-control.md) |
| SQL 引号、布尔与邮件字段候选没有百分百命中率 | 正文与图片列参数单引号、注释、数组、布尔分支及邮箱本地部分变体。 | [方法条目](../by-type/sql-injection.md) |
| JavaScript URL 控制字符先追踪浏览器的真实解析 | 已审阅复用图和正文把大小写、换行、tab、CR及C0控制字符插入 javascript URL 候选。 | [方法条目](../by-type/xss.md) |
| GitHub dork 词表需要落到提交与秘密权限 | 图片词表包含 token、credential、client_secret、password、配置和密钥文件。 | [方法条目](../by-type/info-secrets.md) |
| 筛掉长度零的 fake200 不能替代内容分类 | 图中 httpx 状态/长度管线用 egrep 排除 [0] 形式的输出。 | [方法条目](../discovery/records-and-incremental.md) |
| 重置邮件中的 host 拼接需要最终跳转和令牌边界 | 已审阅复用图以 target.com.evil.com 等主机候选改变重置链接。 | [方法条目](../by-type/open-redirect.md) |
| 七类 MFA 候选需要受保护动作与挑战生命周期 | 正文列直达端点、限流、客户端响应改写、重置/换邮箱关闭2FA、code重用、任意输入和缓存。 | [方法条目](../by-type/authn-session.md) |
| 账号接管清单先固定认证与邮箱身份绑定 | 图片提示重置、SSO、改邮箱和注册等候选。 | [方法条目](../by-type/authn-session.md) |
| WAF 扫描统计说明样本差异而不是稳定绕过 | 宣传与工具表格给出状态统计，但缺固定请求、过滤命中规则和后端结果。 | [方法条目](../by-type/waf-bypass.md) |
| Glob 与 IFS 的命令字形不保证 shell 语义等价 | 正文图组合通配符和 IFS 字符串。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Jira Nuclei 工作流输出仍需处理器和版本证据 | 图片展示工具流程而未给完整请求/漏洞语义。 | [方法条目](../discovery/web-and-api.md) |
| OTP 候选输入与旧挑战需要服务器绑定对照 | TOTP题名、复用旧code图及 #### 建议没有完整验证码流程。 | [方法条目](../by-type/authn-session.md) |
| SVG 读文件标题要区分渲染器与文件消费者 | 图片只有声称任意文件读取的历史标题，缺上传、服务端转换、协议和文件响应。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Deck 对象访问要匹配登录身份与对象成员 | 保存图片及正文围绕已认证对象访问候选。 | [方法条目](../by-type/idor-access-control.md) |
| Favicon 哈希关联保留算法、错误与时间 | 复用图列 curl/base64/mmh3/Shodan，当前 favihash 显示一条 SAME HASH，另有DNS失败、拒绝、超时和404。 | [方法条目](../discovery/passive-and-services.md) |
| Rails redirect_to 历史报告仍要核对 URL 消费者 | 图片提到历史重定向报告及边界。 | [方法条目](../by-type/open-redirect.md) |
| Dropbox 与 Box 搜索命中先分公开分享和非公开内容 | 保存搜索图展示云文件候选。 | [方法条目](../discovery/passive-and-services.md) |
| 邮箱验证 token 的账户与邮箱绑定不可由参数名推断 | 正文示例 ver_token=XXXemail=email 缺少分隔符，不能静默补成实际URL。 | [方法条目](../by-type/authn-session.md) |
| 浏览器 file URL 读取与服务端 LFI 使用不同权限域 | HTB图 XMLHttpRequest 片段的构造调用语法不完整，另有 view-source:file 桌面浏览器路径描述。 | [方法条目](../by-type/desktop-client.md) |
| 关注计数累加要先证明业务唯一性和幂等规则 | 正文声称100次Intruder返回403，而20次Repeater使关注者加20，图片奖励/状态没有原始请求。 | [方法条目](../by-type/business-logic.md) |
| 旧端点命名模式必须匹配同一受保护资源 | 正文建议复用开发者命名寻找旧API，图片状态栏缺实际请求。 | [方法条目](../by-type/idor-access-control.md) |
| Duplicate 报告访问受到原报告隐私边界限制 | 两张回复说明原报告可能有其他用户PII或额外漏洞细节，因此不能直接加入。 | [方法条目](../reporting.md) |
| 退款合约的特定收款人需要权限与价值流证据 | 保存文字称可由任意特定收款人提取退款，Critical正文与High图片有评级差异。 | [方法条目](../by-type/smart-contract.md) |
| Cloud exploit 工具菜单不能替代具体授权错误 | ThunderCloud help 只展示模块定位，包括活动操作、后门或SSO相关功能。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 换邮箱后验证状态与旧令牌需一并追踪 | Cloudflare图描述已验证账户更换邮箱时的生命周期候选。 | [方法条目](../by-type/authn-session.md) |
| Compose 可下载要区分部署秘密与开发配置 | 图片展示 docker-compose 内容含服务/端口/environment，值已脱敏。 | [方法条目](../by-type/info-secrets.md) |
| 路径词表与空画布只提供输入资源定位 | OneListForAll仓库卡、leaky-paths题名和无节点Trickest画布没有词表全文或运行结果。 | [方法条目](../targeted-fuzzing.md) |
| AWS 网段与证书字段关联需防共享基础设施误归属 | 正文建议用云IP范围及证书CN/O/OU找候选，图片仓库卡没有结果。 | [方法条目](../discovery/passive-and-services.md) |
| Tomcat 版本与 manager 入口仍需权限验证 | 图片TomcatScanner显示私网目标、大端口集合、版本及CVE候选。 | [方法条目](../discovery/web-and-api.md) |
| 云存储 dork 的无摘要结果不证明匿名文件读取 | 图片有 Azure/OneDrive/SharePoint 候选，其中还出现第三方homeassistant结果及无信息摘要。 | [方法条目](../discovery/passive-and-services.md) |
| JWT kid 路径候选依赖真实密钥查找实现 | 正文JSON漏逗号，kid指向 ../../etc/groups 只是猜测路径。 | [方法条目](../by-type/jwt.md) |
| CSRF 方法与 token 变体必须在真实浏览器跨站条件比较 | 正文列POST换GET、旧/空/缺token与删除headers候选。 | [方法条目](../by-type/csrf.md) |
| 对象级授权清单按最终操作与两个自有主体验证 | 正文/图片列ID位置、数组/对象、HPP、通配符、API版本/扩展/方法、Referer、GUID和异步导出。 | [方法条目](../by-type/idor-access-control.md) |
| 算术标记需要排除反射并不能直接证明 RCE | 正文 {{7*7}} 算术应是49，原文14错误；图中引擎判定与另一 waybackurls/qsreplace/ffuf replay-proxy 搜索81仅候选。 | [方法条目](../by-type/ssti.md) |
| 环回地址规范化不应混淆 inet_pton 与宽松解析 | 正文把 inet_aton/inet_pton、127/8、127.1、::80及DNS指向localhost混在一起。 | [方法条目](../by-type/ssrf.md) |
| OSINT 流程与搜索引擎列表按数据类型留证 | 图包含公开域名/邮件/姓名流程，搜索引擎图24项有服务器、证书、WiFi、代码、威胁情报和攻击面且重复服务。 | [方法条目](../discovery/passive-and-services.md) |
| Nmap 分片与地址伪装列表需协议与许可边界 | 图片/正文列fragment、decoy、zombie及spoof候选，没有实际回包或网络路径。 | [方法条目](../discovery/client-and-cloud.md) |
| Mass assignment 要证明持久的服务端权限变化 | 正文把请求 admin:false 改true，只描述字段修改。 | [方法条目](../by-type/idor-access-control.md) |
| 新功能线索需要可追溯版本与资产范围 | 正文建议从公开社交发布观察新功能。 | [方法条目](../discovery/records-and-incremental.md) |
| 目录列表的可见性和可读配置应分别证明 | 目录泄露报告结构图片缺直接目录/内容响应。 | [方法条目](../by-type/info-secrets.md) |
| ASP.NET 重复参数需校验实际合并和输出顺序 | 复用图与正文声称HTTP parameter pollution能绕WAF。 | [方法条目](../by-type/xss.md) |
| 文件扩展名筛选不能识别有效秘密或解析 URL | 正文使用扩展名匹配及Google OR查询发现文件候选。 | [方法条目](../by-type/info-secrets.md) |
| 发现用户名参数与默认凭据工具不等认证成功 | Arjun发现 j_username/j_password 但正文明确尚未找到作用入口；CredzCheckr只描述默认web凭据工具。 | [方法条目](../by-type/authn-session.md) |
| 本地查阅工具与修改权限需要分开使用 | 正文 more/grep/find/man 用于分页、查找和帮助，chmod实际修改文件权限。 | [方法条目](../discovery/records-and-incremental.md) |
| 文件名存储 XSS 标题缺最终渲染位置 | 正文只给 LINE filename stored XSS 历史标题、Low与100美元，没有响应或DOM。 | [方法条目](../by-type/xss.md) |
| 错误 SQL 注入严重度取决实际泄露与权限 | 正文给错误SQLi及Critical定义，没有数据库返回。 | [方法条目](../by-type/sql-injection.md) |
| 客服与员工对象 ID 先确定数据权限模型 | 正文提出userid暴露员工私有信息候选。 | [方法条目](../by-type/idor-access-control.md) |
| Dalfox 高并发与跳过检查需要记录覆盖缺口 | 图片管线使用高并发、skip-bav与跳过mining/grepping选项。 | [方法条目](../by-type/xss.md) |
| 泄漏情报 API 自动化不得混淆收集与凭据验证 | 正文PyIntelX描述API key/keywords并把账号密码线索发到Slack，没有运行结果。 | [方法条目](../by-type/info-secrets.md) |
| ELMAH 模板匹配要回到错误日志真实内容 | 一图P1 cookie题名缺值和请求，另一Nuclei版本输出含模板语法错误、medium匹配。 | [方法条目](../by-type/info-secrets.md) |
| ATT&CK 映射工具角色不等实际攻击技术证据 | 正文Decider用于把对手行为映射ATT&CK，图片只是应用构建日志，没有具体行为/技术映射。 | [方法条目](../hunting-strategy.md) |
| XML 内的 XHTML 脚本执行依赖浏览器渲染来源 | 正文XML namespace脚本与localhost/xss.xml提示框只证明本地浏览器当次解析执行。 | [方法条目](../by-type/file-upload.md) |
| 猜测重置路由与可预测口令需要真实认证证据 | 图片叙述 /api/u/resetPwd 猜到 /api/su/resetPwd，并称 username 加固定尾缀重置密码；无原始请求/响应/登录结果。 | [方法条目](../by-type/authn-session.md) |
| inurl 参数筛选只产生公开 URL 候选 | Google site:tesla.com inurl:& 返回公开商店、招聘和车辆页面。 | [方法条目](../discovery/passive-and-services.md) |
| CloudFlair 历史扫描关联到源站还需独立证据 | 仓库卡称使用Censys全网扫描数据找Cloudflare后源站，缺实际IP和可访问性。 | [方法条目](../discovery/passive-and-services.md) |
| PHP 自定义 gadget RCE 案例明确要求已有权限 | ExpressionEngine摘要明确登录控制面板且有权限后构造链，最终High8.5，缺代码。 | [方法条目](../by-type/deserialization-rce.md) |
| phpMyAdmin 路径大小写差异与 setup 权限分别核验 | 正文小写路径301到登录、混合大小写200到setup。 | [方法条目](../by-type/idor-access-control.md) |
| 命令注入字符清单需要具体 shell 和数据流 | 图含分隔符、替换、延时、输出重定向与OOB，所谓通用列表混入ls/id等平台差异。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 群聊非法密钥的崩溃条件要落到客户端消费者 | LINE摘要称无效E2EGroupKey在群内共享，再收到用该key加密的消息使iOS客户端崩溃，引用历史CVE-2022-41568。 | [方法条目](../by-type/mobile-ios.md) |
| 工具清单按输入消费者分工而不按数量计覆盖 | 图片标题123 tools，实际1–69有重复Burp/ZAP、代理、CMS、注入、无线、密码及Android静态工具。 | [方法条目](../hunting-strategy.md) |
| 试用期限客户端字段需核验持久权益与服务端时钟 | 正文称改 trial_expires Unix时间延长试用，缺受保护功能结果。 | [方法条目](../by-type/business-logic.md) |
| 泄漏 token 的评级不替代目标范围与授予权限 | 图片仅GitHub授权token题名、P5/Resolved和遮挡目标，正文称由P1降级。 | [方法条目](../scope-and-rules.md) |
| document.domain 改写与 with 变体要核对执行上下文 | 两图响应把 document.domain 改成 document_domain，另保留 with(document)alert(domain)，没有浏览器执行。 | [方法条目](../by-type/xss.md) |
| Subfinder 被动来源列表不等解析与授权覆盖 | 正文介绍被动子域来源，没有最新解析验证结果。 | [方法条目](../discovery/passive-and-services.md) |
| CRLF 管线的字面拼写与原始换行字节要保留 | 正文HTTPX/CRLF候选管线将 crlf 与 grep clrf 拼写混用。 | [方法条目](../by-type/crlf-response-splitting.md) |
| SVG 弹窗证据只覆盖该次直接打开的来源 | 图地址为上传SVG并显示提示框，域名遮挡。 | [方法条目](../by-type/file-upload.md) |
| DNS SERVFAIL 与 REFUSED 仅是接管候选状态 | 图dig A示例SERVFAIL并推荐can-i-take-over-dns。 | [方法条目](../by-type/subdomain-takeover.md) |
| 浏览器远程调试开关会改变观测条件 | 正文Burp嵌入浏览器profile支持关闭remote debugging以减少某些antibot检测，未给实际结果。 | [方法条目](../discovery/web-and-api.md) |
| 公开 newsletter ID 与私有订阅者列表需要分别授权 | LinkedIn保存摘要给订阅者GET接口，contentSeriesUrn含NewsletterId；说明另一用户替换公开ID可读订阅者列表，最终High7.5。 | [方法条目](../by-type/idor-access-control.md) |
| 版本控制和 WordPress 备份路径需内容证明 | 图列 .git/HEAD/config/index/logs、.svn/entries、.gitignore/.gitkeep；另一图wp-config.php.save直接返回PHP配置源及遮挡密钥。 | [方法条目](../by-type/info-secrets.md) |
| replace 首次替换与全局净化不能混为一谈 | 已审阅两张复用图讨论字符串replace与控制域。 | [方法条目](../by-type/xss.md) |
| 短 payload 与 polyglot 都依赖解析上下文 | Tiny XSS 两图用name、URL、frame索引、srcdoc、外部script及eval；polyglot图标注引号/注释/脚本闭合和details ontoggle。 | [方法条目](../by-type/xss.md) |
| undici host 值注入需落到 HTTP 序列化入口 | 历史摘要CVE-2023-23936称Node fetch/undici host header未挡CRLF，涉及当时16/18/19分支并指向request.js。 | [方法条目](../by-type/crlf-response-splitting.md) |
| OpenSSL 错误栈清理影响同线程后续操作 | 历史Node crypto CVE-2023-23919摘要称前序操作未清理OpenSSL错误栈，同线程后续加密操作误报错误可导致DoS。 | [方法条目](../source-audit.md) |
| 重定向参数 grep 词频只用于候选排序 | 正文按redirect参数和频率筛选，含非标准引号示例。 | [方法条目](../by-type/open-redirect.md) |
| High water 与 rebalance 候选需要明确合约不变量 | 两张High文字图声称分配high water可高于实际、rebalance算错状态破坏池invariant；背景SSRF教程不属于该合约证据。 | [方法条目](../by-type/smart-contract.md) |
| S3 预签名 POST 字段要检查 policy 授权约束 | JSON图有url、fields.key、x-amz-credential、security-token、policy及signature，值遮挡，符合预签名上传结构。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 已披露修复绕过要以当前边界和回归对照审查 | 正文建议复查hacktivity并称绕过一份旧报告，缺保存实现。 | [方法条目](../source-audit.md) |
| server-info 状态和报告侧栏不足以证明配置泄露 | 正文候选命令与侧栏High7.2/Duplicate/Private缺 /server-info 原始响应。 | [方法条目](../by-type/info-secrets.md) |
| MSI 二进制提取要校验产物且保持静态分析 | msidump图显示本地MSI提取一对象，宣称882056字节而目录文件1156019，计数不同。 | [方法条目](../discovery/client-and-cloud.md) |
| 范围外 DoS 的版本和 attack started 不是验证许可 | vsftpd截图有版本banner与工具 attack started，无持续不可用/恢复/基线，正文承认DoS不在范围。 | [方法条目](../scope-and-rules.md) |
| 失效社交用户名链接需要原站引用与平台生命周期 | Nextcloudfrance历史报告叙述官网链接到404用户名，认领后指向研究者账户，Medium。 | [方法条目](../by-type/subdomain-takeover.md) |
| Gobuster 批处理的输入输出映射需要逐项可追溯 | bash图两个循环读alive_$1.txt，cut斜线第三段作文件名，分别dir/files词表及-f/-e/-r/-k；gobuster/输出和cat当前目录路径不一致。 | [方法条目](../discovery/records-and-incremental.md) |
| Host localhost 与 socket 目的地及 SNI 分别核对 | 复用图用Host:localhost配目录fuzzing。 | [方法条目](../by-type/host-header.md) |
| 客户端 IP header 限流候选依赖可信代理配置 | 正文列X-Forwarded-For等header用于reset/OTP候选。 | [方法条目](../by-type/authn-session.md) |
| XLSX 上传需要服务器解析器的实体加载证据 | 正文只描述XXElixir可修改XLSX。 | [方法条目](../by-type/xxe.md) |
| 后台浏览器扩展需要观测范围和输入授权 | 正文说扩展在普通或Burp浏览器背景运行，缺规则和输出。 | [方法条目](../discovery/web-and-api.md) |
| 旧 OOS 奖金例外只说明该次项目处理变更 | 截图称旧范围外默认凭据报告误关，另一研究者补充后项目接受并平分bonus，另有限定披露许可。 | [方法条目](../scope-and-rules.md) |
| 服务指纹工具需要实际协议响应及时间 | FingerprintX正文定位开放端口服务发现，图片仅标志。 | [方法条目](../discovery/passive-and-services.md) |
| 目录递归下载需限制边界与敏感采集 | 复用图为localhost Apache/Windows/PHP列表，正文提wget -r --no-parent。 | [方法条目](../by-type/info-secrets.md) |
| 二十五个 LFI 参数名仍需服务端文件消费者 | 新图与复用图列cat/dir/action/board/date/detail/file/download/path/folder/prefix/include/page/inc/locate/show/doc/site/type/view/content/document/layout/mod/conf。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Padding oracle 需要稳定区分填充失败与认证失败 | 正文padre用于CBC padding oracle，仓库卡无目标密文或结果。 | [方法条目](../experiment-design.md) |
| 响应拆分到其他用户队列污染仍缺连接关联条件 | 正文询问CRLF响应拆分为何未导致HTTP smuggling。 | [方法条目](../by-type/request-smuggling.md) |
| APK pull、反编译与重打包是不同分析阶段 | 正文 Apk.sh 描述 pull/decode/rebuild/patch 工具功能，没有样本或执行结果。 | [方法条目](../by-type/mobile-android.md) |

| Swagger 搜索结果与真实 API 权限需要分别确认 | 正文API-docs/apidocs/swagger/api-explorer查询，图片仅datax子域swagger-ui.html无摘要。 | [方法条目](../discovery/passive-and-services.md) |
| 秘密正则、页面源码与 Git 历史各有可见边界 | 正文gf-secrets、Noseyparker和查看源码关键词提供候选；Burp图response body regex搜索未勾in-scope，完整regex裁切，含GoogleMaps apiKey与CLIENT_SECRET模板。 | [方法条目](../by-type/info-secrets.md) |
| Security Lab 的 Ruby 查询贡献需要检测规则证据 | 两张报告分别ZipSlip/TarSlip检测和SSTI，链接Security Lab issue且标注Ruby query奖励；缺规则、解压/模板代码或实际目标。 | [方法条目](../source-audit.md) |
| Actuator 200 与 favicon 关联不足以确认 RCE | 正文固定favicon hash找Spring Boot，图列env/heapdump等路径200与size。 | [方法条目](../by-type/info-secrets.md) |
| 自动 XSS 工具能力应以输入与最终事件核对 | 正文XSScrapy称XSS/SQL发现功能，未显示请求、输出或规则。 | [方法条目](../by-type/xss.md) |
| Burp 路径 URL 正则只能筛参数值形状 | 保存regex匹配问号后含斜线、scheme或短域后缀候选。 | [方法条目](../targeted-fuzzing.md) |
| HEAD 跟随跳转再 grep 地址仍需导航证据 | 图片管线Wayback、grep等号http、bhedak替换、curl -L -I及grep示例域。 | [方法条目](../by-type/open-redirect.md) |
| 发现到 Katana Nuclei 管线要逐级保留输入证据 | 图片rootDomains→assetfinder→httpx多个端口→hosts→Katana并发50→Nuclei模板占位，无结果。 | [方法条目](../discovery/web-and-api.md) |
| 开放重定向 dork 的参数名不等可控目的地 | 正文url/u/link/redirect/redirectUrl带http候选，部分site带scheme或问号语法未经验证。 | [方法条目](../by-type/open-redirect.md) |
| NGINX 路径探测名称不能替代文件读及规范化证据 | 正文httpx多斜线点段、匹配200与root字符串。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 截断的 Cloudflare 字符串不能视为有效绕过 | 保存字符串含domument等异常属性及省略号，指向第三方回连地址，没有请求/DOM结果。 | [方法条目](../by-type/xss.md) |
| 源码 URL 抽取正则需要解析与相对路径对照 | 正文curl｜grep -oP表达式包含https*任意字符及不完整字符类候选，缺实际输出。 | [方法条目](../discovery/passive-and-services.md) |
| Cookie 外传模板需区分执行与可读取会话 | 正文percent编码document.write/img模板被截断，缺实际渲染/请求。 | [方法条目](../by-type/xss.md) |
| 自定义标签 mouseover 要核对存储与受害者渲染 | 正文自定义tag、引号、样式及onmouseover字符串，没有保存/再显示证据。 | [方法条目](../by-type/xss.md) |
| JSON 数组内容到 JS 执行还缺实际消费者 | 正文只有数组内引号/alert/comment字符串并称WAF bypass。 | [方法条目](../by-type/xss.md) |
| 大型字典与 AI 来源不能作为覆盖率证据 | 正文bbFuzzing及三百万子域词表，复用仓库头像无词条或运行。 | [方法条目](../targeted-fuzzing.md) |
| select 与 noembed 混合模板需核对 HTML 状态切换 | 正文混合select/noembed/script、引号、换行编码与Unicode标识符，没有DOM或执行。 | [方法条目](../by-type/xss.md) |
| 扩展名 grep 找到文件候选后仍需内容与权限 | 正文txt/log/cache/secret/db/backup/yml/json/gz/rar/zip/config匹配建议。 | [方法条目](../by-type/info-secrets.md) |
| 函数级授权定义要落到角色与持久动作矩阵 | 正文MFLAC定义函数/动作缺权限，封面无实例。 | [方法条目](../by-type/idor-access-control.md) |
| 单页弹窗与批量模板结果要分别核验证据 | 图浏览器SVNWebClient error.jsp的errormessage脚本及提示框，下方多产品Nuclei模板/info/medium结果。 | [方法条目](../by-type/xss.md) |
| 代理池分摊来源不改变目标请求预算 | 正文Socksprox上游SOCKS集群负载均衡，未给目标结果。 | [方法条目](../discovery/web-and-api.md) |
| 后台发现线索与管理权限分开建证 | 正文列GitHub、blindXSS、端口、强制浏览及JS找到后台。 | [方法条目](../hunting-strategy.md) |
| Wayback 与 gf 的 redirect=no 列表只是候选 | 图存档URL含redirect=no、编码问号与重复参数，管线timeout2/thread100。 | [方法条目](../by-type/open-redirect.md) |
| 钓鱼取得 SSH 密钥的奖金声明没有测试授权 | 正文只称钓鱼员工SSH key获1337欧元，没有流程或项目许可。 | [方法条目](../scope-and-rules.md) |
| GraphQL 删除 spotlight 需要对象归属检查 | 阿拉伯语正文与报告图说明已登录myposts，DeleteStorySnaps mutation的ids数组及SPOTLIGHT_STORY替换分享URL对象ID，历史High15000。 | [方法条目](../by-type/idor-access-control.md) |
| JSON 登录单次 WAITFOR 耗时需要独立对照 | 图User注入SQLServer WAITFOR8秒，9314ms返回250 unknown/空正文。 | [方法条目](../by-type/sql-injection.md) |
| MySQL 引号配对参考取决实际查询和模式 | 图片示例在SELECT字符串where id上下文，以引号/反斜杠配对恢复语法，列mysql需root、information_schema历史版本。 | [方法条目](../by-type/sql-injection.md) |
| 弹窗函数替换要核对语法与实际事件 | 正文prompt/confirm/regex source/window属性候选，confrim拼写错误须保留。 | [方法条目](../by-type/xss.md) |
| cookie 属性访问变体不扩大可读会话范围 | 正文with(document)、括号与regex拼接属性名。 | [方法条目](../by-type/xss.md) |
| security.txt 搜索和榜单爬取需要实际项目策略 | 图security.txt结果只有Policy/mailto片段，正文建议Alexa百万榜爬文件。 | [方法条目](../scope-and-rules.md) |
| Wayback 旧论坛技巧需要版本与消费者复核 | 正文通过存档查看已失效XSS/SQL论坛，未保存帖全文。 | [方法条目](../discovery/records-and-incremental.md) |
| TLS pass through 减少工作台噪声也减少可见证据 | 正文建议Burp TLS pass through但名单图片未保存。 | [方法条目](../discovery/records-and-incremental.md) |
| JS 中 localhost 常量不能直接证明内网服务可读 | 复用裁剪图JS regex含localhost端口，正文建议搜索main.js/app.js。 | [方法条目](../by-type/ssrf.md) |
| 动态路径静态后缀缓存需跨主体取回与秘密绑定 | 摘要两条件为动态search/minNightlyPrice任意尾路径反射session，.jpeg被缓存，并称HASESSIONV3可取profile ha.crumb。 | [方法条目](../by-type/cache-deception.md) |
| hav cookie 反射与缓存投毒的共享消费需分别证明 | 图只显示四问题中的前两：.js路径var hav字符串反射，双引号处理但角括号未处理及WAF变体。 | [方法条目](../by-type/cache-deception.md) |
| 二十五项检查表需要消费者和证据门槛 | 图片列资产/端口/GitHub/CORS/权限/CSRF/SSRF/XSS/SSTI/token/OAuth/upload/HRS/overflow等。 | [方法条目](../hunting-strategy.md) |
| 激活接口返回管理员 JWT 需主体与权限证据 | 正文只称新增范围应用activation endpoint泄露admin敏感信息及JWT，缺响应。 | [方法条目](../by-type/authn-session.md) |
| 二十四个情报来源按数据类型与查询边界使用 | 图片表含服务器、WiFi、代码、证书、历史URL、威胁情报、反向图像、邮件、CVE和PoC来源。 | [方法条目](../discovery/passive-and-services.md) |
| 代码片段分类目录不能替代源码数据流审计 | 仓库图按AuthBypass/overflow/code/cmd/connectionstring/file/IDOR/upload/LDAP/log/NoSQL等目录分类并显示语言占比，缺具体源码。 | [方法条目](../source-audit.md) |
| 基础设施允许工具使用与目标扫描授权分开 | Linode历史ticket称再次允许Axiom并指更新帖子，提示不当分布式扫描可暂停服务。 | [方法条目](../scope-and-rules.md) |
| 扫描器分歧与六成漏报断言都需可复核样本 | sqlmap介绍、Ghauri故事及不定制漏至少60%说法，没有原始输入或检测结果；图仅Critical/2500Pending。 | [方法条目](../by-type/sql-injection.md) |
| SCCM SMB 文件发现还需读取身份与 ACL | 正文CMLoot用于找Configuration Manager共享文件，没有输出。 | [方法条目](../discovery/client-and-cloud.md) |
| 高概率关键词查询的 admin 结果不证明后台访问 | 两图config/env/setting/backup/admin/php搜索均仅admin子域无摘要结果。 | [方法条目](../discovery/passive-and-services.md) |
| 按 Nuclei 严重度排序只改变候选显示顺序 | 正文脚本按target及Critical到Info排序，缺实际输出。 | [方法条目](../discovery/records-and-incremental.md) |
| Unicode 点与多层编码须核对最终 authority | 两图报告标题Chinese dot、Referer多层percent和redirect_to多斜线/Unicode点，状态P4Duplicate或历史Low/Open，没有Location。 | [方法条目](../by-type/open-redirect.md) |
| 盲 SQL 的定义与报告标签仍需响应差异证据 | 正文定义查询结果/错误未直接显示，并称两个参数七表，图片只有报告列表/封面。 | [方法条目](../by-type/sql-injection.md) |
| GSuite 悬挂记录案例必须保留接管失败结论 | 图题名明确unsuccessful GSuite takeover，正文却把404/ghs.google映射称可用workspace认领，侧栏Low/50与正文N/A不同。 | [方法条目](../by-type/subdomain-takeover.md) |
| SPF 与 DMARC 配置线索不等投递成功 | Spoofy正文/仓库卡仅说明根据SPF/DMARC检查spoofability，无解析或邮件输出。 | [方法条目](../by-type/authn-session.md) |
| distribute 重入需要回调与余额状态证据 | 正文说node owner重入distribute分配运营者/用户余额，图只有drain distributor文字且背景SSRF无关。 | [方法条目](../by-type/smart-contract.md) |
| 消息删除报告的未复现状态不能省略 | 历史图已登录messages，Trash产生DELETE到账号标识/消息ID路径；研究者明确暂无备用消息不能复现，侧栏High/2250与正文N/A不同。 | [方法条目](../by-type/idor-access-control.md) |
| 已验证或已复现与待审、奖励和修复分开记录 | 一图validated后提交remediation review，最终 ruling/fix与severity仍可变；Apple图reproduced/investigating仍查rootcause。 | [方法条目](../reporting.md) |
| Flash crossdomain 策略与现代浏览器 CORS 不同 | 2018报告列过宽crossdomain.xml、第三方/范围外子域及SWF/AkamaiPlayer loaderContext，缺完整policy/加载与ATO链。 | [方法条目](../by-type/cors.md) |
| 自动化教学目录需要每阶段实际产物 | 图片列Katana/Wayback/DNSx/Naabu/Nuclei/XSSjson/qsreplace/Burp/命令和重定向，无完整命令或结果。 | [方法条目](../discovery/web-and-api.md) |
| 400 文件路由与实际文件返回构成不同证据层 | 第一图/file/400及favicon404，第二图重复反斜杠点段到文件返回200/Jetty6.1.11与系统账户行，目标遮挡。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 代理编码与 HttpOnly 秘密正文反射需要分别追踪 | 32red摘要称URL编码改变转发、cookie XSS回传，CAKEPHP虽HttpOnly却在HTML反射；POC要求victim已登录和日志服务器，无具体wire/执行/兑换。 | [方法条目](../by-type/xss.md) |
| CVE 仓库和版本警报需要实际部署与缺陷路径 | 正文称汇总1999–2023全部PoC及Elementor Pro早于3.11.6的Critical，缺完整清单/组件启用/入口。 | [方法条目](../source-audit.md) |
| SQLi dork 结果数不说明参数进入 SQL | 正文id/pid/category/cat/action/sid/dir与&查询，图37100结果只展示analytics路径。 | [方法条目](../discovery/passive-and-services.md) |
| URL valid 分类要保留语法、网络与业务差异 | 正文URV按status分valid/invalid，仓库卡没有定义或输出。 | [方法条目](../discovery/records-and-incremental.md) |
| 方法错误到 email 返回字段需同主体权限对照 | 三图selector.php GET实际200正文Method Not Allowed，POST无值200 missing email，再POST email返回账户/角色/密码旧值/付款字段标签，值遮挡/身份未知。 | [方法条目](../by-type/idor-access-control.md) |
| 限流 header 清单要核对可信来源与聚合键 | 图列X-Originating-IP/Host/Forwarded-Host/For/Remote/Client字段无结果。 | [方法条目](../by-type/authn-session.md) |
| 公司邮箱情报是身份线索而非升级权限 | 正文建议Hunter找公司邮箱以升级bug，无结果。 | [方法条目](../discovery/passive-and-services.md) |
| 学习路线首页的奖励与竞争叙述不保证结果 | 图片首页定义安全bug对CIA影响、bounty与奖励类型，学习仅Computer Fundamentals，未给完整路线。 | [方法条目](../hunting-strategy.md) |
| 请求评级复核需要明确新的影响证据 | 正文建议不满意可重评，没有项目回复或承诺。 | [方法条目](../reporting.md) |
| OIDC state 错配响应泄漏预期值破坏保密边界 | Nextcloud历史摘要callback比较会话state，错配JSON却回显expected state/debug leftover，CVE-2023-28848；ID4ME明确未测试仅近似代码假设。 | [方法条目](../by-type/oauth-oidc.md) |
| Bucket 容器定义仍需对象与身份权限模型 | 正文只有S3是对象容器定义，封面无漏洞条件。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 模式化子域枚举题名仍需候选与 DNS 证据 | 正文alterx介绍active enumeration with patterns，无模式/结果。 | [方法条目](../discovery/passive-and-services.md) |
| 模型生成 Redis 样例需要源码与终止行为核验 | 截图提示MSETNX认证后assertion，模型解释special crafted key/value，例子却只显示(integer)0没有崩溃。 | [方法条目](../source-audit.md) |
| SSRF dork 的邮箱页面只提供 URL 参数候选 | 正文http/url/path/dest/html/data/domain/page查询，图mail消息URL无摘要。 | [方法条目](../discovery/passive-and-services.md) |
| seq 的整数词表需要有限范围和输入契约 | 图seq10到20输出11个整数，正文min/max。 | [方法条目](../targeted-fuzzing.md) |
| 原型 has trap 片段没有跨源 JSON 读取证明 | 图Object.setPrototypeOf及Proxy has trap仅alert属性名，缺JSON响应/加载方式/浏览器结果。 | [方法条目](../by-type/cors.md) |
| user_id 参数导致 401 到 200 仍需对象内容对照 | 正文messages无参401、有victim_uuid200，没返回内容。 | [方法条目](../by-type/idor-access-control.md) |
| JS 正则抽取 query mutation 要保留语法覆盖缺口 | 保存nestle嵌套regex加sed替换转义换行，限制操作名字母/数字组合，未示结果。 | [方法条目](../by-type/graphql.md) |
| 历史 CNAME 反查需要当前委派与资源归属 | 正文dnshistory按特定CNAME找hosts，无结果。 | [方法条目](../discovery/passive-and-services.md) |
| SSRF 通用定义不能直接确认敏感访问 | 正文说明可绕安全控件/访问服务，图片仅封面。 | [方法条目](../by-type/ssrf.md) |
| Spot 与 futures 转账增发需账本守恒与幂等对照 | 正文称钱包转账无限增资产，图只有封面/无关SSRF背景。 | [方法条目](../by-type/business-logic.md) |
| 公司与 SSO 关键词需核对仓库部署和凭据类别 | 正文GitHub目标域名加password/secret以及Atlassian/Okta/Jira/Onelogin词组。 | [方法条目](../by-type/info-secrets.md) |
| 参数注入到文件写入还需程序选项和后续消费者 | 图片15binary功能表及git-archive --output=/tmp/foo例子，缺完整tree/cwd/参数调用，链接旧GitLab覆盖RCE。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 静态分析平台 logo 不代表规则检出 | Grepmarx正文仅source static analysis平台，图logo。 | [方法条目](../source-audit.md) |
| 奖励通知的披露许可与到账状态分别留证 | 350美元通知明确金额之外弱点需项目许可，称未来自动付款；没有漏洞机制。 | [方法条目](../reporting.md) |
| SQL polyglot 的多个分支仍受数据库和引号语义限制 | 两正文混合if/XOR/引号/注释及sleep、exp候选，称至少三场景零成本；条件版仍含sleep分支，不能归为全无时间型。 | [方法条目](../by-type/sql-injection.md) |
| LFI 参数搜索命中要回到真实文件读取接口 | 正文include/dir/detail/file/folder/inc/locate/doc/conf与&查询，图只生活频道comments URL。 | [方法条目](../discovery/passive-and-services.md) |

| Cookie 与页面中的 API 标识要按权限证据分类 | 保存帖称gcid/API token在Cookie头与子域页面源码出现，可访问API；现有图仅cleartext-cookie标签与初审通知。 | [方法条目](../by-type/info-secrets.md) |
| 初审、工程修复与奖金决定分开记录 | 邮件把初审、转交工程师、修复后Resolved与数周后的奖金决定分开。 | [方法条目](../reporting.md) |
| 退订操作的 CSRF 要确认跨站凭据和持久状态 | ResMed历史摘要指登录用户GET update-subscriptions退订Communication/Reward会员，称无anti-CSRF token并展示部分HTML起始。 | [方法条目](../by-type/csrf.md) |
| SSRFmap 的自动化功能需要明确请求消费者 | 保存内容仅把SSRFmap介绍为自动SSRF fuzz与利用工具，未保存代码或输出。 | [方法条目](../by-type/ssrf.md) |
| Minipool delegate 切换要按调用顺序审查不变量 | RocketMinipoolBase摘要称owner可切换delegate实现，夹在minipool调用前后可能干扰运行。 | [方法条目](../by-type/smart-contract.md) |
| Alterx 的模板排列是 DNS 候选而非有效资产 | 图从passive.txt输入，按sub-word.suffix模板与secure/private/staging词生成12个scanme.sh候选。 | [方法条目](../discovery/passive-and-services.md) |
| RCE 与 SSRF 参数 dork 只筛搜索候选 | 两帖分别按cmd/exec/query/code/do/run/read/ping与http/url/path/dest/html/data/domain/page搜URL，图返回Yahoo beacon或邮件message链接。 | [方法条目](../discovery/passive-and-services.md) |
| 付费功能选题要以可用角色和权益边界建模 | 正文建议关注premium功能，声称竞争较少但没有统计或案例。 | [方法条目](../hunting-strategy.md) |
| java 标签拼接 location 的结果要按实际 DOM 核对 | 保存模板以自定义java标签的tagName、innerHTML与location.hash拼接导航，contentEditable/autofocus/onfocus负责触发。 | [方法条目](../by-type/xss.md) |
| 工具清单需要按输入和产出角色评估 | 图称24工具，但可见编号只到22并缺17，底部裁切。 | [方法条目](../hunting-strategy.md) |
| nexturl 的后缀绕过要保留反斜线和截断边界 | 正文声称仅公司子域获准，混入evil.com、省略号与多个反斜线后跳出；没有完整请求或Location。 | [方法条目](../by-type/open-redirect.md) |
| GraphQL 查询层与 NoSQL 数据库要分开审查 | 正文将GraphQL与MongoDB一起列为NoSQL数据库，这是分类错误；GraphQL是API查询层，resolver可连接不同后端。 | [方法条目](../by-type/graphql.md) |
| JSP ContextPath 中实体与点段要逐层解析 | 保存ContextPath候选URL含&sol;、&num;和/..;/路径段，无请求响应。 | [方法条目](../by-type/xss.md) |
| Katana headless 覆盖 DOM 仍需完成与负载证据 | 图为headless爬取示例，显式rate110、并发8及输出文件。 | [方法条目](../discovery/web-and-api.md) |
| TLS Pass Through 的降噪设置也是解密覆盖缺口 | 正文列TLS透传域名模式，含前导*、不匹配括号与pkil拼写等疑点；不能把通配符和正则语法混用或自动改正。 | [方法条目](../discovery/records-and-incremental.md) |
| config.php 波浪号备份泄露要验证静态正文 | 图GET config.php~返回MoodlePHP配置片段，数据库字段被遮挡。 | [方法条目](../by-type/info-secrets.md) |
| debugHunter 的 modified response 需要语义与副作用核对 | 保存说明Chrome扩展改动debug参数并通知响应变化，图仅仓库功能卡片。 | [方法条目](../discovery/web-and-api.md) |
| 点段和百分号造成 403 到 200 要核对同一处理器 | 正文列%2e/%2f、/./与其他斜线变体，示例只给403/200。 | [方法条目](../by-type/idor-access-control.md) |
| content dam 的 AEM 指纹需要内容与部署交叉验证 | 图以inurl:/content/dam ext:txt找AEM候选，结果含多机构公共文本。 | [方法条目](../discovery/passive-and-services.md) |
| 本地 IP 头限流假设要核对可信代理链 | 正文把X-Originating-IP/X-Forwarded-For/X-Remote-IP设为127.0.0.1，没有响应。 | [方法条目](../by-type/authn-session.md) |
| 管理员登录旁的注册入口需确认默认角色 | 示意图建议在隐蔽子域管理员登录附近找POST注册。 | [方法条目](../by-type/idor-access-control.md) |
| 云代理的配置和销毁不改变聚合请求责任 | 两帖介绍BurpVPSProxy支持AWS/DigitalOcean/Linode，图显示实例创建、SOCKS5配置、销毁和恢复设置。 | [方法条目](../discovery/web-and-api.md) |
| 录制器生成 JS 的注释上下文不能只做字符串转义 | ElasticSyntheticsRecorder截图解释waitForNavigation把URL放在/*...*/注释里，quote转义引号仍容许*/结束注释，随后进入生成JavaScript。 | [方法条目](../source-audit.md) |
| AEM 默认账号列表要区分匿名、复制与示例角色 | 三份历史列表含admin/author、anonymous、replication-receiver与Geometrixx示例用户。 | [方法条目](../by-type/authn-session.md) |
| 2FA 响应改写必须回到服务器的验证状态 | 正文建议把success:false改为true或把4xx改200。 | [方法条目](../by-type/authn-session.md) |
| SQL 参数名列表要追到实际查询构造 | results/sleep/fetch/order/keyword/column/field/delete/string/number/filter等名字只是输入候选。 | [方法条目](../by-type/sql-injection.md) |
| HTTP 方法与参数污染要以端点语义和解析顺序建模 | 学习帖列HTTP方法、stateless与HPP。 | [方法条目](../discovery/web-and-api.md) |
| OTP 脑图转成绑定、刷新与会话的有限验证矩阵 | 两保存帖同脑图覆盖发送/刷新/验证限流，禁用2FA/改密再认证，密码后预验证会话、启用2FA后的旧会话，以及OTP跨账户/动作复用、旧码同码、泄露/弱随机、web/mobile端点和锁号。 | [方法条目](../by-type/authn-session.md) |
| 越界发现获得奖励也不扩大后续许可 | 正文称out-of-scope域SQLi获100美元，图仅TriagedOpen/High侧栏。 | [方法条目](../scope-and-rules.md) |
| now 与 sysdate 的延时条件仍受 SQL 语义约束 | 保存XOR/if/now()=sysdate()/sleep(6)候选，没有计时响应。 | [方法条目](../by-type/sql-injection.md) |
| Self XSS 加 CSRF 改密链要证明受害者无需粘贴 | 图声称先在账户panel发现SelfXSS，再以CSRF导入脚本读取改密页token并POST；报告为Duplicate/Unresolved。 | [方法条目](../by-type/xss.md) |
| Node 默认 OpenSSL 配置路径要按平台与写权限审查 | 图标题是MacOS/home/iojs/build，正文称共享MacOS主机自选iojs用户影响其他用户，摘要却描述Linux18.x默认路径；这些平台描述不能混为同一已证实条件。 | [方法条目](../source-audit.md) |
| llhttp 的 CRLF 解析缺口需要前后端分帧差异 | 图描述Node18.7.0 llhttp接受不以CRLF正确结束的header，前一空值头可混淆Transfer-Encoding；上游忽略TE而后端按chunked处理可能导致请求走私。 | [方法条目](../by-type/request-smuggling.md) |
| WebCrypto 熵来源的失败值和强度要分别测试 | 历史Node18报告称SecretKeyGenTraits::DoKeyGen调用EntropySource而未检查返回值，且输出未必密码学强度。 | [方法条目](../source-audit.md) |
| CGI Cookie 属性注入和响应拆分需核对真实头字段 | 两图引用CVE-2021-33621：不可信输入生成CGI响应可能注入header/body，CGI::Cookie构造未充分检查属性。 | [方法条目](../by-type/crlf-response-splitting.md) |
| VS Code AI 分析器要审查源码出站与结论证据 | 保存内容介绍调用ChatGPT API分析代码的扩展，图只有logo，未保存扩展源码或结果。 | [方法条目](../source-audit.md) |
| 图片元数据和双扩展名不自动变为 PHP 执行 | 正文把PHP文本写进EXIF Comment并将jpg改为php.jpg，没有上传响应或解释器行为。 | [方法条目](../by-type/file-upload.md) |
| 正则可视化匹配还要核对实际引擎与消费者 | EasyRegex说明展示文本中匹配片段，无规则或产出。 | [方法条目](../targeted-fuzzing.md) |
| 历史报告表应保留状态、设备和稳定来源 | 图表头包括Category/Name/ID/Status/ReportLink/Severity/CVE/Bounty/TestDevice/Notes。 | [方法条目](../discovery/records-and-incremental.md) |
| WHOIS 组织检索导出不是完整资产或授权清单 | Netlas截图按registrant.organization查询并提供JSON/CSV字段导出，同时警告WHOIS索引极不完整且开发冻结。 | [方法条目](../discovery/passive-and-services.md) |
| Git 配置泄露应覆盖部署子路径并验证正文 | 正文提醒.git暴露可发生任何URL子路径，图有三个深路径.git/config状态200。 | [方法条目](../by-type/info-secrets.md) |
| 共享登录的多控制台注销要验证每个会话撤销 | Cloudflare历史摘要说明Dashboard与ZeroTrust共享登录，但退出前者未自动退出后者，攻击需要本地浏览器访问。 | [方法条目](../by-type/authn-session.md) |
| JS 中 PHP 文本的 tentative 命中需内容级证据 | Nextcloud报告指主题dist/js/main.js可能返回PHP源码，图仅扫描器tentative摘要和通用影响，没有实际代码。 | [方法条目](../by-type/info-secrets.md) |
| 主题 logo 的 key 可控要进一步核对写入边界 | Nextcloud摘要称上传logo/favicon时key作为filename且可修改，历史Low2.4/CVE-2023-28833。 | [方法条目](../by-type/file-upload.md) |
| 多 VPS 分发任务需要全局去重、预算和收据 | 正文称bash分发域名处理，图仅distributed_tasks仓库卡片。 | [方法条目](../discovery/records-and-incremental.md) |
| 修复邮件自述需要独立复测记录 | Pearson邮件自述已修复、reference遮挡且征询保密反馈。 | [方法条目](../reporting.md) |
| 可搜索词表别把工作目录和未引用路径直接传给 fuzz | 保存alias从当前目录和/opt/wordlists找所有文件再fzf选择，用ffuf -w $(wordlists)调用；另一帖只是词表仓库。 | [方法条目](../targeted-fuzzing.md) |
| DOM Invader canary 到可执行 sink 需要上下文证据 | 正文建议广泛放canary寻找可控sink。 | [方法条目](../by-type/xss.md) |
| 日志、元数据和会话写入要与 include 消费者分开 | 保存的3/3续帖说可把某payload放metadata/log/upload/PHPsession文件，前两段与payload未保存。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 方法和重写头的 403 测试需固定路由及动作语义 | 正文列Content-Length:0、X-rewrite-url/X-Original-URL/X-Custom-IP-Authorization/XFF及GET改POST/TRACE/PUT/OPTIONS，没有结果。 | [方法条目](../by-type/idor-access-control.md) |
| 邮箱重置污染要证明投递与 token 的主体绑定 | 图列重复email、CRLFcc、分隔符、无域/TLD和JSON数组候选。 | [方法条目](../by-type/authn-session.md) |
| 试用到期与扣款失败要按权益状态机判断 | 正文以余额不足的虚拟卡等待试用结束，再观察订阅。 | [方法条目](../by-type/business-logic.md) |
| SSH 用户时序判断要控制网络和认证分支 | osueta例子指私有IP、不同delay和用户列表，第二行含Unicode长横线的dos选项，未有结果。 | [方法条目](../discovery/client-and-cloud.md) |
| Nmap 分层扫描必须把端口集合传到后续阶段 | 图先发现主机，再TCP/UDP常用与全端口、版本/OS识别。 | [方法条目](../discovery/passive-and-services.md) |
| 短 calldata 的钱包提示要与合约实际解码对齐 | MetaMask历史摘要称solc<0.5合约未校验calldata长度，缺字节按0读，钱包遇异常长度未展示正常transfer/approve提示。 | [方法条目](../by-type/smart-contract.md) |
| AI 网站的弹窗应按普通 Web 数据流复核 | 西班牙文称在线AI工具常有XSS，图仅遮挡站点的q参数与alert弹窗，payload截断。 | [方法条目](../by-type/ai-application.md) |
| TalentMAP 用户端点要用 guest 与自有对象矩阵 | 报告图介绍本地Docker建种子与测试用户，guest可访问/api/v1/permission/user/{USER_ID}的主张，无返回正文。 | [方法条目](../by-type/idor-access-control.md) |
| 通用建议落到范围、业务动作和证据日志 | 保存建议从scope、理解应用、工具、坚持、日志和项目沟通开始。 | [方法条目](../hunting-strategy.md) |
| JSON 登录的 WAITFOR 示例仍需数据库消费者 | 正文与图给username上的WAITFOR DELAY八秒例子，没有响应。 | [方法条目](../by-type/sql-injection.md) |
| 路径穿越定义应区分读取、写入与执行影响 | 正文将traversal描述为读取任意文件，图只是标题封面。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 分布式 headless 模板启动量不是完成量 | 图Axiom的nuclei-screenshots模块创建工作目录，输入50行，没有最终截图或结果。 | [方法条目](../discovery/web-and-api.md) |
| 测试 workflow 的 DeepSource token 要核对真实权限 | Weblate历史图称GitHub测试workflow包含DeepSource秘密，可用CLI访问环境并报告artifacts，厂商改用运行时secret。 | [方法条目](../by-type/info-secrets.md) |
| 删帖越权需要对象所有者与公司角色对照 | LinkedIn历史摘要指可删他人及公司页面帖子，图无请求且是2018年Resolved案例。 | [方法条目](../by-type/idor-access-control.md) |
| CT 订阅与模板请求是两个不同观察阶段 | Certwatcher正文介绍CT跟踪/YAML DSL，图模板却GET /.env并对APP_NAME/KEY等body词做or匹配，示例有超时且标earlydevelopment。 | [方法条目](../discovery/passive-and-services.md) |
| env 模板的 or 词匹配不能直接标 High | 图Laravel env模板以APP_NAME/ENV/KEY/DEBUG/URL/PASSWORD等匹配body，任何一个词可能只出现在普通页面。 | [方法条目](../by-type/info-secrets.md) |
| Chrome gpu launcher 的选项注入需要真实 argv 边界 | 正文给chrome --gpu-launcher候选，引号不完整，并列command/file/read/library能力。 | [方法条目](../by-type/cmd-injection-rce.md) |
| phpinfo 的影响需定位到实际暴露字段 | Expedia历史图只有phpinfo.phpURL与一般侦察影响，Low3.7/奖金额，没有配置正文。 | [方法条目](../by-type/info-secrets.md) |
| Backup Finder 的探测结果需排除 soft 404 和公开副本 | 保存工具说明与卡片列备份/旧/临时/未引用文件，缺运行结果。 | [方法条目](../by-type/info-secrets.md) |
| QR 导航的 UXSS 要证明跨 origin 执行而非普通弹窗 | Brave图列Android13及历史stable/nightly/beta/Chromium版本，称扫描QR后在所有打开domain执行；QR和步骤截断。 | [方法条目](../by-type/mobile-android.md) |
| WordPress 注册路径存在不等管理权限开放 | 保存建议使用wp-login?action=register及临时邮箱，路径可能缺.php且未给响应。 | [方法条目](../by-type/authn-session.md) |
| 审核员样式用户名要与可信角色标识分离 | 两保存帖的图是同一h1_analyst_*普通用户名报告，Resolved/Low3.5/500美元，后帖称33字短报告。 | [方法条目](../by-type/business-logic.md) |
| 云终端教程不能把披露政策搜索当扫描授权 | 图建议找security report/reward政策、打开Google云终端装工具再扫，且提示闲置断连。 | [方法条目](../scope-and-rules.md) |
| chmod 的对象必须是本地已审查文件 | 正文把http://pingScript.sh传给chmod再执行本地脚本，混淆URL与文件路径。 | [方法条目](../discovery/records-and-incremental.md) |
| Nagios 面板默认口令与 P3 标签需要部署证据 | 正文给/nagios和单一nagiosadmin默认值，图仅P3/Unresolved标题。 | [方法条目](../by-type/authn-session.md) |
| GraphQL 测试表必须使用真实 schema 与后续消费者 | 图列__schema types{name}、users(where:name)的SQL字符串、仅引号XSS和file(path)穿越，未给目标schema/响应。 | [方法条目](../by-type/graphql.md) |
| FileContentProvider 的 SQL 注入要保留本地调用前提 | ownCloudAndroid历史图称exported FileContentProvider含SQLi，同设备恶意app/用户可取内部信息；manifest/SQL代码截断。 | [方法条目](../by-type/mobile-android.md) |

| GAU 与 httpx 的发现数量须区分响应和可访问接口（2023 案例） | 归档提出从 GAU 的上万条 JS 线索筛到约千条“live”请求，却同时遇到 403。 | [方法条目](../discovery/web-and-api.md) |
| 邮箱身份归一化与邮件头构造是两条信任边界 | 帖子把换行 cc/Bcc、加号别名和邮箱校验放在同一组技巧中。 | [方法条目](../by-type/authn-session.md) |
| 邮箱换行需要区分 SMTP 信封与消息头 | 对 cc/Bcc 换行候选，记录字段从解码、校验到邮件库调用的顺序，分别检查 SMTP 信封收件人与消息头生成。 | [方法条目](../by-type/crlf-response-splitting.md) |
| ImageMagick MSL 线索须绑定已安装组件与预览调用链 | 归档 ownCloud 案例将 OC\Preview\Bitmap、ImageMagick 与上传后已知路径串联。 | [方法条目](../by-type/document-rendering.md) |
| HTTP 方法切换必须比较同一对象操作的授权 | 归档列出 GET、POST、PUT、DELETE、PATCH 及非标准方法作为差异线索。 | [方法条目](../by-type/idor-access-control.md) |
| 宽松 Content-Type 与任意扩展名不等于上传后执行 | 帖子上传请求的类型设置与任意扩展名接受现象用于寻找解析差异。 | [方法条目](../by-type/file-upload.md) |
| AEM 历史资产与时间过滤工具提供的是有日期的线索 | 归档提及 2023 年 AEM 资产字典与按时间查看历史 URL 的 TimeMachine。 | [方法条目](../discovery/passive-and-services.md) |
| SQL 与 RCE 搜索语法只产生入口假设 | 帖子利用搜索语法寻找疑似参数、脚本和产品页面。 | [方法条目](../discovery/passive-and-services.md) |
| CRLF 检测器的命中需还原到实际响应头 | 归档介绍 Node.js CRLF 检测工具的用途。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 转发响应流程图不能替代 SSRF 元数据结果 | 图片以代理转发外部站点再触及元数据入口说明攻击链假设。 | [方法条目](../by-type/ssrf.md) |
| 钱包中的双向文本域名显示应与真实授权来源对照 | MetaMask 配图利用双向文本影响 0-metamask.io 一类字符串的视觉顺序。 | [方法条目](../by-type/smart-contract.md) |
| 删除账户后的会话失效需要实际受保护请求确认 | 帖子记录删除账户后当前会话仍然存在的现象。 | [方法条目](../by-type/authn-session.md) |
| 跨用户 RollToken 可能影响可用性而未必泄露令牌 | 归档把已知其他用户 UUID 传入 RollToken 作为问题。 | [方法条目](../by-type/idor-access-control.md) |
| 重置邮箱的重复字段和控制字符须追到令牌绑定及实际投递 | 配图将重复 email 参数、CR/LF、cc、分隔符、无 TLD 和 JSON 数组作为候选。 | [方法条目](../by-type/authn-session.md) |
| 多用户 XSS 回连服务要区分部署配置与目标证据 | 帖子提及在 XSS Hunter 分支添加多用户环境配置，配图为工具仓库卡片。 | [方法条目](../discovery/web-and-api.md) |
| SOAP 中的 CDATA 脚本不证明外部实体解析 | 保存请求把脚本样式文本置于 SOAP 字段的 CDATA 中。 | [方法条目](../by-type/xxe.md) |
| SOAP 文本进入展示页面才形成独立的存储型 XSS 假设 | SOAP/CDATA 示例中的脚本文本需要从提交字段追到存储位置及后续展示页面，记录编码、HTML 上下文与浏览器解析。 | [方法条目](../by-type/xss.md) |
| 组织和相册 API 应比较嵌套对象关系及返回的数据 | 归档出现组织 UUID、相册/照片 user_id、把相册操作移到评论端点，以及消息接口添加 user_id 后 401 变 200。 | [方法条目](../by-type/idor-access-control.md) |
| 失效社交链接可能是身份信任线索，领取账号不是漏洞证明 | 截图显示应用/社区指向不存在或不再有效的社交账号，帖子以抢注为方向。 | [方法条目](../scope-and-rules.md) |
| 移动工具菜单和 MobSF 功能要映射到实际分析阶段 | QuadraInspect 图片展示 APKLeaks、AndroPass、MobSF、RMS 等菜单与本地启动；另帖介绍 MobSF 静态/动态分析角色。 | [方法条目](../by-type/mobile-android.md) |
| DigitalOcean 元数据路径应按提供商和网络主体核对 | 帖子提到 169.254.169.254 的 metadata/v1.json。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 反馈接口错误中的元数据字段需要区分内容与推断 | 配图为反馈请求与 200 响应，JSON 的 success 为 false，解析错误中出现与 AWS 元数据有关的字段。 | [方法条目](../by-type/ssrf.md) |
| 扫描器严重性统计和自动化总量应保留原始计数口径 | Nuclei 图片按 severity 列出 2605、764、279、47、18 等数量，另一帖用大量域名/地址和管道宣传自动化能力。 | [方法条目](../discovery/records-and-incremental.md) |
| 公开 JEB 许可证页面应按暴露字段评估 | 图片展示姓名、邮箱、用户 ID 和许可证 ID 等字段。 | [方法条目](../by-type/info-secrets.md) |
| 注册邮箱的多消费者验证要分开处理 SQL、SMTP 与模板假设 | 归档将邮箱字段内的 SQL、SSRF、CRLF/SMTP RCPT、XSS/SSTI 语法集中列举。 | [方法条目](../by-type/authn-session.md) |
| 邮箱模板表达式需区分格式变化与实际求值 | 保存帖提出邮箱中的 {{7*7}} 被变成 {7*7}，并举 Django 调试标签等候选。 | [方法条目](../by-type/ssti.md) |
| 从架构和代码习惯生成可证伪假设 | 归档建议了解系统结构及开发者习惯。 | [方法条目](../source-audit.md) |
| 邮箱编码与 X-Forwarded-For 更改不能直接证明限流绕过 | 帖子列举 %00、%2e、%0d/%0a 邮箱变体及 X-Forwarded-For/地址轮换。 | [方法条目](../by-type/authn-session.md) |
| 通配符与 JSON 类型突变应绑定具体解析语义 | 归档使用 *、%、_、点号及 username 的 true/null/列表/字典和 $neq 风格候选。 | [方法条目](../targeted-fuzzing.md) |
| PHP 过滤链的内存错误信号与文件读取应分开 | 配图用重复 UTF-8→UCS-4LE 转换展示超过 134217728 字节的内存限制错误。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 同一 API 的表单、XML、JSON 表示应比较解析与授权 | 帖子建议将表单 Content-Type 改成 XML 或 JSON。 | [方法条目](../discovery/web-and-api.md) |
| 上传检查清单应按消费者分组并保留反例 | 二十项图片覆盖扩展名、MIME、文件名/目录、权限、重复覆盖、图像处理、大小/时间/速率、错误、元数据 XSS/SQL 与日志。 | [方法条目](../by-type/file-upload.md) |
| 直达源站线索必须核对目标归属和等价请求 | 图片显示 DNS/SSO 相关线索，帖子提出绕过 Akamai 直达源站。 | [方法条目](../by-type/waf-bypass.md) |
| logout 的 javascript 参数需证明到达可执行导航消费者 | 请求中 logout.jsx 的 home 参数是 javascript 风格表达式。 | [方法条目](../by-type/xss.md) |
| 有 PHP 上传执行权的邮件演示应先识别既有权限 | 帖子让用户在托管站点 public HTML 中上传 PHP 发邮件，截图为截断的 SMTP 代码片段。 | [方法条目](../by-type/authn-session.md) |
| wp-cron 可访问与资源耗尽是不同命题 | 归档把 wp-cron 大量请求描述为高危。 | [方法条目](../experiment-design.md) |
| XML-RPC 回连假设需要区分预期 pingback 与敏感访问 | 帖子提及 xmlrpc.php、外部回连及 pingback，但保存材料没有完整请求结果。 | [方法条目](../by-type/ssrf.md) |
| 域名字符串后缀相似不能代替 CORS 信任来源 | 归档以 domain.com.attacker.com 提示来源校验风险。 | [方法条目](../by-type/cors.md) |
| 奖金与预计付款须与已验证技术结果分开记录 | 保存图片出现 CORS 相关奖金额、沟通及预计支付信息。 | [方法条目](../reporting.md) |
| 错误响应的 MIME 嗅探要记录实际浏览器解释 | 图片展示 ASP.NET 错误响应中类似 img 事件内容，帖子讨论 MIME 嗅探。 | [方法条目](../by-type/xss.md) |
| 点号编码绕过需要定位解码和规范化顺序 | 归档以删除 ../ 后尝试编码 %2e%2e%2f 为线索。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 从范围外历史 URL 迁移到范围内验证应重建证据 | 帖子利用范围外 Wayback 路径或类似 credentials.txt 线索猜范围内入口。 | [方法条目](../scope-and-rules.md) |
| API 版本差异与自动替换需要约束到预期字段 | 帖子从 v1/v2 或日期化路径找差异，另帖用 AutoRepeater 将请求中 v2 改 v1。 | [方法条目](../discovery/web-and-api.md) |
| sitemap 偏移参数延时样本需核对真实请求字节和数据库语义 | 多个保存帖重复 sitemap_index.xml 的 offset、IF/CONST/SLEEP 类示例。 | [方法条目](../by-type/sql-injection.md) |
| JS 的三个正则只提取特定文本形态 | 图片使用 grep/sed 风格表达式提取引号内相对路径。 | [方法条目](../discovery/passive-and-services.md) |
| 奖金进度工具应核对输入口径与单环境反馈 | BountyMeter 图片有目标 40000、进度 30% 等展示；另帖和 GitHub issue 记录 Python 重写后某用户的 Mac 终端可用。 | [方法条目](../discovery/records-and-incremental.md) |
| errorlog 中邮箱和 JWT 的线索需要实际字段及访问边界 | 帖子描述 errorlog 页面出现邮箱/JWT，图片主要是报告状态，未展示字段或访问结果。 | [方法条目](../by-type/info-secrets.md) |
| 本地 shell 运行与远程注入入口不能互相替代 | 归档一例 Python 将 input 交给 os.system 并显示 root 风格提示，另一图在 CentOS shell 中利用引号、算术/转义及 here-string 表示 $0 执行目录列表。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 服务端原型污染工具候选需分离写入原语与利用消费者 | SSPP 工具卡片及简介用于定位服务端原型污染。 | [方法条目](../by-type/prototype-pollution.md) |
| Web 指纹与扫描强度参数应按请求预算解释 | 归档比较 Nmap、whatweb 不同 aggression、webanalyze 抓取深度，并介绍 wafw00f。 | [方法条目](../discovery/web-and-api.md) |
| Burp 与 Wayback 的脚本发现要保留 URL 和消费版本 | 保存帖从站点记录、FindScripts 和 Wayback 搜索 JS。 | [方法条目](../discovery/passive-and-services.md) |
| hash 动态调用 parent 函数需检查来源、可达性和实际参数 | 代码图把 commReceive.html 的 hash 按 ｜｜ 拆分，再调用 `window.parent[functionName](若干参数)`。 | [方法条目](../by-type/xss.md) |
| 范围外 LFI 的奖金案例不能扩大测试授权 | 保存帖讨论一个范围外 LFI 并显示奖金金额，实际请求/文件内容未保存。 | [方法条目](../scope-and-rules.md) |
| 模板和 AI 报告必须保持实际载荷及证据原样 | 保存图片展示 HackerOne 上传报告模板，另一图的生成报告把源帖 SVG 候选改为 img 事件语法。 | [方法条目](../reporting.md) |
| Nuclei 模板结构应审查匹配条件与负例 | 帖子列出模板 ID、协议、请求、匹配器等结构。 | [方法条目](../source-audit.md) |
| 同一 OIDC 签名的 token 仍需受众校验 | 归档 Argo CD 案例描述 JWT 未检查 aud，其他应用的同一 OIDC 签名 token 可能被接受，并映射 groups 到权限。 | [方法条目](../by-type/jwt.md) |
| Airflow Provider 输入问题须分别绑定连接配置与执行消费点 | 两个帖指向 CVE-2023-25691/25692，示例环境为 Airflow 2.5.1 与 provider 8.8.0，并提及 provider 8.10.0 之前。 | [方法条目](../by-type/cmd-injection-rce.md) |
| WAF 绕过语法需先确认原始字节能形成浏览器语法 | 保存示例用外观类似括号的 « » 等字符包围 form/action javascript 风格文本，且部分语法不完整。 | [方法条目](../by-type/xss.md) |
| WAF 的误报和漏报应结合应用实际消费行为 | 帖子提出检测 WAF 的 false positive/negative。 | [方法条目](../by-type/waf-bypass.md) |
| 支付清单应覆盖金额与账本状态而非只按旧评分筛选 | 支付图片列出十一项通用安全检查并使用 CVSS v2 大于 4 的筛选说法。 | [方法条目](../business-modeling.md) |
| 头部数字枚举与 DNS 回连需要唯一请求关联 | Pitchfork 图片按 1–2000 数字生成请求头名称/回连候选，但请求图编号为 125、Taborator DNS 图编号为 123，不能直接归因为图中那个头。 | [方法条目](../by-type/ssrf.md) |
| 三十项 API 检查应落到主体、对象和状态证据 | 配图混合静态/动态、认证、输入、SQL/XSS、暴力破解、社工和资源耗尽等项目。 | [方法条目](../discovery/web-and-api.md) |
| 随机 UA 与可缓存提示头需分别验证 | 图片为使用 ffuf 的 GET 返回 403，并含 X-Check-Cacheable: YES，帖子建议随机 UA。 | [方法条目](../by-type/cache-deception.md) |
| 延时参数三点差异仍需无延时基线和执行次数分析 | 图片中 sleep 1、5、8 的响应约 10285、50216、80205 ms，均为 200 和 338 字节，体现随参数变化且约十倍的耗时。 | [方法条目](../by-type/sql-injection.md) |
| 复用 CSRF token 要定义所谓另一个 instance | 帖子把来自另一个“instance”的 token 用于请求。 | [方法条目](../by-type/csrf.md) |
| 重定向元数据目录结果要逐跳核对 URL 与请求头 | 请求携带 Metadata-Flavor: Google 与 X-Google-Metadata-Request: True，先访问外部重定向地址，响应内嵌 GoogleFrontEnd 的 0.1/、1.0/、computeMetadata/ 目录列表。 | [方法条目](../by-type/ssrf.md) |
| 反序列化清单中的类型和签名控制需绑定对象图及解析时机 | 二十五项图覆盖输入/类型/类过滤、对象图/长度、签名、沙箱、行为、日志、依赖与培训。 | [方法条目](../by-type/deserialization-rce.md) |
| 数字路由枚举应区分页面发现与私有对象权限 | 帖子用 /node/1–500 等数字路径寻找隐藏页面。 | [方法条目](../targeted-fuzzing.md) |
| 分号和重复斜杠绕过需对照代理与后端实际路由 | 归档用 /;/、/.;/、//;// 等形式尝试跨过 403。 | [方法条目](../by-type/idor-access-control.md) |
| Trusted Types 日志工具需实际堆栈与消费者支持 | 帖文提到通过日志/堆栈追踪 Trusted Types，配图为 Google 首页的空 DevTools 控制台。 | [方法条目](../by-type/xss.md) |
| Android 线索迁移到 iOS 要重建客户端及后端边界 | 保存帖建议在 iOS 重复 Android 的发现，续篇并不完整。 | [方法条目](../by-type/mobile-ios.md) |
| Oracle XML 函数回连样本需核对数据库解析及关联事件 | 归档 SQL/XML 候选使用 EXTRACTVALUE、xmltype、dual 与外部参数实体，保存字符串还有 httpp//burp/ 一类不完整地址。 | [方法条目](../by-type/xxe.md) |
| Pulsar 管理口的默认凭据说法需核对服务及实际权限 | 帖文将管理入口与 pulsar 默认凭据联系起来，但未保存成功登录/权限结果。 | [方法条目](../by-type/authn-session.md) |
| 私有 API 文档中的对象 ID 不授予批量访问权 | 帖子根据私有端点文档处理用户 ID，配图只有 IDOR 报告列表/Low 标签。 | [方法条目](../by-type/idor-access-control.md) |

| Host 改成回环地址后的数据库错误不能单独证明服务端请求 | 保存请求是 GET /、HTTP/2、Host: 127.0.0.1，响应显示 WordPress mysqli 的 getaddrinfo 与数据库连接失败，帖文明确说继续 fuzz localhost/私有地址仍无结果。 | [方法条目](../by-type/host-header.md) |
| 数据库连接错误中的路径泄露应按实际字段描述 | 保存图片展示 WordPress 文件路径、行号、数据库连接/名称解析错误，未见完整凭据或数据。 | [方法条目](../by-type/info-secrets.md) |
| 反射 XSS 的沟通评分不构成通用高危标准 | 图片中作者因修复后载荷无效要求提高严重性，triager 仍保留 Medium，正文提及 6.1 而侧栏为 4.7，并有奖金通知。 | [方法条目](../reporting.md) |
| 邮件显示名称保护需与真实发件身份和认证结果区分 | 保存帖声称可将邮件显示为 Google，但没有保存原始邮件或伪装 PoC。 | [方法条目](../by-type/authn-session.md) |
| 不再复现与由本报告推动修复须分别举证 | 图中产品团队说明：若问题已不可复现，可能来自例行维护/计划升级，且未因该报告创建内部修复请求。 | [方法条目](../reporting.md) |
| 围绕一个漏洞类型学习要形成可验证的消费者模型 | 帖子建议选一个漏洞类型，研究资源、原理和不同载荷。 | [方法条目](../experiment-design.md) |
| 回连日志通知需要独立保存事件和归因证据 | 帖子介绍 PHP 日志加 Telegram 通知用于 SSRF、XXE、盲 XSS；图中是一条 curl GET、代理/来源头与时间信息。 | [方法条目](../discovery/records-and-incremental.md) |
| script.src 与 default-src self 问题需核对完整策略及资源内容 | 保存帖仅提问：CSP default-src self 下 script src 是 sink 是否可绕过。 | [方法条目](../by-type/xss.md) |
| 每日扫描前一千端口并不覆盖全部服务或证明未授权面板 | 帖子用 naabu top-ports 1000 且排除 80/443 寻找开放仪表盘，并提到奖金。 | [方法条目](../discovery/passive-and-services.md) |

| 搜索索引和 JS 路径用于发现，接口权限须另行验证 | 归档描述搜索操作符及从 JS 找未认证接口。 | [方法条目](../discovery/passive-and-services.md) |
| dotenv 与备份配置暴露需按原始响应和字段用途确认 | 归档线索包括 /.env、/api/.env、wp-config.php.bak 和 config.inc.php_bk。 | [方法条目](../by-type/info-secrets.md) |
| UDP 单包发现与服务探测的覆盖口径不同 | UDPX 介绍单包及服务标签；Nmap 示例用 -sU/-sV/强度 0/-F，续帖却称前千端口。 | [方法条目](../discovery/passive-and-services.md) |
| 程序年龄和已解决数量不能替代授权模型覆盖 | 帖子以旧私有程序仍发现问题及访问控制适合初学者为方向。 | [方法条目](../hunting-strategy.md) |
| HTML 实体协议变形需追踪实际解码与链接消费者 | 帖子从合法/非标准 href 测到 javascript 被拦及编码实体候选。 | [方法条目](../by-type/xss.md) |
| 流量模型建议必须留在候选层并保留证据来源 | BurpGPT/ReconAIzer 介绍流量分析，图片展示建议参数/端点菜单和模型输出的 SQL/授权候选。 | [方法条目](../by-type/ai-application.md) |
| 搜索请求与 sqlmap 命令截图不证明数据库执行 | 图片为 WordPress 搜索 POST 路径及 sqlmap 参数，未保存完整正文、计时对照或工具结果。 | [方法条目](../by-type/sql-injection.md) |
| 脚本聚合端点的资源问题须有有界基线 | 图片摘要说 load-scripts.php 一次聚合多 JS/CSS 且数量/大小未限，历史编号 CVE-2018-6389。 | [方法条目](../experiment-design.md) |
| 计划帖创建与编辑链接应采用同一协议校验 | RichText/Markdown 案例摘要指出编辑计划帖时服务端链接过滤与创建不一致，可能存入 javascript scheme。 | [方法条目](../by-type/xss.md) |
| 仓库中的重入缺口与部署合约风险需要分别证明 | eth-monero 原子交换图片提及 SwapFactory.sol 及攻击者构造参数，同时明确作者未找到该代码的实际部署，另一已见合约未受影响。 | [方法条目](../by-type/smart-contract.md) |
| SSH 连接复用应把认证选项纳入等价关系 | libcurl 历史案例称两个 SSH 设置未参与连接池匹配，换 SSH key 后仍可能复用旧连接。 | [方法条目](../by-type/desktop-client.md) |
| 静态后缀的缓存欺骗需证明跨身份取到私有内容 | Algolia 摘要描述登录用户访问随机 CSS 名后缀，代理缓存动态私有响应。 | [方法条目](../by-type/cache-deception.md) |
| SSH CA 证书的用户名扩展不能代替应用主体校验 | Gist 历史摘要把 login@github.com 的用户名扩展与缺失认证流检查联系，涉及受信证书机构、组织身份及已知 gist URL；图中另修正公开 gist 也可能被修改。 | [方法条目](../by-type/authn-session.md) |
| 扩展名、phpinfo 与禁用函数是不同上传消费边界 | 归档列 .htaccess、SVG/大小写/双扩展/空字节、引号文件名和多种应限制扩展；另帖说上传 PHP 能看到 phpinfo 但命令函数禁用。 | [方法条目](../by-type/file-upload.md) |
| 跨搜索引擎、WHOIS 和证书索引需保留归属与日期 | Netlas 图片展示 WHOIS/DNS/相关域/服务标签及带时间字段的导出弹窗，帖文提倡多引擎和证书过滤。 | [方法条目](../discovery/passive-and-services.md) |
| UA 阻断与可缓存提示不证明跨请求污染 | 图片中 Fuzz Faster U Fool UA 的 GET 返回 403、X-Check-Cacheable: YES。 | [方法条目](../by-type/cache-deception.md) |
| 通用检查清单应从范围和实际功能落地 | 保存清单从程序规则/范围、功能、域名/目录、技术栈和默认/测试/敏感文件开始，但续篇不完整。 | [方法条目](../scope-and-rules.md) |
| 域名导出脚本需核对采集完整性与密钥边界 | SecurityTrails 图中 Python 直接解析 subdomains 并追加文件，硬编码 API key、关闭 TLS 校验且未见状态/超时/分页/去重处理。 | [方法条目](../discovery/passive-and-services.md) |
| Burp 中 URL 形态参数是请求消费者候选 | 帖子搜索 =https:// 或 =http:// 寻找隐藏 SSRF。 | [方法条目](../by-type/ssrf.md) |
| 隐藏参数与漏洞类型需要实际数据流支持 | 归档提示检查隐藏参数并称发现 XSS，图片只有奖金邮件。 | [方法条目](../targeted-fuzzing.md) |
| JSON 的 $where 延时样本须定位数据库脚本消费者 | 图中 configId 数组旁的 $where 使用 Date 忙循环约三十秒，帖文把它称服务器 JavaScript 注入。 | [方法条目](../by-type/nosql-injection.md) |
| 三层对象 ID 的替换应验证父子归属而非穷举排列 | 图片列 account/user/note 路径的六种替换，另帖提到 Drupal /node/，配图仅 triaged 通知。 | [方法条目](../by-type/idor-access-control.md) |
| 远程命令读取循环以已有执行权限为前置 | PowerMeUp 图能见 TCPClient/网络流、读取命令并调用表达式的循环，部分小字和参数不完整。 | [方法条目](../source-audit.md) |
| AEM selector 路径差异需保持原样并核对真实 servlet | 归档从 /content.1.json 404 转向 /conten/.1.json、/conten/t.1.json、tidy/infinity 等变形，其中原拼写并不一致。 | [方法条目](../discovery/web-and-api.md) |
| 拖放填充受控数据需证明目标动作及信任边界 | 帖文说让用户拖放以将受控数据写入表单，未保存基本样例的实际代码/结果。 | [方法条目](../discovery/client-and-cloud.md) |
| 多步点击覆盖样例与拖放标题并非同一机制 | 保存图实际是透明 account iframe 叠在两个提示点击位置，未见拖放数据处理。 | [方法条目](../by-type/clickjacking.md) |
| shell 运算符、编码和引号变形应按真实解释器语义验证 | 归档用引号终止、管道/条件/后台/换行及 Base64 候选；解码文本仅为文件读取加过滤，没有执行。 | [方法条目](../by-type/cmd-injection-rce.md) |
| URL 中凭据的历史索引线索不能授权使用他人账号 | 帖子建议对 GET 用户名/密码搜索 Web Archive，图片只有感谢信息。 | [方法条目](../by-type/info-secrets.md) |
| 注册报错后访问入口需核对事务与会话状态 | 归档建议在注册字段填 1、忽略错误，再访问原先跳登录的端点。 | [方法条目](../by-type/authn-session.md) |
| 相邻搜索路由的反射标记不能合成已确认 XSS | 两张 Equifax 报告图分别是 personal/help/search 的 search 和 personal/search 的 q，显示 broook 在源码/JavaScript 中出现。 | [方法条目](../by-type/xss.md) |
| 导出环境变量只沿进程继承边界传播 | 归档把 export MYGLOBAL 称全局，并展示 unset。 | [方法条目](../source-audit.md) |
| 离线账户文件修改以文件控制和系统权限为前置 | 帖子提到 chntpw/SAM 与 Linux shadow/passwd。 | [方法条目](../by-type/desktop-client.md) |
| 请求头延时筛选需要数据库消费与计时负例 | 归档把 User-Agent/X-Forwarded-For 的 XOR/IF/SLEEP 及 httpx 大于十三秒阈值作为候选。 | [方法条目](../by-type/sql-injection.md) |
| 截图列表需要逐项结果而非仅输入域名 | Haylxon 图片只显示 urls.txt；另帖建议 httpx 后 Aquatone 截图。 | [方法条目](../discovery/records-and-incremental.md) |
| BitLocker 恢复保护操作需要权限和实际状态证据 | 归档给定 SYSTEM 登录任务添加恢复密钥及查看保护器的命令，但没有运行结果。 | [方法条目](../by-type/desktop-client.md) |
| 归档 URL 聚合界面需保留来源与现存性 | LazyHunter/帖称 LazyRecon 的截图列历史 CSS/JS/字体路径及 Wayback 脚本入口。 | [方法条目](../discovery/passive-and-services.md) |
| 静态网站减少部分消费者而不消除全部安全边界 | 帖子把 Hugo/Jekyll 静态站点描述为没有安全顾虑。 | [方法条目](../source-audit.md) |
| 大规模 recon 管道要核对采样、去重和阶段回执 | 图片的 SQL 管道串联子域/DNS/历史 URL、问号筛选、前二十条、HTTP 和多 URL 检测；正文称五 VPS、百万资产及数十亿请求。 | [方法条目](../discovery/records-and-incremental.md) |
| Kiosk 的文件、shell 协议和对话框访问需要实际限制模型 | 归档列系统二进制、C$、环境变量、file 路径变体、shell 协议及文件上传对话框。 | [方法条目](../by-type/desktop-client.md) |
| 端口、ICMP 与协议发现要按实际参数集合计数 | 归档含固定端口 masscan、ICMP echo/timestamp、HTTP 端口、SCTP INIT 和 assetfinder→httprobe。 | [方法条目](../discovery/passive-and-services.md) |
| URL 拼接与可信服务例外应以最终解析主机为准 | 可见书页讨论硬编码店铺域名与用户部分拼接，以及历史 Zendesk 自定义域/return_to 绕过外站提示的案例。 | [方法条目](../by-type/open-redirect.md) |
| Firebase 配置可见与数据库 Rules 放行是不同证据 | 图片代码从公开配置初始化后调用 db.get 并遍历所有记录，没有执行结果。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| SQL 延时摘要与元数据提取结论需要各自原始证据 | Sony 图片摘要称用 sleep(0) 及 SQLMap 提取表名/数据库身份/主机名，但原请求、计时与工具输出均未保存。 | [方法条目](../by-type/sql-injection.md) |
| URL 列表附认证头需限制凭据作用域并保留对照 | 帖子介绍多线程目录探测及 cookie/Authorization URL 检查，图片仅工具仓库卡。 | [方法条目](../discovery/web-and-api.md) |
| 认证实验题目分类不能代替真实流程覆盖 | 图列已完成的认证实验：不同响应/时间/锁定的枚举、2FA、重置、IP 防护、长期 cookie、离线口令、多凭据等。 | [方法条目](../by-type/authn-session.md) |
| 注销反馈里的盲 XSS 需要绑定实际后续阅读环境 | 保存帖给出注册、删除账户时填反馈的入口，没有保存载荷或回连。 | [方法条目](../by-type/xss.md) |
| 多模板和严重性终端标签须回到响应与版本验证 | 图中 Nuclei v2.9.2、模板 9.4.2/outdated、Swagger/phpMyAdmin/Jira/CVE/OAST 等标签，目标数为 30274/90937。 | [方法条目](../discovery/records-and-incremental.md) |
| 备份扩展和逐路径发现需保留真实工具语法及采样范围 | 归档列多种扩展与类似 dirsearch-e 的原写法，另帖称隐藏文件包含多数漏洞。 | [方法条目](../targeted-fuzzing.md) |
| 嵌套表单操作符与真假差异须核对查询构造 | 帖子给出 list/List、数组形式 $lt/$in/$nin 的 true/false 差异。 | [方法条目](../by-type/nosql-injection.md) |
| 联系人删除的 GET 跨站操作与跨用户授权应分开 | 图中自有联系人删除是 GET，给出默认 GET 表单且说缺少 CSRF。 | [方法条目](../by-type/csrf.md) |
| 云客户端密钥标题不证明整个租户管理权 | Azure 图声称 JS client ID/secret 可生成 token，AWS 图仅称可列资源，均缺少原字节/授权请求/策略结果。 | [方法条目](../by-type/info-secrets.md) |
| WHOIS 查询中的 SQL 字样需要真实后端消费证据 | 归档将带引号/条件的 WHOIS 查询发往指定服务并称可取所有信息。 | [方法条目](../by-type/sql-injection.md) |
| 审计策略基准对照与 SIEM 事件接收不同 | auditpolCIS 表比较各子类别的当前/预期审计设置和 pass/fail，并包含不要求审计的规则。 | [方法条目](../discovery/records-and-incremental.md) |
| 文件样式内容需独立绑定入口，不能从配文补链 | Netlas 证书导出配文的实际图片却为浏览器中 passwd 风格账户行，URL/参数被遮挡。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Prow 签名 URL 应限制到获授权桶和对象前缀 | 图片摘要称通过 job-history/S3 路径签名基础路径可能读取非日志对象，展示编码路径但缺少实际签名/响应。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 报告结构与自动摘要中的根因和修复要回到原证据 | 结构图列标题类型/入口/方式、描述、复现、载荷、条件、影响与可选建议/引用；Hacktivity 图明确多条摘要自动生成。 | [方法条目](../reporting.md) |
| Kubernetes Java YAML 库的风险需证明下游可达 | 图提 Kubernetes Java Client 17.0.0 的 Dynamics 将不可信 YAML 转 DynamicKubernetesObject 与 SnakeYAML/CVE-2022-1471，作者未找到测试之外下游使用。 | [方法条目](../by-type/deserialization-rce.md) |
| 启用 2FA 的旧会话与零验证码新登录是两类检查 | Rocket.Chat 摘要称启用 2FA 后已有会话仍有效；另帖称 000000 可过 2FA/邮箱确认但被列 informative。 | [方法条目](../by-type/authn-session.md) |
| 相同前端栈的另一子域要重新核对模板与范围 | 帖子由 Angular 指纹和 XSS 清单转向另一子域，图片为 CSTI resolved 通知。 | [方法条目](../by-type/waf-bypass.md) |
| 编辑消息时间应区分原始创建时间与编辑排序 | Rocket.Chat 摘要称修改消息会改变原时间戳和排序。 | [方法条目](../by-type/business-logic.md) |
| 解析器 ReDoS 需区分库版本、复杂度与网络可达性 | Ruby Time/URI 图片分别描述非法字符串的特定字符导致耗时及历史 gem 分支修补。 | [方法条目](../experiment-design.md) |
| SQLite 错误中的表名和占位 SQL 不证明注入 | 图的 errno 19/SQLITE_CONSTRAINT 包含 BasketItems INSERT 和占位符片段。 | [方法条目](../by-type/info-secrets.md) |
| 模块搜索元数据不能证明目标满足利用条件 | MSF 示例按平台、端口、目标和模块类型筛选，只是目录查询。 | [方法条目](../source-audit.md) |
| 回连 shell 的启动示例以既有执行权和通信条件为前置 | 归档 Bash Base64 解码只是带 nohup 的回连命令，Xterm 示例依赖 X 服务/显示及连接授权。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 预览与 webhook 需约束解析和连接时的最终地址 | Matrix 图片只支持部分盲的服务名称/IP 线索，RCE 被列为需另行许可的可能；Omise 摘要仅提自定义 URL 的 DNS rebinding。 | [方法条目](../by-type/ssrf.md) |
| 发行桶的未认领声明需绑定实际分发与验证策略 | Brave 两份历史摘要涉及 RPM keyring 和 APT 安装所用 S3 名称，作者称已认领/上传 proof，但完整附件未保存。 | [方法条目](../by-type/subdomain-takeover.md) |
| 错误页 HTML 注入和 cPanel 路径载荷须分别验证执行 | coins.state.gov 图明确 XSS 尝试无结果而仅 HTML 注入；另帖给 cpanelwebcall 编码路径及历史 CVE-2023-29489，但没有目标响应。 | [方法条目](../by-type/xss.md) |
| 注册延时载荷与 P1 奖金须分开作为证据 | 正文给参数中的条件/SLEEP 候选，图片仅 Unresolved/P1、奖金额和点数。 | [方法条目](../by-type/sql-injection.md) |
| 联系表单的邮件头注入需要实际信封与投递对照 | 帖子描述未校验输入进入 SMTP 头，图片仅教程封面和模糊 SSRF 背景。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 可公开取得秘密与获准使用秘密不同 | 帖文讨论密码公开及程序范围取舍。 | [方法条目](../scope-and-rules.md) |
| ADB 工具功能以配对、设备权限和既有访问为前置 | PhoneSploit Pro 菜单显示连接、shell、截图、文件/应用及 Metasploit 动作，没有实际设备结果。 | [方法条目](../by-type/mobile-android.md) |

| SQL 错误索引与等待函数的归因边界 | 保存帖以 MySQL/SQL Server/Oracle 错误搜索串寻找候选，并宣称 WAITFOR/SLEEP 后出现延迟。 | [方法条目](../by-type/sql-injection.md) |
| Karaf 默认凭据线索与管理能力的独立证明 | 保存帖声称 Karaf 默认用户名/密码。 | [方法条目](../by-type/authn-session.md) |
| 缺值 SQL 错误不是注入的充分证据 | 示例 MySQL 1064 查询中 id 缺值且另有 nom_hachage 条件。 | [方法条目](../by-type/sql-injection.md) |
| cPanel webcall 错误页反射与模板误报分开审查 | 保存 YAML/PoC 指向 /cpanelwebcall 并使用编码标签；图片错误页与 prompt 对话框支持特定历史反射场景。 | [方法条目](../by-type/xss.md) |
| Nuclei cPanel 模板的输入、匹配条件与运行证据 | 分别保存引擎/模板版本、模板摘要、原始路径字节、matchers-condition 和每个 matcher 的实际输入。 | [方法条目](../source-audit.md) |
| 字符引用混合脚本方案需穿过真实链接消费者 | 保存 href 例子用 HTML 字符引用、控制字符和动态属性取值构造脚本方案。 | [方法条目](../by-type/xss.md) |
| LiteSpeed 过滤差异的比较单位是解码后的消费者 | 归档称 ModSecurity/LiteSpeed 可被编码变体绕过，但没有规则版本与实际请求响应。 | [方法条目](../by-type/waf-bypass.md) |
| Symfony 调试入口与配置查看的可见范围 | 正文列 profiler/phpinfo/debug 路径，原文 /_fragement 拼写保留为候选，不能静默修正后当作已验证入口。 | [方法条目](../by-type/info-secrets.md) |
| 理解应用设计后再提出漏洞假设 | 保存帖以设计缺陷获奖为例；可复用的是梳理用户、角色、状态、数据归属和受保护操作，找出同一规则跨入口是否一致。 | [方法条目](../hunting-strategy.md) |
| 响应请求和调解需要新增事实而非状态推断 | 把 Request a response、提交支持请求和调解分别记录为沟通入口；明确争议是范围、对象可得性、影响还是重复关系。 | [方法条目](../reporting.md) |
| 奖金额分享许可与技术披露许可分开 | 保存材料明确只获准分享奖金额。 | [方法条目](../scope-and-rules.md) |
| JBoss 管理入口可见性与部署权限逐步验证 | 端口发现→HTTP 服务识别→管理身份验证是不同阶段。 | [方法条目](../by-type/authn-session.md) |
| 配套移动应用 TLS 验证与设备链分开 | Ray-Ban 配套 app 的缺少证书验证只是保存正文的声明。 | [方法条目](../by-type/mobile-android.md) |
| 数字 node 的前导零与对象授权规范化 | /node/ 编号及前导零变体是候选。 | [方法条目](../by-type/idor-access-control.md) |
| 拼接运算符受数据库与表达式上下文约束 | 正文列 Oracle/PostgreSQL 双竖线、SQL Server 加号和 MySQL 字符串/CONCAT 形式。 | [方法条目](../by-type/sql-injection.md) |
| 目录列表中的 CSV 文件名与隐私内容分开 | 上传目录或 listing 暴露文件名不等于正文声称的 30k PII 已获证明。 | [方法条目](../by-type/info-secrets.md) |
| DNS 候选、服务协议和网页可达性分别计数 | DNS zone 导出要求已有权限；related-domain/解析器/通配筛选只提供候选，不授予扫描范围。 | [方法条目](../discovery/passive-and-services.md) |
| MongoDB 脚本族结果按信息与权限拆分 | 保存 Nmap mongo* 与默认端口例子没有实际输出。 | [方法条目](../by-type/nosql-injection.md) |
| 交互终端与横向执行工具依赖已有执行权限 | PSEXEC/WMI/远程 PowerShell、PTY/script、ReverseSSH 是已有权限下的操作角色，不能当作最初命令注入证据。 | [方法条目](../by-type/cmd-injection-rce.md) |
| multipart 限文件数仍需限制全部 part 与解析成本 | 保存 Rack 公告指出只限制 file parts、未限制 total parts 会放大解析耗时。 | [方法条目](../source-audit.md) |
| Git 配置、历史提交和失效凭据的证据边界 | Git 是目录/元数据结构，不能把 .git 当一般文件扩展名。 | [方法条目](../by-type/info-secrets.md) |
| 地图 API key 前缀与可滥用权限不是同一事实 | AIza 类前缀是识别候选，需核对键用途、来源和是否设计为公开客户端标识。 | [方法条目](../by-type/info-secrets.md) |
| Connection 指定长度字段后的多跳边界错配 | 保存图示第一代理以 Content-Length 读取正文、又因 Connection 提名剥离该字段，第二代理把余下 body 解释成另一请求，造成响应队列错配。 | [方法条目](../by-type/request-smuggling.md) |
| 依赖混淆以实际解析器选源为前提 | 未注册包名或同名公共仓库只提供冲突线索。 | [方法条目](../source-audit.md) |
| 登录方式冲突可能是账号状态锁死而非 2FA 绕过 | 历史正文称 Google 登录与邮件登录/2FA 状态冲突导致无法登录。 | [方法条目](../by-type/authn-session.md) |
| 探测性能与去重必须保留逻辑资产维度 | subfinder→httpx screenshot、hrekt 和 reconbulk 只是候选/探测链。 | [方法条目](../discovery/records-and-incremental.md) |
| 消息外部媒体请求的接收者和可见字段 | 保存 LinkedIn 报告把 GIF 消息 JSON 的外部 media 引用改为接收器，称收件人打开消息触发请求。 | [方法条目](../by-type/info-secrets.md) |
| 账号凭据变更在每个业务入口绑定再认证 | 保存 extra-member JS 路由与 create-credentials 表单，文章声称该入口能变更当前账号邮件/密码而无需 MFA。 | [方法条目](../by-type/authn-session.md) |
| 链接预览超时不能代替字节与并发预算 | 保存 Nextcloud reference fetch 报告说明 10 秒 timeout 内仍可消耗大量网络/临时磁盘。 | [方法条目](../by-type/ssrf.md) |
| Firebase 工具成功输出仍需 Rules 与回读对照 | 截图先因缺少 exploit.json 失败，创建本地文件后给出 Exploited URL。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| ReconAIzer 的建议应回到资产证据链 | 复用已审阅的 ReconAIzer 菜单材料，只把 AI 枚举/解释视为候选生成。 | [方法条目](../by-type/ai-application.md) |
| 验证、复测和关闭分别留下可复现结论 | 截图时间线先 validated/triaged、后修复团队 review、retesting、No the fix works、accept retest 和 Resolved。 | [方法条目](../reporting.md) |
| GitConfig 和 Grafana 索引结果保留采集时间 | LeakIX 插件/国家查询可显示 gitconfig origin，Netlas title 查询可显示 Grafana 历史响应、IP/ASN 和分页数量。 | [方法条目](../discovery/passive-and-services.md) |
| 更新攻击工具帮助与供应链可达链分开 | 保存 sh4dowup help 列镜像/路由、包修改、keygen/sign/HSM、build/check 等角色。 | [方法条目](../source-audit.md) |
| 历史链接和隐藏参数只生成可验证候选 | Wayback、hakrawler depth、kxss、Arjun 等输出需保留来源日期、目标路径和参数上下文，先筛范围与重复，再确认当前路由和消费者。 | [方法条目](../discovery/web-and-api.md) |
| 代理头列表应按具体消费者拆解 | 原帖列 Host、X-Forwarded-*、X-Forwarder-* 等且有拼写/空格差异，保留原字节作为待核对线索，不静默补成合法头。 | [方法条目](../by-type/host-header.md) |
| 直接源站候选仍需资产归属和项目授权 | 保存 Confluence/Okta 案例声称由源站 IP 和弱凭据绕过入口，图片却有超时及厂商明确资产不在程序内的回应。 | [方法条目](../scope-and-rules.md) |
| UTM 参数的缓存键与响应差异分别比较 | utm_content 等追踪参数可能改变响应而不进缓存键，但仅名为 UTM 不证明风险。 | [方法条目](../by-type/cache-deception.md) |
| PHPUnit eval-stdin 的部署路径和执行结果绑定 | 保存截图 GET vendor/phpunit/.../eval-stdin.php 带 PHP body，响应展示 www-data 身份。 | [方法条目](../by-type/cmd-injection-rce.md) |
| REcollapse 规范化探索以双消费者对照收敛 | 工具 help 说明字符位置、编码形式、范围、大小、规范化次数/表。 | [方法条目](../targeted-fuzzing.md) |
| 重置申请不应在验证完成前改变账号凭据 | 保存正文称 reset request 先变更密码、邮件后验证。 | [方法条目](../by-type/authn-session.md) |
| 扫描 SaaS 评估先核对私密数据出境边界 | 保存帖子批评收费封装工具及私密程序数据上传第三方，价格批注不是欺诈证据。 | [方法条目](../scope-and-rules.md) |
| Blind XSS 回调应绑定输入、渲染主体和时间 | 原帖有自动参数/头部喷射以及历史 URL→User-Agent 外部脚本命令。 | [方法条目](../by-type/xss.md) |
| image_proxy 读取响应与云接管不是同一证据 | 截图 url 参数指向 link-local metadata 并返回 Success/AWS-HMAC 字段，但凭据未展示。 | [方法条目](../by-type/ssrf.md) |
| SQL shell 与 OS shell 依赖不同权限 | 正文 sqlmap 参数只提供工具调用意图。 | [方法条目](../by-type/sql-injection.md) |
| phpinfo 指纹确认保留 HTTP 主机与状态反例 | Shodan SSL/200 线索与 ffuf 200/429 过滤只是候选。 | [方法条目](../by-type/info-secrets.md) |
| Stripe 历史无 CSP 绕过报告保留执行边界 | 截图描述 custom link 的脚本方案与 CUSTOM Button href，作者承认 CSP 阻止执行；当时特定程序允许无 CSP bypass 的有效 XSS 降级受理。 | [方法条目](../by-type/xss.md) |
| ICE 服务器配置暴露不自动成为 TURN 内网代理 | POST 配置响应列 webrtc_server 的 STUN/TURN URL 及用户名/credential。 | [方法条目](../by-type/ssrf.md) |
| contenteditable 事件与顶层调用的触发条件 | 正文 onbeforeinput、array map 等变体只有在 HTML 属性解析、可编辑元素实际输入与执行环境满足时才有意义。 | [方法条目](../by-type/xss.md) |
| AI 与表单生成的 dork 先验证语法和范围 | 生成界面以输入域名组合 ext/inurl/report 查询；AI 多引擎输出仍可能有无效语法、非范围域名或空结果。 | [方法条目](../discovery/passive-and-services.md) |
| 资产导出来源失败应与最终完成提示分开 | DNSdumpster 导出/数量限制属于保存帖的历史工具描述；CIDR 聚合脚本用 RIR org/customer/POC 邮件、BGP、区域登记产生 CSV/列表，却有 network unreachable 后仍 found/finished。 | [方法条目](../discovery/passive-and-services.md) |
| 漏洞收件方以具体公司和资产责任归属确认 | 保存 Volvo Cars 邮件指出同品牌不同公司、该 homepage 非其资产并转正确公司；正文还提醒负责任通报而非威胁索款。 | [方法条目](../scope-and-rules.md) |
| SLEEP 请求和报告状态不能替代时间对照 | 正文宣称 SLEEP(5) 得到约 15 秒，头部卡片用 MySQL XOR/now/sysdate 及 SLEEP5/10，状态图片无计时。 | [方法条目](../by-type/sql-injection.md) |
| self HTML 注入转为 SSRF 需要另一个服务端消费者 | 自己浏览器渲染 HTML 可触发客户端资源请求；要升级 server fetch，必须证明预览/转换/文档渲染等另一消费者实际接收该内容并以服务器身份发请求。 | [方法条目](../by-type/ssrf.md) |
| 路径字符串进入脚本的上下文不能由短 payload 推算 | 保存 TD 报告给 TechnicalInsight 路径和拼接风格字符串，URL 含分隔符。 | [方法条目](../by-type/xss.md) |
| 私网地址范围与重定向响应的取回主体 | 归档把 172.16 地址称 Class B；应按 172.16.0.0/12 即 172.16–31 范围识别，不能扩大到整个 172/8。 | [方法条目](../by-type/ssrf.md) |
| GraphQL 删除 campaign 仍需执行对象归属检查 | 保存 Delete Campaigns 报告只露 POST/graphql、cookie、JSON/CSRF 和编辑页 referer，实际 mutation 在裁切外。 | [方法条目](../by-type/idor-access-control.md) |
| SSO 多入口会话测试保留步骤缺口 | 只保存第 3/4 步及另一 aspx 入口描述，不能补造之前账号、cookie 和重放序列。 | [方法条目](../by-type/authn-session.md) |
| 支付沙箱测试参数不等于生产绕过 | Stripe/Plaid sandbox 文档链接未保存全文，正文提示使用测试流程。 | [方法条目](../business-modeling.md) |
| Android 静态目录、改签与组件权限分别审计 | 保存速查表列 APK 的 manifest/DEX/lib/assets、数据目录、签名、重打包、provider 和 activity。 | [方法条目](../by-type/mobile-android.md) |
| iOS bundle、容器与插桩返回值的身份边界 | 保存 iOS 表列 bundle ID、应用 bundle/data UUID 目录、Frida/Objection、文件观察和 NSLog。 | [方法条目](../by-type/mobile-ios.md) |
| iOS 备份取证先绑定加密、时间和 Manifest 映射 | 保存 forensics 表区分 USB 备份、加密/解密、Manifest.db 及 data/network/config/log artifacts。 | [方法条目](../by-type/mobile-ios.md) |
| 本地调试与 ELF 修改建立可复现崩溃证据 | PWN 表列 GDB/LLDB attach、断点、内存观察、ADB forward、AFL/QEMU 与 PatchELF。 | [方法条目](../by-type/mobile-android.md) |
| 防火墙清单按策略层与会话前提解释 | 保存清单混列网络探测、隧道、WAF、ARP/TLS 和应用注入工具；不能按一个 tool label 推断所有 firewall bypass。 | [方法条目](../discovery/passive-and-services.md) |
| shell glob 与 IFS 展开只在实际解释器内成立 | 已审阅相同根目录 glob/IFS 图片，当前正文继续推荐 globbing。 | [方法条目](../by-type/cmd-injection-rce.md) |
| JSON 邮件数组到 JavaScript sink 需逐层证明 | 保存 JSON array 邮件样例包含脚本风格字符串；合法 JSON 字符串/数组本身不会执行。 | [方法条目](../by-type/xss.md) |
| favicon 指纹绑定原文件和算法而非品牌授权 | 当前图片复用已审阅 favicon 查询菜单。 | [方法条目](../discovery/passive-and-services.md) |
| HTTP header 名中的换行与下游命令执行分开 | 保存 Ruby Net::HTTP 示例在 header key 中放 CRLF，展示接收 socket 的报文，历史报告为 Informative/0。 | [方法条目](../by-type/crlf-response-splitting.md) |
| deep link 入口需要复核本地 PIN 守卫 | Nextcloud Android 报告标题称第三方生成 deep links 可绕本地 PIN，截图没有 intent/操作序列。 | [方法条目](../by-type/mobile-android.md) |
| 验证后再规范化可重新生出路径穿越片段 | 保存 Folder::getFullPath 先 isValidPath 再 normalizePath 的代码，说明反斜杠转斜杠可能再次形成 /../。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 本地响应编辑不改变服务器权限事实 | DevTools header 编辑及 user_role→admin_role 匹配替换可能只改客户端显示。 | [方法条目](../by-type/idor-access-control.md) |
| JWT claim 的 DOM 输出与签名信任分开 | 如果 claim 被解码并渲染进 DOM，XSS 依赖具体 sink、编码和可控制字段；显示任意未验证 token 与服务器接受签名 token 是不同路径。 | [方法条目](../by-type/jwt.md) |
| Unicode 引号示例保持原字节与数据库上下文 | 正文登录绕过式字符串使用弯引号/长横线等，未显示实际发送请求和 SQL 文本。 | [方法条目](../by-type/sql-injection.md) |
| 带 tab 的脚本方案受 URL 消费者与用户动作约束 | 保存反向 URL/编码 javascript 候选。 | [方法条目](../by-type/xss.md) |
| 交易列表与详情以对象归属对照证明越权 | 保存图片列表为 id830551、详情请求为830、正文又用另一ID；三者不能自动绑定同一交易。 | [方法条目](../by-type/idor-access-control.md) |
| 隐藏参数发现后仍需 DOM source 到 sink 链 | Arjun/Dalfox 及编码闭合脚本变体只是候选生成/检测角色。 | [方法条目](../by-type/xss.md) |
| 大小写与 onsubmit 触发必须在原上下文验证 | 保存 Expedia origCity/UPPER/WAF 报告称 onsubmit 还需点击。 | [方法条目](../by-type/xss.md) |
| 可嵌入页面与诱导提交链需要独立证据 | 同报告把 clickjacking 当 XSS 触发辅助，必须分别确认 frame-ancestors/X-Frame-Options、受害主体、自控嵌入层、可见交互和 onsubmit 后实际保护操作。 | [方法条目](../by-type/clickjacking.md) |
| 少见标题和相邻 ASP 文件只产生路由假设 | Shodan title 与 frmLogon2→frmLogon1 等相邻名称可提示候选；保存采集日期、当前范围、方法和请求参数，确认是否同应用及真实消费者。 | [方法条目](../discovery/web-and-api.md) |
| 持续项目与按需项目的范围按当次规则记录 | 归档提到 On-Demand、新邀请、私密和 ongoing 程序的选题偏好。 | [方法条目](../hunting-strategy.md) |
| 盲 fetch 与端口推断分别设置可证伪对照 | 保存 Elastic /api/v1/http/default/raw 的 regex/statusCode/url 请求指向回调端口，未保存回调或时间响应。 | [方法条目](../by-type/ssrf.md) |
| slash redirect 模板命中需保留真实 Location | Nuclei 保存输出含 slash URL 和引擎/模板历史版本，只有 matcher 命中。 | [方法条目](../by-type/open-redirect.md) |
| Opera 文件接收路径到 CGI 映射分别追踪 | 保存 FileReceiver 的 filename 指向 D 盘 CGI 目录、multipart CGI 内容及随后 operabin CGI 返回本地文件片段。 | [方法条目](../by-type/file-upload.md) |

| 代码索引候选必须绑定文件用途与最小暴露字段 | GitHub dork、代码片段站和 Trello 搜索只是候选来源。 | [方法条目](../by-type/info-secrets.md) |
| 历史 IP 到实际站点服务的范围与路由映射 | Shodan IP、目录发现、httpx 与模板扫描分别产出不同层候选。 | [方法条目](../discovery/passive-and-services.md) |
| 已知泄露路径和参数标记需检查真实响应内容 | gf/参数列表、AEM content/dam、历史 IP 目录线索可提示检查点，但模式匹配不提供内容或读权限证据。 | [方法条目](../by-type/info-secrets.md) |
| 短时阅读应用与异常流程假设的验证单位 | 将注册、登录、对象归属、状态切换和主要保护动作写成规则，再对边界值和异常顺序提出可证伪假设。 | [方法条目](../hunting-strategy.md) |
| 程序发现偏好不能推断竞争和授权 | 新公开、私密邀请和多个赏金平台可以作为选题线索；结合当前已持有邀请、范围、业务变化和可投入时间决定优先级。 | [方法条目](../hunting-strategy.md) |
| 失效域名的 IP 候选仍需 Host 与默认站点对照 | 域名不解析与历史关联 IP 上仍有虚拟主机服务是两个事实。 | [方法条目](../discovery/passive-and-services.md) |
| 搜索勾选和指纹工具输出是资产假设 | Google Hacking 选项、Wappalyzer 标识与 Subdomain Finder 名称列表应记录引擎、输入、来源和时间，并独立检查 DNS、权属、实际服务及范围。 | [方法条目](../discovery/passive-and-services.md) |
| 披露目录和 Burp scope 不构成测试许可 | responsible disclosure 搜索可用于找到规则入口；按当次项目政策绑定资产、账户、允许操作与日期。 | [方法条目](../scope-and-rules.md) |
| 业务更新和移动 UA 的新路径需独立落到资产记录 | 关注已授权目标的业务更新，并在同一路径比较普通/移动 User-Agent 的响应、重定向和最终 origin，记录客户端版本、账户及时间。 | [方法条目](../discovery/records-and-incremental.md) |
| WebSocket 的 OTP 线索须绑定消息方向和会话 | 先从已保存流量区分握手、连接所属账户、消息类型、方向和发送时点，再定位 OTP 是否由服务端发给正确用户。 | [方法条目](../by-type/websocket.md) |
| 批量模板来源先审查行为与匹配条件 | 多个 GitHub 模板仓库或克隆脚本只是来源集合。 | [方法条目](../source-audit.md) |
| 爬虫 GET 与 POST 发现需要分别记录输入来源 | Pcrawl 类工具称可发现 GET/POST；将链接、表单、JavaScript 与实际观察到的请求分别记录，保留动作、参数、内容类型、身份和消费者。 | [方法条目](../discovery/web-and-api.md) |
| 换行变体必须到达实际 HTTP 序列化边界 | 保存清单列 Set-Cookie、Location、Content-Length 与 HTML 混入候选。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 恢复缓存和数据库标签不代替 SQL 条件对照 | Ghauri 输出显示恢复历史布尔结果、MySQL 标签，却在数据库数量或输出长度处失败。 | [方法条目](../by-type/sql-injection.md) |
| 工具阶段计数与报告总数需说明分母 | AORT 的子域、JSON、重定向、XSS 计数与另一轮结果差异很大，Git/Secret 检查还有失败或跳过；思维导图节点和 Obsidian 词数也不能当证据数。 | [方法条目](../discovery/records-and-incremental.md) |
| 接管流水线要补服务生命周期与独立范围检查 | 子域发现→解析→HTTP 存活→takeover 模板只有候选筛选。 | [方法条目](../by-type/subdomain-takeover.md) |
| 重复报告的新增影响需有独立事实链 | 反射 XSS 被判重复后寻找新链，应说明输入、sink、受害条件与实际保护能力在哪一环新增，用自控身份提供最小证据和反例。 | [方法条目](../reporting.md) |
| JSON 消息调用需要双向绑定来源与命令能力 | 截图将新窗口、JSON 消息与 App.apiCall 连接。 | [方法条目](../by-type/websocket.md) |
| JSONP 编码和消息链不能跳过脚本消费者 | 保存代码中 callback 和双重编码字串只能说明构造方式。 | [方法条目](../by-type/xss.md) |
| 携带凭据的 fetch 需证明跨源响应是否可读 | 截图的 profile 请求使用 credentials:include；这不证明 cookie 一定随跨站发送或 CORS 允许读取。 | [方法条目](../by-type/cors.md) |
| 读取 token 与更新 profile 的状态改变分开证明 | 消息/JSONP/profile 链声称获取 csrf token 并更新 profile，应分别绑定 token 会话、请求动作、来源验证和最终自有账户状态。 | [方法条目](../by-type/csrf.md) |
| 跨子域 cookie 链依赖域属性和接管能力 | 保存的 Azure CNAME/NXDOMAIN、作者接管叙述和日志 Cookie 展示需分别归因。 | [方法条目](../by-type/subdomain-takeover.md) |
| 跨域收到 cookie 与服务器接受会话是两级证据 | AspNetCore.Cookie 的日志记录可能支持浏览器向特定子域发送 cookie，仍需区分属性、时点、账户和当前有效性。 | [方法条目](../by-type/authn-session.md) |
| 语法混淆要按 HTML、XML 与 JavaScript 消费者区分 | 保存 onbeforeinput、数值字符、iframe srcdoc、top/this 转换、XML 的 XHTML 命名空间与 new Function 变体。 | [方法条目](../by-type/xss.md) |
| OAuth 登录 CSRF 检查的是发起会话到回调的绑定 | 缺 state 或 PKCE 的帖子给出候选，应审查 authorization request、issuer/client/redirect、登录发起会话、返回 code/state 及 verifier 的关联。 | [方法条目](../by-type/oauth-oidc.md) |
| 管线参数反射只能支持 source 线索 | 历史 PHP URL、httpx、kxss、blind-XSS 替换管线分别负责候选与回显。 | [方法条目](../by-type/xss.md) |
| MySQL XML 函数报错与 XPath 注入类别分开 | 保存 extractvalue/Rand/USER 表达式可能利用 MySQL XML 函数产生 SQL 错误。 | [方法条目](../by-type/sql-injection.md) |
| 自定义 emoji 查询的未认证延时线索 | Rocket.Chat 摘要称 listEmojiCustom 存在 unauthenticated NoSQL 注入且至少一个自定义 emoji 才触发。 | [方法条目](../by-type/nosql-injection.md) |
| 搜索结果 Markdown 渲染受 CSP 与解析器配置约束 | SearchMessages 摘要指出 Markdown 标签进入搜索结果且当时需要关闭 CSP。 | [方法条目](../by-type/xss.md) |
| 权限检查晚于成员查找会产生存在性 oracle | muteUserInRoom 摘要指在 channel 权限检查前查用户名/成员，未加入者可能据响应差异推知成员。 | [方法条目](../by-type/idor-access-control.md) |
| 消息处理热循环应追踪成本与取消路径 | Rocket.Chat 消息处理摘要称 crafted message 引发 loop 和较高 CPU。 | [方法条目](../source-audit.md) |
| 消息迁移须同时校验原对象与目标房间 | updateMessage 摘要称修改 rid 可把已知私有消息 ID 移到公开房间。 | [方法条目](../by-type/idor-access-control.md) |
| 事件拼接变体仍依赖浏览器事件与原 sink | 归档以 onbeforeScriptexecute 和拆分字符串称绕 Cloudflare。 | [方法条目](../by-type/xss.md) |
| 允许与拦截表格不能证明所有 WAF 可绕 | 变体应在相同业务 sink、规则版本、会话及输入预算下比较 WAF 状态与下游行为。 | [方法条目](../by-type/waf-bypass.md) |
| 下载告警受浏览器版本和设置前提影响 | Brave Windows 保存帖称“询问下载保存位置”设置改变危险文件警告。 | [方法条目](../by-type/desktop-client.md) |
| HTTP 重置邮件需追踪令牌第一跳 | Mattermost 文字和邮件图称工作区使用 HTTP 密码重置链接，但图片按钮未显示实际 href。 | [方法条目](../by-type/authn-session.md) |
| 漏洞收购宣传与披露授权没有等价关系 | 保存材料包含购买未报告漏洞及联系入口，只能说明宣传。 | [方法条目](../scope-and-rules.md) |
| 代理配置和 URL 规范化需保留原输入 | 多个 Burp 实例、代理/UA 配置与按 // 切分的 URL 去重，应保存原始请求/URL、账号和各实例规则。 | [方法条目](../discovery/records-and-incremental.md) |
| Cookie 解析差异须绑定浏览器与服务端版本 | 保存文章图片展示 Chrome 的孤立代理项、Jetty/Undertow 的带引号 cookie 吞并后续字段、Undertow 引号末尾和 Zope 逗号分隔差异。 | [方法条目](../by-type/authn-session.md) |
| Cookie 混淆影响 CSRF 要有令牌消费者对照 | 服务端将后续 cookie 合并进 quoted 值或把逗号视为分隔，可能改变 token/session 读取。 | [方法条目](../by-type/csrf.md) |
| 重定向生成器需保留浏览器最终 origin | 反斜杠、全角点、userinfo、协议相对与 tab 字串只提供解析候选。 | [方法条目](../by-type/open-redirect.md) |
| NTLM 元数据和协议入口不等于中继或认证成功 | NTLMRecon JSON 示例列 NetBIOS、DNS、forest、computer 与 ADFS/windowsTransport、Autodiscover/OAB/EWS/Rpc 路径。 | [方法条目](../by-type/authn-session.md) |
| 云告警架构需保持扫描、存储和处置分工 | DomainProtect 图将 CloudWatch、账户列表、Step Functions、分账户扫描、DynamoDB 和 SNS 联系起来；保存各阶段输入、执行身份、范围、失败及告警去重/回执。 | [方法条目](../discovery/records-and-incremental.md) |
| 图片检查的 fetch 与内网端口判别分开 | 8x8 ChatApps 摘要给出 /api/v2/chats/image-check 的 JSON url，示例指向 loopback，说明图片验证接口可能消费 URL。 | [方法条目](../by-type/ssrf.md) |
| Django 调试屏的字段展示与有效访问分开 | 保存 META 调试页展示 PJANGO 开头的数据库变量、端口、HTTP_COOKIE 与 WSGI/Python 信息，其中值遮挡。 | [方法条目](../by-type/info-secrets.md) |
| 从静态文件与模型生成的域名要分别标记来源 | Indicator Intelligence 关联线索来自静态文件或日志，GPT 子域列表则是预测。 | [方法条目](../discovery/passive-and-services.md) |
| 模型流量分析需要最小输入和独立可证伪结果 | Burpgpt 类被动 HTTP 分析应说明选择了哪些已授权流量、模型实际接收内容及保密边界；对 token、cookie、个人信息先最小化/遮挡。 | [方法条目](../by-type/ai-application.md) |
| 管理注册路径变体需证明最终账户权限 | 保存正文 /admin/register 与截图 /admin/auth/register 不同，另图只显示尾斜杠后的 Strapi 初始化/注册页面。 | [方法条目](../by-type/authn-session.md) |
| 默认口令标签需要实际部署与保护动作证据 | 正文以 8080 端口及默认口令称客户数据暴露，截图只有 P2 标题。 | [方法条目](../by-type/authn-session.md) |
| 改角色 cookie 或本地响应仍需服务端权限对照 | isadmin/角色值或响应 false→true 改写可影响客户端展示，原图只含报告状态。 | [方法条目](../by-type/idor-access-control.md) |
| 上传默认目录和历史文件管理器参数不能直接等同任意写 | Wayback 的 CKEditor/Filemanager 参数可提示上传路径消费者。 | [方法条目](../by-type/file-upload.md) |
| 匿名 LDAP 要区分 RootDSE 与受限目录数据 | 保存标题称 LDAP Anonymous，图片终端细节不足。 | [方法条目](../by-type/authn-session.md) |
| 关联对象的修改权与展示效果独立验证 | LinkedIn 摘要分别涉及公司置顶、付费讨论组、课程问答 reply URN 删除和 newsletter 发布。 | [方法条目](../by-type/idor-access-control.md) |
| 业务访问资格和关系对象状态分别建模 | 付费课程的讨论组应区分链接发现、加入资格、成员关系与内容读取；newsletter 创建者与关联发布权也不同。 | [方法条目](../business-modeling.md) |
| 参数爬取失败保留 shell 输入单位与空结果 | 原帖 shell 循环含 python http://paramspider.py、未限定输入单位，截图用含 scheme 的字符串作 Domain/输出文件名并得到 0 unique URLs。 | [方法条目](../discovery/records-and-incremental.md) |
| 邮件模板 HTML 注入与浏览器脚本执行分开 | 姓名/邮箱等字段进入通知邮件可能产生 HTML 注入。 | [方法条目](../by-type/xss.md) |
| 桌面二进制里的应用凭据需识别消费者 | 标题声称 APK，但保存详情明确 GlassWire EXE/Setup 1.1.26.0 与应用 ID、secret、OAuth application token。 | [方法条目](../by-type/info-secrets.md) |
| 客户端凭据来源按实际平台与版本追踪 | 静态检查二进制/配置应绑定实际 EXE 名称、来源、hash、版本及字段到 API 的消费者。 | [方法条目](../by-type/desktop-client.md) |
| 导出接口要检查对象和角色而非文件名猜测 | 保存 WordPress doaction/predirect 导出路径与 timestamp CSV 声称暴露个人资料。 | [方法条目](../by-type/idor-access-control.md) |
| CSV 导出内容以最小字段样本和归属定影响 | 姓名、邮箱、电话、角色和组织是待核验字段类别。 | [方法条目](../by-type/info-secrets.md) |
| 域名 available 标签不证明注册资格或接管 | TLDHunt 将不同后缀标作 available/taken，应记录查询源、时间、返回语义、后缀准入条件和真实注册局状态。 | [方法条目](../discovery/passive-and-services.md) |
| 复查报告与沟通记录以技术事实为主 | 复查修复应保持原始入口、账号、对象和动作一致，说明当前范围、预期拒绝结果及实际差异；resolved/default credentials 的状态没有登录或保护操作证据。 | [方法条目](../reporting.md) |
| 并购资产关系不能自动扩展原项目范围 | 并购后域名、历史 Wayback 路径及 Google 结果需要重新核对当次项目资产、经营主体和允许注册/操作规则。 | [方法条目](../scope-and-rules.md) |
| 注册审批守卫应跨登录与重置流程保持一致 | 管理注册或需审批用户的重置密码可能绕开初始登录流程，需记录注册申请、审批状态、token 会话绑定、回调和最终角色。 | [方法条目](../by-type/authn-session.md) |
| Header SQL 命中要把条件、时序和工具归因拆开 | X-Forwarded-For 可由用户输入，但需定位其日志/查询消费者。 | [方法条目](../by-type/sql-injection.md) |
| 敏感 GET 与缺 Origin 需按浏览器发送规则验证 | img 导航请求可能携带 Referer 而不带 Origin；Origin 缺失/null/同源/跨源需要分别有服务端策略。 | [方法条目](../by-type/csrf.md) |
| 鉴权字符串前缀须与路由解析语义对齐 | 保存 Express 代码在 req.url.startsWith(/api) 时验 token，再挂载 /api 路由，存在原 URL 字符串判断与路由消费不一致的审查点。 | [方法条目](../source-audit.md) |
| Elasticsearch 服务线索不等同无认证数据权限 | 9200、Shodan org 与浏览器扩展可提示候选服务，但 org 字段和公开端口不提供授权。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 口令尝试输出不能替代最小账号授权验证 | 图片展示 WPScan 对一用户 XMLRPC 尝试与成功标记，也提示未配置 API token。 | [方法条目](../by-type/authn-session.md) |
| 推荐 bundle 引入的 XSS 前提按具体应用记录 | Nextcloud 截图摘要称推荐 Office bundle 安装 richdocumentscode 后出现 RXSS/CSP bypass，并列历史 CVE-2023-31145。 | [方法条目](../by-type/xss.md) |
| 部署遗留 Git 元数据与历史配置暴露分级 | .git 暴露和 private/classes/Config.php 等仓库树提示部署包含本地版本控制元数据；导出发布包不应等同保留历史工作副本。 | [方法条目](../by-type/info-secrets.md) |
| 目录权限关系图不等于凭据改写已成功 | ShadowSpray/GenericWrite/GenericAll 线索及 BloodHound 多条 GenericAll 边说明需检查主体、对象 DACL、继承、适用权限与既有身份。 | [方法条目](../source-audit.md) |
| 合法删除请求与跨站删除能力分开 | 删账户图需页面输入 YES，捕获 POST /users/deleteAccount 包含 Cookie、X-Requested-With 和同源 Origin/Referer，正文下半段未保存。 | [方法条目](../by-type/csrf.md) |
| 退出导航的脚本方案要逐层核验历史前提 | ServiceNow logout_redirect.do/sysparm_url 示例包含编码反斜杠与脚本方案，摘要称未认证用户点击可执行并列 SanDiego SP6 之前/CVE-2022-38463。 | [方法条目](../by-type/xss.md) |
| SpellCheck XML 入口仍需实体解析与响应证据 | RapidSpellHelpFile.aspx 保存请求需先登录带 cookie、Content-Type:text/xml，裁切处只到 XML 声明。 | [方法条目](../by-type/xxe.md) |

| 报表导出路径与内容参数要分开约束 | rdExportFilename 与 rdReportName 摘要分别声称控制文件目录/类型和内容，复现需登录、运行报表、截获 Export to Excel 请求。 | [方法条目](../by-type/file-upload.md) |
| 活动新闻稿范围不能代替当前测试规则 | 报告明确承认当前范围之外，引用过去新闻稿解释动机。 | [方法条目](../scope-and-rules.md) |
| LDAP NULL bind 的可见范围要逐项界定 | 保存摘要给出 ldap* and not brute 脚本筛选，但未给真实查询或属性响应。 | [方法条目](../by-type/authn-session.md) |
| AEM selector JSON 输出需验证实际资源权限 | 追加 /.1.json 被描述为模板/文件/用户名披露，原图未保存具体 JSON。 | [方法条目](../by-type/info-secrets.md) |
| 备份文件与文件清单泄露按最小内容证据提炼 | wp-config.php_、.sql/.sqlite 字典、test.sql 与 files.md5→/db/sqlsrv/full.sql 提示静态备份或路径索引。 | [方法条目](../by-type/info-secrets.md) |
| 管理默认认证线索需落到具体服务和保护能力 | Kinetic /kinetic/app/ 与 ZooKeeper 2181 的默认无认证/弱凭据说法需绑定实际协议、版本、配置与已授权测试账户。 | [方法条目](../by-type/authn-session.md) |
| Bing 创意模式域名清单不是权属发现 | Prompt 要求列公司所有域名，图片给出多个域名及跳转解释，却没有 DNS/权属/跳转来源。 | [方法条目](../by-type/ai-application.md) |
| 日期解析正则的回溯成本需有长度与失败条件 | Ruby Time.rfc2822/rfc822 摘要展示多个空白量词及 recheck 结果边缘。 | [方法条目](../source-audit.md) |
| 多源子域聚合保留输入单位、时间和失败 | amass 原文输入带 scheme，写 1.txt 又读 results.txt；crt.sh、API、SecurityTrails、Shodan 与 subfinder/httpx 也混合域名和网页候选。 | [方法条目](../discovery/records-and-incremental.md) |
| 文件名和元数据回显必须到达实际渲染 sink | 图片文件名、header、cookie 与 metadata 是不同 source，需绑定原字节、解码、存储与最终 HTML/JS 消费者。 | [方法条目](../by-type/xss.md) |
| Git 检测和源码调试入口的状态与内容分开 | DotGit 界面数、dirsearch、PHP source claim 与 Spring Boot favicon/env/heapdump 管线只是候选。 | [方法条目](../by-type/info-secrets.md) |
| 零抵押参数与跨链 ID 转型按状态语义审查 | Morpho LTV=0 AToken 与 Aave 的 HF/borrowing power 差异、CBridgeFacet destinationChainId 转 uint64 是保存摘要的两个审查点。 | [方法条目](../by-type/smart-contract.md) |
| 速率限制以操作、主体和时间窗为单位 | Additional emails、投稿、登录和删账户当前密码确认需要不同 limiter key 与副作用预算。 | [方法条目](../by-type/business-logic.md) |
| 生产调试信息按可见字段和身份定影响 | Symfony app_dev.php/_profiler 与 phpinfo 路径提示开发工具暴露。 | [方法条目](../by-type/info-secrets.md) |
| 营销服务 XSS 公告保留用户动作与修复范围 | Cisco 保存公告称输入验证不足、用户点击恶意链接、managed service 已更新。 | [方法条目](../by-type/xss.md) |
| 前端邮箱拒绝与后台盲渲染是不同验证链 | 正文称先合法邮箱提交、拦截改参数、账号创建后稍后 blind trigger；图片只见 Email Address invalid 和报告标题。 | [方法条目](../by-type/xss.md) |
| HTTP 请求字段注释不要混淆来源与实际协商 | HTTP/1.1 图中的 Host 是 authority 主机信息，图把其值标作 URI 不准确；路径与请求目标、方法和版本分别记录。 | [方法条目](../discovery/web-and-api.md) |
| 运行时参数 hook 只覆盖实际执行路径 | 复用已核验相同 SHA 的 Eval Villain 图片说明 URLSearchParams.get 的参数名和 stack 可帮助定位动态读取。 | [方法条目](../by-type/xss.md) |
| 低影响 ID 向敏感动作传递仍须逐环授权 | 正文提出由 org_id/user_id 线索转向邮件变更等敏感动作，图片只有组织接管标题。 | [方法条目](../by-type/idor-access-control.md) |
| 技能测试隐私需同时覆盖失败与隐藏徽章状态 | LinkedIn 摘要给出 AssessmentAttemptReports URN 查询并区分失败、通过但 badge 私密。 | [方法条目](../by-type/idor-access-control.md) |
| 隐藏系统标签被工作流消费时仍需权限检查 | restricted/invisible tags 的标题指向标签查找与 workflow 设置两层权限。 | [方法条目](../by-type/idor-access-control.md) |
| DNS 超时信号分支与线程安全标识分开 | curl siglongjmp 摘要要求特定缺线程支持构建的 USE_ALARM_TIMEOUT 分支、双线程 DNS 解析、信号超时及寄存器上下文冲突。 | [方法条目](../source-audit.md) |
| 代码分包索引发现路由后仍需具体对象授权 | Webpack runtime 的 chunk ID→hash 路径可提示尚未加载资源，单 chunk 图只含模块依赖和按钮代码。 | [方法条目](../discovery/web-and-api.md) |
| 恢复 SQL 会话与不常见数据库须保留归因边界 | sqlmap --level 5/--all 图片显示存储会话、error-based 函数、遮挡的 DBMS、retrieved 与无法取 entries 的警告。 | [方法条目](../by-type/sql-injection.md) |
| 存储容器公开层级与 CDN 响应相似性分别验证 | Azure 摘要称 container public 而非 private 导致 blob 可读；S3 帖子以 HTTP/HTTPS 响应相同猜 bucket 名。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 日志表达式嵌套的资源成本不能由 Waiting 判定 | Log4j 2.16 DoS 帖子有嵌套表达式 User-Agent 请求和空响应/Waiting，缺 logger 版本、栈、CPU 与恢复对照。 | [方法条目](../source-audit.md) |
| reference URL 的读取主体与协议消费者需定位 | 子域/历史 URL/Arjun 管线及 file 方案声称 SSRF→LFI；先定位 reference 在服务端 fetch、浏览器读取或文件 API 哪一层消费，记录解码、协议白名单、重定向与自控回调。 | [方法条目](../by-type/ssrf.md) |
| file 方案字符串不等于文件系统越界读取 | 追踪原参数到最终 canonical 路径、允许根、符号链接及读回方式，用自有无害文件与拒绝路径作比较。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Shell 引号和展开清单依赖具体解释器 | 保存 quote 拼接、glob、变量替换、IFS、base64/rev 与 brace 变体，需绑定用户输入到进程参数/具体 shell、工作目录、变量及文件匹配条件。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 协作平台公开内容仍须区分授权与秘密用途 | Trello、Google Groups 和代码关键词搜索可提供公开可见候选。 | [方法条目](../by-type/info-secrets.md) |
| TLS pass-through 的匹配范围与可见流量分开 | 归档列 Burp TLS Pass Through 表达式，其中通配/正则和括号拼写不一致。 | [方法条目](../discovery/records-and-incremental.md) |
| 接受、奖励、功能缺陷和修复回复按事实记录 | 邮件 HTML 注入在不同项目是否 eligible、内容政策链接 404、Coop 相信已修复回复说明不同沟通状态。 | [方法条目](../reporting.md) |
| 重置链接污染需要最小自控交付与令牌链 | Host header 注入标题询问是否应证明影响；应分别确认服务器信任哪个 authority、生成的绝对链接、邮件原始 href 和自有 token 消费者。 | [方法条目](../by-type/host-header.md) |
| TLS 主机匹配必须区分证书模式与待验证名称 | curl 历史报告指 hostmatch 对 pattern 检查 xn--，作者指出应看 hostname；证书 CN/SAN 模式和待验主机是不同输入。 | [方法条目](../source-audit.md) |
| HTTP handle 复用的请求方法需从 wire 验证 | curl POST-after-PUT 摘要指出旧修复仅 CURLOPT_POST、而 POSTFIELDS 也能设 POST。 | [方法条目](../source-audit.md) |
| 导出接口要对未提交草稿执行状态和角色过滤 | HackerOne 摘要给出草稿不发送→export_reports→邮件 CSV 含标题/severity/weakness，而 inbox 不可见。 | [方法条目](../by-type/idor-access-control.md) |
| 报告草稿生命周期必须跨导出路径保持隐私规则 | 将 draft、submitted、disclosed 及预期接收方列为业务状态，检查异步导出在查询/生成/下载每阶段是否保持同一状态筛选与授权。 | [方法条目](../business-modeling.md) |
| LaTeX 文件和命令能力受编译沙箱与 shell 设置限制 | input/include/verbatiminput 可能消费编译环境文件，write18/pipe 例子依赖引擎与 shell-escape/许可配置，PDF 链接还依赖 viewer 协议策略。 | [方法条目](../by-type/document-rendering.md) |
| PDF 中脚本方案链接与网页 XSS 不是同一 sink | LaTeX url/href 脚本方案需确认最终生成 PDF/HTML 哪种输出、链接注释内容、viewer 协议处理和用户点击。 | [方法条目](../by-type/xss.md) |
| 租户、ASN 和 registrant 关联不授扫描范围 | PingCastle 说明由 OpenID/CT 构建 tenant 关联，NSE targets-asn 返回含重叠 CIDR，Reverse WHOIS/BGPView 提供登记或路由线索。 | [方法条目](../discovery/passive-and-services.md) |
| 切换会话和同邮箱注册不自动证明账号接管 | Reddit chat 摘要改 reddit-session 后看另一测试账号，OAuth 摘要从 Google 登录退出后同邮箱创建本地新账号。 | [方法条目](../by-type/authn-session.md) |
| 依赖 CVE 和客服上传标题缺少真实渲染链 | 保存 jQuery CVE 风格 option/style 载荷与 Zendesk 上传摘要，却无输入入口、版本/配置、文件名/类型到 sink、浏览器执行。 | [方法条目](../by-type/xss.md) |
| 登录后重定向和错误方案 fallback 按消费者分开 | Reddit dest 脚本方案摘要要求登录/SSO 后执行；另一图用 ws/wss/resource 使 302 不按通常方式跟随，并给未转义 href 标签。 | [方法条目](../by-type/xss.md) |
| 同源表单 token 与跨站状态变更证据分开 | 截图 profile 请求携 __RequestVerificationToken、cookie、same-origin fetch metadata，响应 302/Profile/Confirm 和 Set-Cookie。 | [方法条目](../by-type/csrf.md) |
| 错误页和 header 回显仍可能携带私有缓存内容 | 404 后缀诱发缓存与 wotif info.php 缓存最后请求 headers 摘要，需要区分源应用动态内容、边缘 key、status、Vary、身份/cookie 与命中来源。 | [方法条目](../by-type/cache-deception.md) |
| 缓存 header 中的 cookie 暴露与接受身份分开 | wotif 摘要声称最后来访者 HTTP headers 可被下一人读取，底部只见 TEMP 等字段，未保存 Cookie 实际回包。 | [方法条目](../by-type/info-secrets.md) |
| HTML 与 CSS 注入不能从样式允许推脚本执行 | wotif 作者称 style/form 可注入但当时无法 XSS。 | [方法条目](../by-type/xss.md) |
| 世界可写日志须追踪本地权限和后续消费者 | Airflow 2.5.1 摘要称日志 chmod 666、低权限本地主体能读改，列历史 before 2.6.0。 | [方法条目](../source-audit.md) |
| 特权恢复接口必须独立校验主体与凭据生命周期 | 复用已核验相同 SHA 的保存图叙述 /api/u/resetPwd 与 /api/su/resetPwd、用户名及可预测后缀密码。 | [方法条目](../by-type/authn-session.md) |
| CDN 脚本命名与 HTML 引用只拓展有限候选 | 复用已核验 CDN 命名图及当前 Shodan http.html 卡片可提示子域标签、构建版本和静态资源引用。 | [方法条目](../discovery/client-and-cloud.md) |
| 购买资格与 Helm 对象权限要在服务端分别校验 | 叙述未购买服务却 helmCreate success:true、listHelm 看见不同创建者，随后配置接口返回云键。 | [方法条目](../by-type/idor-access-control.md) |
| 应用角色到云密钥再到云权限的链逐步验证 | Helm 叙述把配置接口回 access keys 与公司容器/私有数据串联，原图没有实际键或云响应，配置路径字体不确定不补字节。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 认证模式枚举必须拒绝未知值且延后发会话 | login_method Normal→未知值的叙述先出现 success 却未登录，reload 后称 cookie 能用于保护 API。 | [方法条目](../by-type/authn-session.md) |
| 升级失败后代理不得只凭请求头切换隧道 | fake WebSocket 图示请求 version 1337、后端 426、前端未核对响应。 | [方法条目](../by-type/request-smuggling.md) |
| 重定向 dork 命名只提示输入候选 | go/return/redirect/dest/continue 路径或参数名搜索需保存索引日期、实际参数和当前范围。 | [方法条目](../by-type/open-redirect.md) |
| 残缺指针事件载荷不能静默修成执行证明 | Imperva 帖子中的引号、全角符号与 lavas/cript 片段有歧义，需保存原字符、HTTP 字节及反射上下文。 | [方法条目](../by-type/xss.md) |
| 声称 WAF bypass 的比较必须保持同一业务请求 | 绑定规则版本、身份、正常与变体字节、拦截响应和业务 sink，区分 WAF 放行与浏览器执行。 | [方法条目](../by-type/waf-bypass.md) |
| 社区内容字段用业务消费者限定测试 | 文章、问题、评论和“不遗漏输入”可用于列 source 清单；记录谁能写、谁会读、是否保存、对象归属与每个 sink。 | [方法条目](../targeted-fuzzing.md) |
| 跨站 WebSocket 劫持不自动获得任意漏洞能力 | 先确认握手是否校验 Origin、cookie/会话来源、消息 schema 与服务器对每个命令的权限，用本地自控两个 origin 比较。 | [方法条目](../by-type/websocket.md) |
| 403 变体以最终资源身份和权限判定 | X-Original-URL、rewrite/trust-IP 头、编码点斜杠、大小写、分号和方法变体要追踪到每层代理及 canonical 路由。 | [方法条目](../by-type/idor-access-control.md) |
| 第三方投票弹窗到帖子存储渲染须绑定 origin | Crowdsignal poll answer→Website Popup→WordPress 新帖保存→打开页面的摘要说明跨产品内容链。 | [方法条目](../by-type/xss.md) |
| 请求转换工具保留明文、密文和原 wire 身份 | PyCript v0.2 宣称 Python/Java、header 和复杂 JSON/响应加解密能力，但未给实际算法。 | [方法条目](../discovery/records-and-incremental.md) |
| 特殊 workspace 的开户资格不能只由客户端请求决定 | GovSlack 摘要给新用户创建 workspace、复制 signup.createTeam multipart fetch。 | [方法条目](../by-type/authn-session.md) |
| PDF 水印搜索与敏感内容必须分别判断 | site/ext:pdf/CamScanner 搜索可提示公开扫描文档，示例只有数学作业与水印。 | [方法条目](../discovery/passive-and-services.md) |
| APK 关联以二进制 hash 区分同包名版本 | Koodous 输出同 com.brata.rat/1.0 名称却有多个 SHA/大小。 | [方法条目](../by-type/mobile-android.md) |
| 注册角色数组应由服务端按开户资格赋值 | 正文 roles:[10]→[100] 声称管理员。 | [方法条目](../by-type/idor-access-control.md) |
| 邮箱域约束与 OTP 成功响应不可只在客户端实施 | 员工邮箱注册条件和拦截改成个人邮箱、复制 OTP 成功响应的叙述需分开验证。 | [方法条目](../by-type/authn-session.md) |
| 详情路径移除 ID 后的列表必须重新检查权限 | /api/utilisateurs/{myID}→collection 的正文声称全员工 PII/密码。 | [方法条目](../by-type/idor-access-control.md) |
| SAML 错误输入的 HTML 输出与认证协议分开 | Cisco ASA /+CSCOE+/saml/sp/acs?tgname=a POST SAMLResponse 保存示例用标签片段声称 CVE-2020-3580。 | [方法条目](../by-type/xss.md) |
| SAML 端点反射不能推断断言校验绕过 | 协议入口收到非正常 SAMLResponse 后可能走错误页 HTML sink，应单独记录 XSS 输出验证与 XML/assertion 的签名、issuer/audience、时效和会话绑定。 | [方法条目](../by-type/saml-sso.md) |
| 密码变化后的旧会话按类型和撤销策略对照 | Failure to invalidate session after reset/change 图片只有标题，正文 P4 是个人判断。 | [方法条目](../by-type/authn-session.md) |
| 花括号模板输出与存储 XSS 分类需有消费者证据 | 标题称 SSTI→Stored XSS，外链标题却是 reflected。 | [方法条目](../by-type/ssti.md) |
| URN decoration 要同时限制可展开字段和目标资源 | LinkedIn 摘要指任意文本字段放 emailAddress URN 后 decoration 展开，需分别验证字段 allowlist、资源类型、对象归属与展开身份。 | [方法条目](../by-type/idor-access-control.md) |
| 登录时序图记录身份、challenge 与令牌发放时点 | 自定义 flow 图 app→auth 重定向、密码、OTP trigger/validate→session 可整理请求链。 | [方法条目](../discovery/records-and-incremental.md) |
| API key 用途和验证动作先于有效性猜测 | KeyHacks 资源描述有效性检查，需确认字段是公开客户端标识还是服务凭据、所属项目与允许的验证动作。 | [方法条目](../by-type/info-secrets.md) |
| PIN 数组形态必须在解析和认证函数保持类型约束 | POS 叙述把 loginpins scalar 变为数组，示例只有单个元素，无验证代码和认证响应。 | [方法条目](../by-type/authn-session.md) |
| 缓存 purge 的受理回执不等于真实失效 | 图片给 PURGE curl.se 与 status:ok/id 的叙述，但步骤多处占位。 | [方法条目](../by-type/cache-deception.md) |

| 自身账号删除的确认策略与越权影响要区分 | 登录后删除自身账户而未再次输入密码，只能作为敏感动作确认策略线索。 | [方法条目](../reporting.md) |
| Signer 的循环末项与已有模块边界须分别审查 | SwapSigner 最后 owner 无效与 HatsSignerGate 在已有超过五个模块的 Safe 上异常，是两个历史边界线索。 | [方法条目](../by-type/smart-contract.md) |
| 多端点与多秘密按根因和权限消费者组织报告 | 多个子域/端点复现同一根因，应保留独立资产与权限证据并按项目规则归并；多个 secret 则分别确认服务、权属、有效时点和权限消费者。 | [方法条目](../reporting.md) |
| 报告可读性与最小 HTTP 复现须同时保存 | 代码块、清楚截图和尊重的措辞帮助复核；删无关头和 cookie 前应保存脱敏原请求。 | [方法条目](../reporting.md) |
| 公开报告目录作为检索索引而非机制全文 | Google 公开报告表的题目、作者、计划和更新时间可以记录检索线索与历史披露时点。 | [方法条目](../discovery/records-and-incremental.md) |
| 多组件链逐环证明来源、消费者和浏览器边界 | 正文给出 postMessage、JSONP、WAF、DOM XSS 与 permissive CORS 到一点击 CSRF 的链名。 | [方法条目](../by-type/xss.md) |
| 资产映射与历史计划标签不能扩展测试许可 | orgs-data 的计划到 GitHub 组织映射、披露目录 safe-harbor/bounty 徽章和 Mobile VRP 首方 Android 公告可作候选来源。 | [方法条目](../scope-and-rules.md) |
| HTML 链接注入与脚本执行使用不同结论 | 输入被输出为可点击的外域锚点说明 HTML 内容控制线索。 | [方法条目](../by-type/xss.md) |
| 外域锚点点击不等同服务器开放重定向 | HTML 中外域链接依赖用户点击，需与服务器 Location、自动客户端导航和协议相对 URL 分开记录。 | [方法条目](../by-type/open-redirect.md) |
| 归档邮箱与历史凭据按最小字段证据判断 | Wayback URL 经 grep 匹配 gmail 只是字符串筛选，不能证明私人邮箱或当前泄露；归档路径出现用户名/密码与后续管理员访问也需分别绑定来源、时点、身份和权限。 | [方法条目](../by-type/info-secrets.md) |
| 控制台默认身份与管理权限分别核验 | 默认凭据和 MDM 全权限管理面板的正文/标题提供认证检查方向。 | [方法条目](../by-type/authn-session.md) |
| Rails Accept 模板解析路径与最终文件边界分开 | 保存帖以 Rails render file 和 Accept 头路径片段描述历史 CVE-2019-5418。 | [方法条目](../by-type/lfi-path-traversal.md) |
| SSH 指纹错误日志不能引用已释放缓冲区 | curl 摘要指出 fingerprint_b64 在 free 之后作为失败日志参数使用。 | [方法条目](../source-audit.md) |
| 编码路径穿越的响应需绑定同一资源和身份 | 保存请求在多级路径及 uploads 下使用百分号编码点段，响应可见 Linux 账户行。 | [方法条目](../by-type/lfi-path-traversal.md) |
| URN 展开必须约束字段类型和目标对象权限 | Voyager decoration 示例把 emailAddress URN 放在自有 profile 文本字段，再查询展开并在 included 返回邮件资源。 | [方法条目](../by-type/idor-access-control.md) |
| 盲渲染标记要连接到具体存储字段和消费者 | 独立 ID 可关联延迟 blind trigger；Android 设备名也可能由同步/管理后台渲染。 | [方法条目](../by-type/xss.md) |
| 角色字段由服务端资格规则赋值 | GitHub 认证入口增加 admin/org_admin 与个人资料 User 改 Admin，是角色绑定审查候选。 | [方法条目](../by-type/idor-access-control.md) |
| 邮件图片和托管租户域作为关联线索 | 订阅邮件中的 S3 图片主机及 force.com/secure.force.com 租户名，可用于记录客户端资源与业务关联。 | [方法条目](../discovery/client-and-cloud.md) |
| 查询字典仓库的文件名不能代替查询内容审查 | 保存目录包含 admin、token、SQL、carding 等混合名称，只能确认当时仓库的条目元数据。 | [方法条目](../source-audit.md) |
| 域名管线保留合法字符与每阶段输入单位 | 从子域提取标签做词表，应保留原 FQDN、来源和去重映射；域名中连字符合法，不能为清理空白一并删除。 | [方法条目](../discovery/records-and-incremental.md) |
| AI 辅助侦察需保护输入并独立核对输出 | ReconAIzer 的 GPT 工具介绍只是能力声明。 | [方法条目](../by-type/ai-application.md) |
| 客户端请求日志不能代替服务端取址证明 | CDX/gf/qsreplace 管线将 URL 参数换成回环域后用 curl 提取标题/状态；另一脚本用 -L/-I 和 grep 回调字符串。 | [方法条目](../by-type/ssrf.md) |
| 魔术字节伪装与上传后解释执行要逐段验证 | 保存卡片把图片头签名与 PHP 命令解释代码组合为文件。 | [方法条目](../by-type/file-upload.md) |
| 邮箱输入引发的网络活动先按协议区分 | 邮箱域、回环地址和回调字串可能被邮件投递、DNS、验证服务或 HTTP 消费。 | [方法条目](../by-type/ssrf.md) |
| 邮件字段换行需验证解码后真正的头边界 | 正文同时提出邮箱参数和 HTTP/SMTP 头注入。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 内容协商与 JSON 错误反馈按实际响应分类 | Accept JSON/JavaScript 偏好可改变表示，JSON 参数故意不合 schema 可能反馈允许字段。 | [方法条目](../discovery/web-and-api.md) |
| 共享 Okta 应用标识仍需校验各信任边界 | 两个域名使用同一 Okta app ID 只能提示相关登录配置。 | [方法条目](../by-type/oauth-oidc.md) |
| 递归路径探索和规范化变体需要明确终止条件 | 目录递归建议与 pathbuster 的 normalization 描述可作候选策略。 | [方法条目](../targeted-fuzzing.md) |
| 动态载荷来源与响应基线先于自动化结论 | Supp-truder 描述远程载荷、regex、基线、tamper、头与 POST 处理。 | [方法条目](../targeted-fuzzing.md) |
| Git 的命令选项消费也是参数注入边界 | release-sdk 的 LSRemoteExec 摘要指出用户输入可被当作 Git upload-pack 等选项，截图有局部 Go 调用示例。 | [方法条目](../by-type/cmd-injection-rce.md) |
| IAM 到 Kubernetes 身份映射须绑定签名内容 | aws-iam-authenticator 通过签名 STS GetCallerIdentity 映射 K8s username/groups。 | [方法条目](../cloud/container-k8s-security.md) |
| 技术证据、重复归并和最终等级分别记录 | 有效报告被定 Low、先 Triaged 后 Duplicate，以及题目 HIGH 与系统 Medium 不同，都显示技术有效性、归并、严重性和奖励是不同状态。 | [方法条目](../reporting.md) |
| 侦察配置升级保留用户覆盖和新默认差异 | reconFTW 配置更新建议备份旧配置再比对新配置。 | [方法条目](../discovery/records-and-incremental.md) |
| 一次性登录链接需在服务端原子消费 | Magic link reused 的标题可指导检查账号、token 摘要、用途、有效期、已消费状态与会话发放。 | [方法条目](../by-type/authn-session.md) |
| OTP 客户端响应变化不能代替验证因素 | 拦截 OTP 响应改变注册界面，只能说明客户端信任候选。 | [方法条目](../by-type/authn-session.md) |
| 增量主机与漏洞通知统计采用不同单位 | 保存发现仪表板与邮件分别展示新主机数量和新 XSS 通知。 | [方法条目](../discovery/records-and-incremental.md) |
| 自动化 XSS 结果必须回到真实上下文 | 扫描器生成的反射 URL、autofocus/focus handler 说明只是候选；需保留单次请求、原始反射、DOM 解析、事件触发、origin 与 CSP，再以安全编码和无事件对照。 | [方法条目](../by-type/xss.md) |
| 备份中 AWS 字段与云权限使用分层证据 | 正文声称 backup_1 中 AWS key 能上传/下载。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Argo CD 错误差异只能证明受限应用存在性线索 | 保存 CVE-2022-41354 摘要说明已认证但无权限用户，由 not found 与 unauthorized 判别应用名；为了 RBAC 的 project/namespace 信息先 fetch 应用。 | [方法条目](../by-type/idor-access-control.md) |
| 历史源站 IP 需绑定当前 Host 与 SNI | DNS 历史可发现候选源站地址，但必须核对时间、归属、当前 Host/SNI、服务实例和范围。 | [方法条目](../discovery/passive-and-services.md) |
| 管理员审批状态必须由登录消费者复核 | 审批前开发者账户登录的标题指向待批准、拒绝、已批准状态到会话发放的边界。 | [方法条目](../by-type/authn-session.md) |
| 双重提交值相等还需确认浏览器可构造请求 | 正文称 token 和 cookie 都设为1，保存图仅有 X-Csrf-Token:1、JSON、自定义头及 200/success。 | [方法条目](../by-type/csrf.md) |
| 客户端模板求值与服务器模板求值分别定位 | CSTI 介绍指用户输入被前端动态模板消费。 | [方法条目](../by-type/ssti.md) |
| 选择安装工具仍需确认依赖和实际动作 | PDTM 的指定工具列表与私有 bin 位置可整理工具管理方式。 | [方法条目](../source-audit.md) |
| JSONP 回调与跨域读取使用不同浏览器规则 | Param Miner 找到 callback 参数后，需确认响应是否真以脚本方式消费、callback 控制、实际数据、凭据和 Content-Type/CSP；脚本加载与 CORS fetch 响应读取不同。 | [方法条目](../by-type/cors.md) |
| SSO 清单落到协议、身份与会话不变量 | 20项图涵盖认证发放/校验、token 修改/过期/吊销、CSRF、角色授权、会话固定、单点登出、SAML、协议互通、错误、IdP/SP、MFA、传输、身份映射、超时、头和扫描。 | [方法条目](../by-type/oauth-oidc.md) |
| 构建目录权限与容器内 root 的影响分别界定 | Cloudflare Pages v2 摘要称可替换两项构建可执行文件取得构建容器 root；目录却仅描述 user-readable，必须另证写权限或可替换父路径。 | [方法条目](../cloud/container-k8s-security.md) |
| 前端格式化与匹配替换作为受控观察工具 | 断点、格式化和 Burp match/replace 可帮助定位 JavaScript 输入与运行栈。 | [方法条目](../source-audit.md) |
| 通过代理导入 URL 与浏览器行为分别记账 | 保存管线以10并发 curl 经本地8080代理导入历史 URL，并丢弃 stdout；代理仍可能保留请求/响应。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史错误页 XSS 需确认具体版本和输出分支 | 正文声称 cPanel CVE-2023-29489 能利用403页。 | [方法条目](../by-type/xss.md) |
| file URL 处理与边缘规则命中是两层边界 | PDF status_url 示例以 file scheme 读取本地资源：一图敏感路径得到 Akamai403，另三图显示调度、网络表及配置内容。 | [方法条目](../by-type/ssrf.md) |
| XSS 标签以持久化和真实浏览器 sink 划分 | 保存图片列 reflected、stored、DOM-based 三类。 | [方法条目](../by-type/xss.md) |
| 同步 DNS 超时的全局跳转缓冲区需并发隔离 | curl CVE-2023-28320 摘要要求同步 resolver 构建，用 alarm/siglongjmp 超时，全局缓冲区无 mutex 时多线程可能崩溃。 | [方法条目](../source-audit.md) |
| 模板标记命中保留单次 URL 和求值对照 | qsreplace 放入9*9再并行 curl/grep ssti81，仅给出合并输出标记。 | [方法条目](../by-type/ssti.md) |
| API 对象授权需绑定文档操作与最终资源 | API 文档能帮助列 endpoint、对象 ID、动作和角色，但文档列出参数不授访问其它对象。 | [方法条目](../by-type/idor-access-control.md) |
| 状态方法与资源加载路径按真实浏览器请求核验 | POST改GET、avatar/img加载动作URL和 SameSite=Lax 都需要实际方法、cookies、Origin/Fetch metadata 和最终状态。 | [方法条目](../by-type/csrf.md) |
| 限流验证不能以更换来源默认扩大授权 | Tor 绕过标题只有验证方向，没有已保存机制全文。 | [方法条目](../scope-and-rules.md) |
| AEM 候选路径先核产品和各路由权限 | content/dam 文档查询与 Sling/AEM 管理、CRX、JCR、配置、query、replication 和 content selector 路径属于候选线索。 | [方法条目](../discovery/web-and-api.md) |
| 被动 DNS 保留观测时间和记录类型 | 保存界面列 record type、query/answer、first/last seen、次数及 TTL。 | [方法条目](../discovery/passive-and-services.md) |
| 备份文件候选与下载体积不能代替内容证明 | 域名/旧文件名构造 tar/zip/bkp 是候选策略，原帖的逗号字符不能静默当成域名点号。 | [方法条目](../by-type/info-secrets.md) |
| SQLi 正则数量与真实数据库求值分开 | SQLiDetector 的14载荷/152正则是工具规则数量，不是14个或152个已验证 SQLi。 | [方法条目](../by-type/sql-injection.md) |
| 模板收集完成需记录失败、去重和实际版本 | AllForOne 保存终端显示118仓库进度完成、99160文件复制，同时三项 clone 失败。 | [方法条目](../source-audit.md) |
| 归档 URL 验活脚本原字符与真实失败须保留 | 正文的引号/选项和输出写法存在歧义，不能静默修补再称原脚本验证成功。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史查询参数筛选只是重定向候选 | 保存管线从 subfinder、httprobe、waybackurls 到去重/query筛选，再指定外链 Nuclei 模板。 | [方法条目](../by-type/open-redirect.md) |
| 邮箱或图片回调应辨明 HTML 与 JavaScript 消费 | 引号邮箱/标签和脚本被过滤后换图片源，可帮助列解析与输出检查点。 | [方法条目](../by-type/xss.md) |
| TLS 与 nginx 搜索不能确认 Django 调试模式 | 保存图只有 Shodan 的 TLS域名/nginx 产品筛选，正文却称找 Django debug。 | [方法条目](../discovery/web-and-api.md) |
| PII 的字段、权限与用户动作分别定影响 | Indeed 参数及 JS route 的正文称需交互、通常P3，但赏金图隐藏参数与对象。 | [方法条目](../impact-and-acceptance.md) |
| eMode 价格源分支需要明确零地址与回退语义 | Morpho _getAssetPrice/isInEMode 描述涉及 priceSource 为零地址的分支。 | [方法条目](../by-type/smart-contract.md) |
| 方法覆盖应在各层按最终动作统一校验 | POST中 _method 选择PUT/DELETE可能被框架转换，需分别记录原方法、覆盖字段解析、代理路由、认证/CSRF/授权校验顺序与最终消费者。 | [方法条目](../discovery/web-and-api.md) |
| 相对图片路径不能赋予目标动作免验证 | 保存示意将 change_photo 的 filename 写成相对 change_password 路径并回到 img src。 | [方法条目](../by-type/csrf.md) |
| 路由器恶意链示意保留初始执行前提 | GobRAT 图从 SSH 执行开始，后续loader下载、daemon/start脚本、ELF创建/执行再连C2。 | [方法条目](../by-type/iot-security.md) |
| CSRF token 数组必须保持严格 schema | 正文提出 csrf token[]/空数组，需保留原参数、解析后类型及验证函数。 | [方法条目](../by-type/csrf.md) |
| 页面端点提取应保留异步与浏览器访问限制 | 保存console脚本从script src fetch正则匹配及outerHTML收集，再Set去重/3秒后document.write。 | [方法条目](../discovery/client-and-cloud.md) |
| Merge Request 分支名渲染依赖具体 rebase 条件 | GitLab 报告要求semi-linear或fast-forward merge、需要rebase、访问者不能push source branch、目标分支名含HTML。 | [方法条目](../by-type/xss.md) |
| FogBugz 导入 URL 与后台登录请求按时序关联 | 保存GitLab导入示例把用户输入URL指向同容器loopback listener，截图有POST api.asp及登录字段。 | [方法条目](../by-type/ssrf.md) |
| 可认领服务名与 CSP 指令能力分别证明 | 保存Fastly报告称自动生成freetls域可由另一账号控制，且GitLab的connect-src包含该域。 | [方法条目](../by-type/subdomain-takeover.md) |
| RelayState 保存后的下一次登录重定向需独立校验 | GitLab摘要称SAML登录POST的RelayState外跳被保存在cookie，后续signin又导航。 | [方法条目](../by-type/saml-sso.md) |
| 回调中的 cookie 样字符串不补齐完整执行链 | 保存Collaborator记录有DNS/HTTP、favicon请求与Referrer中编码的cookie样字段。 | [方法条目](../by-type/xss.md) |
| 异常 Content-Type 差异先验证浏览器与后端解析 | 正文用 text/plain 后附 application/json 声称跨站绕过。 | [方法条目](../by-type/csrf.md) |
| JSON 包装对象不应信任其名称赋予权限 | 保存图声称root array能登录管理员，实际示例是嵌套root对象。 | [方法条目](../by-type/authn-session.md) |
| Expo return URI 状态污染需绑定合法登录交易 | 两图显示正常移动登录经Expo/Facebook回到应用scheme，以及攻击示意先污染ru/returnUrl再让后续token去外域。 | [方法条目](../by-type/oauth-oidc.md) |

| 频道资产条目保留采集上下文 | Discord 频道中的域名条目只能成为待核候选。 | [方法条目](../discovery/records-and-incremental.md) |
| LFI 编码与包装器按解码链验证 | 保存图列出路径编码、空字节/截断、过滤器和归档包装器等候选。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 响应中的内网地址是拓扑线索 | 响应出现私有地址时先保留字段上下文、响应身份和调用来源。 | [方法条目](../discovery/passive-and-services.md) |
| PTR 批量结果区别于正向解析 | dnsx PTR/CIDR 示例展示 IP 到名称的反向关联。 | [方法条目](../discovery/passive-and-services.md) |
| 重定向流水线保留最终 authority 证据 | 保存的 subfinder、httprobe、Wayback 与 Nuclei 组合先发现候选，正文和截图的输入 scheme 不一致，需核对各工具接受裸域名还是完整 URL。 | [方法条目](../by-type/open-redirect.md) |
| JS 线索追到真正消费者 | 静态工具、文件名猜测及人工阅读可相互补充。 | [方法条目](../source-audit.md) |
| 根对象示例先核对 schema 与认证结果 | 保存帖把 nested JSON 根对象与 root array 的说法混在一起。 | [方法条目](../by-type/authn-session.md) |
| 搜索规则页与鸣谢先确认许可 | 搜索 bug bounty、security.txt 或 reward 字样可定位政策候选，检索语法本身须保留，不能把误写的操作符当有效筛选。 | [方法条目](../scope-and-rules.md) |
| 邀请角色非法值核对账户状态边界 | 邀请流程中的 admin/edit/view 角色枚举应绑定邀请者权限、目标组织和接收者状态。 | [方法条目](../by-type/business-logic.md) |
| CT 工具输出保留证书历史与去重关系 | CRTER 示例输出重复子域名。 | [方法条目](../discovery/records-and-incremental.md) |
| SSRF 到 Windows 强制认证需要协议前提 | 保存正文提出 Responder、NetNTLM 哈希、破解或 SMB relay 链。 | [方法条目](../by-type/ssrf.md) |
| Burp 显示字体调整不改变请求证据 | 保存图区分界面字体与 HTTP message 字体，字号调整有助于阅读长请求。 | [方法条目](../discovery/records-and-incremental.md) |
| FPM full status 暴露只按实际字段计影响 | 保存帖及既有已读图 `1664180026429046784-02.jpg` 展示 PHP FPM full status 可含 worker 指标、当前请求及路径。 | [方法条目](../by-type/info-secrets.md) |
| 移动 Cloud Shell 示例区别于执行验证 | 已读图片 `1664180798545858561-02.jpg` 展示移动端 Cloud Shell 文件与工具界面。 | [方法条目](../experiment-design.md) |
| 报告 participants 列表校验报告 ACL | 邀请未注册邮箱为协作者后，participants 接口的字段可能扩大可见面。 | [方法条目](../by-type/idor-access-control.md) |
| H2C 升级隧道核对逐请求策略边界 | 保存示意图中代理转发 Upgrade/HTTP2-Settings 等 hop-by-hop 信息，后端 101 后形成 H2 明文隧道，可能使后续流量跳过代理的路由、WAF 或认证。 | [方法条目](../by-type/request-smuggling.md) |
| 注册字段的 blind XSS 要绑定后台消费者 | 保存正文称在注册 fullname/email comment 写入后出现回调。 | [方法条目](../by-type/xss.md) |
| VDP 接受回执保留不公开条款 | 保存回执明确不允许公开披露。 | [方法条目](../scope-and-rules.md) |
| 回调验证保留 token 与输入位置对应 | Canarytokens/Collaborator 与 Intruder header 示例都需要将唯一受控 token 绑定到单一请求、字段、身份和时间。 | [方法条目](../discovery/records-and-incremental.md) |
| 深入项目靠可追溯的增量覆盖 | Wayback/gau/katana、手工 JS 阅读和私有词表分别提供历史、爬取与猜测候选。 | [方法条目](../hunting-strategy.md) |
| worker 控制到 bastion 输出跨终端边界 | 保存截图描述先经 CI/docker socket 控制 worker，再让替换的 daemon 信息被 docker-machine 读取并输出到 bastion。 | [方法条目](../cloud/container-k8s-security.md) |
| 私有 personal snippet 的评论操作绑定父对象 | 保存代码中 PersonalSnippet 分支使用全局集合，而其他分支限定项目/用户。 | [方法条目](../by-type/idor-access-control.md) |
| epic 关联需要两端授权与可见性检查 | 保存片段描述 Ultimate 多层 epic API 可把自有组 child 指向其他组 parent ID。 | [方法条目](../by-type/idor-access-control.md) |
| Kroki 语言校验值必须与取值来源一致 | 保存代码允许 code 或 pre 的语言满足选择条件，却优先取 parent 的语言生成结果属性；合法 child 的语言不能替任意 parent 值背书。 | [方法条目](../by-type/xss.md) |
| 扫描器清单按角色与动作拆分 | 既有图片 `1664466327455805443-02.jpg` 混列 Nuclei、Metasploit、Nikto、Jaeles、retire 等不同工具。 | [方法条目](../discovery/web-and-api.md) |
| 空过滤器不能代替 GraphQL 对象授权 | 保存正文称 filter 为空可返回其他用户。 | [方法条目](../by-type/graphql.md) |
| WebDAV 认证限速与 Basic 编码分别验证 | 保存图中私有 calendar/WebDAV 链接使用 Basic 认证，用户名/密码的 Base64 是编码，不能当作绕过因素。 | [方法条目](../by-type/authn-session.md) |
| ASN 与索引服务发现分别核实权属 | ASN/Naabu 示例、Shodan TLS 搜索、InternetDB 和 BGPView API 提供路由、证书或历史服务候选。 | [方法条目](../discovery/passive-and-services.md) |
| 邮箱到 Oculus 用户关联按隐私边界计影响 | 保存 Meta 答复支持特定邮箱可关联 Oculus 用户的历史去匿名问题。 | [方法条目](../impact-and-acceptance.md) |
| 生成子域候选仍需独立来源验证 | SubGPT 的工具题名与卡片没有实际查询结果。 | [方法条目](../by-type/ai-application.md) |
| 技术指纹不能补成重定向复现 | Wappalyzer 截图中的框架、像素、HSTS、CDN/captcha 标签可用于选择后续检查，但需保存来源 URL、时间和识别依据，并允许误判。 | [方法条目](../discovery/web-and-api.md) |
| RAG 架构图片与正文分开绑定来源 | 本帖正文指向 Burp 提示，但保存图描绘 STIX/TAXII 到文档、分词/embedding、向量库、retriever 与 LLM 的流程。 | [方法条目](../by-type/ai-application.md) |
| CSRF 清单按真实浏览器与最终状态归因 | 保存清单含 token 移除/替换/跨账号、方法变更、Content-Type、Referer、XSS/CORS 读 token 等分支。 | [方法条目](../by-type/csrf.md) |
| URL 前缀切片校验与消费者解析要一致 | 保存 isSafeHost 片段按首个 :// 切片再 startsWith allowlist，缺少严格 scheme、hostname 与端口解析；javascript 或注释文本可能使字符串片段看似可信。 | [方法条目](../by-type/open-redirect.md) |
| SiteMinder Unicode 转义依赖真实解码 sink | 保存片段将历史 SiteMinder CVE-2013-5968 与 USERNAME 参数和 Unicode 转义关联。 | [方法条目](../by-type/xss.md) |
| 索引凭据发现与后续利用链分段举证 | 保存正文称先发现可登录但无权限的凭据，再找到另一组并接续历史 CVE 利用。 | [方法条目](../by-type/info-secrets.md) |
| 延时型 SQL 假设排除并发与异步消费者 | 正文中的 URL 参数、ORDER BY 及 X-Forwarded-For 时间表达式都应先定位真实 SQL 消费者、方言和代理对 header 的处理。 | [方法条目](../by-type/sql-injection.md) |
| 参数键去重保留接口与出现位置 | unfurl --unique keys 后排序可汇总 URL 参数名，但键名并集会丢失来源、接口、重复值及角色。 | [方法条目](../discovery/records-and-incremental.md) |
| 官方反射 XSS 摘要保留执行证据缺口 | 保存 TikTok 摘要支持 link 参数相关的历史浏览器脚本问题。 | [方法条目](../by-type/xss.md) |
| 家庭配对限制操作校验关系与动作权限 | 保存 TikTok 摘要描述 POST 中 user_id 可影响 screen limit，涉及家庭配对关系和受限制账号。 | [方法条目](../by-type/idor-access-control.md) |
| 后台自动化流水线保持阶段输出类型 | 保存 bash 把 subfinder/assetfinder 追加输出交给 httpx，再把带状态文本交给 Wayback，存在 URL 与展示文本混用。 | [方法条目](../discovery/records-and-incremental.md) |
| API 异常输入先定位消费语义 | 保存建议对 API 参数尝试异常值。 | [方法条目](../targeted-fuzzing.md) |
| 更换网络出口不能改变项目限速许可 | 保存 VPN 连接界面只能支持连接状态，不能证明测试解除封禁或获得新许可。 | [方法条目](../scope-and-rules.md) |
| 重新评估报告靠新增受保护动作证据 | 保存状态通知展示 NA、重开、复核与 triaged/resolved 的变化。 | [方法条目](../reporting.md) |
| 严格 token 流程用宏保持真实事务关系 | Burp macro 可帮助在获准自有流程中刷新 CSRF/session 值。 | [方法条目](../discovery/records-and-incremental.md) |
| 登录后 dest 必须按最终 URL 消费者校验 | 保存正文描述 Reddit 登录后 dest 接受 javascript 形式。 | [方法条目](../by-type/xss.md) |
| 接管监控变化保留基线与失败集合 | dig/subzy/DNS recon 与 watchtower 示例提供接管候选，奖励邮件和 landing 页均不独立证明第三方资源可认领。 | [方法条目](../discovery/records-and-incremental.md) |
| Ferox bash 先审参数展开和输出覆盖 | 保存脚本的数组元素可能把多个选项当单 argv，带引号的 ~ 不展开，共用输出路径可能覆盖；HTTP 前缀、grep 200/awk 字段和闲置变量也依赖具体输入/格式。 | [方法条目](../targeted-fuzzing.md) |
| .git 列表暴露与源码执行链分开 | 截图可见 .git 元文件目录索引。 | [方法条目](../by-type/info-secrets.md) |
| 非标准 IPv4 统一规范化后检查地址边界 | 保存帖列举十六进制、八进制和混合 octet 等 metadata 地址表示。 | [方法条目](../by-type/ssrf.md) |
| 链接触发崩溃需要版本与异常轨迹 | WhatsApp 的 wa.me/settings 字段截图只展示输入，缺少完整崩溃栈、版本和恢复验证。 | [方法条目](../by-type/mobile-android.md) |
| B2B owner 变更校验现任与目标资格 | owner 更新须检查调用者对当前对象的管理权限、目标成员资格及组织边界，并保持原子更新。 | [方法条目](../by-type/idor-access-control.md) |
| PURGE 接受响应不足以证明缓存驱逐影响 | 保存图返回 status ok/id，受理回执与实际驱逐是两项证据。 | [方法条目](../by-type/cache-deception.md) |
| 转换名称字段区分渲染与持久传播 | AdWords conversion name 截图包含事件形式和 origin 弹窗。 | [方法条目](../by-type/xss.md) |
| Jira 到 Bitbucket 链每一跳检查权限 | 正文提出 Jira SSRF 访问内部 7990 再到源码。 | [方法条目](../by-type/ssrf.md) |
| Joomla public 参数不能决定配置 API 授权 | 保存正文把 Joomla 4.0.0–4.2.7 的配置 API 与 public=true 关联。 | [方法条目](../by-type/info-secrets.md) |
| 2FA 修复覆盖全部会话签发路径 | 保存帖称两条绕过路径中只修一条。 | [方法条目](../by-type/authn-session.md) |
| enabled 状态字段绑定管理权限与会话状态 | 保存片段从中间步骤描述 enabled=true 对组织账号状态的影响。 | [方法条目](../by-type/idor-access-control.md) |
| 404 缓存污染验证隔离 key 与干净读取 | 保存帖描述 X-Forwarded-Host 影响缓存后的错误页。 | [方法条目](../by-type/cache-deception.md) |
| 模板目录元数据只用于选择候选 | 模板的 ID/name/tags/author 可帮助定位相关检查，但需保存具体模板版本、哈希、匹配条件和会触发的动作。 | [方法条目](../source-audit.md) |
| 关闭管理员 2FA 的题名保留动作前提 | 正文只给出 CSRF 关闭 admin 2FA 的题名。 | [方法条目](../by-type/csrf.md) |
| JS 候选与公开凭据文件按真实内容分类 | 保存 JS 搜索管道停在 URL 清单，grep 的关键字命中不能代替获取并审阅真实 JS 响应，.js 未转义及递归 grep/管道语义也要核对。 | [方法条目](../by-type/info-secrets.md) |
| APK 静态泄露候选保存规则与版本 | 既有已读图片 `1665988005188759552-02.jpg` 展示 APKLeaks 文件/规则/JSON 参数。 | [方法条目](../discovery/client-and-cloud.md) |
| JS 到上传执行链按消费者分段 | 正文把大量报告、JS、上传过滤器与 RCE 串联。 | [方法条目](../by-type/file-upload.md) |
| API 白皮书宣传不独立证明分类覆盖 | 保存正文介绍 ChatGPT/API Top 10 白皮书，没有全文、数据集或评估。 | [方法条目](../by-type/ai-application.md) |
| 目录数量与状态是历史发现元数据 | 2362 等目录计数、徽章与平台表格可帮助找候选，但需保留截图时间、样本范围及缺失项。 | [方法条目](../scope-and-rules.md) |
| YouTube 字样检查须绑定精确 authority | 保存正文描述输入中的 YouTube 字样使检查通过，而 URL authority 指向 loopback。 | [方法条目](../by-type/ssrf.md) |
| XSS 字符改写不能声称 Cloudfront 通用绕过 | 保存提示组合属性名拆分、模板标签调用、SVG 分隔符及百分号编码。 | [方法条目](../by-type/waf-bypass.md) |
| 爬虫首次到达路径保留导航与身份 | Burp Crawl paths beta 图显示首次到达页面的点击链。 | [方法条目](../discovery/records-and-incremental.md) |
| 验证者列表索引修复核对不变量 | 保存正文描述 validator 错索引使计数停止，缺少完整合约代码。 | [方法条目](../by-type/smart-contract.md) |
| CASB integration 创建校验委托租户归属 | 保存公开摘要支持历史 Cloudflare CASB 问题：Microsoft tenant UUID/domain 或 GitHub installation_id 已被另一客户集成时，攻击者可据这些标识建立新 integration 并显露敏感信息。 | [方法条目](../by-type/oauth-oidc.md) |
| 修复确认与披露草稿审阅分别记录 | 保存 Microsoft 邮件确认修复/结案并要求协作审阅披露稿以避免客户风险。 | [方法条目](../scope-and-rules.md) |
| Windows Hello 提示必须绑定密钥访问控制 | 保存 Bitwarden 报告说明生物识别 master key 写入 Windows Credential Manager，可由当前用户会话的普通进程通过 CredRead 取得，并与本地 data.json 一起在锁定/关闭后持久。 | [方法条目](../by-type/desktop-client.md) |
| 公开报告附件审阅其独立敏感内容 | 保存报告指出已发布报告中的截图暴露私有 program 的入口与遮盖不足。 | [方法条目](../reporting.md) |
| Android 深链写入与回包出口分开检查 | 保存 Basecamp 公开摘要关联 com.basecamp.bc3 3.26.3：路径穿越影响应用私有目录写入，恶意 intent/custom deeplink 还可把服务端敏感响应发给第三方应用。 | [方法条目](../by-type/mobile-android.md) |
| FAQ 分类从 self XSS 到邀请用户要证明可达 | 保存正文描述自有 FAQ category 中的脚本式内容经编辑/ID 和邀请用户流程到达他人。 | [方法条目](../by-type/xss.md) |
| Agartha 生成选项与漏洞验证分开 | 保存 Burp 扩展界面显示 DT/LFI、Command Inj/RCE、SQLi、Depth、Waf Bypass 和 Authorization Matrix。 | [方法条目](../targeted-fuzzing.md) |
| 历史品牌范围描述逐项核对当前权属 | 保存 Sony 范围图描述其拥有、运营、控制的产品/域名。 | [方法条目](../scope-and-rules.md) |
| 私有项目邀请与修复回执不授权公开 | 保存私有项目邀请要求保密；另有重开/解决回执。 | [方法条目](../scope-and-rules.md) |

| 图片型 SSRF 验证区分获取能力与产品指纹 | 正文给出 base 参数候选和仅能读取特定图片的 SSRF 假设。 | [方法条目](../by-type/ssrf.md) |
| QR 扫描后的导航仍须用户确认边界 | 保存 Brave 摘要描述 QR 扫描器打开链接时缺少用户知情确认，关联历史 Android/浏览器版本。 | [方法条目](../by-type/open-redirect.md) |
| TLS pass through 排除项记录解密覆盖缺口 | 保存帖建议对第三方域名设置 Burp TLS Pass Through，但把 HTTP scheme、空格和域名模式混列。 | [方法条目](../discovery/records-and-incremental.md) |
| env.js 中字段公开与有效 secret 分开评估 | 保存图含 window.env 的 API/WebSocket/auth URL、clientId/clientSecret、scope 和 responseType。 | [方法条目](../by-type/info-secrets.md) |
| SVG 上传的存储与脚本消费者分别证明 | 保存正文只给 stored XSS via SVG file upload 的题名，图片是礼品卡回执。 | [方法条目](../by-type/file-upload.md) |
| 配置文件扩展大小写差异检查真实响应体 | 保存帖对 wp-config.php 的 403 与大写扩展的 200 做比较，多端口 one-liner 的 subfinder 输入在正文和图片中还存在 scheme 差异。 | [方法条目](../by-type/info-secrets.md) |
| API 业务敏感性与重复动作成本按流程建模 | 正文强调相同 API 流程在不同公司意义不同，并列购买、优惠券校验、图片上传等重复动作。 | [方法条目](../business-modeling.md) |
| 接管报告等级改变需回到权利与影响证据 | 保存通知显示 Medium 5.3 改为 None 0.0，却没有完整解释或 DNS/认领过程。 | [方法条目](../reporting.md) |
| 域名与直接 IP 访问核对虚拟主机上下文 | 正文称同一路径在域名无结果而直接 IP 访问出现内容。 | [方法条目](../by-type/host-header.md) |
| GeoServer 模板题名绑定产品版本和匹配动作 | 保存 GeoServer SQL 注入 CVE 题名与 Nuclei 搜索/模板命令可作为历史检查线索。 | [方法条目](../source-audit.md) |
| 组织到 ASN 前缀转换保留查询类型与时间 | BGP 目录步骤和 ASNmap 的 ASN/ORG/DNS/IP 到 CIDR 转换提供路由候选。 | [方法条目](../discovery/passive-and-services.md) |
| 403 与重定向入口仍按单资产限定发现 | 正文建议继续枚举 403 或立即跳到另一主机的入口。 | [方法条目](../targeted-fuzzing.md) |
| 编码载荷与 OOB 请求需绑定相同渲染链 | 保存 POST fullname 示例把 Base64 字符串交给事件处理器的 eval/atob，正文称简单输入 302 而 OOB 输入 200。 | [方法条目](../by-type/xss.md) |
| JS exposures 管道先审语法与真实权限 | 保存 one-liner 的 grep 额外引号造成 shell 语法风险，.js 模式未转义，httpx Content-Type 展示与 awk 字段依赖格式。 | [方法条目](../by-type/info-secrets.md) |
| 请求头自动补全保留字段语义与版本 | Burp 扩展截图展示 Content-* 词表补全。 | [方法条目](../discovery/records-and-incremental.md) |
| Credential Management 调用不等于凭据已泄露 | 保存正文只有 navigator.credentials.get 的赋值示例。 | [方法条目](../by-type/xss.md) |
| 搜索 IP 与生成 dork 保留索引证据边界 | IP 限制检索和 DorkSearch 页面提供候选查询，既有已读图片 `1667218161123610625-02.png` 记录历史搜索条件及词数截断。 | [方法条目](../discovery/passive-and-services.md) |
| cPanel 错误页状态与脚本执行独立判断 | 保存历史 cPanel CVE-2023-29489 资料指向 webcall 错误输出中的编码输入，另一图可见 400 错误页与 prompt。 | [方法条目](../by-type/xss.md) |
| 支持票据创建不信任邮件 From 字段身份 | 保存正文提出邮件 From 冒用可能让支持系统把票据归到另一用户。 | [方法条目](../by-type/authn-session.md) |
| 代理与 Tomcat 路径规范化用同一资源对照 | 保存正文描述 nginx 与 Tomcat 对分号段处理不同，以及 Windows/Tomcat 的重复斜线差异。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 清单和表单生成器保持浏览器请求约束 | 保存清单含 token 移除、跨账号/同长度替换、方法与媒体类型、Referer、XSS/CORS 和旧 Flash 分支。 | [方法条目](../by-type/csrf.md) |
| 预接管争议按账号生命周期区分根因 | 正文只有 OAuth/pre-account takeover 与 duplicate 的争议，缺少完整链。 | [方法条目](../reporting.md) |
| 隐藏参数反射与实际消费者分开 | ffuf 的 PARAM/XSS 匹配和 Arjun 的词表只提供参数候选。 | [方法条目](../targeted-fuzzing.md) |
| 范围更新截图只证明历史具体条目 | 保存 Shopify 图标明 admin URL Added in Scope/Eligible true。 | [方法条目](../scope-and-rules.md) |
| DOM sink 日志继续追源和转义 | 人工 JS 阅读与 Untrusted Types 日志可帮助定位 document.write/innerHTML/eval。 | [方法条目](../by-type/xss.md) |
| LFI dork 参数名只作为消费者候选 | 保存 dork 含重复 page 及 API_HOME_DIR/cmd 等名称。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Wayback 到模板管道保留阶段候选与遗漏 | 保存命令中的 waybckurls 拼写与各阶段输入要核对，Google ext:php 检索条件也不会自动传入管道。 | [方法条目](../discovery/records-and-incremental.md) |
| eMMC 拆卸前检查板上测试点前提 | 保存硬件提示建议先检查芯片附近测试点，避免直接拆卸损坏设备。 | [方法条目](../by-type/iot-security.md) |
| 下载接口参数变更核对对象与查询边界 | 保存图片称从公开 git 源码发现 download.php 的另一参数，原参数下载为空，并展示部分用户表。 | [方法条目](../by-type/idor-access-control.md) |
| JS 路径提取保留来源和运行时可达性 | JSend/JSpector/LinkFinder 提供静态路径候选，图片展示重复条目、localhost 地址及 Information/Certain 标签。 | [方法条目](../source-audit.md) |
| 耗时截图与 header 扫描标签不是成对 SQL 证明 | 保存 POST JSON 的 customer.email 示例响应耗时约 13.6 秒，HTTP 404 又含业务 status 401；header 扫描图的多次候选有约 5/35 秒变化。 | [方法条目](../by-type/sql-injection.md) |
| 漏洞资源搜索类别与全文证据分开 | 保存页面含 XSS/SSRF/SQLi/RCE/IDOR 类别、q 查询及 JSON export。 | [方法条目](../discovery/records-and-incremental.md) |
| 参数变数组的错误信息按可见字段计影响 | 正文提出向参数传数组可能暴露路径。 | [方法条目](../by-type/info-secrets.md) |
| Wix 委托候选需要服务归属验证 | 保存 Omise 报告称域指向 Wix 且未认领，图片只显示摘要和状态，正文评级与图中 No Rating 不一致。 | [方法条目](../by-type/subdomain-takeover.md) |
| 重置链接外发日志与账户控制分段举证 | 保存受控请求日志含 reset-password 路径和邮箱参数，正文称 Host→重置链接→XSS→接管链。 | [方法条目](../by-type/authn-session.md) |
| 空响应和双版本路径是 API 候选线索 | Swagger 路径清单与 /api/v1/report-v2 的命名可引导寻找文档或历史并行接口。 | [方法条目](../discovery/web-and-api.md) |
| 默认欢迎页与旁路 JS 线索分别记录 | 保存 IIS 默认页本身没有 URL、产品版本或可操作功能。 | [方法条目](../discovery/web-and-api.md) |
| 默认密码候选必须绑定实际身份能力 | 正文提出 test:test 或 JBoss admin-console 的默认值。 | [方法条目](../by-type/authn-session.md) |
| 重复报告反馈转为具体研究问题 | Chrome 状态列表有 Duplicate、Closed、Triaged 和 Fixed，正文把它解释为内部工具覆盖多数问题。 | [方法条目](../hunting-strategy.md) |
| 改密码错误提示后核对真实事务状态 | 保存页面在前端长度/匹配检查通过后提示 Change password error。 | [方法条目](../by-type/authn-session.md) |
| 匿名文件访问按目录权限和最小数据判断 | 正文称匿名 FTP 或目录索引暴露文件/地址证明。 | [方法条目](../by-type/info-secrets.md) |
| 通配检索品牌关联不替代资产归属 | 保存 site 通配 dork 可能匹配含品牌字样的外部域或历史子域。 | [方法条目](../discovery/passive-and-services.md) |
| 研究投入用阶段性判断条件而非不断加时 | 正文中翻倍时间、日常坚持和休息建议要与实际信息增量结合。 | [方法条目](../hunting-strategy.md) |
| 导出 Activity 到 WebView 和本地 token 分环验证 | 正文给出 exported activity、WebView 与 SharedPreferences 的接管链名。 | [方法条目](../by-type/mobile-android.md) |
| 邮箱规范化必须与查重和会话绑定一致 | 保存注册对照中小写邮箱返回 422 已存在，改域名大小写后 201 并返回规范化邮箱、session 与 user 字段。 | [方法条目](../by-type/authn-session.md) |
| dnsx 到 httpx 输出核对输入词表语义 | 保存命令把 programs.txt 与逗号分隔候选交给 dnsx，图片有多个 grafana 名称的 200。 | [方法条目](../discovery/records-and-incremental.md) |
| public 前缀变体检查同一对象的保护规则 | 正文建议把受登录保护的路径前加 public。 | [方法条目](../by-type/idor-access-control.md) |
| 404 重试变 200 先确认可比请求与状态 | 保存两个截图的路径、header 和响应字段被遮盖，时间相近但不能核实字节与身份完全一致。 | [方法条目](../experiment-design.md) |
| 模板下载 token 不进入命令与日志证据 | 保存 newclei 命令含部分遮盖的 GitHub token。 | [方法条目](../by-type/info-secrets.md) |
| 下载模板清单与实际加载覆盖分别保存 | 图片中的编码文件名涵盖文件审计、malware、网络、HTTP 与 GraphQL，不是模板正文。 | [方法条目](../source-audit.md) |
| unkeyed 输入到缓存污染还需干净读取对照 | 正文只描述操纵未纳入 key 的输入使响应缓存。 | [方法条目](../by-type/cache-deception.md) |
| ParamSpider 与 Nuclei 组合保留错误和独立验证 | 保存 NucleiFuzzer 图有 134 个 URL、18 个模板、扩展排除、旧协议警告及 30 次不响应后跳过入口。 | [方法条目](../targeted-fuzzing.md) |
| Security Lab 查询改进题名只作审计索引 | 保存资料列 Python Unicode 校验、Next.js XSS 源/sink、C++ 长度/除零、Go JWT、Paramiko SSH、GitHub Actions 与解包/TarSlip 等查询方向。 | [方法条目](../source-audit.md) |
| 历史 signup token 不应自动赋予当前注册权限 | 正文称只有 sign-in 界面，却从 Wayback 找到 signup/referral token 可创建账号。 | [方法条目](../by-type/authn-session.md) |
| 代码追问仍保留 root array 题名的类型错误 | 本帖正文只提视频深入研究，既有已读图片 `1668945427687788547-02.jpg` 实际示例是 nested JSON root object。 | [方法条目](../by-type/authn-session.md) |
| 搜索邮箱字串保留公开设计反例 | 保存 dork 中的 Gmail 字串可以定位索引候选。 | [方法条目](../by-type/info-secrets.md) |
| 鸣谢旁的 Unique 与 Total 计数不代表已修复覆盖 | 保存图注明 Unique 含 Triaged/Unresolved/Informational，Total 还包含 Duplicate。 | [方法条目](../scope-and-rules.md) |
| 第三方托管页面与新功能归属分别核实 | 正文建议从 sites.google.com 中找公司页面。 | [方法条目](../discovery/passive-and-services.md) |
| 名称字段跨子域显示检查每个真实 sink | 正文提示表单 name 可能在另一子域显示。 | [方法条目](../by-type/xss.md) |
| 工程优先级与确认修复和奖金各自保留状态 | 保存 Google 邮件分别更新 type、priority、severity、In Progress/Accepted，说明后续产品修复与 VRP 评审另待通知。 | [方法条目](../reporting.md) |
| Openfire setup 例外与规范化后受保护路由分层核验 | 保存本地历史 Openfire 图片显示 setup 前缀下编码路径到 log/plugin-admin/user-create，随后管理员属性页面，关联 4.7.4。 | [方法条目](../by-type/authn-session.md) |
| 订单地址页弹窗保留未知输入与持久性 | 保存图片展示 billing address 页面和 XSS 文本弹窗，origin 被遮盖。 | [方法条目](../by-type/xss.md) |
| CSP 信任 CDN 需要匹配真实脚本消费者 | 正文提出第三方 CDN 上传内容可能落入 CSP 允许范围。 | [方法条目](../by-type/xss.md) |
| 配图的对象权限机制不冒充正文漏洞类型 | 一帖正文标 SSRF，而保存图描述从源码找到 user_id 后修改其他账号 email/name；另一帖写 password reset，图却是 IDOR 1234→1235 的示意。 | [方法条目](../by-type/idor-access-control.md) |
| 目录扫描排除规则不能当没有敏感入口 | 保存 dirsearch 命令排除多种状态和扩展。 | [方法条目](../targeted-fuzzing.md) |
| 进程资源截图与任务完成证据分开 | 保存 htop 照片显示大量进程及 CPU/内存，部分细字不可完整读取。 | [方法条目](../discovery/records-and-incremental.md) |
| 子域词表比较保持共同基线与资源预算 | 正文比较自建/n0kovo 的 50k/200k 词表命中数，缺少测试时间、范围和 wildcard/去重定义。 | [方法条目](../experiment-design.md) |
| JS 下载与生成词表绑定响应版本 | 正文工具功能分成 Wayback/gauplus/subjs 候选、可选下载与从内容生成词表。 | [方法条目](../source-audit.md) |
| 代码托管检索先确定内容来源与公开意图 | 正文的 repl.it 查询语法有不完整 intext 条件。 | [方法条目](../by-type/info-secrets.md) |
| 重定向参数 JS 改写需要同一导航 sink 对照 | 保存正文给出 next 从外域导航到 javascript 改写的两部分，图片有 cookie 样文本弹窗。 | [方法条目](../by-type/xss.md) |
| 按组织名猜存储桶不证明文档本应私有 | 正文列 storage.googleapis.com 下组织名候选。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| Chamilo 命令注入题名追到服务端执行消费者 | 保存 Nuclei 图显示历史 CVE-2023-34960、additional_webservices.php、单模板和多个目标标签，其中含 loopback/私有/示例地址。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 爬取到 Dalfox 的 one-liner 保留原样语法错误 | 保存命令有 -c/-d 粘连、黑名单拼写/分隔错误、awk 引号语法及 -o 换行等问题。 | [方法条目](../discovery/records-and-incremental.md) |
| PHP URL 错误匹配不形成二元 SQL 漏洞判断 | 保存图片的 one-liner 用 grep/sed 改写 PHP URL 后追加编码字符，curl 匹配固定 SQL 错误并打印 Vulnerable/Not Vulnerable。 | [方法条目](../by-type/sql-injection.md) |

| Django 路由前缀命中应与视图授权分开检查 | 保存代码把 `^inbox/` 注册到 `views.index`，未显示结束锚点；这使“哪个完整路径进入同一视图”成为源码审计问题。 | [方法条目](../source-audit.md) |
| 缓存命中与持久脚本执行需要分别建立证据 | 正文把 reflected XSS 加上 `X-Cache: Hit` 推为 stored XSS，附图只显示 cache poisoning、零点击 ATO 的报告标题。 | [方法条目](../by-type/cache-deception.md) |
| WAF 片段、事件属性与 XSS 到 CSRF 的链条分步验证 | 保存正文包含 HTML 实体、字符串拼接、鼠标或焦点事件及反射脚本到 CSRF/BXSS 的主张。 | [方法条目](../by-type/xss.md) |
| robots 和 sitemap 描述发现入口而非访问许可 | 正文建议检查 robots 与 sitemap。 | [方法条目](../discovery/web-and-api.md) |
| 浏览器 fetch、服务器请求与远程文件包含不是同一个消费者 | 正文从 XSS 中的 `fetch` 推到 RFI/SSRF，截图仅列出待评估的报告标题。 | [方法条目](../by-type/ssrf.md) |
| 扫描通知卡片必须回链到具体运行和可复核响应 | 图片显示扫描完成、端口扫描以及 LFI/XSS 高危通知。 | [方法条目](../discovery/records-and-incremental.md) |
| .git 目录拒绝访问仍须区分子文件与完整仓库暴露 | 两个同文帖子附图分别显示 `.git/` 的 403 和 `.git/config` 的 200，配置响应可见 Git 核心配置，余下内容被遮挡。 | [方法条目](../by-type/info-secrets.md) |
| metadata 响应归因应服从响应内容而非标题中的云厂商 | 保存请求使用 metadata 地址，正文称为 AWS；图片响应正文却显示 `computeMetadata/`，没有 AWS 凭据、完整元数据路径或后台调用记录。 | [方法条目](../by-type/ssrf.md) |
| 侦察工具列表按输入与输出阶段组织 | 图片列出 DNS、端口、截图、历史 URL、词表和模板等工具。 | [方法条目](../discovery/records-and-incremental.md) |
| 秘密候选按字段语义、当前有效性和实际授权能力分级 | 保存正文把 keyhacks、shell 历史、配置文件及 CI 文件当作秘密来源。 | [方法条目](../by-type/info-secrets.md) |
| 请求清理与动态令牌自动化须保留会话和请求对应关系 | 请求清理图片保留 POST 表单、Cookie、CSRF 字段及重定向；另图是带唯一 CSRF 令牌的表单，课件描述 Recursive Grep、Pitchfork 和 session handling rules。 | [方法条目](../discovery/records-and-incremental.md) |
| 登录响应中的 password 字段先判定类型和对象归属 | 图片显示后台登录接口返回包含用户名和十六进制形态 password 字段的实体。 | [方法条目](../by-type/info-secrets.md) |
| AI 生成模板和请求建议需要独立的语法与证据验证 | 保存帖宣传 Nuclei GPT 和 AI 在 Burp 中分析流量；仓库卡片没有实际生成模板或评估集。 | [方法条目](../by-type/ai-application.md) |
| InternetDB 的端口和 CVE 标签属于有时间边界的资产线索 | 图片展示 InternetDB 返回端口、标签及漏洞编号，没有完整 IP、观测时间和当前版本证据。 | [方法条目](../discovery/passive-and-services.md) |
| 方法覆盖的鉴权应绑定实际执行方法 | 正文描述历史 ESP v2 的 JWT 校验与 `X-HTTP-Method-Override` 处理顺序，保存图以 POST 模拟 PUT 解释覆盖功能。 | [方法条目](../by-type/authn-session.md) |
| JavaScript 路径发现须回到实际调用点和资源权限 | 正文建议从 JavaScript 获取隐藏端点，路径发现只证明字符串或调用线索存在。 | [方法条目](../source-audit.md) |
| 奖励与项目允许披露的信息应分开确认 | 图片邮件讨论奖励金额披露和项目内容限制。 | [方法条目](../scope-and-rules.md) |
| 关闭检测提示不等于设备状态或授权边界改变 | Android 模块图片显示开发者相关检测开关及模块内 Test Off。 | [方法条目](../by-type/mobile-android.md) |
| 合法业务流程观察应形成可检验的角色与状态模型 | 正文建议花时间按真实用户操作浏览功能。 | [方法条目](../business-modeling.md) |
| APK 情报提取的静态线索应与运行权限区分 | Artemis 介绍把 APK 中的域名、字符串、权限等转成情报。 | [方法条目](../discovery/client-and-cloud.md) |
| Whitelabel 错误页只能说明一次错误处理路径 | 图片显示 Whitelabel 404；这可以提示某条请求进入默认错误处理器，但无法确定框架版本、actuator 暴露或所有端点都不存在。 | [方法条目](../discovery/web-and-api.md) |
| 邀请凭据必须绑定目标工作区和允许加入的条件 | 正文讨论儿童班级邀请令牌；Slack 历史披露截图描述 `api/signup.createUser` 将工作区一次性邀请凭据与可替换 team ID 组合，使用户加入其他工作区。 | [方法条目](../by-type/idor-access-control.md) |
| 私网 DNS 候选与 HTTP 代理探测应分阶段计证 | Surf 正文和帮助图将域名输入、私网解析检查以及默认 HTTP 探测区分，`-x` 为只做 DNS 私网候选检查而不进行 HTTP 请求。 | [方法条目](../by-type/ssrf.md) |
| SQL 工具帮助和延迟参数不构成注入证据 | HBSQLI 帮助列出 URL、列表、请求头、payload 文件、verbose 及延迟参数。 | [方法条目](../by-type/sql-injection.md) |
| 候选 URL、解析失败和浏览器执行属于不同验证阶段 | 正文宣称自动侦察发现高比例 XSS，图片显示 AutoRecon 阶段文件、Wayback 候选和 Dalfox POC 日志，也出现 invalid URL escape；另一图在测试站显示 alert(1) 与 SQL 错误。 | [方法条目](../targeted-fuzzing.md) |
| 测试页 alert 的证据范围限定到该页面与触发上下文 | 图片实际显示测试站浏览器 alert(1)，但没有完整输入请求、最终 DOM、执行栈及无输入对照；同屏 SQL syntax error 不是独立 SQL 注入证明。 | [方法条目](../by-type/xss.md) |
| JavaScript 与配置文件流水线须保留原始响应和字段权限 | 正文用 gau、JavaScript 筛选、httpx content-type、awk 和 Nuclei exposures 组合发现秘密；另帖筛选多种文件扩展并提到配置字典。 | [方法条目](../by-type/info-secrets.md) |
| 同文范围通知必须按各帖图片分别保留变化 | 两个 Superbet 同文帖的图片不同：一图加入 affiliates.superbet.com 与 .rs 且奖励资格为 false；另一图加入四个 Napoleon 通配域且资格为 true，同时移除特定 metrics 路径。 | [方法条目](../scope-and-rules.md) |
| 403 变体比较要确认是否抵达同一受保护处理器 | 正文列出尾斜杠、空白编码、`X-Original-URL` 和 `X-Rewrite-URL` 等路径变体。 | [方法条目](../by-type/idor-access-control.md) |
| 从 Shodan IP 或组织查询到授权验证还须确认归属和虚拟主机 | 正文与图片建议先索引查询再目录枚举，另帖用 org/title 等查询筛选。 | [方法条目](../discovery/passive-and-services.md) |
| 字段建议推断 schema 后仍须逐 resolver 检查权限 | 正文介绍在关闭 introspection 时利用字段建议恢复 GraphQL schema；卡片只有工具描述。 | [方法条目](../by-type/graphql.md) |
| 尾斜杠限流差异与底层总限额须同时记录 | 两个帖以 `/path` 与 `/path/` 描述端点限流差异，项目回复明确还有更高的 catch-all 总限额并提及奖励。 | [方法条目](../by-type/authn-session.md) |
| URL 状态探测应记录失败和重定向语义 | hakcheckurl 介绍只承诺列表到 HTTP 状态码。 | [方法条目](../discovery/records-and-incremental.md) |
| 同一代理后端的多个 location 应具有一致的访问守卫 | vRNI 历史片段显示 `/saasresttosaasservlet` 带 localhost allow/deny，而更广的 `/saas` 指向同一 127.0.0.1:9090 后端并有相似 rewrite，却未显示同样 ACL。 | [方法条目](../source-audit.md) |
| 历史索引中的邮箱要判定来源、公开意图及实际隐私边界 | 报告图片用归档 CDX 查询寻找约 30 个邮箱，示例值遮挡；正文讨论 Informational 评级。 | [方法条目](../by-type/info-secrets.md) |
| Postman、静态扫描插件和 JS 提取工具只提供候选消费者 | Postman collections、Trufflehog 插件及 jsluice 介绍可帮助发现接口、样例、路径和疑似秘密。 | [方法条目](../source-audit.md) |
| AEM JSON 选择器中的字段仍需证明实际敏感性和身份边界 | 正文指出 AEM `/etc.1.json` 可能含哈希。 | [方法条目](../by-type/info-secrets.md) |
| 子域流水线中先筛 200 会缩小最终覆盖集合 | 图片展示 assetfinder/subfinder 去重后以 httpx 的 `-mc 200` 筛选，再用 awk/cut 截取字符串；最终域名列表只代表该筛选阶段的存活结果。 | [方法条目](../discovery/records-and-incremental.md) |
| JSON 转表单必须验证服务端语义和浏览器请求条件 | 图片把嵌套 `user.id/name` JSON 转成括号键编码的 form body。 | [方法条目](../by-type/csrf.md) |
| 删除对象的 IDOR 需要绑定两自有身份与可恢复的最终状态 | Mars 报告截图描述两个自有账户创建对象，拦截删除请求后替换 animal ID，历史状态为 Resolved/Medium。 | [方法条目](../by-type/idor-access-control.md) |
| 越权更改邮箱和账号接管应按实际恢复能力区分 | Mars 截图明确说明可修改另一个账户邮箱，但新邮箱激活返回 JSON.parse 错误，作者不能访问该账户；报告重点是阻止原用户恢复，历史评级 High。 | [方法条目](../by-type/idor-access-control.md) |
| 运行时权限模型还须覆盖原生代码加载入口 | Node.js 历史报告指出 Node 20 启用 permission model、禁止 native addon 时，`crypto.setEngine()` 仍可加载兼容 OpenSSL engine，从而执行模型外的原生代码；归档编号为 CVE-2023-30586。 | [方法条目](../source-audit.md) |
| 编码跳转参数要在解码后校验完整 URL | Nextcloud UnsupportedBrowser.vue 历史片段把 `redirect_url` base64 解码后赋给 `window.location`，未显示可信目标验证，归档为 CVE-2023-35171。 | [方法条目](../by-type/open-redirect.md) |
| 跨 frame 原生桥接须验证调用 origin、UI 提示和最终脚本上下文 | Brave iOS 历史报告描述三个条件：跨源 subframe 可直接调用 U2F.postMessage；FIDO 提示显示顶层 frame 的 origin；消息 version 未转义进入 evaluateJavaScript。 | [方法条目](../by-type/mobile-ios.md) |
| 绝对形式 request-target 与 Host 的解析边界须独立确认 | DoD 历史图片给出 absolute-form GET 外部回连域，同时 Host 为目标站，报告称 DNS/HTTP external service interaction。 | [方法条目](../by-type/ssrf.md) |
| Docker Registry 的公开索引、镜像权限和源码内容分步验证 | 历史报告以 Shodan 和证书 CN 找到直接 IP 的 Registry v2，并称可下载镜像、可能含机密源码；保存图没有 catalog、manifest、blob 请求或实际内容。 | [方法条目](../cloud/container-k8s-security.md) |
| 对象属性泄露应结合角色必要性检查 | 正文讨论 BOPLA，举 VIN、PII 等响应属性。 | [方法条目](../by-type/idor-access-control.md) |
| 奖励与评级截图不能替代字段级影响说明 | 一图说明读取有限、较低敏感度数据而评为 Medium 并奖励 200；配置文件帖另一图为 Low 3.9、Triaged/Open、150。 | [方法条目](../impact-and-acceptance.md) |
| 联邦共享接收者持有 token 不代表有权扩大权限 | ownCloud 截图描述 X 上用户 A 只读分享给 Y 上用户 B；B 使用其数据库中的 share ID/token 向 federatedfilesharing notifications 提交 RESHARE_CHANGE_PERMISSION，permission 包含 read/write/share。 | [方法条目](../by-type/idor-access-control.md) |
| 等价 MIME 的大小写应在净化和渲染前统一解释 | Nextcloud Contacts PHOTO SVG 报告标题指出只有全小写 MIME 才进入净化，附图 CVE-2023-33182、Resolved、Severity None、无奖励；没有请求或实现。 | [方法条目](../by-type/file-upload.md) |
| 解码 JWT 的用户标识和 API 地址不等于签名或权限缺陷 | 正文提到 URL 解码后的 customer ID、UUID 与 API base URL。 | [方法条目](../by-type/jwt.md) |
| 受理、确认署名、严重度和奖励是独立记录 | 图片显示 P5/Unresolved 报告，以及 MSRC 更新署名资料、计划发布 acknowledgement、关闭案件并把奖金问题转给另一团队。 | [方法条目](../reporting.md) |
| 客户端配置、受限 access_key 和外部存储凭据须按消费者区分 | env-config.js 图片可见 window._env_、BACKEND_URL、被遮挡的 AUTH0 字段和 IS_PROD，但无完整值或权限。 | [方法条目](../by-type/info-secrets.md) |
| URL 百分号与 HTML 实体解码链应追到实际导航消费者 | 两个同文帖分别保存 PNG/JPEG，地址栏可见包含 `%26%2302` 与 `%26%23115` 的 javascript 变形，浏览器弹窗出现，origin 被遮挡。 | [方法条目](../by-type/xss.md) |
| 邮箱情报工具的命中标签不证明账号归属或有效泄露 | zehef 图片输出 suspicious、breached、Pastebin 链接、possible accounts 和多次重复的示例社交账号。 | [方法条目](../discovery/passive-and-services.md) |
| 多行求值放大的延迟不能只用总耗时归因 | 正文把空 bit 字面量的转换与 13 行各 sleep(5) 解释为约 66 秒；图片仅两次同条件 curl 总耗时，缺数据库方言、实际行数与 false/control 对照。 | [方法条目](../by-type/sql-injection.md) |
| 证书名称匹配应在 IDN 规范化后遵守通配边界 | curl 历史报告 CVE-2023-28321 描述 built-in TLS 名称匹配器对转换成 `xn--` 的 IDN 接受部分 wildcard，如 `x*`，而这种模式应拒绝。 | [方法条目](../discovery/client-and-cloud.md) |
| 复用网络句柄时方法与请求体来源要一起重置 | libcurl 历史 CVE-2023-28322 描述 HTTP/3 同一句柄先 PUT 使用 READFUNCTION，改 POST 并设 POSTFIELDS 后仍错误调用旧读回调，可能发错数据或使用失效内存。 | [方法条目](../discovery/client-and-cloud.md) |
| 错误路径引用已释放数据应追踪到展示消费者 | libcurl 历史 CVE-2023-28319 描述 SSH SHA256 指纹校验失败后先释放指纹，再在错误消息引用该内存，风险是堆数据被错误文本暴露。 | [方法条目](../discovery/client-and-cloud.md) |
| 多个注入占位符应明确变量对应与请求预算 | Turbo Intruder 图片只有 GET 路径和 TrackingID Cookie 的两个 `%s` 占位符，没有队列代码或输出。 | [方法条目](../targeted-fuzzing.md) |
| 登录页后 admin 返回 200 仍须证明未授权业务权限 | 正文称从登录页切换到 admin 得到面板。 | [方法条目](../by-type/idor-access-control.md) |
| 响应延迟检测器的 Vulnerable 输出仍需可解释的对照 | Fortigate 检测介绍宣称用响应方式安全识别 CVE，图片只有 example.com:10443 和 Vulnerable 输出，没有代码、原始响应或时间样本。 | [方法条目](../experiment-design.md) |
| 资料字段、对象授权、脚本执行和钱包签名链条分别建模 | NFT 帖宣称 IDOR 与 XSS 导致钱包相关影响，图片只显示 nickname、mail、社交资料字段。 | [方法条目](../business-modeling.md) |
| 跨产品嵌入内容的存储与渲染应保持同一净化边界 | WordPress/Crowdsignal 历史图描述 poll answer 注入属性，share link 嵌入 WordPress post，再 View Results 触发脚本；含 pointer 事件与样式覆盖，不能写成零交互。 | [方法条目](../by-type/xss.md) |
| User-Agent 进入后台联系表单时须确认实际查看消费者 | 正文建议在 User-Agent 放置 blind XSS，候选边界是请求元数据进入日志、联系表单或后台页面时是否转成可执行 HTML。 | [方法条目](../by-type/xss.md) |
| 报告时间范围和聚合粒度决定成本约束 | 8x8 截图描述登录用户在 reports 中扩展 dateFrom/dateTo 后响应字节和延迟增大，同时存在时区、偏移与 timeInterval。 | [方法条目](../business-modeling.md) |
| 私有项目奖品邮件不授权公开发现内容 | 奖品邮件同时明确项目私有、发现内容严格保密并禁止公开披露。 | [方法条目](../scope-and-rules.md) |
| 批量评论是否越过业务配额须先定义被保护资源 | 正文用大量评论及缺少限流描述滥用。 | [方法条目](../by-type/business-logic.md) |
| 影响分析要形成小而可复核的问题和及时证据 | 正文建议深入理解低等级或重复发现，并围绕认证、令牌提出问题。 | [方法条目](../reporting.md) |
| 未验证邮箱占位、身份合并与账号阻断须按生命周期验证 | 正文讨论阻止 Google 账号注册，图片仅有 person JSON、测试邮箱、active=true、Renter 等字段，缺少注册请求、邮件验证和最终恢复状态。 | [方法条目](../by-type/authn-session.md) |
| 代码仓库中的 Jira token 应按实际 API 能力解释 full access | inDrive 历史截图显示 GitHub 中常量文件含 Jira host/base URL 和被遮挡 token，摘要说可能读取 projects、tasks、comments 等信息，标题 full access。 | [方法条目](../by-type/info-secrets.md) |
| 订单接受必须由被要求确认的角色授权 | inDrive 历史图描述司机由 driverrequest 得到 tenderID/orderID，再对 setTenderStatus 操作，使乘客订单被接受并可强制价格；摘要提到 PII 和协商流程。 | [方法条目](../by-type/business-logic.md) |
| 日志字段净化必须覆盖请求方法及最终终端消费者 | Rack common logger 历史图说明 query string 已正确处理，但 request method 原样记录；含退格表示的请求导致 Rack::Lint 相关错误，归档为 CVE-2022-30123。 | [方法条目](../discovery/records-and-incremental.md) |
| 订单 ID 除对象授权外还需检查类型与输出上下文 | 正文提醒数字形态 order ID 也可能进入 XSS。 | [方法条目](../by-type/xss.md) |
| 根路径 403 不代表所有路由相同权限 | 正文对照根路径 403 与 `/state` 的 200。 | [方法条目](../discovery/web-and-api.md) |

| ISAPI 导出与 DLL 生命周期只是调用链的入口 | MOVEit 逆向图片区分扩展导出 `GetExtensionVersion`、`HttpExtensionProc`、`TerminateExtension` 与过滤器导出 `GetFilterVersion`、`HttpFilterProc`，并显示 `DllMain` 的进程/线程附加和分离分支。 | [方法条目](../source-audit.md) |
| 范围变更记录必须同时保留日期、动作与奖励资格 | 历史范围图中的 added、removed 与 eligible_for_bounty 为独立字段：新增资产不必有奖，移除资产也不能作为现行测试许可。 | [方法条目](../scope-and-rules.md) |
| 跳转参数候选要追到 URL 规范化后的导航位置 | 参数清单混合 returnTo、redirect_to、state、image、file、host 等名称，其中很多并非跳转消费者。 | [方法条目](../by-type/open-redirect.md) |
| IPv4 变体必须比较校验器与连接器的实际解析 | 图片列出十六进制、八进制、整数、短分段和百分号混合的 IPv4 表示，示例是公共地址，不是内网访问证明。 | [方法条目](../by-type/ssrf.md) |
| 第三方搜索和 Dork 界面只产生有归属边界的候选 | 保存材料列出 npm、Trello、S3、配置、备份、日志等搜索方向及按漏洞/文件类型生成查询的界面。 | [方法条目](../discovery/passive-and-services.md) |
| innerHTML 与未编码反射需要补齐不可信源和解析上下文 | `innerHTML` 或 kxss 所标记的未编码字符提供审计方向，漏洞需要不可信输入实际抵达该消费者并进入可执行上下文。 | [方法条目](../by-type/xss.md) |
| 路径字典工具输出仍要绑定真实文件消费者 | pathbuster 的 URLs、payloads、wordlist 等输入描述候选路径生成与测试阶段，未保存实际服务器文件响应。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Shodan 元数据查询应保持字段和端口分隔符 | 正文与图片用 org/favicon 等索引字段寻找内存转储线索，命令还存在端口选项缺少分隔与 awk 拼接 IP/port 未加冒号的问题。 | [方法条目](../discovery/passive-and-services.md) |
| 时间序列和工具检测应以真假条件及会话状态归因 | 路径上的 sleep 候选、15/10/2/1 秒耗时图与 email 参数的 10/20 秒图共同提示时间差可能与输入有关。 | [方法条目](../by-type/sql-injection.md) |
| 学习路线和少量工具应落实到可解释的实验 | 路线图覆盖计算机、网络、HTTP/DNS、认证、操作系统、语言与练习材料；正文建议理解技术、适应方法并检查登录后功能及多层域名。 | [方法条目](../hunting-strategy.md) |
| 应用商店评价进入第三方后台时要分开内容与资产授权 | 正文建议评价内容可能进入客服或第三方页面。 | [方法条目](../by-type/xss.md) |
| 双引号 JavaScript 上下文的运算符效果依赖完整语法 | 图片在 script 内展示双引号字符串输入与百分号/空串/alert 运算组合。 | [方法条目](../by-type/xss.md) |
| 上传后的保存、提供下载与服务端解释执行分开验证 | 正文从 HTML/ASPX 上传延伸到 shell 与 whoami，但没有保存完整运行证据。 | [方法条目](../by-type/file-upload.md) |
| 历史重置链接和重复使用要按令牌生命周期验证 | Wayback 中出现重置 URL 只是历史线索，是否能重复消费取决于令牌归属、用途、时效、成功后失效和撤销策略。 | [方法条目](../by-type/authn-session.md) |
| MOVEit 和 Citrix 索引指纹不能替代版本与漏洞证据 | human.aspx、Citrix logout、服务 title 与 favicon 查询给出产品线索；Google 约 2890 结果及 Hunter.how 的 Past year 10736 服务/1.9K IP 都是历史索引统计。 | [方法条目](../discovery/passive-and-services.md) |
| CDN 标签与所谓 Real IP 都需要独立的源站关联证据 | cdncheck 图把结果标为 CDN、cloud 或 WAF；CrimeFlare 图把 Cloudflare 地址和所谓 Real IP、反向主机名、组织、地理信息并列。 | [方法条目](../discovery/passive-and-services.md) |
| 静态 href/src 提取要记录解析遗漏和基准 URL | 正文用 curl/sed 提取链接，正则匹配可能遗漏引号变化、相对路径、HTML 实体、base 元素和动态脚本产生的 URL。 | [方法条目](../discovery/records-and-incremental.md) |
| Blind XSS 通知与脚本到权限链要逐层绑定证据 | 正文含联系表单、请求参数与外部脚本的 blind XSS 想法，还建议读取 Cookie/localStorage；图片只有部分报告状态和通知。 | [方法条目](../by-type/xss.md) |
| Waymore 多源归档要保存分页、时间和失败分母 | 保存图介绍 Waymore 的历史来源和筛选；历史 URL 发现与当前服务可达性是不同结论。 | [方法条目](../discovery/records-and-incremental.md) |
| 证书透明度订阅只提示名称和证书变化 | 图中 Meta CT 邮件订阅界面展示域名与通知设置，未显示当前证书或部署结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 范围外报告被接受的个例不构成测试许可 | 截图中运营方称范围外问题已复现并给出例外奖励。 | [方法条目](../scope-and-rules.md) |
| DiffieHellman 设置私钥后的 generateKeys 需要辨明状态语义 | Node 示例设置明确私钥后调用 generateKeys，图中再次读私钥仍为相同值。 | [方法条目](../source-audit.md) |
| BCheck 的语法、匹配和实际权限要分别验证 | 图中 BCheck v1 beta 用响应包含原始 XSS 字符串报 certain/medium，另例用 Cisco 命令输出 marker 与 200 报 high；同时保存的 Nuclei 终端不是 BCheck 解析或效果验证。 | [方法条目](../targeted-fuzzing.md) |
| 厂商复现反馈要保留版本和调查阶段 | Apple 邮件涉及分开发送问题、补充编号、在当时设备/iOS 版本复测及调查过程中保密。 | [方法条目](../reporting.md) |
| 隐藏参数和相近路由仍需分别确认输出消费者 | 一图显示 product 参数的事件输入产生弹窗，另一图显示隐藏 tab 参数到关闭 script 的构造。 | [方法条目](../by-type/xss.md) |
| 路径大小写差异应检查路由与解释器映射 | 正文称 `/index.php` 渲染，而 `/index.PHP` 暴露源码并关联数据库配置。 | [方法条目](../source-audit.md) |
| Nuclei 目标数和版本警告不是漏洞覆盖分母 | 保存输出含旧版本、模板版本、弃用语法/重复模板告警、7 个候选目标与 6 个 URL、数条 XSS 命中及另图的大批目标加载数字。 | [方法条目](../targeted-fuzzing.md) |
| 自动化仪表盘必须能回链运行与阶段产物 | VulnVision 的 running 行、34 完成/0 运行统计和技术分布，与 Osmedeus 15 小时仍 running、资产/DNS/漏洞计数都是摘要。 | [方法条目](../discovery/records-and-incremental.md) |
| 日志目录与仓库关键字只说明秘密的候选位置 | 日志目录图显示时间与文件名，没有实际日志内容；GitHub 查询例覆盖配置、语言、文件名、历史、key 与用户名/邮箱。 | [方法条目](../by-type/info-secrets.md) |
| 客户端模板算术与服务端模板执行分开归因 | 保存浏览器图显示 3*3→9、5*3→15 及 Angular 相关载荷与弹窗。 | [方法条目](../by-type/ssti.md) |
| 枚举和弱密码候选要与受保护访问结果分开 | 正文讨论详细登录错误、默认凭据与管理员资料；Nagios 图只显示 Basic 登录框，VulnVision 图只显示弱密码模板和含凭证的请求。 | [方法条目](../by-type/authn-session.md) |
| JSON 端点的路由和 MIME 变化决定实际解析器 | 正文描述给 JSON 路由追加 `.html` 或改变参数，及 JSON 内容被以 text/html 提供。 | [方法条目](../by-type/xss.md) |
| Citrix logout 的执行图不补齐响应拆分与 WAF 对照 | 几张不同 SHA 的图在 logout/post_logout_redirect_uri 中有多重换行及事件 HTML，浏览器出现弹窗。 | [方法条目](../by-type/xss.md) |
| 批量用户端点与不可猜标识仍必须执行对象授权 | 正文把 `/me` 改 `/users` 或 `/user`，GET 改 POST 并提交 ids 数组；实际一图只是 `/jobseekers/me` 带 Bearer 的当前用户 200 响应，另一图只有步骤。 | [方法条目](../by-type/idor-access-control.md) |
| AST 提取的未知表达式必须保留为未知 | jsluice 代码图用 tree-sitter 提取 location/open/fetch 的 URL、方法与查询字段；动态拼接部分保留 EXPR，占位符不是可直接请求的端点。 | [方法条目](../source-audit.md) |
| 自定义 AST 匹配器应先核对分支与声称的输出 | 保存规则在 key 包含 api 时 return nil，在值带 AUTH_ 前缀时也 return nil，却将 apiKey/AUTH_ 示例说成预期匹配；代码逻辑与主张相反。 | [方法条目](../by-type/info-secrets.md) |
| 重复状态与原报告评级需与修复事实分开 | 截图说明内部已知问题或同端点/参数重复，并有原报告不同评级与状态变化。 | [方法条目](../reporting.md) |
| 自建登录页面和 HTML 表单不证明跨身份脚本链 | 图片展示 login.php、admin.php、index.html 文件与登录表单，正文部分截断。 | [方法条目](../by-type/xss.md) |
| 敏感资料修改要核对验证后的服务器最终状态 | 正文建议关注设置、资料和手机号等字段，图仅有重复手机号相关的报告标题/状态。 | [方法条目](../by-type/authn-session.md) |
| 跳转到脚本协议的升级需独立确认每一步消费者 | 正文把 open redirect 延伸到 javascript://、编码换行与 reflected XSS。 | [方法条目](../by-type/open-redirect.md) |
| 持久 returnUrl 在合法 nonce 脚本内仍要检查字符串上下文 | 保存图和文字涉及商户离线交易/GraphQL 创建流程，returnUrl 跨两个站点保存后进入带 nonce 的合法 script。 | [方法条目](../by-type/xss.md) |
| 请求词表和多标签页测试要有格式与请求预算 | RapidHand 的多组旧 XSS 候选和 50 标签页/点击启用模式说明界面能力，未保存执行结果；Paraforge 把 localhost 登录请求拆为路径段和参数名。 | [方法条目](../targeted-fuzzing.md) |
| HTML 注释终结与表达式求值不能凭载荷外观判定 | 正文用 `--!>` 与 img/onerror 组合称为注释 XSS，但事件表达式只有 `(document.domain)`，没有弹窗函数。 | [方法条目](../by-type/xss.md) |
| 可重现、源码路径和奖励金额要分别说明影响 | 保存邮件有可重现但 informational 的处理；另一截图只显示已关闭 stored XSS 与金额。 | [方法条目](../impact-and-acceptance.md) |
| 非云 SSRF 要证明后台获取及受保护响应的使用 | 示意图把 URL 参数交给后台，再访问内部 admin 面板；正文“非云”文章仅提供方向。 | [方法条目](../by-type/ssrf.md) |
| RDP 暴露、主机元数据和权限影响分阶段判断 | 截图的端口/域名/主机名报告标为 P2 Resolved，未包含端口握手、认证、命令或跳板访问。 | [方法条目](../discovery/passive-and-services.md) |
| 移动 UA 和 UTF 编码变化要追踪真实响应与字符解释 | 正文指出移动 User-Agent 与 UTF-16 等编码可能改变用户名的展示路径。 | [方法条目](../by-type/xss.md) |
| 排列域名的工作流要区分环境层级与 DNS 命中 | Trickest 图按 test.dev.example.com→dev.example.com 等层级提取环境名，并串联 dSieve、alterx 和 puredns。 | [方法条目](../discovery/records-and-incremental.md) |
| 资产不可达时保留当时证据并说明当前复核限制 | 两图分别显示 env-config.js 报告 P3/Not applicable 和浏览器超时，未保存实际配置内容。 | [方法条目](../reporting.md) |
| Nginx alias 前缀替换要核对最终磁盘路径 | 配置示意对照 `location /img/` 与 `location /img` 的尾斜杠、同一 alias；本地终端用 attachments 前缀变体返回 identity.log，内容是 SQLite 错误、查询字段与栈。 | [方法条目](../by-type/lfi-path-traversal.md) |
| SQL 报错回显是输入路径线索而非数据库权限证明 | MySQL 错误页在随机字符串、普通 h1、script 和非标准元素包装之间显示不同反射/DOM 结果。 | [方法条目](../by-type/sql-injection.md) |
| 报错文本变成 h1 不等于脚本已执行 | 同一组图中普通 h1 被当成文本、script 从 DOM 消失，非标准元素/属性包装则让 h1 进入 DOM 并出现大标题。 | [方法条目](../by-type/xss.md) |
| 模型选择参数不能直接决定未约束的加载路径 | 内部 CWE 分类截图指出 request.version、request.trained_at 被直接插入路径，随后 AutoTokenizer.from_pretrained 读取 tokenizer。 | [方法条目](../by-type/ai-application.md) |
| 模型版本和训练日期字段也可能进入文件路径消费者 | CWE 分类接口 /predict/report_weakness_id 的历史报告描述 version/trained_at 路径拼接并由 tokenizer 加载。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 普通发布者不能自行完成管理员审批状态转换 | inDriver Job 摘要说明职位/简历创建编辑需管理员审批，技术片段指向最终 POST /api/graphql 的 UpdateVacancyStatus。 | [方法条目](../by-type/business-logic.md) |
| GraphQL mutation 的状态枚举必须由服务端角色守卫 | UpdateVacancyStatus 的名字暴露审批状态操作，但判断取决于调用身份、对象所有者、当前状态与目标状态是否在 resolver 中检查。 | [方法条目](../by-type/graphql.md) |
| 资料页面中的 encrypted password 先判断类型与可重放能力 | Newegg 截图描述资料编辑源码出现 encrypted password，改变邮箱本应提交密码。 | [方法条目](../by-type/info-secrets.md) |
| 重新认证要求不能由返回给客户端的密码表示满足 | 资料修改若要求原密码，服务端不应把一个已暴露的等价密码表示作为新的身份验证。 | [方法条目](../by-type/authn-session.md) |
| 邀请接受前的协作者数据要保持字段授权 | HackerOne 报告图描述 pending invitation 尚未接受，编辑协作者入口的请求已暴露被邀请人的私人邮箱。 | [方法条目](../by-type/idor-access-control.md) |
| GraphQL operationName 不能替代响应字段的授权检查 | SaveCollaboratorsMutation 名称关联邀请流程，但数据泄露要落在具体 resolver、返回字段和 pending 状态。 | [方法条目](../by-type/graphql.md) |
| 可信域错误页的文本欺骗应与 HTML 和脚本注入区分 | cryptography.io 报告描述在路径后追加文字，错误页以可信域上下文显示“网站迁移”的内容。 | [方法条目](../by-type/xss.md) |
| 安装说明外链的控制权变化属于供应链信任边界 | stripe/veneur 文档历史指向不再由项目控制的域，图称原侧栏已移除而部分 fork 保留；假设用户按外链安装源码/镜像，则受控文档到可执行产物之间存在信任风险。 | [方法条目](../source-audit.md) |
| 失控文档域与实际可取得域名控制是不同结论 | 保存报告说明旧安装文档链接离开项目控制，风险取决于其当时所有权和用户信任路径。 | [方法条目](../by-type/subdomain-takeover.md) |
| Self XSS 的升级必须新增跨身份输入或浏览器请求链 | 正文提出从 self XSS 延伸到账号破坏或 CSRF 到 reflected XSS，部分内容截断。 | [方法条目](../by-type/xss.md) |
| 启动器切换账号要重新证明当前关联身份 | Rockstar 官方历史摘要有三个必要前提：攻击者已访问受害者 Steam/Epic，已关联 Social Club，且账号拥有相应游戏。 | [方法条目](../by-type/desktop-client.md) |
| 联邦关联不应自动替代敏感切换的近期认证 | 启动器摘要说明仅有外部账号访问及关联即可进入另一个平台资料的历史问题，关键是目标身份的近期认证是否经过服务端验证。 | [方法条目](../by-type/authn-session.md) |
| 验证码是否约束操作取决于服务端验证与绑定 | 正文建议检验表单验证码。 | [方法条目](../by-type/business-logic.md) |
| 重复 Host 污染的 HTML 跳转还不是重置邮件投毒 | 两个帖的图显示 POST /passwords 重复 Host（第二值带 @ 前缀），返回 HTML 的重定向链接把域、逗号和 @ 域拼接到 /sessions/new。 | [方法条目](../by-type/host-header.md) |
| 手机号与邮箱字段的格式约束不代替输出编码 | 正文给出手机号、邮箱等输入位置启发。 | [方法条目](../by-type/xss.md) |
| FortiOS 路径探测的 200 需要文件内容与控制路径 | 两帖保存 httpx 1.3.1 outdated 的 fgt_lang 到 sslvpn_websession 路径和多个 200；未见响应正文、产品版本或对照。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 归档 URL 中的邮箱片段要区分历史公开索引和私密数据 | Wayback/Katana 加正则可提取看似邮箱的片段，图仅有 Users PII 报告状态。 | [方法条目](../by-type/info-secrets.md) |
| 代码搜索中的人员和组织匹配需保留各自查询语义 | GitHub 图片涉及 user、org、登录名、姓名、邮箱与代码语言等查询；每个字段含义和检索对象不同，同名、子串、样例邮箱或转载都可能误关联。 | [方法条目](../discovery/passive-and-services.md) |
| 模板命中与对应 Citrix 弹窗要保留同一请求关联 | 两组 Nuclei 摘要和 Citrix 浏览器图可支持提出同一端点的解析/执行问题，但摘要到浏览器之间缺完整标记、时间和请求响应关系。 | [方法条目](../by-type/xss.md) |
| WAF 绕过主张要保留拦截对照和实际执行两种证据 | Citrix logout 图的输入与浏览器弹窗仅显示一个执行现象，Akamai 标题不能证明防护当时开启、规则版本或所有路径都被绕过。 | [方法条目](../by-type/waf-bypass.md) |

| FreeMarker 类加载链仍取决于模板对象和沙箱暴露 | 归档示例由模板可达对象的 class/protectionDomain/classLoader 继续获取包装器与执行类，并配有类似 passwd 的输出。 | [方法条目](../by-type/ssti.md) |
| 运营者确认、待部署和复测通过分别记录 | 三组保存邮件涉及 2FA、SQL 注入、登录/重置路径：确认问题、准备修复、修复完成但待部署或将再次验证是不同阶段。 | [方法条目](../reporting.md) |
| 编码与嵌套标记穿过过滤器需同时核对浏览器解析 | 一帖列举 IMG SRC/A href 编码候选且最终 Informative/No Rating；另一帖保存 MathML、表格、mglyph/style/CDATA 与编码字符交错的变异候选。 | [方法条目](../by-type/waf-bypass.md) |
| 永久封禁状态要覆盖协作邀请与报告入口 | 保存帖描述新账号或沙箱报告邀请已封禁用户的替代入口。 | [方法条目](../by-type/idor-access-control.md) |
| 身份状态和邮箱验证令牌应绑定最终使用的身份属性 | 封禁后的重置入口、先请求旧邮箱令牌再改为另一邮箱后使用旧链接，以及登录清单共同指向状态使用时的绑定。 | [方法条目](../by-type/authn-session.md) |
| WordPress 嵌入消息的 origin 与实际接收端一起核对 | 保存案例指出恶意博客须被嵌入，wp-embed 的 postMessage origin 检查存在问题，并明确 Safari 与 Chrome/Firefox 表现不同。 | [方法条目](../by-type/xss.md) |
| MetaMask 深链触发下载与写入执行分开证明 | 归档描述深链打开钱包内置浏览器后，攻击页能立即发起下载且缺确认。 | [方法条目](../by-type/mobile-android.md) |
| 参数分析和 JavaScript 发现输出保留推断层级 | 保存介绍涉及参数解码、疑似哈希类型、反射检测、JavaScript 链接/词表与 DOM 扫描。 | [方法条目](../discovery/web-and-api.md) |
| Ghost 静态资源路径穿越需区分主题文件与服务端任意文件 | 保存两次编码路径请求返回 200，并在浏览器显示主题 package.json。 | [方法条目](../by-type/lfi-path-traversal.md) |
| POST 和文档 base 的候选要落到具体浏览器消费者 | POST 参数也可经表单或脚本发送；参数不在地址栏不构成安全保证。 | [方法条目](../by-type/xss.md) |
| 转发头中的延迟候选需要请求级真假条件对照 | 图片中向 administrator 路径的 X-Forwarded-For 放入 SQL 延迟条件，两次 302 和耗时差异只支持延迟候选。 | [方法条目](../by-type/sql-injection.md) |
| 搜索语法和 ASN 条件不能替代资产归属及授权 | 归档保留 Shodan 字段清单、Google 搜索思维导图和 ASN 搜索片段。 | [方法条目](../discovery/passive-and-services.md) |
| 第三方和范围外报告的协作不扩展测试许可 | 保存处理意见涉及第三方/OOS、运营者可能转交或协调，以及某奖励邮件对公开内容的限制。 | [方法条目](../scope-and-rules.md) |
| 邮箱输入延迟与工具库名需要分别保存原始对照 | 图中邮箱候选出现约二十秒等待及 fatal/空白响应，另一图显示 Ghauri 请求计数与数据库名。 | [方法条目](../by-type/sql-injection.md) |
| 修复验证应比较漏洞判据而非错误页面样式 | 归档用报错与空白页面描述 SQL 修复后的变化。 | [方法条目](../reporting.md) |
| GitLab CLI 分支名进入 Windows URL 启动器的解释边界 | 保存示例把特殊字符分支名经 glab mr create --web 带入 cmd.exe/c start 的 URL 参数。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 开发工具打开网页也需视远程仓库元数据为不可信 | 远程仓库默认分支可进入本地 CLI 打开网页流程；导航操作若穿过命令解释器，仓库字段就可能跨越本地执行边界。 | [方法条目](../by-type/desktop-client.md) |
| 依赖混淆须证明解析来源与生命周期脚本的实际消费者 | 保存截图涉及内部依赖名从公共 npm 源获取并由 preinstall 回调报告构建/开发环境。 | [方法条目](../source-audit.md) |
| source 历史记录和目录 rm 命令不等于便捷单步操作 | 两帖把 source ~/.bash_history 与 sudo rm -fr ./* 写成快捷操作或语言包删除。 | [方法条目](../source-audit.md) |
| SQLite 条件溢出候选的前提来自表达式本身 | 保存 CASE 表达式在一个分支调用最小有符号整数的 abs，利用可能的整数溢出差异作为布尔候选。 | [方法条目](../by-type/sql-injection.md) |
| 历史构建清单和扫描标签分别核对当前路由与权限 | Wayback 的 buildManifest、旧目标更新后的目录列表和 Plution 本地多解析器面板提供发现线索。 | [方法条目](../discovery/web-and-api.md) |
| 二次查询拼接不会因第一次使用 prepare 而安全 | 保存 PHP 片段先以 prepare/bind 写入或读取 note，再将数据库取出的值拼接到后续 SQL。 | [方法条目](../by-type/sql-injection.md) |
| 源码函数名单要匹配语言、分支和真实数据流 | 第二阶 SQL 代码与所谓 JavaScript 搜索图共同说明：危险调用只有在不可信值跨入相应解释上下文才构成漏洞。 | [方法条目](../source-audit.md) |
| JavaScript 配置和产品文件按实际权限而非字段名定性 | 归档出现 Algolia appID/key/indexName、Firebase 配置模式、JS 文件中的凭据搜索与 phpMyAdmin ChangeLog。 | [方法条目](../by-type/info-secrets.md) |
| 注册角色字段要由服务端允许列表决定 | 保存帖指出历史 Ultimate Member 注册字段 Wp_capabilities[administrator]=1 可能影响角色，并附小于 2.6.4 的历史条件。 | [方法条目](../by-type/idor-access-control.md) |
| 上传后的 OAST 回调不能单独证明命令执行 | 帖称文件上传后发现盲 RCE，图中只有 Collaborator DNS/HTTP 事件。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Rails SVG 净化候选保留显式标签配置和嵌套解码条件 | 保存材料涉及 ActionView sanitize 在允许 SVG/use 标签或指定 tags 的条件下处理嵌套 data/Base64 SVG 与事件属性。 | [方法条目](../by-type/xss.md) |
| 反射位置和 pointer 交互决定 XSS 最小复现 | 保存 8x8 oem 候选在 img 属性中使用 onpointermove，多个请求位置不代表每处都能执行。 | [方法条目](../by-type/xss.md) |
| Rocket.Chat 下载接口到文件写入执行之间仍有独立门槛 | 归档说明历史下载路径穿越并提到可经文件写入进一步 RCE，明确需要已认证用户，且披露前已修复多年。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Cloudflare 背后地址候选要绑定发现时间与应用关系 | 已保存 CrimeFlare 图片把 Cloudflare 与所谓真实地址并列，正文只有工具介绍。 | [方法条目](../discovery/passive-and-services.md) |
| 发现管道的输入配置、错误和输出来源是覆盖证据 | TLS passthrough、Piper/JSluice、ScopeHunter、CT 扩展与 GAP 输出记录的对象不同：透传域名不产生解密 HTTP 证据；JS 文件名不保证响应是 JavaScript，404/HTML 与 200/script 应分开；字符串提取缺 method 时不能默认为 GET。 | [方法条目](../discovery/records-and-incremental.md) |
| TLS 透传配置与流量缺失需按传输层区分 | 图中五个域名的 TLS passthrough 正则表示可能绕过解密过程。 | [方法条目](../discovery/records-and-incremental.md) |
| 草稿批量提交需比较容量限制与提交时原子校验 | 保存帖称创建很多草稿后并发提交可越过历史 500 草稿上限。 | [方法条目](../by-type/business-logic.md) |
| 备份后缀暴露 PHP 源码需按响应字节和密钥可见性证明 | 图中 common/config.php.new 返回 200/text/html，但正文可见未解释的 PHP 配置语法及遮挡字段。 | [方法条目](../by-type/info-secrets.md) |
| FTP、WHOIS、DNS、favicon 与 CT 提供不同的被动关联 | 保存 FTP 文字、Meta WHOIS 归属搜索、DNS resolver 示意、favicon 统计和 crt.sh 查询都可用于候选关联，但证据类型须明确。 | [方法条目](../discovery/passive-and-services.md) |
| 登录频控按身份、来源和时间窗保存判据 | 归档称大量尝试后未限制且最终 Duplicate；另两张图只给出 Nextcloud 速率限制标题。 | [方法条目](../by-type/authn-session.md) |
| GIF 调色板未初始化的泄露链取决于解码库和进程数据 | 归档描述 ImageMagick 7.0.6-1/GraphicsMagick 1.3.26 的 ReadGIFImage 在缺全局/局部调色板时可能使用未初始化内存，并经图像颜色外显。 | [方法条目](../source-audit.md) |
| 内部资产描述在 CSV 导出中仍须执行字段级授权 | 保存报告指出私有资产描述在范围 UI 中隐藏，但可由 CSV 导出看到。 | [方法条目](../by-type/idor-access-control.md) |
| 远程 XSS 候选清单与实际命中分开记录 | Dalfox 引入 PortSwigger 候选载荷说明的是输入来源，需保存清单版本、下载来源、编码与去重方式，再按目标上下文和明确预算筛选。 | [方法条目](../targeted-fuzzing.md) |
| SQLMap 从历史 session 恢复的结果不能当当前请求证明 | 保存图明确显示 resumed stored session，数据库与表名列表只是工具保存结果的一部分。 | [方法条目](../by-type/sql-injection.md) |
| 影响链条的每一段分别证明权限、交互与消费者 | 帖列 SSRF→RCE、Self-XSS→点击劫持/CSRF、信息泄露→提权等组合方向，另一图仅显示 High→Critical。 | [方法条目](../impact-and-acceptance.md) |
| 复现协作与评级变化按确认范围记录 | SQLMap 缓存和 Critical 评级邮件不能代替完整步骤。 | [方法条目](../reporting.md) |
| 敏感操作 CSRF 需由真实浏览器证明凭据和最终状态 | 保存帖讨论邮箱/密码修改、缺 Origin 时被接受及移动页面候选。 | [方法条目](../by-type/csrf.md) |
| JavaScript 提取的 URL 应保留来源响应与未知请求属性 | Piper 的处理输出既有 script 类型成功响应，也有 JavaScript 文件名下的 404/HTML；JSluice 提取相对 URL 且 method/query/body 为空。 | [方法条目](../discovery/records-and-incremental.md) |
| Airflow Spark JDBC 的本地文件条件属于连接客户端 | 保存历史案例涉及 Spark Provider 4.0.0、4.0.1 前的连接字段/schema 过滤及恶意 MySQL 服务端请求本地文件。 | [方法条目](../by-type/lfi-path-traversal.md) |
| SpEL 的类型解析和文件 API 链需要表达式语法先成立 | 保存字符串企图通过类型解析器访问 Base64/FileUtils 并读取文件；帖子 URL 自动格式化使类型名破损，文件 API 的参数/重载也需对应具体版本。 | [方法条目](../by-type/ssti.md) |
| Kubelet 调试端点取决于配置和实际暴露面 | 保存文字与图涉及历史 health/debug/pprof 接口、可能内存信息和有限资源耗尽，且明确不是所有默认配置都会暴露。 | [方法条目](../cloud/container-k8s-security.md) |
| Host 反射、重定向和密码重置消费者分别建立证据 | 保存帖提出以 Host 影响重置 URL，Python 示例仅在 200 正文或 301/302 响应头匹配 marker。 | [方法条目](../by-type/host-header.md) |
| 自定义自动化和输入清单的价值应由覆盖与证据衡量 | 归档称自定义方法发现很多问题，另有学习清单和未测试教程的玩笑。 | [方法条目](../hunting-strategy.md) |
| 未验证企业邮箱不得直接转换为组织信任 | 保存帖称可输入尚未验证的公司邮箱获得特殊权限。 | [方法条目](../by-type/authn-session.md) |
| 组织属性的展示与实际租户权限分别比较 | 邮件域显示、组织标签与服务端租户成员关系不是同一事实。 | [方法条目](../by-type/idor-access-control.md) |
| Cisco 客户端页面 XSS 保留配置和点击条件 | 历史 ASA/FTD 材料涉及特定 AnyConnect/WebVPN 服务配置以及用户点击。 | [方法条目](../by-type/xss.md) |
| WHOIS 品牌关联只能作为资产关系候选 | 保存 Meta WHOIS 管理员组织检索和所谓大量域名提示信息聚合方向。 | [方法条目](../discovery/passive-and-services.md) |
| DNS resolver 回调示意尚未证明缓存投毒 | 图示由自有邮箱注册触发 Web 应用解析 MX，再由 resolver 请求回调收集器；即使看到查询也只说明一次解析路径。 | [方法条目](../discovery/passive-and-services.md) |
| favicon 索引数量依赖指纹算法和工具输出格式 | 保存 httpx/favicon→anew→awk→Shodan count 管道把输出最后数值作为查询输入。 | [方法条目](../discovery/passive-and-services.md) |
| XSS 回连里的存储数据仍需源、身份和权限消费者 | 图片显示一条回连 URI、Cookie/Referer/UA/Origin 字段、遮挡的 session/localStorage/DOM 与邮件数据标签。 | [方法条目](../by-type/xss.md) |
| ColdFusion 外部管理员限制和公用工具输出分开判断 | 图中 CFIDE utility/WDDX 返回遮挡 hash，另一图只有 Rapid7 历史文章开头称限制 Administrator 外部访问的功能存在绕过。 | [方法条目](../by-type/idor-access-control.md) |
| 披露金额的许可不能自动扩展为公开漏洞细节 | 保存奖励邮件允许公布金额，但 weakness 信息需运营者明确许可。 | [方法条目](../scope-and-rules.md) |
| CT SQL LIKE 的单字符替换会改变候选集合 | 保存帖子用下划线替换百分号处理 crt.sh 查询。 | [方法条目](../discovery/passive-and-services.md) |
| 重复 filename 的校验与写入解析应使用同一结果 | 两帖提到 filename 参数污染的 first/last/array 差异。 | [方法条目](../by-type/file-upload.md) |
| CT 到子域扩展的管道保留原始范围与中间失败 | crt.sh/org 查询→域名解析→去重→子域工具的串联需要保留每阶段输入、输出、时间、错误和根域来源。 | [方法条目](../discovery/records-and-incremental.md) |
| 证书域名扩展先正确处理端口、SNI 和有限迭代 | 保存 awk/openssl/httpx/anew 管道把 URL 以冒号拆开后强拼 443，可能丢显式端口、IPv6、路径信息；未设置 SNI、超时十秒且错误静默会误判证书集合。 | [方法条目](../discovery/records-and-incremental.md) |
| GAP 完成率只覆盖已选择的解析输入与维度 | 界面显示参数50、链接1201、词6703，选中 query/body/multipart、响应链接和部分路径/词变换，JSON/cookies/XML 等未选，来源标签及仅范围内选项未选。 | [方法条目](../discovery/records-and-incremental.md) |
| CSP 静态评价与实际浏览器注入结果分别保存 | 已保存 CSP evaluator 图示含 self、允许站点/img 范围，以及 object-src/TrustedTypes 提示。 | [方法条目](../by-type/xss.md) |
| MathML 与 HTML 混合候选需证明净化后的变异过程 | 保存字符串将 MathML/mtext、table/mglyph/style、CDATA 和 img/title 的实体/制表符交错。 | [方法条目](../by-type/xss.md) |
| 重定向列表中的 New 和 Triaged 不代表最终接受或修复 | 图中四条 Indeed Open Redirect，P4，分别 New/Triaged，均仍评估且具体路径遮挡。 | [方法条目](../reporting.md) |
| 收银系统会话握手阶段也需绑定客户和对象 | Unikrn 平台总结指出 transaction-history 的 session handshake 曾能访问另一客户数据。 | [方法条目](../by-type/idor-access-control.md) |

| 订阅后端授权按每次连接和具体权益核对 | Nord Security 平台总结确认某订阅检查后端曾允许无有效订阅连接 VPN，但每次连接仍须重复步骤，不是永久终身访问，也不影响其他用户的机密性/完整性。 | [方法条目](../by-type/business-logic.md) |
| COM 和 RPC 提权截图保留原有令牌能力 | GodPotato 图先显示服务身份与已启用 SeImpersonatePrivilege，随后 COM/RPC、命名管道与令牌搜索输出 SYSTEM。 | [方法条目](../by-type/desktop-client.md) |
| 发现任务的完成标志只说明所选输入和阶段 | GAP 的 Links 清单、Web-Check 仪表盘、历史 JSON URL 管道、Nuclei 模板合集和 SubSnipe 阶段分别处理不同输入。 | [方法条目](../discovery/records-and-incremental.md) |
| 品牌题名、证书和 CSP 的资产关联分别留证 | 保存材料以产品题名、证书组织名、版权页脚、ASN/网络页面、搜索扩展名、服务 banner 与 CSP 来源发现候选。 | [方法条目](../discovery/passive-and-services.md) |
| 默认凭据介绍必须与真实登录和身份结果分开 | WoodWing Studio 的历史题名与默认用户名密码只提供配置候选，管理界面和批量状态图没有保存登录请求、会话或受保护操作。 | [方法条目](../by-type/authn-session.md) |
| Git 当前文件删除不撤销旧提交中的秘密 | 同帖 Git 目录索引显示 HEAD/FETCH_HEAD/ORIG_HEAD 等，另一信息图说明提交后删文件仍可能保留旧可达提交。 | [方法条目](../by-type/info-secrets.md) |
| 当前密码和重置令牌的频控要落到关键消费者 | 删除账号时当前密码字段缺频控，仍需先有有效凭据；错误密码本身不等于能够删除账号。 | [方法条目](../by-type/authn-session.md) |
| 已有账号控制和源站定位按实际前提解释影响 | 保存运营者将某删除账号频控报告按 low 处理，原因是需要有效凭据且账号已被控制；不能以无次数限制直接宣称无交互删除任意账号。 | [方法条目](../impact-and-acceptance.md) |
| SendGrid 前缀和客户端 key 的权限消费者另证 | 保存正文以 SG 前缀识别 SendGrid key，并展示查询 scopes 的 HTTP 命令；前缀、mobile/JS 来源、标题或 Critical 评级都不证明密钥有效、权限范围或可发送邮件。 | [方法条目](../by-type/info-secrets.md) |
| 数字节点和 id 正则仅筛候选对象引用 | 保存 Drupal /node/数字路由、少用功能泄露主张、自动 IDOR 工具与 Burp id 正则提供候选发现方向。 | [方法条目](../by-type/idor-access-control.md) |
| 并发 gate 的完成不证明成员配额被突破 | 组织最多四成员的正文及 Turbo Intruder gate 示例说明同时释放请求尾字节的候选实验。 | [方法条目](../by-type/business-logic.md) |
| Popover 的 hidden 与 meta 路径依赖属性和目标选择 | 保存四图展示 button popovertarget、popover/onbeforetoggle 与 hidden input/meta/重复 id。 | [方法条目](../by-type/xss.md) |
| robots 的 Disallow 是发现线索而非访问守卫 | Teleport 报告图片列出公开 robots 路径，状态 Informative/None。 | [方法条目](../discovery/web-and-api.md) |
| CFIDE hash 响应与管理员访问控制分别比较 | 图片中 wizard utils.cfc 的工具方法返回遮挡 hash，但缺完整权限身份、版本和受保护管理员操作；CVE 标题/P1 Triaged 同样不是权限证明。 | [方法条目](../by-type/idor-access-control.md) |
| RDoc 生成 HTML 的文本转义和链接协议分别检查 | 保存 RDoc 段落输入生成未转义 script、链接输入生成 javascript href，以及 gen_url 根据 scheme/图像后缀拼接 img/a 的部分源码。 | [方法条目](../by-type/xss.md) |
| 生成器预处理代码的历史验收政策保留适用对象 | RDoc 保存回复明确说明当时政策不把预处理 Ruby 代码当安全漏洞，而按普通 bug 处理，报告 Informative。 | [方法条目](../scope-and-rules.md) |
| 生成器拼接和反序列化崩溃要追到完整数据流 | RDoc 的部分 URL 拼接源码需继续追踪上下文编码和实际 HTML 消费；Ruby 3.2.2/ASan/Marshal.load 的说明则缺附件及诊断栈，运营者认为普通 GC bug。 | [方法条目](../source-audit.md) |
| 重复范围更新正文仍逐图保留动作类型与奖励标记 | Adobe、Fidelity 与 Zebra 的同正文多 ID 对应不同历史范围图。 | [方法条目](../scope-and-rules.md) |
| Werkzeug 客户端错位链需要浏览器同连接后续请求 | 历史图将 Werkzeug 2.1.0–2.1.1 的请求解析与连接复用串到客户端 desync，再让后续 script 资源得到另一个响应。 | [方法条目](../by-type/request-smuggling.md) |
| Unicode 和绝对 URI 跳转比较最终解析的主机 | 正文包含 U+3002 句点和破损的全角字符编码，图片说明 Werkzeug 的 scheme/netloc 解析与绝对 URI 请求可改变跳转目的地。 | [方法条目](../by-type/open-redirect.md) |
| 重定向正文和 200 变体仍按同对象守卫比较 | 302/301 页面正文可能保留业务数据，跳转状态不代替权限；X-Original-URL、大小写、分号、编码点和后缀清单则需追踪代理/应用规范化后的同一对象。 | [方法条目](../by-type/idor-access-control.md) |
| 受理、待补影响、接受未修复和历史披露分别记录 | 保存邮件包括 accepted/fixed 的运营者声明、Needs more info 的影响请求、评级改变后 Pending program review，以及 Unresolved 页面明确说明 accepted valid。 | [方法条目](../reporting.md) |
| IP 编码工具仍需验证校验器和连接器是否一致 | 保存 Burp-Encode-IP 介绍只说明生成多种表示形式，未保存具体转换或请求。 | [方法条目](../by-type/ssrf.md) |
| 邮箱规范化冲突以真实身份和业务状态为准 | 正文声称大小写变体造成账号删除/验证冲突，图中 HTTP 200 却同时出现 authentication SUCCESS 和业务 statusCode 409，未保存 JWT 与完整身份请求。 | [方法条目](../by-type/authn-session.md) |
| 旧项目与接口优先级由覆盖和反馈决定 | 旧发现复查、后台/API 入口、少用功能与自动化都应变成范围内假设，保存每次输入、配置、失败/跳过与受保护结果。 | [方法条目](../hunting-strategy.md) |
| 生物识别代际变化的解锁状态应按保险库绑定 | Bitwarden 历史报告已在 Android 验证，iOS 仅推测：主保险库的生物识别变化后应强制重认证，解锁第二保险库再切回却可能改变主库解锁状态。 | [方法条目](../by-type/mobile-android.md) |
| 多账号客户端切换不能继承另一账号的重认证结果 | 生物识别变化后的主账号需重认证，第二账号解锁产生的状态不能无条件用于主账号。 | [方法条目](../by-type/authn-session.md) |
| WebSocket REPL 先重建合法握手再比较消息权限 | 图示从 Burp /socket 握手的 Copy as curl 转到 wsrepl，并收到 metadata/new_finalized 订阅消息。 | [方法条目](../by-type/websocket.md) |
| 工具改写流量时保留改写前后和连接来源 | WebSocket 的 curl→REPL 与正文提到 MiTMProxy pre-proxy 是不同转换步骤。 | [方法条目](../discovery/records-and-incremental.md) |
| JSON 错误字段与部署测试资源追到实际 HTML 输出 | Keycloak 注册错误将 JSON 字段名带入 ClientRepresentation 错误页面，另图显示 vendor/curl 测试路径的返回字段与弹窗。 | [方法条目](../by-type/xss.md) |
| 长度门槛、POST 搜索和请求头输入都需要查询判据 | SSN 帖把四位前缀与 XOR/延迟候选组合，一图单次约 9.6 秒；另有 POST 搜索、User-Agent/X-Forwarded-For/Referer fuzz 和数据库列举清单。 | [方法条目](../by-type/sql-injection.md) |
| CORS 读权限与同源脚本执行不是同一边界 | 保存标题称 CORS 能缓解 XSS，这种泛化会混淆机制。 | [方法条目](../by-type/cors.md) |
| 子域来源的合并去重应保留时间与阶段范围 | 保存正文介绍 curated URL 来源、证书/子域变化、子域工具集合及 CT+Subfinder。 | [方法条目](../discovery/records-and-incremental.md) |
| Referer 跳转链、方法转换和令牌变体都须真实浏览器对照 | 清单列删/空/长度变化令牌、其他会话令牌、method override、Content-Type、Referrer、数组/NULL 和历史 Flash/307 等候选。 | [方法条目](../by-type/csrf.md) |
| 房间对象操作与聊天命令应由同一服务端策略授权 | Mozilla Hubs 历史摘要称管理员禁创建/移动对象后，聊天命令与客户端房间状态仍可能绕过，声称无需认证/加入房间。 | [方法条目](../by-type/idor-access-control.md) |
| 版本匹配模板输出只确认版本候选 | 正文明确警告 WordPress 模板合集主要按版本匹配会误报，README 的模板数、标签、更新指令和开源宣传不能消除此限制。 | [方法条目](../discovery/records-and-incremental.md) |
| DOM 跳转候选不自动推出原型污染 XSS | 保存正文建议从 DOM Open Redirect 入口继续测试原型污染。 | [方法条目](../by-type/prototype-pollution.md) |
| PII 名称和 GET 邮箱标题按实际暴露范围定性 | 正文询问姓名是否私密、另一帖称解释重置请求邮箱影响后被接受。 | [方法条目](../impact-and-acceptance.md) |
| 显式设置私钥后的生成接口先核对状态契约 | Node DiffieHellman 示例 setPrivateKey 后 generateKeys/getPrivateKey 仍为同值，材料以历史 CVE/Resolved 标记。 | [方法条目](../source-audit.md) |
| X509 公钥断言崩溃需证明外部输入能到达该进程 | 图片描述 Node 18.14.2 CreateAsymmetric 假设证书包含有效公钥并出现 pkey 断言/Abort。 | [方法条目](../source-audit.md) |
| 进程权限守卫需覆盖调试模块和继承方法入口 | Node 历史材料涉及 inspector 在 Worker 构造前改变 isInternal，以及 Node 19.6.1 的原型链 require 与普通 require 使用不同守卫。 | [方法条目](../source-audit.md) |
| 内部执行政策与广告账户绑定各自检查授权主体 | 运行时内部 Worker/继承 require 入口要保留原始进程权限与政策；LinkedIn Business Manager 的平台摘要则确认无关 Campaign Manager Account 曾能被绑定。 | [方法条目](../by-type/idor-access-control.md) |
| Node 文件政策分别核对路径规范化和 API 遗漏 | Node 20.0.0 图显式 allow-fs-read=* 但只允许 restricted 目录写，父目录路径说明的是写边界；openAsBlob→text 与 watchFile 是另两种读/观察 API。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Blob 读取和文件观察的授权检查不能只复用表面名称 | 保存示例在 experimental-permission 未给读取许可时调用 openAsBlob/text 或 watchFile。 | [方法条目](../source-audit.md) |
| 收件后的披露时机和奖励喜讯分别遵循当次许可 | 自动收件邮件称 being reviewed/if valid，要求修复机会后公开；SBB 奖励邮件允许分享喜讯但技术细节需明确许可。 | [方法条目](../scope-and-rules.md) |
| 自动受理邮件的 if valid 不能写成已确认漏洞 | Citrix Secure Access for Windows 的保存回信仅说明收件并审核，后续确认和修复是条件性承诺。 | [方法条目](../reporting.md) |
| 异步 XSS 入口与回连保留身份和等待窗口 | 保存建议使用可回看邮箱及反馈/评论入口，另有 ezXSS 工具介绍。 | [方法条目](../by-type/xss.md) |
| 编码与截断清单按具体解码器版本和文件消费者筛选 | 复用已实际看过的 LFI 图涉及单/双编码、旧 null byte/截断、filter/zip 等，普通 UTF-8 与 overlong 的分类不能混用。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 混合输入探针按语法、解释层和实际消费端拆解 | 清单把邮箱/phone-context/ext、引号、百分号、标签、模板括号、路径编码和 XML 文件混在一起。 | [方法条目](../targeted-fuzzing.md) |
| 清单中的跨租户检查只比较明确授权的对象 | 清单要求在全部租户测试并列 JS 函数、复制 URL、Referer 与管理员候选，不能据此访问任意真实租户。 | [方法条目](../by-type/idor-access-control.md) |
| 邮箱引号与格式接受不能替代 SQL 条件对照 | 一图仅对照 quoted local-part、空格/括号等是否触发 Bad format/Email andatidak Valid；复用另一已审图片才包含引号错误和数据库长度条件的延迟差异。 | [方法条目](../by-type/sql-injection.md) |
| HTML smuggling 的编码内容与网络请求错位分别理解 | 保存正文只定义 HTML 页面/附件中的编码恶意内容，未给具体构造或执行链。 | [方法条目](../by-type/document-rendering.md) |
| 缓存欺骗到令牌泄露需证明另一身份取得缓存响应 | 正文主张 Web Cache Deception→CSRF token→应用范围 CSRF→接管，并称敏感页加 private 修复。 | [方法条目](../by-type/cache-deception.md) |
| 泄露某个 CSRF 令牌并不保证全应用状态可改变 | 缓存泄露假设成立后，还需令牌属于哪个会话/用途、是否一次性或过期、目标方法、浏览器凭据与最终敏感状态。 | [方法条目](../by-type/csrf.md) |
| 历史 PHP 参数和 ASN 管道保留原始语法与候选性质 | 正文 Wayback→.php?id= 的 grep 片段缺实际模式/输出，HEDnsExtractor 示例把 URL 自动格式化成脚本名并接 httpx/grep。 | [方法条目](../discovery/records-and-incremental.md) |
| Android 包搜索结果需绑定实际 APK 和代码证据 | 保存 KoodousFinder package 查询只说明按包名/样本标签检索。 | [方法条目](../by-type/mobile-android.md) |
| PHP 文件和参数发现后的 XSS 仍需源到 sink 证据 | 正文用 ffuf 找 PHP、arjun 找参数并称得到反射 XSS，图只给 User-Agent 标题与接管主张。 | [方法条目](../discovery/web-and-api.md) |
| package.json 信息到依赖解析执行不能跳过证明 | 保存帖称配置文件泄露能链依赖混淆，图仅 P2 Triaged。 | [方法条目](../source-audit.md) |
| Base64 的不拦截与浏览器执行须分别验证 | 正文比较 script 候选 blocked 与其 Base64 表示 bypassed，却未保存应用解码位置、WAF 当时状态、输出 sink 或浏览器结果。 | [方法条目](../by-type/waf-bypass.md) |
| Heroku 欢迎页不能单独证明子域资源可被认领 | 保存 Red Bull 子域页面显示 Heroku 新应用欢迎文案，缺 DNS/CNAME、资源删除状态、绑定/认领条件和唯一控制标记。 | [方法条目](../by-type/subdomain-takeover.md) |
| GraphQL source 参数的服务端取址边界逐层核对 | EXNESS 报告摘要指出 allTicks 的 source 用于 GET，并描述回调 DNS/HTTP。 | [方法条目](../by-type/ssrf.md) |
| schema 模拟和 resolver 请求能力分别建立证据 | graphquail 介绍含 schema 构建、introspection emulation 和自定义头，模拟出来的 schema 不证明服务端 introspection 已开启或每字段可访问。 | [方法条目](../by-type/graphql.md) |
| stat 与 fopen 之间的路径身份不能靠先检查保证 | curl 保存片段在 stat 失败或非普通文件时退回直接 fopen 写，时间间隙内路径对象可能变化。 | [方法条目](../source-audit.md) |
| 主题深链到执行的链需保留安装和用户交互门槛 | Huawei ThemeManager 截图明确要求安装自定义主题，远程需用户动作，礼物/二维码/hwt deep link 是诱导入口，主题审核还会限制使用。 | [方法条目](../by-type/mobile-android.md) |
| 请求正文改 XML 需先确认解析器和权限等价 | 保存建议把 POST/PUT/PATCH body 改 XML 并改 Content-Type；混合清单亦列 SVG/Office/SOAP/XML 为候选。 | [方法条目](../by-type/xxe.md) |
| 邮件 HTML 插入与脚本执行及可信界面误导分别证明 | 保存正文称邮件内容 HTML injection，图只有报告列表。 | [方法条目](../by-type/xss.md) |
| 历史源站关联保留证书、Host 和 SNI 的各自证据 | 2019 报告于 2023 披露，作者以证书/相同内容关联云服务地址并声称指定 resolve 直连。 | [方法条目](../discovery/passive-and-services.md) |
| 源站直连主张需要同应用的防护路径对照 | 归档声称非代理来源能直连源站，与经 Cloudflare 的路径不同。 | [方法条目](../by-type/waf-bypass.md) |
| 私有项目页面的公开讨论限制仅保留为历史许可证据 | 保存页面明确要求项目公开前不要公开讨论，项目名与注册报告细节遮挡。 | [方法条目](../scope-and-rules.md) |
| 本地与远程文件包含候选各自确认读取和解释权限 | 混合清单列双斜杠、编码、旧截断与远程包含，但路径字节被接受不证明文件已读取，取回远程内容也不证明被解释为代码。 | [方法条目](../by-type/lfi-path-traversal.md) |

| Rails 与 Rack 耗时问题按解析入口拆分审计 | Range、Content-Disposition、RFC2183 boundary、ActiveSupport underscore、GlobalID model name 是不同输入与调用链；保存截图给出异常耗时或正则回溯说明，不能把一项修复或静态复杂度预测套到全部组件。 | [方法条目](../source-audit.md) |
| libcurl 保存状态文件的 stat 与 fopen 竞争窗口 | cookie、HSTS、alt-svc 持久化在检查路径后打开文件，路径被本地竞争者替换可能使受害进程创建或覆盖其权限下的受保护文件。 | [方法条目](../source-audit.md) |
| CRLF 路径标记与 301 独立 Set-Cookie 行的证据 | 保存请求路径携带编码换行，响应 301 中出现独立 Set-Cookie 标记，可提炼为解码后输入跨入响应头边界的线索。 | [方法条目](../by-type/crlf-response-splitting.md) |
| HTTP 头作为数据库输入的候选入口 | 保存正文仅提出 SQLi through HTTP Headers 并指向外链，未给触发全文。 | [方法条目](../by-type/sql-injection.md) |
| 短链 Location 候选保留原始 URI 和错误状态 | 同哈希已审阅图展示 requests 不跟随跳转并对 Location 做 urllib 解码的旧式脚本。 | [方法条目](../discovery/records-and-incremental.md) |
| 数据库与 webconfig 备份泄露须区分内容和连接权限 | 正文分别自述发现 DB_USER/PASSWORD 后连接数据库，以及 webconfig 备份外部暴露；截图只保留评级/状态，没有秘密获取和连接回执。 | [方法条目](../by-type/info-secrets.md) |
| Metabase setup 校验链与检测脚本输出分开归因 | 正文指向 CVE-2023-38646；一图只输出 localhost Token/Vulnerable，不能当执行证明。 | [方法条目](../source-audit.md) |
| Hilton 基域 URL 与 wildcard 历史新增分别登记 | 历史图新增 *.hiltonhotels.jp、hiltonhotels.jp、*.hiltonlocalbiz.com，资产类型分别 wildcard、URL、wildcard，三项 eligible for bounty=true。 | [方法条目](../scope-and-rules.md) |
| 从 urlscan 历史记录找回未发现路径 | 正文说明常规来源未找到可测入口，随后从 urlscan 搜索目标获得路径，再自述三条 RXSS。 | [方法条目](../discovery/passive-and-services.md) |
| LFI 到 Kubernetes 服务账号材料的影响边界 | 已确认文件读取时，/var/run/secrets/kubernetes.io/serviceaccount 目录可作为容器身份材料线索，不能读取目录名就假定泄露 token。 | [方法条目](../cloud/container-k8s-security.md) |
| 历史无密码登录 URL 必须验证实际身份授予 | 正文疑问称 Wayback 找到只要 email 的 signin，无完整请求或后续会话。 | [方法条目](../by-type/authn-session.md) |
| Rails inline SVG 的 CSP 覆盖取决于响应类型 | 保存图说明 send_file/send_data 以 image/svg+xml 且 inline 返回时，预期 default-src 'none' 却只对 HTML 应用 CSP，上传 SVG 的活跃内容可能执行。 | [方法条目](../by-type/xss.md) |
| Rails helper 属性名称与属性值分别验证 | FormTagHelper/TagHelper 的 options 将 data-*、aria-* 或其它非 boolean 属性 hash 的 key 变成属性名；对 value escape 不能补足对标签名/属性名允许字符的限制。 | [方法条目](../by-type/xss.md) |
| ActiveStorage variant 处理层级先于命令注入判定 | 截图保存 variants→image_processing→mini_magick→ImageMagick 的转换链和测试版本 ActiveStorage 6.1.3.1、image_processing 1.12.1、mini_magick 4.11.0，题名声称参数/代码注入，但未保存恶意参数和执行回执。 | [方法条目](../source-audit.md) |
| redirect_to 控制字符丢失 Location 后的点击 XSS | 保存报告针对 Rails 7.0.4.3，说明 URL 控制字符导致下游移除 Location，但响应 HTML 的 href 仍保留可控 URI，javascript URI 可在点击时触发；可见字符范围为 %01–%08、%0b、%0c、%0e–%1f。 | [方法条目](../by-type/xss.md) |
| 盲 XSS 评级与先知问题的奖励回执独立保存 | 正文只自述 blind XSS，评论中的方法未保存；邮件把问题评 High，称 IP 封禁缓解升级，并说明另一独立报告使团队先注意问题，仍认可贡献并奖励。 | [方法条目](../reporting.md) |
| 黑盒混合探针先拆出单一解析边界 | 正文列生成/变异 fuzz、payload 与行为识别；同哈希已审阅图用标签、引号、百分号、括号、模板括号及反斜杠观察错误或解析。 | [方法条目](../targeted-fuzzing.md) |
| 前端脚本中的隐藏参数回到实际服务端边界 | 正文建议从 JS 和隐藏参数发现弃用开发入口；截图只有不同漏洞题名和评级。 | [方法条目](../discovery/web-and-api.md) |
| BucketLoot 的过滤、命中与真实云权限分别记录 | 正文说明支持 AWS/GCS/DigitalOcean、30+ regex、自定义 keyword 与资产提取；图显示 GCS 示例 400 对象、117 兴趣文件，keyword/URL/Google service-account SECRET 分类命中。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| ASP.NET Content-Type 与请求解码的存储 XSS 线索 | 正文仅自述 2017 年 Request Validation 可经 Content-Type 绕过而存储 XSS，未保存外链全文。 | [方法条目](../by-type/xss.md) |
| ZIP wrapper 从文件读取到 PHP 执行的额外前提 | 允许上传 ZIP 与存在 LFI 时，zip:// 只说明可选归档成员路径，RCE 还要求可控制上传位置/成员内容、目标 PHP 支持该 wrapper，以及调用确为能解释 PHP 的 include/require。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 地点搜索输出需要目标归属而非联系人数量 | MAPSDUMPER 声称采集地图电话、邮箱、网站、reviews，图只显示 laundry 搜索、逐地点链接、API place 与每项十条 reviews。 | [方法条目](../discovery/passive-and-services.md) |
| 父级 403 不保证子资源与数字对象权限一致 | 正文记录 JS 发现 admin 路由、父路径 403，再找到 users/images 仍 403，而 /users/1–100 自述列出用户照片/PII。 | [方法条目](../by-type/idor-access-control.md) |
| WebCopilot 子域发现与漏洞扫描分阶段限定 | 正文列参数候选与多类扫描，帮助图包含目标、输出目录、threads 默认 100、BXSS server、排除域与仅子域枚举。 | [方法条目](../discovery/web-and-api.md) |
| 删除账号后的 JWT 有效性和业务授权必须同步验证 | 正文称删除账号后旧 token 仍能创建 API key 并经 endpoint 查看；图仅报告标题。 | [方法条目](../by-type/authn-session.md) |
| 证书子域枚举按 DNS 标签防相似域误归属 | 正文 Nmap hostmap-crtsh 一行涉及证书来源；示例输出 stage/qa/sandbox 和一个将品牌作为前缀的 donsson.com 域。 | [方法条目](../discovery/passive-and-services.md) |
| 本机 shell 工具握手不等远程执行或免杀 | pyFUD 图片只有 127.0.0.1 listener、单客户端连接和 list/id/back 帮助。 | [方法条目](../experiment-design.md) |
| 搜索型 query 的 dork 结果保留原始语义 | 正文按 site 和 inurl:search=/s=/message=/q= 寻找输入入口。 | [方法条目](../discovery/web-and-api.md) |
| Tplmap 识别与 sandbox escape 仍需模板求值证据 | 正文只介绍 SSTI/Code Injection 工具和逃逸能力，未保存具体模板或结果。 | [方法条目](../by-type/ssti.md) |
| Ivanti 指纹发现与预认证 API 影响各留证据 | 正文声称 EPMM/MobileIron Core CVE-2023-35078，并给标题及 favicon 查询；图中两种查询历史结果分别 1606 与 2514。 | [方法条目](../discovery/passive-and-services.md) |
| 多斜杠路径筛选 302 后还要解析 Location | 正文 httpx 将 ///evil.com 路径和 302 筛选联用。 | [方法条目](../by-type/open-redirect.md) |
| 资源检索器分类输出保留保存范围 | 同哈希已审阅图是 BugBountyHunting 搜索 UI，含 XSS/SSRF/SQLi/RCE/IDOR/INJECTION 分类与 keyword/JSON export，没有结果全文。 | [方法条目](../discovery/records-and-incremental.md) |
| Shodan 查询字段不同对应不同证据层 | 图列键前缀、Grafana 标题、FTP banner、ASN、favicon、证书 subject/issuer、wp-config 提示、组件和目录标题。 | [方法条目](../discovery/passive-and-services.md) |
| 页内目标在底部时的 iframe 定位与同源限制 | 正文建议 auto-scroll iframe。 | [方法条目](../by-type/clickjacking.md) |
| 从流量识别栈后按应用和范围选择方法 | 书页实际保存的是：新目标先识别前后端框架、第三方服务、文件与域、HTML/JSON 和代理历史，再选择方法；目标持续变化值得回访，不因别人已经测过放弃，也可在无有效线索时切换目标。 | [方法条目](../hunting-strategy.md) |
| 金额币种数量篡改必须看服务端结算与交付 | 正文列改 request/response 价格、USD→SAR/INR、quantity 1.00→0.01，案例自述免费但 OOS。 | [方法条目](../by-type/business-logic.md) |
| 备份配置后缀与技术栈候选不能只凭 200 判定 | /common/config.php.new 图实际返回 PHP 配置且值遮盖；正文另列 WP/Joomla/Drupal/PrestaShop tar/zip、Apache tar及压缩变体、Nginx tar、IIS zip/cab、Tomcat war/jar，为经验候选而非固定规则。 | [方法条目](../by-type/info-secrets.md) |
| email disavow 动作 URL 区分无登录和无授权 | Liberapay 图用历史 URL 搜 disavow，报告称打开可解除 email，侧栏却为 Informative。 | [方法条目](../by-type/authn-session.md) |
| 参数发现把稳定性与差异因子分别保存 | ParamPamPam 正文是 GET/POST 参数发现介绍；Arjun 2.1.5 图先测稳定性、响应异常和潜在名称，再按 redirection/http code/body 提示 url/filter/page。 | [方法条目](../discovery/web-and-api.md) |
| 第三方支持系统冒名工单与范围例外独立 | HackerOne 摘要说明 Freshdesk 配置改变修复冒名工单；该支持资产当时未列范围，None 严重性仍出现 1000 奖励与状态变化。 | [方法条目](../scope-and-rules.md) |
| GitHub Pages 释放绑定与 DNS 保留的短窗口 | 保存摘要说明 CNAME hold 被释放、DNS 仍指向 GitHub，约十分钟窗口可从另一个仓库绑定域名，后增加 Domain Verification 并转回。 | [方法条目](../by-type/subdomain-takeover.md) |
| JWT 可读结构与验签授权分别审计 | 手册图描述常见 JWS header.payload.signature、Base64url JSON，例 HS256/typ/sub/role/exp；解码不等验证，载荷也不因编码保密。 | [方法条目](../by-type/jwt.md) |
| WARP 输入崩溃的本地触发与实际安全影响 | 保存摘要：隧道排除/包含 IP ranges 文本框不限制输入长度，长 string 可令客户端 crash。 | [方法条目](../by-type/desktop-client.md) |
| MySQL MSSQL PostgreSQL 探针按数据库和载体分离 | 正文给 sleep、WAITFOR DELAY、PG_SLEEP，图分别出现 multipart reg_CustName（约16.112秒）、username（约6.246秒）和 GraphQL userId（约7.696秒）。 | [方法条目](../by-type/sql-injection.md) |
| WebSocket REPL 保存控制帧和业务帧的生命周期 | 图记录 0x1 JSON trade、0x9 ping、0xA pong、方向和时间戳；正文介绍 wsrepl Python 生命周期 hooks。 | [方法条目](../by-type/websocket.md) |
| 解包 IPA 的模板命中需验证秘密用途 | 正文建议解包 ipa/decrypted.ipa 后用 mobile Nuclei 模板找硬编码敏感数据。 | [方法条目](../by-type/mobile-ios.md) |
| 缓存投毒到 XSS 与 ATO 分别证明 | 正文一例称 unkeyed header 反射脚本且 Cache-Control: public,max-age=500，另一例声称需交互的 stored XSS 链成 ATO；截图只有题名。 | [方法条目](../by-type/cache-deception.md) |
| 同正文 MTN 更新按各帖图片绑定四项变化 | 两个同正文保存帖配不同图片：第一新增 mtnzakhele.co.za 并移除 mtnghonlineservices.mobi；第二新增 https://www.mtn.com/wp-json/ 并移除 mtn.com.gh，均 URL 类型且 eligible for bounty=false。 | [方法条目](../scope-and-rules.md) |
| target blank 链接 XSS 保留浏览器点击类型 | 正文声称 Firefox 中 target=_blank anchor 可借类似 Chrome 中键/修饰键点击方式访问 document.cookie，外链全文未保存。 | [方法条目](../by-type/xss.md) |
| 账号合并分支不能绕过已启用 MFA | LinkedIn 摘要明确 merge-accounts 可在已知受害者凭据时进入账号而未执行 2FA。 | [方法条目](../by-type/authn-session.md) |
| Apache 内容协商 406 的候选文件清单归因 | mod_negotiation 会选择与客户端能力匹配的文件，图称无效 Accept 可使 /index 406 响应含伪目录变体清单，提供基础名/扩展/备份候选。 | [方法条目](../discovery/web-and-api.md) |
| PR diff 视图必须与最终 Git 对象一致 | GHES refs/replace 相关错误比较可显示错误 diff 造成 commit smuggling，摘要明确须仓库 write 权限，历史 >=3.7.0、修复3.7.9/3.8.2/3.9.1，CVE-2023-23764。 | [方法条目](../source-audit.md) |
| GraphQL 更新阵容的单队长不变量由服务端约束 | 保存 Sorare 摘要：在自有队伍编辑确认的 /federation/graphql CreateOrUpdateSo5LineupMutation 中，多个球员 captain=true 可违反 UI 单队长限制，每队长给 50% score bonus。 | [方法条目](../by-type/business-logic.md) |
| Autorize 匿名对照须移除全部身份渠道 | 正文询问去除 Authorization Bearer 以验证匿名。 | [方法条目](../by-type/idor-access-control.md) |
| 凭据组合策略与公开发现集合的许可分开 | 正文介绍 Nuclei credential stuffing/spraying、Pitchfork 与 Cluster Bomb；图用 admin/admin 模板结合 Shodan/FOFA uncover，500 limit 后显示1000 targets、916 URL。 | [方法条目](../by-type/authn-session.md) |
| Hetty 帮助中的监听证书存储边界单独核验 | 图显示 MITM proxy、GraphQL 和 admin interface、CA/key、db、监听 :8080，以及 --chrome 设置代理并忽略 certificate errors。 | [方法条目](../experiment-design.md) |
| 直连源站须保持 Host SNI 和应用身份 | 正文称从 DNS 找到 Cloudflare 源 IP 后直连可绕过 WAF。 | [方法条目](../by-type/host-header.md) |
| 报告处理停滞与预算耗尽不能混同 | 正文猜测项目三个月无活动且预算耗尽；截图仅能证明 triage 尚未得到团队回复并再次 ping。 | [方法条目](../hunting-strategy.md) |
| XMLRPC 序列化限制不能替代反序列化类限制 | Ruby XMLRPC0.3.2 图在 create.rb 以 ENABLE_MARSHALLING/Marshallable 限制序列化，但 parser struct(hash) 读取 __class__ 的反序列化限制不足。 | [方法条目](../by-type/deserialization-rce.md) |
| Steam Deck 浏览器立足点与跨进程提权逐层验证 | 保存摘要指历史 CEF Chromium85.0.4183.121/CVE-2020-16040，在用户点 Steam Chat 链接后进入 deck 身份的 steamwebhelper，CEF sandbox disabled，可访问/改用户文件。 | [方法条目](../by-type/desktop-client.md) |
| CRUD 动作逐项检查跨站身份与状态变化 | 正文建议 CRUD 时测 CSRF，截图只 triaged 通知。 | [方法条目](../by-type/csrf.md) |
| 测试卡被接受与生产权益交付分开证明 | 正文建议 provider 测试卡触发 premium 功能；图片是等待评估邮件。 | [方法条目](../by-type/business-logic.md) |
| 路径遍历图只证明应验证的读边界 | 图以 ../../../etc/passwd 示意从普通目录进入 private 目录再响应文件内容，没有真实请求。 | [方法条目](../by-type/lfi-path-traversal.md) |
| details ontoggle 混合属性探针区分 WAF 与浏览器 | 正文给 details/open、大小写与混合属性形式的 ontoggle payload，但无响应或执行截图。 | [方法条目](../by-type/waf-bypass.md) |
| Telegram 远程工具输出保留 HTTP 原始证据 | 六格图是 Lockdoor root 菜单、dirsearch0.3.9/GET/10threads/6027词，在示例目标输出大量301/302。 | [方法条目](../experiment-design.md) |
| Tor PDF 请求的冷启动初始化顺序决定通路 | Brave 2019 报告在 Windows10，启动后 Tor 窗未访问任何 HTTP/HTTPS 时，直接 chrome-extension PDF viewer URL 的 AJAX 未通过 proxy，源服务见真实 IP；先在 Tor 窗初始化 HTTP/HTTPS 是关键反例。 | [方法条目](../by-type/desktop-client.md) |
| 三十种历史检索来源按证据对象选择 | 图服务名单包含 DeHashed、SecurityTrails、DorkSearch、ExploitDB、ZoomEye、Pulsedive、GrayHatWarfare、PolySwarm、FOFA、LeakIX、DNSDumpster、FullHunt、AlienVault、ONYPHE、Grep App、URLScan、Vulners、WayBackMachine、Shodan、Netlas、crt.sh、Wigle、PublicWWW、BinaryEdge、GreyNoise、Hunter、Censys、IntelligenceX、Packet Storm 和 SearchCode。 | [方法条目](../discovery/records-and-incremental.md) |
| xurlfind3r 历史 URL 保留 query 与来源版本 | 图0.2.0主要 wayback，0.3.0另有 urlscan，均 --include-subdomains；含图片、:80、大小写后缀、index.php路径和 tab/p/display/wc-ajax 等 query。 | [方法条目](../discovery/records-and-incremental.md) |
| id 后缀正则只筛候选且有结构性漏报 | 保存正则为 `(?i)\b\w*id\b(?!\w)\s*=\s*("[^"]*"｜'[^']*'｜[^&\s}]*)`，偏向等号赋值且名称以 id 结尾。 | [方法条目](../by-type/idor-access-control.md) |
| frame ancestors 子域模式与基域匹配须实际验证 | 正文策略 `frame-ancestors 'self' https://*.foo.foo:*` 并建议检查 http://foo.foo 是否 claimed。 | [方法条目](../by-type/clickjacking.md) |
| 月度泄露列表逐入口记录而非拼成攻击链 | 正文分别列 Citrix CVE、RabbitMQ guest 与员工 email、partner PII/Symfony、Laravel debug 基础设施密码和系统日志；图片另是内部 IP 与 Ambari 奖励/状态和付款通知。 | [方法条目](../by-type/info-secrets.md) |
| WARP IPv6 DNS ULA 与 loopback 的本地网络差异 | 摘要说明 Windows WARP IPv4 DNS 地址为 loopback，而 IPv6 能力网络上使用 ULA；特定条件可能指向同 LAN 其它设备，导致 DNS 查询暴露。 | [方法条目](../by-type/desktop-client.md) |
| 奖励后的类别排除从生效政策判断资格 | 匿名邮件说额外 300 与 P2 相当，并将 XSS 从后续 VDP 中排除。 | [方法条目](../scope-and-rules.md) |
| 用户信息公开性与业务影响决定评级证据 | 匿名邮件一项认为 API 返回用户信息但不含 secret，评 P4/75；另两项说基于 business 理解调整至 P3/150。 | [方法条目](../impact-and-acceptance.md) |
| 首报重评与新增独立问题按证据建工单 | 一邮件确认 P3/150 首报，另一调整 P2/300 并要求额外问题以新 ticket 提交。 | [方法条目](../reporting.md) |
| 有限披露与 credentials 修复不推断撤销完成 | Nutanix 保存题名是员工凭据提交 GitHub 已 fixed；timeline Critical→Medium5.3、Resolved、取消披露请求，没有秘密原文或验证权限。 | [方法条目](../reporting.md) |
| V8 native pointer 调试截图保留原语缺口 | 图混合 Windows memory viewer 与 Linux GEF，标出函数对象 pointer、可执行区域的 int3 和 rip 值，是调试状态而非完整可重放链。 | [方法条目](../source-audit.md) |
| Google Accepted 状态与 VRP 资格审核独立 | 两图显示 Customer Issue→Bug、S4→S3、Assigned→In Progress Accepted，后文说产品团队评估是否修复，VRP panel 另审奖励、初看可能不足。 | [方法条目](../reporting.md) |
| 重用删除账号用户名不能继承旧数据权限 | 正文提出同用户名重新注册后是否能访问旧数据。 | [方法条目](../by-type/authn-session.md) |
| Noir 源码攻击面发现回到版本和路由证据 | 正文仅介绍从源码检测攻击面的 Noir，未保存实现或输出。 | [方法条目](../source-audit.md) |
| Points 调试对象泄露与积分业务能力各需证据 | 图 Points_LCP 对象包含会员 validation request/response、balance、会员字段以及 macID/macKey 等材料，值被遮盖。 | [方法条目](../by-type/info-secrets.md) |
| 同类路径跨国家域查询保持资产与 prefix 边界 | 正文建议对目标拥有的 ccTLD 使用 /anything*，图是 .com.br URL prefix 的9256历史记录。 | [方法条目](../discovery/records-and-incremental.md) |
| Oracle 多重 ALL_USERS 计数不能当低成本延时证明 | 正文 email 参数含五张 ALL_USERS 的笛卡尔 COUNT 比较，可能产生巨大计算开销；图仅 POST email SQLi triaged 通知，无基线或查询回执。 | [方法条目](../by-type/sql-injection.md) |
| kOps GCP state bucket 权限可将 pod 立足点升级 | 保存摘要：kOps 给节点关联 service account 读取 state bucket 的权限，已有 pod shell 的用户可请求实例凭据读取 state 敏感材料，再转 cluster admin，进一步影响 control-plane GCP identity。 | [方法条目](../cloud/container-k8s-security.md) |
| Metabase H2 校验返回错误与数据库副作用分别观察 | 同哈希已审阅图在 setup validation 的 H2 输入含 TRACE/trigger 链，并出现 SQL 42000 错误。 | [方法条目](../by-type/sql-injection.md) |
| Metabase 校验链的运行时回调只按归因升级 | 保存图包含从 H2 trigger/JavaScript 到运行时命令的路径和 DNS/HTTP 回执。 | [方法条目](../by-type/cmd-injection-rce.md) |
| Metabase 预认证 setup 状态与 token 暴露条件 | setup token 与 validate route 的组合需要确认实际部署 setup 状态、token 获取是否免身份、重复/过期语义以及受影响版本；工具 Token/Vulnerable 输出不代替 HTTP 入口及身份对照。 | [方法条目](../by-type/authn-session.md) |
| setup 验证器的错误前副作用归因矩阵 | 对 Metabase 已保存链，在隔离副本控制身份、setup 状态、token、driver、trigger 和回调 marker，每次仅改变一项；同步保存原始错误、时间和自控回调。 | [方法条目](../experiment-design.md) |
| Metabase 校验注入先限定获准环境与无害副作用 | 产品存在与 setup route 可达不授予执行命令或外传；以许可环境的最低影响证据确认验证边界，令测试时间、资源和回调可控。 | [方法条目](../scope-and-rules.md) |

| XML业务错误不能佐证本地DTD XXE（2023保存案例） | XMLstockCheck productId Change_the_object/storeId1，400JSON Invalid productID；证实XML业务格式非DTD/实体解析或本地DTD读取，先区分XML支持与XXE。 | [方法条目](../by-type/xxe.md) |
| 子域接管流水线的活性过滤与手工确认（2023保存案例） | 子域接管Part1subfinder/amass passive非recursive/assetfinder来源合并；每源输出身份/时间/失败单记，去重候选不代表current可接管，图末合并下页。 | [方法条目](../by-type/subdomain-takeover.md) |
| 浏览器翻译前后保留原始测试证据（2023保存案例） | Firefox右键TranslateEnglish入口；翻译变DOM/文本，需保留原文原始response和业务词义，菜单不证明translation正确/插件无外传。 | [方法条目](../experiment-design.md) |
| 代理明文与真实传输加密的区别（2023保存案例） | WakaTime报告称卡数据无加密MITM，自述无抓包/URL协议，图侧栏Spam、timelineNotApplicable；代理解密不证实公网明文，需真实TLS通路与观察位置，不按High标签当valid。 | [方法条目](../reporting.md) |
| 编码src反射与实际HTML执行上下文（2023保存案例） | 地址栏src参数编码body onload→浏览器alert1，域蓝遮/响应未见；可见执行线索但需实际DOM、解码阶段/点击/源归因，不把任何编码通用绕WAF。 | [方法条目](../by-type/xss.md) |
| 开放重定向检测须保留多跳最终导航（2023保存案例） | OpenRedireX3URLs44payloads logout redirect/redirect_uri多跳，INFO站内跳FOUND最终google例；必须完整Location链与browserURIparse/userinfo/多斜线，FOUND标签不等所有同类入口vuln，不访问原目的地。 | [方法条目](../by-type/open-redirect.md) |
| 搜索界面中的扩展名候选没有授权含义（2023保存案例） | TakSecdorkUI目标tesla/PHP?、公开报告搜索、log/txt/conf/cnf/ini/env/old/git/svn/htpass/htaccess候选；UI不是搜索结果或敏感返回，OR/site约束需核对，右侧裁切不补。 | [方法条目](../discovery/passive-and-services.md) |
| GraphQL别名登录必须按认证尝试计数（2023保存案例） | 实验室 GraphQL 请求将大量不同密码登录尝试放入别名 bruteForce0–62；响应中多数 success=false，bruteForce49 为 true。 | [方法条目](../by-type/graphql.md) |
| 书签抽取中的协议相对URL与静态资源（2023保存案例） | JS Endpoints 书签工具展示混合的绝对、协议相对和站内相对 URL，包括脚本/图片域、登录注册、manifest 与时间线路径；底部书签代码截断，可辨延迟输出。 | [方法条目](../discovery/web-and-api.md) |
| 不同分辨率弹窗截图的解码证据边界（2023保存案例） | 另一分辨率截图显示 src 参数内编码 body onload 后弹出 alert(1)。 | [方法条目](../by-type/xss.md) |
| 作者第三方用户名链接的回收与冒名风险（2023保存案例） | JFrog 作者页引用失效/改名的 Twitter 用户名，报告描述重新占用该标识后冒充作者，建议更新或删除链接；截图状态 Low/Resolved。 | [方法条目](../by-type/subdomain-takeover.md) |
| 范围外例外奖励不修改后续测试许可（2023保存案例） | 邮件明确页面仍在赏金范围外，但愿意为可复现的问题例外奖励200欧元。 | [方法条目](../scope-and-rules.md) |
| 堆快照路径的历史残留与数据最小化（2023保存案例） | heaptruffle 示例展示从浏览器堆快照抽出的设置路径、带构建哈希的脚本与帮助页面 URL。 | [方法条目](../discovery/client-and-cloud.md) |
| 案例搜索分类与JSON导出仅是资料入口（2023保存案例） | Bug Bounty Hunting Search Engine 界面提供 XSS/SSRF/SQLi/RCE/IDOR/Injection 类别、q 查询和 JSON 导出。 | [方法条目](../discovery/records-and-incremental.md) |
| 数字实体和URL百分号解码的先后顺序（2023保存案例） | 被遮挡目标的 url 参数包含百分号编码的数字实体与 javascript URI，截图弹窗内容被涂抹。 | [方法条目](../by-type/xss.md) |
| 侦察按钮矩阵需要逐组件审阅和范围约束：被动来源（2023保存案例） | 深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。 | [方法条目](../discovery/passive-and-services.md) |
| 侦察按钮矩阵需要逐组件审阅和范围约束：Web/API候选（2023保存案例） | 深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。 | [方法条目](../discovery/web-and-api.md) |
| 侦察按钮矩阵需要逐组件审阅和范围约束：云资源（2023保存案例） | 深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 侦察按钮矩阵需要逐组件审阅和范围约束：资料记录（2023保存案例） | 深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。 | [方法条目](../discovery/records-and-incremental.md) |
| 侦察按钮矩阵需要逐组件审阅和范围约束：源码边界（2023保存案例） | 深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。 | [方法条目](../source-audit.md) |
| 侦察按钮矩阵需要逐组件审阅和范围约束：授权边界（2023保存案例） | 深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。 | [方法条目](../scope-and-rules.md) |
| 重定向报告评分字段与向量不一致（2023保存案例） | Open Redirection 编辑页上部 Score4.1、下部计算器4.7不一致，向量显示网络/低复杂度/无权限/需交互/范围变更/完整性低。 | [方法条目](../impact-and-acceptance.md) |
| PDF用户名脱敏的空值和短名边界（2023保存案例） | HackerOne PDF 导出勾选 redact all usernames 后仍泄露用户名；摘要说明空值、短名和其他边界导致历史功能回滚。 | [方法条目](../by-type/info-secrets.md) |
| Seller重定向命名参数的XSS与导航分别确认：脚本上下文（2023保存案例） | TikTok Seller 报告摘要说明 hack_redirect_now 参数用户输入未适当 HTML 转义/输出编码导致 XSS，标题并列 DOM XSS/open redirect，截图没有重定向请求链。 | [方法条目](../by-type/xss.md) |
| Seller重定向命名参数的XSS与导航分别确认：导航边界（2023保存案例） | TikTok Seller 报告摘要说明 hack_redirect_now 参数用户输入未适当 HTML 转义/输出编码导致 XSS，标题并列 DOM XSS/open redirect，截图没有重定向请求链。 | [方法条目](../by-type/open-redirect.md) |
| 威胁情报平台类别与被动关联证据（2023保存案例） | 威胁情报工具图分别介绍Shodan/Censys设备服务索引、被动DNS/IP/声誉关联、VirusTotal/Hybrid分析、MISP/OpenCTI/TheHive共享协作与样本库。 | [方法条目](../discovery/passive-and-services.md) |
| ASN分组不会扩大云及CDN资产授权（2023保存案例） | ip2asn --json 示例把多个输入IP归入AS15211/54113/13335/16509/1299。 | [方法条目](../discovery/passive-and-services.md) |
| 历史域名条目的范围和赏金资格分开核对（2023保存案例） | 截图显示 x.com URL Eligible For Bounty true/Added in Scope，仅为历史特定条目。 | [方法条目](../scope-and-rules.md) |
| Contact Form7特殊文件名上传的版本及执行条件（2023保存案例） | CVE2020-35489图含Contact Form7 before5.3.2因特殊文件名导致 unrestricted upload/RCE 的历史描述；249累计/94近12周/+18%是报告统计，不是当前受影响资产数量。 | [方法条目](../by-type/file-upload.md) |
| 邮箱格式校验报错之前的脚本执行（2023保存案例） | 登录邮箱栏包含类数组/引号JS片段，界面显示请输入有效邮箱同时弹XSS。 | [方法条目](../by-type/xss.md) |
| 登录错误弹窗不足以从Self XSS升级ATO（2023保存案例） | 登录错误页面弹alert1，目标及输入被裁切。 | [方法条目](../by-type/xss.md) |
| LFI扫描器路径标签需要响应内容对照（2023保存案例） | LFI FINDER终端向同一URL参数迭代不同深度的../etc/passwd并标红Vuln Url；没有响应内容或错误路径对照。 | [方法条目](../by-type/lfi-path-traversal.md) |
| IIS cookieless路径重写与目录过滤差异（2023保存案例） | IIS Restricted Path Bypass片段描述.NET Framework cookieless路径段(S(X))，将其插入protected/bin名称形成过滤路径与框架处理路径差异；示例保护目录Basic认证，bin目录默认限制。 | [方法条目](../by-type/idor-access-control.md) |
| 公开并购搜索的归属时效和范围边界（2023保存案例） | Google site:*.crunchbase.com acquired by yahoo约681结果，是公开并购线索候选。 | [方法条目](../discovery/passive-and-services.md) |
| PDF脚本交互和网络权限取决于查看器（2023保存案例） | Chrome PDF查看器显示单页 CLICK ANYWHERE，文件名暗示弹窗发送输入，但截图没有实际弹窗或网络行为。 | [方法条目](../by-type/document-rendering.md) |
| PTR名称不能单独证明整个网段归属（2023保存案例） | prips某/23网段管道到revit，输出PTR名含VPN/corp/unknown。 | [方法条目](../discovery/passive-and-services.md) |
| 本地URL后缀模板不是服务端秘密读取（2023保存案例） | Nuclei URL extension inspector file模板对本地test.urls.txt报.bak/.php.bak/.sql.tar.gz/public_html/.z/.xls，file模式不是目标HTTP读取。 | [方法条目](../by-type/info-secrets.md) |
| Unicode转义需要真正的JSON或JS解码阶段（2023保存案例） | Unicode XSS图给出字面\u003e/\u003c img onerror片段，无触发截图。 | [方法条目](../by-type/xss.md) |
| AppPassword旁路必须继承近期密码确认（2023保存案例） | Nextcloud历史CVE2023-39963报告：UI/AuthSettingsController要求近期确认密码，已有登录会话可走/ocs/v2.php/core/getapppassword路由取得AppPassword。 | [方法条目](../by-type/authn-session.md) |
| OAuth2控制器不能遗漏失败认证预算（2023保存案例） | Nextcloud OAuth2 API controller缺失暴力保护历史CVE2023-39958，图仅标题/摘要链接/时间线，没有具体参数或重试预算。 | [方法条目](../by-type/oauth-oidc.md) |
| 外部存储删除的owner和type检查缺口（2023保存案例） | Nextcloud报告摘要：DELETE /apps/files_external/userstorages/<storage_id>只检查mount存在，不验证owner/type，按id删除关联数据库配置，非管理员能影响用户/全局外部存储且无需挂载选项开启。 | [方法条目](../by-type/idor-access-control.md) |
| WebDAV应独立核对认证失败保护覆盖（2023保存案例） | Nextcloud WebDAV excessive authentication attempts历史CVE2023-39960，标题/公告链接/时间线，无具体绕过请求或限速值。 | [方法条目](../by-type/authn-session.md) |
| SQL语法回显与数据库XPath报错通道（2023保存案例） | Burp截图accountID值带单引号，JSON errorText回显email/password查询与SQL syntax error。 | [方法条目](../by-type/sql-injection.md) |
| Notes附件预览的HTML呈现与脚本隔离（2023保存案例） | Nextcloud Notes attachments render HTML in preview mode历史CVE2023-39955，标题/公告链接/时间线，无具体附件或执行。 | [方法条目](../by-type/file-upload.md) |
| Burp范围正则需完整主机边界与工具约束（2023保存案例） | Burp Advanced scope字段Host or IP range只写yahoo、ProtocolAny/其他空，规则是正则。 | [方法条目](../scope-and-rules.md) |
| 同源脚本CSP不能补救原样HTML输出（2023保存案例） | PHP挑战代码设CSP script-src self;object-src none后原样echo GET input。 | [方法条目](../by-type/xss.md) |
| ENL共享网络库仍需按游戏构建核对影响（2023保存案例） | Nintendo ENL历史报告介绍NEX匹配/PIA UDP点对点，使用于Mario Kart/Splatoon/Animal Crossing等，称最后修复2023-08-03。 | [方法条目](../by-type/iot-security.md) |
| 匿名支持票据与后续账户操作身份校验（2023保存案例） | HackerOne support票据系统接受邮箱/用户名、作者称代理转交删账号请求，摘要说明重复报告归属误判。 | [方法条目](../business-modeling.md) |
| 侦察GUI的零进度和组件运行证据（2023保存案例） | Wolf Recon V1 GUI列出Sub-Domain/httpx/WayBackUrls/Nuclei及组合、Google/GitHub dorking，进度0%。 | [方法条目](../discovery/web-and-api.md) |
| 移动工具按静态动态代理及设备权限选择：Android（2023保存案例） | 移动测试工具图将静态分析/逆向APKTool/Qark/MobSF、动态Frida/Droidbox、代理Burp/Ratproxy、ADB和iOS日志/流量/动态工具混列；称APKiD检测恶意包不准确，指纹识别不等同恶意判断。 | [方法条目](../by-type/mobile-android.md) |
| 移动工具按静态动态代理及设备权限选择：iOS（2023保存案例） | 移动测试工具图将静态分析/逆向APKTool/Qark/MobSF、动态Frida/Droidbox、代理Burp/Ratproxy、ADB和iOS日志/流量/动态工具混列；称APKiD检测恶意包不准确，指纹识别不等同恶意判断。 | [方法条目](../by-type/mobile-ios.md) |
| 图像服务报告标题与SSRF初稿证据分离：脚本上下文（2023保存案例） | image.hackerone.live报告标题RXSS via url，但可读初稿写full read SSRF并提供外部URL，后续附件仅可见Multiple Choices上部。 | [方法条目](../by-type/xss.md) |
| 图像服务报告标题与SSRF初稿证据分离：服务端请求（2023保存案例） | image.hackerone.live报告标题RXSS via url，但可读初稿写full read SSRF并提供外部URL，后续附件仅可见Multiple Choices上部。 | [方法条目](../by-type/ssrf.md) |
| 源码端点抽取必须匹配部署与条件注册（2023保存案例） | Noir示意Source Code→Detector→Analyzer→Output/Deliver→ZAP/Burp，源码路由候选可带URL/method/params，但配置/条件注册/构建环境/部署版本可能不同。 | [方法条目](../source-audit.md) |
| 频道ID关联私有邮箱的对象权限验证（2023保存案例） | IBM video历史摘要确认channel ID导致customer email disclosure已修复，时间线评级从Critical调High/范围变化。 | [方法条目](../by-type/idor-access-control.md) |
| 协作者错误分支泄漏私有项目存在性（2023保存案例） | H1 collaborator邀请报错：private返回foo not invited to HANDLE which is a private program，public返回无适当访问。 | [方法条目](../by-type/info-secrets.md) |
| 构建残留OpenSSL配置路径的实际解析前提（2023保存案例） | Node18.4 Ubuntu64Docker startup尝试读构建残留/home/iojs/build/...openssl.cnf，作者明确尚未证明配置真的解析，只怀疑同机攻击者可控制该路径。 | [方法条目](../source-audit.md) |
| 临时目录API在实验权限模型中的验证遗漏（2023保存案例） | Node20实验permission model的fs.mkdtemp与sync缺getValidatedPath，摘要称可路径穿越创建任意目录，CVE2023-32003。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Buffer和string路径的权限验证一致性（2023保存案例） | Node20实验permission model filesystem API对Buffer形式路径处理不当，路径穿越绕过，CVE2023-32004。 | [方法条目](../by-type/lfi-path-traversal.md) |
| createRequire的策略调用者身份与模块边界（2023保存案例） | Node实验policy机制module.constructor.createRequire可冒充策略中其他模块身份加载policy.json之外模块，历史CVE2023-32006/16.x18.x20.x。 | [方法条目](../source-audit.md) |
| inspect无效IPv4解析和DNS重绑定链（2023保存案例） | Node --inspect历史CVE2022-32212，IsIPAddress未正确拒绝10.0.2.555类无效IPv4，浏览器按名称DNS解析，短TTL先返回外部再127.0.0.1，可读取/json的webSocketDebuggerUrl并尝试连调试器。 | [方法条目](../by-type/ssrf.md) |
| 活跃Agent计数不能替代任务结果和退出状态（2023保存案例） | ENSEMBLE Beta1 workspace Twitter Bug Bounty UI显示4ActiveAgents/0RunningJobs与地图，任务统计均0%。 | [方法条目](../experiment-design.md) |
| 单次SLEEP延迟截图缺少低影响时间对照（2023保存案例） | Burp q参数含SLEEP15嵌套SELECT，响应HTTP200右下15360ms；单样本延迟吻合但缺基线/无延迟条件/重复样本，缓存、网络和服务负载可混淆。 | [方法条目](../by-type/sql-injection.md) |
| 历史参数流水线的工具拼写和语义保留（2023保存案例） | 流程图从site/extphp→waybckurls拼写错误→grep问号→uro→httpx→nuclei fuzzing templates。 | [方法条目](../discovery/web-and-api.md) |
| 侦察路线图每一阶段必须有确认标准（2023保存案例） | WolfRecon路线图把域名枚举→httpx活性、Nuclei模板、Wayback普通/正则结果→XSS/SQL扫描与Google/GitHub检索连接。 | [方法条目](../discovery/web-and-api.md) |
| ImpressCMS管理参数SQLi的登录及配置前提（2023保存案例） | ImpressCMS1.4.3及之前历史报告步骤要求Admin登录，再针对system/admin.php fct=mimetype/op=mod/mimetypeid POST参数。 | [方法条目](../by-type/sql-injection.md) |
| OTP封面参数不足以证明完整电信ATO（2023保存案例） | Telecom ATO文章封面内嵌Burp仅见MA_VerifyOTP/forgetPassword、pin1–4/pin_input字段与拦截响应菜单，没实际响应/令牌或已登录结果。 | [方法条目](../by-type/authn-session.md) |
| 邮箱域Unicode规范化与Pendingapproval边界（2023保存案例） | 邀请界面拒绝@yopmail.com因组织域限制；正文声称将域中的i换成带点大写İ（yopmaİl），必须区分Unicode大小写折叠、NFC、IDNA/邮箱域投递，不默认是同一域。 | [方法条目](../by-type/authn-session.md) |
| 反射端点作为同源脚本的CSP挑战条件（2023保存案例） | 挑战解法把同一个PHP反射端点作为script src，第二请求input=alert(1)//响应脚本正文且弹1。 | [方法条目](../by-type/xss.md) |
| document.cookie弹窗不证明HttpOnly凭据可窃取（2023保存案例） | 搜索字段内闭合标签script片段，弹窗显示document.cookie中多种追踪/会话命名cookie。 | [方法条目](../by-type/xss.md) |
| APKiD保护指纹不等同恶意或漏洞判定（2023保存案例） | APKiD2.0测试APK输出anti_vm、anti_debug、compiler dx、manipulator dexmerge、packer Naga和anti_disassembly。 | [方法条目](../by-type/mobile-android.md) |
| 已废弃JS参数须区分客户端残留和服务端仍接受 | 从保存正文可提炼：旧JavaScript中的参数可能标记已移除UI功能，却仍被后端接受。 | [方法条目](../discovery/client-and-cloud.md) |
| 文件名HPP须比较验证器与落盘选择规则 | 同名filename参数重复时，入口校验与后端存储可能分别取首值、末值或合并数组，形成扩展名校验差异。 | [方法条目](../by-type/file-upload.md) |
| PDF目录候选须证明发票私有性和请求权限 | 正文称发现/pdf目录中的发票并快速分诊，图片只展示Directorylisting标题。 | [方法条目](../by-type/info-secrets.md) |
| 公开漏洞报告政策搜索只能生成候选项目 | 正文的submit vulnerability report与Bugcrowd/HackerOne平台文本搜索用于发现政策入口，减去news等只是降噪。 | [方法条目](../scope-and-rules.md) |
| Blind XSS标识文本与数字过滤不是通用规则 | 正文将含xss或数字的回连域均称错误，这只是可能遇到关键词过滤的假设。 | [方法条目](../by-type/xss.md) |
| JavaScript闭合片段应先按真实语法位置验证 | 保存片段含单引号、分号后未配对右括号，不能在脱离上下文时作为有效载荷。 | [方法条目](../by-type/xss.md) |
| 组织前缀自定义头只能按实际消费方验证 | 正文建议Origin失败后改x-组织-origin/host并推广到所有头。 | [方法条目](../by-type/host-header.md) |
| 隐藏参数的标签替换需要实际解析和可达性 | 正文称script被拦后换svg/onerror/onload成功，但保存图片只是报告列表。 | [方法条目](../by-type/xss.md) |
| 403目录下子路径枚举不能承诺总能绕过 | 正文建议403目录继续目录枚举；配图是敏感存储报告元数据。 | [方法条目](../by-type/idor-access-control.md) |
| 历史JSON Content-Type筛选只能定位内容候选 | Wayback URL经httpx状态/Content-Type过滤得到JSON候选，不证明其中含秘密或后台权限。 | [方法条目](../by-type/info-secrets.md) |
| SQLmap高风险枚举选项不能称基本配置 | 原帖同时列risk3/level5/threads10及users/passwords/dbs/DBA查询，测试强度和数据访问明显增加。 | [方法条目](../by-type/sql-injection.md) |
| 代理地址空格与实际请求留存须分别核对 | 保存SQLmap --proxy URI带多余空格，不应直接照抄。 | [方法条目](../experiment-design.md) |
| OTP响应泄漏与服务端接受需要同一事务证据 | 正文只有OTP leakage in response描述，配图仅报告评级。 | [方法条目](../by-type/authn-session.md) |
| DNS重绑定须核对校验和连接阶段的解析 | 禁用IP列表可能仅校验第一次域名解析，后续网络连接重新解析到受限地址。 | [方法条目](../by-type/ssrf.md) |
| X-Original-URL必须证明实际路由与业务权限 | 原帖把POST /admin/deleteUser403与POST /加X-Original-URL后的200当成功。 | [方法条目](../by-type/idor-access-control.md) |
| 子域关键字筛选的输入格式和覆盖遗漏 | subfinder -d需要域名而原帖传http://URL；dnsx输出字段与cut假设也需核对。 | [方法条目](../discovery/passive-and-services.md) |
| 报告数量和Accepted状态不能证明权限矩阵穷尽 | 正文强调重新看已有多人测试的应用访问控制；报告列表没有具体请求。 | [方法条目](../by-type/idor-access-control.md) |
| LIKE模式转义与SQL参数绑定是不同层 | WordPress esc_like主要处理LIKE模式中的通配/反斜杠，whereRaw是否危险取决于原始SQL拼接和绑定；缺某个函数不支持99%漏洞概率。 | [方法条目](../by-type/sql-injection.md) |
| Cookieless历史案例须限定.NET和IIS配置 | 两个保存帖介绍ASP.NET/IIS cookieless及历史CVE标题，其中可用截图给出(S(X))路径段差异。 | [方法条目](../by-type/idor-access-control.md) |
| 侦察工具源码可见不代表依赖和安装脚本安全 | WolfRecon“无加密代码”只改善可审阅性；Go安装示例将短链返回内容直接管道bash且固定旧版本。 | [方法条目](../source-audit.md) |
| 客户端expire_at修改不能证明服务端PIN超期接受 | 1691222861281的量级对应毫秒时间戳，换日期必须核对单位和时区。 | [方法条目](../by-type/authn-session.md) |
| 导出Receiver到私有偏好访问需完整调用链 | 导出广播接收器仅代表某种可达性，仍需Manifest权限、调用者限制、Intent extra类型、反序列化类路径和最终私有状态使用。 | [方法条目](../by-type/mobile-android.md) |
| JSpector端点候选与IDOR业务结果分开 | 正文称由JSpector发现API并报告IDOR，图片只有Critical/InfoDisclosure/$1500侧栏。 | [方法条目](../discovery/web-and-api.md) |
| 登录日志的私有字段暴露与Stored XSS是独立机制 | 正文提及cPanel日志含用户名/IP/结果/时间，以及将恶意用户名写入失败登录日志后影响日志查看者；图片只为报告标题，其中作者承认错图。 | [方法条目](../by-type/info-secrets.md) |
| Android iframe不能普遍同时造成LFI与Stored XSS | iframe指向/etc/hosts需要真实WebView渲染、有效file基准URL/文件访问设置和可读权限，且储存及其他用户可达性另需证明。 | [方法条目](../by-type/mobile-android.md) |
| POST反射XSS的跨用户投递不能省略请求条件 | 方法改写、CSRF和JSON伪装只是可能的投递候选，各依赖服务端接受方法、Content-Type/CORS、浏览器可发请求和受害者凭据策略。 | [方法条目](../by-type/xss.md) |
| 端口扫描速度宣传不证明覆盖完整 | 正文称65k端口3秒，截图没有运行结果。 | [方法条目](../targeted-fuzzing.md) |
| 包名识别不能代替Android备份权限验证 | aapt dump badging应指向实际APK文件，保存命令abc.ap可能是扩展名误写。 | [方法条目](../by-type/mobile-android.md) |
| 窄范围深挖和付费部署需明确业务及访问前提 | 对单应用建立角色、流程、状态和对象关系，比无限扩张侦察更容易形成可证伪假设。 | [方法条目](../hunting-strategy.md) |
| 不同子域或IP不自动构成两份独立漏洞 | 相同症状跨子域出现，须比较共享代码/部署配置、权限边界、数据及修复对象。 | [方法条目](../reporting.md) |
| 缺失token比较必须保留实际跨站凭据与状态 | 正文建议同时删除token名称和值，应分别比较缺字段、空值、错误值、其他事务值及正常值。 | [方法条目](../by-type/csrf.md) |
| 公开粘贴的第三方API密钥不作为可用凭据资料 | 保存帖包含第三方Shodan密钥，已读取但不复制到知识正文、不尝试使用。 | [方法条目](../by-type/info-secrets.md) |
| 移动端抽取路由加入Web词表前核对平台与范围 | Android/iOS包可能包含Web/API入口，可按包哈希、环境、基础URL、路径、方法和参数拆分并去重。 | [方法条目](../discovery/web-and-api.md) |
| GTM配置中的域名需关联具体容器和版本 | 仅在目标实际加载Google Tag Manager时，从已保存脚本/配置提取候选并记录容器ID、环境、版本及引用位置。 | [方法条目](../discovery/client-and-cloud.md) |
| 路径与自定义头403变200须比较各层路由 | 保存可用旧图列出路径编码、分号/斜线、头字段和200/302结果；复用原图审阅记录，当前文件`1690015216669495296-02.png`。 | [方法条目](../by-type/idor-access-control.md) |
| 403候选矩阵仍受具体资产和操作许可限制 | 当前绑定图`1690015216669495296-02.png`是历史头/编码路径矩阵，不给任何现实目标测试许可。 | [方法条目](../scope-and-rules.md) |
| Nginx alias遍历工具启发式须确认实际location配置 | navgix介绍heuristic/brute-force，只提供工具定位用途。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Liferay名称存储与注册末步反射是两条sink | 正文称姓名在他人访问profile时存储XSS，以及注册末步URL反射XSS。 | [方法条目](../by-type/xss.md) |
| Wayback脚本去重须保留完整URL和实际源码 | uniq在sort之前仅去相邻重复，筛.js也可能命中查询中的字样；python http://linkfinder.py是无效本地脚本路径形式。 | [方法条目](../discovery/client-and-cloud.md) |
| OTP字符串与布尔值必须严格校验类型 | 正文对比错误数字串403和otp=true200/resetToken，提示宽松类型转换或条件判断候选。 | [方法条目](../by-type/authn-session.md) |
| Safe Harbor等级不能替代响应SLA证据 | 正文将Safe Harbor Gold1解释为快速回复、周末处理和协作，但法律/许可条款与响应速度属于独立信息。 | [方法条目](../scope-and-rules.md) |
| 日志备份和配置后缀只生成有限待核对候选 | 正文列.gz/.bin/.log/.cache/.secret/.db/.backup/.bkp/.yml/.json/.txt/.rar/.zip/.config，grep片段用了弯引号且waybackruls拼写不准。 | [方法条目](../by-type/info-secrets.md) |

| 保存图证0187-1-xss：条件与证明边界 | 搜索字段闭合标签后弹document.cookie，目标被涂抹。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-2-xss：条件与证明边界 | 被遮挡站点的移动弹窗显示/xss/，没有原始邮箱请求或输出上下文。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-7-report：条件与证明边界 | Evidence页面有Start recording及Record with Audio开关，无录制结果。 | [方法条目](../reporting.md) |
| 保存图证0187-22-xss：条件与证明边界 | 另一尺寸被遮挡移动弹窗/xss/，仅执行效果，无原始邮箱值或sink。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-26-passive：条件与证明边界 | SubreconGPT示例以admin子域生成dev/qa/test/prod/secure猜测，仅test解析到192.0.2.123示例地址。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0187-27-sql：条件与证明边界 | Google样式搜索页q为单引号，页面出现MySQL syntax error文字；正文称旧子域，图地址却是www.google.com/search。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0187-31-business：条件与证明边界 | 网站测试表列Header/Footer布局、Logo跳转、导航/搜索、订阅邮箱校验、空值错误/成功确认、社交链接和断链。 | [方法条目](../business-modeling.md) |
| 保存图证0187-32-scope：条件与证明边界 | Moonpay更新图将*.plexlabs.io WILDCARD和plexlabs.io URL同时Added in Scope，但EligibleForBounty false。 | [方法条目](../scope-and-rules.md) |
| 保存图证0187-37-scope：条件与证明边界 | JohnDeere图列jdquote2/jdlink/salescenter/payload/partsadvisor/myjohndeere/jdwarrantysystem/developer八个deere.com精确URL新增，赏金false。 | [方法条目](../scope-and-rules.md) |
| 保存图证0187-40-auth：条件与证明边界 | ShopPay ATO文章截屏描述自有新商店账户、虚构地址，账号有普通Shop而无ShopPay，另方用相同邮箱+受控手机号注册ShopPay。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0187-42-xss：条件与证明边界 | 测试站attributeHtml参数body/onload片段先赋onerror再引用未定义x，弹框显示Uncaught ReferenceError:x is not defined。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-45-xss：条件与证明边界 | SnapNewsroom历史报告：国家/语言search q未净化，可插入带style绝对定位的外部链接并诱导点击。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-46-report：条件与证明边界 | 微软邮件写赏金资格3000美元，同时明确赏金审查不代表已修复或允许公开披露。 | [方法条目](../reporting.md) |
| 保存图证0187-53-secret：条件与证明边界 | 源码AccountSettings数组有随机_id、被遮挡accountId和USD/EUR。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0187-54-scope：条件与证明边界 | Aktia历史investors.aktia.com精确URL新增但Eligiblefalse，完整主机和资格分别核对，不继承给其他aktia域。 | [方法条目](../scope-and-rules.md) |
| 保存图证0187-58-xss：条件与证明边界 | Yelp报告摘要：guvo cookie回显进window.ySitRepParams和window.yelp.guv，部分未转义；后台cookie解析可将guvo夹入yelpmainpaastacanary，后者可由?canary=值设置。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-58-auth：条件与证明边界 | Yelp报告摘要：guvo cookie回显进window.ySitRepParams和window.yelp.guv，部分未转义；后台cookie解析可将guvo夹入yelpmainpaastacanary，后者可由?canary=值设置。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0187-60-lfi：条件与证明边界 | Node20实验permission模型中可访问的相对symlink经rename/link改变所在位置，解析目标随基准目录变化，示例rename到escape后readdir读父目录。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0187-67-source：条件与证明边界 | Cargo历史CVE2023-38497：UNIX-like解压crate直接保留归档权限而忽略umask，若本地其他用户可写缓存源码且系统无其他限制，可在下次编译/执行时修改依赖。 | [方法条目](../source-audit.md) |
| 保存图证0187-69-fuzz：条件与证明边界 | Ruby URI历史CVE2023-36617是CVE2023-28755修复不完整，rfc2396/rfc3986 parser处理特定非法URL耗时增长；图推荐uri0.12.2/0.10.3按Ruby系列。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0187-70-deser：条件与证明边界 | Kredis JSON历史CVE2023-27531，特制JSON可产生意外对象，Fixed1.3.0.1，截图VersionsAffectedAll是公告当时概括。 | [方法条目](../by-type/deserialization-rce.md) |
| 保存图证0187-71-fuzz：条件与证明边界 | Rack header parsing历史CVE2023-27539，影响>=2.0.0，修复2.2.6.4/3.0.6.1，特制头解析耗时异常。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0187-75-crlf：条件与证明边界 | TikTok Seller hack_redirect_now输入校验不足可能响应拆分，摘要并列反射XSS/cookie与开放重定向；时间线Duplicate#2007093、评级变更/后续reopen，下部截断。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图证0187-75-xss：条件与证明边界 | TikTok Seller hack_redirect_now输入校验不足可能响应拆分，摘要并列反射XSS/cookie与开放重定向；时间线Duplicate#2007093、评级变更/后续reopen，下部截断。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-75-redirect：条件与证明边界 | TikTok Seller hack_redirect_now输入校验不足可能响应拆分，摘要并列反射XSS/cookie与开放重定向；时间线Duplicate#2007093、评级变更/后续reopen，下部截断。 | [方法条目](../by-type/open-redirect.md) |
| 保存图证0187-77-source：条件与证明边界 | 自托管GitLab /explore可列公开或当前用户可访问项目，建议查秘密/内部资产。 | [方法条目](../source-audit.md) |
| 保存图证0187-81-deser：条件与证明边界 | H1Disclosed转发Kredis JSON公告，小图可读固定1.3.0.1、特制JSON可能产生意外对象，未增加gadget/RCE条件。 | [方法条目](../by-type/deserialization-rce.md) |
| 保存图证0187-83-takeover：条件与证明边界 | S3接管邮件上部：CNAME指S3 bucket并混称publiclyaccessible/claim与存储数据访问，右侧/目标截断。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0187-84-deser：条件与证明边界 | Kredis v1.3.0 type/json.rb可读cast_value(value)直接JSON.load(value)，报告指出意外class反序列化CVE2023-27531。 | [方法条目](../by-type/deserialization-rce.md) |
| 保存图证0187-85-lfi：条件与证明边界 | LFI Finder迭代不同../深度读取etc/passwd并标红VulnUrl，画面没有响应内容。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0187-86-report：条件与证明边界 | YesWeHack回复能复现，因原报告已Resolved所以Accept新报告且eligible奖励。 | [方法条目](../reporting.md) |
| 保存图证0187-97-source：条件与证明边界 | Node历史CVE2023-32002，Module._load绕过实验policy.json模块限制，影响公告当时16.x/18.x/20.x。 | [方法条目](../source-audit.md) |
| 保存图证0187-98-iot：条件与证明边界 | MarioKart8DX/8 metadata validation2历史图说Switch2.3.0于2023-03-09修复、WiiU4.2/internalv81于2023-08-03修复；比赛SimpleSearchObject metadata的ID2name/4description/7-8team/3icon，弱点ArrayIndexUnderflow。 | [方法条目](../by-type/iot-security.md) |
| 保存图证0187-99-iot：条件与证明边界 | 另一MarioKart metadata parsing报告弱点NULLPointerDereference，Switch2.2/internal851968于2022-12-07、WiiU4.2/internal81于2023-08-03修复。 | [方法条目](../by-type/iot-security.md) |
| 保存图证0187-101-auth：条件与证明边界 | 2FA思维图分Setup/Bypass/Disable，列密钥轮换/启用后仍获取、旧会话、邮箱校验、IDOR、响应泄码/复用/预算/旧码失效、空值/JSON类型/直接请求/sessionpermission/SMS↔email/OAuth/timeout及CSRF/click/backupcode/passwordreset/reconfirm禁用。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0187-103-passive：条件与证明边界 | ffuf示例将FUZZ放一级/中间子域并变8443端口，匹配200/403，却缺-w词表参数。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0187-107-xss：条件与证明边界 | Octagon挑战地址name含script src同源/blog/wp-json/wp/v2/users/1...，弹[object Object]。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-111-access：条件与证明边界 | Rockstar摘要：未授权用户删除任意Crew给任意SocialClub用户的未决邀请；服务端补检查原邀请发送者或该Crew授权成员。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0187-113-auth：条件与证明边界 | 转发图完整列复制自己cookie→logout→恢复cookie→刷新并称sessionhijacking，另列email编码SVG弹窗。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0187-113-xss：条件与证明边界 | 转发图完整列复制自己cookie→logout→恢复cookie→刷新并称sessionhijacking，另列email编码SVG弹窗。 | [方法条目](../by-type/xss.md) |
| 保存图证0187-114-graphql：条件与证明边界 | Graphinder说明-d域名/-s脚本/-b目录/-p precision、默认bruteforce和script开启、可-f域列表。 | [方法条目](../by-type/graphql.md) |
| 保存图证0187-118-scope：条件与证明边界 | IBM政策范围表：Products与Websites类型Other，Inscope/Critical/Ineligible，网站描述*.ibm.com或ownedbyIBM另举weather等，页底第三行截断。 | [方法条目](../scope-and-rules.md) |
| 保存图证0187-121-records：条件与证明边界 | Amass/OAM循环：Retrieval范围种子→Discovery采集准备→Store数据库→Notify新/变资产。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0187-121-source：条件与证明边界 | Lua扩展vertical(ctx,domain)将output_dir/assetfinder --subs-only与domain拼接后io.popen，逐行new_name再close。 | [方法条目](../source-audit.md) |
| 保存图证0187-121-passive：条件与证明边界 | Dangling PTR示例join assets/relations筛ptr_record、namespace LIKE %owasp.org并NOTIN已有A/AAAA/CNAME from_asset。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0187-124-access：条件与证明边界 | 报告标题显示alerts/<ALERT-ID>/cancel路径，目标涂抹，正文两个账号替换ID。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0187-125-access：条件与证明边界 | 本地crawl列表grep alerts可见activate/cancel/edit不同ID，目标大部遮挡。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0187-129-passive：条件与证明边界 | Shodan http.favicon.hash:309020573历史图144结果含不同组织及证书/时间/HTTP头。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0187-131-web：条件与证明边界 | gospider -S domain.txt -t3 -c100管道tr/grep排除.js、筛HTTPS含=再qsreplace生成SVG onload URL。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0187-135-passive：条件与证明边界 | 反向WHOIS图建议以主域注册邮箱找更多域。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0187-136-web：条件与证明边界 | Nuclei headless extractURLs示例navigate BaseURL/waitload/script/querySelectorAll src href url action属性集合返回/kv extractor。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0187-136-source：条件与证明边界 | Nuclei AI文档称解读用户报告再生成复现模板、用公共模板/CVE数据；AI Assistance编辑器无实际结果。 | [方法条目](../source-audit.md) |
| 保存图证0187-136-experiment：条件与证明边界 | AI模板文档列详细POC、理解格式、Validation/Linting、TestTemplate和ReviewMatchers/knownvulnerabletargets；例提示/redirect?url外部域底部截断。 | [方法条目](../experiment-design.md) |
| 保存图证0187-148-csrf：条件与证明边界 | 删除账号界面要求输入 delete 并点击按钮。 | [方法条目](../by-type/csrf.md) |
| 保存图证0187-154-auth：条件与证明边界 | 示意图比较 GET /ResetPassword 与 /ResetPassword.json：均为 200，后者含 success 和 token。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0187-158-takeover：条件与证明边界 | Webflow 自定义子域接管报告展示 Unclaimed 描述、Resolved 状态及部分服务解释，目标涂抹，证明部分被底部裁切。 | [方法条目](../by-type/subdomain-takeover.md) |
| 搜索和邮箱输入的上下文探针：从弹窗到真实执行位置（0187） | 保存帖展示关闭 script 或邮箱引号编码加 SVG onload 的探针，邮箱例含 `%27`、反斜线、`%22`、`%3E%3Csvg`。 | [方法条目](../by-type/xss.md) |
| API、路径和功能入口的分层发现（0187） | 从 Swagger、接口字典、现有页面、JavaScript、历史 URL 和公司公开代码整理候选，按子域/IP/端口、技术、目录文件、API/参数、功能、脚本和截图保存可追溯产物。 | [方法条目](../discovery/web-and-api.md) |
| files.md5 与 SQL 备份曝光的逐层确认（0187） | 保存帖将 `/files.md5` 列表与 `/db/sqlsrv/full.sql` 联系起来，并声称含客户端 ID 和 secret。 | [方法条目](../by-type/info-secrets.md) |
| URL 型参数与令牌路由只构成入口候选（0187） | `dest`、`redirect`、`uri`、`path`、`continue`、`url`、`window`、`next`、`data`、`site` 等参数先区分服务端请求、浏览器跳转、路径选择与普通数据。 | [方法条目](../by-type/ssrf.md) |
| 公开域名线索、模型猜测和归属确认（0187） | 公开搜索、证书透明度、反向 WHOIS、favicon 哈希和模型生成的相似子域产生候选。 | [方法条目](../discovery/passive-and-services.md) |
| 退出后恢复自己的 Cookie：会话注销检查（0187） | 先登录自有账号保存测试会话，正常退出，再恢复同一会话并发起可证明当前身份的服务端请求。 | [方法条目](../by-type/authn-session.md) |
| 保留历史目录结果以便版本条件重查（0187） | 保存目录侦察的路径、时间、响应指纹、范围及技术版本，再用新漏洞的受影响条件筛选旧结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 历史归档与压缩包扩展名筛选的证据边界（0187） | 从 wayback、爬虫结果中筛选 `.gz`、`.bin`、`.log`、`.cache`、`.secret`、`.db`、备份、配置、JSON、文本和压缩包，只形成待核对列表。 | [方法条目](../by-type/info-secrets.md) |
| 客户端 ID 与 secret 的用途及暴露等级（0187） | 发现 `client_id` 或 `client_secret` 后，先识别它是否属于 OAuth、客户端类型、预期公开程度、服务端信任与实际权限。 | [方法条目](../by-type/oauth-oidc.md) |
| 按用户流程建立功能和状态检查表（0187） | 以单一授权项目的正常流程为基线，走查导航、搜索、订阅、表单校验和关键业务操作；保存输入、所属角色、预期状态及实际响应。 | [方法条目](../business-modeling.md) |
| 按阶段选择工具并保留真实产物（0187） | 将端口/服务发现、参数发现、目录枚举、公开资产数据和 HTTP 分析分别绑定到可核对的输入输出。 | [方法条目](../hunting-strategy.md) |
| 切换媒体类型与 SVG 上传的实际 XML 解析条件（0187） | JSON 或表单接口只有在确实选择 XML 解析器时，媒体类型变化才有意义；保存帖 `applcation/xml` 拼写不完整，实际请求需符合目标接受的类型和结构。 | [方法条目](../by-type/xxe.md) |
| Shop Pay 与普通 Shop 身份绑定的最小链条（0187） | 保存图证区分普通 Shop 和尚未启用 Shop Pay 的客户，围绕邮箱、手机号、登录完成及 Shop Pay 会话交换展示特定链条。 | [方法条目](../by-type/authn-session.md) |
| 按原始字节和解析上下文验证 WAF 差异（0187） | Cloudflare 示例通过 body onload 中设置 onerror 后引用未定义变量触发错误；BIG-IP 示例在 `+ontoggle` 前加分号，可能改变 WAF 与浏览器的属性解析。 | [方法条目](../by-type/waf-bypass.md) |
| 搜索结果 HTML 注入与脚本执行分开证明（0187） | Snap Newsroom 的 q 输入图证展示链接和样式注入，可影响页面呈现并产生仿冒风险。 | [方法条目](../by-type/xss.md) |
| 奖励、受理、Resolved 与实际修复分开记录（0187） | 奖励邮件说明受理或付款，Resolved、accepted、patching 等标签说明平台状态。 | [方法条目](../reporting.md) |
| 公开代码里的硬编码 ID 与真正敏感信息（0187） | 人工查看公司代码、AccountSettings 配置与 GitLab `/explore` 项目时，先确认公开可见是否符合预期、代码版本、目标归属和字段用途。 | [方法条目](../source-audit.md) |
| 上传后缀、处理器映射和空字节的版本条件（0187） | 保存帖建议 IIS 的 `.cer`/`.asa` ASP 映射、`.eml` 配合 `text/html` 以及 `shell.php%001.jpg`。 | [方法条目](../by-type/file-upload.md) |
| Cookie 派生查询数据进入 DOM 的数据流追踪（0187） | Yelp 图证把 guvo Cookie、canary 派生查询、解析和 JavaScript 插入点串联起来。 | [方法条目](../by-type/xss.md) |
| Node 实验权限模型中的相对链接与路径边界（0187） | 保存报告讨论 Node 20 实验权限模型与相对符号链接、rename/link 的基准路径。 | [方法条目](../by-type/lfi-path-traversal.md) |
| Protobuf 转 JSON 后仍需保留真实传输语义（0187） | ProtoBurp 线索适用于先识别 protobuf 消息边界、字段号、wire type、描述信息及实际 HTTP/gRPC 传输，再把可控字段转换为易观察形式。 | [方法条目](../discovery/web-and-api.md) |
| 延迟 Blind XSS 的归因和输入预算（0187） | 公司字段中的探针在数日后触发时，使用每入口唯一的无敏感标记关联提交时间、字段、账号和触发页面；时间接近不能单独归因。 | [方法条目](../by-type/xss.md) |
| 工作任务、邀请和提醒 ID 的状态授权对照（0187） | 建立两个自有账号的对象：未分享工作任务、待处理 Crew 邀请或邮件提醒。 | [方法条目](../by-type/idor-access-control.md) |
| Cargo 解压权限与本地构建缓存风险（0187） | 图证 CVE-2023-38497 围绕归档解压权限和缓存中的本地可写内容。 | [方法条目](../source-audit.md) |
| 多仓库变体搜索要从可到达数据流出发（0187） | 将已知缺陷抽象为输入来源、危险操作、缺失校验和版本条件，再在同类仓库搜索语法和数据流变体。 | [方法条目](../source-audit.md) |
| URI 与 Rack 的历史 ReDoS：隔离性能对照（0187） | URI CVE-2023-36617 图证涉及早期 CVE-2023-28755 修复不完整和 RFC2396/RFC3986 非法 URL；Rack CVE-2023-27539 涉及特定请求头解析，保存版本从 2.0 起及修复 2.2.6.4/3.0.6.1。 | [方法条目](../targeted-fuzzing.md) |
| JSON.load 与 gadget 链的实际可到达条件（0187） | Kredis CVE-2023-27531 图证展示旧版类型转换中的 `JSON.load(value)`，公告指出构造 JSON 可恢复意外对象，修复为 1.3.0.1。 | [方法条目](../by-type/deserialization-rce.md) |
| 延时注入要验证数据库语法与时间因果（0187） | `WAITFOR DELAY` 是 SQL Server 语法；页面为 ASP 不证明后端使用 SQL Server。 | [方法条目](../by-type/sql-injection.md) |
| 同一页面的 CRLF、XSS 和跳转分别验证（0187） | TikTok 相关保存摘要列出三类发现及 duplicate/timeline 标签。 | [方法条目](../by-type/crlf-response-splitting.md) |
| etcd 2379 与历史 v2 API 暴露的最小检查（0187） | 保存帖给出 `:2379/v2/keys/?recursive=true`。 | [方法条目](../cloud/container-k8s-security.md) |
| WebLogic 部署配置暴露与任意文件读取的区分（0187） | `.//META-INF/MANIFEST.MF`、`.//WEB-INF/web.xml`、`portlet.xml` 和 `weblogic.xml` 是保存帖的候选路径。 | [方法条目](../by-type/lfi-path-traversal.md) |
| S3 与 Webflow 接管的绑定能力证据（0187） | 缺失 bucket、unclaimed 页面或自定义域未绑定只是候选，分别核对 DNS、当前服务响应和第三方资源的可声明条件。 | [方法条目](../by-type/subdomain-takeover.md) |
| LFI 工具命中要读响应与阴性基线（0187） | LFI Finder 输出展示 traversal 探针与成功标签。 | [方法条目](../by-type/lfi-path-traversal.md) |
| OpenRedireX 的多跳跳转与 URL 解析差异（0187） | 复用已读原图 `1691769120289882121-02.jpg`：工具例包含三个 URL、44 个 payload，以及 logout/redirect_uri 跳转链，局部 INFO 与最终 FOUND 对应不同阶段。 | [方法条目](../by-type/open-redirect.md) |
| 修复后的相邻入口与重复根因判断（0187） | 同一 WAF 绕过、公开 Git 或敏感数据问题出现在多个子域和参数时，先确认各入口是否受同一部署、配置和权限边界影响。 | [方法条目](../hunting-strategy.md) |
| 外部 iframe 与 DOM 数据源的正确分类（0187） | `<iframe src=//0e.vc>` 可加载外部内容，但子框架的脚本通常不在父页面源执行；需另证 sandbox、源关系或消息信任问题。 | [方法条目](../by-type/xss.md) |
| JWT 签名、算法与 kid 的独立信任边界（0187） | 分别检查服务端是否验证签名、固定允许算法、使用匹配密钥并验证 issuer/audience/时间条件；kid 仅能选择受信密钥，不能直接作为任意文件路径。 | [方法条目](../by-type/jwt.md) |
| 正则匹配 ID 与秘密字段的误报控制（0187） | 正则命中 key/password/token 等赋值前缀或 email/name/ID 参数，只提示检查位置。 | [方法条目](../by-type/info-secrets.md) |
| 匿名 FTP 的读取和写入权限逐项确认（0187） | 匿名登录需核对实际客户端选项和服务端响应，保存帖 `ftp -A` 不能保证所有实现具有同样含义。 | [方法条目](../discovery/passive-and-services.md) |
| 负价格与购物车服务端总额一致性（0187） | 保存帖示例把价格 10 的商品与价格 -9 的商品组成总额 1。 | [方法条目](../by-type/business-logic.md) |
| Node Module._load 策略绕过与权限模型区分（0187） | 保存图证 CVE-2023-32002 涉及 Node 16/18/20 的实验策略机制与 Module._load。 | [方法条目](../source-audit.md) |
| 游戏元数据校验与解析缺陷的版本定位（0187） | MK8DX 两张保存公告分别讨论 metadata validation 2 的数组下溢与解析阶段空指针，涉及不同字段、Switch 与 Wii U 构建及不同修复时间。 | [方法条目](../by-type/iot-security.md) |
| 2FA 生命周期检查的状态矩阵（0187） | 以注册/绑定、启用、登录挑战、可信设备、恢复/备份码、重置、禁用与会话存续为轴，比较拥有者、低权限身份与未经挑战会话。 | [方法条目](../by-type/authn-session.md) |
| 执行 JavaScript 的服务端浏览器与本地 WebSocket（0187） | 先证明所谓 SSRF 实际进入会执行 JavaScript 的服务端浏览器，再核对该环境网络可达的本地 WebSocket、握手 Origin 校验、认证及消息权限。 | [方法条目](../by-type/ssrf.md) |
| CSP self 与同源 WordPress JSONP 的具体条件（0187） | 保存代码含原样输出 name 的 HTML 注入点及 `script-src self`、`object-src none`；另一图引用同源 `/blog` WordPress users 路由与被裁切的回调地址。 | [方法条目](../by-type/xss.md) |
| Graphinder 默认发现行为与明确请求预算（0187） | 保存帮助图提供目标域、文件、脚本、字典和代理等参数，并说明默认暴力路径与 JavaScript 扫描。 | [方法条目](../by-type/graphql.md) |
| 范围导出与平台范围表的时点核对（0187） | 公开子域列表、CyberChef 处理或 bbscope 账号范围导出都只用于整理候选。 | [方法条目](../scope-and-rules.md) |
| 资产关系图的生命周期和不完整性（0187） | Amass Workshop 图证展示发现、检索、存储、通知及 FQDN/IP/netblock/ASN/RIR/组织关系与首次/最后时间。 | [方法条目](../discovery/records-and-incremental.md) |
| Lua 资产收集插件的命令拼接审计（0187） | 保存 Lua 代码将输出目录、assetfinder 和 domain 拼接后交给 io.popen。 | [方法条目](../source-audit.md) |
| URL 汇总、参数替换与 headless DOM 提取（0187） | xurlfind3r 的 Wayback/Git/URLScan 汇总及 gospider→筛选→qsreplace 管线输出候选 URL；保留来源时间、查询键重复、编码和去重语义。 | [方法条目](../discovery/web-and-api.md) |
| 邮箱复用和权限降低后的身份索引失效（0187） | 邮箱场景：自有 A 将邮箱 a 改为 b，自有 B 从 c 改为重新可用的 a，再注销/登录比较不变账号 ID 与资源归属。 | [方法条目](../by-type/authn-session.md) |
| 异常 PUT 响应中的 bucket 名称只是服务线索（0187） | 保存帖建议带 `%c0` 的 PUT 触发错误并观察 S3 bucket 信息。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| AI 生成检测模板的正反例和行为检查（0187） | 将保存报告转成模板前，明确入口、版本、请求结构、所需认证和能够区分漏洞的 matcher。 | [方法条目](../experiment-design.md) |
| SSRF 升级影响必须补齐独立链条（0187） | 保存帖只询问 CVE-2021-24243 是否可从 SSRF 提升到 XSS，未提供完整证明。 | [方法条目](../impact-and-acceptance.md) |
| 删除确认页面与跨站操作能力分开核对（0187） | `deletion_confirmation.js` 显示删除页可能源于路由回退；“输入 delete”也可能只发生在前端。 | [方法条目](../by-type/csrf.md) |
| ResetPassword.json 返回令牌的能力验证（0187） | 保存图比较 GET `/ResetPassword` 与 `.json` 版本，后者示意 `success:true` 与 token。 | [方法条目](../by-type/authn-session.md) |

| 保存图证0188-2-access：机制与验证条件 | Radancy报告称单一公开链接可搜索png/user并下载上传文件、访问XML。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-3-secret：机制与验证条件 | Mantra终端从js.txt读取输入并标出JS地址旁脱敏键值。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0188-9-cors：机制与验证条件 | Radancy报告显示带Origin example.com的sockjs POST请求，但响应头与可读取数据位于裁切外。 | [方法条目](../by-type/cors.md) |
| 保存图证0188-11-records：机制与验证条件 | Wayback CDX原始多行有urlkey、2014/2015时间、原始URL、text/html、200、摘要和长度；多个时间共享摘要。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0188-12-ssrf：机制与验证条件 | backend/bffwa?path指向169.254.169.254/latest/meta…，页面显示AWS-HMAC临时凭据结构Code Success/LastUpdated/Expiration，敏感值遮挡，路径末尾裁切。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0188-12-impact：机制与验证条件 | 同案例评论研究者声称AWS凭据即完全访问实例，平台将High改Medium5.3并称键只能在该机器使用，随后奖励Resolved。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0188-20-access：机制与验证条件 | 开放注册editor可编辑内容并披露25k邮箱的报告摘要、P1变更；没有请求和数据，需角色默认值、注册校验与两个自有主体的权限对照，数量/评级非证明。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-28-scope：机制与验证条件 | 搜索项目用responsible disclosure、report security vulnerability、powered by hackerone、bug bounty、reporting policy等词。 | [方法条目](../scope-and-rules.md) |
| 保存图证0188-30-xss：机制与验证条件 | image.hackerone.live url参数RXSS复测图含Safari弹窗及Accept差异：Safari无image/avif,image/webp，Chrome/Firefox包含。 | [方法条目](../by-type/xss.md) |
| 保存图证0188-36-oauth：机制与验证条件 | Nextcloud user_oidc CVE-2023-39953说明token issuer须匹配discovery issuer，与aud检查类似；作者明确没有OIDC环境验证且其他问题未核实，MITM影响仅声明。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0188-37-oauth：机制与验证条件 | Nextcloud CVE-2023-39954区分公开client ID与私有client secret，明文DB快照读取可导致服务端冒名；secret需要原值不能简单hash替代，需独立密钥加密静态存储及DB/应用权限边界。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0188-38-access：机制与验证条件 | Nextcloud Text CVE-2023-39961：user0分享图片文件夹但不允许下载，user1新建文本插图可下载预览，对常见类型AttachmentController可请求原图。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-40-xss：机制与验证条件 | URL参数带引号/脚本片段写入iframe src及JavaScript脚本src字符串，代码左/右裁切，实际执行未展示。 | [方法条目](../by-type/xss.md) |
| 保存图证0188-41-impact：机制与验证条件 | Uber摘要确认PhpDebugBar暴露凭据并曾登录，但强调开发中实例无真实数据、未连生产，保密/完整性影响低；侧栏Critical9.1与标题production冲突。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0188-42-xss：机制与验证条件 | 图列换行/percent编码javascript scheme和属性拼接top[ale+rt]、document/domain。 | [方法条目](../by-type/xss.md) |
| 保存图证0188-45-access：机制与验证条件 | LinkedIn草稿job直接查看报错但flag/report端点接受草稿ID，后续TrustSafety通知泄露部分草稿细节。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-46-logic：机制与验证条件 | LinkedIn Premium价格篡改摘要确认个人账号大折扣，其他账号未受影响；side IDOR/High不说明具体参数。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0188-47-access：机制与验证条件 | 未验证邮箱用户在normFirstPartyArticle API403及UI缺失，而POST /voyager/api/publishing/contentSeries据称可创建newsletter。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-48-access：机制与验证条件 | 精选图片删除以ImageId/ProfileId绑定主体，两个标识在公开图片链接中可获，不必暴力枚举。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-49-access：机制与验证条件 | 超级管理员降为analyst但原页面未刷新，仍能发布的报告步骤。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-55-passive：机制与验证条件 | 在线SubdomainFinder展示uber368条部分列表，数据来源/时间和解析未显示。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0188-58-passive：机制与验证条件 | Rayder0.0.3按TARGETS_FILE/RATE40000/OUTPUT_DIR运行masscan→generate-output→save，输出http/https IP。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0188-60-cache：机制与验证条件 | Glassdoor GET test.js?cb=1含X-Forwarded-Scheme http、X-Forwarded-Host受控域，报告称缓存跳转JS。 | [方法条目](../by-type/cache-deception.md) |
| 保存图证0188-62-scope：机制与验证条件 | 历史PlayStation新增ca.account.sony.com、my.account.sony.com均URL bountyeligible true；资产新增与资格分字段记录，当前范围需重核不作为现行授权。 | [方法条目](../scope-and-rules.md) |
| 保存图证0188-65-web：机制与验证条件 | robots.txt显示openresty404HTML源码，状态行未见；须真实状态/软404对照。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0188-68-lfi：机制与验证条件 | FileMage CVE39026模板GET /mgmnt/后编码反斜线../链指向programdata/filemage/gateway/config.yaml，匹配body user/filemage/localhost且200。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0188-83-auth：机制与验证条件 | Burp前9请求200后429、Retry-After51，uvicorn JSON响应；证明按请求节流线索，图没见同一请求邮件数组或实发数量。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0188-84-secret：机制与验证条件 | AWS GitHub查询覆盖amazonaws/aws_access_key_id/aws_secret/aws_token/连接RDS密码/bucket/S3_endpoint及org限定，配置字段/资源名/示例不同于有效秘密；记录所属repo版本、上下文和脱敏证据，不使用命中键。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0188-85-source：机制与验证条件 | Airflow JDBC Provider CVE-2023-22886 before4.0.0，Connection URL不限制可控驱动参数，可能通过不同driver执行代码提升到服务端权限。 | [方法条目](../source-audit.md) |
| 保存图证0188-86-source：机制与验证条件 | Airflow ODBC Provider CVE-2023-34395 before4.0.0，OdbcHook可控driver参数加载动态库，4.0.0起仅hook constructor设driver。 | [方法条目](../source-audit.md) |
| 保存图证0188-87-passive：机制与验证条件 | realm -d example.com -n3递归证书DNS名示例重复遍历com/org/edu/net八名字。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0188-88-access：机制与验证条件 | WordPress开放注册报告自称可上传shell/编辑删除所有内容但实际正文只叙述注册enabled，New/High未核实。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-90-crlf：机制与验证条件 | Rayder子域→HTTP→CRLF探测示例含多个编码换行/Set-Cookie标记，ERR与VLN并存。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图证0188-91-passive：机制与验证条件 | httpx1.1.2输出404GitHubPages、200API/docs、301support等技术标题；HTTP活性与DNS解析、非Web服务活性不同，404/301也应保留，技术猜测需独立核对。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0188-93-logic：机制与验证条件 | 评分UI显示14.1/5orders，正文说系统应最多5但续篇未保存；可能显示/聚合/服务器范围校验问题。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0188-97-records：机制与验证条件 | realm默认93条vs-n5 385条，首个命令sort -u > tee before.txt使用重定向而不是｜tee，不能原样认定before文件有输出；比较深度应同源同时间去重/失败账本，结果跨根域需再核范围，不单以计数推更全面。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0188-103-xss：机制与验证条件 | PHP代码htmlentities token后去\n和\0但留\r，把input同时放Content-Disposition filename及JS TOKEN字符串。 | [方法条目](../by-type/xss.md) |
| 保存图证0188-105-auth：机制与验证条件 | Crowdsignal分享结果密码POST无尝试限制的报告，公开分享URL被抓取与口令猜测风险独立；需自有受控分享页、有限错码/预算与授权读成功对照，没密码的公开分享可能是预期。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0188-106-ios：机制与验证条件 | PowerShell脚本用Frida列PID/Identifier并要求目标Identifier，底部注入/返回裁切。 | [方法条目](../by-type/mobile-ios.md) |
| 保存图证0188-107-secret：机制与验证条件 | BackupFinder显示40788/40900、localhost HEAD请求多200长度0和htaccess403，旧/zip/git/idea路径。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0188-108-ssrf：机制与验证条件 | ipfuscator1.0.0把127.0.0.1生成为整数/hex/octal/短形式/IPv4mappedIPv6等，curl本地200只能证明该客户端解析。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0188-109-fuzz：机制与验证条件 | 邮箱图列XSS/SSTI/SQLi/SSRF/HPP不同探针，所谓全部valid并不可靠：域名嵌script不合法，quoted localpart/注释取决解析器；外域邮件DNS/SMTP回连≠HTTPSSRF，email=串需具体表单解码。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0188-112-passive：机制与验证条件 | 另一尺寸httpx1.1.2同200/301/404技术列表，保留自己的source；不筛掉非200/非HTTP记录，DNS解析与应用可达分层。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0188-115-secret：机制与验证条件 | Index /.git显示HEAD/config/index/objects/refs/logs及2014时间，目录可见和完整对象可读取不同；只最小脱敏证据检查当前私有代码边界，不由名称认为已有凭据。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0188-116-sql：机制与验证条件 | UNION INTO OUTFILE片段将PHP shell写到var/www/html，图只有SQL字符串没有响应/执行。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0188-117-web：机制与验证条件 | Telegram截图机器人接收URL、/scan排队并返回Cloudflare检查页，OBS录屏和子域列表无漏洞。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0188-121-access：机制与验证条件 | HackerOne员工说明program members/Triage能edit information修改原始报告（包括disclosed），示例改变后已恢复；其他program仅推测。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-122-secret：机制与验证条件 | 另一尺寸/.git目录图，HEAD/config/index/objects/refs等与2014时间，不证明当前私有源码或秘密；需权限/内容证据。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0188-123-xss：机制与验证条件 | inDrive促销按driver ID查询，POST api/spreadsheet/promocodes可把activationDate存脚本，同ID后查询触发。 | [方法条目](../by-type/xss.md) |
| 保存图证0188-125-sql：机制与验证条件 | localhost/sqli/login.php显示Welcome admin及拼接SELECT username/password，输入为/1#反斜线模式；页面查询与欢迎文本只是练习线索，需明确SQL引号/反斜线模式、数据库版本和服务端真实身份，对照参数绑定反例，不能移植通用登录绕过。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0188-126-android：机制与验证条件 | Rayder0.0.4 APK threads.apk经Apktool2.5.0解析资源/manifest/dex后抽URL，输出含Android文档/Apple/Wikipedia/FB/第三方。 | [方法条目](../by-type/mobile-android.md) |
| 保存图证0188-128-hrs：机制与验证条件 | Node llhttp CVE-2023-30589接受单CR分隔header，公告列当时v16/v18/v20且摘要20.2.0；前后端请求边界不一致是HRS前提。 | [方法条目](../by-type/request-smuggling.md) |
| 保存图证0188-130-fuzz：机制与验证条件 | Airflow before2.6.3 已认证用户构造regex输入令当前request挂起，作者称代理队列可能连带冻结到超时但没展示队列实验；须区分单请求/worker/全服务资源影响，隔离限时性能对照，不生产DoS。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0188-131-report：机制与验证条件 | Apple邮件称计划未来安全更新且要求更新前保密；计划≠发布/修复验证≠允许披露，保留reportID隐私，正文无漏洞细节不補造。 | [方法条目](../reporting.md) |
| 保存图证0188-132-sql：机制与验证条件 | 邮箱格式矩阵所有普通校验status字段200但message不同；空格/未引用括号Badformat，quoted括号返回Email invalid说明进入后续检查，Valid列是作者标签不等账号有效。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0188-136-strategy：机制与验证条件 | 完整25项侦察/检查清单含CNAME/Wayback/ports/Git/CORS/email SMTP Host/iframe/access/BurpHistory/Arjun/CSRF/SSRF/XSS/SSTI/reset token/unicode/rateheaders/dir/HRS/redirect/socialstate/upload/buffer。 | [方法条目](../hunting-strategy.md) |
| 保存图证0188-137-sql：机制与验证条件 | Burp Collaborator HTTP GET output=nt%20service%5Cmssqlserver、WindowsPowerShell UA，时间2021片段。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0188-138-access：机制与验证条件 | v2/applications GET带Bearer、Origin/referrer遮挡；身份和租户必须与v1保持同一，不能仅URL版本判授权差。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0188-140-report：机制与验证条件 | 邮件声称成功resolved并请求研究者复测后反馈分配奖励；修复声明与复测证据分开，有限范围自有样本/原始与fixed对照，邀请复测不等全部资产授权。 | [方法条目](../reporting.md) |
| 保存图证0188-149-report：机制与验证条件 | HackerOne PDF导出redactnames摘要提用户名结尾点号边界；报告正文另提仅agree goingpublic/reportbecamepublic活动、无评论的团队成员仍显示。 | [方法条目](../reporting.md) |
| 保存图证0188-150-waf：机制与验证条件 | 原始img onerror查询被Cloudflareblock，正文另称加on0x=1绕过；图只阻挡基线。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0188-152-logic：机制与验证条件 | 币种修改经验称平台要求完成购买，作者选UGX并说200UGX约0.05USD，支付渠道是否接受与历史汇率不能作为当前事实。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0188-153-xss：机制与验证条件 | 无括号XSS利用window.name字符串和instanceof对象自定义Symbol.hasInstance:eval，SVGonload及iframe name传值。 | [方法条目](../by-type/xss.md) |
| 保存图证0188-155-lfi：机制与验证条件 | Flarum文件/图像功能FILTER_VALIDATE_URL后file_get_contents再initFromBinary，仅像URL且必须有效图片；file/内部HTTP可能到达取决wrapper/配置，图未显示有效限制协议。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0188-157-access：机制与验证条件 | HackerOne CreateOrUpdateHackerCertification GraphQL操作用别人的认证对象ID导致删除，报告提供自有A/B两浏览器创建测试对象。 | [方法条目](../by-type/idor-access-control.md) |
| 重复图片中的 Kredis 历史 JSON 公告（0188） | 本帖正文只介绍转发账号内容变化，可用旧图 `1695672845760893260-03.png` 仍展示 Kredis CVE-2023-27531 特制 JSON 可能恢复意外对象及修复 1.3.0.1。 | [方法条目](../by-type/deserialization-rce.md) |
| Firebase Remote Config 的客户端可见性与真正秘密（0188） | Remote Config 通常要向移动客户端提供配置；检查 APK 和已有应用流量中的配置键、版本及用途，辨别公开功能开关、测试值与本应服务端保管的秘密。 | [方法条目](../by-type/mobile-android.md) |
| 公开下载链接的预期分享与跨文件权限（0188） | 单一链接可搜索 png/user 并列出上传文件的保存摘要提示存储访问边界。 | [方法条目](../by-type/idor-access-control.md) |
| JavaScript 与 GitHub 密钥候选的脱敏验证（0188） | Mantra、KeyHacks 和 AWS 搜索词用于定位 JS/HTML/仓库中的字段与值。 | [方法条目](../by-type/info-secrets.md) |
| JS 提取与版本监控的来源和差异保存（0188） | jsluice 语法提取、Wayback bookmarklet 和正则抽取只能生成 URL/路径/秘密候选。 | [方法条目](../discovery/records-and-incremental.md) |
| bffwa 路由的元数据返回与凭据权限（0188） | 保存请求通过 `/backend/bffwa?path=` 指向 link-local metadata，并展示目录与遮挡的临时 AWS 凭据结构。 | [方法条目](../by-type/ssrf.md) |
| 公开日历枚举与误配置隐私的区别（0188） | 保存帖以邮件地址构造 Google Calendar cid 链接。 | [方法条目](../by-type/idor-access-control.md) |
| Chrome 扩展审计插件的实际检查范围（0188） | ChromeAudit 线索将 Nuclei 插件定位于扩展审计。 | [方法条目](../discovery/client-and-cloud.md) |
| CMS 开放注册后的默认角色与服务端权限（0188） | 在授权环境建立新测试账号，记录注册入口、是否审批、默认角色、对象范围和合法操作。 | [方法条目](../by-type/idor-access-control.md) |
| 调试端点暴露须关联可见数据与环境边界（0188） | `/debug/pprof/` 与 PhpDebugBar 是不同调试入口，先确认真实处理器、认证、可见内容及环境。 | [方法条目](../by-type/info-secrets.md) |
| POST 转 GET 后仍需证实受害者可达和执行（0188） | 记录同一入口的 POST body 与 GET query 解析差异，保留 CSRF/认证、响应类型和真实输出上下文。 | [方法条目](../by-type/xss.md) |
| URL parser 绕过候选的多层路由对照（0188） | 针对已有明确范围的 40X 入口，先保存原始请求目标和身份，然后用单一编码/分隔变体比较代理、应用所见路径及自有只读标记资源。 | [方法条目](../by-type/idor-access-control.md) |
| 政策搜索与历史范围新增的使用边界（0188） | 通过 responsible disclosure、报告漏洞、平台标记和 reporting policy 搜索候选项目，先读当前范围、允许动作与提交条件，再开始测试。 | [方法条目](../scope-and-rules.md) |
| OIDC issuer 与客户端 secret 的两条信任边界（0188） | 对 ID Token 验证签名、issuer 与 discovery 的精确关系、audience、nonce 及时间条件；使用两套受控 issuer 的正反例，不由代码意见补造 MITM。 | [方法条目](../by-type/oauth-oidc.md) |
| 禁止下载权限要传播到富文本附件和预览（0188） | 以自有图片分享给另一测试账号并关闭 Allow download，比较原共享入口、Text 新建文档嵌入、预览与 AttachmentController 原图请求。 | [方法条目](../by-type/idor-access-control.md) |
| 浏览器 Network 与代理快捷键的可复现记录（0188） | 在正常自有操作中用 Network/代理关联入口、请求方法、认证、响应与后续状态，敏感字段脱敏并保留原始时序。 | [方法条目](../experiment-design.md) |
| 同类功能、对象 ID 和降权后的授权矩阵（0188） | 用两个自有账号建立草稿、精选图片、newsletter、页面角色和证书等测试对象，分别观察直接访问、举报后的通知、发布、更新及删除。 | [方法条目](../by-type/idor-access-control.md) |
| 订阅价格、币种与客户端响应更改的结算对照（0188） | 保存内容分别涉及 Premium 大折扣、订阅支付跳转时拦截响应和改为 UGX 的经验。 | [方法条目](../by-type/business-logic.md) |
| 测试邮箱归属与企业邮箱资格分开确认（0188） | 为长期测试使用自己控制、可收到确认与发票的邮箱，保持账号和操作证据关联。 | [方法条目](../by-type/authn-session.md) |
| DNS、端口和 HTTP 的活性分层（0188） | 先保留 DNS 解析和非 Web 服务候选，再分别核对授权端口、HTTP/TLS 与 Host/SNI。 | [方法条目](../discovery/passive-and-services.md) |
| 未引用模板与备份路径的内容确认（0188） | 保存两帖同正文比较 robots.txt 404 与 robots.txt.dist 下载，图片显示 26 字节但未见内容。 | [方法条目](../discovery/web-and-api.md) |
| FileMage Windows 路径规范化与模板误报对照（0188） | 保存模板标注 CVE-2023-39026、FileMage Gateway 1.10.8 及之前，GET mgmnt 后多层编码反斜线 traversal 目标为 programdata 配置。 | [方法条目](../by-type/lfi-path-traversal.md) |
| GraphQL 字典规模与真实 schema/授权覆盖（0188） | 由生产端点词汇构建的 GraphQL wordlist 可用于猜测字段和类型，但 60k+ 端点声明不保证当前项目 schema 完整或字段可用。 | [方法条目](../by-type/graphql.md) |
| 无登录表单的滥用与会话依赖的 CSRF（0188） | Contact/support 表单若不依赖受害者身份，跨站提交可能是垃圾消息/业务滥用，不能仅因缺 token 判定典型 CSRF。 | [方法条目](../by-type/csrf.md) |
| 退出流程的跳转参数与完整链条（0188） | 保存续帖只有登录、开启代理和拦截 logout 的起始步骤。 | [方法条目](../by-type/open-redirect.md) |
| CMS 指纹与漏洞扫描的版本关联（0188） | WordPress/Magento/AEM 等扫描工具先识别真实产品、插件/组件版本和部署入口，再匹配受影响条件与修复版本。 | [方法条目](../source-audit.md) |
| 按实际邮件与认证尝试计算预算（0188） | 请求计数限制可能漏同一请求内多封邮件、重复接收者或批处理认证尝试。 | [方法条目](../by-type/authn-session.md) |
| Airflow JDBC 与 ODBC 连接参数的驱动加载边界（0188） | 两张公告分别是 JDBC CVE-2023-22886 与 ODBC CVE-2023-34395，Provider before 4.0.0。 | [方法条目](../source-audit.md) |
| 递归 TLS 名称发现的去重、环路和深度（0188） | realm 从证书 DNS 名继续遍历，增加 -n 可能扩大结果，但需保留证书/时间/访问来源、已访问集合、重复、失败及最大请求量。 | [方法条目](../discovery/records-and-incremental.md) |
| 自动化 CRLF 输出与真实头分割的证明（0188） | Rayder 示例对多个换行编码输出 ERR/VLN 标签。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 管理入口候选与机制检查表的执行顺序（0188） | JS、目录、公开搜索、Shodan、授权端口、Git、Wayback 和隐藏子域共同定位入口，管理面名称不证明访问权限。 | [方法条目](../hunting-strategy.md) |
| 评分上限与聚合持久化分别校验（0188） | 保存正文称单评分及个人总评应最多 5，图片显示 14.1，但没有绕过续篇。 | [方法条目](../by-type/business-logic.md) |
| SSTI 表达式的引擎、版本及读取/执行区别（0188） | 保存 curl 例给 desc 中 Python/Jinja 风格 class/mro/subclasses 索引与文件读取。 | [方法条目](../by-type/ssti.md) |
| 同一输入进 Header 与 JavaScript 的跨上下文失配（0188） | PHP 片段先 html 实体处理，再去 LF/NUL，留 CR，把值同时放 Content-Disposition filename 与 JS 字符串。 | [方法条目](../by-type/xss.md) |
| 本地越狱检测与解密应用来源的验证范围（0188） | Frida/PowerShell 可先选择自有设备中具体 bundle/process，再比较检测函数返回和应用行为；列 PID 不证明全部机制可绕过，更不代替服务端鉴权。 | [方法条目](../by-type/mobile-ios.md) |
| IP 替代表达在验证器和连接器中的差异（0188） | ipfuscator 把 loopback 转为整数、十六进制、八进制、短地址或 IPv4-mapped IPv6；本地 curl 200 仅说明该客户端解析。 | [方法条目](../by-type/ssrf.md) |
| 邮箱语法、解码与下游漏洞类型的分层探针（0188） | quoted localpart、注释、括号、引号及域 literal 的接受条件因解析器不同，图中“全部 valid”不能采纳。 | [方法条目](../targeted-fuzzing.md) |
| 对象 ID 修改与水平访问控制的定义边界（0188） | 对象 ID 变化只是水平越权的候选输入。 | [方法条目](../by-type/idor-access-control.md) |
| 多参数标记扫描的归因与副作用（0188） | 所谓 SPRAY 把多个 URL 参数改为 XSS 标记，适合先定位反射位置，但同时改值会破坏业务并失去归因。 | [方法条目](../by-type/xss.md) |
| 单 CR 与前后端 HTTP 解析边界（0188） | 保存 Node llhttp 公告 CVE-2023-30589 指出当时 v16/v18/v20 将单 CR 接受为 header 分隔。 | [方法条目](../by-type/request-smuggling.md) |
| CORS PoC 与外部隧道的验证内容（0188） | 工具宣称生成 PoC 并用 ngrok 验证，先审阅请求、外部地址及哪些数据会离开测试环境。 | [方法条目](../by-type/cors.md) |
| 已认证 ReDoS 与代理排队影响分开量化（0188） | Airflow before 2.6.3 的公告声明已认证构造输入可使请求挂起。 | [方法条目](../targeted-fuzzing.md) |
| text/xml 与命名空间脚本的实际解析条件（0188） | 保存片段用 x:script 配 `http://w3.org/1999/xhtml`，这与标准 XHTML 命名空间 `http://www.w3.org/1999/xhtml` 不同；示例可能因此不能按预期识别。 | [方法条目](../by-type/xss.md) |
| OOB 回连的输出归因与 SQL 到执行链条（0188） | 保存图显示 Collaborator 请求包含 SQL Server 服务身份字符串与 PowerShell User-Agent。 | [方法条目](../by-type/sql-injection.md) |
| API v1/v2 的同身份和租户集合对照（0188） | 保存图中带 Bearer 的 v2/applications 返回空 collection，而 v1 响应显示 borrower 和相关人员对象。 | [方法条目](../by-type/idor-access-control.md) |
| 方法覆盖头与缓存键是否一致（0188） | X-Http-Method-Override 若影响服务端行为而未纳入缓存键，可能使无该头的后续客户端获得错误响应。 | [方法条目](../by-type/cache-deception.md) |
| 报告业务影响由最小证据支持（0188） | 把具体能力、受影响角色/对象、可达前提与实际业务损失联系起来，同时保留范围上限和反例。 | [方法条目](../impact-and-acceptance.md) |
| PDF 姓名遮盖要覆盖评论、活动和匹配边界（0188） | 在受控报告中测试评论参与者、仅同意公开的团队成员、活动日志及带特殊结尾字符的姓名，比较启用脱敏前后的导出 PDF 可见文本、可搜索字串和元数据。 | [方法条目](../reporting.md) |
| 未知属性变体的阻挡和执行双基线（0188） | 保存正文 claim 在 img 中加入 on0x=1，使 onerror 探针绕 Cloudflare；可用图只展示原形被 blocked。 | [方法条目](../by-type/waf-bypass.md) |
| instanceof 调用钩子与 window.name 数据流（0188） | 图用 `window.name instanceof {[Symbol.hasInstance]:eval}` 触发指定函数，绕过反射位置的括号词法过滤，另一输入 iframe name 则提供待执行字符串。 | [方法条目](../by-type/xss.md) |
| PHP wrapper 盲文件 oracle 的响应分类（0188） | URL 字符串进入 file_get_contents 再要求图像解码时，HTTP/file/php stream 的允许条件应与 URL 校验一致。 | [方法条目](../by-type/lfi-path-traversal.md) |
| URL 会话 ID 与登录后轮换的固定会话检查（0188） | 保存定义说明攻击者可给受害者指定 URL 会话 ID，属于 session fixation 候选。 | [方法条目](../by-type/authn-session.md) |

| 正文提炼0189：iDRAC 指纹与默认账号候选 | Shodan 的 org、200 和 favicon 哈希只能提供管理界面候选，IP/组织字段需复核实际设备所有者、授权清单、产品型号及版本；正文给出历史默认口令，不应在未知真实设备尝试。 | [方法条目](../by-type/iot-security.md) |
| 正文提炼0189：TLS Pass Through 排除也会排除证据 | TLS Pass Through 会让匹配流量经过代理但不解密，故少了可读请求/响应，不能把少噪声当保留完整覆盖。 | [方法条目](../discovery/web-and-api.md) |
| 正文提炼0189：把他人技巧转成目标自己的可证伪假设 | 不易访问的范围可提供差异化观察，但不保证高危。 | [方法条目](../hunting-strategy.md) |
| 正文提炼0189：侦察流水线的输入形状与覆盖记录 | 正文 cat scope→httpx→nuclei→dirsearch 思路需逐步保存输入、失败、协议/端口、来源时间及范围，而不是仅留成功结果。 | [方法条目](../discovery/passive-and-services.md) |
| 正文提炼0189：连接地址、SNI 与 Host 三个边界 | 在 HTTPS URL 不变时，Host:127.0.0.1 通常只改变HTTP主机路由输入，连接仍到原地址、TLS SNI 仍按URL。 | [方法条目](../by-type/host-header.md) |
| 正文提炼0189：URL 正则提取须保留原始字符 | 保存命令的字符类仅含字母数字、点/斜线/问号/等号/下划线/横线，会在&、%、冒号端口、fragment、IPv6及非ASCII等位置截断；末尾引号外的*还可能被shell展开。 | [方法条目](../discovery/records-and-incremental.md) |
| 正文提炼0189：一行回显扫描只生成 XSS 候选 | gf xss、source=过滤、qsreplace与curl/grep链只找候选和回显，缺乏浏览器上下文、输出编码、DOM sink及CSP执行证据。 | [方法条目](../by-type/xss.md) |
| 正文提炼0189：反引号的调用语义取决于 JavaScript 上下文 | 当括号字符被过滤，反引号可能在已有可调用标识符后构成 tagged template 调用，但不是在所有HTML/属性/字符串中通用的括号替代。 | [方法条目](../by-type/xss.md) |
| 正文提炼0189：隐藏参数与时延要分开证明 | Arjun发现候选参数、手工观察再sqlmap验证，是探索顺序而不是枚举全部端点/所有可能参数的保证。 | [方法条目](../by-type/sql-injection.md) |
| 正文提炼0189：X-Original-Host 反射进 meta content 的影响门槛 | 保存正文只观察该头反射到meta的content属性并称影响接近零。 | [方法条目](../by-type/host-header.md) |
| 正文提炼0189：盲 XSS 的提交、渲染与回连三段 | 正文脚本src绝对HTTP/协议相对域与$.getScript分别依赖混合内容策略、CSP、网络许可、jQuery及当前页面上下文。 | [方法条目](../by-type/xss.md) |
| 正文提炼0189：登录 SQL 字符串须结合查询与数据库方言 | 保存帖列引号、OR、LIKE、等号及注释变体；它们的布尔/拼接/注释意义依赖SQL方言、引号位置、类型与编码，参数化或白名单是主要反例。 | [方法条目](../by-type/sql-injection.md) |
| 正文提炼0189：审批动作的权限与状态应独立核对 | 正文建议测试管理员approve按钮，但图只奖项侧栏。 | [方法条目](../by-type/idor-access-control.md) |
| 正文提炼0189：GTM 脚本是带版本的资产线索 | 从 HTML 的 GTM 容器加载及额外JS规则提取域名/路径，记录容器ID、版本、页面与原始脚本来源，再复核目标归属与范围。 | [方法条目](../by-type/info-secrets.md) |
| 正文提炼0189：替换成功 JSON 不能直接证明 ATO | 保存流程是先正确密码登录留响应，退出后将错误登录响应替成成功JSON，作者称没有Cookie/token即可ATO。 | [方法条目](../by-type/authn-session.md) |
| 正文提炼0189：删除 token 后必须完成真实浏览器对照 | 省略authentication_token/verification token的请求被接受仅是服务器校验候选；还须跨站浏览器可构造method/Content-Type、Cookie/SameSite、Origin/Referer、有效会话以及真实状态变化。 | [方法条目](../by-type/csrf.md) |
| 正文提炼0189：同步发请求不等于原子性失效 | Burp group tabs可帮助协调并发/单包发起，但网络同时到达不保证同一后端事务交错。 | [方法条目](../by-type/business-logic.md) |
| 正文提炼0189：参数名与值经过不同反射路径 | 保存帖称value里的script被拦而param[script字符串]进JS页面源码；必须区分框架括号参数解析/数组对象化、未知key序列化与JS字符串/对象键编码。 | [方法条目](../by-type/xss.md) |
| 正文提炼0189：归档功能不能只按扩展名归类 | 完整保存正文只列拼接、压缩、多功能三类并在五类说法后截断；不补未保存两类。 | [方法条目](../by-type/file-upload.md) |
| 正文提炼0189：未知用途 token 不按账号登录凭据处理 | 正文在/checkPaymentStatus的IDOR相关响应发现token但作者不知道用途。 | [方法条目](../by-type/authn-session.md) |
| 正文提炼0189：弱口令与管理员权限分开确认 | 正文声称邮箱名等于密码并配Admin仪表板；要证明需授权自有实例的初始凭据策略、强制改密、服务端角色与最小操作，先有账号授权。 | [方法条目](../by-type/authn-session.md) |
| 正文提炼0189：Firebase 公共配置与规则授权分开 | 自动提取projectID/APIkey只提供配置定位；Firebase公共客户端APIkey常用于标识项目，不应直接认定secret/DB接管。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 正文提炼0189：postMessage 跟踪后仍须验证消费者 | URL/domain/stack及Raven/NewRelic/jQuery包装层的观察用于关联窗口间通信，但事件发生不证明漏洞。 | [方法条目](../discovery/web-and-api.md) |
| 正文提炼0189：schema 推断与 resolver 鉴权是两回事 | Clairvoyance保存描述是introspection关闭时推断schema，未含实际schema/实现；可作为错误信息/字段候选与端点建模线索。 | [方法条目](../by-type/graphql.md) |
| 正文提炼0189：持续维护词表时保留来源与字节 | 从tips/writeups/讨论收集端点可以维护个性化词表，但加入前保存来源、时间、适用技术、路径/参数类型、编码及授权条件。 | [方法条目](../targeted-fuzzing.md) |
| 正文提炼0189：POST JSON 改 GET 只是可投递性假设 | 保存正文只到把POST参数移到GET，后续XSS/ATO未保存。 | [方法条目](../by-type/xss.md) |
| 正文提炼0189：影响证据先于奖励期待 | 把奖励翻倍的建议转成说明真实可利用边界、用户交互与受控影响的报告要求；扩大伤害、批量操作或窃取数据不应成为证明手段。 | [方法条目](../impact-and-acceptance.md) |
| 正文提炼0189：VM SSH 的工作流与暴露面限制 | 正文sudo services ssh start很可能将service写成services，具体OS/服务管理器需要核实；ifconfig也不保证预装。 | [方法条目](../discovery/web-and-api.md) |
| 正文提炼0189：noscript 片段须锁定解析时的脚本状态 | 保存片段在noscript里的p title嵌闭合noscript与img字符串；是否成为真实img/onerror取决于scripting enabled、净化上下文、namespace、序列化/重解析及库版本。 | [方法条目](../by-type/xss.md) |
| 正文提炼0189：转义字符和真实控制字节不能混称 | 正文script示例含字面反斜线、Cr和反斜线点，不能假定被解码成有效标签；details ontoggle示例也依赖实际HTML属性/事件及浏览器交互。 | [方法条目](../by-type/waf-bypass.md) |
| 正文提炼0189：重置 hash 必须绑定邮箱主体 | 两自有账号A/B：A发起重置，保存链接hash与mail参数，再仅变mail指B，是token与账号绑定的受控比较。 | [方法条目](../by-type/authn-session.md) |
| 正文提炼0189：TE 中 TAB 必须按原始链路解析验证 | 正文只提示在T.E header尝试TAB，未指明在头名、冒号、值前还是分隔位置，不能补猜payload。 | [方法条目](../by-type/request-smuggling.md) |
| 正文提炼0189：重置 URL 投毒仍需邮件生成与点击条件 | 此帖只含Host注入题名，现有图与另一保存帖同hash，已核读的图示Host/X-Forwarded-Host参与/reset邮件链接生成，用户点击后token可能落外域。 | [方法条目](../by-type/host-header.md) |
| 正文提炼0189：javascript 链接需要执行与交互证据 | 正文明确无需交互payload被滤，改a href=javascript:alert()后需Click。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-6-iot：机制与验证条件 | 可见 iDRAC9 Enterprise、/restgui/start.html 登录界面与 Username、Password、Domain=This iDRAC 字段。 | [方法条目](../by-type/iot-security.md) |
| 保存图证0189-8-web：机制与验证条件 | HTTP Request Headers 教学图展示 Host、User-Agent、Referer、Authorization Basic、Cookie、Content-Type application/json、X-Forwarded-For、If-Modified-Since、Range bytes=0-100、Content-Length=200、Connection keep-alive 及攻击标签。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0189-10-redirect：机制与验证条件 | OpenRedireX 终端截图：3 个 URL、44 个 payload；logout/redirect_uri 的 userinfo、多个斜线及编码片段，INFO 中停留 example.com，而 FOUND 示例最终落地 google.com。 | [方法条目](../by-type/open-redirect.md) |
| 保存图证0189-11-auth：机制与验证条件 | Acronis 报告 1435392：既有账号发起换邮箱但暂不确认，再用该邮箱注册新账号且不点新确认邮件，退出后点旧换邮箱确认链接进入另一登录页，作者称该页无速率限制。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-14-csrf：机制与验证条件 | Mars 2029753 删除宠物接口 /kisallataim/ANIMAL_ID/delete；图示自动提交 form 未声明 method，默认 GET。 | [方法条目](../by-type/csrf.md) |
| 保存图证0189-15-xss：机制与验证条件 | Mars 2037234 可见 POST /_post/usuario_actualizar.php 表单，nombre、apellido、email、rut、idProvincia、idLocalidad、optin 等字段，apellido 值为 script alert；截图在第 12 行截断，enctype 右边被截，不能补猜整个 PoC。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-15-csrf：机制与验证条件 | Mars 2037234 可见 POST /_post/usuario_actualizar.php 表单，nombre、apellido、email、rut、idProvincia、idLocalidad、optin 等字段，apellido 值为 script alert；截图在第 12 行截断，enctype 右边被截，不能补猜整个 PoC。 | [方法条目](../by-type/csrf.md) |
| 保存图证0189-16-logic：机制与验证条件 | Mars 1943252 Banfield 预约：邮箱验证码随机输入，拦截响应把 false 改 true。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0189-17-xss：机制与验证条件 | Mars 2061049：show 参数被描述为反射到 HTML，目标 wikichat.fr；图仅见问题描述和风险矢量，利用链接下方被截断。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-18-access：机制与验证条件 | Mars 2055081：从 Shodan、404 资产与 Web Archive/搜索发现 info.banfield.com/unsub-confirm?qs=长串及 /unsub?EmailAddress=；作者称后者无需登录取消任意邮箱订阅。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0189-23-redirect：机制与验证条件 | 开放重定向图列直接换域、协议相对 //、反斜线、无双斜线 scheme、%40 userinfo、后缀拼接、%2e、查询/fragment 放白名单域、斜线后小圆符号、中文句号编码与 %0d/%0a。 | [方法条目](../by-type/open-redirect.md) |
| 保存图证0189-24-host：机制与验证条件 | ffuf 图以 Host:127.0.0.1 替换虚拟主机并 fuzz /FUZZ，-fs 过滤普通响应长度；目标 HTTPS URL 仍决定连接地址/SNI，Host 改写不会把网络连接改到服务器本机。 | [方法条目](../by-type/host-header.md) |
| 保存图证0189-26-xss：机制与验证条件 | nuclei v2.9.8/模板 v9.6.2 单目标单模板 admin-ajax-xss 命中，/wp-admin/admin-ajax.php?action=zip_search&nonce=…&zip=10001&callback=jQuery… 后接编码 img onerror 字符串。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-31-report：机制与验证条件 | HackerOne 2061367：创建 dummy program/report，以 team member 查看并编辑研究员报告；平台摘要称与2096271相同但更早而补发奖励。 | [方法条目](../reporting.md) |
| 保存图证0189-33-secret：机制与验证条件 | 报告通知标题可见 DB Dump At …/dump.sql，正文只有 triaged 与联系服务所有者；辅助明确图中是 dump.sql，而保存正文 dump.sqI 最后一字母为大写 I，不能静默当作同一字节。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0189-34-source：机制与验证条件 | CakeFuzzer 架构图：CakePHP Web App 位于 OS；连续 Attack Queue/Single Executor PHP 触发，Process/Output/FileSystem/FileContents monitors 观察，Registry 记录发现；Configuration、Instrumentation on/off、Fuzzer strategy 设置观察器/调度队列。 | [方法条目](../source-audit.md) |
| 保存图证0189-35-sql：机制与验证条件 | 被作者批评的文章截图声称 Django 登录页 Admin/Admin 失败后密码 admin' or '1'='1 即登录 Admin；没有原始 SQL、参数化情况、请求或实际会话证据。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0189-38-sql：机制与验证条件 | Burp 图 GET /v1/orderDetail?orderId=1+AND+ELT(1,SLEEP(20))，JSON HTTP/2 200、计时40214millis，Age0/X-CacheMISS。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0189-43-impact：机制与验证条件 | 平台回复明确这是暂时可用性问题，团队已发现，通常不奖非安全问题但此次奖100美元/5分；可直接作为奖励不等于漏洞的反例。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0189-45-xss：机制与验证条件 | 高清一行式图 gf xss｜grep source=｜qsreplace｜curl｜grep 标 Vulnerable；使用弯引号、while read host do ; do、不正确单横线长选项、未正确ANSI转义。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-51-xss：机制与验证条件 | Access Request 表单 Name、Email、Request Comments textarea name=comments，150字符 UI 限制，作者标注 Vulnerable Parameter；可提炼低频申请/后台审核为潜在延后渲染入口，服务端长度约束与存储/输出链须分别确认。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-55-scope：机制与验证条件 | Snapchat scope变化图把 Lens Studio 可执行文件/API 源码 Eligible For Bounty 从 true 改 false，同时 Tier B Non Core 文本移除 Lens Studio 保留 Bitmoji/Playcanvas。 | [方法条目](../scope-and-rules.md) |
| 保存图证0189-60-secret：机制与验证条件 | 图片是SMTP月度额度订单邮件，订单号、用户名、密码可见，其他金额/域名打码；不抄录或验证真实凭据。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0189-61-web：机制与验证条件 | Transposh Translation Filter 介绍图可见历史清单：<=1.0.7 tp_tp RXSS24910、tp_translation storedXSS24911；<=1.0.8.1 多CSRF24912、tp_translation默认弱翻译权限2461、tp_history无认证信息2462、行政utilities授权25810、tp_editor多认证SQLi25811；下一条25812底部被截，勿补猜。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0189-62-passive：机制与验证条件 | Bug Bounty Recon GUI 按钮矩阵包含directory/config/database/log/backups/login/sqlerrors/apache/robots/phpinfo、安装文件、headers、redirect、CMS、第三方源码/员工/论坛、归档、CT、Censys IP/domain/cert、Shodan、S3/Spaces、WSDL、SWF、Git与特定旧CVE标签。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0189-64-web：机制与验证条件 | Wolf-Recon流程：Domain→subdomain enum→httpx/httprobe存活、takeover、LinkFinder端点、Nuclei模板/模糊模板、Waybackurls正常/regex结果→XSS/SQL候选；Dorking→Google/GitHub。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0189-69-auth：机制与验证条件 | Serv-U Web Client /Web Client/ListDir.htm 登录后样式的Home/目录列表、Upload/Download/Delete按钮，目录名称打码。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-73-passive：机制与验证条件 | Google 查询图实际 site:people.sap.com "打码词"，一个结果标题 Admin - SAP People、member since/连接/积分；图与正文 site:http://people.sap.com 的语法不同，应以正确主机site限定而非URL协议形式。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0189-75-proto：机制与验证条件 | 运行时日志列 [PP][Prop delimiter/depth/ignoreQueryPrefix/interpretNumericEntities/parameterLimit/parseArrays/plainObjects/strictNullHandling] qs/lib/parse.js，Express locals/_all、body-parser _body/body、type-is transfer-encoding/content-length、etag time、fresh if-modified-since 等属性/元素访问及行号。 | [方法条目](../by-type/prototype-pollution.md) |
| 保存图证0189-76-auth：机制与验证条件 | Airflow CVE-2023-40273/2121960 摘要：管理员重置用户密码后原认证会话持续至过期；修复数据库session后端会注销该用户旧会话，securecookie后端仍需变更secure_key/重启注销全体并给UI警告，建议2.7.0+。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-84-impact：机制与验证条件 | 项目回复确认有漏洞但明确需要另一用户或管理员参与，不能独立利用，第二项300欧两项共500；与critical标题须区分实际交互前提。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0189-86-files：机制与验证条件 | ZIP教学图将rce.php压入file.zip后上传，再page=zip://path/file.zip#rce.php；成立须有攻击者可控压缩内容、已知服务端路径、PHP zip流包装器支持以及page真正进入include/require而非readfile/download。 | [方法条目](../by-type/file-upload.md) |
| 保存图证0189-86-lfi：机制与验证条件 | ZIP教学图将rce.php压入file.zip后上传，再page=zip://path/file.zip#rce.php；成立须有攻击者可控压缩内容、已知服务端路径、PHP zip流包装器支持以及page真正进入include/require而非readfile/download。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0189-87-auth：机制与验证条件 | /checkPaymentStatus 相关图是裁切响应，challenge、token及长编码串可见；看不到HTTP状态、对象身份、token用途/有效性。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-88-auth：机制与验证条件 | B2C Dashboard显示Admin样式、Active Consumers计数1791516；正文称弱默认账号。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-90-sql：机制与验证条件 | 局部GET行可见timezone/dateType/startDate/endDate/currency/accountIds/country/agency/screeningAccountId；agency处候选'%2b(select*from(select(sleep(20)))a)%2b'。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0189-93-sql：机制与验证条件 | sqlmap1.7.3#pip 对POST username/password，图先302跳转询问是否跟随/重发原POST，服务器置PHPSESSID询问接受，之后heuristic显示username might not be injectable。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0189-94-passive：机制与验证条件 | DNSWatch截图CLI -i接口/-o输出/-t目标IP/-adt分析/-doh/-fd目标domain/-d数据库；SQLite dns_requests记录timestamp/source/destinationIP/MAC/packet_size/TTL/type/checksum、请求域denizhizal.com及8.8.8.8往返。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0189-99-cloud：机制与验证条件 | S3 Bucket Recon图8路线：Google dorks、Burp sitemap/地址及x-am-bucket样式头、图片virtual-hosted bucket URL、GitHub工具、grayhatwarfare/osint目录、s3-detect.yaml、JS regex、subfinder｜httpx title grep Amazon S3。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存图证0189-100-web：机制与验证条件 | HTTP Response Headers 图列 Server Apache2.4.41、X-Powered-By PHP7.3.11、nosniff、CSP default-src self、ACAO*、HSTS max-age1337、Content-Disposition attachment、XFO SAMEORIGIN、Cache-Control no-store/no-cache、Set-Cookie sessionID、WWW-Authenticate Basic。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0189-115-android：机制与验证条件 | Cloudflare WARP Android 2043885/CVE2023-3747：管理员禁止禁用WARP但可发临时override code；本地可访问设备者调设备日期时间延长断开时限，摘要称缺服务端验证。 | [方法条目](../by-type/mobile-android.md) |
| 保存图证0189-116-xss：机制与验证条件 | Proton Mail已净化邮件再将svg替换proton-svg：purify.ts querySelectorAll/svg、ownerDocument.createElement、replaceChild，省略子节点搬移代码用[… ]明确未显示。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-120-xss：机制与验证条件 | rails-ujs CVE2023-23913/2125679摘要：用户将含data-method、data-remote或data-disable-with的HTML剪贴板粘入contenteditable，库的行为委托可能引DOMXSS；图写影响>=5.1.0、<5.1.0不受影响，修复6.1.7.3/7.0.4.3，应按相应分支修复版本收紧，不写所有>=5.1永远脆弱。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-125-ssrf：机制与验证条件 | JSON endpoint=/adduser 例子：插入@burpcollab.com前缀后若后台无路径分隔地拼成https://website@burpcollab.com/adduser，website成为userinfo而host变回连域。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0189-126-waf：机制与验证条件 | Sucuri图两候选：script拼写中可见字面反斜线与Cr以及document反斜线点，另一details/open/…ontoggle=(alert)(document.domain)。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0189-127-scope：机制与验证条件 | H1 Time Based Blind SQLi triage邮件明确要求 please do not conduct any further testing operations。 | [方法条目](../scope-and-rules.md) |
| 保存图证0189-130-xss：机制与验证条件 | Yelp2089042摘要：biz.yelp.com未验证商户邮箱反射入提示产生XSS，cookie bridge先将入口带到其他用户，再第二次利用泄漏HttpOnly session cookies，称business与regular账号可能受影响。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-131-auth：机制与验证条件 | HackerOne2109382：关闭support@主入口邮件建票后，Freshdesk租户support@…freshdesk.com备用入站仍按伪造From创建受害者工单，标题绕2001913；截图给假邮件服务步骤但不运行。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-132-logic：机制与验证条件 | 100美元PayPal备注 Manipulate User By changing display name to admin，只是奖励描述。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0189-133-auth：机制与验证条件 | HackerOne2079502：作者通过伪造发件人发送邮件到support@hackerone.com，再在自有support.hackerone.com看到新工单；公开PoC打码、None0及1000奖励。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-135-deser：机制与验证条件 | Airflow Spark provider CVE2023-40195/2127968摘要 before4.1.3：已装Spark provider且用户有配置Spark hooks/connection权限，把连接指向恶意Spark服务器使pyspark客户端处理不可信反序列化数据，Airflow节点可能执行代码。 | [方法条目](../by-type/deserialization-rce.md) |
| 保存图证0189-138-xss：机制与验证条件 | DoD2045549 CVE2023-24488保存复现URL /oauth/idp/logout?post_logout_redirect_uri=%0d%0a%0d%0a<script>alert(document.domain)</script>，另有cookie stealing陈述但无真实回显或cookies。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-138-crlf：机制与验证条件 | DoD2045549 CVE2023-24488保存复现URL /oauth/idp/logout?post_logout_redirect_uri=%0d%0a%0d%0a<script>alert(document.domain)</script>，另有cookie stealing陈述但无真实回显或cookies。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图证0189-139-sql：机制与验证条件 | DoD2081316 /qsSearch.aspx，作者点击sort抓包；图只见POST、ASP.NET Session/TS cookie、form-urlencoded UTF8、X-Requested-With XMLHttpRequest、X-MicrosoftAjax Delta=true，body与payload在下方未显示。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0189-140-auth：机制与验证条件 | DoD2081332 LDAP anonymous login叙述可能读用户/组织资料但没有bind/search结果。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0189-141-access：机制与验证条件 | ColdFusion DoD2082528 CVE2023-38205：限制外部访问Administrator的功能绕过，图URL /hax/..CFIDE/wizards/common/utils.cfc?method=wizardHash&inPassword=foo&_cfclient=true&returnFormat=wddx（图是..CFIDE而非../CFIDE）。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0189-149-ws：机制与验证条件 | ArgoCD2123094 webterminal session从2.6.0起打开后token过期仍能发websocket messages，补丁2.6.14/2.7.12/2.8.1；已登录用户开terminal等待websession到期。 | [方法条目](../by-type/websocket.md) |
| 保存图证0189-150-cmd：机制与验证条件 | Node.js IBB2120719/CVE2023-32559：实验policy.json模块访问限制能由deprecated process.binding加载内部模块并访问spawn_sync绕过，摘要历史影响active16.x/18.x/20.x；需预先能执行JS且启用该实验policy，不能称任意公网未认证RCE或OS权限提升。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0189-153-host：机制与验证条件 | reset教学图两变体：POST/reset Host=evilsite.com 或原Host加X-Forwarded-Host=evil.com，作者称重置邮件URL引用输入域、收信人点击后token出现在该域日志。 | [方法条目](../by-type/host-header.md) |
| 保存图证0189-156-xss：机制与验证条件 | DevTools Elements中facetfilter按钮aria-label含字面<h1>String，子span却有真正<h1 aria-level=2>String</h1>节点，隐藏span末尾也含h1字串。 | [方法条目](../by-type/xss.md) |
| 保存图证0189-159-logic：机制与验证条件 | 完整社交教学图：自有免费试用时保存付费功能请求，试用结束再以免费账号重放测试权益撤销，附2058549 Medium4.3/750卡。 | [方法条目](../by-type/business-logic.md) |
| 已核图0189-42：OpenRedireX 解析与最终落地 | 此批 `1697468553660960869-02.jpg` 与此前已核原图相同哈希，无需重复观看/记账。 | [方法条目](../by-type/open-redirect.md) |
| 已核图0189-65：GTM 容器及规则候选 | 此批三图与已核图同哈希，分别绑定当前来源：`1698122461416452273-03.jpg` 提示从HTML容器提取额外JS的子域、URL及秘密候选；`1698122461416452273-04.jpg` 展示googletagmanager.com/gtm.js?id=的公开加载ID；`1698122461416452273-05.jpg` 规则里多个Seagate子域和产品路径。 | [方法条目](../by-type/info-secrets.md) |
| 已核图0189-111：全端口链的范围与失败 | `1699728497126826214-02.jpg` 为已核同hash图：chaos -d hackerone.com → naabu -ports full → httpx，多协议非标准端口及1m29计时。 | [方法条目](../discovery/passive-and-services.md) |
| 已核图0189-155：同图的另一保存来源 | `1700617019677200509-02.jpg` 与本批已实际核读 `1700590393388363907-02.jpg` 是相同hash，分别对应不同保存帖。 | [方法条目](../by-type/host-header.md) |

| 保存正文0190：编码与事件变体不能单独证明WAF绕过 | 保存示例分别涉及SVG onload/atob、SVG set/onbegin与换行URL编码、img/onerror、details/ontoggle和JavaScript Unicode标识符。 | [方法条目](../by-type/waf-bypass.md) |
| 保存正文0190：Apache server-status需要实际敏感输出证据 | server-status是候选路径，正常403、仅基础运行指标、soft404和详细工作进程/请求/虚拟主机输出需分开。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0190：ping斜杠变体与OAuth入口的授权边界 | 正文/ping为OK、/ping/进入登录页及dummy Google账号可访问的声称。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存正文0190：Laravel调试路径只是信息暴露入口候选 | /_debugbar可能指向调试组件；端点出现并不等于整个生产应用APP_DEBUG=true。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0190：搜索索引中的Origin IP必须重新归属核对 | Shodan/Censys返回的历史IP是候选，需与当前DNS、证书、虚拟主机/Host路由、资产授权和目标特征交叉验证。 | [方法条目](../discovery/passive-and-services.md) |
| 保存正文0190：PHP开发快照后门与普通版本及SQLi区分 | 保存文本给出PHP8.1.0-dev及异常User-Agentt头的zerodium表达式；这是历史被篡改开发快照/供应链后门线索，版本字符串本身不证明构建有后门，sleep延迟也不是SQL注入证据。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存正文0190：熟悉功能与复杂状态转换提升假设质量 | 长期理解一个获授权项目可发现新功能和状态边界；复杂功能、曾被忽视的SSO是检查优先级信号，不代表一定有漏洞或一定重复。 | [方法条目](../hunting-strategy.md) |
| 保存正文0190：多域Google dork的约束和拼写 | 正文混用ext:php/ext:asp与exp:aspx，后者只是保存拼写不能视为有效扩展名算子。 | [方法条目](../discovery/passive-and-services.md) |
| 保存正文0190：phpLDAPadmin登录及cmd路径需分支验证 | phpldapadmin/index.php、phpldapadmin/cmd.php和cmd.php是候选，保存续篇未提供XSS具体参数。 | [方法条目](../by-type/ldap-xpath.md) |
| 保存正文0190：GTM公开配置与秘密材料分开 | 保存图展示GTM容器ID、加载脚本与规则/域名。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0190：密码找回之后2FA状态与完整认证分别核对 | 保存流程为注册自有账号→启用TOTP→退出→找回并重置密码→Save Changes后无需2FA登录。 | [方法条目](../by-type/authn-session.md) |
| 保存正文0190：角色与管理员功能需要服务端操作对照 | 不同角色与登录/后台入口只是覆盖队列。 | [方法条目](../by-type/idor-access-control.md) |
| 保存正文0190：邮箱验证令牌自助泄漏与企业权限的必要链 | 待验证用户若从自身API取得emailConfirmationToken，再使用它完成验证，可能将账户登录替代邮箱控制权。 | [方法条目](../by-type/authn-session.md) |
| 保存正文0190：URL抓取图片的预期功能与非预期网络边界 | 允许抓取外部URL可能是产品预期；检查的是受控服务端请求是否越过规定协议/地址/租户网络边界。 | [方法条目](../by-type/ssrf.md) |
| 保存正文0190：载荷语法与解码层不能由文本省略 | onmouseover示例正文confirm(document.cookie)x连续写法与图中%0d换行边界不同；Unicode标识符、tagged template与javascript%3a/throw%2520示例分别依赖HTML/JS解析和一层/两层解码。 | [方法条目](../by-type/xss.md) |
| 保存正文0190：缓存令牌到CSRF必须逐段成立 | 正文链为Web Cache Deception→authenticity_token缓存→敏感操作CSRF，仅为链纲要。 | [方法条目](../by-type/cache-deception.md) |
| 保存正文0190：域名包含匹配不能代替Origin与邮箱归属 | target.com.evil.com与eviltarget.com检验前/后缀包含误判；应按URL规范化后的scheme/host/port精确判断Origin，凭据CORS还需浏览器实际带身份并可读敏感响应。 | [方法条目](../by-type/cors.md) |
| 保存正文0190：支持邮件发件身份与账户删除的操作授权 | 正文声称以另一邮箱伪装自有支持账户导致删除其他用户，保存图仅奖励。 | [方法条目](../by-type/authn-session.md) |
| 保存正文0190：User-Agent盲注的延迟渲染证据 | 请求头可能进入运营日志/工单/后台后延迟渲染，Burp全局替换范围容易扩及第三方。 | [方法条目](../by-type/xss.md) |
| 保存正文0190：Oracle EBS不同注册流程分别建模 | 保存的/OA_HTML/ibeCAcpSSOReg.jsp、ibeCRgpIndividualUser.jsp、ibeCRgpPrimaryCreate.jsp、ibeCRgpPartnerPriCreate.jsp分别为候选注册入口；SSO、个人、主要和伙伴流程的实际角色/审批可能不同。 | [方法条目](../discovery/web-and-api.md) |
| 保存正文0190：base64 state及journey的重定向白名单检查 | 保存正文称state内base64编码的URL和journey可指定eviltarget.com。 | [方法条目](../by-type/open-redirect.md) |
| 保存正文0190：同参数扩展到其他端点仍逐点验证 | 已验证参数可为其他获准端点提供假设，字段名相同不保证处理器、输出上下文、身份或对象权限相同。 | [方法条目](../targeted-fuzzing.md) |
| 保存正文0190：参数收集流水线的输出只是反射候选 | 保存流程sub列表→paramspider -l→results/*.txt→kxss。 | [方法条目](../targeted-fuzzing.md) |
| 保存正文0190：PDF转换组件版本不是SSRF与文件读取证明 | wkhtmltopdf0.12.6是保存帖历史组件线索；需实际渲染进程、资源加载选项、补丁/构建、网络及本地文件权限。 | [方法条目](../by-type/document-rendering.md) |
| 保存正文0190：接管后自建漏洞不会增加原资产影响 | 帖用托管一个自有易受RCE应用后申报Critical作讽刺。 | [方法条目](../impact-and-acceptance.md) |
| 保存正文0190：ZIP与PHP备份暴露的证据边界 | users.php、config/const.DB.php.bak是备份/源码候选，后缀可能导致源码直接服务也可能仍执行/返回soft404。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0190：重置邮箱参数中的换行与邮件解析分别验证 | 保存示例email含%0a%0dcc:，顺序LFCR不能简单当标准CRLF；mail.secry本身有末级标签，作者No TLD描述不充分。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存正文0190：admin路径字符变体的响应差异需保护内容验证 | /admin/files到/authFailure为302，/adminFUZZ/files或/admin/FUZZ/files为200只是候选。 | [方法条目](../by-type/idor-access-control.md) |
| 保存正文0190：CRUD方法与组织生命周期授权独立核验 | CRUD为Create/Read/Update/Delete，保存帖误写Change。 | [方法条目](../by-type/idor-access-control.md) |
| 保存正文0190：JS下载与关键字命中必须保留来源和含义 | 保存脚本未引用变量、关闭TLS验证并将cat *混合grep -r -E，存在分词、通配、文件混淆和正则误报。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0190：Unicode身份碰撞需跨流程绑定证据 | 保存续篇仅1/6与K小写映射示例。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-3-waf：机制与验证条件 | 保存原图文件：1700840778195485120-02.jpg。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0190-6-lfi：机制与验证条件 | 保存原图文件：1700902092167373236-02.jpg。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0190-7-lfi：机制与验证条件 | 保存原图文件：1700902227081416950-02.jpg。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0190-8-passive：机制与验证条件 | 保存原图文件：1700919976293446074-02.jpg。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0190-14-oauth：机制与验证条件 | 保存原图文件：1701084616663114149-03.jpg。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0190-16-xss：机制与验证条件 | 保存原图文件：1701200820027404327-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-18-auth：机制与验证条件 | 保存原图文件：1701219183705636906-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-19-auth：机制与验证条件 | 保存原图文件：1701219322964885857-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-20-xss：机制与验证条件 | 保存原图文件：1701219470726041966-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-23-access：机制与验证条件 | 保存原图文件：1701245058521997696-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0190-25-secret：机制与验证条件 | 保存原图文件：1701279604416323826-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0190-26-cmd：机制与验证条件 | 保存原图文件：1701284899536126036-02.jpg。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0190-31-waf：机制与验证条件 | 保存原图文件：1701365182549709137-02.jpg。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0190-33-auth：机制与验证条件 | 保存原图文件：1701392754251563477-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-34-xss：机制与验证条件 | 保存原图文件：1701430565549810072-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-34-waf：机制与验证条件 | 保存原图文件：1701430565549810072-03.jpg。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0190-35-secret：机制与验证条件 | 保存原图文件：1701461946715734161-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0190-36-xss：机制与验证条件 | 保存原图文件：1701506066251723196-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-37-ssrf：机制与验证条件 | 保存原图文件：1701536284030980443-02.jpg。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0190-46-sql：机制与验证条件 | 保存原图文件：1701816412736819408-02.jpg。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0190-48-access：机制与验证条件 | 保存原图文件：1701853354304102434-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0190-50-desktop：机制与验证条件 | 保存原图文件：1701898676921356329-02.jpg。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0190-52-scope：机制与验证条件 | 保存原图文件：1701913903410589905-02.jpg。 | [方法条目](../scope-and-rules.md) |
| 保存图证0190-54-xss：机制与验证条件 | 保存原图文件：1701943964776222927-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-55-ssrf：机制与验证条件 | 保存原图文件：1701948254903062769-02.jpg。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0190-56-desktop：机制与验证条件 | 保存原图文件：1701959054900306179-02.jpg。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0190-60-secret：机制与验证条件 | 保存原图文件：1701989251012018196-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0190-62-xss：机制与验证条件 | 保存原图文件：1702060654214132152-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-65-xss：机制与验证条件 | 保存原图文件：1702189436325474459-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-66-auth：机制与验证条件 | 保存原图文件：1702224189715837346-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-67-scope：机制与验证条件 | 保存原图文件：1702250932853981682-02.jpg。 | [方法条目](../scope-and-rules.md) |
| 保存图证0190-70-access：机制与验证条件 | 保存原图文件：1702340728461127944-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0190-70-cmd：机制与验证条件 | 保存原图文件：1702340728461127944-02.jpg。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0190-72-web：机制与验证条件 | 保存原图文件：1702366874451976687-02.jpg。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0190-75-xss：机制与验证条件 | 保存原图文件：1702384889025405156-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-77-lfi：机制与验证条件 | 保存原图文件：1702396945288011872-02.jpg。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0190-79-secret：机制与验证条件 | 保存原图文件：1702427148622217488-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0190-81-xss：机制与验证条件 | 保存原图文件：1702508193803346368-02.png。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-83-cmd：机制与验证条件 | 保存原图文件：1702589534632862040-02.jpg。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0190-85-cloud：机制与验证条件 | 保存原图文件：1702593223343124512-02.jpg。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存图证0190-86-web：机制与验证条件 | 保存原图文件：1702595478620127647-02.jpg。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0190-96-strategy：机制与验证条件 | 保存原图文件：1702756815891734683-02.jpg。 | [方法条目](../hunting-strategy.md) |
| 保存图证0190-96-web：机制与验证条件 | 保存原图文件：1702756815891734683-02.jpg。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0190-100-xss：机制与验证条件 | 保存原图文件：1702883931266109867-02.png。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-107-xss：机制与验证条件 | 保存原图文件：1703115914839752869-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-107-fuzz：机制与验证条件 | 保存原图文件：1703115914839752869-02.jpg。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0190-109-web：机制与验证条件 | 保存原图文件：1703153948499050708-02.jpg。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0190-110-csrf：机制与验证条件 | 保存原图文件：1703162860141195572-02.jpg。 | [方法条目](../by-type/csrf.md) |
| 保存图证0190-114-xss：机制与验证条件 | 保存原图文件：1703348201057865766-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-116-fuzz：机制与验证条件 | 保存原图文件：1703396310366265661-02.jpg。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0190-117-passive：机制与验证条件 | 保存原图文件：1703420769487761905-02.jpg。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0190-124-oauth：机制与验证条件 | 保存原图文件：1703755898131558417-02.jpg。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0190-124-cloud：机制与验证条件 | 保存原图文件：1703755898131558417-02.jpg。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存图证0190-125-auth：机制与验证条件 | 保存原图文件：1703756047012561374-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-129-access：机制与验证条件 | 保存原图文件：1703861590876184653-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0190-130-contract：机制与验证条件 | 保存原图文件：1703861726520000746-02.jpg。 | [方法条目](../by-type/smart-contract.md) |
| 保存图证0190-130-access：机制与验证条件 | 保存原图文件：1703861726520000746-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0190-131-secret：机制与验证条件 | 保存原图文件：1703976073984352560-02.png。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0190-135-auth：机制与验证条件 | 保存原图文件：1704123054006108223-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-138-passive：机制与验证条件 | 保存原图文件：1704146451675160668-02.jpg。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0190-139-strategy：机制与验证条件 | 保存原图文件：1704156762243236153-02.png。 | [方法条目](../hunting-strategy.md) |
| 保存图证0190-142-xss：机制与验证条件 | 保存原图文件：1704176172702064992-02.png。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-148-passive：机制与验证条件 | 保存原图文件：1704213046586134768-02.jpg。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0190-150-passive：机制与验证条件 | 保存原图文件：1704220237128986806-02.png。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0190-156-auth：机制与验证条件 | 保存原图文件：1704431040452854103-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0190-159-xss：机制与验证条件 | 保存原图文件：1704450473988931693-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0190-149-waf：路径错误差异与同条件比较 | 当前保存图1704214535161401832-02.jpg与先前1621064147248222209-02.jpg同哈希，沿用已完成的原图查看记录，不重复计数。 | [方法条目](../by-type/waf-bypass.md) |

| 保存图片中的机制与证据边界（1704450609980854518-02.jpg）：by-type/websocket.md | 图片 `1704450609980854518-02.jpg`：Mozilla1888545 hello.dev.myhubs.net：管理员建房、攻击者加入后presence_diff响应含别人的session_id；摘要称可代发消息，图在presence_diff小附件处截断，没有发送消息请求或接收端状态。 | [方法条目](../by-type/websocket.md) |
| 保存图片中的机制与证据边界（1704450609980854518-02.jpg）：by-type/idor-access-control.md | 图片 `1704450609980854518-02.jpg`：Mozilla1888545 hello.dev.myhubs.net：管理员建房、攻击者加入后presence_diff响应含别人的session_id；摘要称可代发消息，图在presence_diff小附件处截断，没有发送消息请求或接收端状态。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1704480665092370795-02.jpg）：by-type/info-secrets.md | 图片 `1704480665092370795-02.jpg`：Bugzilla1989901：触发登录限流后后续来自其他IP的登录错误可能显示此前触发限流的IP，摘要说错误密码也可看到。 | [方法条目](../by-type/info-secrets.md) |
| 保存图片中的机制与证据边界（1704480665092370795-02.jpg）：by-type/authn-session.md | 图片 `1704480665092370795-02.jpg`：Bugzilla1989901：触发登录限流后后续来自其他IP的登录错误可能显示此前触发限流的IP，摘要说错误密码也可看到。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1704480796390862913-02.jpg）：source-audit.md | 图片 `1704480796390862913-02.jpg`：curl2171309 Informative，摘要称idn.c NULL dereference可读写/RCE，代码只看到decoded=NULL、result=CURLE_OK初始化，后续分配/错误检查/使用截断。 | [方法条目](../source-audit.md) |
| 保存图片中的机制与证据边界（1704480796390862913-02.jpg）：impact-and-acceptance.md | 图片 `1704480796390862913-02.jpg`：curl2171309 Informative，摘要称idn.c NULL dereference可读写/RCE，代码只看到decoded=NULL、result=CURLE_OK初始化，后续分配/错误检查/使用截断。 | [方法条目](../impact-and-acceptance.md) |
| 保存图片中的机制与证据边界（1704544665121472821-02.jpg）：by-type/csrf.md | 图片 `1704544665121472821-02.jpg`：CSRF清单含改GET、删令牌参数/空值、未使用令牌/自有另一账号令牌、等长错值、改首尾、Content-Type变体、Referer正则/省略。 | [方法条目](../by-type/csrf.md) |
| 保存图片中的机制与证据边界（1704547174615499022-02.jpg）：discovery/web-and-api.md | 图片 `1704547174615499022-02.jpg`：宽范围VDP清单经公司收购/被动枚举、httpx、空白200、/directdelivery302、JSP/JS历史找getMaterials.jsp；错误提示疑似需两个参数，param1数组触发不同错误暴露param2，后单引号500并称sqlmap确认。 | [方法条目](../discovery/web-and-api.md) |
| 保存图片中的机制与证据边界（1704547174615499022-02.jpg）：by-type/sql-injection.md | 图片 `1704547174615499022-02.jpg`：宽范围VDP清单经公司收购/被动枚举、httpx、空白200、/directdelivery302、JSP/JS历史找getMaterials.jsp；错误提示疑似需两个参数，param1数组触发不同错误暴露param2，后单引号500并称sqlmap确认。 | [方法条目](../by-type/sql-injection.md) |
| 保存图片中的机制与证据边界（1704641887104098496-02.png）：by-type/mobile-android.md | 图片 `1704641887104098496-02.png`：ARM64反汇编显示svc 0x0及w8=0x38、寄存器设定，提示可能通过直接syscall绕过仅libc层hook的观测；图缺上下文函数/返回值/路径，不证明实际root检测绕过。 | [方法条目](../by-type/mobile-android.md) |
| 保存图片中的机制与证据边界（1704718775839551711-02.jpg）：by-type/desktop-client.md | 图片 `1704718775839551711-02.jpg`：Electron app.asar用asar extract提取资源候选；归档解包不是反编译保证，可能含JS/映射/本机模块，代码可读不自动漏洞。 | [方法条目](../by-type/desktop-client.md) |
| 保存图片中的机制与证据边界（1704718775839551711-02.jpg）：source-audit.md | 图片 `1704718775839551711-02.jpg`：Electron app.asar用asar extract提取资源候选；归档解包不是反编译保证，可能含JS/映射/本机模块，代码可读不自动漏洞。 | [方法条目](../source-audit.md) |
| 保存图片中的机制与证据边界（1704718775839551711-03.jpg）：by-type/subdomain-takeover.md | 图片 `1704718775839551711-03.jpg`：GitHub Pages不存在提示和not found搜索可发现候选，缺失页面不能证明域名可注册/当前接管；需当前DNS、目标归属、平台资源绑定/域验证、授权及受控非敏感证明。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图片中的机制与证据边界（1704718775839551711-04.jpg）：by-type/cache-deception.md | 图片 `1704718775839551711-04.jpg`：AEM/api.json候选Host、X-Forwarded-Server/Host及absolute URI localhost建议。 | [方法条目](../by-type/cache-deception.md) |
| 保存图片中的机制与证据边界（1704718775839551711-04.jpg）：by-type/host-header.md | 图片 `1704718775839551711-04.jpg`：AEM/api.json候选Host、X-Forwarded-Server/Host及absolute URI localhost建议。 | [方法条目](../by-type/host-header.md) |
| 保存图片中的机制与证据边界（1704718775839551711-05.jpg）：by-type/ssrf.md | 图片 `1704718775839551711-05.jpg`：图建议HTTP1.1改HTTP0.9删Host绕过历史修复。 | [方法条目](../by-type/ssrf.md) |
| 保存图片中的机制与证据边界（1704817267815723071-02.jpg）：by-type/crlf-response-splitting.md | 图片 `1704817267815723071-02.jpg`：CRLF清单含%0d%0a、孤立CR/LF、片段%23、双编码%25、路径段及UTF-8字节/字面\u000a、Set-Cookie标记。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图片中的机制与证据边界（1704873265343164652-03.jpg）：by-type/info-secrets.md | 图片 `1704873265343164652-03.jpg`：WPEngine /_wpeprivate/config.json候选图列SESSION_DB_USERNAME/PASSWORD、wpengine_apikey、WP_CACHE_KEY_SALT样例。 | [方法条目](../by-type/info-secrets.md) |
| 保存图片中的机制与证据边界（1704888380948197503-02.jpg）：by-type/file-upload.md | 图片 `1704888380948197503-02.jpg`：Basecamp2107680：用户SVG头像由旧librsvg处理，未初始化内存被编码进预览像素；同处理进程可能有配置/请求等数据。 | [方法条目](../by-type/file-upload.md) |
| 保存图片中的机制与证据边界（1704888380948197503-02.jpg）：by-type/info-secrets.md | 图片 `1704888380948197503-02.jpg`：Basecamp2107680：用户SVG头像由旧librsvg处理，未初始化内存被编码进预览像素；同处理进程可能有配置/请求等数据。 | [方法条目](../by-type/info-secrets.md) |
| 保存图片中的机制与证据边界（1704915539108282415-02.jpg）：by-type/mobile-android.md | 图片 `1704915539108282415-02.jpg`：QuadraInspect帮助菜单SET target及START install_tools/apkleaks/andropass/mobfs/rms，fake.apk与RMS1.5.15本地5000服务启动。 | [方法条目](../by-type/mobile-android.md) |
| 保存图片中的机制与证据边界（1704978949485613367-02.jpg）：by-type/websocket.md | 图片 `1704978949485613367-02.jpg`：Slack1639600官方摘要：创建/撤销Shared Invite Link时，经WebSocket向其他workspace成员传输密码hash，客户端UI未显示；平台无理由认为获明文密码并重置受影响密码。 | [方法条目](../by-type/websocket.md) |
| 保存图片中的机制与证据边界（1704978949485613367-02.jpg）：by-type/info-secrets.md | 图片 `1704978949485613367-02.jpg`：Slack1639600官方摘要：创建/撤销Shared Invite Link时，经WebSocket向其他workspace成员传输密码hash，客户端UI未显示；平台无理由认为获明文密码并重置受影响密码。 | [方法条目](../by-type/info-secrets.md) |
| 保存图片中的机制与证据边界（1705046758982598841-02.jpg）：by-type/xss.md | 图片 `1705046758982598841-02.jpg`：原始HTML示例OpenSearch的h1 String标记反射到og:url meta content和canonical href属性内。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1705200161637662945-03.jpg）：by-type/cmd-injection-rce.md | 图片 `1705200161637662945-03.jpg`：浏览器.jsp?cmd=ls显示autodeploy/Realm.properties/tmp等目录候选，Host及路径遮蔽。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图片中的机制与证据边界（1705220586329563554-02.jpg）：by-type/oauth-oidc.md | 图片 `1705220586329563554-02.jpg`：Nord2049021手动连接服务凭据需邮箱验证的流程；GET /oauth2/auth?redirect_uri=...callback&id_token_hint=...把include_granted_scopes从1改0被声称绕过。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图片中的机制与证据边界（1705220586329563554-02.jpg）：by-type/authn-session.md | 图片 `1705220586329563554-02.jpg`：Nord2049021手动连接服务凭据需邮箱验证的流程；GET /oauth2/auth?redirect_uri=...callback&id_token_hint=...把include_granted_scopes从1改0被声称绕过。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1705296120346443872-02.jpg）：by-type/idor-access-control.md | 图片 `1705296120346443872-02.jpg`：LinkedIn560668摘要限定Recruiter seat持有者可看超出权限的应聘者资料，不是匿名读取所有简历；无端点/字段。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1705361272349298926-02.jpg）：by-type/file-upload.md | 图片 `1705361272349298926-02.jpg`：文件上传帖图内浏览器.php?cmd=cat%20/etc/group，页面为root:x:0等组数据后拼接表情图。 | [方法条目](../by-type/file-upload.md) |
| 保存图片中的机制与证据边界（1705361272349298926-02.jpg）：by-type/cmd-injection-rce.md | 图片 `1705361272349298926-02.jpg`：文件上传帖图内浏览器.php?cmd=cat%20/etc/group，页面为root:x:0等组数据后拼接表情图。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图片中的机制与证据边界（1705417073873113465-02.jpg）：by-type/xss.md | 图片 `1705417073873113465-02.jpg`：og:url属性内h1 String原样，og:title/description编码成&lt;h1&gt;；同输入多个上下文处理不同，应逐输出点观察原始HTML与DOM，属性内尖括号并非新标签，编码差异本身未证明XSS。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1705547136434106470-02.jpg）：by-type/mobile-android.md | 图片 `1705547136434106470-02.jpg`：Frida16.1.3 -U -l root_bypass.js -f遮蔽包，Pixel连接/Spawn恢复后右侧注册页；只表明插桩启动和可见UI，不显示脚本hook内容、JailMonkey版本或业务后端结果。 | [方法条目](../by-type/mobile-android.md) |
| 保存图片中的机制与证据边界（1705657443181568391-02.jpg）：by-type/file-upload.md | 图片 `1705657443181568391-02.jpg`：Carnage输出扩展名混合大小写、双后缀和magic bytes尝试，编号431–438，未示上传接受/保存/执行响应。 | [方法条目](../by-type/file-upload.md) |
| 保存图片中的机制与证据边界（1705658601845473452-02.jpg）：by-type/ssrf.md | 图片 `1705658601845473452-02.jpg`：autoSSRF示例url参数testing.html、Interactsh1.0.7列1个OOB payload地址，未显示接收interaction。 | [方法条目](../by-type/ssrf.md) |
| 保存图片中的机制与证据边界（1705685948867006749-02.png）：by-type/sql-injection.md | 图片 `1705685948867006749-02.png`：POST login.php form username为XOR(if(now()=sysdate(),sleep(5*5),0))表达式，响应302空body显示25,497ms。 | [方法条目](../by-type/sql-injection.md) |
| 保存图片中的机制与证据边界（1705775309512171667-02.jpg）：by-type/xss.md | 图片 `1705775309512171667-02.jpg`：DOM中输入h1string被形成非标准h1string元素并包含span残留，value属性也有同标记；说明重新解析/标签拼接候选，未知元素本身不执行。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1705892274268160247-02.jpg）：by-type/graphql.md | 图片 `1705892274268160247-02.jpg`：Apollo Sandbox/api/graphql?endpoint=https://evil.com使UI Endpoint改变，subscription仍ws://localhost:4000，ExampleQuery id可见；开发探索器可能本来允许任意endpoint。 | [方法条目](../by-type/graphql.md) |
| 保存图片中的机制与证据边界（1705949131707916747-02.png）：targeted-fuzzing.md | 图片 `1705949131707916747-02.png`：crt.sh HTML pup解析、sort/uniq/awk、httpx只200、cut URL取域、paramspider/kxss/grep<>的流水线，输出只显示取历史URL。 | [方法条目](../targeted-fuzzing.md) |
| 保存图片中的机制与证据边界（1705949131707916747-02.png）：discovery/passive-and-services.md | 图片 `1705949131707916747-02.png`：crt.sh HTML pup解析、sort/uniq/awk、httpx只200、cut URL取域、paramspider/kxss/grep<>的流水线，输出只显示取历史URL。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图片中的机制与证据边界（1706210387824161081-02.jpg）：discovery/passive-and-services.md | 图片 `1706210387824161081-02.jpg`：AORT -d example.com --all显示passive候选域，工具宣称valid但图无DNS/HTTP验证；--all可能包含主动阶段，不能按passive标题默认全只读。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图片中的机制与证据边界（1706211558857077247-02.jpg）：by-type/xss.md | 图片 `1706211558857077247-02.jpg`：Toxssin演示handler.js会话及登录表单输入监控/事件注入，说明已有浏览器脚本执行后可影响表单交互；图没有初始XSS注入点，工具宣称MITM并非网络中间人证据。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1706211558857077247-02.jpg）：impact-and-acceptance.md | 图片 `1706211558857077247-02.jpg`：Toxssin演示handler.js会话及登录表单输入监控/事件注入，说明已有浏览器脚本执行后可影响表单交互；图没有初始XSS注入点，工具宣称MITM并非网络中间人证据。 | [方法条目](../impact-and-acceptance.md) |
| 保存图片中的机制与证据边界（1706236146634682761-02.jpg）：by-type/sql-injection.md | 图片 `1706236146634682761-02.jpg`：SQLi Auth Bypass master list为真假恒等式/引号/括号/注释变体；实际字符串或标识符上下文、DB方言/注释空格、绑定参数和后置password条件决定效果，不通用。 | [方法条目](../by-type/sql-injection.md) |
| 保存图片中的机制与证据边界（1706258675692720524-02.jpg）：by-type/authn-session.md | 图片 `1706258675692720524-02.jpg`：Workplace旧文章截图2021：请求含identifier、nonce激活码、community_id、form_data和access_token掩码，称知道目标community_id即可注册并看公司数据，上缘端点/前置流程裁切。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1706258675692720524-02.jpg）：by-type/idor-access-control.md | 图片 `1706258675692720524-02.jpg`：Workplace旧文章截图2021：请求含identifier、nonce激活码、community_id、form_data和access_token掩码，称知道目标community_id即可注册并看公司数据，上缘端点/前置流程裁切。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1706268392842248250-02.png）：by-type/ssrf.md | 图片 `1706268392842248250-02.png`：Encode IP BApp1.0界面只展示选IP→编码方法→复制，不展示具体编码算法或有效绕过。 | [方法条目](../by-type/ssrf.md) |
| 保存图片中的机制与证据边界（1706281791126905242-02.png）：by-type/host-header.md | 图片 `1706281791126905242-02.png`：POST认证流程请求X-Forwarded-Host:evil.com，响应HTML form action指向https://evil.com/auth/realms/...。 | [方法条目](../by-type/host-header.md) |
| 保存图片中的机制与证据边界（1706281791126905242-02.png）：by-type/authn-session.md | 图片 `1706281791126905242-02.png`：POST认证流程请求X-Forwarded-Host:evil.com，响应HTML form action指向https://evil.com/auth/realms/...。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1706315116281770379-02.jpg）：source-audit.md | 图片 `1706315116281770379-02.jpg`：JS instrumentation思路从功能反推参数编码/DOMsink/postMessage与调用函数，hook addEventListener('message')记录处理器和console.trace追来源。 | [方法条目](../source-audit.md) |
| 保存图片中的机制与证据边界（1706315116281770379-02.jpg）：discovery/web-and-api.md | 图片 `1706315116281770379-02.jpg`：JS instrumentation思路从功能反推参数编码/DOMsink/postMessage与调用函数，hook addEventListener('message')记录处理器和console.trace追来源。 | [方法条目](../discovery/web-and-api.md) |
| 保存图片中的机制与证据边界（1706315116281770379-03.jpg）：by-type/xss.md | 图片 `1706315116281770379-03.jpg`：document.write用Proxy apply记录参数并Reflect.apply(...arguments)转发，截图同时讲临时/解包扩展注入。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1706527213292835145-02.png）：discovery/records-and-incremental.md | 图片 `1706527213292835145-02.png`：httpx历史清单含不同twitter子域301/302/404与HSTS/长度列；去重/唯一域不等于唯一服务或完整覆盖。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图片中的机制与证据边界（1706599080011427941-02.jpg）：scope-and-rules.md | 图片 `1706599080011427941-02.jpg`：报告2097911于2023-08-06提交且Resolved(Closed)，仅时间/状态可作政策版本证据，不能证漏洞或奖励应付。 | [方法条目](../scope-and-rules.md) |
| 保存图片中的机制与证据边界（1706602662324572173-02.jpg）：by-type/idor-access-control.md | 图片 `1706602662324572173-02.jpg`：旧报告裁切步骤明确两个账号取organization id、A会话对B org请求并称可取Mopub APIkey；左缘原始路径/字段和响应下半缺失，data含mopub_identity id/confirmed/primary不展示实际秘密。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1706602662324572173-02.jpg）：impact-and-acceptance.md | 图片 `1706602662324572173-02.jpg`：旧报告裁切步骤明确两个账号取organization id、A会话对B org请求并称可取Mopub APIkey；左缘原始路径/字段和响应下半缺失，data含mopub_identity id/confirmed/primary不展示实际秘密。 | [方法条目](../impact-and-acceptance.md) |
| 保存图片中的机制与证据边界（1706624791590109445-02.jpg）：by-type/authn-session.md | 图片 `1706624791590109445-02.jpg`：Nextcloud2052795保存流程/reset填邮箱后Intruder1–50、称302 OK且没有限流。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1706707914109362524-02.jpg）：by-type/iot-security.md | 图片 `1706707914109362524-02.jpg`：MIPS32 debugger messagingagent线程SIGSEGV，saved寄存器及PC/RA出现cyclic样式aaaa值，无法访问/反汇编地址。 | [方法条目](../by-type/iot-security.md) |
| 保存图片中的机制与证据边界（1706725347088269533-02.jpg）：by-type/lfi-path-traversal.md | 图片 `1706725347088269533-02.jpg`：RFI教学图：外部file参数→服务器include远程内容→执行候选；远程URL抓取本身是SSRF/数据加载而不必执行，需确认include/eval语义、语言配置、身份与可达性。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图片中的机制与证据边界（1706862473184215453-02.jpg）：by-type/xss.md | 图片 `1706862473184215453-02.jpg`：script内configureParams['query']赋值单引号字符串含h1 String，未成为HTML元素，需JavaScript字符串上下文检查，不应套HTML标签载荷。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1706942234623438912-02.jpg）：discovery/passive-and-services.md | 图片 `1706942234623438912-02.jpg`：Skanuvaty截图仅大量google子域字符串，包括可疑/重复候选，未给耗时/1000个计数/解析核对。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图片中的机制与证据边界（1706943319496896991-02.jpg）：by-type/cmd-injection-rce.md | 图片 `1706943319496896991-02.jpg`：TryHackMe示例FIFO/Bash/nc循环重复连接监听器，File exists/Connection refused均可见，whoami=root与同IP源目的地。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图片中的机制与证据边界（1706943319496896991-02.jpg）：impact-and-acceptance.md | 图片 `1706943319496896991-02.jpg`：TryHackMe示例FIFO/Bash/nc循环重复连接监听器，File exists/Connection refused均可见，whoami=root与同IP源目的地。 | [方法条目](../impact-and-acceptance.md) |
| 保存图片中的机制与证据边界（1706973509501497694-02.jpg）：by-type/idor-access-control.md | 图片 `1706973509501497694-02.jpg`：私有YouTube视频旧文章开始：区分Public/Unlisted(知道链接可看)/Private(指定许可)，自有第二账号设Private用第一账号试访问；下部具体feature/帧请求未保存。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1707062680538976740-02.jpg）：by-type/subdomain-takeover.md | 图片 `1707062680538976740-02.jpg`：Mozilla2171494摘要mozaws.net某子域dangling DNS被研究者注册并可托管内容，未保存具体子域/服务/绑定步骤。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图片中的机制与证据边界（1707092884548460722-02.jpg）：by-type/desktop-client.md | 图片 `1707092884548460722-02.jpg`：curl2146691/CVE-2023-38039摘要：libcurl为headers API保存响应头，无数量/大小上限让恶意服务器持续发头导致内存耗尽；引用原报告2072338。 | [方法条目](../by-type/desktop-client.md) |
| 保存图片中的机制与证据边界（1707168376613937339-02.jpg）：by-type/subdomain-takeover.md | 图片 `1707168376613937339-02.jpg`：Liberapay 2125346 的历史团队成员 Twitter 失效链接被描述为可注册名称导致可信链接导流；团队卡片及报告文字未证明当前名称可领取或既有账号被接管。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图片中的机制与证据边界（1707168376613937339-02.jpg）：impact-and-acceptance.md | 图片 `1707168376613937339-02.jpg`：Liberapay 2125346 的历史团队成员 Twitter 失效链接被描述为可注册名称导致可信链接导流；团队卡片及报告文字未证明当前名称可领取或既有账号被接管。 | [方法条目](../impact-and-acceptance.md) |
| 保存图片中的机制与证据边界（1707268135907475495-02.jpg）：by-type/lfi-path-traversal.md | 图片 `1707268135907475495-02.jpg`：SMA1000 CVE-2023-0126 单行命令仅是遍历及路径候选；while/read 语法、引号、8443 的实际协议及 curl 对点段的规范化都会影响请求。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图片中的机制与证据边界（1707268135907475495-02.jpg）：targeted-fuzzing.md | 图片 `1707268135907475495-02.jpg`：SMA1000 CVE-2023-0126 单行命令仅是遍历及路径候选；while/read 语法、引号、8443 的实际协议及 curl 对点段的规范化都会影响请求。 | [方法条目](../targeted-fuzzing.md) |
| 保存图片中的机制与证据边界（1707320251216535950-02.jpg）：by-type/idor-access-control.md | 图片 `1707320251216535950-02.jpg`：用户名修改接口返回不透明 E 字段，被移入发票查询示意；所示查询响应为 200 Entity does not belong to client，即对象归属检查拒绝，未展示越权成功。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1707320251216535950-02.jpg）：by-type/authn-session.md | 图片 `1707320251216535950-02.jpg`：用户名修改接口返回不透明 E 字段，被移入发票查询示意；所示查询响应为 200 Entity does not belong to client，即对象归属检查拒绝，未展示越权成功。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1707333333292838946-02.png）：by-type/cmd-injection-rce.md | 图片 `1707333333292838946-02.png`：Juniper 示例 POST / 的 multipart 中 PHPRC=/dev/fd/0 与 auto_prepend_file=/etc/passwd，响应显示账号文件文本及设备管理页；提示客户端输入进入 PHP 配置或预包含通路，但文件文本不能证明命令执行或 root 权限。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图片中的机制与证据边界（1707333333292838946-02.png）：by-type/lfi-path-traversal.md | 图片 `1707333333292838946-02.png`：Juniper 示例 POST / 的 multipart 中 PHPRC=/dev/fd/0 与 auto_prepend_file=/etc/passwd，响应显示账号文件文本及设备管理页；提示客户端输入进入 PHP 配置或预包含通路，但文件文本不能证明命令执行或 root 权限。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图片中的机制与证据边界（1707334475741635032-02.jpg）：by-type/xss.md | 图片 `1707334475741635032-02.jpg`：Mattermost 1502099/CVE-2023-1421 文字列出 OAuth complete 路由，base64 state 的 redirect_to 进入输出的候选；图中本地 GitLab 登录启用与 mobile action 是前提，截断部分没有实际弹窗。 | [方法条目](../by-type/xss.md) |
| 保存图片中的机制与证据边界（1707334475741635032-02.jpg）：by-type/oauth-oidc.md | 图片 `1707334475741635032-02.jpg`：Mattermost 1502099/CVE-2023-1421 文字列出 OAuth complete 路由，base64 state 的 redirect_to 进入输出的候选；图中本地 GitLab 登录启用与 mobile action 是前提，截断部分没有实际弹窗。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图片中的机制与证据边界（1707513168476442680-02.jpg）：targeted-fuzzing.md | 图片 `1707513168476442680-02.jpg`：AI 回答明确给出 hypothetical 日志 URL 示例，example.com/logs/access.log 等不是已发现资产。 | [方法条目](../targeted-fuzzing.md) |
| 保存图片中的机制与证据边界（1707513168476442680-02.jpg）：discovery/passive-and-services.md | 图片 `1707513168476442680-02.jpg`：AI 回答明确给出 hypothetical 日志 URL 示例，example.com/logs/access.log 等不是已发现资产。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图片中的机制与证据边界（1707834821098221907-02.png）：discovery/passive-and-services.md | 图片 `1707834821098221907-02.png`：终端显示 curl 抽取 HTML script src、继续获取 JS 后用正则提取路径；输出混有 SVG 编码片段、第三方 URL 及路径模板。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图片中的机制与证据边界（1707834821098221907-02.png）：discovery/client-and-cloud.md | 图片 `1707834821098221907-02.png`：终端显示 curl 抽取 HTML script src、继续获取 JS 后用正则提取路径；输出混有 SVG 编码片段、第三方 URL 及路径模板。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图片中的机制与证据边界（1707863135225286698-02.jpg）：by-type/host-header.md | 图片 `1707863135225286698-02.jpg`：密码重置教学示例把 Host 或 X-Forwarded-Host 指向外部域，并文字称邮件含该域 token 链接。 | [方法条目](../by-type/host-header.md) |
| 保存图片中的机制与证据边界（1707863135225286698-02.jpg）：by-type/authn-session.md | 图片 `1707863135225286698-02.jpg`：密码重置教学示例把 Host 或 X-Forwarded-Host 指向外部域，并文字称邮件含该域 token 链接。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1707863135225286698-04.jpg）：by-type/business-logic.md | 图片 `1707863135225286698-04.jpg`：密码重置教学列出重复 email 字段及 JSON email 数组；候选风险在验证、查账号、发邮件及消费凭证环节采用不同解析结果。 | [方法条目](../by-type/business-logic.md) |
| 保存图片中的机制与证据边界（1707863135225286698-05.jpg）：by-type/crlf-response-splitting.md | 图片 `1707863135225286698-05.jpg`：注册邮箱教学列逗号、分号、CRLF、NUL、模板字符等候选，未展示服务器或投递结果。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图片中的机制与证据边界（1708036664722112723-02.jpg）：discovery/passive-and-services.md | 图片 `1708036664722112723-02.jpg`：RapidDNS 导出后用 sed 按逗号切列；实际 CSV 字段结构、引号及换行未展示，简单正则可能错取字段或丢记录。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图片中的机制与证据边界（1708036664722112723-02.jpg）：discovery/records-and-incremental.md | 图片 `1708036664722112723-02.jpg`：RapidDNS 导出后用 sed 按逗号切列；实际 CSV 字段结构、引号及换行未展示，简单正则可能错取字段或丢记录。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图片中的机制与证据边界（1708067593100100071-02.jpg）：by-type/idor-access-control.md | 图片 `1708067593100100071-02.jpg`：PayPal 历史文章截图示例 PUT /businessmanage/users/api/v1/users 中两处 id，文字称首项可任意、第二项关联次级用户并导致管理权限和密码修改；没有实际响应或跨账号结果。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图片中的机制与证据边界（1708067593100100071-02.jpg）：by-type/authn-session.md | 图片 `1708067593100100071-02.jpg`：PayPal 历史文章截图示例 PUT /businessmanage/users/api/v1/users 中两处 id，文字称首项可任意、第二项关联次级用户并导致管理权限和密码修改；没有实际响应或跨账号结果。 | [方法条目](../by-type/authn-session.md) |
| 保存图片中的机制与证据边界（1708164932850561388-02.jpg）：scope-and-rules.md | 图片 `1708164932850561388-02.jpg`：正文称 LINE 范围更新，图片却写 Yahoo Japan OTHER Added in Scope 与 Eligible For Bounty false，不能将两者认定同一平台资产或政策。 | [方法条目](../scope-and-rules.md) |
| 保存图片中的机制与证据边界（1708210274673795535-02.jpg）：source-audit.md | 图片 `1708210274673795535-02.jpg`：Node.js 2078581/CVE-2023-30587 摘要限定 Node20 experimental permission 模型，内置 inspector 与 Worker kIsInternal/internal worker 路径可能绕过进程资源权限。 | [方法条目](../source-audit.md) |
| 保存图片中的机制与证据边界（1708210274673795535-02.jpg）：by-type/desktop-client.md | 图片 `1708210274673795535-02.jpg`：Node.js 2078581/CVE-2023-30587 摘要限定 Node20 experimental permission 模型，内置 inspector 与 Worker kIsInternal/internal worker 路径可能绕过进程资源权限。 | [方法条目](../by-type/desktop-client.md) |
| 保存图片中的机制与证据边界（1708331612406968688-02.png）：by-type/waf-bypass.md | 图片 `1708331612406968688-02.png`：WAFW00F 输出宣称目标位于 ModSecurity OWASP CRS 后且请求数 11；没有完整请求响应、规则版本或误报对照。 | [方法条目](../by-type/waf-bypass.md) |
| 输入参与端点构造时先验证每个边界 | 正文建议串联不安全设计并观察输入是否加入端点 URL。 | [方法条目](../business-modeling.md) |
| 公开编辑器 SFTP 配置须确认字段语义 | 两条同正文保存帖给出 /.vscode/sftp.json。 | [方法条目](../by-type/info-secrets.md) |
| WebLogic 模板命中与可利用部署分开确认 | 正文称 WebLogic CVE-2019-2729 模板命中和 RCE，图片仅命令页片段。 | [方法条目](../discovery/web-and-api.md) |
| CakePHP 历史异常页须定位输出上下文 | 正文标注 CakePHP 2.2 stack error 和路径中的引号、标签事件候选，无实际异常响应或执行。 | [方法条目](../by-type/xss.md) |
| CMSmap 历史输出只是部署审计候选 | 相同哈希已审阅图片的当前文件 `1705259160063914367-02.png` 显示 WordPress 4.9.1、2018 年扫描、xmlrpc、用户名、LICENSE、缺失头与 EDB 候选。 | [方法条目](../discovery/web-and-api.md) |
| 公共子域名和证书集合须保留来源时间 | Chaos 公开计划域名文件与 CloudRecon IP/CIDR 证书说明是候选来源。 | [方法条目](../discovery/passive-and-services.md) |
| 状态码路径及非常见端口不能替代资源证据 | 正文提到 403 后追加 /、403/404 过滤 fuzz、多级子域名、非常见端口和 Juniper 搜索。 | [方法条目](../discovery/web-and-api.md) |
| APK 静态 URL 正则不能当运行时接口 | 保存 grep 示例无命令选项空格、使用弯引号，ERE 的 \d/\D 不能按 PCRE 解释。 | [方法条目](../discovery/client-and-cloud.md) |
| PHP 参数名只是 SQL 注入候选 | 正文建议 .php 的 id 与 list[select]，图片只给 Critical 报告标题。 | [方法条目](../by-type/sql-injection.md) |
| AEM 资产 API 与 dispatcher 解析差异 | 正文提出 /content/dam、/api/assets/.../.1.json 及 /content/..;/crx/de/index.jsp。 | [方法条目](../discovery/web-and-api.md) |
| Juniper PHPRC 通路区分配置影响与文件读取 | 正文与图片 `1707333333292838946-02.png` 给 PHPRC=/dev/fd/0、auto_prepend_file=/etc/passwd 与文件文本。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 客户端插桩只记录观察到的调用 | 正文推荐和已保存 Doyensec 图片支持观察 source/sink。 | [方法条目](../source-audit.md) |
| 增量侦察建立可比较的版本集合 | 正文建议持续对比历史数据。 | [方法条目](../discovery/records-and-incremental.md) |
| AEM HTTP 方法差异须证明对象权限 | 正文给 PUT /api/assets/evil..js 和不同 verbs，没有创建/删除结果。 | [方法条目](../by-type/file-upload.md) |
| 生成词表比例与目标覆盖无关 | 正文称 bbFuzzing.txt 90% 来自 ChatGPT，示例图为 example.com。 | [方法条目](../targeted-fuzzing.md) |
| 参数替换须保留解析边界对照 | 正文称按参数或子串替换值，封面无实现。 | [方法条目](../targeted-fuzzing.md) |
| 长期深挖须建立业务权限图 | 正文建议熟悉同一广范围项目。 | [方法条目](../hunting-strategy.md) |
| 搜索配置字段后确认暴露及语义 | 正文声称 Google 条目含 username/password/client_id/client_secret，但保存 dork 只有 > 1，不补造查询和值。 | [方法条目](../by-type/info-secrets.md) |

| 保存图证0192-1-auth：机制与验证条件 | 保存图片 `1708622619803550205-02.jpg`：清单截图实际仅显示基础 admin 示例与空 login/password 两项，标题 97 不能代表保存了全部测试。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0192-7-secret：机制与验证条件 | 保存图片 `1708771306374574246-02.jpg`：ChopChop 示例 foobar.com/.git/config 被标 High/Git exposed，没有完整响应或可恢复仓库。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0192-8-passive：机制与验证条件 | 保存图片 `1708776032214417505-02.jpg`：侦察流程图涵盖 WHOIS/DNS/收购、主动/被动枚举、httpx、端口、历史 URL、目录、Git/JS 和模板扫描。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0192-8-web：机制与验证条件 | 保存图片 `1708776032214417505-02.jpg`：侦察流程图涵盖 WHOIS/DNS/收购、主动/被动枚举、httpx、端口、历史 URL、目录、Git/JS 和模板扫描。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0192-12-access：机制与验证条件 | 保存图片 `1708799828124172435-02.jpg`：API 思维图列对象/属性/功能权限、认证、资源消耗、敏感业务、SSRF、配置、版本清单及第三方数据。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0192-12-business：机制与验证条件 | 保存图片 `1708799828124172435-02.jpg`：API 思维图列对象/属性/功能权限、认证、资源消耗、敏感业务、SSRF、配置、版本清单及第三方数据。 | [方法条目](../business-modeling.md) |
| 保存图证0192-12-web：机制与验证条件 | 保存图片 `1708799828124172435-02.jpg`：API 思维图列对象/属性/功能权限、认证、资源消耗、敏感业务、SSRF、配置、版本清单及第三方数据。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0192-13-auth：机制与验证条件 | 保存图片 `1708801350987845847-02.png`：同形域名图比较字母 l/数字1与所谓西里尔字符视觉相似；图中文字标注不能证明实际 Unicode 码点或 IDNA 有效性。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0192-13-host：机制与验证条件 | 保存图片 `1708801350987845847-02.png`：同形域名图比较字母 l/数字1与所谓西里尔字符视觉相似；图中文字标注不能证明实际 Unicode 码点或 IDNA 有效性。 | [方法条目](../by-type/host-header.md) |
| 保存图证0192-18-ldap：机制与验证条件 | 保存图片 `1708840641466089472-02.png`：Nmap 图仅显示80/389/443 open和其他地址未扫；不能证明 LDAP 匿名 bind、目录可读或全部地址覆盖。 | [方法条目](../by-type/ldap-xpath.md) |
| 保存图证0192-18-passive：机制与验证条件 | 保存图片 `1708840641466089472-02.png`：Nmap 图仅显示80/389/443 open和其他地址未扫；不能证明 LDAP 匿名 bind、目录可读或全部地址覆盖。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0192-19-source：机制与验证条件 | 保存图片 `1708851831705878621-02.png`：ASP.NET 内部图列 IIS 扩展至 handler 映射与 TemplateParser 派生类，以及 ascx 注册/global.asax/master 等入口。 | [方法条目](../source-audit.md) |
| 保存图证0192-19-web：机制与验证条件 | 保存图片 `1708851831705878621-02.png`：ASP.NET 内部图列 IIS 扩展至 handler 映射与 TemplateParser 派生类，以及 ascx 注册/global.asax/master 等入口。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0192-21-xss：机制与验证条件 | 保存图片 `1708865379601117434-02.jpg`：本地 PHP8.2.10 返回 text/xml;charset=UTF-8，p 参数 inject 标签被放在 aaa/bbb 与尾部杂项中；这说明反射，不证明合法 XML、HTML 解析或脚本执行。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-28-secret：机制与验证条件 | 保存图片 `1708972331169652894-03.jpg`：/config/parameters.yml 浏览器显示 pdo_mysql、3306、root 字段，主机/库/密码遮挡。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0192-33-fuzz：机制与验证条件 | 保存图片 `1709109108790497369-02.jpg`：ffuf循环图存在 $1/FUZZ 而迭代变量是 i，域名去端口/协议生成输出名会冲突覆盖，未引用列表变量也易切分。 | [方法条目](../targeted-fuzzing.md) |
| 保存图证0192-33-records：机制与验证条件 | 保存图片 `1709109108790497369-02.jpg`：ffuf循环图存在 $1/FUZZ 而迭代变量是 i，域名去端口/协议生成输出名会冲突覆盖，未引用列表变量也易切分。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0192-37-waf：机制与验证条件 | 保存图片 `1709183962029973965-03.jpg`：Jenkins Script Console 中 Groovy ProcBuilder 加载依赖并拟调用 bash/cat；只是输入，没有执行结果与初始鉴权证据。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0192-37-cmd：机制与验证条件 | 保存图片 `1709183962029973965-03.jpg`：Jenkins Script Console 中 Groovy ProcBuilder 加载依赖并拟调用 bash/cat；只是输入，没有执行结果与初始鉴权证据。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0192-49-xss：机制与验证条件 | 保存图片 `1709399734673145885-02.png`：mobile-header/anchor href 中 String 标记和 URL 编码参数，appID路径/查询片段混合；静态源码呈现的 <h1> 与属性关系不能独立证明最终 DOM 或事件执行。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-49-client：机制与验证条件 | 保存图片 `1709399734673145885-02.png`：mobile-header/anchor href 中 String 标记和 URL 编码参数，appID路径/查询片段混合；静态源码呈现的 <h1> 与属性关系不能独立证明最终 DOM 或事件执行。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0192-56-web：机制与验证条件 | 保存图片 `1709539008542613731-02.jpg`：inDrive2078527摘要称 /metrics 大写变体绕过，保存部分只给/api/metrics基准及期望403，大写结果未保存。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0192-63-takeover：机制与验证条件 | 保存图片 `1709659799452049887-02.jpg`：Mozilla2017323历史摘要称 eideticker dangling DNS 注册后可托管内容，但未给provider/DNS记录/步骤。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0192-64-takeover：机制与验证条件 | 保存图片 `1709659931501289983-02.jpg`：Mozilla2135054历史摘要称 google-cdn-delivery.dev.mozaws.net dangling DNS 后托管，具体provider和请求缺失。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0192-65-redirect：机制与验证条件 | 保存图片 `1709660613176373603-02.jpg`：重定向候选列表混用userinfo @、后缀主机、path中@、编码斜杠和无效host；例如 attacker.com.target.com 属 target 子域而 target.com.attacker.com 属 attacker，path/@ 不自动改变host。 | [方法条目](../by-type/open-redirect.md) |
| 保存图证0192-68-host：机制与验证条件 | 保存图片 `1709721258227531833-02.jpg`：header列表将Base-Url/Client-IP/Referer及拼错字段等值设127.0.0.1；请求头只能在应用实际消费时改变来源/URL语义，不能把全部复制认定SSRF。 | [方法条目](../by-type/host-header.md) |
| 保存图证0192-68-ssrf：机制与验证条件 | 保存图片 `1709721258227531833-02.jpg`：header列表将Base-Url/Client-IP/Referer及拼错字段等值设127.0.0.1；请求头只能在应用实际消费时改变来源/URL语义，不能把全部复制认定SSRF。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0192-69-cmd：机制与验证条件 | 保存图片 `1709777804181520747-02.jpg`：Supermicro BMC40289示例已带SID和CSRF token，config_alert邮件字段夹带shell分隔符和写/tmp/poc命令；没有实际响应/文件证据。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0192-69-iot：机制与验证条件 | 保存图片 `1709777804181520747-02.jpg`：Supermicro BMC40289示例已带SID和CSRF token，config_alert邮件字段夹带shell分隔符和写/tmp/poc命令；没有实际响应/文件证据。 | [方法条目](../by-type/iot-security.md) |
| 保存图证0192-69-source：机制与验证条件 | 保存图片 `1709777804181520747-03.jpg`：反编译图用snprintf拼接 msmtp 命令，sender/mail/路径未显示独立转义，末尾 j_do_popen(command,...)是执行候选sink；用户名密码分支和gmail分支需分别检查，图片没有输入赋值全链。 | [方法条目](../source-audit.md) |
| 保存图证0192-70-xss：机制与验证条件 | 保存图片 `1709810787370643659-02.jpg`：Informatica39069历史2014/Firefox34.0.5例子search.jspa?q含闭合script再新script，2014报告与2023披露不同。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-76-auth：机制与验证条件 | 保存图片 `1709938838687347106-02.jpg`：SMS接口请求带masked手机，响应有ConfirmationStatus true及179/180秒倒计时；这只说明一个响应，不能证明实际发短信、无限次数或公司成本。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0192-76-logic：机制与验证条件 | 保存图片 `1709938838687347106-02.jpg`：SMS接口请求带masked手机，响应有ConfirmationStatus true及179/180秒倒计时；这只说明一个响应，不能证明实际发短信、无限次数或公司成本。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0192-79-access：机制与验证条件 | 保存图片 `1710007082475561420-02.jpg`：LinkedIn1538177摘要称公司页管理员可读取其他公司potential competitors，未给endpoint/字段响应。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0192-85-xss：机制与验证条件 | 保存图片 `1710100686862467372-02.png`：新增 message[subject] 到原有message[body]请求，编码文本示意script/getScript第三方地址；只展示参数构造，管理员查看后触发是正文声称，无callback/浏览器结果。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-85-access：机制与验证条件 | 保存图片 `1710100686862467372-02.png`：新增 message[subject] 到原有message[body]请求，编码文本示意script/getScript第三方地址；只展示参数构造，管理员查看后触发是正文声称，无callback/浏览器结果。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0192-87-files：机制与验证条件 | 保存图片 `1710124099442262330-02.png`：本地127.0.0.1 MLA stream-image.php 的 mla_stream_file 指ftp外部资源，渲染结果显示WordPress配置中的getenv_docker/default示例字段。 | [方法条目](../by-type/file-upload.md) |
| 保存图证0192-87-lfi：机制与验证条件 | 保存图片 `1710124099442262330-02.png`：本地127.0.0.1 MLA stream-image.php 的 mla_stream_file 指ftp外部资源，渲染结果显示WordPress配置中的getenv_docker/default示例字段。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0192-88-xss：机制与验证条件 | 保存图片 `1710125222337065162-02.png`：过滤区button title与可见内容都反射h1/String，前者属性文本、后者HTML候选上下文；相同字符串跨上下文编码要求不同。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-90-access：机制与验证条件 | 保存图片 `1710218469810327751-02.jpg`：HackerOne2069593摘要称draft report评论经program Slack通知泄露，修复阻止draft活动外发。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0192-90-secret：机制与验证条件 | 保存图片 `1710218469810327751-02.jpg`：HackerOne2069593摘要称draft report评论经program Slack通知泄露，修复阻止draft活动外发。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0192-93-sql：机制与验证条件 | 保存图片 `1710350661399806352-02.jpg`：/v1/tagsfilter=asc双引号请求得到MariaDB语法错误，where tag.title_en/id like附近片段；正文称desc双引号而图为asc，要保留差异。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0192-96-strategy：机制与验证条件 | 保存图片 `1710421547511427361-02.jpg`：方法清单列CNAME/历史URL/端口/Git/CORS/CSRF/SSRF/XSS/上传等，存在Arjun找hidden endpoints的误写，应为参数候选；IP头不天然控制可信来源，iframe加载不等于clickjacking，CNAME不等于领取性。 | [方法条目](../hunting-strategy.md) |
| 保存图证0192-96-web：机制与验证条件 | 保存图片 `1710421547511427361-02.jpg`：方法清单列CNAME/历史URL/端口/Git/CORS/CSRF/SSRF/XSS/上传等，存在Arjun找hidden endpoints的误写，应为参数候选；IP头不天然控制可信来源，iframe加载不等于clickjacking，CNAME不等于领取性。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0192-99-report：机制与验证条件 | 保存图片 `1710497500996784289-03.jpg`：报告备注显式列关联历史报告、已付/待付/待审，并称root causes/endpoints不同；这是避免仅标题判断重复的沟通方式，不证明它们实际上独立。 | [方法条目](../reporting.md) |
| 保存图证0192-100-xss：机制与验证条件 | 保存图片 `1710497677228802258-02.png`：DOM图显示img src及onerror与独立字面 \x20 属性，不能把 HTML 中 \x20 当真正U+0020空格；JS字符串解码与HTML词法是不同层。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-100-waf：机制与验证条件 | 保存图片 `1710497677228802258-02.png`：DOM图显示img src及onerror与独立字面 \x20 属性，不能把 HTML 中 \x20 当真正U+0020空格；JS字符串解码与HTML词法是不同层。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0192-102-auth：机制与验证条件 | 保存图片 `1710686557055877588-02.jpg`：WordPress1927360步骤在A/B两设备登录后A开启2FA，B旧会话仍活跃；无全站插件/版本证明。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0192-104-desktop：机制与验证条件 | 保存图片 `1710731860203241972-02.jpg`：Node2091137/CVE30586摘要限定Node20实验permission模型，crypto.setEngine可加载兼容OpenSSL native engine，可能绕过/禁用进程内permission。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0192-104-source：机制与验证条件 | 保存图片 `1710731860203241972-02.jpg`：Node2091137/CVE30586摘要限定Node20实验permission模型，crypto.setEngine可加载兼容OpenSSL native engine，可能绕过/禁用进程内permission。 | [方法条目](../source-audit.md) |
| 保存图证0192-106-desktop：机制与验证条件 | 保存图片 `1710747091855913095-02.jpg`：Node2104564/CVE32004摘要针对Node20实验模型filesystem API处理Buffer路径中的traversal，完整触发/补丁未保存。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0192-106-lfi：机制与验证条件 | 保存图片 `1710747091855913095-02.jpg`：Node2104564/CVE32004摘要针对Node20实验模型filesystem API处理Buffer路径中的traversal，完整触发/补丁未保存。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0192-108-jwt：机制与验证条件 | 保存图片 `1710750989538808008-02.jpg`：OTP JSON code:true 后permission错误并未登录，图继而称JS有HS256 .sign(secret)/Uint8Array并改exp，但无server接受结果。 | [方法条目](../by-type/jwt.md) |
| 保存图证0192-108-auth：机制与验证条件 | 保存图片 `1710750989538808008-02.jpg`：OTP JSON code:true 后permission错误并未登录，图继而称JS有HS256 .sign(secret)/Uint8Array并改exp，但无server接受结果。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0192-109-desktop：机制与验证条件 | 保存图片 `1710762058139275732-02.jpg`：Electron2138080/CVE2023-29198明确contextIsolation+contextBridge，返回嵌套不可序列化对象或getter抛出用户异常的两个前提可能使main-world触及隔离privileged context。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0192-109-source：机制与验证条件 | 保存图片 `1710762058139275732-02.jpg`：Electron2138080/CVE2023-29198明确contextIsolation+contextBridge，返回嵌套不可序列化对象或getter抛出用户异常的两个前提可能使main-world触及隔离privileged context。 | [方法条目](../source-audit.md) |
| 保存图证0192-112-xss：机制与验证条件 | 保存图片 `1710861825749733809-02.jpg`：保存源码有anchor href javascript片段与span中iframe srcdoc内script，域/后半裁剪且无执行结果。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-123-xss：机制与验证条件 | 保存图片 `1711245237811872195-02.jpg`：IRCCloud1887917明确启用Chat&embeds/Embed social media links，用户发Mastodon toot链接后client从[domain]/api/v1/statuses/[id]取canonical URL，第三方instance数据可恶意javascript URL。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-123-client：机制与验证条件 | 保存图片 `1711245237811872195-02.jpg`：IRCCloud1887917明确启用Chat&embeds/Embed social media links，用户发Mastodon toot链接后client从[domain]/api/v1/statuses/[id]取canonical URL，第三方instance数据可恶意javascript URL。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0192-125-xss：机制与验证条件 | 保存图片 `1711335836334309664-02.jpg`：Acronis1940788历史15.0.31791步骤：自有plan+validdevice，plan name持久化img事件，Stop再Confirm后临时消息渲染。 | [方法条目](../by-type/xss.md) |
| 保存图证0192-128-auth：机制与验证条件 | 保存图片 `1711381143415828566-02.jpg`：On1322243历史步骤称Intruder1000错误密码401/正确200，无实际时间窗、锁定状态或后端成功操作。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0192-132-cloud：机制与验证条件 | 保存图片 `1711416868655735198-02.png`：AI泛化AWS配置清单将unused安全组、旧IAM、resource leaks等直接等同风险；未用/旧本身不证明暴露，跨S3复制也不自动明文传输。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存图证0192-132-access：机制与验证条件 | 保存图片 `1711416868655735198-03.png`：AI回答称缺MFA+cloudtrail:CreateTrail可通过创建跨区trail提升权限、仅组织邮箱即可admin，图中没有信任策略或调用链，不能采纳该推断。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0192-135-source：机制与验证条件 | 保存图片 `1711577432183222465-02.jpg`：Cosmovisor2094056摘要称旧版本print sink可能DoS或配置依赖RCE，完整sink代码/攻击输入/host配置缺失。 | [方法条目](../source-audit.md) |
| 保存图证0192-135-cmd：机制与验证条件 | 保存图片 `1711577432183222465-02.jpg`：Cosmovisor2094056摘要称旧版本print sink可能DoS或配置依赖RCE，完整sink代码/攻击输入/host配置缺失。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存图证0192-142-desktop：机制与验证条件 | 保存图片 `1711668027350233180-02.jpg`：Burp1274695历史2021摘要描述headlessChrome远程调试WebSocket端口、已知Chrome XSS+JS端口探测/clickjacking→取得debugGUID，再经download写user.vmoptions，下一次Burp启动及OOM参数才触发OS命令。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0192-142-source：机制与验证条件 | 保存图片 `1711668027350233180-02.jpg`：Burp1274695历史2021摘要描述headlessChrome远程调试WebSocket端口、已知Chrome XSS+JS端口探测/clickjacking→取得debugGUID，再经download写user.vmoptions，下一次Burp启动及OOM参数才触发OS命令。 | [方法条目](../source-audit.md) |
| 保存图证0192-142-click：机制与验证条件 | 保存图片 `1711668027350233180-02.jpg`：Burp1274695历史2021摘要描述headlessChrome远程调试WebSocket端口、已知Chrome XSS+JS端口探测/clickjacking→取得debugGUID，再经download写user.vmoptions，下一次Burp启动及OOM参数才触发OS命令。 | [方法条目](../by-type/clickjacking.md) |
| 保存图证0192-144-client：机制与验证条件 | 保存图片 `1711698240775831552-02.jpg`：Stripe1575014描述Node SDK把用户identifier . 或 ..拼进API路径后规范化，Retrieve Session可能变List Sessions，示例/.变到collection。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0192-144-access：机制与验证条件 | 保存图片 `1711698240775831552-02.jpg`：Stripe1575014描述Node SDK把用户identifier . 或 ..拼进API路径后规范化，Retrieve Session可能变List Sessions，示例/.变到collection。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0192-145-passive：机制与验证条件 | 保存图片 `1711713615428903199-02.png`：枚举记录wc32838输入与476 httpx200候选，再按WordPress等指纹grep分组/正则抽IPv4。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0192-145-records：机制与验证条件 | 保存图片 `1711713615428903199-02.png`：枚举记录wc32838输入与476 httpx200候选，再按WordPress等指纹grep分组/正则抽IPv4。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存正文0192：Servlet 矩阵参数需比较解析边界 | 正文称Java Servlet矩阵参数曾得到奖励，未保存完整请求。 | [方法条目](../discovery/web-and-api.md) |
| 保存正文0192：AEM childrenlist 的反射须匹配渲染上下文 | 正文给childrenlist.html路径中的编码img/event候选，没有响应或执行。 | [方法条目](../by-type/xss.md) |
| 保存正文0192：JCR selector 输出和 SHA1 字段不能推断秘密 | /content/.5..json/a.png是selector/深度/路径解释候选，正文称可能发现SHA1，未给实际字段。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0192：eval(name) 依赖可控浏览器上下文 | script eval(name)只是执行sink示例，需先有脚本注入和对应window.name可控值、同源导航/浏览器行为及CSP。 | [方法条目](../by-type/xss.md) |
| 保存正文0192：奖励例外不替代测试范围规则 | 正文称out of scope有时奖励或SMS限速例外接受，图片只奖励/单个接口结果。 | [方法条目](../scope-and-rules.md) |
| 保存正文0192：跨端 SSO 的 2FA 与旧会话状态分别核对 | 正文建议web开启2FA后检查mobileSSO，WordPress图仅旧会话继续活跃。 | [方法条目](../by-type/authn-session.md) |
| 保存正文0192：搜索词进入路径或页面不证明命令执行 | 正文whoami反射到/whoami.php仅提出疑问。 | [方法条目](../by-type/xss.md) |
| 保存图证0192：docker compose 是配置暴露候选 | 当前 `1709322255530865031-03.png` 与既有原图同哈希，沿用已完成查看。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0192：ACL fuzz 标签需真实保护资源对照 | 工具描述测试headers、path normalization与verbs，inDrive摘要仅有metrics403基准。 | [方法条目](../discovery/web-and-api.md) |
| 保存正文0192：资源名可用与领取后域控制不同 | trafficmanager正文称名字可用却创建失败，GitHubPagesnotfound搜索与模板命中是另外候选。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存正文0192：页面依赖 API 的授权须单独核对 | 正文admin.target.com调用api2，而列出的scope只有admin/api。 | [方法条目](../scope-and-rules.md) |
| 保存正文0192：returnTo 协议校验与脚本 sink | 正文称login returnTo=javascript:值后登录弹窗，图片只有奖励卡。 | [方法条目](../by-type/xss.md) |
| 保存正文0192：AI 词表来源不是覆盖证明 | bbFuzzing90%来自ChatGPT只有来源比例，已保存封面无词条。 | [方法条目](../targeted-fuzzing.md) |
| 保存正文0192：被拒绝的编码穿越须保留为反例 | 正文仅称普通、多斜杠及doubleencoded .%252e/.../etc/passwd被Forbidden，成功后续未保存。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存正文0192：Juniper 指纹与 PHPRC 文件响应分开 | 正文Shodan title/favicon与PHPRC=/dev/fd/0、auto_prepend_file文件示例分别是识别与PHP配置/预包含候选。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存正文0192：客户端 verify 改真不证明 OTP 绕过 | 正文修改响应verify:false为true，图片只有支付邮件。 | [方法条目](../by-type/authn-session.md) |
| 保存正文0192：混合闭合字符串必须匹配实际上下文 | 保存payload混合JS注释、script闭合、引号和alert片段，图仅Resolved。 | [方法条目](../by-type/xss.md) |
| 保存正文0192：iframe srcdoc 需要嵌套上下文检查 | 正文给iframe srcdoc中的script示例，另保存图有anchor/span嵌套iframe候选。 | [方法条目](../by-type/xss.md) |

| 保存正文0193：带参数 URL 的索引只是候选入口 | 正文以inurl问号/百分号问号及OR含&检索构造参数URL候选。 | [方法条目](../discovery/passive-and-services.md) |
| 保存正文0193：CloudShell 计算资源不提供测试授权 | 正文提出打开CloudShell终端运行自动化，但未保存具体流程。 | [方法条目](../scope-and-rules.md) |
| 保存正文0193：Unicode、Hex 和 HTML 实体须按解码层拆分 | 正文推荐Unicode/Hex/HTML实体和CyberChef。 | [方法条目](../by-type/xss.md) |
| 保存正文0193：客户端 AG Grid license 不自动属于身份秘密 | 正文从setLicenseKey关注商业license费用。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0193：旧目录和大小写变体先核实实际功能 | 正文phpmyadmin/setup/index.php返回403，而phpMyAdminOLD/setup/index.php称200。 | [方法条目](../discovery/web-and-api.md) |
| 保存正文0193：将邀请 URL 整体作输入需证明服务器取回 | 正文仅说整段邀请URL引向blind SSRF，保存步骤不完整。 | [方法条目](../by-type/ssrf.md) |
| 保存正文0193：RCE 向量清单不能跳过执行链的额外前提 | 正文列EXIF、SSTI、依赖、SQL、LFI、XXE、命令、反序列化和上传等候选。 | [方法条目](../by-type/cmd-injection-rce.md) |
| 保存正文0193：config.js 的字段可见与凭据有效性分开 | 正文提API key/client id/secret并保留curl连接失败。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0193：额外 on0x 属性与真实事件执行分开 | 正文声称WordPress DOM XSS绕Cloudflare并给img src=x on0x=1 onerror示例。 | [方法条目](../by-type/xss.md) |
| 保存正文0193：过滤绕过必须绑定原始字节和同一注入上下文 | 正文普通script受403、img额外属性被接收的说法只有局部DOM图支持。 | [方法条目](../by-type/waf-bypass.md) |
| 保存正文0193：云存储 dork 的品牌文字不证明资源归属 | 正文给s3、blob、googleapis、drive等索引候选。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存正文0193：空文件响应不能直接推存在可枚举子目录 | 正文建议空内容仍继续向内fuzz。 | [方法条目](../targeted-fuzzing.md) |
| 保存正文0193：点段和空查询响应不同不直接证明认证绕过 | 正文同体两帖列/admin403、/random-dir/../admin200及Cloudflare1006对/admin?200。 | [方法条目](../by-type/idor-access-control.md) |
| 保存正文0193：env.example 可以泄配置，也可以只是示例 | 两帖补充/.env.example词表。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0193：Burp 噪音排除可能形成观测盲区 | 正文以google/gstatic/googleapis/analytics/tagmanager等正则降噪。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存正文0193：第三方桶索引和枚举器只负责候选发现 | 正文指向GrayhatWarfare和cloud_enum，线程其余未保存。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存正文0193：启动本地 Burp 不会把远端源 IP 自动变为回环 | 两帖说开启Burp后IP变127.0.0.1而所有路径打开，未保存实际header/转发链。 | [方法条目](../by-type/waf-bypass.md) |
| 保存正文0193：复杂 SaaS 功能拆成状态和角色边界 | 正文建议寻找最复杂、令人困惑的功能。 | [方法条目](../business-modeling.md) |
| 保存正文0193：正则检查器告警需有可控长度与成本证据 | 正文建议审注入点regex并借助ReDoS checker。 | [方法条目](../source-audit.md) |
| 保存正文0193：docker-compose.yml 可发现配置，标题不证明秘密 | 正文仅给路径，图三个High报告标题。 | [方法条目](../cloud/container-k8s-security.md) |
| 保存正文0193：PHP 备份响应必须确认静态源码泄露 | 正文wp-config.php403而wp-config.php.bak200并称下载DB凭据。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0193：测试邮箱规则属于项目约束 | 正文称使用普通邮箱而非H1 alias被关闭。 | [方法条目](../scope-and-rules.md) |
| 保存正文0193：ServiceNow 扫描阳性仍需最小数据证据 | 正文列scanner、新表、--fast-check，并明确exposed table可能有意公开；截图模板对widget-simple-list t=kb_knowledge&f=text输出500。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0193：按问号前路径去重会丢失参数结构 | 正文awk -F问号以$1首次保留,page23/page22示例会保留第一条整URL而非清空参数；同路径不同参数名/方法/鉴权/状态可能合并丢失。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存正文0193：多层编码事件载荷需按实际解析顺序验证 | 正文details含%0A、onToGgle、co\u006efirm别名、%28及HTML字符引用；同帖保存拒绝页与确认框两图。 | [方法条目](../by-type/xss.md) |
| 保存正文0193：Bard 回答与 Critical 字段不能证明泄密 | 同一截图curl2199174状态N/A，报告根据Bard声称curl_easy_setopt整数溢出及尚未公开补丁，与同批保存SOCKS5状态机报告机制不同。 | [方法条目](../reporting.md) |
| 保存正文0193：重置码必须绑定待修改的账号主体 | 正文称保留自己的reset link只替换Email后改另一人密码，保存图有Code、Email与RequestVerificationToken但无结果。 | [方法条目](../by-type/authn-session.md) |
| 保存正文0193：DotGit 扩展不能保证还原完整仓库 | 正文用Shodan证书公司名定位IP，再由DotGit下载仓库。 | [方法条目](../by-type/info-secrets.md) |
| 保存正文0193：在线端口检测的观测点不同于本地 | 正文以portchecker替代Nmap。 | [方法条目](../discovery/passive-and-services.md) |
| 保存正文0193：scope 更新截图是历史差异 | 正文称Databricks scope更新，图只五域eligible true。 | [方法条目](../scope-and-rules.md) |
| 保存图证0193-96：复用 IDOR 清单时保留当前来源与反例 | 当前文件1713621439004418480-02.jpg与先前已视觉审阅SHA相同，未重复计视觉审阅。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0193-4-client：机制、前提与最小验证 | 已查看的原始图片：1712015316350648410-02.jpg。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0193-5-client：机制、前提与最小验证 | 已查看的原始图片：1712015464950563207-02.jpg。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0193-18-desktop：机制、前提与最小验证 | 已查看的原始图片：1712166349970297192-02.jpg。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0193-20-doc：机制、前提与最小验证 | 已查看的原始图片：1712318128128950657-02.jpg、1712318128128950657-03.jpg。 | [方法条目](../by-type/document-rendering.md) |
| 保存图证0193-24-impact：机制、前提与最小验证 | 已查看的原始图片：1712423012983783837-02.jpg。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0193-28-secret：机制、前提与最小验证 | 已查看的原始图片：1712582122983075963-02.png。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-30-xss：机制、前提与最小验证 | 已查看的原始图片：1712674268486512919-02.jpg、1712674268486512919-03.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0193-30-waf：机制、前提与最小验证 | 已查看的原始图片：1712674268486512919-03.jpg。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0193-35-auth：机制、前提与最小验证 | 已查看的原始图片：1712785402820808817-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0193-36-contract：机制、前提与最小验证 | 已查看的原始图片：1712793678639730850-02.jpg。 | [方法条目](../by-type/smart-contract.md) |
| 保存图证0193-37-xss：机制、前提与最小验证 | 已查看的原始图片：1712815758844314010-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0193-39-takeover：机制、前提与最小验证 | 已查看的原始图片：1712830694408298678-02.jpg。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0193-42-secret：机制、前提与最小验证 | 已查看的原始图片：1712845785384272044-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-51-client：机制、前提与最小验证 | 已查看的原始图片：1712966583755419769-02.jpg。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0193-51-lfi：机制、前提与最小验证 | 已查看的原始图片：1712966583755419769-02.jpg。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0193-52-client：机制、前提与最小验证 | 已查看的原始图片：1712966716270272776-02.jpg。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0193-52-lfi：机制、前提与最小验证 | 已查看的原始图片：1712966716270272776-02.jpg。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0193-53-client：机制、前提与最小验证 | 已查看的原始图片：1712966859207921907-02.jpg。 | [方法条目](../discovery/client-and-cloud.md) |
| 保存图证0193-54-logic：机制、前提与最小验证 | 已查看的原始图片：1713011879415890382-02.jpg。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0193-59-secret：机制、前提与最小验证 | 已查看的原始图片：1713130465752715350-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-61-secret：机制、前提与最小验证 | 已查看的原始图片：1713139332775583794-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-63-xss：机制、前提与最小验证 | 已查看的原始图片：1713194634753573206-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0193-66-records：机制、前提与最小验证 | 已查看的原始图片：1713207711553261681-02.jpg。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0193-73-csrf：机制、前提与最小验证 | 已查看的原始图片：1713283675289493618-02.jpg。 | [方法条目](../by-type/csrf.md) |
| 保存图证0193-73-xss：机制、前提与最小验证 | 已查看的原始图片：1713283675289493618-02.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0193-89-secret：机制、前提与最小验证 | 已查看的原始图片：1713547774225248398-02.png。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-90-xss：机制、前提与最小验证 | 已查看的原始图片：1713556041386926551-02.png。 | [方法条目](../by-type/xss.md) |
| 保存图证0193-92-desktop：机制、前提与最小验证 | 已查看的原始图片：1713562873689948348-02.png、1713562873689948348-03.jpg、1713562873689948348-04.png。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0193-92-source：机制、前提与最小验证 | 已查看的原始图片：1713562873689948348-02.png。 | [方法条目](../source-audit.md) |
| 保存图证0193-92-secret：机制、前提与最小验证 | 已查看的原始图片：1713562873689948348-04.png。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-97-access：机制、前提与最小验证 | 已查看的原始图片：1713633216572338530-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0193-99-access：机制、前提与最小验证 | 已查看的原始图片：1713654039970287649-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0193-104-waf：机制、前提与最小验证 | 已查看的原始图片：1713783215305949614-02.jpg、1713783215305949614-03.jpg。 | [方法条目](../by-type/waf-bypass.md) |
| 保存图证0193-104-xss：机制、前提与最小验证 | 已查看的原始图片：1713783215305949614-03.jpg。 | [方法条目](../by-type/xss.md) |
| 保存图证0193-107-report：机制、前提与最小验证 | 已查看的原始图片：1713902765431558327-02.jpg。 | [方法条目](../reporting.md) |
| 保存图证0193-107-ai：机制、前提与最小验证 | 已查看的原始图片：1713902765431558327-02.jpg。 | [方法条目](../by-type/ai-application.md) |
| 保存图证0193-110-secret：机制、前提与最小验证 | 已查看的原始图片：1713931526394523881-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-111-logic：机制、前提与最小验证 | 已查看的原始图片：1713932957470367920-02.jpg。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0193-112-cloud：机制、前提与最小验证 | 已查看的原始图片：1713941004431110261-02.jpg。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 保存图证0193-116-secret：机制、前提与最小验证 | 已查看的原始图片：1713997801007280210-02.jpg。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0193-117-ws：机制、前提与最小验证 | 已查看的原始图片：1713997838840152426-02.jpg。 | [方法条目](../by-type/websocket.md) |
| 保存图证0193-118-access：机制、前提与最小验证 | 已查看的原始图片：1713999151526969781-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0193-119-cors：机制、前提与最小验证 | 已查看的原始图片：1713999851283988719-02.jpg。 | [方法条目](../by-type/cors.md) |
| 保存图证0193-120-auth：机制、前提与最小验证 | 已查看的原始图片：1714000176010928137-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0193-120-access：机制、前提与最小验证 | 已查看的原始图片：1714000176010928137-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0193-127-scope：机制、前提与最小验证 | 已查看的原始图片：1714260078298116141-02.jpg。 | [方法条目](../scope-and-rules.md) |
| 保存图证0193-134-passive：机制、前提与最小验证 | 已查看的原始图片：1714448454347534572-02.jpg。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0193-137-access：机制、前提与最小验证 | 已查看的原始图片：1714582096574914676-02.jpg。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0193-137-auth：机制、前提与最小验证 | 已查看的原始图片：1714582096574914676-02.jpg。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0193-138-xss：机制、前提与最小验证 | 已查看的原始图片：1714582274862440476-02.jpg。 | [方法条目](../by-type/xss.md) |

| 0194：SVG 上传的客户端拦截与实际渲染边界 | 正文说 SVG 仅被客户端阻止，留下的是验证方向。 | [方法条目](../by-type/file-upload.md) |
| 0194：AEM dispatcher 与 JSP 路由解析差异 | 保存正文给出 /content/..;a=a/crx/de/index.jsp/.css、index.jsp;.css、index.jsp?.css 三类候选。 | [方法条目](../by-type/waf-bypass.md) |
| 0194：二次上下文中的输入重用与验证语义 | 配图把外部 /profile?id 值拼入带认证的内部 /api/profiles/.../info 路由，并讨论 %23、%3f、%26、%2e、%2f、%40 等 URI 保留字符和编码。 | [方法条目](../discovery/web-and-api.md) |
| 0194：OTP 的成功响应必须绑定验证入口 | Authy 示意指出 SDK 拼接路径可落到另一总是返回 success 的入口。 | [方法条目](../by-type/authn-session.md) |
| 0194：隐藏管理入口的发现与权限检验 | /admin、/admin/dashboard、/cms 及 Adminfinder/Gobuster 属于入口候选。 | [方法条目](../discovery/web-and-api.md) |
| 0194：APK 中的 URL 与 IP 是版本化候选 | apk2url 宣传说明从 APK 提取地址。 | [方法条目](../discovery/client-and-cloud.md) |
| 0194：混合编码事件属性的解析前提 | 正文 details/onToggle 候选同时使用百分号、JavaScript Unicode 标识符转义和 HTML 数字实体。 | [方法条目](../by-type/xss.md) |
| 0194：模板代码协议与签名的不同保证 | 保存 Nuclei v3 宣传明确模板可执行 bash/shell/Python，并可组合 DNS/HTTP 与签名。 | [方法条目](../source-audit.md) |
| 0194：脚本输出字段和下载证据的稳定性 | 配图中的 awk 固定字段与 wget ZIP 输出可用于梳理项目记录，但空白、字段变化、未引用变量、同名覆盖和下载失败会污染结果。 | [方法条目](../discovery/records-and-incremental.md) |
| 0194：点击劫持以敏感动作而非登录页为验证单位 | 正文建议关注每个敏感动作。 | [方法条目](../by-type/clickjacking.md) |
| 0194：源站 IP 候选需要同一虚拟主机对照 | 保存工具说明用 HTTP 响应和 Censys 等线索比较候选源站。 | [方法条目](../discovery/passive-and-services.md) |
| 0194：双斜线输入与浏览器最终 authority | 正文 https://www.[target].com//evil.com/ 的双斜线位于已有 authority 后，通常是目标主机的路径。 | [方法条目](../by-type/open-redirect.md) |
| 0194：备份词表与当前可读取内容 | backup-gen 从输入 URL 生成备份候选。 | [方法条目](../discovery/passive-and-services.md) |
| 0194：隐藏参数发现与漏洞效果应分开 | 正文 Arjun 找参数和奖金只说明线索。 | [方法条目](../targeted-fuzzing.md) |
| 0194：web.zip 的主机与备份路径不能混写 | 正文多次写 http://web.zip，这是独立主机 URL，不能直接当当前目标的 /web.zip。 | [方法条目](../by-type/info-secrets.md) |
| 0194：UUID、整数和邮箱标识走不同查询分支 | 保存正文建议对同一用户的 UUID、整数、邮箱比较。 | [方法条目](../by-type/idor-access-control.md) |
| 0194：tx.origin 示例先核编译与实际授权主体 | 截图的 withdrawFunds 用 tx.origin==owner 后低层发送余额，并对未声明 balance 做减法。 | [方法条目](../by-type/smart-contract.md) |
| 0194：DOM sink 要按解析与导航语义区分 | 正文列举 location、innerHTML、eval，图片显示 redirecturl=javascript:... 和弹窗。 | [方法条目](../by-type/xss.md) |
| 0194：添加监控项与发现变化的证据 | Sublert 图仅显示添加 monitored domain，另一图只是监控视频封面。 | [方法条目](../discovery/records-and-incremental.md) |
| 0194：日志中的云盘 key 与可读对象边界 | 正文主张 /logs 泄 Dropbox authorization key 并能读取未播出的节目，图片只有奖励通知。 | [方法条目](../by-type/info-secrets.md) |
| 0194：CMS 首页登录不能代表所有 API 的授权 | WordPress 首页跳登录、图片显示 Office365 与本地登录只说明前端入口。 | [方法条目](../discovery/web-and-api.md) |
| 0194：公开视频 PoC 的脱敏要覆盖整段附件 | 多个保存图关联 H1 2134874/2215434 及公开视频中邮箱或文件夹标识；附件细节未完整保存，不转录个人值。 | [方法条目](../reporting.md) |
| 0194：白名单检查和实际 token 发送目标必须一致 | GitSourceEditor 图文描述先用 new URL(a).origin 校验，再对整个 URL 使用正则抽取 host/project/file；合法 googlesource origin 的路径/fragment 可让后续组指向另一 host。 | [方法条目](../by-type/oauth-oidc.md) |
| 0194：泄露 token 的 scope 与业务 entitlement 分开 | 截图列 email/profile/openid/gerritcodereview/androidbuild.internal，部分仓库读写是正文所述测试，内网权限及其他编辑器仅为假设。 | [方法条目](../impact-and-acceptance.md) |
| 0194：历史资产资格与范围外奖励不构成新授权 | CosmWasm SOURCE_CODE eligible:true 图是当时单个代码资产资格，Airlock 通知则明示报告 out of scope 但奖励。 | [方法条目](../scope-and-rules.md) |
| 0194：CitrixBleed 扫描命中与会话泄漏证明 | 截图 Nuclei 3.0.1/template 9.6.7 对 GetUserName 路径报 Critical 命中，没有原始 matcher、响应 bytes 或泄露 token。 | [方法条目](../by-type/info-secrets.md) |
| 0194：时间型 SQL 候选需要方言、上下文和交错计时 | 两段正文使用 MySQL XOR/if(now()=sysdate(),sleep(...),0)，一段放 X-Forwarded-For 并以 httpx 响应超过 13 秒筛选。 | [方法条目](../by-type/sql-injection.md) |
| 0194：后台 probe 回调与内网枚举是不同证据 | Exness 图片保存 probe POST 的 data.url 及 Oastify DNS/HTTP GET。 | [方法条目](../by-type/ssrf.md) |
| 0194：AI 扫描图必须保留执行与证据边界 | Nebula 图把模型、漏洞候选、命令建议、执行及存储串联；工具列表和箭头不证明这些能力已实现或可靠。 | [方法条目](../by-type/ai-application.md) |
| 0194：对象 key、文件元数据与本机路径要分别证明 | 正文称上传后泄本机路径，但保存图只见 S3 key 中 users/username/hash/profile 与 Screenshot 日期文件名。 | [方法条目](../by-type/file-upload.md) |
| 0194：历史 URL 文件筛选保留发现时间和归属 | Wayfiles 正文说明筛选 gau/waymore/waybackurls 的本地文件或目录。 | [方法条目](../discovery/passive-and-services.md) |
| 0194：搜索 query 的事件触发与 DOM 标签的证据 | TD 搜索截图给出包含标签及 onmouseover 的 query，需要实际 HTML 插入和悬停。 | [方法条目](../by-type/xss.md) |
| 0194：未公开 mutation 与隐藏界面不代替对象授权 | Copilot 图描述 JS 中的未公开 GraphQL 与 DestroyLlmConversation，移除 hidden 类只控制显示。 | [方法条目](../by-type/graphql.md) |
| 0194：Ingress 可写字段到配置注入的连续边界 | permanent-redirect annotation 与 spec.rules.http.paths.path 两报告图的前提都是 Ingress create 或 update 权限。 | [方法条目](../cloud/container-k8s-security.md) |
| 0194：OTP 状态必须由每个日志下载入口执行 | Lark 图描述组织内用户直接下载 AdminLog 绕过邮件 OTP。 | [方法条目](../by-type/authn-session.md) |
| 0194：HTML 子域正则的匹配数和唯一主机数 | 三张图 wget 保存 HTML 后 grep [a-z0-9]*.yahoo.com 并得到 wc 531。 | [方法条目](../discovery/passive-and-services.md) |
| 0194：公共历史提交中的 API key 需要权限分类 | Flickr 图定位 Mozilla 公共仓库特定 commit 与 media/js/flickr.js#L4，附件不可见且无有效调用。 | [方法条目](../by-type/info-secrets.md) |
| 0194：自动化配图的实际阶段与正文主张 | 正文说 JS 端点发现，但图是多个子域源、Shodan JSON、sort-uniq、puredns、dsieve 与分级 bruteforce。 | [方法条目](../discovery/passive-and-services.md) |
| 0194：旧登录入口与三倍延迟线索 | 正文新登录 SQLi 失败、旧 OLD_login.asp 单引号 500 再 WAITFOR 候选；图中 6 秒标记约 18 秒，4 秒约 12 秒。 | [方法条目](../by-type/sql-injection.md) |
| 0194：生成 dork 链接不代表已搜索或可读取 | 本帖图片与已阅 1688178235643727873-02.jpg 的 SHA 完全一致，当前文件 1717747045258101107-02.jpg 为重复图。 | [方法条目](../discovery/passive-and-services.md) |
| 0194：存储下载与工作站冒充主张缺少链条 | 正文称 AWS 下载会执行恶意脚本并冒充公司工作站，配图只有 OBS 录屏窗口。 | [方法条目](../cloud/cloud-misconfiguration.md) |
| 0194：第三方翻译编辑权到发布影响的边界 | Mozilla 图描述泄露的 Smartling 凭据关联部分项目及内部翻译 jobs/documents。 | [方法条目](../business-modeling.md) |
| 0194：一人一次投票必须检查最终原子状态 | Urban Dictionary 图保存 vote GET 和 11 线程重复接受主张。 | [方法条目](../by-type/business-logic.md) |
| 0194：提交 notes 不应授予 DagRun 其他字段写权限 | Airflow 图述 2.7.1 之前 DAG-view 用户通过 notes 提交修改配置/开始时间。 | [方法条目](../by-type/idor-access-control.md) |
| 0194：删除状态在旧 RSS 读取链上的一致性 | Glassdoor 摘要限定删除 employer profile 后部分 interview 仍从弃用 RSS 可读。 | [方法条目](../discovery/records-and-incremental.md) |
| 0194：取得用户 token 与目标 client 校验是两个边界 | 保存流程图区分授权 code 与 access token，并声称给 TimePlanner 签发的 token 被另一登录应用接受。 | [方法条目](../by-type/oauth-oidc.md) |
| 0194：公开 Postman 集合中的模板与真实凭据 | PostLeaks 图提取请求路径、query、headers、bearer 和 {{token}} 模板。 | [方法条目](../by-type/info-secrets.md) |
| 0194：改造公开方法保留来源与独立验证 | 正文建议借用他人的思路但以自己的合法发现报告。 | [方法条目](../reporting.md) |
| 0194：403 与 JS 线索不能直接升级成 PII 越权 | 正文提出 403 后从 JS/GAP/OSINT 寻入口并称获得 PII，配图只有报告标题。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0194-4-oauth：1714650037718749438-02.png | OAuth AuthorizationCode图Browser→Server→IdP返code→server兑换accessToken→profile→数据；将OAuth当认证省略state/redirectURI/client/PKCE及IDtoken校验。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-6-report：1714672833761304957-02.jpg | H1公开262661视频PoC6:00-7:15泄研究者邮箱，报告2134874无rating；图视频嵌套小无可读邮箱，不转录PII。 | [方法条目](../reporting.md) |
| 保存图证0194-6-secret：1714672833761304957-02.jpg | H1公开262661视频PoC6:00-7:15泄研究者邮箱，报告2134874无rating；图视频嵌套小无可读邮箱，不转录PII。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-11-strategy：1714872137163678078-02.jpg | 4tips responsible disclosure、少工具懂原理、改造公开method、JS/postauth/multilevel拓展。 | [方法条目](../hunting-strategy.md) |
| 保存图证0194-11-scope：1714872137163678078-02.jpg | 4tips responsible disclosure、少工具懂原理、改造公开method、JS/postauth/multilevel拓展。 | [方法条目](../scope-and-rules.md) |
| 保存图证0194-16-desktop：1714991932701913556-02.jpg | 图管理员PowerShell左poc/Terminator.sys载driver并终止防护进程，右IEX加载InvokeMimikatz privilege::debug/logonpasswords哈希遮盖；正文NativeSyscall injector与图不同链。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0194-17-web：1715012428801720620-02.jpg | 二次路由profile?id=1前端host→internalhost api/profiles/1/info返JSON；服务端另请求可能带auth，输入拼路径/headers需独立边界验证。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0194-17-ssrf：1715012428801720620-02.jpg | 二次路由profile?id=1前端host→internalhost api/profiles/1/info返JSON；服务端另请求可能带auth，输入拼路径/headers需独立边界验证。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0194-17-web：1715012428801720620-03.jpg | 识别二次route：/api/../ vs/、%23%3f%26%2e%2f%40多编码、目录headers变化、internalhost8080 500信息。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0194-17-auth：1715012428801720620-04.jpg | Authy示例拼/protected/json/verify/token/id，服务器仅200+success true而/protected/json也真；路径参数能改endpoint则与验证语义错绑。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0194-27-records：1715299642601263594-02.png | Bash脚本用echo未引用prog_details_values按awk$8$9取bounty/time显示表，dumper wget-q未引用$prog_url输出$selected_prog.zip；空白/字段漂移、引用/文件名碰撞/下载失败记录需核，ZIP后缀不是内容证明，脚本未运行。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0194-29-xss：1715307044381859939-02.jpg | Mozillaunsubscribe1913263报告明确IP被封未获得realPoC，只给闭title/script/marqueeURL，script Alert(xss)大小写/未定义变量也需context核。 | [方法条目](../by-type/xss.md) |
| 保存图证0194-37-secret：1715427820841980190-02.jpg | /_vti_inf.html代码注释FPVersion16.0.0.000、FPshtmlScriptUrl _vti_bin/shtml.dll/_vti_rpc、FPAuthorScriptUrl author.dll、FPAdminScriptUrl admin.dll、TPScriptUrl owssvr.dll。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-37-web：1715427820841980190-02.jpg | /_vti_inf.html代码注释FPVersion16.0.0.000、FPshtmlScriptUrl _vti_bin/shtml.dll/_vti_rpc、FPAuthorScriptUrl author.dll、FPAdminScriptUrl admin.dll、TPScriptUrl owssvr.dll。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0194-44-secret：1715668195254628477-02.jpg | Salesforce /s/sfsites/aura?r=5&aura.RecordUi.getRecordWithFields=1 POST响应actions.state ERROR exceptionEvent/useDefaultfalse aura serverActionError资源不存在含stackTrace/core.connect.api.ConnectInJavaException。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-59-access：1716093428709421564-02.png | SQL subscribers CASE优先$1>0 id，否则$2非空uuid::$UUID，再$email；参数化代码本身不证SQLi/IDOR，SELECT*无可见owner条件也可能外层鉴权。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0194-59-source：1716093428709421564-02.png | SQL subscribers CASE优先$1>0 id，否则$2非空uuid::$UUID，再$email；参数化代码本身不证SQLi/IDOR，SELECT*无可见owner条件也可能外层鉴权。 | [方法条目](../source-audit.md) |
| 保存图证0194-65-secret：1716199066852282670-02.jpg | PHP配置dbtype mysqli hostlocalhost user/password/db/dbprefix/secret多遮盖，来自web.zip题名无实际HTTP/zip成员路径。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-67-contract：1716323533524246560-02.jpg | TestContract owner构造msg.sender，withdrawFunds检查tx.origin==owner，低层to.call全余额后balance-=contractBalance（balance未声明）图错误标最后行为bug。 | [方法条目](../by-type/smart-contract.md) |
| 保存图证0194-74-xss：1716436296875258252-02.jpg | 浏览器redirecturl=javascript:confirm(document.cookie) activation失败页弹cookie确认框，图无sink代码/网络原始来源。 | [方法条目](../by-type/xss.md) |
| 保存图证0194-74-redirect：1716436296875258252-02.jpg | 浏览器redirecturl=javascript:confirm(document.cookie) activation失败页弹cookie确认框，图无sink代码/网络原始来源。 | [方法条目](../by-type/open-redirect.md) |
| 保存图证0194-76-records：1716437666009387299-02.png | sublert1.0 python-u paypal.com图Adding monitored domains并询问list，只有加候选未见diff/DNS/通知或来源。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0194-85-web：1716615536715657267-02.jpg | WordPresswp-login.php?wp_lang=en_US&o365=error有Office365+本地用户名密码。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0194-85-auth：1716615536715657267-02.jpg | WordPresswp-login.php?wp_lang=en_US&o365=error有Office365+本地用户名密码。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0194-90-report：1716769161341513814-02.jpg | H1 2215434从2134874关联284143 h1_TabNab.mp4视频folders邮箱，正文说注册已用而triage先Informative已修，侧边ResolvedLow100；邮箱不可盲注册验证/关联实名，不推固定奖励/公开秘密值。 | [方法条目](../reporting.md) |
| 保存图证0194-90-secret：1716769161341513814-02.jpg | H1 2215434从2134874关联284143 h1_TabNab.mp4视频folders邮箱，正文说注册已用而triage先Informative已修，侧边ResolvedLow100；邮箱不可盲注册验证/关联实名，不推固定奖励/公开秘密值。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-92-oauth：1716824364455280844-02.png | GitSourceEditor先newURL(a).origin白名单但再regexexec全URL捕host/project/file，合法android.googlesource origin中path/fragment嵌攻击host1337#.googlesource.com，regex组可导请求到其他host携access_token。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-92-redirect：1716824364455280844-02.png | GitSourceEditor先newURL(a).origin白名单但再regexexec全URL捕host/project/file，合法android.googlesource origin中path/fragment嵌攻击host1337#.googlesource.com，regex组可导请求到其他host携access_token。 | [方法条目](../by-type/open-redirect.md) |
| 保存图证0194-92-oauth：1716824364455280844-03.png | edit.chromium.org/edit file/repo URL操纵路径%2E/编码片段给PoC1337/1338；须已AndroidBuildTeamOAuth授权或用户grant，HTTPSPoC更新ChromiumGerritAboutme显示token权限，图无live结果。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-92-oauth：1716824364455280844-04.png | GitSourceEditor泄scope列email profile openid gerritcodereview androidbuild.internal，正文测试profile/repo读写而内网权仅assume/不清楚，其他editor只是may，pluginMode不OAuth尚未找到利用但enable-gis可强制候选。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-92-impact：1716824364455280844-04.png | GitSourceEditor泄scope列email profile openid gerritcodereview androidbuild.internal，正文测试profile/repo读写而内网权仅assume/不清楚，其他editor只是may，pluginMode不OAuth尚未找到利用但enable-gis可强制候选。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0194-94-report：1716832631814492542-02.jpg | H1 2215434独立截图库1844143视频folders邮箱复用公开附件审查机制，100Low不代替泄露字段实证，遮盖值保留无注册确认；不转录PII。 | [方法条目](../reporting.md) |
| 保存图证0194-94-secret：1716832631814492542-02.jpg | H1 2215434独立截图库1844143视频folders邮箱复用公开附件审查机制，100Low不代替泄露字段实证，遮盖值保留无注册确认；不转录PII。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-94-report：1716832631814492542-03.jpg | H1 2134874完整可见6:00-7:15公开视频两邮箱已遮盖，建议disclosure前隐藏所有敏感提交内容，单帧不覆盖视频全部。 | [方法条目](../reporting.md) |
| 保存图证0194-94-secret：1716832631814492542-03.jpg | H1 2134874完整可见6:00-7:15公开视频两邮箱已遮盖，建议disclosure前隐藏所有敏感提交内容，单帧不覆盖视频全部。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-96-scope：1716887397005132033-02.jpg | CosmWasm/cosmwasm SOURCE_CODE eligibletrue addedscope历史截图，只这个代码资产非Cosmos链/所有infra授权；执行前核最新项目规则/commit范围和奖励资格。 | [方法条目](../scope-and-rules.md) |
| 保存图证0194-98-secret：1716985243792474253-02.jpg | CitrixBleed4966 Nuclei3.0.1 template9.6.7十targets三匹配/logon/LogonPoint/Authentication/GetUserName Critical；图无原始请求/内存token/版本matcher。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-103-ssrf：1717179362762793068-02.jpg | Exness /api/partner_integrations/template/probe POST data.url自有候选，图DNS/HTTP GET Oastify Host/UserAgent pythonrequests2.28.1/sentrytrace；回调佐证后台取回，关联唯一标记/时间/主体，排除浏览器预览，DNSalone不HTTP。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0194-104-ai：1717194429080150331-02.jpg | Nebula示意model selection→input→vuln discoveryPoCautomation/search/resultprocessing/commandsuggestion/execution/resultstorage/CLI。 | [方法条目](../by-type/ai-application.md) |
| 保存图证0194-104-strategy：1717194429080150331-02.jpg | Nebula示意model selection→input→vuln discoveryPoCautomation/search/resultprocessing/commandsuggestion/execution/resultstorage/CLI。 | [方法条目](../hunting-strategy.md) |
| 保存图证0194-105-files：1717220663042494689-02.jpg | S3objectkey users/username/hash/profile/Screenshot时间png日期暴露命名元数据；图未含本地绝对路径/文件内容/EXIF。 | [方法条目](../by-type/file-upload.md) |
| 保存图证0194-105-secret：1717220663042494689-02.jpg | S3objectkey users/username/hash/profile/Screenshot时间png日期暴露命名元数据；图未含本地绝对路径/文件内容/EXIF。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-109-xss：1717254914815283385-02.jpg | TD 搜索报告截图给出 query 中的 <i> 与带 onmouseover 的 <a>，需要鼠标悬停才能触发该事件。 | [方法条目](../by-type/xss.md) |
| 保存图证0194-111-graphql：1717330395501584769-02.jpg | Copilot 报告截图描述从 JS 发现未公开 GraphQL 查询与 DestroyLlmConversation mutation，并用前端移除 hidden 类显示界面。 | [方法条目](../by-type/graphql.md) |
| 保存图证0194-111-access：1717330395501584769-02.jpg | Copilot 报告截图描述从 JS 发现未公开 GraphQL 查询与 DestroyLlmConversation mutation，并用前端移除 hidden 类显示界面。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0194-112-container：1717330577119179169-02.jpg | Kubernetes ingress-nginx 报告描述有 create Ingress 权限的用户控制 nginx.ingress.kubernetes.io/permanent-redirect annotation，经未转义模板写入 nginx 配置。 | [方法条目](../cloud/container-k8s-security.md) |
| 保存图证0194-113-auth：1717330783588024687-02.jpg | Lark 管理员日志报告截图描述组织内用户直接调用 AdminLog 下载入口绕过邮件 OTP。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0194-113-access：1717330783588024687-02.jpg | Lark 管理员日志报告截图描述组织内用户直接调用 AdminLog 下载入口绕过邮件 OTP。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0194-116-passive：1717463568872800531-02.jpg | 手工子域收集截图仅显示 wget 保存 Yahoo HTML，HTTPS 200 和文件大小是下载记录，不是子域覆盖率或漏洞。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0194-116-passive：1717463568872800531-03.png | HTML 中 grep 的正则 [a-z0-9]*.yahoo.com 使用未转义点且允许零字符，输出重复 www、区域及其他主机。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0194-116-passive：1717463568872800531-04.png | 截图把相同 grep 结果存入 sub_yahoo.txt，wc 为 531 行，不是 531 个唯一可用子域。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0194-117-secret：1717466235255030175-02.jpg | Flickr 报告截图在 Mozilla 公共仓库特定历史 commit 的 media/js/flickr.js#L4 定位 API key；附件未展示，也没有 key 权限或调用结果。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-119-container：1717496437100134442-02.jpg | Kubernetes 报告截图描述有 Ingress create/update 权限的用户经 spec.rules.http.paths.path 注入 nginx.conf，再配置 log_format/access_log 写文件，并 include 该文件绕过 path sanitizer。 | [方法条目](../cloud/container-k8s-security.md) |
| 保存图证0194-120-passive：1717597200035790987-02.jpg | 正文声称 JS 端点自动发现，配图实际是子域流水线：根 URL 与 GitHub key 输入，assetfinder/findomain/subfinder、GitHub 子域与 Shodan JSON 合并，经 sort-uniq、puredns 及分级 dsieve/bruteforce 得到候选。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0194-120-secret：1717597200035790987-02.jpg | 正文声称 JS 端点自动发现，配图实际是子域流水线：根 URL 与 GitHub key 输入，assetfinder/findomain/subfinder、GitHub 子域与 Shodan JSON 合并，经 sort-uniq、puredns 及分级 dsieve/bruteforce 得到候选。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-122-sql：1717727219454197817-02.jpg | 旧登录 ASP 截图中 URL 编码 WAITFOR DELAY 0:0:6 对应约 18 秒，图注如此描述；延迟并非请求中的 6 秒一一对应，可能多次执行或其他耗时。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0194-122-sql：1717727219454197817-03.png | 第二张旧登录截图把 WAITFOR DELAY 调为 0:0:4 并标注约 12 秒，与前图呈 3 倍关系，可作为重复执行或计时机制线索。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0194-122-sql：1717727219454197817-04.png | 截图显示 sqlmap fetching current user 和 hostname，返回值被遮蔽。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0194-122-report：1717727219454197817-04.png | 截图显示 sqlmap fetching current user 和 hostname，返回值被遮蔽。 | [方法条目](../reporting.md) |
| 保存图证0194-125-secret：1717843727266492773-02.jpg | Mozilla 翻译工具报告截图描述泄露的第三方 Smartling 凭据关联部分 Mozilla 项目，工具负责翻译 jobs、内部文档与内容改动。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-125-business：1717843727266492773-02.jpg | Mozilla 翻译工具报告截图描述泄露的第三方 Smartling 凭据关联部分 Mozilla 项目，工具负责翻译 jobs、内部文档与内容改动。 | [方法条目](../business-modeling.md) |
| 保存图证0194-127-logic：1717919242237219200-02.jpg | Urban Dictionary 报告截图保存 /v0/vote?def=...&direction=up&key=... 请求和 11 线程并行接受多次票的主张。 | [方法条目](../by-type/business-logic.md) |
| 保存图证0194-128-access：1717934324513923257-02.jpg | Airflow CVE-2023-40611 报告摘要描述 2.7.1 之前，已认证且 DAG-view 授权用户提交 notes 可修改部分 DagRun 字段，如配置参数和开始时间。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0194-129-access：1717934458744295640-02.jpg | Glassdoor 摘要明确限定已删除 employer profile 的部分 interview 记录仍经已弃用 RSS endpoint 可访问。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0194-129-records：1717934458744295640-02.jpg | Glassdoor 摘要明确限定已删除 employer profile 的部分 interview 记录仍经已弃用 RSS endpoint 可访问。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0194-130-oauth：1717949393985573318-02.jpg | 正常 Facebook 登录示意图是 relying party 请求 code，用户向 Facebook 取得供 Grammarly 使用的 code，再 POST facebook_login.code 给 auth.grammarly.com。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-130-oauth：1717949393985573318-03.jpg | Bukalapak 示意图声称给 YourTimePlanner 客户端签发的 Dan token 被另一应用接受并登录 Dan，体现跨 client/audience 的 token substitution。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-131-oauth：1717975703923429609-02.jpg | OAuth 示意图画出 Facebook 把 token 放在回跳 URL fragment，前端读取后由 Randomsite 请求 graph /me 获得 email。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-131-oauth：1717975703923429609-03.jpg | Vidio 正常登录示意把 token 明确标为给 Vidio client 92356，再由 provider 返回 Dan email。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-131-oauth：1717975703923429609-04.jpg | TimePlanner 所有者通过自己应用的正常用户授权取得供该应用使用的 token，图示 token 来源与跨应用误接受是不同边界。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-131-scope：1717975703923429609-04.jpg | TimePlanner 所有者通过自己应用的正常用户授权取得供该应用使用的 token，图示 token 来源与跨应用误接受是不同边界。 | [方法条目](../scope-and-rules.md) |
| 保存图证0194-131-oauth：1717975703923429609-05.jpg | 拼图显示 POST /api/facebook/auth 提交 fb_access_token，并截取 200 与 X-Auth-Tokens 返回，图注声称来自 TimePlanner 且登录为 Dan。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0194-131-report：1717975703923429609-05.jpg | 拼图显示 POST /api/facebook/auth 提交 fb_access_token，并截取 200 与 X-Auth-Tokens 返回，图注声称来自 TimePlanner 且登录为 Dan。 | [方法条目](../reporting.md) |
| 保存图证0194-132-secret：1717979531443933332-02.jpg | PostLeaks 终端截图从 Postman collection 提取 GET/POST、路径、query、header 与 bearer/token 模板，若干内容遮蔽；没有请求执行或有效性验证。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0194-132-passive：1717979531443933332-02.jpg | PostLeaks 终端截图从 Postman collection 提取 GET/POST、路径、query、header 与 bearer/token 模板，若干内容遮蔽；没有请求执行或有效性验证。 | [方法条目](../discovery/passive-and-services.md) |

| 0195：NoSuchBucket 与资源接管之间的验证边界 | 正文的子域→爬取→aws-s3标签→NoSuchBucket匹配只产生候选；subfinder 的域名输入与 http:// URL 混用也需先检查工具参数。 | [方法条目](../by-type/subdomain-takeover.md) |
| 0195：逐参数扩展扫描仍需 source 与 sink 对照 | XnlReveal 宣传单参数自动找 XSS；保留原始正常请求和参数来源，每次只改变一个可控输入，观察反射上下文、真实 sink、事件条件及无害执行标记。 | [方法条目](../by-type/xss.md) |
| 0195：Frida 与系统证书配置是测试环境前提 | Pen-Andro 宣传安装应用、frida server 与移动 Burp 证书。 | [方法条目](../by-type/mobile-android.md) |
| 0195：客户端模板表达式依赖引擎和求值上下文 | CSTI 候选包含双大括号、constructor.prototype、charAt 改写与 $eval，是特定客户端模板表达式而非通用服务端模板输入。 | [方法条目](../by-type/ssti.md) |
| 0195：凭据格式分类应避免向第三方暴露秘密 | API Guesser 以 key/token 输入判断供应商，保存图空输入框，没有实现或本地处理证明。 | [方法条目](../by-type/info-secrets.md) |
| 0195：盲回调到支持面板影响需要连续证据 | 正文自称 blind XSS 后可读所有邮件，图只有 Critical 报告摘要。 | [方法条目](../by-type/xss.md) |
| 0195：断链检查与可控制目的资源不是同一结论 | socialhunter 与 broken-link 自动检查产生链接候选；核实际引用页面、目的资源类型、当前可用性、服务所有权与 provider 绑定规则。 | [方法条目](../by-type/subdomain-takeover.md) |
| 0195：缩小学习范围以验证机制 | 正文建议初学者选单应用、单类机制、有效报告并配合 CTF/研究。 | [方法条目](../hunting-strategy.md) |
| 0195：修改 422 为 200 后空面板与回登录的反例 | 正文实际描述改响应后短暂进入空面板，两秒后回登录；这支持客户端显示被误导，不能独立证明后端认证突破。 | [方法条目](../by-type/authn-session.md) |
| 0195：相同路径的不同方法应按授权决定比较 | 正文问三种 method 是否因同 endpoint 被合并，图片只展示 DELETE 对 integration ID、POST 创建带 schedule 的对象，无真实状态。 | [方法条目](../reporting.md) |
| 0195：AEM 指纹和 Groovy 执行入口的前提分离 | 保存串帖只有子域/AEM 模板识别与 /bin/groovyconsole/post.servlet 候选，中间续篇未保存。 | [方法条目](../source-audit.md) |
| 0195：CVE 版本、搜索指纹与实际部署不能互相替代 | 正文给 Confluence 8.0.0–8.5.1、Grafana 8.0.0-beta1–8.3.0 与 Citrix Gateway 名称及 Shodan/Nuclei 链，这些仅是保存时的版本/检索主张，未取公告全文。 | [方法条目](../discovery/passive-and-services.md) |
| 0195：跨应用 token reuse 需证明 issuer 与受众 | 正常 code 图、TimePlanner token 流程、Grammarly 登录响应/页面是不同证据层。 | [方法条目](../by-type/oauth-oidc.md) |
| 0195：AI 生成模板的可用性由隔离正负样例证明 | 保存公告与空编辑器提供 AI 生成入口，无模板或输出。 | [方法条目](../by-type/ai-application.md) |
| 0195：responsible disclosure 线索仍需明确范围 | 正文建议用 dork 找小项目与 Open Bug Bounty，只有节选。 | [方法条目](../scope-and-rules.md) |
| 0195：旧 login.js 注释中的密码主张要绑定版本 | 正文链是历史 URL→login.js→格式化→注释中 admin password，但无代码片段或验证。 | [方法条目](../by-type/info-secrets.md) |
| 0195：id/../id2 的归一化与实际对象权限 | 正文说 ID 中加路径跳转还不足以成立，配图奖励信仅称已知 userUUID/recipientID 的 GraphQL 读改权限。 | [方法条目](../by-type/idor-access-control.md) |
| 0195：模板循环输出与引擎语义、影响分开 | 正文 for/双大括号循环 [1,2,3] 并输出 tuple，作者仍难证明影响；没有响应。 | [方法条目](../by-type/ssti.md) |
| 0195：BCC 邮件的隐私判断依赖收件人可见原始头 | 正文称正常注册邮件 BCC 含五百邮箱，但无原始邮件。 | [方法条目](../by-type/info-secrets.md) |
| 0195：注销后浏览器返回的缓存与活会话分离 | 正文注销后 Back 回 profile，图片只有 Cacheable Sensitive Response 题名。 | [方法条目](../by-type/authn-session.md) |
| 0195：默认凭据登录主张需实际管理权限对照 | 正文给示例默认 admin 账号/口令，图只 High 分类。 | [方法条目](../by-type/authn-session.md) |
| 0195：全页截图工具的观察范围应有页面状态 | Hxn 宣传终端全页截图，配图空终端。 | [方法条目](../discovery/records-and-incremental.md) |
| 0195：htmlspecialchars 的保护取决于输出上下文 | 正文说代码审查绕 htmlspecialchars 找反射 XSS，没有代码。 | [方法条目](../by-type/xss.md) |
| 0195：收购、ASN 与反查形成有来源的候选图 | 正文列 acquisition→ASN→reverse whois→Shodan→subdomain→ports/fuzz/GitHub。 | [方法条目](../discovery/passive-and-services.md) |
| 0195：删除主机标签会产生另一个资产候选 | 正文把 x.y.domain.com 改为 x.domain.com 后 fuzz 并称 AWS key，配图仅报告元数据。 | [方法条目](../discovery/passive-and-services.md) |
| 0195：五类表单 dork 不是表单或盲 XSS 的完整覆盖 | 正文/图 DorkKing 按 domain 生成 intext/intitle/inurl、注册与联系五类候选。 | [方法条目](../discovery/passive-and-services.md) |
| 0195：范围新增、移除与奖励资格按时点记录 | Priceline 图 flyiin.com added/eligible true；Mondelez 两帖同正文图分别 philadelphia.be 与 nabiscoholiday.com 新增、另有 training-indonesia.cocoalife.org 和 cadbury.co.uk 移除，eligible 均 false。 | [方法条目](../scope-and-rules.md) |
| 保存图证0195-1-desktop：1718024921258103230-02.jpg | Rockstar 摘要明确登录后短时间内应用内存明文含邮箱和密码，攻击者需要设备 user-level access 并在登录后 dump 该进程。 | [方法条目](../by-type/desktop-client.md) |
| 保存图证0195-1-secret：1718024921258103230-02.jpg | Rockstar 摘要明确登录后短时间内应用内存明文含邮箱和密码，攻击者需要设备 user-level access 并在登录后 dump 该进程。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-2-host：1718273916282753397-02.jpg | CitrixBleed 文章截图指出 JSON hostname 实际来自 HTTP Host 而非管理员配置，重复插入六次可超出0x20000字节；保存请求为OIDC discovery，响应长度147441并见非打印/相邻HTTP材料。 | [方法条目](../by-type/host-header.md) |
| 保存图证0195-2-secret：1718273916282753397-02.jpg | CitrixBleed 文章截图指出 JSON hostname 实际来自 HTTP Host 而非管理员配置，重复插入六次可超出0x20000字节；保存请求为OIDC discovery，响应长度147441并见非打印/相邻HTTP材料。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-2-source：1718273916282753397-03.jpg | Citrix 截图指出两函数 ns_aaa_oauth_send_openid_config 和 ns_aaa_oauthrp_send_openid_config 对应 idp/rp OIDC discovery，原代码 snprintf(...,0x20000,...) 返回iVar3直接交ns_vpn_send_response作长度；代码横向裁切且未展示patch代码全文。 | [方法条目](../source-audit.md) |
| 保存图证0195-2-secret：1718273916282753397-03.jpg | Citrix 截图指出两函数 ns_aaa_oauth_send_openid_config 和 ns_aaa_oauthrp_send_openid_config 对应 idp/rp OIDC discovery，原代码 snprintf(...,0x20000,...) 返回iVar3直接交ns_vpn_send_response作长度；代码横向裁切且未展示patch代码全文。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-2-source：1718273916282753397-04.png | 解释图明确 snprintf 返回若空间足够应写的长度而非实际写入字节，patched仅返回值小于0x20000才发送。 | [方法条目](../source-audit.md) |
| 保存图证0195-2-secret：1718273916282753397-04.png | 解释图明确 snprintf 返回若空间足够应写的长度而非实际写入字节，patched仅返回值小于0x20000才发送。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-3-crlf：1718296707270951405-02.jpg | Mozilla oauth/authorize报告截图给redirect_uri的%0d%0a候选，并声称无需授权可改headers，截图响应HTTP/2 302、location部分在下方裁切，未展示新header完整行。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图证0195-3-oauth：1718296707270951405-02.jpg | Mozilla oauth/authorize报告截图给redirect_uri的%0d%0a候选，并声称无需授权可改headers，截图响应HTTP/2 302、location部分在下方裁切，未展示新header完整行。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0195-7-auth：1718598699742646660-02.jpg | H1报告描述账号报告提交被ban、普通直接请求403，但API key入口仍能提交；图片提及自建sandbox program和key，未展示API请求/最终报告。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0195-7-access：1718598699742646660-02.jpg | H1报告描述账号报告提交被ban、普通直接请求403，但API key入口仍能提交；图片提及自建sandbox program和key，未展示API请求/最终报告。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-8-takeover：1718609090476204133-02.jpg | Azure CNAME 示意为资源正常、撤销后danglingDNS、另一主体占用后内容控制。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0195-8-takeover：1718609090476204133-03.png | 四行GitHubPages示意称blog.github.io失效且注册即可控制blog.example.com；服务名不是普通可随意注册的域名，需provider账户命名与自定义域验证/保留规则。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0195-14-access：1718682058070110389-02.jpg | 认证bypass清单删除原数字ID后/api//users与反斜线、.json、尾斜线、v2、路径&及X-Original-URL候选。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-14-web：1718682058070110389-02.jpg | 认证bypass清单删除原数字ID后/api//users与反斜线、.json、尾斜线、v2、路径&及X-Original-URL候选。 | [方法条目](../discovery/web-and-api.md) |
| 保存图证0195-15-takeover：1718699839306018952-02.jpg | 一行工具图串联 subfinder/assetfinder/amass 追加FILE与subjack指纹，依赖列haccer/subjack但fingerprint路径cybertix；没有去重、版本或结果。 | [方法条目](../by-type/subdomain-takeover.md) |
| 保存图证0195-15-passive：1718699839306018952-02.jpg | 一行工具图串联 subfinder/assetfinder/amass 追加FILE与subjack指纹，依赖列haccer/subjack但fingerprint路径cybertix；没有去重、版本或结果。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-19-lfi：1718749692115423263-02.jpg | phpBB图片说明已认证acp_icons.php导入emoji的pak拼入file读取数组，代码有check_form_key与file()；文述不能读/etc/passwd而/proc/self/fd/1是阻塞候选，后续被裁切。 | [方法条目](../by-type/lfi-path-traversal.md) |
| 保存图证0195-19-experiment：1718749692115423263-02.jpg | phpBB图片说明已认证acp_icons.php导入emoji的pak拼入file读取数组，代码有check_form_key与file()；文述不能读/etc/passwd而/proc/self/fd/1是阻塞候选，后续被裁切。 | [方法条目](../experiment-design.md) |
| 保存图证0195-23-passive：1718845105375781149-02.jpg | SSH代理示意LocalDocker/portforward↔remoteSSH(无admin)↔internalnetwork。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-23-scope：1718845105375781149-02.jpg | SSH代理示意LocalDocker/portforward↔remoteSSH(无admin)↔internalnetwork。 | [方法条目](../scope-and-rules.md) |
| 保存图证0195-29-oauth：1718935705873686869-02.png | Auth0截图是scope字符串，含client_grants/users/keys/connections/rules/roles/actions/tenant_settings等读写。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0195-29-secret：1718935705873686869-02.png | Auth0截图是scope字符串，含client_grants/users/keys/connections/rules/roles/actions/tenant_settings等读写。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-30-secret：1718995052515434743-02.jpg | API Guesser空输入UI提供key/token分类，未展示识别逻辑或本地处理保证。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-34-xss：1719051684373213372-02.jpg | 8x8报告摘要称已提交付款数据可修改，POST /api/patchPaymentMethod/ID JSON ipAddress含SVG onload，回显端点与32字符随机receipt hash。 | [方法条目](../by-type/xss.md) |
| 保存图证0195-34-access：1719051684373213372-02.jpg | 8x8报告摘要称已提交付款数据可修改，POST /api/patchPaymentMethod/ID JSON ipAddress含SVG onload，回显端点与32字符随机receipt hash。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-44-passive：1719249945453285491-02.jpg | dork列表indexof结合config/sql/admin/backup/db.frm/common.crt/ca.crt/proxy.pac/owncloud等，没有site边界或搜索结果。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-44-secret：1719249945453285491-02.jpg | dork列表indexof结合config/sql/admin/backup/db.frm/common.crt/ca.crt/proxy.pac/owncloud等，没有site边界或搜索结果。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-46-experiment：1719293275713200389-02.jpg | Informative报告2230842自述Burp编辑responseheaders可让人误以HTTPS变HTTP，同时明确仍HTTPS；VPN添加匿名未改变证据。 | [方法条目](../experiment-design.md) |
| 保存图证0195-46-report：1719293275713200389-02.jpg | Informative报告2230842自述Burp编辑responseheaders可让人误以HTTPS变HTTP，同时明确仍HTTPS；VPN添加匿名未改变证据。 | [方法条目](../reporting.md) |
| 保存图证0195-56-passive：1719379806520045673-02.jpg | 第二版相同内容dork清单字形不同但独立hash；indexof config/session/backup等仍只是无site的候选，OR项可能逃出限制。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-56-secret：1719379806520045673-02.jpg | 第二版相同内容dork清单字形不同但独立hash；indexof config/session/backup等仍只是无site的候选，OR项可能逃出限制。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-56-passive：1889681567993168075-02.jpg | 同正文第二post的第三版indexof dork图有独立像素hash，当前文件1889681567993168075-02.jpg需绑定本post；内容为无site的config/session/backup证书等候选清单，没有命中或秘密。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-56-secret：1889681567993168075-02.jpg | 同正文第二post的第三版indexof dork图有独立像素hash，当前文件1889681567993168075-02.jpg需绑定本post；内容为无site的config/session/backup证书等候选清单，没有命中或秘密。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-57-strategy：1719410092821426199-02.jpg | 中英阿学习图按Linux/Windows命令、网络/Web/IT、pentest、OWASP、bugbounty基础到公开writeup/进阶课程。 | [方法条目](../hunting-strategy.md) |
| 保存图证0195-57-strategy：1719410092821426199-04.jpg | 图建议按SQLi等机制查公开report、在HTB/THM与localtest练习并学写报告/英文。 | [方法条目](../hunting-strategy.md) |
| 保存图证0195-57-report：1719410092821426199-04.jpg | 图建议按SQLi等机制查公开report、在HTB/THM与localtest练习并学写报告/英文。 | [方法条目](../reporting.md) |
| 保存图证0195-59-crlf：1719512216393924819-02.jpg | TikTok摘要描述Pangle file_name参数CRLF与未HTMLescape导致反射JS，只有厂商摘要没有原始头/body/PoC。 | [方法条目](../by-type/crlf-response-splitting.md) |
| 保存图证0195-59-xss：1719512216393924819-02.jpg | TikTok摘要描述Pangle file_name参数CRLF与未HTMLescape导致反射JS，只有厂商摘要没有原始头/body/PoC。 | [方法条目](../by-type/xss.md) |
| 保存图证0195-60-secret：1719527326168605100-02.jpg | FetLife报告Informative图示位置搜索前端直调Mapbox geocoding带access_token，curl片段在下方裁切，无tokenscope/滥用结果。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-61-xss：1719539685209313640-02.jpg | Collaborator列表DNS/HTTP与GET /deployment/env/...config.js?_=... UserAgentFirefox、SecFetchModecors/sameorigin，host部分遮盖。 | [方法条目](../by-type/xss.md) |
| 保存图证0195-61-ssrf：1719539685209313640-02.jpg | Collaborator列表DNS/HTTP与GET /deployment/env/...config.js?_=... UserAgentFirefox、SecFetchModecors/sameorigin，host部分遮盖。 | [方法条目](../by-type/ssrf.md) |
| 保存图证0195-63-access：1719582435518841288-02.jpg | 截图DELETE /ic/integration-server/ic-task-hive/askme JSON integrations:[283]、Authorization占位，注释称跨组织删任意integration但无响应。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-63-report：1719582435518841288-02.jpg | 截图DELETE /ic/integration-server/ic-task-hive/askme JSON integrations:[283]、Authorization占位，注释称跨组织删任意integration但无响应。 | [方法条目](../reporting.md) |
| 保存图证0195-63-access：1719582435518841288-03.jpg | 同路径POST含name/settings.startingUrl、schedule、systems等，图注说创建提权无角色/状态证据。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-63-business：1719582435518841288-03.jpg | 同路径POST含name/settings.startingUrl、schedule、systems等，图注说创建提权无角色/状态证据。 | [方法条目](../business-modeling.md) |
| 保存图证0195-70-oauth：1719723468999057679-02.jpg | TimePlanner所有者取得为其client签发的正常授权token示意，独立hash不同排版；合法本app授权不代表他人或其他client登录授权。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0195-70-scope：1719723468999057679-02.jpg | TimePlanner所有者取得为其client签发的正常授权token示意，独立hash不同排版；合法本app授权不代表他人或其他client登录授权。 | [方法条目](../scope-and-rules.md) |
| 保存图证0195-70-oauth：1719723468999057679-04.jpg | Grammarly拼图POST /api/login facebook_login.access_token，响应grauth/csrf-token cookie与user字段，图注明TimePlannertoken，敏感值不转录。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0195-70-report：1719723468999057679-04.jpg | Grammarly拼图POST /api/login facebook_login.access_token，响应grauth/csrf-token cookie与user字段，图注明TimePlannertoken，敏感值不转录。 | [方法条目](../reporting.md) |
| 保存图证0195-70-oauth：1719723468999057679-05.jpg | Grammarly登录UI显示邮箱与Secretdocument卡片，图注connectedDan；它是登录后页面片段，无文档正文/编辑结果或token受众。 | [方法条目](../by-type/oauth-oidc.md) |
| 保存图证0195-70-impact：1719723468999057679-05.jpg | Grammarly登录UI显示邮箱与Secretdocument卡片，图注connectedDan；它是登录后页面片段，无文档正文/编辑结果或token受众。 | [方法条目](../impact-and-acceptance.md) |
| 保存图证0195-72-scope：1719736122538930219-02.jpg | Priceline历史scope图写flyiin.com URL eligibletrue added。 | [方法条目](../scope-and-rules.md) |
| 保存图证0195-84-sql：1720107265770803673-02.jpg | SQLMap图称GET id booleanWHERE/HAVING与OracleDBMS_PIPE.RECEIVE_MESSAGE时间型，355requests，并列UNION初猜/不可NULL警告与schema枚举。 | [方法条目](../by-type/sql-injection.md) |
| 保存图证0195-84-report：1720107265770803673-02.jpg | SQLMap图称GET id booleanWHERE/HAVING与OracleDBMS_PIPE.RECEIVE_MESSAGE时间型，355requests，并列UNION初猜/不可NULL警告与schema枚举。 | [方法条目](../reporting.md) |
| 保存图证0195-89-ai：1720149202473460095-02.jpg | NucleiAI模板UI空编辑器与Scan/Share/StartwithAI，没有生成模板/scan输出。 | [方法条目](../by-type/ai-application.md) |
| 保存图证0195-89-source：1720149202473460095-02.jpg | NucleiAI模板UI空编辑器与Scan/Share/StartwithAI，没有生成模板/scan输出。 | [方法条目](../source-audit.md) |
| 保存图证0195-91-secret：1720152615424770257-02.jpg | WPconfig命令图将subfinder→多端口httpx路径/wp-config.PHP筛200，并混入损坏-status-codeithub...fingerprints参数、输出takeover。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-91-passive：1720152615424770257-02.jpg | WPconfig命令图将subfinder→多端口httpx路径/wp-config.PHP筛200，并混入损坏-status-codeithub...fingerprints参数、输出takeover。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-94-access：1720177877360967736-02.jpg | 奖励信描述已知userUUID与recipientID时GraphQL路径授权可读/改recipient数据，没有query/variables/response。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-94-graphql：1720177877360967736-02.jpg | 奖励信描述已知userUUID与recipientID时GraphQL路径授权可读/改recipient数据，没有query/variables/response。 | [方法条目](../by-type/graphql.md) |
| 保存图证0195-102-auth：1720369940191178979-02.jpg | Java doFilter截图在authenticateUser false且无SAMLResponse时检查isStarshipRequest，若无USER_IN_SESSION创建ProductAccess loginName admin，rest/user/session/roles值来自X-Starship-* headers，roles equalsadmin设Admin并调用validateAllowedOperations后写session。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0195-102-saml：1720369940191178979-02.jpg | Java doFilter截图在authenticateUser false且无SAMLResponse时检查isStarshipRequest，若无USER_IN_SESSION创建ProductAccess loginName admin，rest/user/session/roles值来自X-Starship-* headers，roles equalsadmin设Admin并调用validateAllowedOperations后写session。 | [方法条目](../by-type/saml-sso.md) |
| 保存图证0195-102-source：1720369940191178979-02.jpg | Java doFilter截图在authenticateUser false且无SAMLResponse时检查isStarshipRequest，若无USER_IN_SESSION创建ProductAccess loginName admin，rest/user/session/roles值来自X-Starship-* headers，roles equalsadmin设Admin并调用validateAllowedOperations后写session。 | [方法条目](../source-audit.md) |
| 保存图证0195-114-secret：1720727807939232067-02.jpg | H1截图说明监控JS出现GoogleForms链接，定位assets/static/js/5930...chunk.js并给/edit#responses形式，声称能改表单看邮箱/回答。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-114-access：1720727807939232067-02.jpg | H1截图说明监控JS出现GoogleForms链接，定位assets/static/js/5930...chunk.js并给/edit#responses形式，声称能改表单看邮箱/回答。 | [方法条目](../by-type/idor-access-control.md) |
| 保存图证0195-114-records：1720727807939232067-02.jpg | H1截图说明监控JS出现GoogleForms链接，定位assets/static/js/5930...chunk.js并给/edit#responses形式，声称能改表单看邮箱/回答。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0195-118-secret：1720876200082452707-02.jpg | PHPMailer源码配置Host/Username/Password等被遮，SMTPAuthtrue/SMTPSecuretls/Port587/SMTPDebug3，没repo地址/commit/发送结果。 | [方法条目](../by-type/info-secrets.md) |
| 保存图证0195-118-source：1720876200082452707-02.jpg | PHPMailer源码配置Host/Username/Password等被遮，SMTPAuthtrue/SMTPSecuretls/Port587/SMTPDebug3，没repo地址/commit/发送结果。 | [方法条目](../source-audit.md) |
| 保存图证0195-125-passive：1721051036964569298-02.jpg | DorkKing UI按目标生成FormFinder intext/intitle/inurl、RegisterSignup、Contactus五类，只有按钮未显示查询/结果。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-125-xss：1721051036964569298-02.jpg | DorkKing UI按目标生成FormFinder intext/intitle/inurl、RegisterSignup、Contactus五类，只有按钮未显示查询/结果。 | [方法条目](../by-type/xss.md) |
| 保存图证0195-126-csrf：1721105288043102716-02.jpg | ownCloud10.12.2报告图在admin会话下POST/settings/users/users，form-urlencoded创建groups[]=admin用户，缺requesttoken且伪Origin http://abc:8080。 | [方法条目](../by-type/csrf.md) |
| 保存图证0195-126-auth：1721105288043102716-02.jpg | ownCloud10.12.2报告图在admin会话下POST/settings/users/users，form-urlencoded创建groups[]=admin用户，缺requesttoken且伪Origin http://abc:8080。 | [方法条目](../by-type/authn-session.md) |
| 保存图证0195-129-passive：1721141074087780547-02.jpg | 第二DorkKing图分辨率不同独立hash，同五个表单候选按钮，未显示完整dork或搜索返回；按当前post绑定像素与来源，保持site边界/索引时间/实际表单及后台sink分离，不以按钮数量证明覆盖。 | [方法条目](../discovery/passive-and-services.md) |
| 保存图证0195-129-xss：1721141074087780547-02.jpg | 第二DorkKing图分辨率不同独立hash，同五个表单候选按钮，未显示完整dork或搜索返回；按当前post绑定像素与来源，保持site边界/索引时间/实际表单及后台sink分离，不以按钮数量证明覆盖。 | [方法条目](../by-type/xss.md) |
| 保存图证0195-130-scope：1721155593115672991-02.jpg | Mondelez历史图philadelphia.be addedeligiblefalse、training-indonesia.cocoalife.org removedfalse。 | [方法条目](../scope-and-rules.md) |
| 保存图证0195-130-records：1721155593115672991-02.jpg | Mondelez历史图philadelphia.be addedeligiblefalse、training-indonesia.cocoalife.org removedfalse。 | [方法条目](../discovery/records-and-incremental.md) |
| 保存图证0195-130-scope：1725071397951541319-02.jpg | 同一正文另一时点图nabiscoholiday.com addedfalse、cadbury.co.uk removedfalse；重复正文不代表资产变化一致，必须将每张图绑定具体post/time，再核当前范围，不因eligiblefalse推scope外也不因品牌关联自动授权。 | [方法条目](../scope-and-rules.md) |
| 保存图证0195-130-records：1725071397951541319-02.jpg | 同一正文另一时点图nabiscoholiday.com addedfalse、cadbury.co.uk removedfalse；重复正文不代表资产变化一致，必须将每张图绑定具体post/time，再核当前范围，不因eligiblefalse推scope外也不因品牌关联自动授权。 | [方法条目](../discovery/records-and-incremental.md) |

## 首轮提炼范围与未采纳内容

首轮快照曾盘点并进行机器解析/筛选：52,716 篇帖子、81,961 个媒体文件，以及采集清单、诊断页和系统元数据。正文有 51,463 个不同内容哈希，媒体有 29,700 个不同内容哈希；去重用于减少重复阅读，不把转载当独立验证。

本次 31 组知识来自 72 篇代表性正文的语义复核及 2 张技术截图的视觉复核；63 篇采纳机制，9 篇纠正推断或操作建议。全量 OCR 是筛选材料，23,994 张提取到文字、5,703 张未检测到文字、3 张解码失败；它不表示已逐图理解，也不补全外链、完整线程或平台时间线。不能据此声称所有帖子和图片均已语义读完、历史漏洞已复现或当前检出率已提高。

重复技巧合并到既有专题；宣传、奖金/点赞、工具清单、只有标题或图片但缺过程的内容不单独生成操作规则。采集清单和诊断页只贡献恢复、覆盖和来源缺口方面的经验，系统元数据不作为安全知识。错误算术、客户端响应篡改等于 MFA 绕过、XHR 通用绕预检、批量 PIN 穷举和高线程余额实验等未按原建议采纳。

上述72篇首轮来源、指纹、读取范围和分类对应关系保存在 [提炼来源](community-distillation-sources.json)，后续全量复核以 [覆盖状态](../../evals/post-distillation/status.json) 和其同目录审计记录为准，包含媒体缺失及内嵌图片检查；这些文件仅用于追溯；知识使用不依赖访问这些外部原帖。未运行源帖 PoC、未知工具或历史目标测试。
