# 云配置错误（Misconfiguration）

## 暴露的存储桶/对象存储
- 检查点：S3/OSS/COS/Blob 公共读/写、ACL=public-read、Policy 含 `*` 主体
- 探测：直接 GET 桶 URL、`?list-type=2` 列对象、响应头 `x-amz-acl`
- 域名：`<bucket>.s3.amazonaws.com`、`<bucket>.oss-cn-<region>.aliyuncs.com`、`<acct>.blob.core.windows.net`
- 验证：列目录 + 读取一个非敏感对象样例证明（不批量拉取）

## 云数据库/中间件公网暴露
- 常见：Redis 6379 未鉴权、MongoDB 27017 无认证、ES 9200 未鉴权、MySQL/Postgres 弱口令
- 工具：Shodan/FOFA/Censys 资产测绘（见 asset-discovery.md）
- 验证：端口连通 + 无害指令（Redis INFO/PING）证明，不导数据

## 备份/快照/密钥管理
- 备份桶公开、快照未加密、KMS 密钥策略过宽
- 检查：备份文件是否含敏感配置（.env/密钥文件）

## 无服务/云函数
- 触发器未鉴权（HTTP 触发无需 token）、函数角色权限过大
- 环境变量含密钥、依赖供应链投毒

## 云网络配置
- 安全组/NSG 0.0.0.0/0 放行高危端口（22/3306/6379/9200）
- 对等连接/VPC 共享不当、公网负载均衡后端暴露

## 验证铁律
- 全部使用范围内资产；仅证明配置错误存在与影响
- 不真实写入/删除对象、不改安全组、不触发真实账单
