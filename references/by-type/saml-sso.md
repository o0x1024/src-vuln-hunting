# SAML SSO

适用信号：企业 IdP/SP、SAMLResponse、Assertion 消费

## 检查与最小实验

从正常测试登录记录 IdP、SP、ACS、请求 ID、签名覆盖节点和最终使用的身份字段。先用离线 XML/验签工具追踪“被验证的节点”与“被业务消费的节点”是否同一对象。

分别核对受信 IdP 证书、Audience、Recipient/Destination、时效、重放与流程关联。对签名包装线索只使用测试断言和隔离环境，避免把重复 XML ID 当成已绕过。IdP 发起与 SP 发起模式不同，缺 InResponseTo 需要结合实际 flow。

## 证据与反例

Assertion 未单独签名不一定有问题，合法签名的整个 Response 可覆盖它；自签名 IdP 证书也不等于不可信。应证明未受信身份/属性被用于建立会话，或不应接受的断言被实际消费。

## Agent 行为

敏感断言离线处理，使用自有测试身份。需要新增 IdP、改信任或跨 SP 的动作只按现有许可执行；缺条件则记录协议线索并继续其他分支。

## 调研来源

- [OWASP-saml · SAML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

## SSO登录提示与已验证会话主体

旧图以阻断/删除Cookie、改saml?login邮箱后“登录另一账号”的流程描述风险，未提供SAMLResponse、实际IdP认证与SP会话证据。查询邮箱可仅是登录提示/账号选择，不应代替经过信任验证的断言主体；还需排除IdP残留登录、合法委派、错误页和仅UI变化。

对获准两个合成身份或已有脱敏日志，串起登录提示、AuthnRequest关联、IdP认证主体、被验签Response/Assertion、业务消费身份字段、SP稳定账号ID与新会话能力。浏览器清一个站点的Cookie不保证另一个IdP身份已退出；提示值变化只有在错误主体真正用于会话/资源授权时才支持接管。保留拒绝/合法提示反例，不登录真人身份、安装Cookie编辑扩展或改企业SSO信任。


## SAML浏览器往返的SP与IdP信任边界

图画SP产生请求、浏览器转IdP认证、IdP响应经浏览器送ACS再登录，没有签名检查实现。

绑定SP/IdP/ACS、请求身份及会话、被验签的具体节点、issuer/audience/recipient/时间和重放检查；合法登录序列、只存在SAML响应、缺签名实现或配置不匹配是反例。流程图用于定位校验点，不能补出签名绕过。

来源：[保存帖1](https://x.com/i/status/1441792688769011715)。


## SAML 会话签名产物与服务端身份接受分别取证

图显示会话数据解码、签名生成和 Cookie 页面，但浏览器仍展示登录界面。

定位真正的签名验证者、密钥来源、主体绑定与会话创建条件，再核服务端是否接受及最终角色。生成字符串不代表伪造成功；Cookie 的 HttpOnly/Secure 属性也不能弥补签名或主体校验缺陷。保留字段关系，不复制令牌值。

来源：[保存帖1](https://x.com/i/status/1524443563156963328)。


## SAML 的 XML 解析与签名绑定需分别核对

实体及XML属性是解析候选，签名绕过则取决于验证的节点与最终消费的断言是否同一个对象。记录解析器、实体开关、canonicalization、ID唯一性及签名引用；在受控身份用有效/无效签名、重复节点或实体被禁的对照，确认实际subject/audience/时效/会话变化。单纯XML能解析或异常并不等于签名绕过或SSO接管。

来源：[保存帖1](https://x.com/i/status/1632781442324520960)。


## SAML 端点反射不能推断断言校验绕过

协议入口收到非正常 SAMLResponse 后可能走错误页 HTML sink，应单独记录 XSS 输出验证与 XML/assertion 的签名、issuer/audience、时效和会话绑定。保存片段无有效断言/登录结果；字符串在 SAML 参数中不自动是 SAML auth bypass 或 XXE。

来源：[保存帖1](https://x.com/i/status/1660289196420890624)。


## RelayState 保存后的下一次登录重定向需独立校验

GitLab摘要称SAML登录POST的RelayState外跳被保存在cookie，后续signin又导航。审查协议回调/返回URL规范化、会话与浏览器状态绑定、可保存/可消费时点，以自控允许/拒绝目的地比较每跳。token偷窃断言没有完整保存的第三方交换链，开放重定向、持久导航与各OAuth token consumer分别证明，不推所有第三方ATO。

来源：[保存帖1](https://x.com/i/status/1663485784618311680)。

保存图片 `1663485784618311680-02.jpg`：GitLabSAMLRelayStateURL不充分校验redirect且cookie保存，后续signin再次转，作者token偷窃断言而截图未完整oauth链；persistentnextredirect独立state/callback/tokenconsumer，不推所有第三方ATO。本段仅使用实际查看的保存原图，不补未保存内容。


## 保存图证0195-102-saml：1720369940191178979-02.jpg

Java doFilter截图在authenticateUser false且无SAMLResponse时检查isStarshipRequest，若无USER_IN_SESSION创建ProductAccess loginName admin，rest/user/session/roles值来自X-Starship-* headers，roles equalsadmin设Admin并调用validateAllowedOperations后写session。isStarshipRequest与authenticateUser函数未给，不能推任意header即bypass。核入口可信代理header清理、predicate/凭据校验、session创建与最终权限，在隔离fixture比较可信/伪造header与拒绝控制；标题CVE不替版本或完整漏洞确认。

实际保存图：1720369940191178979-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1720369940191178979)。
