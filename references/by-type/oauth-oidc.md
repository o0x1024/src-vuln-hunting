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

## 调研来源

- [RFC-oauth · RFC 9700: Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
