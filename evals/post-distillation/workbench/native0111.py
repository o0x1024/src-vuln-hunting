"""Append manually distilled0111 facets after precheck. Own helper only."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "by-type/open-redirect.md",
    "前缀过滤重定向与斜杠消费者对照",
    "截图称正常绝对URI返回403，前置斜杠后绕过；另两帖列三斜杠、无双斜杠scheme与反斜杠组合，没有Location或最终目的地。\n\n固定获准跳转参数，比较服务端过滤、URL解析、响应Location与浏览器最终origin；相对站内路径、统一错误页、未跟随跳转或不同base是反例。前缀字符串不等于外部origin，不能把这些形态视为通用绕过。\n\n来源：[保存帖1](https://x.com/i/status/1441390877931229189)、[保存帖2](https://x.com/i/status/1444599877082619910)、[保存帖3](https://x.com/i/status/1445026114666123270)。"
  ],
  [
    "source-audit.md",
    "文档安全警告检索转为具体实现假设",
    "正文替代文字与截图给grep-HanriEC2检索deprecated、unsafe、must not及common pitfall等词，并保留两行上下文。\n\n对每个命中记录文档版本、调用契约、危险默认值、调用者/配置及到达条件，再追到实现与受控反例；历史弃用提醒、未使用接口或只是说明词是反例。匹配数量不证明漏洞，安全方法写为可独立使用的审计步骤，不能要求读取原归档或当前目录。\n\n来源：[保存帖1](https://x.com/i/status/1441412213038714888)。"
  ],
  [
    "targeted-fuzzing.md",
    "多字典URL拼接的输入契约与CSV解析",
    "ffuf帖给URL与FUZZ两个字典、200筛选、CSV输出后awk取第三列；Haklistgen图只是人物词汇文本，Bopscrk图为歌词短语1342经长度过滤1202。\n\n固定占位符/运行模式、base尾斜杠与路径、笛卡尔组合预算，用CSV解析器保留引号/逗号/表头与原响应身份；重定向/统一200、词表候选、列错位或截断是反例。词表数量不等于有效口令，未执行字典枚举或登录尝试。\n\n来源：[保存帖1](https://x.com/i/status/1441617313250172930)、[保存帖2](https://x.com/i/status/1441511314082435074)、[保存帖3](https://x.com/i/status/1444999349403017222)。"
  ],
  [
    "discovery/web-and-api.md",
    "侦察流水线的阶段产物与路径展开",
    "正文串subfinder、httprobe与aquatone，自述210个子域并把输出路径写为波浪号紧接工具名。\n\n核对域名空格、每段stdin/stdout类型、授权资产、超时失败与输出目录实际展开，保存候选/存活/页面截图各阶段数和hash；未展开目录、统一页、缺阶段产物或210候选是反例。截图可定位功能，不能证明敏感信息或全部子域覆盖。\n\n来源：[保存帖1](https://x.com/i/status/1441668074218745856)。"
  ],
  [
    "by-type/file-upload.md",
    "上传导图中的解析消费者与触发条件",
    "三张导图副本列后缀/MIME/魔数、WindowsADS、图片SVG/GhostScript、音视频ffmpeg/HLS、XML/OOXML/ODF、ZIP链接和配置文件分支。\n\n先画上传→校验→存储→预览/转换/解压→受害读者的链，绑定具体OS、handler、版本、内容类型和权限；保存可控字节、读取身份、受控marker与原样合法文件对照。扩展名或Content-Type变化、仅存储、静态下载、无对应转换器是反例；历史CVE标签不等于任意图片RCE，像素洪泛/批量资源消耗不执行。\n\n来源：[保存帖1](https://x.com/i/status/1441716242386231301)、[保存帖2](https://x.com/i/status/1442781222405505025)、[保存帖3](https://x.com/i/status/1444964055182036995)。"
  ],
  [
    "by-type/business-logic.md",
    "业务功能的端点操作身份矩阵",
    "作者自述连续35份业务报告并建议查不同端点，没有保存报告原文。\n\n按同一业务对象、创建/读取/修改/审批、Web/API/客户端与角色/租户记录请求、前置状态和权威后置状态，比较owner/非owner/未验证身份；只是可见页面、响应变化、历史奖励或无跨边界效果是反例。35是作者统计，不提升为已复现数量。\n\n来源：[保存帖1](https://x.com/i/status/1441730255878688778)。"
  ],
  [
    "discovery/web-and-api.md",
    "SSH反向隧道转代理的两端角色",
    "正文在本地向VPS建-R8080到本地127.0.0.1:8080的SSH隧道，再于VPS用本地回环端口代理。\n\n明确VPS监听端→SSH通道→工作机代理端，分别确认绑定接口、端口冲突、隧道进程、TLS信任与代理历史中实际请求/响应；SSH进程存在、curl启动或HTTP失败是反例。把隧道建立与捕获收据分别记录，本轮未建立连接或修改CA。\n\n来源：[保存帖1](https://x.com/i/status/1441845685943345154)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "侦察数据库配置中的端点身份和TLS校验",
    "BBRF示例含VPS CouchDB、用户名/口令占位、通知字段并设置ignore_ssl_errors true；ELK帖只述收集和可视化。\n\n保留授权endpoint、来源/时间/方法、对象身份、失败计数和去重键，凭据/通知字段用占位符；按端点配置受信CA，区分数据储存/检索/可视化与真实验证。忽略TLS校验、同名数据或仪表盘展示不是可靠来源证明，不导入原帖秘密或发送通知。\n\n来源：[保存帖1](https://x.com/i/status/1441891893114114051)、[保存帖2](https://x.com/i/status/1444936978865156099)。"
  ],
  [
    "by-type/saml-sso.md",
    "SAML浏览器往返的SP与IdP信任边界",
    "图画SP产生请求、浏览器转IdP认证、IdP响应经浏览器送ACS再登录，没有签名检查实现。\n\n绑定SP/IdP/ACS、请求身份及会话、被验签的具体节点、issuer/audience/recipient/时间和重放检查；合法登录序列、只存在SAML响应、缺签名实现或配置不匹配是反例。流程图用于定位校验点，不能补出签名绕过。\n\n来源：[保存帖1](https://x.com/i/status/1441792688769011715)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "社交登录共享信息提示与真实授权范围",
    "邮件图称登录Rell并共享name and profile picture，可Edit Settings；不是数据库或API响应。\n\n区分consent提示、实际scope、访问token主体/受众及第三方实际字段读取，以自有授权数据验证最小权限和撤销后读者；预期共享、提示邮件或名字头像不是泄漏证据。通知日期不替代当前授权状态，未访问第三方账户或使用token。\n\n来源：[保存帖1](https://x.com/i/status/1441917902391816196)。"
  ],
  [
    "by-type/authn-session.md",
    "分号路径上的认证授权与应用状态差异",
    "截图同一JWT在Settings路径收到401，标为FORBIDDEN；加入分号后200且JSON出现权限字段true，路径和数据部分打码。\n\n保留两条完整raw target、身份/方法/参数及应用最终对象，检查网关匹配、路由/分号规范化与同一权限检查链；401不是403，200/配置字段true不自动证明更改已持久化。匿名/低权对照和独立读取状态是必要反例，本案例不能概括只影响Java。\n\n来源：[保存帖1](https://x.com/i/status/1441970176501567492)。"
  ],
  [
    "reporting.md",
    "报告质量与公开信息的可识别组合",
    "正文强调准确可复现无偏报告；另一帖提醒程序名、细节和客户引用组合可能识别目标。\n\n写清获准范围、请求身份、前后状态、最小复现、反例和未证实链，公开前按适用披露约定去标识化组合字段；打码用户名但暴露路径/时间/唯一响应仍可能可识别。奖励、程序争议和自称FULL VALIDATED不替代技术证据，未发送报告或公开原始数据。\n\n来源：[保存帖1](https://x.com/i/status/1442066145700458496)、[保存帖2](https://x.com/i/status/1444338854526394369)、[保存帖3](https://x.com/i/status/1442127316465844244)。"
  ],
  [
    "hunting-strategy.md",
    "漏洞分类导图转为功能和信任边界路线",
    "Web导图列注入/SSRF/IDOR/缓存/竞态等，另图列侦察分支和为何构建网站、测试145项目但未展开。\n\n从获准业务功能定位输入、身份/对象、处理器、存储、跨origin读者，再选相关专题与具体假设；总览节点、折叠数字或工具链接不说明这些方法均已跑完。按业务可达性与证据选路，不机械遍历每类。\n\n来源：[保存帖1](https://x.com/i/status/1442074897170132993)、[保存帖2](https://x.com/i/status/1444144856369033223)。"
  ],
  [
    "by-type/authn-session.md",
    "MFA导图中界面修改与服务端授权的分离",
    "导图把successfalse改true、401改200、Referer、直接访问、旧会话、备用码、重用和跨账号OTP均列绕过，还建议大量重复请求。\n\n按登录/启用/禁用/恢复/改邮箱/备用码建立挑战对象、主体、会话、用途、期限、次数和服务器权限状态，使用自有受控身份最小对照；只改客户端响应、旧合法会话、跳过页面但API拒绝是反例。真正绕过需独立受保护动作的服务端证据，不沿图执行100至200重复或验证码穷举。\n\n来源：[保存帖1](https://x.com/i/status/1442075033791258629)。"
  ],
  [
    "by-type/waf-bypass.md",
    "跨字段拼接与终端HTML上下文",
    "图把firstname末尾img开标签与lastname属性/事件合并成页面弹窗。\n\n定位字段是否被同一模板拼接、分隔符、逐字段编码及最终HTML token/DOM，分别比较单字段与组合的受控marker、origin/CSP及触发；纯文本/独立DOM安全插入、事件未触发或误拼接是反例。字段级扫描未见完整字符串仅提示检查组装层，不证明所有WAF可绕。\n\n来源：[保存帖1](https://x.com/i/status/1442091593293574145)。"
  ],
  [
    "scope-and-rules.md",
    "项目搜索结果与当前明确授权",
    "正文给bugbounty相关Google查询，Chaos图按bountytrue和平台筛URL后下载/解压/删除zip；discloseio帖给历史2297等政策计数。\n\n记录候选来源/时间，回到当前项目政策核对域/对象/身份/方法，单列第三方与禁止动作；搜索命中、bountytrue、邀请程序名或goodfaith计数都不是授权。保留候选清单与来源即可，不执行下载解压删除或扩大项目范围。\n\n来源：[保存帖1](https://x.com/i/status/1442351256043802631)、[保存帖2](https://x.com/i/status/1443980460896436228)、[保存帖3](https://x.com/i/status/1443787767922659360)。"
  ],
  [
    "discovery/passive-and-services.md",
    "空间搜索的证书域名与HTTP响应角色",
    "C2搜索图有IP、证书签发者/受体域名和IIS8.5、404/Content-Length0；cero帖建议所有IPv4或云范围取证书。\n\n区分颁发者组织、受体CN/SAN、观测IP/时间/服务、DNS当前归属与当前范围，采用已有被动证据并仅核对获准资产；CA组织、证书名字、404、共享云IP或所有IPv4建议是反例。命中不能证明C2、漏洞或资产所有权，本轮未扫描全网。\n\n来源：[保存帖1](https://x.com/i/status/1442480662540292099)、[保存帖2](https://x.com/i/status/1446010048556195843)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "网页技术指纹库与实际漏洞的验证差距",
    "WebStor图把DNS传送/端口/HTTP响应和Wappalyzer导入数据库，再按名称regex取URLs/IPs；Cariddi自述130kURL十分钟50目标。\n\n按域/IP/端口/Host/SNI、响应hash、时间、权限和扫描方法保存数据，分开候选、存活、匹配和确认；关键词、历史指纹、同名响应或吞吐自述不能证明当前漏洞。数据库复用仍要当前范围与版本/配置验证，不执行DNS传送或全量扫描。\n\n来源：[保存帖1](https://x.com/i/status/1443323240219299840)、[保存帖2](https://x.com/i/status/1442536830574993408)。"
  ],
  [
    "by-type/authn-session.md",
    "限流验证与猜测凭据的动作边界",
    "正文问限流在范围但密码暴力不在范围如何判断；SharpSpray图只有AD/Csharp/LDAP标题。\n\n先以当前政策确定允许的自有账号、固定无效marker、请求预算和恢复间隔，观察配额键/挑战/锁定状态；随机密码、轮换多人账户、广告称avoidlockouts或无错误均不能作为授权。限流和凭据猜测分开描述，本輪未认证或喷洒。\n\n来源：[保存帖1](https://x.com/i/status/1442697923247034368)、[保存帖2](https://x.com/i/status/1442824979951800327)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "库存功能命令输出与受控输入因果",
    "图片显示库存POST表单storeId后附命令片段，200返回Linux uname样式文本，像实验室页面。\n\n确认实际调用shell/argv、可控字段、执行身份、低影响marker和独立对照，区别正文回显、预置演示响应或合法固定uname输出；200和OS文本单图未证明生产RCE。截图中的session不复制使用，不发命令。\n\n来源：[保存帖1](https://x.com/i/status/1442757285143482372)。"
  ],
  [
    "by-type/xss.md",
    "注册查询参数进入meta属性的浏览器读者",
    "阿拉伯语帖述拦注册请求改payload与cookie，图显示registerdo参数闭合meta og:url属性并形成script，另图浏览器弹出cookie样式值。\n\n绑定GET/POST区别、响应实际属性字节、HTML解析/DOM、受害者origin及触发前提，使用无秘密marker验证；单人自注入、无法让另一读者访问、HttpOnly不可读或无法确认cookie认证价值是反例。截图支持该浏览器观察，不补出全部cookie可读/会话接管，秘密值不复制。\n\n来源：[保存帖1](https://x.com/i/status/1442871467025203202)。"
  ],
  [
    "by-type/waf-bypass.md",
    "点击链接混合编码的上下文与浏览器条件",
    "图片标题声称Akamai全部浏览器有效，包含实体/控制字符的hrefjavascript与点击文本并把location发送到外站。\n\n拆分raw编码、URL解码、HTML实体、属性解析、javascript消费者和用户点击，保存具体浏览器/版本、CSP、WAF规则与无外传marker；锚点不点击、scheme被拒、只有静态字符串或未知后端是反例。单张payload卡不支持全部浏览器/全部配置，未外传location。\n\n来源：[保存帖1](https://x.com/i/status/1443042803760517127)。"
  ],
  [
    "by-type/xss.md",
    "无效UTF8触发旧登录页的版本和回退路径",
    "cPanel帖有loginuser事件payload，图SEC596描述无效UTF8触发LegacyLogin输出编码不足，列修复11.98.0.8和11.94.0.16。\n\n把字节解码失败→旧模板选择→用户字段输出→focus/fragment触发分开核对，记录安装build、具体浏览器和CSP；新模板、已修复、属性正确编码或无法触发是反例。图是历史公告摘录，不据此判当前cPanel均受影响。\n\n来源：[保存帖1](https://x.com/i/status/1443092453809065986)。"
  ],
  [
    "by-type/xxe.md",
    "XML候选位置与实际DTD外部实体配置",
    "正文列SVG/sitemap/SAML/HTML/SOAP/XMLAPI；上传图还有OOXML/ODF。\n\n按获准功能定位谁解析XML、解析器版本/DTD和外部资源开关、转换/预览/存储过程及网络/文件权限，用受控无秘密marker与关闭解析对照；HTML普通渲染、静态XML下载、实体禁用或只扩展名为XML是反例。候选面不意味着任意文件读取或SSRF。\n\n来源：[保存帖1](https://x.com/i/status/1443236724629336070)、[保存帖2](https://x.com/i/status/1441716242386231301)、[保存帖3](https://x.com/i/status/1444964055182036995)。"
  ],
  [
    "by-type/info-secrets.md",
    "公开邮箱候选与泄漏凭据的事实边界",
    "Zen图描述找GitHub用户邮箱，正文把员工邮件/泄漏和credentialstuffing连在一起，未保存有效凭据。\n\n记录公开出处、时间、组织关联可信度、必要最少字段，区分邮箱地址、历史泄漏记录与当前认证秘密；同名/离职/公开联系方式/查询无结果是反例。不能将邮箱列表称为有效口令或全体员工，不查询泄漏密码或尝试登录。\n\n来源：[保存帖1](https://x.com/i/status/1443267207069421578)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Base64身份token与对象级授权并非等同",
    "IDOR漫画示范改Base64token内id读取他人记录并说弱session/不应使用用户输入；小副本正文仍可辨但细节有限。\n\n区分token完整性/身份来源与每次对象/动作/租户授权，建立自有owner/非owner、GET/写操作对照；编码可解码本身无漏洞，签名有效/不可篡改仍可能对象授权缺失。受控对象和有效拒绝是反例，不能把全部IDOR归因为session或禁用所有对象输入。\n\n来源：[保存帖1](https://x.com/i/status/1443473395090219012)。"
  ],
  [
    "by-type/idor-access-control.md",
    "API密钥签发对象与权限证明",
    "保存1/2描述生成密钥需user_id及email；Ghost图仅列adminAPI路径200，没显示密钥字段和低权identity。\n\n将签发、读取、权限scope/受众、撤销和实际获准动作分别核对，使用两自有对象和最小无秘密标记；改参数、200路径、未保存响应/另一身份或未知密钥能力是反例。缺续文按覆盖处理，不补任意密钥或管理员接管。\n\n来源：[保存帖1](https://x.com/i/status/1443490637546856455)、[保存帖2](https://x.com/i/status/1446345820412923906)。"
  ],
  [
    "by-type/authn-session.md",
    "模型预测口令与认证结果的区别",
    "SharpML图从共享文件数据/规则与AD用户输入模型，再产用户口令对并连接Login，未给实际认证结果。\n\n绑定数据授权、候选来源、质量/偏差和模型产物，不收集真实口令；模型预测、弱密码分类、用户名配对或共享文件权限不证明可登录。认证动作另需明确范围，本轮未读取共享目录/AD或验证候选。\n\n来源：[保存帖1](https://x.com/i/status/1443549861320736770)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "S3词典枚举的Host与资源权限分离",
    "正文ffuf原请求Host带http scheme，过滤404400并建议300线程；无实际桶响应。\n\n先校验requesttarget、authorityHost、SNI与具体S3 endpoint类型，分开桶存在、列目录、对象读取、账户归属和授权；错误Host、403、代理统一响应、历史名称或公开预期对象是反例。用获准自有桶最小对照，不能沿帖进行300并发或认领桶。\n\n来源：[保存帖1](https://x.com/i/status/1443591814611492874)。"
  ],
  [
    "by-type/authn-session.md",
    "PKINIT与ADCS图示的具体证书身份",
    "PKINIT终端显示请求并保存TGT，ADCS图只有Root/SubCA颁发/安装关系；Kekeo图画AS/TGS/AP往返。\n\n区分证书subject映射、模板ACL/用途、链信任、TGT主体和服务票据权限，保存具体身份/版本与合法基线；合法申请TGT、证书安装或协议流程图是反例。没有模板配置/跨主体证据，不补域管理员提权、私钥窃取或登录。\n\n来源：[保存帖1](https://x.com/i/status/1443700911105261580)、[保存帖2](https://x.com/i/status/1443912254383136773)、[保存帖3](https://x.com/i/status/1444274497960427520)。"
  ],
  [
    "reporting.md",
    "受理修复署名和奖励评估的不同终态",
    "Apple图分别写reviewinvestigating、无法再复现/署名询问和possible rewardevaluation；另图功能问题不是安全漏洞，Crowdin礼盒。\n\n保留原报告ID占位与各次日期/状态，区分受理、技术确认、修复复测、署名和奖金结论；礼盒、受理邮件、still evaluating或奖励金额不是技术复现。复测保存旧基线与当前拒绝/状态，不将沉默或评价猜成最终结论。\n\n来源：[保存帖1](https://x.com/i/status/1443211615801860100)、[保存帖2](https://x.com/i/status/1444361007548174339)、[保存帖3](https://x.com/i/status/1443866356336582660)、[保存帖4](https://x.com/i/status/1443947353430319111)。"
  ],
  [
    "by-type/desktop-client.md",
    "下载文件完整性与被替换执行链",
    "帖子称未完整性校验使替换exe执行，奖励图只给No secure integrity check of downloaded file200。\n\n核对权威下载源、传输/重定向、期望hash/签名来源、验证位置、写权限与最终加载/执行身份；缺UI校验、同源可改hash、合法签名文件或仅手动运行是反例。端到端替换执行需实际信任边界证据，奖励不补二进制执行，本轮未下载或运行。\n\n来源：[保存帖1](https://x.com/i/status/1444019438634819595)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "系统代理CA与捕获请求的不同收据",
    "Proxverter图列importcert、setsysproxy、engage、delsysproxy，使用回环8081和is_https。\n\n确认API版本、代理协议/端口、CA信任store、浏览器是否采用代理和实际HTTPS历史，再独立记录原配置/恢复结果；导入成功、浏览器启动、API调用或连接错误不是捕获证明。未安装CA、改系统代理或访问目标。\n\n来源：[保存帖1](https://x.com/i/status/1444026540422017034)。"
  ],
  [
    "by-type/business-logic.md",
    "银行业务三类假设与权威交易状态",
    "正文列篡改支付通信、回调未校验、虚拟卡号可预测，没有完整通信；付款测试图述误用真卡而扣款。\n\n在沙箱/明确允许自有对象内核对订单主体、价格来源、回调验签/时效/重放、余额/交付的权威账本，卡号预测与有效卡/授权交易分别验证；成功页面、无OTP、可猜号码或客户端价格是反例。保留预算/停止点，不使用真卡或产生真实交易。\n\n来源：[保存帖1](https://x.com/i/status/1444155911908429825)、[保存帖2](https://x.com/i/status/1445112073772417024)。"
  ],
  [
    "discovery/web-and-api.md",
    "HTTP方法和状态码的具体语义与应用动作",
    "方法图列GETHEADPOSTPUTDELETECONNECTOPTIONSTRACE，状态图把3xx全概括为跳到不同资源。\n\n按实际endpoint/身份/内容类型/对象核对方法路由、状态、响应体和服务器副作用；HEAD/OPTIONS展示、200错误体、304缓存协商或标准方法名是反例。GET预期安全不保证实现无副作用，3xx并非均跳到外站，枚举允许方法不能代替授权测试。\n\n来源：[保存帖1](https://x.com/i/status/1444167525223124994)、[保存帖2](https://x.com/i/status/1444171214050582529)、[保存帖3](https://x.com/i/status/1444192473689903113)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "Flexbe模板命中与可认领服务条件",
    "图仅示nuclei2.3.4加载一模板并命中flexbe takeover high，正文指向模板PR和issue。\n\n保留模板版本/hash、请求响应与DNS/服务绑定状态，核对已解除绑定、第三方认领机制和范围允许的无接管证明；high标签、统一错误页、仍有owner或无法注册是反例。扫描命中是候选，未执行模板或认领。\n\n来源：[保存帖1](https://x.com/i/status/1444220039335268353)。"
  ],
  [
    "by-type/document-rendering.md",
    "CSV导出中的公式解释与后续程序执行",
    "正文把上传/导出CSV直接称RCE，替代文字只是服务广告，未保存公式。\n\n追踪不可信单元格→CSV字段转义→导入软件/版本/设置→公式解释/提示→后续动作，比较纯文本和安全标记；CSV本身不执行、软件不解释、仅公式求值或用户未操作是反例。公式注入/外部连接/命令执行分别取证，不能统一提级RCE。\n\n来源：[保存帖1](https://x.com/i/status/1444232592127979521)。"
  ],
  [
    "by-type/ssrf.md",
    "fileURL由哪个服务端消费者处理",
    "正文列file路径/多斜杠与ssrfphp参数并说可读服务器文件，未给响应。\n\n固定实际serverfetch库/允许scheme、URL解码/规范化、沙箱和文件权限，以自有无秘密文件marker验证；浏览器file导航、禁scheme、无读取接口或仅参数反射是反例。file读取不同于HTTP网络SSRF，未访问系统文件。\n\n来源：[保存帖1](https://x.com/i/status/1444245949996417031)。"
  ],
  [
    "by-type/authn-session.md",
    "OTP请求控制字段与挑战最终状态",
    "注册OTP图只有POST请求，result_ids指otpdiv、dispatch标verifyregister及OTP字段，没有响应或已验证状态。\n\n核对字段是否只是视图selector、派发器、挑战subject/用途/期限、验证码真实检查和注册后服务器verified状态；修改result_ids、任意验证码请求、200展示或token仅预认证是反例。截图提出控制字段假设，不能单独确认OTP绕过。\n\n来源：[保存帖1](https://x.com/i/status/1444263673594146820)。"
  ],
  [
    "source-audit.md",
    "反汇编system导入与可达命令边界",
    "r2图从afl usefulFunction到反汇编/bin/ls/systemcall，再看system导入跳转；efi图为仿真SMIhandlerreturned记录。\n\n绑定样本hash/架构、调用约定、参数数据流、触发函数和权限，区分固定命令/合法函数与受控外部输入；system符号、仿真handler正常return、静态字符串或调用约定warning是反例。只用于静态定位，未运行归档二进制/固件/仿真器。\n\n来源：[保存帖1](https://x.com/i/status/1444296727729631232)、[保存帖2](https://x.com/i/status/1444636891278725127)。"
  ],
  [
    "impact-and-acceptance.md",
    "历史CVE热度与具体漏洞影响分离",
    "9月CVE曲线列多个编号，未定义纵轴采样；正文说not all bugs critical，另GoogleForms称低影响intended。\n\n将图的数据源/单位/窗口、产品版本和真实业务影响分开；峰值、奖励、作者不认同或CVE编号不能提升当前严重度。以被跨越的身份/对象/动作/数据/范围和反例证明影响，缺文章正文不补GoogleForms机制。\n\n来源：[保存帖1](https://x.com/i/status/1444487404182650881)、[保存帖2](https://x.com/i/status/1444623707683659777)、[保存帖3](https://x.com/i/status/1446325840925454339)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "侦察自动通知的阶段完成与证据保留",
    "Morya正文称bash侦察加Discord通知，AttackSurface图DiscoveryDB→Nmap→各模块→ReportAlert循环。\n\n每阶段保留获准输入、版本、请求预算、具体产物/失败、来源hash和去重身份，仅授权模块进入执行；循环/通知/工具成功不等于覆盖或漏洞确认。喷洒/暴力/Metasploit与截图展示分开，无发消息指令时不发送外部通知。\n\n来源：[保存帖1](https://x.com/i/status/1442548354936803330)、[保存帖2](https://x.com/i/status/1444991322260074501)、[保存帖3](https://x.com/i/status/1446237506094120962)、[保存帖4](https://x.com/i/status/1443816530228121604)。"
  ],
  [
    "by-type/ssrf.md",
    "OAST服务配置和目标回调的来源绑定",
    "正文称interact旧域变化并给带空格的aliasnuclei参数，另一图把iframe样式插入请求但200长度0。\n\n按当前工具帮助确认server选项/版本，记录独一marker、请求身份、回调时间/协议/源和控制请求；alias拼写、空响应200、浏览器或研究者自身访问回调是反例。区分OAST基础设施健康与目标服务端访问，未启动工具或触发外传。\n\n来源：[保存帖1](https://x.com/i/status/1444994148717662210)、[保存帖2](https://x.com/i/status/1444965167666712576)。"
  ],
  [
    "hunting-strategy.md",
    "少见漏洞的消费者跨层路线",
    "保存列表1到4为HTTP2smuggling、OfficeXMLXXE、PDF生成XSS→SSRF、SVGXSS，后续未保存。\n\n从实际前后端HTTP解释、Office解包XMLparser、服务器渲染器网络权限和SVG读取上下文挑专题，保留输入/消费者/受害读者/对照；只是支持PDF/SVG上传、HTML静态存储或库标签是反例。缺后6项按覆盖处理，不虚构完整十项或通用链。\n\n来源：[保存帖1](https://x.com/i/status/1445103677744852994)、[保存帖2](https://x.com/i/status/1446128183137370122)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "WordPress用户路径拼接与数据公开性",
    "正文awk把每行域名追加wpjsonwpv2users；方括号是帖子包装，未给返回内容。\n\n用URL解析规则处理schema/尾斜杠/路径base，保留获准目标和精确endpoint，再核对响应公开字段/角色与当前策略；打印路径、404、公开作者名单或空结果是反例。生成清单不证明用户名泄漏/账户接管，未访问端点。\n\n来源：[保存帖1](https://x.com/i/status/1445352023445155841)。"
  ],
  [
    "by-type/automotive-security.md",
    "车辆工具菜单中的观察与发送动作",
    "CarPunk菜单分CANinterfaceupdown、sniffrecordplay，没有操作结果。\n\n绑定获准隔离测试设备、总线/协议和测试状态，区分被动观察/记录与接口状态改变/报文回放的副作用；菜单、选项号或工具启动不是车辆控制证明。记录功能边界与停止条件，本轮未连接设备或发CAN报文。\n\n来源：[保存帖1](https://x.com/i/status/1445361637930700807)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "Apache旧版本路径规范化与CGI条件",
    "旧图分别见2.4.49读取passwd、2.4.48返回400，另图2.4.50本地CGI500后临时marker文件出现，以及49/50响应daemonuid。\n\n绑定构建/配置、Alias映射、目录拒绝规则、原始编码路径和请求体；文件读取与CGI执行分别证明，500并不排除副作用但仅500无执行证据。官方说明41773影响49，42013为49/50修复不完整，需目录权限条件、CGI启用才可能执行，不能把50统称41773或所有Apache受影响。依据：[Apache官方公告](https://httpd.apache.org/security/vulnerabilities_24.html)。未读取文件/发CGI命令。\n\n来源：[保存帖1](https://x.com/i/status/1445386557574324234)、[保存帖2](https://x.com/i/status/1445677701029789698)、[保存帖3](https://x.com/i/status/1446024810316828673)、[保存帖4](https://x.com/i/status/1446247473694003202)、[保存帖5](https://x.com/i/status/1446426613881745413)。"
  ],
  [
    "targeted-fuzzing.md",
    "批量路径脚本的原始字节和响应特征误判",
    "正文sed给目标追加cgi编码点段，再httpxmatchroot；没有运行收据。\n\n检查尾斜杠/原target、客户端规范化、每行授权与预算、实际响应而非仅匹配字符串，建立安全自有marker和失败对照；统一HTMLroot文本、客户端已去点段、混合base或命中不含文件结构是反例。批量匹配候选不证明CVE、文件读取或RCE，未执行脚本。\n\n来源：[保存帖1](https://x.com/i/status/1445667010508062722)。"
  ],
  [
    "by-type/authn-session.md",
    "缓存激活和邀请链接的对象生命周期",
    "正文称cachedactivationreset可攻破，另帖从档案发现上千projectteaminvites并自述非成员可加入。\n\n把发现时间、链接对象/租户/权限、受众、一次性/过期/撤销与消费后的权威membership分开，使用自有邀请最小对照；过期/已消费、预期公开邀请、需原owner或只见历史URL是反例。数量不等有效邀请数，不打开第三方reset/activation或加入团队。\n\n来源：[保存帖1](https://x.com/i/status/1445389563783000087)、[保存帖2](https://x.com/i/status/1445958287929880576)。"
  ],
  [
    "by-type/prototype-pollution.md",
    "原型污染库定位与gadget分开的数据库复用",
    "图DetectionSelenium/extension/CodeQL→关键词/断点/阻断JS定位库→sourcegadget，再存librarygadget库和被动regex检索。\n\n记录库hash/版本、可控合并输入、实际prototype写入、具体gadget读属性到sink与受害origin，用移除库/禁source/无害marker对照；关键词、网站引入库、断点或主动屏蔽导致页面坏掉是反例。数据库匹配与污染、污染与XSS各单独取证，作者18/80/1000自述不当当前确认数。\n\n来源：[保存帖1](https://x.com/i/status/1445403406571614214)。"
  ],
  [
    "by-type/xss.md",
    "BBCode转换后的HTML与原文属性界面",
    "正文提醒BBcode可有XSS，但外链实现未保存；另帖lng值闭title后iframe，未给响应。\n\n定位BBCode解析器/允许标签与属性、转换后编码和最终读者DOM；title文本结束、iframe插入和脚本执行分别取证，嵌入跨origin不自动读取外站或当前cookie。纯文本BBcode、正确编码、sandbox/CSP或只能自看是反例。未加载图中外站scriptlet。\n\n来源：[保存帖1](https://x.com/i/status/1445431001199611907)、[保存帖2](https://x.com/i/status/1445717253928808453)。"
  ],
  [
    "by-type/sql-injection.md",
    "UNION适用查询位置与独立返回证据",
    "正文仅说明SELECT可UNION两结果；另帖问时间盲注扩展，无具体请求。\n\n先确认参数到实际查询位置/DB语法/列数类型与页面可见结果，分别设计安全真假标记或受控小延迟随机对照，记录基线抖动/重复次数；仅关键词、网络慢、统一错误或无反馈是反例。基本语法不是任何endpoint可注入，工具名称不能替代因果证据，不执行SQL。\n\n来源：[保存帖1](https://x.com/i/status/1445571199816192002)、[保存帖2](https://x.com/i/status/1445439808482865154)。"
  ],
  [
    "by-type/info-secrets.md",
    "页面源码凭据线索与真实保密边界",
    "正文称敏感credential奖励并建议源码，图仅确认修复/奖金额打码。\n\n区分公开客户端标识、示例值、过期配置与真正服务端秘密，记录源码上下文、读者权限、权限/期限和最小无使用证明；公开ID、测试placeholder、奖励或修复邮件是反例。发现值只脱敏保留类型/hash/位置，不验证真实密钥或复制值。\n\n来源：[保存帖1](https://x.com/i/status/1445604622119235588)。"
  ],
  [
    "by-type/waf-bypass.md",
    "编码绕过卡的各层解释规则",
    "正文列case和percent，图片再列Unicode/HTML混合编码、注释、doubleencode、通配符、垃圾/换行及未初始化变量。\n\n按WAF解码/规则→应用参数→实际SQLHTMLshell等解释器记录每层字节和值，一次变化配合法基线和无害marker；后端不解码、大小写敏感、纯文本通配符、无shell变量或事件未触发是反例。混合编码只是候选，不称任何WAF通用绕过或所有内容语义等价。\n\n来源：[保存帖1](https://x.com/i/status/1445606175614009345)、[保存帖2](https://x.com/i/status/1445632561447768070)、[保存帖3](https://x.com/i/status/1445960842718027777)。"
  ],
  [
    "by-type/crlf-response-splitting.md",
    "注册XSS与CRLF头写入的独立消费者",
    "正文payload拼script和字面反斜杠r/n再SetCookie，没给原始响应头；AWSWAF卡混杂percent控制字节/事件/atob。\n\n分别记录rawbytes、URL/form解码、HTML属性/事件和真实HTTP头边界，使用无秘密marker验证；字面转义、仅HTML文本、200但无新增header或CSP阻止是反例。script反射不证明响应分割，SetCookie文本不证明服务器设置cookie，payload卡不证明AWS全部配置。\n\n来源：[保存帖1](https://x.com/i/status/1445646309399019523)、[保存帖2](https://x.com/i/status/1446104023170359302)。"
  ],
  [
    "by-type/authn-session.md",
    "改邮箱token的主体绑定与session假设",
    "正文自述自有账号改自有邮箱链接被受害者打开后改受害者邮箱，并归因token不绑session。\n\n绑定token内/存储中的account、待确认邮箱、动作、期限、一次性和当前登录identity，记录两自有账号前后权威邮箱/登录控制；链接只更新原账号、无登录会话也能安全完成或邮箱未可用于恢复是反例。token未绑浏览器session本身可正常设计，关键是不应让持有者会话替代token主体，未向别人发送链接。\n\n来源：[保存帖1](https://x.com/i/status/1445867416412557317)。"
  ],
  [
    "by-type/authn-session.md",
    "重置主体参数与返回token能力的拆分",
    "multipart图password/password2/id/action仅请求；另一正文改GETuseridreset取token并称cookieeditor登录，未给响应终态。\n\n分别核对重置授权/挑战、目标对象、重复口令校验和返回token的类型/受众/期限，再以两自有账户验证权威密码变化或会话主体；改id、确认字段不一致、预认证token、200或cookie编辑是反例。字段值不复制，未重置密码/用token登录。\n\n来源：[保存帖1](https://x.com/i/status/1445969662836043780)、[保存帖2](https://x.com/i/status/1446203097987129345)。"
  ],
  [
    "by-type/api-property-pollution.md",
    "邮箱验证码字段的JSON标量与数组类型",
    "图PUTmailverify把code标量换成多项数组，200响应含id/token，未保存最终verified状态。\n\n核对schema类型、服务端数组遍历/字符串化、challenge绑定、原正确/错误标量与小受控类型对照，分别记录每个值是否尝试及预算计费；200、预认证token、数组被拒或只采用一项是反例。候选数组不等一次穷举成功，不能从图补全部验证码可绕。\n\n来源：[保存帖1](https://x.com/i/status/1446027906640138248)。"
  ],
  [
    "by-type/authn-session.md",
    "HostURL生成与限流身份键分别验证",
    "正文把XFHostresetpoisoning、XFFloopback、null和case统称限流；reset图只见改Host请求。\n\n区分URL来源/反向代理信任链、限流key和账号规范化，记录自有重置邮件实际链接、挑战配额/拒绝状态和原身份；缺邮件、host反射、错误地址、稳定统一响应是反例。Host生成错误不自动是限流绕过，XFF不自动可信，本轮未发重置邮件/切换IP。\n\n来源：[保存帖1](https://x.com/i/status/1446152664572567564)、[保存帖2](https://x.com/i/status/1444880818594201610)。"
  ],
  [
    "by-type/xss.md",
    "cookie弹窗的脚本上下文与接管能力",
    "Huawei协作帖图片只有裁剪地址栏与cookie弹窗，没有输入/响应上下文。\n\n记录完整触发输入/响应、读者origin、浏览器/交互/CSP与自有跨读者marker，区分安全演示、自XSS、认证cookie与非认证WAFcookie；单个弹窗、缺source或cookie名称本身是反例。不能补会话接管或第三方平台登录能力，不复制cookie或联系协作对象。\n\n来源：[保存帖1](https://x.com/i/status/1446097299965362177)。"
  ],
  [
    "scope-and-rules.md",
    "平台邮箱别名与软件演示访问授权",
    "正文称用bugbounty平台邮件别名使厂商以为企业请求演示。\n\n按真实身份、软件当前测试政策和许可明确演示账户权限，限制到自己的授权环境；平台域别名、试用邀请或厂商误认不扩展资产/社会工程范围。未请求演示或对外传递身份信息，把此帖保留为范围反例。\n\n来源：[保存帖1](https://x.com/i/status/1446362981214818315)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "隐蔽通道生成文件与命令实际执行的区别",
    "CovertTube图运行generatevideo，输入命令并列出outputavi，未保存上传/接收端/执行收据。\n\n区分生成载荷媒体、获准传输渠道、接收解析和终端执行/身份，按文件hash与各阶段日志定位边界；提示符输入、输出视频存在或标题声称远程控制是反例。未生成/上传媒体或执行命令，不把通道包装视为入侵证明。\n\n来源：[保存帖1](https://x.com/i/status/1446448857496313858)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0111.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==108 and len(urls)>0
assert all(pid in ids for pid in urls)
assert len({title for _,title,_ in facets})==len(facets)
grouped=defaultdict(list)
for f,title,body in facets:
 p=T/'references'/f
 assert p.is_file() and ('## '+title) not in p.read_text(),(f,title)
 grouped[p].append('\n\n## '+title+'\n\n'+body+'\n')
community=T/'references/research/community-distillation.md'
marker='\n## 首轮提炼范围与未采纳内容\n'
c=community.read_text();assert c.count(marker)==1
routes=[]
for f,title,body in facets:
 summary=body.split('\n')[0].split('。')[0]+'。'
 assert '|' not in summary and '\n' not in summary
 routes.append(f'| {title} | {summary} | [方法条目](../{f}) |')
for p,parts in grouped.items():p.write_text(p.read_text()+''.join(parts))
community.write_text(c.replace(marker,'\n'+'\n'.join(routes)+'\n'+marker,1))
print('Added',len(facets),'facets and routes to',len(grouped),'topic files; all',len(urls),'source URLs batch-bound')
