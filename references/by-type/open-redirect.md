# 开放重定向与转发

适用信号：return URL、登录后跳转、链接中转、服务端 forward

## 检查与最小实验

先区分服务端 Location、客户端导航、内部 forward。用获准受控落点检查解析后的 scheme/host/port，而非只检查文本前后缀；记录浏览器最终 URL 与全部跳转链。

只在输入验证代码或实际行为支持时，检查相对 URL、编码和多层解析差异；不要把一份历史 URL 变体表无条件跑遍目标。

## 证据与反例

页面里出现链接、被拒绝的 URL、正常允许的链接中转不等于违规重定向。若声称 OAuth 凭据泄露，要证明凭据实际到达受控落点；单纯开放跳转不自动获得该影响。

## Agent 行为

不向真实用户发送链接，不跟随到未授权站点。单项是否收录按具体 SRC 规则；风险链未验证时明确写潜在条件，见 [OAuth/OIDC](oauth-oidc.md)。

## 调研来源

- [OWASP-redirect · Unvalidated Redirects and Forwards](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
