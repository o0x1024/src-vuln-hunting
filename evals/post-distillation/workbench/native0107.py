"""Curated0107 facets. Own append helper; execute once after precheck."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "by-type/ssrf.md",
    "Gopher预制字节与数据库握手的协议条件",
    "SSRF提示图给MySQL Gopher示例但明确truncated，描述SHOW DATABASES而无实际响应。支持TCP或scheme与完成数据库协议不是同一能力。\n\n绑定获准消费者、scheme支持、实际编码/解码字节、连接/握手、认证和最终协议语义。截断示例、需要动态challenge、只见DNS/连接或数据库拒绝都是反例；不能以载荷生成工具补认证或命令结果，未连接数据库或运行Gopher数据。\n\n来源：[保存帖1](https://x.com/i/status/1421435484950208513)。"
  ],
  [
    "experiment-design.md",
    "人脸检测截图与隐私变换效果的评价",
    "Ruse宣传改变照片以阻识别，图片却是Original和FaceDetected，含landmark和概率。检测人脸、识别身份、人类可用性和处理后模型效果需要不同证据。\n\n固定受控原图/处理图、变换配置、模型任务/版本、同条件评价与人类可用性指标；记录失败和样本限制。仅原图被检测、工具UI或单一概率都不能补隐私保护成功，也不证明所有识别模型失效。\n\n来源：[保存帖1](https://x.com/i/status/1421459147401441282)。"
  ],
  [
    "by-type/mobile-android.md",
    "APK发布版本与签名及变体覆盖",
    "dapk图5页138 releases只显示四个版本下载行。镜像列表、组织名称和文件名不是全部官方有效制品或已完成下载的证明。\n\n关联包名、版本号/构建号、签名、ABI/渠道、原始来源时点及制品hash，保留分页终止、下载失败和重复变体。只有日志、缺hash或缺版本变体是反例；旧APK发现不授权安装和登录，也不推当前服务仍匹配旧客户端。\n\n来源：[保存帖1](https://x.com/i/status/1421462801357418505)。"
  ],
  [
    "discovery/web-and-api.md",
    "参数发现的heuristic与差异因子",
    "Arjun图一张v2beta列url/page/filter及httpcode/body因子，一张2.1显示8个heuristic名。正文把参数发现称端点发现，两个集合并不相同。\n\n绑定同一端点、身份与正常基线，记录参数名/类型、变更后的语义、重复对照、噪声及真实业务消费者。状态抖动、已知表单字段和只有heuristic输出是反例；工具候选不能算隐藏端点、字段被消费或安全影响已验证。\n\n来源：[保存帖1](https://x.com/i/status/1421476460276199427)。"
  ],
  [
    "by-type/idor-access-control.md",
    "用户集合与版本及单对象的公开字段合同",
    "v3/v4 users集合被拒，而编号对象返回id/name/username/Public_email。集合不可枚举不意味着每个公开profile必须拒绝，也不保证私有字段受限。\n\n建立版本/集合/对象/字段权限矩阵，固定受控身份、owner和公开性合同；分别确认查询访问权、返回属性与真正私有内容。合法公开资料、不同版本handler和统一错误是反例，不把顺序编号或字段名字自动算敏感数据泄露。\n\n来源：[保存帖1](https://x.com/i/status/1421517413527343107)。"
  ],
  [
    "by-type/idor-access-control.md",
    "移除数字路径段与斜线规范化的同对象条件",
    "原路径含数字段返回403，移除该段并用双斜线或反斜线后称200。输入同时改变对象标识和路径表示，未证相同保护对象。\n\n逐层关联原始wire、代理/框架规范化、租户/对象解析、授权检查和最终handler；比较同主体相同受保护数据或动作。换成集合、公开路由、登录页或其他vhost是反例，状态变化不能补认证绕过。\n\n来源：[保存帖1](https://x.com/i/status/1421748795298127874)、[保存帖2](https://x.com/i/status/1422677163384311813)、[保存帖3](https://x.com/i/status/1423830697236566017)、[保存帖4](https://x.com/i/status/1424599271035207682)。"
  ],
  [
    "scope-and-rules.md",
    "域名与范围IP交集的时点和共享租户",
    "建议大IP范围内找公司域名并取落在in-scope地址的交集。DNS对应关系、组织归属与当前可测试动作必须分别记录。\n\n保留当前范围版本、精确IP段/资产类型、解析时间与位置、SNI/Host及租户/共享服务关系；域名解析到范围内IP不自动授权所有vhost，范围外地址也不因品牌相同而可测。历史解析、CDN共享和域名转租是反例，不执行扫描。\n\n来源：[保存帖1](https://x.com/i/status/1421795566187651073)。"
  ],
  [
    "by-type/graphql.md",
    "mutation输入subValues与返回resolver的字段权限",
    "低权创建Value时加入subValues空数组，据称响应暴露管理员隐藏子值，卡片只写mutation且对象名遮挡。写入字段与返回resolver可能采用不同授权路径。\n\n绑定actor角色、父对象/子对象owner、输入schema、字段选择/服务端扩展及返回子字段的独立ACL；比较合法低权与受控管理身份的同对象结果。空数组被忽略、只返回自有项或允许公开子值是反例，不能以mutation标题补隐藏数据已泄露。\n\n来源：[保存帖1](https://x.com/i/status/1421813960043470852)。"
  ],
  [
    "by-type/xss.md",
    "InfluxDB查询错误到HTML提示的输出消费者",
    "InfluxDB UI1.0/Server1.0图包含查询语法错误、反射和alert，数据库语句未成功。错误文本进入网页与数据库执行是两个消费链。\n\n关联受控输入、服务端错误结构、前端实际DOM插入、编码/净化、origin及可触发的读者；同次正常错误作对照。只在自己查询页构造、文本展示或无跨主体传播是反例，alert截图不能补有效数据库查询、其他版本受影响或接管。\n\n来源：[保存帖1](https://x.com/i/status/1422107719167709186)。"
  ],
  [
    "by-type/xxe.md",
    "移动账户数据的编码外壳与XML实体读者",
    "交通App图从账户ChangeMyData入口到text/plain编码请求，响应text/html内呈XML与passwd行。历史MIME列、外层Content-Type和实际XMLresolver是不同层。\n\n绑定原始字节、外壳解码、内层XML解析器/配置、认证主体、实体读权限与最终响应。XML文本出现不自动证明外部实体被消费；passwd读取也不补SSH私钥或远程登录。遮挡完整请求时保留链条缺口，不运行实体或访问文件。\n\n来源：[保存帖1](https://x.com/i/status/1422200096414785537)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "代理替换JSON与末端扩展日志的原始收据",
    "MatchReplace图启用UA/Referer/body与escapedJSON载荷，另一帖要求Logger++置最后。变换后的合法请求与完整末端日志都不能由配置位置保证。\n\n分别保留原始请求、规则顺序/scope、转义后JSON/wire、发送者扩展、最终消费者和末端收据；记录被忽略、失败及未解密流。未勾规则、畸形JSON、插件未经过记录器或只有菜单是反例，回连须同次marker/时点，不复制借用域名。\n\n来源：[保存帖1](https://x.com/i/status/1422247377516122114)、[保存帖2](https://x.com/i/status/1422783223138902020)。"
  ],
  [
    "by-type/info-secrets.md",
    "历史SQL快照日历与实际内容暴露",
    "Google SQL候选后查询Wayback图为四次capture，日期2017至2021，没有显示SQL全文。删除原站文件不会自动使历史记录消失，日历也不保证可恢复内容。\n\n关联原始URL、capture时点、响应类型、保存字节与当前/历史公开性，区分目录、错误页与真正数据库内容。只有日历、旧模板和当前原站拒绝都是反例；不能推当前站点仍可读或整库泄露，未拉取外链内容或使用其中秘密。\n\n来源：[保存帖1](https://x.com/i/status/1422309387914387459)。"
  ],
  [
    "by-type/info-secrets.md",
    "仓库关键词与提供者标记的活跃配置证据",
    "Git-Secret图选master并检查README/apikeys等，输出Google/AWS标记。匹配字符串只是候选，提供者名称和文件名不保证值的格式、私密性或权限。\n\n绑定commit/branch、原始字段位置、真实运行配置、允许公开的客户端key限制和撤销状态；示例、错误标记、过期值和不被消费是反例。Sentry info或YouTube调用会真实使用凭证，须另有明确允许范围；本轮只提炼，不复制或验证key。\n\n来源：[保存帖1](https://x.com/i/status/1422543085213388806)、[保存帖2](https://x.com/i/status/1423802814426451974)、[保存帖3](https://x.com/i/status/1424152205645520898)、[保存帖4](https://x.com/i/status/1424933036089479168)。"
  ],
  [
    "source-audit.md",
    "HTTPS代理hook定义与插件注册及实际wire",
    "Proxverter图定义request hook并启动127.0.0.1:8081 HTTPS，未展示插件注册或客户端链路。定义方法、启动监听和请求实际被修改是独立阶段。\n\n核对插件实例/注册、代理选择、CA/解密、请求路由、变换前后收据和服务端最终消费；保留失败和未经过代理的流。仅类定义、is_https参数或启动日志是反例，不能凭十行代码说全部浏览器流已拦截，源脚本未运行。\n\n来源：[保存帖1](https://x.com/i/status/1422585731332153346)。"
  ],
  [
    "by-type/info-secrets.md",
    "研究服务器目录索引与历史命令的秘密层级",
    "WEBrick索引图列bash_history/.ssh、工具目录和大小，历史命令截图含扫描/删除等文本。索引可见、文件可读和当前凭证可用不相互替代。\n\n绑定获准资产、身份、索引与实际文件公开合同、同次响应内容/制品hash及当前配置；文件名、历史命令和过期路径是反例。不得重放历史、下载真实凭证或推合法目标服务器可测，研究者服务器的标签也不授权访问。\n\n来源：[保存帖1](https://x.com/i/status/1422615931344261127)、[保存帖2](https://x.com/i/status/1424980012243976193)。"
  ],
  [
    "by-type/info-secrets.md",
    "LAPS的LDAP认证主体与密码读取ACL",
    "SharpLAPS图给认证参数并显示masked密码输出。LDAP已认证读取可能是正常管理权限，工具标题不证明任意低权或未认证可获取。\n\n关联获准机器对象、actor/groups、属性读取ACL、凭证轮换和允许证明的最终能力；比较受控合法管理与低权对象权限。仅received output、合法ACL或值已失效是反例，截图秘密不复制或用于登录，提取能力与远程执行权分别记录。\n\n来源：[保存帖1](https://x.com/i/status/1422923944361857031)。"
  ],
  [
    "by-type/authn-session.md",
    "认证状态机的挑战输入输出与合法转移",
    "Raider介绍将每步视作state，带Cookie/header/CSRF输入输出。它可帮助组织认证实验，但框架存在不证明路径完整或安全缺陷。\n\n按受控actor、状态、挑战用途/目标/期限、凭据来源和最终权限画转移；保存失败、回退、重用和退出后的状态。客户端界面越过步骤而权威动作被拒、陈旧challenge或跨主体错配是反例；缺实际收据不能补接管或全流程验证。\n\n来源：[保存帖1](https://x.com/i/status/1422935355108597762)。"
  ],
  [
    "by-type/xss.md",
    "联系表单延迟后台消费的时间和读者身份",
    "叙述联系表单两日后后台触发BXSS且截图含支持数据。输入保存、队列、后台读者渲染和回连是独立阶段，延迟不能由提交响应解释。\n\n关联受控marker、提交时点、任务/记录ID、消费端origin/角色和同次回连；外部预览机器人、重复消费或无输入关联是反例。截图没有保存时不补真实用户数据读取，采用合成材料与最小证据，不投递外部脚本或联系支持人员。\n\n来源：[保存帖1](https://x.com/i/status/1422890880722079749)。"
  ],
  [
    "by-type/business-logic.md",
    "支付确认重放与单次交付账本",
    "图片描述数字商品一次支付后重放确认请求可多次获得产品，奖卡称无限。已付款状态和每个合法交付权仍需幂等合同。\n\n绑定受控交易/订单ID、实际已付金额、交付次数/对象、确认的单次消费和权威账本；区分重复下载同一已购制品与额外新权益。客户端重复展示、幂等返回旧结果或测试模拟是反例，不能由P1标题补无限真实获利，不开展支付。\n\n来源：[保存帖1](https://x.com/i/status/1422974475360899077)。"
  ],
  [
    "by-type/ssrf.md",
    "RSS订阅保存与后台feed获取的回连归因",
    "正文只说profile关联RSS feed并发现盲SSRF，卡片称内网发现。订阅保存与定时获取、重定向和解析各有消费者。\n\n关联受控URL/marker、保存记录、fetch时点、发起身份、逐跳scheme/目标及实际协议响应；只见合法RSS获取、DNS或外部验证器是反例。没有获准内网协议收据时不能补内部主机可达或数据读取，未创建订阅或扫描服务。\n\n来源：[保存帖1](https://x.com/i/status/1422994795887153159)、[保存帖2](https://x.com/i/status/1424989978333876228)。"
  ],
  [
    "by-type/authn-session.md",
    "多个登录注册入口的同身份策略矩阵",
    "dork图列login/signup/dashboard等，称各入口保护可能不同。搜索结果只是观察入口，并不证明某处弱保护或当前可用。\n\n逐入口保存资产/版本、同一受控actor、挑战/session、恢复/注册状态及最终业务权限；区分旧入口、不同应用、公开页面和统一认证跳转。相同策略或接口只返回说明是反例；命中数量不计流程验证，旧平台总量/比例不补当前许可。\n\n来源：[保存帖1](https://x.com/i/status/1423006099850944515)、[保存帖2](https://x.com/i/status/1423494048032051207)。"
  ],
  [
    "source-audit.md",
    "API hash解析名称与动态调用的分层",
    "IDA图显示hash映射LoadLibrary、VirtualAlloc和WinHttp函数，API Monitor图却No process monitored。静态识别、函数实际调用与监控覆盖都须独立证明。\n\n绑定获准制品hash/架构、地址、真实引用、加载模块和同次运行/监控附着收据；空表、未选进程和只有名称注释是反例。不能把静态名匹配当已执行，也不能把无数据称无监控syscall或unhook成功，未运行二进制。\n\n来源：[保存帖1](https://x.com/i/status/1423044715612676100)、[保存帖2](https://x.com/i/status/1425083137495810057)。"
  ],
  [
    "by-type/file-upload.md",
    "jpeg.php声明与保存位置及解释器消费",
    "上传图filename为jpeg.php且MIME image/jpeg，另一图UI只列两个SVG名。客户端声明、服务端保存名和真正解释/渲染行为分开。\n\n关联受控制品hash、内容检测、允许扩展、保存路径/重命名、返回MIME/Disposition、读者及解释器映射。仅表单提交、改扩展名或普通下载是反例，SVG条目不补PHP执行。未见执行响应时不能接受RCE标题，Cookie/token不复制或使用。\n\n来源：[保存帖1](https://x.com/i/status/1423163595701977088)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "单字符端点模式与ID关键词的候选限制",
    "提取端点的regex在slash后字符类没有重复量词，不能覆盖多字符路径；另例默认grep查id模式，被称最简单IDOR。文本模式与权限验证不同。\n\n保存实际regex引擎/转义、输入文件来源和匹配跨度，区分原始URL、AST/字符串、动态拼接、空值及查询字段。绝对/转义/多字符路径漏失、误匹配字母或仅出现id都是反例，候选文件不能计全部端点或越权成功，源one-liner未执行。\n\n来源：[保存帖1](https://x.com/i/status/1423349860296757254)、[保存帖2](https://x.com/i/status/1423371847417044994)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "历史JS子串过滤与当前源码集合",
    "gau图按.js子串过滤并排除.jsp/.json，使用追加输出；JS列表不证明当前响应是JavaScript。过滤器也可能漏掉无扩展模块或把查询参数当扩展。\n\n关联原始来源URL/时点、完整路径与query、Content-Type/真实字节、脚本版本及累计/去重规则；记录不可达、错误页、重复和source map。只有历史URL或奖卡是反例，静态参数候选须真实XHR/handler消费，不推所有JS已审计。\n\n来源：[保存帖1](https://x.com/i/status/1423621665443958786)、[保存帖2](https://x.com/i/status/1423021016037658630)、[保存帖3](https://x.com/i/status/1424743051432501249)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "来源开关与队列inactive的结果完整性",
    "Sigurlfind3R help列include/exclude/use/list sources，WARCannon图DeployYES但JobINACTIVE和0Messages。配置存在、任务已部署和结果处理完成不同。\n\n逐源保存有效开关、输入schema、取回时点、解析失败、去重键与最终集合hash；队列还需任务ID、终态、失败/取消及所有产物完成。来源未消费、旧缓存或仅inactive都不能补全量扫描，图中文字遮挡时保留范围，不运行工具。\n\n来源：[保存帖1](https://x.com/i/status/1424720945458159616)、[保存帖2](https://x.com/i/status/1423634660995878918)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "证书issuer字段与id查询的标识合同",
    "crt.sh图取JSON issuer_ca_id后接id查询并grep SHA1。字段名字表示的对象与目标查询消费者期待的标识类型需要显式对应，不能凭都是整数互换。\n\n保留原始schema、记录/issuer标识、查询参数、响应对象和证书指纹算法/编码；确认关联映射后再去重。缺实际响应、取错对象、匹配页面普通40位字符串或丢失败都是反例，不计证书全集、资产所有权或TLS实际部署。\n\n来源：[保存帖1](https://x.com/i/status/1424339601804599304)。"
  ],
  [
    "by-type/info-secrets.md",
    "PDF打印页脚URL标识与能力传播",
    "打印PDF页脚显示Booking对象路径，正文把GUID或token统一视作危险。对象标识公开性与可直接授予权限的bearer能力不能合并。\n\n关联生成/打印/分享消费者、实际URL字段、认证绑定、用途/有效期、允许读者及最终受保护动作；观察合成文档的传播范围。无权访问的普通GUID、公开引用和失效能力是反例，仅页脚不能补当前可访问内容，实际标识和个人信息不复制。\n\n来源：[保存帖1](https://x.com/i/status/1424266026993164296)。"
  ],
  [
    "by-type/authn-session.md",
    "PHP非严格比较的操作数与版本边界",
    "缺严格比较提示需核实真实类型。按[PHP比较文档](https://www.php.net/manual/en/language.operators.comparison.php)，数字字符串比较与类型一致比较不同，PHP8也改变数字和非数字串的旧行为。\n\n绑定运行版本、请求解码/schema、两个实际操作数类型、比较器与最终身份/权限条件；不能把旧0对任意串的结果推广所有版本。严格类型检查、有效数值域、未消费字段或认证动作仍拒绝是反例，未运行PHP载荷或以报错代接管。\n\n来源：[保存帖1](https://x.com/i/status/1424371583515246593)。"
  ],
  [
    "by-type/xss.md",
    "cookieless会话路径到输出属性的消费链",
    "ASP.NET图A路径含引号/事件样文本并有alert1，另图只列ArchivedMedium报告。路径中的会话表示和网页输出sink需分别确认。\n\n关联准确框架/配置、路径会话规范化、实际返回链接/form/属性、编码及读者origin，保存同次受控正常对照。普通URL文本、session不被采用或输出被编码是反例；无响应HTML时不能确定是哪一sink，更不能推当前所有ASP.NET均受影响。\n\n来源：[保存帖1](https://x.com/i/status/1424646323714760709)、[保存帖2](https://x.com/i/status/1425076663398842389)。"
  ],
  [
    "discovery/passive-and-services.md",
    "域名JSON提取与重复DNS行的观察身份",
    "Anubis regex列表末尾带大括号，sonarbyte图重复api/根域/www，RapidDNS主页给大总量。三个数字分母不是同一个集合。\n\n按真实JSONschema/完整域名、后缀边界、来源版本/时点、原始行和唯一记录区分解析与归属；记录转租、失败和历史观测。正则碎片、重复行和库总量是反例，不能补目标当前解析或范围许可，也不执行其网络管道。\n\n来源：[保存帖1](https://x.com/i/status/1424814695530237958)、[保存帖2](https://x.com/i/status/1425062109495369786)、[保存帖3](https://x.com/i/status/1424240264391036930)。"
  ],
  [
    "by-type/xss.md",
    "JS字符串转义与实体URI的解析顺序",
    "productId单引号示例用编码空白换行及find(alert)，embed和formaction示例使用HTML实体。JS语法、HTML属性与URI解析是不同消费者。\n\n保存原始输入、URL解码、输出位置、HTML实体后值、URI处理及最终JS语法；formaction还涉及真实激活行为。无点击、标签当文本、不受支持scheme或语法错都是反例；不能以变换后看似javascript和Dup叙述推WAF绕过，不执行示例。\n\n来源：[保存帖1](https://x.com/i/status/1422702544195837964)、[保存帖2](https://x.com/i/status/1423148542126739464)、[保存帖3](https://x.com/i/status/1424070599505108993)。"
  ],
  [
    "by-type/xss.md",
    "Base64文本与eval消费者的语法有效性",
    "SVG/eval/atob片段被称绕过，但只读解码其字节为XSS haxor，没有可用JS表达式。文本能解码与eval成功求值不同。\n\n逐层绑定过滤、HTML闭标签、SVG实际事件、Base64字节、JS解析和CSP；字符/标签被删、编码被改变、仅文本展示或语法无效是反例。不得静默换载荷再称原文成功，code闭标签是否必要只能由完整输出状态判断；本轮只解码未执行。\n\n来源：[保存帖1](https://x.com/i/status/1424727426014265350)、[保存帖2](https://x.com/i/status/1423578366918025229)、[保存帖3](https://x.com/i/status/1422935296874893318)。"
  ],
  [
    "by-type/idor-access-control.md",
    "HTTP方法矩阵的同资源与最终权限",
    "legacy图GET/HEAD403、POST/OPTIONS200，其他方法405/501/400。High报告标题又称SQLi，矩阵本身没有受保护返回内容或查询消费者。\n\n固定actor、host、路径、body schema、对象及实际handler，区分方法可用、preflight、错误与真正权限动作。普通OPTIONS、登录页、业务拒绝和新公开路由是反例，200不补越权，405也不证明所有变体安全；SQLi链要独立证据。\n\n来源：[保存帖1](https://x.com/i/status/1425708957750923264)。"
  ],
  [
    "by-type/authn-session.md",
    "银行响应RC与PIN的权威后端状态",
    "两图分别RC0109 BLOCKED和RC0102成功并提示建立PIN。代理改响应可改变UI，不能直接改变服务器已登记的认证状态。\n\n关联受控账户/设备、OTP/激活挑战、前端分支、真实后端PIN设置与最终受保护身份；保存正常成功/拒绝对照。仅界面开放、后续动作仍校验、状态未变或已有会话是反例，不能以成功消息推接管，未登录银行或修改PIN。\n\n来源：[保存帖1](https://x.com/i/status/1425727143569346564)。"
  ],
  [
    "source-audit.md",
    "Nexus3.14版本边界与读取和执行能力",
    "帖称小于3.14.0，但图Server3.14.0-04。按[Sonatype公告](https://community.sonatype.com/t/botnet-exploitation-of-nxrm-up-to-3-14-0/1993)，CVE2019-7238受影响3.x包含3.14.0，3.15.0修复，2.x不在该影响范围。\n\n对应准确制品/版本、配置、认证主体、完整extdirect请求和实际消费者；图请求裁切而passwd文本不自动证明Java代码执行。版本banner、模板命中和人口地域计数都不補当前实例成功或许可，旧标题边界不能代产品公告，未调用服务。\n\n来源：[保存帖1](https://x.com/i/status/1425799315184775173)。"
  ],
  [
    "source-audit.md",
    "ProxyShell模板命中与RCE链的独立验证",
    "Nuclei2.2.0图一规则标CVE34473/critical并列多个URL，未给matcher或有效载荷结果。扫描器名称和critical标签不是最终执行能力。\n\n关联获准产品版本/配置、模板hash、请求与匹配字段、正常/失败对照及每段实际能力；候选route可达与最终代码执行分别证。统一响应、误匹配、旧cache或仅命中URL是反例，不统计为多条已确认RCE，也不运行源扫描器。\n\n来源：[保存帖1](https://x.com/i/status/1425114660374724615)。"
  ],
  [
    "by-type/mobile-ios.md",
    "同一消息在Web与iOS WebView的渲染差异",
    "正文称消息过滤后Web未触发，却在iOS App WebView触发。存储字段相同不保证所有客户端使用相同净化、HTML解析和权限环境。\n\n关联受控消息ID/原始与保存字节、各读者的版本、模板/sink、origin、脚本开关和native bridge能力；比较同份输入。不同消息、普通文本、仅打开UI或无原始链条是反例；脚本触发不自动等于native权限、任意文件或接管，未操作设备。\n\n来源：[保存帖1](https://x.com/i/status/1425674198605721606)。"
  ],
  [
    "by-type/idor-access-control.md",
    "profile图片UUID与聊天内容对象权限",
    "聊天机器人帖从profile图片UUID改用户聊天请求而称管理员聊天披露，卡片无内容。UUID的不可猜性和内容读权限是不同保护。\n\n用受控admin/user生成独立聊天，记录认证主体、owner/tenant、对象参数、返回内容及缓存身份；图片标识只作候选来源。公开对话、共享授权、错误或相同已授权聊天是反例，标识泄露不自动授予私有聊天读权，也不发真实消息。\n\n来源：[保存帖1](https://x.com/i/status/1425839304983465995)。"
  ],
  [
    "by-type/idor-access-control.md",
    "游戏双会话与评论删除的关系权限",
    "游戏建议两个自有账号隔离会话交换user/object参数；评论图六步叙述公开comment ID后可删除。对象标识来源与动词授权分别判断。\n\n按受控actor、owner、共享关系、资源状态和具体读/写/删除/设置动作建立矩阵；合成评论须能恢复并核对权威最终状态。合法自有操作、不同对象或仅正文宣称是反例，不由一个例子推所有评论可删，不对真实用户执行动作。\n\n来源：[保存帖1](https://x.com/i/status/1425013591485341700)、[保存帖2](https://x.com/i/status/1425422853214662665)、[保存帖3](https://x.com/i/status/1425426934989606913)。"
  ],
  [
    "by-type/xss.md",
    "TinyXSS长度与浏览器和能力条件矩阵",
    "TinyXSS图列15样例与script/style/eval/frames、name/URL控制、innerHTML及浏览器标签。字符长度只在对应条件成立时有意义。\n\n先确定实际source/sink、攻击者可控name/URL/子frame、CSP能力、渲染方式和真实引擎/版本，再判断候选语法和最终效果。缺控制源、CSP拒绝、脚本未走解析分支或不同浏览器是反例；菜单全选不表明目标同时有全部能力，未点击PoC。\n\n来源：[保存帖1](https://x.com/i/status/1426038293586530304)。"
  ],
  [
    "by-type/xss.md",
    "Ghost授权CodeInjection与支持聊天注入的边界",
    "LiveChat HTML注入标题配Ghost CodeInjection设置图，说明主题header/footer用于插入代码。正常发布权限与低权聊天输入进入后台sink不是同一机制。\n\n绑定actor角色、实际产品/模块、允许发布范围、受控输入字段及最终读者；比较合法管理能力与未经授权的输入消费。只有管理员设置页、空编辑框或标题错配是反例，功能名CodeInjection不能直接当漏洞或后台BXSS。\n\n来源：[保存帖1](https://x.com/i/status/1426106700507992065)。"
  ],
  [
    "by-type/open-redirect.md",
    "DOM导航与文档解析及XHR的不同sink",
    "所谓15个DOM重定向参数混location属性、assign/replace/open、srcdoc、Ajax和XHR。属性读取、导航、文档解析和网络请求并不等价。\n\n标记实际读/写方向、输入来源、URL解析/allowlist、真实导航目的地与文档origin；XHR open/send还需区分方法和请求体消费。只读location、正常API请求、非导航srcdoc或输入未控是反例，API名列表不证明开放重定向，更不补XSS或接管。\n\n来源：[保存帖1](https://x.com/i/status/1426137788999553040)。"
  ],
  [
    "source-audit.md",
    "Karton产物hash与静态动态任务的队列合同",
    "Karton图区分producer/classifier/unpacker、动态dump、静态配置、报告消费者。箭头说明架构，不给本次样本或分析执行结果。\n\n以获准制品hash关联父子产物、路由条件、沙箱环境、任务终态/失败与报告内容；静态特征、解压和真实执行权限分开。只见架构、0消息、未选进程或生成help是反例，不能补恶意样本已运行或所有分支完成；源程序未执行。\n\n来源：[保存帖1](https://x.com/i/status/1425219038909771787)、[保存帖2](https://x.com/i/status/1425807971456634882)、[保存帖3](https://x.com/i/status/1425581755654868996)。"
  ],
  [
    "by-type/ssrf.md",
    "Digest降Basic的challenge与凭证作用域",
    "正文称SSRF诱导Digest降Basic泄漏API凭证。[RFC7617](https://www.rfc-editor.org/rfc/rfc7617.html)说明Basic把用户密码对Base64编码，不提供加密；它不保证任意客户端会接受降级。\n\n关联获准fetch客户端、配置的scheme、challenge/realm、origin/重定向凭证范围和真实发送头；只发401、Digest-only配置或不向变化来源带凭证是反例。协议格式与服务端实际泄漏分开，使用合成凭证才可设计获准验证，本轮未发请求或收集密码。\n\n来源：[保存帖1](https://x.com/i/status/1425193884309725184)。"
  ],
  [
    "by-type/authn-session.md",
    "组织成员信息与员工email字段的恢复能力",
    "邀请用户进入组织后可见信息被称IDOR，经理员工接管标题图却仅email输入/返回不同。成员资料可见、email变更与恢复/最终员工身份是不同能力。\n\n绑定管理者职责、目标受控员工/tenant、本人接受/同意、资料公开合同、权威email字段、challenge用途与最终身份。合法成员资料、忽略输入、只改变显示字段或恢复仍绑定本人是反例；缺完整接受/恢复收据不补无交互接管，未发邀请或改邮箱。\n\n来源：[保存帖1](https://x.com/i/status/1425669830556803081)、[保存帖2](https://x.com/i/status/1426163564595789828)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0107.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==73 and len(urls)>0
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

