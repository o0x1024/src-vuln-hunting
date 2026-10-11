# CSRF

适用信号：依赖浏览器自动附带身份的状态操作

## 检查与最小实验

先确认操作、自动凭据、攻击者可构造的字段三项条件。用受控跨站页面触发一次获准的可逆测试操作，同时记录浏览器实际请求与服务端前后状态。分别看缺失/错误/另一测试会话的 token 是否被拒绝，以及方法或服务端接受的媒体类型变化是否走了不同防护路径。

SameSite 的 site 与 origin 不同；用真实浏览器记录 cookie 是否发送、Origin/Referer 与预检。Bearer 令牌若无法由攻击页获得，也非浏览器自动发送，不能手工在重放工具里补上后宣称 CSRF。

## 证据与反例

确认的是被禁止的跨站状态变化；缺 token、能发请求、读不到响应都不是单独结论。CORS 拒绝读取并不保证动作未执行。排除重新认证、SameSite、Origin 校验和幂等操作；允许的跨站工作流不是缺陷。

## Agent 行为

浏览器完成请求可行性验证，工具读取权威状态；只使用测试账号并及时恢复。登录 CSRF 与账户绑定场景还需核对最终身份，见 [OAuth/OIDC](oauth-oidc.md)。

## 宽容解析与跨站可构造性

JSON 接口声明改成 text/plain 后仍接受正文，只证明后端解析宽容。先用正常字段和无害标记确认输入确实被消费，再从受控外站验证相同请求是否可构造、凭据是否附带、防护是否生效及最终状态是否变化。内容类型接受、CORS 无法读取与 CSRF 动作成立分别记录。

## 调研来源

