# WebSocket 与跨站连接劫持

适用信号：实时消息、订阅、握手升级和长连接身份

## 检查与最小实验

分别记录握手身份、Origin、消息类型/资源 ID、连接生命周期。先在自建频道建立基线，再检查消息级对象权限以及退出/撤权后的后续消息。

CSWSH 要用受控外源页面在真实浏览器中建立连接，确认凭据是否自动携带且攻击页能收发被禁止的数据。`Sec-WebSocket-Key` 是协议握手字段，不能当成防 CSRF 令牌；CORS 响应头也不替代 WebSocket 的来源/身份控制。

## 证据与反例

101 只证明协议升级；公开聊天室跨站可读可能符合设计。必须证明以受害测试身份发生了未授权消息/动作。长连接不失效需结合项目的撤销语义，不能仅因握手未重做就确认。

## Agent 行为

记录每条测试消息和预期事件，绑定连接 ID 与会话。没有消息能力的 HTTP 工具不能声称已测试 WebSocket；结束关闭测试连接，避免后台订阅持续运行。

当功能操作没有新增普通 HTTP 请求时，检查已有连接的消息和浏览器调用路径，不能据 HTTP 历史为空判定没有输入。将消息字段继续跟到存储、广播与最终渲染角色；握手授权、消息内对象授权和存储型 XSS 是不同验证分支。代理看不到消息时可用获准浏览器调试或现有日志补观察，缺工具就保留消息覆盖缺口。

## 调研来源

