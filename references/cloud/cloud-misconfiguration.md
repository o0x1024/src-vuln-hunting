# 云资源配置与访问边界

## 适用信号与前提

对象存储、数据库、中间件、备份、快照、函数、网络策略。取得资源用途及是否应公开的依据；准备获准的非敏感测试样例或只读配置。公网可达和允许匿名读取本来公开的静态资源不直接构成漏洞。

## 最小实验

- 存储：区分列举权限与对象读取权限。优先请求已知测试对象；列举仅在获准且有限返回时进行，不自动翻页读取业务数据。普通响应头不能代替有效 ACL/策略证据。
- 数据库/中间件：端口连接仅说明可达。使用获准的最小协议操作区分健康检查、认证要求与实际不应开放的读取能力，不导出内容或尝试弱口令。
- 备份/KMS/网络：在可用的只读配置中检查有效策略与实际用途，区分加固偏差和可达权限；不下载完整备份验证敏感性。
- 函数：确认 HTTP 入口是否预期公开、触发动作是否会收费或变更资源；没有许可不调用可能产生这些效果的动作。

## 确认与反例

确认需要实际读取了应受限的授权测试内容，或由完整有效策略证明违反已知权限规则。单个 Policy 通配符、端口、PING、未加密字段或缺少 ACL 不能独立支持高危结论。

排除公开 CDN 内容、资源策略/组织策略限制、身份条件、网络隔离、协议层认证与仅健康检查返回。若只有配置材料，将结果标为配置审计结论并说明缺少动态证明。

## 下一步、停止与报告

默认只读。当前授权明确允许测试夹具的创建、写入或清理时，可以在指定资源命名空间内使用唯一标记的非敏感自建样例，先预留状态核对、费用和清理额度，按 [实验设计](../experiment-design.md) 管理生命周期；不得覆盖既有对象或把生产策略修改、凭据使用、第三方资源注册推导为已获准。仅有读取许可或范围不明时不写/删、不创建或触发收费动作。缺样例/权限则待补证；控制列举返回并按 [证据协议](../state-and-evidence.md) 脱敏。

报告列出资源标识、预期公开性、实际能力、配置依据及限制，按 [验证](../verification.md) 判断，不把基础设施暴露自动定为未授权。

## 调研补充：有效权限的证据

对对象读取、列表、写入和管理权限分别建证据。S3 应结合资源策略、ACL 与组织/账户/桶/接入点层面的 Block Public Access 计算有效访问；看见一段允许策略不能跳过其他限制。用项目提供的自建非敏感对象验证预期私密性，公开网站对象可以是正常用途。各云厂商策略模型分别查证，不把 S3 语义套给 OSS/COS/Azure。

## 调研来源

