# OAuth / OIDC 与账号绑定

适用信号：第三方登录、授权回调、code 兑换、账号关联

## 检查与最小实验

记录 client、授权服务器、资源服务器、redirect URI、浏览器会话、PKCE/state/nonce 各自用途；OAuth 授权与 OIDC 身份认证分开。用两个自建身份跑通正常流程，再只改变一个绑定条件。

| 维度 | 核对 |
|---|---|
| 回调 | 精确注册回调和实际落点；原生 loopback 端口有规范例外。开放跳转链只向获准接收端验证。 |
| 事务 | code 的客户端、回调、会话、PKCE 绑定与单次消费；没有 state 不自动缺 CSRF 防护，正确绑定的 PKCE/nonce 可能承担相应保护。 |
| 身份 | issuer/subject 与本地账号如何关联，email 是否已验证且来自可信发行者；不能仅按显示名推断账号接管。 |
| 令牌 | audience、scope、用途、刷新生命周期；令牌字符串变化不等于旧令牌已失效。 |

## 证据与反例

需要实际关联到错误测试账号、把凭据交付不应接收的受控端，或资源服务器接受错误用途的令牌。登录成功但身份仍正确、回调只反射文本、代码已拒绝，均不支持接管。

## Agent 行为

不同授权事务隔离保存，只用已授权账号和回调。不把 `nonce` 当所有 OAuth 流必需字段；对实际 flow 按 RFC 9700 核对，JWT 细节见 [JWT](jwt.md)。

有效邮箱与有效提供方令牌必须属于同一被验证身份。用两个自有提供方账号核对令牌中的可信主体与客户端声称邮箱、本地账号关联结果；分别验证“凭据有效”“邮箱存在”不能代替验证二者的绑定。邮箱大小写/规范化、未验证邮箱与合法账号合并也需分别解释，不能仅因登录成功就写账号接管。

## 调研来源

