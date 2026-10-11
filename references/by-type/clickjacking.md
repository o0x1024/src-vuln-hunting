# 点击劫持

适用信号：敏感操作页面可被不可信站点嵌入

## 检查与最小实验

先检查实际响应的 frame-ancestors / X-Frame-Options 与浏览器嵌入结果，再确认嵌入后是否仍带有效身份、有敏感可操作控件。用受控页面和自建账号演示一个获准的可逆操作。

保留浏览器版本、视口、点击落点和权威状态变化；存在重新认证/确认步骤时纳入实际交互链。只验证页面可加载不能替代动作可达。

## 证据与反例

缺防嵌入响应头、静态宣传页可 iframe 加载，不足以证明业务影响。CSP 阻止嵌入或第三方 cookie 策略使身份不可用时，应限定结论。

## Agent 行为

仅做自我控制的界面验证，不向用户投递诱导页面；按项目是否接受该类型及实际影响定级，不自动和 CSRF 合并。

## 调研来源

- [PS-click · Clickjacking](https://portswigger.net/web-security/clickjacking)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

CSP与X-Frame-Options的关系按有效指令、交付方式与浏览器版本判断：CSP中的其他指令不自动覆盖X-Frame-Options；[CSP3工作草案frame-ancestors与XFO关系](https://www.w3.org/TR/CSP3/#frame-ancestors-and-frame-options)规定资源交付的enforce策略含frame-ancestors时忽略XFO（2026-10-09核对）。记录实际响应、有效策略与受控嵌入结果，不能用“CSP是XFO敌人”推导可点击劫持；响应不能嵌入也不说明[CSRF](csrf.md)请求必然未发生。

## 嵌入API与响应保密性

Cookie认证的API能在iframe中加载，不代表外站脚本可读取其私密正文；同源策略、嵌入许可、自动身份和可诱导的敏感控件分别核对。纯JSON/资料展示没有可操作控件时不能仅凭iframe代码确认点击劫持；读取主张应另转[CORS](cors.md)或[XSSI](xssi-jsonp.md)，状态侧信道转[XS-Leaks](xs-leaks.md)。只检查自有账号的合成内容与可逆动作，不“收集受害者数据”。


## 缺响应头的 clickjacking 通知不是敏感动作证明

完整奖赏图写lack of sensitive headers leads clickjacking300，正文建议检查每个项目，没有响应/CSP、可嵌入页面或动作结果。

离线自有两个origin比较XFO/CSP frame-ancestors、实际嵌入、会话Cookie策略与敏感合成动作是否被误触。缺header、能框公开页面或奖赏不是影响；浏览器拒绝、无动作或额外确认为反例，先绑定项目资格与行为规则而非批量检查全部站点。

来源：[保存帖1](https://x.com/i/status/1495240347756077057)。


## 多步点击覆盖样例与拖放标题并非同一机制

保存图实际是透明 account iframe 叠在两个提示点击位置，未见拖放数据处理。需核对可嵌入策略、frame-ancestors/X-Frame-Options、页面布局/滚动、各次点击与最终敏感操作；用自有账户比较正常与覆盖操作。CSS opacity/z-index 和两个标签只说明布局候选，不证明成功诱导或权限绕过；不把点击例子改写为已实现的拖放漏洞。

来源：[保存帖1](https://x.com/i/status/1649810040205762563)。

现有图片证据 `1649810040205762563-02.png`：样例为opacity0.1/z-index2的accountiframe覆盖firstClick/secondClick两位置标签；不是dragdata代码，需实际framing policy/UIstate/action，帖子drag标题与click例子不一致。


## 可嵌入页面与诱导提交链需要独立证据

同报告把 clickjacking 当 XSS 触发辅助，必须分别确认 frame-ancestors/X-Frame-Options、受害主体、自控嵌入层、可见交互和 onsubmit 后实际保护操作。允许嵌入不等于可以诱导特定动作，视频封面不能补用户点击序列。仅在自控两页面验证，无外部用户诱导。

来源：[保存帖1](https://x.com/i/status/1654237184184991745)。

保存图片 `1654237184184991745-02.jpg`：Expedia origCity UPPER/WAF title，onsubmit需点击并声称clickjacking，视频封面未播放；eventtrigger/大小写HTML和JS不同、iframe可嵌入不等完整诱导。 本段只使用已保存且实际查看的内容。


## 页内目标在底部时的 iframe 定位与同源限制

正文建议 auto-scroll iframe。先确认目标可被嵌入并在实际浏览器找到可交互元素，再验证用户点击后的业务效果；跨源父页不能任意访问 iframe DOM 或执行滚动脚本。可用位置布局或受控交互的实际效果必须录证，自动滚动建议不等所有跨源页面都可控，更不消除点击和敏感操作前提。

来源：[保存帖1](https://x.com/i/status/1685761181188083712)。


## frame ancestors 子域模式与基域匹配须实际验证

正文策略 `frame-ancestors 'self' https://*.foo.foo:*` 并建议检查 http://foo.foo 是否 claimed。scheme、wildcard 子域、基域和端口各是不同匹配条件，http 基域不能据字面视为该 https wildcard 的允许源。先在实际策略/浏览器版本核对 framing，再判断获准控制的源是否匹配及敏感点击可达；域可注册也不自动绕过 CSP，更不授权注册真实第三方域。

来源：[保存帖1](https://x.com/i/status/1687019472438321153)。


## 保存图证0192-142-click：机制与验证条件

保存图片 `1711668027350233180-02.jpg`：Burp1274695历史2021摘要描述headlessChrome远程调试WebSocket端口、已知Chrome XSS+JS端口探测/clickjacking→取得debugGUID，再经download写user.vmoptions，下一次Burp启动及OOM参数才触发OS命令。多步本地配置/未来启动是前提，非单iframe即时RCE；视频与完整步骤未保存。审计调试通道transport/文件写权限/重启与预算，隔离无害标记验证，不探端口、写启动参数或制造OOM。

来源：[保存帖1](https://x.com/i/status/1711668027350233180)。


## 0194：点击劫持以敏感动作而非登录页为验证单位

正文建议关注每个敏感动作。应在自有页面确认目标可被嵌入、有效 frame-ancestors/X-Frame-Options、实际用户手势、会话、目标按钮与最终状态改变，比较保护开启和顶层访问。iframe 可见本身、诱导截图或奖励通知不等于动作成功；无需在他人会话上试验。

来源：[保存帖1](https://x.com/i/status/1715366514721988867)。
