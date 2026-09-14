# WebSocket 与跨站连接劫持

适用信号：实时消息、订阅、握手升级和长连接身份

## 检查与最小实验

分别记录握手身份、Origin、消息类型/资源 ID、连接生命周期。先在自建频道建立基线，再检查消息级对象权限以及退出/撤权后的后续消息。

CSWSH 要用受控外源页面在真实浏览器中建立连接，确认凭据是否自动携带且攻击页能收发被禁止的数据。`Sec-WebSocket-Key` 是协议握手字段，不能当成防 CSRF 令牌；CORS 响应头也不替代 WebSocket 的来源/身份控制。

## 证据与反例

101 只证明协议升级；公开聊天室跨站可读可能符合设计。必须证明以受害测试身份发生了未授权消息/动作。长连接不失效需结合项目的撤销语义，不能仅因握手未重做就确认。

## Agent 行为

记录每条测试消息和预期事件，绑定连接 ID 与会话。没有消息能力的 HTTP 工具不能声称已测试 WebSocket；结束关闭测试连接，避免后台订阅持续运行。

## 调研来源

- [PS-ws · WebSockets](https://portswigger.net/web-security/websockets)
- [PS-cswsh · Cross-site WebSocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
