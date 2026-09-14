# Web 缓存投毒

适用信号：输入影响响应但未进入共享缓存键

## 检查与最小实验

先识别共享缓存与真正生效的键：路径、query、Host/端口、编码、Vary 等。只在项目提供或已证明隔离的测试缓存空间用无害标记；随机 query 不保证隔离，因为它可能根本不入键。

在受控会话写入标记，再由独立干净客户端以正常请求验证复用；保留变体前后响应、Age/Cache 头、内容差异、编码协商和过期信息。正常响应对照必须落在同一待测键，隔离性验证使用不同键，不能混为一谈。

## 证据与反例

反射标记、单次 HIT、速度变快都不能证明投毒影响另一请求。HackerOne #1096609 的复核过程表明 Accept-Encoding 差异可能影响复现；其最终影响按平台时间线记录，不能照抄标题的 DoS。

## Agent 行为

无法隔离共享缓存就只记录候选/本地复现，不污染公共热门路径。验证后清除已授权测试键或记录过期与交接，不全站 purge。缓存规则误把私密页面当静态资源转 [缓存欺骗](cache-deception.md)。

## 调研来源

- [PS-cache-poison · Web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning)
- [H1-cache · Report #1096609: Host header web cache poisoning](https://hackerone.com/reports/1096609)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
