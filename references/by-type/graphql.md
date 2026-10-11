# GraphQL

适用信号：query/mutation/subscription、schema 或 GraphQL 正常流量

## 检查与最小实验

优先读取已有客户端操作与可用 schema，按 Query/Mutation、对象、字段和 resolver 建图。schema discovery 与权限测试分开；关闭 introspection 后仍可能从正常操作得到接口信息。

用两个自建对象检查直接 node 查询、嵌套关系和 mutation 返回字段是否一致授权；顶层接口通过认证不表示每个 resolver 已授权。HTTP 200 仍需检查 `errors`、部分 `data` 和具体字段。

别名或批量会让单个 HTTP 请求包含多次逻辑操作：同时计请求数和 resolver/业务动作数。只在明确预算内用最小样本检查逐操作控制，不进行深度/宽度耗尽或密码猜测。

## 证据与反例

introspection、字段建议、GraphiQL 可见只说明可发现性；公共 schema 不直接泄密。确认需要受限制数据或状态实际暴露/改变。客户端缓存和旧变量必须排除。

## Agent 行为

保存 operationName、查询指纹、变量归属与字段路径；只加载当前 resolver 相关 schema，避免整份模型充斥上下文。

同一注册、邮箱验证或账户恢复流程若同时存在 REST 与 mutation，比较服务端对相同受控身份的前置状态检查。直接调用 mutation 返回成功仍须核对实际账号、验证状态和后续受保护能力；不能只因绕过了 UI 步骤就确认认证缺陷。字段扩展仅使用自有对象，单包批处理不产生额外 OTP 猜测许可。

## 调研来源

