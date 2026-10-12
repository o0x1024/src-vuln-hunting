"""Append manually distilled0109 facets after precheck. Own helper only."""
import json,re
from collections import defaultdict
from recover import T,W
facets=[
  [
    "discovery/web-and-api.md",
    "脚本与爬虫候选流水线的来源和字段保持",
    "JSSpider图含同脚本重复及第三方域；gospider串联grep状态、awk第五列、qsreplace和dalfox的文字没有真实漏洞结果。\n\n保留发现页、原始URL、域归属、提取阶段、参数类型和过滤前后计数，逐步检查每段输入输出格式；第三方源、错误列、带等号的非参数、重复脚本、历史URL过期或未进真实sink是反例。候选流的数目不能替代覆盖或XSS证明。\n\n来源：[保存帖1](https://x.com/i/status/1430529851585404928)、[保存帖2](https://x.com/i/status/1431179316642160643)。"
  ],
  [
    "by-type/authn-session.md",
    "MFA重发动作和预启用状态的分层",
    "正文把resend请求POST改DELETE后删除2FA设置称绕过；图报告仍为P3 New。\n\n绑定设置资源owner、开启前后状态、动作权限、challenge和最终登录会话；预启用清理、删除一次未完成设置、报告新建或无服务端challenge消费是反例。重发、删除和已启用MFA绕过是不同动作，不据HTTP动词变更补认证成功。\n\n来源：[保存帖1](https://x.com/i/status/1430555895881035778)。"
  ],
  [
    "hunting-strategy.md",
    "方法脑图节点与实际验证产物的对应",
    "两份Frogy图把域/subdomain/app/IP/cert、端口/OSINT、扫描工具和手工unexpected/extra/less/sequential input组合。\n\n为每节点绑定获准资产、输入、预算、产物、失败与终态；从资产线索进入具体功能、身份和状态假设，再做低副作用单变量对照。图中的工具名单不表示已运行、全协议覆盖或已确认漏洞，目录名称也不替代图内方法。\n\n来源：[保存帖1](https://x.com/i/status/1430578383025491969)、[保存帖2](https://x.com/i/status/1430923809717030915)。"
  ],
  [
    "by-type/authn-session.md",
    "WebSocket消息中的身份字段与握手授权",
    "两张WebSocket测试图分别出现SessionID/customerLogout以及customerProfileChanged、目的用户名；缺握手cookie、Origin和实际授权主体。\n\n分别记录握手认证继承、跨站允许来源、消息身份字段消费、订阅对象及最终读写权；消息打印、SessionID字样、独立本地客户端或只登出通知是反例。不能用业务消息代替跨站握手/会话劫持因果。\n\n来源：[保存帖1](https://x.com/i/status/1430599877826781188)、[保存帖2](https://x.com/i/status/1432983815371182083)。"
  ],
  [
    "discovery/web-and-api.md",
    "站点摘要中的状态指纹和真实内容覆盖",
    "goverview图给HTTP200、时间、8322长度、checksum、CSP和favicon指纹。\n\n记录取回URL、重定向、响应时间、内容类别、checksum算法及取样范围；统一登录页、通用图标、动态长度或未知hash语义是反例。状态和指纹只能筛选候选，不证明敏感数据、控制权或全站请求覆盖。\n\n来源：[保存帖1](https://x.com/i/status/1430608574405808133)。"
  ],
  [
    "by-type/cicd-supply-chain.md",
    "供应链图中源码构建和制品的八个边界",
    "SLSA图列A至H：不当源码、源码管理、后续修改、构建平台、依赖、CI绕行、仓库和消费者的风险点。\n\n给各边绑定获准仓库、源码版本、构建身份、隔离环境、依赖及制品hash、provenance和消费验证；只有架构图、缺签名/生成主体、hash匹配但来源不可信或未核对实际构建是反例。不能据图赋达成等级或当前标准符合性。\n\n来源：[保存帖1](https://x.com/i/status/1430654880545452036)。"
  ],
  [
    "by-type/ssrf.md",
    "云身份字段与本地文件标题的证据错配",
    "一帖列crossdomain、SVG、文件处理与元数据候选，两图显示云IAM credential JSON；标passwd的图仍给元数据URL和Code/Type/Token/Expiry结构。\n\n将具体输入、backend取回、响应来源、身份信息与可用凭证分别标注，逐图对照正文；图错配、只字段结构、值遮掩、浏览器取回或未知代理是反例。不补LFI或有效云权限，只用合成目的地设计验证，不访问真实元数据。\n\n来源：[保存帖1](https://x.com/i/status/1430810341936492554)。"
  ],
  [
    "discovery/passive-and-services.md",
    "代码与情报索引的类型时间和授权边界",
    "grepgithub半百万仓库宣传、Phonebook域/URL结果及多站代码查询图都给索引线索。\n\n保存索引/查询时间、代码或域或邮箱类别、查询分组、源URL、关键词、版本与owner；第三方paste、历史结果、选Domains却当邮箱、空结果或不在书面范围是反例。数量宣传不表示完整覆盖，情报出现不授权登录、秘密使用或资产测试。\n\n来源：[保存帖1](https://x.com/i/status/1431038344004263937)、[保存帖2](https://x.com/i/status/1433254378073464834)、[保存帖3](https://x.com/i/status/1434471021264973824)、[保存帖4](https://x.com/i/status/1435040258039689217)。"
  ],
  [
    "by-type/idor-access-control.md",
    "权限关系图中的可能路径与实际动作",
    "adalanche图为2targets、19 possible pwns、7users、1group、0computers，未给每条边真实动作结果。\n\n逐边核对对象类型、ACL版本、继承/组传递、主体、目标及特权消费者，再用获准身份验证具体动作；过期目录、不可传递权、只图形连线或无终态是反例。计数只能描述模型，不能补19个成功提权。\n\n来源：[保存帖1](https://x.com/i/status/1431244132744302597)。"
  ],
  [
    "by-type/info-secrets.md",
    "Profiler候选路径与可读性能数据的分离",
    "SymfonyProfiler图列app_dev及_profiler等候选路径和Open instances，没有保存有效profile数据。\n\n核对实际框架/版本、路由、profile token、响应类型、reader权限及最小敏感字段；404、Token not found、空dashboard、登录页或仅路径表是反例。组件存在和性能数据可读分别留证，不把路径命中算秘密泄漏。\n\n来源：[保存帖1](https://x.com/i/status/1431582344201265157)。"
  ],
  [
    "by-type/ssrf.md",
    "Webhook校验解析和取回解析的时刻区别",
    "正文描述Webhook域名先正常解析后变127地址/端口21并出现内部error，缺具体socket取回证据。\n\n在获准实验中使用自有受控目的地，绑定validator/fetcher的DNS时刻、缓存、TTL、重解析、redirect及实际连接日志；错误页、DNS记录变化、仅解析未连接或连接仍旧地址是反例。DNS变化不自动证明重绑定或内部端口开放。\n\n来源：[保存帖1](https://x.com/i/status/1431629590309580804)。"
  ],
  [
    "by-type/host-header.md",
    "Host变体中的请求目标和代理消费者",
    "十种变体图含Host前缀/空白/重复、absolute URI、空行、XFH、另一host/端口/IP；反向代理图仅internet→proxy→server结构。\n\n分别记录request-target authority、Host、代理信任头及路由/业务URL生成者，保持会话、目标和单变量一致；解析拒绝、规范化一致、被忽略字段、统一默认页或无业务消费是反例。HTTP200不能证明任意主机信任，更不能推所有子域绕过。\n\n来源：[保存帖1](https://x.com/i/status/1431633632167219202)、[保存帖2](https://x.com/i/status/1433338646443274241)。"
  ],
  [
    "experiment-design.md",
    "认证头长度与资源耗尽的因果对照",
    "正文用Basic/NTLM约20与约二百万字符比较3秒和3分钟，自述未给服务资源、队列或重复测量。\n\n先在自有隔离环境核对头大小限制、代理/认证模块、请求终态、对照资源和恢复；排队、网络/重试、超时、格式错误或单次计时是反例。授权与预算独立于payload长度，本轮没有构造或发送巨大头，不把慢响应自动判DoS。\n\n来源：[保存帖1](https://x.com/i/status/1431721616640118784)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "OAuth清单按发行传输和消费阶段重排",
    "完整清单图列access/refresh token、code、泄漏、scope、redirect、CSRF、replay、credential等；另一正文把请求body含token直接列问题。\n\n绑定具体协议流、client/issuer/resource actor、redirect精确匹配、state/nonce/PKCE、令牌用途/受众和秘密持有者；协议允许body传token、合法回调、一次性code拒复用或无越权终态是反例。每条类别须有独立入口与对照，不能把token出现本身判漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1431964514631577600)、[保存帖2](https://x.com/i/status/1435899874591928321)。"
  ],
  [
    "by-type/mobile-ios.md",
    "iOS采集层与哈希输出选项的证据合同",
    "MEAT帮助分别列logical AFC jailed和filesystem path，以及md5/sha1和输出选项。\n\n先记录设备授权、采集访问层、路径与时间、每制品hash和完整性限制；选项存在、单文件hash、jailed视图或缺受保护路径是反例。不能把logical采集自动计完整设备/密钥链提取，未连接设备或采集用户数据。\n\n来源：[保存帖1](https://x.com/i/status/1431968519407771649)。"
  ],
  [
    "by-type/api-property-pollution.md",
    "PHP参数名称折叠与原始字节保留",
    "正文列点/空格/account方括号等；图显示account_id与未闭合account[id输入折叠后只留一个_GET值，缺PHP版本。\n\n保存query/form原始字节、重复键顺序、前端/WAF/框架各自键名、版本和实际值类型；语法拒绝、一致规范化、变量名碰撞但业务不消费或只本地demo是反例。未闭合键样例不推广为通用数组解析，不以名称折叠单独判授权绕过。\n\n来源：[保存帖1](https://x.com/i/status/1432023286867582976)。"
  ],
  [
    "by-type/idor-access-control.md",
    "分享与提案发送之间的跨动作能力合同",
    "正文把POST shares替为data_requests/id/send_proposal，界面原先不显示发送能力；图只是报告triaged。\n\n用两个自有角色固定对象owner及版本，比较分享、提案创建、发送和最终recipient可见状态；UI隐藏、合法公开proposal、只请求成功或无对象终态是反例。对象可见性与动作权限分开，不能从改路径或triage补IDOR。\n\n来源：[保存帖1](https://x.com/i/status/1432297421644566529)。"
  ],
  [
    "by-type/open-redirect.md",
    "重定向端点与脚本scheme消费的两段保存线程",
    "保存1/2给external-link.jspa url候选，保存2/2自述javascript对话框成功，没有执行origin/浏览器图。\n\n将参数解码、允许scheme、Location或前端导航、读者origin、CSP和最终执行分别记录；仅字符串反射、浏览器阻止、脚本在另一个origin或普通外链是反例。只合并已保存两段，不由dork或success字样补所有同类端点可XSS。\n\n来源：[保存帖1](https://x.com/i/status/1432322673791537153)、[保存帖2](https://x.com/i/status/1432322675435708419)。"
  ],
  [
    "by-type/xss.md",
    "unescape百分号算法与源码词法转义的区别",
    "两帖把百分号tab和反斜杠x/u写法归为unescape自动转换。已核对规范：unescape识别百分号起始的两位hex或u加四位hex；字符串字面量的反斜杠转义在词法阶段处理。\n\n先保存函数收到的真实字符串/码元，再标注JS源、HTML entity、URL或JSON处理层；源码已转tab与字面反斜杠仍保留是关键对照，不能仅看展示形式判函数解码。依据：[unescape算法](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-unescape-string)、[字符串词法规则](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-literals-string-literals)。本轮未执行来源脚本。\n\n来源：[保存帖1](https://x.com/i/status/1432349872523448327)、[保存帖2](https://x.com/i/status/1432351172501942275)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "扫描进度更新与误报质量验证的不同收据",
    "HawkScan1.9 changelog列百分比、行数、实时error、json/csv/txt和降低误报的描述；trick3st图20 running但只有2成功节点。\n\n每任务保留版本、输入资产、resolver/record types、预算、游标、节点终态和产物hash；开始日志、running计数、部分成功、格式选项或质量宣传是反例。质量需获准样本集和判定对照，进度可观测性不证明扫描完成或误报减少。\n\n来源：[保存帖1](https://x.com/i/status/1432371978367811586)、[保存帖2](https://x.com/i/status/1432779287132844035)。"
  ],
  [
    "source-audit.md",
    "可写注册表和检测红标到特权消费的缺口",
    "Reg1c1de帮助列HKLM可写、属性与日志；BeaconEye图仅两红色进程/monitoring2。\n\n把候选对象、获准身份、实际ACL/进程版本、匹配规则与特权消费者分层留证；帮助菜单、红标、合法用户可写但无特权消费或缺通信上下文是反例。不能从可写探测补提权，不能从进程颜色补CobaltStrike命令。\n\n来源：[保存帖1](https://x.com/i/status/1432466718413230085)、[保存帖2](https://x.com/i/status/1431017134080110599)。"
  ],
  [
    "by-type/authn-session.md",
    "恢复令牌返回端点与重置消费的同一绑定",
    "正文写resetPassword，而图为getPasswordToken username后JSON id/token/stamp；没有认证上下文或实际重置终态。\n\n分别记录发行端点、调用主体、目标owner、token用途/受众、challenge时效与一次性消费、最终身份；合法自有恢复、token仅状态标识、另一路径、遮掩或无消费是反例。端点名字不能替代证据，未索取第三方token或发送重置邮件。\n\n来源：[保存帖1](https://x.com/i/status/1432593583790432263)。"
  ],
  [
    "by-type/graphql.md",
    "GraphQL批量能力与逻辑操作预算",
    "正文推荐BatchQL的batch、CSRF和introspection；另帖Graphw00F仅指纹标题。\n\n区分实现识别、schema可见、请求格式、多operation/alias/resolver、认证与状态改变；一次HTTP可承载多个逻辑动作，预算按resolver/动作而非仅请求数。指纹、公开schema、合法只读batch或未消费mutation是反例，不据工具名补批量绕过或CSRF。\n\n来源：[保存帖1](https://x.com/i/status/1432719827609739267)、[保存帖2](https://x.com/i/status/1435939597163376649)。"
  ],
  [
    "reporting.md",
    "模板引用输出与模板检测命中的分离",
    "wmn图按Nuclei template ID产生四个引用URL，没有HTTP匹配请求或漏洞结果。\n\n保存ID、模板commit/hash、引用来源/用途、适用版本、实际匹配器和受控响应；引用列表、同名旧模板、仓库issue或无匹配收据是反例。引用是线索元数据，不能替代技术全文已读、资产命中或修复确认。\n\n来源：[保存帖1](https://x.com/i/status/1432827454444359686)。"
  ],
  [
    "by-type/authn-session.md",
    "2FA秘密可读与认证后的持续用途",
    "正文引用旧VRT下2FA秘密仍可获得的P4分类，以及gauth_token泄漏标题；没有当前规则或令牌内容/消费证明。\n\n区分TOTP种子、bearer、challenge与展示二维码，记录读取主体、启用前后、issuer用途和最终认证；本人才可读、一次设置展示、名字相似但非秘密、过期或只UI接受是反例。历史类别不决定当前影响/奖励，不能把任意gauth_token认作可登录种子。\n\n来源：[保存帖1](https://x.com/i/status/1432978322925961216)、[保存帖2](https://x.com/i/status/1435609638720835589)。"
  ],
  [
    "discovery/passive-and-services.md",
    "通配符DNS过滤的随机对照和空输入风险",
    "massdns/wildcard文字使用dig样例含http前缀、egrep排除和共享IP；缺实际解析收据。\n\n用获准域的DNS名称、多个随机label、record type、resolver、时间及CNAME链保存对照，验证空结果不会变空正则删除全部；共享CDN IP、DNS抖动、URL当域名或仅一随机样本是反例。工具过滤结果不保证无wildcard或接管条件，未执行shell替换/扫描。\n\n来源：[保存帖1](https://x.com/i/status/1433044108331859973)。"
  ],
  [
    "source-audit.md",
    "修改签名文件的工具自述与平台验证",
    "SigFlip图给msbuild、输入/输出SHA1不同、padding/optional header及signed标志，没有Windows独立签名验证。\n\n绑定原始和修改制品、签名覆盖区域、hash、证书链、平台策略和实际消费者；工具打印signed、编译成功、保留证书表或未做信任/执行验证是反例。可观察制品变化不代表签名仍可信或代码执行，没有处理或运行来源PE。\n\n来源：[保存帖1](https://x.com/i/status/1433056519776571399)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "WEB-INF配置内容与标题拼写的实际读边界",
    "正文路径写.EB-INF而图为WEB-INF/web.xml，可见JavaEE/Spring配置；另帖Confluence特殊路径只列pom/seraph/decorators候选。\n\n保留raw target、解码/路径规范化各层、实际文件字节类别、访问主体和版本；正文错字、404、静态默认配置、仅候选或未读到秘密是反例。一个配置文件可读不等于全部源码、任意宿主文件或RCE，具体影响按字段与消费者判。\n\n来源：[保存帖1](https://x.com/i/status/1433386408178237448)、[保存帖2](https://x.com/i/status/1434169918497468416)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "合法sudo与页面指纹不替代首次执行",
    "SSH key RCE题图显示admin、sudo密码提示后root；Confluence检测图只GET doenterpagevariables并grep form action后标Vulnerable。\n\n各自绑定入口认证、执行主体、具体触发输入、权限和独立终态；已有合法sudo、仅页面可达/表单字符串、脚本标签或未知版本是反例。合法提权截图不补SSH绕过，页面指纹不补OGNL/CVE26084成立。\n\n来源：[保存帖1](https://x.com/i/status/1433407530827276293)、[保存帖2](https://x.com/i/status/1435206707949408257)。"
  ],
  [
    "reporting.md",
    "报告编号错配与debug摘要的最小事实",
    "Mailru正文报告号与图1083543不同；图resolved/critical摘要列AWS、SMTP、DB、Django等类别，未展示原始秘密。\n\n将每个编号、时间、报告标题、处置和具体证据绑定；只摘要/评级、截图对应另一编号、缺字段语义或无权限消费是反例。保留编号错配，不能把摘要补为有效云key、RCE或当前敏感数据，秘密值不复制/使用。\n\n来源：[保存帖1](https://x.com/i/status/1433618138411765762)。"
  ],
  [
    "by-type/api-property-pollution.md",
    "结构字段进入可调用消费者的因果链",
    "locale JSON含system/id的图与Includes标签中的uid1000/www-data响应关联；未保存受控基线或处理实现。\n\n区分普通对象、反序列化映射、动态callable/函数派发、最终执行主体；固定无害输入与单字段变化，审计获准源码消费者及输出因果。静态截图、自填响应、合法字段显示或处理器不调函数是反例，不能据结构名字补全RCE。本轮未运行命令或复制PII。\n\n来源：[保存帖1](https://x.com/i/status/1433744883169193988)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "每日资产差异与漏洞差异的版本绑定",
    "UML图为daily cron：scope输入、多工具、dedup、每日log、与前日比对、DB及带auth的web查看。\n\n保存每日获准范围快照、工具版本/失败、原始/规范化标识、resolver时间、产物hash和新增/消失原因；DNS暂失、权限/工具变化、失败产物为空或历史去重覆盖是反例。新资产需范围复核，不能把delta自动算漏洞或静默扩大扫描。\n\n来源：[保存帖1](https://x.com/i/status/1433886968597958656)。"
  ],
  [
    "by-type/idor-access-control.md",
    "文件移除成功响应与对象终态",
    "removefiles图提交file_id并得到HTTP200 success_0，正文称IDOR/DoS。\n\n以两个自有账号和可丢弃对象固定owner，分别验证动作授权与一次操作后的对象终态/访问能力；no-op、异步pending、对象仍在、合法共享权或仅统一JSON是反例。响应不证明实际删除，更不证明服务耗尽，未做真实删除或重复负载。\n\n来源：[保存帖1](https://x.com/i/status/1434080768683249666)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "Windows路径读取与远程include的不同消费者",
    "LFI→RFI图片以Windows PHP/SMB share和allow_url_include/fopen禁用为提示；可见路径只有单前导反斜杠。\n\n记录实际传入路径字节、Windows根相对/UNC语义、PHP版本、filesystem或URL wrapper、include还是普通read、网络身份与获准消费者；路径拼写不完整、无法连接、静态读不解释或配置不符是反例。不能由示意补网络取回/代码执行，未连接share或取回制品。\n\n来源：[保存帖1](https://x.com/i/status/1434119056840445961)。"
  ],
  [
    "impact-and-acceptance.md",
    "accepted金额和发现难易的独立事实",
    "Google图显示accepted但奖励稍后；Synack500图题为Blind SSRF internal port scan，缺端口技术证据；重定向自述1150条无查询数据。\n\n分别记录技术机制、triage、accepted、奖励、修复及时间，不用数量/奖金估算当前风险或通用发现难易。成功登录、accepted标题、没有数据的比例或仍未发奖是反例；不能把这些状态补漏洞成立、P级或当前政策。\n\n来源：[保存帖1](https://x.com/i/status/1431265117501599753)、[保存帖2](https://x.com/i/status/1434164998612287494)、[保存帖3](https://x.com/i/status/1434174456654532608)。"
  ],
  [
    "by-type/crlf-response-splitting.md",
    "邮件标识中的换行候选与真正输出字节",
    "用户名拼接正文列百分号0a再0d及链接文字，顺序为LFCR，没有实际生成消息或header结果。\n\n按原始字节、URL/表单解码、规范化、身份标识存储和邮件正文/header消费者逐层记录；转义显示、只正文字符串、拒绝字符或LFCR没有被作为分隔是反例。不能据候选称CRLF注入或发送给第三方，本轮未发邮件。\n\n来源：[保存帖1](https://x.com/i/status/1434489676094578692)。"
  ],
  [
    "source-audit.md",
    "注入技术菜单远程管理与实际执行动作",
    "GoPurple帮助列13种技术且server8000无incoming；SharpStrike图显示WMI/CIM主机身份与进程表；Penelope图已有PTY后的脚本/文件操作。\n\n区分工具能力、配置、连接、已有会话、获准动作及独立结果/制品hash；菜单、payload生成、进程列表、time0、已登录PTY或日志成功字样是反例。不能补首次RCE、EDR失效或权限绕过，未用图中凭据、运行脚本或取回文件。\n\n来源：[保存帖1](https://x.com/i/status/1434490019721449473)、[保存帖2](https://x.com/i/status/1435713170979659781)、[保存帖3](https://x.com/i/status/1435214791669395456)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "S3对象清单中的文件名与敏感读取分层",
    "S3图列versions、gz、signature和工具zip等键，正文建议AWS/recon命令；未保存内容、下载权限或秘密字段。\n\n分别记录bucket/prefix owner、list/read/write动作、身份与policy、对象版本/hash和最小字段语义；名称像密钥、公开安装包、仅list允许、加密或取回拒绝是反例。对象清单不证明敏感文件可读，不从对象名推有效凭证或宿主文件访问。\n\n来源：[保存帖1](https://x.com/i/status/1434513022798598148)。"
  ],
  [
    "by-type/jwt.md",
    "JWT算法文字与密钥信任来源的校正",
    "JWT图把HS256写为symmetric encryption，并列alg None/RS与HS、kid、jku/jwk/x5u/x5c等候选。\n\nHS256提供MAC而非内容加密；逐个绑定实际验证器版本、算法白名单、密钥类型/来源、issuer/audience/时间及最终主体。只是解码、header可修改、远程键未被信任、合法轮换或签名拒绝是反例。图的分支不是已验证攻击，本轮未破解密钥或请求远程键。\n\n来源：[保存帖1](https://x.com/i/status/1434614836847988740)。"
  ],
  [
    "by-type/business-logic.md",
    "数量小数与计价交付合同的同一口径",
    "正文用quantity从1变0.1、234变23.4说明逻辑问题，没有计量单位、订单或交付收据。\n\n先确定按件整数还是重量/时长等合法小数，绑定单价、数量解析/舍入、库存、结算与实际交付；按比例交付、backend重算、拒绝小数或仅前端总价变化是反例。正确算式不是漏洞，需同一订单的授权最小流程和终态，不进行真实付款。\n\n来源：[保存帖1](https://x.com/i/status/1434782360218734593)。"
  ],
  [
    "by-type/business-logic.md",
    "邀请预占和真正加入组织的状态门",
    "一帖邀请未注册邮箱会自动建team；另一org/team邀请图企业回复只发email、无法join组织。\n\n分清预占对象、发送、接受、确认身份、角色赋权和数据可见性，固定邀请者/受邀者自有身份及组织版本；未接受、pending、不能join、成员权仍拒绝或预期邀请功能是反例。保留回复中的负证据，不把邀请能力升级组织接管，不发送真实邀请。\n\n来源：[保存帖1](https://x.com/i/status/1434849788751593477)、[保存帖2](https://x.com/i/status/1435296497675894788)。"
  ],
  [
    "by-type/info-secrets.md",
    "IIS配置可下载与实际秘密字段的区别",
    "web.config图为200 application/octet-stream及enableVersionHeader=false、removeServerHeader=true；正文称影响低无奖但修复。\n\n区分文件访问事实、配置字段敏感语义、secret有效性及具体业务消费者，用最小脱敏内容/合成字段留证；一般header设置、公开模板、无秘密/内部身份或评级自述是反例。配置后缀/HTTP200不能自动P1，修复和奖励分别记录。\n\n来源：[保存帖1](https://x.com/i/status/1434867381512249352)。"
  ],
  [
    "by-type/authn-session.md",
    "旧请求再登录后的cookie冻结对照",
    "正文称logout/password reset后旧profile edit失效，登录后旧请求又成功，没有保存重放所用cookie。\n\n冻结原session标识/hash，在独立容器避免代理自动更新cookie，比较旧会话与新会话、注销/重置时间及最小受保护动作；请求历史被新cookie覆盖、合法新会话、CSRF改变或旧session仍拒绝是反例。不能把重新登录后的成功自动判旧会话复活。\n\n来源：[保存帖1](https://x.com/i/status/1434920403495915521)。"
  ],
  [
    "by-type/idor-access-control.md",
    "历史URL退出截图的独立无会话验证",
    "正文建议收集认证后的历史URL，logout后用aquatone；没有保存实际私有响应。\n\n用独立无cookie会话及两个自有角色固定URL/对象owner，核对真实敏感字段和读者权限；200登录shell、静态公共页、缓存本人才见、截图器继承cookie或无对象内容是反例。发现URL与未授权读取分别留证，历史数量不代表BAC覆盖。\n\n来源：[保存帖1](https://x.com/i/status/1435071210425966592)。"
  ],
  [
    "by-type/document-rendering.md",
    "电子签名文档在各读者和存储阶段的origin",
    "电子签名图从APP发文档到recipient签名再到多云存储；payload图列事件属性、实体、引号及localStorage读取，未保存真实sink。\n\n绑定上传者/签署者/预览者、文档版本、HTML属性/JS/URL解析、重编码、CSP、执行origin及token消费；下载静态文件、不同origin、实体只变文字、broken quote、未执行或无可用身份是反例。架构图不证明XSS/ATO，未发送文档或外传token。\n\n来源：[保存帖1](https://x.com/i/status/1435277872038563845)、[保存帖2](https://x.com/i/status/1435527806616629248)。"
  ],
  [
    "targeted-fuzzing.md",
    "表单线索转测试参数的类型和副作用合同",
    "正文建议HTML input属性/data schema用于ffuf/jaeles；另一每API都fuzz观点配白皮书封面。\n\n从已观察method/action/name/type、必需hidden/CSRF和业务用途形成参数候选，选择授权单变量、小预算及无副作用对照；页面展示字段、未提交API、字段类型不符、状态改变或统一错误是反例。候选数量/奖金不证明正确入口，不把全端点fuzz设为默认许可。\n\n来源：[保存帖1](https://x.com/i/status/1435689810115629058)、[保存帖2](https://x.com/i/status/1435291816480231429)。"
  ],
  [
    "by-type/authn-session.md",
    "邮箱旧验证链接与对象版本和用途的绑定",
    "正文描述未验证账号改邮箱、验证新邮箱后使用旧验证link导致删除；图只有250奖励。\n\n绑定账号owner、email版本、challenge发行目的/时间、兑换一次性、状态迁移及最终对象读取；旧link拒绝、只注销/页面错误、删除的是临时对象或只有奖金是反例。不能补实际删除因果，最小实验需自有可丢弃对象且不调用真实删除。\n\n来源：[保存帖1](https://x.com/i/status/1435465631436967939)。"
  ],
  [
    "by-type/idor-access-control.md",
    "公开转私有后的关注关系终态",
    "正文为A follow B→unfollow→B改private→重放旧follow，称200再次关注；图只是250奖励。\n\n记录两自有账号、B策略版本、关系状态pending/active、邀请/批准要求、最终可见内容及API/界面一致性；只200、pending审核、私有内容仍拒绝或合法既有关系是反例。关系动作成功与私人内容授权分开，不从重放标签补账号接管。\n\n来源：[保存帖1](https://x.com/i/status/1435507655011803141)。"
  ],
  [
    "by-type/ssrf.md",
    "图片URL的浏览器嵌入与后台取回区分",
    "正文问网页接收任意图片URL能做什么，没有保存backend取回请求。\n\n先区分img浏览器加载、服务器代理、转换器和后台任务，绑定获准自有目的地、请求身份/来源与阶段marker；只有客户端请求、第三方预览扫描、仅DNS或未消耗URL是反例。图片字段不自动SSRF，也不能由前端XSS泛称补内网扫描或劫持。\n\n来源：[保存帖1](https://x.com/i/status/1435558260619231233)、[保存帖2](https://x.com/i/status/1436015313770909705)。"
  ],
  [
    "by-type/mobile-android.md",
    "恢复客户端参数构造与服务端挑战绑定",
    "Android Java图向auth/flashcall_account_recovery构造cuid、encrypted_phone_numbers和cli等字段，缺服务端回复/校验。\n\n将源码版本、调用链、字段类型、发起身份、目标账号、电话challenge、服务端签发及最终兑换绑定；静态HashMap、客户端可改、合法加密值或服务端拒绝是反例。请求构造不证明信任客户端导致ATO，未发送恢复请求或验证码。\n\n来源：[保存帖1](https://x.com/i/status/1435568040112898049)。"
  ],
  [
    "by-type/authn-session.md",
    "MFA提示与最终认证会话的不同阶段",
    "TrevorSpray图两账号、1 valid，并提示MFA in use，缺最终会话或资源访问。\n\n区分帐号存在、密码接受、MFA要求、challenge完成、token发行和受众/资源权限；provider通用错误、提示MFA、部分有效日志或未获得授权session是反例。认证第一阶段不能升级绕过MFA，本轮未喷洒、登录或使用截图凭据。\n\n来源：[保存帖1](https://x.com/i/status/1435577266352840707)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "MinIO目录视图与默认凭证有效性的分开确认",
    "正文提默认帐号和非标准端口；图9000/minio/cdn显示目录/PNG、1.61GB，没有认证方式。\n\n核对产品/版本、访问主体、匿名/public与登录session、bucket action policy及最小受控对象；公开预期目录、图片无认证上下文、已换默认或只有端口是反例。端口不构成认证，默认文档也不证明当前实例有效，本轮未登录或复用帐号密码。\n\n来源：[保存帖1](https://x.com/i/status/1435718207210409986)。"
  ],
  [
    "hunting-strategy.md",
    "历史漏洞分类映射与任务覆盖矩阵",
    "OWASP图展示2017→2021分类映射和统计；图片描述历史版本而无资产实际测试。\n\n固定使用版本，将资产、入口、身份、对象/动作、状态和证据映射到类别，记录合并/拆分但保留原具体机制；类别名齐全、榜单统计、badge、教程链接或缺实测结果是反例。分类覆盖不是测试覆盖，不能据历史Top10推当前全部风险或承诺。\n\n来源：[保存帖1](https://x.com/i/status/1435809828517998593)。"
  ],
  [
    "by-type/authn-session.md",
    "限流候选变换与同一逻辑身份计数",
    "rate poster列session/IP/cache/429及X头、空白、UA、cookie/编码等；没有真实计数日志。\n\n按同业务主体、同动作/对象、时间窗和backend计数键，对一个候选做获准小预算对照，辨验证规范化与计数规范化是否一致；换合法不同身份、缓存响应、统一429、请求数与多逻辑动作不符或无服务端终态是反例。不能从变换表补绕限流或执行批量OTP/发信。\n\n来源：[保存帖1](https://x.com/i/status/1435883641280684037)。"
  ]
]

ids={pid for row in json.loads((W/'batch-0109.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==78 and len(urls)>0
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
