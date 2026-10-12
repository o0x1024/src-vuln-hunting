"""Own batch0105 native distillation; one-time append, no source execution."""
from pathlib import Path
from collections import defaultdict
import json,re
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
W=T/'evals/post-distillation/workbench'
facets=[
  [
    "source-audit.md",
    "BOF模块枚举与句柄及系统调用权限",
    "FindObjects配图FindModule枚举clr.dll与多个PID。这说明采样时哪些进程加载模块，不能倒推可读写句柄、注入能力或直接系统调用的隐蔽效果。\n\n按进程身份、架构、模块采集来源与实际访问权限分层，保存目标和有效枚举分母。未加载、枚举权限失败、已授权管理员访问都是不同反例；展示模块名不计任意进程控制。\n\n来源：[保存帖1](https://x.com/i/status/1412913459038142474)。"
  ],
  [
    "cloud/container-k8s-security.md",
    "容器发行版与linuxkit内核及宿主身份",
    "Docker图同时出现Ubuntu18.04.2、Tomcat6文件、CentOS4.9/glibc2.3.4及4.9.125-linuxkit内核。容器的用户态版本、运行内核、已有root身份与宿主权限属于不同层。\n\n关联容器镜像摘要、运行时/宿主、有效capabilities、挂载与实际服务配置；安装旧文件不证明该服务运行或可达。wmiexec密码提示和半交互shell是已有认证流程，不能与容器root画面拼成未认证宿主接管。\n\n来源：[保存帖1](https://x.com/i/status/1413029188311785472)。"
  ],
  [
    "by-type/authn-session.md",
    "API key跨管理员披露与角色降级后的权限版本",
    "帖叙述管理员B读取管理员A的Base64 key，B降为User仍能用该key；High/Resolved标题没有具体响应。需分清可见性策略、key真实主体、委托权限与降级应撤销哪些能力。\n\n以受控账号固定key创建者/主体、读取者、角色版本、缓存/有效期和最终动作，分别比较降级前后及撤销后。合法共享服务key、只是编码标识或降级后仍允许的动作是反例；编码不是保密控制，展示key不自动证明所有管理员可互相接管。\n\n来源：[保存帖1](https://x.com/i/status/1413039946231803905)。"
  ],
  [
    "by-type/subdomain-takeover.md",
    "失效社交链接的用户名分配与官方信任链",
    "旧Instagram/YouTube链接帖提出第三方用户名重新分配。候选涉及平台handle规则与官方页面信任，不可直接套用DNS资源接管结论。\n\n记录官方链接的当前目标/历史来源、失效原因、用户名是否可分配及平台允许的控制形式，判断用户可能依赖的身份声明。链接仅404、名称保留、已合法归他人或无官方关联都是反例；报告Low/Medium或几小时修复不补实际控制与复测。\n\n来源：[保存帖1](https://x.com/i/status/1413076678440591362)、[保存帖2](https://x.com/i/status/1414080976775376901)。"
  ],
  [
    "by-type/authn-session.md",
    "恢复能力跨邮箱变更与2FA状态的身份绑定",
    "密码重置自动进入Dashboard、邮箱变更后旧重置链接有效及认证不只login的帖子，应追恢复能力实际授权的账户与状态转换。\n\n固定令牌主体、用途、签发身份版本、有效/消费状态，比较邮箱变更、2FA启用及批准恢复后的最终受保护动作。允许恢复时重新认证或政策允许重建2FA与绕过不同；Dashboard、本地跳转和令牌未过期不能替代服务端动作证据。admin view-as另需委托与审计合同。\n\n来源：[保存帖1](https://x.com/i/status/1413086081877041155)、[保存帖2](https://x.com/i/status/1413421951981219843)、[保存帖3](https://x.com/i/status/1414556268207935490)。"
  ],
  [
    "by-type/authn-session.md",
    "移动预验证登录与Web验证合同的最终动作",
    "帖声称Web先验证邮箱而移动端能先登录且响应含PII。不同客户端UI顺序可能合法不同，关键是共同账户状态允许哪些数据和动作。\n\n绑定同一受控身份、验证阶段、token audience/权限、实际响应字段和最终动作，区分允许的未验证会话、自有数据与跨身份读取。页面提示、第七天ATO记述或status成功不能补服务端身份改变，未保存原始响应时仅作为合同差异候选。\n\n来源：[保存帖1](https://x.com/i/status/1414160524388954115)、[保存帖2](https://x.com/i/status/1415773275783794688)。"
  ],
  [
    "by-type/xss.md",
    "函数别名逗号表达式与弹窗图的消费者证据",
    "函数别名和逗号表达式建议依赖实际JS变量绑定、执行上下文及消费者；帖子称五个XSS却仅四张裁切弹窗，没有输入或调用栈。\n\n保留原始输入、解码/过滤后的值、输出上下文和真实读者，区分脚本表达式、普通文本与工具本地注入。变量未定义、安全文本展示或不同WAF规则均可能否定假设；几张不同品牌弹窗不计独立根因或通用WAF绕过率。\n\n来源：[保存帖1](https://x.com/i/status/1413495937138237443)、[保存帖2](https://x.com/i/status/1413535823836983300)。"
  ],
  [
    "by-type/xxe.md",
    "XML resolver到调试服务的协议与执行边界",
    "保存叙述把XML resolver、gopher和Java的TelnetDebugging串成RCE。实体解析、允许协议、出口连通、目标帧格式、调试服务认证及执行能力必须逐项成立。\n\n只沿已观察消费者建立能力图，区分名字解析、连接、原始字节传输与真正调试命令接受；称Telnet不能补JDWP等协议交换。禁用实体、协议拒绝、需要认证或只有连接证据是反例，缺中间响应时不将整条链记成功。\n\n来源：[保存帖1](https://x.com/i/status/1413496149894475777)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "文本列提取与累计字典的原始记录合同",
    "hakrawler输出筛script取第二列、将转义点转换为换行后sort -u再tee -a、Cewl/cut管道都依赖具体输出格式；片段还含弯引号和间距问题。\n\n保存原始URL/label、工具版本、每步字段映射、接受/排除原因和单次运行标识，再统计独立候选。单次去重不去累积重复，任意点切分可能破坏域名，第二列不必是JS地址；字典输出存在不证明所有页面或脚本已采集。\n\n来源：[保存帖1](https://x.com/i/status/1413541772467359749)、[保存帖2](https://x.com/i/status/1414542627651817472)、[保存帖3](https://x.com/i/status/1415050316471406592)。"
  ],
  [
    "by-type/business-logic.md",
    "重复注册与已完成状态的单次消费",
    "重复signup叙述称触发四个ATO，但未保存四条链。应定位同一身份完成状态下是否重新分配所有权、覆盖凭证或重复消费一次性能力。\n\n绑定受控身份的规范化键、注册事务、确认状态、版本和最终账户所有权；对照新邮箱合法注册、别名被拒绝及重复请求幂等结果。重复调用有响应或产生新公开profile不等于接管，跨邮箱/挑战/状态的不同问题不能自动合并。\n\n来源：[保存帖1](https://x.com/i/status/1413569120088387590)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "GetBucketAcl读权与Owner字段及对象访问",
    "S3 owner建议提供ACL查询候选。按[GetBucketAcl官方契约](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html)，读取ACL需要READ_ACP等相应能力；响应的Owner字段不能自动解析为某自然人或测试授权。\n\n绑定请求身份、bucket标识、ACL响应来源与采集时点，分别判断ACL读取、对象读取及变更权限。owner enforced下仍可读取ACL不代表ACL仍控制对象访问；公开对象、无ACL读权与训练示例是不同反例，部分AWS ID或region也不补完整所有者。\n\n来源：[保存帖1](https://x.com/i/status/1413763570521710597)、[保存帖2](https://x.com/i/status/1414993063139741707)。"
  ],
  [
    "by-type/sql-injection.md",
    "XML字段输入的解析层与数据库查询消费者",
    "productId放SQL表达式的图没有响应，另图用弯引号可能使XML本身错误；XML只是输入容器，不能由标签名归为XXE。\n\n分开保存原始XML字节、解析结果/字段类型、查询构造与实际数据库输出，区分格式错误、数据绑定和表达式求值。外部实体需要实体声明/解析消费者及独立证据；正常字面值和统一错误都是反例。原始畸形输入不得默默修复后称原帖可复现。\n\n来源：[保存帖1](https://x.com/i/status/1413825337927114756)、[保存帖2](https://x.com/i/status/1413831395319844872)。"
  ],
  [
    "by-type/mobile-android.md",
    "ADB代理intent与有效网络及应用流量",
    "ProxySetter命令给的是代理配置意图，没有设备端生效及实际流量收据。SSID、当前网络、设备用户、系统代理、应用网络栈与TLS信任需要分别确认。\n\n关联受控设备/应用版本、配置前后值、连接网络与同次请求在代理历史中的来源。应用忽略系统代理、走蜂窝/独立栈或TLS拒绝都可能造成无流量；配置成功不代表HTTPS内容可见，代理进程监听也不代表完整采集。\n\n来源：[保存帖1](https://x.com/i/status/1413932483427586057)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "GNU parallel字段重组与输出碰撞的覆盖分母",
    "图中parallel按列重组目标、只取URL字段1和3，10个jobs运行Nuclei并用同字段命名输出；severity只保留critical/high/medium。路径可丢失，同host多个输入可能共写文件。\n\n记录原始目标到最终请求的映射、每任务独立制品、工具内并发与外层jobs的总预算、有效severity和失败/过滤数。共享文件、只发现host或漏掉低级别结果都不能算完整URL覆盖；两个哈希相异的同图已分别复核，不计两次真实扫描。\n\n来源：[保存帖1](https://x.com/i/status/1413932704677126145)、[保存帖2](https://x.com/i/status/1415703117157392385)。"
  ],
  [
    "by-type/jwt.md",
    "JWT工具valid input与服务端算法和key合同",
    "HS256菜单和valid input表示工具接受了格式，不表示服务器验证了签名。修改alg声明也不证明服务器允许该算法或把不同类型key混用。\n\n[JWT BCP RFC8725](https://www.rfc-editor.org/info/rfc8725/)要求明确支持/允许的算法并约束key与算法使用。以实际验证器、调用方允许集、key来源/类型、签发主体与最终服务端动作判断；仅能解码、签名失败或其他完整性保护是反例。图片token不作可用凭证复制或复用。\n\n来源：[保存帖1](https://x.com/i/status/1414212398668521476)。"
  ],
  [
    "by-type/idor-access-control.md",
    "客户端filter移除与真实租户查询边界",
    "帖将Grafana/Elastic查询称GraphQL并建议删filter/filterid，声称约30%能读额外数据。字段名不证明实际协议，比例缺样本分母。\n\n先确定真实请求语法与查询消费者，再绑定受控主体、tenant/object、服务端过滤及实际返回字段；比较UI显示、请求过滤建议与强制授权条件。服务端独立租户约束、合法全局数据或客户端过滤只为展示都是反例；隐藏字段/参数删除不等于数据越权。\n\n来源：[保存帖1](https://x.com/i/status/1414257809403809793)。"
  ],
  [
    "by-type/info-secrets.md",
    "AEM JSON元数据与完整私有内容和性能分开",
    "图中.json包含sling OrderedFolder、dam相关及示例主题元数据，URL遮挡，帖提节时但缺前后图和耗时。文件夹结构存在不等于私有资产内容读取。\n\n保留身份、原始路径/选择器、有效JSON字段、对象所有权及返回内容范围，排除示例公开资源和登录/错误页。元数据公开可能仍有独立影响，但不得补完整文件；速度结论需同任务基线、有效结果分母和实际测量。\n\n来源：[保存帖1](https://x.com/i/status/1414528751145156608)。"
  ],
  [
    "by-type/authn-session.md",
    "未验证邮箱预占2FA与锁定造成的恢复状态",
    "未验证邮箱先注册再设2FA可能阻碍邮箱所有者恢复，另帖称IP block/用户lockout/captcha总应启用。二者都需明确挑战与业务状态合同。\n\n绑定账户创建者、邮箱确认、2FA密钥所有者、锁定键/阈值、账户复用及恢复后的最终权限。允许未验证准备2FA而确认时重建、合法限流或受控锁定与账户预占不同；用户锁定本身可形成拒绝服务，单一防护并非所有流程的通用结论。\n\n来源：[保存帖1](https://x.com/i/status/1414531921183346693)、[保存帖2](https://x.com/i/status/1416007610562719744)。"
  ],
  [
    "by-type/mobile-android.md",
    "设备名进入后台读者与2FA动作的独立关系",
    "Android/iOS设备名BXSS建议把改设备名与所有应用开启2FA连在一起。设备名必须实际被对应客户端上传、保存并送至HTML/脚本消费者，2FA开关不自动构成这条数据流。\n\n固定受控设备、平台/应用版本、上传字段、持久化位置、真实后台读者和输出上下文；不同平台与应用分别建立证据。仅OS名称变化、应用不发送或安全文本显示都是反例；不要以2FA流程标题补盲脚本回连。\n\n来源：[保存帖1](https://x.com/i/status/1414572032897929224)。"
  ],
  [
    "by-type/info-secrets.md",
    "Laravel env默认值与活跃凭证的配置证据",
    "env图有localhost、空APP_KEY、默认样式数据库字段和遮挡mail，但缺取得文件的原始HTTP来源。配置文本存在不证明活跃生产数据库、网络可达或凭证权限。\n\n绑定制品来源/哈希、应用环境与真正配置消费者，区分模板、失效旧部署、受限本地服务和当前敏感值泄露。空值和占位字段不是可用秘密；报告仅保留字段名及脱敏结构，不利用数据库或mail值验证权限。\n\n来源：[保存帖1](https://x.com/i/status/1414598462998335491)。"
  ],
  [
    "discovery/passive-and-services.md",
    "AXFR训练zone的记录类型与公开性和范围",
    "DNSrr图给zonetransfer.me的AXFR记录，含TTL与NS/A/AAAA/PTR/HINFO。训练zone返回多类记录不意味着任意服务器可转移或记录天然敏感。\n\n关联获准zone、查询服务器/类型、采集时点、响应完整性及记录归属，区分公开DNS数据、可配置转移和越界暴露。记录里的loopback/IP不扩展测试范围；失败、部分响应或公开训练配置均是反例，截图不计当前DNS复测。\n\n来源：[保存帖1](https://x.com/i/status/1414936656982024195)。"
  ],
  [
    "by-type/info-secrets.md",
    "API错误变体的schema认证与代理层归因",
    "建议把数字改字符串、去字段、损坏JSON和删header/Cookie以寻找错误。每项可能进入不同校验层，500或错误文本本身不证明调试秘密泄露。\n\n保持正常请求与每次单一变体，记录实际wire类型、入口身份、错误来源、可读字段及响应来源；区分schema错误、认证失败、上游统一页和真实服务端内部信息。规范错误对象、脱敏栈或本来公开值是反例，删除Cookie也会改变主体而污染比较。\n\n来源：[保存帖1](https://x.com/i/status/1414966799574126600)。"
  ],
  [
    "by-type/authn-session.md",
    "KeyCredentialLink写入与实际证书映射及TGT",
    "Whisker图显示属性更新、证书生成和提示下一步运行Rubeus；该阶段尚未证明目标身份成功获票或可用权限。属性写入、证书制品与认证消费是不同边界。\n\n按受控主体的实际目录写权、对象、key标识、映射配置、服务能力及同次认证收据判断。已有合法写权、映射拒绝或未执行认证均否定完成接管结论；可见证书/密码不复制，工具文字不代最终受保护动作。\n\n来源：[保存帖1](https://x.com/i/status/1415072729645166594)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "DOM书签span采集的集合类型与虚拟列表覆盖",
    "书签console片段直接对getElementsByTagName返回集合用forEach且打印所有span。按[HTMLCollection文档](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection)，它是动态类数组集合，不能假定具备数组forEach接口。\n\n核对实际集合类型与调用结果，关联每条已保存post的稳定ID、完整正文和采集来源；滚动页面可能卸载旧DOM，span也混有按钮/导航。当前DOM数量、滚动到底或控制台打印量不证明全部历史posts已保存，覆盖需稳定ID集合与全文逐项核对。\n\n来源：[保存帖1](https://x.com/i/status/1415195749822783498)。"
  ],
  [
    "by-type/xss.md",
    "邮件双斜线处理后的mailto消费者与HTML注入",
    "email HTML图显示双斜线处理后mailto scheme，第二哈希图内容相同。链接方案和目标变化是HTML/URL消费者问题，不自动产生JS执行。\n\n保留原输入、过滤后HTML、客户端解析的真实href、点击上下文与最终scheme/目标，区分纯展示、合法邮件地址和未经允许的导航。脚本执行需自己的可达读者与执行上下文证据；客户端差异不能以一个图推所有邮件客户端绕过。\n\n来源：[保存帖1](https://x.com/i/status/1415247734261510150)、[保存帖2](https://x.com/i/status/1415638525702119425)。"
  ],
  [
    "by-type/document-rendering.md",
    "RFD文本响应到下载名称和打开程序的消费链",
    "messagehistory TXT图含JS/PHP样式文字，但缺完整Content-Type、Content-Disposition、下载名与实际打开程序。响应有脚本文本不证明浏览器执行或服务端PHP执行。\n\n分别记录可控响应、有效MIME、文件名决策、下载/展示行为与获准自有读者的实际解释器；标题RFD不是链。纯文本安全展示、不可控下载名或用户未进入危险打开流程均为反例，文本和执行收据不得混用。\n\n来源：[保存帖1](https://x.com/i/status/1415297103614550019)。"
  ],
  [
    "by-type/sql-injection.md",
    "SQLi读权限到页面写入和存储脚本的独立能力",
    "图在正常static_pages_content字段旁标Inject Stored XSS，未展示真实注入。数据库读取漏洞不自动拥有任意表行写权，写入文本也不自动在其他读者执行。\n\n分别绑定查询主体、可写表行/事务、页面对象、渲染位置/转义和真实读者；获准受控验证还需批准的回滚与持久化范围。只读角色、写不到被渲染字段或安全文本展示都是反例，不能由一个箭头补完整SQLi到XSS链。\n\n来源：[保存帖1](https://x.com/i/status/1415321434654748682)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "curl http_code的000与首跳和错误丢失",
    "shell循环打印http_code却压掉stdout/stderr，URL未引用且未跟随跳转。000可表示未收到HTTP响应，不能当真实远端HTTP状态或访问被拒绝。\n\n保存URL原始字节、参数边界、退出码、DNS/TLS/连接错误及每跳响应/最终消费者；空白导致shell拆词时已不是原输入。首跳状态与最终可达性、错误丢失与成功空响应分别计，统一按status筛选会损坏覆盖分母。\n\n来源：[保存帖1](https://x.com/i/status/1415382648101359617)。"
  ],
  [
    "targeted-fuzzing.md",
    "WordPress候选路径与插件名称及攻击计数",
    "wp-config备份/debug.log路径、Wpscvn的WP4.9.8和插件名只是候选层。145626 total attacks与Shell exploit链接没有命中响应或实际插件版本。\n\n区分目标WordPress、真实插件版本/配置、匹配器前提和敏感文件返回字节，保留有效请求/失败/过滤分母。统一404/登录页、模板默认内容、插件未启用或版本不受影响是反例；旧攻击字典大小不能当独立漏洞数量或要求运行全部载荷。\n\n来源：[保存帖1](https://x.com/i/status/1413908241084522497)、[保存帖2](https://x.com/i/status/1415435091145265154)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "YApi mock返回passwd文本与动态求值及文件读取",
    "YApi mock路径图显示passwd样式文本，缺实际输入、求值调用和命令结果来源。mock功能本来可返回固定字符串，因此文本相似不能判RCE或真实文件泄露。\n\n绑定同次受控合成标记、配置/请求输入、动态处理器、服务身份和输出/读取收据，区分固定mock、模板计算、真实读取与命令执行。缓存旧响应、可配置样例或正常文本结果是反例，不能用路径名与熟悉输出补版本普遍漏洞。\n\n来源：[保存帖1](https://x.com/i/status/1415484190561161216)。"
  ],
  [
    "by-type/business-logic.md",
    "用户名保留名与路由优先级及安全handler",
    "index.php作用户名后profile位于对应路径的叙述涉及命名空间与路由优先级。公开profile路径可由用户名生成并不自动覆盖首页或认证handler。\n\n按规范化后的账户名、保留规则、实际路由匹配、资源所有权与最终动作建立对照，区分显示URL、重定向、静态文件和安全入口。合法用户目录、冲突拒绝或安全handler仍优先都是反例；仅文章标题或单个profile截图不足以确认业务路径劫持。\n\n来源：[保存帖1](https://x.com/i/status/1415508190653861889)。"
  ],
  [
    "discovery/passive-and-services.md",
    "CDN WAF子网列表的更新时间与租户归属",
    "YAML子网工具声称每日00UTC更新并覆盖CDN/WAF。预定更新时间不是已完成采集收据，提供商共享IP不等于某目标租户或获准资产。\n\n保存数据源/版本、实际更新时点、prefix/地址族与归属依据，区分计划、拉取成功与本地缓存；将候选关联具体获准入口。旧列表、共享边缘或失配租户均限制结论，不以提供商全子网扩大动作范围或证明目标防护存在。\n\n来源：[保存帖1](https://x.com/i/status/1415627411874631683)。"
  ],
  [
    "scope-and-rules.md",
    "bbscope混合资产类型与public-only及当前规则",
    "bbscope图带public-only而结果混合域名、仓库、包和移动应用，token不复制。读取范围列表的账户能力与可对该资产实施的动作权限不同。\n\n逐条保存项目、规则版本/时点、资产类型、精确范围、排除项与允许动作；域名匹配器不能处理bundle/package/repository的授权语义。公开API列表、历史礼物/奖励与邀请关系都不补当前授权；Shopify旧邮件一次例外且未来排除店铺，更不能推广为当前测试许可。\n\n来源：[保存帖1](https://x.com/i/status/1415729846118928384)、[保存帖2](https://x.com/i/status/1415430712761540609)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "分页终止与后台线程及CSV完整性",
    "H1 CSV图显示NEXT_PAGE、getScope、Thread.start、写文件及public skip，截图外的join/异常处理未知。分页结束与后台线程产物全部完成是两个条件。\n\n以稳定项目/资产ID关联页游标、采集身份、线程完成/失败/取消及最终输出哈希，保留public/private过滤与类型分母。只见next缺失、日志称all done或部分CSV并不能确认所有范围已落盘；不能从裁切外猜代码错误，也不能凭私有API可读扩大动作许可。\n\n来源：[保存帖1](https://x.com/i/status/1416056320248193024)。"
  ],
  [
    "by-type/idor-access-control.md",
    "分号路径的授权检查与实际路由消费者",
    "帖称admin/index.jsp403而加分号变200，Go403Bypass图13路径403/404、9头全403。候选路径变形与实际权限成功必须分开记录。\n\n绑定原始路径、代理/框架规范化结果、授权检查资源、最终handler及同一受保护内容/动作；比较受控低权和合法高权身份。200登录或统一错误页、安全handler未命中、工具全部失败均不能算绕过；有限候选失败也不证明所有变体安全。\n\n来源：[保存帖1](https://x.com/i/status/1415799483384823808)、[保存帖2](https://x.com/i/status/1416069180550303751)、[保存帖3](https://x.com/i/status/1416692494603939845)。"
  ],
  [
    "by-type/sql-injection.md",
    "Nexpose SQLi恢复缓存与产品版本及当前响应",
    "sqlmap图显示resumed旧session、已有Cookie、PostgreSQL11.7和Nexpose<=6.6.48标签。数据库版本、工具标题和缓存不是当前Security Console真实版本或新执行证据。\n\n[Rapid7 6.6.49发布说明](https://docs.rapid7.com/release-notes/nexpose/20201014/)记录修补CVE2020-7383；不由此推所有旧部署配置。固定获准产品身份/版本、认证主体、原始成对输入响应与缓存来源；只有历史结果、正常query或未受影响版本是反例，不复制Cookie或将恢复缓存计新复现。\n\n来源：[保存帖1](https://x.com/i/status/1415919103261364226)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "盲SQL总查询耗时与HTTP500的时序证据分母",
    "盲SQL图212次查询、3460.94秒、24个HTTP500及遮挡currentDB/stored logs。总耗时混合网络、重试和错误，不等于每个条件成对时延或完整数据库导出。\n\n保留同环境正常/对照/候选请求的时点、有效样本、失败/重试、缓存和实际解析消费者，区分DB名、字段值与全库制品完整性。500、延迟抖动和旧session不是成功数据读取，测量分母必须排除未完成却保留失败记录。\n\n来源：[保存帖1](https://x.com/i/status/1415921482597683203)。"
  ],
  [
    "source-audit.md",
    "Windows缓解支持表与实际架构及启用配置",
    "旧Win7/8缓解表列SafeUnlink、NX、SMEP和参考材料。OS支持某项能力不代表当前进程/CPU/内核已启用，也不证明攻击可行或已被拦截。\n\n将系统/架构版本、具体制品、有效策略、实际执行环境与可观察对照分层。仅支持表、help、Server Started或生成制品日志都不能补运行权限、接收数据和动态效果；缺哈希和同次收据时保留静态线索等级。\n\n来源：[保存帖1](https://x.com/i/status/1416038990768222212)、[保存帖2](https://x.com/i/status/1416748466773037062)。"
  ],
  [
    "by-type/idor-access-control.md",
    "跨租户邀请的issuer目标与接受后成员状态",
    "叙述User1 Org1把邀请orgid改Org2并带Org2邮箱，Critical/Resolved标题没有具体接受结果。邀请参数、发信、令牌接受及最终成员权限是独立边界。\n\n绑定发起actor、issuer tenant、目标组织、被邀受控身份、token用途/有效期及接受后权威membership，比较最终受保护动作。显示Org2标签、可发邮件、既有成员或接受被拒绝都是反例；不由奖励卡片补真实跨租户授权变更。\n\n来源：[保存帖1](https://x.com/i/status/1416275862505197568)。"
  ],
  [
    "by-type/sql-injection.md",
    "SQL拼接方言模式与注释原始字节",
    "SQL方言帖将MySQL双竖线写拼接并说块注释通常不工作。按[MySQL逻辑运算符](https://dev.mysql.com/doc/refman/8.4/en/logical-operators.html)，默认双竖线为OR，PIPES_AS_CONCAT可改变语义；[注释规则](https://dev.mysql.com/doc/refman/8.4/en/comments.html)支持块注释，双短横线后有空白等要求。\n\n记录真正数据库/版本、SQL模式、编码/过滤后的原始字节和表达式上下文，区分普通参数绑定、语法错和实际求值。MSSQL/Oracle建议也需本身消费者证据；示例缺配对引号不能静默补齐，再称原文成功或通用注释失效。\n\n来源：[保存帖1](https://x.com/i/status/1416431258268221441)。"
  ],
  [
    "cloud/container-k8s-security.md",
    "Cilium架构图与有效eBPF策略及身份覆盖",
    "Cilium图从Pod/CNI到kernel eBPF并标policy/logging/metrics，说明架构分层，未给当前部署、附着点、身份标签或有效规则。\n\n绑定获准workload/node、网络方向、身份标签、实际附着和生效策略，用同次受控允许/拒绝流与日志判断覆盖。仅组件存在、metrics有值或架构图不证明策略启用；标签失配、未管理端点与不经过附着点的流需分别保留，不能计全群集隔离已验证。\n\n来源：[保存帖1](https://x.com/i/status/1416522212274802690)。"
  ],
  [
    "targeted-fuzzing.md",
    "Intruder处理菜单与变换顺序及实际wire字节",
    "Burp图处理规则菜单Hash高亮、payload/request计数0、URL encode勾选。菜单可见不等于规则已添加或编码已执行，不能补实际攻击请求。\n\n保留原始字段、已配置变换顺序、每步字节及最终Content-Type/传输编码，区分Base64/Hash、URL编码和多字段结构。结合挑战与主体绑定确认最终消费者；0请求、只改UI或被额外编码改变语义都是反例，线程/载荷数量也不能证明认证成功。\n\n来源：[保存帖1](https://x.com/i/status/1416748666581405696)、[保存帖2](https://x.com/i/status/1413834185232486403)。"
  ]
]
ids={pid for row in json.loads((W/'batch-0105.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
assert len(urls)==60 and len(urls)>0
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

