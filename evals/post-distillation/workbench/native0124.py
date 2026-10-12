# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "discovery/passive-and-services.md",
    "snetra nrich InternetDB 的 CVE 输出须保留索引身份",
    "正文称stdin IP扫描端口/漏洞；完整图实际列hostname、端口、CPE与历史CVE，另有dnsx解析第二列、移除方括号、sort-u后交nrich。没有对目标发请求或版本/漏洞消费者。\n\n离线候选按来源、索引时间、DNS关系、IP/端口和CPE保存，将库关联与主动验证分层。扁平IP去重会丢失域、共享地址和时间关系；旧banner、CVE名称、已修补版本为反例，不能计已确认漏洞或当前全端口覆盖，不运行保存管道。\n\n来源：[保存帖1](https://x.com/i/status/1499755546974760962)、[保存帖2](https://x.com/i/status/1499946707978579970)、[保存帖3](https://x.com/i/status/1500096187231518721)。"
  ],
  [
    "targeted-fuzzing.md",
    "Nmap 加号强制脚本只改变 rule 适用条件",
    "正文建议--script +http-methods解决不运行；没有具体拒绝原因、脚本版本或执行结果。\n\n官方NSE文档说明加号可越过portrule/hostrule条件。离线核选择表达式、加载错误、服务识别、适用协议和实际输出；这不保证修复脚本语法、依赖、网络权限或正确结果。无适配消费者/执行失败为反例，不强制真实扫描或运行第三方脚本。\n\n规范核对：[Nmap NSE usage](https://nmap.org/book/nse-usage.html)。\n\n来源：[保存帖1](https://x.com/i/status/1499812702436433929)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "IOC Parser 支持类型目录与提取正确性分开",
    "完整图列ASN、IPv4/IPv6、URL/domain、email、MD5/SHA1/SHA256/filename、MAC、MITRE ATT&CK IDs/YARA，描述blog/PDF/CSV、defang和whitelist，没有提取样本/结果。\n\n离线合成文档分别记录来源、格式/编码、上下文、规范化前后值、类型和白名单依据，对照URL与hash相似字符串、断行和误识别。支持表、技术标签和defang字样不是正确提取证明；误类/丢来源/未有结果为反例，不运行存档规则或访问IOC地址。\n\n来源：[保存帖1](https://x.com/i/status/1500082257998061568)。"
  ],
  [
    "by-type/document-rendering.md",
    "Excel WEBSERVICE 的执行者决定是否服务端抓取",
    "完整tip有WEBSERVICE公式，并声称只对Windows servers有效，未显示导出文件、计算触发或请求。公式若只在接收者桌面算，不能直接归为原应用服务器SSRF。\n\nMicrosoft说明函数依赖Windows特性、Mac不返回结果，ftp/file不受支持；平台条件描述Excel消费者，不是所有导出后台。离线合成表格分字段到公式、实际版本/计算模式、运行位置和网络身份，比较字面文本/不重算/禁止连接；缺消费者或只本机请求为反例，不打开保存公式联网。\n\n规范核对：[Microsoft WEBSERVICE](https://support.microsoft.com/en-US/Excel/functions/webservice-function)。\n\n来源：[保存帖1](https://x.com/i/status/1500088756132589570)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Authz0 的 URL role credential 矩阵仍需对象结果",
    "正文介绍自动授权工具按URLs、roles和credentials发现未授权，完整图只是logo，没有具体用例和结果。\n\n离线自有两账号矩阵固定同一对象、动作、租户与字段，分别绑定凭据和预期权限，再比较正常/拒绝/不存在对象及状态变化。角色名称、200、重定向登录和UI相同都不是越权；缺受限数据/写入为反例，不使用存档凭据或自动试真实账号。\n\n来源：[保存帖1](https://x.com/i/status/1500233324371095560)、[保存帖2](https://x.com/i/status/1500249269835493381)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Burp Bounty 自动更新要保留检查时规则版本",
    "完整2.4.0changelog写profiles/rules、扩展自动更新、Collaborator替代host、Variations/Request passive修复，没有安装或扫描结果。\n\n离线验证记录扩展/规则版本、更新前后配置、输入/匹配器、负例、回连主体与错误。自动更新说明不保证当前规则已更新或覆盖；旧配置、更新失败、过宽匹配为反例，不安装来源扩展或联系回连主机。\n\n来源：[保存帖1](https://x.com/i/status/1500301302760304643)。"
  ],
  [
    "source-audit.md",
    "扩展代码审阅从 manifest 到特权消息消费者",
    "正文给CRXcavator、manifest与读代码三步，没有具体扩展版本、结果或漏洞。\n\n离线自有扩展清单先列matches、permissions、执行world，再追页面输入/消息origin/身份到特权API和输出编码。权限声明与实际可达桥不同；无桥、正确校验、仅本人console为反例，不能从风险评分或权限名称直接判注入，不安装存档扩展。\n\n来源：[保存帖1](https://x.com/i/status/1500351722664955906)。"
  ],
  [
    "by-type/xss.md",
    "字符码片段不完整与二千二百奖励归属冲突",
    "正文将onmouseover与不完整with/String/eval/fromCharCode片段描述为POST并获2200；完整图是CSRF端点1800和两项RXSS50/350，总和2200。没有实际POST和执行消费者。\n\n离线分别核JS语法、字符串/属性上下文、编码过程、真实读者与CSP；奖励按独立报告归属，不能把合计数字当一次XSS升级证据。语法错误、无实际发送/执行、仅标题与混合奖赏为反例，不运行保存片段或收集cookie。\n\n来源：[保存帖1](https://x.com/i/status/1500367358325579776)。"
  ],
  [
    "by-type/idor-access-control.md",
    "prod dev 与 ID1 差异须保持资源和身份一致",
    "完整文字tip描述prod/profile常规邻近ID与1失败，dev邻近ID仍失败而dev/profile/1称可读admin用户名、邮箱、角色；没有实际请求响应，P2/700是作者记录。\n\n离线两自有环境/账号同时固定版本、身份、对象归属与字段，比较正常所有者、非所有者和不存在ID。不同环境可能有公开样例/不同对象；dev名称、ID1和奖励不足以证实越权，不枚举真实用户。\n\n来源：[保存帖1](https://x.com/i/status/1500558681011859463)。"
  ],
  [
    "by-type/info-secrets.md",
    "Wayback mp3 候选与录音敏感字段的最小证据",
    "完整tip称从Wayback发现mp3，姓名式文件名和听到姓名、号码、地址、超过900用户，未保存实际音频/HTTP权限对照。\n\n离线自有合成音频对象分历史索引、当前取回、匿名权限、预期保密与实际字段，脱敏最小样例。URL、文件名、作者人数不是已核实披露总数；不可访问、公开演示、已授权身份为反例，不下载/收听第三方录音或收集客户数据。\n\n来源：[保存帖1](https://x.com/i/status/1500563353399447556)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "CIDR sdlookup 到 Osmedeus urls 启动只到 probe 阶段",
    "完整图从CIDR经sdlookup-open、httprobe-c100、tee得到多http/https IP端口，再启动Osmedeus4.0.3 urls/probe，未显示后续扫描结果。\n\n离线输入契约保留IP范围归属、索引来源/时间、协议端口、probe错误、Host/SNI和每阶段hash。候选地址/开始main steps不证明发现漏洞；共享IP、范围外段、空输出或错误为反例，不能把CIDR全面加入授权，不运行管道。\n\n来源：[保存帖1](https://x.com/i/status/1500702598222938115)。"
  ],
  [
    "experiment-design.md",
    "SYN 半连接原理图不等目标资源已耗尽",
    "完整图表示多SYN、服务端SYN-ACK等待第三次握手、正常用户请求后服务不可用，没有真实目标、测量或配置。\n\n离线有界状态模型比较半连接计数、队列上限、时间回收、防护和正常请求处理，记录预测与反例。示意箭头、包数量和概念图不是实际DoS证据；SYN防护或未有资源消耗为反例，不发起真实流量耗尽。\n\n来源：[保存帖1](https://x.com/i/status/1500729487947796482)。"
  ],
  [
    "by-type/authn-session.md",
    "重复 phone_no 的 OTP 交付和身份绑定须同源",
    "正文两次JSON都重复phone_no并声称短信到攻击者号码但会话为受害者，没有保存短信、解析后对象或会话。\n\nRFC8259建议对象成员名唯一，重复时实现可取后者、报错或保留全部。离线假短信/身份模型比较发送、校验、查询账号各消费者的取值/顺序与事务绑定；都取同值、拒绝重复或未跨身份为反例，不能因重复键直接判zero-click P1，不发送OTP或试真实登录。\n\n规范核对：[RFC8259 Objects](https://www.rfc-editor.org/rfc/rfc8259.html#section-4)。\n\n来源：[保存帖1](https://x.com/i/status/1500803809341493249)。"
  ],
  [
    "by-type/business-logic.md",
    "Add Bank 表单字段不等验证绕过",
    "完整图是Add Bank/UPI、姓名/银行/确认账号/IFSC、Cheque或statement照片与JPG/PNG最大5MB，没有保存提交、bank verification或另一个主体。\n\n离线两自有账号分表单限制、对象归属、后端校验、可写字段、验证状态与允许业务动作，比较被拒绝和正常状态。UI按钮、文件限制或BOLA标题不能证明写入/财务权限，状态符合预期为反例，不上传真实金融资料或操作资金。\n\n来源：[保存帖1](https://x.com/i/status/1500848385212964872)。"
  ],
  [
    "reporting.md",
    "影响补充和漏附件应绑定具体报告证据",
    "正文要求按功能写影响并避免漏PoC；两张完整邮件说明clarification后RXSS由P3升P2，另有Email code bypass500奖励但无机制。\n\n离线报告检查资产/身份、最小步骤、附件hash、请求响应、影响与反例，新增影响要对应新证据而非改标题。历史升级仅支持该报告状态；无对照/附件缺失、别人不能复现或纯主张为反例，不能自动套P2/奖励，不发送报告或消息。\n\n来源：[保存帖1](https://x.com/i/status/1500666929928806401)、[保存帖2](https://x.com/i/status/1500894400443871233)、[保存帖3](https://x.com/i/status/1500984346001518594)、[保存帖4](https://x.com/i/status/1503692812122214404)。"
  ],
  [
    "experiment-design.md",
    "DirtyPipe 本机 uid 变化不证明所有发行版适用",
    "两图分别显示改passwd后新名字rootz与另一VM运行dirtypipe2后uid1000到uid0；后者有hijack/drop/restore日志。没有kernel版本、补丁条件或独立文件恢复hash。\n\n离线审核分初始本地权限、内核/配置前提、受限文件消费者、有效uid与后续状态；账户名称/提示符和工具restore打印不能证明权限或恢复完成。修补内核、无入口或不同环境为反例，不执行PoC、修改passwd/SUID文件或创建shell，不能推广全部distros。\n\n来源：[保存帖1](https://x.com/i/status/1500955937481404423)、[保存帖2](https://x.com/i/status/1501126009122295809)。"
  ],
  [
    "discovery/passive-and-services.md",
    "数据库 banner dork 与敏感数据访问分开",
    "正文列MongoDB/mongo-express、MySQL3306、elastic9200、PostgreSQL5432、ProFTPD21等搜索词，另有Free Shodan Tips标题，没有真实权限响应。\n\n离线候选按引擎、时间、端口、banner、认证要求、数据公开预期和归属记录。-authentication关键词、200和数据库名称不证明匿名敏感读取；缓存/代理/误指纹为反例，不连接数据库、FTP或枚举真实表。\n\n来源：[保存帖1](https://x.com/i/status/1501042053593329668)、[保存帖2](https://x.com/i/status/1501461063145070593)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "小时 Git recon 归档要区分快照和发布完成",
    "正文按/platform/company/domain/amass.json分层并给每小时git add/commit/push；完整图private repo按平台文件夹、有56commits，没有cron/推送回执。\n\n离线合成快照保留文件hash、时间、来源、变化/错误与敏感脱敏，再核提交、远端分支、实际SHA和权限。cron表达式、repo私有标志、commit数量不证明定时完成/允许上传；无变更、推送失败或私密材料为反例，不设置任务或推送真实数据。\n\n来源：[保存帖1](https://x.com/i/status/1501109315557634049)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "random 目录再返回的 LFI 状态码需真实文件消费者",
    "正文列大小写api/bEtA、....//与../../etc/random/../passwd，称403变200；没有文件字节、真实文件系统或路径规范化记录。\n\n离线路由/虚拟文件系统逐层比较过滤、单次/重复替换、点段、目录存在、符号关系、根限制和真实读操作。路径能否越过不存在目录取决具体消费者，不凭语义化字符串假定相同；200错误/不同公共资源、无读取为反例，不读取来源真实passwd。\n\n来源：[保存帖1](https://x.com/i/status/1500175294291795968)、[保存帖2](https://x.com/i/status/1501080749755092992)、[保存帖3](https://x.com/i/status/1501792267329224706)、[保存帖4](https://x.com/i/status/1502353284043993090)、[保存帖5](https://x.com/i/status/1502395684846198790)。"
  ],
  [
    "by-type/graphql.md",
    "GraphQL Cop help 和十项检测说法不是审计完成",
    "完整图GraphQL Cop1.0帮助只有目标URL/path、JSON输出和版本；正文后称约十种DoS/CSRF/info leak检测，repo卡没有具体规则。\n\n离线按schema/字段、请求身份、查询深度/批次、允许方法与证据分别设计有界样例、负例和结果。帮助启动、检测类别或工具名称不能确认漏洞/全覆盖；无结果、无跨主体或正常拒绝为反例，不运行深查询/批量认证或资源耗尽。\n\n来源：[保存帖1](https://x.com/i/status/1501169526708314114)、[保存帖2](https://x.com/i/status/1501169699450617859)、[保存帖3](https://x.com/i/status/1503445859375198213)。"
  ],
  [
    "targeted-fuzzing.md",
    "vaf GET 时间和长度输出不能继承漏洞判断",
    "完整vaf1.8.0图在[]标记URL使用wordlist/.html后缀，reflex与URL encode为false，输出index.html200/1256/61ms；正文描述计时和显示优化。\n\n离线合成页面比较真实公共页、统一错误页、动态延迟与编码输入，绑定工具版本、过滤条件和错误。单次时间、200、长度或版本更新不证明注入/发现全面；通用页面、缓存和无消费者为反例，不执行来源程序。\n\n来源：[保存帖1](https://x.com/i/status/1501233921417170949)。"
  ],
  [
    "by-type/ssrf.md",
    "Windows file URL 到 NTLM 需要系统消费者与身份",
    "正文建议SSRF指向file URL并运行Responder接收NetNTLMv2再破解，实际保存图片为meme，视频未保存按豁免。没有协议握手和挑战响应。\n\n离线假URL/文件消费者区分可用协议、UNC解释、系统网络身份、鉴权策略、出网与真实产生者。SSRF标题、Windows机器或file字符串不保证发NTLM；禁协议、无网络身份或无出网为反例，不运行Responder、收集hash、触发回连或破解凭据。\n\n来源：[保存帖1](https://x.com/i/status/1501252172545081347)。"
  ],
  [
    "discovery/passive-and-services.md",
    "唯一 analytics ID 关联网站不等相同所有权",
    "正文列分析ID站点，Synapsint图列Domain/IP/IPv6/ASN/SSL、Analytics/AdSense/email/phone、Bitcoin/CVE；没有实际query或来源结果。\n\n离线关系图保存ID类型、采集时间、原始上下文和关联依据，对照公共模板、第三方SDK、共享托管与旧值。共享ID/ASN不能自动归为同一公司授权域，分类UI不等已获高质量数据；未知来源/误关联为反例，不查个人手机号位置。\n\n来源：[保存帖1](https://x.com/i/status/1501482934372503554)、[保存帖2](https://x.com/i/status/1502267361201733639)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "损坏的 Shodan ffuf 行先验证文本契约",
    "保存串有favicon hash分离、awk中81/$2字形、while read do形状和mc200选项缺失，未有运行结果。\n\n离线自有输入样例逐阶段对照字段格式、分隔、IP/端口、stderr、退出码、默认页面与实际资源。命令外形、org或favicon匹配和200不足以判Spring Boot漏洞；语法错误/未知归属/默认页为反例，不修复后直接对来源目标执行。\n\n来源：[保存帖1](https://x.com/i/status/1501515021171687427)。"
  ],
  [
    "discovery/passive-and-services.md",
    "GeoWiFi 多库部分命中不等当前位置或路由器权限",
    "完整图有遮蔽BSSID/OUI TP-Link、多个提供者not_found、OpenWiFi部分坐标和JSON/map输出路径，没有采集时间或现场证明。\n\n离线合成记录按BSSID/SSID、来源、时间、精度与误关联保留，各库错误/未命中与阴性分别计算。厂商OUI、相似SSID、地图文件和部分坐标不证明当前位置/拥有者，设备移动或旧索引为反例，不查询第三方精确位置、复制坐标或连接WiFi。\n\n来源：[保存帖1](https://x.com/i/status/1501531906986450944)、[保存帖2](https://x.com/i/status/1501533316381503491)。"
  ],
  [
    "by-type/mobile-android.md",
    "WebView 可加载 URL 与桥接特权须分层",
    "保存正文只有WebView checklist主题和任意URL影响方向，没有WebView代码、配置、加载来源或JS bridge。外链全文按豁免。\n\n离线自有移动模型区分可控URL、origin、脚本/文件访问配置、消息/bridge校验、宿主权限与无害结果。能加载网页不自动得到宿主权限/敏感文件；无bridge、禁止脚本或正确origin限制为反例，不安装来源app或访问真实设备。\n\n来源：[保存帖1](https://x.com/i/status/1501679218471620619)。"
  ],
  [
    "by-type/mobile-ios.md",
    "iOS 测试主题清单与可解密流量证据分开",
    "正文列架构、样例app、proxy/jailbreak、检测/pinning与敏感暴露方向，没有证书、配置、请求响应或绕过结果。\n\n离线自有应用按OS/app版本、测试身份、代理路径、信任链、pinning实现、数据存储和允许行为建证据清单。代理启动/菜单选项不等解密，越狱也不保证绕过pinning；未可见流量/无敏感字段为反例，不修改真实设备或读取私人数据。\n\n来源：[保存帖1](https://x.com/i/status/1501709418068680706)。"
  ],
  [
    "by-type/request-smuggling.md",
    "Invalid Header 图片需要原始连接队列证据",
    "完整Burp请求有GET /404、单独0和另一个GET /buy，render视图出现400 Invalid Header及文字403，缺完整framing头和连接时序。正文称无法poison socket。\n\n离线合成HTTP消费者分别记录原始发送字节、前后端解析边界、连接复用、队列和下一请求身份，比较正常、畸形与拒绝。render页面嵌HTTP文本、400、403或单独0不能证明desync；连接关闭/两端同样拒绝为反例，不发送真实smuggling流量。\n\n来源：[保存帖1](https://x.com/i/status/1501683358392516611)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Amass intel enum track db 的历史示例不等当前覆盖",
    "三图列org/CIDR/ASN/whois、active/brute、API config/resolvers/maxqueries、track/db/show/names和viz，未写实现版本、来源响应、结果或diff。\n\n离线按发现范围、提供者/配置、主动/被动模式、输入、限制与错误计数保存快照，再核时间/去重与变化。API配置出现不等有效、db命令不等已读库、ASN或whois关系不等范围；版本不兼容/跳过源为反例，不执行历史命令或扩张真实扫描。\n\n来源：[保存帖1](https://x.com/i/status/1501748595720323072)。"
  ],
  [
    "reporting.md",
    "同一 Mail Injection 多端点的奖励仍按根因归并",
    "正文建议同问题多找端点；完整回信250奖励覆盖最近essentially same issue的全部tickets，无邮件注入输入/解析机制。\n\n离线报告以输入消费者、权限边界、根因和修复面去重，保留所有受影响端点与各自复现/反例。更多URL、票据数和作者标题不等独立漏洞/各自奖金；同一修复与同消费者为反例，付款待信息不能计已付，不提供支付或联系信息。\n\n来源：[保存帖1](https://x.com/i/status/1501807375824551941)。"
  ],
  [
    "by-type/info-secrets.md",
    "zip tar 备份名与受限档案字节分开",
    "正文建议搜索zip/tar，dorks另含日志、email.xls、id_rsa和database.sql.zip；完整图只HIGH500奖赏/付款信息，没有档案内容。\n\n离线候选按索引时间、文件真实格式、归属、预期公开、权限与最小脱敏字段记录。后缀、目录列举、搜索词和奖金不是秘密暴露；HTML错误、样例、空档案或仅索引为反例，不下载私人备份、恢复仓库/数据库或使用key。\n\n来源：[保存帖1](https://x.com/i/status/1501844404604125188)、[保存帖2](https://x.com/i/status/1503673857583984641)。"
  ],
  [
    "by-type/authn-session.md",
    "VERIFIED 响应字段与服务端会话创建分开",
    "完整图OTP POST及HTTP200 JSON有VERIFIED/userId/token，多数关键值像素化；正文称Response Manipulation接管，没有修改前后、真实响应来源或最终身份。\n\n离线自有状态机分客户端渲染、后端验证码校验、token签发/验证、事务主体与后续受限动作。替换本地响应、字符串VERIFIED和token字段不能改变服务端权限；后台拒绝/同一身份为反例，不复制或交换真实token。\n\n来源：[保存帖1](https://x.com/i/status/1501864499170594820)。"
  ],
  [
    "source-audit.md",
    "SAST 分类统计和规则目录不能代替可达 flow",
    "Scanmycode WebGoatPHP图55critical/1minor及code/file/XSS/key/entropy等分类；Codecat0.56图JavaScript规则目录有CSRF/SCE/XSS/SSRF/DOM/XMLHttpRequest等，没有具体代码或确认结果。\n\n离线自有样例将规则版本、输入source、清洗/类型、sink、调用可达性、权限与正反例绑定。统计数量、分类标签、锁定行或规则名不能确认运行漏洞；不可达/正确编码/未执行为反例，不拉来源项目或把训练SAST数量作生产漏洞数。\n\n来源：[保存帖1](https://x.com/i/status/1501894368797634562)、[保存帖2](https://x.com/i/status/1502634174951395330)、[保存帖3](https://x.com/i/status/1502681484921999363)、[保存帖4](https://x.com/i/status/1503343861388742662)、[保存帖5](https://x.com/i/status/1503367681852211203)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "verbose recon 到 Nuclei CVE 的 stdout 契约",
    "正文和完整图amass-passive-v接httpx-verbose再交nuclei cves路径，声称很快找已知漏洞，没有输出或每步错误。\n\n离线合成行核hostname/URL与日志是否混在stdout、协议/端口、去重、stderr/退出码、规则版本和否定匹配。文本文件、流程结束、CVE名称或空输出不证明完整成功；日志污染、跳过服务/范围外资产为反例，不运行真实CVE扫描。\n\n来源：[保存帖1](https://x.com/i/status/1501945807712358400)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "Firestore 无条件 write 使更窄 update 条件失去限制",
    "完整v2规则在posts/comments递归路径allow read,write if true，又有update要求author/comment与已有字段相同，未保存实际部署和写入。\n\nFirebase说明匹配allow任意条件为真即放行，v2递归通配符覆盖零或更多路径项；因此在匹配路径/操作内，窄update不会取消已有write。离线自有权限模型比较匿名/两账号、create/update/delete、直接/后代对象与预期不变量；未部署/不匹配路径为反例，不修改真实Firestore或发评论。\n\n规范核对：[Firebase rules structure](https://firebase.google.com/docs/firestore/security/rules-structure)。\n\n来源：[保存帖1](https://x.com/i/status/1501952765299363841)。"
  ],
  [
    "discovery/passive-and-services.md",
    "MOBOTIX 搜索街景截图不证明当前设备公开权限",
    "完整Shodan图有历史时间、IP/主机/地区、MOBOTIX200和街景截图，没有当前请求、设备所有者或认证策略。\n\n离线发现清单分索引快照、实际服务、预期公开与资产许可，只保存最少元数据。街景、品牌标题、共享IP或200可能为公开演示/旧缓存，不能推设备控制或当前未认证录像；不连接摄像头、获取录像或复制个人地址。\n\n来源：[保存帖1](https://x.com/i/status/1501975760373964805)。"
  ],
  [
    "discovery/web-and-api.md",
    "历史 DNS 找 origin IP 要核 Host SNI 同一性",
    "正文称Incapsula后通过viewdns.info找到origin IP，没有DNS记录、连接或后端权限响应。\n\n离线路由模型比较记录时间、解析关系、归属、连接IP、Host/SNI、证书、路由与同一对象。旧IP、共享托管、默认站点和能连接不等边缘保护绕过；不同资源/后台继续拒绝为反例，不访问范围外IP或把历史DNS当测试许可。\n\n来源：[保存帖1](https://x.com/i/status/1501980086391787525)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "ASSAMEE AES 名称与半程上传不能证明保密完整",
    "完整图菜单upload/download/package、遮蔽API key、archive、AES-256-CBC密码提示及54%传输，没有IV/完整性、完成收据或解密回读。\n\n离线自有合成档案区分本地打包/加密、传输、存储权限、元数据、完整性验证与roundtrip，用hash比较原文/恢复内容。cipher名称、connection OK、进度和密码提示不是安全/完成证明；未知实现/失败/无回读为反例，不使用key、上传私人资料或安装包。\n\n来源：[保存帖1](https://x.com/i/status/1502045272863649800)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "Log4j XFF 表达式和 403 要分 lookup 执行证据",
    "完整图是vcenter SAMLRequest、X-Forwarded-For中的JNDI/hostName/Java版本表达式与403 Forbidden，正文有Google1337奖励标题。未保存组件版本、日志消费者或回连。\n\n离线自有日志模型分输入进入日志、lookup解析、协议连接、类加载、执行身份和结果，绑定同一事务。403不证明无下游日志，但lookup字符串/奖金也不证明已有执行；无可达Log4j/受限lookup或加载为反例，不触发回连、启动服务或复用SAML/token。\n\n来源：[保存帖1](https://x.com/i/status/1502123075109748736)、[保存帖2](https://x.com/i/status/1502214613915430912)。"
  ],
  [
    "by-type/waf-bypass.md",
    "h1 百分号编码与 iframe 实体要追完整解码层",
    "正文给h1混合大小写/百分号属性与iframe javascript实体，声称Cloudflare或括号过滤可绕，未保存响应/DOM；括号变体仍含一个字面右括号。\n\n离线分别记录URL/form解码、HTML实体、实际属性名、JS语法/事件及CSP，比较单次/无解码与原始过滤条件。百分号属性名不会仅靠标签字面就成为事件；不满足过滤条件、需点击却未触发/无reader为反例，不推广全部当前WAF。\n\n来源：[保存帖1](https://x.com/i/status/1502148715452133378)、[保存帖2](https://x.com/i/status/1502227741961195521)、[保存帖3](https://x.com/i/status/1502500964359675906)、[保存帖4](https://x.com/i/status/1502548780251418624)。"
  ],
  [
    "by-type/authn-session.md",
    "百分号零空字符与 rate limit 计数键分开",
    "正文建议%00用于认证的No Rate Limit bypass，完整回信是认证bypass High/P2和凭证奖励，无具体输入、计数或身份消费者。\n\n离线合成限流与身份模型分别记录原始字段、解码/截断/规范化、计数键、账号绑定、限制时间窗与错误。变体字符串、奖励和未限流名称不能证明可改身份；拒绝NUL、计数统一或仅本人账号为反例，不发批量登录/OTP或耗尽真实服务。\n\n来源：[保存帖1](https://x.com/i/status/1502176585817804801)。"
  ],
  [
    "by-type/crlf-response-splitting.md",
    "CRLF MIME 片段须证明字节进入响应头边界",
    "完整保存片段含CRLF、X-XSS-Protection、text/html及脚本/cookie，没有HTTP回应；同正文两条post IDs。\n\n离线合成响应比较URL解码、头值校验、真实CR/LF分隔、body字节、浏览器内容类型和CSP/实际读者。百分号文本、拒绝header或只反射到body为反例；历史header名字不保证当前浏览器行为，不凭片段判XSS或数据泄露，不执行保存脚本。\n\n来源：[保存帖1](https://x.com/i/status/1502203242620588036)。"
  ],
  [
    "hunting-strategy.md",
    "新功能和 release 页是变化线索而非更高漏洞概率保证",
    "正文称新功能发现概率always更高，建议观察release页，没有对比样本、版本差异或确认结果。\n\n离线将已授权资产的版本、功能、角色、对象和状态变化转为具体不变量/证据缺口，保持旧关键路径复查。发布时间、新颖性、未测量基数和旧漏洞遗漏为反例；新功能不是scope许可或高危保证，不创建未经请求的监控任务。\n\n来源：[保存帖1](https://x.com/i/status/1502228493761118208)。"
  ],
  [
    "by-type/jwt.md",
    "JWT None 大小写和无签名许可要按验证器确认",
    "正文称None标准算法并给alg:None与is_admin=true空签名片段，没有验证器、应用策略或受限权限结果。\n\nRFC7518注册值为小写none、算法名区分大小写，并要求不能默认接受未保护JWS。离线自有验证器比较允许列表、签名验证、issuer/audience/事务、claim到授权；只改is_admin、解码成功或大小写字串为反例，缺实际消费者不判admin，禁止交换真实token。\n\n规范核对：[RFC7518 none](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.6)。\n\n来源：[保存帖1](https://x.com/i/status/1502487219730219008)、[保存帖2](https://x.com/i/status/1502487222146068482)。"
  ],
  [
    "by-type/info-secrets.md",
    "客户供应商表截图不证明五千二百条越权",
    "完整图只有两小表的客户/供应商姓名、地址/电话部分遮蔽，正文称BAC泄露5.2k，未有endpoint、身份对照、全量或数据来源。\n\n离线合成对象比较正常所有者/非所有者、返回字段、预期公开与数据归属，用最小脱敏样例记录。文件可见、title人数、表格和合法导出不是越权证明；本人权限、样例/未知来源为反例，不批量读表、保存PII或把人数计已核实影响。\n\n来源：[保存帖1](https://x.com/i/status/1502422973759827968)、[保存帖2](https://x.com/i/status/1502530297862131714)、[保存帖3](https://x.com/i/status/1503324578478796803)、[保存帖4](https://x.com/i/status/1503324686591004672)。"
  ],
  [
    "reporting.md",
    "私项目沟通应关联 ticket 且待支付不等已支付",
    "完整回信说愿付up to250、要求PayPal信息，提醒ticket外沟通可能遗漏；正文称Open Redirect到StoredXSS私项目，未保存链。\n\n离线报告将同一ticket、问题、附件、回应、有效性与付款状态分别关联，按指定项目渠道准备可审材料。愿意支付、外部线程和赏金感受不补漏洞证据，也不等收款成功；缺状态/票据关联为反例，不发送消息或提供支付信息。\n\n来源：[保存帖1](https://x.com/i/status/1502589091392929792)。"
  ],
  [
    "scope-and-rules.md",
    "KYC 背景检查和 VDP 资格不是资产授权替代",
    "正文建议完成KYC/背景检查、读规则、从VDP和旧报告开始；另有未回应/不支付但修复的个案说法，未有当前规则或证据。\n\n离线区分平台身份、项目参与资格、资产/行为scope、接收类型、披露和奖励政策，记录规则版本及旧报告可复现性。平台通过、VDP名称、历史支付新闻和作者抱怨不是允许所有动作/承诺赏金；范围不明/不允许行为为反例，不提交个人证件或联系项目。\n\n来源：[保存帖1](https://x.com/i/status/1501493349844324352)、[保存帖2](https://x.com/i/status/1502614871929667589)、[保存帖3](https://x.com/i/status/1503017440908910594)。"
  ],
  [
    "by-type/xss.md",
    "regex source 拼接与 cookie 弹框仍依赖 reader",
    "正文有regex.source组合事件调用、window括号属性和十六进制al\\x65rt，Microsoft图弹框可辨MUID/MC1 GUID其余模糊，另仅RXSS Medium5.4状态。没有边缘链、完整DOM或其他读者/会话。\n\n离线分URL/form中加号、HTML属性/字符串、JS regex与实际事件执行，比较转义/CSP和无害标记。分析cookie、本人浏览器、报告级别、blocked/passed主张不是可用会话或普遍WAF绕过；无真实reader/不能重用为反例，不收集cookie或执行原payload。\n\n来源：[保存帖1](https://x.com/i/status/1502621725481406465)、[保存帖2](https://x.com/i/status/1502679109293457412)、[保存帖3](https://x.com/i/status/1502853563604938762)、[保存帖4](https://x.com/i/status/1503483711450275852)、[保存帖5](https://x.com/i/status/1503641037906006016)、[保存帖6](https://x.com/i/status/1503705646025572357)、[保存帖7](https://x.com/i/status/1503736101588340737)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "LinkFinder 的 JS 文本 endpoint 与实际可达 API 分开",
    "正文介绍从JavaScript提取endpoints及参数，没有输入JS、调用图或执行结果。\n\n离线合成JS对照字面量/拼接、base URL、动态加载、第三方库、旧源码与实际请求消费者，记录版本和过滤/错误。字符串、dead code和参数名称不等现存授权API或漏洞；无调用/来源归属为反例，不拉远程JS或批量访问候选。\n\n来源：[保存帖1](https://x.com/i/status/1502692400929685504)。"
  ],
  [
    "by-type/ssrf.md",
    "strcmp 黑名单比 hostname 与连接 IP 会留下不同边界",
    "完整演示slide画域名到169.254.169.254并写Bypassing strcmp，正文称读AWS metadata，但无DNS回应、实际抓取和字段。\n\n离线假DNS/抓取者记录输入hostname、URL解析、DNS结果、连接地址、重定向、校验时点和Host/SNI。只比较字符串不等已核目的IP；但图中箭头/品牌不证明实际请求。禁止地址已校验、固定连接或无字段为反例，不解析存档回连域或访问元数据。\n\n来源：[保存帖1](https://x.com/i/status/1502706736771514371)。"
  ],
  [
    "targeted-fuzzing.md",
    "二十五项 XSS dork 图实际为 query 字段名",
    "完整图列q/s/search/id/lang/keyword/page/year/email/type/name/month/immagine/url/key/begindate/enddate等25参数形状，未有搜索引擎语法或命中结果。\n\n离线字段目录保留真实输入来源、上下文、解码/反射/DOM消费者与读者，比较不反射/编码/无事件。名字或payload占位不等XSS；仅查询参数忽略JSON/header/form也不能算全输入覆盖，不批量发送源片段。\n\n来源：[保存帖1](https://x.com/i/status/1502729720890535937)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "DomainAlerting 日期文件行数不等新注册域覆盖",
    "完整图有日期目录、domain-names.txt的wc-l计数与head三行，正文说按关键词每日注册提醒，没有注册权威数据、查询条件或通知。\n\n离线快照保存提供者、注册/下载时间、hash、去重、错误/缺日与关键词匹配结果，再比较新增/首次观测/重新出现。行数、文件日期和通知工具名不能证明新注册或全部覆盖；重复/历史文件/缺数据为反例，不设置未经请求的自动提醒或访问域。\n\n来源：[保存帖1](https://x.com/i/status/1502754937729695749)、[保存帖2](https://x.com/i/status/1502964035402145795)。"
  ],
  [
    "by-type/open-redirect.md",
    "回连 token 和自动探测要核真正产生者",
    "正文称redirecturl回连带token/param0，完整图ngrok/Python HTTP日志出现一条含query的GET和.env/git/svn/robots等404；未有身份、token用途/权限或真实用户导航。\n\n离线自有合成导航与服务端扫描分别记录关联标记、发送者、请求时间、参数来源、会话绑定/失效与受保护动作。回连可来自扫描器、分诊者或普通传递；字段名token、200与探测日志不是ATO/加重等级，不开真实server/收token或触发callback。\n\n来源：[保存帖1](https://x.com/i/status/1502898662015643652)。"
  ],
  [
    "by-type/authn-session.md",
    "重置 URL 前缀接受须核解析后 hostname 与交付",
    "完整文字故事给正常email/url重置链接、改google后host为空、再用target.com.evil.com被拼入邮件；未保存完整请求/邮件字节或新会话。\n\n离线假重置消费者比较解析后hostname、scheme、端口、userinfo、子域边界与绝对/相对URL，在合成邮箱记录链接/事务/目标身份绑定。字符串含目标域不等同源；正常固定域/严格hostname拒绝为反例，作者故事不补实际交付/ATO，不发送邮件或试hashKey。\n\n来源：[保存帖1](https://x.com/i/status/1502947577309790214)。"
  ],
  [
    "by-type/ssti.md",
    "Go define template 是模板源码权限而非数据转义绕过",
    "正文给define/T1/template与script字面量并称Go SSTI/XSS bypass，没有引擎、Parse/Execute调用或输出。\n\nGo html/template假设模板作者可信并对Execute数据上下文转义；若攻击者控制Parse源码，字面脚本属于作者内容，这与普通数据插值不同。离线用无执行文本比较数据参数、模板源和明确的安全类型/引擎版本；未编译输入、被编码或CSP禁止为反例，不能推广全部Go应用。\n\n规范核对：[Go html/template security model](https://pkg.go.dev/html/template#hdr-Security_Model)。\n\n来源：[保存帖1](https://x.com/i/status/1502992243568922627)、[保存帖2](https://x.com/i/status/1503294744298164227)。"
  ],
  [
    "by-type/waf-bypass.md",
    "ASP NET 重复参数的拼接分隔符决定解析结果",
    "完整tip分两段同名parameter并声称ASP.NET/IIS无分隔拼成svg事件，没有HTTP/实际API或响应。\n\nMicrosoft NameValueCollection.Get返回同键值的逗号分隔列表，不等图中无分隔字符串；具体应用也可能first/last/array/自定义拼接。离线核API、版本、顺序、分隔与WAF/HTML/事件消费者，比较单值和拒绝重复。缺拼接链/多出字符破坏属性/CSP为反例，不声称所有IIS可绕。\n\n规范核对：[Microsoft NameValueCollection.Get](https://learn.microsoft.com/dotnet/api/system.collections.specialized.namevaluecollection.get)。\n\n来源：[保存帖1](https://x.com/i/status/1503257367403806722)。"
  ],
  [
    "by-type/xss.md",
    "preg_replace delimiter 错误要分结果与两次消费者",
    "完整训练图preg_replace提示No ending delimiter并显示源码：处理GET payload后进入JS name单引号，再拼到greeting.innerHTML。截图页面仍是问候，没有成功执行。\n\n离线先记录PHP字符串转义后的正则、错误/返回值/异常处理，再分别核JS字符串和HTML解析结果。过滤报错不能自动假设原文通过或成功XSS；空/null输出、正确编码、CSP与无真实事件为反例，不执行页面hook或源代码，只分析训练条件。\n\n来源：[保存帖1](https://x.com/i/status/1503281647034445824)。"
  ],
  [
    "by-type/xss.md",
    "JSON 字符串变对象只有代码消费者才会执行表达式",
    "完整图是单引号/name/alert(document.domain)片段，正文称JSON string变object初始化执行，但没有语法上下文或eval/JSON.parse消费者。\n\n离线分别核JSON语法、JS对象字面量、动态源码/eval与安全解析，保留输入到初始化语句的数据流。JSON.parse不把函数调用当合法JSON执行；语法拒绝、纯字符串和未插入JS源码为反例，不凭对象转换标题判断XSS或运行原片段。\n\n来源：[保存帖1](https://x.com/i/status/1503352199564468236)。"
  ],
  [
    "by-type/authn-session.md",
    "test test 与 token secret 题目仍缺身份结果",
    "正文称默认test/test与endpoint token-secret，完整图只有两个Medium标题，没有登录交换、端点字段或权限。\n\n离线自有身份模型分登录前后主体、预期角色、受保护对象与字段用途/失效状态，再比较拒绝与正常账号。默认账户名/两个报告题目不等有效凭据/秘密，示例值/后台拒绝为反例，不尝试密码或复用token。\n\n来源：[保存帖1](https://x.com/i/status/1503374254607376388)。"
  ],
  [
    "source-audit.md",
    "WordPress Editor 菜单缺失不等 PHP 功能被绕过",
    "完整图对比WordPress4.9.9普通主题/插件Editor与所谓our application没有Editor，正文是disable_functions到remote shell文章标题，没有PHP配置、请求或shell结果。\n\n离线自有权限模型区分菜单展示、capability/路由检查、文件编辑配置、代码写入和PHP运行时函数限制。隐藏菜单、角色不同、只源码编辑或未执行为反例；缺图中链不能推disable_functions bypass，不编辑真实主题/插件或安装shell。\n\n来源：[保存帖1](https://x.com/i/status/1503387483534413827)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "Lnkbomb 创建 recovery 和 removed 日志不证明 NTLM 获取",
    "完整图打印在网络share创建.url、生成.recovery并随后removed，没有文件hash/目录确认、读者打开、挑战响应或破解结果。\n\n离线假文件/网络消费者区分写入权限、shortcut格式、自动读取者、协议策略、运行身份与回连，恢复操作独立核原前后hash。文件生成名、清理打印或share可写不能证明凭据泄露；无读者/禁网络鉴权为反例，不创建/删除真实share文件、收集hash或破解。\n\n来源：[保存帖1](https://x.com/i/status/1503494891791343624)。"
  ],
  [
    "by-type/idor-access-control.md",
    "X Client IP 回环字段要核代理信任边界",
    "正文建议403增加X-Client-IP:127.0.0.1，无保存回应或网络身份。\n\n离线自有代理/后端模型分别记录连接真实peer、可信上游、可被客户端伪造字段、规范化及权限判断；比较同对象正常/伪造/未知peer。请求头存在、变200、缓存或公共页为反例，必须证明非可信输入改变同一受限对象授权，不发送真实伪造请求。\n\n来源：[保存帖1](https://x.com/i/status/1503625295319994368)。"
  ],
  [
    "by-type/sql-injection.md",
    "Spotify UNION 与返回数据库字串仍需基线归属",
    "完整BurpPOST adminajax图body含UNION ALL SELECT/from information_schema.schemata，响应track_streams类JSON末有sys/wordpress；未保存正常基线、身份/权限和任意查询范围。\n\n离线合成查询保留参数进入SQL消费者、列数/类型、原返回字段、独立无害标记与拒绝对照，绑定同一事务。反射、固定字段、只作者数据库名或已授权访问为反例；单截图不能证明任意表读取/当前部署RCE，不运行保存SQL或读取真实表。\n\n来源：[保存帖1](https://x.com/i/status/1503688432891031555)。"
  ],
  [
    "by-type/ssrf.md",
    "单次双次跳转都必须重核最终目的地址",
    "正文给一层PHP Location到回环和第二层再跳第一层，称同样可到元数据，没有实际抓取/重定向处理和结果。\n\n离线假HTTP抓取器逐跳记录URL解析、解析IP、连接、协议、端口、最大跳数与每跳校验，再对照禁跟随/目的地址拒绝。只首次检查与最终连接不同才有候选机制；不跟随、每跳拒绝或无后端请求为反例，不部署来源PHP/访问回环或云元数据。\n\n来源：[保存帖1](https://x.com/i/status/1503689761285804033)、[保存帖2](https://x.com/i/status/1503690674155130881)。"
  ],
  [
    "discovery/web-and-api.md",
    "WordPress 十二端点名不等可读配置或执行能力",
    "正文列wp-includes目录、index、login、opml、activate、blog-header、cron、links、mail、xmlrpc、settings、trackback，未有请求、权限或输入消费者。\n\n离线自有端点表分目录/脚本、正常公开功能、认证/动作、版本与返回字节，再以业务不变量设计比较。文件名存在、200或WordPress标识不是秘密/执行/漏洞，空输出/正确权限为反例，不批量调用cron/mail/xmlrpc或读取配置。\n\n来源：[保存帖1](https://x.com/i/status/1503740692346318851)。"
  ],
  [
    "by-type/authn-session.md",
    "支持邮件 From 到 ticket 账号必须验证身份来源",
    "完整图仅fake-mail composer的From victim、To support、plaintext、附件与Send按钮；正文称创建受害ticket和5000奖励，没有发送/交付/ticket或敏感动作。\n\n离线合成邮件模型分显示From、envelope、认证结果、入站规则、账号映射、ticket所有者和允许动作；比较伪造显示字段与可信认证绑定。composer、From字符串、送达与奖励不是越权结果；拒绝/隔离/正确映射为反例，不发送伪造邮件、操作他人ticket或使用真实地址。\n\n来源：[保存帖1](https://x.com/i/status/1503744476996640774)。"
  ],
  [
    "experiment-design.md",
    "虚拟机破坏和 CTF 练习需明确要验证的不变量",
    "正文主张新Linux VM动手至坏以及boot-to-root CTF可建立方法，没有实际问题、对照或验证产物。\n\n离线自有练习先列版本、身份/对象、权限和预期状态，再用可撤销无害输入观察、最小修复与复测，记录每个证据缺口。刻意脆弱训练/已经root不能证明真实站点同漏洞，单次成功不等全面能力；不操作真实系统或执行存档利用。\n\n来源：[保存帖1](https://x.com/i/status/1500137500748414978)、[保存帖2](https://x.com/i/status/1503071019015172098)。"
  ],
  [
    "discovery/passive-and-services.md",
    "子域 endpoint 参数三个阶段要保留关系和未知",
    "正文给三类recon目标、SingleFile保存页资源与Osmedeus可组合基础的主张，没有具体采集结果/流程验证。\n\n离线自有材料将asset→服务→endpoint→输入→消费者对应来源、时间、版本和授权，不把静态页面保存等同全部XHR/API业务流。工具列表、可整合宣传、快照文件存在或仅URL参数为反例，保留未采集动态状态/错误，不安装来源工具或访问外部内容。\n\n来源：[保存帖1](https://x.com/i/status/1499790928567017474)、[保存帖2](https://x.com/i/status/1501604028421402624)、[保存帖3](https://x.com/i/status/1501819492347019265)、[保存帖4](https://x.com/i/status/1501965681243279361)。"
  ],
  [
    "reporting.md",
    "拒绝表 accessible 与 acceptable 不是同一理由",
    "正文抱怨2000报告website not acceptable/cannot reproduce；完整表实际Website is not accessible及Can't reproduce vulnerability，未有原始复现或资格政策。\n\n离线按资产当前可达性、scope资格、请求/身份、附件与独立读者最小复现分别诊断，保留原文状态而非转换为平台有效性结论。拒绝计数、表格行数、作者情绪不等2000确认漏洞；目标不可达/步骤缺失为反例，不重新提交或联系项目。\n\n来源：[保存帖1](https://x.com/i/status/1503348044946972682)。"
  ],
  [
    "by-type/host-header.md",
    "SCIM 创建响应不能直接继承 Host Header pre ATO 结论",
    "保存正文称Host Header Injection导致preATO；图片可辨SCIM users POST携带不同Host并返回201及用户JSON。它只显示创建响应，未保存正常Host同请求对照、身份权限、链接生成或邮件交付。\n\n在隔离的本地SCIM模拟中固定认证身份、用户对象和请求体，仅改变合法测试Host；记录入口代理实际转发值、创建对象归属、返回URL消费者、邀请或恢复流程绑定。若入口忽略Host、URL固定基准域或最终身份需受害者独立确认，则创建201不构成接管。保存字段微小/遮蔽限度，不猜具体账号，不创建生产用户或发送邮件。\n\n来源：[保存帖](https://x.com/i/status/1500065269703610375)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Dome active passive 解析命中要保留模式与 wildcard 边界",
    "Dome卡片本身没有实现；另一保存图可辨1.1版本、active模式50线程、resolvers和wildcard check，active/passive found域名IP列表。正文工具能力介绍和这些输出不能证明检查了开放端口，也不能确认当前资产归属。\n\n用离线合成域名/解析结果保留provider、模式、resolver来源、时间、域→IP关系和wildcard对照；比较已知随机子域与明确主机，记录解析失败、共享IP和过滤丢失。passive来源旧条目、active仅DNS可解析、wildcard与业务域共享IP都是反例；根据目标真实授权决定是否后续验证，不能由工具能力说明继承许可。不执行图中网络命令。\n\n来源：[保存帖](https://x.com/i/status/1502981461342920709)、[另存介绍](https://x.com/i/status/1503001029759348737)。"
  ]
]
ids={pid for row in json.loads((W/"batch-0124.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert len(urls)==116 and all(pid in ids for pid in urls)
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
 summary=summary.replace("|","｜")
 assert "|" not in summary and "\n" not in summary
 routes.append(f"| {title} | {summary} | [方法条目](../{f}) |")
for p,parts in grouped.items():p.write_text(p.read_text()+"".join(parts))
community.write_text(c.replace(marker,"\n"+"\n".join(routes)+"\n"+marker,1))
print("Added",len(facets),"facets/routes to",len(grouped),"topics;",len(urls),"batch-bound URLs")

