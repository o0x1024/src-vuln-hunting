# CORS 跨源读取

适用信号：API 返回 ACAO/ACAC 或允许不可信来源

## 检查与最小实验

先选有明确私密性要求的自建资源。检查完整 origin（协议、主机、端口）的匹配，及动态反射、后缀判断、null origin 的真实可达条件。然后从受控外源页面发起请求，在默认浏览器策略下观察 JS 能否读取私密标记。

保留预检与实际请求、cookie 策略、凭据模式和读取结果。不要关闭浏览器安全策略来制造“跨域成功”。不可信页面没有权限获得 Authorization 时，不能在手工 curl 中添加它替代攻击可行性。

## 证据与反例

`Access-Control-Allow-Origin: *` 配合凭据请求会被浏览器阻止读取，不能仅凭它和 `Access-Control-Allow-Credentials: true` 报窃取。公开 API 的跨源读取可以是设计。Vary 缺失只是缓存线索，跨用户复用需转 [缓存投毒](cache-poisoning.md) 验证。

## Agent 行为

先确认浏览器可达与身份，再解释影响；不以“响应头配置看起来宽松”代替私密数据读取。实验页面仅显示自建无敏感标记，不外传真实响应。

## 调研来源

- [PS-cors · CORS](https://portswigger.net/web-security/cors)
- [MDN-cors · Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

## 归档经验纠偏

跨源发送、凭据是否附带与脚本读取响应是三件事；同站不等于同源，不能把 SameSite=None 写成所有跨源证明的统一前提。使用当前浏览器实际证据及敏感内容判断，见 [K15](../research/crawl-xz-patterns.md)。

改用 XMLHttpRequest、启用 withCredentials 或手工添加 Origin，不是普遍绕过预检的方法。保留真实浏览器选择的请求方法、头、内容类型、OPTIONS 结果及实际读取证据；如果失败发生在预检，不能把代理直接重放成功替代为攻击页已读取响应。

## 名称匹配与动态跨源参数

域名允许规则应比较解析后的完整origin与标签边界。图片把target.com与sub.eviltarget.com的字符串命中当绕过，实际后者不是target.com的子域；图中裸域形式也不是浏览器完整Origin。用受控合法子域、相似尾部的独立域作对照，保存实际响应头、凭据模式及浏览器对自建私密标记的读取。只反射输入没有读取证据时保留为配置假设。

名为corsDomain的查询参数可能选择响应策略，也可能完全未被消费者使用。跟踪实际参数、浏览器Origin和响应差异；一个历史URL/手工添加头不证明当前服务允许不可信来源读取。公开无凭据资源是反例，不把供应商公共服务纳入原项目测试范围。

## CRLF注入与浏览器Origin来源

旧图把Origin值中加入回车后反射为Content-Type，再称CORS绕过。按[Fetch header value](https://fetch.spec.whatwg.org/#concept-header-value)与[禁止请求头](https://fetch.spec.whatwg.org/#forbidden-request-header)，普通Fetch头值不允许HTTP换行，Origin由浏览器控制（2026-10-09核对）。代理手工构造不是外站网页可构造证据；历史IE/Edge还需精确版本和独立前提，不能推当前浏览器成立。把原始字节的头注入、改变MIME的消费者与真实跨源私密读取三段分别证明，转[CRLF](crlf-response-splitting.md)保留未接上的边；不投递来源载荷或伪造浏览器结果。

## HEAD与Origin文本匹配的误报

HEAD响应任一行含输入Origin、工具打印VUL TO CORS，不能证明浏览器可以读取私密正文。该文本可能来自Location、错误提示或其他非授权头；HEAD与真实业务GET也可能走不同处理器。截图批量绿字只有匹配器输出，不能将每个资产标为confirmed。

分别记录实际Access-Control-Allow-Origin/凭据条件、浏览器自动请求头、预检/重定向、读取到的内容及预期读者。用当前浏览器与两个获准来源的合成数据验证读取边界；公共正文或单反射头没有自动敏感影响。历史300/200并发、全域搜索与follow-redirects不作为执行配置，跨跳范围和每个主动动作独立受限。

## null来源序列化与真实私密读取

Origin: null不是名为null的可信网站，也不唯一标识某个本地文件。[MDN允许来源说明](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin#null)解释部分非层级URL和sandbox文档会序列化为null（2026-10-09核读相关段落）。原帖把Access写成Acess，不能静默当成有效响应头；即使真实重放得到正确的ACAO null与ACAC true，也只是策略候选，还缺真正浏览器来源与私密读取。

对获准合成资源记录来源如何形成、浏览器版本/策略、自动身份实际发送、预检、响应头和JS读取的私密标记。Cookie被阻、资源本来公开、主体无权或响应走不同处理器均是反例；不把手工设置Origin当浏览器证据，也不渲染来源页面触发真实用户。

## 同源示意图的箭头与浏览器读取

协议/主机/有效端口共同决定普通Web URL来源，路径差异本身不改变origin。[MDN同源说明](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)给出该比较规则（2026-10-09核读相关段落）。来源图却在example.com和foo.com之间画允许返回箭头；两个名字不同仍是跨源，图中没有CORS策略/实际浏览器结果，不能用绿色勾判同源读取。

分别记录跨源发送/嵌入、自动身份、响应读取以及后端授权；SOP不是阻止一切网络通信的防火墙。只对获准合成受保护标记以正常浏览器来源核对，排除公开资源及合法跨源共享，不关闭安全策略或加载图中真实网站。

## 读取聊天标识与写入聊天消息的链条

跨站能读chat sessionId与借此发消息是两个消费者。先证明浏览器以当前允许凭据/第三方Cookie策略读取私密响应，再追标识是否实际充当写入能力，或仍需要身份、CSRF token、Origin与业务权限。代理看到响应不代表外站脚本可读；P3/Triaged题名未给完整链。

[MDN凭据与通配Origin说明](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS/Errors/CORSNotSupportingCredentials)指出带凭据时ACAO星号不能让浏览器读响应（2026-10-09核读）。ACAC true、预检头反射和HTTP200也不能代替真实读/写结果。用获准合成聊天对象或已有处理器代码核对内容类型、自动身份、会话归属和最小状态差异，不能把标识泄露自动视作CSRF成立，不向客服/真人发送消息。


## ACAO序列化Origin与带凭据浏览器读回

正文给出裸主机ACAO和ACAC true，另一图201返回组织字段并用星号。响应头出现并不能补真实跨站读回。

在受控浏览器环境记录完整scheme/host/port Origin、凭据模式、Cookie有效条件、预检及实际可读的受保护字段；裸主机不是正常序列化Origin。星号与带凭据响应、服务端JSON可见与脚本读回必须分开；无Cookie、公开数据或浏览器拒绝读回是反例。

来源：[保存帖1](https://x.com/i/status/1417394778208014339)、[保存帖2](https://x.com/i/status/1418510719839002625)。


## Burp Origin 替换、项目持久化与浏览器差异

Match/Replace 图展示替换请求 Origin 并保存项目配置。

明确规则匹配范围、开关和实际发送头，用正常/替换/关闭规则三份线报文保持主体与资源一致。研究者代理能伪造 Origin 不等于浏览器允许任意 Origin；CORS 影响还需具体读者、凭据策略和浏览器可读敏感响应，不能仅因代理响应变化判成立。

来源：[保存帖1](https://x.com/i/status/1449339347002613765)。


## 本地 xhr 页面与跨站写入的独立条件

截图只有本地文件页面与sessionid弹窗；另一帖将JSON改成urlencoded以避免preflight。

区分CORS读权限、浏览器自动带凭据、服务器Content-Type解析、Origin/CSRF校验与持久状态改变。无需preflight不自动绕过CORS，读到字符串不证明受保护写入；凭据缺失、SameSite阻止、类型拒绝、CSRF拒绝或仅公开数据为反例。保存原始头/body与真实读者链，不打开归档HTML或修改账号。

来源：[保存帖1](https://x.com/i/status/1459415332930473992)、[保存帖2](https://x.com/i/status/1461684616667045893)。


## Origin ACAO 精确差异与浏览器读权限

片段先列wwwx.in精确匹配，再列evil.ie与evilx.ie不一致同时ACAC true，没有浏览器响应读取。

固定真实请求Origin、响应ACAO/ACAC、自动带cookie及敏感字段，检查整个Origin值与真实读者差分。字符串包含、后缀相似或ACAC true不自动允许任意Origin；不一致拒绝、没有凭据、公开内容为反例，不以改Origin的Repeater响应代替浏览器读证据。

来源：[保存帖1](https://x.com/i/status/1465408726140030976)。


## Trust Tokens 本地存储画面不证明 CORS 读取

正文称CORS已解决，完整图是DevTools本地Trust Tokens发行者与WebSQL数据库表，未显示Origin、CORS响应头或跨站读取。

离线两个自有origin核请求身份、预检、凭据模式、ACAO/ACAC与JS读取结果，对比允许与拒绝。DevTools能看本地数据库、localhost记录、header名称或请求发出为反例；需真实浏览器读取受保护合成字段才支持影响，不能把本地存储截图当成跨域证据。

来源：[保存帖1](https://x.com/i/status/1492102034589421593)。


## CORS 响应需用浏览器实际 Origin 与凭据条件核对

图中的手工 Origin 和允许来源都是无方案的 google.com，并设置允许凭据，未显示真实浏览器可读结果。

保留原始头与浏览器序列化来源的差异，再核发送凭据、预检和实际响应可读性。手工字段回显不证明浏览器允许跨来源读取，也不能与同图 DNS 回调合并为接管链。规范核验：[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)。

来源：[保存帖1](https://x.com/i/status/1527151958959616000)。


## 可控子域 XSS 到凭据 CORS 读取的逐段条件

链条要求脚本能在受信子域实际执行，受保护接口认可该实际 Origin，浏览器发送相应凭据，并允许脚本读取响应。保留精确 origin、ACAO/ACAC、实际 Cookie 发送条件、受害测试账户和最小响应。withCredentials 设置与对任意子域的文字说明不证明全部条件成立；不能把子域、同站和同源混为一谈。[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)解释凭据请求和读取条件。

来源：[保存帖1](https://x.com/i/status/1534574595692724225)。


## CORS 告警和真实浏览器非公开读取分开

CORScanner 图列 reflect_origin、trust_any_subdomain、https_trust_http 和 credentials 标志；另一组图给出 withCredentials 的 XHR 与弹窗中的会话数据，且请求设置自定义 API 头。保留真实发起 Origin、OPTIONS/实际请求、ACAO/ACAC、cookie 策略和最小响应，证明受控外部源能读到该测试账号的非公开内容。

curl 响应、反射 Origin 或 200 不等于浏览器可读，自定义头可能触发预检。核查登录状态、公开基线及数据用途；alert 的返回值赋给 innerHTML 不能补出额外 XSS，截图里的会话/JWT 不复制或使用。

来源：[保存帖1](https://x.com/i/status/1552020733072551936)、[保存帖2](https://x.com/i/status/1553376300047400962)。


## Origin前后缀候选必须证明浏览器读取真实保护数据

正文提醒CORS前后缀匹配，图片是Prefix match奖励标题。记录实际Origin解析、允许源逻辑、ACAO、凭据、预检和浏览器行为，用两个自有来源及自有账户验证能否读取本应保护的最小响应。仅反射Origin、返回200或支付记录不足；请求可发送与响应可跨源读取须分开。

来源：[保存帖1](https://x.com/i/status/1557357144395042816)。


## ACAC true 单一响应头不能认定 CORS 数据泄露

保存 Yelp 报告图将 ACAC true 视为风险但状态为 Informative。按真实跨站浏览器验证 Origin、credentials mode、Cookie 发送条件、预检和最终脚本可读响应；服务器重放伪造 Origin 不替代浏览器实验。带凭据读响应需要匹配的 ACAO 与 ACAC，星号 ACAO 不支持 include；见 [Fetch CORS credentials](https://fetch.spec.whatwg.org/#cors-protocol-and-credentials)。仅看头不证明敏感数据、身份或实际跨站影响。

来源：[保存帖1](https://x.com/i/status/1575366570238435328)。


## CORS 批量管道须验证浏览器实际共享的认证响应

保存命令用target=$(curl...)后grep未连接变量，curl -I仅取头且语法残缺，不执行。Origin字符串出现不是漏洞；对实际GET/身份、敏感自有标记、允许Origin与credentials进行浏览器正负对照。Fetch要求include模式下明确Origin和ACAC true，*不能替代；保留预检与实际请求区别、缓存和Vary条件。

校正依据：[Fetch CORS与凭据](https://fetch.spec.whatwg.org/#cors-protocol-and-credentials)，实际读取共享规则。

来源：[保存帖1](https://x.com/i/status/1580378333086646272)、[保存帖2](https://x.com/i/status/1580544182170824704)。


## 过期或可购买 Origin 不自动完成 CORS 读取链

正文仅保存步骤4–6，称一个域可买但昂贵，图为 Dell 奖励通知。区分允许 Origin 名单、域实际可控制、浏览器携带会话、Allow-Origin/Allow-Credentials 及真实敏感响应可读，在自有隔离域与帐号做允许/拒绝对照。可注册域和奖励题名不证明完整链，不购买域、不补造缺失步骤或真实后端响应。

来源：[保存帖1](https://x.com/i/status/1590976530389565440)。


## 返回 session 的 Origin 反射示例：浏览器读取和真实身份均需证据

1597231588118450178-03.jpg 把请求 Origin 原样写入 ACAO、credentials=true，并返回 id/name/email/session；GetCredentials 是固定对象示意。分开核验受信任 Origin 策略、cookie 实际附带、浏览器是否可读、缓存分区，以及真实认证主体与 token 权限。反射来源加 credentials 是风险线索，示例并不提供真实会话校验；仅以两个自有来源/身份和假 token 验证数据流，不把 demo 固定 session 当作有效秘密。

来源：[保存帖1](https://x.com/i/status/1597231588118450178)。


## CORS 加方法覆盖头：读取策略与真实动作仍是两道边界

正文主张 CORS 端点加 HTTP override 可扩展访问、绕过 CSRF/XST，但没有请求或结果；1597629835781689344-02.jpg 只是人物画。分别确认浏览器预检/允许头、实际 cookie/身份、覆盖头是否被目标路由消费、最终方法以及对象/动作授权，读取 CORS 响应不能省略状态变化证明。TRACE/XST 还受浏览器方法和消费者限制，不从口号推断任意端点或身份数据可读，不测试历史目标。

来源：[保存帖1](https://x.com/i/status/1597629835781689344)。


## Origin 反射要核对浏览器实际读取与私密数据

保存历史 CORS 请求在 /wp-json 送非本域 Origin，响应 ACAO 回显，credentials 头与后续效果裁切。核对原始响应、真实浏览器 CORS 处理、凭据/预检、SameSite 与受限 body；公共 API 内容即使可跨域读也不必越权。区分服务端允许域匹配与线上 ACAO 语法，不能把 *.domain 当浏览器支持的任意子域列表。只用自有两个 origin 和合成私密对象作允许/拒绝对照，curl 加 Origin 成功和平台评分不证明跨站泄露或当前仍有漏洞。

来源：[保存帖1](https://x.com/i/status/1612749766592548870)。

已实际查看保存图片 `1612749766592548870-02.jpg`：Acronis2020CORS报告/wp-json/Origin非本域→ACAO反射，ACAC后续裁切；Dcors实际自有浏览器读取受限body/credentialsCookie-SameSite/preflight，publicwp-json无私密不成立、响应头不授权client；*.domain例不能当浏览器合法ACAO域通配，服务端匹配与wire不同，不称当前有。


## of-CORs 工具公告不能把网络可达性等同浏览器跨源读取

正文只有typosquatting、内网CORS与回传工具的能力声明，未保存实现。提炼为边界：自有两个origin、本地模拟服务、无敏感响应，对照Origin、credentials、预检和最终JS可读正文；浏览器同源限制、网络策略和服务器授权分别记录。curl可访问、域名拼错或响应含ACAO均不证明跨源敏感读取。无需注册相似域名、诱导用户或回传真实内网数据。

来源：[保存帖1](https://x.com/i/status/1613928907895615490)。


## CORS 响应读取权限与服务认证分开建模

保存正文定义以响应头指定允许来源，图只有封面。先固定请求 Origin、是否携带凭据、目标会话与返回数据，再在真实自有浏览器来源中比较能否读取自有私密响应；预检和实际响应需要分别记录。宽泛响应头、命令行读到页面和公开资料不证明跨站秘密读取，CORS 也不授予服务端对象权限。正文未保存具体漏洞交换，将此作为检查模型而非已确认案例。

来源：[保存帖1](https://x.com/i/status/1618523574540861440)。


## Origin 反射清单纠偏：浏览器可读私有数据才是确认点

图片把 Origin 中带 slack、前后缀相似域、任意域或子域获反射列为漏洞，其中若干示例缺少 scheme。实际浏览器 Origin 是包含 scheme/host/port 的源或特殊 null，手工任意 header 不代表攻击页可发出同样来源。用受控浏览器页面验证请求能否带有效身份、预检是否通过、响应 ACAO/ACAC 如何组合，以及脚本能否读到本来不可公开的数据。反射公开响应、只允许可信子域或服务器回显字符串均不足以确认影响；子域控制权、credential 模式及敏感 endpoint 应独立证明。此图是测试候选，不能视为普遍漏洞判据。

来源：[保存帖1](https://x.com/i/status/1624816107520421888)。

现有图片证据 `1624816107520421888-02.jpg`：CORSallowlist图Origin缺scheme列不同TLD/subdomain左右拼接等→reflect就vuln断言；错误，实际browserOrigin规范/credential/privatebodyread/子域可控及scope独立。


## CORS 反射 origin 与带凭据敏感读取的浏览器对照

CORS应结合SOP理解：服务端许可哪些origin读取响应；不是任何跨站请求都被禁止。报告图片写ACAO evil.com及ACAC true但只有文字，ACAO还需有效完整origin。自有浏览器页面固定origin、credentials、Cookie/SameSite、预检和真实敏感响应，以不受信origin被拒绝为对照；Burp任意改头或错误凭据登录响应不能证明受害者数据可读。公开无敏感内容或浏览器拒绝读取是关键反例。

来源：[保存帖1](https://x.com/i/status/1628416069709987840)、[保存帖2](https://x.com/i/status/1629445603762532358)、[保存帖3](https://x.com/i/status/1629884637995573250)。

现有图片证据 `1629884637995573250-02.jpg`：CORS login报告称ACAO evil.com与ACAC true，截图是报告文字和错误凭据入口；ACAO需合法完整origin、浏览器凭据及敏感响应读出，不能仅凭Burp改头认定泄露。


## 自定义 X 头、压缩与 CORS 方法声明不是安全授权

表将X-*、Content-Encoding、ACAO/ACAM与多种攻击相连，不能据标签推因果。X-Forwarded-IP/Origin等客户端值需可信代理边界，不可当真实IP；Content-Encoding是编码/压缩而非加密。ACAO允许哪些origin读取，ACAM只涉及跨站方法声明，不代替服务器认证/对象权限；用浏览器origin、凭据、预检与实际敏感响应对照。通配或null需精确上下文，不能因某头存在即认为安全。

来源：[保存帖1](https://x.com/i/status/1632678412694298624)。

现有图片证据 `1632678412694298624-03.jpg`：安全头表2/2列Cache-Control no-cache/no-store、Content-Disposition、CORP、X-*自定义/转发/限流、Content-Encoding、ACAO/ACAM；压缩不是加密，任意X头不是真实IP，方法许可不代替认证。


## 去点域名需要真实浏览器 Origin 和可读响应

wwwTarget.com式候选可能利用substring/regex origin检查，须核对真实可控注册域、scheme/port及浏览器Origin，记录ACAO/ACAC、Cookie/SameSite和跨站脚本能读的非公开内容。Burp改Origin或500奖励不证明浏览器泄露，公开数据/无credential/头不匹配都是反例。

来源：[保存帖1](https://x.com/i/status/1636777974614704133)。


## Flash crossdomain 策略与现代浏览器 CORS 不同

2018报告列过宽crossdomain.xml、第三方/范围外子域及SWF/AkamaiPlayer loaderContext，缺完整policy/加载与ATO链。先界定实际Flash运行环境、来源、允许域与凭据/响应消费者，记录角色/会话条件。历史Critical不能外推当前浏览器fetch或所有子域接管；范围外域引用不授予测试授权，不加载旧SWF。

来源：[保存帖1](https://x.com/i/status/1642837178324484096)。

现有图片证据 `1642837178324484096-02.jpg`：2018跨域报告列过宽crossdomain.xml及外部/范围外子域，提SWF on l.unibet.fr与AkamaiPlayer loaderContext；图缺完整policy/加载代码及ATO兑换。Flash策略不是浏览器CORS，历史Critical不能当前通用ATO。


## 原型 has trap 片段没有跨源 JSON 读取证明

图Object.setPrototypeOf及Proxy has trap仅alert属性名，缺JSON响应/加载方式/浏览器结果。核对实际subresource MIME、同源策略、凭据、解析语法与可观察值，固定版本做隔离对照。局部原型变更不等跨域数据泄漏或应用prototype pollution，题名modern web不能外推所有当前浏览器。

来源：[保存帖1](https://x.com/i/status/1643304171293270017)。

现有图片证据 `1643304171293270017-02.png`：现代JSONhijacking插图 Object.setPrototypeOf(__proto__,new Proxy(__proto__,has trap alert(name)))；没有JSON响应、跨源加载、数据值/浏览器结果。仅局部原型观察片段，不证明现代所有浏览器跨源JSON可读或prototypepollution。


## 域名字符串后缀相似不能代替 CORS 信任来源

归档以 domain.com.attacker.com 提示来源校验风险。比较实际 Origin、Access-Control-Allow-Origin、credentials 设置及浏览器在受控来源读取的响应，检查服务器是精确主机匹配、正确的子域边界还是不安全的字符串包含。响应头宽松与真正读取受身份保护数据不同；需记录 cookie/令牌发送、预检和敏感内容，不能仅凭相似域名、图片上的奖金额或预期付款认定影响。

来源：[保存帖1](https://x.com/i/status/1646935738670260240)。


## 携带凭据的 fetch 需证明跨源响应是否可读

截图的 profile 请求使用 credentials:include；这不证明 cookie 一定随跨站发送或 CORS 允许读取。记录发起 origin、cookie 属性、实际请求、允许 origin/credentials 响应及浏览器读取结果，再定位 csrf token 是否可被下一步消费者使用。仅见请求代码不能跳过 SameSite、CORS 或权限，单独保留服务端处理与浏览器可读两层结果。

来源：[保存帖1](https://x.com/i/status/1655581821940412416)。

保存图片 `1655581821940412416-02.jpg`：oneclickCSRF静态页windowopen/search、2秒timer、doubleencodedJSONPcallback、postMessage JSON arg App.apiCall；另一JScredentialsinclude profile token→updateProfile；图裁切update下半与trust/CORS响应缺失，多边界需分别验证，禁止偷token/更新外部profile。 本段仅使用实际查看的保存原图，不补未保存内容。


## JSONP 回调与跨域读取使用不同浏览器规则

Param Miner 找到 callback 参数后，需确认响应是否真以脚本方式消费、callback 控制、实际数据、凭据和 Content-Type/CSP；脚本加载与 CORS fetch 响应读取不同。所有 API 都有 callback 的声称不能由一项参数命中推广，API key 名称也不证明秘密泄露。用自有对象与禁止 callback/跨域请求对照，不调用实际敏感接口。

来源：[保存帖1](https://x.com/i/status/1662063531435458560)。


## CORS 读权限与同源脚本执行不是同一边界

保存标题称 CORS 能缓解 XSS，这种泛化会混淆机制。CORS 控制浏览器对跨源响应的读取，XSS 需另证不可信输入进入可执行上下文和被信任 origin；来源权限配置不能代替输出编码或净化。若主张串联，分别保留浏览器来源、凭据、响应允许来源和脚本消费者，以无害自有样例作对照。文章全文未保存，不补成 YouTube 的具体绕过、当前策略或漏洞请求。

来源：[保存帖1](https://x.com/i/status/1681898458578386944)。


## 保存图证0188-9-cors：机制与验证条件

Radancy报告显示带Origin example.com的sockjs POST请求，但响应头与可读取数据位于裁切外。须证明ACAO/凭据/preflight及浏览器可读敏感响应，任意Origin请求可发送不证明CORS影响。 可用原图：`1693880867721236639-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1693880867721236639)。


## CORS PoC 与外部隧道的验证内容（0188）

工具宣称生成 PoC 并用 ngrok 验证，先审阅请求、外部地址及哪些数据会离开测试环境。对受控两个源证明浏览器是否携带所需凭据、preflight 是否允许及最终能读取哪些受保护数据；curl 成功、Origin 反射或公开响应不证明敏感 CORS 影响。没有保存实现或浏览器结果时，不声称工具已验证。

来源：[保存帖1](https://x.com/i/status/1696204735160762796)。


## 保存正文0190：域名包含匹配不能代替Origin与邮箱归属

target.com.evil.com与eviltarget.com检验前/后缀包含误判；应按URL规范化后的scheme/host/port精确判断Origin，凭据CORS还需浏览器实际带身份并可读敏感响应。company.com.burpcollaborator.net邮箱域同样不能当company.com成员；收到SMTP只证明发信，不证明已通过验证、成员加入或权限升级。使用自有域/账号、最小标记，不发送真实组织邀请。

来源：[保存帖1](https://x.com/i/status/1702635559796031681)、[保存帖2](https://x.com/i/status/1702750276049162564)。


## 保存图证0193-119-cors：机制、前提与最小验证

已查看的原始图片：1713999851283988719-02.jpg。client.amplifi.com /api/user CookieGET+Origin https://aaaa.ubnt.com.evil.com，响应ACAO同值ACACtrue JSON个人资料，后缀子串校验候选。Repeater可任意Origin且手工Cookie不同浏览器凭据流程；浏览器攻击origin fetch credentialsinclude实际读自有资料、SameSite/HTTPS/preflight对照，不以200推任意域都可。

来源：[保存帖1](https://x.com/i/status/1713999851283988719)。
