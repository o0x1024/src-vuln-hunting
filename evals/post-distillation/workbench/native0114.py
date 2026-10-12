"""Own native distillation; no source code execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "discovery/records-and-incremental.md",
    "并行枚举脚本的阶段产物与失败回执",
    "保存脚本把域名枚举、历史URL、参数加工和多个扫描器串接；另帖把admin=true加工后交给不匹配的管道。\n\n分别定义各阶段输入类型、输出结构、范围过滤、工具版本和完成回执；引用变量、目录隔离、删除临时文件与并发预算需独立审查。URL字符串加工不产生管理员能力，列表模式也不能凭作者描述当作执行模式。错误选项、空输入、被排除的状态、非零退出或覆盖他人文件为反例。仅分析脚本，不执行枚举、扫描或数据库提取。\n\n来源：[保存帖1](https://x.com/i/status/1457146124112850952)、[保存帖2](https://x.com/i/status/1457366069568581639)、[保存帖3](https://x.com/i/status/1457492702313041921)、[保存帖4](https://x.com/i/status/1457818541269340160)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Shodan 服务指纹与凭据主张的分离",
    "帖子列MongoDB、FTP、Jenkins、Telnet、SNMP及RDP查询，并把一段RDP响应前缀标为密码。\n\n保存查询、采集时间、服务原始字段和资产归属；协议前缀、端口、登录页或成功状态不是密码，也不证明匿名权限。代理横幅、过期索引、共享IP和公共服务均为反例。先做已有资料的归属与权限假设，不连接候选、尝试默认口令或复用凭据。\n\n来源：[保存帖1](https://x.com/i/status/1457215293831405573)、[保存帖2](https://x.com/i/status/1459564043643998212)、[保存帖3](https://x.com/i/status/1459594798382211236)、[保存帖4](https://x.com/i/status/1461008603146375174)。"
  ],
  [
    "source-audit.md",
    "反汇编 INT3 分支与调试检测结论",
    "IDA图可见比较、条件跳转及INT3，但未保存执行路径与异常处理。\n\n绑定二进制hash、实际版本、调用条件、分支可达性及异常处理者；区分静态存在、动态到达和产生安全影响。死代码、正常断点、条件不可控或异常被捕获是反例。不由一条指令推断必然反调试或漏洞，不执行样本。\n\n来源：[保存帖1](https://x.com/i/status/1457415428158869507)。"
  ],
  [
    "by-type/idor-access-control.md",
    "localhost 头与双斜线路由的同对象对照",
    "正文提出X-Client-IP localhost；图把带对象ID的users路由403与省略对象ID后的另一users路由200并列，另帖切换Zabbix dashboard动作。\n\n固定同一主体、租户、对象、动作和后端，再追代理信任、路径规范化、路由与处理器授权。集合公共页、空结果、允许的guest视图或不同动作是反例；200不足以证明原对象可读。保留保护数据的最小差分和实际能力，不猜认证头或访问第三方对象。\n\n来源：[保存帖1](https://x.com/i/status/1457472936160419844)、[保存帖2](https://x.com/i/status/1458417780428984320)、[保存帖3](https://x.com/i/status/1461240642261164034)。"
  ],
  [
    "by-type/info-secrets.md",
    "源码敏感词与可用秘密的证据界限",
    "候选包括dockercfg、私钥、FuelPHP profiler配置、门户JSON、Azure JS字段及两条被遮挡的ASIA匹配；Stacs图只是封面。\n\n分类公开标识、配置定位符、掩码值与真正秘密，绑定源码位置、版本、暴露读者和可见原始证据。租户/client ID、API产品公开键、样例、失效值和不可见字段是反例；匹配数量不证明权限。对临时凭据另记类型、组成、到期与授权边界，不能凭前缀判断可用性。仅留掩码，不尝试密钥。[AWS临时凭据](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)说明其具有期限，过期后不再接受。\n\n来源：[保存帖1](https://x.com/i/status/1457689206243807237)、[保存帖2](https://x.com/i/status/1459486331399249920)、[保存帖3](https://x.com/i/status/1459665441224286213)、[保存帖4](https://x.com/i/status/1460289898875961356)、[保存帖5](https://x.com/i/status/1460899061960265730)、[保存帖6](https://x.com/i/status/1461341821569626115)、[保存帖7](https://x.com/i/status/1462529835721494540)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Kunyu 与 Gotanda 的查询入口不是资产结果",
    "Kunyu帮助列hash、fingerprint、WHOIS及搜索模式；Gotanda菜单列IP、ASN、证书、URL和第三方查询入口。\n\n入口仅说明可调用的查询类型，实际资产需响应快照、查询时间、来源与归属对照。相同favicon、CDN共享地址、历史证书和无结果是反例。含token的URL不能原样交给第三方服务；不运行工具或提交真实敏感查询。\n\n来源：[保存帖1](https://x.com/i/status/1457698013686681601)、[保存帖2](https://x.com/i/status/1460717969961631745)。"
  ],
  [
    "by-type/sql-injection.md",
    "按位并行盲注的字符模型与稳定 oracle",
    "图有14行提取日志和7线程ASCII示例；另一卡片称检查多种参数形态即可100%找SQL注入。\n\n先证明输入到SQL表达式的可控性，再以自有固定数据对照真假条件、稳定排序、字符位宽、轮次与噪声。7位假设不覆盖所有Unicode字符，并发会放大共享状态和延迟偏差。错误页、类型校验、反射或工具自动化均可是假阳性；不承诺成功率，不提取真实库内容。\n\n来源：[保存帖1](https://x.com/i/status/1457798092246245383)、[保存帖2](https://x.com/i/status/1459014792438419459)、[保存帖3](https://x.com/i/status/1460902936662315009)、[保存帖4](https://x.com/i/status/1461009301225365510)。"
  ],
  [
    "by-type/file-upload.md",
    "多等号与上传扩展名的实际消费者",
    "帖子建议文件名参数额外等号、PHP改phtml；Fuxploider图在localhost实验环境列12请求及phpinfo正则命中。\n\n分开请求解析后的键值、客户端校验、服务器保存路径、取回响应MIME、路由处理器与解释权限。额外等号可能仅进入值，扩展名接受不等于执行；静态文件、重命名、拒绝下载或正则匹配示例为反例。绑定原始字节与自有无害标记，不上传shell或触发解释器执行。\n\n来源：[保存帖1](https://x.com/i/status/1457812375252439049)、[保存帖2](https://x.com/i/status/1459079229656768514)、[保存帖3](https://x.com/i/status/1460132114045845508)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "批量 Git 更新与克隆的逐仓库状态",
    "更新图同时出现非仓库、非目录、本地修改导致中止和已更新；ghorg图列69个仓库并显示Success。\n\n记录每个仓库的来源、分支/commit、权限、分页完整性和本地变更，逐项保存成功或失败。汇总Success不证明所有仓库及内容完整；私有仓库缺权、改名、分页遗漏、目录不匹配及脏工作树为反例。归档内容只读，不克隆、拉取或覆盖现有修改。\n\n来源：[保存帖1](https://x.com/i/status/1457881859971485707)、[保存帖2](https://x.com/i/status/1461093538859528205)。"
  ],
  [
    "by-type/graphql.md",
    "GraphQL 七类标签与具体执行边界",
    "正文列注入、认证授权、业务逻辑和拒绝服务等类别，没有某个resolver的请求回执。\n\n把类别落实到schema可达字段、解析/验证、resolver、下游消费者与对象权限；为一个受保护动作建立允许/拒绝对照。schema暴露、错误信息或复杂查询本身不证明影响，已授权字段和查询限制是反例。不执行复杂度压测或DoS。\n\n来源：[保存帖1](https://x.com/i/status/1457889593353592835)。"
  ],
  [
    "reporting.md",
    "奖励与 Triaged 邮件的证据阶段",
    "图中有Duplicate Closed、Still being assessed、P1/P4、高危标签及多份奖励；目录递归帖的750美元由两份不同金额图组成。\n\n报告绑定稳定ID、根因、发生时间、真实主体、原始差分和持久能力，把提交/分级/接受/奖励分开记录。邮件标题与金额不能替代方法，重复单也不能猜关联私有内容。准确复现步骤帮助审阅，但不由等级推断任意目标均受影响，不联系邮件收件人或填写支付表单。\n\n来源：[保存帖1](https://x.com/i/status/1457643162529374210)、[保存帖2](https://x.com/i/status/1457934640589717513)、[保存帖3](https://x.com/i/status/1458243194089529349)、[保存帖4](https://x.com/i/status/1458309525069385730)、[保存帖5](https://x.com/i/status/1459892509363027972)、[保存帖6](https://x.com/i/status/1459964562086653953)、[保存帖7](https://x.com/i/status/1460791941659074568)、[保存帖8](https://x.com/i/status/1461214895735664640)、[保存帖9](https://x.com/i/status/1461698833960910850)、[保存帖10](https://x.com/i/status/1462451844542656513)。"
  ],
  [
    "by-type/authn-session.md",
    "JWT 在线解码与验证边界",
    "帖子推荐在线JWT解码器，未保存签名校验或受保护操作。\n\n先在本地以脱敏样本区分payload可读、签名验真、算法/密钥选择与服务端权限。可解码不等于能修改；正确拒绝篡改、过期/受众校验和后续动作受限是反例。不把真实token交给公共网站，也不复用归档会话。\n\n来源：[保存帖1](https://x.com/i/status/1457951873709707266)。"
  ],
  [
    "by-type/xss.md",
    "双引号反斜杠与 JavaScript 语法的消费顺序",
    "帖子列双引号逃逸、globalThis、正则source、call/apply与HTML数字实体编码，没有真实浏览器成功回执。\n\n固定原始响应字节和实际HTML属性、script或DOM消费者，逐层记录实体/URL解码、字符串转义、JS解析、事件触发及CSP。单个过滤器不识别某拼写不证明代码可达；反斜杠奇偶、文本节点、非活动属性和事件不触发是反例。只做静态上下文分析，不执行拼接payload或绕过在线WAF。\n\n来源：[保存帖1](https://x.com/i/status/1458057536658096133)、[保存帖2](https://x.com/i/status/1458176429485694981)、[保存帖3](https://x.com/i/status/1459722794023804930)。"
  ],
  [
    "by-type/xss.md",
    "ENS 名称与客户端校验后的存储读者",
    "正文把ENS名称、绕过前端校验的字段、后台读取UA/IP及邀请邮件HTML作为入口，图片多为封面或报告标题。\n\n外部名称/表单/日志/邮件输入只有到达实际读者并进入活动上下文才支持注入影响。分别追存储、模板编码、邮件客户端、后台身份和触发方式；文本显示、HTML无脚本呈现、隔离文档或没有后台阅读是反例。不注册链上名称、不发送邮件或远程回调，不以奖励补出完整执行链。\n\n来源：[保存帖1](https://x.com/i/status/1458066290694758404)、[保存帖2](https://x.com/i/status/1459113640020250624)、[保存帖3](https://x.com/i/status/1460678440080793606)、[保存帖4](https://x.com/i/status/1461384618196627459)。"
  ],
  [
    "by-type/waf-bypass.md",
    "Cloudflare Blocked 图的失败基线",
    "配文声称Cloudflare新绕过，实际截图明确Blocked。\n\n保存失败响应、规则版本、输入字节、应用是否收到请求及真正下游消费者。仅过滤器识别差异或另一次响应不能补成成功；被阻页、未触发事件和规则不同为反例。把主张标为待验证，不把它当作稳定绕过技巧。\n\n来源：[保存帖1](https://x.com/i/status/1458300734940741635)。"
  ],
  [
    "by-type/business-logic.md",
    "分两步保存的中间状态与故障范围",
    "作者称组名保存两步中断后刷新崩溃，图仅有DoS标签、500分类及分级奖励。\n\n区分前端临时状态、服务端部分提交、对象校验与读者容错；需要同一自有对象的前后状态、失败步骤和恢复回执。短暂异常、合法空状态、缓存或只有单个对象受影响是反例。保存提出的状态机假设，不制造生产崩溃、批量损坏或不可逆状态。\n\n来源：[保存帖1](https://x.com/i/status/1458309525069385730)。"
  ],
  [
    "by-type/authn-session.md",
    "NTLM Type1 到 Type3 与真正的模拟权限",
    "RottenPotato图展示DCOM/SSPI握手；Nosferatu图仅见LSASS模块列表中一个非标准DLL。\n\n握手完成、DLL已加载、可用模拟token和越权行为是四个独立阶段。绑定模块hash/来源、进程与加载权限、token身份、模拟级别及策略；正常认证、预置权限、非活动模块或无法模拟是反例。没有初始权限链不能当远程入口；不加载DLL、读取LSASS、抓取认证或执行后门。\n\n来源：[保存帖1](https://x.com/i/status/1458407645967233026)、[保存帖2](https://x.com/i/status/1461805178567409664)。"
  ],
  [
    "hunting-strategy.md",
    "学习计划的反馈节奏与独立实验",
    "手写图强调基础、Bash、自动化、CTF、周计划与专注；两组重复正文强调方法需适合环境。\n\n围绕一个机制设问题、前提、最小对照、证据和停止条件，以每轮失败/反例调整下一步。工具学习和CTF完成不等于目标已覆盖，固定睡眠/工时和Fuzz everything不作为通用标准；根据授权、资源和目标数据模型设实际预算。\n\n来源：[保存帖1](https://x.com/i/status/1458424484260581377)、[保存帖2](https://x.com/i/status/1459180943642660892)、[保存帖3](https://x.com/i/status/1460377327989313548)、[保存帖4](https://x.com/i/status/1460573253416759303)。"
  ],
  [
    "source-audit.md",
    "PAN-OS 版本分布与 CVE-2021-3064 适用性",
    "Shodan图计84632项且包含PAN-OS 9.1等版本；另帖扫描命令与新闻提到走私加溢出链。\n\n计数只说明搜索命中。按实际产品、版本、GlobalProtect portal/gateway开启状态及网络可达性判断历史漏洞，不从横幅或CVE标题推断利用成功；版本误报、已修补、功能关闭或不适用产品为反例。[厂商公告](https://security.paloaltonetworks.com/CVE-2021-3064)限定PAN-OS 8.1低于8.1.17，9.0/9.1/10不受该CVE影响，Prisma Access不受影响。仅审阅已有资料，不扫描或执行历史PoC。\n\n来源：[保存帖1](https://x.com/i/status/1458661324544569349)、[保存帖2](https://x.com/i/status/1458794745090740224)、[保存帖3](https://x.com/i/status/1460833387015335944)、[保存帖4](https://x.com/i/status/1462058998987821056)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "二维码公共视频通道的既有接收者",
    "图显示YouTube公开QR视频1或3秒，正文提到多个云服务控制通道。\n\n需要已存在的读取/解码程序、云权限、消息格式、调用者及执行回执；承载数据的公开视频不提供目标初始执行能力。无接收者、未解码、下载失败、策略拒绝或只是正常视频是反例。只分析保存截图，不访问通道、下载媒体或建立控制端。\n\n来源：[保存帖1](https://x.com/i/status/1458770050274496521)。"
  ],
  [
    "targeted-fuzzing.md",
    "从 URL 与子域提取词表的结构损失",
    "管道把URL标点转换为换行去重；PyIntruder图选参数标记、1到100、10线程与编码模式；子域图用tok加工后从ffuf展示文本切字段。\n\n先按URL/域名结构保留字段、层级、编码与来源，再选择一个真实消费者及最小变化。记录线上的最终键值、请求身份、预算和响应差分。文本切字段、相同200/长度、数字被过滤或合并不同上下文是反例；工具位置标记不是服务端参数边界。不安装工具或启动枚举/爆破。\n\n来源：[保存帖1](https://x.com/i/status/1458783069511507969)、[保存帖2](https://x.com/i/status/1461397727850512394)、[保存帖3](https://x.com/i/status/1462448271440314374)。"
  ],
  [
    "by-type/waf-bypass.md",
    "历史 origin 候选与 Host TLS 应用身份",
    "一图在IP显示Angular/IIS并标50% sure，另一域名HTTPS图显示Akamai；证书CN与Cloudmare只是候选来源。\n\n比较时间、证书、Host/SNI、页面/资源hash、归属及真实应用路由，确认是否同一受保护消费者。共享主机、旧证书、复制页面、源站仍有独立访问控制或不同应用为反例；两幅图不能证明稳定绕过。仅归类已有线索，不访问源站或扩大范围。\n\n来源：[保存帖1](https://x.com/i/status/1458849557723291650)、[保存帖2](https://x.com/i/status/1459297861921824775)、[保存帖3](https://x.com/i/status/1460898689384214531)。"
  ],
  [
    "experiment-design.md",
    "Boofuzz reset 与进程崩溃的关联证据",
    "图列RUNNING、连接重置和监视进程的segfault代码；Hyenae仅显示菜单。\n\n在获授权的隔离样本上绑定输入case hash、运行版本、进程PID/重启、异常栈、双方协议与重复基线。reset可能网络断开，菜单不是流量回执；超时、无同一进程因果关系、正常退出或不可重复为反例。此次只审阅图，不启动fuzzer、流量生成或生产压测。\n\n来源：[保存帖1](https://x.com/i/status/1458906050355212288)、[保存帖2](https://x.com/i/status/1460944598793076745)。"
  ],
  [
    "by-type/idor-access-control.md",
    "旧 Mongo ObjectID 结构与对象权限",
    "保存newsletter按时间、机器、PID、计数器解释ObjectID，未保存当前驱动生成器或越权响应。\n\n先核对实际驱动/版本和两个自有对象的生成方式，再独立验证对象授权；能预测ID不等于可跨主体读写。[当前mongosh文档](https://www.mongodb.com/docs/manual/reference/method/objectid/)为4字节时间、5字节每进程随机值和3字节计数器，不能把旧机器/PID拆分当所有实现的现行结构。随机性、权限拒绝、不同生成器和不可控对象为反例，不枚举第三方ID。\n\n来源：[保存帖1](https://x.com/i/status/1458928362374717453)、[保存帖2](https://x.com/i/status/1460833387015335944)。"
  ],
  [
    "by-type/ssrf.md",
    "Base64 与 NAT 转发各自需要的消费者",
    "正文提出base64让XXE/SSRF白名单失效、SSRF到NAT转发；另一命令只替换URL参数为回调地址，没有发送阶段。\n\n逐层确认原始输入、实际解码、scheme处理器、网络发起者、重定向与NAT映射权限。base64字符串或加工后的URL不等于服务器请求，NAT可达不等于认证或代码执行。未支持协议、无解码、无发送、客户端访问或映射拒绝为反例；不创建转发、访问内网或发远程回调。\n\n来源：[保存帖1](https://x.com/i/status/1458342362057375753)、[保存帖2](https://x.com/i/status/1459004253863743489)、[保存帖3](https://x.com/i/status/1462109040226578445)。"
  ],
  [
    "by-type/authn-session.md",
    "新密码接口的 ID 旧密码与挑战绑定",
    "一图显示新密码POST的ID、existing encrypted password注释与200 code0；重置帖只保存accepted标题与两次奖励图。\n\n追谁能取得旧密码材料、reset/verify挑战、目标账号、单次/时效绑定及服务端最终权限；以自有账号对照正确与错误目标，区分UI成功和最终会话。需要已知旧密码、只回显ID、未持久变更或错误挑战被拒为反例。token泄漏主张没有原始读者链，不能补成任意ATO；不发短信/邮件或修改真实账号。\n\n来源：[保存帖1](https://x.com/i/status/1459062462142058500)、[保存帖2](https://x.com/i/status/1462451844542656513)。"
  ],
  [
    "discovery/passive-and-services.md",
    "OSI 示意图与实际跨层攻击链",
    "示意图把攻击名分到七层，混列ARP、MITM、DoS、钓鱼和应用漏洞。\n\n归档该分类时追真实输入、协议状态、路由身份、应用解释与受保护动作，不把一个标签限定在单层或从图推断漏洞。合法协议处理、应用权限仍拒绝或缺失下游消费是反例；分类用于提出问题，不替代流量证据。\n\n来源：[保存帖1](https://x.com/i/status/1459236976490594307)。"
  ],
  [
    "cloud/container-k8s-security.md",
    "虚拟机与 Kubernetes 安装回执的状态分层",
    "Windows实验图有ISO下载、KVM/VNC及驱动准备；Kubeapplier列30/30 Applied与黑名单，Kubernetes Goat图为实验目录。\n\n区分素材准备、配置提交、运行健康、网络可达、身份权限和实验漏洞回执。Applied不是健康部署，实验主页不是生产发现；缺驱动、进程未启动、RBAC拒绝、未暴露及实验内容没有执行是反例。本次不下载、安装、创建VM/Pod或修改集群。\n\n来源：[保存帖1](https://x.com/i/status/1459268482000994305)、[保存帖2](https://x.com/i/status/1461322003755978752)、[保存帖3](https://x.com/i/status/1461442702730571776)。"
  ],
  [
    "by-type/xss.md",
    "javascript URL 跳转与最终脚本来源",
    "DOM帖子只有accepted标题；NASA图分别展示HTML标题及域名弹窗。\n\n独立保存入口、URL解析/导航方式、实际sink、点击/事件要求、最终origin与浏览器回执。HTML节点呈现不是JS执行；报告标题、被阻导航、其他origin及示例页为反例。历史弹窗只支持该场景，不外推ATO或所有同名域；不重放到目标。\n\n来源：[保存帖1](https://x.com/i/status/1459325903901642765)、[保存帖2](https://x.com/i/status/1460306222100353035)、[保存帖3](https://x.com/i/status/1461226181429104641)。"
  ],
  [
    "by-type/cors.md",
    "本地 xhr 页面与跨站写入的独立条件",
    "截图只有本地文件页面与sessionid弹窗；另一帖将JSON改成urlencoded以避免preflight。\n\n区分CORS读权限、浏览器自动带凭据、服务器Content-Type解析、Origin/CSRF校验与持久状态改变。无需preflight不自动绕过CORS，读到字符串不证明受保护写入；凭据缺失、SameSite阻止、类型拒绝、CSRF拒绝或仅公开数据为反例。保存原始头/body与真实读者链，不打开归档HTML或修改账号。\n\n来源：[保存帖1](https://x.com/i/status/1459415332930473992)、[保存帖2](https://x.com/i/status/1461684616667045893)。"
  ],
  [
    "by-type/sql-injection.md",
    "数据库 root 到 Web 执行仍有多道权限",
    "帖子直接从数据库root及outfile推断PHP shell或Windows IIS执行。\n\n分别验证数据库角色、文件功能约束、数据库进程OS身份、路径可写性、服务器真实映射及解释器权限。DB管理员不等于OS管理员；受限路径、静态下载、隔离容器、不同文件系统或未启用处理器为反例。只保留分阶段假设，不执行SQL写文件、部署shell或读真实敏感数据。\n\n来源：[保存帖1](https://x.com/i/status/1459419434947268610)、[保存帖2](https://x.com/i/status/1459561215819087880)。"
  ],
  [
    "by-type/authn-session.md",
    "注销后的返回页面与新网络请求",
    "正文把注销后Back看到敏感页面解释为缓存漏洞，未保存网络请求或会话验证。\n\n分浏览器历史/内存恢复、HTTP缓存、service worker及新请求，记录敏感数据在哪个读者继续可见、共享终端场景与注销后会话拒绝。旧画面不证明会话仍有效；新请求拒绝、无敏感信息或本就公共页面是反例。对自有数据建立读者差分，不由截图推断服务器未注销。\n\n来源：[保存帖1](https://x.com/i/status/1459431260175040512)。"
  ],
  [
    "by-type/info-secrets.md",
    "phpinfo profiler 与目录清单的可见内容",
    "图包含开发环境DB字段、Mongo URI、FuelPHP配置与目录文件名；有些值被遮挡，有些确实可见。\n\n按最小证据记录字段类别、暴露路径、来源版本、访问主体和实际读者；目录名不等于文件已读，字段存在不等于凭据有效或可以被复用。掩码、公开示例、空值、失效账号和仅元数据为反例。保留遮挡，不抄出URI口令，不读取候选文件、不登录数据库；部署在AWS不自动归AWS供应商范围。\n\n来源：[保存帖1](https://x.com/i/status/1459439449960550400)、[保存帖2](https://x.com/i/status/1459486331399249920)、[保存帖3](https://x.com/i/status/1459665441224286213)、[保存帖4](https://x.com/i/status/1461341909230637061)。"
  ],
  [
    "scope-and-rules.md",
    "WHOIS 外范围线索与供应商授权边界",
    "图明示只有政策允许all org-owned assets时扩展；另一帖建议从外范围找内范围线索，招聘邮件说可能明年开展合作。\n\n当前正式政策、资产所有权及允许动作共同决定范围，WHOIS、云托管、关联公司、第三方帮助中心和未来招聘都不授予测试权。可从已有公开材料提线索再归属，不能把关联自动变成主动请求授权。过期政策、转售资产、共享服务和合作未成立为反例，不发送申请或消息。\n\n来源：[保存帖1](https://x.com/i/status/1459501309485322244)、[保存帖2](https://x.com/i/status/1459512695498199048)、[保存帖3](https://x.com/i/status/1460232267767365640)、[保存帖4](https://x.com/i/status/1461380474035707914)、[保存帖5](https://x.com/i/status/1462449955210072068)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Azure 审计查询的时间窗与完整性",
    "截图连接Exchange Online并配置6小时、12间隔、1000聚合条目，没有查询结果。\n\n绑定租户、已有权限、源日志、起止时区、分页/限制、延迟和遗漏窗口；连接命令或参数不证明已取证，也不证明全部事件覆盖。截断、限流、跨窗口、角色不足或零数据为反例。只审阅保存参数，不连接云租户或读取日志。\n\n来源：[保存帖1](https://x.com/i/status/1459509921309933574)。"
  ],
  [
    "discovery/web-and-api.md",
    "访问日志 200 筛选与 robots 的候选保真",
    "日志管道grep 200后切引号字段，robots管道裁掉首字符；ffuf图显示普通页面与config长度差异。\n\n按实际日志schema区分状态字段与请求字符串，保留原始行、时间、Host和规范化路径。robots需保留User-agent组、Allow/Disallow、注释、通配符和原始层级，它不是访问控制。200子串误中、裁掉有意义字符、公共路由、不同主体或历史路径为反例；长度差异不是秘密读取，不自动请求列表。\n\n来源：[保存帖1](https://x.com/i/status/1459665441224286213)、[保存帖2](https://x.com/i/status/1460443580485435393)、[保存帖3](https://x.com/i/status/1460443582263803905)。"
  ],
  [
    "by-type/business-logic.md",
    "Stripe 测试接受与生产履约状态",
    "原帖建议在生产结算尝试测试卡，配图为表情图，没有交易/订单证据。\n\n审查网关模式、后端验证、订单状态与权益发放是否一致，使用已授权隔离测试数据；不能把UI接受或测试支付状态当真实付款。[Stripe测试文档](https://docs.stripe.com/testing)要求测试卡配合测试API keys，测试环境无真实资金，不能用测试卡/真实卡测试生产付款。未发权益、订单仍未付款或测试隔离为反例，此处不尝试生产结算或交易。\n\n来源：[保存帖1](https://x.com/i/status/1459891881253478409)。"
  ],
  [
    "discovery/web-and-api.md",
    "ChopChop 的插件等级与响应证据",
    "完整alt解释工具，图有Git exposed High、gitconfig路径、插件和修复建议。\n\n保存插件版本、匹配条件、实际响应类型、可见文件内容和访问主体；High是规则等级，gitconfig可读也不等于完整代码/历史可下载。固定模板、重定向、示例文本、没有真实内容或权限拒绝为反例。只抽取候选机制，不运行工具或下载仓库。\n\n来源：[保存帖1](https://x.com/i/status/1459857231558627332)、[保存帖2](https://x.com/i/status/1460024234697273352)。"
  ],
  [
    "by-type/idor-access-control.md",
    "低权限重放管理员新增动作",
    "正文先捕获管理员请求再换非管理员；图题为ManageOrgAccounts升为admin与奖励。\n\n非管理员仍可能已认证，不能写成无认证。对照真实低权限actor、租户、允许授予的role、管理员cookie是否清除、处理器校验、最终持久角色和新增保护能力。继承admin会话、合法委派、只改显示或没有完成grant是反例。本次只分析资料，不创建/授予真实管理员。\n\n来源：[保存帖1](https://x.com/i/status/1460032301006532609)。"
  ],
  [
    "by-type/xss.md",
    "CSP 图表的 fetch fallback 与 Report-Only",
    "两张完整CSP图把default-src和各种指令并列，并简化为允许/禁止资源。\n\n根据真实响应、enforce/Report-Only、nonce/hash及实际消费者逐项确定有效策略。[CSP3](https://www.w3.org/TR/CSP3/)中default-src是fetch指令的fallback，并不接替所有安全指令；script元素/属性还存在各自回退链。Report-Only用于报告而非阻止，meta也有位置与功能限制。缺CSP不证明漏洞，拒绝活动执行、文本读者或不同响应策略为反例，不执行图中的脚本。\n\n来源：[保存帖1](https://x.com/i/status/1460276604186337282)、[保存帖2](https://x.com/i/status/1461208413665259520)。"
  ],
  [
    "by-type/xss.md",
    "Blind XSS 通知数量与实际后台读者",
    "图为XSS Hunter的30/70 notifications及payload fired标题；正文猜登录UA被管理员页面消费。\n\n关联唯一提交、实际时间、阅读主体、原始输入、DOM上下文和独立触发回执，排除自测、扫描器、预览与重复通知。通知数不等于受害管理员数，日志存储不等于脚本执行；转义显示或没有真实阅读为反例。不发送callback或注入线上日志，不记录完整会话。\n\n来源：[保存帖1](https://x.com/i/status/1460311558609850374)、[保存帖2](https://x.com/i/status/1460678440080793606)。"
  ],
  [
    "scope-and-rules.md",
    "IP Rotate 与高并发建议不能突破授权",
    "帖子推广换IP绕过封禁、Fuzz everything及5000线程递归；另一帖主张所有子域进入HTTP前都需指定DNS链。\n\n请求主体、资产范围、行为与总预算不随代理/出口变化而扩大，阻止/封禁应触发停止与范围核对。DNS和HTTP消费者分别保留解析来源、通配符、当前归属及实际响应，流程须适应数据；并发数字不是效果证据。未授权出口、共享目标、解析差异、限流及重复请求为反例，不部署云网关或运行高负载扫描。\n\n来源：[保存帖1](https://x.com/i/status/1460377864067506178)、[保存帖2](https://x.com/i/status/1460573253416759303)、[保存帖3](https://x.com/i/status/1461214895735664640)、[保存帖4](https://x.com/i/status/1461622803048898564)。"
  ],
  [
    "by-type/info-secrets.md",
    "S3 AccessDenied 与各动作权限",
    "帖子从AccessDenied推测仍可找敏感脚本；另帖声称任意上传但未保存脚本全文或写入回执。\n\n分别检查已授权自有对象的List/Get/Put及路径/策略，不能从根列表被拒推断全部动作，也不能由候选URL推断写权限。对象不存在、显式拒绝、签名过期、公共示例或写入未持久是反例。把实际读取与写入影响分开，不猜桶、读取secret或上传对象。\n\n来源：[保存帖1](https://x.com/i/status/1460708402871558149)、[保存帖2](https://x.com/i/status/1461468627228667904)。"
  ],
  [
    "by-type/race-conditions.md",
    "Newsletter 的 race 名称与 TOCTOU 状态",
    "完整newsletter提ConcreteCMS上传及Palo走私/溢出，底部ResourceSpace内容被裁切，没有具体竞态回执。\n\n对race说明资源、两个参与者、检查和使用点、交错窗口、不变量及最终状态；并发工具或漏洞标题不证明竞争。顺序执行也成功、独立资源、事务原子或服务已修补为反例。仅保留可检验问题，不补写被裁内容或开展竞争测试、文件上传和生产DoS。\n\n来源：[保存帖1](https://x.com/i/status/1460833387015335944)。"
  ],
  [
    "by-type/waf-bypass.md",
    "Telerik rau 编码命中与真实处理器",
    "正文把路径中一个字符百分号编码后得到200称为upload绕过，未保存上传或执行结果。\n\n追边缘解码、后端路由、真实处理器、已部署版本和权限，固定方法、主体与同一资源比较。默认页、空响应、重写到其他处理器或未取得上传能力为反例；状态变化不能直接推断CVE利用或RCE。不发送多部分上传或执行历史payload。\n\n来源：[保存帖1](https://x.com/i/status/1460841043562139651)、[保存帖2](https://x.com/i/status/1460841252044173314)、[保存帖3](https://x.com/i/status/1461069213380988932)。"
  ],
  [
    "by-type/authn-session.md",
    "登录 Help 到独立 IT 服务的访问边界",
    "图仅显示Okta登录帮助里的IT ticket入口；配文称可自注册再读资料。\n\n分别核对链接的实际origin、租户归属、注册政策、成员资格、文档受众和受保护字段。帮助入口公共、正常公开注册、需审批或仅公开文档为反例；超链接不能证明密码泄漏或跨租户访问。不注册外部账号、提交工单或读取私有帮助文档。\n\n来源：[保存帖1](https://x.com/i/status/1460875140904849409)。"
  ],
  [
    "by-type/mobile-ios.md",
    "iOS 思维导图的客户端与服务端权限",
    "完整图列本地文件、备份/日志、Keychain、URL schemes、WebView、认证、第三方库与通信，资源卡标July2020。\n\n按当前版本/构建和实际消费者审查每类数据的存储、读取身份、外部调用与服务器保护能力。客户端patch或关闭pinning仅改变自有设备行为，不证明服务端越权；正常本地数据、模拟环境、正确验证和历史教程失效为反例。只提方法，不改设备、抓第三方凭据或执行旧教程。\n\n来源：[保存帖1](https://x.com/i/status/1460981739338170369)、[保存帖2](https://x.com/i/status/1461123750733221899)。"
  ],
  [
    "by-type/smart-contract.md",
    "合约五阶段审计与业务不变量",
    "完整图从非代码信息、代码检查、漏洞思路、手动审计到工具验证，列transfer/send/delegatecall/selfdestruct等函数候选。\n\n先确定链/VM/编译器版本、角色、价值流、信任边界和允许状态转换，再追一个输入对资产/权限不变量的影响。函数名和检测器命中不是漏洞；正确访问控制、合法委托、余额守恒或版本语义不同为反例。静态阅读与隔离自有模型结论分别记录，不发送链上交易、闪电贷或资金操作。\n\n来源：[保存帖1](https://x.com/i/status/1461034949398700041)。"
  ],
  [
    "by-type/prototype-pollution.md",
    "PPScan 到 XSS 的 gadget 缺口",
    "正文说ppmap把prototype pollution升级为XSS，图片为工具封面。\n\n需要可控的原型写入、污染传播、实际gadget、活动DOM消费者及浏览器执行条件；检测器存在不代表目标具备整条链。自身属性覆盖、冻结原型、无消费者、安全文本输出和CSP限制为反例，不自动把PP报告升级XSS，也不运行扩展或payload。\n\n来源：[保存帖1](https://x.com/i/status/1461205450146271238)。"
  ],
  [
    "discovery/passive-and-services.md",
    "NS 异常与二阶断链的实际消费",
    "图有.cd的NS dig记录与扫描全TLD主张，另帖建议broken link checker找二阶接管。\n\n保存解析时间、权威来源、实际受控能力、现存上游引用与消费者信任。NS记录、404或坏链接不等于可注册/可认领，也不证明上游会再次读取；缓存、域名不可得、完整性校验和已删除引用为反例。只做已有证据关联，不注册域名、认领资源或查询全TLD。\n\n来源：[保存帖1](https://x.com/i/status/1461354281588559882)、[保存帖2](https://x.com/i/status/1461387295831982084)。"
  ],
  [
    "by-type/api-property-pollution.md",
    "设置接口的属性映射与持久权限",
    "正文建议在设置POST里加入页面/请求没有映射的字段，没有实际持久差分。\n\n追请求解析、服务端可写字段白名单、模型映射、存储和保护动作，按字段类型选择自有低风险对照。字段被忽略、只回显、正确role校验、客户端不可编辑但服务端合法为反例。不能从参数存在推断mass assignment，不修改真实角色或他人数据。\n\n来源：[保存帖1](https://x.com/i/status/1461428181802618882)。"
  ],
  [
    "by-type/waf-bypass.md",
    "nginx 分块初始化与历史 WAF 读者",
    "保存图包含content_length_n置零、chunk-size大小写处理片段及一次blocked/另一次用户字段响应；附件列表本身没有全文。\n\n按源码commit、实际构建、原始HTTP字节、边缘解码和应用读取阶段对齐，片段推断须保留GUESS与裁切限制。TE-only不是普适绕过，字段响应也不证另一连接的解析分歧；统一解析、关闭连接、未转发或不同规则版本为反例。[RFC9112](https://www.rfc-editor.org/rfc/rfc9112.html#section-6.3)禁止发送端同时发TE与CL，收到双头有特殊处理，转发前须去除CL并处理TE。不执行旧Python/PoC、不发送混淆报文。\n\n来源：[保存帖1](https://x.com/i/status/1461659031152386053)。"
  ],
  [
    "by-type/request-smuggling.md",
    "过滤器漏检与双端消息边界的不同证据",
    "newsletter讲Palo链，nginx文章图说明WAF可能未检查body，没有前后端连接关联记录。\n\n走私需双方协议/边界解析、连接复用及后续请求被错误归属的证据；单端内容检查缺失或200不构成这条链。边界一致、连接关闭或受控内容合法处理为反例。本次仅区分假设，不发送生产混淆流量。\n\n来源：[保存帖1](https://x.com/i/status/1460833387015335944)、[保存帖2](https://x.com/i/status/1461659031152386053)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "进程树 伪造日志与 LSASS 模块的可信来源",
    "MSTIC图有explorer/iexplore/msiexec及PID/命令；伪造日志帖只有封面，RegistryRecon只有菜单，SillyRAT列listener与Active session。\n\n绑定采集器、日志真实性、时间、稳定进程身份、模块hash、运行者和原始回执，区分父子关系、加载、控制菜单、会话上线与具体行为。伪造记录、PID复用、预置权限、同名进程或仅菜单为反例；没有初始授权链不能当漏洞。不运行后门、读取注册表/LSASS或建立监听端。\n\n来源：[保存帖1](https://x.com/i/status/1461684289578442758)、[保存帖2](https://x.com/i/status/1461805178567409664)、[保存帖3](https://x.com/i/status/1462031650267836435)、[保存帖4](https://x.com/i/status/1462182643936772100)、[保存帖5](https://x.com/i/status/1462393999935918086)。"
  ],
  [
    "by-type/ldap-xpath.md",
    "phpLDAPadmin anonymous 选项与目录可读范围",
    "正文称anonymous checkbox可读并分级high，图片只有triaged邮件。\n\n认证方式、目录授权、字段受众和实际读者需逐层独立证据；anonymous登录本身可能是配置允许行为。只公开属性、正确拒绝私有条目、没有查询回执或误认邮件等级是反例。本次不连接LDAP或提取目录数据。\n\n来源：[保存帖1](https://x.com/i/status/1461698833960910850)。"
  ],
  [
    "source-audit.md",
    "PDO prepare 内的字符串拼接不是参数绑定",
    "代码图在getUserEmail把userid拼入SQL字符串再交给prepare，没有参数占位符。\n\n从实际调用者追输入类型/约束、SQL字节、驱动和执行路径，再审查权限与输出；函数名不能证明安全。[PDO手册](https://www.php.net/manual/en/pdo.prepare.php)要求用参数绑定输入，参数代表完整数据字面量，不能用于任意SQL片段。不可控常量、严格类型约束、路径未执行或真实绑定为反例。保存可达性问题，不执行查询或读取用户邮箱。\n\n来源：[保存帖1](https://x.com/i/status/1461708354699542536)。"
  ],
  [
    "discovery/passive-and-services.md",
    "多解析器答案选择与子域去重",
    "卡片把多个DNS resolver结果交jq的answers[0].name再anew，另一卡用展示文本取存活子域。\n\n保留完整RR类型、名称/值、TTL、返回码、resolver与查询时间，区分第一答案、CNAME和目标A记录；按真实身份归属再去重。空answers、通配符、分裂DNS、轮转与展示格式变化为反例；结果存在不等于当前资产或可测范围。不跑暴力解析或大规模查询。\n\n来源：[保存帖1](https://x.com/i/status/1461811928842620928)、[保存帖2](https://x.com/i/status/1462448271440314374)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "Metabase GeoJSON 的版本与文件读者",
    "图有nuclei单模板命中、浏览器passwd样式内容及一串遮挡URL列表，没有全部目标的请求身份与完整回执。\n\n[官方公告](https://github.com/metabase/metabase/security/advisories/GHSA-w73v-6p7p-fpfr)限定x.40.0至x.40.4，修补版本0.40.5/1.40.5及x.41+，说明GeoJSON URL可暴露文件/环境信息。核对部署版本、实际处理器、访问身份与自有无害标记；root:x grep或列表不是OS root/代码执行证据。固定样例、输入反射、已修补或路由受限为反例，不读passwd/环境变量、不扫描列表或执行模板。\n\n来源：[保存帖1](https://x.com/i/status/1461957553378582531)、[保存帖2](https://x.com/i/status/1462120496129003522)、[保存帖3](https://x.com/i/status/1462489182090182657)。"
  ],
  [
    "impact-and-acceptance.md",
    "弹窗后的影响推导与受保护能力",
    "帖子鼓励从XSS弹窗继续探索，没有后续权限链。\n\n先确定活动origin、触发者权限、真实可读/可写能力和业务规则，再提出最小且授权的后续证明。alert只证该上下文执行，不必然ATO、文件读取或跨租户能力；隔离origin、服务端校验、不可读取数据和交互条件为反例。不通过窃取cookie/敏感数据或真实状态操作扩大影响。\n\n来源：[保存帖1](https://x.com/i/status/1462263751017742339)。"
  ],
  [
    "discovery/web-and-api.md",
    "WordPress 检查清单的检测与认证分层",
    "完整卡片列header、xmlrpc、wp-cron、版本、主题插件、备份、用户枚举与口令爆破，并把random user agent称防火墙绕过。\n\n分别标记信息来源、实际版本、组件启用/可达性和对应漏洞前提。用户枚举不等密码成功，随机UA不证绕过，候选版本不等未修补；公共端点、禁用组件、定制返回或已修补为反例。此处只抽取候选结构，不更新安装WPScan、扫描目标或进行密码尝试。\n\n来源：[保存帖1](https://x.com/i/status/1462287717241212930)。"
  ],
  [
    "by-type/waf-bypass.md",
    "4-ZERO-3 SQLi help 与执行结果",
    "帮助图增加SQLi模式并用2xx至5xx着色，没有SQL求值或成功权限回执。\n\n工具选项与状态码仅描述模式和响应分类，需实际输入、WAF/后端版本、真正SQL消费者及独立真假对照。公共200、错误页、不同路由和被阻请求为反例；不由ModSecurity/libinjection标签断言稳定绕过，不执行bash工具。\n\n来源：[保存帖1](https://x.com/i/status/1462512880339677186)。"
  ]
]

ids={pid for row in json.loads((W/"batch-0114.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert all(pid in ids for pid in urls)
assert len({title for _,title,_ in facets})==len(facets)
grouped=defaultdict(list)
for f,title,body in facets:
 p=T/"references"/f
 assert p.is_file() and ("## "+title) not in p.read_text(),(f,title)
 grouped[p].append("\n\n## "+title+"\n\n"+body+"\n")
community=T/"references/research/community-distillation.md"
marker="\n## 首轮提炼范围与未采纳内容\n"
c=community.read_text();assert c.count(marker)==1
routes=[]
for f,title,body in facets:
 summary=body.split("\n")[0].split("。")[0]+"。"
 assert "|" not in summary and "\n" not in summary
 routes.append(f"| {title} | {summary} | [方法条目](../{f}) |")
for p,parts in grouped.items():p.write_text(p.read_text()+"".join(parts))
community.write_text(c.replace(marker,"\n"+"\n".join(routes)+"\n"+marker,1))
print("Added",len(facets),"facets/routes to",len(grouped),"topics;",len(urls),"batch-bound URLs")