- [AWS-s3 · Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

## 控制台身份与单项能力

通过S3控制台打开另一个桶时，记录当前AWS主体/账号/角色和实际请求，不能把“个人账号登录”当匿名访问。[AWS S3身份与权限说明](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam.html)将登录身份与资源操作授权分开，权限不因使用控制台或CLI改变（2026-10-09核对）。桶页面/列表可见不证明对象可读、可删或可改ACL；界面按钮也不是服务器放行证据。仅在指定测试对象与动作许可下逐项对照，跨账号合法分享作反例，不从读取许可派生删除/生产策略变更。

## Cognito标识、临时身份与资源权限

应用内的identity pool/user pool/app client标识、用户令牌与AWS临时凭据分别登记。[AWS身份池概述](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)说明身份池可为配置允许的访客或已认证用户提供临时AWS凭据（2026-10-09核对）；这不表示所有应用内Cognito字符串都是秘密或允许任意S3访问。核对实际身份类型、提供商、所选角色、会话条件与具体资源/动作策略，正常受限访客能力作反例。优先提供的只读配置与合成资源，不以发现池ID为由签发身份、读取未知桶或使用生产凭据。

## S3列举、对象读取与sync的权限

仅能列桶不意味着可读对象，更不会因为改用sync而绕过权限。[S3操作权限表](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)区分ListObjectsV2所需s3:ListBucket与GetObject读取权限；[CLI sync文档](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)描述递归复制新/变化对象，并非ACL绕过（2026-10-09核对）。

从获准策略/脱敏日志分别记录主体、桶/对象资源、前缀条件、列举元数据与实际读取授权，排除另有对象策略/凭据造成的读权限。个别对象可读不证明全桶可读；CLI默认差异比较、过滤与既有本地文件也影响“全量”输出。不要按原帖sync整桶到个人桌面或把列举许可扩大为下载；以自建无害对象与有限读权限证据保留能力边界。

## JFrog匿名主体与仓库权限目标

公开JFrog入口或匿名登录界面只给产品/访问方式线索。核对实际实例、版本、是否启用匿名访问、匿名主体在具体仓库与路径上的权限目标，以及制品原本是否应公开。[JFrog权限说明](https://jfrog.com/help/r/how-to-grant-an-anonymous-user-access-to-specific-repositories)将匿名开关与按仓库授予权限分开（2026-10-09核对文本）；域名含jfrog.io或搜索命中品牌不表示所有内容可读。

把仓库浏览、指定制品读取、部署/覆盖及其他管理动作分别记录，匿名与已登录角色用同一合成资源作对照。公开发布依赖包是反例；私密制品或配置向非预期主体开放才有具体授权差异。真实秘钥的效力/权限仍需独立依据，不下载整库、运行包内代码或修改权限目标来证明读取效果。

## 营销链接与共享文件角色

正常营销邮件中的云盘链接，可作为已获准材料的资源引用；宣传文档公开读取可以是预期行为，full access题述不证明任意主体可删除或替换内容。记录邮件来源/时点、实际登录主体、分享受众、My Drive/shared drive位置及每项动作的预期角色。

[Google Drive files文档](https://developers.google.com/workspace/drive/api/reference/rest/v3/files)把canAddChildren、canModifyContent、canTrash、canDelete等细项能力分开，角色/界面按钮不能替代具体操作授权与内容限制。优先项目提供的权限快照与自建无害资源，不批量订阅邮件、不更改真实优惠文档、删除文件或上传替换内容来确认风险。2026-10-09已读官方相关检索文本。

## 定时任务、消息与函数的身份链

书页片段展示Scheduler→Pub/Sub→函数及HTTP函数示例，只覆盖可见局部，不能当整本云手册或真实部署结果。分开记录任务创建/修改/运行主体、消息主题/订阅授权、函数调用身份、函数运行身份与后续资源权限；触发函数并不自动取得其所有身份能力。

[Scheduler IAM说明](https://docs.cloud.google.com/scheduler/docs/access-control)提示作业创建权限可涉及项目内Pub/Sub发布；[HTTP目标认证](https://docs.cloud.google.com/scheduler/docs/http-target-auth)则区分关联服务账号与目标invoker权限，HTTP与消息触发不可套用同一检查。优先审已提供配置/IAM/日志及合成事件关联，保留函数代际/入口和实际授权差异，不创建持久化任务、部署代码、调用命令、读取密钥或删除审计日志。2026-10-09只核读相关官方权限/身份段落。

## Firebase产品、资源与规则分别绑定

Realtime Database、Firestore和Cloud Storage须分别记录产品、项目、资源、实际路径、请求主体及操作规则。[Firebase规则说明](https://firebase.google.com/docs/rules)明确各产品独立定义规则，且Realtime Database规则语言与Firestore/Storage不同（2026-10-09核读相关段落）。某.firebaseio.com/.json可读或403，均不能推出另一个appspot.com资源全部可读写或项目接管。

优先已有配置和脱敏合成记录，分别核对read/create/update/delete、公开业务目的、身份和范围。域名相关性、历史奖励截图与工具标题不代替实际规则/消费者；缺少写入能力就保留缺口，不枚举数据库或修改他人云数据。

## 错误XML中的存储名称与对象权限

URL末尾%C0导致XML URI中露出bucket名称的声明，需要区分原字节、UTF-8/路径规范化拒绝、错误生成组件、后端存储前缀和当前实际bucket归属。图/首段未展示XML原件，名字是架构/对象候选，不自动意味着可列举、读私有对象、写入或P2/P3。

在获准已有脱敏错误/配置中关联存储适配器、当前项目/区域/对象键与正式受众，再按明确许可核对最少合成对象操作；真实role/publicpolicy/私密内容仍分别举证。没有名称响应或不同错误handler为反例，本次不发送非法编码请求、猜bucket、访问云对象或采用历史固定评级。

## 已有执行权限与实例元数据是两条证据链

旧帖先假定reverse shell，再给metadata/latest路径；已有RCE、运行环境身份和云资源权限必须分别证明，不由Linux或AWS字样推出EC2/实例角色。[AWS IMDS说明](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)给出的层级是/latest/meta-data/，IMDSv2先生成实例绑定token再携带它读取，required配置拒绝无有效token请求（2026-10-09核读）。保留旧路径错误，不静默修正后执行。

在获准配置/合成回执中核对实例与容器边、IMDS是否启用、版本/网络可达/跳数及实际角色策略。元数据项目、临时凭据出现与具体云能力分别绑定；没有角色、请求拒绝、受限权限及来自模拟端点的正文作反例。IMDSv2不是已获得本机代码执行后的普遍安全保证，也不是任何SSRF都能读凭据；不建立反向连接、读取元数据秘密或使用所得凭据扩大验证。

## Lambda调用回执与实际执行消费

旧Lambda图把同步描述为主线程A完成再B开始、异步画为事件请求、流处理画为队列拉取。这不是全局串行性或所有来源投递保证；服务拆成微服务也不独立证明采用serverless。关联实际事件来源、schema版本、发起者、函数处理器、执行角色、任务/消息ID与最终状态，不能把图中文字当所有提供商的wire字段。

[AWS调用文档](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html)区分同步等待处理结果、异步先入队立即返回，以及流/队列通过event source mapping提供批次（2026-10-09核读）。请求接受、函数执行成功、重试/重复投递与业务幂等效果分别记账；调用者权限与函数角色权限也不同。用获准配置或合成回执验证失败/重试及终态，不由HTTP成功推任务已完成，不部署函数、触发真实队列或假设A/B全局执行顺序。

## S3兼容端点与逐操作身份

旧八步清单只有第一条指定HTTP自定义endpoint，后续省略；9000端口及AWS CLI字样不能证明是Amazon S3或任何特定产品。逐条保存端点来源、profile/签名主体、region、TLS和对象/prefix；遗漏endpoint选项须核对实际配置，不能把不同调用当同一服务器。保留原文拼写错误而不静默修正执行。

[AWS CLI ls说明](https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html)将ls定义为列出桶/对象/prefix，--endpoint-url覆写默认URL（2026-10-09核读）；ls对象不是下载对象。LIST、GET、PUT、DELETE、读policy是独立能力，上传成功不能证明可删除或读其他对象，“not readable/writable”可能掩盖鉴权/超时/不同操作失败。只用获准脱敏配置和隔离自有小对象建能力矩阵，不照清单上传/删除生产对象、修改policy或使用发现的凭据。

## Airflow连接密文、配置密钥与DAG源码

Airflow连接表中的密码、fernet_key配置、DAG里的硬编码数据库参数和执行日志不是同一种保护范围。[Airflow1.10.12历史安全文档](https://airflow.apache.org/docs/apache-airflow/1.10.12/security.html#securing-connections)说明Fernet保护连接密码，密钥可来自配置或环境（2026-10-09核读）；这不能保护所有Python源码，也不证明旧配置load_default_connections/dont_pickle等标志在当前版本具有相同效果。

对获准已有材料绑定版本、配置来源/覆盖优先级、角色可读位置、字段是否遮盖、实际密文与密钥消费者。图中Dremio连接、pymysql源码及被遮盖密钥仅给位置线索，不能重建口令、确认有效权限或把多个平台logo当每个平台都泄露。连接读取、源文件/配置暴露、运行身份与下游权限分别证明；只记录最少脱敏字段，不解密真实连接、登录数据库、下载全部DAG或运行图中Python。

## Cloud Shell容量与研究工具环境的使用约束

旧帖以5GB/每周50小时建议用Google Cloud Shell做recon。容量、会话持久性与允许运行动作分开。[Cloud Shell配额与限制](https://docs.cloud.google.com/shell/docs/quotas-limits)当前说明默认每周50小时、home目录5GB，并明确禁止network scanning；非交互40分钟、会话12小时限制也不提供持续任务保证（2026-10-10核读）。

研究环境选择应匹配当前服务用途、数据持久化和目标授权，不由免费容量推扫描许可。保留版本/日期与实际制品位置，home之外修改及短暂会话不能当可靠长期检查点。只校正文献，不开启Cloud Shell、创建云资源、改变账号/配额或执行recon；旧文章全文未读。


## APK中的Firestore线索与主动规则检查

FireStorePwn示例图先反编译APK、从Manifest/strings/smali取项目与Tweets集合，再提示查询费用、询问permission checks并显示readable/not writable。静态项目/集合线索与主动访问规则核查不同，工具界面的y不提供项目授权；返回样例也没证明请求匿名、当前规则错误或所有集合都读写开放。

沿制品版本/hash→项目/产品→collection/document路径→请求主体→操作规则→允许受众核对，读与create/update/delete分别保留结果及未知。公开样例、合法认证读与不可写是反例；调用次数与费用属于真实操作成本，不能以“scanner”名义忽略。优先已有脱敏配置/日志/合成样例，不执行APK/反编译器/工具、枚举数据库或修改云对象；整仓库实现未读。来源：[保存帖](https://x.com/i/status/1397904544999391232)。


## 跨云实验拓扑与真实访问控制和遥测

BlueCloud图将Azure/AWS子网、Windows节点、管理端口和Sysmon/Winlogbeat等遥测连接并列。节点/箭头表达设计意图，端口标签不证明实际监听、SG/NSG来源规则、身份权限、隔离或采集到达；公共前端也不说明后端全部公开。

沿获准配置绑定环境/账号、规则方向/源目标/端口、实际管理身份、日志关联及隔离反例，分开部署、可达、认证和遥测观察。共享实验凭据不提供第三方资格，不复制图中密码或部署/连接机器；实验架构不能冒充生产验证。来源：[保存帖](https://x.com/i/status/1403340274932273153)。


## Azure管理面枚举与匿名Blob数据面的证据

BlobHunter图先显示登录主体及两个subscriptions，第一段报告21个storage accounts、2个PUBLIC containers，第二段还在检查。已认证管理面可列资源、工具标公开、匿名读某对象及全任务完成是不同事实。

绑定租户/订阅、实际主体、每个账户/容器及访问策略快照，区分发现、尝试、失败/未完成和数据读取；合法公开内容、无对象权限或仅一段完成为反例。工具标题Public scanner不让登录扫描变匿名。本批未登录Azure、枚举订阅或读取Blob。来源：[保存帖](https://x.com/i/status/1408564837689528320)。


## S3历史ACL清单的资源层与READ_ACP语义

Pastebin图的bucket_exists、AuthUsers/AllUsers及READ/READACP是旧扫描标签，还有NoSuchBucket异常与后行黏连，不能认当前所有资源或全部对象暴露。[AWS ACL说明](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html)区分桶READ列举、对象READ读取及READ_ACP读取ACL。

保存原始行/操作/时点、桶和对象身份、ACL实际作用层及有效策略；查看ACL不等于读内容，列举也不证明写/执行。合法公开资源、对象拒绝、ACL未参与授权和无法归属的错误分别记；历史名单不提供测试资格。本批没有访问清单资产、调用云API或复制对象。来源：[保存帖](https://x.com/i/status/1408732964104589317)。


## S3列举的截断信息与HTML对象浏览器origin

ListBucketResult图有MaxKeys1000、IsTruncated false和images/零字节marker，屏幕下部仍裁切；服务响应的集合边界与截图可见集合不同，目录样式键也不是可浏览真实文件夹。

列表项→对象读取→内容类型/实际托管origin→脚本/HTML消费者与目标用户身份分别核对。旧营销HTML可能公开且无外来输入，SVG文件名/ETag/LastModified不能补XSS执行或当前字节一致；列举权不代对象读取权。没有下载对象、渲染不可信文件或执行脚本。来源：[保存帖](https://x.com/i/status/1409397897955794945)。


## 实验VPC图的路由、VPN路径与未部署节点

AWS实验图的public路由指IGW、private仅local，另列WireGuard、SG端口及NACL标签。Docker节点明确to be done；示意图不能计部署完成、实际入出规则或所有私有服务隔离。

沿获准已有配置/日志绑定账号/VPC、有效路由、管理身份、VPN来源、规则方向/CIDR/端口和真实监听，区分公共入口、内网可达与服务认证。NACL allow标签不补SG实际允许，VPN通路也不等于任意第三方权限；本批没有部署、连接云主机或启动实验。来源：[保存帖](https://x.com/i/status/1409636796506415107)。


## AWS地址段匹配与租户及桶地域的分别归属

onaws图把IP匹配到AWS subnet、EC2服务和eu-west-1。此输出只说明该版本数据中的地址段匹配；共享云地址、租户账号、正式测试范围和某个S3桶的地域仍各需对应证据。

保留数据版本/时点、输入域名的解析结果及实际匹配记录，将provider归属作为候选分类。域名多地址、CDN共享或陈旧网段是反例；不能从EC2地域补桶地域或把所有同云地址纳入范围。本次没有解析、扫描或访问云资源。

来源：[保存帖1](https://x.com/i/status/1409788704504225797)。


## GetBucketAcl读权与Owner字段及对象访问

S3 owner建议提供ACL查询候选。按[GetBucketAcl官方契约](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html)，读取ACL需要READ_ACP等相应能力；响应的Owner字段不能自动解析为某自然人或测试授权。

绑定请求身份、bucket标识、ACL响应来源与采集时点，分别判断ACL读取、对象读取及变更权限。owner enforced下仍可读取ACL不代表ACL仍控制对象访问；公开对象、无ACL读权与训练示例是不同反例，部分AWS ID或region也不补完整所有者。

来源：[保存帖1](https://x.com/i/status/1413763570521710597)、[保存帖2](https://x.com/i/status/1414993063139741707)。


## MongoExpress会话与后端数据库认证的分层

MongoExpress图显示admin/config/local/testdb、MongoDB4.4.6、8086以及连接统计。Web界面可能以自身受控凭证访问数据库，不能推出原生MongoDB未认证。

分别记录浏览器/Web账号、管理界面准入、后端连接身份、数据库角色与具体读写动作。库名可见、UI按钮和软件版本都不能补写权；合法管理会话、只读委托和仅公开元数据是反例，不点击写入、删除或导出按钮。

来源：[保存帖1](https://x.com/i/status/1421047723399204869)。


## AWS类别表中的对象动作与本机路径区别

正文列S3公开read、认证write、目录路径、POSTpolicy和Lambda；图下半截还出现反向代理/Cognito类别，内容裁切。清单没有具体配置或请求结果。

按资源owner、actor、对象/前缀、read/write/list动作、策略条件、签名与执行消费者建立矩阵；公开预期内容、写入不可执行、对象键中passwd字样或缺实例配置是反例。S3对象路径不自动读取宿主文件，不因top10/P1标签补漏洞。

来源：[保存帖1](https://x.com/i/status/1430494198684262411)。


## S3对象清单中的文件名与敏感读取分层

S3图列versions、gz、signature和工具zip等键，正文建议AWS/recon命令；未保存内容、下载权限或秘密字段。

分别记录bucket/prefix owner、list/read/write动作、身份与policy、对象版本/hash和最小字段语义；名称像密钥、公开安装包、仅list允许、加密或取回拒绝是反例。对象清单不证明敏感文件可读，不从对象名推有效凭证或宿主文件访问。

来源：[保存帖1](https://x.com/i/status/1434513022798598148)。


## MinIO目录视图与默认凭证有效性的分开确认

正文提默认帐号和非标准端口；图9000/minio/cdn显示目录/PNG、1.61GB，没有认证方式。

核对产品/版本、访问主体、匿名/public与登录session、bucket action policy及最小受控对象；公开预期目录、图片无认证上下文、已换默认或只有端口是反例。端口不构成认证，默认文档也不证明当前实例有效，本轮未登录或复用帐号密码。

来源：[保存帖1](https://x.com/i/status/1435718207210409986)。


## API Gateway域发现与端点认证合同

正文把execute-api通配域搜索后fuzz称No auth required；没有具体route/stage或私有对象结果。

绑定书面范围、API/stage/route、方法、无会话/低权限/owner身份及实际业务动作；公开预期端点、默认错误、前端shell、路由需auth或无对象内容是反例。域名格式不决定无认证，也不授权批量扫描或跨program探测。

来源：[保存帖1](https://x.com/i/status/1436617773732540417)。


## FirebaseURL和HTML数据库字样的公开配置边界

一帖Wappalyzer/source找到Firebase db URL；另一MongoDB pass放HTML文字无实际字段图。

区分公开项目标识与真实secret/私有数据，绑定owner、规则/认证、read/write动作、字段用途/时效和最小脱敏证据；公开SDK配置、只有URL、合成字串、访问拒绝或缺真实consumer是反例。名称不证明有效数据库身份，未访问数据或使用秘密。

来源：[保存帖1](https://x.com/i/status/1438355065518002180)、[保存帖2](https://x.com/i/status/1438767689183502342)。


## S3词典枚举的Host与资源权限分离

正文ffuf原请求Host带http scheme，过滤404400并建议300线程；无实际桶响应。

先校验requesttarget、authorityHost、SNI与具体S3 endpoint类型，分开桶存在、列目录、对象读取、账户归属和授权；错误Host、403、代理统一响应、历史名称或公开预期对象是反例。用获准自有桶最小对照，不能沿帖进行300并发或认领桶。

来源：[保存帖1](https://x.com/i/status/1443591814611492874)。


## CDN 原站 IP 候选与直接访问后的权限

保存外链标题称发现原站 IP 可绕过 Cloudflare 并导致 DDoS，图只是 CDN 架构。

IP、DNS 历史或架构只是候选来源；若获准研究，比较正确 SNI/Host 的服务、应用身份验证、原站策略与实际受保护资源。发现地址不证明可直连或访问控制失效，更不证明可用性影响；此档案没有实际原站请求，不开展流量压力测试。

来源：[保存帖1](https://x.com/i/status/1447851450982277122)。


## 云函数命令参数、调度调用与服务账号凭据类型

图把 Scheduler/PubSub/函数串联，Python 函数直接读请求命令并调用 os.popen，另一图只有 Beanstalk 应用健康页。

区分部署者权限、触发/调用 IAM、请求来源、运行服务账号、出网与具体敏感数据。预置命令处理代码需要先前部署权限，不证明任意云实例本身有漏洞；健康页不是执行回执。[Google 官方认证说明](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads)中的 metadata access token 是短期访问令牌，不能泛称长期服务账号私钥或保证跨服务权限。仅审计保存代码，不部署、调用或外传。

来源：[保存帖1](https://x.com/i/status/1449825332299714562)。


## Firebase REST PUT 回显与允许写入范围

图为一个Firebase用户路径PUT JSON及200相同字段，没有后续读取/规则/认证结果。

区分请求身份、自有namespace、数据库规则、写入持久性及受保护业务数据；回显不等任意路径读写。公开实验数据、可写自有对象、模拟固定响应或读者拒绝为反例。最小影响需独立后读与规则证据，本次不写/覆盖Firebase对象或读取第三方数据库。

来源：[保存帖1](https://x.com/i/status/1466679748881305606)。


## SageMaker Self XSS 到 CSRF 的用户动作缺口

图片只有同notebook域的Start Attack链接和Jupyter/SageMaker页签，正文称instance takeover链。

记录attacker/victim origin、既有notebook权限、交互、自执行代码到跨站动作的桥接及最终实例能力。自己控制的notebook或按钮不证其他租户/实例接管；无受害操作、正确Origin/CSRF或权限拒绝为反例。外链全文豁免，不点击链接、运行notebook或创建云实验。

来源：[保存帖1](https://x.com/i/status/1467091257654583296)。


## Firebase 公共规则图与 REST 权限范围

早图为标题封面，后完整Rules图显示根read/write true及公共警告；未给实际部署项目/REST请求和持久数据。

区分配置截图、实际生效规则、认证主体、路径继承/校验与读/写/删除各项能力；只在自有可逆实验保存规则版本和读回对照。离线示例、不同项目/环境、未部署、路径规则拒绝或无数据为反例，不写/删真实数据库。

来源：[保存帖1](https://x.com/i/status/1468852084091068418)、[保存帖2](https://x.com/i/status/1472215255375757314)。


## S3 ListBucket 拒绝不说明 PutObject 被拒绝

正文分别称ls拒绝、cp上传，图只为Misconfigured s3 bucket Triaged邮件。

[AWS权限文档](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)将ListObjects/ListObjectsV2的ListBucket和上传PutObject分为动作。固定认证主体、bucket/key/prefix与策略条件，分别记录读、列、写和持久读回。已凭据授权写、不同前缀、预签名、未完成上传或只有邮件为反例；不写/删真实桶，不把单动作推导全部权限。

来源：[保存帖1](https://x.com/i/status/1473620224444223490)。


## S3 匿名列举与签名身份的动作差异

正文声称普通ls失败而no-sign-request可列。两请求身份/权限上下文不同，失败不推出不存在，匿名成功也不推出完整对象读取或写删。

固定bucket/prefix/分页与身份条件，在自有fixture比较ListBucket/GetObject/PutObject等独立动作及策略。[AWS动作文档](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)区分列表和对象动作；错误凭据、只某prefix、过期快照、匿名仅列为反例。不列真实对象、使用秘密或试写删。

来源：[保存帖1](https://x.com/i/status/1477001940173303810)。


## S3 链接、unclaimed 标题与资源接管

正文只建议检查所有S3链接，200奖励邮件题名unclaimed bucket on login页，没有实际引用、归属、注册可能/控制后的消费证据。

静态绑定页面/资源URL/时间/owner及当前scope，分不存在、可列、可读、可写/注册、被应用消费；自有合成资源只核引用与安全拒绝。只有名字/错误/奖金、第三方bucket、受限注册或无消费为反例；不claim或写真实资源，不把S3链接算takeover。

来源：[保存帖1](https://x.com/i/status/1485191930480939011)。


## Osmedeus 云向导配置与实际资源操作分离

保存正文与两图为4.0.2历史发行说明、新DNS/anew及云向导选择Linode/DigitalOcean、默认镜像/规格/区域、掩码token与YAML覆盖，再校验或列SSH镜像等信息。没有成功创建、扫描或账单。

本地合成配置分离凭据读取、列表权限、创建权限、区域/规格和预算，记录版本与失败；列表成功、向导结束或设置token不证明全云覆盖。不得用保存凭据、真实创建资源/支付或执行扫描，发布名称也不构成目前配置保证。

来源：[保存帖1](https://x.com/i/status/1491829464904339456)。


## CloudSploit ACM WARN 与有限收集范围

完整图显示跳过AWS分区设置、只测ACMCertificateValidation、收集2个API调用后四项邮箱验证WARN表格，没有全云扫描或漏洞利用。

离线合成资源保留账号/区域、插件版本、选项、调用成功/失败/跳过、配置规则和业务预期。WARN只支持该规则候选，不能等同证书可冒充或所有AWS不安全；空/跳过区域、邮件验证属于允许流程或无权限证据为反例，不使用云凭据或扫描账号。

来源：[保存帖1](https://x.com/i/status/1492472266189422599)。


## GCS 缺斜杠示例先纠正 URL 语法与读取权限

正文示例把storage.googleapis.com与target name直接相连，不能静默视为合法bucket URL；没有实际列表/对象内容。

离线自有URL模型先区分host/path、bucket标识、对象与列表API，再核请求身份、允许动作和字段预期。语法错误、不存在bucket、仅list允许或公开对象为反例；列举/对象读取/写入各有权限，不将端点拼接等同全部秘密暴露，不在线请求bucket。

来源：[保存帖1](https://x.com/i/status/1493918505292668928)。


## S3 PRE 列表不等匿名对象读取或写入

完整图仅aws s3 ls某dev bucket及许多PRE前缀，未显示CLI身份/配置、匿名参数、对象读取或写入。列表可能使用已有授权。

离线自有权限矩阵分别比较anonymous/已有role、list/object get/put及具体prefix策略，记录期望公开与实际合成字节。目录前缀、dev名称和已有凭据列表不能确认误配置，确认需非预期主体获非预期动作；不访问bucket或使用云账号。

来源：[保存帖1](https://x.com/i/status/1495413876653178881)。


## 混淆 Google 服务 ID 不等管理员角色已赋予

完整片段有SERVICE_ADMIN_ROLE、Services Administrator及APPADMIN/VIEWDLPRULE、遮蔽serviceIds，没有ID映射、请求、角色赋予或权限结果。

离线合成权限模型分别记录服务ID命名、角色定义、赋予主体/对象、实际消费权限及审计结果。隐藏数字、源码常量和角色名称不是管理员权限；未知服务映射、未赋予或后台拒绝为反例，不猜ID或修改真实角色/支付服务。

来源：[保存帖1](https://x.com/i/status/1497257010751885314)。


## Firestore 无条件 write 使更窄 update 条件失去限制

完整v2规则在posts/comments递归路径allow read,write if true，又有update要求author/comment与已有字段相同，未保存实际部署和写入。

Firebase说明匹配allow任意条件为真即放行，v2递归通配符覆盖零或更多路径项；因此在匹配路径/操作内，窄update不会取消已有write。离线自有权限模型比较匿名/两账号、create/update/delete、直接/后代对象与预期不变量；未部署/不匹配路径为反例，不修改真实Firestore或发评论。

规范核对：[Firebase rules structure](https://firebase.google.com/docs/firestore/security/rules-structure)。

来源：[保存帖1](https://x.com/i/status/1501952765299363841)。


## S3 read write delete 标签需要各自对象回执

S3Sec图只是三个标注bucket位置，没展示对象内容、写入或删除回应。

离线policy模型按principal/action/resource分别比较匿名读、受控测试对象写和删，不以list/read继承write/delete。打印标签或bucket公共名字无具体对象证据；不写删生产存储，也不复制图中名称尝试权限。

来源：[保存帖88](https://x.com/i/status/1505509373774372869)、[保存帖91](https://x.com/i/status/1505580378329071617)。


## Service Bus 队列传输示意不证明 Azure 授权漏洞

图片实际是 CobaltBus server/client、入出队列、专属 beacon 队列和 named pipe/目标进程，正文仅 C2 工具说明。

离线用合成消息追云队列、连接身份、方向、请求关联与消费进程；传输编排不等无凭据越权，也不能由云服务品牌推出正常安全。保存图没有 token/RBAC/实际接收，不建立队列、连接 C2 或发送消息。

来源：[保存帖1](https://x.com/i/status/1510606637698105345)、[保存帖2](https://x.com/i/status/1510625225532080128)。


## 公开 S3 搜索结果要核归属和具体访问能力

正文只推荐公开 bucket 搜索站点，没有对象或响应。

区分索引记录、桶归属、列表能力、对象读取、写入和是否预期公开。公开命中不证明秘密暴露或允许测试，历史索引也不说明当前策略；每种影响都需范围内最小对象证据，不遍历、写入或使用发现的材料。

来源：[保存帖1](https://x.com/i/status/1519936550846746624)。


## Cognito 用户令牌与 AWS 资源权限的交接边界

图把 User Pool 令牌、Identity Pool、临时 AWS 凭据和云服务连成流程。

分别记录用户身份验证、身份映射、角色选择和资源策略。取得用户令牌不等于账户接管，取得临时凭据也不等于管理员权限；需要具体主体、资源、动作和实际允许结果，按最小证据报告每一层边界。

来源：[保存帖1](https://x.com/i/status/1520270038153891840)。


## AWS 策略文档与主体有效权限分别核验

图分别显示云 API 动作名称日志和读取 AWS 管理策略的 Allow 通配文档。

记录当前账号、主体、策略是否附加、资源、请求条件与实际结果。动作名称不证明允许；能读取策略文档也不证明当前主体拥有该策略。有效权限还受适用边界、组织策略和显式拒绝约束。规范核验：[AWS policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)。

来源：[保存帖1](https://x.com/i/status/1521976663856324624)、[保存帖2](https://x.com/i/status/1522034257295646720)、[保存帖3](https://x.com/i/status/1522943164029431809)。


## Lambda 批量任务日志需保留角色成本与结束状态

图显示 Lithops/AWS Lambda 作业、对象存储区域、43 个激活及 1/43 的进度。

记录调用角色、区域、任务输入、预算和每个输出凭据。激活成功与作业完成不同，开始进度不能证明全批执行或发现有效；跳过上传也不代表部署版本已核验，本次不启动云任务。

来源：[保存帖1](https://x.com/i/status/1526914141738389504)。


## 子域清单与 S3 桶命名不是同一种对象

正文将子域枚举文件直接交给桶扫描工具，并建议下载内容。

核输入格式、桶/端点命名、区域、所属租户与许可，分别证明列表可见和对象可读。域名包含云特征不代表对应桶存在或公开；数量不能替代权限证据，不在资料提炼中枚举或下载云对象。

来源：[保存帖1](https://x.com/i/status/1530401980065058817)。


## 云攻击模拟按权限、资源、观测与回滚拆解

技术列表把 IAM、EC2、S3、CloudTrail 等动作映射到不同战术。实验前限定测试账户和资源，记录动作所需权限、变化前后状态、日志关联与回滚；日志关闭、凭据读取、共享快照和新增身份具有不同后果。列表或检测标签不证明动作已经发生，更不意味着全账号权限；提炼仅保留实验与检测边界。

来源：[保存帖1](https://x.com/i/status/1533799499486863363)。


## 云交互 Shell 中的本地 root 不等于云项目控制

截图显示环境内提权及容器相关结果。先明确当前 Shell 属于何种运行环境、OS 主体和隔离边界，再核实云身份的实际权限、可访问资源及审计轨迹。宿主命令的 uid、容器操作或本地 sudo 成功不能自动推导项目管理员、其他租户访问或横向控制；本轮仅提炼观察边界，不执行提权命令。

来源：[保存帖1](https://x.com/i/status/1537438620092510213)。


## Firebase 下载能力、规则和扫描判定分层检查

正文含下载 token/媒体访问与匿名读写论断；图片实际显示 APK 反编译发现实例后给出 Secure 判定。项目标识、下载能力链接与规则授权是不同信息，不能由实例名、token 参数、PDF 路径或通配文字推导列举/写入权限。记录具体存储产品、对象、身份与最小读写对照，按自有可回收对象验证规则；工具结论需要原始响应，Secure 截图不支持正文匿名读写主张，不复制 token。

来源：[保存帖1](https://x.com/i/status/1538105747325784064)、[保存帖2](https://x.com/i/status/1540012410970353665)。


## Firebase 客户端配置、数据规则与路径访问分开核查

保存正文指出 init.js/init.json 与数据 .json 路径可提供配置和资源线索。提取项目、应用和公开端点关系后，分别核对当前数据规则、认证主体和具体读写路径；公开客户端配置本身通常只是定位信息。

不要把配置可读或一个 .json 响应等同全库公开。用两个自有身份和最小测试对象确认字段可见性与持久化状态，保持配置、匿名读取、跨对象读取和写入权限的证据独立。

来源：[保存帖1](https://x.com/i/status/1540816850594013185)。


## 云资源枚举保留身份、区域、服务与分页缺口

awsEnum 保存图显示 profile、region、EC2 和 JSON 输出。记录实际凭证身份、请求 API、区域、服务、分页、权限拒绝和失败；成功获取一个区域的一类资源不能算全部云环境已覆盖。

空列表、无权限、配额与传输错误分别保存，避免合并为“没有资产”。只使用当前自有或授权的凭证与最小读取接口；输出中的秘密或个人字段脱敏，不复用归档凭据。

来源：[保存帖1](https://x.com/i/status/1542859206759424003)。


## S3 列举到第三方密钥权限按每步证据拆解

保存正文描述子域发现、S3 列表、读取 JS 中的第三方 Authorization key 和访问员工信息，图片只显示接受状态。S3 ListBucket 与读取对象需要分开确认；“只有列举”不能单独支撑已读 JS 的权限结论。

记录资产归属、列表结果、实际 GetObject、凭据来源及第三方服务授权范围，每步只保留脱敏最小证据。密钥字符串存在、文档中的 API 能力和实际读取权限是不同阶段；不使用归档密钥，也不采集员工联系方式。

来源：[保存帖1](https://x.com/i/status/1547175625844297728)。


## credential_process 配置写入到执行需实际消费链

保存的 AWS 文档图说明 credential_process 由所选配置驱动外部程序，读取 stdout 的 JSON 凭据并以非零退出码报告失败。先确认谁能修改配置/程序、哪个 profile 被实际采用、CLI 调用及程序运行身份，把文件可写与后续真实调用分开。

这不是配置字段出现就成立的匿名 RCE；若程序不被使用或没有相应文件权限，链路仍缺一环。临时凭据刷新、外部程序自身缓存和实际运行窗口也影响观测。stderr 与命令参数的可见性属于另一泄漏边界，敏感值不可写入日志。

只在受控配置中用无害可恢复程序验证，不改现有 AWS 配置、不调用归档凭据。规范来源：[AWS external credential process](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html)。

来源：[保存帖1](https://x.com/i/status/1548495575272009728)。


## 云实验镜像启动不等于资源部署与测试完成

TerraformGoat 保存图展示 aliyun 0.0.4 镜像拉取、run 和 exec 后提示符。实验记录应固定镜像摘要、版本、云账户/区域、最小权限、计划中的资源、费用及清理责任，分清容器启动、云部署和单项测试。

图中 Pull complete 不证明真实资源已创建、隔离或漏洞已验证。只保存实验前提，不运行镜像、注入凭据或部署云资源，也不从未保存仓库补出完整实验内容。

来源：[保存帖1](https://x.com/i/status/1552734216445906945)。


## 临时凭据字段截图不补出 SSRF 或权限链

Slack 保存图显示名为 awskeys.xlsx 的上传内容，含被遮挡的 AccessKeyId、SecretAccessKey、Token 和 2019 过期时间。只记录凭据类型、展示位置、生命周期及必要脱敏字段，区分历史示例、实际服务端获取和当前有效权限。

图片没有 SSRF 输入请求、元数据消费者或 IAM 授权结果，不能补出云账号接管。过期内容不作当前秘密使用，不复制字段、不执行凭据请求；更多影响需要当前授权的独立证据。

来源：[保存帖1](https://x.com/i/status/1553315742166032384)。


## AWS训练首页只支持学习范围不能替代云权限证据

同组两条保存图片均为flAWS首页，说明AWS配置陷阱和可只读提示的训练方式。将训练目标归类为配置与权限理解，在自有授权实验中记录主体、有效IAM及资源策略、服务行为和修复对照。首页未展示真实配置或漏洞，完成训练或工具扫描不证明生产环境安全，也不授权探测真实云资源。

来源：[保存帖1](https://x.com/i/status/1557658731852091395)、[保存帖2](https://x.com/i/status/1557934016741122048)。


## Firebase配置中的标识与数据授权是不同边界

保存图片是客户端Firebase配置，未提供数据库规则或数据响应。用于Firebase服务的API key主要标识项目，资源访问由相应授权和Security Rules等约束；其用途、API限制及是否被混用于其他服务仍需核对。只在自有项目检查最小数据的角色边界，不因配置可见而认定秘密泄露，也不据此认为所有配置安全。依据：[Firebase API keys](https://firebase.google.com/docs/projects/api-keys)。

来源：[保存帖1](https://x.com/i/status/1559533057165623299)。


## 按需部署的云训练环境要核对隔离与清理

HazProne 帮助展示 start/stop、quest 和 AWS profile，宣传按需部署易受攻击资源。只在授权的独立实验账户规划，先核对 profile 实际身份、区域、资源清单、网络暴露和预算，再定义验证与清理读回。停止命令不代表资源已经全部移除；图中的使用方法不证明当前版本行为、部署安全或真实目标存在同样漏洞。不从原帖直接运行部署。

来源：[保存帖1](https://x.com/i/status/1562500234122387456)。


## 多云资源清单需核对凭据身份和分页

Cloudlist正文介绍多provider资产收集。先在授权账户验证只读身份、provider/account/region、资源类型与API分页，保留每项ID和采集时间，错误/拒绝/未查区域显式记录。工具支持多云不等于当前已查所有账户，IP/域映射也不自动取得第三方访问权；不复制真实云凭据或把清单导出到未授权服务。

来源：[保存帖1](https://x.com/i/status/1568109444143136771)。


## Leonidas 部署链与测试资源必须分别核对权限

Leonidas 架构把 CI/CD、Lambda、测试资源和 SIEM 连接起来。审计分别记录部署角色、触发者、目标账户/区域、测试动作及对应日志事件；成功部署不证明所有测试执行，也不证明告警有效。通过自有资源的唯一标记关联动作和日志，未触发/未授权的阶段保留为缺口。

来源：[保存帖1](https://x.com/i/status/1573001680232120320)。


## Cloudfox all checks 保留区域权限错误与缓存来源

截图在assumed-role下列inventory、instances、secrets、IAM模拟等，同时存在任务失败、部分结果和缓存说明。按账户/区域/服务记录实际权限、请求、错误及数据生成时间，保留0结果和未运行的区别。模拟提权路径或任务完成不证明能提升角色；不能从缓存数据认定当前资源存在，也不因allchecks称云全覆盖。

来源：[保存帖1](https://x.com/i/status/1578418462287962112)。


## JS 到云凭据再到 RCE 的每段保留权限前提

初学者图串联隐藏JS、外AWS、admin、SSRF、凭据、bucket、私有API与RCE，无请求。每段核对资产范围、产物实际有效性、进程/云身份、资源权限和下一消费者可达，不能以JS含主机扩大授权。只用自有标记验证最小连接，不使用发现凭据、批量下载bucket或执行归档链。

来源：[保存帖1](https://x.com/i/status/1581654523546054661)。


## Azure 容器列举与 blob 读取是独立授权动作

正文简写 comp=list，图显示 EnumerationResults 的 ContainerName、Blobs Name/Url/ETag/Size/ContentType。先确认实际容器而非任意文件夹、完整请求参数/认证状态和分页 marker，比较自有公开/私有容器的列举与单对象读取，只列必要少量无敏感对象。XML 清单能揭示名称元数据，不自动证明匿名、全部对象可读或可写；截图缺完整请求，不能补造缺失 restype、绕过方式或当前云策略。

来源：[保存帖1](https://x.com/i/status/1587181764862251009)。


## Nuvola 的 PassRole 图：静态边与有效云权限之间

1595666023021158400-03.jpg 把 PassRole、CreateAutoScalingGroup、CreateLaunchConfiguration 与多个角色画成图；1595666023021158400-02.jpg 只是 logo。静态允许关系可作为权限组合候选，需再核验资源/条件、显式拒绝、边界/SCP、服务角色信任、实例配置与实际运行身份，避免把边数量当成权限提升成功。只在自有离线配置模型审计和记录候选链，不创建云资源、转交角色或访问凭据；未知版本的历史 API 名称不当作当前可用保证。

来源：[保存帖1](https://x.com/i/status/1595666023021158400)。


## S3 命令表混合读写：先确定身份与具体权限

1595837676728782848-02.jpg 同列 ACL、列举、移动/上传和删除命令。必须拆分匿名与已认证身份、桶/对象、list/read/write/delete 和有效策略边界，ACL 不是全部权限来源。提炼默认只读的自有测试对象对照，保存身份、拒绝/允许响应与最小内容证据；写入或删除需独立明确授权和可恢复对象，不把命令表照搬为任意桶测试流程。

来源：[保存帖1](https://x.com/i/status/1595837676728782848)。


## 历史保存帖0152：Firebase 公共配置与数据库授权分开

apiKey、databaseURL 等前端配置出现并不自动等于秘密泄漏或可写数据库。应核对具体项目、规则、请求身份、操作类型和对象路径，在自有项目区分匿名/登录读、创建、更新与删除；保存截图只有配置及报告声称可读写，没有完整规则和写入证据。避免复用图中配置对现网发请求。

来源：[保存帖1](https://x.com/i/status/1598310421819179008)。

已实际查看保存图片 `1598310421819179008-02.jpg`：Firebase report public config apiKey/databaseURL and claims read/write poc.json, lower snippet cropped; public configuration not authorization bypass, database rules/principal/readwrite evidence required, do not use key/write live database.


## 历史保存帖0152：Cortex 观测端点认证和信息暴露边界

Shopify 历史摘要确认 Cortex 误暴露且加认证修复，列出 config、pprof 与 cmdline。将配置、调试资料、命令行与业务 API 分层，核对身份、实际字段、网络边界及只读权限；端点可达不等于每个 API 可用。DoS 在文字中是声明，没有负载实证，不把信息读取当高负载试验许可。

来源：[保存帖1](https://x.com/i/status/1598810398693761031)。

已实际查看保存图片 `1598810398693761031-02.jpg`：Shopify Cortex 未加员工认证的历史摘要，/config 与 /debug/pprof/、cmdline 示例暴露配置/命令行，正文声称可 DoS 无实验。提炼管理/观测面认证和敏感字段，DoS 仅假设，不进行高负载试验。


## 历史保存帖0152：Atlantis 可达界面与 PR 执行权限分层

历史 Atlantis 服务暴露摘要注明未披露敏感信息、限制访问后修复。把服务入口、仓库关联、webhook 验证、PR 发起者和 Terraform 执行授权分别核对；公共管理页面并不自动使未授权者可执行基础设施命令或获取云秘密。不发真实 apply/plan 来扩大影响，最小只读配置证据和本地模拟足以定位边界。

来源：[保存帖1](https://x.com/i/status/1600218473052966922)。

已实际查看保存图片 `1600218473052966922-02.jpg`：Atlantis/Terraform PR 自动化服务暴露历史报告；企业摘要明确没有敏感信息披露，限制服务访问后解决。提炼管理页/仓库 webhook/PR 执行授权分层，开放界面不等同能执行 Terraform 或泄露凭据。


## 历史保存帖0153：MS Graph 枚举具有现有 token 前提

AzureGraph help 要求有效 MS Graph token/refresh token。审计身份来源、tenant、scope/role、分页和实际可读用户/设备字段，已有身份合法读取不等于匿名数据暴露。工具标题没有授权缺失证明，令牌不可复制进方法或拿来访问其他租户。

来源：[保存帖1](https://x.com/i/status/1601732287950905344)。

已实际查看保存图片 `1601732287950905344-02.png`：AzureGraph help 要求已有 MS Graph token，可用 refresh token，并声称查询AzureAD用户/设备。提炼 token来源、tenant、scope/role、分页/限制及实际字段，已有有效身份不是未认证枚举漏洞，不使用截图外令牌。


## AzureGraph 帮助页的令牌前提与权限输出分开

图示工具需要 MSGraph/refresh token，并有用户、设备等查询接口。先记录既有身份、租户、令牌受众和授权范围，比较自有身份预期读取能力；查询失败区分权限、过期、受众和运输错误，输出绑定所用身份。拿到公开工具或帮助页不构成匿名枚举、跨租户权限或获得凭证；不从截图复制令牌或对外部租户查询。

来源：[保存帖1](https://x.com/i/status/1603985843672186883)。

已实际查看保存图片 `1603985843672186883-02.jpg`：AzureGraph help现有MS Graph/refresh token前提，用户设备查询。区分token来源/租户/scope与实际读权限，已有有效身份不是未认证枚举，不能试用真实token。。


## JS 中的 S3 地址与 users.csv 读取权限各自确认

正文从 main.js 找 bucket，称只读开放 users.csv 泄 PII，无保存完整数据。记录地址来源、桶归属、公共发布预期、列举/单对象读取/写入权限及身份，用自有合成对象最小读取确认公开边界；只读权限仍可影响机密性，但 URI 暴露和公共静态资产本身不证明错误配置。真实个人资料不批量下载，报告最小去敏字段和权限预期，服务商名不代替客户范围确认。

来源：[保存帖1](https://x.com/i/status/1607700462853324804)。


## 发现 AWS 密钥与证明权限不能以弹窗代替

保存 Trufflehog API key 发现弹窗和 enumerate-iam 验证说明，没有保存密钥对或权限结果。区分 access key 标识、秘密部分、临时 session、账户主体、用途/区域、有效期和具体动作/资源权限；匹配规则/弹窗不是有效性证据，某身份识别也不等于全部 IAM 权限。用自有测试密钥或模拟授权响应记录最小必要允许/拒绝，不使用保存凭据或大范围权限枚举；脱敏保留来源与撤销状态，未知权限不补成全控制。

来源：[保存帖1](https://x.com/i/status/1612472382551396352)、[保存帖2](https://x.com/i/status/1612658486009298944)。


## GCP SSH 用户名与公钥拼接需检查元数据写入边界

图显示ssh.cloud.google的newLinuxUsername值混入编码公钥并带行结束符，未保存授权请求或后端结果。候选链为URL参数→用户名解码/验证→SSH key元数据行构造→实例允许的登录主体。仅自有隔离实例用无效用户名和无权限标记key对照，审计结构化写入、CRLF拒绝及实际主体权限；截图长URL或public key并不证明匿名SSH登录。不得补造有效利用结果或向真实实例追加密钥。

来源：[保存帖1](https://x.com/i/status/1614688717368590338)。

已实际查看保存图片 `1614688717368590338-02.jpg`：GCP SSH浏览器端newLinuxUsername URL含attacker及编码public key和末尾CRLF；截图未见请求鉴权或metadata结果，审计用户名与公钥结构化边界。


## Cognito Identity Pool 公共标识与匿名角色权限要分开

保存图从bundle定位identityPoolId、userPoolId、clientId和region，并声称匿名临时凭据访问AWS服务。这些公共标识不是密钥，匿名身份机制也可为预期功能。审计identity到IAM role的映射、策略resource/action/condition及业务允许的匿名能力；用自有canary资源对照匿名和已登录角色的无害读取/拒绝。取得临时凭据或公共poolID不证明超权限，未保存角色实际权限时保留候选结论。

来源：[保存帖1](https://x.com/i/status/1615016093730607194)。

已实际查看保存图片 `1615016093730607194-02.jpg`：Cognito bundle识别IdentityPool/UserPool/Client/Region，匿名临时凭据需IAM实际超权限，公共ID不是secret。


## 已有 Aliyun 凭据的列桶与对象权限分离

正文与替代文字明确先配置 aliyun 凭据，再用 oss ls 列可访问桶及桶内容；截图有 Size、ETag 与 Region。枚举结果仅证明该主体的相应列表权限，不能推出匿名读取、对象 Get、写入或跨租户能力。记录主体、资源与动作，必要时用自有桶及自有 canary 分别验证允许/拒绝；列表成功不构成公开存储证据，不复制真实凭据或批量下载对象。

来源：[保存帖1](https://x.com/i/status/1616638746819960832)。

已实际查看保存图片 `1616638746819960832-02.jpg`：Aliyun配置凭据后oss ls桶及内容Size/ETag/Region列表，权限来自已有creds，不证明匿名读/写，list≠get。


## 云存储 dork 的公开资料反例与索引语法

保存正文和替代文字包含 s3.amazonaws.com、blob.core.windows.net、googleapis.com、drive.google.com 的 site 条件，部分正文还嵌入 http://，需先核对检索语法。两张图实际命中公开 Tesla PDF，说明域名关键词只能建立关联候选。记录文档公开用途、资产归属和观察时间，再以自有测试资源区分匿名、已有会话与凭据权限；搜索命中不证明桶公开配置错误或内容机密。

来源：[保存帖1](https://x.com/i/status/1616852760141627393)、[保存帖2](https://x.com/i/status/1617121699090288641)、[保存帖3](https://x.com/i/status/1617348174976540672)。

已实际查看保存图片 `1616852760141627393-02.png`：Google s3 @domain命中公开Tesla datasheet，证明公开文档反例不等于秘密。

已实际查看保存图片 `1617121699090288641-02.jpg`：再次云存储dork公开PDF反例，图格式不同仍实际核读。


## S3 指纹、列表和匿名读写分成不同候选

正文宣传 S3Scanner 与导出内容；另一图用 httpx 的 AmazonS3 标识或 AccessDenied 筛选。服务标识、拒绝信息和子域命名都只产生存储候选，AccessDenied 可能正是正常权限控制。确认桶/对象归属后，用自有 canary 分别检查列表、读取、写入及匿名/已认证主体，不批量导出。示例把 http://target.com 传给 amass 的域名参数，需先规范化为域名并按实际工具版本确认输入格式。

来源：[保存帖1](https://x.com/i/status/1616859132069564419)、[保存帖2](https://x.com/i/status/1618951046239518723)。

已实际查看保存图片 `1618951046239518723-02.jpg`：截图用 subfinder 与 httpx 按 AmazonS3 的服务器标识或 AccessDenied 响应筛选候选。两者都不证明公开对象、可写权限或可接管，AccessDenied 可能是正常授权拒绝；需确认资源归属及允许的探测范围。


## 云评估与认证前后工具必须对应真实身份和资源

AWS 图只是 VPC 公私网、实例与 S3 关系，O365 DRAFT 工具表分 recon、audit/review、phishing、authentication attacks、post-authentication。将工具选择绑定账户/租户、IAM 或会话权限、网络路径、允许动作、采样时间和覆盖资源，分别记录无需登录、已认证审计及额外攻击动作的前提。以自有只读权限和拒绝资源作对照，检查评估实际输出与缺失资源；架构箭头、工具列名、Prowler/Scout 等名称不证明有效配置或全部覆盖。泄漏数据库、喷洒和钓鱼不能由工具目录自动授权。

来源：[保存帖1](https://x.com/i/status/1621542771340283904)、[保存帖2](https://x.com/i/status/1623029771692290049)。

现有图片证据 `1623029771692290049-02.png`：O365SupportingToolsetsDRAFT清单recon/audit/phishing/authentication/postauth，工具多阶段和已有权限不能相混，不使用名单尝试第三方账户。


## S3 搜索结果：桶归属和对象权限分别核验

正文建议在 s3.amazonaws.com 下带目标域名搜索。该形式可发现被索引的候选桶或对象，但正文中的目标域名字符串既不能证明桶属于目标，也不能证明对象应为私有。记录桶端点、对象键、归属依据、访问身份与公开意图；先检查已允许读取的最小非敏感样本以及是否列目录。读取、列举、上传和删除属于独立权限边界，不能由搜索命中互相推导。没有实际对象响应和配置时，仅作为被动候选。

来源：[保存帖1](https://x.com/i/status/1623547879351808000)。


## 服务账号私钥示意：JWT assertion、token 交换和 IAM 权限分层

图片用 jose/RS256 和 PKCS8 私钥占位生成含 kid、iss、scope、aud、iat、exp 的 assertion，再拟向 Google token endpoint 交换 access token 并访问 Firestore。提炼时区分 Firebase 公开客户端配置与真正服务账号私钥，确认密钥所属账户、有效期/撤销及 IAM 权限；签出 assertion 不等于 token 被接受，拿到 token 也不等于具备数据库读取权限。图代码的单引号 body 含 ${JWTToken} 不会插值，外层 getAccessToken 未 await 会得到 Promise，原样不是已证明可用脚本。没有实际密钥或交换响应，不执行或复用它。

来源：[保存帖1](https://x.com/i/status/1626175144027627521)。

现有图片证据 `1626175144027627521-02.jpg`：generateAccessToken.js 示意用 jose、RS256、PKCS8私钥占位、kid/iss/scope/aud/iat/1h声明并POST tokenendpoint后拟请求Firestore；没有有效秘密或响应；fetch body单引号含${JWTToken}不会插值，getAccessToken返回Promise却未await。


## S3 ls、cp 与 sync：列举、上传和读取互不推导

图文字叙述历史 URL→JS→linkfinder 发现桶，ls 成功，cp 本地 note 上传 AccessDenied，sync 下载并称敏感文件。核验应记录请求身份、桶归属与公开意图，分别比较 ListBucket、GetObject 和 PutObject 的最小自有样本结果。上传失败不能证明读不可行，列表成功也不能证明所有对象可读；全量 sync 会扩大数据获取，不适合作为最小确认。存档只有叙述，没有真实对象样本、policy 或响应，不能推断敏感范围/当前桶权限。

来源：[保存帖1](https://x.com/i/status/1626995962299224064)。

现有图片证据 `1626995962299224064-02.png`：文字流程waybackurls→JS→linkfinder→S3，ls成功/cp本地note上传AccessDenied/sync下载成功claim；上传拒绝和读列权限独立，没有实际对象样本/身份/owner，不应全量下载。


## AWS 访问控制清单与 S3 列举报告的不同边界

AWS清单列S3权限、CloudFront/S3接管、计算应用、主机网络加固与服务凭据提权，作为独立审查维度。S3图片ListBucketResult只证明某响应包含名称/大小/时间且被截断，未给匿名身份、对象内容或秘密；前端JS和map本身通常需进一步敏感性证明。分别检查列举、读取、写入、策略与业务预期，不能由list推出write。Not applicable是该项目报告处理结果，不能推广为所有桶都无风险。接管还须资源认领条件和目标消费链。

来源：[保存帖1](https://x.com/i/status/1629058555151269888)、[保存帖2](https://x.com/i/status/1629138126475087873)、[保存帖3](https://x.com/i/status/1629550641952555008)。

现有图片证据 `1629138126475087873-02.jpg`：S3 ListBucketResult 展示文件名、大小和修改时间，IsTruncated=true；不是源码或秘密内容，匿名请求身份也未显示。公开前端 JS 与 map 本身不足以定性敏感泄露。

现有图片证据 `1629138126475087873-03.jpg`：Bugcrowd AWS 对象列举报告被判 Not applicable，VRT 1.10.1；仅说明该项目该报告的处理结果。

现有图片证据 `1629550641952555008-02.jpg`：AWS 清单列举 S3 访问控制、S3/CloudFront 接管、计算服务应用、主机网络加固、凭据提权；属于审查维度而非漏洞证据。


## Pages 符号链接读取需限定实际租户边界

历史Cloudflare Pages摘要称构建脚本可借宽泛文件权限与符号链接读取配置/环境，但明确仅限同一用户站点变量。验证构建隔离身份、链接解析、允许目录及原始读取回包，使用自有无敏感标记文件作对照；同用户变量不自动构成跨租户泄露，摘要没有具体链接路径也不补造令牌或读取过程。

来源：[保存帖1](https://x.com/i/status/1632788298920804354)。

现有图片证据 `1632788298920804354-02.jpg`：Cloudflare Pages 历史报告摘要称构建脚本借符号链接读取配置/环境，但明确变量限同一用户站点，未证明跨租户读取；截图无具体链接路径或读取回包。状态 Medium 4.8、500 美元、Resolved，不能扩大到他人凭据。


## EC2 后续 shell 工具依赖既有云权限

EC2StepShell题名声称公私EC2高权限shell，没有凭据/策略/命令结果。审计时先核对调用者IAM、实例归属与管理通道、实例role及动作授权，在许可自有环境观察实际权限；题名不是初始突破或所有实例高权限证明，不安装/调用云管理或shell。

来源：[保存帖1](https://x.com/i/status/1635935018789793792)。


## Cloud exploit 工具菜单不能替代具体授权错误

ThunderCloud help 只展示模块定位，包括活动操作、后门或SSO相关功能。先列云账户/身份、策略和资源边界，优先审查配置及最小只读证据；框架功能与能力宣传不说明已执行或发现漏洞。没有参数和输出时，不运行安装、凭据、持久化或外部通知功能。

来源：[保存帖1](https://x.com/i/status/1640326454742331395)、[保存帖2](https://x.com/i/status/1640761012042498049)。

现有图片证据 `1640326454742331395-02.png`：ThunderCloudhelp列Cognito验证extractcreds、AWS已有key/secret、backdoorrole、SSO钓鱼/roles、S3upload、Azureconnection/blob/sharedkey；帮助并非实际结果，已有访问能力与攻击前提分开，不执行。


## S3 预签名 POST 字段要检查 policy 授权约束

JSON图有url、fields.key、x-amz-credential、security-token、policy及signature，值遮挡，符合预签名上传结构。检查policy期限、桶/对象前缀、内容条件、调用者与对象访问绑定；credential字段不是完整secret access key。客户端持有签名是流程的一部分，不自动长期凭据泄露或任意桶写入，不执行上传/读取真实对象。

来源：[保存帖1](https://x.com/i/status/1641377601846644737)。

现有图片证据 `1641377601846644737-02.png`：S3 JSON 结构有 url、fields.key、x-amz-credential、security-token、policy、signature；值遮挡，表现为预签名 POST 上传字段，不是完整 IAM secret。需 policy 范围/过期/对象前缀/content条件及调用者绑定，不能当作长期密钥泄露。


## Bucket 容器定义仍需对象与身份权限模型

正文只有S3是对象容器定义，封面无漏洞条件。分别记录bucket、对象key、访问身份与策略/ACL/签名用途，核对最小许可读写边界；名称、云品牌或存在bucket不是misconfiguration。未保存续篇按豁免，不补公开读写、凭据或上传链。

来源：[保存帖1](https://x.com/i/status/1643180493100433410)。


## DigitalOcean 元数据路径应按提供商和网络主体核对

帖子提到 169.254.169.254 的 metadata/v1.json。把路径视为提供商相关假设，先核对实际运行环境、发起请求的网络命名空间及目标功能，不能把其他云厂商的头、令牌或目录规则直接套用。证明 SSRF 与读取敏感值需要关联请求和实际返回字段；可达目录、错误信息或帖子声称可读 root 信息不能证明拿到凭据或具有相应权限。

来源：[保存帖1](https://x.com/i/status/1646654212913385472)。


## Firebase 配置可见与数据库 Rules 放行是不同证据

图片代码从公开配置初始化后调用 db.get 并遍历所有记录，没有执行结果。apiKey/projectId/authDomain 等客户端配置本身不证明管理秘密泄露；需要实际项目/服务、匿名与鉴权 Rules、最小自有路径的读取身份及返回内容。配置正确也可能被权限拒绝，整库遍历不是必要验证；本次不执行脚本或读取外部数据，不将配置存在定为数据库失守。

来源：[保存帖1](https://x.com/i/status/1650571465060671514)。

现有图片证据 `1650571465060671514-02.jpg`：FirebasePython config初始化db.get遍历全部record代码，无结果/Rules；apiKey配置不是服务端秘密，整库读取过量，应自有最小路径/匿名与鉴权rules对照，不运行。


## Prow 签名 URL 应限制到获授权桶和对象前缀

图片摘要称通过 job-history/S3 路径签名基础路径可能读取非日志对象，展示编码路径但缺少实际签名/响应。审查输入→对象键规范化→签名身份与策略，限定桶、前缀、对象及读取主体；用隔离自有日志/非日志对象作对照。公开 job 日志并不自动泄露生产数据，“Latest”和整桶描述不证明所有部署可取；签名 URL 读取也不等掌握 AWS 密钥或桶接管，不进行遍历。

来源：[保存帖1](https://x.com/i/status/1650892591884382208)。

现有图片证据 `1650892591884382208-02.jpg`：ProwS3job-history路径/%2e%3f和签basepath可见整桶摘要，称Latest但无日期版本/签URL/实际对象结果；公开joblog与越界非log区分，不能等于S3密钥/所有公司桶被接管。


## Firebase 工具成功输出仍需 Rules 与回读对照

截图先因缺少 exploit.json 失败，创建本地文件后给出 Exploited URL。先核对 Firebase 产品、真实请求方法、身份、Rules 和自控节点；以读/写的服务端响应及独立回读证明权限，不将 Possibly Vulnerable/Exploited 文案当事实。允许公开数据并非配置漏洞，归档无回读证据，不运行其写入功能。

来源：[保存帖1](https://x.com/i/status/1652315807051837443)。

保存图片 `1652315807051837443-02.png`：FirebaseExploiter缺exploit.json后自建并显示ExploitedURL；未显示HTTP状态、Rules/身份及回读，工具成功文案不是未授权写入证明。 本段只使用已保存且实际查看的内容。


## Elasticsearch 服务线索不等同无认证数据权限

9200、Shodan org 与浏览器扩展可提示候选服务，但 org 字段和公开端口不提供授权。记录资产、服务协议、鉴权/网络策略、响应类型与最小自有测试对象，分别检查元数据、索引读取和写入权限。无认证握手或 banner 不证明真实敏感索引可读，不枚举索引、不抓取所谓“juicy data”。

来源：[保存帖1](https://x.com/i/status/1657679647234990080)。


## 存储容器公开层级与 CDN 响应相似性分别验证

Azure 摘要称 container public 而非 private 导致 blob 可读；S3 帖子以 HTTP/HTTPS 响应相同猜 bucket 名。分别记录资产、DNS/证书、CDN origin 配置、对象权限与最小自有标记响应，public listing、单对象读取和账号管理不同。响应相同不证明源 bucket 同名，triager 文字不补实际 PII；不枚举/读取他人对象或使用 cloud key。

来源：[保存帖1](https://x.com/i/status/1658897306169618432)、[保存帖2](https://x.com/i/status/1659337066109624321)。

保存图片 `1658897306169618432-02.jpg`：triager指出Azurestorage blobs无授权可读且container应private而非container层public；没有实际blob请求/PII数据，public级别/策略与DB或云账号接管分开。 本段仅使用实际查看的保存原图，不补未保存内容。


## 应用角色到云密钥再到云权限的链逐步验证

Helm 叙述把配置接口回 access keys 与公司容器/私有数据串联，原图没有实际键或云响应，配置路径字体不确定不补字节。分别绑定应用角色、tenant、键的类型/所有者/权限及受控自有云对象，身份名称不证明资源归属。应用服务可交互、密钥可见和云读取是不同权限，本次不使用键、访问云账号或下载 PII。

来源：[保存帖1](https://x.com/i/status/1659254937409421312)。

保存图片 `1659254937409421312-02.jpg`：Helm购买资格应用叙述：750+失败endpoint，helmCreate success:true后listHelm出现自有/他人chart及用户名，约一周后配置接口回云accesskeys，作者推断加Administrators；配置路径字体不确定，不造原字节；未示原HTTP/角色状态/云消费结果，不复用keys不扫描750路由。 本段仅使用实际查看的保存原图，不补未保存内容。


## 备份中 AWS 字段与云权限使用分层证据

正文声称 backup_1 中 AWS key 能上传/下载。分别绑定备份来源、字段类别、密钥用途/权限范围、项目与允许操作，先以脱敏结构和自有测试 key 确认语义；S3 对象操作不等于 AWS 账户接管。无真实最小对象证据时不推全部权限，不下载整包、使用发现的他人密钥或进行真实对象写入。

来源：[保存帖1](https://x.com/i/status/1661793488743067650)。


## 按组织名猜存储桶不证明文档本应私有

正文列 storage.googleapis.com 下组织名候选。核对当前 bucket/对象归属、匿名读取权限和公开设计，按获准最少字段判断文档敏感性；名称相似、listing 或 URL 存在都不授权整桶下载。未保存对象内容时不声称内部文档泄露，不抓取或访问真实候选。

来源：[保存帖1](https://x.com/i/status/1669822910167650304)。


## BucketLoot 的过滤、命中与真实云权限分别记录

正文说明支持 AWS/GCS/DigitalOcean、30+ regex、自定义 keyword 与资产提取；图显示 GCS 示例 400 对象、117 兴趣文件，keyword/URL/Google service-account SECRET 分类命中。保存枚举范围、max-size 和搜索过滤、对象来源与未读原因；过滤产生的未覆盖项不能算无秘密。正则命中不等密钥有效或高权限，URL 提取不自动扩大资产授权；仅保留必要脱敏字段，不访问原 bucket 或使用材料。

来源：[保存帖1](https://x.com/i/status/1684941887873204230)。

已审阅原图 `1684941887873204230-02.jpg`：BucketLoot示例GCS400对象117兴趣文件，keyword/URL/Google服务账号SECRET分类输出；max-size/search过滤会漏覆盖，regex命中不证明密钥有效或权限，不访问源bucket。


## 侦察按钮矩阵需要逐组件审阅和范围约束：云资源（2023保存案例）

深色 Big Bounty Recon 全界面有目录、配置、数据库、日志、备份、WordPress、安装页、SQL错误、Git/CT/Censys/Shodan/云桶等按钮。界面入口不等于58项实现已审阅；区分被动检索、主动探测、第三方资产和个人信息，各输出只是待授权验证候选，未运行程序。

图片证据：`1688732157458391040-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1688732157458391040)。

相同内容的当前附件：`1688732157458391040-03.jpg`（按已保存原图审阅记录复用，不重复审阅）。


## 异常 PUT 响应中的 bucket 名称只是服务线索（0187）

保存帖建议带 `%c0` 的 PUT 触发错误并观察 S3 bucket 信息。只有特定代理、解码及错误处理组合才可能暴露名称；比较无效字节、正常请求、缓存和 CDN 响应来源。名称泄露不意味着可读、可写或可接管，更不授权向真实存储发写入请求。

来源：[保存帖1](https://x.com/i/status/1692681782876131627)。


## 正文提炼0189：Firebase 公共配置与规则授权分开

自动提取projectID/APIkey只提供配置定位；Firebase公共客户端APIkey常用于标识项目，不应直接认定secret/DB接管。按Realtime Database/Firestore/Storage/Auth/API restriction等具体产品、有效身份及目标对象分别验证规则和最小权限，区分预期公开/认证自有数据/跨用户写读；不扫描无关项目或全量数据库，提取成功不等于11种漏洞覆盖。

来源：[保存帖1](https://x.com/i/status/1698933272678367464)。


## 保存图证0189-99-cloud：机制与验证条件

S3 Bucket Recon图8路线：Google dorks、Burp sitemap/地址及x-am-bucket样式头、图片virtual-hosted bucket URL、GitHub工具、grayhatwarfare/osint目录、s3-detect.yaml、JS regex、subfinder|httpx title grep Amazon S3。Google首条site重复/表意不清、x-am-bucket非统一标准、xargs -I {} curl -s {}无范围/超时与引用、grep标题和s3.amazonaws.com regex会漏regional/pathstyle/custom CDN；只用于候选。公开对象不等于可list/write/读敏感对象，桶归属及各操作权限独立确认，不下载全桶、不开公共写、不把工具目录等于覆盖完成。 可用原图：`1699318555915993248-02.jpg`（保存帖 1699318555915993248）。

来源：[保存帖1](https://x.com/i/status/1699318555915993248)。


## 保存图证0190-85-cloud：机制与验证条件

保存原图文件：1702593223343124512-02.jpg。

8x8报告1895783摘要：暴露Atlantis Terraform pull-request自动化服务器；平台明确称未泄露敏感信息，后完全限制服务访问。管理面公网暴露与实际计划/应用权限、webhook认证、代码仓库和凭据边界分开；先验证匿名/角色最小可见面，不触发Terraform apply。不由Medium/Resolved推出泄密、云资源控制或RCE。

来源：[保存帖1](https://x.com/i/status/1702593223343124512)。


## 保存图证0190-124-cloud：机制与验证条件

保存原图文件：1703755898131558417-02.jpg。

Cloudflare CASB报告2086301：删除的GitHub/Box installation_id或Microsoft tenant UUID/domain曾被合法连接，攻击者知道标识后可在自己账户重新添加并接触旧集成findings。机制为删除后授权/资源归属绑定未重新验证的confused deputy；跨两个自有租户做连接→删除→异租户重连和重新同意对照，检查服务端授权、旧凭据及数据生命周期。平台限定少量集成，调查未发现研究者账号外的数据影响；不可把公开UUID本身称秘密或推断全部客户受害。

来源：[保存帖1](https://x.com/i/status/1703755898131558417)。


## 保存图证0192-132-cloud：机制与验证条件

保存图片 `1711416868655735198-02.png`：AI泛化AWS配置清单将unused安全组、旧IAM、resource leaks等直接等同风险；未用/旧本身不证明暴露，跨S3复制也不自动明文传输。按实际有效权限、网络可达、TLS/存储加密配置、日志覆盖和资源归属逐项留证；清单是候选非审计结果，不改云配置或获取数据。

保存图片 `1711416868655735198-03.png`：AI回答称缺MFA+cloudtrail:CreateTrail可通过创建跨区trail提升权限、仅组织邮箱即可admin，图中没有信任策略或调用链，不能采纳该推断。CreateTrail本身不是AssumeRole授权，邮箱不是IAM身份凭证；核对有效policy、role trust、条件/MFA和resource/action范围，Pacu/CLI推荐不构成漏洞证明，不自动运行提升权限工具。

来源：[保存帖1](https://x.com/i/status/1711416868655735198)。


## 保存正文0193：云存储 dork 的品牌文字不证明资源归属

正文给s3、blob、googleapis、drive等索引候选。品牌名文本和云主机后缀不证明桶属于目标、当前公开或在范围；先由自有页面/配置引用确定关联，再分别核list/get/write与预期公开属性。历史索引只负责发现，不能代替权限和敏感性证据。

来源：[保存帖1](https://x.com/i/status/1712689379523932635)。


## 保存正文0193：第三方桶索引和枚举器只负责候选发现

正文指向GrayhatWarfare和cloud_enum，线程其余未保存。命名命中需结合目标真实引用确定归属和范围，索引不证匿名get/write或数据敏感性；故意公开静态资源是反例。确认最小对象和权限，不批量整桶下载，不将VPN可达当授权。

来源：[保存帖1](https://x.com/i/status/1713223346098192607)、[保存帖2](https://x.com/i/status/1713941004431110261)。


## 保存图证0193-112-cloud：机制、前提与最小验证

已查看的原始图片：1713941004431110261-02.jpg。S3 URL浏览器XML Contents包含key lastmodified etag size owner/storageclass，证列举响应而非对象读取/写入或敏感数据；static/media可故意公开，size0非秘密。先归属/范围和匿名身份，再分别list/get/write权限，最小对象证据不整桶下载。

来源：[保存帖1](https://x.com/i/status/1713941004431110261)。


## 0194：存储下载与工作站冒充主张缺少链条

正文称 AWS 下载会执行恶意脚本并冒充公司工作站，配图只有 OBS 录屏窗口。可提炼的是必须逐段确认对象写入者/来源、响应类型、下载后执行动作、客户端信任边界、初始身份与实际凭据/会话用途；下载文件不自动执行或授予身份。材料没有脚本、权限或 trace，只保留候选与缺证，不补成已实现 exploit。

来源：[保存帖1](https://x.com/i/status/1717819381881708660)。
