# Web 缓存欺骗

适用信号：动态私密页面与静态缓存规则的路径解释不一致

## 检查与最小实验

在隔离测试路径比较普通动态 URL、附加无意义后缀、带已观察分隔/规范化特征的 URL。分别确认源站映射哪个资源、缓存按什么规则存储；仅“加 .css 返回 200”不足。

用 A 的自建私密标记触发缓存，再用不携带 A 凭据的 B/匿名干净客户端请求同一测试键，核对是否读到 A 数据。另一个隔离键作控制，记录 Vary、Cookie、编码和浏览器实际 URL 序列化。

## 证据与反例

源站忽略后缀或缓存显示 HIT 只是链条中的一步。正常公开响应、身份实际串用、CDN 未缓存的源站响应都不能确认泄露。特定框架的分隔符和解码顺序不能推广到所有 CDN。

## Agent 行为

从 X 经验追溯到原研究后才挑适用分支。只使用自建数据和已证明隔离的缓存空间；随机 cache-buster 未必生效。无法隔离则在本地模型验证并保留待补证。

## 调研来源

- [PS-cache-deceive · Web cache deception](https://portswigger.net/web-security/web-cache-deception)
- [PS-cache-research · Gotta cache 'em all: bending the rules of web cache exploitation](https://portswigger.net/research/gotta-cache-em-all)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。


## no-cache、no-store 与内容下载策略的独立含义

表中Cache-Control区分no-cache重用前验证和no-store不存储；Content-Disposition控制inline/attachment，CORP限制跨origin资源消费。缓存欺骗还须缓存路由/键、个人响应储存和跨身份命中，并非缺头或静态后缀就成立。自有两身份夹具对冷暖响应、Vary/认证和真实缓存行为，保留敏感内容未缓存反例；attachment文件名不代表脚本可执行，安全视图不等于禁止下载。

来源：[保存帖1](https://x.com/i/status/1632678412694298624)。

现有图片证据 `1632678412694298624-03.jpg`：安全头表2/2列Cache-Control no-cache/no-store、Content-Disposition、CORP、X-*自定义/转发/限流、Content-Encoding、ACAO/ACAM；压缩不是加密，任意X头不是真实IP，方法许可不代替认证。


## 编码 CSS 后缀到缓存 XSS 要证明独立读者

self email XSS→.css被挡→%2ecss200/cached需要缓存键、解码/路由、内容类型、存储资格及身份差异。用受控A写入惰性标记，B或匿名从同key独立读取，观察Age/命中/TTL/清理和实际浏览器上下文。单次200/cached或仅A回显是反例，没有跨读者和执行链不能升级为公共XSS。

来源：[保存帖1](https://x.com/i/status/1636677827109048325)。


## 动态路径静态后缀缓存需跨主体取回与秘密绑定

摘要两条件为动态search/minNightlyPrice任意尾路径反射session，.jpeg被缓存，并称HASESSIONV3可取profile ha.crumb。固定路径处理器、cache key/Vary/CacheControl/TTL与A/B自有会话，证明另一主体取回含标记的缓存后再核对token权限。200/后缀和作者ATO声明不足，去除页面token为历史修复建议，不补造当前headers或兑换结果。

来源：[保存帖1](https://x.com/i/status/1642270945598492672)。

现有图片证据 `1642270945598492672-02.jpg`：Cache deception摘要两条件：200动态search/minNightlyPrice任意尾路径反射session token，.jpeg后缀被缓存；声明可用HASESSIONV3访问profile取ha.crumb。缺完整header/另一主体取回与兑换证据，需key/Vary/CacheControl/TTL/主体对照，保留历史修复去除token。


## hav cookie 反射与缓存投毒的共享消费需分别证明

图只显示四问题中的前两：.js路径var hav字符串反射，双引号处理但角括号未处理及WAF变体。追踪响应MIME/HTML/JS消费者、编码顺序与真实事件，另核对cookie是否进缓存key、跨主体取回和过期。不能补后两问题，反射/XSS候选不自动缓存共享或ATO，图片截断变体不当有效payload。

来源：[保存帖1](https://x.com/i/status/1642271042113552384)。

现有图片证据 `1642271042113552384-02.jpg`：Cache poisoning截图仅四问题中的前两：hav cookie在.js路径响应var hav字符串反射，双引号处理但角括号未处理，claim闭script绕WAF；底部编码/引号变体且未完整。缺缓存key/另一主体取回/真实DOM与ATO链，不能补后两问题。


## 随机 UA 与可缓存提示头需分别验证

图片为使用 ffuf 的 GET 返回 403，并含 X-Check-Cacheable: YES，帖子建议随机 UA。头名称和值不是实际缓存命中、缓存键或跨用户污染证据；核对 Age/命中信号、响应指纹、重取行为及 Vary/键配置，保持其余条件一致。没有保存 UA 改变后的对照，不能认定可绕过 403；更不能从一个 YES 推导缓存投毒或敏感数据可被他人取得。

来源：[保存帖1](https://x.com/i/status/1648168615772921858)。

现有图片证据 `1648168615772921858-02.jpg`：UserAgentFuzzFasterUFool GETindexhtml403/X-Check-CacheableYES，只有单响应，没有randomagent对照或真实cachehit；UA阻断不证明cachekey规则。


## 静态后缀的缓存欺骗需证明跨身份取到私有内容

Algolia 摘要描述登录用户访问随机 CSS 名后缀，代理缓存动态私有响应。核对应用路径解析、缓存分类/键、cookie/身份和真实命中，用自有 A/B 会话标记比较首次与后续读取。页面带 .css、缓存头或奖金状态不等跨用户泄露，公开内容缓存也不构成同等影响。缺失原响应时保留条件，不让他人访问验证链接。

来源：[保存帖1](https://x.com/i/status/1649136815666782209)。

现有图片证据 `1649136815666782209-02.jpg`：Algolia缓存欺骗摘要：登录用户访问随机CSS后缀URL→代理存私有响应→后续取得，无实际头/响应；需路径解释、缓存键/身份和自有A/B内容对照，不接触受害者。


## UA 阻断与可缓存提示不证明跨请求污染

图片中 Fuzz Faster U Fool UA 的 GET 返回 403、X-Check-Cacheable: YES。用受控合法 UA 与候选 UA 的单变量对照核对缓存键、Vary、真实命中及后续自有会话内容，区分应用/网关拒绝。头名和 YES 不证明实际缓存或 DoS；没有跨请求结果，不补出“换 UA 即绕过”或缓存投毒，验证不得采用高并发压力。

来源：[保存帖1](https://x.com/i/status/1649463620386914317)。

现有图片证据 `1649463620386914317-02.png`：GET/index.html UAFuzzFasterUFool返回403/X-Check-CacheableYES；没有缓存命中/跨UA键或二次用户响应，不能证明缓存投毒DoS。


## UTM 参数的缓存键与响应差异分别比较

utm_content 等追踪参数可能改变响应而不进缓存键，但仅名为 UTM 不证明风险。在自控缓存/账号使用唯一无害标记，比较有/无参数、同键不同用户、冷/热缓存响应及 Age/缓存命中证据。确认跨请求持久污染和受影响用户；普通反射、浏览器缓存或未缓存私有响应均为反例。

来源：[保存帖1](https://x.com/i/status/1653033800144941057)。


## 错误页和 header 回显仍可能携带私有缓存内容

404 后缀诱发缓存与 wotif info.php 缓存最后请求 headers 摘要，需要区分源应用动态内容、边缘 key、status、Vary、身份/cookie 与命中来源。用自有 A 登录写入无害标记，再由无 A 身份 B 读取同键，记录响应和失效时间；404 不保证无隐私。原文 /vc 与摘要 /vs 路径不同，约一小时说法无实际时序，不对真实用户投毒或读取 cookie。

来源：[保存帖1](https://x.com/i/status/1659239550823038977)、[保存帖2](https://x.com/i/status/1659959973693075458)。

保存图片 `1659959973693075458-02.jpg`：wotif正文/标题 /vc/blog/info.php与摘要/vs/blog不同，缓存约1h的最后HTTPGETheaders，作者无法XSS但style/form接受/HttpCookie下位访问可能读前访headers；底部仅TEMP环境几行不见cookie回包，需A/B自控缓存序列，NO真实cookieuse，不宣称WAF通用可绕。 本段仅使用实际查看的保存原图，不补未保存内容。


## 缓存 purge 的受理回执不等于真实失效

图片给 PURGE curl.se 与 status:ok/id 的叙述，但步骤多处占位。用自控缓存键比较 purge 前后命中/年龄/版本及允许/未允许身份，明确管理动作的授权、范围和副作用预算。异步受理不证明实际失效或带宽成本，站点缓存接口也不自动是 curl 库缺陷；不向公网发 purge、不做 DoS。

来源：[保存帖1](https://x.com/i/status/1659952438684573699)。

保存图片 `1659952438684573699-02.jpg`：PURGE curl.se回应statusok/id叙述，Informative及大量模板占位；需相同缓存键purge前后命中/身份对照，受理不等完成失效/成本DoS，不对公网发送。 本段仅使用实际查看的保存原图，不补未保存内容。


## PURGE 接受响应不足以证明缓存驱逐影响

保存图返回 status ok/id，受理回执与实际驱逐是两项证据。用授权隔离 key 对比调用前命中、调用者身份、驱逐后干净读取及后端成本，确认 key、host、scheme、TTL 和异步处理。截图中 HTTP 与正文 HTTPS 不一致须保留；未认证属性、实际命中变化和 DoS 都未完整证明，历史 Low/accepted 不能泛化到任意缓存。

来源：[保存帖1](https://x.com/i/status/1664365820682567692)、[保存帖2](https://x.com/i/status/1665404227441807361)。

保存图片 `1665404227441807361-02.jpg`：PURGE返回statusok id HTTP非正文https且targethidden，受理≠实际samekeycacheeviction/backendcostnoauthproof本段仅使用实际查看的保存原图，不补未保存内容。


## 404 缓存污染验证隔离 key 与干净读取

保存帖描述 X-Forwarded-Host 影响缓存后的错误页。用项目允许的隔离 key 记录正常请求、单一 header 变化、随后不带该 header 的第二身份读取及 Age/命中证据，确认 query 是否实际纳入缓存键。反复看到 404 不证明共享或无限期污染，TTL 未知不写成永久；unique query 本身亦不能证明隔离，不污染公共 key。

来源：[保存帖1](https://x.com/i/status/1665758310589399053)。

保存图片 `1665758310589399053-02.jpg`：MDNXForwardedHost错误404缓存返回shared用户claim，使用uniquequerycachebusteronly该key，TTL未知repeat并不无限证明；responsehead未示 hit/age控制二会话干净request，勿污染publickey本段仅使用实际查看的保存原图，不补未保存内容。


## unkeyed 输入到缓存污染还需干净读取对照

正文只描述操纵未纳入 key 的输入使响应缓存。确定实际缓存键、可控输入消费者、共享对象和 TTL，以获准隔离 key 对比正常响应、单一变化和随后不带该输入的第二身份读取。响应变化不独立证明缓存或跨用户污染，隔离 query 是否入 key 也要证实；不污染公共缓存。

来源：[保存帖1](https://x.com/i/status/1668640760105779200)。


## 缓存命中与持久脚本执行需要分别建立证据

正文把 reflected XSS 加上 `X-Cache: Hit` 推为 stored XSS，附图只显示 cache poisoning、零点击 ATO 的报告标题。命中表示缓存参与了这次响应，不能证明不可信输入被写入共享缓存、进入脚本执行上下文或影响另一身份。需要记录写入请求、完整缓存键相关输入、响应来源和有效期，用自有第二会话发出不含测试输入的干净读取，再验证是否返回同一标记并进入实际脚本消费者。若标记仅在带参数的本次响应、私有缓存或不能执行的文本中，链条不成立；会话接管还需独立证明受保护权限变化。

来源：[保存帖1](https://x.com/i/status/1670187950087233536)、[保存帖2](https://x.com/i/status/1672193524798828546)。


## 缓存欺骗到令牌泄露需证明另一身份取得缓存响应

正文主张 Web Cache Deception→CSRF token→应用范围 CSRF→接管，并称敏感页加 private 修复。每一段分别记录实际路由/静态后缀解释、共享缓存键、缓存命中、第二身份可读取的受保护字节及令牌绑定。private 针对共享缓存的预期处理仍需实际配置/响应比较，不能从加 directive 宣称所有浏览器缓存或所有消费者已安全。保存材料无这些原始结果，不补全接管链或获取真实令牌。

来源：[保存帖1](https://x.com/i/status/1683063527584432128)。


## 缓存投毒到 XSS 与 ATO 分别证明

正文一例称 unkeyed header 反射脚本且 Cache-Control: public,max-age=500，另一例声称需交互的 stored XSS 链成 ATO；截图只有题名。确认输入未入 cache key、共享缓存确实存储且独立受害请求取得污染响应，再证明浏览器在预期 origin 执行；缓存指令不等实际 cache hit。ATO 需要敏感操作/会话影响回执，不能从脚本、题名或 public max-age 推成全部用户失陷；保留点击前提。

来源：[保存帖1](https://x.com/i/status/1686302783560138753)、[保存帖2](https://x.com/i/status/1686311896939438080)。


## 保存图证0188-60-cache：机制与验证条件

Glassdoor GET test.js?cb=1含X-Forwarded-Scheme http、X-Forwarded-Host受控域，报告称缓存跳转JS。图未见响应和另一个客户端缓存命中，Accept text/css及dest style也需确认实际资源用途；必须无注入头第二请求同缓存键/TTL对照，跳转≠脚本执行。 可用原图：`1694779312216625663-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1694779312216625663)。


## 方法覆盖头与缓存键是否一致（0188）

X-Http-Method-Override 若影响服务端行为而未纳入缓存键，可能使无该头的后续客户端获得错误响应。针对可恢复隔离资源记录原始方法、覆盖方法、key、TTL/Vary 和第二客户端无注入头的命中；仅重放一次有头请求不证明共享缓存污染。限制允许动作，不按“所有 verbs”直接发生产 DELETE/写操作；ATO 标题还需独立可执行和身份影响证明。

来源：[保存帖1](https://x.com/i/status/1696350007471780201)。


## 保存正文0190：缓存令牌到CSRF必须逐段成立

正文链为Web Cache Deception→authenticity_token缓存→敏感操作CSRF，仅为链纲要。必须分别证明敏感响应进入共享缓存、未授权自有会话能取到对应受害测试会话令牌、令牌在目标操作有效、浏览器跨站能携带必要身份且服务端状态真的变化。缓存HIT、公开匿名token、过期/不同用户token及无会话发送均为反例；避免第三方敏感操作，不由奖励标题补造缓存键。

来源：[保存帖1](https://x.com/i/status/1702418933079593006)。


## 保存图片中的机制与证据边界（1704718775839551711-04.jpg）：by-type/cache-deception.md

图片 `1704718775839551711-04.jpg`：AEM/api.json候选Host、X-Forwarded-Server/Host及absolute URI localhost建议。机制须证明不入缓存键的输入影响共享缓存响应且干净第二自有请求复用，不是单次反射；比较缓存键/TTL/Vary/代理信任链/归属和实际业务结果。绝对URI、HTTPHost、网络目标分开，不操作公共缓存或推断所有AEM可污染。

来源：[保存帖1](https://x.com/i/status/1704718775839551711)。
