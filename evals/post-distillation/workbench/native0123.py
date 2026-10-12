# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "experiment-design.md",
    "Voltron 调试器画面须绑定架构和当前停点",
    "完整画面包含反汇编、寄存器、栈与GDB的argc/strcmp、sleep和循环示例；这说明本地调试状态，没有远程漏洞入口。\n\n离线自有程序分别记录架构、线程、停点、地址和寄存器/内存变化，将输入到分支与执行结果关联。布局工具、地址列表或已经进入调试器不是任意代码执行证明；错误线程、过期停点、无法控制输入为反例，不执行保存样例。\n\n来源：[保存帖1](https://x.com/i/status/1495507089774592002)。"
  ],
  [
    "by-type/xss.md",
    "SVG 未编码尖括号须追到实际 HTML 消费者",
    "正文称关闭SVG的右尖括号被转义而尾部左尖括号未处理，另一帖提供编码SVG并声称除Firefox外可用；未保存原始响应、完整DOM和浏览器版本。\n\n离线合成页面分别对HTML文本、属性和SVG命名空间保留输入/输出字节及实际解析树，比较转义与无害标记事件。单字符存留、无事件触发、已清洗、CSP阻止或浏览器差异为反例，不将编码片段推广为通用绕过。\n\n来源：[保存帖1](https://x.com/i/status/1495604143192424450)、[保存帖2](https://x.com/i/status/1497278782465613827)。"
  ],
  [
    "by-type/waf-bypass.md",
    "iframe javascript 与 ESI 注释要分清不同解析阶段",
    "完整浏览器图有十六进制编码的iframe javascript属性与空白prompt；正文还有fo<!--esi-->cus/a<!--esi-->lert变体。没有边缘规则、上游处理后的字节或ESI处理证据。\n\n离线分别模拟原始输入、服务端ESI/注释转换与浏览器属性解析，保存版本、CSP和允许/拒绝基线。普通HTML注释不会自动等同服务端ESI删除；弹框、注释字样或作者WAF名称不足以证明当前全规则绕过，不在线发送原片段。\n\n来源：[保存帖1](https://x.com/i/status/1495649900679565312)、[保存帖2](https://x.com/i/status/1496777513019736064)、[保存帖3](https://x.com/i/status/1498694254054367241)、[保存帖4](https://x.com/i/status/1499046914574196740)。"
  ],
  [
    "impact-and-acceptance.md",
    "document.cookie 弹框要证明实际可用权限",
    "完整图显示问卷分数参数、注入片段及cookie弹框，可以辨认分析类cookie等字串，没有其他读者或可用会话证据。\n\n离线两个自有账号比较执行origin、可读存储类型、HttpOnly、token有效期/绑定及允许的合成动作。分析cookie、本人的浏览器、不可重用值或后台拒绝都是反例；弹出cookie不自动形成ATO或RCE，不复制真实值或外发数据。\n\n来源：[保存帖1](https://x.com/i/status/1496035563073327110)。"
  ],
  [
    "by-type/info-secrets.md",
    "词表命中 config.json 与真实秘密暴露分层",
    "完整图有config.json连接串UID/password、数据库/服务器和AWS/S3字段；另一组JS图有crypt.secret、document token加密注释及demoConfig的orgId/token/restUri/searchHub。正文还列Contentful、Rollbar、Scandit与密钥关键词，没有验证权限。\n\n离线合成材料分字段名称、预期公开的客户端配置、样例值、部署秘密、所属项目和失效状态；消费者决定token读写权限与密钥用途。只有名称/格式、公开搜索token、过期值或无受保护消费者为反例；脱敏记录可见内容，不尝试数据库、API或云凭据。\n\n来源：[保存帖1](https://x.com/i/status/1496042257665097729)、[保存帖2](https://x.com/i/status/1498314216700264453)、[保存帖3](https://x.com/i/status/1498689653792133124)、[保存帖4](https://x.com/i/status/1499700990651494401)。"
  ],
  [
    "by-type/xss.md",
    "phpinfo 服务端回显与 HttpOnly 读取限制分开",
    "完整图phpinfo的$_COOKIE/ci_session与DevTools HttpOnly=true/Secure=false并列；另一图JS用带凭据同步XHR读取info.php，再按HTTP_COOKIE索引截取与base64；multipart另有外部script，JSONsuccess=true。后两图未显示受害读者、XHR完整结果或回连。\n\nHttpOnly限制脚本读取cookie，但浏览器仍可能在XHR/fetch中发送符合条件的cookie。离线同源合成页面比较凭据模式、鉴权、服务器是否回显、SOP/CORS、CSP和真实读者；substring不是精确提取，保存成功也不等脚本执行。无回显、无读取权限、跨源拒绝或无其他读者为反例，不执行外部脚本/外发。\n\n规范核对：[MDN Set-Cookie HttpOnly](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#httponly)。\n\n来源：[保存帖1](https://x.com/i/status/1496091043334344704)。"
  ],
  [
    "source-audit.md",
    "Git clone 与 mirror 的引用覆盖范围需列清",
    "正文提示普通clone与mirror可能暴露范围不同，没有保存具体引用集合、敏感提交或服务端权限。\n\n离线自有仓库清单分别记录远端公开引用、抓取refspec、HEAD、分支/标签与历史可达对象，比较两种采集契约。仅默认分支干净不证明全公开历史无秘密；镜像名称、未实际抓取的引用或无敏感内容为反例，不恢复真实目标仓库或复用历史密钥。\n\n来源：[保存帖1](https://x.com/i/status/1496191307189997571)。"
  ],
  [
    "discovery/web-and-api.md",
    "路径后缀和账户标识变体须保留对象同一性",
    "正文列PHP/ASP候选和API的.json、?、斜杠、v2、账户路径、X-Original-URL；另称网站/users/reports/settings拒绝而API子域200。没有基线与受限数据响应。\n\n离线路由/授权模型逐次只改一个维度，记录Host、方法、路径、解析对象、身份、角色与字段，比较公开不存在资源。后缀不证明技术栈；200错误/登录页、不同对象或预期公共API为反例，不把状态码差异直接判认证绕过。\n\n来源：[保存帖1](https://x.com/i/status/1496197554291322884)、[保存帖2](https://x.com/i/status/1496390979502411779)、[保存帖3](https://x.com/i/status/1496786769316294659)、[保存帖4](https://x.com/i/status/1497861151320731649)。"
  ],
  [
    "by-type/idor-access-control.md",
    "手机 POST userid 到接管仍缺执行消费者",
    "正文说手机登录POST能控制userid、网页没有并需用户交互；完整图只有Android误配置报告Medium5.4/1000奖励状态，没有请求、响应或被接管会话。\n\n离线自有两账号比较同一登录事务、主体userid、身份来源与最终会话授权，分设备API表面和后端信任。只改客户端UI、普通用户详情、分诊评级或未跨主体为反例，不由手机特有字段和奖励推导ATO。\n\n来源：[保存帖1](https://x.com/i/status/1496289535902289924)。"
  ],
  [
    "discovery/passive-and-services.md",
    "nrich Shodan ADB 与来源归属边界",
    "正文介绍IP标准输入获取Shodan metadata，另将5555端口ADB banner称Android Root Bridge并联系ETH挖矿速度；没有设备权限与shell结果。ADB是Android Debug Bridge，端口/名称不等root。\n\n离线合成索引记录采集者、时间、IP/端口、banner、协议与资产所有权，再分服务存在、认证要求和运行权限。缓存、共享IP、误指纹、鉴权ADB或未有shell为反例，不连接公开设备、试认证或安装矿工。\n\n来源：[保存帖1](https://x.com/i/status/1495889084581310464)、[保存帖2](https://x.com/i/status/1496429862726549506)。"
  ],
  [
    "scope-and-rules.md",
    "奖励与地区 dork 搜索不能扩展项目许可",
    "保存正文按奖励政策、地区/行业关键词及域检索，有拼写/语法差异，没有当前项目条款与实际授权。\n\n离线保存候选来源、规则版本、资产所有者、允许行为和排除类型；搜索命中只建立发现线索。reward关键词、历史礼品、第三方托管和地区后缀不是许可；当前规则未知或动作不允许为反例，不按搜索结果自动测试。\n\n来源：[保存帖1](https://x.com/i/status/1496431484563075077)、[保存帖2](https://x.com/i/status/1496431487528353798)、[保存帖3](https://x.com/i/status/1496431490288484353)、[保存帖4](https://x.com/i/status/1496431496479088640)、[保存帖5](https://x.com/i/status/1496431500346204160)、[保存帖6](https://x.com/i/status/1496431513788989450)、[保存帖7](https://x.com/i/status/1498458896159051778)。"
  ],
  [
    "reporting.md",
    "四十八小时未回应不是统一升级披露时限",
    "正文建议等48小时后追问并借社交媒体/大客户催促，没有项目协议和报告状态上下文。\n\n将项目约定的回应期限、复现材料、收件渠道、严重性与披露条款分别记录，离线准备最小复现及待补信息。周末、需补证据、重复状态或条款不允许公开为反例；个人建议不成为自动发布/联系客户流程，不发送消息。\n\n来源：[保存帖1](https://x.com/i/status/1496481932699648005)。"
  ],
  [
    "discovery/web-and-api.md",
    "DorkSearch 分类 UI 与可用搜索结果分开",
    "完整图显示漏洞公告、错误、秘密文件、登录、设备等dork类别，没有查询文本、命中内容或资产归属。\n\n离线把每类映射到预期材料与最小证据字段，记录时间、归属、是否样例和敏感性。分类菜单或品牌图标不是漏洞发现；无查询、缓存、公开样例为反例，不执行批量搜索。\n\n来源：[保存帖1](https://x.com/i/status/1496528120815534084)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Nuclei Burp 生成器与可验证模板分开",
    "两张完整Burp图在Nuclei页展示localhost:8081的GET /，无响应/匹配器结果；正文鼓励编写目标相关模板。\n\n离线合成请求响应分别测试模板变量、方法/编码、响应条件、负例、版本和受限行为，记录生成、执行与人工确认各阶段。生成页出现、请求成功、过宽200匹配或没有目标响应为反例；不安装来源插件或在线运行模板。\n\n来源：[保存帖1](https://x.com/i/status/1495952673795112963)、[保存帖2](https://x.com/i/status/1496552195432812548)、[保存帖3](https://x.com/i/status/1496843213276995586)、[保存帖4](https://x.com/i/status/1499112304641720325)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "aquatone takeover 输入与服务归属独立判断",
    "正文给带http scheme的-d示例，但没有DNS、服务专属错误、当前可注册状态或受控内容。\n\n先在离线输入契约核域名/URL格式，再分DNS别名、失联服务、归属和注册限制；记录工具历史版本与错误。命令标题、404或错误输入不是可接管证据，已保留/已占用资源为反例，不实际占用资源。\n\n来源：[保存帖1](https://x.com/i/status/1496605500359729159)。"
  ],
  [
    "by-type/info-secrets.md",
    "银行文档被索引与上传删除权限分别验证",
    "正文问被Google索引的银行PII照片/存折、上传和删除如何影响，没有保存文件正文、访问身份或操作结果。\n\n离线合成文档区分公开索引、下载权限、对象所有者、上传与删除动作，使用脱敏元数据和两账号权限对照。索引URL、已公开样例或同一所有者操作为反例；不下载第三方银行资料、不上传/删除或尝试财务操作。\n\n来源：[保存帖1](https://x.com/i/status/1496681761018892288)。"
  ],
  [
    "reporting.md",
    "视频和 CVSS 好评不能充当统一奖励公式",
    "完整图报告质量反馈给CVSS与视频不同分值并有奖励时间线；正文强调攻击者视角。属于历史个案，没有普遍奖金公式。\n\n报告围绕主体、对象、前提、最小复现、结果和反例选择清晰证据；视频、文字或截图都要能追到同一请求/业务结果。形式评分、可读性和实际影响分开，单个项目反馈/个人偏好不证明当前通用评级或奖金。\n\n来源：[保存帖1](https://x.com/i/status/1496746775897513985)。"
  ],
  [
    "by-type/authn-session.md",
    "WinBruteLogon 的 found 输出与真实认证分离",
    "完整help列username/domain/wordlist及线程/verbose，示例打印本机Visitor、10001候选、2线程和OK found password。正文声称Guest、无限次和几乎任何密码，但无独立登录证据。\n\n离线自有认证模型区分Guest/禁用账户、API返回、权限/锁定策略和新会话身份，记录版本与误报条件。工具打印、本机账户列表、没有真实认证消费者或错误状态解释为反例；不尝试保存密码、暴力认证或运行工具。\n\n来源：[保存帖1](https://x.com/i/status/1496820859100618756)。"
  ],
  [
    "by-type/ssrf.md",
    "DNS rebinding 要比较解析检查和实际连接地址",
    "正文称被阻断SSRF可尝试DNS rebinding并找到两项，没有DNS时序、地址校验或连接结果。\n\n离线假DNS/HTTP消费者分别记录首次解析、校验、连接时重解析、缓存、重定向与Host/SNI，比较固定允许/禁止/变化地址。域变化、纯浏览器解析、连接锁定原地址或禁止范围为反例；不访问内部/云元数据或触发外部DNS回连。\n\n来源：[保存帖1](https://x.com/i/status/1496865043652268034)。"
  ],
  [
    "by-type/open-redirect.md",
    "二十五个 redirect 名称不等重定向消费者",
    "完整词表含next/url/target/destination/redirect_uri/returnTo/checkout_url/continue等，另一图是Message参数与hacked弹框，未有Location或外部导航。\n\n离线分别识别HTTP Location、前端导航、服务端抓取和业务返回路径，核URL解析、相对地址与允许origin。参数名称、XSS弹框、状态200或只回显字串为反例；需要真实导航消费者及无害同源/拒绝对照，不把redirect_uri直接判开放重定向。\n\n来源：[保存帖1](https://x.com/i/status/1496919715306156032)、[保存帖2](https://x.com/i/status/1496932065039822856)。"
  ],
  [
    "hunting-strategy.md",
    "忽略已被工具发现的子域会遗漏重要旧资产",
    "正文建议amass/subfinder扫到的全部忽略去找新目标；其他帖描述被动数据源与工具比较，没有覆盖、时效或风险结果。\n\n离线候选集合保存提供者、时间、所有权与重复关系，按业务敏感性、变化和证据缺口排序；对排除资产记具体理由。新颖性不等风险；已有但新增服务、过期索引或遗漏来源为反例，不默认排除全部常见资产。\n\n来源：[保存帖1](https://x.com/i/status/1497037378128850944)、[保存帖2](https://x.com/i/status/1497901767618883591)、[保存帖3](https://x.com/i/status/1497936591687340033)。"
  ],
  [
    "by-type/graphql.md",
    "GraphQL 空 OTP 成功字段不能直接证明 2FA 绕过",
    "完整图POST /graphql有遮蔽token、空otp_code及六位verification_code；HTTP200 JSON同时有was_successful=true与errors.edges。正文标题延伸到RCE，没有完整mutation、语义和会话状态。\n\n离线合成mutation区分phone验证、登录二因素、字段校验、错误和最终身份，比较正常/空值/失败与后续权限。HTTP200、局部布尔成功、其他验证步骤或错误拒绝为反例；无绑定变化不能判2FA绕过，更不能凭标题推RCE。\n\n来源：[保存帖1](https://x.com/i/status/1497118123387801600)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "JNDI server 监听和生成链接不等目标类加载执行",
    "完整图是本地JNDI工具java参数与open Calculator示例，HTTP/RMI/LDAP监听及输出url，并注释历史JDK trustURLCodebase要求；没有目标lookup/加载/执行。\n\n离线模型绑定实际Java组件版本、输入来源、lookup配置、类来源、加载权限与执行结果。工具启动、生成链接、DNS/LDAP请求都不足以单独证明执行；无可达消费者、受限加载或仅本机演示为反例，不启动来源服务或进行回连。\n\n来源：[保存帖1](https://x.com/i/status/1497183115147726848)、[保存帖2](https://x.com/i/status/1497185828006629382)。"
  ],
  [
    "experiment-design.md",
    "复制 WordPress 插件搭建练习不能代替目标复现",
    "正文建议识别站点插件后自建相同WordPress再测试，并称总能找到XSS；没有目标版本、设置、输入或其他读者。\n\n自有离线模型对齐插件/核心版本、启用功能、角色、配置和数据流，再记录偏差。只匹配插件名称、不同角色或修复版本为反例；本地发现只是候选机制，不能宣称生产站点有相同问题或保证所有插件有XSS。\n\n来源：[保存帖1](https://x.com/i/status/1497221854725029898)。"
  ],
  [
    "discovery/passive-and-services.md",
    "PublicWWW 代码索引与当前完整站点不同",
    "正文介绍从HTML/JS/CSS文本搜索并导出网站列表，没有目标命中与当前代码。\n\n离线候选保留索引时间、关键词来源、域归属、上下文和去重；将代码引用、第三方资源和当前部署分层。关键词命中、缓存、公共库或域列表不是秘密/漏洞证明；不能以导出列表宣称全站覆盖或授权。\n\n来源：[保存帖1](https://x.com/i/status/1497225924735119361)。"
  ],
  [
    "by-type/idor-access-control.md",
    "POST 改 PUT 的方法差异须跨同一权限边界",
    "正文称修改HTTP方法可出IDOR，没有实际交换或对象变更。\n\n离线两个自有角色对同一对象与动作比较方法路由、body解析、认证、授权和持久状态；保留正常主体/非所有者/不存在对象。405/200、不同操作、无数据或预期允许为反例；需要非预期身份确实读写受限对象，不执行真实写入。\n\n来源：[保存帖1](https://x.com/i/status/1497230317153062915)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "混淆 Google 服务 ID 不等管理员角色已赋予",
    "完整片段有SERVICE_ADMIN_ROLE、Services Administrator及APPADMIN/VIEWDLPRULE、遮蔽serviceIds，没有ID映射、请求、角色赋予或权限结果。\n\n离线合成权限模型分别记录服务ID命名、角色定义、赋予主体/对象、实际消费权限及审计结果。隐藏数字、源码常量和角色名称不是管理员权限；未知服务映射、未赋予或后台拒绝为反例，不猜ID或修改真实角色/支付服务。\n\n来源：[保存帖1](https://x.com/i/status/1497257010751885314)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "Tomcat 凭据中的 root 字符串不等系统 root",
    "正文描述历史演练从公网Tomcat root/root到AD，没有保存认证/进程身份和跨域授权链。\n\n离线自有身份图分应用账号、服务进程uid/权限、宿主机与域身份及必要凭据来源，记录每一步允许动作。默认密码名字、登录页或应用管理员不自动是OS root；无成功认证/目标权限为反例，不尝试凭据或进入真实目录。\n\n来源：[保存帖1](https://x.com/i/status/1497410380322459650)。"
  ],
  [
    "by-type/idor-access-control.md",
    "管理员页面 UI 不证明访问控制已绕过",
    "完整图实际Shipment Details界面和物流历史；另有SelfXSS Duplicate Closed及APIIDOR P3/850报告，双重复正文称v1拒绝v2允许。未保存跨身份请求与返回。\n\n离线自有两账号比较接口版本、对象归属、字段和真实权限，保留正常/拒绝基线与业务状态。界面、奖金、重复标题或仅200为反例；版本差异需证明同一受限对象跨主体返回，不能拼成管理员或重置接管链。\n\n来源：[保存帖1](https://x.com/i/status/1497511157803851777)、[保存帖2](https://x.com/i/status/1497525901503967240)、[保存帖3](https://x.com/i/status/1497529982725369858)。"
  ],
  [
    "discovery/passive-and-services.md",
    "NTLMRecon 多端点认证 challenge 与登录不同",
    "完整终端列43种候选端点，EWS的NTLM、ActiveSync Basic realm、PowerShell Kerberos与Rpc Basic并保存CSV；没有凭据认证、授权读取或执行。\n\n离线合成响应按端点记录挑战头、realm、协议、响应来源和版本，避免将单端点能力推广全站。401挑战、代理通用realm、工具表格都不证明密码有效或匿名访问；不发送握手/试密码，将服务元数据与实际权限分开。\n\n来源：[保存帖1](https://x.com/i/status/1497545612018999296)、[保存帖2](https://x.com/i/status/1497560778966138882)。"
  ],
  [
    "by-type/host-header.md",
    "Host 进入 SilverStripe Location 与重置毒化分开",
    "完整GET /admin/pages带Host bing.com及cookie，响应302 Location包含该Host，另有控制器、locale HttpOnly和CSP。没有原始Host对照、重置邮件或缓存受害结果。\n\n离线路由模型分别核Host校验、反向代理可信字段、重定向构造、重置URL消费者和缓存键。Location引用输入只支持该行为候选；普通跳转、无受害消费者、缓存不共享或后台固定邮件域为反例，不重放cookie或发送真实重置邮件。\n\n来源：[保存帖1](https://x.com/i/status/1497550104990928897)。"
  ],
  [
    "by-type/waf-bypass.md",
    "点路径与分号路径须核前后端规范化差异",
    "完整tip写/image/../secretfolder和/image/..;/secretfolder并要求首目录存在，没有实际403/200、规范化后的对象或服务响应。\n\n离线比较前端与后端的解码次数、点段、分号path参数、文件/路由识别和权限作用点，保存实际消费者。差异字符串、工具返回200、访问公共对象或两端一致拒绝为反例，不以变体列表宣称绕过所有当前WAF。\n\n来源：[保存帖1](https://x.com/i/status/1497552035855675394)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Katoolin3 标题与 v1.0 安装菜单不是同一版本证据",
    "完整图是Katoolin v1.0列330工具、仓库更新、类别、菜单与帮助，正文称Katoolin3。没有安装结果或当前仓库状态。\n\n离线自有工具清单绑定实现版本、包源、选项、成功/失败与可见功能，保留正文和图片版本冲突。菜单数量、仓库存在或工具集合标题不等所有安装完成/安全；不安装、添加源或执行保存命令。\n\n来源：[保存帖1](https://x.com/i/status/1497681580193726464)、[保存帖2](https://x.com/i/status/1497707538871058432)。"
  ],
  [
    "by-type/xss.md",
    "反射存储 DOM 和 self 标签不是互斥四类",
    "正文将XSS分四种，另一帖声称mutation XSS，图仅XSS Hunter fires列表、受害URI/IP、缩略图与操作按钮，没有变异前后解析字节。\n\n离线按输入持久性、服务器/DOM消费者、实际读者权限及解析变换分别建维度；mutation还需清洗前后与重解析DOM差异。回连界面、标签名称或本人console不等独立受害链；未出现解析变化/无跨读者为反例，不触发真实回连。\n\n来源：[保存帖1](https://x.com/i/status/1497784305979990020)、[保存帖2](https://x.com/i/status/1498986395817308166)。"
  ],
  [
    "targeted-fuzzing.md",
    "全端口建议仍需服务和预算覆盖证据",
    "正文建议先全端口再Nuclei，没有保存端口范围、扫描错误、服务确认或项目许可。\n\n离线候选计划分协议/端口、发现时间、权限、速率和时间预算，记录成功、拒绝、超时和跳过；服务指纹后再选择适配方法。端口列表、banner或扫描结束不证明全资产安全/存在漏洞，不运行真实扫描。\n\n来源：[保存帖1](https://x.com/i/status/1497852994976550914)。"
  ],
  [
    "discovery/passive-and-services.md",
    "staging 与 log 关键词只生成历史候选",
    "正文把Subfinder带http域输入、grep staging与Google日志搜索串联，没有DNS、响应或日志内容；另有被动recon文章标题。\n\n离线验证工具输入契约、host/URL归一、提供者/时间、候选归属和材料预期公开。staging名称不等低权限、搜索log不等敏感日志；缓存、无当前解析或非本项目为反例，不访问保存真实域或外链全文。\n\n来源：[保存帖1](https://x.com/i/status/1497864905533566980)、[保存帖2](https://x.com/i/status/1497893317777887234)。"
  ],
  [
    "by-type/graphql.md",
    "GraphQL 思维图把 schema 和动作候选分开",
    "完整图可辨端点/Playground/Schema、基础/深层introspection、类型/字段/参数、query/mutation、用户/权限及商业逻辑；部分微小叶子字不可辨。没有实际服务交换。\n\n离线合成schema按端点、身份、可查询字段、动作和角色归属记录；schema描述与实际授权分别对照。只出现admin/delete词、能introspection、图中列batch/brute或深查询不证明漏洞；无越权结果、文档公开为反例，不执行真实变更、认证批量尝试或深度耗尽。\n\n来源：[保存帖1](https://x.com/i/status/1497905641104736257)、[保存帖2](https://x.com/i/status/1497930716289527813)。"
  ],
  [
    "experiment-design.md",
    "已经 root 的 CTF flag 不能补全初始入口",
    "完整图训练Gift主机root提示符、列user.txt与flag，并有Root and User Flag alt；未保存取得root的方法。\n\n记录训练身份、入口前状态、每步权限变化和本地合成结果，区分读flag与漏洞机制。已特权shell、共享SSH密码或旗标存在不能证明提权/生产越权；不复制旗标/密码或连接训练之外目标。\n\n来源：[保存帖1](https://x.com/i/status/1497976067683860480)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "DRAKVUF 样本元数据和进程树不是恶意结论",
    "完整报告有PE32+ x86-64 Windows样本、哈希、约15秒运行以及系统/测试进程树，没有完整API行为、网络或恶意因果。\n\n离线报告分别绑定样本哈希、系统/虚拟机、运行窗口、进程父子和观测缺口，比较良性控制和具体行为。工具名称、test.exe、系统进程或短运行窗口不是恶意/安全证明；不运行存档样本或安装分析环境。\n\n来源：[保存帖1](https://x.com/i/status/1498043946227978250)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "二十五个 RCE 参数名称仍缺命令执行 sink",
    "完整词表含cmd/exec/command/ping/query/code/func/load/process/read/module/payload/run/print等，另一图列前十项。没有请求、输出或执行消费者。\n\n离线合成应用按输入到参数化API、模板、shell或系统命令的数据流追踪，比较字面值和无害本地标记。参数名、500、工具告警或仅回显为反例；须真实解释器消费才支持命令注入，不运行保存payload/批量猜参数。\n\n来源：[保存帖1](https://x.com/i/status/1498053222757695488)、[保存帖2](https://x.com/i/status/1498264630929477633)。"
  ],
  [
    "by-type/ssrf.md",
    "嵌套 image URL 到元数据仍缺请求身份",
    "正文从localhost image?url嵌套到云元数据并声称header/WAF变体，没有保存HTTP链、header内容或返回字段。\n\n离线假服务模型分外层抓取者、内层地址解析、转发header、重定向和网络身份，比较拒绝地址/不抓取/授权合成字段。URL看似metadata、浏览器请求或只回显为反例；不访问内部服务或云元数据，不凭标题推全账号接管。\n\n来源：[保存帖1](https://x.com/i/status/1498219178699878402)。"
  ],
  [
    "reporting.md",
    "提交收据与邮件 claim 不等分诊完成",
    "完整图提示submission received，并要求邮件关联finding；没有已认领、分诊、有效性或支付。\n\n离线记录提交标识、渠道规则、收据与后续状态，每一步保留实际证明。收据、回复模板或待claim说明不能计入确认漏洞/奖励；不发送邮件或认领他人提交，将未完成状态如实留档。\n\n来源：[保存帖1](https://x.com/i/status/1498239456242909187)。"
  ],
  [
    "by-type/ssti.md",
    "Ruby ERB 的字符串数据与模板代码执行边界",
    "正文描述用户输入ERB表达式进入模板渲染，没有完整模板、环境或实际结果。\n\n离线自有模板比较作为普通变量输出和被编译成模板源码的路径，记录引擎、上下文、转义和无害算术标记。花括号、错误或只回显不是SSTI，静态模板/安全数据插值为反例；不执行系统命令或推断RCE权限。\n\n来源：[保存帖1](https://x.com/i/status/1498324305872318464)。"
  ],
  [
    "by-type/csrf.md",
    "CSRF 接管标题仍需浏览器凭据和状态绑定",
    "完整图只有CSRF导致ATO的P2 Triaged/仍评估状态；另一帖是RXSS窃取登录表单接管文章标题。没有跨站请求、凭据策略或会话结果。\n\n离线两个自有origin/账号比较浏览器发起、Cookie策略、Origin/token、受限动作与登录身份绑定。分诊标题、相同站点请求、需已有会话或服务端拒绝为反例；XSS能力和CSRF条件单独证明，不发送真实重置/登录请求或收集凭据。\n\n来源：[保存帖1](https://x.com/i/status/1498460984608014338)、[保存帖2](https://x.com/i/status/1499424800686624774)。"
  ],
  [
    "by-type/ssrf.md",
    "Java URL 的 url 前缀须按实际 JDK 解析",
    "完整代码先用^[a-z]+:检查scheme并只拒绝file；另一图JDK1.8.0_261的new URL(url:http://example.com)交HttpURLConnection GET读到Example Domain。这里只演示HTTP，不能把file URL直接强转同类连接后当已读取。\n\nOpenJDK8u URL构造器源码会先去空白并跳过不区分大小写的url:前缀，再解析真实协议；原始regex前缀与消费者不一致。离线只比较字符串检查、解析结果、有效协议与连接类型，不实际建网；非此版本、拒绝非HTTP或没有后续请求为反例，不推广所有Java/客户端。\n\n规范核对：[OpenJDK8u URL.java](https://raw.githubusercontent.com/openjdk/jdk8u/master/jdk/src/share/classes/java/net/URL.java)。\n\n来源：[保存帖1](https://x.com/i/status/1498629916337729536)。"
  ],
  [
    "by-type/file-upload.md",
    "polyglot 上传需要两个真实格式消费者",
    "正文声称始终使用polyglot且多数目标适用，没有文件、上传回应或浏览器/服务端解释结果。\n\n离线用无执行内容合成文件比较校验器与下游解析器对同一字节的识别、存储重命名、MIME、下载/展示路由。双格式名称、上传成功或只下载附件不是执行；校验与解释一致、无第二消费者为反例，不能保证多数上传存在漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1498649604090662914)。"
  ],
  [
    "by-type/idor-access-control.md",
    "bankVerificationStatus JSON 与可变更权限不同",
    "完整JSON有币种INR、测试银行/账号字段、active=false、bankVerificationStatus=1、isSystemAccount=false和空documentFileHandle，未保存POST、身份/所有权或实际变更。\n\n离线合成两账号将可见字段、对象归属、可写属性和验证消费者分开，比较被允许/拒绝写入及真实状态。枚举值1、字段可见、CSRFtoken出现或同一账号为反例；不要推银行已经验证/资金可操作，不复制真实token或账户值。\n\n来源：[保存帖1](https://x.com/i/status/1498659488701632514)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Osmedeus report done 与 installer 下载各自有限",
    "完整图有4.0.3历史更新、workspace flow done/fast26/26与各报告路径，以及premium/Linux64强制下载说明；未读报告对象、没有完整安装结果。\n\n离线记录具体版本、流程步骤、输出hash、成功/失败/跳过、重复目录与安装阶段；下载、done或输出文件名不能证明所有检查完成/无漏洞。缺结果断言、失败隐藏、私人包授权未知为反例，不下载/传播私有包或运行安装器。\n\n来源：[保存帖1](https://x.com/i/status/1498712190853193728)、[保存帖2](https://x.com/i/status/1498858180222218241)。"
  ],
  [
    "cloud/container-k8s-security.md",
    "空 Docker registry 匿名可见不等可利用写入",
    "正文称私人registry空且无需认证可上传，询问怎么利用，没有目录对象、push权限、镜像或消费者。\n\n离线自有registry权限矩阵分目录/manifest/blob读取、写入、标签更新和部署消费者，明确预期公开/私有。空列表、返回200和作者可上传说法不足以证明受限写入或执行；无实际对象/部署为反例，不上传镜像或修改真实registry。\n\n来源：[保存帖1](https://x.com/i/status/1498913816104431616)。"
  ],
  [
    "reporting.md",
    "多报告和重复状态不能替代独立根因计数",
    "完整图有Sony Medium5.3、Ubisoft混合P1/P3/P4 Triaged、NotApplicable、Duplicate、High Duplicate Closed、两P5 Informational及OAuth925支付。没有独立请求或根因。\n\n离线记录每份报告的资产、状态、根因、受影响对象与证据，分别计提交、确认、重复和奖励。奖励、作者8项说法、同一问题不同位置和严重性标签不能自动计8个独立确认；保持历史状态，不推广评级或补全漏洞链。\n\n来源：[保存帖1](https://x.com/i/status/1497033054510264320)、[保存帖2](https://x.com/i/status/1498944701923086340)、[保存帖3](https://x.com/i/status/1498956844047417348)、[保存帖4](https://x.com/i/status/1498977821993037826)、[保存帖5](https://x.com/i/status/1499023685809700864)、[保存帖6](https://x.com/i/status/1499294333685551104)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "CAPE 仪表盘容量指标不证明样本行为覆盖",
    "完整仪表盘显示任务/样本数、Top20、running3/pending0和时间/容量估算，没有单样本过程或检测证据。\n\n离线按样本哈希、配置、运行窗口、事件与观测缺口保存证据；队列完成、产品名称或无告警不等良性/全部行为已覆盖。未实际运行、短窗口、未触发条件为反例，不安装/运行存档恶意软件。\n\n来源：[保存帖1](https://x.com/i/status/1498995056019132420)。"
  ],
  [
    "by-type/authn-session.md",
    "重置 token 公共前缀不能证明可预测",
    "完整tip给两个32位十六进制示例，共享00000007前缀，其余部分明显不同；不足以支持只差末字符或下一token可猜。\n\n离线合成生成器分固定版本/分片字段、随机部分、用户/时间/事务绑定和失效，预测器必须用独立留出样本验证。公共前缀、两个样本、事后拟合或不同账号为反例，不尝试真实token或宣称已恢复随机种子。\n\n来源：[保存帖1](https://x.com/i/status/1499043105521213451)。"
  ],
  [
    "by-type/sql-injection.md",
    "Moodle 第二阶存储到 SQL 执行须分别留证",
    "完整MySQL图select mdl_badge_criteria_param返回field_lastname行，value含id条件及SLEEP(5)字串，本次select显示0.00sec。证明数据库存有文本，未显示下游查询执行或延时。\n\n离线合成两阶段模型记录首次输入/存储字节、取出路径、再次拼接与参数化对照，比较无害等值条件；时间证据还要控制噪声和重复。存储payload、字段名称或select输出不等第二阶SQLi，字面值/参数化或无下游为反例，不执行保存SQL/延时或读真实表。\n\n来源：[保存帖1](https://x.com/i/status/1499111160091529218)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Searpy 历史搜索输出与当前漏洞分开",
    "完整图是2020-09-14的Searpy2.3更新及Google inurl:php?id结果URLs，没有当前状态、范围或SQL执行。\n\n离线候选清单记录引擎、时间、query、输出/错误、分页/去重和归属。搜索命中、php参数、旧发行信息或缓存不证明当前漏洞/全部结果；不跑搜索脚本或访问真实候选。\n\n来源：[保存帖1](https://x.com/i/status/1499146181422768130)、[保存帖2](https://x.com/i/status/1499421736227737600)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "Gateway refresh 图片需补 route 写入与执行链",
    "完整图localhost:9000的POST /actuator/gateway/refresh带RewritePath表达式及Runtime open Calculator、HTTP200和计算器GUI；正文标CVE-2022-22947，没有此前route注册、真实部署和权限。\n\n离线状态模型分配置/版本、端点权限、route写入、refresh加载、表达式解析和进程身份，保留同一次无害标记与拒绝基线。200、GUI同屏、CVE名称和本机演示不能证明远程未认证通用RCE；未触发路由/表达式为反例，不执行表达式、注册真实路由或刷新网关。\n\n来源：[保存帖1](https://x.com/i/status/1499337806308524039)。"
  ],
  [
    "targeted-fuzzing.md",
    "Litefuzz help 的模式和后处理不能算崩溃",
    "完整help包含local/server/client、迭代/超时/mutator、crash/temp目录、minimize/superminimize、TLS/attach、postcmd、ReportCrash/memdump及禁用选项，没有crash样本和复现。\n\n离线自有fuzz计划绑定目标版本、最小无害输入、随机种子、迭代/时间预算、隔离与结果；区分网络/本地模式及后处理副作用。帮助选项、超时或目录存在不等漏洞，非确定复现/不同环境为反例，不attach进程、运行保存命令或触发真实崩溃。\n\n来源：[保存帖1](https://x.com/i/status/1499357635392552961)、[保存帖2](https://x.com/i/status/1499421855727636482)。"
  ],
  [
    "experiment-design.md",
    "Build Hack Fix Repeat 要保留业务不变量",
    "正文建议自行做注册、登录、用户/管理员与数据库练习再攻击、修复和重复，没有已测应用或产物。\n\n用自有离线小模型先声明身份/对象/状态不变量，再作单变量比较、观察结果、最小修复与回归负例。只是能登录、学会工具或一次修复不证明全系统安全；保留未知和每轮验证边界，不将练习成果自动映射真实目标。\n\n来源：[保存帖1](https://x.com/i/status/1499359462330880004)。"
  ],
  [
    "discovery/passive-and-services.md",
    "uncover 多引擎 IP 端口命中不能归并成同一资产",
    "完整图uncover0.0.1以jira字词给Shodan/FOFA/Censys结果，其中同IP不同端口及重复引擎记录；没有当前Jira响应、所有权或漏洞。\n\n离线保留每个IP/端口/协议、引擎、时间、查询和来源，明确按endpoint而非IP粗去重。索引命中、旧banner、共享IP或不同服务为反例；工具名称Perfect不证明覆盖，不自动把引擎集合当授权资产。\n\n来源：[保存帖1](https://x.com/i/status/1499380758791831557)。"
  ],
  [
    "scope-and-rules.md",
    "战时项目计数和 testing tag 仍须明确授权",
    "完整图是Ukraine相关项目views/reports/hackers计数与profile alt；另帖列third-party security testing字样。没有明确本次资产和行为许可。\n\n记录项目主体、规则版本、具体资产与动作范围，分个人动机、标签和正式授权；计数、旗帜、热度、同行参与或平台tag不是权限。未知归属/禁止行为为反例，不发起攻击或以战争主题推定许可。\n\n来源：[保存帖1](https://x.com/i/status/1499396449007640586)、[保存帖2](https://x.com/i/status/1499467903405473814)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "recon 管道覆盖和 tee overwrite 需要可复核计数",
    "完整管道聚合subfinder/amass/assetfinder、httprobe、wayback、hakrawler、paramspider并排除后缀；另一正文waybackurls和gau分别tee到同一文件可能覆盖，sort uniq-i可能合并大小写语义不同URL。\n\n离线集合对照每阶段输入/输出hash、追加/覆盖、错误、去重键、时间和归属，比较JSON/form/header、非标准端口、大小写与被过滤后缀。文件存在、静默空输出或只query参数不等全输入覆盖；保留来源与遗漏，不执行真实爬取/探测。\n\n来源：[保存帖1](https://x.com/i/status/1499399267890262031)、[保存帖2](https://x.com/i/status/1499701397939318793)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Proxy Everything 与拿到所有参数的说法有边界",
    "正文建议Burp全代理、Ctrl-R和获取所有参数，没有TLS解密条件、请求保留/过滤或结果。\n\n离线合成流量按浏览器/代理/接口、协议、可解密条件、身份和请求响应关联，记录未经过代理及被过滤数据。代理启动、页面可见或历史表有行不证明所有流量/参数已收集；缺JSON/header/动态流程为反例，不代理第三方私人数据或重放来源请求。\n\n来源：[保存帖1](https://x.com/i/status/1499400510302199808)。"
  ],
  [
    "by-type/xss.md",
    "CVE 单行 grep onmouse 不证明事件可执行",
    "正文给形状不完整的while read/curl --insecure /admin/module.php示例并grep onmouse后打印vulnerable，没有响应上下文、CSP或浏览器结果。\n\n离线合成响应比较同词在文本/编码/属性的情况，记录状态、TLS错误、输入反射、实际DOM及无害事件。关键词、CVE标签、命令打印或无消费者为反例；语法错误/隐藏失败不能计命中，不执行保存循环或关闭真实TLS检查。\n\n来源：[保存帖1](https://x.com/i/status/1499460421165940736)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "taser Spider 与 uro 的过滤损失须量化",
    "完整taser图从subdomain经httpx和xargs-P10 PythonSpider，再正则抽JS并把错误重定向/dev/null，结果含/maps/api/js和chunk.js；正文uro删除boring/duplicate。\n\n离线合成页面比较相对URL、query/hash、动态加载、非.js路径与后缀过滤，记录工具版本、并发、超时和错误。匹配样例不等抓全JS；静默错误、语义不同URL被压缩、API/js路径漏掉为反例，不安装来源包或运行Spider。\n\n来源：[保存帖1](https://x.com/i/status/1499489808032612352)、[保存帖2](https://x.com/i/status/1499519998234034176)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "CVE critical 和 readme 命中仅是扫描线索",
    "完整Nuclei图片只有CVE-2020-35489/http/critical及contact-form-7/readme.txt路径，没有请求、响应、实际版本和触发漏洞。\n\n离线模板对照精确版本条件、路径响应、否定样例与真正漏洞消费者，分fingerprint和确认。readme可见、组件名称、critical标签或过宽匹配为反例；版本陈旧文件不自动等已部署版本，不在线发起验证或执行漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1499524650891714562)。"
  ],
  [
    "discovery/web-and-api.md",
    "vhost Host authority 格式和状态码不能混同",
    "正文ffuf把http://FUZZ放进Host并按多个状态码保留，没有完整交换和服务内容。Host authority和URL不是同一输入格式。\n\n离线自有路由比较合法host[:port]、未知Host、绝对URL字段、SNI和不同backend，记录响应体/内容身份。200、默认站点、400、缓存或不同对象为反例；需要实际虚拟主机内容与范围，不用候选名单扩展授权或测试第三方站点。\n\n来源：[保存帖1](https://x.com/i/status/1499608441840541701)。"
  ],
  [
    "by-type/authn-session.md",
    "重置管理员标题的用户详情 GET 不构成重置证据",
    "完整图只有GET /rest/user/view/54191、遮蔽BEARER TEMP token与同站Origin/Referer，未保存响应、重置提交、被选身份或新会话。\n\n离线两自有账号分详情读取、临时token用途、重置事务、目标账号绑定、交付/提交和最终身份；分别比较正常/非所有者/失效token。请求头或用户ID存在不等越权，标题/截图不能补全管理员重置链，不复制token或调用真实接口。\n\n来源：[保存帖1](https://x.com/i/status/1499665391823384577)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "OCR Recon 的 success timeout 与语义提取分开",
    "完整终端以Sign关键词运行OCR Recon，显示www.amazon.com success与youtube timeout，没有图像、识别文字、坐标或页面类别。\n\n离线自有截图把采集成功、图像hash、OCR文字/置信度、区域、关键词匹配和业务语义分阶段记录，人工核误识别。成功日志不等已识别登录/敏感内容，超时不能计负例；无图片/输出或字形误读为反例，不运行真实网站OCR采集。\n\n来源：[保存帖1](https://x.com/i/status/1499719989389144073)、[保存帖2](https://x.com/i/status/1499730637103964161)。"
  ],
  [
    "discovery/passive-and-services.md",
    "SQLi tale 的被动资产清单与注入确认分开",
    "保存正文第一部分描述根域、收购关系、Wiki/Crunchbase/WHOIS和子域工具，未保存SQL查询、错误或注入响应。被动发现阶段不能从SQLi系列标题继承漏洞结果。\n\n离线候选图保留来源/时间、公司与域关系、当前所有者及范围；工具输出与当前可用服务分别验证。收购旧资料、共享基础设施、历史WHOIS或无权限资产为反例，不把公司关系自动扩成测试许可，也不声称未保存后续章节已读。\n\n来源：[保存帖1](https://x.com/i/status/1496217791976054784)。"
  ],
  [
    "impact-and-acceptance.md",
    "Android Server Status 奖赏标题不能继承接管影响",
    "保存手机快速P4正文与完整图是Apache Server Status、via127.0.0.1、Unresolved/accepted valid issue和历史VRT1.10.1。没有端点交换、访问主体、敏感字段或0click接管链。\n\n离线合成服务状态页分别核预期公开、认证、调用者、返回字段及是否含非公开业务数据，比较正常/非授权主体。赏金、移动设备、localhost说明或分诊状态只支持历史个案；无受限信息/无跨身份结果为反例，不能推ATO或固定评级。\n\n来源：[保存帖1](https://x.com/i/status/1496099083521785857)。"
  ],
  [
    "impact-and-acceptance.md",
    "Meta 图片视频项目的奖励门槛只适用于所述上下文",
    "完整回信称已知多个报告低于该项目奖励门槛，并说明只涉图片/视频、项目关闭且未写敏感XSS影响。没有实际执行链或当前政策。\n\n离线报告矩阵分执行读者、资产资格、数据敏感性、允许动作、已知/重复与影响证据；把具体项目资格与技术可复现性分开。低于奖励门槛不等所有XSS无效；其他项目、敏感对象或不同读者为反例，不把历史回信当通用评级或当前scope。\n\n来源：[保存帖1](https://x.com/i/status/1498590020055465992)。"
  ]
]
ids={pid for row in json.loads((W/"batch-0123.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert len(urls)==115 and all(pid in ids for pid in urls)
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