- [PS-ws · WebSockets](https://portswigger.net/web-security/websockets)
- [PS-cswsh · Cross-site WebSocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

Cookie在浏览器过期与已经建立的WebSocket连接被服务器撤销不是同一个事件。固定自有测试连接/握手凭据、订阅对象、到期/退出/撤权时点与项目规定的会话寿命，分别记录旧连接后续合成消息、同凭据重新握手及新合法会话的能力。持续连接可能符合明确设计；握手未重复、客户端仍在线或读到本地旧消息不证明泄露。若策略要求即时停止，需权威状态之后真实服务器继续交付被禁止的测试数据/动作，并排除自动重连和刷新签发，结束关闭连接。


## WebSocket Origin 与成员消息授权分开验证

Mattermost图只有2017报告/2023披露题名与CriticalCSRF状态。检查真实浏览器握手Origin、cookie/SameSite、token绑定及跨站脚本能否接收非公开帧；连接成功与读取消息分别证实，Origin校验不能用HTTPACAO结论替代。旧题名不证明当前版本、不默认未认证或所有聊天泄漏。

来源：[保存帖1](https://x.com/i/status/1638866113441193984)。


## WebSocket 的 OTP 线索须绑定消息方向和会话

先从已保存流量区分握手、连接所属账户、消息类型、方向和发送时点，再定位 OTP 是否由服务端发给正确用户。过滤界面隐藏字符串不代表未发送；看见一个码也不证明另一主体可获取或登录。使用自有账户消息作对照，分别证明错误接收和服务端是否接受，不使用真实他人 OTP。

来源：[保存帖1](https://x.com/i/status/1655144476858277889)。


## JSON 消息调用需要双向绑定来源与命令能力

截图将新窗口、JSON 消息与 App.apiCall 连接。审查接收端 event.origin、event.source、消息 schema、允许命令、参数及关联会话；发送端指定 url.origin 仅限制自己的消息目的地，不证明接收端验证来源。固定两秒等待不保证加载完成，必须确认可控消息确实到达受保护调用，用本地两窗口最小夹具排除错误窗口或拒绝命令。

来源：[保存帖1](https://x.com/i/status/1655581821940412416)。

保存图片 `1655581821940412416-02.jpg`：oneclickCSRF静态页windowopen/search、2秒timer、doubleencodedJSONPcallback、postMessage JSON arg App.apiCall；另一JScredentialsinclude profile token→updateProfile；图裁切update下半与trust/CORS响应缺失，多边界需分别验证，禁止偷token/更新外部profile。 本段仅使用实际查看的保存原图，不补未保存内容。


## 跨站 WebSocket 劫持不自动获得任意漏洞能力

先确认握手是否校验 Origin、cookie/会话来源、消息 schema 与服务器对每个命令的权限，用本地自控两个 origin 比较。双向读写是协议属性，不证明 SQL/XSS/RCE sink 可控，正文“anything else”需拆成具体消费者与最小状态证据。封面没有握手/消息响应，不伪造全能力或使用真实用户会话。

来源：[保存帖1](https://x.com/i/status/1659485363973533696)。


## WebSocket REPL 先重建合法握手再比较消息权限

图示从 Burp /socket 握手的 Copy as curl 转到 wsrepl，并收到 metadata/new_finalized 订阅消息。保留 scheme、Origin、认证身份、握手字段、订阅和每帧时间/内容，转换时核对 shell 转义与实际新连接；不能逐字复用历史 Cookie、Sec-WebSocket-Key 或把 HTTP/2 UI 展示直接当可重放 Upgrade 请求。收到公共主题数据不证明跨用户访问，消息类型与对象授权需独立比较；本任务不重放会话或打开连接。

来源：[保存帖1](https://x.com/i/status/1681672743454949380)。

保存图证 `1681672743454949380-02.jpg`：Burp/socket握手Copy as curl(bash)转wsrepl并显示订阅metadata/new_finalized消息；保留Origin/Cookie/Upgrade/连接身份、命令转义与新握手，HTTP2视图不等于可逐字重放Upgrade，不复用图中会话或执行网络命令。收到公共消息不证明跨用户权限。


## WebSocket REPL 保存控制帧和业务帧的生命周期

图记录 0x1 JSON trade、0x9 ping、0xA pong、方向和时间戳；正文介绍 wsrepl Python 生命周期 hooks。握手、重连、心跳和消息处理与业务身份/订阅权限分层验证，保留原始帧、连接身份和相关动作；公开 trade channel 不代表私有交易可读。未保存 hook 源码，不补实现，不因 copy UI 或 REPL 存在声称会话绕过。

来源：[保存帖1](https://x.com/i/status/1686059203046322181)。

已审阅原图 `1686059203046322181-02.png`：WebSocket示例0x1JSON交易帧/0x9ping/0xApong、时间戳方向和channel，copy UI；协议生命周期与业务权限独立，公开trade数据非私有越权，工具hook无源码。


## 保存图证0189-149-ws：机制与验证条件

ArgoCD2123094 webterminal session从2.6.0起打开后token过期仍能发websocket messages，补丁2.6.14/2.7.12/2.8.1；已登录用户开terminal等待websession到期。复用握手鉴权vs长连接逐消息/到期撤销检查：旧socket在过期后无害message、过期token新握手、正常未过期基线分别比较服务端拒绝/断开/状态，不以UI开放等于命令权限。功能需webterminal已启用及已有权限，不是未登录RCE；版本限定按修复分支，不泛化所有>=2.6。 可用原图：`1700509546945585452-02.jpg`（保存帖 1700509546945585452）。

来源：[保存帖1](https://x.com/i/status/1700509546945585452)。


## 保存图片中的机制与证据边界（1704450609980854518-02.jpg）：by-type/websocket.md

图片 `1704450609980854518-02.jpg`：Mozilla1888545 hello.dev.myhubs.net：管理员建房、攻击者加入后presence_diff响应含别人的session_id；摘要称可代发消息，图在presence_diff小附件处截断，没有发送消息请求或接收端状态。广播会话标识不应当写入主体授权凭据；用两个自有房间用户比较消息sender与连接身份绑定、跨房间/同房间和服务端实际归属，不能由公开ID推断完整冒充复现。

来源：[保存帖1](https://x.com/i/status/1704450609980854518)。


## 保存图片中的机制与证据边界（1704978949485613367-02.jpg）：by-type/websocket.md

图片 `1704978949485613367-02.jpg`：Slack1639600官方摘要：创建/撤销Shared Invite Link时，经WebSocket向其他workspace成员传输密码hash，客户端UI未显示；平台无理由认为获明文密码并重置受影响密码。传输加密不保护合法成员收到的多余字段，hash仍属敏感但不是明文/已接管。两个自有成员及邀请操作对照字段最小化/订阅范围，使用非敏感沙箱值，不抓取其他用户hash或猜解。

来源：[保存帖1](https://x.com/i/status/1704978949485613367)。


## 保存图证0193-117-ws：机制、前提与最小验证

已查看的原始图片：1713997838840152426-02.jpg。浏览器WebSocket open/isTrusted true/readyState1仅建立连接，isTrusted是浏览器事件来源不是peer可信或授权；无消息payload/跨源Origin/受害cookie。CSWSH需恶源带受害session能读写消息，XSS另证消息到HTMLsink；open不等applicationwideXSS/CSRF。

来源：[保存帖1](https://x.com/i/status/1713997838840152426)。
