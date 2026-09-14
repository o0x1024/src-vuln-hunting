# CSRF

适用信号：依赖浏览器自动附带身份的状态操作

## 检查与最小实验

先确认操作、自动凭据、攻击者可构造的字段三项条件。用受控跨站页面触发一次获准的可逆测试操作，同时记录浏览器实际请求与服务端前后状态。分别看缺失/错误/另一测试会话的 token 是否被拒绝，以及方法或服务端接受的媒体类型变化是否走了不同防护路径。

SameSite 的 site 与 origin 不同；用真实浏览器记录 cookie 是否发送、Origin/Referer 与预检。Bearer 令牌若无法由攻击页获得，也非浏览器自动发送，不能手工在重放工具里补上后宣称 CSRF。

## 证据与反例

确认的是被禁止的跨站状态变化；缺 token、能发请求、读不到响应都不是单独结论。CORS 拒绝读取并不保证动作未执行。排除重新认证、SameSite、Origin 校验和幂等操作；允许的跨站工作流不是缺陷。

## Agent 行为

浏览器完成请求可行性验证，工具读取权威状态；只使用测试账号并及时恢复。登录 CSRF 与账户绑定场景还需核对最终身份，见 [OAuth/OIDC](oauth-oidc.md)。

## 调研来源

- [PS-csrf · CSRF](https://portswigger.net/web-security/csrf)
- [MDN-cors · Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