- [RFC-oauth · RFC 9700: Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

回调可用子域、开放跳转、XSS或引用接管时，先证明各组件的实际控制权，再关联同一次合法测试授权的注册回调、每跳落点、凭据表示和最终受控接收者。截图中的“token stealing”步骤是组合假设，缺少真实凭据流不能补造；access token、ID token、code的用途分别核对，取得一种值不自动允许登录或接管。仅用自有身份和合成受保护资源，不使用源图的任何凭据。

回调链接触发会话循环或持续刷新时，保存授权事务、回调消费结果、实际Cookie的Domain/Path/顺序、服务器选值与每次刷新/重签发。用两个隔离自有浏览器核对合法回调与另一事务链接的绑定、受影响会话范围及清除/恢复路径；缺state、页面循环和“可能多Cookie”分别为观察或假设，不能直接证明因果与全账号DoS。交叉参照[会话状态](authn-session.md)，不向真实用户投递链接，也不以刷新压力扩大影响。

## 登录与账号链接的不同绑定

账号链接请求同时包含提供方令牌、userid和email时，分别核对可信提供方主体、当前业务会话、被修改本地账号及链接后的登录身份。用两个自有测试账号对照允许的链接和本应拒绝的主体变化，保存最终绑定/解绑与合成资源能力；字段可改或链接成功页面不证明接管。登录流程的主体绑定正确不代表链接处理器也正确，合法管理员代链接与用户授权迁移作反例，不获取他人提供方令牌。

## state全局存在与发起会话归属

state在系统中存在，不等于它属于当前回调浏览器发起的事务。按两个隔离自有会话记录发起者、待关联的业务账号、提供商账号、state/PKCE等事务保证、回调消费和最终绑定。图示中的另一会话点击链接只是假设投递路径；在当前会话仍有其他正确绑定时应拒绝，不能用缺少某一字段替代整条链。账号链接还须核对现有主体确认与允许的提供商身份；不向真实用户发送链接，不重放有效生产code。

## 第三方创建身份之后的本地重复注册

第三方登录创建本地账号后，同邮箱本地注册可能是允许添加新认证方式、创建另一个空账号，或未经验证修改既有身份凭据。关联可信issuer/subject、本地稳定ID、原账号合成资源、邮箱验证和新增密码的所有权；仅显示相同邮箱或新密码可登录不能区分这些分支。

用自有提供方身份与隔离本地账号分析注册前后、验证前后和两种入口的绑定，核对原本受保护资源及产品允许的链接流程。源图开始已登录某Gmail账号，缺独立受害者主体/请求终态，不把它当他人账号已接管的完整证明；不使用真人邮箱或关闭验证页后假定验证已通过。

## 请求hd与可信组织身份

Google OAuth请求里的hd优化账号选择，不是应用组织授权的依据。[Google OIDC文档](https://developers.google.com/identity/openid-connect/openid-connect#hd-param)要求校验返回ID token的hd；并校验签名、iss、aud和exp，以可信issuer/sub关联身份，邮箱域名不能替代组织声明（2026-10-09核对）。

旧图仅显示公司邮箱提示与把hd改成gmail.com后回到redirect_uri的说明，无公司资源/服务端主体结果。用自有测试身份跟到已验证令牌、本地租户资格、邀请/审批和受保护合成能力；正常回调不证明组织边界被跨越。图中scope没有openid，不能把示意URL自动当完整OIDC事务；不登录真实公司或使用图中凭据。

另一旧帖写hd=http://company.com，官方示例值是example.com这类组织域而非带scheme的URL；保留来源写法，不修正为已执行成功的参数。公司邮箱预填截图只证明UI提示，[Google相关参数与令牌说明](https://developers.google.com/identity/openid-connect/openid-connect#hd-param)在2026-10-09再次核读，仍要求可信返回声明与实际应用准入检查，不能以更换提示或自有邮箱进入回调认定绕过。

## 撤销同意后的待兑换code

[原研究者CVE-2020-13294公告](https://security.lauritz-holtmann.de/advisories/cve-2020-13294/)描述GitLab作为提供方时，已有同意后签发的新code尚未兑换，用户撤销应用权限，旧待兑换code仍签出新令牌并恢复授权记录的历史机制（2026-10-09阅读）。攻击视角是持有该客户端兑换能力的服务提供方，不能混作恶意身份提供方。

分别绑定主体/client、code签发/到期/单次消费、撤销代际、兑换时点和新access/refresh/ID token的实际能力；退出本地会话、撤销同意和刷新凭据失效不是同一动作。用自有隔离提供方/客户端的无秘密记录比对正常兑换与撤销后结果，授权列表重现本身不足以证明资源访问。公告为历史版本，不认定当前GitLab仍受影响；未消费原code/token或执行外PoC，旧厂商发布链接现重定向不能当已读原发布正文。

## 错误分支的回调校验与流程图角色

无效scope与修改redirect_uri同时发生时，错误落点改变不能直接归因于scope绕过。[RFC6749错误处理](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.1.2.1)要求无效client/redirect_uri不自动重定向；其他授权错误可回到合法回调，invalid_scope是明确错误类型。分别固定变量，记录校验时点、真正回调、state、code/token或错误参数及受影响业务（2026-10-09核读相关段落）。

授权端点和code兑换的token端点角色不同；书中流程图把兑换请求标为/oauth/authorize，不当真实部署契约。图未画state/PKCE也不证明实现没有；沿实际交易绑定、code一次性/客户端/回调绑定及现有现代安全要求核对，错误页到外域不等于凭据外送或登录接管，不触发真实授权流程。

## 联邦登录缺失邮箱时的本地主体映射

第三方身份没有email字段时，区分字段缺失、null、空字符串、权限未授予和未经验证地址；每一层规范化结果都应关联可信issuer/subject和本地稳定账号ID。两个合法第三方用户都无邮箱，不应仅因相同空值就被映射到同一既有主体；正常创建独立空账号或拒绝该流程可为反例。

在获准隔离的自有身份中核对账号创建/链接顺序、异常回退、会话绑定与合成资源归属；邮箱是辅助属性，不替代受信唯一身份。来源声称ATO但只给一个测试条件，没有完整绑定和终态，不创建/连接他人社交账号或自动申请邮箱权限补证。

## 评论仓库配置与OAuth应用权限

Gitalk配置图列clientID/clientSecret/repository/owner/admin，密钥被遮盖；评论仓库和可初始化Issue的名单是应用配置，不能独立证明认证提供商将令牌限制在该仓库。“GitHub Application”也不足以区分OAuth app和GitHub App；本次未取得Gitalk维护者README，不能据此声称完整实现已核读或所有版本均有同一权限。

[GitHub应用差异文档](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)区分OAuth token的scopes与installation token选择的仓库/权限；[授权流程文档](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps)还要求授权code及相关兑换绑定（2026-10-09核读）。据此核对实际应用类型、公共客户端/后端保密位置、用户同意、scope、组织策略、回调和真实API消费者；clientSecret可见不自动等于已有用户token或全部仓库能力。只分析获准脱敏配置，不重建密钥、搜索真实泄露、发起OAuth同意或调用仓库API。

## 旧授权类型选择图与当前安全要求

旧流程图按machine/user、web/native/browser及first/third party选择Client Credentials、Code、Implicit或Password grant，描述的是历史分类而非当前通用配置建议。先核对token代表的主体、客户端能否保密、实际redirect/code消费者、PKCE及资源权限，不能从“first party”直接赋予输入用户密码的资格。

[RFC9700 §2.4](https://www.rfc-editor.org/rfc/rfc9700.html#section-2.4)禁止使用Resource Owner Password Credentials grant（2026-10-09核读）；历史图不能覆盖该要求。授权类型名只作架构线索，实际漏洞仍需用户/客户端/发起会话/资源之间绑定被破坏的证据；旧图无具体流程缺陷。以当前正式实现与权限文档建立正常对照，不登录提供商、授权应用或索取密码来验证。

## UserInfo声明与ID Token的主体绑定

OIDC简介图把ID Token说成可用access token从UserInfo得到，应纠正消费对象：UserInfo返回用户claims，通常为JSON，协商后也可为签名/加密JWT；JWT外观不使其自动成为ID Token。图右侧/底部裁切未补成完整流程，未保存的讲解不是已核读实现。

[OIDC Core §5.3](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo)要求UserInfo的sub与已验证ID Token的sub严格匹配，失配不能使用这些claims（2026-10-09核读）。区分access token的资源能力、ID Token的认证主体与UserInfo的身份字段，再核对当前issuer/audience/签名/事务绑定和真正账号映射消费者。以获准脱敏事务及隔离自有主体对照，不把能取claims算作接管、不从旧图索取令牌或发起提供商登录。

## 未取得邮箱claim时的手工回填与资格判定

旧线程仅保存步骤6至8：社交授权不给email权限，产品随后要求填写company email并接受任意声明，称资格校验绕过。OAuth认证的稳定subject、provider实际返回且已验证的email claim、手工输入地址及组织成员资格是不同保证；scope未取得email不能让手工字段继承provider验证。

追登录/账号绑定、缺claim分支、地址验证终态、组织映射/邀请与真实授予能力，比较有claim、缺claim后待验证和合法试用三种状态。缺失步骤1至5及当前产品策略不能补成ATO，奖金不补邮箱控制权。优先获准源码/合成身份状态，不登录来源产品、伪装员工、输入真人邮箱或触发验证邮件。


## acr_values请求偏好与实际认证保证

OIDC图仅有authorize请求的acr_values=otp+password和state。[OIDC Core](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest)把acr_values定义为可选、空格分隔的认证上下文偏好，并将对应acr作为Voluntary Claim；请求文字不是已完成OTP/密码或强制二因素的认证结果。

分别绑定RP策略、OP执行的认证流程、实际返回且验证过的身份令牌/上下文，以及最终动作所要求的保证；不能由客户端改请求参数或一张请求图认绕过/安全。缺失/不满足的上下文与普通低保证流程须按权威策略处理，本批没有授权登录或发送OAuth请求。来源：[保存帖](https://x.com/i/status/1407184853255155717)。


## OAuth缺email声明后的自填邮箱和保留地址政策

正文描述去Facebook email scope后应用要求自填邮箱，可填原本禁止的admin地址；截图回信称regression并奖励。注册显示邮箱和拥有邮箱/管理员权限不同。

核对授权scope、身份主键、email来源和verified状态、保留地址政策、验证流程及应用实际角色；同名显示、未验证待激活或仍是普通账号是反例。回信证明个案评语，不给管理员权限收据；只以自有身份设计后续验证。

来源：[保存帖1](https://x.com/i/status/1427343103938088967)。


## OAuth清单按发行传输和消费阶段重排

完整清单图列access/refresh token、code、泄漏、scope、redirect、CSRF、replay、credential等；另一正文把请求body含token直接列问题。

绑定具体协议流、client/issuer/resource actor、redirect精确匹配、state/nonce/PKCE、令牌用途/受众和秘密持有者；协议允许body传token、合法回调、一次性code拒复用或无越权终态是反例。每条类别须有独立入口与对照，不能把token出现本身判漏洞。

来源：[保存帖1](https://x.com/i/status/1431964514631577600)、[保存帖2](https://x.com/i/status/1435899874591928321)。


## 社交登录共享信息提示与真实授权范围

邮件图称登录Rell并共享name and profile picture，可Edit Settings；不是数据库或API响应。

区分consent提示、实际scope、访问token主体/受众及第三方实际字段读取，以自有授权数据验证最小权限和撤销后读者；预期共享、提示邮件或名字头像不是泄漏证据。通知日期不替代当前授权状态，未访问第三方账户或使用token。

来源：[保存帖1](https://x.com/i/status/1441917902391816196)。


## JWT 认证 URL 与 returnto 的重定向链证据

保存 JWT 接管文章的图片只显示含认证值及 returnto 的 GET 和返回同一认证地址的 302。

分别识别 JWT 的用途、接收方和认证状态，记录每跳 Location、最终 origin、允许列表与 URL 解析。返回同一地址并未证明外部跳转、令牌泄露或接管；先区分站内相对地址、错误重试和真正跨信任边界的认证值转发，不保存原始 JWT/cookie。

来源：[保存帖1](https://x.com/i/status/1446745869378744329)。


## OAuth 完整导图的 code grant 与撤销不变量

完整图含code复用/跨client、state、redirect URI/mobile scheme/open redirect/Referer、clientsecret/token、grant错配、refresh竞争及evil app revoke。

逐一绑定授权服务/client、redirect URI、发起会话、code挑战/时效/单次使用、grant与token受众/权限及撤销后状态。缺state字段不单独证明CSRF，回调泄漏需真实读者，race需同资源交错，client字段未显示不等服务未校验。合法scope/受众、绑定拒绝、已撤销和无最终能力为反例；不发真实OAuth授权、抢code/token或竞争刷新。

来源：[保存帖1](https://x.com/i/status/1467027116290043906)。


## 同一第三方主体连接两个本地账号

保存步骤是provider先连account1再连account2，邮件题名为authorization token misconfiguration/3000；未保存redirect/state/token交换。

绑定issuer+稳定sub与本地账号、当前登录主体、连接/断开和重新登录，用自有账号比较正常重复连接策略及最终权益。合法多账号连接、确认旧绑定、被拒或只邮件为反例；绑定冲突不自动token窃取/ATO，不链接真实第三方账号。

来源：[保存帖1](https://x.com/i/status/1473649582034804743)。


## authorization_code 字样与可用授权码

正文建议在JS搜authorization_code，没有保存一次真实授权响应或可兑换材料。

区分参数名、示例配置、静态字符串与绑定client/redirect/主体/有效期的一次性材料；自有fixture只验证消费者和错误/过期/错client对照。关键词或格式匹配、公开示例及绑定正确为反例，不把出现字样叫秘密，不兑换他人代码。

来源：[保存帖1](https://x.com/i/status/1480578354352992261)。


## OAUTHScan 十项检查与协议消费者

正文说扩展含10+OAuth/OpenID检查，图只有仓库卡片；具体规则/版本/结果未保存。

离线自有协议记录client/redirect、state/nonce、code/token绑定与实际分支，合法/错绑定/拒绝对照。工具数、OAuth标签、只UI或无服务端结果为反例；不补出10条未存实现、不安装运行扩展。

来源：[保存帖1](https://x.com/i/status/1491139771607191552)。


## OAuth match replace 响应与服务端身份绑定

保存正文称改变OAuth响应即可绕过，没有授权码交换、token或服务端身份状态。客户端看到成功可以与后台仍拒绝并存。

用自有离线身份状态模型比较正常/失败响应与后续权限读取，分别核issuer、audience、回调/事务绑定、账号映射和会话创建。确认需有原始交换和服务端以不同身份授权的证据；UI成功、伪造本地响应或后端拒绝为反例，不操作真实账号/授权流程。

来源：[保存帖1](https://x.com/i/status/1491460711775617034)。


## Cognito 双池流程图不证明 zero click 接管

两张完整图画login→User Pool/第三方登录→JWT→Identity Pool token exchange→临时AWS credentials→S3，共六步。正文多个zero-click ATO标题，图没有异常账号映射或权限比较。

离线自有身份模型将应用会话、JWT验证/账号绑定、身份池映射/role条件、临时凭据与S3动作逐一关联，比较有效自有身份/拒绝/受限角色。正常流程图、临时凭据存在或宣传zero-click不是越权；权限符合预期、未跨主体为反例，不交换真实token或访问云资源。

来源：[保存帖1](https://x.com/i/status/1493103699262316544)、[保存帖2](https://x.com/i/status/1494993982606045184)。


## 正常 signup 与 OAuth signup 需要同一身份状态比较

正文提醒两入口注册不同，图只有WeakRegistration150奖励。

隔离模型对比新旧账号、verifiedemail、provider subject、tenant、邀请/组织加入以及碰撞处理，保持可验证邮箱归属；入口差异只有在服务端赋予错误身份或权限时才构成漏洞。奖励通知和跳转页面无绑定链，不借OAuth名称推接管。

来源：[保存帖74](https://x.com/i/status/1505045199805812738)。


## 参数污染到授权码泄露标题应分三条信任边

正文只有 pollution→redirect→OAuth code 的文章标题，没有参数顺序或消费者。

离线核各层重复参数的选值、跳转允许规则、code 收件端点和 client/state/PKCE 绑定；拿到 code 还需证明可被正确消费者换取身份。标题不提供三个环节的证据，不补写外链利用步骤。

来源：[保存帖1](https://x.com/i/status/1511638703436976131)。


## 社交登录的可解码字段不等于可信身份声明

正文把 signature 可解码与邮箱修改联系到接管；图仅是社交认证 POST，含 provider、邮箱和 social_media_id。

Base64 解码只还原表示。核发行方证明、签名验证、subject 与本地账号绑定，再确认会话发行及受限消费者。请求中可改邮箱和 provider 不证明服务端信任这些值，也不能由单个请求认定 ATO。

来源：[保存帖1](https://x.com/i/status/1516725879526756352)。


## M2M 客户端凭据交换要保留机器主体

图明确由 client ID 和 client secret 换访问令牌，再访问 API。

这属于机器客户端认证，需核发行方、受众、scope 与 API 授权的实际主体。客户端秘密暴露与签名伪造、用户账户接管分别评估；成功取令牌也不代表令牌具有任意资源权限。

来源：[保存帖1](https://x.com/i/status/1524831867580600321)。


## 第三方登录建议先识别真实信任与主体绑定

保存正文建议应用采用另一服务登录时读取其文档，外链案例全文未保存。先列出实际身份提供方、客户端、用户主体映射、回调消费者与登录状态，区分第三方功能说明和应用真正采用的认证约束。

集成存在不证明账号接管；需要受控账号下实际认证及受保护请求的对应关系，未保存的案例步骤不补造。遵守当前服务与资产范围，不使用真实他人会话或凭据验证。

来源：[保存帖1](https://x.com/i/status/1545812907950309377)。


## 回调 URL 外观与实际 OAuth 接收方分开验证

正文给出 userinfo 中看似目标域名以及在恶意主机路径中放目标域名的候选。先由实际 URL 解析器确认协议、主机、端口和路径，再检查客户端、回调允许名单、授权状态、code/token 的接收方及绑定关系。

字符串含目标域或发生重定向不自动泄露 OAuth 凭据或账号接管；省略协议的片段还可能被当相对路径。使用受控账户与回调地址，分别保留登录前后主体和受保护操作结果，不从历史重复票据数量推断漏洞成立。

来源：[保存帖1](https://x.com/i/status/1549823501603065856)。


## 社交注册和账号链接须核对服务端可信身份

ATO清单建议修改socialsignon的email、去掉scope后手填邮箱、电话号码注册再链接既有邮箱。先区分被签名身份、用户自填资料与经过服务端验证的地址，用自有账户比较验证前后链接及最终登录主体。缺失scope或更改客户端字段不能替代服务器接受证据；检查issuer/sub/verified属性、绑定确认与防重复规则，不推定相同email即可接管第三方账户。

来源：[保存帖1](https://x.com/i/status/1569004089207160832)。


## OAuth外部redirect示意要绑定客户端与实际授权响应

图片的 response_type=token 概念箭头没有真实完整会话。以自有客户端和账户记录注册 URI、输入/解析值、client_id、state、用户同意及实际回跳；验证最终响应是否到达未允许目的地，再分析哪些 token 真被传输。概念图不能证明泄漏；字符串包含或域相似不是精确允许列表校验，不使用第三方 token。

来源：[保存帖1](https://x.com/i/status/1569702446447869953)。


## OAuth 授权响应 回调和资源权限分别绑定

保存帖列 redirect/XSS/CSRF 外链，图画授权请求、code、token 和资源服务器。分别记录 client、callback 实际规范化、state/nonce/PKCE 及会话对应关系，再证明 token 用在何 issuer/audience/资源。URL 跳转、脚本消费和 CSRF 不是一个通用绕过；缺失全文不补写利用，用自有账户确认最终 principal 和获准资源。

来源：[保存帖1](https://x.com/i/status/1575337732183932928)。


## 外部账号改名后绑定以稳定身份和实际权限判断

TikTok/Instagram 摘要称 username 改后 profile 链接未更新。审计 provider 的稳定 subject 与可变显示名/用户名、回收/改名、解绑重绑及缓存更新；用自有 A/B 外部账号确认展示链接与真实授权对象。旧链接不等于新用户继承权限，摘要未给的账号接管流程不能补造。

来源：[保存帖1](https://x.com/i/status/1576064299897872384)。


## OAuth 同意、scope、token 受众与资源权限是不同决定

保存 AAD/Graph 图分开 owner→client 同意、授权服务器发 token、client 向资源服务器携带 token 与 API 暴露 scope。审计自建客户端的同意主体/租户、token 类型/受众/有效期与资源侧实际操作权限，在自有对象上比较正确/错误受众及无权限场景。示意拓扑不证明帐号喷洒、外传或后门能力，scope 字符串和收到 token 不能替代资源授权，不使用归档凭证或执行工具。

来源：[保存帖1](https://x.com/i/status/1591056776060968962)。


## Facebook 账号绑定的 userid 与 oauth token 必须属于同一主体

保存请求形状为 oauth={token}&userid=本账号&email=本邮箱，帖文建议替换 userid。应核验服务端如何从 token 取得外部身份并与当前登录主体、目标本地账号和绑定意图交叉验证，不能只相信客户端 userid/email。用两个自有账号比较绑定前后身份与后续登录/解绑状态；一次请求通过不等于目标身份已经被控制。

来源：[保存帖1](https://x.com/i/status/1593855309855870976)。


## API 清单的 redirect、state 与 scope：字段存在不代表绑定

1595046632894111745-02.jpg 列 redirect_uri 服务端校验、code 响应、state 与 scope。提炼为每个值与客户端、浏览器会话、授权请求和目标资源绑定的核验矩阵；白名单字段存在仍需检查精确匹配和规范化，state 需实际校验而非只生成，scope 需授权端及资源端共同限制。历史清单不构成当前标准全文，不从图片推出整个实现安全。

来源：[保存帖1](https://x.com/i/status/1595046632894111745)。


## 历史保存帖0152：OAuth 回调与状态逐个边界核验

图列出开放重定向回调、路径规范化、伪子域、HTML/referrer、state 和 client_secret。逐项建立客户端注册→请求会话→规范化后的回调源→代码/令牌实际交付→兑换约束链；state 缺失/改变需证明会话或身份绑定失效，泄漏需证明数据确实到达自有接收端及密钥用途。不能由参数名称或假域示例推定账户接管，不使用图中的任何凭据。

来源：[保存帖1](https://x.com/i/status/1598398060509683712)。

已实际查看保存图片 `1598398060509683712-02.jpg`：OAuth 图列出回调开放重定向、路径规范化、伪子域、HTML/referrer 泄漏、state 和 client_secret。须分别核对注册客户端、会话绑定、最终回调源、实际令牌交付和兑换约束；图本身没有当前目标复现证据。


## 历史保存帖0152：外部身份解除关系与登录授权状态

身份关系被删除、外部提供商令牌被撤销以及本应用会话失效是三个状态。历史解绑报告可用于画出绑定→登录→解绑→旧会话操作的状态机，核对每一步的账户、provider、client 和重认证时间；界面显示解绑不证明登录凭据吊销，重新绑定必须有独立授权依据。

来源：[保存帖1](https://x.com/i/status/1598417119221276676)。

已实际查看保存图片 `1598417119221276676-02.jpg`：Shopify 外部 Google 身份解除绑定后既有会话仍可操作的历史报告。前提为先取得账户访问并绑定身份；解除绑定、会话吊销、再次绑定的权限与重认证应分别核验，不能将此前提链当作初始接管。


## 重定向 URI 多层编码需逐层标注解析结果

OAuth 幻灯片展示编码路径、点段和 fragment 中 code 的候选。将注册校验、URL 解码、代理路由、应用跳转、浏览器最终 origin/query/fragment 分开记录；各层记录原始字节与解析后的值。在自有客户端和回调地址比较单次/二次解码，核查 client、state、精确目标绑定以及授权结果是否被预期客户端消费。幻灯片中的字符串不证明 code 泄露、可兑换或通用平台缺陷。

来源：[保存帖1](https://x.com/i/status/1604266196312162304)。

已实际查看保存图片 `1604266196312162304-02.jpg`：OAuth slide redirectURI百分号双编码/点路径，最终展示fragment里的Facebook code与开放重定向；未见注册client/session绑定/实际转发。提炼每层解码/路由规范化、query vs fragment、最终源和兑换约束，不能由slide认定真实代码泄漏/接管。。


## user_oidc 的 HTTP provider 配置先审查谁能设置和秘密如何传输

截图显示容器/管理配置中 provider URL 及 client secret，秘密传输结果未完整保存。追踪具有配置权限的主体、允许的协议、实际 token/discovery 请求及传输中使用的秘密，用自有 provider 和合成秘密比较 HTTP 被拒绝或允许的路径。区分管理员明确配置不安全端点、低权限能改配置和系统静默降级；报告中的规范引用不等于已阅读完整规范。不得由配置截图直接推定真实生产秘密已被截获。

来源：[保存帖1](https://x.com/i/status/1604445845449048066)。

已实际查看保存图片 `1604445845449048066-02.jpg`：Nextcloud user_oidc历史报告自有docker安装、管理员添加http provider/client_secret，支持明文传输配置风险线索；图下实际capture裁切。核对真实请求URL/transport/认证secret消费、配置者权限和策略，管理员可配置前提不是任意用户泄漏，不将报告引用规范当已读正式规范。。


## 设备码授权审查绑定发起客户端与用户所见目的

QR/MFA 更新邮件只是设备授权诱导示意。记录请求设备码的客户端、租户、scope、码有效期、待授权身份与用户实际确认的信息；检查用户是否可辨别此次授权的应用和用途，授权结果回到哪个请求者。仅在自有测试客户端/身份做正常与取消授权对照，不扫描保存 QR 或复用现存码。合法登录域名与完成 MFA 都不自动证明用户授权给了预期客户端，工具名也不等于已存在平台认证漏洞。

来源：[保存帖1](https://x.com/i/status/1605582504601296898)、[保存帖2](https://x.com/i/status/1605923805519806464)。

已实际查看保存图片 `1605582504601296898-02.png`：Squarephish邮件示意MFA更新QR及Microsoft deviceauth链接，没有认证票据/真实主体流程；设备码与发起客户端、用户授权、scope/tenant/session必须明确，不发送钓鱼邮件不扫描QR不使用现存码，防误授权审查。。


## open redirect 链需要实测授权结果在哪一跳交付

图把 return_to、redirect_uri 和 CDN 跳转连到盗 OAuth token，未给最终授权响应。在自有客户端记录每跳 origin、query/fragment、浏览器导航、state、client、PKCE/受众及结果消费者；比较固定允许回调与不可信回调被拒绝的路径。跳转可达不等于 code/token 泄露且可兑换，范围排除也不因高影响标题失效；每个桥接条件必须有实际链证据。

来源：[保存帖1](https://x.com/i/status/1606630820671897601)。

已实际查看保存图片 `1606630820671897601-02.jpg`：Openredirect→OAuth token宣传图return_to/callback组合，只有构造URL未展示最终code/token流；记录每跳origin/query/fragment/client/state/PKCE+实际受众，不因跳转自动ATO，不把inscope规则从标题绕开。。


## XSS 后的事件与 OAuth 链需要实际授权回流

保存帖把 HttpOnly、改邮箱需当前密码与 OAuth+event listener 联为“最容易 ATO”，但未保存监听类型和授权流程。分别证明现有同源脚本原语、客户端/租户/scope、用户实际授权、事件来源/接收者、票据用途与最终权限；若为消息事件，还要校验 origin/source/schema，不能将任意监听当已收到有效 token。HttpOnly 与重新认证仍各自有边界，一条 XSS 或 token 可读不自动绕过它们。仅用自有客户端/会话和无敏感回流标记，不获取他人票据或自动发授权请求。

来源：[保存帖1](https://x.com/i/status/1612008867143057409)。


## GHES App scoped token 提权摘要要求已有安装权限

保存摘要要求拥有安装 GitHub App 的管理权限，风险是受限 user-to-server token 被错误授权为管理员/组织Owner，不能提炼为匿名提权。用自有实验组织区分安装者角色、App permissions、token scopes 和目标组织/操作权限，对照受限token、原用户token与撤销后token的同一无害操作。确认越过声明scope才成立；用户本来有权不证明token限制正确。3.3.17/3.4.12/3.5.9/3.6.5及CVE-2022-23741只保留历史信息。

来源：[保存帖1](https://x.com/i/status/1613909344872964096)。

已实际查看保存图片 `1613909344872964096-02.jpg`：GHES scoped user-to-server token提权；先有admin安装App权限，历史修复3.3.17/3.4.12/3.5.9/3.6.5；CVE-2022-23741摘要，非匿名提权。


## 授权请求字段与服务端授予能力分开审计

截图包含 authorize 的 clientId、PKCE S256、scope、nonce 和 cookie，正文强调服务端验证 token；未保存取得管理员能力的响应。先确定令牌类型和服务消费者，再核对签名/有效期、发行者、受众、绑定客户端及实际授权范围；不同令牌类型的校验要求不能混用。请求 scope 字符串或本地改 token 不改变已授予权限，PKCE 也不能代替资源端的对象授权。使用自有应用与账户检查允许和拒绝两侧。

来源：[保存帖1](https://x.com/i/status/1616479259123384332)、[保存帖2](https://x.com/i/status/1618661631189450752)。

已实际查看保存图片 `1616479259123384332-02.jpg`：OAuth authorize含clientId、PKCE S256、scope、nonce及cookie等截图，未见response/admin功能；scope字样非已授予，不重用会话。


## GitHub App 的仓库 scope 与组织 Project V2 权限分离

保存摘要描述 Scoped-User-To-Server token 可操作 GraphQL 组织用户/项目等非仓库资源，同时明确仓库内容、issues/pulls 不受同一问题影响。历史摘要标为 CVE-2022-23739，并列修复版本 3.3.16/3.4.11/3.5.8/3.6.4/3.7.1；这些是保存材料的版本条件，不代表当前状态。用自有组织与应用分别验证资源类别、实际授予 scope、成员角色及允许/拒绝操作，不能从仓库 scope 推断组织项目完整权限，也不把它混同其他 GitHub App CVE。

来源：[保存帖1](https://x.com/i/status/1618657787541602307)。

已实际查看保存图片 `1618657787541602307-02.jpg`：GHES App GraphQL org非repo资源无scope也可改users/projects；repo内容/issues/pulls明确不受影响；历史fix3.3.16/3.4.11/3.5.8/3.6.4/3.7.1 CVE23739。


## OAuth 授权说明与页面身份认证标题分开

正文自身定义 OAuth2 为客户端代表用户访问资源的授权框架，封面却写 Authentication。审计时分别确认资源 token 的受众/scope、当前主体和应用需要的身份认证断言，不由一个 access_token 自动赋予登录或对象权限。用自有应用和账户比较允许/拒绝能力，身份关联要求稳定 subject 及已验证来源；保存内容只是定义，没有完整实现或攻击，不把授权框架名称当安全证明。

来源：[保存帖1](https://x.com/i/status/1621068045191102466)。


## 跨第一方登录流的主体与会话状态逐步绑定

保存 FB/Meta/Oculus 链以 FB 已登录、Oculus 未登录开始，提到 logout/login CSRF 再走第一方 OAuth。记录每个 origin 的会话、发起者、预期账户、subject、state 与实际授予 token，用两个自有隔离账户比较账户混淆与正常关联。退出、登录成功和接管能力是独立终态，截图没有原始请求及完整账号效果，不能从第一方标签或现有会话推出授权，不重放保存 app_id 或登录真实账号。

来源：[保存帖1](https://x.com/i/status/1621153968930934784)。

已实际查看保存图片 `1621153968930934784-02.jpg`：保存Meta/FB/Oculus链：FB已登录Oculus未登录，logoutCSRF与loginCSRF起点，OAuthresponse_type=token nestedredirecturi，称token进forums.oculusvr/openredirect#access_token再漏ysamm；fragment不随HTTP，须真实DOMrelay/navigation/message消费者和subject/tokenaudience绑定，URL显示oculus.com/oculusvr变更/步骤无实际请求，勿重放appid/泄token/登录真实账号。


## 嵌套 redirect_uri 与 fragment token 的转交链单独核验

同图为 response_type=token、内外 redirect_uri，称 fragment token 经论坛 openredirect 外泄。逐跳记录解码、准确 scheme/host/path、预期客户端、URL fragment 的真实读取者与导航/message 转交；fragment 不会仅因普通 HTTP 请求就传给服务器。截图的 oculus.com 与 oculusvr.com 还发生变化，没有 DOM relay/完整交换；用假 token 和自有 origin 验证拒绝条件，不将 URL 展示等同真实泄漏、复制第一方 token 或推断当前可利用。

来源：[保存帖1](https://x.com/i/status/1621153968930934784)。


## Rooms 无权限成员启动 calendar OAuth：init 与授权效果拆开

保存 8x8 历史摘要给出 /meet-external/spot-roomkeeper/v1/calendar/auth/init 和指向 rooms/add 的 successRedirectUrl，嵌入页同时提示没有 Rooms 权限。启动 OAuth、得到跳转或返回页面只代表流程入口；应检查 state/会话/用户/tenant 绑定、callback 接受及最终 calendar/room 授权对象。以有效管理员和无权限成员对照，只有受限成员成功绑定本不允许的凭据或创建受保护对象才能说明权限问题。图未显示完成 grant/callback 或最终状态，不能把 init 可达认定为 OAuth 接管。

来源：[保存帖1](https://x.com/i/status/1625767090815700995)。

现有图片证据 `1625767090815700995-02.jpg`：无 Rooms 权限成员可启动 calendar OAuth 的历史报告：GET /meet-external/spot-roomkeeper/v1/calendar/auth/init，successRedirectUrl 指向 rooms/add；页面同时显示无权限，未展示授权完成或实际房间创建。


## 移动 deeplink 授权码劫持须闭合 PKCE 兑换绑定

Shop/Outlook历史摘要说明恶意app同自定义scheme可截取code，工程师加PKCE缓解。检查callback路由的唯一/验证关联、state与发起会话、code challenge/verifier、client/redirect绑定及一次性消费。只有得到code且能兑换并访问正确主体资源才支持接管；看到URL或注册同scheme不自动足够。历史Low3.7/900与报告总结不证明当前App仍有问题。

来源：[保存帖1](https://x.com/i/status/1631414207223672832)。

现有图片证据 `1631414207223672832-02.jpg`：Shopify Shop/Outlook历史摘要称恶意app可截取自定义deeplink授权code，工程师加PKCE缓解；依赖callback劫持与code兑换，普通URL可见不等于可兑换。


## Google hd 选择提示必须与组织授权解耦

改OAuth URL的hd参数可能更改账号选择提示，hd不是可信授权输入。服务器须核对可信IDtoken签名、issuer/audience/nonce等与组织hd声明及本地成员规则，在自有不同组织账号比较登入后角色/tenant。允许选择任意邮箱或提示后缀变化不等于组织权限绕过；缺后端授权结果不定ATO。

来源：[保存帖1](https://x.com/i/status/1634541690655481857)。

现有图片证据 `1634541690655481857-02.jpg`：GoogleOAuth图建议改hd URL参数绕过公司域提示；hd选择提示不是授权，必须服务器验证可信IDtoken签名、issuer/audience及组织hd声明，不能依email后缀或请求hd授予组织角色。


## MFA、OAuth 配置与账户占位用身份生命周期判别

正文仅记录2FA报告被改为OAuthMisconfiguration/AccountSquatting，缺具体流量。复核注册标识验证、既有账户关联、外部发行者主体、MFA前后会话和最终受保护动作，保留每项实际前提。标签争议不证明绕过或接管，不能补出未保存的流程。

来源：[保存帖1](https://x.com/i/status/1638063949269573632)。


## 授权码泄漏链在 redirect 路径与统计消费者分别闭合

pixiv图通过redirect_uri路径规范化到攻击者商品页，再由其GA配置获取query中的code。审计回调精确匹配与解码/规范化顺序、页面控制权、统计/Referer数据，以及code客户端绑定、一次性/过期/PKCE与交换权限。code出现不自动可兑换或ATO，High奖励是历史个案，不访问历史链。

来源：[保存帖1](https://x.com/i/status/1638480902765379584)。

现有图片证据 `1638480902765379584-02.jpg`：pixiv OAuth redirect_uri路径../到自有booth商品页再GA query泄漏authorizationcode；需redirect规范化与白名单/页面控制/令牌交换PKCE状态完整链，High历史不当通用ATO。


## OIDC state 错配响应泄漏预期值破坏保密边界

Nextcloud历史摘要callback比较会话state，错配JSON却回显expected state/debug leftover，CVE-2023-28848；ID4ME明确未测试仅近似代码假设。审查state绑定会话/发行者/期限/一次性及错误分支输出，用自有会话确认泄漏，再独立证明跨站可读/重用与最终登录主体。不能由源码相似写成ID4ME已复现或直接ATO，不补实际攻击链。

来源：[保存帖1](https://x.com/i/status/1643176933205721089)。

现有图片证据 `1643176933205721089-02.jpg`：Nextcloud OIDC摘要：callback state与会话值比较，错配JSON响应竟包含expected state/debug leftover；引用CVE-2023-28848及LoginController行336–344。ID4ME明确未测试仅代码近似假设；泄漏需浏览器跨站读/会话绑定/复用证明，不补成ID4ME已复现。


## OAuth 登录 CSRF 检查的是发起会话到回调的绑定

缺 state 或 PKCE 的帖子给出候选，应审查 authorization request、issuer/client/redirect、登录发起会话、返回 code/state 及 verifier 的关联。state 缺失不能单独证明 CSRF，PKCE 与 state 的目的也不完全相同；按实际实现找替代绑定与反例。仅在两个自有会话中比较错误发起会话的回调是否拒绝，不补造未保存 Gist 或真实账号接管。

来源：[保存帖1](https://x.com/i/status/1655853354390548480)。


## 共享 Okta 应用标识仍需校验各信任边界

两个域名使用同一 Okta app ID 只能提示相关登录配置。分别绑定 issuer、client、注册 redirect URI、租户、cookie origin、state/nonce 与最终应用会话，比较自控正常/拒绝回调。应用 ID 一致不证明 SSO 绕过，也不能自动把另一域或组织纳入 scope，未有真实流转响应不推账号接管。

来源：[保存帖1](https://x.com/i/status/1661518077710807043)。


## SSO 清单落到协议、身份与会话不变量

20项图涵盖认证发放/校验、token 修改/过期/吊销、CSRF、角色授权、会话固定、单点登出、SAML、协议互通、错误、IdP/SP、MFA、传输、身份映射、超时、头和扫描。按实际 OAuth/OIDC/SAML 流程选择条件，为每项定义合法/拒绝对照与保护结果；单点登出按部署策略核对，并非任意 token 应同时失效。清单不是20个漏洞或已测试证据，不运行泛化扫描。

来源：[保存帖1](https://x.com/i/status/1662072472622223361)。

保存图片 `1662072472622223361-02.png`：20项SSOchecklist auth/token校验到期吊销CSRF授权会话singlelogoutSAML协议错误IdPSPMFAtransportidentitymappingtimeoutheadersscannerpentest，要协议-specificexpectedproof不是20漏洞。本段仅使用实际查看的保存原图，不补未保存内容。


## Expo return URI 状态污染需绑定合法登录交易

两图显示正常移动登录经Expo/Facebook回到应用scheme，以及攻击示意先污染ru/returnUrl再让后续token去外域。审查大小写/URL规范化、allowlist、租户/应用、cookie/state、回调与发起交易绑定，以自有正常/拒绝URI逐跳比较。图是流程示意而非当前真实抓包；Facebook许可与最终token消费者不能省略，不推广所有使用Expo的站点或交换真实token。

来源：[保存帖1](https://x.com/i/status/1663553348119801857)。

保存图片 `1663553348119801857-02.jpg`：Expo exploit图混合大小写returnUrl保存ru外域，后续FBtoken到auth.expo.io再发attacker fragment/query，污染会话callback状态绑定示意未真实抓包。本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1663553348119801857-03.png`：正常mobileExpoFB回调图ru codeacademy scheme expoauthsession channelcode token，两图可对比合法returnURI/租户/app/session绑定；URL图不证全部站受影响。本段仅使用实际查看的保存原图，不补未保存内容。


## CASB integration 创建校验委托租户归属

保存公开摘要支持历史 Cloudflare CASB 问题：Microsoft tenant UUID/domain 或 GitHub installation_id 已被另一客户集成时，攻击者可据这些标识建立新 integration 并显露敏感信息。以自有双租户校验调用者、授权委托、目标租户和安装归属，再检查创建后数据消费者。租户标识可公开，不应视为持有即授权；摘要中的阻止同 tenant 重复 integration 是历史修复描述，不能单独替代归属证明。Critical/Resolved 页面不证明当前全部集成都可利用。

来源：[保存帖1](https://x.com/i/status/1666377394976964608)。

保存图片 `1666377394976964608-02.jpg`：Cloudflare CASB公开摘要：若枚举到已经集成的Microsoft tenant UUID/domain或GitHub installation_id，可新建integration露出敏感信息，修复阻止同tenant多integration。结果页面Critical9.7/3300/Resolved；核心租户归属和委托授权，公共tenantID非secret，不能以阻止重复单独代替所有权校验。本段仅使用实际查看的保存原图，不补未保存内容。


## OAuth2控制器不能遗漏失败认证预算（2023保存案例）

Nextcloud OAuth2 API controller缺失暴力保护历史CVE2023-39958，图仅标题/摘要链接/时间线，没有具体参数或重试预算。可提炼同类认证入口保护覆盖检查，不能补造速率、成功token或无认证绕过。

图片证据：`1689547486216765440-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689547486216765440)。


## 客户端 ID 与 secret 的用途及暴露等级（0187）

发现 `client_id` 或 `client_secret` 后，先识别它是否属于 OAuth、客户端类型、预期公开程度、服务端信任与实际权限。ID 通常是标识符；名为 secret 的示例值或无效值也不证明凭据泄露。以脱敏配置和合法测试客户端的最小对照证明用途，避免使用泄露值登录、兑换令牌或扩大权限。

来源：[保存帖1](https://x.com/i/status/1690854487164887040)。


## 保存图证0188-36-oauth：机制与验证条件

Nextcloud user_oidc CVE-2023-39953说明token issuer须匹配discovery issuer，与aud检查类似；作者明确没有OIDC环境验证且其他问题未核实，MITM影响仅声明。需受控两个issuer配置/签名/aud/iss对照，不能把代码意见视为已实现攻击。 可用原图：`1694379121743376845-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1694379121743376845)。


## 保存图证0188-37-oauth：机制与验证条件

Nextcloud CVE-2023-39954区分公开client ID与私有client secret，明文DB快照读取可导致服务端冒名；secret需要原值不能简单hash替代，需独立密钥加密静态存储及DB/应用权限边界。截图没有实际DB或冒名请求，不推导远程任意读取。 可用原图：`1694379251800346716-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1694379251800346716)。


## OIDC issuer 与客户端 secret 的两条信任边界（0188）

对 ID Token 验证签名、issuer 与 discovery 的精确关系、audience、nonce 及时间条件；使用两套受控 issuer 的正反例，不由代码意见补造 MITM。client ID 可公开，client secret 往往需要原值完成客户端认证，不能用普通哈希简单替代；静态加密还需密钥独立存储与数据库读取权限边界。只读 DB 快照泄露与远程任意账号接管分开证明。

来源：[保存帖1](https://x.com/i/status/1694379121743376845)、[保存帖2](https://x.com/i/status/1694379251800346716)。


## 保存正文0190：ping斜杠变体与OAuth入口的授权边界

正文/ping为OK、/ping/进入登录页及dummy Google账号可访问的声称。路径路由差异与登录后成员授权是两个假设；对照原始路径、代理重写、OAuth回调与实际业务资源。自有外部邮箱、获准域邮箱及未验证邮箱分别检查email_verified、受允许域、组/租户绑定和会话后端授权。登录UI或健康端点可达不构成绕过，图片OAuth2Proxy版本是历史上下文，不能补造回调参数。

来源：[保存帖1](https://x.com/i/status/1701084616663114149)。


## 保存图证0190-14-oauth：机制与验证条件

保存原图文件：1701084616663114149-03.jpg。

/ping/ 登录界面有OAuth2 Proxy versionv7.1.3和SigninwithGoogle；正文/ping=OK与/ping/面板路由差异，以及dummyGoogle能访问声称需分层。尾斜线仅表明不同路由，登录按钮不证明访问已获准；用自有授权账号确认email_verified、允许域/组/角色与真正上游受保护请求，比较原ping/尾斜线及未授权身份，界面版本不自动CVE或ATO。

来源：[保存帖1](https://x.com/i/status/1701084616663114149)。


## 保存图证0190-124-oauth：机制与验证条件

保存原图文件：1703755898131558417-02.jpg。

Cloudflare CASB报告2086301：删除的GitHub/Box installation_id或Microsoft tenant UUID/domain曾被合法连接，攻击者知道标识后可在自己账户重新添加并接触旧集成findings。机制为删除后授权/资源归属绑定未重新验证的confused deputy；跨两个自有租户做连接→删除→异租户重连和重新同意对照，检查服务端授权、旧凭据及数据生命周期。平台限定少量集成，调查未发现研究者账号外的数据影响；不可把公开UUID本身称秘密或推断全部客户受害。

来源：[保存帖1](https://x.com/i/status/1703755898131558417)。


## 保存图片中的机制与证据边界（1705220586329563554-02.jpg）：by-type/oauth-oidc.md

图片 `1705220586329563554-02.jpg`：Nord2049021手动连接服务凭据需邮箱验证的流程；GET /oauth2/auth?redirect_uri=...callback&id_token_hint=...把include_granted_scopes从1改0被声称绕过。参数不是邮箱验证事实本身；需比较原始/修改授权范围、回调身份和后端是否真实给未验证账号服务凭据，防止仅UI变化/旧完整会话。不保存id_token_hint/凭据，图底部截断未显示最终返回；不能泛化所有OIDC服务。

来源：[保存帖1](https://x.com/i/status/1705220586329563554)。


## 保存图片中的机制与证据边界（1707334475741635032-02.jpg）：by-type/oauth-oidc.md

图片 `1707334475741635032-02.jpg`：Mattermost 1502099/CVE-2023-1421 文字列出 OAuth complete 路由，base64 state 的 redirect_to 进入输出的候选；图中本地 GitLab 登录启用与 mobile action 是前提，截断部分没有实际弹窗。分别验证 state 的会话绑定及 redirect_to 的输出上下文编码；无效 code 错误分支、CSP、实际浏览器执行须单独记录，base64 不提供完整性。

来源：[保存帖1](https://x.com/i/status/1707334475741635032)。


## 0194：白名单检查和实际 token 发送目标必须一致

GitSourceEditor 图文描述先用 new URL(a).origin 校验，再对整个 URL 使用正则抽取 host/project/file；合法 googlesource origin 的路径/fragment 可让后续组指向另一 host。追踪规范化 URL、正则组、最终 fetch URL 与 token 附着范围，比较含伪 host 的路径及正确主机。只对自有 client/身份确认最小作用域，不把浏览器白名单字符串当实际 authority；图片提到 Gerrit/Android 相关权限，不能推断全 Google 或内网资源接管。

来源：[保存帖1](https://x.com/i/status/1716824364455280844)。


## 0194：取得用户 token 与目标 client 校验是两个边界

保存流程图区分授权 code 与 access token，并声称给 TimePlanner 签发的 token 被另一登录应用接受。provider /me 返回用户资料并不足以证明受众正确。自有身份和两个受控 client 比较 issuer、app_id/audience、expiry、会话绑定、code 一次性及 subject/email 映射；图中 auth 请求/200 是片段，须额外绑定 token 所属 client 和目标实际自有账号。应用所有者可取得本应用授权 token 不代表可以用于别的应用或他人账户，token 值不转录。

来源：[保存帖1](https://x.com/i/status/1717949393985573318)、[保存帖2](https://x.com/i/status/1717975703923429609)。


## 保存图证0194-4-oauth：1714650037718749438-02.png

OAuth AuthorizationCode图Browser→Server→IdP返code→server兑换accessToken→profile→数据；将OAuth当认证省略state/redirectURI/client/PKCE及IDtoken校验。标清code/token/subject各角色，绑定会话与client，错误code/其他client token对照，图非安全实现证。

实际保存图：1714650037718749438-02.png。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1714650037718749438)。


## 保存图证0194-92-oauth：1716824364455280844-02.png

GitSourceEditor先newURL(a).origin白名单但再regexexec全URL捕host/project/file，合法android.googlesource origin中path/fragment嵌攻击host1337#.googlesource.com，regex组可导请求到其他host携access_token。分别验证浏览器authority与应用regex组/实际fetch目的、令牌传输；合法字符串子串不等最终host，修核canonicalparsedhost及credentials限定。

实际保存图：1716824364455280844-02.png。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1716824364455280844)。


## 保存图证0194-92-oauth：1716824364455280844-03.png

edit.chromium.org/edit file/repo URL操纵路径%2E/编码片段给PoC1337/1338；须已AndroidBuildTeamOAuth授权或用户grant，HTTPSPoC更新ChromiumGerritAboutme显示token权限，图无live结果。被授trust app不等token可发任意host，不推整个GoogleATO；自有账号只最小scope回读且不运行保存server。

实际保存图：1716824364455280844-03.png。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1716824364455280844)。


## 保存图证0194-92-oauth：1716824364455280844-04.png

GitSourceEditor泄scope列email profile openid gerritcodereview androidbuild.internal，正文测试profile/repo读写而内网权仅assume/不清楚，其他editor只是may，pluginMode不OAuth尚未找到利用但enable-gis可强制候选。按真实scope/账号entitlement/过期revocation限制影响；假设内库/供应链不当已证全Google接管。

实际保存图：1716824364455280844-04.png。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1716824364455280844)。


## 保存图证0194-130-oauth：1717949393985573318-02.jpg

正常 Facebook 登录示意图是 relying party 请求 code，用户向 Facebook 取得供 Grammarly 使用的 code，再 POST facebook_login.code 给 auth.grammarly.com。示意图不是抓包，也不展示错误配置；服务端交换 code 应绑定 client、redirect URI 与发起会话、一次性和时效，区别 access token 登录协议，不能从 code 字段推定 token 未校验。

实际保存图：1717949393985573318-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717949393985573318)。


## 保存图证0194-130-oauth：1717949393985573318-03.jpg

Bukalapak 示意图声称给 YourTimePlanner 客户端签发的 Dan token 被另一应用接受并登录 Dan，体现跨 client/audience 的 token substitution。需要在自有测试身份与两个受控 client 中比较正确、错误 audience/client、issuer、expiry，并检查 provider 可信验证与 subject 映射；图片为概念流程没有实际请求响应，不等于已证明接管现实账户。

实际保存图：1717949393985573318-03.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717949393985573318)。


## 保存图证0194-131-oauth：1717975703923429609-02.jpg

OAuth 示意图画出 Facebook 把 token 放在回跳 URL fragment，前端读取后由 Randomsite 请求 graph /me 获得 email。fragment 通常不作为 HTTP 请求传给服务端，需区分前端采集、后端转发与 provider 校验。查询 /me 只证明 token 关联用户，不自动证明 token 是给此 client；需绑定 issuer、client/audience、会话及 email 的验证语义。示意非抓包，secret123 是图中占位标记。

实际保存图：1717975703923429609-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717975703923429609)。


## 保存图证0194-131-oauth：1717975703923429609-03.jpg

Vidio 正常登录示意把 token 明确标为给 Vidio client 92356，再由 provider 返回 Dan email。应验证 token 受众而非只相信客户端传入的 email 或用户 ID；对照正确 client 与另一受控 client，当前图片没有真实校验响应或服务端实现，不能证明实际 Vidio 当时的缺陷。

实际保存图：1717975703923429609-03.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717975703923429609)。


## 保存图证0194-131-oauth：1717975703923429609-04.jpg

TimePlanner 所有者通过自己应用的正常用户授权取得供该应用使用的 token，图示 token 来源与跨应用误接受是不同边界。用户为某 client 同意授权不代表同意用于另一应用登录或真实账户测试；仅用自有身份和受控 client 建立受众替换对照，不收集他人的 token。

实际保存图：1717975703923429609-04.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717975703923429609)。


## 保存图证0194-131-oauth：1717975703923429609-05.jpg

拼图显示 POST /api/facebook/auth 提交 fb_access_token，并截取 200 与 X-Auth-Tokens 返回，图注声称来自 TimePlanner 且登录为 Dan。凭据与会话 token 不应转录；200/返回会话是证据片段，仍需脱敏请求、provider app_id/audience 证明、目标登录后自有账户 ID 及错误 client 被拒绝的对照，图片不独立证明全量身份接管。

实际保存图：1717975703923429609-05.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717975703923429609)。


## 0195：跨应用 token reuse 需证明 issuer 与受众

正常 code 图、TimePlanner token 流程、Grammarly 登录响应/页面是不同证据层。自有身份与两个受控 client 核 token issuer、provider app_id/audience、subject、expiry 和会话绑定，再比较错误 client 被拒绝及目标自有 userID。/me 返回用户资料或 Set-Cookie 不自动证明受众正确；不能从图推广到所有热门 app，真实 token、邮箱和会话值不转录。重复已阅图当前文件 1719723468999057679-03.jpg 与 1717949393985573318-02.jpg 哈希一致，内容是 Grammarly facebook_login.code 的正常流程，并非 access_token 缺校验的抓包。

来源：[保存帖1](https://x.com/i/status/1719723468999057679)。


## 保存图证0195-3-oauth：1718296707270951405-02.jpg

Mozilla oauth/authorize报告截图给redirect_uri的%0d%0a候选，并声称无需授权可改headers，截图响应HTTP/2 302、location部分在下方裁切，未展示新header完整行。要追踪参数解码、框架header序列化与线上协议转换，普通Location反射/编码文本不等CRLF拆分；用自有无害header名对照记录原始HTTP/1或有效HTTP/2头，不能推Set-Cookie生效或ATO。

实际保存图：1718296707270951405-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1718296707270951405)。


## 保存图证0195-29-oauth：1718935705873686869-02.png

Auth0截图是scope字符串，含client_grants/users/keys/connections/rules/roles/actions/tenant_settings等读写。作用域清单不证明token来源、签名、audience、有效性、所属tenant或实际可用权限；建立泄露来源→服务端校验→自有受控资源最小读取→实际entitlement对照，不能据critical题名断言任意管理/接管，不转录token。

实际保存图：1718935705873686869-02.png。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1718935705873686869)。


## 保存图证0195-70-oauth：1719723468999057679-02.jpg

TimePlanner所有者取得为其client签发的正常授权token示意，独立hash不同排版；合法本app授权不代表他人或其他client登录授权。两个自有client用issuer/app_id/audience/subject/expiry做替换对照，不收集他人token或以图说所有app可接管。

实际保存图：1719723468999057679-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1719723468999057679)。


## 保存图证0195-70-oauth：1719723468999057679-04.jpg

Grammarly拼图POST /api/login facebook_login.access_token，响应grauth/csrf-token cookie与user字段，图注明TimePlannertoken，敏感值不转录。SetCookie+user字段是片段，需providerapp_id和目标自有userID及错audience拒绝对照证明跨client误接受；cookieSecure/HttpOnly/SameSite与tokenaudience缺陷无互相替代关系，截图不能推出所有账户/应用受影响。

实际保存图：1719723468999057679-04.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1719723468999057679)。


## 保存图证0195-70-oauth：1719723468999057679-05.jpg

Grammarly登录UI显示邮箱与Secretdocument卡片，图注connectedDan；它是登录后页面片段，无文档正文/编辑结果或token受众。关联自有userID、正常/错client与文档访问权限比较；标题/卡片不能证明读取秘密或全账号接管，遮盖真实邮箱和session信息。

实际保存图：1719723468999057679-05.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1719723468999057679)。
