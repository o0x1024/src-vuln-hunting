# 悬空 DNS 与子域接管

适用信号：CNAME 指向失效第三方资源、停用站点或域绑定错误

## 检查与最小实验

记录 DNS 链、TTL、服务商错误页及资源归属；再查该服务商当前绑定/验证流程、资源名称复用限制和保留期。悬空引用与可被另一租户重新声明是两个条件。

先用只读证据判断可声明性；实际注册资源、绑定域名、申请证书或改变 DNS 只有项目明确允许该验证动作时才执行。使用可回收测试内容并核对已有用户流量影响。

## 证据与反例

NXDOMAIN、404、旧指纹命中、同名资源看似可创建，不单独证明接管；TXT 所有权验证、服务商防复用和保留期可能阻止绑定。第三方服务状态变化不产生目标授权。

## Agent 行为

证据不足记“悬空 DNS / 可接管性待证”。不收集真实访问者 cookie、邮件或流量；不把 Azure 的具体规则套给其他 SaaS。

## 调研来源

- [Azure-dns · Prevent dangling DNS entries and avoid subdomain takeover](https://learn.microsoft.com/en-us/azure/security/fundamentals/subdomain-takeover)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
