# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "by-type/file-upload.md",
    "polyglot 的外观、格式和消费者判断",
    "正文把polyglot定义为看似A而实际也符合B的文件，视频正文未保存。表面后缀、声明MIME、解析结果与最终消费者应分开。\n\n自有无害合成文件静态记录两格式边界、验收器与存储/访问路由，比较单格式、畸形文件和安全消费者。只有名称/MIME、B被拒、仅下载或没有解释器为反例；多格式成立不自动是代码执行，不加载未存外部PoC。\n\n来源：[保存帖1](https://x.com/i/status/1484143681598889995)。"
  ],
  [
    "by-type/ssrf.md",
    "Collaborator 多面板 DNS 事件的关联键",
    "自建Collaborator帖子图是五个客户端面板的DNS查询/payload/时间，没有HTTP正文或真实触发主体。另帖Log4j canary回调求助、XSSHunter邮件仅截断fired标题。\n\n每个自有离线实验输入保留唯一标记、位置、时间、DNS/HTTP阶段及真实执行者，区分服务端、浏览器、triager与重放。共享标记、延迟/未归因、只有DNS/通知或无消费者为反例；回调不证明代码加载/敏感影响，不联系或重放真实目标。\n\n来源：[保存帖1](https://x.com/i/status/1484160827418677259)、[保存帖2](https://x.com/i/status/1485218540752076800)、[保存帖3](https://x.com/i/status/1485516963292057605)。"
  ],
  [
    "discovery/passive-and-services.md",
    "常见端口表与实际服务识别的距离",
    "图给FTP20/21、SSH22、Telnet23、SMTP25、DNS53、HTTP80、POP3 110和HTTPS443，只是常见服务关联，不包含某个目标的探测。\n\n在自有静态服务清单分别记录协议、实际监听端口、banner/版本和部署归属，比较非标准端口/代理映射/伪banner。只有端口号、不同服务占用、转发层或历史关联为反例；端口开放不等于服务存在、版本受影响或测试许可。\n\n来源：[保存帖1](https://x.com/i/status/1484186075807752195)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "LFI 重复 dot、双编码和分隔符的消费者",
    "完整图给重复dot、双URL编码、%00与%5C变体，并自注sometimes且不知原因，没有保存实际读取交换。\n\n静态追入口→每次decoder→过滤/拼接→OS路径解析→文件loader/权限；自有合成路径比较普通、缺失、安全拒绝和编码变体。未再解码、OS不认分隔符、零字节被拒或文件受限为反例；字符串清单不是万能过滤绕过，不读系统文件。\n\n来源：[保存帖1](https://x.com/i/status/1484239130435661824)。"
  ],
  [
    "by-type/csrf.md",
    "OAuth 注册分支移除当前密码后的改密保护",
    "完整正文说普通改密要求当前密码，OAuth注册后同动作不用当前密码并声称CSRF，没有保存跨站请求和持久化结果。\n\n用自有合成账户分别记录两注册分支、会话与改密合同，静态核token/Origin/SameSite/请求格式和重认证；最小比较正常/错来源/缺token/不满足重认证，持久化能力独证。仅表单不显示密码、另一防御生效、浏览器未送凭据或未改变服务器状态为反例，不改他人密码。\n\n来源：[保存帖1](https://x.com/i/status/1484414294842556418)。\n\n语义校核：[OWASP CSRF 防御](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)。"
  ],
  [
    "by-type/idor-access-control.md",
    "权限清单必须拆成主体、对象和动作",
    "图片清单并列path traversal、authorization schema、vertical/horizontal、missingauth与IDOR；另外只有低权限附件accepted标题。\n\n以自有两个主体/两角色建立对象所属与动作合同，固定会话/请求位置，对照本人合法、同角色他对象、低角色高动作和缺身份。路径可达、公开设计、仅标题或正常拒绝为反例；清单打勾不等于发现，随机ID/文件路径不是授权机制。\n\n来源：[保存帖1](https://x.com/i/status/1484447103216599040)、[保存帖2](https://x.com/i/status/1484433708744847360)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Burp 参数筛选会隐藏非参数对象入口",
    "资源帖实际图框出HTTP history的Show only parameterized requests，框内未勾；正文链接未保存。path/header/cookie和升级连接消息也可承载对象信息。\n\n保存捕获全集与筛选配置，离线自有请求集合比较显示和隐藏项，分别核path、query、body、headers、cookies、消息的主体/对象/动作。未勾、仅视觉框、缺响应、过滤后剩余列表或没有某类请求为反例；显示范围不等捕获覆盖，更不等权限测试完成。\n\n来源：[保存帖1](https://x.com/i/status/1484477220491915264)、[保存帖2](https://x.com/i/status/1486647673981603842)。"
  ],
  [
    "expert-reasoning.md",
    "Wireshark 描述与 Tenable 菜单不对应",
    "两正文介绍流量关联TI/资产/漏洞插件，唯一新图片却是Tenable Vulnerability Detail/List/Summary菜单，缺插件实现和原始流量。\n\n记录材料的产品/版本/来源对应，再分观察流量、关联标签、假设和确认，用自有合成流量核字段映射。错图、仅菜单、历史TI或共享IP标签为反例；不能将另一工具UI补成插件已运行或当前漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1484514794988261382)、[保存帖2](https://x.com/i/status/1484516023890235394)、[保存帖3](https://x.com/i/status/1484998005166125064)。"
  ],
  [
    "by-type/xss.md",
    "Shopify HTML 编辑器未保存状态的执行边界",
    "正文称admin/product XSS resolved/high/1000，图为Unsaved changes编辑器中的img事件属性，没有显示保存成功、DOM执行或另一主体读者。\n\n自有静态fixture分输入编辑、存储、预览/后续读者、浏览器事件和CSP；正常文本、安全编码/拒绝和真正节点各留证据。未保存、源码编辑显示、本人主动执行、无后续读者或策略阻断为反例；奖励状态不替代服务器/浏览器链，cookie表达式不等于HttpOnly泄露。\n\n来源：[保存帖1](https://x.com/i/status/1484554895399157763)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "proc、home 用户路径与挂载的读权限",
    "完整清单有cmdline/mounts/sched_debug/motd/mysql配置、home用户history/SSHkey，另一帖列cwd源码、net视图/environ及K8s serviceaccount。\n\n静态区分文件/目录、PID/用户/容器namespace、挂载、当前路径和loader权限；自有无敏感目录用普通/缺失/拒绝对照。未挂载、错误用户、目录当文件、读权限不足或不同namespace为反例；清单不证明任意文件读或集群控制，不读取真实key/环境/票据。\n\n来源：[保存帖1](https://x.com/i/status/1484560911562117121)、[保存帖2](https://x.com/i/status/1487331595686084608)。"
  ],
  [
    "by-type/waf-bypass.md",
    "self 注释、iframe 训练和 top 属性解码",
    "正文保存self/bracket/comment编码、iframe+/ON/onload及top属性hexescape对照；图WAF Tester明确globalHTML/attribute、单context限制，另一图只有alert。\n\n静态保留URL→HTML/entity→JS解码、原反射上下文/事件、真实CSP、版本与实例；自有无外联fixture只变一层。训练消费者、不同站点、错误语法、console/self执行或缺原始交换为反例；一张alert不证明当前所有Cloudflare配置可绕过，不运行归档载荷。\n\n来源：[保存帖1](https://x.com/i/status/1484813141087162370)、[保存帖2](https://x.com/i/status/1485019050602381318)、[保存帖3](https://x.com/i/status/1485766633704812545)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "extensive 与 quick CIDR 工作流的覆盖差异",
    "完整YAML图extensive/general/domain有subdomain→probing→screenshot→sto/fingerprint→spider/archive/ipspace→vulnscan，并extensive分支portscan/dirbscan/pvulnscan；quick CIDR/cidrfile/forceparams固定HTTP端口子集，只portscan/screenshot/vulnscan/dirb。\n\n静态核类型/validator、分支/产物依赖、预算/失败和选择的端口集，离线输入/空结果/未运行对照。模块定义、启动、子集遗漏或缓存为反例；quick不等全端口，flow不代表完成，不执行扫描。\n\n来源：[保存帖1](https://x.com/i/status/1484819211755343874)。"
  ],
  [
    "targeted-fuzzing.md",
    "Pwndora 扫描范围、超时和端口子集",
    "CLI图start/end IPv4、range文件、threads默认50、socket timeout0.5、top20与all1000、HTTP screenshot及Wappalyzer更新，没有运行结果。\n\n静态核实际输入归属/当前许可、端口集/协议、超时与退出/产物字段，离线对照慢服务/空输入/模块失败。帮助页、超时漏检、只截图或端口子集为反例；all标签不必是65535端口，更不是漏洞数，不安装/启动全网扫描。\n\n来源：[保存帖1](https://x.com/i/status/1484862019278979072)。"
  ],
  [
    "by-type/info-secrets.md",
    "Postman 搜索、contact JS 与 Algolia 标识",
    "图建议公共Postman按scope域搜索，但所示只是example/RAML/demo；正文另说contact JS可能SMTP秘密和AlgoliaAPPID/APIKEY，未存实际材料权限。\n\n静态记录出处/环境/预期公开、材料类型、所属服务/消费者与声明动作，以自有合成公开/受限字段作对照。示例、公开应用ID、搜索用途材料、无有效期/权限交换或另一归属为反例；字符串不等可用秘密，不发SMTP邮件/使用真实key。\n\n来源：[保存帖1](https://x.com/i/status/1484868458403835904)、[保存帖2](https://x.com/i/status/1485482902070566914)、[保存帖3](https://x.com/i/status/1486300884581892099)、[保存帖4](https://x.com/i/status/1484392365125079041)。"
  ],
  [
    "by-type/authn-session.md",
    "六项 OTP 清单中的客户端和服务端边界",
    "正文两列表把响应/状态改写、码泄露、JS分析、复用与限速同称bypass；图仅401 InvalidOTP/successfalse。真正被保护的是服务端因子完成与后续动作。\n\n自有合成状态静态分码发行→主体/会话/动作绑定→过期/一次性→验证→能力，比较正常/错码/过期/复用/仅改UI。只有状态200/true、可见字段、缺rateUI或服务端仍拒绝为反例；不发OTP或猜码，缺限速的影响独证。\n\n来源：[保存帖1](https://x.com/i/status/1484882978337542145)、[保存帖2](https://x.com/i/status/1485614599991078915)、[保存帖3](https://x.com/i/status/1485927217289117696)。"
  ],
  [
    "scope-and-rules.md",
    "DoD header 接收口号与默认密码速查",
    "两帖说DoD只接受server在header，repo图只有简介；默认凭据repo和大公司允许bruteforce/P2高奖泛称也无当前政策。\n\n记录目标项目/资产/动作、政策版本、受理条件与安全预算，当前任务独立核许可和真实消费者；离线材料只分类发现/认证/影响。历史口号、header指纹、公司规模、密码表或奖励故事为反例；不把它们当统一准入/等级/猜密许可。\n\n来源：[保存帖1](https://x.com/i/status/1484912758126743553)、[保存帖2](https://x.com/i/status/1484995368333234176)、[保存帖3](https://x.com/i/status/1485243318233538560)、[保存帖4](https://x.com/i/status/1486232802341367810)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "Grafana 原始 request-target 含井号的层级差异",
    "保存Raw HTTP/2图的plugins/welcome路径确含literal #及dot段，响应200有passwd字段。浏览器URL fragment通常先分离；原始HTTP工具发送的字节需要独立处理。\n\n静态记录浏览器/工具入口、实际request-target、各代理/应用规范化、插件版本/权限和响应来源，自有合成路径与正常/缺失/拒绝比较。浏览器未送fragment、纯回显、教程/缓存、未知层或无真文件对应为反例；不能把原始图推成浏览器通用NGINX400绕过，不读取系统文件。\n\n来源：[保存帖1](https://x.com/i/status/1484946505576423430)。\n\n语义校核：[RFC 3986 fragment](https://www.rfc-editor.org/rfc/rfc3986)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "XSS、任意写和 Laravel 标签到 RCE 的缺口",
    "XSS→RCE图只indexphpalert1，Meta预告明确任意写转RCE是应用特定，LaravelIgnition图仅low报告列表和maybeRCE。它们没有完整执行消费者。\n\n静态分脚本上下文、文件内容/落点/权限、加载/解释器/启动消费者及实际进程能力；自有无害离线标记逐段比较。只有alert、写文件标题、组件/模板名、无可达消费者或限制有效为反例；不拼出未存链，不写真实文件/执行代码。\n\n来源：[保存帖1](https://x.com/i/status/1485081757884076038)、[保存帖2](https://x.com/i/status/1485991571854090251)、[保存帖3](https://x.com/i/status/1486814974433394689)。"
  ],
  [
    "by-type/sql-injection.md",
    "二阶 SQL 的空白页面与错误差异",
    "正文仅线程1说应用二阶blindSQL页面始终空白，只有查询错误时不同，未保存发行/存储/二次查询交换。\n\n自有合成fixture分别绑定初始输入、持久化值、后续消费者、会话/时间，比较普通/格式错误/安全绑定/实际查询差异；记录失败和事务状态。空页面、一次异常、未存值、无二次语法消费或并发干扰为反例；空白不等于无副作用，也不证明数据库控制，不执行归档SQL。\n\n来源：[保存帖1](https://x.com/i/status/1485099754921017353)。"
  ],
  [
    "by-type/info-secrets.md",
    "Symfony Profiler 的路径、变量与配置文件",
    "正文说debug/profiler enabled，实际图参数路径下ExceptionController/200/headers及phpinfo服务器变量，数值多遮蔽。请求路径与真实配置文件正文不同。\n\n静态登记实例/版本、预期读者、可见字段及模板，离线合成普通/缺身份/受限访问对照。仅200、路径名、phpinfo环境键、被遮蔽值或正确权限为反例；debug线索不证多漏洞或有效凭据，不取得真实配置/环境。\n\n来源：[保存帖1](https://x.com/i/status/1485111531478028288)、[保存帖2](https://x.com/i/status/1485581428847169540)。"
  ],
  [
    "scope-and-rules.md",
    "平台注册清单和 HoF 的历史契约",
    "平台图按公开注册/邀请列网站，是历史分类；FlexLists HoF图明确无bounty并列排除项，NoRateLimit标题没有因子/动作证据。\n\n记录项目/账户资格/资产/允许动作、政策时间和受理/奖励/表彰各自条件，自有离线归类将scope与结果分开。历史名单、能注册、HoF名字、邀约或排除项为反例；表彰不保证奖金，平台准入不授予任意资产测试许可。\n\n来源：[保存帖1](https://x.com/i/status/1485184073039589378)、[保存帖2](https://x.com/i/status/1487045205320617987)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "S3 链接、unclaimed 标题与资源接管",
    "正文只建议检查所有S3链接，200奖励邮件题名unclaimed bucket on login页，没有实际引用、归属、注册可能/控制后的消费证据。\n\n静态绑定页面/资源URL/时间/owner及当前scope，分不存在、可列、可读、可写/注册、被应用消费；自有合成资源只核引用与安全拒绝。只有名字/错误/奖金、第三方bucket、受限注册或无消费为反例；不claim或写真实资源，不把S3链接算takeover。\n\n来源：[保存帖1](https://x.com/i/status/1485191930480939011)。"
  ],
  [
    "source-audit.md",
    "git 与 svn 清单中的元数据和源码区别",
    "完整词表包含HEAD/index/logs、attributes/config/keep/modules/review及svn entries/ignore，另一帖仅git/svn/env，报告1/2还要求客户/用户影响。\n\n静态分目录、仓库元数据、项目正文/对象、配置及预期读者，用自有无秘密样本核实际返回字节和关联关系。软200、空占位gitkeep、公开源码、受限对象或无业务能力为反例；文件名不证明完整仓库/秘密，不批量恢复源码或使用密钥。\n\n来源：[保存帖1](https://x.com/i/status/1485196354930737152)、[保存帖2](https://x.com/i/status/1485503260744372227)、[保存帖3](https://x.com/i/status/1487590646491717634)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "Second-Order depth 与 ripgen 生成候选",
    "help图SecondOrder depth1/threads10/repeat headers/insecure/output/target，ripgen卡片domainpermutation，Freshdesk只有signupform。候选生成/爬取/资源绑定是不同阶段。\n\n静态保存源/时间/参数、解析/服务归属、当前policy和第三方资源生命周期，离线合成正常/缺失/受限注册对照。help、排列名称、免费试用表单、TLS绕检或无受害域消费为反例；不注册/claim资源，不将千域标题当已证接管。\n\n来源：[保存帖1](https://x.com/i/status/1485224388656050178)、[保存帖2](https://x.com/i/status/1485273686852907011)、[保存帖3](https://x.com/i/status/1485637558381989890)、[保存帖4](https://x.com/i/status/1485893949743312896)。"
  ],
  [
    "reporting.md",
    "curl 转换 PoC 时保持交换语义",
    "图片curlPOST XMLRPC/ContentType/data转Python requests.post，另有logo；转换界面没有执行/响应结果。\n\n静态逐项核method/URL/query、原始body字节、编码、headers、身份和新客户端redirect/TLS/timeout默认，脱敏合成交换最小对照。只是语法生成、字节变化、会话缺失、默认跳转或未存响应为反例；可运行样式不等可复现，避免发布真实token/执行归档代码。\n\n来源：[保存帖1](https://x.com/i/status/1485279198516293636)、[保存帖2](https://x.com/i/status/1484523522387066890)。"
  ],
  [
    "source-audit.md",
    "Whatfiles 和 FACT 的观察权限与采集收据",
    "Whatfileshelp新命令或attachPID须root、log/stdout/debug；FACTUI targets/UUID/disks/partition/mount/collectedtime及capture/ingest按钮。它们描述取证能力和已有采样状态。\n\n静态绑定主体/权限、PID/主机/namespace、时间、产物哈希与完成收据，离线合成日志比较缺事件/不同进程/失败。按钮、help、旧时间、未采内容或无来源为反例；工具能力不证漏洞/任意读，不安装/attach进程/采真实内存磁盘。\n\n来源：[保存帖1](https://x.com/i/status/1485375308127780865)、[保存帖2](https://x.com/i/status/1485385767363149827)、[保存帖3](https://x.com/i/status/1485949205613002756)。"
  ],
  [
    "by-type/idor-access-control.md",
    "email UserProfile 与随机 username 回退的比较",
    "完整正文称枚举email再读取profile，图GETUserProfiles带Authorization并返回多字段；另一帖username null→xyz得到随机profile，缓存只是作者疑问。\n\n仅自有A/B合成profile固定身份、对象、时间与请求关联，比较合法/错主体/不存在/重复输入，区分枚举、对象授权、字段披露、缓存和默认回退。公开字段、样本不足、缓存未证或正确服务器拒绝为反例；随机返回不自动IDOR，不列举真实用户/PII。\n\n来源：[保存帖1](https://x.com/i/status/1485405269563940865)、[保存帖2](https://x.com/i/status/1485784071636725767)。"
  ],
  [
    "expert-reasoning.md",
    "ffuf 必用与详细解释的验证关系",
    "正文alwaysffuf及理解core/不用花哨one-liner建议，只是方法取向，无实际端点/结果。\n\n从输入结构、消费者、身份/对象/状态与预算选择最小实验，记录原始交换、工具参数/版本和失败。工具名、执行时间/奖金、规则列表或无消费者为反例；自动化可发现候选，机制解释和对照仍是确认依据，不能保证5秒P1。\n\n来源：[保存帖1](https://x.com/i/status/1485264361560363008)、[保存帖2](https://x.com/i/status/1485531015619645440)、[保存帖3](https://x.com/i/status/1485540662833336321)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Twitter 和 BlackHat 资料检索的可信度",
    "图保存list/min_faves/filterlinks/SSRF/Latest查询样式，正文BlackHat site/intext/topic/filetypepdf；YouTube概览声称快速critical，没有实际漏洞链。\n\n静态记录资料来源/年份/保存范围与候选架构/功能，当前系统另核部署/角色/允许动作；离线样本对比历史/示例/失效资料。热度/排序、媒体概览、相似UI或标题为反例；资源发现不证明当前漏洞，不发消息或补写未存外链全文。\n\n来源：[保存帖1](https://x.com/i/status/1485957126174523393)、[保存帖2](https://x.com/i/status/1486064572330954752)、[保存帖3](https://x.com/i/status/1486345178755788802)。"
  ],
  [
    "discovery/web-and-api.md",
    "Http2Smugl help 到协议转换边界的距离",
    "图help仅detect/request/completion/connect-to/timeout10s，正文说H2→H1转换可导致smuggling，另一帖只是相同工具链接。\n\n静态分客户端H2消息、转换层H1序列、后端边界/连接复用和实际响应归因，用自有离线合成序列比较一致/不一致解析及未复用连接。help、超时、单请求异常、无转换证据或相同边界为反例；工具detect标签不能代替desync证据，不向真实服务发送走私请求。\n\n来源：[保存帖1](https://x.com/i/status/1485722809653469186)、[保存帖2](https://x.com/i/status/1486967991665369089)。"
  ],
  [
    "source-audit.md",
    "GET map 控制 array_map 的 callable",
    "完整PHP图input来自GET map，再array_map(input,[0,23,454,234])。可控制的是callback名字，调用参数仍由固定数组给出。\n\n静态核callback是否存在/可调用、签名/参数类型、版本/禁用配置、可达权限与副作用；自有纯数据映射用允许/不允许/不存在名字比较。正确allowlist、签名不匹配、固定值不能满足危险操作或不可达为反例；callback选择不自动等于任意命令控制，不运行归档PHP。\n\n来源：[保存帖1](https://x.com/i/status/1485782487917686784)。\n\n语义校核：[PHP array_map](https://www.php.net/manual/en/function.array-map.php)。"
  ],
  [
    "by-type/authn-session.md",
    "任意收件人 OTP 数量与身份完成分层",
    "完整正文求给任意email含未注册者无限发OTP定级，另一帖NoRateLimit HoF和大公司bruteforce口号都缺实际验证。\n\n静态分发行/收件人合同、注册状态披露、消息成本/预算、限速维度及验证/一次性绑定，自有合成事件比较发行拒绝和身份仍未完成。只无UI限制、无发送计数/成本、未认证或政策禁止为反例；发送量不等OTP绕过/固定P2，不发真实OTP/刷消息/DoS。\n\n来源：[保存帖1](https://x.com/i/status/1485980345350897669)、[保存帖2](https://x.com/i/status/1486232802341367810)、[保存帖3](https://x.com/i/status/1487045205320617987)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "弱候选保留状态不预先证明连链",
    "正文建议记录selfXSS等暂时不能利用的候选，以便后来寻找连接。长期保存的只是带前提的假设。\n\n记录输入/消费者、主体/环境/时间、当前限制和最小反例；有新材料才独立核下一消费者与状态变更，保持原证据。学习新技巧、相邻标签、失效前提、不同实例或无权限桥为反例；不能预定每个selfXSS都可升级，不为连链扩大授权范围。\n\n来源：[保存帖1](https://x.com/i/status/1486034319227428866)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "api file 的 path 与 type 提示不是读取证明",
    "正文链接显示api/file?path=config/products/crystals/ruby.jpg&type=image/jpg并问问题，未保存请求/响应或loader实现。\n\n静态区分用户path、类型声明、基址拼接/规范化、包含性与文件权限，用自有合成普通/缺失/拒绝路径比较实际字节/消费者。只是jpg参数、纯反射、固定合法资源或正确包含性为反例；type=image不证明内容验证，也不证明路径遍历，不取真实文件。\n\n来源：[保存帖1](https://x.com/i/status/1486073951205965828)。"
  ],
  [
    "by-type/xss.md",
    "POST XSS 加 CSRF 不自动成为 stored",
    "完整正文写POSTXSS=P5、加CSRF=storedP3，图只是triaged/stillassessed标题。跨站送入与保存后新读者消费是两个不同边界。\n\n自有静态fixture区分请求方法、浏览器携带凭据/来源验证、服务器存储、后续渲染/读者和CSP，分别比较正常/拒绝与真实持久化。仅POST、回显、无存储读者、CSRF被拒或自执行为反例；不能用公式定stored或统一等级，不向他人账号写入。\n\n来源：[保存帖1](https://x.com/i/status/1486089011823357965)。"
  ],
  [
    "source-audit.md",
    "PTY、TERM 和 stty 改变交互而非权限",
    "完整正文给pty.spawn、TERM、挂起/stty raw/fg序列，未保存环境/控制流或执行结果。PTY分配、终端模式和远端身份能力不同。\n\n静态记录既有会话、本地/远端终端、作业控制与输入输出模式，离线合成状态比较有/无PTY及终端恢复。命令文字、未有控制终端、不同shell环境或仅本地模式为反例；交互改善不证明初始入口/提权，不运行shell/改真实终端状态。\n\n来源：[保存帖1](https://x.com/i/status/1486090754858573828)。"
  ],
  [
    "by-type/sql-injection.md",
    "SQL 百分之百口号与完整 alt 的类型变体",
    "正文及有意义alt保留引号/反引号/反斜线/注释、q[]/q=[1]、OR、括号、函数样式等变体，图仅SQL封面。输入类型变更与查询语法改变不是一回事。\n\n自有合成查询静态追URL解析/数组或标量、框架类型转换、SQL绑定和真实语法位置，比较普通值/格式错误/安全参数化及最小无敏感标记。应用校验/报错、空白、反射、类型拒绝或绑定有效为反例；不存在100%保证，不执行归档条件或枚举数据库。\n\n来源：[保存帖1](https://x.com/i/status/1486145250728955906)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "subjs 双 tee、uniq 与跨域资源证据",
    "完整管线subjs后两次tee写同一js_url、uniq及stderr重定向，图实际列分析/营销/CDN资源和带query版本JS；另一帖bash后写HTTP脚本名，实际JSFScan图是本地启动和19/19links/LinkFinder队列。\n\n静态核输入/输出契约、每个写者顺序/截断风险、相邻去重与源/失败留存，按父页、资源host和当前scope分别关联。并写覆盖、非邻重复、第三方脚本、队列未完成或URL当脚本文件为反例；列表/进度不等秘密发现，不执行管线。\n\n来源：[保存帖1](https://x.com/i/status/1486264317104304131)、[保存帖2](https://x.com/i/status/1487162313073381381)。"
  ],
  [
    "by-type/info-secrets.md",
    "AWS 数据库标题与 SSH 日志图的字段归因",
    "帖子标题千开放AWS数据库/RCE/K8s，图却Kibana sshd invaliduser/kex/closed日志，process.cmd部分accepted不等认证成功。\n\n静态核真正数据源、字段语义、读者/身份/时间和实例，离线合成日志比较进程状态与认证事件/受保护能力。只有accepted进程标签、失败日志、错图/不同主机或标题为反例；可见日志不推出数据库开放/SSH控制/RCE，不查询真实日志或复制敏感值。\n\n来源：[保存帖1](https://x.com/i/status/1486262346867933186)。"
  ],
  [
    "by-type/info-secrets.md",
    "file hosts 地址与 PHP DB 定义的对应缺口",
    "图片地址栏写file:///etc/hosts但页面展示PHPheader/DBdefine/include，值全部遮蔽，正文只有不披露感叹。\n\n静态绑定实例、requesttarget/loader和响应源，分别比较文件类型、预期读者及字段类别，自有合成内容核对应关系。地址和正文不对应、redaction、教程/缓存、无真实字段为反例；不能从DB_PASSWD键名认有效秘密或任意读，不尝试真实配置/凭据。\n\n来源：[保存帖1](https://x.com/i/status/1486312854454431753)。"
  ],
  [
    "discovery/web-and-api.md",
    "WebSocket 握手和消息生命周期的覆盖",
    "正文指出WebSockets与HTTP不同、工具支持较少和规模发现困难，外部talk后续未存。仅HTTP列表可能遗漏消息消费者。\n\n静态记握手身份/Origin/路由、连接状态、消息类型/对象与动作，离线自有两主体/断线重连/错对象对照，核服务端每动作权限。只有101、浏览器UI、未发消息、预期公开或每动作验证有效为反例；升级成功不证明消息权限突破，也不把同一连接身份当永久授权。\n\n来源：[保存帖1](https://x.com/i/status/1486402304844652545)。"
  ],
  [
    "by-type/ssrf.md",
    "vCenter header 端口对照的连接消费者",
    "两图同GET vropspluginui getvcdetails且带session/多个headers，vcIP一图127.0.0.1:22返回500/UnrecognizedSSLplaintext，另一127.0.0.1:2返回Connectionrefused。原始堆栈指向HTTP/TLS连接消费。\n\n静态固定身份/路由/headers，仅在自有离线fixture比较受控端口的拒绝/协议不符/正常响应，记录错误层级/时间及来源。模板错误、不同会话、cachederror、未达网络或无真实源为反例；连接差异不证明读数据/元数据/RCE，不重放session/扫描端口。\n\n来源：[保存帖1](https://x.com/i/status/1486582542807420928)。"
  ],
  [
    "hunting-strategy.md",
    "复杂功能先拆合同而非按复杂度判漏洞",
    "正文建议复杂站先用access/logic/auth强项建立信心，另一条直接complex=lesssecure。复杂度只影响研究成本，不直接给漏洞结论。\n\n静态拆主体/角色、对象/动作、状态转换、输入消费者和依赖，按当前scope与预算选最小对照，记录覆盖/失败。UI复杂、业务分支多、正确权限/事务或缺实际差异为反例；经验取向不保证高奖，不跳过消费者证据。\n\n来源：[保存帖1](https://x.com/i/status/1486584059358711810)、[保存帖2](https://x.com/i/status/1487457761784913921)。"
  ],
  [
    "by-type/idor-access-control.md",
    "IDOR 入口比例不能当当前漏洞概率",
    "正文列REST/query/body/GraphQL/PUT/header/cookie/querylanguage，图REST31.8%、GET25.8%、POST21.2%、GraphQL9.1%等，没有样本分母，类别也可能重叠。\n\n作为输入覆盖目录逐项追主体-对象-动作与服务器权限，离线自有多入口比较相同对象的合同。统计/标签、参数位置、公开资源、统一权限拒绝或缺分母为反例；不能按图推当前发生率或把不同入口都算独立漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1486647673981603842)。"
  ],
  [
    "reporting.md",
    "Abuse Risk 分流和奖励资格分开记录",
    "Googlebot通知identifiedAbuseRisk/triagedTrustSafety，并说稍后回应；它描述处理队列，不提供漏洞机制、最终受理或奖金承诺。\n\n报告状态分别记接收、分流、技术复现、修复/回归、资格和支付的来源/时间/条件，离线自有记录比较不同状态。机器人邮件、triaged标签、等待时长、不同计划或未有决定为反例；不能由TrustSafety转送判断必有bounty，不发消息/替用户填表。\n\n来源：[保存帖1](https://x.com/i/status/1486685976676257797)、[保存帖2](https://x.com/i/status/1487085998962262017)。"
  ],
  [
    "experiment-design.md",
    "Burp 仍开启与页面等待的诊断顺序",
    "meme把页面不加载归因BurpProxy仍开，没有实际网络日志。代理启用、拦截等待、连接/TLS和服务器响应是不同状态。\n\n自有离线链静态记录浏览器proxy、listener、intercept/forward、证书、请求与响应时序，比较代理旁路/拦截/正常转发和失败。只有代理开关、无捕获、后端慢或TLS失败为反例；代理开不必卡，不据meme自行更改真实代理/证书。\n\n来源：[保存帖1](https://x.com/i/status/1486698388225769475)。"
  ],
  [
    "impact-and-acceptance.md",
    "长密码报告的不同项目与资源成本证据",
    "保存两完整图分别Imgur resolved/medium/250与Asana同类标题N/A；前者文字声称72/48常见限制但没有哈希成本/服务指标，目标/环境/政策不同。\n\n静态核注册字段合同、长度/编码、哈希/预处理与资源预算，离线合成小样本比较正常/受限/截断及成本，报告分别记实际影响/资格/处理。只长字符串、单延迟、无资源数据、不同项目或允许设计为反例；不能据两图认新人歧视、通用长度或DoS，禁止真实大输入负载。\n\n来源：[保存帖1](https://x.com/i/status/1485849893541449729)、[保存帖2](https://x.com/i/status/1486720814443495424)。"
  ],
  [
    "by-type/ssrf.md",
    "SSRF 图的可读、盲连接和协议前提",
    "完整图分environment、canreadresponses、URL/header/webhook/PDF/document入口、ftp/dict/gopher/file/ldap、跳转/数值地址及internalservices/metadata。图中示例网段不穷尽地址分类也不授予许可。\n\n静态追真实loader的scheme/host/解析/网络权限、重定向每跳和响应归因，用自有离线合成只确认单边界。client不支持协议、仅浏览器/OOB、正确目标限制或无响应为反例；连接能力不证明内部敏感读取/SMTP/代码执行，不触碰metadata或真实内网。\n\n来源：[保存帖1](https://x.com/i/status/1486799559011430402)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Gh-Dork valid cache 和覆盖输出的完整性",
    "CLI图wordlist、users/org/repo、validitems缓存和outputdir会覆盖内容；正文另一帖仅工具链接，未存一次搜索结果。\n\n静态保留输入版本/来源/时间、cachedvalid依据、每source完成/失败与原始/合并产物，离线已失效/新增/空输入对照。旧缓存、输出被覆盖、名称关联、API失败或未运行为反例；过滤后的valid标签不证明当前归属/秘密，不查询/取得真实敏感材料。\n\n来源：[保存帖1](https://x.com/i/status/1486809838478835718)、[保存帖2](https://x.com/i/status/1486969872110268421)。"
  ],
  [
    "by-type/sql-injection.md",
    "html 路径到标题投影的后端消费者",
    "完整正文path后缀.html含UNION投影，四图title显示DBuser/db/version、再列schema字段与账号hash。后缀不决定服务器实际执行，也不决定受影响范围。\n\n静态追路由重写/参数提取、查询语法/绑定、投影与模板title；自有合成无敏感标记比较普通/安全拒绝/真实差异，记录原始字节。工具栏、纯回显/缓存、不同实例、参数化或无查询消费者为反例；最小投影已足，不复制hash、枚举真实库/用户或破解凭据。\n\n来源：[保存帖1](https://x.com/i/status/1486919018883604480)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Osmedeus chunk 首块不是全部完成",
    "两个原图chunk-parts20：域名单10139行首块509、CIDR116行首块7，skip-subdomain后probing/65kportscan启动，没有全部块收据。\n\n静态绑定完整输入与每块原值/哈希/索引，保存完成/失败/产物和合并去重映射；离线fixture比较余数、空块、重复/遗漏。首块数量/启动、阶段跳过、未收齐块或只合并成功为反例；提前看结果可以但覆盖完成要核全块，本任务未运行扫描。\n\n来源：[保存帖1](https://x.com/i/status/1486966672065921026)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Google Sites ListScripts 的标识和能力层级",
    "图POST某site的gateway/ListScripts而Referer是另一site，带cookie/token，响应privateScript name/id/service/function；正文7500IDOR/RCE标签没有下一能力交换。\n\n仅自有两合成site静态核主体/对象合同、请求path/Referer和真正服务器授权，比较本人合法、错对象和缺身份。仅ID/name、公开脚本元信息、Referer不用于授权、无主体对照或正确拒绝为反例；可见ID不等读取脚本/执行，不能把RCE hashtag作证据，不用图中cookie。\n\n来源：[保存帖1](https://x.com/i/status/1486977638283366401)。"
  ],
  [
    "source-audit.md",
    "Combobulator 公共同名包与依赖解析",
    "图四Maven包publicprovider、包龄/versions4of4计数，未保存真正应用resolve、下载或运行；重复帖尾部whitecheckmark不是结果。\n\n静态记录namespace/版本/registry顺序/lockfile与构建环境，离线合成公共同名/固定内部源/拒绝下载对照。公开存在、heuristic统计、已pin/checksum、正确源优先或未达构建为反例；同名包不证明dependencyconfusion执行，不发布包/触发真实构建。\n\n来源：[保存帖1](https://x.com/i/status/1487036427586129934)、[保存帖2](https://x.com/i/status/1487040217580142593)。"
  ],
  [
    "scope-and-rules.md",
    "SSL 发现到负载均衡后台的身份和等级",
    "完整五步SSLTarget→EC2 internal login→Okta/auth→默认账号→LBdashboard，图只是厂商valid/4.6medium/500邮件；缺原始登录/角色/后台动作。\n\n静态核资产/环境/当前scope、真正认证消费者、主体/角色及无副作用能力，离线合成正常/错角色/安全拒绝比较。证书名、共享EC2、标题、仪表盘外观或仅奖励为反例；SSL关联不授予登录/猜密许可，厂商分值不通用于别的实例，不填支付表/用真实凭据。\n\n来源：[保存帖1](https://x.com/i/status/1487132034409852930)。"
  ],
  [
    "source-audit.md",
    "Mininode 粗细依赖图与动态消费者",
    "架构图Parser→Valuebinding→Loaddependencybuilder/Callgraphbuilder→Reducer输出reducedapplication，蓝/红粗细两种路径，无具体裁剪结果。\n\n静态记录入口/依赖版本、动态加载/反射/插件消费者与保留功能，在自有离线合成图比较可达、未知和已移除节点。只有图/节点变少、遗漏动态边、功能变化或未有行为对照为反例；裁剪不自动保持功能或消除漏洞，不安装/执行工具。\n\n来源：[保存帖1](https://x.com/i/status/1487172166428803074)。"
  ],
  [
    "source-audit.md",
    "opaque after 参数与 Java RCE 标签的缺口",
    "JavaRCE帖子图片只有GET api/v1/list size25/after不透明值、placeholder cookie和常规headers，没有响应、解码格式或执行消费者。\n\n静态分分页标识、编码/签名、反序列化类型及后续sink，离线合成正常/畸形/受限数据对照。类似Base64、无schema/反序列化入口、只是cursor或正确签名/类型限制为反例；不透明值不自动是可执行对象，不擅自造攻击链，不重放网络请求。\n\n来源：[保存帖1](https://x.com/i/status/1487336516061786112)。"
  ],
  [
    "by-type/document-rendering.md",
    "PDF iframe 的 file 与 HTTP 网络消费者",
    "完整tips图HTML注入到PDFgenerator iframe/cloudmetadata，正文另给filepasswd。服务端渲染、本机file读取、HTTP请求和云身份能力是四个阶段。\n\n静态核渲染器/版本、HTML允许元素、URL协议、进程文件权限/出站政策、响应来源与实际文档读者，自有合成文件/离线HTTP标记对照。浏览器侧iframe、file禁用、无网络/凭据能力或仅文本为反例；HTML可插不自动是SSRF/秘密读取，不请求metadata/系统文件。\n\n来源：[保存帖1](https://x.com/i/status/1487405174763278338)、[保存帖2](https://x.com/i/status/1487522184557957133)。"
  ],
  [
    "by-type/ssrf.md",
    "公共表单回调到 SSTI 还需模板消费者",
    "完整正文及alt建议公共form收到request后trySSTI，未保存模板表达式/计算结果和真正出站发起者。\n\n静态追表单字段→存储/邮件/机器人/模板各消费者，绑定输入/时间/唯一合成标记；离线模板fixture比较纯字符串/安全绑定/真实无害计算。DNS/HTTP回调、浏览器/triager触发、无模板语法消费或固定模板为反例；OOB不证明SSTI/RCE，不提交真实表单或发外联。\n\n来源：[保存帖1](https://x.com/i/status/1487592995423940608)。"
  ],
  [
    "source-audit.md",
    "sudo 跑未读代码的假设不能当工具方法",
    "meme声称50行太长直接sudo，另一帖给畸形HTTP脚本名。下载/安装/执行是不同动作，名字和代码长度不证明可信。\n\n静态核来源/版本、入口/依赖、权限、网络/文件/进程副作用，离线只审文本和自有解析结果。未读代码、动态图外依赖、权限不必要或未授权副作用为反例；不因称工具即执行，不运行归档PoC或升级权限。\n\n来源：[保存帖1](https://x.com/i/status/1487662835907899393)、[保存帖2](https://x.com/i/status/1487162313073381381)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "JS 后缀、状态和 MIME 三重筛选的漏项",
    "完整gau→grep.js$→httpx200/contenttype→grepapplicationjavascript图列workerjs，查询版本/noext/错MIME可能漏，软200或第三方资源也可能进列表。\n\n静态保留原URL/来源/时间及解析path/query，记录状态、真实字节/类型与当前资源scope；离线合成带query/无扩展/软404/非JS对照。列表、MIME声明、历史归档、纯壳或第三方脚本为反例；筛选结果不等全部JS/秘密发现，不运行网络命令。\n\n来源：[保存帖1](https://x.com/i/status/1487706106055041028)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Amass CIDR 到 nuclei 管线的 stdin 和地址键",
    "完整链Amass loopback/21→subfinder文件输出→rustscan filearg/全端口→grepOpen/sed→httpx→nuclei。发现网络、域名清单、IP/端口和URL格式的契约可能不匹配。\n\n静态逐段核stdin/argv、范围/归属、输出地址/端口/协议、退出码/并发预算及产物，自有离线结构化样本比较正常/空/失败输入。ignoredstdin、文件名当地址、丢端口、错误被吞或不在scope为反例；one-liner不保证可运行/漏洞完成，不扫描loopback网段或真实目标。\n\n来源：[保存帖1](https://x.com/i/status/1487757649580298240)、[保存帖2](https://x.com/i/status/1484171181221572609)。"
  ]
]

ids={pid for row in json.loads((W/"batch-0120.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert len(urls)==107 and all(pid in ids for pid in urls)
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