- [PS-graphql · GraphQL API vulnerabilities](https://portswigger.net/web-security/graphql)
- [OWASP-api3 · API3:2023 Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

`__schema` 属于 GraphQL introspection 系统，不能称为“替代 introspection 的查询”。按当前目的选择有效字段集合，记录实际返回类型/字段、错误、截断和身份；查询 schema 不证明已读取所有类型/私密业务数据，也不自动构成权限缺陷。见 [GraphQL 官方 introspection 说明](https://graphql.org/learn/introspection/)（2026-10-09 核对）；禁用状态与真实 resolver 授权仍分别检查，不为获取整份模型扩大查询成本。

## 操作类型与实际副作用

query用于读取、mutation用于状态改变是协议设计，不能替代对目标resolver实际行为的核对。[GraphQL官方mutation说明](https://graphql.org/learn/mutations/)要求顶层mutation字段之外的解析无副作用且幂等，但实现仍可能违规（2026-10-09核对）。恢复正常测试请求时，将操作类型、各字段/参数、真实身份和权威状态关联；mutation返回字段也要授权。不要因query名字或schema可视化工具就授予纯读取预算，更不自动执行插件生成的全部操作；副作用未知先读获准源码/业务契约。

## POST改GET与只读查询的证据边界

操作类型、传输方法、token检查、自动认证、字段授权和真实状态分别记录。旧图把getUser查询由POST改成GET并去掉头，但没有响应、Cookie或前后状态；不能由name/email字段查询直接认定状态改变型CSRF，也不证明敏感响应可被外站读取。

先恢复目标真实合法query及变量定义，再确认当前处理器是否接受该方法和实际消费者。若真实resolver改变状态，按CSRF条件核对；若只是私密读取，检查对象/字段受众与浏览器响应读取边界，不能把同一个截图同时当成这些结论均已成立。

## OTP字段省略的输入强制转换与认证分支

GraphQL登录去掉错误OTP后“登录成功”的声明，需要区分字段/参数省略、显式null、空字符串、变量缺失与默认值。已有schema/输入校验/实际resolver路径应关联挑战主体、验证码验证分支和会话签发；可选输入被接受不等于通过认证。[GraphQL输入对象强制转换规范](https://spec.graphql.org/September2025/#sec-Input-Objects.Input-Coercion)说明缺失值、默认值、必需字段及null的不同处理（2026-10-09核读相关段落），不要假定所有省略都会抵达同一分支。

在获准隔离合成身份或离线日志中，固定未认证基线、挑战代际及原始操作/变量，对照正常、错误和缺字段后的服务端真实身份及受保护能力。排除先前已认证Cookie、前端成功文案或其他合法密码less凭据；源文未给schema/签发证据，保留为具体候选，不请求真人OTP或把全部GraphQL视为同一认证弱点。

## GraphQL错误分层与私密内容受众

畸形/意外输入的错误可能来自文档语法、schema/变量校验、resolver或下游异常，各自消费与受众不同。关联原始operation/变量、实际拒绝层、当前身份、正常基线、错误的path/扩展字段及是否出现业务私密数据/秘密；公开字段建议或一般类型名不自动等于敏感信息泄漏。

用获准已有错误/源码及普通合成类型差异核对被返回内容，不为触发报错扩大复杂度或改变业务状态。相同HTTP状态可承载不同GraphQL错误，错误消息与真正越权读取分开；来源仅首条首段，未读全系列/外线程，不自动枚举全部schema或数据库异常。

## 内省类型种类与查询字段的匹配

GraphQL手写笔记里的Schema/Type/TypeKind/Field/InputValue/EnumValue/Directive是模型线索，不是完整查询；名称需按实际内省元字段和类型处理。[GraphQL September2025 §4.2.2](https://spec.graphql.org/September2025/#sec-The-__Type-Type)规定__Type.kind与可用字段的对应：对象字段、输入对象inputFields、枚举enumValues、联合/接口possibleTypes及LIST/NON_NULL的ofType（2026-10-09核读相关段）。联合成员是对象类型，不能把Union当任意参数列表。

只沿当前需要的获准字段恢复有效选择与类型包装，记录不适用的null、错误、截断、deprecated筛选和已知操作；不据笔记称已取得完整schema。introspection开关、深度/复杂度限制与resolver授权分别依部署证据，不能概括成所有实现的同一默认。没有返回字段/受众证据不认泄露；不执行完整dump、深层查询或耗尽型操作。

## GraphQL搜索输入到NoSQL操作符的边界

旧GraphQLmap图的doctors search参数内含lastName/$regex并返回Admin记录，随后显示nosqli及未输入的Query提示。GraphQL解析通过、JSON样式字符串被后端解释、NoSQL查询操作符生效及权限突破是不同步骤；返回Admin可以是正常搜索结果，工具命令名不证明注入成功或管理员登录。

核对schema输入类型、resolver解析/字段白名单、数据库驱动实际查询、角色/租户过滤与合成结果集，用普通等值搜索/被拒操作符作有限隔离对照。来源没有完整nosqli操作、密码或终态，不补所有GraphQL都支持该格式，不运行工具、枚举真实医生资料或访问图中挑战站点。

## 表单中间件、GET副作用与XS-Search

旧帖指GraphQL中间件可能接受表单POST、GET mutation和XS-Search。[Doyensec原始研究](https://blog.doyensec.com/2021/05/20/graphql-csrf.html)展示格式转换、query内误放状态改变、csrf_exempt及时序旁路；其2021小样本比例不代表当前全部实现（2026-10-10核读技术正文）。

分开浏览器可发送的格式、凭据实际携带、Origin/CSRF/SameSite、resolver效果和响应读取能力：能够提交读取query不自动是状态改变CSRF，也不代表外站可直接读数据。XS-Search需独立可观察通道/正常对照；时延不能未经样本/缓存/噪声控制就判断私人记录存在。优先获准同版源码/隔离合成操作，不改真人邮箱、上传文件、诱导受害者或枚举私密用户。


## 关闭内省后的候选schema与模型完整性

clairvoyance旧宣传称内省关闭仍可输出供Voyager/InQL使用的JSON。将正常操作、客户端字段、校验错误/建议和工具推断分别标明来源；内省配置、候选字段可发现性和resolver权限是三个问题。JSON格式能被工具接受不证明所有字段/参数/输入类型都恢复，也不说明与当前部署一致。

从已有获准操作及错误构建与当前消费者相关的小模型，记录版本/身份/时点、已见字段和未知部分，再与真实schema契约核对；字段名猜测不当完整模型，公开接口描述不自动泄密。不执行工具枚举、生成全部操作或继承工具的complete宣称，完整仓库与外部工具教程未读。来源：[保存帖](https://x.com/i/status/1397613730016505863)。


## 批处理中的挑战身份与验证次数

旧帖将单包多邮箱/密码及全部2FA值直接称限流绕过。传输层数组batch、单个operation的多个别名和实际验证调用不同，是否支持需目标处理器证据。一个HTTP请求可触发多次业务尝试，但不保证所有实现接收、共用挑战或只扣一次计数。

沿每个元素/字段记录账号规范化身份、挑战ID/代际、验证消费者、失败次数/锁定/消费状态和会话签发，以获准隔离正常/拒绝回执确认请求级与业务级预算；每次逻辑尝试均计数。拒绝batch、逐次限额、已消费挑战拒绝和合法独立批次作反例，不尝试真实密码/2FA空间或制造耗尽，外部Wallarm文章全文未读。来源：[保存帖](https://x.com/i/status/1397628837970784258)。


## mutation输入subValues与返回resolver的字段权限

低权创建Value时加入subValues空数组，据称响应暴露管理员隐藏子值，卡片只写mutation且对象名遮挡。写入字段与返回resolver可能采用不同授权路径。

绑定actor角色、父对象/子对象owner、输入schema、字段选择/服务端扩展及返回子字段的独立ACL；比较合法低权与受控管理身份的同对象结果。空数组被忽略、只返回自有项或允许公开子值是反例，不能以mutation标题补隐藏数据已泄露。

来源：[保存帖1](https://x.com/i/status/1421813960043470852)。


## GraphQL批量能力与逻辑操作预算

正文推荐BatchQL的batch、CSRF和introspection；另帖Graphw00F仅指纹标题。

区分实现识别、schema可见、请求格式、多operation/alias/resolver、认证与状态改变；一次HTTP可承载多个逻辑动作，预算按resolver/动作而非仅请求数。指纹、公开schema、合法只读batch或未消费mutation是反例，不据工具名补批量绕过或CSRF。

来源：[保存帖1](https://x.com/i/status/1432719827609739267)、[保存帖2](https://x.com/i/status/1435939597163376649)。


## creator邮箱字段路径与订阅者列表声称的区别

VoiceCreator图文字称可列subscriber邮箱，query实际指向publications.creator.email_settings.confirmed_email.email_address，没有response。

绑定调用身份、resolver/object owner、可见性意图、具体返回field、分页和敏感字段最小对照；只query、公开creator邮箱、合法订阅资料、无结果或字段归属不同是反例。结构路径不证明全订阅者名单/权限缺失，未执行GraphQL请求。

来源：[保存帖1](https://x.com/i/status/1440934050059882502)。


## 关闭 introspection 后的查询发现与 resolver 授权

保存帖问 introspection 关闭后还能怎样发现接口，没有给实际查询。

从获准客户端已使用的查询、fragment 和操作名还原可见 schema 线索，分别记录查询合法性及 resolver 的主体、对象和字段授权。关闭 introspection 不等于消除越权或注入，已知合法查询也不等于任意字段可读；不凭问题标题补写攻击回执。

来源：[保存帖1](https://x.com/i/status/1449355902625140744)。


## GraphQL 七类标签与具体执行边界

正文列注入、认证授权、业务逻辑和拒绝服务等类别，没有某个resolver的请求回执。

把类别落实到schema可达字段、解析/验证、resolver、下游消费者与对象权限；为一个受保护动作建立允许/拒绝对照。schema暴露、错误信息或复杂查询本身不证明影响，已授权字段和查询限制是反例。不执行复杂度压测或DoS。

来源：[保存帖1](https://x.com/i/status/1457889593353592835)。


## 批量删除 JSON 与逐对象授权

Phineas正文/flag替代文字配图却是多个数字payload均200和data.BulkDeleteAlertDefinitions，结果是website/alertDefinitions/id/typename嵌套。

绑定实际operation、身份、对象归属和持久状态读回；HTTP200/嵌套对象并不证明成功删除、越权或所有对象有漏洞。错误字段、空列表、合法本人对象或仅响应为反例，不执行批量删除，也不按CTF题名解释此图。

来源：[保存帖1](https://x.com/i/status/1474281187862409219)。


## graphql-path-enum 资源名与 resolver 授权

正文推荐path枚举工具并称上周有帮助，未存查询、schema或结果。路径发现和resolver的主体/对象权限是两层。

离线自有schema保留入口、类型、参数、角色和resolver，比较可达/不可达、合法/错对象。工具链接、禁用introspection、路径存在或正常权限拒绝为反例；枚举结果不等全部API已测试，不安装/运行未存仓库。

来源：[保存帖1](https://x.com/i/status/1488197131814928388)。


## GraphQL 空 OTP 成功字段不能直接证明 2FA 绕过

完整图POST /graphql有遮蔽token、空otp_code及六位verification_code；HTTP200 JSON同时有was_successful=true与errors.edges。正文标题延伸到RCE，没有完整mutation、语义和会话状态。

离线合成mutation区分phone验证、登录二因素、字段校验、错误和最终身份，比较正常/空值/失败与后续权限。HTTP200、局部布尔成功、其他验证步骤或错误拒绝为反例；无绑定变化不能判2FA绕过，更不能凭标题推RCE。

来源：[保存帖1](https://x.com/i/status/1497118123387801600)。


## GraphQL 思维图把 schema 和动作候选分开

完整图可辨端点/Playground/Schema、基础/深层introspection、类型/字段/参数、query/mutation、用户/权限及商业逻辑；部分微小叶子字不可辨。没有实际服务交换。

离线合成schema按端点、身份、可查询字段、动作和角色归属记录；schema描述与实际授权分别对照。只出现admin/delete词、能introspection、图中列batch/brute或深查询不证明漏洞；无越权结果、文档公开为反例，不执行真实变更、认证批量尝试或深度耗尽。

来源：[保存帖1](https://x.com/i/status/1497905641104736257)、[保存帖2](https://x.com/i/status/1497930716289527813)。


## GraphQL Cop help 和十项检测说法不是审计完成

完整图GraphQL Cop1.0帮助只有目标URL/path、JSON输出和版本；正文后称约十种DoS/CSRF/info leak检测，repo卡没有具体规则。

离线按schema/字段、请求身份、查询深度/批次、允许方法与证据分别设计有界样例、负例和结果。帮助启动、检测类别或工具名称不能确认漏洞/全覆盖；无结果、无跨主体或正常拒绝为反例，不运行深查询/批量认证或资源耗尽。

来源：[保存帖1](https://x.com/i/status/1501169526708314114)、[保存帖2](https://x.com/i/status/1501169699450617859)、[保存帖3](https://x.com/i/status/1503445859375198213)。


## GraphQL OTP 批处理按业务操作数约束

正文建议将多个 OTP 尝试放在一个 GraphQL 请求内，未给验证结果。

区分请求数量、批内操作数、执行次数和每账户失败计数，核执行上限、错误处理和状态是否一致。自有有限样本只用于观察计数边界；一次 HTTP 请求不等于一次验证，批处理存在也不证明验证码可破解。

来源：[保存帖1](https://x.com/i/status/1524801545799405575)。


## 模式发现和扩展加载分别核查完成状态与权限

保存正文描述 GraphCrawler 收集查询、变更、认证和猜测模式；InQL 图片显示加载进度及空 Output/Errors，并未显示加载完成。先固定工具/运行时版本、加载结果、当前身份、模式来源和实际端点。

模式可见不等于对象或字段越权，加载界面也不说明查询已执行。用自有对象对照真实查询与变更结果，给模式猜测及变更单独设置操作预算和清理，不把未保存的仓库能力当已验证行为。

来源：[保存帖1](https://x.com/i/status/1549801307053203456)、[保存帖2](https://x.com/i/status/1551272080343060481)。


## GraphQL批量请求应核对每个操作的计数与授权

正文提示 GET 与 batch queries，外链标题将批量与密码、MFA 和对象枚举并列。先确定端点支持的传输和批格式，再用有上限的自有操作比较单请求、多操作中的权限、错误及限制计数。一次 HTTP 成功不等于每个操作成功；批量存在也不证明绕过限流、MFA 或对象权限。身份和状态读回分开记录，未保存的外链内容依用户按覆盖，不补造利用细节。

来源：[保存帖1](https://x.com/i/status/1563347818915303424)、[保存帖2](https://x.com/i/status/1565716193515753473)。


## Schema路径和工具评分不能代替字段授权

GraphCrawler图显示mutation读取错误、十二queries、零敏感项、_service授权及三条CoreVideo路径。分别核对schema/查询/字段/对象权限，用两个自有角色与对象固定query和变量比较实际返回，保留introspection关闭、错误及未查变体。schema有路径不等于可读敏感节点，_service成功不等于所有查询开放；自动Criticality数值不是业务严重度。限制深度/宽度/成本并避免默认mutation。

来源：[保存帖1](https://x.com/i/status/1568603816349646848)。


## GraphQL批处理按逻辑操作而非HTTP包数检查限流

CrackQL 宣传涉及批量破解、2FA、IDOR；只有工具能力声明。用自有账户与无害操作比较单操作、alias/批次、费用与身份边界，记录每个 resolver 的实际结果和服务端计数。一次 HTTP 请求可能包含多次逻辑尝试，状态 200 不能证明每项成功；限流和对象越权需要独立负对照，少量预算后停止，不枚举第三方账号。

来源：[保存帖1](https://x.com/i/status/1570789627447087105)。


## GraphQL schema 可见不等于 SQL 注入

正文标题SQLi但图实际为__schema和types/fields返回，未见数据库sink或结果。将schema发现、操作可调用、字段授权与SQL消费者分开记录；用自有操作确认身份/对象，再对可达数据库参数做有限无害对照。200/schema名称不证明敏感数据或SQL执行，不能用标题补全被省略的链。

来源：[保存帖1](https://x.com/i/status/1582712154083315712)。


## GraphQL introspection 的分级须落到可访问数据和操作

正文讨论 introspection 被不同平台评级，图片只有修复及奖励邮件。把 schema 暴露、未授权字段读取、跨用户对象访问和写操作权限分别检验；用自有角色和对象对照错误、返回字段及实际状态。仅能 introspect 不意味着业务操作授权失效，也不能以历史 P 等级或奖金预定当前影响；缺失 schema/query 的奖励图只保留为历史上下文。

来源：[保存帖1](https://x.com/i/status/1586205416978948096)。


## GraphQL 正则提取和遗漏 batching 都需回到实际执行预算

保存 nestle 输出通过 query/mutation 正则与 sed 换行抽取，依赖命名与嵌套格式；另一帖说安全指南遗漏 batching，未保存指南正文。以已授权本地 schema/请求样本比较匿名/命名、多行/fragment/嵌套及批量输入的解析集合，分别评估每请求、每操作、深度和聚合成本及授权。正则提取不等完整 AST 或所有对象覆盖；支持 batching 本身不构成漏洞，未读指南细节不补造，资源对照在隔离样例进行。

来源：[保存帖1](https://x.com/i/status/1588663734389846016)、[保存帖2](https://x.com/i/status/1590781062061658112)。


## Schema 可见与数据对象权限是不同边界

保存 API 图列 introspection、可视化和查询枚举，用于理解 GraphQL 结构，不能推出“数据库每个查询都可访问”。在自有实例记录 schema 版本、operation、变量类型、身份与字段/对象权限，区分公开元数据、查询验证和实际解析器数据消费。用两自有对象的单字段无害查询与拒绝对照；可视工具或 introspection 返回不证明越权，扫描不到结构也不能证明无隐藏方法，不枚举他人数据。

来源：[保存帖1](https://x.com/i/status/1611989144464678915)。

已实际查看保存图片 `1611989144464678915-02.jpg`：API完整脑图read：reco版本v1v2v3/开源定制/RESTSOAPGraphQL/WADLWSDLpublic-local/GETPOSTPATCHPUTDELETE/cookie-headerauth/JWT加密编码序列化hashID/比较doc/fuzzendpointactionobject/bodyheader映射/Swagger；enumRESTresourcesobjects与响应头长度行为/GraphQLintrospection与Voyager/kiterunner-unfurl；工具Postman导入环境collections+proxy/authOTP/JSJSONtest、SoapUIWADLWSDL/endpoint、Burpmonitorrequests/content/header/JS、有限fuzz端点对象methods(FfufIntruderArjun)/SecListsFuzzDB或waybackdocsJSrepo开源造字典。Dweb/fuzz/auth/graphql接口描述与实际部署/身份schema权限/状态写入/范围预算，不能introspection=所有DB权限或tool默认安全。


## GraphQL 风险清单需按 resolver 数据流而非类别名确认

正文列normalization、DoS、SQLi、auth、introspection、CSRF及errors。建立schema字段→resolver→底层服务/数据库/授权/渲染链，分别用自有小查询检查类型规范化、字段/对象权限及最小错误；限制深度、别名和预算，不运行耗尽测试。introspection或详细错误是信息候选，SQLi需要实际非参数化sink，CSRF需要浏览器认证状态改变，auth需要无权结果；清单标题不是多个漏洞已确认。

来源：[保存帖1](https://x.com/i/status/1616130317399764993)。


## GraphQL aggs 必须在聚合前应用相同可见性约束

保存报告search与opportunities_search的aggs参数/返回字段可暴露private program handles。对象hits过滤正确仍可能让未授权行进入buckets/counts；聚合键、计数、nested索引与租户条件均须相同授权。自有公开/私有两组canary比较管理员与无权用户普通搜索和聚合，确认私有标记或可推导信息泄漏；仅有aggs字段、总数或introspection不独立证明私密信息。限制查询规模，禁止列举真实私有计划。

来源：[保存帖1](https://x.com/i/status/1616148972568969253)。

已实际查看保存图片 `1616148972568969253-02.jpg`：GraphQL search/opportunities_search aggs返回私有program handles，聚合必须先受相同可见性过滤，不只过滤hits。


## GraphQL 目录转换为解析器和操作权限检查表

保存目录和正文覆盖查询/变更、参数、变量、内省、错误、数据库注入和鉴权。将每项绑定实际 resolver、主体、对象和字段：查询可见性、变更权限、变量类型与底层查询拼接分别验证。内省、函数名或错误信息本身不等于未授权访问，SQLi 需要真实数据库 sink；只用自有对象构建有权/无权对照，不把一张目录计作多项已复现漏洞。

来源：[保存帖1](https://x.com/i/status/1616465596778176512)、[保存帖2](https://x.com/i/status/1616857430843092994)。

已实际查看保存图片 `1616465596778176512-02.png`：GraphQL目录：enum/introspection/args/functions/query/mutation/lessinputs/wildcards/IDOR/database/DOS/amplification/variables/pagination/tools；目录无规则实测。


## GraphQL 分页与放大量以实际资源预算核验

目录提到 pagination、wildcards、较少输入、DoS 和 amplification，但没有实测阈值。由此形成检查问题：页大小、嵌套深度、别名数量和聚合是否受主体与全局预算约束，返回对象是否在分页前后都经过权限过滤。用小规模自有数据比较成本和结果，超时或大响应只作为候选，不运行耗尽服务的查询，也不把目录中的名称当成确定漏洞。

来源：[保存帖1](https://x.com/i/status/1616465596778176512)。


## introspection 转 Postman 请求：schema 存在与对象权限分开

正文建议把 GraphQL introspection 结果交给 Postman 构造 queries。首先保留 schema 获取身份/时间和实际导入版本，人工确认变量类型、必填参数、operation 与所需 header/会话，检查工具是否只是生成请求模板。introspection 公开和可生成 query 不等于敏感数据可读，每 resolver 的对象/字段/tenant 授权需要两个自有身份及最小查询对照；mutation 应单独约束副作用。存档没有导入操作/返回结果，不宣称当前所有版本自动支持同样步骤。

来源：[保存帖1](https://x.com/i/status/1628279463313043457)。


## GraphQL 范围、模式发现与邮件流程授权分开确认

帖子声称范围外GraphQL发邮件可批量ATO，图只有P1接受/升严重性通知；另有introspection和自动化外链与logo。模式发现、suggestions和查询可达仅暴露结构，不证明数据或mutation授权失效。确认端点明确纳入范围，以两个自有账户对照resolver主体、对象归属、邮件目标/令牌绑定和结果；不要批量发送真实邮件。跨业务链每环分别留证，范围外成功标题不会自动授权后续测试。

来源：[保存帖1](https://x.com/i/status/1629556526229643266)、[保存帖2](https://x.com/i/status/1629679252466458625)、[保存帖3](https://x.com/i/status/1629769654620024833)。


## GraphQL schema 和控制台发现须连接 resolver 权限

graphql/altair/playground、debug及旧版本提示可发现入口，内省有多种查询形态但不能把“两版本”当通用标准。记录schema版本、接口身份及每字段/resolver对象/tenant权限，在受控mutation验证持久更新；注入另需实际下游SQL等消费者。公开控制台/schema、工具Voyager/Altair/Raider和REST包装说法不证明漏洞或所有端点漏授权。

来源：[保存帖1](https://x.com/i/status/1634235166104141827)、[保存帖2](https://x.com/i/status/1634565339202633729)。

现有图片证据 `1634235166104141827-02.jpg`：GraphQL图建议schema/introspection、graphql/altair/playground、debug与旧版本，工具Altair/Voyager/Raider；所谓两版本内省不构成通用标准。控制台/内省公开并非漏洞，需resolver逐字段对象/tenant授权、mutation结果和实际下游SQL消费者验证。


## GraphQL 提取工具与 schema 公开不等于授权缺陷

Graphicator帮助有目标header/file、proxy/Tor、insecure、multi/no-cache等配置，影响请求身份/TLS/缓存须固定记录。内省图有FullType/TypeRef/InputValue而operationName仍GetSiteStats，需完整请求契约与schema响应验证。53KB声明没有完整回包，schema公开只是发现面；resolver逐字段/对象/tenant与mutation持久效果才确认权限问题，不能由提取成功推数据泄露。

来源：[保存帖1](https://x.com/i/status/1635268759794634752)、[保存帖2](https://x.com/i/status/1635644011624140801)。

现有图片证据 `1635268759794634752-02.png`：Graphicator帮助包含use-tor默认9150、insecure禁证书警告、proxy/Burp、header键值、file目标、multi和no-cache；工具名标Extractor，不证明GraphQLschema/对象授权缺陷，代理/TLS/缓存会影响证据需固定配置。

现有图片证据 `1635644011624140801-02.jpg`：GraphQL curl截图片段有FullType/TypeRef/InputValue内省片段、header上下文与GetSiteStats operationName；没有完整53KB响应，operationName和query需契约一致，内省schema不是数据读取/授权漏洞。


## JS 正则抽取 query mutation 要保留语法覆盖缺口

保存nestle嵌套regex加sed替换转义换行，限制操作名字母/数字组合，未示结果。保留源码/hash和原字符串位置，核对匿名操作、下划线、fragment、变量/字符串与转义，以GraphQL解析结果分类。抽取文本不等schema、可达接口或授权，sed改变内容可能误解字符串，不执行抽出的mutation。

来源：[保存帖1](https://x.com/i/status/1643337702790811649)。


## GraphQL 查询层与 NoSQL 数据库要分开审查

正文将GraphQL与MongoDB一起列为NoSQL数据库，这是分类错误；GraphQL是API查询层，resolver可连接不同后端。追踪输入值是否进入NoSQL操作符/查询对象或SQL拼接，固定schema、类型转换与过滤条件，比较自有对象的正常/异常查询结果。查询语言标签或NoSQL封面不证明注入；图背景SSRF拼贴不能补出数据库利用链。

来源：[保存帖1](https://x.com/i/status/1644263681193283584)。


## GraphQL 测试表必须使用真实 schema 与后续消费者

图列__schema types{name}、users(where:name)的SQL字符串、仅引号XSS和file(path)穿越，未给目标schema/响应。先确认类型、字段/变量与角色，追踪resolver到SQL/NoSQL/文件及后续HTML呈现，以有限自有对象比较允许/拒绝对照。introspection可能设计公开，自造字段不通用，引号不是XSS执行；列表“comprehensive”不证明批量/深度/成本和对象授权已测。

来源：[保存帖1](https://x.com/i/status/1646154995543207938)。

现有图片证据 `1646154995543207938-02.jpg`：GraphQL表格含__schema types{name}、where名字SQL注入、XSS仅引号、file(path:../etc/passwd)；自造schema/类型不通用、普通引号不是XSS、introspection公开不是越权，需resolver/存储/呈现consumer具体验证。


## 空过滤器不能代替 GraphQL 对象授权

保存正文称 filter 为空可返回其他用户。为 resolver 定义身份、允许对象集合与字段可见性，以自有 A/B 对比合法筛选、空值、省略值和分页/批量路径。筛选用于缩小结果集，服务端仍须按调用者授权；空结果、报错或含其他对象都需结合对象本应可见的规则。正文没有完整响应，保留假设与最小对照，不推断全量用户泄露。

来源：[保存帖1](https://x.com/i/status/1664489666828029952)。


## 字段建议推断 schema 后仍须逐 resolver 检查权限

正文介绍在关闭 introspection 时利用字段建议恢复 GraphQL schema；卡片只有工具描述。错误建议能提供类型或字段线索，但字典猜测不保证完整 schema，更不证明查询、变更或跨用户 resolver 缺少授权。在自有 GraphQL 中保存候选、建议响应和实际可调用字段，比较正确、错误及受限字段，追踪 resolver 的角色与对象检查。被猜到的公开字段或正确拒绝的 mutation 不是越权；缺少实际 schema 输出时保持为方法线索。

来源：[保存帖1](https://x.com/i/status/1671754140505047040)。


## GraphQL mutation 的状态枚举必须由服务端角色守卫

UpdateVacancyStatus 的名字暴露审批状态操作，但判断取决于调用身份、对象所有者、当前状态与目标状态是否在 resolver 中检查。自有模型比较普通发布者和审批者对同一合成职位，核对 resolver、允许转换与实际公开状态。端点存在或客户端能传枚举不等于绕过；守卫正确拒绝、发布仍待人工审批是反例。截图没有完整变量/响应，不补造 GraphQL 请求。

来源：[保存帖1](https://x.com/i/status/1676644096184664065)。

保存图证 `1676644096184664065-02.jpg`：inDriver Job 招聘/简历创建编辑需管理员审核，最后 POST /api/graphql 调用 UpdateVacancyStatus；报告描述跳过审批并发布内容，操作参数与执行响应裁切，实际可发布状态需要普通用户/管理员权限和外部可见性对照。


## GraphQL operationName 不能替代响应字段的授权检查

SaveCollaboratorsMutation 名称关联邀请流程，但数据泄露要落在具体 resolver、返回字段和 pending 状态。自有合成对象对照同一查询在不同邀请状态/角色下的字段选择，记录服务器真实响应，不能仅凭 mutation 名称、编辑按钮或捕获请求证明邮箱暴露。操作参数被裁切，未保存接受前后完整交换；历史 High 与奖励仅作为报告元数据，不发起邀请。

来源：[保存帖1](https://x.com/i/status/1676645302759989255)。

保存图证 `1676645302759989255-02.jpg`：HackerOne SaveCollaboratorsMutation 邀请后 pending 未接受状态，编辑添加协作者入口捕获的请求能出现目标邮箱；报告描述私人邮箱在接受前披露，HTTP 请求裁切，须对照邀请状态、调用身份和实际响应字段，不批量邀请真实用户。


## schema 模拟和 resolver 请求能力分别建立证据

graphquail 介绍含 schema 构建、introspection emulation 和自定义头，模拟出来的 schema 不证明服务端 introspection 已开启或每字段可访问。allTicks/source 则需具体 resolver、参数处理和 HTTP 消费者，权限、查询成本及受保护状态各自比较。工具能力或高评级不能补齐实际 query/响应，未知字段保持未知；不安装扩展、执行查询或补抓仓库内容。

来源：[保存帖1](https://x.com/i/status/1682405213452533760)、[保存帖2](https://x.com/i/status/1683711376613855233)。

保存图证 `1683711376613855233-02.jpg`：EXNESS报告summary allTicks查询source参数用于GET，可设回调域并观察DNS/HTTP；嵌套请求截图太小原始字节不可读，底部HTTP证据被截，未证明私网/元数据/内网端口或RCE。要绑定resolver参数、服务端来源、redirect/DNS目的地址权限，不发回调。


## GraphQL别名登录必须按认证尝试计数（2023保存案例）

实验室 GraphQL 请求将大量不同密码登录尝试放入别名 bruteForce0–62；响应中多数 success=false，bruteForce49 为 true。HTTP 200、响应大小或令牌字段的存在不能代替成功状态与会话验证。别名批处理可能绕过按 HTTP 请求计数的预算，应比较按解析字段/认证尝试计数与按请求计数；仅为实验室示例，不复用账号密码。

图片证据：`1688194082047422465-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1688194082047422465)。


## 保存图证0187-114-graphql：条件与证明边界

Graphinder说明-d域名/-s脚本/-b目录/-p precision、默认bruteforce和script开启、可-f域列表。默认主动行为和发现范围需确认/限定，loadedbrowser脚本来源不代表全站；发现GraphQL端点≠schema或未授权操作，版本参数需查实际工具，未运行。 可用原图：`1692413066477207675-03.jpg`。

来源：[保存帖1](https://x.com/i/status/1692413066477207675)。


## Graphinder 默认发现行为与明确请求预算（0187）

保存帮助图提供目标域、文件、脚本、字典和代理等参数，并说明默认暴力路径与 JavaScript 扫描。先从正常流量和前端脚本识别 GraphQL 候选，再将目标、字典、方法、认证及代理绑定到授权范围；返回 200 或工具定位 endpoint 不证明 introspection、越权或资源耗尽。使用帮助参数前核对安装版本，记录最小样本与请求量。

来源：[保存帖1](https://x.com/i/status/1692413066477207675)。


## GraphQL 字典规模与真实 schema/授权覆盖（0188）

由生产端点词汇构建的 GraphQL wordlist 可用于猜测字段和类型，但 60k+ 端点声明不保证当前项目 schema 完整或字段可用。将候选与实际查询错误、类型、角色和合法查询基线关联；字段发现与对象授权分开验证，限制查询数量与复杂度。词表适配 Goctopus/Clairvoyance 不代表所有版本的默认行为相同。

来源：[保存帖1](https://x.com/i/status/1695017752149590495)、[保存帖2](https://x.com/i/status/1695118847286845662)。


## 正文提炼0189：schema 推断与 resolver 鉴权是两回事

Clairvoyance保存描述是introspection关闭时推断schema，未含实际schema/实现；可作为错误信息/字段候选与端点建模线索。禁用introspection不保证字段保密，推断结果可能不完整且依赖验证错误；记录身份/角色与每个可见字段，resolver对象/字段访问必须独立受控对照。schema可见并不等于敏感数据可读，工具宣称不补具体枚举结果。

来源：[保存帖1](https://x.com/i/status/1699133349191877119)、[保存帖2](https://x.com/i/status/1699273633410248830)、[保存帖3](https://x.com/i/status/1699779622966292765)。


## 保存图片中的机制与证据边界（1705892274268160247-02.jpg）：by-type/graphql.md

图片 `1705892274268160247-02.jpg`：Apollo Sandbox/api/graphql?endpoint=https://evil.com使UI Endpoint改变，subscription仍ws://localhost:4000，ExampleQuery id可见；开发探索器可能本来允许任意endpoint。需证明受害者操作、敏感查询/手动Authorization头是否实际发往攻击者受控站及产品承诺，跨域凭据和UI改址不等于泄漏。保存图无发出查询/响应/凭据，不测试真实用户。

来源：[保存帖1](https://x.com/i/status/1705892274268160247)。


## 0194：未公开 mutation 与隐藏界面不代替对象授权

Copilot 图描述 JS 中的未公开 GraphQL 与 DestroyLlmConversation，移除 hidden 类只控制显示。先用自有 A/B 会话比较普通读、同 owner mutation 与异 owner 拒绝，读回实际状态；删除类操作只在隔离对象验证。图没有请求/删除结果，接口未公开与前端藏按钮都不自动证明 IDOR。

来源：[保存帖1](https://x.com/i/status/1717330395501584769)。


## 保存图证0194-111-graphql：1717330395501584769-02.jpg

Copilot 报告截图描述从 JS 发现未公开 GraphQL 查询与 DestroyLlmConversation mutation，并用前端移除 hidden 类显示界面。客户端显示控制与服务端对象授权是两个边界；需要授权的 A/B 自有会话比较 mutation 的所有权校验和实际状态变化。截图没有请求或删除结果，显示隐藏界面本身不授予服务端权限。

实际保存图：1717330395501584769-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717330395501584769)。


## 保存图证0195-94-graphql：1720177877360967736-02.jpg

奖励信描述已知userUUID与recipientID时GraphQL路径授权可读/改recipient数据，没有query/variables/response。与正文id/../id2结合仅路由归一化候选，GraphQLresolver或其REST二次请求需绑定owner/tenant。自有A/B对象单ID比较读与写后状态、UUID知识不授权限；奖励金额/题名不代替PoC，未保存更多细节。

实际保存图：1720177877360967736-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1720177877360967736)。
