---
name: src-vuln-hunting
description: 面向合法授权的 SRC（安全应急响应中心/众测平台）漏洞挖掘方法论：范围合规、资产测绘与信息收集、高价值漏洞检测（业务逻辑/越权优先）、按漏洞类型（SQL注入/WAF绕过/XSS/SSRF/越权/上传/RCE等）的实战技巧、云安全（云配置错误/IAM/容器/K8s）排查、最小化验证留证、漏洞报告编写。需要制定 SRC 渗透测试方案、梳理挖洞经验、排查云安全漏洞或编写漏洞报告时使用。
---

# SRC 漏洞挖掘方法论

面向合法授权的 SRC（Security Response Center / 众测平台）的漏洞挖掘工作流。**仅可在目标平台明确授权的范围内测试**，超范围行为属于非法入侵。

## 何时使用
- 用户要针对某个 SRC 平台进行漏洞挖掘
- 需要制定授权范围内的渗透测试/安全测试方案
- 需要整理 SRC 挖洞经验、方法论或检查清单
- 需要编写或评审漏洞报告
- 需要排查云安全漏洞（云配置错误/IAM/容器/K8s）或编写云安全文档

## 铁律（优先级高于一切）
1. 只在授权范围内测试，范围外资产一律不碰
2. 红线行为（DDoS、社工、暴力破解、批量拖取真实用户数据、破坏性操作）绝对不做
3. 最小化验证：能证明危害即可，不做数据导出/破坏
4. 全程留证：请求包、响应、截图、时间戳、复现步骤

## 工作流总览
| 阶段 | 内容 | 参考文件 |
|---|---|---|
| 1 规则先行 | 通读范围/评分/规范，确认红线 | references/scope-and-rules.md |
| 2 资产测绘 | 子域名/端口/指纹/JS/移动端/云资产 | references/asset-discovery.md |
| 3 漏洞检测 | 逻辑/越权优先，再经典 Web 与组件 | references/vuln-detection.md |
| 4 验证留证 | 最小化验证 + 证据留存 | references/verification.md |
| 5 报告提交 | 结构化报告，可一键复现 | references/reporting.md |
| 6 运营复盘 | 新业务/活动/复盘 | references/checklist.md |

## 价值排序（决定投入优先级）
业务逻辑漏洞（越权/支付/验证码/竞态）> 未授权访问 > 认证与访问控制缺陷 > 经典 Web 漏洞（OWASP Top 10）> 组件历史 CVE > 基础设施未授权。

常规 Web 漏洞被挖得多、审核严；**业务逻辑漏洞是 SRC 高分值洼地**。

## 按漏洞类型速查（references/by-type/）
| 类型 | 文档 | 高价值点 |
|---|---|---|
| SQL 注入 | sql-injection.md | 报错/盲注/堆叠、二次注入 |
| WAF 绕过 | waf-bypass.md | 编码/注释/参数污染/分块传输 |
| XSS | xss.md | 存储型优先、DOM XSS 与 CSP 绕过 |
| SSRF | ssrf.md | 云元数据、内网 Redis、gopher |
| 越权/访问控制 | idor-access-control.md | 水平/垂直越权、未授权访问 |
| 认证与会话 | authn-session.md | 密码找回、JWT、OAuth |
| 文件上传 | file-upload.md | 双扩展、图片马、解析差异 |
| 命令注入/RCE | cmd-injection-rce.md | 拼接符、SSTI、参数注入 |
| 反序列化/RCE | deserialization-rce.md | fastjson/PHP/Java gadget |
| 文件包含/路径穿越 | lfi-path-traversal.md | 伪协议读源码、日志投毒 |
| 业务逻辑 | business-logic.md | 支付/验证码/竞态/流程绕过 |

## 云安全速查（references/cloud/）
| 主题 | 文档 | 高价值点 |
|---|---|---|
| 云安全总览 | cloud-security.md | 云攻击面、权威源（MITRE 云矩阵/OWASP K8s Top10/CSA） |
| 云配置错误 | cloud-misconfiguration.md | 暴露存储桶、公网数据库、备份/快照/KMS |
| 云 IAM | cloud-iam.md | 过度授权、跨账户信任、硬编码凭证、STS |
| 容器与 K8s | container-k8s-security.md | 特权容器、RBAC、kubelet、NetworkPolicy、Secret |

## 使用方式
1. 先读 references/checklist.md 掌握全流程检查点
2. 按阶段进入对应参考文件执行
3. 按漏洞类型查 references/by-type/ 下对应技巧文档
4. 云安全排查查 references/cloud/ 下对应文档
5. 产出：资产清单、验证证据、结构化漏洞报告
