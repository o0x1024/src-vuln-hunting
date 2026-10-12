"""Append manually distilled0110 facets after precheck. Own helper only."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "by-type/xss.md",
    "反射扫描HTML标签分类与浏览器执行证据",
    "Reflector2.5图列POST200、Reflected Yes、script HTML tag、Vulnerable Yes或Maybe，并显示两个奖励条目。\n\n保存原请求/字段、响应反射字节和上下文、完整DOM、读者origin、浏览器/CSP及实际受控marker执行；字符串匹配、统一200、工具标签、奖励或未触发事件是反例。测试完成日志只说明工具终态，不能把反射和脚本执行合成一项。\n\n来源：[保存帖1](https://x.com/i/status/1436284358671970306)、[保存帖2](https://x.com/i/status/1437364056927653889)。"
  ],
  [
    "discovery/passive-and-services.md",
    "域枚举帮助函数与具体对象查询产物",
    "EDD帮助列function、domain、computer/group/process/user、share/search、输出和threads5，help后打印done。\n\n绑定获准目录/共享、调用身份、函数及对象类型、实际请求和产物hash，记录访问拒绝/部分结果；help done、通配符、输出路径或线程选项是反例。帮助终态不是目标枚举完成，未执行目录查询或读取共享文件。\n\n来源：[保存帖1](https://x.com/i/status/1436302132186165256)。"
  ],
  [
    "source-audit.md",
    "路径反斜杠触发PCRE构造错误的定位",
    "两图URL包含反斜杠，分别出现PCRE不支持escape及No ending delimiter错误，未保存实现。\n\n对照原字节、URL解析、路由和regex构造/转义及错误传播，区分输入被当模式还是被匹配文本；只是格式拒绝、稳定错误页、无秘密或未知消费者是反例。编译异常支持审计regex边界，不能直接补RCE、任意文件或权限突破。\n\n来源：[保存帖1](https://x.com/i/status/1436370887155109892)。"
  ],
  [
    "by-type/crlf-response-splitting.md",
    "百分号hex大小写和实际换行消费者",
    "正文建议百分号0A改0a避403；没有真实响应分隔结果。RFC规定百分号hex大小写等价于同一八位值。\n\n分别保存raw input、WAF字符串规则、解码顺序、实际响应/邮件header字节及受控真假对照；大小写状态不同但都未进header、统一错误页或文本转义是反例。规范字节等价不保证各实现过滤等价，依据：[RFC3986百分号编码](https://www.rfc-editor.org/rfc/rfc3986.html#section-2.1)。\n\n来源：[保存帖1](https://x.com/i/status/1436328175324258308)。"
  ],
  [
    "discovery/web-and-api.md",
    "递归页面搜索中的匹配层和链接范围",
    "WWWGrep帮助可按literal/regex、case、header、HTML、JS、text/comments搜索，并区分root或any链接递归，另有代理/auth与separator。\n\n按获准域/路径、响应类别、具体消费者、原页面与抽取URL保持来源，设置递归深度/请求预算并留阶段计数；跨域any、隐藏字段但未消费、自定义分隔器破坏格式、登录内容或仅help是反例。所有匹配不计所有API/秘密。\n\n来源：[保存帖1](https://x.com/i/status/1436438018617974785)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "API Gateway域发现与端点认证合同",
    "正文把execute-api通配域搜索后fuzz称No auth required；没有具体route/stage或私有对象结果。\n\n绑定书面范围、API/stage/route、方法、无会话/低权限/owner身份及实际业务动作；公开预期端点、默认错误、前端shell、路由需auth或无对象内容是反例。域名格式不决定无认证，也不授权批量扫描或跨program探测。\n\n来源：[保存帖1](https://x.com/i/status/1436617773732540417)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "WindowsADS候选的文件流与目录消费者",
    "两张不同尺寸卡列ASP文件::$DATA与admin目录$INDEX_ALLOCATION，未保存响应。\n\n先确认OS/filesystem、web handler、原始与规范化路径、授权检查和最终stream/目录消费，区分源码读取与认证路径绕过；非NTFS、colon拒绝、规范化一致、解释器正常执行或只卡片是反例。候选示例不说明所有Windows版本支持漏洞，未发请求。\n\n来源：[保存帖1](https://x.com/i/status/1436655772058927106)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "搜索工具版本更换后的输入输出合同",
    "pagodo2.0图改搜索库、字典返回、原生HTTP/SOCKS、min/max等待和固定all_dorks文件，移除旧依赖/UA禁用。\n\n固定版本和查询资源hash，保存实际查询/返回字典schema、代理归属、预算和失败，核对旧脚本是否仍消费正确结构；旧命令、固定文件被覆盖、空结果、广告版本或无运行收据是反例。changelog不是当前全索引或成功检索证明。\n\n来源：[保存帖1](https://x.com/i/status/1436748081601519621)。"
  ],
  [
    "by-type/authn-session.md",
    "路径大小写分号与限流键的规范化一致性",
    "正文称加分号只在Java可绕限流，并建议端点大小写变化避forbidden。\n\n逐层记录edge/router/framework/filesystem实际路径和authorization/计数键，固定同身份同逻辑动作/时间窗作最小对照；路由不等价、规范化一致、静态公共页、仍拒绝或仅状态变化是反例。不能把实现限定推广所有Java或认为非Java不可能，路径字面差异不是自动权限突破。\n\n来源：[保存帖1](https://x.com/i/status/1436949934872408068)、[保存帖2](https://x.com/i/status/1437283763822620677)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Grafana错误页返首页与后端权限分离",
    "正文叙述403目标某JS路径为Grafana404，点home后正常，无保存会话/私有API数据。\n\n固定浏览器cookie、主机/路径、redirect链、用户及真实dashboard/API对象权限；前端shell加载、登录页、cookie刷新、公共home或未读私有内容是反例。UI状态改变不等于后台403授权绕过，发现组件和读写权分别记录。\n\n来源：[保存帖1](https://x.com/i/status/1436960656985624581)。"
  ],
  [
    "by-type/authn-session.md",
    "历史默认帐号表与部署身份的独立确认",
    "正文列多个产品默认帐号密码，无实际目标/版本/登录收据。\n\n从获准部署文档/配置核对初始化流程、版本、已更改/禁用状态、实际认证模式和允许的低副作用动作；历史版本、SSO、改密、部署未开放或仅列表是反例。列表不证明当前密码有效/资产易入，值不转录也不用于尝试登录。\n\n来源：[保存帖1](https://x.com/i/status/1437259562738806790)。"
  ],
  [
    "business-modeling.md",
    "官方功能教程到业务假设的版本对应",
    "正文建议成熟公司教程发现未用功能；另一图反思盲改请求转为理解资产连接。\n\n保存文档/产品版本、实际可达入口、对象生命周期、角色、后续消费者和单变量假设，设预算/反例/停止条件；已弃功能、教程不适用、无授权或只随机改值是反例。功能发现不保证无人测试、高收益或有漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1437313571898028036)、[保存帖2](https://x.com/i/status/1438125679795658760)。"
  ],
  [
    "by-type/authn-session.md",
    "Flashcall返回映射与恢复终态的同一挑战",
    "Facebook图请求should_use_flash_call及cli字段，回包出现code_length和flash_call_cli_filter_map，缺新密码或最终会话。\n\n绑定调用者、目标owner、phone/cli的数据类型、challenge发行/时效/用途、filter结果和最终兑换；参数可控、返回success、普通映射、OTP仍要求或没有password/session终态是反例。静态图不补暴力枚举/ATO，未发送OTP/恢复或使用图中身份材料。\n\n来源：[保存帖1](https://x.com/i/status/1437683860750229509)。"
  ],
  [
    "source-audit.md",
    "票据输出与ACL修改和权限恢复的区别",
    "targetedKerberoast终端显示认证上下文和长票据样式串，微小字段没有可靠全读；缺ACL修改/恢复日志。\n\n分别记录获准测试身份、真实目录ACL/对象、修改前后、票据来源、恢复验证与具体权限消费者；仅ticket文本、help、同权限正常取票或无ACL变化是反例。票据不等于破解/提权，未转录或使用hash，不运行来源工具。\n\n来源：[保存帖1](https://x.com/i/status/1437751601851158538)。"
  ],
  [
    "by-type/xss.md",
    "挑战规则的读者域和浏览器矩阵",
    "0921页面规则指定该域、Chrome/Firefox、域对话框、非selfXSS/MITM和时间范围。\n\n将限定域、产品/浏览器版本、读者触发方式、执行origin和实验终态逐项绑定；别的域、自操作控制台、仅支持浏览器选择、MITM或无受控marker是反例。截图中的历史活动规则不提供今天测试真实网站的授权，未打开挑战或执行payload。\n\n来源：[保存帖1](https://x.com/i/status/1437789926951727111)、[保存帖2](https://x.com/i/status/1441271859245305856)。"
  ],
  [
    "by-type/mobile-android.md",
    "反编译HTTP注解与动态路由和真实请求",
    "jadx grep图列GET/POST注解、路径变量和动态{url}，方法名涉及app/store；正文只按Java文件搜注解。\n\n保留APKhash/版本、完整baseURL/环境、注解库、callsite、字符串构造和实际请求，合并静态/动态入口；混淆遗漏、native网络、运行时URL、未调用方法或别的版本是反例。grep能给候选，不提供全部API/认证行为，未反编译或运行来源APK。\n\n来源：[保存帖1](https://x.com/i/status/1437829983674712074)。"
  ],
  [
    "by-type/idor-access-control.md",
    "成员移除与旧编辑添加动作的撤销边界",
    "正文叙述admin移除成员后旧请求仍编辑/新增文件；奖邮件标题却为removed customers add reports on data_requests。\n\n固定两自有角色、成员版本、会话/token、具体object/action和撤销时间，验证允许的最小状态；files与reports对象错配、独立分享仍有效、合法异步过渡、仅奖励或无最终对象是反例。一次成功不证明forever，权限撤销与重新认证独立核对。\n\n来源：[保存帖1](https://x.com/i/status/1437978659449495552)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "fileURL问号解码与shell文字的不同解释器",
    "保存多帖候选含问号、百分号双编码、变量和命令替换样式，未给consumer或结果。\n\n记录raw target、URL path/query、解码次数、wrapper/path消费和过滤顺序；若输入只作为字符串，shell语法不自动展开。URL被拒、问号作为查询而未到文件名、无shell消费者或没有读回内容是反例。不把候选当通用WAF绕过，不执行替换/文件请求。\n\n来源：[保存帖1](https://x.com/i/status/1438050683085754369)、[保存帖2](https://x.com/i/status/1438186469496180743)、[保存帖3](https://x.com/i/status/1438453932108304395)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Jira功能路径dork与实际CVE条件",
    "正文用ContactAdministrators路径dork称RCE，未保存版本、配置、输入或执行结果。\n\n把功能可达、产品版本/补丁、受影响配置、认证主体、具体触发和独立最小终态分层；旧索引、同路径修补、正常form或仅CVE名是反例。dork只发现候选，不补当前可利用实例，未搜索/提交真实页面。\n\n来源：[保存帖1](https://x.com/i/status/1438057998199316483)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "ASN和归档URL模板的执行与范围输入",
    "模板商店图列ASN network/subdomain、archiveURLs、JS credentials、redirect、port/S3/fuzz等动作卡。\n\n固定获准范围和每模板动作权限、工具版本、输入schema、预算、产物/失败/终态，按主动与被动工作分类；ASN关联不等所有owner、公开URL不等scope、模板名字或开始日志是反例。模板可用不代表运行成功，不从卡片授权扩大目标或批量扫描。\n\n来源：[保存帖1](https://x.com/i/status/1438123379085692931)、[保存帖2](https://x.com/i/status/1438985281697374211)。"
  ],
  [
    "by-type/xss.md",
    "事件属性中的脚本加载与分类标签错配",
    "正文onfocus接jQuery.ajax dataType script；图Search输入却分类Stored，triaged high但无执行/持久化截图。\n\n区分反射/持久存储、真实HTML属性/JS解析、jQuery及版本、event触发、CSP/外部加载和读者origin；$不存在、只输入被接受、库未加载、外部脚本被阻止或无其他读者是反例。分类和奖金不证明Stored或特定WAF普适绕过，未加载远程脚本。\n\n来源：[保存帖1](https://x.com/i/status/1438202622041755648)。"
  ],
  [
    "by-type/business-logic.md",
    "支付回调页与账单结算交付的一致性",
    "图建议取Success/Referer/Callback里payment/hash URL重新打开，称支付成功，没有backend账单证据。\n\n使用授权沙箱将订单owner/金额/币种/版本、provider签名及事件id、服务器核验、状态迁移和交付绑定；仅thankyou页、合法pending、重复事件幂等、backend未paid或未交付是反例。页面成功不能认免费权益，未创建真实订单、付款或回调。\n\n来源：[保存帖1](https://x.com/i/status/1438326025230839811)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "FirebaseURL和HTML数据库字样的公开配置边界",
    "一帖Wappalyzer/source找到Firebase db URL；另一MongoDB pass放HTML文字无实际字段图。\n\n区分公开项目标识与真实secret/私有数据，绑定owner、规则/认证、read/write动作、字段用途/时效和最小脱敏证据；公开SDK配置、只有URL、合成字串、访问拒绝或缺真实consumer是反例。名称不证明有效数据库身份，未访问数据或使用秘密。\n\n来源：[保存帖1](https://x.com/i/status/1438355065518002180)、[保存帖2](https://x.com/i/status/1438767689183502342)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "多源枚举退出成功与缺失模块的实际覆盖",
    "OneForAll0.2dev图因缺APIkey跳过多个模块；0.3dev图有404/500、DNS/wildcard流程、只port80、2alive和csv overwrite，最终exit0。\n\n按版本、source/module、输入范围、已跳过/失败、DNS记录/时间、端口集合、实际产物及覆盖追加分别记录；exit0、两个alive、外部失败、固定结果覆盖或单端口是反例。运行终态不等全源/全服务/接管完成。\n\n来源：[保存帖1](https://x.com/i/status/1438398469803237380)。"
  ],
  [
    "by-type/file-upload.md",
    "multipartHTML输入与取回读者合同",
    "图只给cat.html、text/html和h1 test的multipart请求；正文列黑白名单与Exif类别，没有上传响应。\n\n分别核对filename/声明MIME/实际字节、保存改名与重编码、存储策略、取回ContentType/disposition、执行handler和读者origin；请求截图、静态下载、正文转义或无保存结果是反例。扩展名/Exif可改不证明脚本执行，未上传或取回真实文件。\n\n来源：[保存帖1](https://x.com/i/status/1438409855769841664)。"
  ],
  [
    "by-type/prototype-pollution.md",
    "本地污染fixture与控制台主动原型写的差别",
    "Plution图对本地fixture输出Vulnerable；JSPanda图控制台直接defineProperty Object.prototype后显示CLOSURE_BASE_PATH Polluted。\n\n绑定应用控制入口、实际原型写、属性读/gadget和权限/后果，每次实验隔离并恢复；scanner标签、自有console写入、无应用source、没有gadget或非真实目标是反例。主动写入是实验动作，不证明应用允许攻击者污染或已XSS，本轮未执行图中JS。\n\n来源：[保存帖1](https://x.com/i/status/1438476371408343040)、[保存帖2](https://x.com/i/status/1441149046068940801)。"
  ],
  [
    "by-type/document-rendering.md",
    "文档同屏计算器与文档触发的进程因果",
    "CVE40444标题的图仅Word页面、坏图像和Calculator窗口，缺文档触发或父子进程。\n\n绑定授权隔离实验的文档hash、Office/OS版本、打开/激活步骤、保护视图、外部资源和子进程链；手工已开Calculator、只同屏、缺时间/父进程或安全策略阻止是反例。不能由PoC generator名/同屏补CVE成功，未生成/运行恶意文档。\n\n来源：[保存帖1](https://x.com/i/status/1438506586905841672)。"
  ],
  [
    "discovery/passive-and-services.md",
    "并发ping日志与主机存活的协议边界",
    "两帖把254个ping后台任务追加文件称全部alive探测，未给wait/任务结果；端口表和网络工具图只是协议类别。\n\n限定书面资产和预算，分任务id、timeout/exit、终态与日志交错、ICMP结果及实际服务观察；ICMP被过滤、队列未收完、无响应、单端口或端口与协议不符是反例。无ping不证明hostdown，后台启动不等采集完成，未扫描网络。\n\n来源：[保存帖1](https://x.com/i/status/1438506749493870602)、[保存帖2](https://x.com/i/status/1438972880390262787)、[保存帖3](https://x.com/i/status/1439555903225618436)。"
  ],
  [
    "scope-and-rules.md",
    "信任链内证据与范围外资产的授权分开",
    "正文建议scope外XSS用于scope内CORS，开放RDP推整subnet/VPS，政府清单推可猎目标；另帖自述FacebookSSRF禁止提升RCE。\n\n逐资产、动作、停止规则和书面时间版本确认授权，用自有origin/账号设计链对照；信任关系、公开列表、资产连通、历史奖励/政策或开放服务是反例。scope内影响不自动授权scope外前置动作，未登录、使用RDP或调用第三方API，也未假定历史条款当前有效。\n\n来源：[保存帖1](https://x.com/i/status/1439125764071477249)、[保存帖2](https://x.com/i/status/1439649809665724417)、[保存帖3](https://x.com/i/status/1440780132659052547)、[保存帖4](https://x.com/i/status/1441170858546905096)。"
  ],
  [
    "by-type/sql-injection.md",
    "恒真表达式相同响应的零信息反例",
    "正文称正常username和附恒真式返回同内容就确认SQLi，缺恒假和查询构造。\n\n固定身份、输入解析、参数类型和DB方言，设计获准无敏感数据的成对真假/普通无效字串对照并审计构造；忽略整个参数、查询失败回默认、缓存、转义当字串或恒真恒假相同是反例。单个同响应不证明SQL执行或注入，未运行SQL。\n\n来源：[保存帖1](https://x.com/i/status/1439027721221206024)。"
  ],
  [
    "by-type/info-secrets.md",
    "历史JS取回到秘密模式扫描的阶段连接",
    "图gau先cut query、regex选JS/JSON，fff保存200，再遍历gf _secrets模式；未显示gf从哪个目录/流读取。\n\n保存原URL/query、scope、历史与现版本、真实响应产物hash、输出目录、扫描stdin/文件来源及命中上下文；丢query改变资源、regex错选、200登录页、循环无输入或公共示例key是反例。模式命中需owner/用途/时效，不能补有效秘密，本轮未下载或使用key。\n\n来源：[保存帖1](https://x.com/i/status/1439163101438414851)、[保存帖2](https://x.com/i/status/1440360172518445070)。"
  ],
  [
    "by-type/info-secrets.md",
    "Drupal模块目录和配置字段的不同敏感度",
    "卡片给extension/services、sync目录和swiftmailertransport路径；正文>=8隐藏内容推荐没有配置响应。\n\n核对真实组件/版本、部署映射、读取身份、YAML字段及具体消费者，以最小脱敏片段分公开服务定义与有效secret；公开核心配置、无sync目录、列模块但无秘密、拒绝读取或默认模板是反例。版本范围/模块名单不等全机密配置泄漏。\n\n来源：[保存帖1](https://x.com/i/status/1439192489093644292)、[保存帖2](https://x.com/i/status/1439198521308205058)。"
  ],
  [
    "discovery/passive-and-services.md",
    "证书内网名称和组件产品名单的资产归属",
    "正文用证书internal CN和reversewhois找名称；OMIGOD完整alt列Azure Automation/Update/OMS/Log Analytics/Configuration/Diagnostics/Container Insights。\n\n分别保存证书时间/SAN/issuer/归属、组件真实版本/配置及获准可达路径；历史证书、通配名、多tenant、只有服务产品名或无实际OMI是反例。名字发现不证明内网可达/当前受影响，更不授权访问；未使用搜索名单作扫描范围。\n\n来源：[保存帖1](https://x.com/i/status/1439244049689554948)、[保存帖2](https://x.com/i/status/1439023651035271169)。"
  ],
  [
    "by-type/host-header.md",
    "代理拼接的地址顺序与身份消费者",
    "XFFor图把实际client与自填IP拼数组并称backend读取第二项，正文无最终免费权益证明；Apple图用XFHost影响302Location。\n\n分清受信任代理链、append/replace及索引顺序、业务身份来源与URL生成，固定真实路由/会话对照；合法不同用户、忽略客户端头、只302、userinfo解析差异或私有内容未取回是反例。代理示意不证明全部部署可绕认证或内部app暴露。\n\n来源：[保存帖1](https://x.com/i/status/1439572617543880711)、[保存帖2](https://x.com/i/status/1440825306453925889)。"
  ],
  [
    "by-type/xss.md",
    "上游身份邮箱到下游显示sink的完整类型链",
    "正文称提供者允许特殊邮箱，用其登录别的服务可能XSS，未保存具体字段/DOM。\n\n绑定issuer/client、已验证email声明及真实性、account linking、显示上下文、转义、读者origin和最终执行；合法邮件字符串、下游转义、值没显示、不同origin或无读者触发是反例。输入格式接受和XSS分开，不能据上游邮件含字符补下游漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1439612061458128902)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "竞态标题与逐帖日期提取代码的错配",
    "Race adduser帖子图实际遍历Twitteruser_timeline，用第一条created_at决定时间窗，再抽整个response的expandedURL。\n\n标明图与正文机制不一致；提取方法需每条时间、统一时区、分页/空结果、(URL,author)去重和snapshot版本，不能用最新帖时间判所有帖。只代码、历史API或缺分页是反例，这张图不提供竞态同时请求或adduser配额收据，未执行抓取。\n\n来源：[保存帖1](https://x.com/i/status/1439623781073444874)。"
  ],
  [
    "by-type/mobile-android.md",
    "Manifest静态声明与运行组件权限的独立证据",
    "jadx图app-debug manifest列targetSDK25、网络/storage/calendar、singleInstance及receiver exported=false；另图历史MobileTop10分类。\n\n绑定APKhash/构建类型、OS/SDK版本、具体组件/intent、权限默认/实际授予、调用者和业务对象；debug包、声明但未用、exportedfalse组件不可外达、runtime拒绝或仅分类图是反例。静态列表不等外部可利用/全移动风险覆盖，未部署APK或改设备。\n\n来源：[保存帖1](https://x.com/i/status/1439695423556435968)。"
  ],
  [
    "source-audit.md",
    "NTLM触发制品生成与实际reader回包",
    "图为模板目录、localhost file shortcut及现代格式Created/OPEN/BROWSE说明，多个旧格式被skip。\n\n分别记录授权制品hash、reader/OS/版本、具体触发、网络策略、身份和受控认证响应；只生成、localURL、被skip、用户未打开或无网络回包是反例。制品格式不证明哈希已获或凭证可用，未生成诱导文件、打开或捕获他人认证。\n\n来源：[保存帖1](https://x.com/i/status/1438974592639459329)、[保存帖2](https://x.com/i/status/1440831486609874953)。"
  ],
  [
    "source-audit.md",
    "已有执行会话与脚本打包产物的两种收据",
    "InlineExecuteAssembly图已有beacon打印Seatbelt LastShutdown；PS2EXE图编译HelloWorld.exe及config，未见新exe运行。\n\n分静态源/制品hash、生成、加载、调用、实际输出及执行身份，绑定授权实验；已有beacon、文件列表、编译成功、输出无因果或无权限变化是反例。菜单/打包不补首次入口、EDR绕过或提升权限，未运行Assembly/PowerShell。\n\n来源：[保存帖1](https://x.com/i/status/1439699548583125000)、[保存帖2](https://x.com/i/status/1439925963547201549)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "日志字符串到可解释包含文件的完整前提",
    "彩色/黑白LFI图示include输入、日志污染、error log再include和shell/DoS后果，均为概念链。\n\n需同时绑定可控日志原始字节/转义、实际日志路径与读权限、可包含消费者、解释器版本/策略及最小无害终态；日志被编码、路径不可读、普通read不解释、权限不足或只图示是反例。LFI读取不自动RCE/DoS，未写日志、取回shell或运行payload。\n\n来源：[保存帖1](https://x.com/i/status/1439997933122850822)、[保存帖2](https://x.com/i/status/1441295013015474190)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "PHP输入过滤与进程交互wrapper的能力区别",
    "正文把php file、filter、input等混成LFI→RCE。官方文档说明php://input读取原始请求体，php://filter对stream施过滤；expect://默认未启用且需PECL扩展。\n\n先纠正输入流名称为php://input，按已注册wrapper、版本/扩展、配置、read与include及具体消费者核对；格式拼写错、wrapper缺失、只读过滤、multipart限制或解释拒绝是反例。不把过滤器自动当执行，也不把示例command当实测。依据：[PHP I/O与过滤流](https://www.php.net/manual/en/wrappers.php.php)、[expect扩展条件](https://www.php.net/manual/en/wrappers.expect.php)。\n\n来源：[保存帖1](https://x.com/i/status/1440999244870008839)。"
  ],
  [
    "by-type/info-secrets.md",
    "CDX重复URL与独立有效密钥计数",
    "CDX图original/collapseurlkey列多次相似api-key query且含test字样；正文声称10k premiumkeys但没独立有效性证据。\n\n按源URL/归档时间/值hash/owner/字段用途去重，区分曝光行、独立候选、测试值、仍有效凭据及消费权限；重复端点、过期/已撤销、公开示例或只有清单是反例。历史行数不等可用密钥数，值未复制、下载或用于调用服务。\n\n来源：[保存帖1](https://x.com/i/status/1440230073857052674)。"
  ],
  [
    "impact-and-acceptance.md",
    "metrics拒绝与私人红队Critical标签的独立判断",
    "GC周期/metrics报告图NA closed，正文归因名气；私人红队奖表把default password/BAC/weakpolicy/redirect/phpmyadmin exposure都标Critical。\n\n根据各自政策版本、最小敏感字段、实际身份/动作/消费者和具体影响判定；不同计划、类名相同、一般性能指标、只有标题评级/奖励或无完整链是反例。不能从NA推处置动机，也不能把私人表转通用评级，未改既有等级规则。\n\n来源：[保存帖1](https://x.com/i/status/1440269668011282443)、[保存帖2](https://x.com/i/status/1441093316330749955)。"
  ],
  [
    "scope-and-rules.md",
    "工具UA识别和公开目录的执行授权界限",
    "正文建议改第三方工具UA；另有GitHubAction批扫、多种网络工具及开放主机玩笑。\n\n记录获准项目要求的识别标记、版本/headers、单资产动作、速率和停止条件，区分观察工具与会更改路由/防火墙/namespace的命令；UA改变、平台可运行、端口开放或匿名是反例。不得据这些文字隐藏身份或绕封禁授权，本轮未启动扫描/登录/配置操作。\n\n来源：[保存帖1](https://x.com/i/status/1440310211353350154)、[保存帖2](https://x.com/i/status/1438985281697374211)、[保存帖3](https://x.com/i/status/1440606405682032649)。"
  ],
  [
    "by-type/idor-access-control.md",
    "internal候选路由和HTTP方法的对象合同",
    "正文internal路由403→200和POST改GET只有状态建议，无具体私有对象响应。\n\n固定两自有角色、同owner/object、route handler、动作语义和最终读写状态；200通用error/登录shell、只GET公共信息、另一对象、no-op或未复现是反例。命名internal不表示特殊信任，方法差异不自动IDOR/绕过。\n\n来源：[保存帖1](https://x.com/i/status/1440377743674204167)、[保存帖2](https://x.com/i/status/1439510177678516227)。"
  ],
  [
    "discovery/web-and-api.md",
    "错误页逆图搜索的框架候选和部署验证",
    "正文从error截图逆图搜索发现框架，没有保存实际版本/组件证据。\n\n保存响应headers/最小非敏感error文本、页面来源/hash、时间、资源/部署归属及独立组件特征；模板复制、代理统一error、旧教程图片、图片近似或版本未给是反例。图像相似只形成fingerprint假设，不补框架漏洞或后端实现。\n\n来源：[保存帖1](https://x.com/i/status/1440394841536413699)。"
  ],
  [
    "by-type/xss.md",
    "自操作XSS到其他读者以及客户端取回的边界",
    "正文selfXSS加CSRF、缺X-XSS-Protection会变严重，又以window.location去自有server称XSPA。\n\n验证是否可获准地种植到另一自有读者、cookie/SameSite/CSRF、持久状态、origin和实际DOM执行，另辨浏览器导航与backend取回；仅自己控制台、无法种植、缺旧header、导航回调或无server消费是反例。缺header不是成功链，客户端callback不证明SSRF/内网访问。\n\n来源：[保存帖1](https://x.com/i/status/1440419533290827786)。"
  ],
  [
    "discovery/passive-and-services.md",
    "网络工具图的观察层与配置副作用",
    "整张图列ping/curl、DNS/whois、SSH复制、抓包、route/IP、ARP、VPN/firewall、TLS、性能和namespace等。\n\n按发现标识、请求协议、连接、流量证据、配置和转发分类，绑定获准资产、输入/输出及终态；工具装好、名称相似、单协议无响应或未见对应流量是反例。修改路线、防火墙、流量或命名空间与只读查询分别需动作授权，图未实际运行。\n\n来源：[保存帖1](https://x.com/i/status/1440606405682032649)。"
  ],
  [
    "targeted-fuzzing.md",
    "词种扩增数量与候选预算的关系",
    "Weakpass图两个seed生成432个大小写/后缀候选；正文Haptyc列Sniper/Clusterbomb/Batteringram/Pitchfork。\n\n保存获准输入来源、生成规则/去重、每参数类型、组合数、逻辑动作数和明确预算/停止条件；432不等有效密码、攻击模式不保证正确参数或可授权登录，组合乘积可能远大于请求直觉。本轮未用字典认证/破解或运行TurboIntruder。\n\n来源：[保存帖1](https://x.com/i/status/1440499606022877191)、[保存帖2](https://x.com/i/status/1440722559834546183)。"
  ],
  [
    "by-type/business-logic.md",
    "通知和邀请发送的业务动作配额",
    "两100奖励邮件标题分别提无限admin creation/daily notification及employee invitation emailbomb；OTP图只phone/SMSformat字段。\n\n绑定自有recipient、发送动作/对象、challenge用途、时间窗、规范化身份和backend计数，使用获准极小预算/停止点；奖邮件、参数接受、队列但未实际发、合法不同recipient或429统一页是反例。不能从标题补实际轰炸影响/当前政策，未发送邮件/SMS。\n\n来源：[保存帖1](https://x.com/i/status/1440639317076897793)、[保存帖2](https://x.com/i/status/1439174977274540035)、[保存帖3](https://x.com/i/status/1439680362649726978)。"
  ],
  [
    "by-type/desktop-client.md",
    "协议URI初始argv与后续启动参数的两次消费",
    "WorkSpaces图版本3.1.6.2064初始ProcessStart，--uri内含编码空格及gpu launcher候选，未显示calc子进程；two-tier图只架构。\n\n绑定浏览器/OS handler、URL解码、命令行quoting/argv、客户端再解析/进程派发、权限及最小独立子进程收据；只有URI显示、flags留在字符串、进程正常打开或无child因果是反例。初始argv不等后续参数注入，更不能自动云端RCE，未注册handler或运行客户端。\n\n来源：[保存帖1](https://x.com/i/status/1440647256139468811)、[保存帖2](https://x.com/i/status/1438813781719588865)。"
  ],
  [
    "by-type/graphql.md",
    "creator邮箱字段路径与订阅者列表声称的区别",
    "VoiceCreator图文字称可列subscriber邮箱，query实际指向publications.creator.email_settings.confirmed_email.email_address，没有response。\n\n绑定调用身份、resolver/object owner、可见性意图、具体返回field、分页和敏感字段最小对照；只query、公开creator邮箱、合法订阅资料、无结果或字段归属不同是反例。结构路径不证明全订阅者名单/权限缺失，未执行GraphQL请求。\n\n来源：[保存帖1](https://x.com/i/status/1440934050059882502)。"
  ],
  [
    "by-type/xss.md",
    "符号码元生成与片段调用终态的分离",
    "代码图从第21行起，用类型强转和字符串索引拼constructor/Function/alert字样；标题称无字母数字括号调用，缺最终调用片段。\n\n分实际source code、字符字面量与运行字符串、生成函数/调用语法、CSP和读者origin；仅字符串拼成、comment有字母、缺前后段、语法失败或无实际alert是反例。裁切片段不证明整payload满足字符约束/执行，本轮未执行代码；另alert域截图仍需source/sink/trigger。\n\n来源：[保存帖1](https://x.com/i/status/1441165012727435267)、[保存帖2](https://x.com/i/status/1441062037124042772)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "shell提示符外观与实际执行身份",
    "正文建议exportPS1为井号提高impact，是显示层反讽，没有uid/权限变化。\n\n以实际执行身份/有效权限、具体受控动作和独立输出判边界；prompt井号、Administrator窗口标题、合法既有会话或仅echo外观是反例。环境提示文字不提升uid/能力，不能把视觉变化计提权、root或严重度提升。\n\n来源：[保存帖1](https://x.com/i/status/1441182516451233800)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "客户端路径规范化的真实wire对照",
    "正文称curl/browser会去点段而Python原样，并给urllib示例，未保存实际请求。\n\n绑定具体库/版本/选项、URL解析/重定向、代理和服务端路径，保存受控endpoint收到的raw target和各层规范化值；库差异、redirect二次规范化、只打印response、另代理或未观察wire是反例。不能把语言名当始终原样，也不能从响应错误补traversal成立，本轮未发路径请求。\n\n来源：[保存帖1](https://x.com/i/status/1441204534366326784)。"
  ],
  [
    "by-type/authn-session.md",
    "认证前后矩阵与跨客户端同邮箱身份",
    "一帖建议先preauth场景；另一保存1/2为Web上传私有文档后Android同邮箱不同密码注册，缺续文/最终文档读取。\n\n固定自有身份和realm、email规范化/验证、注册与登录/恢复的状态及各端API主体，分别比较无会话/低权/owner；独立realm、邮箱尚未验证、signup拒绝、私有文档仍拒绝或未给2/2是反例。同邮箱不是同身份/ATO证明，缺续文计覆盖但不补终态。\n\n来源：[保存帖1](https://x.com/i/status/1441330833529311241)、[保存帖2](https://x.com/i/status/1441388316415254551)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0110.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==87 and len(urls)>0
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
