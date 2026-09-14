# 容器与 Kubernetes 安全

## 权威基线
- OWASP Kubernetes Top Ten 2025：供应链漏洞、不安全工作负载配置、认证机制缺陷、网络分段缺失、密钥管理失败、策略执行缺失、日志与监控不足
- CIS Kubernetes Benchmark / CIS Docker Benchmark
- NIST SP 800-190（容器安全）、SP 800-204（微服务安全）

## 容器层检查点
- 镜像：历史 CVE、非官方/过期基础镜像、镜像内嵌密钥、`docker save` 拖取后审计（自建）
- 运行时：特权容器、`cap-add ALL`、宿主机挂载 `/`、`--privileged`（T1204.003 Malicious Image）
- 配置：危险环境变量（凭据）、容器逃逸面（docker.sock 挂载）

## K8s 层检查点
1. RBAC 过宽：`cluster-admin` 绑定普通用户/SA、`*` 通配资源
2. 匿名访问未禁用：`kube-apiserver --anonymous-auth=true`
3. kubelet 未鉴权：10250 端口可无认证调用
4. 网络策略缺失：无 NetworkPolicy 或 default-deny 未启用
5. 密钥管理失败：Secret 明文、configmap 含密码、etcd 未加密
6. API Server 公网暴露、dashboard 无认证

## 验证思路（范围内）
- 只读 API 枚举（`GET /api/v1/namespaces`）验证未授权访问
- 自建集群复现逃逸/提权链，不在生产执行破坏性动作
- 镜像审计在本地/自建环境进行

## 报告要点
- 组件版本 + 风险项（对应 K8s Top Ten 条目）、可达的权限面、修复建议（RBAC 最小化/NetworkPolicy/加密 Secret）
