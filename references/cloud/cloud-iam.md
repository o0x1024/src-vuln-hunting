# 云 IAM 身份与访问控制

## 关键概念（AWS/Azure/GCP/阿里云）
- 身份：IAM 用户/角色/服务账号/托管身份
- 策略：身份策略（Identity-based）与资源策略（Resource-based）
- 信任关系：跨账户角色委派（Role/Service Principal）
- 临时凭证：STS（AWS）、Managed Identity（Azure）、Metadata（GCP/阿里云）

## 高价值检查点
1. 过度授权：Admin 权限绑定到普通用户/服务账号
2. 跨账户信任过宽：信任策略 `Principal:"*"`、`Action:"sts:AssumeRole"` 无条件
3. 硬编码凭证：AK/SK/密码写在源码、配置、.env、GitHub（可用 git 历史扫描）
4. MFA 缺失/可绕过（对应 T1556.006 Multi-Factor Authentication）
5. 密钥轮换缺失：长期 AK 未轮换
6. 角色委派：普通用户可创建角色并赋予高权限（T1098.003 Additional Cloud Roles）

## 利用思路（仅在自建/范围内环境）
- 凭证泄露 → 用云 CLI/SDK 枚举权限（`aws sts get-caller-identity`、`aliyun sts GetCallerIdentity`）
- 过度授权 → 读存储/快照/密钥、调用管理 API
- 信任修改 → 修改 OIDC/身份提供商信任（T1484.002 Trust Modification）
- 新增云账号/凭证做持久化（T1136.003 / T1098.001）

## 最小化验证
- 自建测试账号验证权限放大链路，不碰生产凭证
- 枚举权限后立即停止，不执行真实管理操作
- 涉及生产环境仅报告不利用

## 报告要点
- 受影响身份 + 权限范围、攻击链（哪个入口获取凭证 → 能访问什么）、影响面评估
