# 容器与 Kubernetes

## 适用信号与前提

容器配置、镜像材料、API Server/kubelet/dashboard、RBAC、挂载和 NetworkPolicy。先确定可用视角：外部 API、授权只读身份、用户提供配置或自建集群；缺少内部身份不等于完成内部审计。

## 最小实验

- 镜像/配置：仅分析已提供或获准下载的材料，记录版本、权限、危险挂载及凭据位置；不自动拉取私有镜像。
- API：用获准身份或匿名请求访问指定非敏感测试资源，记录响应语义与授权结果；不枚举所有命名空间、Secret 或执行容器命令。
- RBAC：分析实际绑定、规则与身份，必要时用允许的权限自查/测试资源读取确认；不要修改角色验证。
- 网络隔离：使用已授权测试工作负载及预期隔离关系。缺少 NetworkPolicy 是线索，不能独立证明跨租户可达。

## 确认与反例

`--anonymous-auth=true` 表示接受匿名身份，不等于该身份拥有敏感权限；仍需有效授权规则与实际资源访问证据。[Kubernetes 官方说明](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#anonymous-requests)。健康端点可匿名访问不直接构成漏洞。

特权配置、docker.sock、可写宿主挂载是风险线索；是否可利用取决于已有权限与实际环境。Secret 的编码表示不能代替对存储加密和访问控制的判断。公网 API、版本信息或默认错误响应不能证明集群接管。

## 下一步、停止与报告

逃逸/提权机制研究仅在自建隔离环境；不在目标创建特权 Pod、挂载宿主、修改 RBAC、读取 Secret 或持久化。明确区分配置审计与目标动态验证。

报告记录组件/版本、预期边界、身份/资源、有效配置与访问结果、修复方向和限制。遵守 [验证](../verification.md)。

## 调研补充：有效权限的证据

记录主体、namespace、resource/subresource 与 verb；RoleBinding 引用 ClusterRole 仍可能只授予某 namespace 的权限，不能仅按角色名认定全局权限。匿名认证与 RBAC 授权分开，健康端点公开不证明可读 Secret 或可 exec。用授权策略/测试资源核对具体能力；不从特权配置线索直接宣布容器逃逸。

## 调研来源

- [K8S-rbac · Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [K8S-anon · Anonymous requests](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#anonymous-requests)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

Docker端口可达、系统信息可读、容器命令可执行和宿主能力是不同边界。先核对daemon/API身份、TLS/授权配置及获准非敏感材料；docker info给安装/系统概况和数量，不能据此称已取得每个容器详情或shell。容器命令执行也不自动证明宿主root，需实际挂载/权限/隔离证据；不把源帖docker exec /bin/bash作为线上验证步骤。官方语义：[Docker system info](https://docs.docker.com/reference/cli/docker/system/info/)（2026-10-09核对），未连接目标daemon。

Docker容器列表区分默认运行中条目与--all包含的所有状态；--all不是“只列停止容器”。记录实际API、身份、返回字段及允许受众，列表可读仍不证明exec或宿主能力。[Docker container ls](https://docs.docker.com/reference/cli/docker/container/ls/)（2026-10-09核对）支持这一命令语义，未发起daemon请求。

## exec的对象、生命周期与已授予控制

[Docker exec文档](https://docs.docker.com/reference/cli/docker/container/exec/)说明它在运行中的容器启动新命令，主进程生命周期、可执行文件及用户/环境设置影响结果（2026-10-09核对）。源词containertag不能直接当镜像tag；此处操作对象是容器名称/ID，镜像含bash与否也需实际材料。

先记录所连daemon、身份与exec授权、容器对象及实际进程权限。已获准管理员进入自己的容器查看运行状态是合法管理能力，不能写成外部利用、读取生产secret许可或宿主逃逸。这里只分析语义，不连接daemon、启动shell或读取容器环境秘密。

## 镜像仓库目录、清单与层表示

/healthz不是Docker Registry V2的通用匿名授权证明。仓库目录、tags、manifest/index、config与layer是不同资源；[Distribution V2目录说明](https://distribution.github.io/distribution/spec/api/#listing-repositories)指出目录可按实现/身份限制并分页，缺少条目不证明不存在。[OCI1.1.1 manifest](https://github.com/opencontainers/image-spec/blob/v1.1.1/manifest.md)区分单平台清单与index，层可为tar、gzip或zstd，不能照旧帖把所有blob统一当tar.gz（2026-10-09核读相关段落）。

从获准已有清单绑定registry/namespace/主体、tag解析时点、digest、mediaType与实际读取策略；公开镜像的预期可读不等于私密源代码泄露。一个目录结果不证明能读全部层，层可读也不自动证明可写仓库、容器执行或宿主权限。仅分析最少脱敏元数据，保留分页/未知类型/失败缺口；不批量下载镜像、解包未知归档、运行层内程序或删除/推送制品。

## EKS配置链、Secret列表权限与终端表示

旧图从AWS临时凭据、集群名称与update-kubeconfig走到kubectl get secrets，但没有最终API响应。AWS API身份、集群选择、kubeconfig上下文、集群认证主体、namespace和RBAC verb需逐边确认；写本地配置不等于取得集群权限，命令出现在截图不证明执行成功。

终端默认表格没显示data不能说明list仅有元数据。[Kubernetes Secret实践](https://kubernetes.io/docs/concepts/security/secrets-good-practices/#configure-least-privilege-access-to-secrets)指出Secret的list授权可取得其内容（2026-10-09核读相关段）。审阅获准策略及脱敏合成API记录时区分服务端返回能力与客户端展示，不因表格隐藏或Base64而低估暴露；同时合法管理员已有权限不是外部漏洞。只记录有效主体/对象/verb与不可逆指纹，不运行源命令、更新真实kubeconfig、读取生产Secret或创建Pod。


## RBAC图中的绑定范围与旧PSP准入

Krane图分Subject、Binding、Role、Rule、namespace/cluster-wide，并列resource的API group/verb/name、non-resource URL及旧PSP属性。先从绑定主体到roleRef及规则恢复当前权限，不能把角色名字或图中相连箭头当实际集群生效。[Kubernetes RBAC说明](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)指出RoleBinding引用同namespace Role或将ClusterRole绑定到该namespace，ClusterRoleBinding用于集群范围（2026-10-10核读相关段落）。

RBAC是否允许具体API动作与工作负载是否通过准入不同；图中privileged false不保证所有有效路径都满足约束。[PSP说明](https://kubernetes.io/docs/concepts/security/pod-security-policy/)记录1.21弃用、1.25移除，当前需绑定实际版本及Pod Security Admission/其他准入实现。资源/非资源路径、名称限制、主体namespace和实时绑定分别核对，只分析获准配置/离线图，不部署Pod、提权或以旧图声称当前防护。来源：[保存帖](https://x.com/i/status/1401664424885342213)。


## Compose服务声明与主机暴露和配置内容

旧帖建议留意docker-compose.yml，图列MySQL5.7、phpMyAdmin、WordPress及环境变量、端口、卷、网络，多数值遮盖。文件名候选、HTTP实际返回配置、部署消费者和当前访问能力分开；环境字段名称不证明有效秘密，depends_on不是认证边界。

从获准制品核对插值来源、实际运行环境、容器与主机端口、监听地址、挂载源/目标及公开读者，保留未部署/旧副本/错误页反例。图中容器端口/卷意图不能补当前主机路径或外部可达，遮盖值不恢复。本批未获取真实配置、登录数据库、部署Compose或使用凭据。来源：[保存帖](https://x.com/i/status/1404012291197001735)。


## 容器发行版与linuxkit内核及宿主身份

Docker图同时出现Ubuntu18.04.2、Tomcat6文件、CentOS4.9/glibc2.3.4及4.9.125-linuxkit内核。容器的用户态版本、运行内核、已有root身份与宿主权限属于不同层。

关联容器镜像摘要、运行时/宿主、有效capabilities、挂载与实际服务配置；安装旧文件不证明该服务运行或可达。wmiexec密码提示和半交互shell是已有认证流程，不能与容器root画面拼成未认证宿主接管。

来源：[保存帖1](https://x.com/i/status/1413029188311785472)。


## Cilium架构图与有效eBPF策略及身份覆盖

Cilium图从Pod/CNI到kernel eBPF并标policy/logging/metrics，说明架构分层，未给当前部署、附着点、身份标签或有效规则。

绑定获准workload/node、网络方向、身份标签、实际附着和生效策略，用同次受控允许/拒绝流与日志判断覆盖。仅组件存在、metrics有值或架构图不证明策略启用；标签失配、未管理端点与不经过附着点的流需分别保留，不能计全群集隔离已验证。

来源：[保存帖1](https://x.com/i/status/1416522212274802690)。


## 虚拟机与 Kubernetes 安装回执的状态分层

Windows实验图有ISO下载、KVM/VNC及驱动准备；Kubeapplier列30/30 Applied与黑名单，Kubernetes Goat图为实验目录。

区分素材准备、配置提交、运行健康、网络可达、身份权限和实验漏洞回执。Applied不是健康部署，实验主页不是生产发现；缺驱动、进程未启动、RBAC拒绝、未暴露及实验内容没有执行是反例。本次不下载、安装、创建VM/Pod或修改集群。

来源：[保存帖1](https://x.com/i/status/1459268482000994305)、[保存帖2](https://x.com/i/status/1461322003755978752)、[保存帖3](https://x.com/i/status/1461442702730571776)。


## Whoc runtime 图与容器初始权限

图示runtime执行/proc/self/exe，容器再打开、execve上传进程并发送fd，未存真实文件内容/运行日志。

区分允许运行镜像的既有权限、映射的文件描述符、读取权限、runtime对象来源与传输结果。架构图不证明逃逸/root/初始入口；无host引用、无读取权、隔离runtime、无上传或预置权限为反例。仅静态读图，不运行容器、读host runtime或发送文件。

来源：[保存帖1](https://x.com/i/status/1463496317972451329)。


## DetectionLabELK 的采集检测存储三阶段

架构图从Windows/DC事件、beats、osquery/Velociraptor/Sysmon/Suricata/Zeek至ELK，并列RDP/SSH/web发布端口。

绑定每阶段配置版本、事件源身份、时间、采集回执、解析规则和存储/查询结果；拓扑图不证检测命中或外网暴露。丢事件、错时区、缺权限、端口未发布或只预设图为反例，不部署实验栈、连接RDP或读云日志。

来源：[保存帖1](https://x.com/i/status/1465066622968868873)。


## Tarian 的注册、同步与检测动作

完整架构图含CLI/UI注册、config/analytics DB、RBAC/dex/openEBS、sidecar同步、已知威胁动作/自毁pod、未知变化告警、社区数据和FluentBit聚合。

把声明的工作流与真实部署/权限分开，绑定配置来源、容器/进程身份、观察时间和动作；社区共享数据需验证，检测告警不证明拦截。只拓扑、未注册、不同配置或无回执为反例，不部署、备份恢复或销毁pod。

来源：[保存帖1](https://x.com/i/status/1469415278002024455)。


## 空 Docker registry 匿名可见不等可利用写入

正文称私人registry空且无需认证可上传，询问怎么利用，没有目录对象、push权限、镜像或消费者。

离线自有registry权限矩阵分目录/manifest/blob读取、写入、标签更新和部署消费者，明确预期公开/私有。空列表、返回200和作者可上传说法不足以证明受限写入或执行；无实际对象/部署为反例，不上传镜像或修改真实registry。

来源：[保存帖1](https://x.com/i/status/1498913816104431616)。


## 容器攻击链逐阶段证明权限跨越

将文件上传、主机提权、容器环境探测、逃逸、集群访问和持久化拆成独立阶段。每条边记录前置权限、实际配置或版本、动作和观测结果；SUID、cron、容器标记与历史 CVE 名称只是候选。某阶段成立不能自动推导宿主或集群管理员权限，也不要在提炼时执行链中动作。

来源：[保存帖1](https://x.com/i/status/1532168807896211459)。


## Docker 列表可读与宿主机控制分阶段验证

截图中的容器 JSON 含容器标识、镜像与命令字段，只支持列表信息可读这一观察。记录访问身份、管理端口是否在范围、API 版本和具体端点；列举、配置读取、创建/执行、挂载宿主路径是不同权限与副作用。不要把开放端口或容器列表直接称为宿主机 RCE；本轮未创建容器或执行截图命令。

来源：[保存帖1](https://x.com/i/status/1536357392601927680)。


## 内核调试环境须匹配符号与真实隔离边界

like-dbg图显示ARM64源码、反汇编、线程和SIGINT调用栈，正文称Docker部署调试内核。先核对实际运行内核、架构、镜像/源码/符号版本、调试接口、权限及虚拟化边界；普通容器共用宿主内核，不能凭Docker标题推定安全沙箱。只在授权独立可恢复环境规划，停线程或已有root/debug权限不是漏洞结果，不在用户宿主启动未知镜像或内核操作。

来源：[保存帖1](https://x.com/i/status/1568653025782079489)。


## kubectl秘密读取需按当前RBAC及响应最小化

保存建议仅围绕 kubectl get secrets。先记录自有集群/namespace、有效身份、具体 verb 与资源权限，区分列元数据、读取单个对象和跨 namespace 访问。具有管理权限时读取通常符合设计；不要导出全部 Secret 或把 base64 编码当加密强度。用隔离无敏感对象和拒绝身份对照证明边界。

来源：[保存帖1](https://x.com/i/status/1570119332323270656)。


## 公开 cAdvisor 指标与容器控制分开证明

图摘要指出cAdvisor8080公开性能/资源指标，作者称连续监控发现，没有完整响应或监控配置。核对当前资产范围、部署、认证、指标政策与最少自有字段，再追踪差异来源/时间和实际验证；端口名/性能信息不证明容器权限或RCE。监控声称不等于已观察全部历史，不补造主动探测记录。

来源：[保存帖1](https://x.com/i/status/1584674143185895424)、[保存帖2](https://x.com/i/status/1585468941480124416)。


## 防火墙命令清单需审计方向、规则顺序及默认策略

iptables 图先 flush/delete-chain，再允许 loopback、established、部分 SSH/HTTP/DNS，INPUT DROP 而 FORWARD/OUTPUT ACCEPT。可提炼的是离线审查现有 ruleset 的链方向、state、地址和默认策略，以及修改可能中断管理或扩大转发的边界。比较自有隔离规则副本与流量矩阵，记录修改前后规则；允许端口不代表受限服务安全，INPUT DROP 也不等于全部流量限制，不直接执行归档清空命令。

来源：[保存帖1](https://x.com/i/status/1587107216733372416)。


## KubeEye 架构的 OPA 与节点日志：规则发现和有效权限分开

1597221269505712128-02.png 显示节点日志/Problem/Condition Manager，经 API server 对 RBAC、workload、node 使用 OPA 规则审计。保留配置快照、规则版本、触发字段、评估身份与缺失/不可读项，区分健康告警、策略不符和实际权限链。架构图不包含 exploit 或已部署成效；仅用自有离线配置评估，不因工具发现 HostNet/RBAC 标签就声明提权或创建集群资源。

来源：[保存帖1](https://x.com/i/status/1597221269505712128)。


## 历史保存帖0153：聚合 API 控制后的重定向客户端边界

Kubernetes 历史报告先控制 metrics-server 镜像或 kube-system 匹配标签的pod，再返回30X，使调用客户端转向内部端点。审计控制聚合服务的现有权限、每跳目的地、跟随策略、转发认证和客户端可达性；这不是零前提 SSRF。对AKS版本及其他云的作者泛化不当当前事实，裁切PoC不补写，仅自有桩服务器模拟。

来源：[保存帖1](https://x.com/i/status/1601666082363809793)。

已实际查看保存图片 `1601666082363809793-02.jpg`：Kubernetes 历史报告：需先控制 aggregated API 如 metrics-server，修改镜像或在 kube-system 匹配标签的 pod，使其返回30X，调用客户端跟随到内部端点。提炼聚合服务控制权限、每跳URL目的地/转发认证和客户端实际行为；报告对AKS/all versions及其他云的推测不当当前通用结论，图下方PoC裁切。


## Kubernetes 工具清单覆盖不同审计层而非可运行扫描计划

正文只有kube-hunter、kubeaudit、KubiScan、kubesploit、kubernetes-rbac-audit、peirates链接。将之作为网络暴露、工作负载配置及RBAC候选入口，先界定cluster/namespace/serviceaccount和只读权限；尚未读实现，不声称工具默认无副作用。自有最小manifest和角色配置做静态正/反例，真实cluster只能按明确范围验证实际权限，工具名字不证明漏洞。

来源：[保存帖1](https://x.com/i/status/1615067850326032384)。


## 镜像扫描、仓库管理与漏洞验证的职责区分

Docker帖子列Trivy、Clair、Harbor、Grype、Dagda等仓库；这些项目角色不同，Harbor包含仓库管理与集成扫描能力，不能全部视为同一种独立扫描器。固定镜像digest、SBOM、包版本和数据库时间比较候选，区分构建依赖与运行时可达性；CVE命中不证明实际利用链。外部工具源码/文档未保存，本轮不声称已安装或运行。

来源：[保存帖1](https://x.com/i/status/1630634388865073165)、[保存帖2](https://x.com/i/status/1629780222294859778)。


## Docker 基线检查、监测与逃逸工具列表的角色拆分

列表含docker-bench/CIS/Lynis/Wazuh以及botb/Gorsair/ccat/deepce等外链，没有实际规则输出。先区分主机/容器配置基线、监测与逃逸候选，固定镜像/运行配置、挂载、capability和身份，单条配置不等于宿主控制。自有环境核对可达资源及隔离对照，外部工具不下载执行，历史清单不当当前安装说明。

来源：[保存帖1](https://x.com/i/status/1631977588724846592)、[保存帖2](https://x.com/i/status/1632353542433304577)。


## Argo CD 分片 reconciliation 必须执行命名空间限制

CVE-2023-22736历史摘要描述sharding启用时controller忽略Application namespace glob，argocd-*限制下other命名空间对象被reconcile；只有对象更新触发，攻击者需能更新Application。检查所有分片路径是否应用同一allowednamespace过滤以及Kubernetes RBAC/托管边界，固定配置、角色、更新动作和控制器日志。自有隔离环境对允许/禁止namespace与分片开关比较；截图称2.5.0-rc1起的历史范围不能扩写成所有当前版本。

来源：[保存帖1](https://x.com/i/status/1632440985362808834)。

现有图片证据 `1632440985362808834-02.jpg`：ArgoCD CVE-2023-22736历史摘要：sharding启用，controller未执行allowednamespace glob如argocd-*，other namespace app更新触发reconcile；攻击者须能更新Application，不能声称默认/所有当前版本或任意租户突破。


## Windows Runner 环境值空字节的权限前提

历史GHES CVE-2023-22381摘要要求已有权限控制一个GitHub Actions环境变量值且使用Windows runner，解析空字节可能注入其他环境项；图列3.4.15/3.5.12/3.6.8/3.7.5修复及3.8前范围。记录实际runner/服务版本、允许输入源、环境块构造与无副作用变量差异，排除本就能配置任意env的身份。历史摘要不是所有runner无认证RCE。

来源：[保存帖1](https://x.com/i/status/1633845276795617280)。

现有图片证据 `1633845276795617280-02.jpg`：GitHub Runner历史CVE-2023-22381摘要：已有控制一个环境变量值的权限、Windows runner、空字节导致设置任意其他环境变量；GHES 3.8前，图列修复3.4.15/3.5.12/3.6.8/3.7.5。Resolved/4000，缺实际字节与执行结果，不是无需权限所有runner通用RCE。


## Docker 工具和宿主逃逸题名按能力边界组织

正文列secret-diver、imgcrypt、confine、Falco及若干DockerWriteup链接，只有资源名称。分开镜像秘密静态审计、镜像加密/运行限制、运行事件监测、DockerAPI权限与容器到宿主边界；监测告警不是漏洞证明，容器内执行不自动宿主逃逸。未保存全文按覆盖但不补造实现，不下载/执行仓库或访问历史Docker目标。

来源：[保存帖1](https://x.com/i/status/1638254409132941312)、[保存帖2](https://x.com/i/status/1639584524584534016)。


## Portainer 到 Docker API 的题名保留每一步权限

保存材料只有2018报告/2023披露题名及Critical500状态，无SSRF入口或DockerAPI请求。链上分别确认服务端fetch、实际网络目的地、API认证和允许操作，再核对容器/宿主控制边界。内部API可达不自动创建容器或宿主RCE，评级不代替每步证据，不访问目标。

来源：[保存帖1](https://x.com/i/status/1638858409687613441)。


## IAM 到 Kubernetes 身份映射须绑定签名内容

aws-iam-authenticator 通过签名 STS GetCallerIdentity 映射 K8s username/groups。保存摘要提出未签 cluster ID 重放、提取 AccessKeyID 可改，以及允许其它 action；第三项作者明确缺 host/额外参数控制而影响低。审查校验字段与签名覆盖一致性、目标动作 allowlist、集群绑定及映射权限，用自有合法/拒绝 token 夹具，不把历史 all versions 声明推到现部署或使用真实 AWS 密钥。

来源：[保存帖1](https://x.com/i/status/1661734336146841605)。

保存图片 `1661734336146841605-02.jpg`：IAMauthenticator authenticate签名STS GetCallerIdentity映射K8s身份；未签clusterID重放、提取AccessKeyID可改影响映射、action非GetCallerIdentity作者称低影响因不能控host/addparams；历史allversions声明非现状。本段仅使用实际查看的保存原图，不补未保存内容。


## 构建目录权限与容器内 root 的影响分别界定

Cloudflare Pages v2 摘要称可替换两项构建可执行文件取得构建容器 root；目录却仅描述 user-readable，必须另证写权限或可替换父路径。审查实际 owner/mode、执行时身份与容器隔离，比较拒绝修改与自有普通构建产物。摘要明确 key 仅访问用户自己的 Pages，不能推宿主机 root/跨租户；权限收紧声明不是本次复测结果。

来源：[保存帖1](https://x.com/i/status/1662096608002027520)。

保存图片 `1662096608002027520-02.jpg`：Pagesv2目录描述user-readable但称能replace2exec build提升root，要writable或ancestor权限证实；keys只用户自身Pages容器，不证明跨租户或hostroot，tighten perms。本段仅使用实际查看的保存原图，不补未保存内容。


## worker 控制到 bastion 输出跨终端边界

保存截图描述先经 CI/docker socket 控制 worker，再让替换的 daemon 信息被 docker-machine 读取并输出到 bastion。逐段核对获得的 worker 权限、daemon 接口、输出消费者及终端对控制序列的解释。字符串进入终端不自动等于 shell 执行，worker root 也不等于 bastion root；截图下半 PoC 未保存，不补造控制序列或远端执行结果。

来源：[保存帖1](https://x.com/i/status/1664459733095333889)。

保存图片 `1664459733095333889-02.jpg`：docker-machine从worker返回version等信息给bastion输出escape sequence；需要CI任务已可通过dockersocket rootworker并替换daemon，然后ls输出，终端控制序列≠shellRCE，无PoC下半本段仅使用实际查看的保存原图，不补未保存内容。


## Docker Registry 的公开索引、镜像权限和源码内容分步验证

历史报告以 Shodan 和证书 CN 找到直接 IP 的 Registry v2，并称可下载镜像、可能含机密源码；保存图没有 catalog、manifest、blob 请求或实际内容。证书归属、域名不可达和 HTTP 200 不等于该 IP 在范围内或镜像私密。授权环境用自建公开与私有镜像对照匿名列表、manifest 和单个无敏感 layer 的权限，记录预期公开范围和实际身份，不下载整套第三方镜像。公开镜像或只暴露版本信息限制影响；“probably confidential”保留为假设。

保存图证 `1672311667055534096-02.jpg`：Registry 报告称镜像可能机密，图缺 manifest、blob 与匿名权限对照。

来源：[保存帖1](https://x.com/i/status/1672311667055534096)。


## Kubelet 调试端点取决于配置和实际暴露面

保存文字与图涉及历史 health/debug/pprof 接口、可能内存信息和有限资源耗尽，且明确不是所有默认配置都会暴露。记录组件版本、监听地址/端口、调试配置、认证授权与路由，使用无副作用配置检查区分端口可达、接口存在和数据敏感性。历史截图和概述不证明当前集群所有健康端口可访问或 RCE；不获取 heap dump、不施压端点或启动集群测试。

来源：[保存帖1](https://x.com/i/status/1679370000321355776)。

保存图证 `1679370000321355776-02.jpg`：Kubelet 健康端口未认证暴露 /debug/pprof 的历史摘要，可泄露内存地址/配置或有限 DoS，明确默认配置不暴露；版本阈值/健康端口不同权限与正式 API 需分清，不读取内存或做压力测试。


## LFI 到 Kubernetes 服务账号材料的影响边界

已确认文件读取时，/var/run/secrets/kubernetes.io/serviceaccount 目录可作为容器身份材料线索，不能读取目录名就假定泄露 token。用获准的最小证据区分 token、CA、namespace 等文件，并确认绑定、有效期、audience、挂载与 RBAC；CA 通常不是秘密，token 存在也不自动等于 cluster-admin。仅在既有授权范围验证必要权限，不以敏感文件名称或跳过 /etc/passwd 的建议代替真实影响。

来源：[保存帖1](https://x.com/i/status/1684712772989333504)。


## kOps GCP state bucket 权限可将 pod 立足点升级

保存摘要：kOps 给节点关联 service account 读取 state bucket 的权限，已有 pod shell 的用户可请求实例凭据读取 state 敏感材料，再转 cluster admin，进一步影响 control-plane GCP identity。历史测试 Kubernetes1.25.5/kOps1.25.3；先验证 metadata 可达、节点身份、state bucket IAM、敏感对象和后续真实权限，网络隔离或 least privilege 会阻断链。不是无初始权限远程接管，图片底部 setup 代码裁切不补全文。

来源：[保存帖1](https://x.com/i/status/1687554188841205769)。

已审阅原图 `1687554188841205769-02.jpg`：kOpsGCP节点serviceaccount可读statebucket，任意pod已有shell取得instancecredential→state敏感配置→clusteradmin→controlplaneGCPSA，测试Kubernetes1.25.5/kOps1.25.3；权限与metadata通路前提，setupexport后文裁切，非无初始立足点。


## etcd 2379 与历史 v2 API 暴露的最小检查（0187）

保存帖给出 `:2379/v2/keys/?recursive=true`。先核对该端口确为 etcd、是否启用 v2、TLS/客户端认证与网络隔离，区分通用响应和真实键访问权限。可读性与 Kubernetes 凭据泄露不是同一结论；用自有非敏感键或必要脱敏摘要证明边界，不批量递归导出密钥或使用发现的 token。

来源：[保存帖1](https://x.com/i/status/1691633374786392113)。


## 保存正文0193：docker-compose.yml 可发现配置，标题不证明秘密

正文仅给路径，图三个High报告标题。核服务入口、挂载、环境变量是字面秘密还是变量引用，比较匿名实际YAML与随机路径；200或报告数不能证明数据库/容器权限。禁止用其推所有部署都泄露同样内容。

来源：[保存帖1](https://x.com/i/status/1713461643407990838)。


## 0194：Ingress 可写字段到配置注入的连续边界

permanent-redirect annotation 与 spec.rules.http.paths.path 两报告图的前提都是 Ingress create 或 update 权限。前者描述未转义值入 nginx.conf；后者增加 log_format/access_log 写文件及 include 该文件的阶段。逐段核 RBAC、admission、配置语法、可写路径、reload、controller 身份和版本，用隔离无害配置标记与转义/拒绝控制。截图历史版本不证明当前版本受影响，缺完整 YAML 与执行结果，不能宣称匿名 Web RCE 或整个集群接管。

来源：[保存帖1](https://x.com/i/status/1717330577119179169)、[保存帖2](https://x.com/i/status/1717496437100134442)。


## 保存图证0194-112-container：1717330577119179169-02.jpg

Kubernetes ingress-nginx 报告描述有 create Ingress 权限的用户控制 nginx.ingress.kubernetes.io/permanent-redirect annotation，经未转义模板写入 nginx 配置。截图列出 minikube Kubernetes 1.26.3、controller v1.8.0、nginx 1.21.6，但没有 YAML、最终配置或命令结果。比较 RBAC、annotation admission、配置语法及 reload，并检查 controller 身份权限；不能推导成匿名 Web RCE 或整个集群接管。

实际保存图：1717330577119179169-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717330577119179169)。


## 保存图证0194-119-container：1717496437100134442-02.jpg

Kubernetes 报告截图描述有 Ingress create/update 权限的用户经 spec.rules.http.paths.path 注入 nginx.conf，再配置 log_format/access_log 写文件，并 include 该文件绕过 path sanitizer。显示 Kubernetes v1.23.4，但没有完整注入内容或执行结果。需要按输入到配置语法、可写日志路径到 include、reload 和 controller 身份权限逐段核实；对比经过安全转义或不允许 create/update 的控制，不能宣称匿名 RCE。

实际保存图：1717496437100134442-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717496437100134442)。