- [PS-csrf · CSRF](https://portswigger.net/web-security/csrf)
- [MDN-cors · Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

认证是否依赖 Cookie 要按具体操作及全部实际接受的凭据路径判断。正常客户端使用 Authorization 头，不能代替对 Cookie 回退、其他自动凭据与跨站请求可构造性的检查；若唯一有效凭据确实需要攻击页无法取得的显式令牌，则不能手工补入它来证明 CSRF。分别记录请求发出、服务端认证主体和最终动作。

存在 Origin/Referer 校验不代表所有操作均不可利用：核对具体入口、方法、缺失头时的分支、允许来源与实际浏览器凭据，再判断本次动作。流程图中只写“secret methodology”的分支没有可恢复步骤；历史客户端插件/Flash 方案还缺当前运行前提，不能据图登记为已具备的证明方法。

字段名变化与字段类型变化分开观察：不能把名为token[]的JSON属性直接记成已解析数组；表单数组约定、JSON结构、缺失字段和校验器收到的实际值需逐层核对。用正常token、自有会话的错误/缺失/类型对照记录真实动作，先排除落入未消费正文或另一处理器，再验证浏览器跨站条件。

iframe响应因X-Frame-Options或frame-ancestors不能显示，不保证已经发出的状态请求未生效。分别保存表单/导航请求是否发出、自动身份、服务端动作时序与权威终态，再记录浏览器的响应嵌入错误；请求前被阻断和响应展示阶段拒绝不同。多表单/多步骤只在真实流程依赖成立时，以最少获准请求和可逆测试资源核对，不按源帖错误截图声称CSRF已完成。阶段依据：[CSP3工作草案导航响应检查](https://www.w3.org/TR/CSP3/#frame-ancestors-navigation-response)（2026-10-09核对），实际浏览器实现仍需对照。

文件上传跨站构造时保存字段名、文件字节、文件名、multipart边界、请求来源与实际Cookie，而不只看fetch代码。FormData.append的第三参数是文件名覆盖，不是文件内容；空字符串组成的File仍是空内容，不能靠变量名推存在上传正文。[FormData条款](https://xhr.spec.whatwg.org/#dom-formdata-append)、[HTML条目创建](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#create-an-entry)与[File构造](https://w3c.github.io/FileAPI/#file-constructor)（2026-10-09核对）支持该语义。credentials:include声明不能保证SameSite/第三方Cookie条件下身份真的发送；浏览器请求、文件消费、服务端状态变化与响应读取限制分别核对，仅使用小型无害测试文件，不执行源截图。

恢复正常AJAX请求时，X-Requested-With: XMLHttpRequest可作为客户端行为线索或处理器分支条件，但字段值本身不是身份凭据，也不证明跨站来源。比较实际合法请求、该头缺失时的处理器及服务端防护；重放工具能设置此头不能证明普通攻击网页同样能发送。[Fetch请求头安全列表](https://fetch.spec.whatwg.org/#cors-safelisted-request-header)（2026-10-09核对）不包含X-Requested-With；浏览器跨源添加该头需要核对实际预检/缓存及服务器允许结果，再验证自动身份和权威状态。不能由“加头后接口响应”直接登记CSRF或授权绕过。

Jira表单token缺失告警需要恢复正常会话/表单基线，并区分具体WebWork动作、REST端点和插件处理器。源帖把X-Atlassian-Token: no-check写成请求正文；[Jira表单token文档](https://developer.atlassian.com/server/jira/platform/form-token-handling/#scripting)描述的是HTTP请求头，且用途是脚本请求的token检查路径（2026-10-09核对）。重放工具添加该头后告警消失不证明攻击网页可跨站设置、自动身份会发送或敏感状态已改变；按真实预检/来源和权限核对，不全局禁用XSRF设置，也不从错误页推Jira/Confluence所有版本通用绕过。

## 对象标识与跨站动作保证

高熵userid仍首先是对象标识，是否能充当步骤保证取决于谁可获得、绑定的主体/用途及处理器验证，不能按“无法爆破”代替跨站防护。用已知自有对象核对跨站请求可构造性、自动身份、令牌/来源检查和邮箱等字段的权威终态；对象越权、CSRF与后续恢复接管分别证明。搜索可见ID不是许可，也不需要枚举真实用户来建立对照。

## 双提交值相等与会话绑定

正文token与Cookie同改后200，不能断言只在客户端校验；服务器也可能在执行双提交比较。分别核对值是否与当前会话/签名绑定、真实动作是否完成及另一来源能否设置该Cookie。代理可改两处不证明攻击网页可改Cookie；Domain/Path、可写入口与现有身份是独立前提。只用自有身份的合成值建立对照，不植入真实会话或把session fixation当现成能力。

将POST换成GET后token不再检查，只补处理器/方法差异。还需确认GET真的消费同一状态操作、浏览器能构造请求并带身份，以及Origin/SameSite等其他防护；合法只读GET是反例，200不代替权威终态。

## text/plain表单序列化与JSON字段语义

[HTML text/plain表单算法](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#plain-text-form-data)按name、一个等号、value及CRLF拼接（2026-10-09核对）。先检查实际浏览器条目/序列化字节与JSON解析结果；源帖写出的name/value不能产生其宣称的JSON，不能当作已验证技巧。

即使得到合法的带等号键名，它也不等于原键名，后端可能忽略或走另一字段分支。分别核对媒体类型接受、语法有效、业务字段真正消费、跨站可构造性、自动身份与权威状态变化。只在获准隔离表单和无害字段做对照，不能以JSON解析成功、服务端200或缺token认定CSRF动作已发生。

## 邮箱绑定、确认能力与事后导航

历史图先给自有账号绑定并验证一个邮箱、移除后再通过声称的CSRF给另一主体添加该地址，最后改确认链接的redirect到/home来减少提示。这是多个待证边：先前地址验证是否被跨主体复用、跨站请求实际凭据/防护、确认能力绑定的账号/地址/动作/时效，以及最终恢复/登录用途；拥有收件地址不等于有权绑定其他主体。

/home是同源导航示例，不能仅凭它认定开放重定向；导航藏住设置页也不能代替账号状态变化证明。只分析获准的两个合成身份与隔离邮件/脱敏日志，明确哪个主体发起、哪个主体确认及实际受保护能力，不向真人投递CSRF或确认链接。截图只有步骤叙述，未展示请求、浏览器行为与权威终态，保留这些缺口。

## 空值相等与浏览器可构造请求

双提交的两个值都为空时，先区分字段缺失、显式空串、解析回退与会话/签名绑定，不能只验证相等关系。图中只有脱敏P3/P4 Triaged标题，没展示完整请求或业务状态，评级不能补出技术证明。

Repeater可设置自定义CSRF头，不代表外站HTML表单能设置该头；浏览器脚本的预检、CORS、Cookie/SameSite、Origin与服务端动作另证。用获准自有浏览器和合成动作比较正常值、空/缺失及实际可构造来源，不由返回成功或生成HTML就认定跨站效果，也不向真人投递PoC。

## 表示路由的授权与跨站检查

/authorization与其.json/.xml表示可能选中不同路由、中间件或序列化处理器。某路径的对象授权正确不代表另一路径也执行CSRF检查；反过来，少了token告警也不证明业务动作或跨站条件成立。

以同一自有身份/合成对象的正常请求追踪实际方法、MIME、字段消费和保护步骤，再对有依据的表示分支比较自动凭据、Origin/Referer、token绑定与权威终态。合法公开/只读表示是反例；源HackerOne链接未展开，不补其完整请求或修复范围，也不把后缀变体全站排列执行。

## Lax的顶层导航与方法条件

[MDN Set-Cookie说明](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#lax)规定跨站Lax发送还取决于顶层导航与安全方法，fetch、子资源和iframe导航不同；浏览器省略SameSite时的兼容默认也与显式Lax不同（2026-10-09核对）。GET不是任何场景都自动带身份的开关。

先确认当前Cookie属性/浏览器/site、实际导航及出站凭据，再判同一受保护操作是否接受GET并改变状态；只读GET是反例，手工Repeater改方法不证明浏览器行为。Cookie发送是正常策略语义，缺陷在违反跨站状态保证的消费者；不向真人导航链接或改变真实账号状态。

## Referer的来源结构与附加利用前提

target.example.evil.example属于evil.example下的名称，把target字串放在路径/查询也不改变来源；分别核对实际URL解析后的scheme/host/port、真实浏览器Referer策略、缺失头处理与服务端允许来源。任意子串/前后缀匹配的候选与真实跨站状态效果分开，不能用重放工具手写Referer就声称网页可构造。

分号、点击劫持、子域接管与XSS是独立的解析/权限/交互能力，不能作为Referer通用绕过步骤继承。用获准自有身份/合成动作的正常与拒绝对照核对自动凭据及终态；缺头被拒绝、可靠来源检查、重新认证和合法跨站工作流均是反例，不向真人投递页面或占有外部资源。

## 方法覆盖的处理顺序与JSON请求可构造性

POST加_method=PUT时，记录传输方法、应用有效方法、覆盖来源/优先级、路由与CSRF/授权中间件执行顺序。截图的application/json、Cookie和200响应只说明一次手工请求/回显，不证明外站页面能构造相同请求或状态已变化；URL override不能自动把JSON变成浏览器简单请求。

用获准隔离普通字段及真实浏览器来源，分别核对MIME消费、预检/自动凭据、token/Origin/SameSite和权威终态。JSON里的link/javascript样式值又是另一消费者假设，未展示触发就保持缺口，不从同一个200同时登记CSRF、IDOR和XSS。

## base元素、相对表单目标与独立CSP指令

HTML注入能够影响base元素时，先关联有效的首个href、已有文档基址、相对form action、脚本提交方式和最终解析地址。[MDN base说明](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)指出仅首个href/target生效；[base-uri](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/base-uri)限制基址且不回退default-src，[form-action](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/form-action)独立限制表单提交目的地（2026-10-09核读相关段落）。

在获准离线/隔离的合成表单中追踪注入位置到有效DOM、相对地址解析、实际提交/用户交互和允许目的地。已有有效base、绝对action、脚本指定绝对地址或实际form-action拒绝都是反例；未设置base-uri不证明全部表单内容会外送。不要加载来源webhook载荷或提交真实表单秘密。

## 禁用2FA动作与后续登录条件

禁用2FA的CSRF需关联真实设置动作、浏览器可构造请求、自动会话、CSRF/来源防护、再认证要求、绑定主体与权威配置变化。来源图用两个自有账户叙述生成PoC后2FA关闭，但没展示方法/字段/站点策略；生成HTML本身不证明普通外站能发出同一请求。

获准隔离对照禁用前后设置及独立新登录所需因素，排除UI缓存、仅自身身份修改和合法重新认证。因素关闭不代表攻击者已知密码或获得现有会话，后续账号接管前提分别陈述；不创建线上账号、加载来源PoC或改变真人安全设置来补证。

## 改密缺少当前密码与CSRF因素的分别归因

改密时同时移除当前密码和CSRF token产生的结果，不能区分重新认证缺失与跨站请求防护缺失。两者各有契约：前者限制当前身份的敏感状态变更，后者关联浏览器自动凭据/来源/站点策略/可构造媒体类型；token字段省略仍可能有其他有效校验。

在获准可恢复合成身份/既有日志中固定当前会话、请求方法与字段，按单一因素对照及其组合关联真正密码终态和新登录；排除UI文字、缓存或实际未提交。生成PoC不证明普通外站能重现相同请求，因素缺失也不自动等于攻击者已接管。不发送PoC给真人、修改真人密码或以全部字段一起删代替归因。

## referrer元数据与真实请求头

HTTP头拼作Referer，但HTML元数据名是referrer。[MDN元数据说明](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer)给出name=referrer与content=no-referrer抑制该头的语义（2026-10-09核读）；旧图name=referer/content=never不能直接当当前可工作的例子，Referer策略也不能推出Origin必同时为空。

核对真实文档策略、浏览器、请求类型、自动身份与服务端缺失/空/合法来源分支。去掉token、改方法、改长度、写空Origin与手写Referer都需要分别归因；重放工具行为不证明跨站网页可构造或服务端动作已完成。用已有获准浏览器记录/合成动作与拒绝对照，沿来源检查及权威终态证明，不向真人投递页面或把缺头接受单独记成CSRF。

## 链接noreferrer与导航操作的限制

rel=noreferrer是链接注解，referrerpolicy=no-referrer是来源策略，不能把它们都写成HTTP头值。[HTML链接类型](https://html.spec.whatwg.org/multipage/links.html#link-type-noreferrer)规定跟随该链接不泄露来源信息且具有noopener行为；[Referrer Policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy-no-referrer)规定正确策略拼写为no-referrer（2026-10-09核读）。旧帖no-referer拼写错误，排版弯引号也需与实际HTML字节分开，但有效rel仍可能独立作用，不能把一个拼写错判为全例必无效。

调用链接click属于导航消费者，并不自动构造原API的POST/JSON/自定义头；与img子资源在顶层导航、Cookie/SameSite及Origin行为上也不同。只用获准隔离无害链接/已有浏览器记录核对实际请求、身份、缺Referer分支与权威状态，可靠token/Origin校验及不接受导航方法为反例。缺头接受不单独证明CSRF，不让真人点击或用手写请求头替代浏览器可构造性。

## 浏览器容器与可比较的CSRF主体

旧帖称Chrome里失败可转Firefox Multi-Account Containers。容器可帮助安排多个受控账号，但不是通用CSRF绕过器。[Mozilla说明](https://support.mozilla.org/en-US/kb/containers)确认同站多账号及容器站点分配功能（2026-10-09核读）；不同容器/浏览器也可能改变实际登录主体、设置或流程基线。

固定自有账号、版本、container/profile、cookie是否真实随请求发送、site/origin、方法、token及正常流程，以同一受控对象核对服务端状态。另一个账号成功、扩展隔离状态或Chrome未发凭据不是绕过证明；不安装扩展、改用户设置或在真实账号发跨站写请求。

## 两个账号重放与真正跨站CSRF边界

旧图先从A捕获关闭2FA请求，再关闭标签保持B登录，在新标签提交PoC看B是否关闭。若两个账号共享浏览器凭据，切标签不等于切身份；B能合法关闭自己2FA、直接同源重放及跨站攻击者诱导也是不同结论。

核对独立自有会话、实际Cookie/token、目标账号、Origin/Referer/同站策略、重新认证与服务器权威2FA状态，并用正确自有操作、缺凭据及拒绝分支对照。CSRF需要实际攻击者可发起的跨站请求及受害者身份条件；A票据跨B被接受可另查主体绑定。图没有完整请求/跨站过程，不执行PoC、关闭用户真实2FA或把单纯新标签当跨站证明。


## 密码重置helper表单与浏览器环境的真实状态

重置UI、POST302和Burp生成CSRF HTML使用当前Cookie；另一帖称JWT复制到Cookie后90%可CSRF。都没有给真正跨站浏览器和最终密码状态。

绑定受控第三方origin、Cookie发送条件、SameSite、认证来源、Origin校验、恢复challenge及最终权威状态。助手生成表单、手工带Cookie成功或同站操作不是跨站证明；没有环境凭据、challenge已失效或动作被拒都是反例，不采用90%比例。

来源：[保存帖1](https://x.com/i/status/1419614979880218628)、[保存帖2](https://x.com/i/status/1419687105811394560)。


## 图片触发注销的读者与重复消费条件

保存[1/2]正文提出把注销链接放img src，使组织成员读取后退出。未保存第二段及全员受影响记录。

先确认图片会被实际请求、注销端点是否改变状态、cookie/SameSite/域作用域、受控读者会话及重复渲染；合法本人注销、请求无cookie、GET无副作用或图片被代理拦截是反例。单次退出与持续不可用分开，不由HTML注入推全员DOS。

来源：[保存帖1](https://x.com/i/status/1427143380211957764)。


## CSRF 参数替换与浏览器投递条件

阿拉伯语帖依次建议删除参数、空值、随机长度、其他账号令牌及变更方法；初学文章仅保存标题。

用自有账号验证服务端是否忽略令牌、校验结构或绑定主体/动作，另记录浏览器可发送的方法、编码、cookie、Origin/Referer 与 SameSite。重放器成功或删字段成功不证明跨站投递；必须有实际无害状态改变，缺少登录上下文、方法不可投递或额外挑战均是反例。

来源：[保存帖1](https://x.com/i/status/1447428530065784834)、[保存帖2](https://x.com/i/status/1449555451742466049)。


## Exporter、LazyCSRF 与表单方法覆盖的等价性

Exporter 图提供 clipboard、文件及 XHR/表单生成；LazyCSRF 图把 JSON PUT 请求改成 POST 加隐藏方法字段，并和 Burp 表单比较。

生成文本不证明真实浏览器行为。比较线上请求的 URL、序列化、Content-Type、cookie、Origin、令牌及方法覆盖是否被后端识别；HTML 表单不能任意等价 JSON PUT，隐藏字段也可能无效。保存最终无害状态变化和未覆盖对照，脱敏导出且不执行档案 PoC。

来源：[保存帖1](https://x.com/i/status/1447738688327221251)、[保存帖2](https://x.com/i/status/1447939497413562372)、[保存帖3](https://x.com/i/status/1450571000442195972)。


## 隐藏编辑接口到 CSRF 接管的缺口

正文给找到账号/编辑接口、制作 CSRF、发送受害者的五步自述，配图只有 High 标题。

隐藏接口仍需认证、字段权限、方法与实际用户上下文核对。跨站投递能力、令牌/Origin/cookie 条件和自有账号持久改变分别证明；High 标题、用户可见接口或自己提交成功不是完整接管链。不得向第三方发送 PoC，报告保留缺失步骤而非补写成功。

来源：[保存帖1](https://x.com/i/status/1451167449253089290)。


## WordPress 插件自述与核心奖励标题的组件差异

正文称扫描旧插件后利用 CSRF，图则是 WordPress 核心版本 <4.8.5 的奖励标题。

先对应核心/插件包、版本、处理器、登录条件、令牌/Origin 和自有状态变化，独立核对双方来源。核心标题不能证明某插件受影响；扫描器旧版判断、相似路由或不同安装实例是反例。未保存真实浏览器请求，不运行旧 exploit。

来源：[保存帖1](https://x.com/i/status/1452666873779146752)。


## 删除账号 token 建议与不可逆动作边界

正文建议删/换CSRF token，图为奖励和fixing邮件，没有真实跨站请求或删后状态。

先审查处理器、token主体/挑战绑定、Origin/SameSite/cookie及真实浏览器等价性。优先可逆等价动作或明确授权的一次性实验对象；删除需专门明确范围，本次不执行。其他token被拒、未带cookie、仅提示变化或状态不持久为反例，金额不证CSRF成功。

来源：[保存帖1](https://x.com/i/status/1456691022251970565)。


## 有 token 的 CSRF 假设与 critical 标签

正文建议有token也继续、emailchange，图却含H2RCE P1 New与另单CSRF Critical Triaged；无浏览器跨站证据。

核对token挑战/主体/动作/时效绑定、浏览器凭据、Origin和持久状态；需要可逆自有数据的允许/拒绝对照。其他单等级不能证明emailchange当前失败，已拒绝/未带cookie/仅本地改UI为反例。不更改真实邮箱或发送通知。

来源：[保存帖1](https://x.com/i/status/1467682739478540289)、[保存帖2](https://x.com/i/status/1467758897888776193)。


## 可读取 token 与上传延迟图片错配

正文建议页面取得未绑定CSRF token；所附图却是upload fileName包含sleep15、单次15.3秒与200HTML，并未保存token跨会话动作。

仅用自有A/B会话与不改变数据的fixture比较token绑定、Origin/cookie与实际保护动作；可读token不等于可跨站提交。图片还需正常/无效合成输入、网络/队列时间与实际SQL/命令消费者对照；一次延迟、错配标题或无状态改变为反例，不发延迟/命令载荷。

来源：[保存帖1](https://x.com/i/status/1478893972772691969)。


## OAuth 注册分支移除当前密码后的改密保护

完整正文说普通改密要求当前密码，OAuth注册后同动作不用当前密码并声称CSRF，没有保存跨站请求和持久化结果。

用自有合成账户分别记录两注册分支、会话与改密合同，静态核token/Origin/SameSite/请求格式和重认证；最小比较正常/错来源/缺token/不满足重认证，持久化能力独证。仅表单不显示密码、另一防御生效、浏览器未送凭据或未改变服务器状态为反例，不改他人密码。

来源：[保存帖1](https://x.com/i/status/1484414294842556418)。

语义校核：[OWASP CSRF 防御](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)。


## CSRF 接管标题仍需浏览器凭据和状态绑定

完整图只有CSRF导致ATO的P2 Triaged/仍评估状态；另一帖是RXSS窃取登录表单接管文章标题。没有跨站请求、凭据策略或会话结果。

离线两个自有origin/账号比较浏览器发起、Cookie策略、Origin/token、受限动作与登录身份绑定。分诊标题、相同站点请求、需已有会话或服务端拒绝为反例；XSS能力和CSRF条件单独证明，不发送真实重置/登录请求或收集凭据。

来源：[保存帖1](https://x.com/i/status/1498460984608014338)、[保存帖2](https://x.com/i/status/1499424800686624774)。


## CORS 读权限与 CSRF 状态修改是两个门

正文称攻击域带credentials可造成CSRF，但无保存浏览器请求或修改结果。

分别记录浏览器能发送的请求、Cookie条件、后端Origin/token检查、状态变化，以及响应能否被攻击域读。简单表单可发送而响应不可读，CORS允许读也未必能修改；preflight被拒和后端拒绝都为反例。用隔离模型核对，不向真实账号发请求。

规范核对：[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)。

来源：[保存帖36](https://x.com/i/status/1504309125932777478)。


## 改密码 token 检查不当必须落到服务端结果

正文称CSRF致ATO，图仅passwordchangeP3Triaged；未保存token检查或改密交换。

隔离测试模型固定受害者身份，比较正常/空/无/错token和跨来源条件，记录后端确实改密与旧新凭据的生命周期。响应200、前端消息或P3标签不等改密，更不自动证明接管。

来源：[保存帖64](https://x.com/i/status/1504778412317159438)。


## JSON CSRF 的 simple complex 示例还缺语法和凭据条件

simple图设置textplain却未withCredentials；complexapplicationjson设置withCredentials。两图roleadmin字符串/引号不完整，不能视作可直接执行的PoC。

离线先审JS字符串与JSON格式，再按ContentType、凭据、SameSite和预检建立发送矩阵，确认后端解析/Origin/token检查与角色实际变化。simple可发送不等携带身份，complex被preflight拒绝不等role改变，API无token也可能有其他有效防护。

规范核对：[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)。

来源：[保存帖106](https://x.com/i/status/1505818821818417153)。


## CSRF checklist 的双提交修改要核攻击者 cookie 控制

图列GETPOST、空缺token、同长变字、重用、decode、double submit cookie+param、跨账号token。

隔离模型用服务器绑定session的预期token，逐项比较状态而非回显。改cookie和param只有真实攻击来源能影响对应cookie时才有意义；token可decode或可重用不天然失败，一次性定义与验证范围需核。自动“workedmosttime”没有保存统计证据。

来源：[保存帖143](https://x.com/i/status/1506300802008510465)。


## Origin null 不是单一可信来源的身份

正文建议 data 协议制造 Origin null 来绕过 CSRF 校验。

浏览器 opaque origin 等场景可能产生 null，但要保存真正由浏览器发出的 method、Origin、Cookie、SameSite 结果及服务端状态变化，不能从代理手填 null 推出跨站可利用。无 allow-same-origin 的 sandbox 或 data 文档只能说明来源条件，仍需请求权限和受限动作消费者。依据：[MDN Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin)。

来源：[保存帖1](https://x.com/i/status/1514346096411439105)。


## HTML 表单注入到 token 外送需要表单归属链

正文给出 form 与 textarea 片段，含弯引号和不完整 action，但没有最终 DOM。

核验插入位置、HTML 解析修复、token 控件所属表单、action、用户交互及是否实际提交。存在 HTML 注入不自动把页面全部 token 归入该表单，格式不完整也不能假设有效；外送仅在自有无敏感标记样本中验证。

来源：[保存帖1](https://x.com/i/status/1517151474295656448)。


## CSRF 修改资料后需验证存储和受害者渲染

保存步骤把 CSRF 改 profile name、切换 beta/重定向和 stored XSS 相连。

核真实浏览器携带身份的请求、CSRF 约束、资料持久化与另一自有主体的渲染，再分别确认 beta 状态和跳转。修改成功、保存载荷和脚本执行不是同一结果；一键触发与奖励也不能补足完整权限影响。

来源：[保存帖1](https://x.com/i/status/1519029368240095233)。


## text/plain 表单的最终字节与服务端接受条件

图把 JSON 片段放进表单字段名和值，以容纳 text/plain 序列化产生的等号。

在自有离线样本核最终请求字节、媒体类型、JSON 解析和状态变更，再核浏览器是否携带会话、CSRF 校验与来源约束。表单可跨站发送不等于业务接受；pushState 只改同源历史 URL，不能把发送页面变成目标来源。规范核验：[MDN CSRF](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF)。

来源：[保存帖1](https://x.com/i/status/1520367368731611136)。


## CSRF 生成器产生表单还需真实跨来源业务结果

图展示由代理请求生成表单、Test in browser 和本地 burpsuite 展示 URL。

核生成后的方法、字段与编码，以及发送页面来源、会话、防伪校验和最终状态。工具本地展示地址不等于目标来源，Submit 按钮不证明 CSRF 或 XSS；录像还需绑定最小 HTTP 证据。

来源：[保存帖1](https://x.com/i/status/1528888750499143680)。


## 交易示意中的诱导点击需核身份与防伪绑定

银行交易图把诱导链接、已登录交易页与转账结果相连。

示意不证明真实交易成功。记录发起来源、会话携带、收款对象、金额及防伪校验，再用自有无害业务核最终状态；UI 欺骗与跨站请求是否接受分别解释。

来源：[保存帖1](https://x.com/i/status/1529357081362386944)。


## API 令牌变更的 CSRF 与最终凭据状态

敏感端点候选需在真实跨站浏览器上下文核对请求方法、Cookie/SameSite、反伪造令牌、Origin/Referer 与服务器认证。用自有账户确认令牌实际改变及旧、新令牌状态，区分只编辑 UI、请求被接受和变更成立。奖励截图不提供这些条件，不能从金额或 P2 直接推出接管。

来源：[保存帖1](https://x.com/i/status/1535433325888045056)。


## 浏览器 PoC 先证明跨站自有会话的真实状态变化

保存正文询问生成 CSRF PoC 后测试和发送的含义。先明确目标动作、方法、可由跨站构造的输入、浏览器 cookie 行为、SameSite 与服务端 token/来源检查，再在自有账号和受控来源比较实际前后状态。

能生成表单或点击“Test in browser”不等于 CSRF 成立；须确认浏览器确实附带有效会话并完成非预期姓名或密码变化。使用可恢复测试动作并保护会话，不向其他用户发送 PoC；权限影响与真实状态证据分别报告。

来源：[保存帖1](https://x.com/i/status/1545077438992056322)。


## CSRF 决策图需要真实浏览器发送和服务端状态证据

保存流程图覆盖移动入口、cookie、token 缺省、跨会话 token、可预测性、JSON、简单内容类型以及 CORS。先记录动作是否变更状态、真实认证材料、当前浏览器能构造的方法/头/正文、cookie 行为和服务端 token/来源检查，再在自有会话与受控来源验证前后状态。

移动专用入口和图中“CSRF Not Possible”不能作为绝对结论。token 的缺失、另一会话或另一主体替换需要保持用途、有效期与身份对照；重复器中修改 Referer/Origin 的成功不代表浏览器实际可发送相同请求。

普通表单类请求可能无需预检即可发出，CORS 缺少响应读取许可不直接阻止服务端变更；JSON 与自定义头则检查实际预检、替代内容类型是否被后端消费，以及必要凭据。请求可发出、响应可读和变更成功分开记录，不能靠 OPTIONS 或工具生成 PoC 判定。规范来源：[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)。

来源：[保存帖1](https://x.com/i/status/1545947853826187265)、[保存帖2](https://x.com/i/status/1547209212589137920)、[保存帖3](https://x.com/i/status/1547574791028084736)。


## WebSocket 跨站验证保留握手与真实消息权限

视频帧包含 WebSocket onopen、send、onmessage 示例和跨站劫持解释。验证需要受控外部页面、实际握手 Origin、浏览器携带的认证条件、服务器会话绑定以及接收/发送消息的授权结果。

建立一个示例 socket 或收到消息不自动证明带受害会话跨站访问。用自有账号和无害消息，记录连接与每次消息操作分别的范围/预算和最小状态，不从未保存视频推导完整流程。

来源：[保存帖1](https://x.com/i/status/1551546018516193280)。


## 方法切换与存储XSS链必须分别验证跨站写入和消费

保存正文列出CSRF方法、令牌、会话及Cookie条件，并提出POST改GET将self-XSS转为有效问题；图片仅有CSRF存储XSS题名。核对真实浏览器来源、Cookie策略、令牌与会话绑定、方法处理器及持久状态，再用第二个自有消费者验证保存输入的执行上下文。可发请求、改方法、返回成功或研究者自身弹窗不能自动证明整条链。

来源：[保存帖1](https://x.com/i/status/1558569714686631937)、[保存帖2](https://x.com/i/status/1559620715594366977)、[保存帖3](https://x.com/i/status/1561054128918372353)。


## CSRF 生成器保留中文编码及浏览器凭据条件

LazyCSRF 与 Burp 图对比中文姓名字段，原请求含同源头、会话和 authenticity_token。生成表单后核对字段名/字符编码、方法覆写、Content-Type、token 与会话绑定及 Origin/SameSite 条件；用自有跨站页面和测试对象观测实际提交与最终状态。生成成功或同源重放成功都不能证明跨站攻击成立，菜单入口也不是验证结果。

来源：[保存帖1](https://x.com/i/status/1573696257238802434)。


## 账户信息 CSRF 到恢复流程逐步绑定真实身份

my-account.cfm摘要称CSRF更新信息后password reset接管，code未保存。核对浏览器实际Cookie/SameSite、Origin/token校验、被改字段、自有收件地址及恢复令牌归属；POST和发链接并不自动CSRF。最小自有可还原标记先确认状态，再确认最终principal，未保存步骤不补造或向他人发送测试邮件。

来源：[保存帖1](https://x.com/i/status/1580917211987861509)。


## Create Invite CSRF 区分发送和实际加入团队

Lark摘要称诱导用户运行PoC可触发邀请，缺表单/token/cookie细节。用自有受邀账户和组织核对浏览器会话、SameSite/Origin/token、请求格式、实际邀请与接受后权限；存在邀请端点和缺保护标题不证明0click或已加入。限制邮件副作用，不能补造外链中没保存的PoC。

来源：[保存帖1](https://x.com/i/status/1582894310499958784)。


## CSRF 方法和令牌变异要验证浏览器发送及真实状态变化

正文给 POST→GET、空/缺失/改单字符/长度、帐号 A/B 令牌与 null Origin/data URI 候选；保存跨 Origin 认证 POST 图却返回 410 Access Denied。仅对自有可恢复状态用真实浏览器比较合法操作与跨站表单、令牌缺失/篡改/错绑定；记录 cookies、Origin、方法解析及服务端结果。令牌长度正常、HTTP 200/410、CORS 响应头或代理手改 Origin 不能证明 CSRF；更换方法必须确认参数仍被实际消费，令牌不应被当作必需可解密内容。

来源：[保存帖1](https://x.com/i/status/1586250284711280640)、[保存帖2](https://x.com/i/status/1664574083009335305)、[保存帖3](https://x.com/i/status/1586357283973664768)、[保存帖4](https://x.com/i/status/1586576516506619904)、[保存帖5](https://x.com/i/status/1587027349417398272)、[保存帖6](https://x.com/i/status/1587027359018156032)、[保存帖7](https://x.com/i/status/1587027362583285761)、[保存帖8](https://x.com/i/status/1587027368509853696)。


## CSRF 到反射 XSS 须证明跨站表单响应中的可执行上下文

MTN 截图显示 CFID 的 POST 值包含 HTML 事件标记，但 Origin 为目标同源。提炼两条独立条件：输入在响应中突破正确上下文编码，且真实跨站浏览器能携带必需状态并呈现该响应。自有可恢复场景比较同源与跨站表单、正常标记与已编码标记，记录 cookie/SameSite、响应 MIME/策略和无害执行效果。仅代理 POST、同源 Origin 或 CSRF 标题不能证明跨站链成立。

来源：[保存帖1](https://x.com/i/status/1587065281318424576)。


## 合法会话与邮箱校验不能证明跨站请求符合用户意图

保存 deleteUser POST 带 csrf 参数且跨站 Origin 返回 success；PHP 改邮箱代码用 session/UserCheck/validateemail/EditUser，没有独立 CSRF、Origin 或方法校验。另一帖将 _RequestVerificationToken 当 CAPTCHA，null Origin/data URI 为候选。用自有可恢复操作在真实浏览器比较合法/跨站、缺失/错主体 token 和方法变化，记录 cookie 附带、Origin、业务对象的服务器状态。HttpOnly、合法邮箱、HTTP200或 success 字段不证明防护或实际删除；null Origin 需浏览器可达与 cookie 条件，不执行真实删帐号。

来源：[保存帖1](https://x.com/i/status/1588824105838858241)、[保存帖2](https://x.com/i/status/1588909601298481152)、[保存帖3](https://x.com/i/status/1589618056363642880)、[保存帖4](https://x.com/i/status/1589686834573242369)。


## 移除 CSRF 头或 GET 创建都需要真实跨站状态证明

正文称删anti-csrf header仍有响应；AppSearch图描述GET find_or_create创建curations和登录后另一tab/HTMLPoC。用真实浏览器和自有可恢复对象比较合法/跨站/缺头请求，记录cookies、Origin/导航、实际创建前后与保护条件。回应请求不等有副作用，GET也不能据名字判所有防护失效；数百接口须逐对象动作验证，图中凭证不使用，未执行创建。

来源：[保存帖1](https://x.com/i/status/1593155563567091712)、[保存帖2](https://x.com/i/status/1593236971912151040)。


## 内容类型与 SameSite：浏览器可发送请求和状态变化为准

1595842027832610816-02.jpg 称 JSON/text/plain 失败而 form-urlencoded 成功；1597980588362895361-02.jpg 则仅检查 SameSite 属性，报告为 not-applicable，并提到 None 缺 Secure 时被拒绝。CORS 的读限制和缺少某 cookie 属性均不能独立证明 CSRF。用自有账号真实浏览器核验来源/站点、cookie 实际附带、方法/预检、Origin/Referer/token 校验和状态读回；成功文字不代替动作执行，服务端授权仍须完整。

来源：[保存帖1](https://x.com/i/status/1595842027832610816)、[保存帖2](https://x.com/i/status/1597980588362895361)。


## 历史保存帖0152：点击劫持删除账户需独立交互证据

正文与图片只有删除账户点击劫持奖励标题。可用作危险动作检查项：真实页面可被嵌入、认证 cookie 实际随请求、覆盖引导所需交互、重认证/确认及服务器状态变化；邮件不足以证明任一环节。仅在可恢复的自有测试账户验证，删除影响不应仅靠按钮或200推断。

来源：[保存帖1](https://x.com/i/status/1598591281193689088)。


## 历史保存帖0152：代码题中 SQL 参数化与删除请求来源分离

代码图的 DELETE SQL 使用占位符，但 /delete 为 GET 路由，csrf/session/id 来自服务端读取 Cookie 后的 user 对象，没有可见独立请求令牌校验。审计实际 HTTP 方法、请求携带令牌、当前用户/对象绑定、来源与确认以及操作后的持久状态；SQL 参数化不能替代动作授权或跨站请求防护。GetUserData 省略，不能假定它的安全实现，更不执行删除样例。

来源：[保存帖1](https://x.com/i/status/1599765908032921600)。

已实际查看保存图片 `1599765908032921600-03.jpg`：代码题：Delete SQL 使用占位符，但 /delete 是 GET 路由，csrf/session/id 从 Cookie 派生的服务端用户对象取出，未见独立请求令牌校验；X-Frame-Options 写在 HTML meta 而非响应头。提炼 SQL 参数化≠动作授权/请求来源防护，检查框架响应头、请求方法、实际用户确认和状态读回；GetUserData 省略不假定完整实现。


## 历史保存帖0153：生成 CSRF 表单仍需浏览器认证与读回

工具图只有合成请求和空白PoC区域。生成 HTML 后需核对真实浏览器可发送的编码/方法、cookie条件、来源/令牌校验、交互和持久状态，工具能生成不能证明可利用。不把真实凭据或内部请求提交在线第三方生成器，仅本地自有夹具使用。

来源：[保存帖1](https://x.com/i/status/1601549063224438784)。

已实际查看保存图片 `1601549063224438784-02.jpg`：CSRF 在线生成器图有合成 POST/form-urlencoded 请求、协议与自动提交选项，但 PoC 区为空。生成表单不证明浏览器带认证、来源校验失效或状态改变；不可把真实 cookie/token 提交第三方工具。


## 方法切换、匿名 token 与 CSRF 链都需要真实浏览器对照

正文列 POST→GET、移除 token 及 CSRF 可到创建管理员/改账号的链；图片另称匿名 token 可复用于任意受害者，并展示截断表单。按会话×token 来源×请求方法×Origin×SameSite 建矩阵，在两自有会话检查跨会话 token、缺 token 与正常请求；用实际浏览器交付并回读服务端状态。登录前后同一会话 token 可沿用或代理改包成功，不自动证明跨站可交付。pushState 不改变实际 origin，表单片段也不证明受害者权限；只有具体操作允许跨站触发才进一步评估链，使用可恢复测试对象。

来源：[保存帖1](https://x.com/i/status/1604204803533336578)、[保存帖2](https://x.com/i/status/1604387203135819776)、[保存帖3](https://x.com/i/status/1605243489759166464)、[保存帖4](https://x.com/i/status/1605252922329034752)。

已实际查看保存图片 `1604204803533336578-02.jpg`：Burp Change request method菜单，不能证明改GET后认证cookie送达/CSRFtoken移除有效/跨用户状态改变。POST→GET只是候选，需真实浏览器交付和服务端状态读回。。

已实际查看保存图片 `1605243489759166464-02.jpg`：未登录CSRFtoken拿到登录后重用→anyvictim结论过度；token与会话/身份/Origin/cookie SameSite/CORS/浏览器可交付性需两自有会话交叉对照，匿名会话token迁移本身不证任意受害者。。

已实际查看保存图片 `1605252922329034752-02.jpg`：裁剪HTML表单email字段和history.pushState，没有完整action/method/提交结果或受害者状态；pushState不能改变实际origin，表单示例不保证CSRF→管理员/ATO，需真实浏览器及服务端状态回读。。


## HttpOnly 与 XSS 所处同源请求权限不能混同

正文把无法读 Cookie 时寻找 CSRF token 联到 ATO，奖励图的金额也与正文不同。HttpOnly 限制脚本读取 Cookie，却不自动限制同源脚本发携带会话的请求；CSRF token 的可读性则取决页面/API 和主体绑定。将已存在的 XSS、token 获取、目标敏感动作及重新认证要求分别检查，在自有会话用无害可恢复动作证明所需权限。跨站自定义头还受浏览器跨域约束，不能把同源 XSS 请求示例直接视为跨站 CSRF 或已完成接管。

来源：[保存帖1](https://x.com/i/status/1605579322269372423)。


## Login CSRF 的自动提交示例仍需证实实际会话切换

图片有固定测试账户隐字段、pushState、提交后立即跳 account，action 弯引号和立即导航都可能改变行为。用自有两浏览器会话核查登录前 token、Origin/SameSite、会话轮换、请求确实发送及最终登录主体，比较正常登录/拒绝路径。pushState 不改变 origin，看到 account 页面也不确定主体切换；登录 CSRF 成功需服务端会话证据，不将模板视为必然有效。

来源：[保存帖1](https://x.com/i/status/1607797519769292800)。

已实际查看保存图片 `1607797519769292800-02.jpg`：LoginCSRF HTML POST隐字段固定测试账户并自动submit然后立即location/account，弯引号action和导航可能竞态，pushState不变origin；真实cookie/session切换/预会话token/SameSite/Origin，selfXSS共享执行链需自有两会话标记，禁止keylogging/凭证收集。。


## 登录 CSRF 与自操作脚本链需要会话切换证据

保存正文将 self XSS 与 login CSRF 串联，相关图片的二进制哈希已有实际审阅记录。链条须独立证明外部页面可令浏览器进入指定的自有账号、受害会话确实被切换、可控内容在后续受信上下文执行，以及该效果超出单纯自己操作。固定测试账号的表单、立即跳转与自动提交可能有竞态；history API 不改变 origin。使用两份自有会话与无害标记，记录 cookie、预会话 token、SameSite、Origin 和持久状态，不收集键盘输入、密码或真实会话。弹窗截图不能单独补齐完整链。

来源：[保存帖1](https://x.com/i/status/1608080289649000449)。


## 方法替换与 token 七候选都要核对浏览器状态

保存十条技巧和独立帖把 POST/PUT/PATCH 变 GET、参数移到查询并删除 X-CSRF 头，以 200 声称绕过；七项清单还包括缺失/字符变更/跨账号复用 token、弱生成/可猜以及 XSS 获得 token。用自有两会话比较 token 的会话、动作与用途绑定，记录原方法和替换方法是否真正到达同一状态写入。跨站浏览器能否发送实际 cookies、SameSite/Origin/预检及后续状态回读缺一不可；200 或重定向可能只是空操作。少量 token 看似相似不能证明可预测，XSS 是独立前提，不盗取真实 token 或以接口工具成功替代浏览器可利用性。

来源：[保存帖1](https://x.com/i/status/1608774843146866689)、[保存帖2](https://x.com/i/status/1609143918737629184)、[保存帖3](https://x.com/i/status/1609240599294783488)。

已实际查看保存图片 `1608774843146866689-02.jpg`：十条技巧已全图阅读：ffuf过滤404可能丢实际路由；LFI前缀与规范路径分歧；注册组织UUID→数值2的租户绑定；JSON转XML须实际解析/实体才有XXE；WADL与忘密200不足证明LFI到RCE；Twig算术与函数回调权限分开；Tomcat /..;/manager与HTML/text管理路由和角色分别核验不部署WAR；POST转GET去CSRF头200不足状态/浏览器证据；APK解包来源及头部SQL需实际查询sink；XSS路径别名同根因去重，不推奖励=漏洞或未保存链。

已实际查看保存图片 `1609240599294783488-02.jpg`：CSRF七候选：删除、改数字符、跨自有账号复用、弱生成/可猜、XSS取得、POST转GET。需session/action绑定和实际浏览器cookie、SameSite/Origin、持久状态对照；采样统计不证明可预测，XSS是独立原语，禁止真实盗token。


## 数字零与字符串 token 的类型边界

保存技巧提出 JSON 数字 0 与 PHP 松散比较碰撞。审计线上实际解码类型、字符串/数字拒绝策略和校验表达式，以自有测试 token 比较合法字符串、0、空值/缺失和畸形类型，并记录写入状态；不能由框架名称断定比较语义，历史 PHP 行为不可通用到所有版本。对 token 采用明确类型和合适验证，另证实浏览器能送达该类型及认证 cookie，类型比较候选与跨站状态改变分开确认。

来源：[保存帖1](https://x.com/i/status/1609239287912095750)。


## 公开用户 UUID 不能作为跨站请求的秘密

保存故事将用户 UUID 放在公开 URL/搜索结果却用作 CSRF 防护，并与删除旧密码组合。记录 UUID 的用途和可见性、请求真正认证 cookie、token 的会话/动作绑定、跨站浏览器送达条件、SameSite/Origin/预检和实际持久变化。公开标识不是秘密，但仅缺 token 或知道 UUID 仍不足以证明 CSRF；另一项改密验证失败必须独立成立。只在自有会话用无害可恢复标记证明必要前提，不从搜索到他人 UUID 发敏感请求。

来源：[保存帖1](https://x.com/i/status/1612466222758502401)。

已实际查看保存图片 `1612466222758502401-02.jpg`：改密删oldpassword成功+无CSRF/UUID公开URL/Dork⇒ATO声称，Dauth/csrf缺失vs空错旧密码服务端再认证、UUID不是antiCSRFsecret/session/action/browsercookie-SameSite/Origin实际投送与state；两自有会话无生产改密，不从uuid公开+200直接critical。


## Base64 data URI 只承载 PoC 不保证真实浏览器 CSRF

正文Burp生成HTML→Decoder Base64→data:text/html打开，图为生成入口；另一图localhost GET发送成功。核验真实方法/Content-Type、凭据与SameSite、Origin/Referer、不可预测token及浏览器data opaque origin/CSP行为，不能手改cookie或用代理成功冒充浏览器攻击。两个自有账户与可恢复动作对照正常页面、外源页和无token请求，记录实际状态；成功页面、csrf=1参数或PoC生成均不证明跨站。POST XSS还需独立上下文执行证据。

来源：[保存帖1](https://x.com/i/status/1615112123184721921)、[保存帖2](https://x.com/i/status/1616053484813516821)。

已实际查看保存图片 `1615112123184721921-02.png`：Burp Generate CSRF PoC右键入口，仅生成不证明浏览器真实cookie携带/状态改变。

已实际查看保存图片 `1616053484813516821-02.jpg`：localhost compose GET含msg/rID/action/confirm/csrf=1成功发送页面；单成功页面不证明跨站、token或认证边界。


## 成功 compose 页面须补足跨站浏览器与终态

两张保存图仅显示 localhost GET compose 成功，正文则给出一般 CSRF 定义。先确认有意义的状态改变、受害账户会话及真实浏览器跨站行为，再检查 cookie/SameSite、token 和来源验证。用自有账户与自有站点做同站成功/跨站拒绝对照并读取业务终态；直接访问成功页、代理重放成功或含操作名的 GET 不证明跨站携带会话，更不自动形成 CSRF→XSS→ATO 链。

来源：[保存帖1](https://x.com/i/status/1617502532816838656)、[保存帖2](https://x.com/i/status/1617823565616918529)、[保存帖3](https://x.com/i/status/1618591080617836546)。

已实际查看保存图片 `1617502532816838656-02.jpg`：CSRF预告图localhost GET compose成功，虽与0158同样内容新hash实际核读，不证跨站和cookie。

已实际查看保存图片 `1618591080617836546-02.png`：CSRF文章预览缩略GET compose成功，正文模糊；成功页不证跨站。


## compose 的 GET 成功页不证明跨站会话操作

保存图是 localhost compose GET 的 msg/rID/action/confirm/csrf=1 与成功提示，没有跨站浏览器、cookie 或终态。先确认实际状态改变，再在自有账户/站点记录发起来源、会话携带、token/来源校验和最终对象。命令行或直接导航成功不能证明 CSRF，参数名 csrf=1 也不说明验证有效或无效；保存宣传图不是已完成利用链，不扩大异步消息投送。

来源：[保存帖1](https://x.com/i/status/1620038367101566978)。

已实际查看保存图片 `1620038367101566978-02.png`：CSRFnewslettercompose GETmsg/rID/action/confirm/csrf=1 success图新hash已实际读，无cross-origin/cookie/response/state，成功页非CSRF证明。


## JSON 与表单编码差异不能代替 CSRF 状态验证

图把 application/json 称为普通 HTML form content type，应纠正：原生表单的 enctype 为 urlencoded、multipart 或 text/plain；application/json 不属于 CORS 安全列表，普通跨源脚本设置它通常需预检。将同字段改成 urlencoded 只有在服务实际接受该解析方式且浏览器携带有效会话时才可能影响状态，仍需 token/来源/SameSite 和业务终态的正反对照。图仅为请求示意，CORS 响应不可读也不等于状态不会变化。规范依据：[HTML 表单编码](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-enctype)、[Fetch 安全列表](https://fetch.spec.whatwg.org/#cors-safelisted-request-header)。

来源：[保存帖1](https://x.com/i/status/1621018528789987331)。

已实际查看保存图片 `1621018528789987331-03.jpg`：CSRF图把application/json称standardHTMLform错误；跨源脚本JSON一般需preflight，formurlencoded与samecookie/state/token/origin检验独立，图无成功交换。


## 更改 Content-Type 的 success 不等浏览器跨站 CSRF

图声称 JSON body 在 text/plain 被 Cors origin not allowed 拒绝，而 form-urlencoded 返回 success 就 High。先核应用按 Content-Type 选择的实际 parser 与认证、Origin/CSRF 校验路径，用自有可回滚动作比较合法同站请求、跨站原生表单和拒绝来源；记录浏览器真正发出的 bytes/头、Cookie 条件、必要 token、重定向及服务器终态。原生表单有固定编码结构，不能把手工重放的原始 JSON 等同浏览器请求；CORS 阻止读响应不保证写被拒绝，200/success 也不证明状态已变。是否为 High 由实际保护动作和项目规则决定。

来源：[保存帖1](https://x.com/i/status/1622983812128071682)。

现有图片证据 `1622983812128071682-02.jpg`：CSRF JSONbodytextplainCorsoriginnotallowed→formurlencoded success→High断言，无浏览器cookie/token/Origin终态，CORS和CSRF不同。


## 拿到 CSRF token 后：获取条件和会话绑定仍决定是否可伪造

正文问“有 token 是否仍 CSRF”。模型应记录 token 来源、读取身份、绑定的会话/用户/操作、有效期、一次性与浏览器实际带 cookie 条件，再用两个自有会话测试错配 token/省略 token 的拒绝，观察跨源页面能否合法得到并提交有效值。知道自己 token 不证明可替别人发请求；若另有泄露或 XSS 要分别留证而不能省略那一步。是否 token 存在是弱信号，受害者上下文中的真实状态变更才是确认点。

来源：[保存帖1](https://x.com/i/status/1628004282996776960)。


## Blind stored XSS、CSRF 与 ATO 的独立触发链

联系表单blind stored XSS与电商CSRF ATO标题没有保存外链步骤。可提炼的候选链是输入保存→特定查看者渲染→脚本执行，或跨站发送→受害者会话获授权敏感操作；两者不能仅由题名相互代替。自有测试环境用无害标记核对落库、查看者角色、origin、CSRF token/SameSite与实际状态改变，只有账户控制相关操作成功才支持ATO。回连只证明被取用，不能单独证明管理员脚本执行。

来源：[保存帖1](https://x.com/i/status/1628467306945814529)、[保存帖2](https://x.com/i/status/1629112408391163911)、[保存帖3](https://x.com/i/status/1629808494886146049)。


## JSON 修改密码与 HTML 表单序列化的边界

去掉enctype后HTML表单默认application/x-www-form-urlencoded；HTML实体在属性中解码，不把email/new_password自动转换为JSON。先验证服务器是否接受表单或text/plain、原始请求字节及身份Cookie，再比较同源正常与真实跨站表单，记录SameSite、Origin/Referer、CSRF token及持久密码改变。history.pushState只同源改变历史，不能赋予跨站权限；在线生成器不能替代真实浏览器实验，也不应上传敏感原请求。

来源：[保存帖1](https://x.com/i/status/1632767478408392706)、[保存帖2](https://x.com/i/status/1633211313194164226)。

现有图片证据 `1632767478408392706-02.jpg`：修改密码请求截图仅有 POST 路径及 email/new_password JSON；未显示认证、Cookie、CSRF 校验、响应或密码实际改变。

现有图片证据 `1632767478408392706-03.jpg`：HTML 表单未设 enctype 默认提交 application/x-www-form-urlencoded；属性中的 HTML 实体在构造表单时解码，不会自动产生 JSON。history.pushState 只作用于同源。需验证服务器接受该类型、Cookie/SameSite/Origin/token 与密码持久变更。


## CSV 的 S3 上传与应用导入是两个信任阶段

TaxJar历史图前置双账号、攻击者上传CSV，显示S3 multipart POST但签名字段与后续import裁切。必须分别确认对象上传凭证/归属，以及真实跨站请求在受害Cookie/Origin/SameSite/token条件下触发应用持久导入；保留受控CSV及最终交易变化。缺token、S3可上传或Low250/Resolved不等任意受害账户CSRF成立。

来源：[保存帖1](https://x.com/i/status/1636480171434729472)。

现有图片证据 `1636480171434729472-02.jpg`：TaxJar CSV导入报告前置双账号、攻击者上传CSV，图可见S3 multipart POST而完整签名字段/后续导入被裁切；Low250/Resolved。S3对象上传与应用受害账号import两个信任阶段需分别验证，未显示跨站表单/受害持久导入，不能据无token定CSRF。


## CSRF 方法与 token 变体必须在真实浏览器跨站条件比较

正文列POST换GET、旧/空/缺token与删除headers候选。固定自有账户及可逆动作，记录Origin/Referer、Cookie SameSite、内容类型、token用途和持久变化，核对浏览器能构造该请求。手工重放200、不带header或服务端接受方法不单独证明跨站可利用。

来源：[保存帖1](https://x.com/i/status/1640415613721141250)。


## 退订操作的 CSRF 要确认跨站凭据和持久状态

ResMed历史摘要指登录用户GET update-subscriptions退订Communication/Reward会员，称无anti-CSRF token并展示部分HTML起始。核对方法与参数所控制的订阅、SameSite/浏览器发送凭据、Origin/Referer校验及自有账户动作前后；用许可最小可逆动作证明跨站触发。少一个token或有GET接口不能单独确认CSRF，更不能由单例推出全部会员受影响。

来源：[保存帖1](https://x.com/i/status/1643818669443563528)。

现有图片证据 `1643818669443563528-02.jpg`：ResMed历史CSRF摘要登录用户GET update-subscriptions退订Communication/Reward，缺antiCSRFtoken并有PoCHTML起始；Low3.7，图无真实跨站cookie/最终订阅状态。需SameSite/方法/参数用途和持久动作对照，不能当批量全部用户已退订。


## 复用 CSRF token 要定义所谓另一个 instance

帖子把来自另一个“instance”的 token 用于请求。先明确 instance 是浏览器窗口、同用户会话、另一个用户、租户还是部署，再记录 token 与会话/主体绑定、SameSite、Origin/Referer、双提交方案及真正跨站请求能力。相同主体复用 token 可能是正常设计，不等于 CSRF；需在自有 A/B 账户与受控来源证明缺少绑定导致禁止的状态操作，不能仅凭 token 可重用认定。

来源：[保存帖1](https://x.com/i/status/1648264265378217985)。


## 联系人删除的 GET 跨站操作与跨用户授权应分开

图中自有联系人删除是 GET，给出默认 GET 表单且说缺少 CSRF。确认跨站触发时实际发送的身份、cookie/SameSite、Origin 策略以及自有联系人前后状态；GET 或无 token 不单独证明攻击可达。标题“任何用户”不能替代 IDOR，contact_id 与账户归属还需 A/B 直接授权对照。POST 改动本身也不保证 CSRF 防护，缺失原结果时不补写已成功删除他人资料。

来源：[保存帖1](https://x.com/i/status/1650802079298990080)。

现有图片证据 `1650802079298990080-02.jpg`：AcronisGET/account/delete-contact/contact_id/<your_id>无CSRF描述和默认GETform例子；展示自有联系人步骤，标题anyuser不是直证IDOR，需cross-sitecookie/真实状态/selfA/B对象界限。


## 读取 token 与更新 profile 的状态改变分开证明

消息/JSONP/profile 链声称获取 csrf token 并更新 profile，应分别绑定 token 会话、请求动作、来源验证和最终自有账户状态。可发起请求不等于令牌被接受，读取字段不等于能改账号安全数据；缺少响应与状态对照时只记录潜在链，不能补造账号接管过程。

来源：[保存帖1](https://x.com/i/status/1655581821940412416)。

保存图片 `1655581821940412416-02.jpg`：oneclickCSRF静态页windowopen/search、2秒timer、doubleencodedJSONPcallback、postMessage JSON arg App.apiCall；另一JScredentialsinclude profile token→updateProfile；图裁切update下半与trust/CORS响应缺失，多边界需分别验证，禁止偷token/更新外部profile。 本段仅使用实际查看的保存原图，不补未保存内容。


## Cookie 混淆影响 CSRF 要有令牌消费者对照

服务端将后续 cookie 合并进 quoted 值或把逗号视为分隔，可能改变 token/session 读取。比较同一自有会话正常序列、含特殊分隔序列及安全拒绝结果，记录最终解析键与 CSRF 检查顺序。属性解析变化、令牌不见和操作被接受是三层证据；截图没有完整业务请求，不能直接宣称 CSRF 通用绕过。

来源：[保存帖1](https://x.com/i/status/1656305593437798401)。

保存图片 `1656305593437798401-02.jpg`：Chrome孤立surrogate cookie令document.cookie空历史示例、Jetty/Undertow引号吞分号后的其他cookie作为单value；JS展示与wire/serverparser分别，版本未知非永久通用。 本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1656305593437798401-03.jpg`：Undertowquotedvalue结束无分号可新cookie、Zope逗号delimiter历史例；单cookie控能否影响CSRF依赖实际发送/parser及tokencheck，多cookie注入不自动bypass。 本段仅使用实际查看的保存原图，不补未保存内容。


## 敏感 GET 与缺 Origin 需按浏览器发送规则验证

img 导航请求可能携带 Referer 而不带 Origin；Origin 缺失/null/同源/跨源需要分别有服务端策略。对自有无害状态动作记录 cookie SameSite、实际浏览器请求、来源检查与最终状态。CORS 响应不可读不等于请求未被处理，但仅用“没 Origin”也不证明绕过；不要向真实删号或其它敏感 GET 发跨站请求。

来源：[保存帖1](https://x.com/i/status/1657468983258513408)。


## 合法删除请求与跨站删除能力分开

删账户图需页面输入 YES，捕获 POST /users/deleteAccount 包含 Cookie、X-Requested-With 和同源 Origin/Referer，正文下半段未保存。复核完整请求中的令牌/内容类型及服务端来源策略，再用自控无害状态动作证明跨站浏览器能实际发送哪些字段。原始合法请求无 token 的可见片段不证明整个请求缺 token，自定义 header 还可能需要预检，不实际删号。

来源：[保存帖1](https://x.com/i/status/1658140604553916418)。

保存图片 `1658140604553916418-02.jpg`：CSRF删账户页面需输入YES，截图有POST /users/deleteAccount、Cookie、X-Requested-With、同源Origin/Referer而下半身缺失；原始合法请求不能证明跨站浏览器能携cookie/自定义头或服务端缺少校验，无删号动作。 本段仅使用实际查看的保存原图，不补未保存内容。


## 同源表单 token 与跨站状态变更证据分开

截图 profile 请求携 __RequestVerificationToken、cookie、same-origin fetch metadata，响应 302/Profile/Confirm 和 Set-Cookie。保存正常/缺失/错误 token、来源与会话绑定及自有最终状态；不从合法同源捕获推跨站可发送同样字段或绕过令牌。cookie 属性和 token 值不复用，302 不证明他人个人资料被改。

来源：[保存帖1](https://x.com/i/status/1659215551074549763)。

保存图片 `1659215551074549763-02.jpg`：Profile form Email/First/Last与__RequestVerificationToken，响应302/Profile/Confirm及SetCookie auth，sameorigin Fetchmetadata；cookie/token值不复制，未显示跨站PoC/最终变更/错误令牌对照，不从302断CSRF绕过。 本段仅使用实际查看的保存原图，不补未保存内容。


## 双重提交值相等还需确认浏览器可构造请求

正文称 token 和 cookie 都设为1，保存图仅有 X-Csrf-Token:1、JSON、自定义头及 200/success。分别证明 cookie 设置来源、会话绑定/签名、Origin、SameSite、跨站预检和最终地址状态。代理可改任意头不代表受害浏览器可发送同一请求，200 不证明状态改变；自有本地夹具比较正确/错误绑定，不修改真实用户地址。

来源：[保存帖1](https://x.com/i/status/1661973672658104321)。

保存图片 `1661973672658104321-02.jpg`：X-Csrf-Token1 application/json XRequestedWith请求200success，Origin/cookie/前后地址遮盖；重放≠浏览器跨站成功，customheader预检cookie写入finalstate需证。本段仅使用实际查看的保存原图，不补未保存内容。


## 状态方法与资源加载路径按真实浏览器请求核验

POST改GET、avatar/img加载动作URL和 SameSite=Lax 都需要实际方法、cookies、Origin/Fetch metadata 和最终状态。Lax 并非只限制 POST：跨站顶层导航与子资源携带条件不同，同源页面植入 img 又是另一场景。确认 target 是浏览器加载还是服务器代理，以自有可恢复状态和拒绝方法对照；正常200、img HTML或删token重放不证明跨站动作成功，也不能由客户端img请求推SSRF。

来源：[保存帖1](https://x.com/i/status/1662253636691345409)、[保存帖2](https://x.com/i/status/1662482794147135488)、[保存帖3](https://x.com/i/status/1662692677870125059)、[保存帖4](https://x.com/i/status/1662902308324229121)、[保存帖5](https://x.com/i/status/1663152454245175297)。

保存图片 `1663152454245175297-02.jpg`：change_photo filename相对change_password URL被放imgsrc，profile响应回img；展示为客户端sameorigin GET action chain候选，未显示密码最终变更不是serverSSRF，需受控账号会话和GETstatechangeguard。本段仅使用实际查看的保存原图，不补未保存内容。


## 相对图片路径不能赋予目标动作免验证

保存示意将 change_photo 的 filename 写成相对 change_password 路径并回到 img src。此时可能由访问页面的浏览器发起同源GET，应检查URL解析、受害会话、消费者是否以GET改变密码以及动作确认/CSRF边界。回显HTML并未显示密码状态变化，不能称服务器取址或任意ATO，用自有可恢复状态和禁止动作GET作反例，不改真实密码。

来源：[保存帖1](https://x.com/i/status/1663152454245175297)。


## CSRF token 数组必须保持严格 schema

正文提出 csrf token[]/空数组，需保留原参数、解析后类型及验证函数。比较正确标量、错误标量、空值、数组和明确拒绝输出，确认是否 fail closed、会话绑定与真实动作；解析接受不自动通过校验。缺少框架代码/响应时不推某PHP版本或全部token绕过，不实际改变他人状态。

来源：[保存帖1](https://x.com/i/status/1663321822639833090)。


## 异常 Content-Type 差异先验证浏览器与后端解析

正文用 text/plain 后附 application/json 声称跨站绕过。保留精确header字节，确认浏览器是否允许构造而无需预检、后端真正采用的媒体类型、cookie/Origin与动作guard，再以自有正常/拒绝样本比较最终状态。多个类型字串不能当合法JSON声明，也不能保证所有浏览器/框架解析相同，缺请求链时不判通用CSRF。

来源：[保存帖1](https://x.com/i/status/1663531454515609602)。


## CSRF 清单按真实浏览器与最终状态归因

保存清单含 token 移除/替换/跨账号、方法变更、Content-Type、Referer、XSS/CORS 读 token 等分支。先建立自有账号正常动作与拒绝基线，再一次只改变一个条件，确认浏览器会带哪些 cookie、是否需要 preflight、token 与会话绑定，以及受保护状态是否真的改变。长度相同或返回 200 不证明 token 可预测；方法 override 需要服务端支持，XSS/CORS 是额外前提，旧 Flash 分支不能照搬为现时通用路径。

来源：[保存帖1](https://x.com/i/status/1664650194204385289)。

保存图片 `1664650194204385289-02.jpg`：CSRFlist capture tokens predictability remove/value/name crossaccount samelength methodGET _methodcontenttype Refererblank XSS/CORS tokenread plainJSONFlash; checklist baselineactualbrowsercookies/preflight/finalstate XSS/CORSextra precondsFlashlegacy notautomatic本段仅使用实际查看的保存原图，不补未保存内容。


## 关闭管理员 2FA 的题名保留动作前提

正文只给出 CSRF 关闭 admin 2FA 的题名。记录需要验证的登录会话、跨站请求可达性、浏览器 cookie/token 条件和最终 2FA 状态，并检查关键动作重新认证。题名没有给出这些请求或状态证据，不能独立证明绕过；它只定位高影响动作供授权对照。

来源：[保存帖1](https://x.com/i/status/1665798985595113474)。


## 清单和表单生成器保持浏览器请求约束

保存清单含 token 移除、跨账号/同长度替换、方法与媒体类型、Referer、XSS/CORS 和旧 Flash 分支。先以获准自有流程记录浏览器 cookie、Origin/preflight、token 会话绑定与最终状态，单项变更后对照拒绝。生成 HTML 表单不支持任意 HTTP header/method 的断言，方法 override 要有真实服务端消费者；XSS/CORS 是额外前提，旧 Flash 不当作现时通用技巧。

来源：[保存帖1](https://x.com/i/status/1667229869615513601)、[保存帖2](https://x.com/i/status/1667452844289454081)。

保存图片 `1667229869615513601-02.jpg`：CSRF12项token remove/value/name/samelength/crossuser method/type Referer XSS/CORS oldFlash，cookiepreflight实际最终状态需要独立对照本段仅使用实际查看的保存原图，不补未保存内容。


## JSON 转表单必须验证服务端语义和浏览器请求条件

图片把嵌套 `user.id/name` JSON 转成括号键编码的 form body。模型生成编码只是候选表示，不保证后端解析器接受相同对象、重复键或空值，也未验证完整请求头、长度与会话。自有端点比较 JSON、urlencoded 和被拒绝的类型，记录浏览器是否能发出、Cookie 是否携带、Origin/Referer 与 CSRF 校验，以及最终状态。若服务器拒绝表单、解析为不同键或缺少必要令牌，转换不成立；成功改 Content-Type 本身不能证明 CSRF。

保存图证 `1672259480275361792-02.jpg`：模型转换嵌套 JSON 为括号键表单，没有完整头与服务器语义验证。

来源：[保存帖1](https://x.com/i/status/1672259480275361792)。


## 敏感操作 CSRF 需由真实浏览器证明凭据和最终状态

保存帖讨论邮箱/密码修改、缺 Origin 时被接受及移动页面候选。比较普通/移动处理器的服务端校验、方法、Cookie SameSite、Referer、Origin 和 CSRF token，再用自有账号无害状态证明浏览器实际能携带凭据完成动作。Repeater 手工删除 Origin 不证明浏览器可构造同样请求；缺请求和最终状态时不能扩大为账号接管或移动版普遍无防护。邮箱确认、密码重认证和会话失效应作为独立消费者检查。

来源：[保存帖1](https://x.com/i/status/1679130250632986626)、[保存帖2](https://x.com/i/status/1679144235956666369)、[保存帖3](https://x.com/i/status/1680370164938801152)。

保存图证 `1679144235956666369-02.jpg`：TikTok Webcast 历史摘要称 Origin 有值时校验、无 Origin 接受；缺真实浏览器 Cookie/SameSite/Referer/token/最终状态请求，不把 Repeater 手动删头当可跨站成功，评级曾变化。


## Referer 跳转链、方法转换和令牌变体都须真实浏览器对照

清单列删/空/长度变化令牌、其他会话令牌、method override、Content-Type、Referrer、数组/NULL 和历史 Flash/307 等候选。核对令牌与会话/用途绑定、实际处理方法、浏览器可构造性、Cookie/SameSite、跳转策略和最终受保护状态；手工删头或改方法不证明浏览器能发相同请求，随机 token 也非通用绕过。TikTok 平台确认历史 delegation mode 可被另一卖家启禁，但未保存原始浏览器/身份请求，不能补成所有操作或账号接管，不执行真实状态变更。

来源：[保存帖1](https://x.com/i/status/1681986307675832323)、[保存帖2](https://x.com/i/status/1682804480952217600)、[保存帖3](https://x.com/i/status/1684088866268131328)。

保存图证 `1682804480952217600-02.jpg`：CSRF19项清单删token/长度/他会话token/methodoverride/Content-Type/referrer/DoubleSubmit/array/null/CRLF，Flash+307与meta never是历史候选非当前保证；参数解析、token会话用途绑定、浏览器方法/凭据/重定向策略和最终状态需独立证明，不将headers可删等价浏览器可发。

保存图证 `1684088866268131328-02.jpg`：TikTok平台确认美国seller delegation-login端点可启用/禁用另一卖家delegation mode并已修复；缺原始请求/方法/cookie/token/浏览器和两个卖家身份对照，不补成账户接管或全部操作CSRF。


## 泄露某个 CSRF 令牌并不保证全应用状态可改变

缓存泄露假设成立后，还需令牌属于哪个会话/用途、是否一次性或过期、目标方法、浏览器凭据与最终敏感状态。以自有隔离身份和无害状态比较同令牌/另一身份/另一操作的服务端结果；一个 token 不证明应用所有接口共用防护，更不自动取得密码/邮箱控制。归档无完整状态证据，不重放令牌或声称账号接管已验证。

来源：[保存帖1](https://x.com/i/status/1683063527584432128)。


## CRUD 动作逐项检查跨站身份与状态变化

正文建议 CRUD 时测 CSRF，截图只 triaged 通知。按 create/read/update/delete 的真实接口、身份凭据、token、Origin/Referer、SameSite 和浏览器可发送内容类型分别建矩阵，敏感 read 还须区分跨站可读和仅可发。使用自有对象验证状态前后及用户交互，单删 token 或能发请求不能证明 CSRF 成立。

来源：[保存帖1](https://x.com/i/status/1686671113760194560)。


## 缺失token比较必须保留实际跨站凭据与状态

正文建议同时删除token名称和值，应分别比较缺字段、空值、错误值、其他事务值及正常值。浏览器真实跨站请求是否携带凭据、SameSite/Origin/Referer检查和状态变化都属于成立条件；Repeater返回200不能替代受害者浏览器可达性及服务端写入。服务端拒绝或没有实际状态改变是反例。

来源：[保存帖1](https://x.com/i/status/1689742385582903296)。


## 保存图证0187-148-csrf：条件与证明边界

删除账号界面要求输入 delete 并点击按钮。这仅证明前端确认交互；需核对服务端是否校验确认值、请求方法、令牌和跨站约束，不能据此判定 CSRF。 可用原图：`1693394318214463609-02.jpg`。

访问 deletion_confirmation.js 显示含删除、取消、重复表单及失败提示的 HTML 页面。扩展名可能触发服务端路由回退；应比较原始响应、实际请求方法、令牌、SameSite 和状态变化，不能把页面可访问当成账号已被删除。 可用原图：`1693394318214463609-03.jpg`。

来源：[保存帖1](https://x.com/i/status/1693394318214463609)。


## 删除确认页面与跨站操作能力分开核对（0187）

`deletion_confirmation.js` 显示删除页可能源于路由回退；“输入 delete”也可能只发生在前端。先对自有可恢复测试账号核对原始响应和服务端接受的请求方法、确认值、CSRF token、Cookie SameSite 及来源要求，再用不会真正删除的数据或隔离测试验证跨站可达条件。访问页面、表单呈现或失败提示不证明账号删除成功。

来源：[保存帖1](https://x.com/i/status/1693394318214463609)。


## 无登录表单的滥用与会话依赖的 CSRF（0188）

Contact/support 表单若不依赖受害者身份，跨站提交可能是垃圾消息/业务滥用，不能仅因缺 token 判定典型 CSRF。登录/退出常会改变浏览器会话，需测试是否把受害者绑定到攻击者账号或造成真实状态变化。通过自有隔离表单比较 Cookie、来源、SameSite 和服务端保护，P4/P5 或 informative 属具体项目结论，不能按表单类别固定评级。

来源：[保存帖1](https://x.com/i/status/1695103993809379555)、[保存帖2](https://x.com/i/status/1695103993947836688)。


## 正文提炼0189：删除 token 后必须完成真实浏览器对照

省略authentication_token/verification token的请求被接受仅是服务器校验候选；还须跨站浏览器可构造method/Content-Type、Cookie/SameSite、Origin/Referer、有效会话以及真实状态变化。以自有账号可撤销资料改动比较有效token、缺失、错误及另一会话token，200与页面提示不能代替服务器读回。profile语言/通知等低影响设置与邮箱/安全操作分开评估，不给真实受害者发PoC。

来源：[保存帖1](https://x.com/i/status/1698602282533691891)、[保存帖2](https://x.com/i/status/1700163039775903980)。


## 保存图证0189-14-csrf：机制与验证条件

Mars 2029753 删除宠物接口 /kisallataim/ANIMAL_ID/delete；图示自动提交 form 未声明 method，默认 GET。复用点是以授权自有宠物确认 GET 状态变更、浏览器跨站是否实际带 Cookie、SameSite 和 Origin/Referer 校验，并对照缺凭据/错误对象/无副作用请求；页面 Medium(5.0)、resolved 不替代真实删除状态证据，展示代码不能凭空证明任意用户删除。 可用原图：`1696930917103841410-02.jpg`（保存帖 1696930917103841410）。

来源：[保存帖1](https://x.com/i/status/1696930917103841410)。


## 保存图证0189-15-csrf：机制与验证条件

Mars 2037234 可见 POST /_post/usuario_actualizar.php 表单，nombre、apellido、email、rut、idProvincia、idLocalidad、optin 等字段，apellido 值为 script alert；截图在第 12 行截断，enctype 右边被截，不能补猜整个 PoC。分别验证跨站带凭据写入与后来页面的存储/渲染执行，apellido 插入须依 HTML/属性/JS 上下文确认，单个表单字符串和报告标题不证明执行或接管。 可用原图：`1696931057457942820-02.jpg`（保存帖 1696931057457942820）。

来源：[保存帖1](https://x.com/i/status/1696931057457942820)。


## 保存图证0190-110-csrf：机制与验证条件

保存原图文件：1703162860141195572-02.jpg。

CSRF清单含令牌缺失/空值/删字段/等长错值/跨自有账号替换、POST→GET、_method、替换Content-Type及Referrer缺失。每次只改一因素，保留实际状态变化；浏览器可发送性、Cookie SameSite、Origin/Referer检查、CORS预检需同时成立。_method仅框架支持时有效；meta referrer content=never为历史写法应验证浏览器行为，Flash过时方案不能作当前默认；XSS/CORS令牌读取是独立链，不自动证CSRF。仅清单无实际目标结果。

来源：[保存帖1](https://x.com/i/status/1703162860141195572)。


## 保存图片中的机制与证据边界（1704544665121472821-02.jpg）：by-type/csrf.md

图片 `1704544665121472821-02.jpg`：CSRF清单含改GET、删令牌参数/空值、未使用令牌/自有另一账号令牌、等长错值、改首尾、Content-Type变体、Referer正则/省略。单变量对照浏览器可发送性、Cookie SameSite、Origin/Referer与实际状态；HTTP字段大小写不敏感，referrer拼写与Referer标准字段不同不能称大小写绕过。multipart/form-data才是标准而非图中form-multipart，meta应是name=referrer而非referrer错拼；HTML注入未必能读/外传令牌，需独立数据流。仅教学清单没有目标结果。

来源：[保存帖1](https://x.com/i/status/1704544665121472821)。


## 保存图证0193-73-csrf：机制、前提与最小验证

已查看的原始图片：1713283675289493618-02.jpg。ImpressCMS1.4.2 PHP7.2.24 Firefox85，admin.php POST memberslist_id/memberslist_uname[]未过滤且无CSRF token允许授权用户访问恶页发请求；图仅表单起始history.pushState不等全PoC。分开证cookie/SameSite/Origin/令牌、用户控制输出HTML执行；匿名/缺cookie/有token/编码对照。

来源：[保存帖1](https://x.com/i/status/1713283675289493618)。


## 保存图证0195-126-csrf：1721105288043102716-02.jpg

ownCloud10.12.2报告图在admin会话下POST/settings/users/users，form-urlencoded创建groups[]=admin用户，缺requesttoken且伪Origin http://abc:8080。curl可任意设Origin/Cookie，不是浏览器CSRF可达；核真实跨站浏览器能否携会话、SameSite/Origin/CORS与simpleform、缺token拒绝与最终自有隔离用户创建状态。图片是步骤无响应，不执行创建真实账户。

实际保存图：1721105288043102716-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1721105288043102716)。
