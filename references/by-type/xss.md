# 浏览器输入与脚本执行

## 适用信号与前提

搜索/评论/昵称/上传内容进入 HTML、属性、JS 或 DOM。先记录输入来源、输出上下文、编码和浏览器路径；准备获准测试页面/账号，避免触发真实用户或管理员会话。

## 最小实验

先用唯一无害字符串跟踪输入到输出位置；根据实际上下文设计仅显示测试标记的证明，不读取 Cookie 或业务数据。HTML 文本反射、属性、脚本字符串和 DOM sink 分别分析，不能通用替换。

DOM 场景追踪 source 到实际 sink，保存浏览器运行证据。存储场景需记录写入、存储和后续触发；涉及跨账号影响时使用另一自建测试账号。通过同源测试标记或受控页面状态证明执行即可。

## 确认与反例

需要浏览器在不应执行的目标上下文实际运行测试内容。字符串反射、出现 script 标签、静态 sink 搜索都不是充分证据。区分 HTML 注入、URL 导航、模板表达式与真正脚本执行。

排除已正确转义、不可达代码、sandbox/不同 origin、有效 CSP 阻断、只能本人控制开发者工具的 Self-XSS。CSP 中出现 unsafe-inline/unsafe-eval 不单独证明可利用；结合完整策略和执行路径判断。

## 下一步、停止与报告

规则阻断时记录该条件下未复现；新上下文需新假设。不得为证明影响窃取 Token、诱导真实用户、钓鱼或制造传播。存储测试使用自建隔离资源，按许可清理。

报告记录输入到输出链、浏览器/版本、执行 origin、触发角色、交互条件及证据。类型名称不直接决定等级。遵守 [验证](../verification.md)。

## 调研补充：可执行检查点

- 先用唯一无害标记定位输出上下文，再选择该上下文的最小执行证明；HTML 反射、编码文本和模板表达式不是同一类证据。
- 建立输入面→存储字段→渲染角色链：正常表单、API、导入可能写不同字段；用户视图、管理视图的处理也可能不同。只在受控查看者验证。
- 静态 JS 找 source/sink，浏览器核对实际可达路径；CSP、沙箱、Trusted Types 和交互条件都记入结果。不得从关键词扫描推断执行。
- HackerOne #192210 的平台说明把实际边界定位到管理端渲染；“商店允许 HTML”不能直接推广为后台也允许。这是入口/渲染面差异的历史样本。

客户端消息与命名属性转 [postMessage / DOM clobbering](dom-messaging.md)。

## 调研来源

- [PS-xss · Cross-site scripting](https://portswigger.net/web-security/cross-site-scripting)
- [H1-xss · Report #192210: Stored XSS in blog comments through Shopify API](https://hackerone.com/reports/192210)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

## 归档案例补充：导出消费者

同一输入可能进入浏览器预览和服务端文档消费者，分别确认执行位置及权限。PDF 排版变化不等于 XSS→SSRF→文件读取链已成立，见 [文档处理](document-rendering.md)。

## 间接字段与盲点归因

联系/反馈/举报内容、个人资料、设备名称与认证设备标签，可能在用户页面、通知邮件和管理视图中被不同模板消费。先用唯一无害标记确认实际存储字段、任务和查看者，再选择一个获准受控消费者核对上下文；不能把输入存在直接当作后台脚本可达。

注册邮件正确转义不代表找回邮件采用同一模板；邮件保留 HTML 也不等于浏览器脚本执行。未见反射或未收到回连只能记录观察缺口，不能推导“盲 XSS”或“更盲的存储 XSS”。

延迟回调保留原始输入标记、写入时间、触发时间、任务/对象和受控查看者；几个月后出现请求不自动证明当前版本或某位管理员执行了脚本，还需排除链接扫描器、重放及其他消费者。没有已批准的受控审核流程时，不为加速回调联系真实客服打开测试载荷；测试残留按既有清理/交接规则处理。

`console.log` 等无害标记可减少证明的副作用，但日志函数并不决定输入是否被持久化。仍须核对写入入口、存储字段、后续消费者及清理；确认日志来自目标上下文的真实执行，而非测试者手动在控制台运行。

## CSS 与跨上下文载荷宣称

可控样式单独记录为 CSS 输入能力；若声称泄露或键盘记录，先核对目标值实际存在于什么 DOM 属性/状态、选择条件能否观察它、是否触发受控资源请求及 CSP/缓存条件。用合成标记证明实际可见范围，不把样式修改或公开演示标题升级成任意按键、令牌或跨账号数据读取。

不完整标签、data/javascript URL、编码换行和 polyglot 只是在具体 HTML/属性/脚本/URL 上下文中的候选。逐项验证标签、属性、引用、事件触发和浏览器版本；“所有上下文都能执行”“换浏览器即可绕过”均不作为通用规则。数字外观的订单 ID 等字段也按真实消费者处理，不从字段名排除 XSS。

Markdown/BBCode 等轻量标记要跟完整转换链：原始输入→链接/图片解析→净化→最终 HTML/DOM→浏览器。检查生成的 URL/属性，而非只看原始文本过滤；原始文本区、未加引号属性和解析器状态变化可能使正则假定的上下文失效。用实际 DOM 和无害标记确认可控属性、触发条件与受众，不能从某个函数名或截图载荷断言当前页面可执行。

扩展名为 `.js` 不保证响应按 JavaScript 消费。分别记录直接导航、script 引用、预览或下载时的实际 Content-Type、响应头与浏览器处理路径；JS 字符串转义不能代替 HTML 上下文编码，反之亦然。先确认输入进入哪个解析器及真实 DOM/执行来源，再判断引号或标签能否改变上下文，不能从 MIME 错配直接确认 XSS。

接口返回 JSON 时，沿字段跟到实际 Web、邮件、导出和管理端消费者，再判定各方的编码/净化职责。JSON 字符串含标签本身不证明 XSS；只看 API 当前返回 JSON，也不能认定服务端无需保护或所有后续渲染都安全。分别记录响应类型与浏览器消费方式，不能用一处客户端转义覆盖其他模板或存储后消费者。

多个输入在同一页面相邻反射时，保存各输入的实际位置、长度限制、编码及两者之间的固定模板，再分析最终合成的 HTML/JS；独立片段无效不代表组合无效。只有它们确实汇入同一消费者时才安排有依据的组合对照，并保存每个单独输入与组合后的 DOM/无害执行结果。参数分别可控、输出文本拼在一起或历史多反射载荷，并不能保证跨过了当前净化与浏览器边界。

客户端模板表达式与服务端模板分别定位执行主体和版本：记录普通字段是否成为实际编译模板、模板上下文中可达的能力、框架配置及最终浏览器 sink。Angular/AngularJS 名称不能证明免疫或通用可利用；表达式被渲染、浏览器脚本执行与后端代码执行是不同边界，按受控标记核对，不套用另一版本的模板逃逸片段。

正则删除标签的候选先固定模式、引擎、修饰符、输入解码和替换后文本，再核对浏览器的实际上下文。PHP PCRE默认点号不匹配换行，s/DOTALL改变这一条件；源帖删除模式中的换行差异只支持对应处理链的假设，不自动等于所有标签过滤绕过。用无害标记确认HTML/属性/脚本消费者与执行来源。依据：[PHP模式修饰符](https://www.php.net/manual/en/reference.pcre.pattern.modifiers.php)（2026-10-09核对），未执行源帖JS/PHP。

HTML实体形成的TAB与普通空格分别保存为实际码点，跟实体解码→属性值→URL解析→最终消费者，不按截图中空白外观判断协议或脚本语义。[URL标准基本解析器](https://url.spec.whatwg.org/#concept-basic-url-parser)规定移除ASCII TAB/换行（2026-10-09核对）；本机Node URL对仅含probe标记的字符串观察到此规范化，但未运行JS或导航浏览器。URL结果、真实浏览器执行与CSP条件仍分别证明。

Dangling markup另建HTML解析与取址路径：保存未闭合属性、实际DOM、原始字符、浏览器/版本、元素与最终请求；只用合成标记观察是否被捕获并发往获准接收端。Chromium的[历史移除提案](https://groups.google.com/a/chromium.org/g/blink-dev/c/KaA_YNOlTPk/m/abOHSKhUAQAJ)针对原始URL同时含换行和小于号的HTTP(S)取址（2026-10-09核对）；此条件不能推成“Chrome没有任何dangling markup”。某条资源请求被阻断、HTML注入和脚本执行分别记录，不能通过发送真实页面秘密证明影响，也不能从另一版本绕过报告推导当前浏览器行为。

枚举window上以on开头的属性只产生当前浏览器全局事件处理器候选，不证明任意HTML元素具有同名处理器，也不证明事件可在目标页面触发。记录实际元素、净化后的DOM、事件来源/用户交互、浏览器版本、脚本策略与无害执行结果；属性存在、WAF接受和真实执行分别判定。协议相对script URL与显式HTTPS的差异还需核对文档基址、混合内容、实际网络错误和CSP，不能把两行载荷的不同响应总结成通用绕过。

内联script中的字符串有HTML分词与JavaScript语法两层边界。实际响应中的结束标签可能先结束当前script，即使它位于JS双引号内部；[HTML script-data end-tag状态](https://html.spec.whatwg.org/multipage/parsing.html#script-data-end-tag-name-state)（2026-10-09核对）支持按HTML上下文分析，不能只问是否逃出JS引号。保存响应Content-Type、精确字节、解析状态、实际DOM、script类型/策略与无害执行；外部JS、文本视图、序列化后没有真实结束标签或安全编码都是反例。view-source截图展示构造线索，不等于浏览器已执行；也不能推成任意script字符串都无需转义即可XSS。

邮箱字段按输入语法、应用规范化、实际收件地址与输出消费者四层分析；“符合邮箱RFC”不等于注册端必须接受，更不证明脚本可执行。[RFC5322 §3.4.1](https://www.rfc-editor.org/rfc/rfc5322.html#section-3.4.1)允许quoted-string形式的local-part，而[HTML email输入定义](https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email))有意采用不同约束（2026-10-09核对）。用自有地址/隔离样例恢复客户端与服务端合法基线，跟显示名、资料页、邮件模板和管理员视图的真实编码/DOM；只有文本接受、解析器返回地址或创建账号不能确认XSS，不向真实员工投递载荷。

## 自建data页面与目标执行上下文

在地址栏打开自己写的data:text/html并显示脚本提示，仅证明浏览器处理了测试者自建内容；没有目标输入、投递路径和目标消费者时不称XSS。核对实际浏览器版本、导航/嵌入方式及执行origin，不能继承历史data来源行为。[Mozilla对Firefox57的说明](https://blog.mozilla.org/security/2017/10/04/treating-data-urls-unique-origins-firefox-57/)将创建脚本环境的data导航/iframe来源与嵌入页面分开（2026-10-09核对）。即使脚本在目标上下文成立，Cookie读取、Path覆盖、调用业务函数与受保护状态变化也需分别验证；只用合成标记，不收集真实会话。

## 嵌入来源与重复属性

产品允许嵌入外站网页时，分别记录父页面、iframe/新窗口的实际来源、sandbox及允许能力。自有外站弹窗只证明外站脚本运行；是否越过产品预期边界要由目标上下文执行、桥接消息或可达受保护能力证明。截屏弹窗标出的外站域名不能当目标XSS；合法外部内容嵌入作反例，不收集用户Cookie。

hidden输入的属性注入需保存完整原始标签、ASCII引号/编码、可控value位置与最终DOM属性，而不是只展示载荷。若输入确实能结束value并在已有type前产生新type，[HTML分词器](https://html.spec.whatwg.org/multipage/parsing.html#attribute-name-state)会移除同token中较后出现的同名属性（2026-10-09核对）；已有type在前、引号被编码或后续净化时结果可能不同。type变化、可交互性、事件触发和无害脚本执行各自核对；排版弯引号不能直接当语法引号，也不由不含尖括号推一定绕过WAF。

## XML文本与最终HTML消费者

CDATA中的文本先按XML消费者和解析结果追踪，再检查它是否进入HTML/脚本可执行位置。XML输入被接受不等于XSS，更不因CDATA就自动成立XXE。保留输入文本、XML节点值、序列化/转义和最终DOM上下文，用无害标记区分编码差异；用户双击或提交才触发的历史载荷须记录真实交互前提、元素事件、浏览器与CSP，不能写成无交互执行。

## 表单与CSV导入的共同数据终点

直接表单被净化，不证明CSV导入、后台同步或批量入口经过同一处理器。保存获准合成CSV的字段、编码、分隔/引号、列映射、导入角色与实际存储，再追到列表/详情/预览DOM的转义与消费；CSV公式执行和HTML渲染XSS分别判断。图片中的CSV片段与弹窗不足以绑定完整请求/域/他人可达性，不把一次自有导入扩大为所有角色已验证存储XSS；只使用无害标记，不导入真实秘密记录或要求管理员打开。

## 可选调用与已具备的脚本上下文

可选调用?.()和算术操作只是JavaScript语法，仍需具体输入能进入可执行脚本及该函数真正可调用。[MDN可选链](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)说明null/undefined会短路，但未声明根变量仍可报ReferenceError（2026-10-09核对）。保留解码/拼接后的完整脚本、事件触发、版本与CSP；可选链不自动绕过HTML转义、净化或WAF。图中不完整的URL/表达式没有当前解析结果，不执行源载荷或把自有控制台代码当目标XSS。

## 多个参数恢复到同一个HTML属性

多个参数分开通过输入检查时，关注最终输出是否把完整URL重新拼进同一href或其他HTML位置。保存原始参数顺序/重复键/分隔符、各次URL解码、输出转义、最终响应字节及浏览器解析后的真实DOM；参数拆分不保证分词器把片段组成标签/事件，也不保证WAF采用帖子猜测的正则。

截图中的未转义href/拆分片段只有示意响应，缺当前DOM/实际执行证据时仍是上下文假设。通过已获准无害标记确认目标来源的消费路径，核对CSP、触发动作和身份；自有控制台/页面弹窗与被遮盖域名的单截图不能补当前目标链。盲点位于支持人员后台时只分析获准合成工作流与已有消费证据，不为触发脚本把载荷布满真实资料或诱导员工查看支持工单。

## 动态Function与不同邮件模板

十六进制字符串在JavaScript中解码、交给Function构造并调用，要求先具备该脚本消费者/语法和允许动态编译的运行环境。WAF放行、一次alert图片和自己控制台执行都不能代替目标输入到脚本的链路。[MDN Function构造器](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/Function)说明动态解析/全局作用域及CSP/Trusted Types条件（2026-10-09核对），当前浏览器与策略另证，不把旧Cloudflare/站点标题当通用绕过。

资料的Address2、Unit等少用字段按独立输入/输出位置纳入业务覆盖，不把“所有输入”理解成全站自动投载荷。注册、重置和营销邮件可能采用不同模板；只有已获准自有合成订阅流程存在时跟踪某字段到实际邮件正文及邮件客户端，HTML保留、链接改写与脚本执行分别证明，不批量订阅或向真实人员发送测试邮件。

## 迟到回连与授权有效期

存储输入数月后才被后台消费时，原始写入身份/对象/标记、签发时点、当前消费来源与回连接收证据须关联。回连可来自安全扫描器、重播或另一环境，不能由迟到信号直接认管理脚本执行、内网读权限或接管。

当前授权、残留合成输入清理/撤回、受控接收器保存期限和报告时点分别交接；授权已失效时不继续重投或让脚本收集后台资料。隐含第三方XSS托管工具的功能不是读取管理员数据的许可。已有最小消费证据即可保留，未知消费者/敏感资料扩大读取明确停在缺口。

## 处理指令样式输入与解析器版本

历史材料用以<?开头、含引号和尖括号的字符串解释过滤器与浏览器对属性边界的分歧。先确认输入落在HTML数据、属性、脚本还是XML中，再记录过滤后的实际字节和最终DOM；肉眼看似属性的文本可能属于完全不同的词法状态。

2026-10-09核对[WHATWG HTML解析规则](https://html.spec.whatwg.org/multipage/parsing.html#processing-instruction-open-state)：当前规则包含处理指令的target/data状态，data中的>可结束该token，引号并不启动HTML属性状态；非法或禁止的target还涉及转为comment。不能把旧材料统一写成当前所有浏览器的bogus-comment实现，也不能从标准推出某个已发布浏览器已实现。用隔离、无脚本/无外联的文本标记观察指定浏览器版本、处理前后字节及节点边界，然后分别判过滤缺口、可执行sink和保护条件；未验证WAF或上下文时保留假设。

## 请求位置、转发头与消费位置

把Cookie名称作为query参数、在X-Forwarded-For中写标记，只说明研究者改变了一个请求位置。应用实际读取Cookie/query/header的优先级、可信代理重写和进入模板/日志的路径，需要由获准流量或代码证据确认；名称相同不能认定同一消费者。

图片只展示转发头含script而没有响应/DOM，不能由80%之类比例断言XSS。按精确输入位置到储存/输出sink、HTML或脚本上下文和受保护读者的边逐步确认；普通响应、运维后台和代理日志是不同支线，不能诱导员工读日志补证。保留不可控、被代理覆盖、正确编码或根本未消费的结果，不全量追加参数或复制来源脚本。

## 百分号文本、换行与URL规范化

历史iframe例子明确提醒粘到源中前先URL解码，说明输入形态重要。字面%0A文本、实际换行字符、HTML字符引用及应用显式解码不是同一层；标注哪一层转换成哪些字节，避免把处理顺序抹成通用绕过。

[WHATWG URL基本解析](https://url.spec.whatwg.org/#concept-basic-url-parser)先去除输入中的ASCII tab/newline（2026-10-09核对），不能据此声称任意百分号字符都会先变成换行。之后还要确认最终协议、iframe文档origin/脚本权限、CSP与实际受保护消费者；规范化结果只支持候选，不证明当前浏览器执行。用获准隔离的非脚本文本标记观察转换，不访问来源页面或运行其javascript载荷。

## jQuery组件版本与实际DOM消费者

旧帖把CVE-2020-11023范围写成1.3.0到3.5.0，不能照录为包含修复版的区间。[jQuery维护者公告](https://github.com/jquery/jquery/security/advisories/GHSA-jpcq-cgw6-v4j6)给出>=1.0.3且<3.5.0、修复版3.5.0，并说明不可信含option的HTML进入.html/.append等DOM操作是适用条件，即使此前经过清理也可能受影响（2026-10-09核对）。

先绑定实际加载/执行的组件制品、版本/补丁与输入到该DOM方法的调用链；仓库旧文件名、页面指纹或某处存在旧依赖不证明当前可利用。不同CVE/解析机制及清理器兼容选项分别核对，不以公告中的历史workaround承诺现行清理器接口。只用获准静态调用链或隔离无外联标记确认条件，不对所有旧jQuery站点投载荷或直接升级ATO。

## URL片段、指针事件与二次DOM消费

URL片段进入 location.hash 后，又被解码并写入 innerHTML，是独立于原始反射位置的第二次HTML消费。记录原始响应、浏览器片段、解码函数及实际DOM；网络过滤器看到的请求材料不能代表浏览器最终消费的片段。普通文本显示或没有相应事件触发，是不同反例。

[MDN pointerrawupdate](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerrawupdate_event)说明该事件支持有限并有安全上下文条件；不能把旧事件载荷视为所有浏览器通用绕过。[innerHTML说明](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)区分插入script不执行与其他事件处理路径的风险。核对当前浏览器、实际事件、策略和可信类型/净化流程，以隔离无外联标记确认消费者，不从一个WAF产品名推所有配置均失效。资料核对：2026-10-09。

## 脚本结束标签与输入转换顺序

旧示例把输入中的加号展示为输出空格，但帖子未给出真实请求编码和服务端转换链；不能默认任意输入都经过表单解码。按原始请求→解码/转义→响应字节→HTML分词→JS解析保存顺序。[HTML script-data end-tag规则](https://html.spec.whatwg.org/multipage/parsing.html#script-data-end-tag-name-state)会在匹配的结束标签名之后处理空白、斜杠及大于号，JS字符串中的反斜杠不代替HTML上下文保护。具体历史字符串仍需实际响应及DOM证明，不能只凭帖子排列认定执行。资料核对：2026-10-09。

## 访问键、点击与错误处理链的触发条件

accesskey值、真实键组合/点击、内联处理器编译、全局错误回调与最终效果是不同前提。拆分window/onerror属性名只改变表达式写法，不保证目标净化器或WAF放行，更不保证已能运行处理器。

[MDN accesskey](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey)说明激活方式依浏览器与平台变化并可能有快捷键冲突（2026-10-09核对）。保存实际DOM、浏览器/平台、元素可交互性、策略和触发动作；旧Firefox字符串没有执行截图时保留候选。用隔离无外联标记确认各步，不把需要交互的链写成无交互或通用浏览器XSS。

## 实体、标识符转义与带标签模板

HTML事件属性先经过字符引用解析，所得文本才由JavaScript编译。实体显示形式、实际码点与JS标识符转义分别保存；离线解码可见DiacriticalGrave为U+0060，不能由名字猜成别的重音字符。百分号表示是否先解码仍依真实输入位置。

[JS词法说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)允许合法标识符的Unicode转义；[带标签模板](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)可调用tag函数，因此“没有括号”不等于没有函数调用或只是静态字符串。先核对净化后属性、可调用对象、参数类型、事件/浏览器与策略；旧pointer事件图片只是语法候选，不说明已绕过当前WAF或执行。资料核对：2026-10-09。

## 运算符钩子与函数字符串的固定下标

旧无括号例子借助函数转字符串取固定字符、原型修改和instanceof触发回调；这些步骤要求已经能执行事件代码，不能从文本不含某个字符推可利用。[Symbol.hasInstance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/hasInstance)会参与instanceof判断并调用相应方法，不是纯字符替换。

函数的实际绑定、字符串表示、固定下标、对象方法和动态代码策略都须绑定运行环境；包装函数或不同表示可破坏旧下标假设。[Function.toString说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/toString)区分源码函数与native字符串。静态记录这些依赖和反例，不执行来源片段、不修改真实页面共享原型；厂商致谢名单不是该载荷请求/执行链的证据。资料核对：2026-10-09。

## 属性中的反斜杠与自动聚焦前提

JS式反斜杠转义不能代替HTML属性编码。[双引号属性分词规则](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(double-quoted)-state)按实际引号结束该状态，普通反斜杠没有JS字符串那样的逃逸作用。保存完整标签、原始字节、后续净化和最终DOM；截图中只显示输入value与若干尝试，不能从WordPress标题识别具体插件/版本或现行漏洞。

悬停、聚焦和自动聚焦分别记录真实触发条件：元素是否可聚焦、属性是否保留、文档/嵌入策略、浏览器状态与实际事件。autofocus文字或一次“加载时有效”的叙述不证明所有页面都无交互触发；只以隔离无外联标记核对，不让真实用户/管理员消费。资料核对：2026-10-09。

## 同一脚本中多个参数的词法关联

两个参数分别进入同一行的不同JavaScript字符串时，第一处的反斜杠可能改变后续引号的词法边界，使第二处进入不同表达式；逐字段看“HTML已编码”会漏掉联合输出。保存原始HTTP字节、解码/编码次序、完整拼接源码、函数/对象边界与实际脚本插入方式，不能用美化后的片段代替原始词法关系。

历史三张图给出双参数、结束并重建调用结构的说明，但无完整响应与浏览器执行证据。tag调用、注释余段和语法恢复各有条件，不是任意两参数都可执行；优先获准模板源码与普通标记追踪，先逐处基线再评估组合边。不运行源PoC、把弹窗/脚本投给真人或以新增旁路为当前WAF通用结论。

## fetch作为标签调用的参数与网络条件

[带标签模板文档](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)说明首参数是字符串片段数组，插值另作后续参数；[fetch参数](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch)则是资源及RequestInit。由此，源简写的插值对象不能自动当作已拼入URL的数据；完整配图另造method/headers/body对象，实际是第二参数的候选。

[数组字符串转换](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)通常用逗号连接片段，需核对真实目的地字节而非按普通模板字符串想象（2026-10-09核对）。event.target.attributes固定下标依赖当前DOM次序与属性名，文字反射不证明已取得可执行oninput上下文。脚本执行、DOM读取、请求发出、服务端接收和跨源响应读取分别观察；CSP connect-src、实际请求媒体类型/预检也另证，mode:cors不能通用取消预检。仅静态审阅或获准无敏感标记流程，不执行图中密码读取/外送代码。

## 邮件主题的传输、列表与阅读消费者

邮件主题可能经过邮件头生成、编码/折行、收件列表与独立阅读页面；这些与邮件正文/网站输入框是不同消费者。旧帖称HTML主题在另一邮箱执行，没有提供原始邮件、客户端版本、DOM或真实脚本结果，不能把保留HTML、渲染标签和JavaScript执行合并。

从获准合成离线邮件及已有模板追踪原始主题字节、传输变换、实际字段位置、来源与阅读角色，排除本地邮件预览/扫描器和仅格式变化。脚本上下文与邮件头注入分别证实；不向真人发送载荷或收集其cookie，用无害标记保留未验证分支。

## 删除中间标签可能重新组成语法

移除某段标签不等于剩余文本仍为安全文字：源示例用被删除的结束p标签隔开尖括号/iframe片段，提示原始过滤、替换后文本与浏览器再次解析的顺序。保存精确模式、替换次数/顺序、后续编码/净化和完整输出上下文，不能仅从前后字符串认定执行。

正确输出编码、允许列表净化、未进入HTML消费者或导航策略拒绝都是反例。用无害标记观察最终DOM及允许的行为，奖金/P2不决定当前影响；不运行历史javascript iframe、不把删除任意标签都说成通用绕过。

## JSfuck表示与事件属性的语义

长串括号、方括号和运算符组成的JSfuck片段，不能因为缺少常见函数关键词就视作安全文本。先核对它实际进入HTML属性/事件处理器还是普通文本，保留实体解码、引号、净化后字节与CSP/浏览器消费条件。

旧图仅显示svg onload属性的编码表达式，没有实际DOM/执行结果；外部Pastebin内容未读，不假设载荷与截图完全相同或当所有属性过滤都可绕过。静态跟踪语法与已知安全编码反例，不为“解码”运行表达式、加载外链或向用户页面植入代码。

## 事件参数转字符串与定时器消费者

旧无括号图把hashchange处理器设为setTimeout，并改Object原型的toString/source，使事件参数可能在后续字符串消费中得到另一表示；已经能执行这些赋值与可控hash是前提，不能当普通文本直接取得脚本能力。

[RegExp.toString说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/toString)按source/flags生成表示；[HTML定时器算法](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timers)区分函数与字符串处理，字符串分支还受Trusted Types/CSP检查（2026-10-09核对）。保存真实事件对象、原型/属性继承、API类型转换、最终字符串与浏览器策略；原图无执行证据，不能承诺现行环境接受该旧对象/语法。仅静态追踪，不导航载荷URL、运行表达式或修改用户页面共享原型。

## 类型转换异常的独立输出路径

Boolean等字段拒绝输入时，异常文本仍可能带原始字符串；表单正常输出安全不能代替错误模板、通知或日志读者的编码。按字段解析→类型转换失败→异常处理器→响应MIME/HTML位置→浏览器消费者保存链路，字符反射只定位问题。

旧图有Invalid boolean value文本及脱敏弹窗，没有完整响应、页面来源和输入到执行的关联；正文woot4与图woot3也不能合并为同一次实验。用获准合成字段和无害标记比较合法/非法值与错误输出，排除纯文本错误、本地弹窗或安全编码；不投脚本到真实后台或诱发生产故障补证。

## SRI元数据集合与脚本消费

历史“让hash解析报错即可绕过SRI”的断言要拆成原始integrity字符串、浏览器解析后支持的元数据集合、实际资源字节和加载消费者。[W3C SRI工作草案§3.3](https://www.w3.org/TR/sri/#response-verification-algorithms)区分空集合、最强支持算法及摘要匹配；不支持的算法被略过，但已识别算法的错误摘要不因此全部失效。空集合的匹配算法返回真也不代表其他加载策略放行。

以获准合成材料对照无元数据、有效匹配、有效不匹配与混合/无支持项，记录真实DOM、资源来源、浏览器版本及CSP/CORS/Integrity-Policy条件。研究者能改本地属性不等于攻击者能控制受保护页面；不能从旧Chromium题述推出当前任意parse error都可执行脚本。核对日期2026-10-09，草案日期2026-03-20；本次只读相关规范文本，未加载或执行来源JS。

## 数值进制还原与属性调用

数值经指定进制转成字符串再索引属性，须先还原常量与真正消费者。[ECMAScript2022 Number.toString](https://tc39.es/ecma262/2022/multipage/numbers-and-dates.html#sec-number.prototype.tostring)规定2–36进制及字母数字表示；本次只以自写离线整数除法核对8680439的30进制字串为alert，未执行来源HTML/JS。

字串还原不等于函数调用成立：事件处理器是否创建/触发、top所在窗口的同源条件、属性是否可调用及CSP/沙箱均须关联。合法属性访问、词法过滤差异、实际脚本执行及目标能力分开；不能由旧图或WAF放行推出当前通用绕过，也不导航载荷、调用函数或向第三方传数据补证。2026-10-09核读规范相关算法段落。

## 单次删除与重组后的语法

双斜杠及ononerrorerror等旧例子提示单次/顺序替换可能留下另一段语法，但该帖未保存过滤器实现；不能擅自假定所有重复字符串都能绕过。另一组实际控制台图明确使用字符串pattern依次replace尖括号，额外前缀消耗首次替换而留下后续img样式字符串，只证明展示的字符串变换。[MDN replace说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)区分字符串pattern只替首次、常规非global正则与带g的多次替换，并说明返回新字符串而不改原值（2026-10-09核读）；可自定义Symbol.replace的对象另按实现。全局替换仍不是任意输出语境的安全编码，也不能从未展示的HTML消费者推定执行。逐步保存原始字段、解码、具体替换模式/次数/顺序、替换后字节、输出编码与最终HTML消费者，与已有“删除中间标签”分支关联。

仅在获准离线合成材料比较正常文本与重组后的结构，保留不会重组、正确编码或允许列表净化等反例。字符串出现script/onerror、Stored XSS题述与真正事件创建/触发分别证实；不运行原载荷或让真人消费，也不把某次过滤差异升级为通用WAF绕过。

## DOM接收点记录与插桩覆盖

历史帖子称Untrusted Types记录所有sink；[作者仓库README](https://github.com/filedescriptor/untrusted-types)实际列出导航、已有Trusted Types页面、特定iframe及worker等限制，不能采用“所有”覆盖结论。记录接收点调用只定位消费者，不等于输入可由攻击者控制、绕过净化或已经执行。

对获准合成离线轨迹保留工具/浏览器版本、启用时点、观测上下文、传入值、调用ID/堆栈、实际源码与DOM变化，并区分报告模式/插桩和应用自己的强制策略。没有日志可能是未触发、安装时机或未覆盖通道；一条日志也不证明整站无其他路径。2026-10-09只读README相关说明，未安装扩展、运行来源代码或读取未提供的页面数据。

## noscript与净化后的再次解析

文件名中的noscript片段不是适用于所有上传表单的通用XSS。上传part文件名、存储元数据、列表/通知/下载响应与最终HTML位置分别追踪；搜索栏仅显示输入不证明脚本执行。[HTML解析规范](https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inbody)对noscript按解析上下文及脚本模式选择处理，净化器与后续解析器的模式差异需要独立证据。

保存净化前后文本/DOM、序列化与再次解析的顺序、片段上下文、浏览器/净化库版本、输出编码和策略。安全文字消费、不发生再次解析或模式一致作反例；只静态核对获准合成片段，不渲染原载荷、不发上传请求或用图片标题补mutation成功。2026-10-09只核读相关规范规则，未阅读全部外链视频/文章。

## 更新前值与审计文本的延迟消费者

更新事件可能同时记录FROM旧值与TO新值，下一次更新才让上一版本进入审计模板；“至少更新两次”不是所有功能的必要步骤。把对象/字段、版本与时间、旧/新值、持久化记录、消息模板及授权读者绑定到同一事件，区别当前页面与后台/异步消费者。

优先用已有模板与合成普通标记静态追踪旧值是否按其HTML上下文编码，并保留只显示新值、安全编码或根本不生成审计文本的反例。延迟回连还要归因到真实获准消费者；不向账单地址植入脚本、反复修改真实支付资料或诱使工作人员触发。

## 链接属性的分层语法位置

a标签变形图列出标签/属性分隔、属性值引号、实体与URL内部多个位置，各层不能共享一份“空白都有效”的结论。按原始HTML→实体解码后属性→URL处理→可能的脚本消费者保留值与边界，区分属性名、属性值和协议文本。

[HTML解析规则](https://html.spec.whatwg.org/multipage/parsing.html#tag-name-state)给出状态相关分隔符；[URL解析规则](https://url.spec.whatwg.org/#concept-basic-url-parser)另处理ASCII tab/newline等，不能把一层行为推广到任意Unicode或所有HTML位置。只静态追踪获准合成片段，实际导航/执行/CSP条件仍独立证明；旧图及不同尺寸副本不提供现行绕过结果。2026-10-09核读相关规则，未渲染来源载荷。

## 八进制字符串与动态构造消费者

旧片段用八进制转义表示属性名和构造器参数；自写离线整数到字符转换核对三组内容为filter、constructor、alert(1)，未求值来源JavaScript。外层svg/onload仍含字母，“没有字母”最多描述其中编码部分，不是整个载荷的事实。

[ECMAScript2022字符串规则](https://tc39.es/ecma262/2022/multipage/ecmascript-language-lexical-grammar.html#sec-string-literals-static-semantics-early-errors)将旧八进制转义在严格模式下视为语法错误。记录HTML解码、实际JS源码、模式/引号、属性绑定、动态函数策略与事件触发，字符串还原不是执行证明；正确文字编码、拒绝动态代码或未进入事件消费者为反例。2026-10-09只核读相关规范，不调用构造器或渲染来源片段。

## 代理全局替换与反射搜索

Match and Replace图把匹配请求参数替为脚本，再搜索响应；这是主动改写经过代理的流量，不是单纯检索已有反射。实际正则、参数类型、工具支持/版本、启用范围/时点及所有匹配字段分别记录；同时修改多个字段会改变业务路径并破坏单变量归因。

先在获准离线材料用普通唯一标记绑定原始请求、改写后字节、真实响应位置/上下文、搜索集合及其他请求变化。命中可能在错误页或被编码的文本，截图400/401列表与搜索词不证明HTML执行；零命中也需排除未覆盖/被拒绝路径。不开启全局脚本替换、关闭真实页面防护或让其他用户/员工消费载荷。

## 事件名称列表与真实触发路径

二十事件图混合加载/错误、聚焦、键鼠、表单和卸载，还含onMoveOn标签；列表中的名字不是浏览器已注册事件或元素支持的证明。记录元素类型、属性/绑定API、浏览器/版本、真实事件源、交互条件及策略，任意on前缀文本不自动创建有效处理器。

短oncut、marquee onfinish、script外部src与iframe导航还分别依剪切/动画事件、语法恢复、资源加载和执行来源；外部iframe可加载不等于在父页面同源执行。只静态跟踪获准合成上下文，保留不触发/不支持/安全编码/策略拒绝反例，不加载来源外站、剪切用户内容或把二十条都认作无需交互的XSS。

## 非ASCII标识符、强制转换与动态函数作用域

楔形文字示例改变标识符外观，仍依赖布尔/对象到字符串、固定字符下标、属性拼接、constructor与动态函数消费者。[MDN标识符说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)给出Unicode标识符类别，ASCII过滤不能概括JS词法；这不说明Unicode文字反射就可执行。

静态追踪真实源码、各值类型/下标、模式与赋值绑定，动态构造的函数还须能取得其引用的名字。未声明赋值在不同模式/作用域可失败，包装或不同字符串表示会破坏旧下标。图中的编辑器和弹窗只展示该演示上下文，不能证明目标输入进入脚本、CSP允许动态代码或别的浏览器同样执行；2026-10-09只核读说明和静态材料，未求值片段或调用构造器。

## 标签中的斜杠、字符实体与真实词法层

img/**/src等写法须按HTML tokenizer解释，/**/在标签中不是JavaScript注释；[HTML属性名状态及相关状态](https://html.spec.whatwg.org/multipage/parsing.html#attribute-name-state)把斜杠、等号、空白与普通字符分开处理。保留URL/form解码后的字节、标签/属性结果、事件源码和实际触发，WAF未报警或反射不代替执行。

href中的Tab/NewLine实体、反斜杠Unicode转义与排版弯引号属于不同层；弯引号不是ASCII属性引号，HTML也不直接把JS反斜杠转义当字符实体。脚本标签属性、编码空格、数值转换、atob和看似window的名字仍需真实解析/对象绑定；字符串可还原不自动调用它。2026-10-09核读相关规范，未渲染/导航来源片段，不从AWS/Cloudflare厂商标签承诺当前通用绕过。

## 反射最小长度与检测盲区

反射检测的NAME/VALUE类标记、最小长度和参数名/值位置影响候选集合；URL、body、JSON、XML及属性、multipart属性、cookie须各自匹配实际解析/回显消费者。长度阈值能减少短串碰撞，也会漏掉短反射，不保证零误报或零漏检。

记录工具/配置版本、阈值、请求和响应位置、精确编码/字节与尝试集合，再区分纯文本、HTML属性/脚本等上下文及实际可执行条件。发行说明的新增profile数量与列出的名字不一致时保留差异；名字如SSTI/SQLi不替代规则正文或证据，不安装启用未知profile。

## 数值实体后的标识符绑定与事件执行

&#x101;表示U+0101字符ā，不是分号或JavaScript空白。实体进入事件源码后仍按JS词法解析；前置ā表达式是否有绑定、元素id是否造成该环境中的window命名属性及作用域冲突，都可能改变后续语句能否到达。

保留HTML属性名/值、实体解码结果、实际事件、全局/局部绑定、异常及最终调用。标签模板形式的alert还需真实可调用对象/策略；WAF接受或弹窗故事不证明另一环境可执行。只离线核对字符及源码，不渲染来源HTML或求值事件片段。

## 浏览器脚本与本地主机执行的缺失边

评论进入网页并在目标origin执行JavaScript，只证明该浏览器上下文的脚本能力；图中紧接“attacker got reverse shell”仍缺从Web脚本到本地进程执行的桥梁。独立核对原生桥接、浏览器/扩展漏洞、下载后用户执行或桌面客户端集成，以及各自版本/权限/交互前提。

实际同源标记、受保护业务动作、凭据用途和本地进程能力分开定影响。普通浏览器页面没有已证的原生执行消费者时保留缺口，不把XSS自动升为系统RCE；不下载活动文件、诱导真人执行或启动回连来补图中箭头。

## 指针捕获事件与真实触发前提

gotpointercapture/lostpointercapture不是onclick的同义词；事件属性可写、元素实际捕获/释放指针与脚本在目标来源执行分别记录。[MDN捕获说明](https://developer.mozilla.org/en-US/docs/Web/API/Element/gotpointercapture_event)描述setPointerCapture触发捕获事件，[方法说明](https://developer.mozilla.org/en-US/docs/Web/API/Element/setPointerCapture)要求实际pointerId并记录不对应活动指针时的异常（2026-10-09核读相关段落）。

沿实际HTML/属性解析、浏览器/指针类型、用户交互、应用已有捕获逻辑、释放条件和无害执行标记核对。事件名不常见既不保证触发，也不自动否定可利用性；需要先有任意脚本执行才能调用的“触发代码”不能用来证明最初入口。只静态提炼，不加载来源测试页或执行事件载荷。

## 原先self-XSS的条件变化与再次审查

旧报告因只有自身输入/自身执行而关闭，后来CSRF保护或受众发生变化，应按当前消费者重新打开分支。保存前后版本/规则、可控字段、持久化位置、受害者加载入口、浏览器自动身份和目标来源的脚本触发，说明旧限制由哪一项新事实改变；不是仅凭旧评级再提交。

用获准自有身份和合成无害标记区分攻击者可投递输入、另一身份实际接收/触发、脚本可读内容和可执行的敏感操作。跨站可写不保证XSS执行，XSS执行也不直接等于账号接管；HttpOnly、站点交互、同源与操作再认证分别核对。来源Triaged/High图只说明报告状态，缺少完整交易不能补出真实接管链。

## 联邦个人资料进入另一应用的存储渲染

第三方账号的显示名/username进入登录后的应用，属于跨系统数据输入，不能因为来自受信身份提供方就假定字段已适合HTML/属性/脚本语境。沿声明可信度、字段映射、落库存储、不同读者/管理端渲染、语境编码/净化与最终浏览器来源追踪；值被保存不自动意味着脚本能执行。

在获准自有隔离身份和合成普通标记中核对原值、各层规范化与真正消费者，区分正常显示、仅自身页面执行和他人正常加载所触发的能力。来源建议在所有社交平台设置脚本名，不作为操作步骤；不改变真人外部资料或借登录未知网站来扩展范围。

## 表达式完成值、导航文档与dump输出

来源把可选链findIndex调用dump后拼HTML称作Firefox无需document.write的写DOM方法。[MDN dump说明](https://developer.mozilla.org/en-US/docs/Web/API/Window/dump)将dump定义为非标准stdout日志方法，返回undefined；单独调用不写DOM。[javascript URL说明](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/javascript)说明实际导航中字符串完成值可成为新HTML文档，CSP也可阻止该导航（2026-10-09核读相关段落）。

关联真实入口是否是javascript导航、表达式值/回调参数、dump可用性、浏览器版本、HTML解析/事件触发与目标来源。普通脚本表达式得到字符串不自动插DOM，可选链也不修复未声明根变量；控制台或自建页结果不能证明目标注入。保留来源缺少承载上下文的限制，不执行载荷或将其认作当前Firefox漏洞。

## 删除字面关键词与传输层空格还原

删除javascript字面文本可使包在标签名和事件属性中的文本重新拼成HTML语法；核对删除大小写、次数、递归、转义/解码顺序及最终HTML tokenizer输入，不能只看过滤前字符串。源示例用加号作为标签空格，只有存在实际将加号解成空格的传输/解析步骤才等价；直接HTML中的字面加号不能静默当空白。

先在已提供净化代码/获准离线文本中逐层记录原值及转换后值，再关联实际插入位置、属性语法、事件触发、CSP和浏览器来源。可接受的字符串不证明目标执行；target-specific Akamai声明不能外推所有该供应商版本。只提炼转换失效的条件，不执行源事件表达式或补出缺少的请求上下文。

## 全局属性枚举下标与with作用域

源控制台图中Firefox下标5、Chrome153和Safari5880各自调用弹窗，说明相同数字并无跨浏览器函数身份保证；另一图下标6/7展示不同结果。关联实际this、对象自己的可枚举字符串属性、加载脚本/构建、属性顺序与被选函数；不能为了“有一个会命中”就依次调用未知函数。[Object.values说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values)定义枚举范围，[with说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)说明作用域链扩展且严格模式禁用（2026-10-09核读）。

with(document)中的非限定标识符解析、对象属性遮蔽和真正调用的this仍需分别核对。控制台本就能执行脚本，不证明目标输入已进入可执行语境；cookie读值不含HttpOnly秘密，也不证明接管。用已有脱敏代码/日志确认语境和消费者，不复用图中Cookie或求值枚举表达式。

## 历史Angular文件与当前CSP允许的脚本消费者

在历史索引找到旧Angular文件，只形成曾有资源线索；需关联当前可达且实际相同版本的内容、script-src/nonce/hash/strict-dynamic等有效策略、页面上下文及触发的具体库行为。未被正常业务引用的文件仍可能在同源可取，但历史URL、版本题名和允许某origin本身不证明可执行任意脚本。

在获准现有响应/代码中核对当前制品hash/版本、实际脚本选择与消费者路径，再用隔离合成无害标记判断能力；缓存旧文件、已删除资源、CSP禁止加载或没有相关上下文都是反例。来源没给库版本/实际触发，保留候选，不下载/执行旧库或向真人站注入脚本。

## 编码字符串到计时器或HTML写入消费者

源polyglot把\x28/\x29标Unicode，实际是两位十六进制转义；[MDN词法说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#hexadecimal_escape_sequences)将它与\u形式区分。引号闭合、注释和script结束标记各依实际HTML/JS上下文，标签模板调用还要跟最终字符串转换，不是一条字符串在所有位置可执行。

[setTimeout说明](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout)区分函数与编译执行的字符串输入；延迟只是调度，不赋予跨源父页面能力。另一个document.write(atob(...))例需追base64解码结果到真正HTML解析/脚本上下文/CSP，编码不产生额外权限。弹窗1只展示当前执行，不证明当前Cloudflare普遍绕过或被害者受众；iframe允许嵌入也不取消SOP。只分析既有字符串/代码，不执行polyglot、加载攻击iframe或写浏览器DOM。2026-10-09核读词法与计时器相关说明。

## JavaScript恢复接口与未加引号的iframe拼接

Linkfinder列出viewUserInfo及userId，只恢复客户端接口候选，服务端是否按当前主体校验对象仍需独立证据。另一代码片段把URL接到未加引号的iframe src，再把整段字符串交给body.append；这里是URL构造后再次进入HTML解析，不是设置一个已存在节点的src属性。保存完整拼接代码、可控字段、编码顺序、实际库/版本与最终DOM，路径名字和userId可改不能代替IDOR。

对获准源码/隔离合成材料，分别追对象标识到服务端授权，以及URL字节到HTML属性/事件/执行origin和CSP。空格、引号与等号的意义由具体标签和HTML分词状态决定；URL编码可能在进入HTML前被解码，也可能保留为普通值。公开用户信息、固定服务器URL、正确属性编码和服务端拒绝作反例。实际读到另一主体私密对象与目标上下文脚本执行各自确认后，才能讨论链条影响。

## 事件属性名与净化变换的阶段

事件属性ASCII大小写、百分号解码和HTML字符引用属于不同阶段。[HTML属性名状态](https://html.spec.whatwg.org/multipage/parsing.html#attribute-name-state)将ASCII大写转为小写，其他普通字符追加到名称（2026-10-09核读）；属性名中的&#79;不会按属性值规则自动变成O，百分号也不由HTML tokenizer自动解码。若旧例声称能用这些写法，需要前置URL/实体解码或另一实际消费者的证据，不能把所有编码视为浏览器通用能力。

删除/替换onerror、error或script片段可能生成新的危险字符串；逐步保存原字节、每次变换、最终属性名/值及DOM上下文，核对净化是在解码前、后或会否继续变换。接受字符串、黑名单漏词、替换后含事件名不等于事件已触发；实际HTML消费者、支持的事件、可达触发与CSP仍独立。在隔离无害标记或源码中比较处理顺序和转义反例，不执行来源载荷或向真实读者投递。

## 日志参数、生成脚本与日志查看器

console.log接收字符串/值并输出，不会仅因日志里没有显示引号就重新解析其中的脚本。[console.log说明](https://developer.mozilla.org/en-US/docs/Web/API/console/log_static)区分输出值与格式化字符串（2026-10-09核读）。源帖的log:%input%和log:{alert(xss)}未给实际JS或消费者，应先辨别普通日志内容、模板拼成的脚本表达式、动态求值，以及后台日志查看器的HTML渲染。

真实输入若被拼入可执行脚本，风险发生在解析/求值阶段；若是普通字符串参数，需另有后续危险消费者才成立。沿原字段→序列化/模板→完整生成代码或日志记录→真实读者/DOM/CSP，对照转义文本、正常日志及自有无害标记。控制台手工执行和显示特殊字符都不证明目标XSS，不为证明盲日志消费向真实运维/支持人员投递脚本。

## 兼容规范化与相似斜线的区别

看起来像ASCII的字符不一定由NFKC统一替换。[UAX15](https://www.unicode.org/reports/tr15/)定义兼容分解后组合；自写纯文本核对（Unicode数据13.0.0，2026-10-09）显示U+FF1C、U+FF1D、U+FE35分别变成小于号、等号、左括号，但U+2044 FRACTION SLASH没有分解映射并保持原样。因此旧帖声称整段必变为ASCII斜线的结果不能由标准NFKC单独推出，若出现该结果需额外映射/代码证据。

保留原字节/码点、字符解码、具体规范化形式及版本、自定义替换、校验前后次序与最终HTML/URL消费者。字符串转换不证明标签执行、WAF绕过或SSRF目的地改变；未做映射、转义文本、规范化后可靠校验及CSP拒绝为反例。仅在离线普通文本核对单字符/输出，不加载外部checklist或渲染来源事件载荷。

## 跨参数脚本拼接、行注释与调用

多个查询字段被原样串进同一个JavaScript字符串时，应审完整生成脚本，不能逐参数看关键词是否放行。[MDN词法说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)规定行注释到行结束、块注释及换行对语法的影响（2026-10-09核读）；函数名称与括号之间的换行在具体表达式中可能继续调用，不能假设每个换行都会自动插分号。

沿请求百分号/表单解码、字段拼接次序、字符串闭合、注释范围和实际脚本消费者/CSP，用获准无执行文本及现有代码观察语法边界。旧图about:blank控制台弹框只证明手工上下文，另一幅生成脚本示意也没给目标响应/运行条件；它们不证明当前Akamai绕过。保留参数组合的必要性与单独反例，不求值来源eval/atob片段或把多个字段批量喷洒到真实目标。

## data脚本地址的逗号与反斜杠文本

源帖在HTML的script src属性写字面反斜杠x2C；[HTML双引号属性规则](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(double-quoted)-state)不会像JavaScript字符串解析器那样把它转换成逗号。[Fetch data URL处理](https://fetch.spec.whatwg.org/#data-url-processor)先以实际U+002C分隔媒体类型和正文，找不到该分隔符返回失败，再处理正文百分号编码（2026-10-09核读）。因此需区分静态HTML字节、被JS生成的属性值及应用额外解码，不能用屏幕上相同文本混为同一URL。

沿输出→实际DOM src→URL/媒体类型与正文→script类型/加载策略→真正执行上下文追踪。正文里javascript:文字不是自动二次URL导航，data资源解析成功也不代表通过MIME/CSP或在目标身份执行。仅比较获准无活动代码的普通标记文本，保留原字符串/缺失逗号反例，不渲染源script标签、调用eval或导航旧载荷。

## HTML image兼容名与元素上下文

黑名单没列image并不意味着它是完全无关的新标签。[HTML in-body解析规则](https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inbody)会把image开始标签改为img再处理（2026-10-09核读对应条目）；SVG等外来内容、DOM API直接创建、净化器再序列化与普通HTML解析不能不加区分。单独出现image/details或“allow”文字不证明事件属性存在或实际触发。

以获准无事件/无外部取址的合成标签核对完整HTML上下文、解析后命名空间/元素、净化前后属性及真实消费者/CSP。已有可靠允许列表、编码为文字、没有可触发事件或策略拒绝均为反例；source中的javascript图片src和脚本样式标签又各需版本/加载消费者。不要通过创建真人可见活动内容来证明，也不把一处标签遗漏推广为所有开发者或所有浏览器通用XSS。

## 数值字符引用的前导零与缺失分号

HTML数值字符引用与URL百分号解码分别发生。历史串中的%26%23在确有一次对应解码后才成为&#，十进制000000040表示U+0028左括号；直接放在HTML中的百分号文本不自动还原。[HTML十进制字符引用状态](https://html.spec.whatwg.org/multipage/parsing.html#decimal-character-reference-state)逐位乘10累加，遇非数字且没有分号会记录解析错误并继续数值引用处理；[无引号属性状态](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(unquoted)-state)中的引号也有特定错误恢复（2026-10-09核读相关段）。解析错误不是必然停止或拒绝。

保留输入位置、各解码后字节、属性边界、返回状态与最终事件源码，不能把无引号值内的引号当双引号属性的同一闭合规则。仅静态比较普通字符标记及现有获准输出，真实标签/事件/策略和调用效果另证。旧Cloudflare标签没有目标响应或当前规则，本次不渲染SVG、求值事件或称通用WAF绕过。

## object的data资源与执行文档身份

object data中的data:text/html;base64值先经过资源URL解析与解码，再由实际嵌入消费者处理；Base64不是净化或权限来源。[HTML object条款](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-object-element)按资源类型区分图像与子导航文档（2026-10-09核读相关段）。不能将它与父页面的内联脚本或普通图片加载视为相同执行边界。

追踪完整输出上下文、标签/属性是否保留、解码后MIME、object加载策略、真正子文档origin、脚本策略与可访问资源。子文档出现弹窗也不自动证明父页面身份、Cookie或受保护能力可用；被编码为文字、对象加载被拒绝及隔离origin是不同反例。仅静态读取普通标记/现有记录，不渲染源object或执行其中脚本。

## XML命名空间与浏览器的文档消费者

.xml后缀或application/xml不保证内容只作为无活动文字。历史图含XML节点的XHTML默认命名空间、script元素与浏览器弹窗，支持当时一个文档观察，没给全部浏览器/策略或目标上传链。[XML命名空间§6.2](https://www.w3.org/TR/REC-xml-names/#defaulting)说明默认命名空间作用于范围内无前缀元素，不直接作用于无前缀属性（2026-10-09核读）。本地名相同而namespace不同不能按同一元素处理。

固定真实响应MIME/字节、XML或HTML解析模式、每个元素展开名、资源加载方式、文档origin/CSP与实际读者；下载、普通XML解析、图像嵌入和顶层浏览器文档是不同消费者。净化器只看后缀或本地名可能漏掉另一命名空间，但只有实际脚本消费与受众证据才能确认XSS；此处不渲染XML或用命名空间URI当要下载的远端schema。

## 可选链、括号分组与模板标签调用

可选调用、取属性后的模板标签调用和间接eval有不同语义。[MDN可选链](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)说明eval?.()为间接eval；[模板标签错误说明](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Bad_optional_template)区分直接可选链标签的语法错误与括号分组后普通标签调用，后者不继承链的调用短路，缺函数仍可能抛错（2026-10-09核读）。不能把所有包含?.的字符串当等价载荷。

追踪输入承载位置、百分号/实体解码、拼接后的完整JavaScript、真正事件/导航消费者、函数可用性、浏览器版本与CSP。example.com控制台弹窗只证明手动运行环境的一次观察，不证明目标生成脚本或当前Cloudflare/WAF绕过；跨属性/注释片段也需完整上下文。这里只静态分析文字，不调用eval、渲染载荷或远端注入。

## 重复返回参数与多层编码的实际导航消费者

旧/login例同时给两个ReturnUrl和双百分号编码值，另一例用title闭合、编码属性/实体、location/hash片段宣称Access Denied bypassed。这些串分别涉及query重复选择、百分号解码、HTML分词/实体、JS表达式及导航解释；WAF和应用可能观察不同表示，但正文没有给出各层完整结果。未知loc变量、浏览器语法/事件和输出上下文不静默补全。

保存原始请求目标、各层重复项/值、准确解码次数、净化后DOM/属性、真实事件及最终消费者，先以离线无害标记追踪被消费的那一值。服务器未收到的fragment可能由客户端随后读取，不能因URL带hash就称服务器直接消费。阻断页消失、脚本文字反射或奖励宣称不等于XSS执行；只读来源，不执行载荷/导航来源地址或扩展为通用Akami/WAF绕过。

## Swagger文档来源与元数据链接消费者

旧图用url参数加载外部定义，将termsOfService及contact.url/email都写成javascript字符串。文档能被取得/解析不等于UI生成可执行链接或自动导航；字段格式、净化后的DOM、点击要求、浏览器策略、UI版本及实际来源都要核对。浏览器取定义与服务端取址也不共用SSRF结论。

[Swagger2规范](https://swagger.io/specification/v2/)区分swagger规范版本、info.version应用API版本、联系URL与email字段（2026-10-09核读），图中2.0与1.0.1均不证明Swagger UI自身版本。仅在已有获准定义/脱敏渲染轨迹中用普通链接标记跟消费边；不导入活动定义、点击来源脚本协议、执行全部API请求或把所有Swagger端点称同一XSS。

## 窗口名称、子框架编号与srcdoc策略

旧TinyXSS图把top[0].name、contentWindow.name、top.name、srcdoc外部script、eval(name/URL)分成数种场景。不同字段的可控者、frame创建顺序/编号、同源访问、事件及导航消费者不等价；控制窗口名也不自动取得脚本执行或绕过CSP。禁止unsafe-inline不代表外部script、子文档和eval都允许。

[MDN Window.name](https://developer.mozilla.org/en-US/docs/Web/API/Window/name)说明现代浏览器跨域加载可清空名称并在返回原页恢复（2026-10-09核读），旧持久名称假设须按实际版本/导航核对。沿获准既有普通标记记录name值/读者、sandbox/有效策略、完整srcdoc和最终无害效果；未知父子文档策略保留缺口，不渲染原图载荷、设置真实窗口名或请求图中脚本域。

## 脚本字符串反射与自动Vulnerable标签

旧图把历史URL全部query值替换成script字符串，curl返回后grep文字就打印Vulnerable；同时有Failed writing body。文字命中只证明所取响应中出现匹配片段，不能排除转义文本、非HTML、静态页、错误页或不同消费者；失败项不能从成功集合消失。

保留参数替换范围、实际请求/原始响应、状态/截断和上下文，再追获准脱敏DOM中是否形成可执行结构及策略允许的无害效果。反射是候选阶段，存储/跨用户和实际执行另需证据；不沿历史链接发送载荷，不执行来源脚本或由curl文字标签确认XSS。

## 盲XSS候选字段与真实后续读者

旧列表将review/contact、password、地址、付款姓名和User-Agent列作盲XSS入口。字段可写或被记录不保证经过HTML/JS渲染；密码可能仅校验/哈希，付款字段还可能属于独立处理商/日志读者，User-Agent被代理/日志采集也不是浏览器执行。

用获准源码/已有脱敏记录中的普通唯一标记关联写入→保存/变换→实际后续查看者→上下文/策略/无害效果；各读取origin/主体与任务权限分别绑定。没有受控查看流程时保留缺口，不投递活动脚本给客服/真人，不触发支付或窃取Cookie。HttpOnly限制脚本读该Cookie而不是自动证明/否定同源已认证操作；能力可用隔离普通状态说明，不删除账号来扩大影响。

## 浏览器JavaScript控制台与操作系统shell

旧JSshell图有SVG/SCRIPT/IMG/BODY片段、循环附加document子节点、localhost连接，cookie输出foo=bar、pwd输出hook.html、domain输出example.com。这里的pwd标签描述页面，不证明进程工作目录；浏览器脚本能力仍受origin、会话和平台接口边界限制。裁剪的生成载荷不补完整语法或真实目标执行链。

先确定普通唯一标记经过何字段/后续读者、实际JS消费者及origin和身份，再独立证明任何原生桥接/本地进程能力。工具提示、持续轮询和回连文字不能替代这条桥梁；与既有Web脚本→本地进程边界条目合用。不运行生成器/循环、监听回连或读取Cookie。

## 拼写建议、词典替换与过滤后语法重组

旧帖和图把scrpt/confrm纠正为script/confirm，并称PHP pspell_suggest能绕WAF。词级建议、应用选词/拼接、输出编码和浏览器消费者是独立阶段；不能把示意翻译当库直接把整段HTML修复成程序。[PHP函数手册](https://www.php.net/manual/en/function.pspell-suggest.php)说明它返回候选拼写数组（2026-10-10核读接口/返回值）。

沿获准源码/隔离普通错词保留WAF看到的原输入、词典/locale与替换规则、拼接后字符串、最终输出上下文/CSP和无害结果；纠错后用文本输出是反例。检验重点是安全检查与最终消费者的表示不一致，而非所有PHP搜索自动XSS。不运行来源脚本、投递有效事件或按宣传推当前Cloudflare规则。


## 对话框、动态求值与文档写入的不同消费者

alert关键词被过滤后改confirm/prompt/eval/write，只是候选调用名称改变；这些API不具有相同参数、返回值或安全作用域。先确认输入已进入JS语法及实际函数绑定，再区分对话框观察、字符串求值和document等对象的写入消费者；单独出现eval或非限定write不保证执行或等于alert效果。

保留输出语境、净化后字节、真实对象/函数及策略，使用隔离合成无害标记解释消费，不从关键词未拦截推XSS或普遍WAF绕过。正常纯文本/不可调用值/不存在对象及拒绝策略作为反例，控制台原本可执行也不证明目标输入链。来源：[保存帖](https://x.com/i/status/1397760287353098241)。


## 字符串替换回调与已取得的JavaScript执行

旧帖把replace传入alert函数称“在RegExp中执行”。实际函数是替换回调：搜索值有Symbol.replace时由该消费者处理，可调用replacer接收匹配片段、捕获及位置/原字符串等参数。[ECMAScript RegExp替换算法](https://tc39.es/ecma262/multipage/text-processing.html#sec-regexp.prototype-%symbol.replace%)明确可调用替换值的调用步骤（2026-10-10核读）；这不是正则文本自动执行脚本。

源表达式要求先能执行JS并取得函数引用；要另证外来输入如何突破正常数据语境。document.cookie只是JS可见cookie，不包括HttpOnly秘密，空Safari控制台截图没有执行结果，更不证明所有浏览器测试。以已有脱敏源码解释调用/参数/返回即可，不求值源代码、读真实Cookie或将新语法同义变体独立计为漏洞。来源：[保存帖](https://x.com/i/status/1398828431278690304)。


## 其他主体写入将自触发变成跨读者执行

旧例自存储name XSS，CSRF链未成立，随后通过IDOR修改name并称升级P2。应拆成外来写入权→目标对象/租户绑定→保存字段→其他合法读者→实际输出/执行语境；对象ID可改不说明目标读者必然查看或同一字段被同一消费者渲染。

确认自己以本不应有的权限写入另一合成主体对象，再用获准读者流程区分纯文本、拒绝/清理、自己手动执行及跨主体触发。不能以P5/P4/P2标签补任何边，先前失败CSRF也不自动参与新链。影响跟实际读者身份及受控业务能力，达到最小因果证据即停，不强制串更多问题或操作真实他人资料。来源：[保存帖](https://x.com/i/status/1401786510689533952)。


## 冒号前缀的语句标签与URL方案

旧帖把stop、posting及其他单词后接冒号/调用列为多条XSS载荷。同样字节由JavaScript语句解析器或URL导航消费者处理时含义不同。[ECMAScript Labelled Statements](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-labelled-statements)给出LabelIdentifier冒号LabelledItem语法及语句求值（2026-10-10核读语法/求值段）；换标签名不会凭空建立外来输入到代码的边。

若在href或导航地址中，前缀先参与URL方案解析，任意标签不等于javascript方案；还要实际导航、策略/允许方案及执行语境。只用静态语法/获准合成普通标记区分消费者，不执行这些调用。已有控制台执行与目标外来输入执行分别记，同义标签变体不计独立漏洞。来源：[保存帖](https://x.com/i/status/1401796179252424708)。


## JSONP脚本消费与CORS凭据响应头

旧建议在缺Access-Allow-Credential true时用JSONP取数据；CORS对应响应头实际为Access-Control-Allow-Credentials。fetch/XHR读取、经典script执行与module请求是不同消费者，不能把任意JSON接口变成JSONP。目标需真实返回可执行回调，并在该请求方式下实际带上所需身份和返回敏感内容。

[HTML script说明](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element)区分classic与module，跨来源module要求CORS（2026-10-10核读script属性段）。JSONP还要核对回调名/净化、Cookie/SameSite/第三方策略、Content-Type/nosniff、CSP及跨源资源限制；缺某个CORS头不是所有这些前提的证明。只分析获准脱敏响应/合成公开回调，不加载真实私密JSONP或借挑战链接读他人数据。来源：[保存帖](https://x.com/i/status/1402236597664321543)。


## 团队名模板、悬停渲染与编译作用域

旧帖说团队名模板表达式回显为1，悬停图标弹窗，并称CSTI。先定位字段保存/读取、组件模板编译、表达式作用域、事件渲染及执行读者；单次算值和弹窗描述不说明服务端模板执行，更不能由self名称推每个引擎均暴露同一全局对象。

服务端模板渲染、客户端模板表达式及普通文字插值分开，绑定实际框架/制品/模式、净化后值、编译时点及策略。用获准隔离普通标记与不编译数据的反例解释输入是否成为程序，影响仍需真实跨主体读者。无脚本或悬停记录时保留证据缺口，不求值源表达式、访问团队或将CSTI自动标服务器RCE。来源：[保存帖](https://x.com/i/status/1402527470838947844)。


## IDNA主机映射与已取得的JavaScript调用

日语解说图用anchor设置圈字母HTTP主机，读取a.host得到alert，再通过top的计算属性和tagged template调用；正文代码还带自动链接样式，不能把保存文字与图中语法视为字节完全一致。URL主机映射、字符串值取得、函数引用和JS调用是不同消费者，图为控制台操作，没有外来输入破坏目标数据边界。

[URL Standard IDNA](https://url.spec.whatwg.org/#idna)规定domain parser ToASCII使用Unicode IDNA Compatibility Processing/UTS46（2026-10-10核读当前算法）；不能将所有URL规范化简化成NFKD或推广任意圈字符/浏览器结果。圈主机属性被解析不等于导航/请求已发起，无括号调用语法仍需先有JS执行。只审提供图/规范，不运行表达式或称Twitter已发现XSS。来源：[表达式帖](https://x.com/i/status/1402878611967774722)、[解说帖](https://x.com/i/status/1402881494066946048)。


## failure参数分支与真正的输出消费者

旧建议将failure从1改0后发现XSS，借Arjun/ParamSpider找隐藏参数。参数名字被发现、服务端接受/类型转换、分支变化、外来值进入输出与浏览器执行是各自一条边；0/1字符串也不能无证据当该实现布尔值或保证相同输出语境。

沿获准调用/路由、普通合成值与默认/缺省分支核对真实契约，排除未知参数被忽略、错误页反射、纯文本与输入被净化。只有分支差而无外来数据到代码消费者仍是线索；执行读者及业务能力另证，不运行来源载荷或全站隐藏参数探测。来源：[保存帖](https://x.com/i/status/1404750164347158528)、[文章预告](https://x.com/i/status/1405158219568148483)。


## ASP.NET URL会话段与ResolveUrl属性输出

旧图把ASP.NET cookieless会话段、ResolveUrl和生成script src连接起来。[System.Web会话文档](https://learn.microsoft.com/en-us/dotnet/api/system.web.sessionstate.httpsessionstate.iscookieless?view=netframework-4.8.1)说明会话ID可嵌入应用名之后的URL路径；嵌入路径并不独立证明引号逃逸或脚本执行。原图的版本范围只是原帖声明，不能推广所有.NET或Core。

绑定实际框架/会话配置、原始请求路径、URL生成调用、输出原始字节和浏览器属性解析，分开会话识别、链接重写、属性转义及最终读者能力。净化、固定会话格式、无该消费者与纯文本均为反例；本批仅审图和文档，没有运行载荷或启动服务。来源：[保存帖](https://x.com/i/status/1405285718386114562)。


## Grafana快照originalUrl从保存到按钮读者

图中POST /api/snapshots把originalUrl设为JavaScript URL，200返回快照字段，另一图有Open original dashboard按钮和弹窗；创建、持久保存、其他读者读取及实际点击仍需各自关联，不能由两图补跨用户链或全部匿名权限。响应中的删除/访问键不复制。

[维护者PR23254](https://github.com/grafana/grafana/pull/23254)明确快照originalUrl在渲染链接前净化，并列6.7.2里程碑。绑定实际版本/代码、创建者和读者、保存值/渲染值、URL协议策略与真实交互；API返回成功不等于执行。同字段后来的URL欺骗公告不可替代这次XSS根因。本批未创建快照或执行链接。来源：[保存帖](https://x.com/i/status/1406086490648502279)。


## dangerouslySetInnerHTML命中与外来HTML消费

搜索dangerouslySetInnerHTML找到的是潜在HTML消费者。[React文档](https://react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html)描述raw HTML/TrustedHTML进入DOM innerHTML；API存在并不证明外来输入、净化失效或可执行浏览器上下文。

沿实际数据源、转换/净化、可信策略、渲染分支和读者身份追踪，保留普通文本输出、可信常量、有效过滤及不被访问的分支作为反例。TrustedHTML类型也需核对实际产生策略，不能仅靠类型名认安全或漏洞。未运行前端代码、提交字段或执行脚本。来源：[保存帖](https://x.com/i/status/1406249885838544901)。


## Django技术500模板的局部转义与异常前提

create_user示例路径不是Django通用端点。[Django1.11.5发布说明](https://docs.djangoproject.com/en/5.2/releases/1.11.5/)将CVE-2017-12794绑定到技术500调试模板局部未转义，并要求DEBUG=True；不同于CSRF拒绝页仅显示“更多信息在DEBUG=True”的字符串。

绑定真实版本/调试配置、自定义路由、异常来源、输入如何到错误模板及浏览器读者，不能由路径名或含脚本的查询认当前漏洞。无异常、DEBUG关闭、已修复模板/自定义转义和纯文本为反例。本批没有创建用户、触发服务异常或执行载荷。来源：[保存帖](https://x.com/i/status/1406779605055270914)。


## 左尖括号后的空格与真实HTML状态机

旧列表的空格片段`< svg`不能在HTML Data到tag-open语境中直接成为svg起始标记。[WHATWG解析规则](https://html.spec.whatwg.org/multipage/parsing.html#tag-open-state)在此对非字母等分支报错并输出左尖括号，再回Data消费字符；只有真实前置变换或不同语境才可能改变结论。

保留原始字节、解码/过滤每层与浏览器当前状态，不替作者去空格再认原载荷有效。列表其他属性/JS片段各有适用语境，这一个反例既不证全部无效，也不补Cloudflare通用绕过。未运行HTML或脚本。来源：[原列表](https://x.com/i/status/1406997161875673090)、[同文帖](https://x.com/i/status/1407170521368719364)、[纠错帖](https://x.com/i/status/1407289453962579974)。


## Cisco SAML字段与特定VPN界面的浏览器读者

保存请求写SAMLResponse并配/+CSCOE+/saml/sp/acs页面弹窗，仍需原始POST响应、字段到输出上下文、实际设备/用户界面和交互条件关联。弹窗1不证明取得所有VPN账号或设备OS权限。

[Cisco公告](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-asaftd-xss-multiple-FCB3vPZe.html)限定受影响ASA/FTD版本及特定AnyConnect/WebVPN配置，明确攻击发生在用户的Web服务界面；不能推广所有Cisco设备/当前版本。核对实际消费者/转义、用户身份、补丁/配置与正常拒绝反例，本批没有提交SAML或访问设备。来源：[保存帖](https://x.com/i/status/1408290933322354688)。


## 代理修改响应与服务端反射的证据边

旧一分钟XSS步骤混写intercept response和在request尾加HTML。若仅在自己代理里改响应，浏览器弹窗可能完全来自本地注入；不能将其作为服务端可控输入到其他读者的证明。

保存修改前后的原请求/响应、实际改动方向/生效规则和不修改响应的正常对照，沿真实输入/输出上下文及读者能力核对。仅调试者看见脚本、本地override或错误页固定模板都是反例；参数名redirect_uri也不自动说明OAuth消费者。本批没有修改浏览器流量或执行载荷。来源：[保存帖](https://x.com/i/status/1409494340020342786)。


## reCAPTCHA脚本文本、DOM选择器与可执行上下文

SQLMAP求助图在浏览器显示reCAPTCHA JavaScript文本，包含getElementById的hello选择器与隐藏token字段。参数名/字符串出现在JS或页面、选择器选中元素与攻击者代码执行不同，工具类型标签不能代源/汇分析。

绑定原始响应Content-Type、实际脚本消费者、字符串编码与DOM分支，排除纯文本展示、静态代码或只改变元素选择。sitekey的出现不自动说明秘密泄漏或验证码可绕；第三方脚本本来正常运行也不证明注入执行。本次未运行页面JS、使用验证码key或提交请求。

来源：[保存帖1](https://x.com/i/status/1411268255835062281)。


## document.write标记、同栈重复行与报告状态

DOM Invader图document.write显示三条同栈值，标记位于属性和脚本边界；另一图两报告仍Triaged/Still being assessed。可控值进入汇、实际执行、独立根因数量和最终处理状态不能互换。

绑定原输入、真实输出上下文、变换及消费者调用栈，确认工具未自行补注入，再按根因/对象/读者去重。三条记录可能同一调用，评级不是当前修复重测；只有标记或未经原始链验证的alert图不计完整发现。本次未执行载荷或运行XSS Rush。

来源：[保存帖1](https://x.com/i/status/1411669682017366021)、[保存帖2](https://x.com/i/status/1411972248819306497)。


## DOM Invader合成origin与真实外部发送窗口

DOM Invader介绍和[官方消息设置](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/settings/web-messages)说明工具可修改origin、注入canary及生成消息。这能定位处理器候选，但在工具内接受合成origin不自动证明外部窗口可发送相同事件/数据到相同消费者。

保留原消息与工具变更、event.origin/source/data访问、目标窗口及调用栈，区分读取属性和真正完整验证。在获准自有环境用真实发送origin/窗口能力与严格验证对照判断可达；缺帧能力、源窗口检查拒绝或只本地合成事件是反例。本次未造消息或运行生成PoC。

来源：[保存帖1](https://x.com/i/status/1412426169576787972)。


## 函数别名逗号表达式与弹窗图的消费者证据

函数别名和逗号表达式建议依赖实际JS变量绑定、执行上下文及消费者；帖子称五个XSS却仅四张裁切弹窗，没有输入或调用栈。

保留原始输入、解码/过滤后的值、输出上下文和真实读者，区分脚本表达式、普通文本与工具本地注入。变量未定义、安全文本展示或不同WAF规则均可能否定假设；几张不同品牌弹窗不计独立根因或通用WAF绕过率。

来源：[保存帖1](https://x.com/i/status/1413495937138237443)、[保存帖2](https://x.com/i/status/1413535823836983300)。


## 邮件双斜线处理后的mailto消费者与HTML注入

email HTML图显示双斜线处理后mailto scheme，第二哈希图内容相同。链接方案和目标变化是HTML/URL消费者问题，不自动产生JS执行。

保留原输入、过滤后HTML、客户端解析的真实href、点击上下文与最终scheme/目标，区分纯展示、合法邮件地址和未经允许的导航。脚本执行需自己的可达读者与执行上下文证据；客户端差异不能以一个图推所有邮件客户端绕过。

来源：[保存帖1](https://x.com/i/status/1415247734261510150)、[保存帖2](https://x.com/i/status/1415638525702119425)。


## 百分号解码与JS URI错误处理的实际sink

编码JS URI示例结合析构onerror和throw，另文写prompt却声称alert。输入、解码后的文本与真正运行的函数需要逐层对应。

保存进入URI/HTML/JS的具体消费者、解码次数、过滤后字节、语法上下文和错误处理注册时机；函数名、模态窗口和错误回调不是同一机制。仅有字符串、被当普通文本、scheme不被消费或调用名称不一致都是反例，不以示例补实际Cookie读取。

来源：[保存帖1](https://x.com/i/status/1417105195658514434)、[保存帖2](https://x.com/i/status/1417412355604975621)。


## bogus comment与空HTML注释提前闭合

图片把单连字符形式概括为HTML5注释语法变化。按[WHATWG tokenizer](https://html.spec.whatwg.org/multipage/parsing.html#comment-start-state)，bogus comment和正式注释的开始状态是不同解析分支。

跟踪原始字符、markup declaration分支、bogus/comment-start状态与实际结束符；正式注释起始仍需两个连字符，空注释遇特定结束符可提前闭合。不能凭肉眼认为后续标签都在注释内；无真实输出上下文或只被文本展示是反例。只按规范纠正描述，未运行示例。

来源：[保存帖1](https://x.com/i/status/1417646726412972035)。


## jQuery预过滤与option包装的版本分支

截图两个CVE标题重复但内部示例不同；[官方3.5.0说明](https://blog.jquery.com/2020/04/10/jquery-3-5-0-released/)和[3.5.1解释](https://blog.jquery.com/2020/05/04/jquery-3-5-1-released/)分别说明htmlPrefilter正则处理和旧浏览器option包装相关分支。

区分原生innerHTML与jQuery .html/.append的实际消费者，记录真实加载版本、输入来源、预处理和兼容恢复配置。3.5.0修复不能被截图旧编号替代；已修复且未恢复旧行为、普通文本或未走该分支是反例，示例按钮未点击也未执行。

来源：[保存帖1](https://x.com/i/status/1419510462937325572)。


## Akamai ARL上游获取与展示origin的分离

ARL正文路径7/0/33/1d与截图7/100/33/1d不同，另含上游citysearch和SVG候选。CDN获取、缓存与浏览器展示origin是不同权威边界。

保留准确路径参数、上游URL、返回Content-Type、缓存/转换、实际document origin及输入控制者；不能将不同路径当同次PoC。上游自身页面、被当图片/下载或脚本未进入展示消费者是反例，不推广为所有Akamai部署或当前CDN绕过。

来源：[保存帖1](https://x.com/i/status/1421176297548435459)。


## InfluxDB查询错误到HTML提示的输出消费者

InfluxDB UI1.0/Server1.0图包含查询语法错误、反射和alert，数据库语句未成功。错误文本进入网页与数据库执行是两个消费链。

关联受控输入、服务端错误结构、前端实际DOM插入、编码/净化、origin及可触发的读者；同次正常错误作对照。只在自己查询页构造、文本展示或无跨主体传播是反例，alert截图不能补有效数据库查询、其他版本受影响或接管。

来源：[保存帖1](https://x.com/i/status/1422107719167709186)。


## 联系表单延迟后台消费的时间和读者身份

叙述联系表单两日后后台触发BXSS且截图含支持数据。输入保存、队列、后台读者渲染和回连是独立阶段，延迟不能由提交响应解释。

关联受控marker、提交时点、任务/记录ID、消费端origin/角色和同次回连；外部预览机器人、重复消费或无输入关联是反例。截图没有保存时不补真实用户数据读取，采用合成材料与最小证据，不投递外部脚本或联系支持人员。

来源：[保存帖1](https://x.com/i/status/1422890880722079749)。


## cookieless会话路径到输出属性的消费链

ASP.NET图A路径含引号/事件样文本并有alert1，另图只列ArchivedMedium报告。路径中的会话表示和网页输出sink需分别确认。

关联准确框架/配置、路径会话规范化、实际返回链接/form/属性、编码及读者origin，保存同次受控正常对照。普通URL文本、session不被采用或输出被编码是反例；无响应HTML时不能确定是哪一sink，更不能推当前所有ASP.NET均受影响。

来源：[保存帖1](https://x.com/i/status/1424646323714760709)、[保存帖2](https://x.com/i/status/1425076663398842389)。


## JS字符串转义与实体URI的解析顺序

productId单引号示例用编码空白换行及find(alert)，embed和formaction示例使用HTML实体。JS语法、HTML属性与URI解析是不同消费者。

保存原始输入、URL解码、输出位置、HTML实体后值、URI处理及最终JS语法；formaction还涉及真实激活行为。无点击、标签当文本、不受支持scheme或语法错都是反例；不能以变换后看似javascript和Dup叙述推WAF绕过，不执行示例。

来源：[保存帖1](https://x.com/i/status/1422702544195837964)、[保存帖2](https://x.com/i/status/1423148542126739464)、[保存帖3](https://x.com/i/status/1424070599505108993)。


## Base64文本与eval消费者的语法有效性

SVG/eval/atob片段被称绕过，但只读解码其字节为XSS haxor，没有可用JS表达式。文本能解码与eval成功求值不同。

逐层绑定过滤、HTML闭标签、SVG实际事件、Base64字节、JS解析和CSP；字符/标签被删、编码被改变、仅文本展示或语法无效是反例。不得静默换载荷再称原文成功，code闭标签是否必要只能由完整输出状态判断；本轮只解码未执行。

来源：[保存帖1](https://x.com/i/status/1424727426014265350)、[保存帖2](https://x.com/i/status/1423578366918025229)、[保存帖3](https://x.com/i/status/1422935296874893318)。


## TinyXSS长度与浏览器和能力条件矩阵

TinyXSS图列15样例与script/style/eval/frames、name/URL控制、innerHTML及浏览器标签。字符长度只在对应条件成立时有意义。

先确定实际source/sink、攻击者可控name/URL/子frame、CSP能力、渲染方式和真实引擎/版本，再判断候选语法和最终效果。缺控制源、CSP拒绝、脚本未走解析分支或不同浏览器是反例；菜单全选不表明目标同时有全部能力，未点击PoC。

来源：[保存帖1](https://x.com/i/status/1426038293586530304)。


## Ghost授权CodeInjection与支持聊天注入的边界

LiveChat HTML注入标题配Ghost CodeInjection设置图，说明主题header/footer用于插入代码。正常发布权限与低权聊天输入进入后台sink不是同一机制。

绑定actor角色、实际产品/模块、允许发布范围、受控输入字段及最终读者；比较合法管理能力与未经授权的输入消费。只有管理员设置页、空编辑框或标题错配是反例，功能名CodeInjection不能直接当漏洞或后台BXSS。

来源：[保存帖1](https://x.com/i/status/1426106700507992065)。


## JSON源码字符串与真实HTML消费之间的缺口

view-source图显示JSON值里iframe javascript字符串；另一正文把img onerror中的alert(whoami)当反射XSS升RCE。二者未给服务端命令执行链。

绑定响应Content-Type、真实页面读取点、DOM sink、转义/CSP、读者origin及实际浏览器效果。源码中的HTML、纯JSON展示、未定义JS标识符或仅弹窗是反例；whoami在该表达式里是JS变量，不是OS命令，不能补RCE。

来源：[保存帖1](https://x.com/i/status/1427098501545005062)、[保存帖2](https://x.com/i/status/1427305413758701577)。


## unescape百分号算法与源码词法转义的区别

两帖把百分号tab和反斜杠x/u写法归为unescape自动转换。已核对规范：unescape识别百分号起始的两位hex或u加四位hex；字符串字面量的反斜杠转义在词法阶段处理。

先保存函数收到的真实字符串/码元，再标注JS源、HTML entity、URL或JSON处理层；源码已转tab与字面反斜杠仍保留是关键对照，不能仅看展示形式判函数解码。依据：[unescape算法](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-unescape-string)、[字符串词法规则](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-literals-string-literals)。本轮未执行来源脚本。

来源：[保存帖1](https://x.com/i/status/1432349872523448327)、[保存帖2](https://x.com/i/status/1432351172501942275)。


## 反射扫描HTML标签分类与浏览器执行证据

Reflector2.5图列POST200、Reflected Yes、script HTML tag、Vulnerable Yes或Maybe，并显示两个奖励条目。

保存原请求/字段、响应反射字节和上下文、完整DOM、读者origin、浏览器/CSP及实际受控marker执行；字符串匹配、统一200、工具标签、奖励或未触发事件是反例。测试完成日志只说明工具终态，不能把反射和脚本执行合成一项。

来源：[保存帖1](https://x.com/i/status/1436284358671970306)、[保存帖2](https://x.com/i/status/1437364056927653889)。


## 挑战规则的读者域和浏览器矩阵

0921页面规则指定该域、Chrome/Firefox、域对话框、非selfXSS/MITM和时间范围。

将限定域、产品/浏览器版本、读者触发方式、执行origin和实验终态逐项绑定；别的域、自操作控制台、仅支持浏览器选择、MITM或无受控marker是反例。截图中的历史活动规则不提供今天测试真实网站的授权，未打开挑战或执行payload。

来源：[保存帖1](https://x.com/i/status/1437789926951727111)、[保存帖2](https://x.com/i/status/1441271859245305856)。


## 事件属性中的脚本加载与分类标签错配

正文onfocus接jQuery.ajax dataType script；图Search输入却分类Stored，triaged high但无执行/持久化截图。

区分反射/持久存储、真实HTML属性/JS解析、jQuery及版本、event触发、CSP/外部加载和读者origin；$不存在、只输入被接受、库未加载、外部脚本被阻止或无其他读者是反例。分类和奖金不证明Stored或特定WAF普适绕过，未加载远程脚本。

来源：[保存帖1](https://x.com/i/status/1438202622041755648)。


## 上游身份邮箱到下游显示sink的完整类型链

正文称提供者允许特殊邮箱，用其登录别的服务可能XSS，未保存具体字段/DOM。

绑定issuer/client、已验证email声明及真实性、account linking、显示上下文、转义、读者origin和最终执行；合法邮件字符串、下游转义、值没显示、不同origin或无读者触发是反例。输入格式接受和XSS分开，不能据上游邮件含字符补下游漏洞。

来源：[保存帖1](https://x.com/i/status/1439612061458128902)。


## 自操作XSS到其他读者以及客户端取回的边界

正文selfXSS加CSRF、缺X-XSS-Protection会变严重，又以window.location去自有server称XSPA。

验证是否可获准地种植到另一自有读者、cookie/SameSite/CSRF、持久状态、origin和实际DOM执行，另辨浏览器导航与backend取回；仅自己控制台、无法种植、缺旧header、导航回调或无server消费是反例。缺header不是成功链，客户端callback不证明SSRF/内网访问。

来源：[保存帖1](https://x.com/i/status/1440419533290827786)。


## 符号码元生成与片段调用终态的分离

代码图从第21行起，用类型强转和字符串索引拼constructor/Function/alert字样；标题称无字母数字括号调用，缺最终调用片段。

分实际source code、字符字面量与运行字符串、生成函数/调用语法、CSP和读者origin；仅字符串拼成、comment有字母、缺前后段、语法失败或无实际alert是反例。裁切片段不证明整payload满足字符约束/执行，本轮未执行代码；另alert域截图仍需source/sink/trigger。

来源：[保存帖1](https://x.com/i/status/1441165012727435267)、[保存帖2](https://x.com/i/status/1441062037124042772)。


## 注册查询参数进入meta属性的浏览器读者

阿拉伯语帖述拦注册请求改payload与cookie，图显示registerdo参数闭合meta og:url属性并形成script，另图浏览器弹出cookie样式值。

绑定GET/POST区别、响应实际属性字节、HTML解析/DOM、受害者origin及触发前提，使用无秘密marker验证；单人自注入、无法让另一读者访问、HttpOnly不可读或无法确认cookie认证价值是反例。截图支持该浏览器观察，不补出全部cookie可读/会话接管，秘密值不复制。

来源：[保存帖1](https://x.com/i/status/1442871467025203202)。


## 无效UTF8触发旧登录页的版本和回退路径

cPanel帖有loginuser事件payload，图SEC596描述无效UTF8触发LegacyLogin输出编码不足，列修复11.98.0.8和11.94.0.16。

把字节解码失败→旧模板选择→用户字段输出→focus/fragment触发分开核对，记录安装build、具体浏览器和CSP；新模板、已修复、属性正确编码或无法触发是反例。图是历史公告摘录，不据此判当前cPanel均受影响。

来源：[保存帖1](https://x.com/i/status/1443092453809065986)。


## BBCode转换后的HTML与原文属性界面

正文提醒BBcode可有XSS，但外链实现未保存；另帖lng值闭title后iframe，未给响应。

定位BBCode解析器/允许标签与属性、转换后编码和最终读者DOM；title文本结束、iframe插入和脚本执行分别取证，嵌入跨origin不自动读取外站或当前cookie。纯文本BBcode、正确编码、sandbox/CSP或只能自看是反例。未加载图中外站scriptlet。

来源：[保存帖1](https://x.com/i/status/1445431001199611907)、[保存帖2](https://x.com/i/status/1445717253928808453)。


## cookie弹窗的脚本上下文与接管能力

Huawei协作帖图片只有裁剪地址栏与cookie弹窗，没有输入/响应上下文。

记录完整触发输入/响应、读者origin、浏览器/交互/CSP与自有跨读者marker，区分安全演示、自XSS、认证cookie与非认证WAFcookie；单个弹窗、缺source或cookie名称本身是反例。不能补会话接管或第三方平台登录能力，不复制cookie或联系协作对象。

来源：[保存帖1](https://x.com/i/status/1446097299965362177)。


## Nexploit 的 HTMLi 分类与实际 HTML 消费者

图显示 WAVSEP JSP 输入、HTML 标记示例和 127 LFI、20 SQLi、55 HTMLi 等工具数量。

从原始输入到响应上下文、实际 DOM 节点及用户动作逐层确认。HTML 注入可改变链接、表单或页面内容，仍需真实消费端及影响；它不自动等于 JavaScript 执行、WAF 绕过或 RCE。分类数字与工具页面不等于独立已确认漏洞数量。

来源：[保存帖1](https://x.com/i/status/1447171751838953477)。


## 资料脚本示意与 HTML 图片的实际读取链

资料注入图把 document.cookie 字样拼进脚本 src 的示意，另一正文描述修改上传字节及 MIME 后访问文件页面。

记录保存字段/文件、最终响应 Content-Type、Content-Disposition、来源域、CSP、真实 DOM 和触发交互。示意字符串不是外传回执，允许 text/html 也不证明被同源活跃文档读取；隔离域、下载响应或转码是反例。HttpOnly、脚本可读范围和受害者可达性决定影响，不读取他人 cookie。

来源：[保存帖1](https://x.com/i/status/1449347705797373952)、[保存帖2](https://x.com/i/status/1449988709898592261)。


## 邮件 HTML 注入的 mailto 方案与网页脚本差异

卡片先展示 HTTP 链接和删双斜杠，后称换 mailto 可绕过；没有邮件客户端回执。

比较过滤前后字节、HTML 节点、链接 scheme、真实邮件阅读器及点击后的处理端。mailto 可能仅唤起编写邮件，与站内脚本执行或 HTTP 导航不同；可点击链接仍需欺骗/可控内容和用户影响。缺少实际客户端、标签被转义、净化或不触发均是反例。

来源：[保存帖1](https://x.com/i/status/1451181629448155143)。


## 图片文件名在元数据、URL 和 HTML 属性中的消费者

正文把事件和标签形态放进 png/svg 文件名，未保存真实服务器输出或浏览器回执。

把名称持久化、编码/规范化、列表文本、属性、链接 URL 与文件内容解析分开审查。同一名称在安全文本、百分号编码 URL 或静态下载中不执行；仅当实际 HTML 消费端将可控名称转为活跃节点/事件时才形成假设，需自有无害 DOM 标记及真实阅读上下文。扩展名本身不证明 XSS。

来源：[保存帖1](https://x.com/i/status/1451822235497418756)。


## HTML 注入在订单反馈阅读者中的条件

正文自述订单反馈存储 XSS，配图却是 Google Hangouts GET，没有反馈读者或脚本回执。

记录订单阶段、可控字段、存储版本、实际阅读角色、响应上下文和无害 DOM 标记。安全文本/链接、净化后的节点、独立沙盒或只有发送者可见均须纳入反例。配图消费者不同不能与 Alibaba 自述拼成一条已验证链，不复制图中 cookies。

来源：[保存帖1](https://x.com/i/status/1451932492261257222)、[保存帖2](https://x.com/i/status/1452562453498236929)。


## Lucee missinginclude 路径错误页与实验弹窗

一图为Firefox Lucee5.2.9.31错误页与domain弹窗，另一为自有Neuralegion实验firstname页面rXSS标记。

按应用/构建、输入位置、原始响应、实际DOM、触发事件、阅读者和标记关联分别记录。不同实验不能合并成生产影响；console手输、预置lab、错误分支关闭、路径被转义或沙盒为反例。历史弹窗仅支持其特定观察，不证通用RCE、存储或ATO。

来源：[保存帖1](https://x.com/i/status/1454078934514024454)、[保存帖2](https://x.com/i/status/1455822343125733376)。


## application/json 数据块与 HTML 结束标签

AMP图把alert样式字符串放title/docUrl的JSON中，没有执行回执。

WHATWG规定数据块不直接按JavaScript处理，但HTML解析仍需限制script内容中的结束标签序列，且作者脚本可能另消费数据。分别检查原始HTML字节、结束标签安全性与JSON parse后的DOM使用；安全数据存储/文本输出是反例。不能只因type判永无XSS，也不因出现alert判已执行。[WHATWG script](https://html.spec.whatwg.org/multipage/scripting.html#restrictions-for-contents-of-script-elements)。

来源：[保存帖1](https://x.com/i/status/1456138253371854849)。


## 双引号反斜杠与 JavaScript 语法的消费顺序

帖子列双引号逃逸、globalThis、正则source、call/apply与HTML数字实体编码，没有真实浏览器成功回执。

固定原始响应字节和实际HTML属性、script或DOM消费者，逐层记录实体/URL解码、字符串转义、JS解析、事件触发及CSP。单个过滤器不识别某拼写不证明代码可达；反斜杠奇偶、文本节点、非活动属性和事件不触发是反例。只做静态上下文分析，不执行拼接payload或绕过在线WAF。

来源：[保存帖1](https://x.com/i/status/1458057536658096133)、[保存帖2](https://x.com/i/status/1458176429485694981)、[保存帖3](https://x.com/i/status/1459722794023804930)。


## ENS 名称与客户端校验后的存储读者

正文把ENS名称、绕过前端校验的字段、后台读取UA/IP及邀请邮件HTML作为入口，图片多为封面或报告标题。

外部名称/表单/日志/邮件输入只有到达实际读者并进入活动上下文才支持注入影响。分别追存储、模板编码、邮件客户端、后台身份和触发方式；文本显示、HTML无脚本呈现、隔离文档或没有后台阅读是反例。不注册链上名称、不发送邮件或远程回调，不以奖励补出完整执行链。

来源：[保存帖1](https://x.com/i/status/1458066290694758404)、[保存帖2](https://x.com/i/status/1459113640020250624)、[保存帖3](https://x.com/i/status/1460678440080793606)、[保存帖4](https://x.com/i/status/1461384618196627459)。


## javascript URL 跳转与最终脚本来源

DOM帖子只有accepted标题；NASA图分别展示HTML标题及域名弹窗。

独立保存入口、URL解析/导航方式、实际sink、点击/事件要求、最终origin与浏览器回执。HTML节点呈现不是JS执行；报告标题、被阻导航、其他origin及示例页为反例。历史弹窗只支持该场景，不外推ATO或所有同名域；不重放到目标。

来源：[保存帖1](https://x.com/i/status/1459325903901642765)、[保存帖2](https://x.com/i/status/1460306222100353035)、[保存帖3](https://x.com/i/status/1461226181429104641)。


## CSP 图表的 fetch fallback 与 Report-Only

两张完整CSP图把default-src和各种指令并列，并简化为允许/禁止资源。

根据真实响应、enforce/Report-Only、nonce/hash及实际消费者逐项确定有效策略。[CSP3](https://www.w3.org/TR/CSP3/)中default-src是fetch指令的fallback，并不接替所有安全指令；script元素/属性还存在各自回退链。Report-Only用于报告而非阻止，meta也有位置与功能限制。缺CSP不证明漏洞，拒绝活动执行、文本读者或不同响应策略为反例，不执行图中的脚本。

来源：[保存帖1](https://x.com/i/status/1460276604186337282)、[保存帖2](https://x.com/i/status/1461208413665259520)。


## Blind XSS 通知数量与实际后台读者

图为XSS Hunter的30/70 notifications及payload fired标题；正文猜登录UA被管理员页面消费。

关联唯一提交、实际时间、阅读主体、原始输入、DOM上下文和独立触发回执，排除自测、扫描器、预览与重复通知。通知数不等于受害管理员数，日志存储不等于脚本执行；转义显示或没有真实阅读为反例。不发送callback或注入线上日志，不记录完整会话。

来源：[保存帖1](https://x.com/i/status/1460311558609850374)、[保存帖2](https://x.com/i/status/1460678440080793606)。


## 自带参数在 Request.Form 异常页中的读者

BYOP图有新增参数的POST、500 potentially dangerous Request.Form错误及浏览器弹窗；另帖说UA引号报错就有发现。

把输入→校验异常→错误模板→HTML/JS解析视为实际链，记录原始响应字节、同origin、浏览器/版本与触发条件。500可能仍被活动页面消费，但错误信息本身不证明执行。固定错误模板、转义文本、不同origin或无事件为反例；UA解析错误和图中历史弹窗独立，不能由任意报错推断新洞。

来源：[保存帖1](https://x.com/i/status/1462742972890497025)、[保存帖2](https://x.com/i/status/1463498983670620167)。


## 跨字段拆分属性的最终 HTML 结构

图把q与color两个字段分开，使最终img示意出现额外属性并标Filter Bypassed，没有真实浏览器回执。

检查每个字段的编码、模板拼接分隔和最终浏览器DOM，输入单独过滤不保证组合安全。图中混入with/color等属性仍需实际HTML解析与事件触发对照；引号编码、文本插入、无活动事件或拼接不同为反例，不按绿色标签当运行成功，不执行示例。

来源：[保存帖1](https://x.com/i/status/1463540280838135815)。


## href 字符实体的准确拼写与 URL 规范化

正文给Tab/colon/NewLine候选，但示例含tap以及文字NewLIne等不一致拼写，未存浏览器回执。

[HTML字符规则](https://html.spec.whatwg.org/multipage/syntax.html#character-references)要求命名引用匹配准确大小写；[实体表](https://html.spec.whatwg.org/multipage/named-characters.html)分别定义Tab、NewLine和colon。[URL解析](https://url.spec.whatwg.org/#concept-basic-url-parser)会移除ASCII tab/newline，仍需实际HTML解码后的href、scheme校验、点击和执行条件。错误拼写、文本输出、scheme拒绝或CSP为反例，不把任意实体拼写说成必绕过。

来源：[保存帖1](https://x.com/i/status/1465392136187039745)。


## AEM setPreferences 错误 MIME 与未完成执行

图有setPreferences后缀变化、4xx响应、text/javascript及Invalid keymap文字，h1样式字符串未显示成HTML；正文承认无法绕Content-Type。

保存响应原始字节、Content-Type/nosniff、实际文档/脚本消费者、浏览器和触发事件；直接导航文本反射与活动HTML/JS不同。错误MIME、语法错误、安全文本或没有真正执行为反例，奖励不能补这个缺口。不执行模板、注入脚本或改线上响应类型。

来源：[保存帖1](https://x.com/i/status/1465394815042916352)。


## title noscript 图中的解析模式

图建议闭合title或noscript逃逸并混写unscript，没有当前页面/执行记录。

按HTML/XML、所在位置、scripting flag、原始字节和实际后续sink判断。[HTML语法](https://html.spec.whatwg.org/multipage/syntax.html)对raw/escapable raw text结束标签有限制，[noscript规定](https://html.spec.whatwg.org/multipage/scripting.html#the-noscript-element)行为取决于脚本是否启用。元素名字不能保证普适安全/绕过；正确转义、不同解析模式、无活动consumer或CSP为反例，不执行图中script。

来源：[保存帖1](https://x.com/i/status/1465403313101307904)。


## 数字实体括号与奖励金额的解码层

正文列数字实体编码的SVG函数括号，图片只有两项XSS重新分级各1000及两项信息泄露合计250；另帖为偏好payload。

分别保存URL百分号解码、HTML实体、JS事件语法、实际reader和执行回执。奖金额可以归档为阶段，不能由2250外推出单漏洞/所有Cloudflare规则；payload偏好无适用保证。文本输出、没有实体解码、事件不触发或不同规则为反例，只分析字节不重放。

来源：[保存帖1](https://x.com/i/status/1465425850329796619)、[保存帖2](https://x.com/i/status/1465439144285462538)。


## Base64 FROM_URL 与 Continue 按钮消费者

完整图有activationKey/LANGUAGE/FROM_URL、Base64注入片段和点击Continue步骤，第二图为fixed/sw ag邮件。

追每层URL/Base64解码、实际按钮handler、后续字符串/导航/JS消费者和活动origin，保留需要点击的条件。Base64接受不是自动XSS；安全URL赋值、校验拒绝、token无效、未执行或只回显为反例。不复制activationKey、注册/激活账号或点击归档链接。

来源：[保存帖1](https://x.com/i/status/1465704521233932311)。


## 未闭合资源属性与 dangling markup 的请求证据

完整示意将未闭合img src包裹后续CSRF/email文字并标exfiltrated，没有实际浏览器出站回执。

追注入位置、HTML解析出的最终资源URL、浏览器限制、CSP与真实出站消费者；HTML注入、JS执行和数据泄露是不同能力。后续引号/空白、浏览器拒绝、资源策略阻止或只是示意为反例。仅用脱敏自有标记解释读者，不发送外部资源请求或真实token/PII。

来源：[保存帖1](https://x.com/i/status/1465982647713165314)。


## Markdown 多行和引用链接的同一 URL 校验

正文提Multi-line与reference style链接造成两种Markdown XSS，没有保存源码/渲染回执。

追实际Markdown库/版本、解析后的链接目标、HTML输出/清洗、scheme白名单与浏览器消费者。不同语法需收敛到同一安全目标判断；文本输出、引用未解析、拒绝活动scheme或库已修补为反例。保留候选，不从issue标题补当前所有Markdown漏洞或执行内容。

来源：[保存帖1](https://x.com/i/status/1466124295873208321)。


## 不可编辑 dropdown 的请求值与真实存储

图为Feature request下拉菜单与Submit，正文建议拦截改成XSS/BXSS值。

前端不可编辑不提供后端可信性，追枚举校验、字段存储、后台/邮件读者、输出上下文和触发身份。拒绝未知枚举、安全文本、没有后续读者或只回显为反例；控件可篡改不直接证XSS。不提交工单/邮件或远程回调。

来源：[保存帖1](https://x.com/i/status/1467495413372518404)。


## SVG 上传请求与真正脚本消费者

图可见image/svg+xml请求体及脚本，未展示存储后读取/执行；正文SVG结束标签亦不完整。

绑定服务端接受、存储URL、响应MIME/下载方式、嵌入上下文、CSP与实际读取者；图片显示、独立文档、内联解析等消费者不能混同。仅发请求、强制下载、过滤脚本、未调用或无执行回执为反例；不访问cookie或发送外链。

来源：[保存帖1](https://x.com/i/status/1469963014770098176)、[保存帖2](https://x.com/i/status/1469974869060112388)。


## 反斜线数字引号实体与弹窗的上下文

正文字符串混反斜线、数字引号实体和confirm；图只弹窗1且origin遮挡，没有完整注入位置。

保留原始字节、HTML实体解码、JS字符串边界/转义奇偶、真实触发者和origin对照；只有适用消费者才可能执行。未解码、正确编码、纯文本/不同上下文或无原始请求为反例，不推广为通用filter bypass。

来源：[保存帖1](https://x.com/i/status/1470857654243246083)、[保存帖2](https://x.com/i/status/1471189590169980928)。


## 版权表单 blind XSS 与创作者能力链

正文称假版权通知触发创作者blindXSS/ATO，图只1632奖励及禁止未经许可披露弱点的历史通知，没有真实接收者/会话能力。

只提炼输入→存储/消息→渲染读者→origin/权限→受保护动作的链，在自有实验核对真实读取者和最终能力；callback/奖励不等于ATO。自己的读者、编码文本、无最终动作或只标题为反例，不发假通知、版权投诉、邮件或提取会话。

来源：[保存帖1](https://x.com/i/status/1471744751913168897)。


## XSSR 发现标签与实际浏览器执行上下文

保存图同时出现XSS FOUND标签及查询页弹窗；弹窗显示一次浏览器执行，查询和来源部分裁剪，仍不能直接证明其他主体读取或受保护能力。

固定实际页面、输入位置、响应字节、DOM/脚本消费者和测试主体；用自有无副作用标记保留未变异对照及最终执行来源。仅扫描标签、自己的控制台、不同源页面、裁剪看不见消费者或无法让实际受众到达为反例。发现、执行、跨主体影响与受理分开，不运行归档脚本或访问归档目标。

来源：[保存帖1](https://x.com/i/status/1469254214983434242)。


## XMB 嵌套 BBCode 到事件属性的消费者链

完整保存嵌套url标签文本，图是localhost私信admin到admin和弹窗1，渲染正文混入onclick片段。

记录BBCode解析、链接构造、属性编码与最终DOM事件，比较普通标签和嵌套标签的自有无副作用输出；受众、存储与触发动作分开。只localhost自投、不同版本、安全序列化或不进入事件上下文为反例，不把CVE题名当所有部署验证，不运行归档脚本。

来源：[保存帖1](https://x.com/i/status/1473739430468980745)、[保存帖2](https://x.com/i/status/1476545420897570816)。


## 赋值调用与 optional chaining 的演示边界

正文给赋值confirm和注释/optional chaining变体；后图明确在chrome new-tab控制台自行调用alert。

JavaScript语法可执行与应用输入能进入脚本是两件证据，需真实响应/DOM、编码、语法位置和受众；用自有安全标记比较。控制台粘贴、来源遮挡、不支持语法、被转义或无其他读者为反例，不将语法演示叫WAF/XSS成功。

来源：[保存帖1](https://x.com/i/status/1473980395389554691)、[保存帖2](https://x.com/i/status/1475555795995865088)。


## Content-Disposition 文件名到响应头和 HTML

正文称可控文件名进入Content-Disposition后CRLF修改Content-Type到text/html，无保存原始响应或受众。

按字节追踪文件名校验/编码、头序列化、代理/协议处理、最终MIME及内容消费者；自有标记比较拒绝与正常读回。换行拒绝/编码、HTTP2处理、attachment下载、无可控HTML或无其他受众为反例，不把头反射直接认XSS。

来源：[保存帖1](https://x.com/i/status/1475627378827309061)。


## 地址栏 javascript 弹窗不证明反射 XSS

两图地址栏是javascript:alert，登录页弹窗及cookie文本；没有保存从服务器/DOM输入到执行的请求。

固定真实来源、注入入口、最终消费者和受众；本人书签/地址栏执行与站点反射分别记录。控制台/地址栏自执行、无可控输入、只有自己的cookie或来源遮挡为反例，不复制/使用cookie或认登录ATO。

来源：[保存帖1](https://x.com/i/status/1475760783233478662)。


## 被遮挡的 WAF 变体与执行现象

普通script关键词被blocked，另一截图alert3且关键变体被遮挡。可记录一次边缘拒绝与浏览器执行差异，不能还原万能payload。

固定入口/会话/字节/响应编码和真实DOM消费者，在自有标记比较；仅console自执行、不同路径/策略、遮挡语法或无受害者入口为反例。WAF接受、HTML反射、JS执行及跨主体影响分阶段，不传播猜测载荷。

来源：[保存帖1](https://x.com/i/status/1477372288916140032)。


## JSON 正常出口与 HTML 错误出口

两图正常请求API query中SQL后附HTMLonclick标记，错误页显示SQLsyntaxerror和alert287719；正文说异常改text/html，alt为scanner截图。

在自有合成错误比较正常JSON/错误HTML的ContentType、编码、可控字段与实际DOM/交互，保留请求→异常→渲染链。手工点击/已有JS控制、只文本反射、不同来源或无跨主体入口为反例；浏览器执行不证明SQL语义/认证绕过，不运行图中SQL。

来源：[保存帖1](https://x.com/i/status/1479167037234679810)。


## postMessage 出站追踪与被改写 CSP

三图分别outgoing info记录CSRF/origin*与stack、headless模板改响应CSP为宽松unsafeinline/unsafeeval，以及入站DOMXSS/出站泄露分类。

保存原站策略与实验策略，分别追踪targetOrigin/接收窗口、receiver origin/source校验、消息data到sink及可达读者。在自有无敏感消息比较正常/陌生origin；仅hook输出、改CSP才成功、发送但无接收者或安全sink为反例，不上传CSRF/token，不运行模板或弱化真实页面防护。

来源：[保存帖1](https://x.com/i/status/1479497566916165632)。


## 创建 SCRIPT 需要先有 JavaScript 消费入口

正文createElementSCRIPT+src+append加载外部代码，图有alertOPENBUGBOUNTY；创建元素自身需要已有JS控制/可达代码入口。

用自有无外联标记追踪原反射上下文、DOMsink、append时机和真实CSP/TrustedTypes，区分既有执行与过滤突破。只console、自有脚本、被阻src/无append为反例；不能推成任意XSS过滤万能绕过，不加载图中脚本。

来源：[保存帖1](https://x.com/i/status/1479854901362450434)。


## fragment 训练样例与 HTTP 参数的区别

正文把查询串/hash加123与XSS相连，alt和图片显示训练文档页面onclick及alert。fragment通常由浏览器处理，不能把它当作已送达服务器的参数。

用自有静态fixture分别标记query与fragment，追源字符串、DOM解析/事件消费、真实CSP和交互。只有扫描器/教程、自改页面、无消费者或脚本被阻为反例；alert只能说明该执行上下文，不证明跨主体影响。

来源：[保存帖1](https://x.com/i/status/1480504130993012740)。


## SVG animate 改 href 的交互前提

完整SVG animate/xlinkhref片段带实体编码javascript，另帖有十进制/十六进制与前导零变体。保存字符串没有跨浏览器执行证据。

自有静态fixture追URL解码→HTML/XML实体→SVG/SMIL属性更新→链接交互和真实CSP，记录命名空间与消费者。纯文本、错误namespace、未触发、策略拦截或解析器拒绝为反例；不加载归档外链脚本，不称通用Chrome/WAF绕过。

来源：[保存帖1](https://x.com/i/status/1480925381851033602)、[保存帖2](https://x.com/i/status/1482430543090257921)。


## Grafana constructor 字符串的语法与上下文

保存snapshot/dashboard constructor表达式与alert片段引号不完整，未保存对应版本、入口解析或执行交换。

先作为不可信文本核编码层、完整语法、属性/表达式消费者和实际页面策略，以自有静态无外联标记比较普通字符串与真正语法位置。畸形片段、展示在文档、无constructor调用或受策略阻断为反例；不擅自修成可执行载荷后称原帖已证明漏洞。

来源：[保存帖1](https://x.com/i/status/1481221447368339456)。


## NOSCRIPT、title 与 innerHTML 的解析分层

正文完整h1/NOSCRIPT/p/title/外部script组合，另帖说innerHTML插script不执行但事件属性仍可能运行。两种插入/解析上下文的行为不能混用。

自有静态fixture保留HTML/XML模式、scripting标志、插入API、namespace、事件和原始CSP/TrustedTypes，比较纯文本与DOM节点。只HTML呈现、script inert、无事件或被清理/策略拦截为反例；回调缺失不是全局安全，显示标签也不证明blindXSS，不取回外部脚本。

来源：[保存帖1](https://x.com/i/status/1481256393214676999)、[保存帖2](https://x.com/i/status/1483158016044142594)。

语义校核：[MDN innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)。


## message.data 到 document.write 的接收契约

spotcode图监听message并直接document.write(data)，可见代码没有origin/source判断，但未存真实页面/策略和发送者可达性。

静态追消息发送窗口、接收器注册/时机、data类型、HTML消费者及CSP；自有fixture比较可信/非可信来源和不可达窗口。仅代码片段、隔离世界、接收器不可达、上游正确过滤或策略阻断为反例；危险sink需要实际数据通路，不发送消息到真实页面。

来源：[保存帖1](https://x.com/i/status/1481507403338518531)。


## username 进入 img alt 的属性逃逸边界

图保存username引号/onload进入img alt的代码/呈现，正文称stored XSS，重复帖子复用。未保存完整DOM、存储和另一读者执行记录。

自有静态fixture追原字符串→属性编码→浏览器节点→保存/后续渲染/事件和CSP，比较普通字符/安全编码/无事件。纯文本、正确属性转义、无存储读者或策略阻断为反例；document.cookie表达式不证明HttpOnly泄露，不执行归档事件。

来源：[保存帖1](https://x.com/i/status/1482131903742414854)、[保存帖2](https://x.com/i/status/1482223217494433796)。


## Shopify HTML 编辑器未保存状态的执行边界

正文称admin/product XSS resolved/high/1000，图为Unsaved changes编辑器中的img事件属性，没有显示保存成功、DOM执行或另一主体读者。

自有静态fixture分输入编辑、存储、预览/后续读者、浏览器事件和CSP；正常文本、安全编码/拒绝和真正节点各留证据。未保存、源码编辑显示、本人主动执行、无后续读者或策略阻断为反例；奖励状态不替代服务器/浏览器链，cookie表达式不等于HttpOnly泄露。

来源：[保存帖1](https://x.com/i/status/1484554895399157763)。


## POST XSS 加 CSRF 不自动成为 stored

完整正文写POSTXSS=P5、加CSRF=storedP3，图只是triaged/stillassessed标题。跨站送入与保存后新读者消费是两个不同边界。

自有静态fixture区分请求方法、浏览器携带凭据/来源验证、服务器存储、后续渲染/读者和CSP，分别比较正常/拒绝与真实持久化。仅POST、回显、无存储读者、CSRF被拒或自执行为反例；不能用公式定stored或统一等级，不向他人账号写入。

来源：[保存帖1](https://x.com/i/status/1486089011823357965)。


## CRLF 到 HTML 响应消费的两个边界

正文给编码CRLF、响应头及HTML脚本片段，图只给ReflectedXSS accepted邮件。先核输入是否进入真实响应头、解码/CRLF是否合法，再核正文边界、MIME、浏览器上下文和CSP；改变旧X-XSS-Protection字段不自动关闭所有防御。

离线自有合成响应比较普通值、安全拒绝、头部编码和无害HTML标记；只有字符串回显、邮件、错误响应或未被HTML消费者解析为反例。奖励不能补原始交换，也不能由cookie表达式推出可读HttpOnly。

来源：[保存帖1](https://x.com/i/status/1487822309981564929)、[保存帖2](https://x.com/i/status/1488276085460508673)。


## message listener 正则命中与 DOM sink

正文多次用getJS/httpx正则找addEventListener message；配图是奖励列表或仓库封面，没有真正handler。正则候选可能漏变量、包装器、空白和其他注册形式，也可能匹配注释。

静态追事件origin/source、消息schema、可信窗口关系、字段变换到DOM sink及CSP。自有无外联fixture比较正确来源、错误来源、纯文本及拒绝。只有listener、扫描命中、无危险sink或严格校验为反例；不能将全部message监听当DOM XSS。

来源：[保存帖1](https://x.com/i/status/1487933582354092039)、[保存帖2](https://x.com/i/status/1489122903379812352)、[保存帖3](https://x.com/i/status/1489331257737719817)、[保存帖4](https://x.com/i/status/1491313371647705089)。


## href 中 javascript scheme 仍需真正导航

正文给href用户输入及javascript scheme，并称open redirect→RXSS，模糊图只见hacked对话框。属性无需破引号只是特定上下文，不能推出所有重定向执行脚本。

静态核URL解析、scheme限制、导航消费者、用户动作、origin与CSP，离线自有纯URL/拒绝/无害导航标记对照。HTTP Location被拒、仅文本、策略阻断或没有真实消费者为反例；模糊弹框不证明接管。

来源：[保存帖1](https://x.com/i/status/1488170820803334145)、[保存帖2](https://x.com/i/status/1488717102923988994)。


## og:image 到 SVG 缩略图的二次渲染

正文连续两条说抓取链接metadata并将evilSVG作为缩略图；图保存og:image示例、卡片、遮挡对话框和StoredXSS viaSVGmetadata奖励通知。抓URL、存图和渲染是三段。

静态核URL来源/协议、抓取/转换、存储域/MIME、img或document消费者、CSP及另一读者；离线自有无害SVG比较转码/安全图片/拒绝。只缩略图、img安全模式、本人打开SVG、错origin或无后续读者为反例；奖励不替完整执行链，不抓外部payload。

来源：[保存帖1](https://x.com/i/status/1489128323582095364)、[保存帖2](https://x.com/i/status/1489128808225521664)。


## document domain 标记与接管证据层级

正文建议document.domain比alert1体现执行域，再升级ATO。域标记只能帮助定位执行上下文，不证明另一读者、身份能力或token可读。

自有无害fixture绑定输入/消费origin/事件/CSP及主体，比较训练页、本人console、安全编码和后续受限消费者。弹框、域字符串、HttpOnly或无状态能力为反例；最小证据足够时止步，不为演示接管修改真实账户。

来源：[保存帖1](https://x.com/i/status/1491030050371686409)。


## Blind XSS fired 邮件与所有表单的范围

正文称developerpanelstoredBXSS并建议每表单都注入，图仅两条截断XSSHunterfired通知，没有payload、主体或浏览器上下文。

离线自有表单按存储/邮件/triager/浏览器消费者绑定唯一标记、时间和读者；普通/安全编码/重复标记/延迟回调对照。通知、扫描器/本人触发、无敏感能力或未经许可表单为反例；不普遍提交载荷、不向外部hunter发数据。

来源：[保存帖1](https://x.com/i/status/1491094277791055872)。


## image URL 弹框与 iframe SSRF 标题

完整图地址含image?url外部图片URL，页面弹框显示短字串，没有保存请求/iframe/服务端抓取。正文把SSRF/XSS/RCE同时标签化。

离线自有请求和DOM模型分别核URL被谁抓取、数据进入何上下文、浏览器origin/CSP和实际无害执行。弹框、本人console、纯图片、无服务端网络或错误消费者为反例；XSS不自动SSRF/RCE，不请求外部payload。

来源：[保存帖1](https://x.com/i/status/1489913389748875268)。


## details toggle 与 JavaScript 字符串须绑定真实解析上下文

正文提供details/open/ontoggle与字符串闭合型片段，完整图另有模糊cookie弹框，只能辨认分析cookie样式字串，没有完整请求响应和其他实际读者。事件属性、JS字符串和HTML文本是不同消费者，document.domain弹框也不等会话接管。

离线自有页面保留进入前后字节、引号/转义、DOM、事件触发条件、origin/CSP与无害标记。比较安全编码、纯文本和有事件消费者的情况；本人console、被清洗、未触发事件、CSP拦截或错误上下文为反例，不把片段当作通用绕过。

来源：[保存帖1](https://x.com/i/status/1491442193814667264)、[保存帖2](https://x.com/i/status/1493760232597917696)。


## HTML image 改写不能推广为任意标签过滤绕过

正文称所有标签被过滤时用image，没有保存真实输出。WHATWG在HTML in-body规则下把image开始标签改为img并重处理，此规则不意味着所有解析状态、SVG/XML和sanitizer相同。

离线自有HTML区分输入/输出上下文、命名空间、sanitizer前后、DOM、事件/CSP；与转义文本/被移除属性对照。仅标签保留、未知状态或无执行消费者为反例，不能据此称通用绕过。

规范核对：[WHATWG in-body](https://html.spec.whatwg.org/multipage/parsing.html#parsing-main-inbody)。

来源：[保存帖1](https://x.com/i/status/1492712208467439616)。


## HTML 注入到 javascript iframe 需要独立导航证据

正文把HTML注入升级RXSS并给iframe javascript样式，后续评论未保存按豁免覆盖；没有实际DOM/CSP/导航结果。

离线自有消费者记录注入位置、清洗后的URL、iframe origin/导航策略与CSP，比较文本展示、URL过滤及真实无害执行。HTML注入本身、屏蔽scheme、没有导航或本人console为反例，不虚构丢失评论中的绕过。

来源：[保存帖1](https://x.com/i/status/1492728426704392197)。


## phpMyAdmin CVE 标题弹框与实际入口链

完整图是phpMyAdmin CVE-2022-23808标题页面上的XSS对话框，没有输入、响应、版本验证或真实部署资产。标题和弹框不能补足外链全文。

离线自有页面区分真实服务与演示标签，记录输入传播、DOM/CSP和无害标记；缺交换、只演示图或未知版本为反例。可保留PHP登录页上下文检查方向，不推断所有部署存在同一CVE。

来源：[保存帖1](https://x.com/i/status/1493102483421470727)。


## 事件 handler 词表与 email 字段须核展示消费者

正文推荐生成on事件词表；完整email图列包含script的三个地址形式并称fuzz可能代码注入，工具图只是repo卡片。邮件地址解析、注册输入校验和后续HTML展示是不同边界。

离线合成地址记录合法性、引号/注释解析、保存值、展示上下文、清洗、实际事件/CSP和读者。只wordlist、被拒绝地址、纯文本显示或无事件触发为反例；事件名不能证明全部浏览器有效，不发真实邮件/注册或运行字典。

来源：[保存帖1](https://x.com/i/status/1494717521278246913)、[保存帖2](https://x.com/i/status/1494720894786224134)。


## Escape the Escape 需要区分输入校验与输出编码

正文泛称输入escaping可被escaped，没有语言/上下文或编码过程。正确输出编码的性质不能由口号否定。

离线自有样例按HTML/属性/JS/URL消费者分别记录解码次数、转义实现、模板插值和CSP，比较正确context encoding与混用/二次解码。重复反斜线、仅反射或上下文未知为反例；不能把所有escaping称无效，须定位实际阶段不匹配。

来源：[保存帖1](https://x.com/i/status/1494728482026369024)。


## SVG 未编码尖括号须追到实际 HTML 消费者

正文称关闭SVG的右尖括号被转义而尾部左尖括号未处理，另一帖提供编码SVG并声称除Firefox外可用；未保存原始响应、完整DOM和浏览器版本。

离线合成页面分别对HTML文本、属性和SVG命名空间保留输入/输出字节及实际解析树，比较转义与无害标记事件。单字符存留、无事件触发、已清洗、CSP阻止或浏览器差异为反例，不将编码片段推广为通用绕过。

来源：[保存帖1](https://x.com/i/status/1495604143192424450)、[保存帖2](https://x.com/i/status/1497278782465613827)。


## phpinfo 服务端回显与 HttpOnly 读取限制分开

完整图phpinfo的$_COOKIE/ci_session与DevTools HttpOnly=true/Secure=false并列；另一图JS用带凭据同步XHR读取info.php，再按HTTP_COOKIE索引截取与base64；multipart另有外部script，JSONsuccess=true。后两图未显示受害读者、XHR完整结果或回连。

HttpOnly限制脚本读取cookie，但浏览器仍可能在XHR/fetch中发送符合条件的cookie。离线同源合成页面比较凭据模式、鉴权、服务器是否回显、SOP/CORS、CSP和真实读者；substring不是精确提取，保存成功也不等脚本执行。无回显、无读取权限、跨源拒绝或无其他读者为反例，不执行外部脚本/外发。

规范核对：[MDN Set-Cookie HttpOnly](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#httponly)。

来源：[保存帖1](https://x.com/i/status/1496091043334344704)。


## 反射存储 DOM 和 self 标签不是互斥四类

正文将XSS分四种，另一帖声称mutation XSS，图仅XSS Hunter fires列表、受害URI/IP、缩略图与操作按钮，没有变异前后解析字节。

离线按输入持久性、服务器/DOM消费者、实际读者权限及解析变换分别建维度；mutation还需清洗前后与重解析DOM差异。回连界面、标签名称或本人console不等独立受害链；未出现解析变化/无跨读者为反例，不触发真实回连。

来源：[保存帖1](https://x.com/i/status/1497784305979990020)、[保存帖2](https://x.com/i/status/1498986395817308166)。


## CVE 单行 grep onmouse 不证明事件可执行

正文给形状不完整的while read/curl --insecure /admin/module.php示例并grep onmouse后打印vulnerable，没有响应上下文、CSP或浏览器结果。

离线合成响应比较同词在文本/编码/属性的情况，记录状态、TLS错误、输入反射、实际DOM及无害事件。关键词、CVE标签、命令打印或无消费者为反例；语法错误/隐藏失败不能计命中，不执行保存循环或关闭真实TLS检查。

来源：[保存帖1](https://x.com/i/status/1499460421165940736)。


## 字符码片段不完整与二千二百奖励归属冲突

正文将onmouseover与不完整with/String/eval/fromCharCode片段描述为POST并获2200；完整图是CSRF端点1800和两项RXSS50/350，总和2200。没有实际POST和执行消费者。

离线分别核JS语法、字符串/属性上下文、编码过程、真实读者与CSP；奖励按独立报告归属，不能把合计数字当一次XSS升级证据。语法错误、无实际发送/执行、仅标题与混合奖赏为反例，不运行保存片段或收集cookie。

来源：[保存帖1](https://x.com/i/status/1500367358325579776)。


## regex source 拼接与 cookie 弹框仍依赖 reader

正文有regex.source组合事件调用、window括号属性和十六进制al\x65rt，Microsoft图弹框可辨MUID/MC1 GUID其余模糊，另仅RXSS Medium5.4状态。没有边缘链、完整DOM或其他读者/会话。

离线分URL/form中加号、HTML属性/字符串、JS regex与实际事件执行，比较转义/CSP和无害标记。分析cookie、本人浏览器、报告级别、blocked/passed主张不是可用会话或普遍WAF绕过；无真实reader/不能重用为反例，不收集cookie或执行原payload。

来源：[保存帖1](https://x.com/i/status/1502621725481406465)、[保存帖2](https://x.com/i/status/1502679109293457412)、[保存帖3](https://x.com/i/status/1502853563604938762)、[保存帖4](https://x.com/i/status/1503483711450275852)、[保存帖5](https://x.com/i/status/1503641037906006016)、[保存帖6](https://x.com/i/status/1503705646025572357)、[保存帖7](https://x.com/i/status/1503736101588340737)。


## preg_replace delimiter 错误要分结果与两次消费者

完整训练图preg_replace提示No ending delimiter并显示源码：处理GET payload后进入JS name单引号，再拼到greeting.innerHTML。截图页面仍是问候，没有成功执行。

离线先记录PHP字符串转义后的正则、错误/返回值/异常处理，再分别核JS字符串和HTML解析结果。过滤报错不能自动假设原文通过或成功XSS；空/null输出、正确编码、CSP与无真实事件为反例，不执行页面hook或源代码，只分析训练条件。

来源：[保存帖1](https://x.com/i/status/1503281647034445824)。


## JSON 字符串变对象只有代码消费者才会执行表达式

完整图是单引号/name/alert(document.domain)片段，正文称JSON string变object初始化执行，但没有语法上下文或eval/JSON.parse消费者。

离线分别核JSON语法、JS对象字面量、动态源码/eval与安全解析，保留输入到初始化语句的数据流。JSON.parse不把函数调用当合法JSON执行；语法拒绝、纯字符串和未插入JS源码为反例，不凭对象转换标题判断XSS或运行原片段。

来源：[保存帖1](https://x.com/i/status/1503352199564468236)。


## 自动属性 XSS 的 Collaborator token 不等账号接管

正文将HTML属性注入、无交互与criticalATO关联；图有DNS/HTTP交互及GET t参数，token大部遮蔽。未保存源HTML、自动事件、回连主体及token消费。

隔离追输入→属性DOM→事件触发→同源认证消费者，比较正常文本/事件禁用/CSP阻断及无登录读者；留唯一标记与产生者。DNS或HTTP可能来自渲染服务、安全扫描器或预览，不直接证明浏览器XSS或可用认证token，不主动回连。

来源：[保存帖7](https://x.com/i/status/1503816543381209088)。


## innerText 写入文本不能代替所有上下文防护

正文建议innerText代替innerHTML且不要eval/newFunction，又将HTML编码表述为总能缓解。

innerText适用于文本消费节点，不能保护后续URL、属性、JS源码或再转innerHTML的链。离线比较同字符串在文本节点、HTML、引用属性与代码消费者中的结果，记录每次转义顺序和后续读取；一次文本安全写入不证明整个页面安全。

规范核对：[MDN innerText](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText)。

来源：[保存帖26](https://x.com/i/status/1504117309140516867)、[保存帖112](https://x.com/i/status/1505935118900281344)。


## freq 标签及 h1 字符串匹配要分反射和执行

wayback→gf→uro→qsreplace→freq图有Vulnerable/Not标签；另一行把端口/协议/每等号改写后httpx匹配h1字符串。

离线保持原URL、参数结构与每次改写，比较纯文本、编码HTML与真实事件消费。强制https或全等号替换会换目标/破坏参数，uro会合并有意义值。输出标签或h1存在只到反射/markup候选，须实际浏览器consumer与最小影响。

来源：[保存帖72](https://x.com/i/status/1504932805431767046)、[保存帖195](https://x.com/i/status/1507282836394590231)。


## 引用 value 中实体解码不直接重开 HTML 标签

正文inputsearch的value含quot/lt/imggt，询问绕过；没有后续DOM消费者或执行。

按HTML引用属性状态区分源引号结束与字符引用得到的值，实体解析出来的引号/尖括号不会自动当源代码重新分词。离线比较一次属性值读取、二次innerHTML和JS拼接，只有后续不安全consumer才新增边界；显示文本或无二次解析是反例。

规范核对：[HTML double quoted attribute](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(double-quoted)-state)。

来源：[保存帖219](https://x.com/i/status/1507754748518182914)。


## 图片渲染和 KYC 管理员 XSS 需要实际读者链

正文有图片渲染、KYC 总会成功和 XSS 到管理员凭据说法；图片只文章标题、状态、管理员 XSS 标题及回复认可，没有真实 source/sink 或认证消费者。

离线区分文件元信息、预览 HTML、审核员页面与文档渲染服务的上下文，确认输入存储、实际权限读者及 DOM 执行。后台读取可改变影响，但不自动证明 ATO 或 universal XSS；不上传真实 KYC 或发送回连。

来源：[保存帖1](https://x.com/i/status/1509648359786700809)、[保存帖2](https://x.com/i/status/1509914653597782024)、[保存帖3](https://x.com/i/status/1510251953174900745)、[保存帖4](https://x.com/i/status/1510508573649870852)、[保存帖5](https://x.com/i/status/1510704898509258753)。


## 路径引号与块注释片段应保留编码和消费者

一图地址栏含编码 script 与弹窗，另一图是带引号、alert、块注释和编码空格的 GET 路径，未保存对应 HTML/JavaScript 源。

自有字符串模型保留路径原字节、解码次数、拼接点、引号/注释边界以及最终 DOM/JS，比较正常文本、编码输出和 CSP 情况。请求中的片段不等合法可执行语法，弹窗也需关联同次输入和来源；不把图片拼成已验证漏洞链。

来源：[保存帖1](https://x.com/i/status/1509665343832215557)、[保存帖2](https://x.com/i/status/1511054877044137991)。


## Electron 内容加载与支付 postMessage 标题须追权限消费者

正文只不安全加载和 DOM/postMessage XSS 标题，未保存处理代码或窗口配置。

离线分网页 origin、消息来源/窗口句柄、数据 schema、HTML sink 和 Electron 桥接权限；只有原生能力确实暴露且被调用才能继续评估 RCE，支付页面标题也不证明资金变化。外链全文按覆盖，不填造其中 payload。

来源：[保存帖1](https://x.com/i/status/1510259432722034688)、[保存帖2](https://x.com/i/status/1510259708363374598)、[保存帖3](https://x.com/i/status/1511002501201375240)。


## airixss stdout 确认须追实际浏览器解析

正文历史 URL→gf→uro→httpx→替换 SVG→工具 grep 标签，没有 DOM 与执行记录。

离线保留输入 URL 变更、过滤损失、反射位置及最终解析，明确 stdout 文本匹配与浏览器执行为不同证据。httpx 存活结果不代表最终载荷请求，grep 命中不证明事件触发或受害者权限。

来源：[保存帖1](https://x.com/i/status/1510869384755093512)。


## origin 相等检查后的 innerHTML 仍须验证消息主体

图片代码实际为 onmessage、读取 e.data、严格比较 e.origin 与 window.origin，然后 render 类型直接赋 innerHTML。

这是可审计 sink，但具体漏洞还需来源窗口/导航、接收页 origin、data shape 与 HTML 解析条件。标准中某些 origin 序列化为 null，不同 opaque origin 不能仅靠同字符串当同一主体；离线用合成窗口身份模型核 source 及预期 origin，保留 sandbox 与 CSP 条件，不把尚未保存的挑战答案写成实测。

规范依据：[Window origin](https://developer.mozilla.org/en-US/docs/Web/API/Window/origin)、[MDN sandbox 消息验证](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/sandbox)。

来源：[保存帖1](https://x.com/i/status/1511846053427003393)。


## DOM Invader canary 应串起 source 到 sink

图片给出 Chromium 中开启 DOM Invader、更新 canary、遍历功能、查看反射和 source/sink 的流程。

以自有离线页面逐一触发功能，记录来源值、传播变换、最后的 sink 和当时 DOM。canary 被观察到只是数据流线索；需结合 HTML/属性/URL/JS 上下文及编码确认是否成为可执行内容，普通文本反射不能算 DOM XSS。

来源：[保存帖1](https://x.com/i/status/1512276322844037129)。


## POST 换 GET 的反射需核 handler 和执行位置

正文称 signup 的 productID 在 POST 被阻挡，改 GET 后出现反射型 XSS，没有保存完整页面。

方法可能进入不同 handler 或改变参数来源；保留两种请求的身份、URL、响应字节与 DOM 消费位置，区分普通反射、浏览器解析与实际脚本执行。改变方法只能作为定位分歧的实验，不能保证绕过校验。

来源：[保存帖1](https://x.com/i/status/1514004509319643149)。


## 模板字面量和图片事件片段仍受最终语法约束

正文建议转义/模板字面量绕过括号，截图显示 redirect 参数与页面中直接显示的 image/onmouseover 字符串。

按 URL 解码、HTML 属性与事件 JS 的实际顺序追字节，确认引号、标签闭合和事件触发位置。源码里能看到 payload 或换了调用语法，不等于它已被解释执行；截图没有弹窗/事件结果，保留这一限制。

来源：[保存帖1](https://x.com/i/status/1514005482402365443)。


## XSS 一行管道的过滤器同时定义了遗漏范围

两组正文及图片串 Wayback/anew/等号筛选/gf/nilo/gxss/dalfox，并跳过 DOM mining、若干检查及 302/404/403。

保存各阶段输入输出、过滤条件和原因。只看有等号的历史 URL 会漏其他来源；跳过 DOM 或状态码可能丢失实际页面/错误页消费，gxss 反射与 dalfox 输出仍需浏览器上下文确认。先理解每阶段的检查目标，不能称一行找全 XSS。

来源：[保存帖1](https://x.com/i/status/1514083053131468800)、[保存帖2](https://x.com/i/status/1515293938227322880)、[保存帖3](https://x.com/i/status/1515297302503575554)。


## DumpXSS 的 Found 输出仍需浏览器执行证据

终端图有 XSS Found 与含 image/onerror 的 URL，报告列表只是 rXSS 标题；正文强调输入文件和输出功能。

将 CLI 输入、请求/响应、反射点、浏览器 DOM/事件验证分开，绑定完整 URL 和样本版本。保存文件或自动宣告 Found 不保证载荷在实际上下文执行；报告题名与 Medium 标记同样不能补全缺失的页面结果。

来源：[保存帖1](https://x.com/i/status/1514293329932046339)、[保存帖2](https://x.com/i/status/1515531070845833224)。


## 模板字面量要检查插值语法而非只检查引号

保存片段在 Unicode 转义多类字符的模板字面量中使用 ${...}。

先核验输入是否真正进入未转义模板源码；表达式插值可在不闭合反引号时发生，普通文本和运行时字符串则不同。保留原始输入、生成源码与执行消费者，不能只根据引号处理认定安全。规范核验：[MDN 模板字面量](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)。

来源：[保存帖1](https://x.com/i/status/1516062938498420739)。


## onclick 的 HTML 实体需沿两层解析核验

正文用 &apos; 描述 onclick 字符串上下文，未保存最终页面。

先还原 HTML 属性边界及实体解码，再核验 JavaScript 引号、运算表达式和事件触发。用于 HTML 的编码未必适用于事件源码；实体出现在普通文本、URL 或脚本元素时处理不同，片段不能替代 DOM 与执行证据。

来源：[保存帖1](https://x.com/i/status/1516064117593100294)。


## 反射流水线的过滤和替换要保留原参数身份

正文串联历史 URL、扩展过滤、去重、全参数替换与反射筛选。

未转义的正则点号及宽泛扩展匹配可能删错候选；去重可能合并不同值或状态。逐参数保留输入到响应的映射，反射标签与实际浏览器解析、事件触发及权限影响分别验证，不能由字符串命中认定 XSS。

来源：[保存帖1](https://x.com/i/status/1516635194446401542)。


## JavaScript 字符串转义要检查反斜杠与闭合字节

正文给出带反斜杠、引号和注释尾部的片段，称部分字符已编码或转义。

保留输入字节、各层编码、最终脚本源码与原字符串结束符，判断反斜杠本身如何处理。片段只有在具体源码位置与后续语法成立时才可能改变表达式；正文没有执行对照，不能写成通用字符串绕过。

来源：[保存帖1](https://x.com/i/status/1516752315466010626)。


## transitionend 片段需要实际过渡完成条件

图为自定义元素、outline transition、tabindex 与 transitionend 处理器，没有执行画面。

核验最终 DOM、属性变化、非零过渡、焦点交互及原 CSP；过渡不存在、取消或未完成时不能假定事件发生。元素字符串和 tabindex 本身不证明执行。规范核验：[MDN transitionend](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event)。

来源：[保存帖1](https://x.com/i/status/1517137354800001025)。


## href 上下文中的整段 anchor 不是通用逃逸

正文展示 href 属性与完整带事件 anchor，未说明原属性如何闭合。

保存输入实际插入字节、原引号、属性边界、解析后的 DOM 和事件策略。新的 anchor 字符串可能仍在 URL 属性值里，弯引号或自闭合写法不能假定完成逃逸；真实事件消费者和执行结果另证。

来源：[保存帖1](https://x.com/i/status/1517513911863750658)。


## 反射定义必须连接即时响应中的脚本消费者

正文解释 reflected XSS 是输入经不安全响应处理返回；配图是梗图。

以同一请求绑定输入、响应位置、编码与最终浏览器消费者，区分反射、HTML 注入和脚本执行。没有跨请求存储不是漏洞充分条件，也不能由接口响应含字符串推断另一页面会执行；受影响身份另行限定。

来源：[保存帖1](https://x.com/i/status/1517870157401518081)。


## 不可见管理界面的 stored XSS 仍需回连主体

正文声称输入在不可见后台触发会更严重，没有载荷或实际回连记录。

关联存储请求、记录身份、后台渲染消费者、回连时间与执行主体；安全爬虫或预览服务也可能访问 URL。后台不可见不能自动推出管理员执行或 Critical，影响需具体权限与最小自有证据。

来源：[保存帖1](https://x.com/i/status/1518578154830323712)。


## 混合内容处理与事件触发按实际浏览器核验

历史正文把 Chrome/Firefox 的事件差异概括为固定规律，未保存版本与对照。

核元素、资源类型、原方案、自动升级或阻断、控制台和实际事件；网络未加载与 DOM 事件执行分开。不同浏览器或版本行为不能由历史一句话确定。规范核验：[MDN 混合内容](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Mixed_content)。

来源：[保存帖1](https://x.com/i/status/1519360969591427078)。


## 命令行 XSS 二分标签不能取代浏览器确认

截图在历史 URL、查询去重和多参数替换后打印 Vulnerable/Not Vulnerable，没有浏览器执行画面。

保留原 URL、每个参数、编码层与去重依据；同时替换多个参数会丢失因果归属。stdout 分类可能只是匹配规则，负结果也不覆盖其他状态与 DOM sink；逐一回到真实响应和浏览器消费者。

来源：[保存帖1](https://x.com/i/status/1519413198138531841)、[保存帖2](https://x.com/i/status/1519459252326342656)、[保存帖3](https://x.com/i/status/1519640824295821312)。


## 历史 URL 管道的候选过滤与浏览器执行分层

正文串接 URL 收集、参数去重、替换全部参数和反射检测，最后按标签过滤。

每阶段保留原 URL、方法、参数和值到输出的映射；去重会合并不同业务状态，全部替换会失去单参数归因。反射标签或终端命中只产生候选，需在原身份下核响应上下文、最终 DOM、编码和浏览器执行。

来源：[保存帖1](https://x.com/i/status/1520003220168482818)、[保存帖2](https://x.com/i/status/1520948650603532288)。


## 源码未反射时追导航后的 DOM 消费者

正文建议在重定向后寻找源码不可见的 XSS，附图只有报告标题。

分别保留原始响应、跳转链、落地 URL 和客户端 DOM 更新；输入可能在导航后由脚本读取。源码无字符串不排除 DOM 数据流，跳转本身也不证明脚本执行；需定位具体输入到危险消费者的转换。

来源：[保存帖1](https://x.com/i/status/1520127532544241664)。


## 浏览器 Python 运行时不等于服务端命令执行

图通过脚本资源和 py-script 展示浏览器端 Python 内容，正文把 HTML 注入描述为 RCE。

核最终 DOM、脚本是否加载、浏览器策略与运行时所在主体。网页内代码能力受页面环境约束，不因语言为 Python 就获得服务器或原生进程权限；服务端执行需要另一个具体消费者和权限证据。

来源：[保存帖1](https://x.com/i/status/1520963356517351424)、[保存帖2](https://x.com/i/status/1521480232041168897)。


## Polyglot 的注释引号与事件语法按有限上下文验证

正文和图分别展示不同复合 XSS 字符串，图对注释、引号、标签闭合、事件及 Unicode 标记作注释。

保留正文与图中字节差异，分开测试 HTML 文本、属性、脚本字符串和事件处理器的自有样本。跨几个上下文生效不说明全部解析器可用；Unicode 和引号是否被解码、事件是否可达与浏览器策略分别记录，不把复合字符串当通用成功模板。

来源：[保存帖1](https://x.com/i/status/1521303791475339267)。


## 弹窗截图只支持对应上下文中的有限执行观察

几张图分别展示浏览器弹窗与部分 URL，有的图可见闭合标签和事件片段，有的只可见弹窗；正文还声称多个漏洞或 ATO。

逐个保存原输入、响应、最终 DOM、实际来源和执行主体；遮挡或缺失内容不推断。单个弹窗不证明多个独立入口、账户接管或任意权限；正文与截图的曲引号、编码和实际字节也需区分。

来源：[保存帖1](https://x.com/i/status/1521832018857844739)、[保存帖2](https://x.com/i/status/1523247017572454400)、[保存帖3](https://x.com/i/status/1523978680208437248)、[保存帖4](https://x.com/i/status/1524002935017033729)。


## 个人资料持久化要区分服务端保存与本地残留

正文描述修改个人资料后退出、重新登录仍触发的场景。

把输入、保存请求、持久化对象和再次读取的页面绑定起来；用新会话与自有第二身份核读取，排除缓存和本地存储残留。重复显示字符串只说明数据再现，存储型 XSS 还需最终 HTML/DOM 消费者与执行证据。

来源：[保存帖1](https://x.com/i/status/1524256343204401153)。


## SVG 和多语法片段需回到实际事件及解析上下文

正文用斜杠和空白改变 SVG 标签，但仍包含事件属性；另一图注释引号、注释边界、details 开启事件及 Unicode 字符串。

分别核 HTML/SVG 属性解析、过滤后的字节、脚本语法及事件触发条件。写法变化只覆盖有限上下文，不能自动穿过禁止事件的策略或 CSP；用离线页面逐项对照，避免把多语法标签当作普遍执行保证。

来源：[保存帖1](https://x.com/i/status/1524767185066881024)、[保存帖2](https://x.com/i/status/1525552169789038594)。


## 后置读取响应不是二阶 XSS 执行证据

图展示宏将最终响应供检测工具分析。

区分保存成功、另一消费者读取、响应包含标记和浏览器执行四步；读取身份可能不同，宏运行范围也可能过宽。只有具体读者上下文与执行条件可支撑二阶影响，不能由自动扫描命中补出跨角色执行。

来源：[保存帖1](https://x.com/i/status/1524768403751247873)。


## 焦点触发的 CSS transition 需发生真实属性变化

正文用 outline 和 transition 组合声称可触发脚本。

在自有页面核元素可聚焦、属性实际改变、有效持续时间和事件处理器能否执行。transitionend 是过渡完成事件，过渡被取消或未发生时不能保证触发；具体浏览器与 CSP 条件须记录。规范核验：[MDN transitionend](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event)。

来源：[保存帖1](https://x.com/i/status/1525863259420729346)。


## HTML 类型的 JSON 外形响应要核实际解析上下文

正文建议修改 JSON 内容，图中的历史模板响应为 text/html，包含转义的 JSON 外形字符串及检测标签。

分别保留媒体类型、原始字节、JSON 是否有效及浏览器最终 DOM。JSON 外形并不强制 JSON 解析，字符串转义也不自动提供 HTML 安全；但检测命中仍不能代替真实解析与执行。无效样例和正文/仓库 CVE 编号差异不得补成已验证漏洞。

来源：[保存帖1](https://x.com/i/status/1525866311871565826)、[保存帖2](https://x.com/i/status/1526232515874537472)。


## HttpOnly 不阻止同源脚本读取业务响应字段

图展示 sessionInfo/authUser 响应和 fetch 片段，正文将其称为 HttpOnly 场景中的令牌取得。

区分直接读取 Cookie 与携带会话请求业务接口：HttpOnly 限制前者，仍可由符合条件的请求携带。核脚本所在来源、接口权限、返回字段及字段实际消费者；跨来源还受凭据配置和 CORS 限制，字段可见不等于可复用令牌或账户接管。规范核验：[MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)。

来源：[保存帖1](https://x.com/i/status/1525972417335676929)。


## 片段导航的焦点条件须绑定元素和浏览器状态

正文声称 URL 片段配合焦点事件无需交互可触发。

片段在浏览器侧匹配目标，需核目标 ID、可聚焦性、导航时机、实际焦点变化和事件执行策略。滚动到目标与触发特定处理器不是相同结果，片段也不自动发给服务端；自有样本记录具体浏览器行为。规范核验：[HTML fragment navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-the-fragment)。

来源：[保存帖1](https://x.com/i/status/1526136779904012288)。


## Angular 字符串命中与模板表达式执行分别取证

正文给出 constructor 表达式并按页面字符串搜索，未展示完整执行链。

先核输入只是普通字符串、被编码输出，还是进入客户端模板编译和表达式求值。定位模板版本、表达式上下文和实际副作用；反射匹配不能证明客户端模板注入或脚本执行。

来源：[保存帖1](https://x.com/i/status/1526167298372800514)。


## Swagger configUrl 的外部数据需追到实际 DOM 使用

正文描述从 configUrl 加载外部配置并触发 XSS，未保存文章全文。

核部署版本、参数是否被接受、资源加载来源以及配置字段进入 DOM 的具体方式。能抓取配置不等于脚本执行；版本、CSP、认证和页面来源共同决定条件。保留已保存机制，不扩写未保存利用链。

来源：[保存帖1](https://x.com/i/status/1526425482534588416)、[保存帖2](https://x.com/i/status/1526504371164676096)、[保存帖3](https://x.com/i/status/1527907632191000576)。


## Python 八进制字符串与 PyScript 页面渲染分层

正文用 Python 转义字符串及 print/表达式描述页面执行，没有当前运行证据。

Python 字符串转义生成的是字符，仍需核历史 PyScript 输出接口将其当文本还是 HTML，以及最终 DOM 和事件策略。输出字符串不等于浏览器解析，更不代表服务器代码执行；记录当时运行时，不能推广为当前默认行为。规范核验：[Python 字符串转义](https://docs.python.org/3/reference/lexical_analysis.html#octal-character)。

来源：[保存帖1](https://x.com/i/status/1526710079059333121)、[保存帖2](https://x.com/i/status/1526710387470651399)。


## 片段取值与 auxclick 需保留交互和脚本策略

正文把片段字符串与 SVG auxclick 处理器连接，并称某次 WAF 放行。

片段在浏览器侧消费，仍需实际事件交互、页面上下文、过滤结果及脚本策略。WAF 不看到片段不代表应用一定求值，事件处理器存在也不说明无交互执行；保留该次观察，不推广通用绕过。

来源：[保存帖1](https://x.com/i/status/1529883784069492745)。


## URL 片段聚焦需核匹配元素与真实事件

图把片段 ID 与 input 焦点处理器相连。

核目标元素确实存在且可聚焦、导航时机、实际焦点变化与脚本策略。滚动和聚焦不保证所有浏览器触发同一事件，片段也不作为服务端请求路径；自有页面记录具体条件。规范核验：[HTML fragment navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scroll-to-the-fragment)。

来源：[保存帖1](https://x.com/i/status/1530514231820443649)。


## SOME 窗口关系需核调用时来源和具体动作

完整图描述开启窗口、原窗口导航到目标、另一窗口经回调引用 opener 的 DOM 方法；正文提到同域或子域部署。

按每次导航记录两个窗口来源、opener 是否保留、回调限制与 CSP，再核目标身份、动作及防伪状态。同站/子域不等于同源，已有回调能力也不能推广成所有 CSP 绕过或管理员执行。规范核验：[MDN 同源策略](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)、[opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)。

来源：[保存帖1](https://x.com/i/status/1531022887964098560)、[保存帖2](https://x.com/i/status/1531023890490826757)。


## 高频参数名字不等于当前 XSS 风险

图列 25 个查询参数并引用历史来源，没有具体响应。

把名字用作输入发现候选，记录真实使用位置、编码、输出上下文和浏览器消费者。排名缺少样本方法不能变成当前优先级，参数存在或反射也不保证执行。

来源：[保存帖1](https://x.com/i/status/1531413314210873344)。


## script 字符串、结束标签与 URI 编码的不同消费者

先定位输入是在 JavaScript 字符串、表达式还是 HTML script 元素文本中，再记录引号、反斜杠和结束标签分别经过哪层转义。HTML 解析先于脚本解析，标签边界与字符串语法需要分别检查。图片中的运算符示例有的可能语法无效，必须以完整生成代码和真实触发结果验证，不能视为通用载荷。URI 组件编码保留部分标点，也不能代替 HTML 或 JavaScript 上下文转义。[MDN encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)说明其编码边界。

来源：[保存帖1](https://x.com/i/status/1532228054713438208)、[保存帖2](https://x.com/i/status/1532377352528969729)。


## 过滤差异与事件脚本的实际执行条件

HTML 标签别名、实体解码、事件属性、JavaScript 转义和属性访问语法都要在对应消费者里核对。过滤器接受另一拼写不证明脚本执行；事件需要真实触发，变量必须存在，CSP 和浏览器解析结果也会影响行为。Cookie 读取仅限可访问内容，不代表 HttpOnly 数据或账户接管。保留完整响应、DOM、触发过程及无害结果，避免复制通用外传载荷。

来源：[保存帖1](https://x.com/i/status/1532938388336427009)、[保存帖2](https://x.com/i/status/1533794263179620354)、[保存帖3](https://x.com/i/status/1534165068815822848)。


## Django debug 场景先确认版本与输出消费者

将用户名放入脚本样式内容只是输入；先确认历史漏洞涉及的 Django 版本、debug 状态及错误页面实际输出位置，再判断内容是否进入可执行 HTML。训练代码或漏洞标题不能推定当前默认配置受影响。无具体响应和浏览器触发时保留研究线索，不扩写成已验证存储型 XSS。

来源：[保存帖1](https://x.com/i/status/1533795763708641280)。


## 浏览器弹窗能证明当前执行但不能自动证明存储链

弹窗显示 Cookie 样式文本，只能在排除人工执行、扩展或固定弹窗后支持当前页面脚本执行。存储型结论还需要写入位置、重新加载后的来源及另一自有账户触发；敏感 Cookie、HttpOnly 限制和账户操作影响分别验证。截图会话内容脱敏，不作为可复制测试数据。

来源：[保存帖1](https://x.com/i/status/1535211138412974080)。


## Login CSRF 与 self-XSS 的跨用户触发链

组合链应证明登录 CSRF 能把受害测试浏览器切换到攻击者自有账户，并让已存在的输入在该浏览器自动到达执行点。若仍要求受害者手工粘贴脚本，则未消除 self-XSS 前提。记录身份切换、持久化输入、触发步骤、原始用户数据是否仍可访问及最终实际影响；不能以“加 CSRF”口号推定完整 XSS 或账户接管。

来源：[保存帖1](https://x.com/i/status/1535587660844175361)、[保存帖2](https://x.com/i/status/1535681947934015489)。


## SPA DOM 扫描的会话、路径序列与实际 sink

帮助页提供 Cookie、HTTP 认证、初始序列、存储、代理、排除 URL、超时和检查类型等配置。记录实际载入会话、页面动作、source→sink 与浏览器触发证据；只完成加载或列出 dom/reflected/stored 选项不能证明发现漏洞。排除登出路径保护测试状态，超时和未访问路线计入验证限制。

来源：[保存帖1](https://x.com/i/status/1536109777746542592)。


## 历史参数筛选保留真正的前端输入消费者

图片把历史 URL、等号筛选、静态后缀过滤与参数替换串联。正则中的点需按真实意图转义，过滤 JS 等后缀可能丢掉实际 DOM 消费入口；保留原 URL、参数位置、当前路由与身份。工具反射或候选数量只能指导手工检查，需确定响应/DOM 的上下文、触发事件、浏览器和防护条件，再用无害标记证明执行，不能将筛选输出称为 XSS。

来源：[保存帖1](https://x.com/i/status/1536792659121287173)、[保存帖2](https://x.com/i/status/1540018868818690048)。


## 隐藏头反射与缓存污染分别证明消费者及共享复用

正文把隐藏请求头、反射、XSS 和缓存污染串联。先确定头被哪个响应/DOM 上下文消费，记录正常与实验响应；再独立证明该头未入缓存键、响应确被缓存，以及无该头的受控第二客户端复用到相同对象。反射不等于执行，单请求响应变化不等于共享缓存污染；不以私有缓存或本人会话效果推导跨用户影响。

来源：[保存帖1](https://x.com/i/status/1537512446885347328)。


## 盲注回调按字段与处理者归属区分

正文提到联系/反馈/举报字段与独立回调服务。给每个受控输入独立标识，保留提交请求、可追踪的处理时序和回调上下文，限制字段/次数/工作人员触发副作用。DNS/HTTP 回调只能支持对应连接或渲染观察，不能自动说明管理员浏览器执行或完整接管；私有数据不得交给公共记录器，未保存仓库全文按用户覆盖。

来源：[保存帖1](https://x.com/i/status/1537755440892764160)、[保存帖2](https://x.com/i/status/1538966320896696324)。


## 编码属性与 fragment 使用完整浏览器解析链

正文/图片包含编码属性、片段输入与注释边界载荷。原始 HTML 属性名中的百分号不会因“看起来编码”就普遍转换成事件名；fragment 是否进入网络或被前端读取需记录实际请求和 DOM 消费者。图片执行只支持当前页面/交互，完整上下文、解码次数、HTML 注释状态、事件触发和 CSP 均需确认；不能从某个 alert 外推万能 WAF 绕过。

来源：[保存帖1](https://x.com/i/status/1537799760622518272)、[保存帖2](https://x.com/i/status/1537887562194624512)、[保存帖3](https://x.com/i/status/1538499377798557696)。


## jQuery HTML 转文本前的解析阶段仍需审计

正文用先 .html(text) 再 .text() 的例子。最终返回纯文本不会撤销前一步把不可信输入交给 HTML 消费者的副作用，需确认版本、实际方法、事件/资源触发与插入路径；应直接使用文本消费者或经过适合上下文的可信处理。不能把某种 detached 节点一概判可执行，也不能用最终文本输出证明全过程安全。依据：[jQuery .html 文档](https://api.jquery.com/html/)。

来源：[保存帖1](https://x.com/i/status/1538582109312393223)。


## 主题 Ajax 参数反射要补足真实响应与浏览器触发

图片显示主题密码流程的 Ajax POST，其中 redirect_to 含 HTML 输入，但响应窗为空。应以当前主题/版本、认证与具体 action 还原请求，确认响应编码、渲染消费者、触发事件和执行域，再判断反射 XSS；请求里含事件字符串不证明响应接受或执行。标题中的 CVE/主题名不代替当前部署证据，不复用截图会话。

来源：[保存帖1](https://x.com/i/status/1539869113912201222)。


## CSP 审计输出需要回到实际响应与浏览器执行边界

Lighthouse 保存图片列出 base-uri 缺失、host allowlist 等风险，cspparse 图片则只展开 connect-src。将这些作为定位线索：保存原始响应中的所有 CSP 头、Report-Only 与执行策略、相应页面及最终 DOM，并按实际消费者核查脚本、连接、框架和基地址约束。

评分、单一指令列表和历史工具界面不能证明具体 XSS 已执行。确认来源列表、回退指令、多策略组合及浏览器交互；HTML 注入、策略不足和跨用户脚本执行分开记录，不从 High 标签直接推出业务严重性。

来源：[保存帖1](https://x.com/i/status/1540539528913588229)、[保存帖2](https://x.com/i/status/1544308698176167941)。


## postMessage 的接收来源、窗口身份与数据消费者

保存图显示 window.open 后通过通配 targetOrigin 发送消息，应提炼为跨窗口信任边界核查。记录发送窗口引用、目标当前来源、页面加载时序和实际接收器；接收端分别验证 event.origin、event.source 和消息结构，再追踪数据是否进入 HTML、导航或权限操作。

通配发送、能打开窗口或能收到消息都不单独证明同源策略被绕过。窗口导航、popup 条件、COOP 和加载时序会影响复现；优先使用明确目标来源与无害标记，在自有窗口中证明具体消费者。规范参见 [MDN postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)。

来源：[保存帖1](https://x.com/i/status/1540661091163930627)。


## 反射标记先定位 HTML 与脚本的逐层消费者

保存帖覆盖事件属性、title/meta、输入 value、script 结束标签、CTF 表达式及 javascript URL 等上下文。先用无害标记定位原始响应、最终 DOM 与触发交互，再分别核查 HTML 词法、属性引号、JavaScript 字符串或表达式及 URL 解析；同一个载荷不能跨这些语法直接复用。

HTML 字符引用解码产生的引号不会自动作为当前属性的新分隔符，须查后续是否再次拼接或解析。title 内的反射不等同事件执行；弯引号与复制格式不能代替真实原始字符。javascript URL 还受 URL 有效性、脚本注释、换行、清洗器及 CSP 约束。

浏览器提示框可证明相应页面发生执行，仍需区分自身交互、存储位置、跨用户触发和权限来源；不能从 document.domain 或一次提示推导账号接管，也不能默认读取 HttpOnly cookie。完整源码或后续步骤未保存时只保留可验证的上下文条件。

来源：[保存帖1](https://x.com/i/status/1540757813571424259)、[保存帖2](https://x.com/i/status/1541319706690441216)、[保存帖3](https://x.com/i/status/1541491036320677888)、[保存帖4](https://x.com/i/status/1542362348018896896)、[保存帖5](https://x.com/i/status/1542871580392542208)、[保存帖6](https://x.com/i/status/1543515733254348800)、[保存帖7](https://x.com/i/status/1545038553918238724)。


## 历史 Angular 表达式载荷必须绑定模板编译与版本

保存图片涉及历史 Angular 1.4 至 1.5.8 的表达式、charAt 原型变化和动态脚本组合。复用线索时先确认当前页面确实把受控内容作为 Angular 模板编译，并记录运行版本、表达式消费者、CSP 与所需交互。

源码中存在 Angular 或响应包含表达式不代表执行。不同版本和模板边界不共享同一逃逸条件，不能把历史 payload 作为所有 JavaScript 页面通用绕过；仅在受控页面用无害标记建立实际执行证据。

来源：[保存帖1](https://x.com/i/status/1541025702132293634)、[保存帖2](https://x.com/i/status/1541441755299856384)。


## Tomcat examples 表单 XSS 的历史版本条件

保存 Nuclei 图片显示 examples JSP 路径命中，正文给出搜索标题与历史 CVE。官方 Tomcat 9 公告将 CVE-2022-34305 定位为 examples 的表单认证示例 XSS，受影响 9.0.30 至 9.0.64，9.0.65 修复。核查必须同时绑定实际部署版本、示例应用可达性和受控输入的页面消费者。

模板命中和搜索平台结果只提供候选；不由此推导所有 Tomcat 分支或当前站点均受影响。用实际版本和无害执行证据区分错误指纹、仅安装示例及真实影响。规范来源：[Tomcat 9 安全公告](https://tomcat.apache.org/security-9.html)。

来源：[保存帖1](https://x.com/i/status/1541359080299708416)、[保存帖2](https://x.com/i/status/1541360832986095616)。


## 注册与邀请邮件中的 HTML 内容和脚本执行分开

保存正文及 OneNote 分享输入、邀请邮件的红色 h1 图片说明用户名或留言可能进入邮件 HTML。先追踪输入、模板拼接、实际邮件客户端和最终渲染，检查文本、链接、样式与可信品牌呈现的控制范围。

可控制 HTML 标记不等于邮件客户端执行 JavaScript，也不等于账号接管。以自有邮箱与无害内容验证完整链路，记录链接目的地和必要交互；奖励截图与输入页面不能替代接收端证据，不向他人发送测试消息。

来源：[保存帖1](https://x.com/i/status/1541565858664808449)、[保存帖2](https://x.com/i/status/1542100224847626242)、[保存帖3](https://x.com/i/status/1544231769141981184)。


## 盲 XSS 自动化保留载荷归属与真实后续处理器

保存 SXSS 帮助页只展示提取、生成和检测命令，另一管道在历史 URL 请求的 User-Agent 注入外部脚本。先把候选生成、发出请求、存储位置、后续查看者与实际执行来源分开，每个字段使用独立可关联标记。

自动化输出不是已确认 XSS；回调可能来自本地浏览器、扫描工具或正常异步处理，需结合原始请求与执行来源排除。人工复核后才形成发现，不能由一次回调推导管理员执行或读取全部 cookie，HttpOnly 和实际权限仍需独立判断。

所有主动请求在当前授权范围和有限预算内安排；通知配置只记录证据来源与脱敏结果，保护 webhook 与会话，归档不发送通知、不运行批量载荷或向他人投递。

来源：[保存帖1](https://x.com/i/status/1541617579378229250)、[保存帖2](https://x.com/i/status/1544386493208092673)、[保存帖3](https://x.com/i/status/1544681458530684928)。


## 简单 HTML 标记用于定位消费者而非确认所有漏洞

保存技巧图把无害下划线标记投入输入并显示格式化结果。可复用的是用低影响标记定位原始响应、最终 DOM 和后续展示位置，再识别文本、属性、模板、导航或资源请求的具体消费者。

标记被作为 HTML 解析与 JavaScript 执行是不同结果，格式变化也不证明 SSRF。先验证上下文和真实执行或服务端请求归属，不能把“到处粘贴一个标记”当作全功能覆盖。

来源：[保存帖1](https://x.com/i/status/1545734519629692930)。


## 扫描管道的反射命中与浏览器执行保持独立

保存管道包括 nuclei 模板、kxss、历史 URL、cleanP/injectP、uro、qsreplace 和 httpx 标记匹配。分别保存原始输入、参数选择、转换后的 URL、模板版本与响应断言；含等号筛选会遗漏其他输入，静态后缀及去重可能改变或丢失业务条件。

-mr 的正则与字面字符串匹配不同，标记反射不证明浏览器执行或存储。未加引号的 shell 参数、未确认的工具选项、并发值和模板路径须在当前测试配置中验证，不能按截图直接运行。

每次主动请求按当前范围与预算安排，人工确认实际 HTML/DOM 消费者、CSP 和触发交互后才形成 XSS 证据；归档不执行批量扫描，也不由历史命中推导当前全部资产有漏洞。

来源：[保存帖1](https://x.com/i/status/1545991705060687873)、[保存帖2](https://x.com/i/status/1547026404835049472)、[保存帖3](https://x.com/i/status/1547091493738930176)、[保存帖4](https://x.com/i/status/1547358138701172737)、[保存帖5](https://x.com/i/status/1548620719033987077)、[保存帖6](https://x.com/i/status/1548728736853512195)。


## 页面提示与属性绕过回到原始字符及最终 DOM

保存图可见浏览器提示，正文包含反射标记、脚本语法平衡、属性内角括号编码以及使用 Inspect 与页面源码的建议。分别检查原始响应和运行后 DOM 的变化，定位字符串、属性、HTML 和脚本消费者；DOM 出现新内容仍需追踪其来源到敏感 sink。

只编码角括号并不决定属性内安全性；引用字符、事件边界、JavaScript 字符串和 CSP 都要按实际原始字符判断，复制帖里的弯引号不能替代有效语法。提示框只能说明相应页面的某次执行，入口未保存时不推造触发过程。

同一用户执行、自身调试、存储到他人可见对象和跨来源权限分别证明。不要由 document.domain、提示或静态属性形状宣称账号接管。

来源：[保存帖1](https://x.com/i/status/1546084362634280961)、[保存帖2](https://x.com/i/status/1546171683899183104)、[保存帖3](https://x.com/i/status/1548312193791574016)、[保存帖4](https://x.com/i/status/1548664056894332928)、[保存帖5](https://x.com/i/status/1549264078144675840)。


## 片段与百分号编码变化不能作为通用 URL XSS 绕过

保存正文把编码 javascript 形式和追加井号后的未编码形式进行对比，两者同时改变了编码和片段。先固定原始输入与各层解码，再分别观察属性解析、URL 有效性、最终导航或脚本消费者。

片段通常由客户端处理，不应假设其自动改变服务器编码。把每个变量独立比较，记录实际 DOM、清洗器、CSP 与所需用户动作；例子的不同字符串本身不证明追加井号导致绕过。

来源：[保存帖1](https://x.com/i/status/1546146611629379585)。


## 后执行工具及 postMessage 的数据能力以无害标记确认

toxssin 保存图显示 handler 请求、来源和已有活动会话，正文另建议通过 window.opener 与通配 postMessage 发送 localStorage。先证明具体 XSS 的入口和执行来源，再确认窗口引用、消息接收者及真实可达的存储类别，不把工具会话建立当作全部初始漏洞链。

用自有页面中的无害字段标记确认能力，避免采集或发送真实 localStorage、cookie 或凭据。存储项并非全部具有认证能力，HttpOnly 与来源、窗口、浏览器配置仍限制可读范围；通配发送和来源名称不能自动推出 High 或账号接管。

来源：[保存帖1](https://x.com/i/status/1546402648219213827)、[保存帖2](https://x.com/i/status/1547624860901203970)、[保存帖3](https://x.com/i/status/1548257092045135878)。


## 表单注入的动作、来源与 token 消费逐项确认

保存正文提出表单 action、同站 cookie 和 CSRF token 的影响方向。先确认注入是否被解析为真实 form、是否覆盖提交位置、必要交互和浏览器最终发送的方法/来源；脚本 URL、页面内读取及跨站提交是不同消费者。

同站点不等于同源，cookie 附带也不等于 token 泄露或动作成功。只用自有会话和无害表单字段证明实际行为与最终状态，不发送他人凭据或 token，也不由可控 form 直接推出账号接管。

来源：[保存帖1](https://x.com/i/status/1549167615884644352)。


## 事件属性、搜索页和弹窗分别绑定解析上下文

保存正文给出 div/onmouseover 与 img/onerror 片段，本地图片展示搜索页叠加弹窗。先保存原始输入字节，特别区分弯引号和 ASCII 引号，定位 HTML 属性、事件处理器及真实用户交互，再用唯一无害标记确认执行所在的源和页面。

一张弹窗不提供完整服务端请求、角色或影响链，也不能保证同一片段适用所有浏览器和过滤器。保留原始响应、最终 DOM、事件触发条件与 CSP，排除仅修改自己页面或响应产生的效果。

来源：[保存帖1](https://x.com/i/status/1549606777062309888)、[保存帖2](https://x.com/i/status/1549618142644690946)、[保存帖3](https://x.com/i/status/1553636284165287937)。


## 邮件 HTML 渲染和浏览器脚本执行分别确认

保存邮件图片只展示回信中的 HTML 大图，正文谈到邮箱模板注入及潜在误导。使用自有邮箱和无害标记观察实际邮件客户端、原始 MIME、模板插值位置、被改写的链接及可信品牌上下文。

HTML 内容注入、外部图片加载、脚本执行和账号接管是不同结果；浏览器示例不能替代邮件客户端行为。保留最小可控内容与真实受影响流程，不从未保存的视频补出任意注入请求或钓鱼链。

来源：[保存帖1](https://x.com/i/status/1550454466302087169)、[保存帖2](https://x.com/i/status/1550454760121126912)、[保存帖3](https://x.com/i/status/1552607824189870080)。


## 反射管线和 DOM 执行验证分别计账

保存图片组合子域工具、HTTP 可达性、历史 URL、gf、qsreplace、curl grep 或 kxss，并将它们标为 DOM/XSS。管线应逐段固定输入、输出和解析；图中把 live.txt 当命令、while 语法及 domain/domains 名称不一致均不能照抄，追加输出还可能混入旧记录。

响应含标记只能算反射候选，不证明 DOM source-to-sink 或脚本执行。保留原始字节与真实浏览器消费者，分别核查事件、编码、CSP 和交互；高并发、非标准端口和全部参数改值另核范围与预算。

来源：[保存帖1](https://x.com/i/status/1551263794575183872)、[保存帖2](https://x.com/i/status/1551411919868661761)、[保存帖3](https://x.com/i/status/1551615110883450881)。


## 客户端响应改写和弹窗缺失不能决定漏洞成立

正文询问自己改响应后产生 XSS，并把 Chrome 92 起跨源弹窗限制说成永久结论。先判断攻击者控制的数据能否在真实服务链上到达另一个测试用户的消费者，自己编辑页面或响应只说明本地效果。

没有 alert 也不等于没有脚本执行，应记录实际浏览器版本、帧来源、沙箱/CSP 和交互条件，在隔离页面用无害可观察标记交叉验证。历史版本说法不能一概外推；[MDN alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert) 说明某些条件会抑制弹窗。

来源：[保存帖1](https://x.com/i/status/1551266783524446211)、[保存帖2](https://x.com/i/status/1553469016844509186)。


## 盲 XSS 通知需绑定字段与真实下游展示

保存正文建议大量 User-Agent 请求，图片仅显示 XSS Hunter 通知标题。选择实际会被日志、工单或后台消费的字段，每字段分配独立无害标记，记录输入时间、请求身份和受控下游显示位置。

邮件通知数量不证明触发管理员、实际源或账号接管；须排除本地工具与浏览器回访。给测试请求和异步观察单独设置上限，避免全站喷洒与收集后台个人数据，证据只保留必要脱敏信号。

来源：[保存帖1](https://x.com/i/status/1551952782994939906)。


## 查询解码与导航协议检查需覆盖真实语法

保存本地页面图通过 URLSearchParams 取得 redirectURL，正则只检查含有类似冒号/双斜线的片段，随后赋给 location.href；另一图中编码 U+2028 的 javascript URL 出现 confirm 弹窗。关键是查询解码后的字符、正则匹配范围、协议解析以及 JavaScript 单行注释的终止符不同。

这只展示一个本地消费者例子，不保证所有导航/过滤器都能绕过。协议允许名单应按实际解析的协议和目标核查，实验记录浏览器、CSP、沙箱与无害标记，不把百分号字节直接等同运行时语法。

规范依据：[MDN URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)、[ECMAScript 词法规则](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html#sec-line-terminators)。

来源：[保存帖1](https://x.com/i/status/1553263876019556352)。


## 姓名进入邮件HTML时先证明渲染与可信内容混淆

正文将姓名字段中的图片标记带入邮件，并询问能否提高影响；保存字符串含不完整的URL格式。先用无害标记追踪字段到真实邮件源、客户端渲染和外链处理，区分文本、HTML内容插入、资源加载和脚本执行。只有在自有邮件收件环境证明可信正文被改变、内容误导或实际敏感动作链时才描述对应影响；邮件HTML插入不自动等于XSS或账户接管。

来源：[保存帖1](https://x.com/i/status/1554006011656425472)、[保存帖2](https://x.com/i/status/1555616370724847617)。


## XSS工具与编码候选按输入到消费位置逐层核对

保存清单混合抓历史参数、扫描器、静态分析及编码技巧。明确每个工具提供的是入口、反射、代码模式还是浏览器执行证据，再追踪URL、Base64、控制字符等转换发生在哪一层、转换顺序以及最终HTML或脚本上下文。版本、CSP、用户交互和真实消费位置都应记录；工具数量、编码列表、HTTP成功或反射字符串不能替代XSS验证。

来源：[保存帖1](https://x.com/i/status/1554135807023534080)、[保存帖2](https://x.com/i/status/1554704404221009920)。


## 标签闭合与事件属性候选要追踪持久化消费上下文

保存图片列出不同标签闭合，正文给出h1事件及重复的img事件字符串。先确定输入落在文本、属性、原始文本标签还是脚本，并观察实际HTML解析、转义、CSP及必要的用户交互。存储型判断还需第二个自有消费者读取同一已保存输入，证明持久化与执行链；报告标题、High标签、单次弹窗和通用闭合列表不替代这条链。

来源：[保存帖1](https://x.com/i/status/1555168598531788800)、[保存帖2](https://x.com/i/status/1556388283768344576)、[保存帖3](https://x.com/i/status/1558003867568291844)、[保存帖4](https://x.com/i/status/1558111675651350529)。


## 混淆脚本先静态追踪字符串构造和真实DOM写入

保存图片包含属性索引、隐式字符串转换、递增操作和innerHTML构造，末尾有注释中的alert。识别代码依赖的全局变量、对象结构和转换顺序，再追踪构造值是否可控及是否到达浏览器HTML消费位置。代码复杂、存在innerHTML或出现alert文本不证明可用XSS；保留静态证据，不运行未知存档脚本，不作通用绕过承诺。

来源：[保存帖1](https://x.com/i/status/1555609410642272256)。


## 从GET改为POST要核对处理器解码和浏览器执行

图片声称URL编码阻止XSS时改用自动提交POST。先比较真实请求字节、Content-Type、框架取值和最终消费位置，确认两个方法是否进入相同处理器以及输入如何转义。POST到达和HTTP成功不能证明XSS；如涉及跨站表单，还需独立记录Cookie策略、请求来源及真实持久状态，不能自动认定CSRF成立。

来源：[保存帖1](https://x.com/i/status/1555881420249243651)。


## 盲XSS通知需要最小标记关联持久输入和实际消费者

保存图片显示前端prompt、通知邮件、回调列表及带有打码字段的渲染页面。用唯一无敏感标记将自有提交、保存位置、触发时间、实际消费页面和回调关联，区分研究者自身访问与第二个授权消费者。通知和弹窗不足以推断后台权限或账户接管；避免采集完整私有DOM、Cookie、IP或无关个人字段。

来源：[保存帖1](https://x.com/i/status/1556441022200250372)。


## 404产品指纹与扩展名枚举应回到具体输出上下文

保存正文描述从404和PHP产品指纹到扩展路径、参数及路径XSS的发现顺序，图片只有奖励。把404响应也作为可检查的处理器，保留原始响应、实际路由、参数来源和HTML消费上下文，用许可的小词表逐步收敛。产品名、猜中的PHP路径、反射或奖励不证明执行；按原始字节和浏览器无害标记确认。

来源：[保存帖1](https://x.com/i/status/1557167739139002368)。


## XSS探测流程应保留单变量过滤与消费证据

保存图片建议先试无害HTML、残缺标签、编码控制字符和黑名单变体。以原始文本对照开始，一次只改变一个因素，保留请求字节、服务端转换、响应和实际DOM，区分过滤、规范化、反射与执行。以无害唯一执行标记和真实消费上下文收敛结论；有限候选列表不代表全面XSS覆盖，过滤接受也不证明漏洞。

来源：[保存帖1](https://x.com/i/status/1558149086293131266)。


## XSS流水线的中间结果必须保留原始输入和消费证据

保存正文和图片将爬虫、历史URL、过滤、去重及Dalfox/Nuclei连接，另用正则找message监听器。逐阶段记录原始URL、规范化、参数丢失、外部来源、规则版本和请求预算；正则命中只证明候选代码存在。最后独立核对输入到浏览器消费位置、CSP和无害执行或回调关联；HTTP200、监听器、工具命中或历史列表不代表XSS。

来源：[保存帖1](https://x.com/i/status/1558407353006845953)、[保存帖2](https://x.com/i/status/1560212513077305345)、[保存帖3](https://x.com/i/status/1560621538868854784)。


## SVG事件与表情候选需要实际解码和插入上下文

图片展示SVG候选与弹窗，另有localhost表情乱码加img事件；正文给出不同事件字符串。记录请求与响应字节、编码、HTML解析、转义、CSP和必要交互，比较无害对照，排除本地修改或研究者自身环境。乱码或表情不自动成为绕过原因，历史Cloudflare题名和弹窗不证明当前通用绕过；存储型还需持久化与第二个自有消费者。

来源：[保存帖1](https://x.com/i/status/1559238965630468096)、[保存帖2](https://x.com/i/status/1559427933139218433)、[保存帖3](https://x.com/i/status/1559543613368975361)、[保存帖4](https://x.com/i/status/1559332579802812424)、[保存帖5](https://x.com/i/status/1559520075409129472)、[保存帖6](https://x.com/i/status/1559570688134057988)、[保存帖7](https://x.com/i/status/1560036487940526081)。


## 结账页脚本影响只用自有假数据评估

正文因alert受限而声称记录结账输入。弹窗限制不等于所有脚本不可执行，也不能凭宣称推断支付风险。核对真正可控输入、页面消费位置和允许的脚本行为，使用自有隔离结账环境及假字段观察最小标记，不采集信用卡、真实输入或发送数据到外部。真实证据和影响链必须分开记录。

来源：[保存帖1](https://x.com/i/status/1559272038358982664)。


## 重复参数和截断的Jira载荷不能直接证明反射执行

保存正文给出 Wallboard URL，包含重复 dashboardId 与被截断的 cyclePeriod 脚本候选。先核对实例版本、参数顺序及重复值在代理、服务端和前端的取值规则，再确定该值最终进入 HTML、脚本还是其他上下文。使用自有无害标记记录原始响应和浏览器消费，若主张执行还须观察实际执行及相关限制。截断载荷无法证明语法完整；不要读取或外传 cookie，不把产品名称和 URL 当作普遍漏洞结论。

来源：[保存帖1](https://x.com/i/status/1560922081801404417)、[保存帖2](https://x.com/i/status/1561339153551446017)。


## 邀请邮件与支持页面弹窗需要区分渲染器

正文把公司名称中的输入带入邀请邮件，截图弹窗来源是临时邮箱站点；另一帖在自有账户的支持页看到弹窗。分别记录发送应用、原始邮件或持久字段、接收端渲染器与执行 origin，再用第二个自有消费者检查存储和跨用户边界。发送应用的 HTML 注入、邮件客户端的脚本执行和仅自己触发是不同证据。只用无害标记，不从弹窗直接推导账户接管，不把邮箱站点的问题归给发送应用。

来源：[保存帖1](https://x.com/i/status/1561975177415561216)、[保存帖2](https://x.com/i/status/1563210055096291328)、[保存帖3](https://x.com/i/status/1562007923051610114)。


## 历史CVE批量命中需复核实例与浏览器消费

保存正文和模板输出把 logout_redirect.do 的 sysparm_url 候选标为 ServiceNow XSS/CVE，报告列表又包含重复与不受理状态。绑定每个实例版本、模板版本、输入、重定向处理和浏览器实际消费，用无害标记验证具体执行上下文。CVE 标签、扫描数量和报告列表不证明当前漏洞、补丁状态或所有报告都重复；声明的升级影响仍需独立证据。遵循项目修复和复测政策，不重放真实 cookie 获取载荷。

来源：[保存帖1](https://x.com/i/status/1562960974654582784)、[保存帖2](https://x.com/i/status/1563189288845873156)、[保存帖3](https://x.com/i/status/1564535610718781441)、[保存帖4](https://x.com/i/status/1565287742262714368)。


## 混合XSS载荷需还原解码和HTML修复过程

正文包含多种标签闭合、注释、编码、事件和 JavaScript 片段，图只有报告状态。保留原始字节与每层解码后值，核对应用输出、浏览器解析后的 DOM、真实事件触发及策略；多种候选并列不代表万能向量。一次只验证一个上下文与无害标记，畸形标签可能仅作为文本或被修复。报告标题、Triaged 和奖励不能替代执行证据。

来源：[保存帖1](https://x.com/i/status/1563161124362539009)、[保存帖2](https://x.com/i/status/1563253624670912513)、[保存帖3](https://x.com/i/status/1563804220431937537)、[保存帖4](https://x.com/i/status/1563956265164079104)。


## SVG动画事件候选须核对实际插入方式

正文和图展示 SVG animate 的 onend 候选及浏览器弹窗。保存具体请求、解码层、HTML/SVG 插入方式、事件时间、浏览器与策略，用无害标记核对实际执行。显示 SVG、允许上传或报告弹窗均不自动说明其他消费者可触发；cookie 可见性与会话影响仍分开验证。不复制图中的 cookie，不从单个向量推导全面绕过。

来源：[保存帖1](https://x.com/i/status/1564140655617929217)、[保存帖2](https://x.com/i/status/1564634662886150145)。


## XSS升级标题需要逐跳补齐权限证据

正文将 XSS 与 CMS 命令、恶意软件下载及 AWS SSRF 并列，图片只保存研究封面，未保存完整链条。已有脚本执行不直接赋予服务端命令或内部网络能力；需要分别核对消费者身份、受保护接口、组件版本及下一动作的实际许可前提。用隔离自有环境与无害标记表达已确认的权限变化，不安装恶意软件、建立 hook 或访问云秘密；外链全文依用户按覆盖，不补造文章步骤。

来源：[保存帖1](https://x.com/i/status/1565733814588129286)、[保存帖2](https://x.com/i/status/1565733817440243713)、[保存帖3](https://x.com/i/status/1565733820363587584)。


## 浏览器Hook演示不替代初始XSS证据

Toxssin 图展示已加载 handler 后的会话、按键、表单及响应日志。先证明不可信输入如何在消费者浏览器执行，明确 origin、身份及策略；工具收集能力与初始漏洞是不同边界。使用自有无害标记说明最小影响即可，不收集密码、cookie、键盘或第三方内容，不建立持续 hook。200、session active 和宣传不能证明任意用户均可受影响。

来源：[保存帖1](https://x.com/i/status/1563923007969583105)、[保存帖2](https://x.com/i/status/1564016278301548544)、[保存帖3](https://x.com/i/status/1564032872432177152)。


## 人工子域检查需要保留已查入口与证据

正文建议人工逐一检查子域并宣称 DOM-XSS，未保存具体数据流。将许可子域列表、实际访问、身份、脚本来源和消费点记录，人工与自动结果各自保留误报和遗漏；逐一访问不代表所有状态、路由和参数已覆盖。DOM-XSS 仍需 source 到 sink 的无害执行证据，不用宣称或弹窗描述代替完整链条。

来源：[保存帖1](https://x.com/i/status/1561762300767633408)。


## 上传文件名和SVG脚本要区分各消费者

上传清单含文件名中的标签、SVG script/onload 及 window.location。分开检查业务页面如何输出文件名、SVG 是图片引用还是独立文档/嵌入、执行 origin、响应 Content-Type 与 CSP。用自有无害标记在实际消费者验证，再检查第二个自有用户边界。孤立 SVG 页面执行不等于业务源存储 XSS；内容自身导航也不自动证明服务器开放重定向。保存示例只能作为这些消费者的候选。

来源：[保存帖1](https://x.com/i/status/1566093568909144064)。


## 方法变化和构造器载荷仍须证明初始XSS入口

正文建议GET不反射时换POST，又给hash/eval及Object.prototype扩展和Function构造器字符串变换。先定位实际路由、方法、Content-Type、身份和输入如何进入HTML/事件/脚本sink；用无害标记证明消费和执行。手动注入脚本后读取hash或修改原型已经依赖代码执行，不证明独立DOM-XSS或原型污染写入原语。POST变化也需单独核对实际处理器，禁止在真实页面执行档案代码或变更全局原型。

来源：[保存帖1](https://x.com/i/status/1565956036942770178)、[保存帖2](https://x.com/i/status/1569171632337592320)、[保存帖3](https://x.com/i/status/1569221158771499008)。


## 免括号语法候选仍依赖具体脚本消费者

保存内容从 img 属性、SVG、tagged template、onerror、隐式转换到免括号清单。先画出输入到 HTML/属性/脚本字符串/JavaScript 语法的消费路径，保留实际序列化、浏览器版本和有效 CSP。已有脚本上下文中的表达式技巧不能直接用在文本节点或转义字符串中；以无敏感标记验证实际执行与不执行对照，管理员消费和跨用户影响需单独证据。

来源：[保存帖1](https://x.com/i/status/1569302976615051267)、[保存帖2](https://x.com/i/status/1569839253621981186)、[保存帖3](https://x.com/i/status/1570789618798174209)、[保存帖4](https://x.com/i/status/1572634517067943937)、[保存帖5](https://x.com/i/status/1572995919821549570)。


## SQL挑战的无结果反射还有独立HTML消费者

同一 PHP 截图在无结果分支反射 q。先核对 Content-Type、输出编码、实际 HTML 节点/属性以及最终浏览器解释，用无害标记比较经过 SQL 替换后的输入。SQL 逃逸修补不等于 HTML 安全，反射也不等于执行；需独立 sink 与阴性对照，不能把 SQL 标签替代 XSS 判断。

来源：[保存帖1](https://x.com/i/status/1571849043088662530)。


## CSP阻断与另一浏览器弹窗必须保留同源条件

一图有 SVG onload DOM 节点，另一图是项目以 CSP 阻断关闭，第三图另浏览器 alert 6。完整保存同次请求的原点、响应 CSP/Report-Only、iframe sandbox/继承、用户动作及具体执行上下文，再比较跨浏览器行为。DOM 存在不是执行，孤立弹窗不能反推先前环境；图缺少完整策略与复现时不能宣布 Cloudflare 或 CSP 通用绕过。

来源：[保存帖1](https://x.com/i/status/1572071789177479170)。


## 盲XSS通知计数不能替代输入到消费者归因

XSS Hunter 列表仅显示 fired 通知和数量。记录每个唯一自有 canary 的输入位置、存储/延迟触发、消费者原点、实际时间和无敏感执行标记，排除自己预览、扫描器或多个重复通知。回调数量不等于不同漏洞，也不自动说明管理员权限或凭据窃取；没有具体消费者时保留待验证边界。

来源：[保存帖1](https://x.com/i/status/1572510135247044608)。


## Dalfox discovery 与浏览器及 blind 验证分开

Dalfox 选项图区分 selected parameters、only-discovery、DOM/headless 和 blind。先保存真实参数与回显上下文，仅发现模式不能证明脚本执行；浏览器验证保留来源 origin、DOM、CSP 和无害标记。blind 使用自有回调并区分请求接收、页面触发和执行上下文，不让扫描器批量写入共享通知渠道。

来源：[保存帖1](https://x.com/i/status/1573326367910813698)。


## https 字串存在与无条件前缀不是同一过滤

保存帖一方面说在值前加 https://，另一方面提供含 https:// 字串的 javascript 表达式，两者不能无条件同时成立。先确认实际代码是字串包含检查、前缀追加、URL 解析还是 HTML/DOM sink；记录保存值、最终 DOM 属性与浏览器解析后的 scheme。用无害本地标记验证执行，不能复制 document.cookie 或把这条候选当所有前缀防护通用绕过。

来源：[保存帖1](https://x.com/i/status/1573798925471031301)。


## 集成 Jira title 的渲染到 POST 链保留缺失 gadget 边界

报告截图摘要描述 Jira issue title 缺 HTML 编码，HTML/CSS 注入经 gadget/浏览器行为升级 POST，保存内容没有具体 gadget。审计集成外部字段到模板/DOM，再到同源 script/请求的每一步；保留编码、origin、浏览器和会话条件，用自有字段无害标记。POST 发出、受保护动作接受和 OAuth/SAML 身份变化分别证明，不能按摘要补全接管或创建管理员步骤。

来源：[保存帖1](https://x.com/i/status/1575285299340611584)。


## noscript 解析模式与 WAF 事件词不能生成通用绕过

noscript 候选依赖 HTML parser 的 scripting 模式、上下文与后续重新解析；[HTML noscript 规范](https://html.spec.whatwg.org/multipage/scripting.html#the-noscript-element)说明其解析会随模式变化。核对消毒器输入/序列化/最终 DOM 与真实浏览器，不能只查字串。另帖声称含 on 词可绕 Cloudflare，这只是候选；逐层比较 WAF 动作、源站接受、CSP/事件实际执行和同源无害标记，不把放行或词出现当 XSS。

来源：[保存帖1](https://x.com/i/status/1575788805155848193)、[保存帖2](https://x.com/i/status/1575792952336867328)。


## XSS shell 流水线先修正输入和保留请求语义

保存 XSS automation 管道存在域名/列表输入混淆与未配对引号，不运行原命令。核对各工具当前输入格式，保存 URL 来源及完整方法、认证、参数名/顺序、重复值、编码和正文；统一替换值/格式化去重可能丢失关键上下文。kxss/字串反射仅发现候选，真实浏览器执行仍需 sink、origin、CSP 和无害标记，不能把 results 文件当已确认 XSS 清单。

来源：[保存帖1](https://x.com/i/status/1576395687398322176)。


## 邮件 iframe 假设要确定实际渲染和过滤消费者

保存问题只询问 email iframe，没有示例响应。分别确定邮件模板、提供者过滤、浏览器/webmail 客户端、sandbox 与 origin；字段包含 iframe 不证明标签保留或脚本执行。验证限自有模板/收件箱，以无害显示标记保留提交值、过滤后 HTML 和实际 DOM，缺消费者实证的假设不记为 XSS。

来源：[保存帖1](https://x.com/i/status/1574001996583018501)。


## 字符索引形式的安全头要追溯生成与浏览器处理

响应截图把头文本拆成0、1等数值字段和单字符值。保留原始线上响应，追踪容器类型与序列化，再核对实际Content-Security-Policy和浏览器生效策略。旧X-Content-Security-Policy文字与真正CSP字段不能等同；畸形字段不自动证明可利用XSS，需要具体消费者和无害执行对照。

来源：[保存帖1](https://x.com/i/status/1576855414632611841)。


## 盲 XSS 追踪提交字段到异步渲染消费者

归档给User-Agent替换、signup/demo表单、邀请用户名/mention和票务摘要。每个标记绑定具体请求、身份、时间与字段，追踪后台、邮件、预览、mention或工单消费者及执行origin；延迟通知和多封邮件不等于多个独立漏洞。限定精确范围与自有收件/管理环境，用无害可见标记，DNS/HTTP取回不等于JavaScript执行；不收集cookie，不从通知推导ATO。

来源：[保存帖1](https://x.com/i/status/1577289727031791617)、[保存帖2](https://x.com/i/status/1578711850505510912)、[保存帖3](https://x.com/i/status/1579028378832994304)、[保存帖4](https://x.com/i/status/1579155261125582850)、[保存帖5](https://x.com/i/status/1579621316642086913)。


## jQuery UI 选项注入按初始化与后续事件分开验证

保存卡列position.of、dialog.closeText、tooltip/title与dialog/title等历史消费者。核对部署代码、实际版本、输入到选项或属性的数据流、组件初始化及需要悬停等触发；URL里有HTML文字不自动进入这些sink。仅在自有环境保留无害执行与对照，不把卡片CVE版本标签直接作为当前漏洞结论。

来源：[保存帖1](https://x.com/i/status/1577654011364528130)。


## Flask 字符删除不能覆盖 HTML script 与 DOM 两层

挑战源码在/profile取name、删除单引号后格式化到script中的JavaScript字符串，随后innerHTML追加。分别核对请求解码、Python类型、HTML script结束、JS字符串和DOM解释消费者；单字符删除不构成各层上下文编码。用隔离页面无害标记保存真实返回与DOM，不因有innerHTML就省略上游可控性/初始化证据，缺参错误与XSS分开。

来源：[保存帖1](https://x.com/i/status/1579458374110187520)。


## 盲 XSS 管道修正输入类型与异步来源边界

subfinder输入写成http://target.com，gau后grep &会遗漏单参数/POST/无query入口。先核对实际工具输入、候选来源和范围，保留失败、去重与主动预算；每个无害标记绑定原请求和异步consumer。第三方blind地址及script示例不直接复用，回连不自动证明浏览器执行或管理员权限。

来源：[保存帖1](https://x.com/i/status/1580287926709399555)。


## 跨移动入口到缓存 XSS 要验证每个消费者

正文称网站WAF拦截、移动入口写username、xss.css被缓存，图仅Triaged通知。核对移动写入身份/范围、实际缓存key、内容类型、响应内容与浏览器嵌入origin，用自有唯一key验证写入与独立消费；.css路径和HIT不能证明JavaScript执行，XSS与最终账户权限分开。

来源：[保存帖1](https://x.com/i/status/1580493358770065409)。


## Linkpop 回归与 self XSS 按新旧存储值和消费者验证

截图有旧name残留blindscript、onboarding前几步及addlink javascript输入。区分历史存储内容、当前新写入、管理preview与公开访问、用户点击/输入、origin与CSP；旧回连不自动证明新版本回归。先在自有页面保留无害执行对照，self执行不能直接推广其他用户或ATO，未保存后续不造。

来源：[保存帖1](https://x.com/i/status/1580629610676486146)、[保存帖2](https://x.com/i/status/1580629724346343442)、[保存帖3](https://x.com/i/status/1580675292858826754)。


## ESI 头字段再渲染与 HttpOnly 保护边界分开验证

图中ms字段调用ESI读取HTTP头，另title消费者反射XSS。HttpOnly限制脚本直接读cookie，不能代替服务器对头再输出的编码/权限；分别确认实际ESI启用、可控模板、输出身份/缓存隔离、浏览器同源consumer与权限。用自有非敏感头canary替代cookie，未证明最终会话使用不称ATO。

来源：[保存帖1](https://x.com/i/status/1580933021531766787)。


## Markdown 表单注入与脚本执行分开保留消费者

GitHub截图显示Markdown里登录表单/input/button/textarea，没有提交或执行证据。核对原始标记、过滤后DOM、form action、origin、交互和可见用户，HTML保留不自动XSS。自有页面用无害显示/事件对照，不收集登录信息，奖金额与标题不替代实际跨用户影响。

来源：[保存帖1](https://x.com/i/status/1581712464248377344)、[保存帖2](https://x.com/i/status/1581893849403645953)。


## 营销参数的 CSS 动画事件按实际模板验证

Shopify摘要显示utm_source输入尝试结束属性、设置animation-name与animationstart；未保存完整DOM/执行环境。保留解码、引号边界、过滤后HTML、CSS动画是否触发和浏览器/CSP条件，用无害事件标记核对实际origin。反射、样式保留、截图称alert和奖励分别是不同证据，不从旧案例推广当前网站。

来源：[保存帖1](https://x.com/i/status/1582279342905868288)。


## 404 中的执行现象先定位反射与 DOM 消费者

截图可见404消息、损坏图片及alert遮盖，但不足定位是服务端反射还是DOM插入。用保存原始响应、过滤后DOM、脚本调用和无害标记确定URL输入流向与执行origin；状态404不排除渲染执行，alert样式也不单独证明路径。cookie示例不用于采集真实会话，缺失消费者代码保持未知。

来源：[保存帖1](https://x.com/i/status/1582423752733704192)。


## 单一 alert 样式不能代表输入上下文覆盖

正文批评到处重复script/alert，续篇未保存，图只Stored XSS裁决元数据。先定位实际HTML/属性/JS/URL消费者、解码/编码和触发条件，再用无害标记做针对性对照；同payload无效不能推出无XSS，同payload命中也不保证独立发现。重复率/赚钱宣称不作为证据，不补造第二部分。

来源：[保存帖1](https://x.com/i/status/1584154357314260993)。


## 扩展 detected 输出仍需实际浏览器执行证据

S3C窗口列POST/GET/hidden参数测试和detected链接，没有DOM或执行截图。记录参数解析、请求身份、响应上下文、过滤后DOM、浏览器origin/CSP与触发方式，区分反射候选、工具启发式和无害脚本执行。工具结果数量与下载价格不证明漏洞或当前兼容，不执行归档扩展。

来源：[保存帖1](https://x.com/i/status/1584499669413285890)。


## Swagger 的 HTML 注入与脚本执行分层保留

两图分别供应商确认RXSS摘要与HTML injection摘要，另一弱点标签写DOMXSS但没有真实执行。记录实际部署/组件版本、可控参数/规范来源、渲染DOM、脚本/事件触发、origin和CSP，分标记保留与浏览器无害执行。旧组件、裁决标签和修复建议不证明当前环境，不用标题补造消费者或ATO。

来源：[保存帖1](https://x.com/i/status/1584815803328872448)、[保存帖2](https://x.com/i/status/1585903711359991808)。


## Jolokia 错误路径与 mimeType 消费者独立确认

图述旧1.3.5在read路径输入SVG事件并mimeType=text/html，只有摘要/版本缩图，未见完整响应和执行。核对实际部署版本、解码、错误body上下文、最终Content-Type/CSP和浏览器解析，以无害标记确认origin与触发；版本命中或参数能设置不证明执行。不要用真实cookie演示或补造旧外链漏洞细节。

来源：[保存帖1](https://x.com/i/status/1585903822291013632)。


## XSS 流水线的过滤损失与浏览器入口必须分开记录

保存命令组合历史 URL、gospider、gf、qsreplace、dalfox/nuclei；grep 200、awk 第五列、grep 等号、sed 截断到等号与扩展名黑名单都依赖输出格式，可能丢失多参数、非 200、路径输入及 JS/SVG/PDF 等资源。另一路正则只找 JS message 监听。保留原 URL 与每步损失计数，在授权小样本比较过滤前后真实入口、消息 origin/source 校验及实际 sink。扫描标签、监听存在和参数反射均不能代替浏览器执行证据。

来源：[保存帖1](https://x.com/i/status/1585946214935076864)、[保存帖2](https://x.com/i/status/1586456101260001282)、[保存帖3](https://x.com/i/status/1588147320625012738)。


## XFF 盲 XSS 候选须绑定后台渲染而非仅外部交互

subfinder/gau/bxss 示例把脚本放入 X-Forwarded-For，并引用远端脚本域；域输入不应直接混用完整 URL。可提炼的是请求头值被记录、随后在管理界面未编码渲染的路径。验证只用授权请求和自控无敏感内容标记，区分日志保存、页面渲染、脚本执行及 DNS/HTTP 请求，关联精确原请求与浏览器主体。第三方脚本内容、回调或命令成功不等于盲 XSS，禁止将归档地址用作默认接收端。

来源：[保存帖1](https://x.com/i/status/1585947999716327424)、[保存帖2](https://x.com/i/status/1586219904117547008)、[保存帖3](https://x.com/i/status/1586353857747353606)、[保存帖4](https://x.com/i/status/1598733522587783168)。


## CSP 策略评估结果需结合可控输入与实际指令生效

CSP Evaluator 截图含 unsafe-inline/unsafe-eval、主机白名单、缺 object-src 及未知指令等样例告警；正文列 JSONP、固定 nonce、上传同源文件及 Angular 场景。审计先保存实际响应 policy、浏览器执行上下文与可控资源，分别验证注入位置、允许来源及 nonce 生命周期，比较修正策略后的同一无害标记。工具样例、宽松指令或允许域本身不构成 XSS；Report-Only、多个策略及不可达资源会改变结果。

来源：[保存帖1](https://x.com/i/status/1586008108555452416)、[保存帖2](https://x.com/i/status/1586009915172134912)。


## 社交链接脚本协议可绕过 cookie 读取限制转向同源令牌接口

Linktree 报告描述 SocialIcon URL 未校验而允许 javascript URI；HttpOnly 无法直接读 cookie，但脚本可带现有 cookie 请求同源 /api/token 取得 accessToken。在自有隔离页面验证 URL 规范化、协议允许集、点击触发及同源接口权限，仅记录无害调用/脱敏字段。HttpOnly 不消除同源脚本操作能力；必须区分脚本执行、接口返回和可用权限，不复用图片中外送地址或真实令牌。

来源：[保存帖1](https://x.com/i/status/1587065170718867457)。


## 编码、script 边界及事件属性要回到实际 HTML 上下文

材料包含 terminalId 反射到 script 双引号、路径 URL 编码脚本、混合大小写闭合及 input value 后的 onfocus/autofocus；另正文建议 %00 分隔事件名，图本身未显示 null 字节。对每个例子保存原输入、传输编码、各层解码与最终响应/DOM，用无害标记比较闭合成功、编码后文本及实际事件触发。单 alert/prompt 和大小写变化不是通用 WAF 绕过；%00 是否到达 sink/被拒绝或处理必须单独证明，不能由正常事件属性图倒推。

来源：[保存帖1](https://x.com/i/status/1587065393239162884)、[保存帖2](https://x.com/i/status/1587158497854390273)、[保存帖3](https://x.com/i/status/1587789074009493504)、[保存帖4](https://x.com/i/status/1587845111211298817)、[保存帖5](https://x.com/i/status/1588057101552664577)、[保存帖6](https://x.com/i/status/1588145891600392195)。


## 第三方评论 RSS 需对来源标题按 XML 上下文编码

IntenseDebate 报告将自有博客 title 经评论传播到平台 comments.rss，未编码标题含 XHTML 命名空间 script。审计跨系统的数据链、RSS MIME/编码和浏览器解析，在自有示例比较纯文本、正确 XML 编码与未编码标记的响应及无害执行效果。保存报告描述的是当时案例，当前阅读器/下载行为可能不同；XML 中出现 script 字面量并非自动执行，不能把第三方源传播归类为原站任意执行。

来源：[保存帖1](https://x.com/i/status/1587745794479853568)。


## 盲 XSS 接收记录应关联精确请求和后台浏览器消费者

保存帖子讨论历史 XSS Hunter 下线与自托管 ezXSS，图为演示报告列表；另帖称主题反馈隔天回调以及 admin login 的 UA 盲 XSS，后者仅猜测后台日志。用授权自控无敏感标记记录原请求、存储位置、渲染页面、浏览器主体与回调时间，区分 DNS/HTTP 交互和实际脚本执行。接收平台条目、奖金、时间延后和作者猜测不足以证明消费者；归档服务状态不代表当前产品，不使用第三方收集地址或收集 cookies。

来源：[保存帖1](https://x.com/i/status/1588539061353996288)、[保存帖2](https://x.com/i/status/1589710379935899648)、[保存帖3](https://x.com/i/status/1590210938619428864)、[保存帖4](https://x.com/i/status/1590312871220871168)。


## 主题 CSS 路径拼接只是客户端消费链的一个阶段

Acronis 图显示 color_scheme 拼进 /mc/theme.PARAMETER.css 并发起客户端 GET/加载 CSS。审计原参数、路径规范化、资源选择、响应 MIME 及 CSS/JS 实际解析，隔离用无害样式标记比较合法主题与异常路径，确认访问主体。保存图仅含链首，缺跳转、跨主体读取和敏感外传，不把 CSS 路径可控直接写成帐号接管或完整 XSS 链。

来源：[保存帖1](https://x.com/i/status/1588637364016058368)。


## 反射、特殊标签和隐藏参数要绑定实际 HTML 或脚本上下文

保存例子有 market description 的 iframe/javascript、Harvard 登录弹窗、onpointerenter 逗号表达式、py-script 转义文本、SVG/style/data 与 Param Miner 隐藏参数反射进 JS。先保存输入如何解码、落入 HTML 属性/URL/脚本/模板的字节、实际 DOM 与触发事件，再在自有隔离页面比较纯文本/正确编码和无害标记。特殊运行时如 PyScript 必须实际加载并消费内容，逗号事件还需变量定义及事件可达。弹窗照片、URI字面量和参数反射不证明跨用户执行；不保留图中的 cookie 值，不补造遮挡 URL 或外链 PoC。

来源：[保存帖1](https://x.com/i/status/1588818774438076417)、[保存帖2](https://x.com/i/status/1589559693411655681)、[保存帖3](https://x.com/i/status/1589660745935257600)、[保存帖4](https://x.com/i/status/1589659325869744129)、[保存帖5](https://x.com/i/status/1589704164351016960)、[保存帖6](https://x.com/i/status/1590781532049969160)。


## 短载荷、错误回调和 WAF 品牌标签都依赖解析上下文

保存表和说明包含 TinyXSS 的 inline/eval/external/frame/browser 条件、SVG 大小写/假属性/Unicode标识/注释与 tagged template、throw/onerror/Errorname/eval 以及脚本上下文建议。审计 HTML tokenizer、事件属性、JS表达式/字符串、运行时与实际 CSP，以隔离无害标记比较同一输入在正确编码和原始拼接下的 DOM/执行。原文部分明确猜测过滤器；厂商名、短字符串和无版本的Chrome/Firefox声明不能推出通用或当前绕过，不复制为默认攻击字典。

来源：[保存帖1](https://x.com/i/status/1589945124020432896)、[保存帖2](https://x.com/i/status/1590047424890142720)、[保存帖3](https://x.com/i/status/1590050577098354688)、[保存帖4](https://x.com/i/status/1590050997594124288)、[保存帖5](https://x.com/i/status/1589658254883577860)、[保存帖6](https://x.com/i/status/1589817853351694336)。


## Self-XSS 的标签输入仍需证明另一主体自然触达

保存 suggest tag 图含脚本输入，服务方摘要说仅影响自己。记录存储范围、读取页面、角色、触发动作和浏览器执行，在自有 A/B 对照正常访问者是否无需自注入即可触发。标题 stored XSS、输入含script或自身弹窗都不证明他人影响；缺 CSRF/OAuth 等转换链不能升级为帐号接管。

来源：[保存帖1](https://x.com/i/status/1590066518045458434)。


## 爬取到 Dalfox 的触发标签仍需浏览器执行对照

保存命令用 Katana/qurl→Dalfox，图为教学站cat参数，包含反射、SQL错误、found DOM Object/Triggered 与PoC URL。先保存每一步过滤/去重的原始URL、参数位置与响应，再在自有隔离页面验证真实DOM、事件触发和无害执行，比较正确编码/不可达事件。工具标签或错误行不证明独立真实目标漏洞，更不能把练习站结果外推到当前资产；未执行流水线。

来源：[保存帖1](https://x.com/i/status/1590800226180542464)。


## 参数名、Base64 与无括号脚本都要追踪浏览器解释层

保存查询参数名字表、constructor tagged template、HTML注释/script组合、message Base64、隐藏参数及 redirectUrl/returnPath 的 javascript 候选。记录原始输入、每层解码、最终 HTML/JS/URL、事件或导航触发及浏览器主体，在隔离页面比较纯文本/正确编码与无害标记。参数名、Base64 字符、URI 字面量和短payload不证明执行或他人触达，不能把工具/奖励图当完整DOM证据。

来源：[保存帖1](https://x.com/i/status/1591203119173865472)、[保存帖2](https://x.com/i/status/1591519218994151424)、[保存帖3](https://x.com/i/status/1591764931308883970)、[保存帖4](https://x.com/i/status/1592213985344237569)、[保存帖5](https://x.com/i/status/1593230199159914498)。


## 替换关键词后拼 script 的缺陷是代码上下文信任

代码示例把search值替换 prompt/confirm/print及部分符号后拼 <script> 再送 jQuery .html。审计未加全局标志的首匹配、JS构造和最终DOM，在隔离样例用纯文本/正确输出编码与无害值比较。黑名单删字符不是代码上下文编码，jQuery版本名字本身也不证明漏洞；缺真实站点不外推为当前库缺陷。

来源：[保存帖1](https://x.com/i/status/1591393173548720128)。


## Self-XSS 借静态后缀缓存影响他人需证明同一缓存键

保存示意 /my_profile 不缓存而 /my_profile/xss.css 返回同页面可能缓存；另帖仅有 cache poisoning→stored XSS 外链。隔离自有 A/B 会话追踪源站路由、缓存键/主体、MIME/下载行为、命中与无害执行，确认其他主体无需自行注入即可读到缓存内容并清理实验缓存。静态后缀、缓存命中和自身弹窗各自不足以形成链，缺外链步骤不补造，不污染公共缓存或给用户发链接。

来源：[保存帖1](https://x.com/i/status/1591410557185294337)、[保存帖2](https://x.com/i/status/1592383958217420800)。


## Host 中的 HTML 片段只有经过后台渲染才可能盲执行

正文将img片段置于forgot_password Host，缺响应/渲染位置。追踪实际接收Host、路由、邮件/日志/管理界面是否消费，在隔离自控帐号用无敏感标记比较正确编码与拼接并关联浏览器主体和原请求。Host可控、记录保存或网络回调不是完整XSS，重置链接污染与HTML渲染分开，不往真实后台注入外部收集载荷。

来源：[保存帖1](https://x.com/i/status/1592598195032723456)。


## 模板中已编码 fullname 不保护同一行其他字段

deployKeyRowHtml图片把key.title、avatar_url、isActiveClass插进HTML标签/属性，fullname另有escape调用。逐字段核对可控来源、引号/文本上下文、后续DOM sink和真实CSP，以隔离无害值比较正确上下文编码与原始插值。某字段escape或CSP存在不能保护别的消费，但函数局部图也不证明完整CSP绕过或跨角色执行。

来源：[保存帖1](https://x.com/i/status/1592692291583492097)。


## 净化后保留的 data 属性可能被另一个库二次解释

保存v-safe-html报告称DOMPurify删data-remote/url/type/method却保留data-disable-with，Rails-ujs后续当HTML展示，CI job名经错误消息传递且style/class可遮罩引导点击。审计净化输出到第二消费者的属性/时序/上下文，用隔离无害标记比较去掉属性、纯文本处理及原始处理。净化器名字不能证明最终安全；CSP限制脚本不自动限制所有form动作，但缺实际服务器权限结果不能升级管理员接管，不执行截图表单。

来源：[保存帖1](https://x.com/i/status/1592692400765517824)。


## 联系人名字经 quick command 建议框需要再次编码

保存GitLab报告按group启用CustomerRelations→contact firstname/lastname→project issue /add_contacts或/remove_contacts建议框触发。追踪存储字段、读取身份和建议组件HTML sink，隔离自有A/B联系人比较纯文本/正确编码的无害标记。字段在详情页安全不保证替代组件安全，历史15.0与奖励不预定当前影响，缺跨主体执行记录保留限制。

来源：[保存帖1](https://x.com/i/status/1592692508563312641)。


## 反射筛选和跳过 mining 会限制规模化 XSS 的覆盖

保存subfinder→httpx→Katana→Gxss100→Dalfox且跳过bav/mining/grepping，转述帖仅重复标题。离线保留每阶段原URL、参数/状态、错误和筛选损失，用隔离小样本核对真实HTML/JS/事件消费者及无害执行；审计并发和工具动作。被过滤的非反射/路径/存储输入可能仍重要，命令成功与候选数不代替浏览器验证，不运行批扫。

来源：[保存帖1](https://x.com/i/status/1593581883413110787)、[保存帖2](https://x.com/i/status/1593614894858764289)。


## DoD 的 project 与 plot：事件触发和浏览器执行边界

1593674835904847876-02.jpg 和 1593674945254621187-02.jpg 分别保存 project、plot 参数插入 h1/onauxclick 的报告，要求右键等事件。先在本地可控样例追踪 URL 解码、输出位置、HTML 解析、事件触发与执行主体，再保存原始响应和 DOM；反射文本不自动等于执行，需解释链接如何送达另一个用户。图中把浏览器脚本执行扩展成服务器 RCE 或凭据控制的说法没有对应证据，应单独验证，不能继承。

来源：[保存帖1](https://x.com/i/status/1593674835904847876)、[保存帖2](https://x.com/i/status/1593674945254621187)。


## 编码 NUL 的模板表达式：先确定解码与求值上下文

1593951117490225157-02.png 可见编码 NUL 包裹 constructor 表达式及 alert 1；正文把正常双括号失败与插入 %00 后成功相比。提炼为差异实验：固定框架版本、过滤顺序、URL 解码次数、最终 DOM 和求值器，证明同一输入在何处从文本变为代码。截图不足以确定 Angular 版本或服务端模板执行，不发布通用过滤绕过结论。

来源：[保存帖1](https://x.com/i/status/1593951117490225157)、[保存帖2](https://x.com/i/status/1594032708505997312)。


## 聊天机器人号码输入：HTML 消费、点击条件与跨用户送达

1594007870005190656-02.jpg 保存把 onclick 按钮输入聊天号码字段的报告。核验聊天消息如何被插入 DOM、是否经过安全文本节点/净化、按钮是否需要点击，以及内容能否送达另一个自有用户。保留响应、DOM 与浏览器执行上下文；仅自己输入自己点击可能仍是 self-XSS，报告摘要中的全面控制用户不能代替实际权限证据。

来源：[保存帖1](https://x.com/i/status/1594007870005190656)。


## 短 XSS 列表必须先匹配最终 HTML、JS 与 URL 上下文

保存正文列出 HTML 标签、属性聚焦事件、script 结束、JS 字符串及 javascript URL 等不同输入形状。先定位最终消费者和转义/解码顺序，只测试与该上下文匹配的本地小样本，并记录交互条件、CSP 和真实执行。另帖 href 内把 javascript 写成 javas 空格 cript；普通空格并不自动变成有效脚本协议，必须检查浏览器实际 URL 解析。列表与所谓高成功率不能替代上下文和跨用户送达证据。

来源：[保存帖1](https://x.com/i/status/1594248006907613185)、[保存帖2](https://x.com/i/status/1594503131668570113)。


## Newsletter 的 HTML 转义再入 innerHTML：跨解析阶段审计

1594646225415970817-03.jpg 中 PHP htmlspecialchars 的结果嵌入 JS 字符串，随后拼接 Welcome HTML 并赋值 innerHTML，@ 个数检查仅校验形状。应分别审计 PHP flags/版本、HTML script 文本、JS 字符串转义以及最终 HTML 再解析，不将 HTML 转义当作 JS 或二次 DOM 的通用保护。以本地无害标记记录每阶段字节/字符与 DOM，只有到达可执行消费者才确认 XSS；省略邮件验证代码不能补造。

来源：[保存帖1](https://x.com/i/status/1594646225415970817)。


## PHP 黑盒过滤特征：相似输出不等于同一安全策略

1595052119908057090-02.jpg 对比 htmlentities、filter_var 和多种历史 sanitizer 的输出，并把可保留反斜杠、单引号或再次 URL 解码等情况列为风险。只能将特征当作过滤假设；固定实际运行时、flags、字符集和多阶段编码，检查最终 JS 字符串、HTML 文本/属性或 URL 消费者。保留某字符不自动导致可执行代码，图中通用 vulnerable 注释需收窄，不能凭样例识别唯一函数或宣布通用绕过。

来源：[保存帖1](https://x.com/i/status/1595052119908057090)。


## script 文本终止与字符串转义：两套解析器分开观察

1595842546395410432-02.jpg 把引号、script 结束标签和反斜杠作为测试方向，但例子部分缺变量名；另帖称必须先结束原 script 才执行。先保存最终响应并确定 HTML script 文本与 JS 字符串的边界，检查编码/转义顺序、反斜杠奇偶、CSP 与实际本地浏览器 DOM/执行。JS 字符串转义不自动阻止 HTML 解析器识别结束标签，语法片段也不自动可执行，不把示意列表当成通用成功载荷。

来源：[保存帖1](https://x.com/i/status/1595842546395410432)、[保存帖2](https://x.com/i/status/1597854199735144448)。


## Dovetale 创作者申请：审核者渲染与旧对象加载前提

1597650772929519616-02.jpg 描述创作者姓名字段保存后由品牌管理员审批，包含 object/scriptlet 形状及付费订阅前置条件。核验提交者字段→存储→管理端展示的信任链、上下文净化、跨用户送达、浏览器/插件和审批交互；旧 object 机制不是所有现代浏览器可执行。以自有本地审核样例验证，不沿用外部脚本或创建付费账户，执行与管理员权限影响分别留证。

来源：[保存帖1](https://x.com/i/status/1597650772929519616)。


## 视频发送文本的 stored XSS 摘要：消费者和会话影响分层

1597708447105126400-02.jpg 的双方摘要只说给朋友发送视频时的文本存在载荷，可能会话劫持，没有代码或 DOM。把发送者→存储消息→接收者/后台渲染作为候选链，核验文本插入方式、浏览器来源、CSP 和实际无害执行，分开证明会话 token 的可读性/权限。摘要和 Low 标签不提供具体消费者或接管证据，未保存全文按覆盖但不补造方法。

来源：[保存帖1](https://x.com/i/status/1597708447105126400)。


## 历史保存帖0152：混合标签与事件载荷需回到具体渲染上下文

正文列出混合多标签的 polyglot、details/open/ontoggle、SVG animate/onbegin、SVG onload 等字串。可复用的是识别响应中 HTML/属性/脚本/URL/命名空间位置、解析修复及实际触发事件，再在自有页面验证执行源和 CSP；POST 反射还需接收者可触发的交付路径。缺闭合标签、未定义 domain 变量或仅 WAF 放行都不能算执行，不把例子宣传成通用绕过。

来源：[保存帖1](https://x.com/i/status/1598381423345696768)、[保存帖2](https://x.com/i/status/1598387004919918594)、[保存帖3](https://x.com/i/status/1598395454504726528)、[保存帖4](https://x.com/i/status/1598397196264964098)。


## 历史保存帖0152：统计 postMessage handler 的来源与动作权限

Shopify 历史截图描述 checkout→主站的消息转发及 GA 调用。审计 event.origin、event.source、消息 schema、允许事件/参数和最终动作权限，再区分统计事件污染、可读 cookie、脚本执行与会话接管。缺少 origin 校验不能自动推出任意动作；非 HttpOnly cookie 的链不证明 HttpOnly 读取，下方未保存完整执行步骤不补写。

来源：[保存帖1](https://x.com/i/status/1598401781037498371)。

已实际查看保存图片 `1598401781037498371-02.jpg`：Shopify 历史截图：checkout 页面向主站 postMessage，接收端缺少 origin 校验并调用 GA，提及 cookie/linkid。应核对 origin/source/schema/动作权限及 cookie 作用域，不能由统计调用推导 HttpOnly cookie 或全面接管；下方链条被裁切。


## 历史保存帖0152：富文本策略变更与保存后渲染路径

两个帖子保存同一 Shopify /admin/product、/admin/collections 报告。图中摘要称 HTML 编辑器保存后在后续加载执行，并提到政策开始接受对应富文本 XSS；应核对实际富文本输入、净化/序列化、后续渲染页和接收者权限。政策与版本是历史上下文，截图无完整载荷与执行证据，不把同报告转帖视为两个独立漏洞。

来源：[保存帖1](https://x.com/i/status/1598462567877431296)、[保存帖2](https://x.com/i/status/1598764735389990912)。

已实际查看保存图片 `1598462567877431296-02.jpg`：Shopify /admin/product 与 /admin/collections 富文本存储 XSS 报告，显示政策接受范围变化及保存 HTML 后后续加载执行的报告摘要，没有载荷/接收者权限/执行截图。提炼富文本保存与跨页面渲染路径及政策版本核对。

已实际查看保存图片 `1598764735389990912-02.jpg`：同一 Shopify 存储 XSS 报告的另一张截图；正文、政策和路径一致，仅页面计数改变。合并同一机制，保留两条帖子来源，不重复计作独立漏洞。


## 历史保存帖0152：Swagger 文档加载参数与本地管理端渲染

Acronis 历史截图在本机安装管理端并给出 Swagger url 指向外部页面的路径，未展示完整执行。区分外部文档可加载、格式解析、浏览器渲染/执行与管理员交互的链，记录组件/版本/主机可达性及执行源；localhost 的演示前提不能直接写成互联网免认证接管，不下载或运行档案链接中的安装器。

来源：[保存帖1](https://x.com/i/status/1598779956078776325)。

已实际查看保存图片 `1598779956078776325-02.jpg`：Acronis 历史管理端 Swagger UI 的 url 参数引用外部页面，报告在本机安装运行；未见执行截图。提炼文档加载 URL→解析/渲染权限边界及版本/管理员交互，避免从 localhost 报告推断互联网远程接管。


## 历史保存帖0153：本机事件弹窗与错误页文字分级

教程封面可见本机查询、焦点事件与弹窗，但不包含完整渲染代码或接收者；另一图仅错误页显示被改写文字。分别记录输入、响应位置、事件、执行源和跨用户交付，文字反射/自定义报错不是脚本执行或入侵证明；本机演示不自动有高影响。

来源：[保存帖1](https://x.com/i/status/1600833320194961410)、[保存帖2](https://x.com/i/status/1600852774673321984)。

已实际查看保存图片 `1600833320194961410-02.png`：XSS 教程封面可见 localhost 查询中 contenteditable/autofocus/onfocus 与 alert1 弹窗；下方正文被模糊。可提炼焦点/事件及执行上下文的本机示例，不能由封面获得完整方法或高影响受害者链。

已实际查看保存图片 `1600852774673321984-02.jpg`：ChatGPT /auth/ 错误页显示 Oops 与 hello you have been hacked 文字；没有注入输入、脚本执行、用户交付或服务器改变。仅自定义错误文字不证明 XSS/被入侵，可提炼证据边界纠正。


## 历史保存帖0153：标签结束与映射链接的解析交互前提

正文混合标签结束字串、map/area javascript链接和字符实体前缀。分别记录原始编码、HTML实体解码、上下文、URL协议过滤、实际点击/焦点事件和CSP/浏览器执行；map标签本身不自动运行，中文弯引号/字面\\x转义也不等于响应字节。例子只有候选，不提炼成无交互通用绕过。

来源：[保存帖1](https://x.com/i/status/1602025509256597504)、[保存帖2](https://x.com/i/status/1603111980621254656)、[保存帖3](https://x.com/i/status/1603112860770799616)。

已实际查看保存图片 `1603111980621254656-02.jpg`：img usemap 对 map/area 的 href javascript示例；需实际图像映射、点击交互、URL过滤与CSP/浏览器行为，map标签本身不自动执行。无执行截图，不把示例定为通用无交互XSS。


## 历史保存帖0153：redirect_url 导航到协议消费者

代码图从URLSearchParams取redirect_url，非空直接赋location.href。定位解码、scheme/规范化后来源、导航和脚本执行的边界，用自有接收页/合成页面分别验证开放跳转与脚本协议效果；没有实际执行截图，浏览器与CSP影响不能省略，外部教程内容不补写。

来源：[保存帖1](https://x.com/i/status/1602283123235962880)。

已实际查看保存图片 `1602283123235962880-02.jpg`：JS 教学代码从 URLSearchParams(location.search) 取 redirect_url，非空直接赋 location.href，示例javascript scheme。提炼参数解码→URL scheme/源判定→导航消费者，XSS与跨源跳转需分别验证浏览器/CSP和交付，无执行截图，不假定所有框架效果。


## 历史保存帖0153：净化器标签组合与所有配置入口回归

Rails历史图有svg+style/math+style允许组合保留危险结构，以及select/style在class属性与sanitize参数两种配置路径，补丁只处理一条。建立标签/命名空间×默认/全局/调用参数矩阵，比较净化序列化和浏览器再解析执行，版本升级不能替代配置回归。IRB保留字符串不是浏览器执行证据，未保存下方代码/commit不补写。

来源：[保存帖1](https://x.com/i/status/1603333880542642182)、[保存帖2](https://x.com/i/status/1603333989896491009)。

已实际查看保存图片 `1603333880542642182-02.jpg`：Rails SafeListSanitizer 在 svg+style/math+style 允许组合的历史图，IRB展示消毒前后危险结构保留，version1.4.3；浏览器再解析才证明执行，允许标签组合和命名空间需单独矩阵，不视为默认全部配置受影响。

已实际查看保存图片 `1603333989896491009-02.jpg`：Rails XSS修复不完整：class属性 allowed_tags 与 sanitize 参数两个入口，补丁只处理后者；Rails7.0.3.1配置select/style和升级1.4.2→1.4.3后仍触发的报告文字。提炼全配置入口、默认/覆盖参数与序列化再解析回归，未读下方裁切code/外部commit不补写。


## AngularJS CSTI 的版本表达式以实际编译入口为界

正文列若干版本的表达式，图片仅显示测试标记弹窗。先定位不可信输入是否进入 AngularJS 表达式编译、具体框架版本及配置，区分普通文本输出和模板编译。自有页面用无害算术/标记对照实际消费者、CSP 与模板上下文，再记录受害者可达路径。版本清单、某个弹窗及“1.6 以上”标签均不能保证适用于所有 Angular 或所有部署。

来源：[保存帖1](https://x.com/i/status/1603766377504202752)。

已实际查看保存图片 `1603766377504202752-02.png`：Angular CSTI正文有两段版本标注字串，图仅遮盖域名弹窗。需AngularJS实际编译/表达式消费者、版本/CSP/页面交付与执行源；不是任意Angular/全部>=1.6通用漏洞，弹窗不能证明具体字串和跨用户链。。


## localhost 的 focus 弹窗不能保证绕过任意 WAF

图为 XSS 教学封面及本地 contenteditable/autofocus/onfocus 标记。检查输入是进入属性、HTML 文本还是脚本，聚焦是否自动发生、是否需要交互，以及 CSP/浏览器条件；在自有页面以无害标记记录编码前后值和实际事件。演示环境与远程反射入口、受害者可达性和拦截层不同，不能由标题推出通用 WAF 绕过或更高奖励。

来源：[保存帖1](https://x.com/i/status/1604020469434183680)。

已实际查看保存图片 `1604020469434183680-02.jpg`：XSS payload教程封面本机contenteditable/autofocus/onfocus与alert1、下方正文模糊，显示自有上下文实例不是绕过any filter/WAF或高影响的通用保证。。


## XML 文件扩展名与命名空间均不能独立确认 XSS

保存正文/图将脚本放在 XML 前缀标签内，命名空间写作 http://w3.org/1999/xhtml；另图有 localhost 弹窗但无原始头。审查上传后真实 MIME、浏览器解析模式、精确命名空间、渲染 origin、CSP 和内容转换链。以无害元素/标记在自有消费者比较作为下载、普通 XML 文本和可执行文档的结果。原图的字面 URI 不自动等价于浏览器识别的 XHTML 命名空间；扩展名、代码图与弹窗必须绑定同一原始响应，不能据此宣称任何 XML 都执行脚本。

来源：[保存帖1](https://x.com/i/status/1604364291414450176)、[保存帖2](https://x.com/i/status/1605422534065000448)。

已实际查看保存图片 `1604364291414450176-02.jpg`：localhost/xss.xml prompt图，缺Content-Type、响应正文和原始命名空间；正文http://w3.org/1999/xhtml的字符串需核对是否识别为XHTML。XML扩展名和弹窗不能证明任意XML都脚本执行，记录MIME/namespace/CSP/执行源/用户交付。。

已实际查看保存图片 `1605422534065000448-02.jpg`：XML脚本图与正文同使用http://w3.org/1999/xhtml，未见真实MIME/浏览器解析输出；命名空间字面值不能自动视为标准XHTML，可执行性取决实际消费者/命名空间/响应/CSP，不按扩展名判定XSS。。


## user_oidc 的 Safari 分支要跟踪 HTML meta refresh 消费者

代码截图通过 UA 含 Safari 且不含 Chrome 选择 DataDisplayResponse，把 URL 拼接到 HTML meta refresh。审查 URL 来源/可控配置、属性边界编码、允许协议及文档 CSP，分别记录该分支和其他响应分支。在自有实例用标记比较配置权限、UA 选择、最终 DOM/导航及是否实际执行；用户代理字符串不等于真实浏览器行为。代码拼接可形成候选，但仍需入口控制和可交付性，不能泛化为所有平台账号接管。

来源：[保存帖1](https://x.com/i/status/1604476178848522245)。

已实际查看保存图片 `1604476178848522245-02.jpg`：user_oidc Safari workaround代码检查UA含Safari且不含Chrome，将url直接拼进meta refresh HTML并DataDisplayResponse。提炼可信provider配置→HTML属性转义/URLscheme/CSP与UA分支，可伪UA但平台执行需实测；报告SafariOnly/CSP限制保留，不能推为全部浏览器ATO。。


## self-XSS 升级链逐个证明跨主体传递

正文把缓存投毒、复制 iframe、Cookie 自动登录列为升级方向。先证明输入入口、执行 origin、所需自操作与持久化位置，再以两自有主体对比是否会在另一主体正常访问时执行；缓存方向需确认缓存键和共享范围，登录方向需确认会话与账号绑定。候选链名不能拼成影响结论，要求每个桥接点都有对应请求、状态或浏览器证据；自行粘贴脚本/只影响自己不能自动报告为跨用户 XSS。

来源：[保存帖1](https://x.com/i/status/1604748786064330753)。


## Go 错误消息的 JSON 外形不保证浏览器以 JSON 解析

图片中 invalid license 回显带事件标签并出现域名弹窗，缺真实响应头/原请求。追踪 license 来源→错误构造→实际响应 MIME/文档消费者→浏览器解析，分别比较正确 JSON 编码和 HTML 错误页面分支；用自有标记确认最终 DOM 和实际脚本 origin/CSP。若响应只作为 JSON 数据处理且后续安全文本输出，回显不是 XSS；服务语言或正文长得像 JSON 不代替消费者证据。

来源：[保存帖1](https://x.com/i/status/1604972153585405952)。

已实际查看保存图片 `1604972153585405952-02.jpg`：Go接口invalid license错误消息回显img事件并见域名弹窗；JSON形状正文不等于实际application/json MIME，缺响应头/CSP/原请求上下文。检查真正HTML消费者、错误分支编码和受害者可达性，不因语言而推断安全。。


## 混合大小写、制表符和反引号字符串按真实 URL 消费者检验

正文说直接 javascript 字符串失败后尝试大小写及 ASCII tab 变体，图片仅奖励邮件。先分开服务端过滤、HTML 实体/字符解码、属性值构造及浏览器 URL scheme 解析，在自有夹具用无害标记记录各层原始值与最终导航/执行。某个过滤接受字符串不等于浏览器执行，更不等于受害者可达；反引号在普通文字、模板字符串或 HTML 中意义不同，奖金也不是具体绕过机制证明。

来源：[保存帖1](https://x.com/i/status/1605214585270714369)、[保存帖2](https://x.com/i/status/1605271959721611264)、[保存帖3](https://x.com/i/status/1605394299566579713)。


## 字符变体和 tagged template 分别通过实际解析层验证

正文列混合大小写、ASCII tab、实体、混合标签与反引号调用，图片只有弹窗或本地效果。先定位 HTML 文本/属性/脚本/URL 消费者，记录 URL 解码、实体解码和 DOM 重建的顺序；以无害标记与安全文本输出对照确认实际事件/调用。错误的百分号或语法不应机械补成通用载荷，过滤接受字符串也不代表执行；遮挡 origin 的弹窗不能证明所有 WAF 绕过、无交互或远程受害者影响。

来源：[保存帖1](https://x.com/i/status/1605953259528544258)、[保存帖2](https://x.com/i/status/1606714056047734784)、[保存帖3](https://x.com/i/status/1608348795519275008)、[保存帖4](https://x.com/i/status/1606864697634037761)、[保存帖5](https://x.com/i/status/1607354574867763202)、[保存帖6](https://x.com/i/status/1607817415479668737)。

已实际查看保存图片 `1606714056047734784-02.jpg`：TakSec弹窗与遮挡origin，无法绑定正文4类字符串中的哪条/响应上下文。MixedHTML标签/实体tab/javascript/iframe候选必须实际DOM/URL消费者验证，不能通用bypass。。

已实际查看保存图片 `1608348795519275008-02.png`：同样TakSec弹窗另一png字节内容单独查看，仍缺payload绑定/原始返回，不重复推高影响。。

已实际查看保存图片 `1607817415479668737-02.jpg`：地址栏img事件mixedcase+prompt taggedtemplate1337及弹窗，origin遮挡port8000，无远程输入编码/CSP/原始响应；表达式语法与浏览器context不同，反引号调用不适用于任意字符串/过滤，最小无害标记。。


## 聊天脚本与 Cookie 外传描述缩到入口和跨主体证据

正文用脚本发出 document.cookie 声称 ATO，未保存实际响应/执行链。先检查消息存储、清洗、页面 origin、CSP、HttpOnly 和接收身份，在两自有账户用无害标记确认受害者正常读消息时的执行。可读 Cookie 可能非认证秘密，发出请求不等于建立另一主体会话；证明漏洞不需要记录按键或收集真实 Cookie，不保留原帖外传目标为执行配置。

来源：[保存帖1](https://x.com/i/status/1605967912199602186)。


## postMessage 到 autolink 的信任检查与 href 编码分开

截图显示 autolink 用正则匹配文本后拼接 a href，描述消息可达 challenge，完整输入/消息检查未保存。追踪 event.origin、event.source、schema、文本解析、URL 协议与 DOM 插入，可信发送者也不能让文本自动成为 HTML。自有页面用无害分隔标记比较文本输出和属性编码，并核查最终 DOM；正则截断不补造具体 payload，Critical 标题不提供消息可达性或跨用户执行证据。

来源：[保存帖1](https://x.com/i/status/1606270278492987393)。

已实际查看保存图片 `1606270278492987393-02.jpg`：Khan autolink截图字符串拼<a href=...>正则/前缀http规则，将postmessage内容交autoLink后挑战消费；实际event.origin/source/消息schema、转义/URLscheme/DOM插入需要跟踪，regex已截断不补全payload，titleCritical不是独立依据。。


## dataset owner 的两段名字在拼接边界做文本编码

摘要将 first/last name 拼成 owner 字段，某些普通用户仅 self-XSS，enterprise 共享场景可能跨成员。追踪两字段的存储与最终渲染，避免只对各段校验后在拼接处重新形成标签；用自有标记检查完整组合和安全文本节点输出。另一个自有成员实际可见性是升级关键，不能将字段名字或演示脚本推成任意用户可执行/盗算法。

来源：[保存帖1](https://x.com/i/status/1606270611646517248)。

已实际查看保存图片 `1606270611646517248-02.jpg`：Quantopian datasetowner由firstname/lastname拼接未编码，普通self场景与enterprise共享有区别；合成两字段在拼接边界、存储/渲染中编码，确认另一自有成员可见，无实际盗取算法证明。。


## WebSocket 协作输出仍需按浏览器 HTML 边界编码

两摘要涉及调试 watched expression 输出与 TogetherJS 协作消息，前者 Python 输出被作为 HTML，后者 HTTP 层编码/403 与 WebSocket 处理不同。逐跳记录发送身份、资源权限、消息类型、服务端转发和接收端 DOM sink；同一无害标记分别经 HTTP、WebSocket、共享/clone/run 路径对照。固定表达式的输出和协作者数据都不自动可信，安全文本渲染/一致编码才阻断 HTML 消费；渠道过滤差异或奖金额不能代替另一自有主体的执行证据。

来源：[保存帖1](https://x.com/i/status/1606270836121473026)、[保存帖2](https://x.com/i/status/1606270947228618755)。

已实际查看保存图片 `1606270836121473026-02.jpg`：Quantopian watchedexpression输出HTML不编码，可改变Python输出并在分享/clone/run后另主体渲染；WebSocket set_watch/getdatetime请求示例。受信代码输出仍不可信HTML，明确共享/运行前提、消息主体、DOMsink及文本编码。。

已实际查看保存图片 `1606270947228618755-02.jpg`：Quantopian协作者WebSocket直入img事件，HTTP层403而消息内字符被编码/HTML消费差异，摘要称TogetherJS。过滤入口与WebSocket转发/对端DOM输出编码分开；不同通道对照而非继续盲造绕过字符串。。


## blind XSS 回调唯一标记绑定触发入口和观察来源

正文用 contact/name 和第三方平台描述触发，另推荐新平台。先记录入口、存储、预计后台渲染主体与时间，使用自有无敏感标记/受控回调验证，不让第三方脚本采集真实页面或会话。区分自己预览、过滤器探测、浏览器加载和后台用户执行，回调绑定唯一提交、origin、来源与对照；平台名称及 callback fired 都不自动证明跨用户 XSS 或高权限影响。

来源：[保存帖1](https://x.com/i/status/1606852551647055872)、[保存帖2](https://x.com/i/status/1606977548013170688)。


## 产品名输入与下载页渲染分别保存编码证据

一图产品名显示含 %00 的事件字符串，另一保存页面有按钮及确认窗，未给原始头/DOM/另一用户。追踪输入、解码、存储、不同渲染消费者和 HTML 属性边界，比较安全文本节点、事件拒绝与无害标记；记录需要点击/悬停的交互和执行 origin。不能由字符串可见推定已作为标签执行，也不因点击弹窗推定任意 Cloudflare 绕过；避免展示实际 Cookie/XSRF 值作为漏洞证明。

来源：[保存帖1](https://x.com/i/status/1606897672258195456)、[保存帖2](https://x.com/i/status/1607074750848798720)。

已实际查看保存图片 `1606897672258195456-02.jpg`：Productname显示<button/%00onclick=%00confirm(...)>作为可见文字，未见实际DOM/弹窗/持久化另一主体；%00解码/事件值/HTMLsafe text分开，cookie读取不必要，无任意Cloudflare绕过证明。。

已实际查看保存图片 `1606897672258195456-03.png`：保存后Download页显示ClicktoDownloadbutton并有confirm含XSRF-token等cookie值、origin遮挡；与前图输入→后页HTML不同消费者联系，但未给DOM/headers/另一主体；无害marker替代cookie展示，交互要求记录。。


## self-XSS 与登录 CSRF 链中的每个主体变化需独立证据

保存正文声称 self name→login CSRF→stored XSS，图只模板和遮挡来源弹窗。分别证明名称存储、执行消费者、登录切换、后续正常访问与另一自有主体的标记执行；记录所需交互/账户权限，不从已登录攻击者账户的自执行推成任意受害者。确认安全边界无需 keylogging/凭证收集；两条独立候选未被请求/状态证据串起来时保持链为假设。

来源：[保存帖1](https://x.com/i/status/1607797519769292800)。

已实际查看保存图片 `1607797519769292800-02.jpg`：LoginCSRF HTML POST隐字段固定测试账户并自动submit然后立即location/account，弯引号action和导航可能竞态，pushState不变origin；真实cookie/session切换/预会话token/SameSite/Origin，selfXSS共享执行链需自有两会话标记，禁止keylogging/凭证收集。。

已实际查看保存图片 `1607797519769292800-03.jpg`：TakSec弹窗仅效果/origin遮挡，无实际session切换/另用户/存储入口，链不能仅凭示例和弹窗确认。。


## 闭合标签组合依赖实际解析上下文

保存图给大量闭合标签接 SVG 的组合，只适用于具体注入点的解析状态。追踪原始输入经解码/编码后的字节，分别识别普通 HTML、属性、RAWTEXT/RCDATA、注释、脚本字符串及 inert 内容，检查 DOM 实际结构、CSP、浏览器版本与执行 origin。用自有页面和无害标记比较字面显示、仅出现节点与实际执行，不能认为“闭合很多标签”是全上下文通用 payload，弹窗也不直接证明跨账号影响。

来源：[保存帖1](https://x.com/i/status/1608167195162611712)、[保存帖2](https://x.com/i/status/1608316764689158144)。

已实际查看保存图片 `1608167195162611712-02.jpg`：多个闭合标签+SVGonload polyglot示意，不同HTMLrawtext/RCDATA/templateinert/comment/script解析状态不通用；根据真实上下文/浏览器mode/CSP和重解析验证无害marker，不按大串自动bypass。


## 个人简介中的脚本字面显示不能证明执行

保存简介截图显示脚本字符串，却没有执行效果；正文的 ATO 外链未保存。先比较输入、保存后的内容和不同用户/页面的渲染上下文，确认是否安全作为文本显示、被编码或进入可执行 sink。自有两身份只放无害标记并记录 DOM/origin；不要把 script 文本、允许保存或漏洞标题直接升级为 stored XSS、令牌泄露或账号接管。

来源：[保存帖1](https://x.com/i/status/1608490344252850176)。

已实际查看保存图片 `1608490344252850176-02.jpg`：AppleprofileBiography可见<script>alert(1)</script>普通文本，没弹窗或实际HTMLsink，不能按title推访profile即ATO；展示文本/存储/另主体执行和sourceMIME/DOM分别核查。


## URL 参数闭合脚本与 DOM 执行应按具体 sink 对照

保存 tab 参数截图有编码引号/空格和弹窗，JetBlue vsid 历史摘要给闭合脚本的表达式并显示 High 改为 Low；两者均未保存完整 sink。记录 URL 原字节、一次/二次解码、响应与 DOM、具体脚本/字符串上下文、用户动作、浏览器版本和执行 origin，以自有无害标记作正常、被编码和拒绝反例。一个闭合表达式不适用于所有参数，DOM 类型或弹窗也不自动对应高危或账号接管；历史状态只记录当时评估。

来源：[保存帖1](https://x.com/i/status/1608880448972926976)、[保存帖2](https://x.com/i/status/1608884842585792516)、[保存帖3](https://x.com/i/status/1609040282997211137)。

已实际查看保存图片 `1608880448972926976-02.jpg`：tab=starter1编码单引号/空格;alert//浏览器弹窗1；具体JS上下文及来源/版本未知，保留反射编码到执行对照，不推所有tab/ATO，只自有无害标记。

已实际查看保存图片 `1608884842585792516-02.jpg`：JetBlue vsid DOMXSS H1摘要含引号/括号闭合alert并High→Low3.1状态，无实际DOMsink/用户动作；类型不定高危，记录源到sink/browser origin权限另验。


## 嵌入外部文档不自动执行于父页面

保存 embed src 提问、可信 iframe 域内重定向的建议与密码对话框图片，未给完整浏览器链。区分顶层、iframe、embed/object 与 img 的解析行为、最终 origin、sandbox、CSP/frame 限制、MIME 和用户动作；每个跳转单独核对加载者的安全策略。外部文档执行自身脚本、导航或显示弹窗不等于父域 XSS。仅在自有父/子文档用无害标记和最终 origin 对照，不复制密码输入或采集凭据。

来源：[保存帖1](https://x.com/i/status/1608886499436818432)、[保存帖2](https://x.com/i/status/1609239824082571266)。


## CSP 评估器只产生策略候选

保存示例策略 script-src self 与某允许域、img-src 通配，评估器提示 host 白名单、缺失 object-src 和 Trusted Types；没有具体注入 sink 或实测绕过。审阅实际生效的响应头、meta、多策略交集、页面加载路径和浏览器版本，用自有无害脚本确认被允许/被阻止情况。静态评级不证明可执行漏洞，历史插件提示不能推今天浏览器行为，Trusted Types 建议也不补齐现有 sink 可控性；策略改进仍须与业务允许的脚本来源及回归相配合。

来源：[保存帖1](https://x.com/i/status/1609088146398150657)。

已实际查看保存图片 `1609088146398150657-02.jpg`：CSP评估器示例self+allowed.com/img*提示host白名单、缺object-src、TrustedTypes；仅静态示例无注入sink/实际绕过，保留实际生效HTTP/meta多策略、浏览器版本及加载路径验证，不把旧插件提示或评估器评级当现今必然可执行。


## 盲回调需绑定具体输入实例而非通知数量

保存 Blind XSS manager 有域、URL、hash 和多种上下文候选；另一截图只是 XSSHunter 邮件通知列表。给字段×插入实例×身份×时间分配独立标记，保存原始输入、实际回调 origin、浏览器/消费者与受控执行证据，排除安全扫描器、缓存重放及工具自身访问。URL hash、email 计数和候选 payload 数量都不等于漏洞数；只发最小无害回调，不默认采集 cookies、页面内容或键盘输入，不执行保存的远程 JS。

来源：[保存帖1](https://x.com/i/status/1609527811244687363)、[保存帖2](https://x.com/i/status/1609993670945820672)。

已实际查看保存图片 `1609527811244687363-02.png`：BlindXSSmanager UI Domain/URL/hash与script/JSURI/input/img/video/iframe/XMLHTTP/jquery候选；以字段×插入实例非仅URLhash绑定回调，工具回调不代表目标浏览器执行，默认不收cookie/页面数据，不执行保存payload。


## 搜索历史的保存与再渲染是独立边界

保存帖建议搜索项后来显示在历史中时检查 HTML、重定向和所谓 DDOS。追踪自有输入经保存、编码及不同身份的历史列表/其他消费者再渲染，比较字面文本、节点、导航和实际无害脚本执行；存储不等于执行，导航也不等于父域权限。只有受限消费者的可控 sink 和必要触发条件成立才报告相应原语，避免扩大到其他用户历史或进行资源耗尽测试。

来源：[保存帖1](https://x.com/i/status/1610677826168000515)。


## 清洗器允许标签组合与不完整修复要分别回归

保存 Rails Html Sanitizer 两摘要分别涉及 select+style、不完整修复，以及 math+style 或 svg+style，历史文字同时写 ALL 与 fixed 1.4.4。将组件精确版本、调用上下文、全局配置与单调用 allowlist 覆盖作为必要前提，不能据 ALL 推全部当前 Rails；图片只完整显示首种配置，其余路径不能补造。用自有无害片段检查命名空间、RAWTEXT 与清洗后再解析的树，分别覆盖三组标签、默认配置及禁止组合的反例。修复编号与版本声称不能代替实际树转换和执行上下文回归。

来源：[保存帖1](https://x.com/i/status/1610841740033900549)、[保存帖2](https://x.com/i/status/1610841845637971969)。

已实际查看保存图片 `1610841740033900549-02.jpg`：Rails23520不完整修复23209，配置允许select+style才影响，截图1.4.4fix历史声明并有全版本ALL张力；D记录确切sanitize版本+全局和单调用覆盖两途径、tokenizer树转换+用户context，只对保存版本/组合做无害本地负例，不推所有Rails当前受影响。

已实际查看保存图片 `1610841845637971969-02.jpg`：Rails23519允许math+style或svg+style且全局/调用等四覆盖路径，图只展示第一全局配置其余不保存；D与23520select组合分别反例，历史1.4.4不能当当前所有Rails受影响，树命名空间/rawtext转换与二次parse上下文。


## 资料字段的视觉覆盖与脚本模板要分开判断

保存 firstname/surname/info 的 style 固定覆盖和 mouseover 事件，以及 constructor 模板表达式。先确认每字段的存储/拼接、属性引用与编码，记录事件是否可触发、需要哪些用户动作、CSP 和另一自有消费者；视觉遮挡不是脚本执行。模板表达式须确定实际引擎和可调用能力，不能从框架样式的字符串推通用执行；本地无害标记比较字面显示、DOM 节点和事件结果，不复制覆盖真实界面或收集凭据。

来源：[保存帖1](https://x.com/i/status/1611459581275963393)。


## 百分号和空白字符必须追踪到最终脚本上下文

保存 RXSS 片段含百分号编码、实体、大小写变化、iframe/javascript 与 SVG，以及 script 名称中的 tab/newline；WebPuff URL 摘要还有多层编码和新 IP。记录原字节、各次解码/实体转换、反射位置、最终 DOM/脚本上下文、CSP 与执行 origin，用自有无害标记和安全字面反例。参数名 note/tracking_info、工具命中和技巧题名不保证注入成立；不复制保存 URL 中凭据或读 Cookie，也不能从 IP/TLS 指纹自行推授权范围。

来源：[保存帖1](https://x.com/i/status/1611546161722040324)、[保存帖2](https://x.com/i/status/1611675239611514881)、[保存帖3](https://x.com/i/status/1612621438506213376)。

已实际查看保存图片 `1611675239611514881-02.jpg`：WebPuff5.4/Login URL参数带百分号/多层编码script候选，IP/sslhostname摘要；Dxss当前scopehost/URLdecode/反射实际sink/自有标记执行与safeencoded对照，不复制GET凭据、不推未见cookie/软件安装影响。


## 禁用控件不代表所有事件上下文不可到达

保存 disabled input 上的 beforecopy/beforecut 示例声称在 Chrome 可用，没有保存版本或触发录像。把控件 UI 禁用、DOM 属性可控、事件派发和脚本执行分开，记录浏览器版本、交互方式、CSP 及源到事件属性的编码。用自有离线控件和无害标记比较正常、disabled、事件拒绝与字面文本；事件名字和 disabled 属性均不能独立保证执行或安全，也不把旧技巧作为当前所有浏览器行为。

来源：[保存帖1](https://x.com/i/status/1611790572959956992)。


## 多次反射的组合解析应覆盖跨片段状态

保存图分别给单输入反射两次的 script/comment 跨越，以及两输入在 HTML 属性引号中拼成事件的示意。逐 occurrence 记录解码/编码、上下文、中间可信文本和页面最终连接顺序，检查 HTML tokenizer/脚本注释实际解析树与 CSP，而非只测每个字段单独插入。自有离线片段用无害标记比较单字段拒绝、联合字面显示和确实执行；组合安全性可能不同，但示意不是全页面通用 polyglot 或无需用户动作的影响证明。

来源：[保存帖1](https://x.com/i/status/1612869267510427649)。

已实际查看保存图片 `1612869267510427649-02.jpg`：多次反射完整示意：单input两反射脚本comment跨越闭合，双inputHTML属性引号拼接SVG，Dxss同时各occurrence的decode/encode/上下文/中间可信代码/combinedparse-tree/CSP，单字段安全不必组合安全，有限本地无害标记不通用polyglot。


## BlindF 奖励帖只支持盲执行候选而非必须提取 Cookie

保存帖声称仅 cookie extractor 成功但没有载荷或消费端截图。盲 XSS 应先用唯一无敏感标记关联输入、异步渲染和实际浏览器执行，再记录来源、权限及延迟；DNS/HTTP 探测与脚本执行分开。最小确认不需要上传真实 Cookie，HttpOnly、CSP 和第三方预览/扫描回调是反例。奖金或工具名不补足机制。

来源：[保存帖1](https://x.com/i/status/1613374057860435969)。


## SVG 事件读取 URL fragment 后 eval 的客户端执行链

保存示例为 SVG onload 调用 eval(location.hash.slice(1))，fragment 再创建外部 script。fragment 通常不随HTTP请求发送，审计链为事件属性→hash字符串→eval→脚本加载；外部脚本仍在页面环境执行。先定位模板上下文、编码次数和 CSP，使用自有离线标记对照正常片段、纯文本片段和被阻断事件；确认实际执行及加载条件。hash存在或脚本URL回显不足以确认，也不能推出所有WAF失效；无需下载或执行帖中外部代码。

来源：[保存帖1](https://x.com/i/status/1613592785009152000)。


## 名字分别过滤后拼接成 HTML 属性必须按最终上下文处理

保存两字段示例拼成IMG和onmouseover，后图有xxs弹窗但目标域遮挡。审计字段保存、拼接顺序、模板引号和最终HTML，分别比较单字段、组合字段及最终上下文编码，在自有页面仅显示固定标记并记录触发事件。字段单独无完整危险词不保证拼接安全，弹窗图也不证明所有页面或他人权限下可执行；应按最终消费者上下文编码而非只做词匹配。

来源：[保存帖1](https://x.com/i/status/1614031037062909952)。

已实际查看保存图片 `1614031037062909952-02.png`：FirstName与LastName拼成IMG SRC及onmouseover表达式，分别过滤后拼接可改变HTML解析；图未见执行证据。

已实际查看保存图片 `1614031037062909952-03.png`：两字段示例后alert xxs弹窗，域名遮挡；需要具体拼接模板和浏览器事件路径。


## Markdown 输出保留 IMG 却删除 onerror 是当前反例

保存git mode请求包含img onerror，返回HTML保留img src和样式却没有事件属性。先看解析器版本、rawHTML策略、链接协议白名单及最终DOM；用无害文本与自有图片比较source、渲染和sanitize时序。该图不能声称XSS已执行，图片存在不等于脚本运行。只有实际危险上下文经过净化并在自有浏览器执行才确认；不要凭求助帖补造绕过载荷。

来源：[保存帖1](https://x.com/i/status/1614315540738363392)。

已实际查看保存图片 `1614315540738363392-02.jpg`：Markdown请求git mode含img onerror，输出删除事件属性但保留img src，当前图不支持XSS执行。


## 邀请邮件自定义 message 的 HTML 注入与 ATO 应分开

Mattermost图给guest邀请自定义message插入a/input并在邮件呈现，另一帖只有email-template外链题名。审计模板变量最终HTML/属性/URL上下文及邮件客户端净化，使用两个自有邮箱和固定无敏感标记比较文本编码与真实DOM。可插入链接/输入框只证明HTML内容控制，不能直接认定脚本执行或账户接管；不搭建登录仿冒页面、收集凭据或给其他人发邮件。

来源：[保存帖1](https://x.com/i/status/1615606589498466304)、[保存帖2](https://x.com/i/status/1614327909828673536)。

已实际查看保存图片 `1615606589498466304-02.jpg`：Mattermost邀请guest自定义message渲染a/input HTML到邮件，证明标记注入非脚本/直接ATO；仅自有邮箱无钓鱼。


## Swagger 外部 configUrl 与旧版 HTML 呈现需要 sink 证据

保存JourneyAPI图主要timeline，InDesign标题含configUrl={site}，未见完整配置及执行。先确认实际Swagger UI版本、URL参数开关、配置/规范来源、description等字段以及sanitize→DOM链。自有静态spec用普通文本/无害标记对照可信与不可信配置，观察外部请求、最终DOM和CSP；加载spec、旧版本或HTML显示都不自动证明DOM XSS。历史报告已解决不代表当前页面仍受影响，也不能补造外链载荷。

来源：[保存帖1](https://x.com/i/status/1615606694536519681)、[保存帖2](https://x.com/i/status/1615606798194561024)。

已实际查看保存图片 `1615606694536519681-02.jpg`：JourneyAPI旧Swagger HTML注入标题和timeline，无sink流程。

已实际查看保存图片 `1615606798194561024-02.jpg`：InDesign Swagger configUrl外部配置DOM XSS报告标题，无恶意spec与执行证据，外部配置入口可审计。


## XSSHunter Discord 通知需要绑定输入和实际执行来源

图为W3Schools tryit的payload fired通知，不能作为真实目标漏洞；Discord只为通知渠道。每输入用独立标记/时间和源页面、执行origin、最小权限信息绑定，区分人工演示、扫描预览、重复回调和目标消费者。先在自有隔离页面比较脚本执行与仅资源加载，通知不等于Cookie窃取。停服/selfhost公告属于历史，未保存配置全文按用户覆盖；不安装、发送通知给他人或上传真实会话。

来源：[保存帖1](https://x.com/i/status/1615979039054766080)、[保存帖2](https://x.com/i/status/1616118810565824512)、[保存帖3](https://x.com/i/status/1614301261343625216)。

已实际查看保存图片 `1615979039054766080-02.jpg`：XSSHunter Discord fired通知W3Schools tryit本地演示，通知是观察渠道非目标漏洞与来源保证。


## 任意搜索参数生成 hidden input 时 name 与 value 都是不可信

图描述主搜索附加任意参数后生成hidden input的name/value，未见完整后续执行片段。追踪query解析、重复键、解码次数、属性引号和DOM生成API；两者均需对应上下文安全写入。自有静态页面比较普通参数、特殊字符文本及拒绝/编码结果，只用固定执行标记确认XSS。hidden不可见不提供安全性，HTML注入不等于可读HttpOnly Cookie或ATO；不复用真实会话。

来源：[保存帖1](https://x.com/i/status/1616201977259606017)。

已实际查看保存图片 `1616201977259606017-02.jpg`：主搜索额外query参数生成hidden input name/value，属性上下文逃逸XSS；截图部分无完整payload，可审计动态任意参数渲染。


## 登录参数的反射需要定位实际语法上下文

图片中的 admin 登录 perspective 参数与正文中的 GlobalProtect user 参数都提供了候选入口；保存材料未建立通用的执行结论。记录正常值、无效标记以及响应中标记所在的 HTML、属性或 JavaScript 位置，再在授权测试账户中用无数据读取的标记确认浏览器是否执行。编码、模板和 CSP 都属于前提；产品名、历史载荷和一个 alert 不能证明其他版本或其他上下文同样可用。

来源：[保存帖1](https://x.com/i/status/1616461652626489344)、[保存帖2](https://x.com/i/status/1616863161101189121)。

已实际查看保存图片 `1616461652626489344-02.jpg`：admin login perspective参数onload及alert图，需具体反射HTML上下文和正常/无效基线。


## 多次解码的 DOM 字符数据与再次解析边界

正文声称 %26lt; 先变成 &lt; 再成为 <。必须区分 URL 解码、HTML 实体解析、净化以及 DOM sink 的顺序：实体产生的字符不必然再次成为可执行标签。以无害标记记录各阶段值，检查是否经 innerHTML 等方式重新解析，并分别比较纯文本 sink 与 HTML sink。保存奖励截图不含执行链，不能据此认定所有 DOM sanitizer 可绕过或把编码本身等同 XSS。

来源：[保存帖1](https://x.com/i/status/1616489318520066049)。


## HTML 内容控制与脚本执行及钓鱼影响分层

保存图描绘 HTML 注入后的伪登录表单，只说明内容控制的一种可能影响。先以无害文本或布局标记确定输入进入 HTML 文档、属性还是纯文本，检查净化、输出编码及来源展示；HTML 被解析、JavaScript 执行和凭据诱骗是独立结论。保存材料没有真实跨用户执行或凭据证据，不制作收集凭据页面，也不把 HTML 注入直接写成 XSS/ATO。

来源：[保存帖1](https://x.com/i/status/1617418471134093312)。

已实际查看保存图片 `1617418471134093312-03.jpg`：HTMLinj伪登录收凭据概念图，仅审计内容控制及impact边界不生成钓鱼流程。


## 客服盲 XSS 从采样标记到真实 sink 与披露权限

正文建议在联系表单/客服中到处投送，截图的奖金邮件却明确限制公开漏洞细节。先在允许范围内为单个输入建立唯一无数据读取标记，记录提交者、处理角色和异步回调，再区分内容预览、浏览器执行及真正跨用户影响。回调、奖金与已分享金额都不授予无限测试或公开权限；不得据建议改所有请求或采集客服页面数据，保存未确认 sink 的限制。

来源：[保存帖1](https://x.com/i/status/1617504905278943233)。

已实际查看保存图片 `1617504905278943233-02.jpg`：客服盲XSS500+50奖励邮件明确仅奖金可分享漏洞细节需programpermission；影响与披露分离。


## 反馈链接的 scheme、导航与 opener 分别检查

Slack 图展示反馈 POST、crumb 与 path 字段的 javascript/外部链接候选，window.opener 后续代码未完整保存。先追踪服务端如何保存和输出链接，再检查允许 scheme、浏览器实际导航、同源关系及 opener 的存在/隔离。用自有无害链接比较正常与非法 scheme，不把链接回显、HTML 属性变化或打开新窗直接当作执行或账户接管。跨窗状态改变需要独立终态证据，未保存部分按证据不足保留。

来源：[保存帖1](https://x.com/i/status/1617546943386845187)。

已实际查看保存图片 `1617546943386845187-02.jpg`：Slack feedback submit POST form crumb1/path javascript或外部opener链接；真实导航、scheme allowlist及noopener需区分，未见下半窗口代码。


## Theia WebView 的 postMessage 接收链保留截断限制

保存 Theia/CVE-2021-41038 图包含启用 WebView 的条件、window.open/postMessage、channel/content/args/options，但未保存完整 sink 与校验。审计发送者、接收窗口、origin/source、消息结构及参数到 DOM 的实际链路；用自有测试窗口的无害消息分别确认允许与拒绝。事件收到、对象字段可控与脚本执行是不同阶段，历史 CVE 名称不证明当前 notebook 存在同样问题。

来源：[保存帖1](https://x.com/i/status/1617892603143376896)。

已实际查看保存图片 `1617892603143376896-02.png`：Theia WebView enabled/CVE-2021-41038截断window.open/postMessage channel content argsoptions，未见完整sink及origin校验，receiverchain为关键。


## XSS 变体清单以语法上下文和编码阶段拆分

保存 26 条清单混合 onclick、SVG、onerror、百分号/实体/TAB、javascript、iframe srcdoc、多反射和模板表达式。先将候选对应 HTML 文本、属性、URL、DOM 解码或模板消费者，再比较编码、净化与 CSP；用无害标记记录输出及浏览器结果。“working” 注释和 Cloudflare/WAF 标题没有当前版本证据，多层编码也不自动形成执行，不保存或执行窃取 cookie 的行为。

来源：[保存帖1](https://x.com/i/status/1618005491124404224)。

已实际查看保存图片 `1618005491124404224-02.png`：26条XSS onclick/SVG/onerror/percent/entity/tab/javascript/iframe srcdoc/多反射/模板表达式，working注释无当前WAF证明；按HTML属性/URL/DOMdecoder/CSP分context，不保留窃cookie流程。


## 盲 XSS 扩展的改头范围与变换来源显式记录

图中扩展为 OFF，可添加不存在的头，并对 User-Agent、Referer、XFF、Origin 做编码和随机化。先限定自有允许流量，为每个改动保存原值、变换、请求标识与唯一回调标记，确定哪一消费者读取该头。改头、回调和跨角色执行分别核验，随机化会削弱复现性，URL 编码需对应解码 sink；不能由功能列表推断执行结果或将其自动应用到所有请求。

来源：[保存帖1](https://x.com/i/status/1618707107590856705)。

已实际查看保存图片 `1618707107590856705-02.jpg`：BXSS扩展OFF、添加不存在头、URLencode/randomize/UserAgent/Referer/XFF/Origin；scope限定记录变更和callback消费者，不自动所有请求改头。


## 搜索执行叙述与异源 cookie 影响分别核验

保存报告写搜索栏插入 script 后弹窗，并声称可借其他站点 CORS 获取 cookie/token。必须先证明外部可控输入在目标浏览器进入实际 sink，再将同源可访问数据、HttpOnly 限制与 CORS 允许读取的响应分别判断。CORS 不会直接赋予读取异源 cookie 的能力；用自有无害标记和私密测试响应做正反对照，不复制会话或读取真实 token。文字步骤与影响描述没有保存完整响应/跨站交换。

来源：[保存帖1](https://x.com/i/status/1619327066666635269)。

已实际查看保存图片 `1619327066666635269-02.jpg`：反射XSS搜索栏script+cookiealert文字步骤，目标遮挡；impact称利用别站CORS读cookies/tokens不严谨，JS不能直接读异源cookie/HttpOnly，要实际同源sink/CORS可读私密response/独立证据，不执行或窃取。


## prefixRank 属性事件候选需实际 DOM 和交互条件

图有表单 POST customer.cfm、prefixRank 参数及 accesskey/onclick 片段，包含被遮挡目标及会话。先记录 form 解码、参数消费、输出属性引号边界和浏览器实际 DOM，再在自有页面用无害标记确认事件是否可触达。accesskey 类事件可能需要用户交互，HTTP 反射不是执行。保存图没有响应或最终 DOM，不复用 cookie，也不据 payload 字样推断当前版本可复现。

来源：[保存帖1](https://x.com/i/status/1619327167170596865)。

已实际查看保存图片 `1619327167170596865-02.jpg`：prefixRank参数accesskey/onclick片段，POSTcustomer.cfm CFcookie/ContentType form，缺保存response/DOM；accesskey需交互，语法上下文和可达事件独立验证不复用cookie。


## xAPI 的 file 查询与浏览器可发请求条件分开

报告标题写 URL path，但保存 URL 为 statements?file=…，并要求添加 Basic Authorization 和 X-Experience-Api-Version:1.0.1。先固定实际参数位置、权限主体和服务器返回的 HTML 上下文，再检查普通浏览器链接能否产生同样请求。代理加头重放与受害者导航不是等价条件；使用自有账户和无害标记读取响应/DOM。图未展示响应，cookie 窃取或 ATO 也没有独立链，不复制保存授权头。

来源：[保存帖1](https://x.com/i/status/1619327275572334593)。

已实际查看保存图片 `1619327275572334593-02.jpg`：报告标题URLpath但URL实际/xapi/statements?file=...，需BasicAuth和X-Experience-Api-Version:1.0.1，未保存response；加头proxy重放不等于被害浏览器可由普通链接触发，cookie/ATO无独立链。


## Ads 输出编码根因与 WAF 或接管声称分层

TikTok Ads 保存摘要明确为用户输入反射缺少适当 HTML escaping/output encoding，称 2022-09-07 已修复；另一叙述称 Akamai 绕过与任何账户接管。先以自有标记确定语法上下文和最终浏览器行为，再检查编码修复是否覆盖原 sink；WAF 字样不建立解析差异，XSS 也不自动证明接管。图没有载荷或后续账户能力，保留历史条件与未证影响，不复制 token 或会话。

来源：[保存帖1](https://x.com/i/status/1619327485652475905)、[保存帖2](https://x.com/i/status/1619745580120702976)。

已实际查看保存图片 `1619327485652475905-02.jpg`：TikTokAds摘要明确缺HTMLescaping/outputencoding并历史已修2022-09-07，另作者称akamai bypass/ATO但无载荷或接管链。


## 被过滤函数名与实际执行 sink 不可混同

正文建议 alert 被拦后用 confirm/prompt/eval/write。函数名只是语法构件，eval、document.write 等具有不同消费者与副作用，替换名称不保证通过过滤、上下文或 CSP。用无数据读取的自有标记先确认输入进入可执行位置，再验证输出编码和浏览器行为；字符级过滤并不是安全证明，图片缺失也不补造实际执行结果，不把备选函数当通用绕过。

来源：[保存帖1](https://x.com/i/status/1619410705282928640)。


## Loofah SVG data MIME 案例保留版本和配置条件

保存摘要列 Loofah >=2.1.0 且 <2.19.1、CVE-2022-23515，并称升级 >=2.19.1；特定配置可经 SVG use 绕过 HTML sanitize。分别核对实际版本、允许 MIME/scheme、命名空间、净化结果和浏览器加载文档的上下文。用自有无害 SVG 标记比较原/修复配置，不能因 image/svg+xml 名称推断不可执行或直接判全部 SVG 均执行。底部 payload/DOM 未完整保存，历史摘要不证明当前 Rails 可复现。

来源：[保存帖1](https://x.com/i/status/1619682905034297344)。

已实际查看保存图片 `1619682905034297344-02.jpg`：Loofah>=2.1.0 <2.19.1 image/svg+xml dataURL摘要、升级>=2.19.1/CVE2022-23515；特定配置SVG use可绕sanitize，底部裁切无payload/DOM；历史版本仅保存声称，mime/namespace/rendering。


## Xssor 的反射检查与浏览器执行分别确认

正文说明 Go 版 Xssor 检查载荷在源码的反射，并强调速度与重复 URL 跳过；后帖只是发布 writeup。保留完整 URL、参数、登录态、响应和重复判据，区分文本命中、真实 HTML/DOM 语法位置与浏览器执行。速度不等于覆盖，按 URL 去重可能遗漏不同状态/请求体/身份；用无害自有标记建立允许/拒绝对照，不将反射工具命中直接写成 XSS 或补造未保存实现。

来源：[保存帖1](https://x.com/i/status/1619745874741170177)、[保存帖2](https://x.com/i/status/1621157834129047554)。


## 弹窗和 javascript 书签排除本地主动执行反例

一图只有页面 alert1，另一回复解释地址栏/书签执行 javascript 与 void(0)。外部可控输入经站点 sink 执行、用户主动在自己的页面运行书签、调试控制台或改本地响应是不同路径。以自有无害输入记录原请求、输出/DOM、来源与交互，建立真实跨用户触发条件。图没保存入口和执行链，0day/感染/偷 cookie 的标签不能补证，不执行归档书签或采集会话。

来源：[保存帖1](https://x.com/i/status/1620430979763671040)、[保存帖2](https://x.com/i/status/1620436169204072449)。

已实际查看保存图片 `1620436169204072449-02.png`：回复解释javascript书签/手输地址在自己页面执行、void0等，不是真网站XSS；用户主动本地执行 vs外部可控输入到sink，0dayATO标签不成立。


## 多步表单的状态与反射请求逐步绑定

正文建议从真实表单流程开启 Intercept，到出现反射的请求再修改，图只见代理输入片段。记录自有账户的每步状态、token、对象和请求前提，比较合法流程与孤立 Repeater 重放的差异；必须在实际响应/DOM 中定位最终 sink。拦截改请求不是执行证明，前步接受也不确认后续权限，使用无数据读取标记并限制操作预算，不以盲重放绕开业务状态。

来源：[保存帖1](https://x.com/i/status/1620478876655968259)。

已实际查看保存图片 `1620478876655968259-02.jpg`：BurpInterceptON127.0.0.1:443 H2及imgonerror输入片段，无response/DOM，multistep token/状态推进真实表单与Repeater差异，拦截改请求不是执行证明。


## SVG 从 data 到 blob 的 origin 与打开方式分离

Shopify 摘要称富文本 data SVG 被转成 blob，修复避免该转换；报告明确普通 img 不运行其中脚本，而打开图片后会执行。分别记录 MIME、净化、URL 转换的创建来源、origin 与 img/文档导航模式，以自有无害 SVG 比较显示和打开两条路径。不能把 Base64 当加密或认定所有 SVG/img 都执行；保存图未展示完整脚本与浏览器结果，历史说明不代表当前产品，权限影响需独立确认。

来源：[保存帖1](https://x.com/i/status/1620521781965557760)。

已实际查看保存图片 `1620521781965557760-02.jpg`：Shopifyrichtextdata:image/svg+xml img脚本不执行，openimage后执行叙述；summaryfix避免data→blob，转换改变origin/文档上下文，不能断所有SVGimg运行，base64code右裁缺全链/actualrequest。


## 公开资料 data HTML 链接的执行与站点权限分层

图在产品描述放 data:text/html;charset=utf-7;base64 链接，称点击后运行；Base64 是编码，声明 charset 不保证浏览器采用它。先核验实际导航 scheme、解码、浏览器版本、origin 和 CSP，再在自有无害页面区分新文档执行与原站私密资源访问。data 文档的执行不自动取得站点会话，视频与实际交换未保存，不把“encrypted”或 XSS 名称当跨站能力证明。

来源：[保存帖1](https://x.com/i/status/1620627772983988224)。

已实际查看保存图片 `1620627772983988224-02.jpg`：Publicprofiledescription data:text/html;charset=utf7;base64链接点击声称XSS，base64是编码不是加密，dataopaqueorigin不能直接站点session，charset解释/浏览器导航/sameorigin/CSP，video未保存。


## 邮件预览的嵌入策略与 self-XSS 跨用户条件分离

图描述 image URL 引号/事件产生 self-XSS，应用的 CSP/X-Frame-Options 策略限制外部嵌入，另称 full mail preview 可加载 iframe；后半受害者链未保存。逐项核对外部输入、接收者身份、预览 origin、frame-ancestors/XFO 与实际文档边界，以自有无害视图比较允许和拒绝。self-XSS 不会仅因可放 iframe 就升级，预览是否漏掉相同约束需独立终态，不制作诱骗页面或补造点击链。

来源：[保存帖1](https://x.com/i/status/1620642986492137473)。

已实际查看保存图片 `1620642986492137473-02.jpg`：imageURL quoteonload selfXSS，CSP*.myshopify.com vsXFO SAMEORIGIN、fullmailpreview允许iframes叙述，后半victimchain没保存；self/proxy执行不跨用户，frameancestors/preview trust/dataflow独立，不生成clickjacking。


## 允许富文本与持久 HTML 控制先说明受信任边界

Judge.me 图给 public profile recommendations 描述可存 HTML，作者明确无法执行 JavaScript，报告 Informative。先明确产品允许的富文本、输出位置、查看者及来源展示，再用无害布局/文本标记确认持久化和跨用户影响。HTML 解析与脚本执行或凭据诱骗分别记证据，类别里的 Basic XSS 字样不会改变实际执行能力；预期富文本是反例，不制作钓鱼表单或由状态反推全部 HTML 注入无效。

来源：[保存帖1](https://x.com/i/status/1620643089667735552)。

已实际查看保存图片 `1620643089667735552-02.jpg`：存储HTMLprofile推荐description步骤，作者明确无法执行JS，Informative；HTML解析/允许richtext/跨用户信任以及XSS独立，不以类别BasicXSS自动升级，不生成phishing表单。


## Forwarded Host 反射须跨越可信代理和 HTML 编码两边界

正文在 X-Forwarded-Host 放引号及事件示意。先确认头是否来自允许的可信代理、哪一消费者用它构造站点/URL/页面，再定位实际输出语法和浏览器 sink。用自有域名和无数据读取标记比较未信任头拒绝、正常站点和正确编码；修改 Host 文本或网关回显不是执行证据，保存材料未给响应，不读取 cookie 或将头注入等同接管。

来源：[保存帖1](https://x.com/i/status/1621075613456166912)。


## 盲 XSS 面板应保留事件来源并拆开附加扫描结论

XSS Hunter 保存面板显示 AWS 标识、CORS `*`、Git 配置片段、Browser Time 和 iframe=false；这些属于一个采集事件的多个线索。用自有唯一标记记录写入入口、执行页面主体/来源、回调时间、实际浏览器执行与报告关联，分别验证秘密格式及权限、跨源读取私密响应、Git 实际对象内容。重复 AWS 标识并非完整凭据，CORS 星号并非带凭据读取成立，配置片段中的脚本文本并非全部源码或额外执行证明。托管重启报道不替代事件证据。

来源：[保存帖1](https://x.com/i/status/1621226641480368135)、[保存帖2](https://x.com/i/status/1621539033259347968)。

现有图片证据 `1621226641480368135-02.jpg`：XSSHunter面板Secrets AWS标识重复、CORS*、git配置片段含scriptprompt、时间iframefalse；没有凭据权限/浏览器私密响应/完整Git源码证明。


## 旧 Swagger UI 的 configUrl 消费者需与普通链接导航区分

Jamf Pro 历史截图指出 classicapi/doc 的旧 Swagger UI 可消费 configUrl=data:text/html;base64 并声称出现 alert 或钓鱼页，摘要称 2022 已移除入口。核验链应记录实际 UI 版本、配置 URL 被怎样获取解析、进入 DOM/脚本的消费者、执行文档来源及用户操作；用自有标记、普通配置和拒绝来源对照。钓鱼页面、脚本执行和会话接管各需独立证据；截图未保存完整版本、会话授权链或后续请求，不能推定所有 Swagger UI、当前站点或 data 文档具有目标权限。

来源：[保存帖1](https://x.com/i/status/1621262748914012160)。

现有图片证据 `1621262748914012160-02.jpg`：JamfPro历史SwaggerUI classicapi/doc configUrl=data:text/html;base64及alert/钓鱼步骤裁切；摘要2022移除端点、Resolved Medium6.7 9400，无具体完整版本/会话接管证明。


## 路径反射命中须核最终来源和真实浏览器上下文

图片脚本对路径后缀和假查询参数 curl -L 并 grep xss，示例目标与第二个 PoC 域名还不一致。逐项固定入口、参数、原始编码、每次跳转目的地和最后响应来源，记录文本进入 HTML/属性/JS/URL 的具体上下文；以自有无害标记比是否编码、是否二次解析和浏览器实际执行。终端 grep 和带 xss 的 PoC 字符串仅是反射候选，不证明执行或受害者路径；示例/跳转到不同域名属于来源污染，不能归到原目标。

来源：[保存帖1](https://x.com/i/status/1621868441891377152)。

现有图片证据 `1621868441891377152-02.jpg`：path/query假参curl-L grep xss字符命中仅反射；输出Target test.com.br而POC2brutelogic域不同需来源审计。


## XSS 影响需由真实执行身份和可访问能力限定

保存正文给可窃敏感信息/代操作的概念，图只 Day22 标题。从可控输入到实际 HTML/JS 消费者、受害页面操作、执行文档来源及会话权限逐段记录，用自有非敏感标记与正常编码对照确认。脚本执行后能否读数据或改业务仍受文档来源、会话和应用授权约束，凭据泄露/ATO 不能仅由弹窗或标题推定；不存在执行、只显示文本和自写脚本是反例。未保存的类型/续篇按用户覆盖，不补成实际样本。

来源：[保存帖1](https://x.com/i/status/1622902443838418945)。


## FiveM NUI 弹窗截图：执行上下文和持久化证据分开

现有图片显示 nui://easy-chat 中两个 alert 场景及 XSS Hunter 通知计数，正文称 stored XSS。能提炼的是先确认输入进入哪个聊天字段、是否被存储、在哪个 NUI 文档中重新呈现，以及该文档可访问何种游戏或本地桥接能力。用自有用户的无害标记保存后重新打开页面，并以另一授权用户阅读作对照，记录 HTML/脚本 sink 和存储记录。弹窗只证明相应页面执行了脚本；不单独证明跨用户存储、宿主权限、OS 命令执行或所有通知都是独立漏洞。存档缺少输入到 sink 的完整链。

来源：[保存帖1](https://x.com/i/status/1623471628758790144)。

现有图片证据 `1623471628758790144-02.jpg`：FiveMnui://easy-chatJSalert场景1，无输入源/存储/权限/受害步骤。

现有图片证据 `1623471628758790144-03.jpg`：FiveMnui://easy-chatalert场景2同样缺链，只游戏画面和对话。


## HTML 到 URL 到 JavaScript：绕过载荷依赖分层解析位置

anchor 示例图标注空白、实体和 scheme 等六处变异，另帖给出注释、onmouseover、SVG 与编码混合的 polyglot 文本。先保存原始字节及实际 DOM，确定输入进入 HTML 属性/文本、URL、事件属性还是脚本，再按实际解析顺序查明哪个变异穿过哪个过滤器。使用无害上下文标记和普通拒绝输入对照，确认真正执行时的 origin 与用户交互条件。HTML 实体、百分号或控制字符并非每一层都解码，polyglot 也不能保证所有上下文/WAF 有效。图右下被裁剪，未保存部分不补造。

来源：[保存帖1](https://x.com/i/status/1624821563555213313)、[保存帖2](https://x.com/i/status/1625578121562042370)。

现有图片证据 `1624821563555213313-02.jpg`：atag6mutationpositions byte09/0a/0d/0c20/2f、HTMLreferences、URLencoding/unicode whitespace图底右裁切；HTML tokenizer→URLparser→JS3consumers different notallencodingvalid。


## Triage Wizard HTML 测试：扩展特权和网页 origin 区分

正文/图建议开启 HackerOne Triage Wizard Chrome extension，进入指定 security/bugs 查询的报告页后点 View Triage Questionnaire Beta，声称注入 HTML 可能 XSS。定位用户内容到扩展或网页的实际 HTML sink，并确认脚本在哪个 origin/isolated world 执行、由谁触发、具备何种权限；无害标记、纯文本对照和重新加载后结果应对应同一流程。HTML 插入、扩展启用或视频缩略图不能证明脚本执行及平台其他用户受影响。存档没有完整运行视频和 sink，保留为历史候选。

来源：[保存帖1](https://x.com/i/status/1625600538627678220)。

现有图片证据 `1625600538627678220-02.jpg`：H1TriageWizardChromeExtension开启→URLreportsubjectsecuritybugs1→右键ViewTriageQuestionnaireBeta→HTMLinjected，mayXSS/videocover实际code不可读，扩展消费者前提。


## recon 与 kxss 命中：反射位置必须落到浏览器执行上下文

正文给出常见闭属性 script 载荷及 GET 参数中的单引号减法 confirm 候选，并提到 kxss；图片只有 triaged/duplicate/收件或验证通知。记录原始请求字节、服务端响应反射位置、浏览器生成 DOM 和实际执行 origin，按 HTML、属性、JavaScript 字符串分别选择无害对照。kxss/字符反射和 report received 不证明脚本执行，正文中的弯引号也不能直接当成 ASCII 引号；奖励/重复状态不能补齐 sink。存档没有完整真实请求，不把其三条报告计为三种已证实根因。

来源：[保存帖1](https://x.com/i/status/1626241664120397827)、[保存帖2](https://x.com/i/status/1627187591693971456)、[保存帖3](https://x.com/i/status/1627424120148226048)。


## 反射未闭合转盲回调：触发页面和敏感能力仍要确认

正文建议把无法完整利用的 RXSS 换成盲 XSS 载荷，图只裁剪 cookie 与浏览器 User-Agent 字段。为每个允许输入设独立关联标识，确定是即时受害者浏览器、后台管理员阅读、预览/扫描器还是自身测试触发，记录执行 origin、页面功能及去重规则。一次外部回调不自动证明存储或管理权限，analytics cookie 不等于身份会话；仍须用自有无害数据验证受保护能力。缺失触发链和页面内容按边界保留，不采集或重放真人凭据。

来源：[保存帖1](https://x.com/i/status/1626579844611072001)。

现有图片证据 `1626579844611072001-02.jpg`：盲XSS回调裁剪 Cookies和BrowserAgent，cookies主要analytics样式，未显示身份cookie或触发页面/输入链。


## 模板表达式与 auxclick：客户端解释器和交互条件先于 WAF 标签

正文给 Angular 风格构造器/charAt/$eval 表达式，以及 details 的 onauxclick confirm 示例；图片只有两个 WAF-bypass 报告状态和 Akamai 页面地址栏候选。前者需要输入真正进入可求值客户端模板及对应版本/表达式规则，后者需要相应 HTML sink 和支持的辅助点击事件。用自有标记定位 DOM/表达式执行并明确用户交互、浏览器及 CSP，比较普通拒绝载荷和变异。反射字符串、地址栏或报告名称不能证明“Cloudflare/Akamai 通用绕过”，客户端模板也不能误标为服务端 SSTI。

来源：[保存帖1](https://x.com/i/status/1626612586694471680)、[保存帖2](https://x.com/i/status/1626646903642558464)、[保存帖3](https://x.com/i/status/1626647268937048068)。

现有图片证据 `1626612586694471680-05.jpg`：Akamai首页URL含JavaScript/编码候选但没有alert或执行证明，URL地址栏不证明Cloudflare/Akamai通用旁路。


## POST 改 GET 与 _escaped_fragment_：渲染路线变化单独验证

图片文字称 id 从 POST 改 GET 后 XSS，另说 _escaped_fragment_ 参数可解除阻断。先记录不同方法/参数选择的 endpoint、返回 content-type、响应字节和浏览器 sink，比较同一无害标记在普通页面与替代渲染/爬虫路线中的处理。方法转换并不保留所有业务语义，参数名存在也不保证触发服务器快照逻辑。只有变更让输入进入可执行上下文且在允许浏览器实测才能确认，图缺少真实请求和执行结果，不能泛化所有服务器。

来源：[保存帖1](https://x.com/i/status/1626995962299224064)。

现有图片证据 `1626995962299224064-04.jpg`：图片文字称POSTid改GETXSS成功、隐藏参数_escaped_fragment_后旁路；仅文字叙述无exchange，方法/参数改变可选不同render路由需分别证实。


## SVG 载荷与脚本内反射：浏览器版本和周围字节决定解析

Safari 图给 SVG/a/onload，另一正文给 SVG script xlink:data 示例并说明后续 script 块影响闭标签，第三帖称已在 script 内应从 d=document 开始并讨论 path/query 引号编码。先保存原始 URL、请求字节、响应上下文和实际 DOM，区分 SVG namespace、外部脚本加载、JavaScript 字符串与普通 HTML。解析闭合、事件支持和编码依浏览器/版本/位置不同，不能由“后面还有 script”推断始终执行；路径与 query 必须以实际发送字节验证。Imperva 地址栏图没有执行结果，历史观察不当作所有 Chrome/Safari 当前行为。

来源：[保存帖1](https://x.com/i/status/1627016854723252227)、[保存帖2](https://x.com/i/status/1627018199991734272)、[保存帖3](https://x.com/i/status/1628285732438609926)。

现有图片证据 `1627016854723252227-02.jpg`：SafariXSS图例<svg><a onload=alert(1337)>，只有载荷没有Safari版本或运行证据。

现有图片证据 `1628285732438609926-03.jpg`：Imperva2022首页地址栏X5S含svg/set/onbegin/d=document等候选，图片无alert/DOM/执行；不能推出绕过Imperva。


## CSP allowlist 检查：允许域不等于允许攻击者脚本

保存正文建议检查 google/google-analytics 等 allowlist，图示 default-src example.com 阻止外部 script。先确定实际执行策略的 script-src/default-src、nonce/hash、多个策略与浏览器报错，再确认允许源上是否存在攻击者可控制且被目标加载为脚本的内容，以及重定向/content-type 等条件。域名在列表或单一 CSP 报错不证明 bypass，CSP 绕过也必须配合实际注入 sink 才形成 XSS。存档没有可控允许源或真实执行链，不把历史推荐站点当当前可利用保证。

来源：[保存帖1](https://x.com/i/status/1627306796330389504)。

现有图片证据 `1627306796330389504-02.jpg`：CSP示意default-src https://www.example.com放行本站js/css阻maliciousjs；没有allowlist可控内容或实际绕过。


## 导入 label color 与 scoped label：同一修复覆盖两种消费者

GitLab 历史报告以外部 GitHub 导入 labels.color 未净化为入口；图说明 GitHub 正常不能任意 color，因此需要受控 dummy API、可达服务、api-scope PAT 和 namespace，后续摘要称 15.3.2 修复漏掉 Premium scoped label（名称含 ::）。提炼应分别追踪外部 API 数据、普通/scoped 持久化字段和两个呈现 sink，以自有无害属性标记比较修复前后。导入接口和 HTML 属性闭合的可控段需要真实 DOM/CSP/浏览器结果，存档只保存跨属性 form/input/script 片段，不补完整 CSP 链。不同 label 类别可共根因，但不能假设一处净化已保护全部变体。

来源：[保存帖1](https://x.com/i/status/1627457877559455744)、[保存帖2](https://x.com/i/status/1627457979959091201)。

现有图片证据 `1627457877559455744-02.jpg`：GitLabGitHubprojectimport labels.color未sanitize历史报告，GitHub不能任意color所以自建dummyGitHubAPI、publicIP/node/GitLab api-scopePAT及namespace条件；下部triggercommand裁剪，没有实际sink/CSP链。

现有图片证据 `1627457979959091201-02.jpg`：GitLab15.3.2普通label修复遗漏scopedlabel，Premium条件、name含::、color跨属性注入form/input title script的历史片段，dummyAPI来源；下文未存，无完整CSP/执行证明，不访问演示VPS。


## card.xq id 的 HTML 与脚本候选：界面注入和执行结果分开

历史图给 /card.xq?id 参数，编码字符串闭 title 后写 body/form，form action 指向外源，另一行是 script alert 候选；图同时提到 jQuery1.11.3。先确定反射上下文、解码顺序和浏览器 DOM，使用无害非提交表单标记验证 HTML 结构可改，另测脚本是否在受保护 origin 执行及 CSP。UI 仿冒、脚本执行和真实凭据提交是不同影响，旧 jQuery 版本也不能独立证明本参数 XSS。现有图没有运行/请求对照，本轮不访问目标或提交表单。

来源：[保存帖1](https://x.com/i/status/1627503435728691200)。

现有图片证据 `1627503435728691200-02.jpg`：labs.history.state.gov/card.xq?id历史报告jQuery1.11.3；图完整encoded闭title后body/formaction到外源用于UIinjection，下方scriptalert候选，未有actualDOM或运行。


## 三阶段 XSS 示意：用户浏览器能力不自动成为系统控制

图画攻击者输入代码、页面返回给用户，再写攻击者获得用户数据或系统控制。把该叙述拆成输入存储/反射、浏览器执行 origin、可访问的 DOM/会话与业务操作，给每环节保留实际消费者和对照。脚本执行受同源、cookie 旗标、CSP 和宿主桥接等条件限制，不自动获得 OS 命令能力；控制服务器也需要独立入口。该图是教学地图，正文的三案例全文未保存，无实际 payload/执行链，不补造。

来源：[保存帖1](https://x.com/i/status/1626642669987586048)。

现有图片证据 `1626642669987586048-02.png`：XSS三阶段示意：攻击者插入未过滤代码→用户访问返回→声称控制数据或系统；无具体sink/origin，浏览器执行不自动OS控制。


## 从参数反射、JWT 解码到浏览器执行的分层判据

pagenum截图可见参数闭合JS字符串并使用数组索引/call调用，另图弹窗1；该实例支持该JS上下文执行，不能把表达式套到HTML属性或JSON。JWT例子先在jwt.io构造name字段脚本，再展示遮挡的目标弹窗和triaged通知；构造或解码JWT不等于通过验签，也不证明认证绕过。必须定位claim如何进入DOM/HTML、签名是否校验、浏览器origin和CSP，以惰性文本渲染作反例；不把弹窗推广为cookie窃取或ATO。

来源：[保存帖1](https://x.com/i/status/1629064458218921984)、[保存帖2](https://x.com/i/status/1629064843117613056)、[保存帖3](https://x.com/i/status/1629474052891979776)、[保存帖4](https://x.com/i/status/1630073368149118978)。

现有图片证据 `1629064458218921984-02.jpg`：地址栏returnUrl(正文redirectUrl)编码javascript var/onerror/throwdocument.cookie，图片有被遮cookie弹窗；执行上下文未完整、不能证明cloudflare通用旁路/会话ATO，不复制。

现有图片证据 `1629474052891979776-02.png`：pagenum 参数闭合 JS 字符串后插入数组索引 call 表达式，响应 script 原样反射；需核对执行上下文而非通用 payload。

现有图片证据 `1629474052891979776-03.png`：同一 pagenum 页面浏览器弹窗1，支持该截图环境执行，无 cookie、会话接管或普适 WAF 绕过证明。

现有图片证据 `1630073368149118978-02.png`：jwt.io 编辑器把script字符串写入name claim，仅证明可构造JWT字符串；没有目标验签、解码渲染、浏览器执行，解码展示不等于XSS。

现有图片证据 `1630073368149118978-03.png`：浏览器地址显示JWT长字符串并出现弹窗，域名和内容遮挡；结合前图支持该环境JWT字段渲染执行，不证明签名绕过或账户接管。


## POST 与跨站触发 XSS 的交互和域名边界

公开POST报告fld_displaytype经字符串闭合进入accesskey/onclick，正文称另一域名未被WAF覆盖；必须核对真实响应上下文、点击/快捷键交互及受影响域名在范围内。另一帖view-source提示只有XSS via CSRF状态卡与accepted valid issue通知；跨站可发送、浏览器会话条件和脚本执行需分别证明。Triaged/Unresolved是处理状态，不等于当前修复或完整复现。不保留截图cookies。

来源：[保存帖1](https://x.com/i/status/1629884538158546948)、[保存帖2](https://x.com/i/status/1630621504248463361)。

现有图片证据 `1629884538158546948-02.jpg`：POST reflected XSS 报告 fld_displaytype 字符串闭合、accesskey/onclick，另域名WAF覆盖差异；需要交互条件和授权域名，图片未给浏览器执行结果，不保留cookies。


## 发票备注 HTML 表单与浏览器自动填充的交互条件

Stripe历史报告图片描述memo插入透明输入表单及按钮，已有保存凭据可能自动填充后经GET提交。关键是HTML插入、页面origin、浏览器/密码管理器填充策略及受害者点击；不自动等同脚本XSS或任意账号接管。自有无敏感账号夹具核对最终DOM、自动填充与目标请求，禁止外域表单/正确转义作反例，奖励和Medium只是该历史报告。

来源：[保存帖1](https://x.com/i/status/1630998493731987456)。

现有图片证据 `1630998493731987456-02.jpg`：Stripe invoice memo HTML注入历史报告：注入opacity0表单，浏览器保存登录凭据并点击按钮后GET送出；自动填充/用户交互是前提，未展示实际网络凭据，不笼统声称任意受害者ATO。


## document.write 和 URL hash eval 的源到 sink 条件

document.write静态写入脚本只是演示，漏洞需不可信source进入sink；SVG onload→eval(location.hash.slice(1))再append外部script也先依赖允许SVG事件/JS执行。fragment通常不送服务器，需核对客户端如何取值、CSP是否允许事件/eval及外脚本、实际origin与用户触发。自有无害标记观察执行，惰性文本写入/严格sink处理作反例；不执行存档外部脚本，链接题名没有通用WAF绕过证据。

来源：[保存帖1](https://x.com/i/status/1631373671158923264)、[保存帖2](https://x.com/i/status/1632193189808308224)。


## Blind XSS 页面秘密检测扩展的回连和数据最小化

正文称XSSHunter fork集成Trufflehog、750余检测类型、完整截图与通知；图片只有仓库封面。检测规则数量不等于检出秘密有效或当前覆盖，回连也不直接证明管理员脚本执行。自有页面夹具用示意假钥核对触发origin、浏览器角色、上传数据和权限，敏感截图/DOM要最小化与脱敏；不向通知渠道发送消息、不收集真实凭据。

来源：[保存帖1](https://x.com/i/status/1631770469954207744)。


## Hook URLSearchParams.get 的执行路径与 DOM XSS 判据

Eval Villain图示hook URLSearchParams.get得到参数名和stack，亦列eval/HTML/定时器等hook；优点是找被当前页面执行路径读取的名称。它不覆盖未触发分支、早期取值、别的解析器或服务器参数。用自有页面交互覆盖记录调用栈/source/sink，以无害参数流确认DOM消费；出现get日志不是XSS，必须进一步确认解释执行与origin。

来源：[保存帖1](https://x.com/i/status/1631997679793233922)、[保存帖2](https://x.com/i/status/1632554953133703169)。

现有图片证据 `1631997679793233922-02.jpg`：Eval Villain hook URLSearchParams.get记录参数与stack，UI亦列eval/DOM等函数；可发现被实际执行路径读取的GET名，不是所有服务器参数或XSS已确认。


## 预登录 XSS 改写表单的本地证据和用户提交前提

正文用querySelector(form)修改method为GET、action指向外部，图片依次显示错误页、带script的error参数与输入框、本地127.0.0.1 HTTP server收到演示用户名/密码查询。支持本地示例的表单改写发送，不证明任意真实站点、密码管理器或用户都会触发。检查不可信错误字段进入脚本/HTML、实际form选中、提交交互、CSP/form-action和页面origin，以正常转义及受控接收端作对照；不保留演示密码，不收取真人凭据。

来源：[保存帖1](https://x.com/i/status/1632332198580813826)。

现有图片证据 `1632332198580813826-02.png`：example.com:2255 auth.php错误参数与空登录表单，未显示注入表单action或网络提交；与正文脚本分开，只有输入接收页面。

现有图片证据 `1632332198580813826-03.png`：预登录页面error参数含script，输入框admin及遮挡密码，页面不见实际form属性；网络链需后图支撑。

现有图片证据 `1632332198580813826-04.png`：本地Python HTTP server收到127.0.0.1 GET含用户名/password演示值，支持本地表单改写发送；不保存密码，不证明真实站点或任意浏览器autofill。


## 历史 URL 到 XSS 工具链须保留每个过滤阶段

wayback/gau→gf→去重→参数替换→反射检查→Dalfox/Gxss等是候选流水线。记录原URL、来源时间、编码、上下文与每阶段丢弃数量，按实际接口允许量限速；跳过302/403/404或DOM挖掘会漏掉跳转/客户端入口。字符串反射、grep Not、callback或工具输出不证明脚本执行，需原始响应、可重现浏览器origin及事件触发对照；不运行来源的一行脚本，也不发送通知。

来源：[保存帖1](https://x.com/i/status/1632766366083170307)、[保存帖2](https://x.com/i/status/1633220741280813056)、[保存帖3](https://x.com/i/status/1634615670595022849)。


## 搜索筛选参数 XSS 的弹窗与账户影响分级

历史USDoS segFilter报告有候选URL及嵌入弹窗图，Resolved/Medium4.7。确认时保存输入到响应或DOM的准确上下文、解码、浏览器origin、CSP与触发动作；随后依据实际页面身份能力评估可读数据/可执行操作。弹窗不证明HttpOnly Cookie可读，也不自动支持ATO，历史路径不视为当前可利用。

来源：[保存帖1](https://x.com/i/status/1633301694623645697)。

现有图片证据 `1633301694623645697-02.jpg`：历史USDoS搜索 segFilter 参数反射XSS报告含URL与嵌入弹窗图，Resolved/Medium4.7；下方偷Cookie/ATO为泛化影响，需输出上下文、浏览器origin及真实可访问会话能力证明。


## 参数反射识别与脚本执行是两道验证

参数发现/反射工具须保留请求、输出位置、编码和DOM消费路径，比较无特殊标记及等价编码。文本回显、200或参数存在不是XSS；需上下文可闭合、浏览器实际触发、origin与策略成立，报告实际能力而非工具标签。

来源：[保存帖1](https://x.com/i/status/1633720577671282690)。


## XSS 工具清单需要按观察角色使用

Firebug/JMeter等与专用XSS扫描工具用途不同，不能23个名字都当有效扫描器。核对工具版本、输入、浏览器/HTTP可见范围和结果证据，保留实际源到sink路径，再用正常与惰性标记/上下文触发对照。工具推荐列表不能证明运行、检出率或端到端覆盖。

来源：[保存帖1](https://x.com/i/status/1634250766222327810)。


## textarea 与 srcdoc 需要确认具体解码和嵌套上下文

textarea结束标签及iframe srcdoc涉及不同HTML文本/属性与嵌套文档消费者。记录原始回显、转义、解码次数、DOM和浏览器策略，用惰性标记及正确上下文对照；原帖%26it;script看似it而不是lt实体，不自动修成可执行形式。未出现有效节点/事件和origin结果不能据字符串确认绕过。

来源：[保存帖1](https://x.com/i/status/1634446545792774144)、[保存帖2](https://x.com/i/status/1634612342855196674)。


## CCAI iframe 导航与共享聊天 origin 要分别证明

保存文章图述agent的cobrowseDomain进入iframe位置允许javascript URL且缺embedding保护；client聊天属性/Waiting message进入HTML，SDK共享websdk.ujet.co origin并信任Cobrowse/window.opener形成跨站聊天候选。先验证输入到导航/HTML消费者和实际执行origin，再用自有两个站点/会话核对opener、origin/tenant绑定及受保护消息权限。代码横向裁切无完整运行证据，不把SDK共享域直接等同任意跨租户接管。

来源：[保存帖1](https://x.com/i/status/1634932184195952644)。

现有图片证据 `1634932184195952644-02.jpg`：CCAI文章保存截图：Agent iframe由cobrowseDomain控制javascript URL且无embedding保护；Client聊天链接属性/Waiting message进入HTML；SDK共享websdk.ujet.co origin导致跨网站chat/window.opener信任候选。代码横向裁切，缺实际弹窗/租户对照；需要参数→iframe导航及共享origin/窗口信任两段证明。


## 邮箱合法语法与最终 HTML 消费者分别核对

引号/括号评论和带HTML字样的邮箱可能通过校验后在资料页/邮件模板显示。记录规范化、地址所有权验证及最终HTML/属性/文本上下文，以自有地址的惰性标记和正常/转义对照确认实际DOM与origin。合法邮箱或字符串能保存不是XSS，70%狩猎者不测邮箱是未提供样本的经验数字，不作为概率。

来源：[保存帖1](https://x.com/i/status/1634970760224845825)、[保存帖2](https://x.com/i/status/1635006251108294656)、[保存帖3](https://x.com/i/status/1635231847251836928)。


## redirect_uri javascript 弹窗需定位导航消费者

图中浏览器参数为javascript字样并弹窗，但源域遮蔽、缺HTTP/DOM处理。记录请求、重定向/脚本导航实现、URL协议允许列表、解码、浏览器origin与真实触发；用惰性正常/被拒绝scheme对照核对。弹窗仅支持该截图局部执行线索，不能从参数名判所有OAuth跳转可XSS或直接ATO。

来源：[保存帖1](https://x.com/i/status/1635373245208866818)。

现有图片证据 `1635373245208866818-02.jpg`：浏览器redirect_uri=javascript文本及弹窗Xss By Matrixm；地址部分遮蔽，没有HTTP/DOM消费者或会话影响，需同origin实际导航执行和策略/正常对照，不能只说RXSS所有场景。


## 客户端模板插入输入不必然执行框架表达式

CSTI前提是输入进入客户端框架编译/表达式求值，而非普通DOM文本或已处理数据。固定框架版本、source到编译器路径、CSP/沙箱与受控常量表达式/文字对照，记录DOM和origin。动态页面显示用户数据不等High，只有实际越权能力及触发条件支持评级。

来源：[保存帖1](https://x.com/i/status/1635582532077879297)。


## 反射检查管道的文件与端口覆盖要独立核对

复用已核验图包含passive枚举、resolved过滤、httprobe81/8080/8443、wayback/kxss，domain/domains文件名不一致及追加旧数据。记录源文件、运行版本、端口/协议和阶段失败，测试受控样例确认实际请求归属。反射工具命中不是浏览器执行，旧文件混入/端口缺失不能当目标完整阴性。

来源：[保存帖1](https://x.com/i/status/1636011871320051717)。


## 盲 XSS 面板的 admin 地址与遥测 Cookie 不等角色证据

面板列admin URI/referrer、Mac UA/GPU、遥测session Cookie、NRBA sessionStorage和DOM片段；这些字段可能客户端自报，不保存真实值。绑定唯一惰性源标记、受控浏览器实际执行/回连时间、origin和服务器真实权限，区分浏览器遥测与认证凭据。admin子域、callback或空localStorage不证明管理员会话/ATO，缺源请求和角色就保留限制。

来源：[保存帖1](https://x.com/i/status/1637210171901644800)。

现有图片证据 `1637210171901644800-02.jpg`：盲XSS callback面板URI/referrer指向admin，UA Mac/AppleM2，Cookies仅遥测session类、sessionStorage NRBA/localStorage空、DOM片段与时间；不保留真实值。面板字段可自报，需唯一源标记/真实受控浏览器执行及角色证明，admin子域和遥测cookie不等管理员有效凭据/ATO。


## 全角尖括号候选必须检查存储与输出的真实规范化

正文声称某些ASP.NET/SQLServer路径把全角尖括号规范化。比较提交字节、数据库列类型/排序规则、存取转换和最终浏览器上下文，先用惰性字符标记追踪再确认执行。不能假设SQLServer所有字段都会转换；存储值变化、字形相似或原样显示均不等XSS。

来源：[保存帖1](https://x.com/i/status/1637519362532986881)。


## Intruder 提取反射后仍需最终 DOM 与事件证据

图中部分script已实体转义，img事件串原样突出，正文描述GrepExtract选反射。保存编码前后值、反射上下文与截取位置，区别纯文本、属性、脚本和事件；固定业务请求后检查浏览器真实解析与无害标记事件。原样反射、绿框或可通过WAF不等脚本执行，不把自动提取当XSS验证。

来源：[保存帖1](https://x.com/i/status/1637551042505347072)。

现有图片证据 `1637551042505347072-02.png`：Intruder反射列表部分编码script被转义而img事件原样；缺最终DOM与事件执行，原样反射不等XSS。


## 管理员登录页 XSS 不自动获得管理员权限

保存TD报告描述win进入popupLogin.jsp并跳出引号，附cookie弹窗示意及历史Medium4.7。核对登录前可达路径、最终DOM、浏览器事件和目标cookie可读性，区分HTML/DOM消费与会话权限。管理员登录页面名称、弹窗和非HttpOnly cookie不能证明管理员ATO，不访问历史目标。

来源：[保存帖1](https://x.com/i/status/1637582442079944707)。

现有图片证据 `1637582442079944707-02.jpg`：TD登录popupLogin.jsp的win反射、引号跳出与cookie弹窗截图，历史Medium4.7；登录前可达不等管理员权限/ATO，需上下文/HttpOnly限制。


## Wayback 到 Dalfox 的贪婪截断会改变参数结构

保存管线按gf xss筛选，sed s/=.*/=/从首个等号后删掉全部剩余内容，可能丢后续参数和值。保留原始URL与转换后URL映射，以URL解析器处理指定值，核对可达性/身份及反射上下文；历史存档和工具输出不等执行成功。归档blind回连地址属于他人，不调用或批量扫描。

来源：[保存帖1](https://x.com/i/status/1637683271273418752)。

现有图片证据 `1637683271273418752-02.jpg`：Waybackurls→gf→sed s/=.*/=/→sort/tee→Dalfox，贪婪sed会删除首=之后所有值/后续参数；第三方blind域名非自有，不执行。


## 分字段输入必须在真实合成位置形成相同上下文

图把img/src、onerror与事件值拆到First/Middle/Last，另一图仅有persistent通知标题及奖励。追踪存储、拼接顺序、空格/转义/长度限制和每处渲染上下文，以完整最终DOM和受控账户事件证明。输入框能保存、字段合计长度或单一标题不等所有通知位置可执行。

来源：[保存帖1](https://x.com/i/status/1637856731740135424)。

现有图片证据 `1637856731740135424-03.jpg`：First/Middle/Last拆分img/src事件，需实际拼接分隔符与HTML上下文/存储路径；各字段值图无最终DOM执行。


## 允许富文本也要检查不同字段与 iframe 使用点

正文提出Title+iframe，图只有基本XSS Medium4.3状态。审计每个字段、净化器、嵌入协议/来源及preview/通知/管理页上下文，比较预期允许HTML与越过权限的实际脚本/导航能力。产品允许HTML不意味着所有consumer安全；同时iframe存在或标题不能替代最终DOM与受控执行证据。

来源：[保存帖1](https://x.com/i/status/1638232819875848212)。


## 删除反馈的 Blind XSS 需要后台消费与回连归因

正文建议删除/停用账号后的反馈输入，图只有P2Triaged题名。用许可自有账户和惰性标记记录反馈保存、账号生命周期、后台渲染/导出与回连源；区别自动扫描、浏览器preview与真实受保护后台执行。账户删除或回连菜单不证明管理员ATO，不触发外部反馈/主动脚本。

来源：[保存帖1](https://x.com/i/status/1638397309955473408)。


## HTML 注入与 DOM XSS 的评级记录不能替代消费者

两份Uber图分别HTMLinjection和DOMXSS题名，含历史评级调整/奖励但没有参数或DOMsource/sink。需原始输入、响应/客户端转换、最终上下文、触发条件与受控事件，分开富文本展示与脚本能力。Medium或弱点标签不能用于推断具体编码/利用链，不补造外链全文。

来源：[保存帖1](https://x.com/i/status/1638865931261693953)、[保存帖2](https://x.com/i/status/1638866022907117568)。


## 公开注册页面的军种参数反射按事件上下文确认

两份报告图NextRequestAccount.action militarybranchGET加换行/onmouseover，正文称登录前注册可达。保留各来源与被遮目标，不把相似模板当同一host；检查属性引用、规范化和实际鼠标事件执行。登录前可达扩大输入机会但不自动管理员会话权限，示例/评级不足证明所有部署。

来源：[保存帖1](https://x.com/i/status/1639319130154188800)、[保存帖2](https://x.com/i/status/1639319307120263175)。

现有图片证据 `1639319130154188800-02.jpg`：DoD公开注册NextRequestAccount.action militarybranchGET反射/换行onmouseoverpayload题文，需最终attribute/事件执行/登录前范围，不抄被遮目标或等登录后ATO。

现有图片证据 `1639319307120263175-02.jpg`：DoD另一军种注册端点与g140相同结构不同遮目标，独立post，最终DOM/事件仍需核对。


## 邮件正文预览的双层编码还需要真实 DOM 解析

图PreviewLetterhead.aspx emailbody需先注册登录，HTML实体后再URLencode混合大小写script声明；不验证email不等免登录。保持自有账户，记录URL解码/HTML消费、净化器和最终previeworigin/DOM事件。编码文本能存储或反射不等WAF绕过/脚本执行，不补造被遮目标。

来源：[保存帖1](https://x.com/i/status/1639326753611972618)。

现有图片证据 `1639326753611972618-02.jpg`：PreviewLetterhead.aspx emailbody需注册登录，URL+HTMLencode混大小写脚本声明，注册不验证email不等免登录；需要实际多层decode/最终DOM而非编码串反射。


## JavaScript URL 控制字符先追踪浏览器的真实解析

已审阅复用图和正文把大小写、换行、tab、CR及C0控制字符插入 javascript URL 候选。记录输入字节、URL规范化及最终 href/navigation 消费者，以许可惰性标记和实际DOM/事件核对。文本匹配差异不等浏览器执行；上下文、CSP、浏览器版本和导航触发必须分别满足。

来源：[保存帖1](https://x.com/i/status/1639677021247643648)、[保存帖2](https://x.com/i/status/1639918426339819523)。

现有图片证据 `1639918426339819523-02.jpg`：javascript中newline/tab/CR/C0前缀及大小写图，转义文字与真实控制字节区分，需最终URLparser/context不通用WAF绕过。


## ASP.NET 重复参数需校验实际合并和输出顺序

复用图与正文声称HTTP parameter pollution能绕WAF。保持原始重复参数及顺序，追踪网关/框架/handler分别取首、末、列表或逗号合并的行为及最终HTML消费者。不能假定所有IIS都会拼接脚本；过滤差异、逗号或200都不等执行，实际解析版本与DOM事件需独立证明。

来源：[保存帖1](https://x.com/i/status/1640558328249188352)。


## 文件名存储 XSS 标题缺最终渲染位置

正文只给 LINE filename stored XSS 历史标题、Low与100美元，没有响应或DOM。沿上传/保存名称/列表、通知或预览的实际渲染上下文检查编码与身份，验证自有文件的无害事件。题名不等所有文件名消费都会执行，奖励不补全外链步骤。

来源：[保存帖1](https://x.com/i/status/1640640170507509760)。


## Dalfox 高并发与跳过检查需要记录覆盖缺口

图片管线使用高并发、skip-bav与跳过mining/grepping选项。冻结转换前URL、身份、工具版本及已跳过检查，单变量确认最终反射/DOM/事件再扩展必要候选。并发100和扫描输出不能证明所有消费者已测，禁用发现项会缩小覆盖，不执行外部blind回连或超预算探测。

来源：[保存帖1](https://x.com/i/status/1640676448829599745)。

现有图片证据 `1640676448829599745-02.jpg`：subfinder-all→httpx→katana→Gxss-c100→dalfox skipbav/miningall/grepping，跳过阶段的速度与覆盖区别；无反射/浏览器执行结果，不继承并发100。


## document.domain 改写与 with 变体要核对执行上下文

两图响应把 document.domain 改成 document_domain，另保留 with(document)alert(domain)，没有浏览器执行。记录变换位置、编码与完整上下文，区分对象属性与新标识符；with在严格模式有语法限制，CSP与事件触发也独立。响应原样保留不证明XSS或通用关键字绕过。

来源：[保存帖1](https://x.com/i/status/1640951195245367298)。

现有图片证据 `1640951195245367298-02.png`：原始请求/响应中 document.domain 的点被改成 document_domain，下划线改变标识符语义；只展示响应文本，没证明弹窗或具体过滤实现。

现有图片证据 `1640951195245367298-03.png`：第二张把 with(document)alert(domain) 放入 SVG onload，响应保留该语法。需实际执行上下文、严格模式与 CSP，文本保留不能单独证明 XSS。


## replace 首次替换与全局净化不能混为一谈

已审阅两张复用图讨论字符串replace与控制域。对照首个命中、后续出现和顺序，核实实际传参是字符串还是带g正则、替换后解码及最终输出上下文。单次替换行为不能证明具体站点的XSS；最终DOM/事件、CSP与存储链仍需独立证据。

来源：[保存帖1](https://x.com/i/status/1641132231610564609)。


## 短 payload 与 polyglot 都依赖解析上下文

Tiny XSS 两图用name、URL、frame索引、srcdoc、外部script及eval；polyglot图标注引号/注释/脚本闭合和details ontoggle。追踪可控字段、frame来源、窗口名、严格模式、sandbox和CSP继承，分HTML/属性/JS消费者做惰性对照。关闭unsafe-inline不自动允许外部脚本，长度短、混合大小写及自动事件也不保证执行，不复制外部脚本地址调用。

来源：[保存帖1](https://x.com/i/status/1641144188489338880)、[保存帖2](https://x.com/i/status/1641450902136684548)、[保存帖3](https://x.com/i/status/1641464046443429888)。

现有图片证据 `1641144188489338880-02.png`：Tiny XSS 图包含 window.name、URL、frame 索引、srcdoc、外部 script 和 Firefox eval；声称无 unsafe-inline 时有效不完整，仍取决 script-src、继承 CSP、sandbox、name可控性与实际浏览器。长度短不能保证执行。

现有图片证据 `1641450902136684548-02.png`：Tiny XSS 第二版本同样展示 frame/name/srcdoc/script/URL 模板，支持上下文与 CSP 边界提炼，没有执行结果，不能直接复用为普适绕过。

现有图片证据 `1641464046443429888-02.jpg`：XSS polyglot 注释图解释引号/注释/脚本闭合、details open 与 ontoggle、Unicode标识符、tagged template。跨上下文闭合仅候选，实际 HTML/JS解析、事件触发、编码与CSP需证明，混合大小写或自动事件不保证任意上下文。


## 自动 XSS 工具能力应以输入与最终事件核对

正文XSScrapy称XSS/SQL发现功能，未显示请求、输出或规则。把反射候选、浏览器执行与SQL消费者分开，固定工具/参数/身份及基线再核对实际DOM和事件。工具介绍或自动扫描不说明覆盖完成，不获取外链教程或执行代码。

来源：[保存帖1](https://x.com/i/status/1641876800732286982)。


## 截断的 Cloudflare 字符串不能视为有效绕过

保存字符串含domument等异常属性及省略号，指向第三方回连地址，没有请求/DOM结果。保留原错误与截断边界，追踪HTML属性、JavaScript表达式与CSP，许可惰性事件对照后才认定执行。不能补成有效document.domain或调用外部回连，Cloudflare标签不保证绕过。

来源：[保存帖1](https://x.com/i/status/1641902234249342977)、[保存帖2](https://x.com/i/status/1641920769046511616)。


## Cookie 外传模板需区分执行与可读取会话

正文percent编码document.write/img模板被截断，缺实际渲染/请求。审查编码解码层、HTML/JS上下文、HttpOnly和token是否另在正文反射，以无害自有标记确认事件。脚本能执行不自动会话接管，不复制/调用回连域、提取真实cookie或把截断补成payload。

来源：[保存帖1](https://x.com/i/status/1641903020316450820)。


## 自定义标签 mouseover 要核对存储与受害者渲染

正文自定义tag、引号、样式及onmouseover字符串，没有保存/再显示证据。固定自有账户与输入字段，比较存储值、最终DOM、转义与事件所需交互，区分反射和存储消费。红色大区域或题名StoredXSS不证明跨用户执行，也不证明自动触发。

来源：[保存帖1](https://x.com/i/status/1641903391491383302)。


## JSON 数组内容到 JS 执行还缺实际消费者

正文只有数组内引号/alert/comment字符串并称WAF bypass。追踪JSON解析后的值是否进入HTML、脚本拼接或eval，记录服务器与浏览器编码、实际上下文及事件；合法JSON、响应200或过滤通过不等脚本执行，不把数组语法当普适绕过。

来源：[保存帖1](https://x.com/i/status/1641904823980417027)、[保存帖2](https://x.com/i/status/1641924145696104448)。


## select 与 noembed 混合模板需核对 HTML 状态切换

正文混合select/noembed/script、引号、换行编码与Unicode标识符，没有DOM或执行。追踪实际HTML tokenizer/上下文、净化器、解码顺序与CSP，用许可惰性标记比较输入与最终节点。不同浏览器/上下文不保证相同结果，标签组合或Cloudflare标题不是绕过证据。

来源：[保存帖1](https://x.com/i/status/1641906018073600007)。


## 单页弹窗与批量模板结果要分别核验证据

图浏览器SVNWebClient error.jsp的errormessage脚本及提示框，下方多产品Nuclei模板/info/medium结果。记录该页原始请求、实际产品/版本与最终DOM；弹窗只支持该次脚本执行，模板匹配仍需独立消费者及权限核对。5543加载/979cluster不是漏洞数，也不从一页扩成所有CVE已确认。

来源：[保存帖1](https://x.com/i/status/1642026568624091136)。

现有图片证据 `1642026568624091136-02.jpg`：Nuclei窗口加载5543模板/cluster979，多产品/CVE/info/medium结果；浏览器 SVNWebClient error.jsp参数与弹窗。只能该页面脚本执行示例，不能让所有模板命中成为漏洞、组件归属需核验。


## 弹窗函数替换要核对语法与实际事件

正文prompt/confirm/regex source/window属性候选，confrim拼写错误须保留。先确认输入到可执行JS及最终浏览器事件，区分函数可调用与过滤差异。换函数名称不保证绕过、prompt更好没有普适依据，不静默修正拼写后声称原串有效。

来源：[保存帖1](https://x.com/i/status/1642175097598353409)。


## cookie 属性访问变体不扩大可读会话范围

正文with(document)、括号与regex拼接属性名。固定实际JS上下文/严格模式、净化器与事件，核对HttpOnly及同源可读值；with在严格模式受限，属性字形变化不等过滤必过。可读cookie不自动认证token或ATO，不调用/外传真实会话。

来源：[保存帖1](https://x.com/i/status/1642177732783030272)。


## 代理编码与 HttpOnly 秘密正文反射需要分别追踪

32red摘要称URL编码改变转发、cookie XSS回传，CAKEPHP虽HttpOnly却在HTML反射；POC要求victim已登录和日志服务器，无具体wire/执行/兑换。追踪前后代理解码、header/cookie边界、最终DOM及正文中的会话秘密，区分document.cookie限制与额外泄漏。历史ATO声明不是当前有效接管，不调用外部日志或读取真实会话。

来源：[保存帖1](https://x.com/i/status/1642890044301033473)。

现有图片证据 `1642890044301033473-02.jpg`：32red反向代理报告摘要URL-encoded字符改变转发请求，cookie注入XSS回传；CAKEPHP HttpOnly虽不可document.cookie直接读却被HTML反射，声明可读。POC条件需victim已登录和外部日志服务；截图无具体编码wire/执行/ATO兑换，不调用日志地址，正文N/A与图5250不同。


## java 标签拼接 location 的结果要按实际 DOM 核对

保存模板以自定义java标签的tagName、innerHTML与location.hash拼接导航，contentEditable/autofocus/onfocus负责触发。HTML本身含引号与尖括号，“零特殊字符”说法只可能指某个局部字符串，不能整体照搬。记录实际HTML上下文、tagName大小写、最终scheme、焦点事件、hash与CSP/浏览器版本；拼出javascript文本不等浏览器允许执行，模板无运行证据。

来源：[保存帖1](https://x.com/i/status/1644070463646371840)。


## JSP ContextPath 中实体与点段要逐层解析

保存ContextPath候选URL含&sol;、&num;和/..;/路径段，无请求响应。分别记录HTTP原始路径、代理/容器规范化、contextPath生成、HTML实体解析和最终链接或script src；只有可控值进入真实可执行消费者才评估XSS。实体文本在URL层不自动变为HTML实体含义，路径可变或链接改变也不自动执行脚本。

来源：[保存帖1](https://x.com/i/status/1644304821883744257)。


## Self XSS 加 CSRF 改密链要证明受害者无需粘贴

图声称先在账户panel发现SelfXSS，再以CSRF导入脚本读取改密页token并POST；报告为Duplicate/Unresolved。必须证明外部请求能让受害者浏览器保存/呈现可执行内容，记录origin、Cookie、CSP与具体交互。代码用DOMParser固定input[20]/[17]取fields/key，withCredentials不绕过SOP，POST后alert Done未检查成功；需同源执行和持久改密/再认证对照，流程与示例不等完整ATO。

来源：[保存帖1](https://x.com/i/status/1645069156952186880)。

现有图片证据 `1645069156952186880-02.jpg`：流程图声称账户panelSelfXSS结合CSRF加载JS，再从源码读antiCSRFtoken改密；需要受害者不手动粘贴情况下的注入触发、origin/cookie/CSP/持久化改密，流程声明不等于复现。

现有图片证据 `1645069156952186880-04.jpg`：代码XHR GET改密页面、DOMParser读取input[20]/[17]作fields/key，再带credentials POST密码；固定索引脆弱，withCredentials不绕SOP，alertDone未校验POST成功。


## DOM Invader canary 到可执行 sink 需要上下文证据

正文建议广泛放canary寻找可控sink。按许可输入逐个保留source到sink路径、解码/净化、最终DOM/JS上下文和所需交互，再用惰性事件标记确认消费者。canary可控只证明数据流，进入textContent或受正确转义的HTML不等执行；更多注入次数不代表DOMXSS覆盖完成。

来源：[保存帖1](https://x.com/i/status/1645492733413400595)。


## SOAP 文本进入展示页面才形成独立的存储型 XSS 假设

SOAP/CDATA 示例中的脚本文本需要从提交字段追到存储位置及后续展示页面，记录编码、HTML 上下文与浏览器解析。用自有对象和最小可见标记比较提交前后，确认是否被另一受控会话作为活动内容解析。CDATA 接受、数据库存储或原始响应回显都不能代替浏览器执行；不能将这种 XSS 线索和外部实体绕过混为一个证明。

来源：[保存帖1](https://x.com/i/status/1646534134620381184)。

现有图片证据 `1646534134620381184-02.jpg`：SOAPstoreData text CDATA内script文本，图展示XSS候选不是DTD/XXE；CDATA只是文本，需后续存储HTML渲染，不是绕过禁DTD。


## logout 的 javascript 参数需证明到达可执行导航消费者

请求中 logout.jsx 的 home 参数是 javascript 风格表达式。记录参数在响应、重定向、页面脚本及最终导航中的流转，核对是否被允许为脚本 URL、是否需要点击、同源身份与 CSP。请求可发送、参数回显或注销成功都不能证明浏览器执行；也没有 cookie 外传证据。用受控非敏感标记确认真实消费者，不把请求截图升级为跨用户影响。

来源：[保存帖1](https://x.com/i/status/1646929309561397257)。

现有图片证据 `1646929309561397257-02.jpg`：auth/logout.jsx home=javascript(alert...)候选，目标遮挡，无最终DOM/导航或弹窗；cookie偷取仅泛述，需导航scheme执行/CSP/HttpOnly。


## 错误响应的 MIME 嗅探要记录实际浏览器解释

图片展示 ASP.NET 错误响应中类似 img 事件内容，帖子讨论 MIME 嗅探。核对原始 Content-Type、X-Content-Type-Options、Content-Disposition、请求上下文与实际浏览器版本/加载方式，观察响应是否被当作活动 HTML 解释。500 状态和包含脚本样式字符串都不能证明执行；错误页回显若被纯文本、附件或强制正确类型处理，会阻断该路径。缺少浏览器结果时只能保留反射和嗅探假设。

来源：[保存帖1](https://x.com/i/status/1646954357798195207)。

现有图片证据 `1646954357798195207-02.jpg`：HTTP2 500ASP.NET Error行反射imgonerror，无ContentType/nosniff显示；缺浏览器嗅探最终DOM/弹窗，500/反射不保证HTML执行。


## hash 动态调用 parent 函数需检查来源、可达性和实际参数

代码图把 commReceive.html 的 hash 按 || 拆分，再调用 `window.parent[functionName](若干参数)`。这是不可信片段控制函数选择的候选；需确认加载上下文、父子页面来源、可选函数是否可达，以及传入参数是否到达危险执行点。存在 eval 名称、页面可枚举或声称 967 个 URL 都不证明每个是独立 XSS，也不代表跨源可读取 parent。只用自有页面/账户和非敏感标记建立链路，保留 CSP 和实际浏览器结果。

来源：[保存帖1](https://x.com/i/status/1647687104153939969)。

现有图片证据 `1647687104153939969-02.jpg`：DOMXSS流程commReceive.html读hash分割||，functionName=aa[0],`window.parent[functionName](aa1..4)`，eval||alert等声明执行；枚举0001–9999得967URLs无各结果，需sameoriginframe/parentfunction允许/DOMCSP，URL数不等967独立漏洞。


## WAF 绕过语法需先确认原始字节能形成浏览器语法

保存示例用外观类似括号的 « » 等字符包围 form/action javascript 风格文本，且部分语法不完整。不要悄悄改成正常尖括号再声称原样成功：先保留实际字节、服务端解码/规范化、响应上下文和浏览器 DOM，再核对表单提交/用户动作和 CSP。WAF 放行、文本回显或被编辑器着色不证明可执行；字形相似而未被浏览器解析成标签是必要反例。

来源：[保存帖1](https://x.com/i/status/1647995835991441408)、[保存帖2](https://x.com/i/status/1648001558045659141)。


## Trusted Types 日志工具需实际堆栈与消费者支持

帖文提到通过日志/堆栈追踪 Trusted Types，配图为 Google 首页的空 DevTools 控制台。工具可用于观察实际违规与 source→sink 链，但空控制台既不能证明扫描完成，也不能证明没有危险消费者。需要自有页面动作、实际事件/堆栈、启用策略和输入传播对照；观察插件或告警不是绕过 Trusted Types 的证据，没有保存输出时不补出插件版本行为。

来源：[保存帖1](https://x.com/i/status/1648340955173634048)。


## script.src 与 default-src self 问题需核对完整策略及资源内容

保存帖仅提问：CSP default-src self 下 script src 是 sink 是否可绕过。先保留完整实际策略与回退关系，确认可控值如何到达脚本 URL、URL 是否允许的同源资源，以及返回字节是否真被当作 JavaScript 执行。单一 directive、可设置 src 或同源页面存在不能证明绕过；脚本类型、响应头、页面动作与实际浏览器结果需分别记录。未保存页面和结果时保留条件式问题，不从提问补出通用绕过载荷。

来源：[保存帖1](https://x.com/i/status/1648754685220642824)。


## HTML 实体协议变形需追踪实际解码与链接消费者

帖子从合法/非标准 href 测到 javascript 被拦及编码实体候选。保留原始字节，比较 URL/HTML 解码、校验、最终 DOM 和点击后的协议解释；百分号编码与 HTML 实体并非在所有层都会依次解码。候选字符串被接受或浏览器展示链接不等执行；需自有页面的无害标记、完整策略和负例，不能把给定拼写自动修成通用绕过。

来源：[保存帖1](https://x.com/i/status/1649091314842238978)。


## 计划帖创建与编辑链接应采用同一协议校验

RichText/Markdown 案例摘要指出编辑计划帖时服务端链接过滤与创建不一致，可能存入 javascript scheme。用自有计划帖比较创建、编辑、存储和最终点击消费者，记录 DOM、编码、CSP 与触发动作。图中创建步骤后续被裁切，摘要不是实际执行；接受链接或将字符串存入数据不能证明跨用户执行，也不能由计划帖接口推导普通帖都受影响。

来源：[保存帖1](https://x.com/i/status/1649136543666171909)。

现有图片证据 `1649136543666171909-02.jpg`：Redditscheduledpost RichText/Markdown编辑链接服务端未过滤javascript scheme的摘要，显示创建带链接计划帖步骤，后续请求和执行裁切；需编辑与创建校验/渲染比较。


## 相邻搜索路由的反射标记不能合成已确认 XSS

两张 Equifax 报告图分别是 personal/help/search 的 search 和 personal/search 的 q，显示 broook 在源码/JavaScript 中出现。分别绑定路径、字段、编码、脚本/属性上下文和实际浏览器动作，负例要保留普通文本反射。嵌套截图及后续载荷裁切，无法确认上下文逃逸/执行；相邻路由和相同报告类型不证明同根因，更不能按页面数量计独立漏洞。

来源：[保存帖1](https://x.com/i/status/1650137591839182849)、[保存帖2](https://x.com/i/status/1650137683249733632)。

现有图片证据 `1650137591839182849-02.jpg`：Equifaxpersonal/help/search?search=broook报告显示source反射/JavaScript文字提示，嵌套截图太小且完整载荷/执行裁切；反射标记非XSS确认。

现有图片证据 `1650137683249733632-02.jpg`：第二报告personal/search?q=broook同样source反射但不同路径参数，不能两路合成一个实际漏洞；无完整JS上下文/执行。


## 注销反馈里的盲 XSS 需要绑定实际后续阅读环境

保存帖给出注册、删除账户时填反馈的入口，没有保存载荷或回连。先核对反馈是否存储、谁在哪个页面/工单消费者查看、输出上下文与策略；用授权隔离账号和唯一无害标记建立浏览器实际结果。文本接受、WAF 放行或普通 DNS/HTTP 事件不证明脚本执行；不删除真实账户或向外部联系人投递以补证。

来源：[保存帖1](https://x.com/i/status/1650610558977097729)。


## 错误页 HTML 注入和 cPanel 路径载荷须分别验证执行

coins.state.gov 图明确 XSS 尝试无结果而仅 HTML 注入；另帖给 cpanelwebcall 编码路径及历史 CVE-2023-29489，但没有目标响应。分别记录原字节、反射位置、HTML/属性/脚本上下文及浏览器无害结果；htt.p 的原拼写不默默改成已执行 URL。HTML/DOM 改动、工具标签或历史编号不等脚本执行，更不证明当前 cPanel 部署受影响。

来源：[保存帖1](https://x.com/i/status/1651343177410830340)、[保存帖2](https://x.com/i/status/1651404938768007170)。

现有图片证据 `1651343177410830340-02.jpg`：coins.state.govErrors.aspx?aspxerrorpath文本注入报告：XSS尝试没结果，dalfox仅HTMLinj，视频没保存；区分markup/DOM改动与脚本执行，Low标签不代替浏览器。


## cPanel webcall 错误页反射与模板误报分开审查

保存 YAML/PoC 指向 /cpanelwebcall 并使用编码标签；图片错误页与 prompt 对话框支持特定历史反射场景。需绑定实际监听服务、原始请求、响应反射位置、解码次数和浏览器 HTML 解析及执行结果。不同端口必须独立确认服务与范围；模板 word 匹配或 verified 元数据不能代替浏览器执行，不把单一页面推广为全部 cPanel 版本。

来源：[保存帖1](https://x.com/i/status/1651738000085090305)、[保存帖2](https://x.com/i/status/1651933214024278018)、[保存帖3](https://x.com/i/status/1651956936756297729)。

保存图片 `1651933214024278018-02.jpg`：cPanel CVE2023-29489 Nuclei YAML片段、GET /cpanelwebcall编码img/onerror及wordmatcher起始；verified元数据不是执行证据，完整匹配条件未保存。 本段只使用已保存且实际查看的内容。

保存图片 `1651956936756297729-02.jpg`：cPanel webcall错误页与prompt1并列，多个端口PoC列表；可提炼错误页反射进入HTML解析，端口列表仍需独立映射和实际验证。 本段只使用已保存且实际查看的内容。


## 字符引用混合脚本方案需穿过真实链接消费者

保存 href 例子用 HTML 字符引用、控制字符和动态属性取值构造脚本方案。逐层记录 HTTP 字节、HTML 解析后属性值、URL 处理、点击触发和 CSP；数字进制转字符串不等于所有上下文都能调用相同函数。只能在自控页面验证，不运行归档字符串；WAF 放行与浏览器执行分别出示证据。

来源：[保存帖1](https://x.com/i/status/1651740036717576195)。


## Blind XSS 回调应绑定输入、渲染主体和时间

原帖有自动参数/头部喷射以及历史 URL→User-Agent 外部脚本命令。改为授权、自控接收端的单一无敏感标记，记录输入请求、存储位置、管理员渲染上下文、callback token/时间及实际脚本执行。DNS/HTTP 回调可来自扫描器或预览器，P1 New 标题不证明管理界面执行；不复用他人回调域名、不采集 cookies 或盲喷全部历史端点。

来源：[保存帖1](https://x.com/i/status/1653085593906163712)、[保存帖2](https://x.com/i/status/1654025276123406337)。

保存图片 `1654025276123406337-02.jpg`：BlindXSS MassHunt waybackurls→httpx UA第三方callback；仅命令无回调，不用他人callback/外部批量喷射。 本段只使用已保存且实际查看的内容。


## Stripe 历史无 CSP 绕过报告保留执行边界

截图描述 custom link 的脚本方案与 CUSTOM Button href，作者承认 CSP 阻止执行；当时特定程序允许无 CSP bypass 的有效 XSS 降级受理。标准 button 的 href 与组件实际导航行为不同，需确认组件、HTML/JS sink、触发和 CSP 报错。历史受理政策只约束该保存上下文，不推广其他项目或当前政策；报告状态和奖励不证明脚本实际执行。

来源：[保存帖1](https://x.com/i/status/1653165121630269442)、[保存帖2](https://x.com/i/status/1653165222880845829)。

保存图片 `1653165121630269442-02.jpg`：Stripe custom link javascript LF payload，CSP refusedexecution且保存当时项目允许无CSPbypass低severity；政策只历史特定项目，未显示运行成功/完整sink。 本段只使用已保存且实际查看的内容。

保存图片 `1653165222880845829-02.jpg`：Stripe CUSTOM Button hrefjavascript截图，正文承认未CSPbypass；标准HTMLbutton没有anchorhref导航语义，需组件实际转换/handler，不把示例当执行。 本段只使用已保存且实际查看的内容。


## contenteditable 事件与顶层调用的触发条件

正文 onbeforeinput、array map 等变体只有在 HTML 属性解析、可编辑元素实际输入与执行环境满足时才有意义。记录解码后 DOM、事件触发、函数对象/调用上下文、top 同源限制和 CSP；保存的 payload 不执行，P3 New 截图不能补浏览器证据。过滤器允许字串也可能完全没有可达事件消费者。

来源：[保存帖1](https://x.com/i/status/1653363695949414401)。


## 路径字符串进入脚本的上下文不能由短 payload 推算

保存 TD 报告给 TechnicalInsight 路径和拼接风格字符串，URL 含分隔符。必须保留原始发送路径/query、响应字符位置、编码与脚本语法上下文，再本地无害夹具比较正常/转义反例。截图没有浏览器执行或具体响应 sink，不把 URL 本身当跨用户窃取凭据/植入恶意软件证明，也不静默修正不完整 payload。

来源：[保存帖1](https://x.com/i/status/1653625660554854401)。

保存图片 `1653625660554854401-02.jpg`：TD路径TechnicalInsight/...字符串拼接payload报告，步骤URL有querydelimiter，未显示具体响应sink或弹窗；不自动修正payload字节或声称cookie窃取。 本段只使用已保存且实际查看的内容。


## JSON 邮件数组到 JavaScript sink 需逐层证明

保存 JSON array 邮件样例包含脚本风格字符串；合法 JSON 字符串/数组本身不会执行。先确认服务器类型校验、序列化、模板引号与客户端 DOM/JS sink，再比较标量、数组、转义文本的语义。没有消费者和实际执行则仅为候选，不能把可提交异常 email 自动称 XSS。

来源：[保存帖1](https://x.com/i/status/1653832026380967936)。


## 带 tab 的脚本方案受 URL 消费者与用户动作约束

保存反向 URL/编码 javascript 候选。逐层区分 URL 参数解码、链接属性、路由解析、点击/导航处理及 CSP；浏览器如何处理控制字符必须在实际消费者确认。字串未被过滤不等于执行，普通重定向与脚本方案导航不能共用一项成功证据。

来源：[保存帖1](https://x.com/i/status/1654201589404688387)。


## 隐藏参数发现后仍需 DOM source 到 sink 链

Arjun/Dalfox 及编码闭合脚本变体只是候选生成/检测角色。原字节不能自动补齐语法；定位 query/hash/response 到 DOM/JS sink 的链，记录解码/编码、浏览器触发、执行和转义反例。DOM 标签与 triaged 状态无实现细节，不证明任一隐藏参数均能 XSS。

来源：[保存帖1](https://x.com/i/status/1654215738268307457)。


## 大小写与 onsubmit 触发必须在原上下文验证

保存 Expedia origCity/UPPER/WAF 报告称 onsubmit 还需点击。分开参数名大小写、HTML 标签/属性解析与 JavaScript 标识符的语义，比较同一路径原形/变体实际反射和提交事件。截图只保存视频封面，没有播放执行；不得把大小写替换推广全 WAF 或忽略需要交互的条件。

来源：[保存帖1](https://x.com/i/status/1654237184184991745)。

保存图片 `1654237184184991745-02.jpg`：Expedia origCity UPPER/WAF title，onsubmit需点击并声称clickjacking，视频封面未播放；eventtrigger/大小写HTML和JS不同、iframe可嵌入不等完整诱导。 本段只使用已保存且实际查看的内容。


## JSONP 编码和消息链不能跳过脚本消费者

保存代码中 callback 和双重编码字串只能说明构造方式。逐层绑定搜索参数、URL 解码、JSONP 输出、实际 script 加载、执行 origin 和消息调用；普通回调标识、安全 callback 校验与未加载脚本作反例。截图没有完整信任检查及浏览器结果，不能把 encoded callback 或 API 名字直接当 XSS/账号接管证明。

来源：[保存帖1](https://x.com/i/status/1655581821940412416)。

保存图片 `1655581821940412416-02.jpg`：oneclickCSRF静态页windowopen/search、2秒timer、doubleencodedJSONPcallback、postMessage JSON arg App.apiCall；另一JScredentialsinclude profile token→updateProfile；图裁切update下半与trust/CORS响应缺失，多边界需分别验证，禁止偷token/更新外部profile。 本段仅使用实际查看的保存原图，不补未保存内容。


## 语法混淆要按 HTML、XML 与 JavaScript 消费者区分

保存 onbeforeinput、数值字符、iframe srcdoc、top/this 转换、XML 的 XHTML 命名空间与 new Function 变体。先定位输入进入 HTML 属性、嵌套文档、XML 渲染或 JavaScript 表达式的真实 sink，记录解码、事件、用户动作、sandbox、CSP 和执行 origin。数字字面量不自动变成函数调用，XML 中 script 与 XXE 不是同一机制；动态函数还依赖 CSP，原串残缺时不修成已复现载荷，不运行样例。

来源：[保存帖1](https://x.com/i/status/1655813481256587264)、[保存帖2](https://x.com/i/status/1655863769065738241)、[保存帖3](https://x.com/i/status/1656445477783748608)、[保存帖4](https://x.com/i/status/1656618666295689217)、[保存帖5](https://x.com/i/status/1657377218920693760)、[保存帖6](https://x.com/i/status/1657476395302551552)、[保存帖7](https://x.com/i/status/1657802019170811904)。

保存图片 `1655813481256587264-02.jpg`：contenteditable onbeforeinput arraymap topalert卡片，无实际event/CSP结果。 本段仅使用实际查看的保存原图，不补未保存内容。


## 管线参数反射只能支持 source 线索

历史 PHP URL、httpx、kxss、blind-XSS 替换管线分别负责候选与回显。保留每阶段原 URL/参数/引号上下文，unfiltered 字符列表不证明进入可执行 HTML/JS sink，Google/Wayback 并不限定当前范围。原盲 XSS 管线存在乱码分隔和替换语法歧义，不静默修正后投递；需自控回调与实际触发，否则不声称存储或盲执行。

来源：[保存帖1](https://x.com/i/status/1655870339619102720)、[保存帖2](https://x.com/i/status/1656149311212900353)。

保存图片 `1655870339619102720-03.jpg`：kxss unfiltered字符列表、querys/CID/video候选，无HTML/JS上下文或执行，不由大字符集合断言XSS。 本段仅使用实际查看的保存原图，不补未保存内容。


## 搜索结果 Markdown 渲染受 CSP 与解析器配置约束

SearchMessages 摘要指出 Markdown 标签进入搜索结果且当时需要关闭 CSP。先确认保存消息与搜索结果渲染是否同一 sink，记录解析器模式、标签处理和实际策略，在本地小夹具比较安全文本与允许标签。历史配置前提不能删除；Markdown 回显不自动执行，XSS 与账号接管需要不同证据。

来源：[保存帖1](https://x.com/i/status/1656034179530866689)。

保存图片 `1656034179530866689-02.jpg`：RocketChat SearchMessages markdownparser插标签，CSPdisabled条件才能exploit摘要；消息正文/searchresultrenderer分别，不直接ATO。 本段仅使用实际查看的保存原图，不补未保存内容。


## 事件拼接变体仍依赖浏览器事件与原 sink

归档以 onbeforeScriptexecute 和拆分字符串称绕 Cloudflare。记录同一请求的过滤结果、实际反射上下文、浏览器版本/事件支持和触发条件，用安全编码与不触发事件作反例。正文 cookie 与截图 domain 执行描述不一致，保留两种声明边界；未拦截或 concat 字串不会自动变成可执行链。

来源：[保存帖1](https://x.com/i/status/1656050953660043265)、[保存帖2](https://x.com/i/status/1656293509954170880)。

保存图片 `1656050953660043265-02.jpg`：locationconcat WAF允许/阻断表声称Cloudflare，onbeforescriptexecute非通用事件，正文cookie图resultdomain不一致，缺真实browser/traffic，拼接JS不等支持触发。 本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1656293509954170880-02.jpg`：同WAFconcat另一SHA缩放卡片，输出domain与cookie文本不一致，noactualevidence。 本段仅使用实际查看的保存原图，不补未保存内容。


## 邮件模板 HTML 注入与浏览器脚本执行分开

姓名/邮箱等字段进入通知邮件可能产生 HTML 注入。追踪表单值、服务端模板转义、邮件源和实际邮件客户端渲染，先用自有收件地址普通格式标记作对照，区分本人触发与其它接收方。截图仅到字段输入，没有邮件或脚本结果；HTML 富文本显示不等于 JavaScript XSS、SMTP 注入或外部收件人受影响，本次不寄送邮件。

来源：[保存帖1](https://x.com/i/status/1656977790816727040)。

保存图片 `1656977790816727040-02.jpg`：H1formfirstname/lastnameHTML→收件email模板，comparewithout/withpayload声明未看到两邮件，h1markup非JS/SMTP头注入，不发他人email。 本段仅使用实际查看的保存原图，不补未保存内容。


## 推荐 bundle 引入的 XSS 前提按具体应用记录

Nextcloud 截图摘要称推荐 Office bundle 安装 richdocumentscode 后出现 RXSS/CSP bypass，并列历史 CVE-2023-31145。保存实际产品/app/bundle 版本、入口、输出 sink、CSP 与用户动作，区分主产品、附加服务和执行 origin。图片只到 setup/摘要，没有注入步骤/执行与 ATO 结果；不能推断所有安装或当前 latest 受影响，本次不部署和取未保存外链全文。

来源：[保存帖1](https://x.com/i/status/1658019706303918081)。

保存图片 `1658019706303918081-02.jpg`：Nextcloud报告RXSS/full CSP bypass，推荐Office bundle安装richdocumentscode应用，截图仅到搭环境与摘要、CVE-2023-31145，具体注入/策略/ATO步骤未见；部署bundle前提明确不能推断全版本Nextcloud均受影响。 本段仅使用实际查看的保存原图，不补未保存内容。


## 退出导航的脚本方案要逐层核验历史前提

ServiceNow logout_redirect.do/sysparm_url 示例包含编码反斜杠与脚本方案，摘要称未认证用户点击可执行并列 SanDiego SP6 之前/CVE-2022-38463。追踪参数解码、URL 规范化、允许 scheme、最终导航消费者、CSP 和用户点击。历史版本描述不是当前部署证明，链接文字不证明浏览器执行，也不由页面脚本能力直接推账号接管；本次不打开载荷。

来源：[保存帖1](https://x.com/i/status/1658140731049930752)。

保存图片 `1658140731049930752-02.jpg`：ServiceNow logout_redirect.do sysparm_url携编码反斜杠/JavaScript协议，报告称未认证用户点击执行与SanDiegoSP6之前、CVE-2022-38463；历史摘要与示例不是当前版本证明或实际浏览器执行，保留解码/导航sink阶段。 本段仅使用实际查看的保存原图，不补未保存内容。


## 文件名和元数据回显必须到达实际渲染 sink

图片文件名、header、cookie 与 metadata 是不同 source，需绑定原字节、解码、存储与最终 HTML/JS 消费者。保存标签嵌套/编码示例没有输出上下文；先以自有无害文本标记和安全转义作对照，再确认事件、origin、CSP。polyglot 或未过滤字串不保证跨场景执行，不运行示例和回调。

来源：[保存帖1](https://x.com/i/status/1658343842943496192)、[保存帖2](https://x.com/i/status/1660665570981978114)。

保存图片 `1658343842943496192-02.jpg`：图片文件名标签与编码载荷卡片，无输出sink/实际浏览器执行。 本段仅使用实际查看的保存原图，不补未保存内容。


## 营销服务 XSS 公告保留用户动作与修复范围

Cisco 保存公告称输入验证不足、用户点击恶意链接、managed service 已更新。需绑定具体历史入口、反射/执行 origin、浏览器及受保护能力，点击条件不能省略。图片没有载荷或执行，公告覆盖的几个营销站不推广为所有产品/当前部署，也不把修复声明当本次复测证明。

来源：[保存帖1](https://x.com/i/status/1658482558739582983)。

保存图片 `1658482558739582983-02.png`：Cisco营销站XSS公告CSCwf04021：不足输入验证、用户点击、managedservice已更新；无具体入口/载荷/执行，三站点声明不可推所有部署。 本段仅使用实际查看的保存原图，不补未保存内容。


## 前端邮箱拒绝与后台盲渲染是不同验证链

正文称先合法邮箱提交、拦截改参数、账号创建后稍后 blind trigger；图片只见 Email Address invalid 和报告标题。追踪服务端校验、保存字段、后台消费者及自控标记时序，分别证明受理、持久和渲染。UI 拒绝不证明服务器拒绝，创建成功也不证明管理员执行或 cookie 获取；不向真实后台投递外部回调。

来源：[保存帖1](https://x.com/i/status/1658506123089944576)。

保存图片 `1658506123089944576-02.png`：EmailAddressInvalid与含标签/脚本风格姓名邮箱字符串，支持前端拒绝输入；正文截获改请求并称稍后blindtrigger，图未见真实存储/回调。 本段仅使用实际查看的保存原图，不补未保存内容。


## 运行时参数 hook 只覆盖实际执行路径

复用已核验相同 SHA 的 Eval Villain 图片说明 URLSearchParams.get 的参数名和 stack 可帮助定位动态读取。记录浏览器路径、输入、hook 时点及调用栈，再追踪到真实 sink 和安全编码反例。被读取 GET 名称不代表所有服务端参数、隐藏路由或 XSS 已成立，未执行页面也不在观测覆盖中。

来源：[保存帖1](https://x.com/i/status/1658606001363329024)。

复用图片 `1658606001363329024-03.jpg`：复用已核验相同 SHA 的 Eval Villain URLSearchParams.get/stack 方法图片，不新增视觉 ledger。


## PDF 中脚本方案链接与网页 XSS 不是同一 sink

LaTeX url/href 脚本方案需确认最终生成 PDF/HTML 哪种输出、链接注释内容、viewer 协议处理和用户点击。使用本地无害标记区分可见文本、可点击和脚本执行，安全拒绝作反例。单个 javascript 字串不证明读者浏览器执行，也不按 LaTeX 宏名推网页 script 能力。

来源：[保存帖1](https://x.com/i/status/1659196654128603136)。


## 依赖 CVE 和客服上传标题缺少真实渲染链

保存 jQuery CVE 风格 option/style 载荷与 Zendesk 上传摘要，却无输入入口、版本/配置、文件名/类型到 sink、浏览器执行。实际登录域与报告主品牌不同，需独立 scope/owner/origin。确认 source→处理→HTML/DOM sink 后才讨论 XSS；通用影响段、CVE 编号及视频封面不能补账号接管。

来源：[保存帖1](https://x.com/i/status/1659212821681561600)、[保存帖2](https://x.com/i/status/1659212920042164231)。

保存图片 `1659212821681561600-02.jpg`：CVE2020-11022标签/optionstyleimgPoC，实际域spiketrap登录页、NotApplicable，无输入source/DOM消费者/执行；依赖CVE≠部署可利用，不抓外链或运行。 本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1659212920042164231-02.jpg`：RedditZendesk requests/new uploadRXSS摘要，NotApplicable，无上传内容类型/文件名sink或邮件实际执行；外域客服需独立scope。 本段仅使用实际查看的保存原图，不补未保存内容。


## 登录后重定向和错误方案 fallback 按消费者分开

Reddit dest 脚本方案摘要要求登录/SSO 后执行；另一图用 ws/wss/resource 使 302 不按通常方式跟随，并给未转义 href 标签。逐层记录参数、解码、scheme 白名单、响应 HTML、浏览器版本、登录阶段和实际执行 origin。Location 本身不是 HTML sink，不同方案被拒绝不保证 body 被渲染，不从登录页或示例推通用绕过。

来源：[保存帖1](https://x.com/i/status/1659213015022178307)、[保存帖2](https://x.com/i/status/1659259012863623168)。

保存图片 `1659213015022178307-02.jpg`：accountsReddit dest=javascript...摘要称登录后执行，SSO前后阶段保存；图片仅登录页，未见JS运行/最终origin，需回调后URLscheme消费者。 本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1659259012863623168-02.jpg`：ws/wss及Firefoxresource方案使302 Location不正常跟随并展示href标签注入示例；是否渲染fallbackbody与execution依赖具体browser/版本/CSP，Location字段本身不是HTMLsink，不据“disable”推广现版。 本段仅使用实际查看的保存原图，不补未保存内容。


## HTML 与 CSS 注入不能从样式允许推脚本执行

wotif 作者称 style/form 可注入但当时无法 XSS。追踪请求字段到实际 HTML 输出、编码、form/CSS 消费者与 CSP，区分内容改写、链接/表单欺骗和 JavaScript 执行。HTML/CSS 接受与 WAF 拦截分别记录，保存摘要没有脚本结果，不默升级为 XSS/账号接管。

来源：[保存帖1](https://x.com/i/status/1659959973693075458)。

保存图片 `1659959973693075458-02.jpg`：wotif正文/标题 /vc/blog/info.php与摘要/vs/blog不同，缓存约1h的最后HTTPGETheaders，作者无法XSS但style/form接受/HttpCookie下位访问可能读前访headers；底部仅TEMP环境几行不见cookie回包，需A/B自控缓存序列，NO真实cookieuse，不宣称WAF通用可绕。 本段仅使用实际查看的保存原图，不补未保存内容。


## 残缺指针事件载荷不能静默修成执行证明

Imperva 帖子中的引号、全角符号与 lavas/cript 片段有歧义，需保存原字符、HTTP 字节及反射上下文。只有 source、解析 sink、onpointerenter 实际事件/CSP 和执行 origin 对齐才能证明；手工补齐字符后不能称原文复现。缺图片/外链按覆盖但不补造浏览器结果，不运行载荷。

来源：[保存帖1](https://x.com/i/status/1659419358421217280)。


## 第三方投票弹窗到帖子存储渲染须绑定 origin

Crowdsignal poll answer→Website Popup→WordPress 新帖保存→打开页面的摘要说明跨产品内容链。记录输入、导出片段、集成方式、服务端清洗、浏览器加载方式与执行 origin，普通标记和安全转义作对照。第三方允许 markup 不证明主站执行，保存图片没有实际弹窗或 cookie 结果，不复制脚本到帖子。

来源：[保存帖1](https://x.com/i/status/1659574983490777097)。

保存图片 `1659574983490777097-02.jpg`：Crowdsignalpoll answer标签→share WebsitePopup→WordPress帖子保存→页面执行叙述，跨产品存储render链清楚但图无实际浏览器输出，scope/origin/Sanitizer区分，cookie示例不执行。 本段仅使用实际查看的保存原图，不补未保存内容。


## SAML 错误输入的 HTML 输出与认证协议分开

Cisco ASA /+CSCOE+/saml/sp/acs?tgname=a POST SAMLResponse 保存示例用标签片段声称 CVE-2020-3580。绑定特定历史部署、表单内容类型、错误解析分支、响应编码、浏览器/CSP 和用户动作，用安全文本与拒绝输出作反例。未认证 POST 不证明可强迫受害浏览器执行，归档没有响应或执行，不运行样例。

来源：[保存帖1](https://x.com/i/status/1660289196420890624)。


## 多组件链逐环证明来源、消费者和浏览器边界

正文给出 postMessage、JSONP、WAF、DOM XSS 与 permissive CORS 到一点击 CSRF 的链名。分别列消息 origin/source 校验、JSONP callback 消费、WAF 与 DOM sink、跨域响应及会话动作，每环需要可控输入、输出与独立反例。链名未提供完整代码/响应，CORS 放行不自动 XSS 或 CSRF，缺一环不能宣称完整攻击链成立。

来源：[保存帖1](https://x.com/i/status/1661024326366416896)。


## HTML 链接注入与脚本执行使用不同结论

输入被输出为可点击的外域锚点说明 HTML 内容控制线索。对照安全文本与转义，追踪反射/保存、输出 context、点击与最终 origin；未有 JavaScript sink 和执行证据不能称 XSS。正文提到 403 也只说明特定请求状态，不证明所有权限边界或 WAF 被绕过。

来源：[保存帖1](https://x.com/i/status/1661113271057784849)。


## 盲渲染标记要连接到具体存储字段和消费者

独立 ID 可关联延迟 blind trigger；Android 设备名也可能由同步/管理后台渲染。记录写入身份、原字节、持久字段、读取消费者、触发时点和实际 origin，用自控普通标记与安全编码反例验证。设备名可改、异步回调或延迟通知不自行证明管理员 JavaScript 执行，不对真实后台投递外部脚本或回调。

来源：[保存帖1](https://x.com/i/status/1661385962994249729)、[保存帖2](https://x.com/i/status/1661816078979457024)。


## 自动化 XSS 结果必须回到真实上下文

扫描器生成的反射 URL、autofocus/focus handler 说明只是候选；需保留单次请求、原始反射、DOM 解析、事件触发、origin 与 CSP，再以安全编码和无事件对照。报告中的 should execute、工具名称或大规模自动化标题没有实际执行证明；字符反射、DOM sink 及保护能力分别核对，不把通知或 logo 视作复现成功。

来源：[保存帖1](https://x.com/i/status/1661790671630467083)、[保存帖2](https://x.com/i/status/1663409589444833283)、[保存帖3](https://x.com/i/status/1663557574451671043)。

保存图片 `1661790671630467083-03.jpg`：scanner reflected stpReq编码打断属性插入autofocus focus handler confirm，URL右端截断；报告说should execute无实际DOM/执行证据。本段仅使用实际查看的保存原图，不补未保存内容。


## 历史错误页 XSS 需确认具体版本和输出分支

正文声称 cPanel CVE-2023-29489 能利用403页。确定历史组件版本、可控字段、错误分支、编码及真实浏览器执行，以安全文本/拒绝输出对照。403 是状态而非漏洞特征，不能推所有403或当前所有部署；标题和存续天数不补实际 payload/响应，本次不发送载荷。

来源：[保存帖1](https://x.com/i/status/1662117863753170945)。


## XSS 标签以持久化和真实浏览器 sink 划分

保存图片列 reflected、stored、DOM-based 三类。分别记录数据是否来自响应/持久存储、是否经客户端解析、实际 sink、事件和执行 origin，以字面输出/安全编码对照；这些维度可能交叠。看到标签、返回输入或脚本样字符串不说明执行成立，封面不补课程内容。

来源：[保存帖1](https://x.com/i/status/1662132441241337859)。

保存图片 `1662132441241337859-03.jpg`：reflected stored DOM三个标签按入参持久化和浏览器sink定位，不互斥或见字符串即XSS。本段仅使用实际查看的保存原图，不补未保存内容。


## 邮箱或图片回调应辨明 HTML 与 JavaScript 消费

引号邮箱/标签和脚本被过滤后换图片源，可帮助列解析与输出检查点。确认邮箱 schema、存储字段、HTML sink、浏览器/代理图片获取及事件/CSP，以无害标记与转义反例比较。图片请求不证明JavaScript执行，亦不能单独证明服务端SSRF；“70%有效”无样本依据，不当普遍成功率，不发真实邮件/盲回调。

来源：[保存帖1](https://x.com/i/status/1662999169194430464)、[保存帖2](https://x.com/i/status/1663187884063735809)。


## Merge Request 分支名渲染依赖具体 rebase 条件

GitLab 报告要求semi-linear或fast-forward merge、需要rebase、访问者不能push source branch、目标分支名含HTML。逐项绑定历史版本、分支数据、错误/提示消费者、编码和执行origin，用自有合法名称/安全转义对照。四项条件不能省略，2019 的 latest Docker示意不是当前受影响版本，不启动容器或在真实仓库写恶意分支名。

来源：[保存帖1](https://x.com/i/status/1663448032765960192)。

保存图片 `1663448032765960192-02.jpg`：GitLab MR storedXSS分支名，semilinear或fastforward且需rebase且viewer不能pushsource四条件，无效图片onerror sink候选；latest2019非当前version，不launchDocker。本段仅使用实际查看的保存原图，不补未保存内容。


## 回调中的 cookie 样字符串不补齐完整执行链

保存Collaborator记录有DNS/HTTP、favicon请求与Referrer中编码的cookie样字段。绑定唯一标记、请求类型/来源、时间与脱敏最小类别，再找真实写入字段、浏览器sink、执行origin和受害身份。回调能证某网络活动，却不单独证明谁执行了JS、哪些cookie可读或账号接管，避免传播真实token/个人ID。

来源：[保存帖1](https://x.com/i/status/1663492615277355008)。

保存图片 `1663492615277355008-02.png`：CollabDNSHTTP favicon GET Referrer含大量URL编码cookie样串，HTTP来源可脱敏关联，非JS源sink或被害身份完整证明，勿复制token/userIDs。本段仅使用实际查看的保存原图，不补未保存内容。


## 注册字段的 blind XSS 要绑定后台消费者

保存正文称在注册 fullname/email comment 写入后出现回调。先确定字段如何保存、在哪个后台页面读取和以何种 HTML/JS 上下文渲染，使用授权无敏感标记绑定请求、账号与时间。回调需区分浏览器、扫描器和服务端请求；延迟两分钟不独立证明管理员执行，未保存的外链步骤不补猜。

来源：[保存帖1](https://x.com/i/status/1664340028976410624)。


## Kroki 语言校验值必须与取值来源一致

保存代码允许 code 或 pre 的语言满足选择条件，却优先取 parent 的语言生成结果属性；合法 child 的语言不能替任意 parent 值背书。沿同一实际值追踪选择器、提取、转换及 HTML 属性输出，使用合成 fixture 对比 parent/child 冲突和一致情况，检查最终转义。保存片段关联历史版本且输出末尾裁切，没有完整浏览器执行证据，不声称当前 GitLab 全部可利用。

来源：[保存帖1](https://x.com/i/status/1664460019855683586)。

保存图片 `1664460019855683586-02.jpg`：Kroki enabled selector接受prelang或code lang，却取parent lang优先，validchild如wavedrom使任意parent lang到resultimg attrs；v15.6.2 code截尾，校验消费者值同一来源，没实执行截图本段仅使用实际查看的保存原图，不补未保存内容。


## SiteMinder Unicode 转义依赖真实解码 sink

保存片段将历史 SiteMinder CVE-2013-5968 与 USERNAME 参数和 Unicode 转义关联。记录历史产品版本、可进入的页面、参数解码及最终 HTML/JS 消费者，对比固定文本与单一编码变化。字符串含事件形式不独立证明执行，CA 入口/访问前提和浏览器结果未完整保存；不扩展成当前任意同名登录页漏洞。

来源：[保存帖1](https://x.com/i/status/1664701417339211776)。

保存图片 `1664701417339211776-02.jpg`：SiteMinderhistoricalCVE2013-5968 smpwservices.fcc SMAUTHREASONUSERNAME Unicodeescapedimg event片段，backendJSdecoder andDOMsink/CAaccess前提 noactualbrowserproof本段仅使用实际查看的保存原图，不补未保存内容。


## 官方反射 XSS 摘要保留执行证据缺口

保存 TikTok 摘要支持 link 参数相关的历史浏览器脚本问题。后续复核须记录输入、响应上下文、解码、最终 sink 与受影响 origin，并区分反射、存储和仅导航行为。私有报告未展开，没有 payload 和完整浏览器结果，不把摘要泛化为全部 link 参数或当前版本都可执行。

来源：[保存帖1](https://x.com/i/status/1664754161517318147)。

保存图片 `1664754161517318147-02.jpg`：TikTok官方摘要link参数浏览器JS能力但私report未展开 无payload/sink，historynotalllinks本段仅使用实际查看的保存原图，不补未保存内容。


## 登录后 dest 必须按最终 URL 消费者校验

保存正文描述 Reddit 登录后 dest 接受 javascript 形式。对合成或授权流程核对参数如何持久、登录前后是否重新解析、允许 scheme 以及最终导航/DOM sink。Location 中出现文本不必然执行 JavaScript，未保存视频不补成浏览器证据；修复复核需覆盖所有消费分支及站内正常导航。

来源：[保存帖1](https://x.com/i/status/1665003319151022081)。

保存图片 `1665003319151022081-02.jpg`：Redditdest javascript afterlogin pop described scheme/websafe regression browserconsumer不自动Locationexec，视频未保存不能称完整execution本段仅使用实际查看的保存原图，不补未保存内容。


## 转换名称字段区分渲染与持久传播

AdWords conversion name 截图包含事件形式和 origin 弹窗。核对名称的保存请求、持久状态、HTML/DOM 输出上下文及其他获准角色的可见性，以无敏感标记绑定源与 sink。单个浏览器截图不独立证明 stored 链和其他用户必然到达；界面中的账户标识不复制到提炼或重放。

来源：[保存帖1](https://x.com/i/status/1665464036903854081)。

保存图片 `1665464036903854081-02.jpg`：AdWordsConversionname含SVGonload片段有origin alert，地址带clidocid应不复制ids；单browser图不能证明保存请求/其他用户reach，stored正文需持久证本段仅使用实际查看的保存原图，不补未保存内容。


## FAQ 分类从 self XSS 到邀请用户要证明可达

保存正文描述自有 FAQ category 中的脚本式内容经编辑/ID 和邀请用户流程到达他人。对自有第二用户检查保存请求、分类权限、持久渲染 sink 和邀请后的实际可见页面，将只在自己浏览器执行与跨角色执行分开。改 URL ID 不自动赋予他人读取权限；奖励邮件仅证明回执，不能填补输入到执行的轨迹，不向第三方发送邀请或复制付款资料。

来源：[保存帖1](https://x.com/i/status/1666638356854505473)。


## 编码载荷与 OOB 请求需绑定相同渲染链

保存 POST fullname 示例把 Base64 字符串交给事件处理器的 eval/atob，正文称简单输入 302 而 OOB 输入 200。编码不改变不可信内容应被转义的边界；记录实际解码、HTML/JS sink、origin/CSP 和浏览器结果。200/302 与回调都不独立证明 XSS，跨站构造、cookie 和最终写入又是 CSRF 的额外前提；不能用全参数 Match & Replace 丢失单变量归因或执行外部脚本。

来源：[保存帖1](https://x.com/i/status/1667101670327693312)。

保存图片 `1667101670327693312-02.jpg`：示例POSTfullname含img event eval(atob(this.id))，短Base64只是alert样例；编码未改变sink信任，没实际response/browser本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1667101670327693312-03.jpg`：同fullname更长编码OOB内容到eval，外部脚本回调与单一字段归因分别，勿执行或全面matchreplace改变所有params本段仅使用实际查看的保存原图，不补未保存内容。


## Credential Management 调用不等于凭据已泄露

保存正文只有 navigator.credentials.get 的赋值示例。记录调用返回的 Promise、浏览器允许条件、credential 类型、用户交互/会话与可读取字段，再检查是否存在真实 XSS sink 和获准账号的可观察结果。API 名称和一行脚本不能证明密码返回、账号接管或所有浏览器行为，不对真实已保存凭据调用此方法。

来源：[保存帖1](https://x.com/i/status/1667214440629166082)。


## cPanel 错误页状态与脚本执行独立判断

保存历史 cPanel CVE-2023-29489 资料指向 webcall 错误输出中的编码输入，另一图可见 400 错误页与 prompt。绑定每个来源的产品版本、请求字节、输出上下文和 origin，比较安全文本及转义；400 不排除错误页中的执行，200 也不自动证明执行。产品未升级的声明和弹窗不能独立证明 cookie 窃取或接管，裁切信息不补全为当前所有部署漏洞。

来源：[保存帖1](https://x.com/i/status/1667222988742115330)、[保存帖2](https://x.com/i/status/1669445831638802433)。

保存图片 `1667222988742115330-02.jpg`：cPanel历史CVE202329489报告cpanelwebcall编码img事件示例声称弹窗，无实际browser截图/version值；autoupdate disabled声明不证current cookie theft本段仅使用实际查看的保存原图，不补未保存内容。

保存图片 `1669445831638802433-02.jpg`：cPanel400InvalidwebcallID含img与prompt1；origin/URL裁切version未示，browserdialog和errorstatus可共存，不从400排除XSS或称tokensteal本段仅使用实际查看的保存原图，不补未保存内容。


## DOM sink 日志继续追源和转义

人工 JS 阅读与 Untrusted Types 日志可帮助定位 document.write/innerHTML/eval。保存输入来源、调用栈、实际传入值、解析上下文及转义/Trusted Types 策略，用授权合成标记比较正常与不可信输入。sink 出现或工具的 Certain 标签不证明可控源与执行，日志可漏动态路径；奖励题名不证明所有手工结果，未安装或注入扩展。

来源：[保存帖1](https://x.com/i/status/1667369853533995011)、[保存帖2](https://x.com/i/status/1667391104499716096)。

保存图片 `1667391104499716096-02.png`：UntrustedTypes logDocumentwrite/innerHTML/eval和示例stackcollapsedinputd0mxss变体；sink日志不证控源escaping/execution，TT监控可观察不保证coverage本段仅使用实际查看的保存原图，不补未保存内容。


## 名称字段跨子域显示检查每个真实 sink

正文提示表单 name 可能在另一子域显示。记录字段的保存/传递链、每个输出 origin、上下文、权限与获准用户可达性，对比安全文本及正确转义。跨子域文本出现不自动脚本执行或同一权限；等级提升通知没有补齐具体源/sink，不从一个字段扩展为所有子域漏洞。

来源：[保存帖1](https://x.com/i/status/1669000678750945282)。


## 订单地址页弹窗保留未知输入与持久性

保存图片展示 billing address 页面和 XSS 文本弹窗，origin 被遮盖。记录可能输入字段、真实写入/响应、输出上下文、会话和第二获准用户是否可达，再判反射/存储/DOM 属性。弹窗不证明所有地址字段或持久跨用户链，图没有 source payload 时不能补造，不抄个人地址信息。

来源：[保存帖1](https://x.com/i/status/1669065668082147341)。

保存图片 `1669065668082147341-02.jpg`：BillingAddressform多字段与XSS弹窗origin遮盖，不知sourcepayload/sink/保存/otheruser，不因alert推stored/全字段本段仅使用实际查看的保存原图，不补未保存内容。


## CSP 信任 CDN 需要匹配真实脚本消费者

正文提出第三方 CDN 上传内容可能落入 CSP 允许范围。记录实际策略指令、资源类型、上传控制、返回 MIME/处置及脚本加载 sink，以自有无敏感样本对照允许/拒绝。某域出现在 connect-src/img-src 不独立授权 script，能上传或下载也不必能执行；奖励题名未提供完整策略与浏览器结果，不认定所有 CDN 都可绕过。

来源：[保存帖1](https://x.com/i/status/1669119476875288577)。


## 重定向参数 JS 改写需要同一导航 sink 对照

保存正文给出 next 从外域导航到 javascript 改写的两部分，图片有 cookie 样文本弹窗。核对实际允许 scheme、URL 规范化、浏览器导航/DOM sink、CSP 与 WAF 规则版本，用授权无敏感标记比较普通与改写形式。属性拼接改变字符串特征不改变脚本信任边界；外跳与执行分别举证，图片裁切的请求/host 不补猜，也不复写 cookie 或宣称通用 Akamai bypass。

来源：[保存帖1](https://x.com/i/status/1669686219620466688)、[保存帖2](https://x.com/i/status/1669686560780853249)。

保存图片 `1669686219620466688-02.png`：nextJavascript改写弹窗中cookie样文本，不复写values，图原始next/host被裁切；编码/property拼接语义浏览器scheme/sink+CSP，Akamairulescurrentunknown nofullreset/ATO本段仅使用实际查看的保存原图，不补未保存内容。


## WAF 片段、事件属性与 XSS 到 CSRF 的链条分步验证

保存正文包含 HTML 实体、字符串拼接、鼠标或焦点事件及反射脚本到 CSRF/BXSS 的主张。可提炼的是输入经历 URL、实体和 JavaScript 解码后进入哪个实际消费者，以及事件所需交互；代码外观、绕过某次过滤和报告接受邮件都不足以推广为任意 WAF 绕过或账号接管。使用无敏感数据的标记，在自有页面保留原始请求、服务端响应、最终 DOM、事件触发和执行 origin 的对应关系。随后对状态变更单独比较浏览器 Cookie 策略、CSRF 校验、请求来源及最终服务器状态。不能读取 HttpOnly Cookie、被 CSP 拒绝或操作仍要求二次验证都是链条反例；不执行保存帖中的 Cookie 外传代码。

来源：[保存帖1](https://x.com/i/status/1670187950087233536)、[保存帖2](https://x.com/i/status/1670406717216006146)、[保存帖3](https://x.com/i/status/1671508993410469890)。


## 测试页 alert 的证据范围限定到该页面与触发上下文

图片实际显示测试站浏览器 alert(1)，但没有完整输入请求、最终 DOM、执行栈及无输入对照；同屏 SQL syntax error 不是独立 SQL 注入证明。若要验证工具候选，保存该 URL 到具体请求参数和解码链，记录实际执行 origin、事件与交互；对照普通文本、不能执行的编码和 CSP 拒绝情况。单个演示站结果不能代表所有目标或零点击，也不能推导 Cookie 可盗取。

保存图证 `1671641370359140352-03.jpg`：测试站浏览器显示 alert(1)，同屏 SQL 错误没有完整请求或对照。

来源：[保存帖1](https://x.com/i/status/1671641370359140352)。


## URL 百分号与 HTML 实体解码链应追到实际导航消费者

两个同文帖分别保存 PNG/JPEG，地址栏可见包含 `%26%2302` 与 `%26%23115` 的 javascript 变形，浏览器弹窗出现，origin 被遮挡。保留原始编码中的数字，不把 02 擅自改成另一个载荷；按真实上下文记录百分号解码、实体解码、控制字符归一化以及最终 href 或导航消费者。最小自有对照包括仅返回文本、正确协议拒绝与执行标记，确认实际执行 origin 和触发交互。图缺完整 DOM 和输入输出 trace，两个图不是两项独立发现；不执行保存载荷或补造全链。

保存图证 `1672758000946233344-02.png`：PNG 可见编码 URL 与浏览器弹窗，完整 DOM 与 origin 被遮挡。

保存图证 `1672850112257708032-02.jpg`：另帖 JPEG 显示同样编码与弹窗，应保留独立文件来源而非算新发现。

来源：[保存帖1](https://x.com/i/status/1672758000946233344)、[保存帖2](https://x.com/i/status/1672850112257708032)。


## 跨产品嵌入内容的存储与渲染应保持同一净化边界

WordPress/Crowdsignal 历史图描述 poll answer 注入属性，share link 嵌入 WordPress post，再 View Results 触发脚本；含 pointer 事件与样式覆盖，不能写成零交互。追踪原始答案、保存值、共享表示、嵌入渲染、实际 frame/origin 和事件触发，确认哪个产品负责净化。自有两端用无害标记对照普通文本、正确属性编码、沙箱 iframe 与被阻止的事件。只有保存输入或预览弹窗不证明所有访客受影响，更不证明 HttpOnly Cookie 可读；图缺完整 DOM 和最终执行日志。

保存图证 `1673368630338174976-02.jpg`：poll 答案到分享链接与 WordPress 嵌入的步骤有事件交互前提，缺最终 DOM。

来源：[保存帖1](https://x.com/i/status/1673368630338174976)。


## User-Agent 进入后台联系表单时须确认实际查看消费者

正文建议在 User-Agent 放置 blind XSS，候选边界是请求元数据进入日志、联系表单或后台页面时是否转成可执行 HTML。自有测试系统使用无敏感标记，记录原始头、存储字段、后台展示位置、执行 origin 和读取身份，分别对照文本渲染、安全编码与执行上下文。提交输入、回连标签或后台看见字符串不能证明浏览器执行；本任务不发送联系表单、外传 Cookie 或通知真实人员。

来源：[保存帖1](https://x.com/i/status/1673388152264986625)。


## 订单 ID 除对象授权外还需检查类型与输出上下文

正文提醒数字形态 order ID 也可能进入 XSS。先确认服务端类型约束、对象权限、错误页和正常展示的位置，再追踪是否从字符串进入 HTML、属性、URL 或 JavaScript 消费者。自有合成对象以无害标记比较合法数字、被拒绝类型与正确编码，核对 final DOM 和执行 origin；对象 ID 存在、错误信息反射或页面显示文本不证明执行。访问控制与输出编码是独立守卫，不为测试创建真实订单或执行帖中载荷。

来源：[保存帖1](https://x.com/i/status/1674017299022626818)。


## innerHTML 与未编码反射需要补齐不可信源和解析上下文

`innerHTML` 或 kxss 所标记的未编码字符提供审计方向，漏洞需要不可信输入实际抵达该消费者并进入可执行上下文。自有页面以无害标记对照文本节点、安全编码、动态 HTML 与事件属性，保存输入、响应、DOM、执行 origin 及所需交互。静态可信模板、纯文本反射、被 CSP 拒绝或脚本节点未执行都是反例；发现一个 sink 或候选参数不能证明所有反射都是 XSS。

来源：[保存帖1](https://x.com/i/status/1674226929367408642)、[保存帖2](https://x.com/i/status/1676229910195494914)。


## 应用商店评价进入第三方后台时要分开内容与资产授权

正文建议评价内容可能进入客服或第三方页面。需要知道实际提交者、存储字段、后台渲染者、origin 和净化规则，才能判定跨产品内容是否成为脚本；商店端纯文本展示不决定另一端的解析。自有双端样本对照安全文本、正确编码和无害执行标记，记录真正查看身份。用户能写评价不自动授权测试商店、供应商或工作人员，本任务没有提交评价、联系人员或建立外传回调。

来源：[保存帖1](https://x.com/i/status/1674436560987787264)。


## 双引号 JavaScript 上下文的运算符效果依赖完整语法

图片在 script 内展示双引号字符串输入与百分号/空串/alert 运算组合。应先还原字符串前后字符、转义、注释和解析位置，再判断运算符是否在合法表达式中求值；不是任意百分号都能绕过 WAF。自有片段对照被正确转义、保持字符串及进入表达式的无害标记，记录语法错误与执行点。截图缺完整响应、过滤规则与执行 trace，不能泛化为所有 JS 上下文成功。

来源：[保存帖1](https://x.com/i/status/1674480266646003723)。

保存图证 `1674480266646003723-02.png`：script 内 var ref 的双引号字符串注入位置，没有实际完整响应、转义和运行结果。

保存图证 `1674480266646003723-03.jpg`：空串/百分号/alert 运算组合依赖完整表达式语法和前后字符，未保存 WAF 对照或执行轨迹。


## Blind XSS 通知与脚本到权限链要逐层绑定证据

正文含联系表单、请求参数与外部脚本的 blind XSS 想法，还建议读取 Cookie/localStorage；图片只有部分报告状态和通知。先记录不可信源、持久化、真正后台查看器、DOM 解析、执行 origin 与关联标记，区分提交成功、网络回连和浏览器执行。自有样本对照安全编码、脚本节点不执行、事件被 CSP 拒绝及无敏感执行标记；HttpOnly Cookie 不可读，存储值也未必是可用认证令牌。App 产品与支持供应商属于独立授权资产，添加普通来源标记仅用于取证，不代表权限升级。后续状态变更和接管需自有身份独立证明；不提交工单、评价、外传脚本或真实通知。

来源：[保存帖1](https://x.com/i/status/1674705919588933640)、[保存帖2](https://x.com/i/status/1674714568516329472)、[保存帖3](https://x.com/i/status/1674791022436696067)、[保存帖4](https://x.com/i/status/1675065706067681282)、[保存帖5](https://x.com/i/status/1676603085580378114)。

保存图证 `1676603085580378114-02.jpg`：XSS.Report 邮件通知标题及截断标识，未见回调详情、来源页面、执行身份或关联请求，第三方支持工单需以具体执行来源核对而非通知图推断权限。


## 隐藏参数和相近路由仍需分别确认输出消费者

一图显示 product 参数的事件输入产生弹窗，另一图显示隐藏 tab 参数到关闭 script 的构造。Arjun 或源码搜索只能定位候选，不证明每个同名参数、路由或页面共享同一渲染规则。自有样本保留端点、方法、参数编码、响应片段、DOM、CSP、origin 和事件触发，比较拒绝值与安全输出。一个弹窗不能扩为十个独立漏洞或全部页面；图中的其他标签页也不是其漏洞证据。

来源：[保存帖1](https://x.com/i/status/1674892261585297408)、[保存帖2](https://x.com/i/status/1675506875498913792)。

保存图证 `1674892261585297408-02.jpg`：product 参数中事件输入产生浏览器弹窗，origin 遮挡；另一 phpinfo 标签页不是同一漏洞，不能从一例推成十例。

保存图证 `1675506875498913792-02.png`：隐藏 tab 参数进入关闭 script 的例子与浏览器弹窗，origin 遮挡，没有 Arjun 发现日志或完整 DOM trace。


## JSON 端点的路由和 MIME 变化决定实际解析器

正文描述给 JSON 路由追加 `.html` 或改变参数，及 JSON 内容被以 text/html 提供。要证明同一不可信字段如何经过路由、Content-Type、nosniff 和浏览器消费者成为 HTML，而不是简单看到 JSON 中有特殊字符。自有样本比较 JSON 解析、作为文本下载与明确 HTML 解析，记录请求协商头、响应头、DOM 和 origin。正确 application/json、附件下载、安全编码或只改为错误页都是反例；没有真实响应时不能称为所有 JSON 端点的 XSS。

来源：[保存帖1](https://x.com/i/status/1675275589023051776)、[保存帖2](https://x.com/i/status/1675485220517167105)。


## Citrix logout 的执行图不补齐响应拆分与 WAF 对照

几张不同 SHA 的图在 logout/post_logout_redirect_uri 中有多重换行及事件 HTML，浏览器出现弹窗。可保留实际图中的执行现象，但产品版本、原始响应、Header/Body 边界、Akamai 是否启用及过滤正反例均缺失。自有模拟处理器比较安全编码、明确拒绝与无害执行标记，分别验证 HTML 注入、脚本执行和 CRLF 头边界。标题中的 CVE、bypass 或相同图的多份转载不能推为当前全版本漏洞、任意 WAF 绕过或接管。

来源：[保存帖1](https://x.com/i/status/1675363957899444224)、[保存帖2](https://x.com/i/status/1675844131971629056)、[保存帖3](https://x.com/i/status/1675929579846770698)、[保存帖4](https://x.com/i/status/1676663587752878081)。

保存图证 `1675363957899444224-02.png`：Citrix logout 多重换行输入与浏览器弹窗，页面也显示类似头的文本，但无原始 Header/Body 边界、版本或权限证明。

保存图证 `1675844131971629056-02.jpg`：第一个正文 ID 的 Citrix logout 弹窗，域遮挡且完整响应缺失。

保存图证 `1675929579846770698-02.jpg`：第二个重复正文 ID 的另一 SHA 图片显示同类弹窗，不增加独立漏洞数。

保存图证 `1676663587752878081-02.jpg`：Citrix OAuth logout post_logout_redirect_uri 中换行与 body onload 组合出现浏览器 alert；未见原始响应头、Akamai 拦截对照、产品版本或修复状态，不能称所有 WAF 可绕过。


## 自建登录页面和 HTML 表单不证明跨身份脚本链

图片展示 login.php、admin.php、index.html 文件与登录表单，正文部分截断。需区分研究者自己托管内容、同源受保护应用、真正不可信输入、渲染身份与表单动作接收者。自有两会话以无害标记核对源到 DOM 及安全编码，只有自己页面执行或自己提交表单不能推成受害者接管。截断步骤与未保存令牌消费者不补造，不托管钓鱼页或使用真实凭据。

来源：[保存帖1](https://x.com/i/status/1675586568092876800)。

保存图证 `1675586568092876800-02.jpg`：自建 login.php/admin.php/index.html 与表单代码，无跨身份输入/渲染/令牌消费链；正文截断不补造。


## 持久 returnUrl 在合法 nonce 脚本内仍要检查字符串上下文

保存图和文字涉及商户离线交易/GraphQL 创建流程，returnUrl 跨两个站点保存后进入带 nonce 的合法 script。nonce 保护脚本来源，不能自动净化该脚本内部的不可信字符串；仍需追踪创建权限、持久值、最终 JavaScript 位置、实际 origin 和受影响身份。另一图描述跳转取消异步操作，window.stop 也会取消 fetch，非法 scheme 的行为仅是该情境观测。自有环境对照安全编码、合法导航、被拒绝 scheme 与无害异步标记，记录导航/网络事件及恢复结果。保存材料不证明全浏览器稳定、支付权限或完整账号接管，不创建真实交易或请求令牌。

来源：[保存帖1](https://x.com/i/status/1675874536766464005)。

保存图证 `1675874536766464005-02.png`：商户离线交易/GraphQL returnUrl 保存后跨站进入带 nonce 的合法 script 字符串；nonce 不净化字符串，未见完整 ATO。

保存图证 `1675874536766464005-03.png`：导航取消异步操作示例，window.stop 同样取消 fetch；非法 scheme 的效果只对当前情境，不保证各浏览器完整最终链。


## HTML 注释终结与表达式求值不能凭载荷外观判定

正文用 `--!>` 与 img/onerror 组合称为注释 XSS，但事件表达式只有 `(document.domain)`，没有弹窗函数。注释状态结束取决于完整 HTML、序列化与浏览器解析；表达式求值也不自动产生可见结果。自有片段比较仍在注释内、安全编码、被 CSP 拒绝及无敏感执行标记，记录最终 DOM、事件、origin 与错误。不能把正文缺失的函数补造为原载荷，归档没有实际执行图或响应。

来源：[保存帖1](https://x.com/i/status/1676114366054408192)。


## 移动 UA 和 UTF 编码变化要追踪真实响应与字符解释

正文指出移动 User-Agent 与 UTF-16 等编码可能改变用户名的展示路径。审计应查明端点是否按 UA 选模板、响应声明与实际字节是否一致、解码次数、缓存 Vary 和最终输出上下文。自有固定字符串比较桌面/移动模板、正确字符集和错误解码，保存响应字节、头与 DOM。UA 变化本身不导致 XSS，输入类型、CSP 或安全编码仍可拒绝；没有实际执行 trace 不宣称所有移动页面可利用。

来源：[保存帖1](https://x.com/i/status/1676323997468983296)。


## 报错文本变成 h1 不等于脚本已执行

同一组图中普通 h1 被当成文本、script 从 DOM 消失，非标准元素/属性包装则让 h1 进入 DOM 并出现大标题。可提炼的是错误页对不可信内容的编码、过滤和 HTML 解析不一致，需从响应字节追到最终 DOM 与事件消费者。自有片段对照纯文本、安全编码、错误模板和无害执行标记，记录 origin/CSP。大标题证明该例 HTML 解释变化，不能自动推为 XSS 或 SQL 到接管；没有保存脚本执行与权限变化，图的不同格式不是新发现。

来源：[保存帖1](https://x.com/i/status/1676627917101744128)、[保存帖2](https://x.com/i/status/1676805042400051200)、[保存帖3](https://x.com/i/status/1677106541235691523)。

保存图证 `1676627917101744128-02.png`：引号与 RandomString 进入 MySQL 报错的 URL/页面示例，未显示 SQL 查询或布尔对照；错误回显可作为输入路径线索。

保存图证 `1676627917101744128-03.png`：h1 HTML 字符串在 MySQL 报错中按文本显示，不能仅因反射认定浏览器将其作为标签或执行。

保存图证 `1676627917101744128-04.png`：script 输入在 URL 存在但报错/DOM 不见脚本，提示过滤或不同错误输出；无执行证明，不把 URL 中出现脚本当成 XSS。

保存图证 `1676627917101744128-05.png`：非标准 00 元素及 foo 属性组合使报错输出中 h1 进入 DOM、页面出现大标题；证明这一图的 HTML 解析变化，未显示事件脚本执行或实际 SQL 数据读取。

保存图证 `1676805042400051200-02.jpg`：另一篇同例截图：MySQL 错误回显 RandomString，说明线索不等于稳定 SQL 控制或 XSS。

保存图证 `1676805042400051200-03.jpg`：同例低分辨率另一 SHA 的 h1 DOM/大标题结果，只支持 HTML 解析差异，不新增独立漏洞或脚本执行证据。

保存图证 `1676805042400051200-04.jpg`：同报错示例 script 在地址栏存在但未进入 DOM，未显示脚本执行；过滤行为需结合原始响应。

保存图证 `1676805042400051200-05.jpg`：同报错 h1 输入按文字输出，与非标准元素包装造成 DOM 标题的对照有用，但截图不是 SQL 权限或脚本执行证明。


## 可信域错误页的文本欺骗应与 HTML 和脚本注入区分

cryptography.io 报告描述在路径后追加文字，错误页以可信域上下文显示“网站迁移”的内容。这是不可信文本进入可信错误信息的内容欺骗方向，未显示标签解析或脚本执行。自有错误处理器比较固定安全错误、转义后的路径和可控提示，记录实际用户可见文本及上下文；只作为引用路径或清楚标明原输入可能减轻影响。不能称已验证 XSS，也不把历史 No Rating 外推为当前统一标准。

来源：[保存帖1](https://x.com/i/status/1676645401300967433)。

保存图证 `1676645401300967433-02.jpg`：cryptography.io 错误路径被显示到可信域页面，可插入“网站迁移”文本的报告描述，Resolved No Rating；仅文本/内容欺骗，未显示 HTML 或脚本执行，不能将文字反射当作 XSS。


## Self XSS 的升级必须新增跨身份输入或浏览器请求链

正文提出从 self XSS 延伸到账号破坏或 CSRF 到 reflected XSS，部分内容截断。应明确为何别的身份会带入攻击者输入、浏览器 Cookie/Origin/CSRF 守卫是否允许、在哪个真正渲染器执行以及受保护状态是否改变。自有两会话用合成对象比较只影响作者、正确 CSRF 拒绝和无害跨身份标记，保留请求来源与读回结果。口号、恶意链接或用户自行粘贴不补齐升级，不破坏账号、发联系消息或执行归档载荷。

来源：[保存帖1](https://x.com/i/status/1676667845206331409)、[保存帖2](https://x.com/i/status/1676674737513156616)。


## 手机号与邮箱字段的格式约束不代替输出编码

正文给出手机号、邮箱等输入位置启发。字段名称与传统格式不决定它最终进入 HTML、属性、URL 或脚本；服务端实际类型验证与每个输出消费者才决定风险。自有合成资料以普通值、安全编码和拒绝值对照正常/错误/后台展示，记录最终 DOM、事件与 origin。特殊字符能提交或字段被反射不保证 XSS，也不支持“哪个字段命中更多”的统计主张，不操作真实用户资料。

来源：[保存帖1](https://x.com/i/status/1677080219914477569)。


## 模板命中与对应 Citrix 弹窗要保留同一请求关联

两组 Nuclei 摘要和 Citrix 浏览器图可支持提出同一端点的解析/执行问题，但摘要到浏览器之间缺完整标记、时间和请求响应关系。自有隔离例用唯一无害标记把模板匹配、响应、DOM、事件和 origin 对应，比较纯文本命中、安全拒绝与真实执行。弹窗本身不能补齐全部模板准确率、原始头拆分、产品版本或权限升级；相同页面的不同图不是额外独立漏洞。

来源：[保存帖1](https://x.com/i/status/1675491176416268289)、[保存帖2](https://x.com/i/status/1676135893768232960)。

保存图证 `1675491176416268289-03.jpg`：另一 Citrix logout 事件输入弹窗，未展示原始拆分、CSP/版本、Cookie 或权限链。

保存图证 `1676135893768232960-02.jpg`：另一 Citrix 弹窗图片，不同字节/格式不能当成新漏洞。


## WordPress 嵌入消息的 origin 与实际接收端一起核对

保存案例指出恶意博客须被嵌入，wp-embed 的 postMessage origin 检查存在问题，并明确 Safari 与 Chrome/Firefox 表现不同。应确定消息发送者、iframe/父页关系、接收器对 origin 与消息字段的验证，再追踪接收数据是否进入实际危险 sink。用无害标记和同源/异源对照保留浏览器版本、嵌入配置及最终 DOM；仅见 receiveEmbedMessage 的部分 secret 字段代码不能推断任意网站或所有浏览器都可 XSS。

来源：[保存帖1](https://x.com/i/status/1677333436153905152)。

保存图证 `1677333436153905152-02.jpg`：wp-embed 自动发现的 postMessage origin 检查缺陷摘要，报告限定 Safari、Chrome/Firefox 不成立且须攻击者帖子被嵌入；只见 receiveEmbedMessage/e.data/secret 前几行，没有最终 sink/完整消息及版本，不外推所有浏览器。


## POST 和文档 base 的候选要落到具体浏览器消费者

POST 参数也可经表单或脚本发送；参数不在地址栏不构成安全保证。HTML base 影响相对 URL 的解析，应核对首个有效 base、CSP base-uri、资源类型及绝对 URL，不能宣称所有链接都会改变。另一保存帖拼接 SVG 跳转和 PHP 接收片段，但引号及 URL 编码可使示例失效；独立 SVG 文档与 img 引用的脚本环境也不同。用无害标记证明源到 sink、真实浏览器上下文和交互要求；接收器能写日志不证明浏览器曾成功发送，更不能用 Cookie 字样推导 HttpOnly 绕过或账号接管。

来源：[保存帖1](https://x.com/i/status/1677443988754685953)、[保存帖2](https://x.com/i/status/1677792171653472257)、[保存帖3](https://x.com/i/status/1679542341554561050)。


## Rails SVG 净化候选保留显式标签配置和嵌套解码条件

保存材料涉及 ActionView sanitize 在允许 SVG/use 标签或指定 tags 的条件下处理嵌套 data/Base64 SVG 与事件属性。应记录净化器版本、允许列表、输入类型、输出 DOM 与浏览器的解码/重解析行为，比较默认配置和显式放行配置的无害样例。仅见历史 CVE 名称或候选字符串不能证明所有 Rails 默认配置均受影响，也不能把多层编码当作已经执行；缺当前运行证据时标为历史候选。

来源：[保存帖1](https://x.com/i/status/1678404377575391235)。

保存图证 `1678404377575391235-02.jpg`：ActionView sanitize 历史 SVG/use→data:image/svg+xml;base64 内嵌 image onerror，须全局 allowed_tags 或 helper tags 显式允许 svg/use；配置与二次 SVG 消费是前提，未见完整执行版本，不能套用默认所有 Rails。


## 反射位置和 pointer 交互决定 XSS 最小复现

保存 8x8 oem 候选在 img 属性中使用 onpointermove，多个请求位置不代表每处都能执行。分别标注输入字段、属性引号与编码、输出位置、用户鼠标动作和浏览器版本，以无害标记证明对应 sink。需要指针交互的路径不应写成零点击；没有 Cookie 消费者和权限状态证据，不推导账号接管。

来源：[保存帖1](https://x.com/i/status/1678464756309524481)。

保存图证 `1678464756309524481-02.jpg`：8x8 oem 参数反射至多个 body 位置，其中 img 属性进入 onpointermove，步骤要求鼠标移动；没有原始完整响应/CSP/执行记录，非零交互，不证明 HttpOnly Cookie 可读或接管。


## Cisco 客户端页面 XSS 保留配置和点击条件

历史 ASA/FTD 材料涉及特定 AnyConnect/WebVPN 服务配置以及用户点击。记录产品实际版本、入口启用状态、攻击链接、输入输出上下文与用户动作，比较同一配置下无害标记的浏览器结果。统计图、版本区间或 CVE 列表不提供每台设备的运行证据；缺映射和执行链时不能宣称当前所有设备均可 XSS、无交互或 VPN 权限已被取得。

来源：[保存帖1](https://x.com/i/status/1679731870077186050)。

保存图证 `1679731870077186050-02.jpg`：Cisco ASA/FTD CVE-2020-3580 历史摘要：不可信输入进 web services、用户须点击链接，只影响特定 AnyConnect/WebVPN 配置；1805/25/+108% 提交数量和表中星号不等于当前全版本漏洞，未见原始执行。


## XSS 回连里的存储数据仍需源、身份和权限消费者

图片显示一条回连 URI、Cookie/Referer/UA/Origin 字段、遮挡的 session/localStorage/DOM 与邮件数据标签。保留唯一标记和输入位置，证明是哪一浏览器身份、哪个 origin 和 sink 产生回连，再区分脚本可读值、HttpOnly Cookie、演示数据和服务端 API 数据。遮挡 JSON 与标题不能证明两百员工数据、全用户接口或接管；没有令牌类型、消费者和受保护状态时只记录可见回连范围，不导出 PII、不使用令牌或重放真实会话。

来源：[保存帖1](https://x.com/i/status/1679947591117570050)。

保存图证 `1679947591117570050-02.jpg`：XSS.Report 仪表盘一条遮挡页面 URI 和时间，只是回调摘要，不独立证明 200 员工或权限。

保存图证 `1679947591117570050-03.jpg`：Sent Mail 中大量脱敏用户 JSON 的字段类别 username/email/id/resource_uri 等；没有原始 API 请求、执行身份、对象授权或完整数量，不能推所有员工或当前账号权限，不复制 PII。

保存图证 `1679947591117570050-04.jpg`：XSS.Report URI/Cookies/Referer/Origin 及 UA 摘要，敏感值遮挡；执行/网络来源需关联输入标记，Cookie 字段出现不证明 HttpOnly 可读或有可复用会话。

保存图证 `1679947591117570050-05.jpg`：回调记录 Session Storage/Local Storage/DOM 大面积遮挡，时间和设备信息仅摘要，token类型、消费者、权限未知，未证完整 takeover。


## CSP 静态评价与实际浏览器注入结果分别保存

已保存 CSP evaluator 图示含 self、允许站点/img 范围，以及 object-src/TrustedTypes 提示。先核对真实响应 HTTP/meta 策略、多个策略交集、报告模式及加载上下文，再用无害标记验证实际 sink 和浏览器结果。评价器告警是配置线索，不证明存在注入源、sink、当前旁路或允许域可控；历史图不能代表目标当前策略，不安装插件或生成额外绕过。

来源：[保存帖1](https://x.com/i/status/1680779835810131968)。

保存图证 `1680779835810131968-02.jpg`：复用已实际看过的 CSP evaluator 图片内容；静态允许来源及 object-src/TrustedTypes 提示不证明真实注入源或浏览器绕过。


## MathML 与 HTML 混合候选需证明净化后的变异过程

保存字符串将 MathML/mtext、table/mglyph/style、CDATA 和 img/title 的实体/制表符交错。边界是净化器首次解析、序列化输出与浏览器重新构建 DOM 之间的差异；保存输入、实际净化输出、浏览器 DOM、版本和无害执行标记，分别比较单次文本反射与多次解析。缺运行证据时仅是 mutation 候选，重复状态不能证明通用 XSS 或 WAF 绕过，也不执行保存载荷。

来源：[保存帖1](https://x.com/i/status/1680814300804558854)。


## Popover 的 hidden 与 meta 路径依赖属性和目标选择

保存四图展示 button popovertarget、popover/onbeforetoggle 与 hidden input/meta/重复 id。核对是否能插入或结束属性、事件策略、DOM 顺序与目标解析，以及浏览器支持和用户点击，比较唯一 id、重复 id 和安全转义的无害样例。代码存在不等于已执行；不同元素的有效性需分别证明，不能扩大为所有 hidden/meta 上下文、所有浏览器或零点击 XSS，不运行归档事件载荷。

来源：[保存帖1](https://x.com/i/status/1681028502584442880)。

保存图证 `1681028502584442880-02.jpg`：Popover XSS示例button popovertarget指向id，目标含popover/onbeforetoggle；要用户点击、浏览器支持和实际属性插入位置。不是已证明所有hidden/meta上下文，没运行截图或当前版本，不执行载荷。

保存图证 `1681028502584442880-03.jpg`：meta属性中注入popover/id newsletter/onbeforetoggle，既有按钮和div重复id；需属性可注入、DOM顺序/目标解析、浏览器支持与点击，不是所有meta自动执行。

保存图证 `1681028502584442880-04.jpg`：hidden input与既有div重复id x，button popovertarget x；新增popover/event属性与先后顺序决定选择，无运行日志不推零点击或普遍浏览器。

保存图证 `1681028502584442880-05.jpg`：按钮显式指向带popover/event的hidden input，需要可控属性与用户点击/浏览器实现，静态代码不等于已执行。


## RDoc 生成 HTML 的文本转义和链接协议分别检查

保存 RDoc 段落输入生成未转义 script、链接输入生成 javascript href，以及 gen_url 根据 scheme/图像后缀拼接 img/a 的部分源码。追踪文档来源、生成器版本、允许协议、属性/文本转义与最终浏览器消费者，分别比较普通文本、链接协议和图像路径。text.sub 去前缀不等于 HTML 上下文编码，HTML 转义也不能代替协议允许列表。未保存真实运行和完整源码时不推当前全部 RDoc 版本、任意文档或浏览器都可执行。

来源：[保存帖1](https://x.com/i/status/1681243093688004609)、[保存帖2](https://x.com/i/status/1681243237326131205)、[保存帖3](https://x.com/i/status/1681243449004273666)。

保存图证 `1681243093688004609-02.jpg`：RDoc段落格式例子生成HTML含未转义script，历史CVE-2013-0256/Informative；输入文档→生成HTML→浏览器是链，缺具体版本/真实运行/权限消费者，不运行rdoc/载荷。

保存图证 `1681243237326131205-02.jpg`：RDoc链接javascript scheme进入a href，保存输入与生成HTML；运营者明言政策改变不把预处理Ruby代码当漏洞，Informative。协议允许与HTML转义不同，点击/生成器版本/真实使用信任边界需证；此项目历史政策不可推广。

保存图证 `1681243449004273666-02.jpg`：RDoc 6.3.0 gen_url部分源码：parse_url得到scheme/url/id，根据http/https/link与图像后缀分支拼img或a，text.sub移除前缀但不等于上下文转义；截图下半截缺失，需完整消费者，不能据此断言所有版本或执行结果。


## JSON 错误字段与部署测试资源追到实际 HTML 输出

Keycloak 注册错误将 JSON 字段名带入 ClientRepresentation 错误页面，另图显示 vendor/curl 测试路径的返回字段与弹窗。分别保留原始方法/输入、响应字节与类型、部署版本、输出上下文和实际浏览器 origin，以无害标记比较纯文本与被解析内容。curl 输出本身不执行 JavaScript，错误 JSON 或弹窗也不能补齐当前版本、令牌权限和接管链；未保存的字段及步骤不补造，不执行归档载荷。

来源：[保存帖1](https://x.com/i/status/1681706774728933387)、[保存帖2](https://x.com/i/status/1681947334366707712)。

保存图证 `1681706774728933387-02.png`：Keycloak clients-registration/default错误Unrecognized field ClientRepresentation显示IMG破图并浏览器弹窗；JSON字段名→错误HTML→浏览器是候选，需原始POST/响应Content-Type/版本和sink关联，curl输出本身不执行JS，弹窗不能补成接管。

保存图证 `1681947334366707712-03.jpg`：vendor/curl/tests/server/php-curl-test/post路径浏览器显示request_method GET/key空/mime_content_type ERROR与弹窗，测试资源被部署可成为输入输出面；缺原始请求/字段/响应类型，不把Library版本标题直接当全部应用XSS。


## 异步 XSS 入口与回连保留身份和等待窗口

保存建议使用可回看邮箱及反馈/评论入口，另有 ezXSS 工具介绍。应在已有授权流程中记录输入、消费页面/邮件、唯一无害标记、等待窗口与回连 origin/身份，再追踪实际 sink；订阅、收到营销邮件或工具在线不证明后台执行。Cookie 可见不说明 HttpOnly 或令牌权限，也不能为了声称接管复用真实会话。本任务不订阅、发送消息、部署回调或补抓链接。

来源：[保存帖1](https://x.com/i/status/1682671051996528641)、[保存帖2](https://x.com/i/status/1683334859576737792)。


## 邮件 HTML 插入与脚本执行及可信界面误导分别证明

保存正文称邮件内容 HTML injection，图只有报告列表。应保留输入字段、服务端邮件生成/净化、客户端渲染环境、可控制的结构与用户动作；脚本禁用、文本转义、链接限制等会改变实际消费者。标题和 Medium 标签不提供邮件字节或执行证据，不直接升级为 XSS/接管，也不发送邮件、生成钓鱼界面或访问未保存链接。

来源：[保存帖1](https://x.com/i/status/1684295037805268995)。


## Rails inline SVG 的 CSP 覆盖取决于响应类型

保存图说明 send_file/send_data 以 image/svg+xml 且 inline 返回时，预期 default-src 'none' 却只对 HTML 应用 CSP，上传 SVG 的活跃内容可能执行。比较同一自控文件在 HTML、SVG、attachment、inline 和实际响应头下的浏览器行为，明确源、脚本上下文及用户打开条件；ActiveStorage 的 content_types_allowed_inline 过滤是不同路径的反例，不能将自定义 controller 缺口套给所有上传。图无附件源码。

来源：[保存帖1](https://x.com/i/status/1684851397899268096)。

已审阅原图 `1684851397899268096-02.jpg`：Rails send_file/send_data inline image/svg+xml时只给HTML施加CSP，恶意SVG可执行；default-src none预期与实际header需比较；图注ActiveStorage content_types_allowed_inline过滤构成不同路径反例，CVE2022-22577，无附件源码。


## Rails helper 属性名称与属性值分别验证

FormTagHelper/TagHelper 的 options 将 data-*、aria-* 或其它非 boolean 属性 hash 的 key 变成属性名；对 value escape 不能补足对标签名/属性名允许字符的限制。跟踪用户输入是否真的控制这些名称与 helper 调用，比较生成的原始 HTML 和浏览器 DOM，确认事件边界及执行条件。保存 check_box_tag 示意只覆盖名称路径，底部未保存的后续例子不补造。

来源：[保存帖1](https://x.com/i/status/1684851532762935296)。

已审阅原图 `1684851532762935296-02.jpg`：Rails FormTagHelper/TagHelper对标签名/属性名允许字符检查不足；options中data-*、aria-*、非boolean属性hashkey受控例check_box_tag；属性值escape不能代替名称验证，CVE2022-27777，底部后文裁切。


## redirect_to 控制字符丢失 Location 后的点击 XSS

保存报告针对 Rails 7.0.4.3，说明 URL 控制字符导致下游移除 Location，但响应 HTML 的 href 仍保留可控 URI，javascript URI 可在点击时触发；可见字符范围为 %01–%08、%0b、%0c、%0e–%1f。对照原始 Location、HTML href、状态码和浏览器点击行为，识别移除发生在哪层；这不是仅依据 3xx 的开放重定向，也不能省略点击前提。图中完整 PoC 下部未保存。

来源：[保存帖1](https://x.com/i/status/1684851817833017344)。

已审阅原图 `1684851817833017344-02.jpg`：Rails7.0.4.3 redirect_to URL控制字符令下游移除Location，HTML href仍受控可用javascript URI，需点击；图列%01-%08/%0b/%0c/%0e-%1f，不能归成普通开放重定向或无点击；CVE2023-28362，PoC裁切。


## ASP.NET Content-Type 与请求解码的存储 XSS 线索

正文仅自述 2017 年 Request Validation 可经 Content-Type 绕过而存储 XSS，未保存外链全文。将请求编码、验证时输入、实际解码后值、存储以及最终 HTML/脚本输出上下文分别比较；通过框架请求验证不等输出安全。保持特定历史案例，不补具体字符集、payload 或当前版本受影响范围。

来源：[保存帖1](https://x.com/i/status/1685002125103837185)。


## target blank 链接 XSS 保留浏览器点击类型

正文声称 Firefox 中 target=_blank anchor 可借类似 Chrome 中键/修饰键点击方式访问 document.cookie，外链全文未保存。核对浏览器版本、href 协议/编码、普通与中键及修饰键点击、新窗上下文与 cookie 可访问性；target=_blank 本身不证明 XSS，HttpOnly 与同源仍约束 cookie。没有保存具体 payload 不补齐；用户交互和最终 origin 必须进入报告前提。

来源：[保存帖1](https://x.com/i/status/1686363933060235264)。


## 编码src反射与实际HTML执行上下文（2023保存案例）

地址栏src参数编码body onload→浏览器alert1，域蓝遮/响应未见；可见执行线索但需实际DOM、解码阶段/点击/源归因，不把任何编码通用绕WAF。

图片证据：`1688111129665445889-02.png`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1688111129665445889)。


## 不同分辨率弹窗截图的解码证据边界（2023保存案例）

另一分辨率截图显示 src 参数内编码 body onload 后弹出 alert(1)。可观察页面执行，但缺少原始响应与解码位置，不能将编码片段视为通用绕过；应区分查询解码、HTML 插入上下文和实际受害者可达性。

图片证据：`1688369947959762944-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1688369947959762944)。


## 数字实体和URL百分号解码的先后顺序（2023保存案例）

被遮挡目标的 url 参数包含百分号编码的数字实体与 javascript URI，截图弹窗内容被涂抹。提示多阶段解码/URI 导航候选，需保存每阶段值和插入上下文，不能推断所有实体都会被解码或所有 javascript 导航均被允许。

图片证据：`1688714658281070592-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1688714658281070592)。


## Seller重定向命名参数的XSS与导航分别确认：脚本上下文（2023保存案例）

TikTok Seller 报告摘要说明 hack_redirect_now 参数用户输入未适当 HTML 转义/输出编码导致 XSS，标题并列 DOM XSS/open redirect，截图没有重定向请求链。分别确认 DOM sink 与最终导航，参数名称不能证明开放重定向；历史 Resolved/$1000不外推当前版本。

图片证据：`1688837831626731520-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1688837831626731520)。


## 邮箱格式校验报错之前的脚本执行（2023保存案例）

登录邮箱栏包含类数组/引号JS片段，界面显示请输入有效邮箱同时弹XSS。客户端格式错误不阻止先发生的不安全渲染，需定位原始响应/JS解码/sink，并证明其他用户可达，弹窗不能说明账户接管。

图片证据：`1689157812470038528-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689157812470038528)。


## 登录错误弹窗不足以从Self XSS升级ATO（2023保存案例）

登录错误页面弹alert1，目标及输入被裁切。证明某页面执行但缺少受害者投递/身份边界和ATO操作，Self XSS标题升级不能代替跨用户触发与实际账户控制证据。

图片证据：`1689190357597069312-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689190357597069312)。


## Unicode转义需要真正的JSON或JS解码阶段（2023保存案例）

Unicode XSS图给出字面\u003e/\u003c img onerror片段，无触发截图。JavaScript/JSON转义解码不同于HTML字面文本；先确定实际解码阶段和sink，再比较编码/原字符与安全文本输出，CSP/事件策略可能阻止执行。

图片证据：`1689525340534976512-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689525340534976512)。


## 同源脚本CSP不能补救原样HTML输出（2023保存案例）

PHP挑战代码设CSP script-src self;object-src none后原样echo GET input。代码证明不安全HTML输出与同源脚本许可组合，尚无已运行解法；需分别定位输出上下文与允许脚本源、MIME/nosniff/可控同源资源，CSP不是输出编码替代。

图片证据：`1689720271375093760-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689720271375093760)。


## 图像服务报告标题与SSRF初稿证据分离：脚本上下文（2023保存案例）

image.hackerone.live报告标题RXSS via url，但可读初稿写full read SSRF并提供外部URL，后续附件仅可见Multiple Choices上部。区分服务端发请求/回传内容与浏览器执行；标题修订不证明两机制均成立，未展示OAST归因、内网/云凭据或XSS完整触发。

图片证据：`1690000327850766336-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1690000327850766336)。


## 反射端点作为同源脚本的CSP挑战条件（2023保存案例）

挑战解法把同一个PHP反射端点作为script src，第二请求input=alert(1)//响应脚本正文且弹1。CSP self容许同源资源，原始echo造成可控脚本文本；只在浏览器接受响应MIME且无有效nosniff等条件成立，截图未展示响应头，不泛化所有同源资源。

同帖附PHP代码再次显示CSP self/objectnone+原样echo输入，没有额外独立漏洞；与执行图合并保留同源脚本响应条件。

图片证据：`1690434606628061184-02.jpg`、`1690434606628061184-04.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1690434606628061184)。


## document.cookie弹窗不证明HttpOnly凭据可窃取（2023保存案例）

搜索字段内闭合标签script片段，弹窗显示document.cookie中多种追踪/会话命名cookie。只能证明该上下文脚本执行及非HttpOnly可读值，字段名sid不证明可用认证凭据，HttpOnly不在document.cookie中；目标/路径被遮挡，不复制cookie值或外推ATO。

图片证据：`1690454558470758400-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1690454558470758400)。


## Blind XSS标识文本与数字过滤不是通用规则

正文将含xss或数字的回连域均称错误，这只是可能遇到关键词过滤的假设。分别固定HTML上下文、脚本标签、域名和随机无敏感标记比较，保留受控回连时间/唯一关联ID及可达性。回连缺失还可能来自CSP、队列未处理或网络失败；任意无数字域名不能保证触发，工具域名也不构成当前授权。

来源：[保存帖1](https://x.com/i/status/1687751364879982592)。


## JavaScript闭合片段应先按真实语法位置验证

保存片段含单引号、分号后未配对右括号，不能在脱离上下文时作为有效载荷。先定位原始字符串/调用参数/注释边界，用无害标记在本地解析相同代码；比较输出编码前后和浏览器控制台语法错误。仅复制一个闭合串或声称能弹窗不能证明该输入位于可执行上下文。

来源：[保存帖1](https://x.com/i/status/1687762340517695488)。


## 隐藏参数的标签替换需要实际解析和可达性

正文称script被拦后换svg/onerror/onload成功，但保存图片只是报告列表。应先确认参数进入哪个HTML/JS上下文，再比较无害标记、标签转义和事件处理；SVG、img及事件名称的浏览器行为不同，CSP、净化器和受害者不可达均会阻止利用。不能仅凭标签替换命名为通用WAF绕过。

来源：[保存帖1](https://x.com/i/status/1688191455502684160)。


## POST反射XSS的跨用户投递不能省略请求条件

方法改写、CSRF和JSON伪装只是可能的投递候选，各依赖服务端接受方法、Content-Type/CORS、浏览器可发请求和受害者凭据策略。先记录无害反射上下文，再在自有账号比较原POST与候选投递请求是否命中同一sink。仅在Repeater可发送或客户端改请求不足以证明浏览器可跨站触发。

来源：[保存帖1](https://x.com/i/status/1689350862517448708)。


## Liferay名称存储与注册末步反射是两条sink

正文称姓名在他人访问profile时存储XSS，以及注册末步URL反射XSS。分别记录保存行为/查看者角色与URL来源/输出位置，使用无害唯一标记比较净化、编码与受害者可达性。CMS名称、简单payload或不需要绕过不证明所有版本受影响，只有自己编辑视图触发可能仍是Self XSS。

来源：[保存帖1](https://x.com/i/status/1690045769796005895)。


## 保存图证0187-1-xss：条件与证明边界

搜索字段闭合标签后弹document.cookie，目标被涂抹。只能证明当前HTML/脚本上下文执行以及非HttpOnly可见值；cookie字段名不是有效登录凭据证明，需跨用户投递与真实认证效果对照，不复制值。 可用原图：`1690602330721337344-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1690602330721337344)。


## 保存图证0187-2-xss：条件与证明边界

被遮挡站点的移动弹窗显示/xss/，没有原始邮箱请求或输出上下文。与正文邮箱编码SVG片段关联仅提示输入解码/HTML渲染，不能说明所有email参数都可XSS、绕过哪个过滤器或取得他人会话。 可用原图：`1690652587660341248-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1690652587660341248)。


## 保存图证0187-22-xss：条件与证明边界

另一尺寸被遮挡移动弹窗/xss/，仅执行效果，无原始邮箱值或sink。与g2文本相近，合并编码上下文条件但分别绑定图片来源。 可用原图：`1690844462027505664-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1690844462027505664)。


## 保存图证0187-42-xss：条件与证明边界

测试站attributeHtml参数body/onload片段先赋onerror再引用未定义x，弹框显示Uncaught ReferenceError:x is not defined。利用错误处理器触发不同于正常alert参数；仅测试站执行，需原始响应/sink/CSP和WAF具体规则/配置基线，不能证明所有Cloudflare绕过。 可用原图：`1691133404467589120-02.png`。

来源：[保存帖1](https://x.com/i/status/1691133404467589120)。


## 保存图证0187-45-xss：条件与证明边界

SnapNewsroom历史报告：国家/语言search q未净化，可插入带style绝对定位的外部链接并诱导点击。HTML改页面/钓鱼不等于脚本执行，需编码前后DOM/实际导航对照与用户交互条件，不能从CodeInjection标签推RCE或XSS。 可用原图：`1691147896195051520-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1691147896195051520)。


## 保存图证0187-58-xss：条件与证明边界

Yelp报告摘要：guvo cookie回显进window.ySitRepParams和window.yelp.guv，部分未转义；后台cookie解析可将guvo夹入yelpmainpaastacanary，后者可由?canary=值设置。组合才使他人持久触发，后续自述登录键盘记录/绑定攻击者Google账号，图无完整绑定结果。分别验证设置cookie来源、解析差异、JS编码、受害者触发与账号绑定确认，不外传凭据。 可用原图：`1691434700211093504-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1691434700211093504)。


## 保存图证0187-75-xss：条件与证明边界

TikTok Seller hack_redirect_now输入校验不足可能响应拆分，摘要并列反射XSS/cookie与开放重定向；时间线Duplicate#2007093、评级变更/后续reopen，下部截断。分别需要原始响应CRLF边界、浏览器HTML执行和最终Location解析，不能从摘要推三条证据均已完备，历史状态非当前影响。 可用原图：`1691615894437527680-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1691615894437527680)。


## 保存图证0187-107-xss：条件与证明边界

Octagon挑战地址name含script src同源/blog/wp-json/wp/v2/users/1...，弹[object Object]。提示同源JSONP/script可执行端点需核对callback/实际响应MIME/nosniff和CSP策略，不可从WordPress市占推49%互联网0day，截图URL尾部截断无完整callback。 可用原图：`1692205274965176548-02.jpg`。

挑战9.php设置CSP script-src self;object-src none，原样echo head Hello拼GET name。HTML注入和同源脚本许可需要组合，修补输出编码/可执行callback各有边界，站点有WordPress子域不一定同origin；不请求挑战站。 可用原图：`1692205274965176548-04.jpg`。

来源：[保存帖1](https://x.com/i/status/1692205274965176548)。


## 保存图证0187-113-xss：条件与证明边界

转发图完整列复制自己cookie→logout→恢复cookie→刷新并称sessionhijacking，另列email编码SVG弹窗。前者检查服务端注销/缓存显示而未证明窃取路径，后者依赖解码及HTMLsink；分别保存自有账号服务端认证探测和无害输入对照，不混成一条ATO链。 可用原图：`1692407286784987267-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1692407286784987267)。


## 搜索和邮箱输入的上下文探针：从弹窗到真实执行位置（0187）

保存帖展示关闭 script 或邮箱引号编码加 SVG onload 的探针，邮箱例含 `%27`、反斜线、`%22`、`%3E%3Csvg`。先定位返回 HTML、属性、脚本字符串或 DOM 插入点，保留原始编码和实际解码层；用自有账号及无敏感数据的标记比较原值与单一变体，记录最终 DOM 和执行源。弹窗只能证明当次上下文中的执行，不能自动扩展为持久化、其他用户受影响或账号接管；示例中的 cookie 访问也不等于已读取 HttpOnly cookie。

来源：[保存帖1](https://x.com/i/status/1690602330721337344)、[保存帖2](https://x.com/i/status/1690652587660341248)、[保存帖3](https://x.com/i/status/1690844462027505664)、[保存帖4](https://x.com/i/status/1691001545880485889)、[保存帖5](https://x.com/i/status/1691734739789693380)、[保存帖6](https://x.com/i/status/1692407286784987267)。


## 搜索结果 HTML 注入与脚本执行分开证明（0187）

Snap Newsroom 的 q 输入图证展示链接和样式注入，可影响页面呈现并产生仿冒风险。先记录输出上下文、浏览器 DOM、链接目的地与用户交互；能插入 HTML 不代表能执行脚本，不能自动称为 XSS 或账号接管。后续影响需独立证明同源信任、可触达用户和实际操作。

来源：[保存帖1](https://x.com/i/status/1691147896195051520)。


## Cookie 派生查询数据进入 DOM 的数据流追踪（0187）

Yelp 图证把 guvo Cookie、canary 派生查询、解析和 JavaScript 插入点串联起来。保留输入可控性、解码/序列化过程和真实 sink，证明最小无敏感标记在对应用户上下文执行。标题中的键盘记录、Google 账号绑定和账号接管属于后续独立环节，保存的片段不足以补造完整链条。

来源：[保存帖1](https://x.com/i/status/1691434700211093504)。


## 延迟 Blind XSS 的归因和输入预算（0187）

公司字段中的探针在数日后触发时，使用每入口唯一的无敏感标记关联提交时间、字段、账号和触发页面；时间接近不能单独归因。调查异步审核、后台渲染和再次访问等路径，记录脱敏上下文。批量把探针放入全部字段可能改变真实业务或造成消息扩散，先界定范围、字段副作用和最小提交量。

来源：[保存帖1](https://x.com/i/status/1691469392746266624)、[保存帖2](https://x.com/i/status/1692577279598117330)。


## 外部 iframe 与 DOM 数据源的正确分类（0187）

`<iframe src=//0e.vc>` 可加载外部内容，但子框架的脚本通常不在父页面源执行；需另证 sandbox、源关系或消息信任问题。`document.URL`、documentURI、baseURI、location.search、cookie 和 referrer 通常是数据源，保存帖将其统称 sinks 需纠正：追踪它们是否进入 innerHTML、脚本执行等危险汇，再判断编码和校验。`URLUnencoded` 与写成 `location.\search` 的示例不能当通用浏览器 API。

来源：[保存帖1](https://x.com/i/status/1691786081807556981)、[保存帖2](https://x.com/i/status/1691804504109482142)。


## CSP self 与同源 WordPress JSONP 的具体条件（0187）

保存代码含原样输出 name 的 HTML 注入点及 `script-src self`、`object-src none`；另一图引用同源 `/blog` WordPress users 路由与被裁切的回调地址。先证明注入可控，再核对同源脚本端点是否返回可执行 JavaScript、回调限制、MIME/nosniff 与当前策略。位于另一子域的 WordPress 通常不被 self 自动包含；“49% 网站 0day”是未经覆盖证明的泛化，不能采纳。

来源：[保存帖1](https://x.com/i/status/1692205274965176548)。


## 保存图证0188-30-xss：机制与验证条件

image.hackerone.live url参数RXSS复测图含Safari弹窗及Accept差异：Safari无image/avif,image/webp，Chrome/Firefox包含。应比较内容协商/MIME与同一原始输入，弹窗微缩和请求缺失不补造payload/通用浏览器漏洞。 可用原图：`1694235854250881054-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1694235854250881054)。


## 保存图证0188-40-xss：机制与验证条件

URL参数带引号/脚本片段写入iframe src及JavaScript脚本src字符串，代码左/右裁切，实际执行未展示。iframe消息处理中frameId/height字符串处理另为候选，不能由邻近代码补造postMessage链或AdminATO。 可用原图：`1694416544363655563-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1694416544363655563)。


## 保存图证0188-42-xss：机制与验证条件

图列换行/percent编码javascript scheme和属性拼接top[ale+rt]、document/domain。编码行to%0Ap与解码示例需按URL层是否移除控制字符核对；javascript:在a/iframe/embed的支持、CSP/点击/源约束各不同，字符串拼接只躲词法匹配并非通用执行。 可用原图：`1694491963217834088-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1694491963217834088)。


## 保存图证0188-103-xss：机制与验证条件

PHP代码htmlentities token后去\n和\0但留\r，把input同时放Content-Disposition filename及JS TOKEN字符串。URL%0D与弹窗说明候选：PHP拒绝含CR头导致attachment不再发出、未做JS上下文编码；需原始header/warning/版本对照，非所有PHP头通用移除。 可用原图：`1695837147226427654-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1695837147226427654)。


## 保存图证0188-123-xss：机制与验证条件

inDrive促销按driver ID查询，POST api/spreadsheet/promocodes可把activationDate存脚本，同ID后查询触发。日期类型schema与输出编码双边界，图例id4仅示意，使用自有driver记录；底部截图微缩不能补全执行结果。 可用原图：`1696160858190016860-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1696160858190016860)。


## 保存图证0188-153-xss：机制与验证条件

无括号XSS利用window.name字符串和instanceof对象自定义Symbol.hasInstance:eval，SVGonload及iframe name传值。需要JS解析/ES6、eval策略、实际window.name跨源导航行为与iframe策略；历史跨源保持并非所有当前浏览器，名字包含括号也不违反仅反射位置过滤，代码不等执行图。 可用原图：`1696508859827814578-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1696508859827814578)。


## POST 转 GET 后仍需证实受害者可达和执行（0188）

记录同一入口的 POST body 与 GET query 解析差异，保留 CSRF/认证、响应类型和真实输出上下文。Burp 改方法成功仅提示另一个可接受入口；还需浏览器能构造请求、数据反射到可执行位置及其他用户可触达条件。GET 返回 200、P3/Triaged 或自己输入后弹窗都不能直接证明可投递的反射 XSS。

来源：[保存帖1](https://x.com/i/status/1694023690885779647)。


## 同一输入进 Header 与 JavaScript 的跨上下文失配（0188）

PHP 片段先 html 实体处理，再去 LF/NUL，留 CR，把值同时放 Content-Disposition filename 与 JS 字符串。含 CR 的 header 可能被该版本拒绝，下载保护因此未发出，而 JS 字符串仍缺专用编码，图展示浏览器弹窗。核对原始响应、PHP warning、头是否实际缺失和脚本上下文，使用固定版本正反例；不能把任意 %0D 概括为所有 PHP 头可移除。

来源：[保存帖1](https://x.com/i/status/1695837147226427654)。


## 多参数标记扫描的归因与副作用（0188）

所谓 SPRAY 把多个 URL 参数改为 XSS 标记，适合先定位反射位置，但同时改值会破坏业务并失去归因。使用每参数独立无害标记，保留正常基线、实际输出上下文和单参数复测，避开会话/签名/支付等敏感参数；只见页面变化或某次错误不能证明 JavaScript 执行。

来源：[保存帖1](https://x.com/i/status/1696164646124765560)。


## text/xml 与命名空间脚本的实际解析条件（0188）

保存片段用 x:script 配 `http://w3.org/1999/xhtml`，这与标准 XHTML 命名空间 `http://www.w3.org/1999/xhtml` 不同；示例可能因此不能按预期识别。Content-Type text/xml、命名空间和浏览器 XML 渲染模式需一起核对，另有 CSP、nosniff、下载及插入上下文。Cookie 表达式的存在不证明能读 HttpOnly 数据，片段无运行证据不当成功案例。

来源：[保存帖1](https://x.com/i/status/1696217010789835091)。


## instanceof 调用钩子与 window.name 数据流（0188）

图用 `window.name instanceof {[Symbol.hasInstance]:eval}` 触发指定函数，绕过反射位置的括号词法过滤，另一输入 iframe name 则提供待执行字符串。需要 ES6 语义、实际 name 在导航中保留、frame/sandbox/CSP 允许及目标事件上下文；当浏览器跨源重置 name 或禁用 eval 时是反例。无括号不是无需代码执行条件，也不能补造所有浏览器可用。

来源：[保存帖1](https://x.com/i/status/1696508859827814578)。


## 正文提炼0189：一行回显扫描只生成 XSS 候选

gf xss、source=过滤、qsreplace与curl/grep链只找候选和回显，缺乏浏览器上下文、输出编码、DOM sink及CSP执行证据。源例混入弯引号、错误while语法、单横线长选项和ANSI文本，原样执行不可靠；全参数替换混合归因，source=过滤漏掉其他入口，-insecure会隐藏TLS失败。提炼为范围内单参数、固定会话的原始/无害标记对照，保留请求响应和重定向、再确认浏览器真实执行；Vulnerable打印不作为结果。

来源：[保存帖1](https://x.com/i/status/1697178119273107721)、[保存帖2](https://x.com/i/status/1697533443285143664)。


## 正文提炼0189：反引号的调用语义取决于 JavaScript 上下文

当括号字符被过滤，反引号可能在已有可调用标识符后构成 tagged template 调用，但不是在所有HTML/属性/字符串中通用的括号替代。先定位输出上下文与可控字节、编码/解码和CSP，用无害标记分别比较普通文本、模板字面量、实际调用；报告被resolved后又triaged不证明具体绕过可复现。

来源：[保存帖1](https://x.com/i/status/1697217333503086762)。


## 正文提炼0189：盲 XSS 的提交、渲染与回连三段

正文脚本src绝对HTTP/协议相对域与$.getScript分别依赖混合内容策略、CSP、网络许可、jQuery及当前页面上下文。联系/支持/聊天输入只提供延后渲染假设；每次授权自有提交用唯一无敏感标记，绑定输入、后台渲染来源、回连时间/调用栈，排除安全扫描器和本人浏览器。不要收集真实cookies/页面敏感数据或批量投递；没有回连不证明安全，回连也不自动管理员权限或ATO。

来源：[保存帖1](https://x.com/i/status/1697613954191593863)、[保存帖2](https://x.com/i/status/1697662715857170929)。


## 正文提炼0189：参数名与值经过不同反射路径

保存帖称value里的script被拦而param[script字符串]进JS页面源码；必须区分框架括号参数解析/数组对象化、未知key序列化与JS字符串/对象键编码。一次仅换key或value，跟踪到原始响应与最终JS/DOM sink，保留过滤层与CSP；在源码看到输入不等于执行。两处XSS到fullATO还需每段角色、受害动作和受保护操作，来源未提供时不补猜。

来源：[保存帖1](https://x.com/i/status/1698760907336106240)。


## 正文提炼0189：POST JSON 改 GET 只是可投递性假设

保存正文只到把POST参数移到GET，后续XSS/ATO未保存。比较两方法的认证、CSRF、参数优先级、Content-Type、页面模板与是否真被接受，再定位响应/DOM sink；JSON作为数据返回与HTML执行上下文不同。method转换成功不证明CSTI、XSS或账号接管，状态改变的GET须单独安全评估，未保存chain不补猜。

来源：[保存帖1](https://x.com/i/status/1699519999587623033)。


## 正文提炼0189：noscript 片段须锁定解析时的脚本状态

保存片段在noscript里的p title嵌闭合noscript与img字符串；是否成为真实img/onerror取决于scripting enabled、净化上下文、namespace、序列化/重解析及库版本。比较输入、净化DOM、最终DOM与无害执行标记，保持相同browser/CSP设置；不是WordPress专属或每个站点都有效。缺失版本/实际sink时保留候选，不把payload文本当成功。

来源：[保存帖1](https://x.com/i/status/1699985852028579870)。


## 正文提炼0189：javascript 链接需要执行与交互证据

正文明确无需交互payload被滤，改a href=javascript:alert()后需Click。可控HTML和危险scheme出现在DOM仅是候选，真实无害点击、CSP/浏览器行为和输出编码决定执行；禁止将点击触发写成0interaction。URL应按解析后的scheme白名单过滤，属性文本和真实节点分别记录。

来源：[保存帖1](https://x.com/i/status/1700713126482633167)。


## 保存图证0189-15-xss：机制与验证条件

Mars 2037234 可见 POST /_post/usuario_actualizar.php 表单，nombre、apellido、email、rut、idProvincia、idLocalidad、optin 等字段，apellido 值为 script alert；截图在第 12 行截断，enctype 右边被截，不能补猜整个 PoC。分别验证跨站带凭据写入与后来页面的存储/渲染执行，apellido 插入须依 HTML/属性/JS 上下文确认，单个表单字符串和报告标题不证明执行或接管。 可用原图：`1696931057457942820-02.jpg`（保存帖 1696931057457942820）。

来源：[保存帖1](https://x.com/i/status/1696931057457942820)。


## 保存图证0189-17-xss：机制与验证条件

Mars 2061049：show 参数被描述为反射到 HTML，目标 wikichat.fr；图仅见问题描述和风险矢量，利用链接下方被截断。HTML 注入需证明元素结构变化，XSS 还需安全标记真实执行；须分上下文输出编码和脚本执行能力。报告正文 CVSS 5.4 与侧栏 Medium(4.3) 不一致，采用实际影响而非任选评分。 可用原图：`1696931326975529322-02.jpg`（保存帖 1696931326975529322）。

来源：[保存帖1](https://x.com/i/status/1696931326975529322)。


## 保存图证0189-26-xss：机制与验证条件

nuclei v2.9.8/模板 v9.6.2 单目标单模板 admin-ajax-xss 命中，/wp-admin/admin-ajax.php?action=zip_search&nonce=…&zip=10001&callback=jQuery… 后接编码 img onerror 字符串。只见扫描日志未见响应或执行；需固定 nonce/session/plugin版本与单参数受控比较，辨别 JSONP callback JavaScript 上下文与 zip/s 搜索反射，不能由模板名或 Medium label 判定真实 XSS。模板协议弃用警告也需保留版本限制。 可用原图：`1697132150959579253-02.jpg`（保存帖 1697132150959579253）。

来源：[保存帖1](https://x.com/i/status/1697132150959579253)。


## 保存图证0189-45-xss：机制与验证条件

高清一行式图 gf xss|grep source=|qsreplace|curl|grep 标 Vulnerable；使用弯引号、while read host do ; do、不正确单横线长选项、未正确ANSI转义。提炼归档候选→单参数变换→保留请求响应链的思路，修正 shell 语法和目标范围、curl TLS及超时；只grep script confirm回显无法确认浏览器上下文/编码/CSP/执行，qsreplace全参数会混合归因，grepsource=漏其他参数，不能复制即认定有效扫描。 可用原图：`1697533443285143664-02.jpg`（保存帖 1697533443285143664）。

来源：[保存帖1](https://x.com/i/status/1697533443285143664)。


## 保存图证0189-51-xss：机制与验证条件

Access Request 表单 Name、Email、Request Comments textarea name=comments，150字符 UI 限制，作者标注 Vulnerable Parameter；可提炼低频申请/后台审核为潜在延后渲染入口，服务端长度约束与存储/输出链须分别确认。截图无回连或脚本执行，不能由作者注释认定 Critical/管理员cookies泄漏；使用授权唯一无敏感标记跟踪提交→后台渲染，不收集真实cookies、不大量提交或触达无关支持人员。 可用原图：`1697662598601212240-03.jpg`（保存帖 1697662598601212240）。

来源：[保存帖1](https://x.com/i/status/1697662598601212240)。


## 保存图证0189-116-xss：机制与验证条件

Proton Mail已净化邮件再将svg替换proton-svg：purify.ts querySelectorAll/svg、ownerDocument.createElement、replaceChild，省略子节点搬移代码用[… ]明确未显示。可提炼净化之后 DOM namespace/序列化变换仍是安全边界，不能把DOMPurify整体当普遍失效；锁定净化库/后处理版本，比较净化树、替换后树、序列化及最终iframe重解析，保证再次净化最终上下文。70m用户保存时估计不是本案可影响证明。 可用原图：`1699778387491913756-02.png`（保存帖 1699778387491913756）。

Proton parser differential图：SVG style里a alt属性嵌闭合style与img onerror字符串；SVG上下文属性中的字符串不被当img事件，改外层proton-svg后重解析到HTML，style进入rawtext而字符串能结束style露出img。关键是namespace变化与再次解析，两阶段DOM比较，未发生重解析/保持namespace或最终上下文重净化为反例；无具体版本不泛化所有DOMPurify。 可用原图：`1699778387491913756-03.jpg`（保存帖 1699778387491913756）。

Proton两封邮件链摘要：第一封净化绕过+application/javascript附件+img引用附件+CSS泄漏blob URL三字符片段，客户端将附件转blob并iframe渲染；重构URL后第二封净化绕过+script src指blob，受害者收到并打开再执行。记录附件MIME/源origin、blob生命周期/同源、CSS网络策略、iframe sandbox和CSP实际许可及两次开信交互；图未显示CSS选择器/sandbox逃逸/CSP文本，不补具体payload。用隔离假数据/自有邮箱无害标记验证，不窃真实解密邮件/签名发送。两封需打开不能称0click。 可用原图：`1699778387491913756-04.png`（保存帖 1699778387491913756）。

来源：[保存帖1](https://x.com/i/status/1699778387491913756)。


## 保存图证0189-120-xss：机制与验证条件

rails-ujs CVE2023-23913/2125679摘要：用户将含data-method、data-remote或data-disable-with的HTML剪贴板粘入contenteditable，库的行为委托可能引DOMXSS；图写影响>=5.1.0、<5.1.0不受影响，修复6.1.7.3/7.0.4.3，应按相应分支修复版本收紧，不写所有>=5.1永远脆弱。复用文本编辑粘贴净化与库data-*自动增强之间的边界，需实际rails-ujs加载/版本、浏览器剪贴板权限与粘贴交互、事件触发/CSP和真实sink，不自动无交互执行或ATO。原1767802外链不补读。 可用原图：`1699920631968739680-02.jpg`（保存帖 1699920631968739680）。

来源：[保存帖1](https://x.com/i/status/1699920631968739680)。


## 保存图证0189-130-xss：机制与验证条件

Yelp2089042摘要：biz.yelp.com未验证商户邮箱反射入提示产生XSS，cookie bridge先将入口带到其他用户，再第二次利用泄漏HttpOnly session cookies，称business与regular账号可能受影响。提炼自有邮箱输入→提示渲染→跨子域桥接两阶段鉴权链，但图没有bridge端点或具体泄漏实现，不补猜绕HttpOnly读取：HttpOnly防document.cookie，需桥接服务端/响应读写缺陷的独立证据。验证两自有账号origin、cookie Domain/Path、桥接绑定、每段受保护请求及所需用户动作，不窃真实会话或宣称0click。 可用原图：`1700056520988467337-02.jpg`（保存帖 1700056520988467337）。

来源：[保存帖1](https://x.com/i/status/1700056520988467337)。


## 保存图证0189-138-xss：机制与验证条件

DoD2045549 CVE2023-24488保存复现URL /oauth/idp/logout?post_logout_redirect_uri=%0d%0a%0d%0a<script>alert(document.domain)</script>，另有cookie stealing陈述但无真实回显或cookies。可提炼URL解码→退出重定向响应头/正文边界→浏览器HTML执行三段检查，保留原始响应状态/Location/CRLF字节与MIME，区分仅反射、CRLF注入、真正split和XSS；只用隔离原点无害标记，不声称真实cookie或所有Citrix版本，产品版本该图空白，CVE不能替代部署匹配。 可用原图：`1700207507158045164-02.jpg`（保存帖 1700207507158045164）。

来源：[保存帖1](https://x.com/i/status/1700207507158045164)。


## 保存图证0189-156-xss：机制与验证条件

DevTools Elements中facetfilter按钮aria-label含字面<h1>String，子span却有真正<h1 aria-level=2>String</h1>节点，隐藏span末尾也含h1字串。图可支持相同输入在属性/文本与innerHTML上下文不同的HTML结构注入候选，不能凭h1节点证明JavaScript/CSP绕过或a href javascript点击执行；比较输入来源、服务端原始响应、DOM构建sink和标签编码，仅无害结构标记即可。 可用原图：`1700713126482633167-02.jpg`（保存帖 1700713126482633167）。

DevTools 同filter DOM里实际a href="javascript:"、文本Click，aria-label和隐藏span也含原始字串；空javascript URL未含执行代码。可提炼从允许HTML结构继续测试URL scheme净化，并分真实a节点与属性文本/无事件状态、用户点击/CSP限制。图没有对话框/点击结果，不证明XSS。 可用原图：`1700713126482633167-03.jpg`（保存帖 1700713126482633167）。

另一图真实a href="javascript:alert()"、Click，按钮aria-label有同字符串；这是危险scheme进入DOM的证据，仍需授权无害点击和浏览器CSP/执行结果。不把DOM截图称0click或已执行，不用cookie payload，修复需按URL解析后的scheme白名单及安全DOM构建而非只拦script标签。 可用原图：`1700713126482633167-04.jpg`（保存帖 1700713126482633167）。

来源：[保存帖1](https://x.com/i/status/1700713126482633167)。


## 保存正文0190：载荷语法与解码层不能由文本省略

onmouseover示例正文confirm(document.cookie)x连续写法与图中%0d换行边界不同；Unicode标识符、tagged template与javascript%3a/throw%2520示例分别依赖HTML/JS解析和一层/两层解码。先还原准确字节、source→sink与CSP，再用自有页面标记观察；鼠标事件需要交互，javascript导航与HTTP Location重定向不是同一执行路径。读取cookie受HttpOnly约束，不由一串载荷证明WAF绕过或接管。

来源：[保存帖1](https://x.com/i/status/1702384889025405156)、[保存帖2](https://x.com/i/status/1704211684007759898)、[保存帖3](https://x.com/i/status/1704433016427229581)。


## 保存正文0190：User-Agent盲注的延迟渲染证据

请求头可能进入运营日志/工单/后台后延迟渲染，Burp全局替换范围容易扩及第三方。只对获准目标的受控请求加唯一非敏感标记，关联具体请求与后续受控浏览器执行；服务器/OOB pingback不必然代表浏览器脚本执行。日志保留、运营角色与CSP决定前提，设置预算/失效时点，不无边界注入全部浏览流量。

来源：[保存帖1](https://x.com/i/status/1702749402249699782)。


## 保存图证0190-16-xss：机制与验证条件

保存原图文件：1701200820027404327-02.jpg。

BlindXSS dork GUI列intitle/inurl contactus、feedback、message、support、submit、supportcenter、request/report/attachments/requesttype等入口词。可复用延迟后台渲染输入面与范围内索引发现；关键词/表单存在不证明XSS，只在授权自有提交用唯一无敏感标记关联后端渲染/回连并排除扫描器，不批量联系支持/上传payload。

来源：[保存帖1](https://x.com/i/status/1701200820027404327)。


## 保存图证0190-20-xss：机制与验证条件

保存原图文件：1701219470726041966-02.jpg。

TVA1362995 /siteminderagent/forms/smpwservices.fcc?USERNAME=…&SMAUTHREASON=7，PoC链接以字面\u003c/\u0020等转义形式呈现img/onerror/confirm(document.domain)，附件xss.png未在图中展示。须记录原始URL字节、应用JS/JSON/HTML解码来源、反射上下文及实际浏览器执行；URL本身不自动解码JSUnicode，不能由泛泛cookie盗取/下载malware叙述扩大影响，HttpOnly/CSP另核。

来源：[保存帖1](https://x.com/i/status/1701219470726041966)。


## 保存图证0190-34-xss：机制与验证条件

保存原图文件：1701430565549810072-02.jpg。

DevTools Colour/selected-facets/title中有真实h1 String节点；支持HTML结构注入候选，但不含危险JS执行、参数原始响应或WAF结果。分输入→sink→节点构建，使用无害结构标记，不把标签变DOM就当ATO。

来源：[保存帖1](https://x.com/i/status/1701430565549810072)。


## 保存图证0190-36-xss：机制与验证条件

保存原图文件：1701506066251723196-02.jpg。

Radancy1619445 Webmail /admin/，图见document.write构造script src并拼getGeneratedDefaultsPath返回值；urlParams函数读取document.location.search.substr(1).split('&')，其余映射/具体键在下方截断或打码。提炼location.search到URL构造/HTML写入的DOMXSS数据流，需定位确切参数、编码/scheme/origin、脚本source许可及管理员实际交互；不能由摘要任意动作直接认定ATO或补不存在的查询键。

来源：[保存帖1](https://x.com/i/status/1701506066251723196)。


## 保存图证0190-54-xss：机制与验证条件

保存原图文件：1701943964776222927-02.jpg。

Revive Adserver报告1694171/CVE-2023-38040：默认layerstyles的simple中padding/bordercolor为CSS注入，shifth在align=center、shiftv在valign=middle时进入JavaScript；geocities中padding为CSS、closetext为HTML；floater中rmargin/lmargin为JavaScript。按参数、样式分支与输出上下文分别追踪编码和类型校验，以自有测试广告/无敏感标记验证；CSS/HTML注入不自动证明脚本执行。保存的是摘要，版本、原始请求及成功执行未显示。

来源：[保存帖1](https://x.com/i/status/1701943964776222927)。


## 保存图证0190-62-xss：机制与验证条件

保存原图文件：1702060654214132152-02.jpg。

教学图对title、textarea、script、select/option上下文比较直接SVG字符串与先闭合对应元素后插入SVG。关键是HTML解析上下文改变，不是所有编码均可绕过：若<保持实体、正确上下文转义或CSP阻止事件则不执行；script原始文本结束标记与JS字符串边界分开。仅示意标签Executed，无真实浏览器请求或执行日志；自有页面无敏感标记比较原始响应、DOM和执行。

来源：[保存帖1](https://x.com/i/status/1702060654214132152)。


## 保存图证0190-65-xss：机制与验证条件

保存原图文件：1702189436325474459-02.jpg。

无括号XSS示例将window.name作为instanceof左值，以对象自定义Symbol.hasInstance=eval隐式调用，攻击者iframe name预置表达式、反射SVG事件触发。依赖可控制window.name、可嵌入目标、对应浏览器跨站name行为、事件与eval可执行/CSP允许；括号过滤并不能建立安全边界。图仅代码无执行证据；隔离页面以非敏感标记验证数据流及跨源导航是否清空name，不能假设任意站点可用。

来源：[保存帖1](https://x.com/i/status/1702189436325474459)。


## 保存图证0190-75-xss：机制与验证条件

保存原图文件：1702384889025405156-02.jpg。

地址栏title参数含大小写混合HTML/onmouseover及confirm(document.cookie)%0dx，画面显示cookie字符串确认框。保存正文把尾x写为连续语句会误导：图中%0d是换行边界，需分开原始URL解码、HTML解析和JS语法确认；事件需鼠标经过，CSP/HttpOnly决定可执行及可读范围。单张确认框未证明任意WAF绕过或ATO；保留脱敏页面与对照，不复制cookie值。

来源：[保存帖1](https://x.com/i/status/1702384889025405156)。


## 保存图证0190-81-xss：机制与验证条件

保存原图文件：1702508193803346368-02.png。

DOM Invader图中非敏感canary进入createContextualFragment的li/div HTML及属性多个位置，DOMContentLoaded时高亮并有Exploit按钮。污点到HTML sink为候选，不等于脚本执行；需要source位置、真实响应/DOM调用栈、上下文编码/CSP和本地标记执行对照，避免把工具按钮或canary出现作为漏洞证据。

来源：[保存帖1](https://x.com/i/status/1702508193803346368)。


## 保存图证0190-100-xss：机制与验证条件

保存原图文件：1702883931266109867-02.png。

DOM图显示搜索结果内插入a标签，fixed top0 left0 z-index9999 width/height100%及onmouseover=alert(1)。CSS覆盖面可增大鼠标触发概率，仍依赖真实布局、pointer命中、用户移动与CSP，不是零交互。DOM属性存在未显示执行；不等同跨源clickjacking；用自有页面标记比较事件触发与正常节点。

来源：[保存帖1](https://x.com/i/status/1702883931266109867)。


## 保存图证0190-107-xss：机制与验证条件

保存原图文件：1703115914839752869-02.jpg。

Bash一行示例gau历史URL→含=过滤→qsreplace脚本字符串→curl --path-as-is --insecure→grep -qs载荷即标Vulnerable。字节反射只能判候选，grep默认正则还会误解元字符；需固定字符串/确切上下文、编码、状态、CSP和浏览器执行证据。历史URL严格限范围、限速去重并保存每条原始请求响应；跳过TLS验证掩盖端点问题。图片仅命令无输出，未执行该命令。

来源：[保存帖1](https://x.com/i/status/1703115914839752869)。


## 保存图证0190-114-xss：机制与验证条件

保存原图文件：1703348201057865766-02.jpg。

IPS报告2031855：用户可保存含VLE标记的post/comment/signature，管理员启用Quick Translating并访问后触发；摘要定位ips.customization.visualLang.js第254行，.text()得到未转义文本交给jQuery replaceWith按HTML解析。攻击演示取管理员csrfKey并改board_name，需管理员操作、功能开关与有权会话，不是匿名自动管理接管。隔离社区用低权限内容和无敏感DOM标记比较禁用/启用VLE及修复版，检查text→HTML语义；0px隐藏不构成根因，截图没有最终改名页面。

来源：[保存帖1](https://x.com/i/status/1703348201057865766)。


## 保存图证0190-142-xss：机制与验证条件

保存原图文件：1704176172702064992-02.png。

找回密码页顶部显示SVG/on[removed]load与alertalert([removed])文本，地址栏有嵌套<script>及双alert；说明过滤后的字节/反射候选，没有执行弹框或DOM有效事件。应比较删除替换前后原始响应、HTML节点和JS可解析性；黑名单删除可能产生新语法，也可能安全地阻断，不能由alert关键字或页面回显证明XSS。

保存原图文件：1704176172702064992-03.png。

Burp GET路径内反射HTML样式字符串，Render页输出标记文本三次；无Cookie/查询参数显示，响应raw/有效DOM未保存。路径反射需保留原始request-target、代理规范化、编码次数和多个输出位置；Render文字并不证明HTML注入或浏览器XSS，和同组过滤图分别留证。

来源：[保存帖1](https://x.com/i/status/1704176172702064992)。


## 保存图证0190-159-xss：机制与验证条件

保存原图文件：1704450473988931693-02.jpg。

Mozilla报告2111291：普通用户comment持久化内容在管理员edit comment时进入另一渲染路径，串联闭合标签与image onerror/import(data:)示例。作者明确未绕过CSP，称关闭CSP时弹document.domain，并在本地实例成功；因此是编辑路径注入候选及CSP限制，不能称线上管理员脚本已执行/ATO。自有沙箱比较正常查看/编辑、不同角色、实际默认CSP和修复版DOM；无敏感标记验证，默认策略不得为制造漏洞而关掉。

来源：[保存帖1](https://x.com/i/status/1704450473988931693)。


## 保存图片中的机制与证据边界（1705046758982598841-02.jpg）：by-type/xss.md

图片 `1705046758982598841-02.jpg`：原始HTML示例OpenSearch的h1 String标记反射到og:url meta content和canonical href属性内。带尖括号的属性值仍可能只是文本，不自动创建节点；追踪属性引号、URL编码和浏览器DOM，再用无敏感标记对照，未显示执行。

图片 `1705046758982598841-03.png`：同参数h1 String进入button title属性及按钮内容两个上下文，onclick=removeFiltersByName(this)为原始业务处理器。分别验证属性与文本/HTML解析边界，原始处理器存在不是注入执行；图仅源码高亮无成功弹框。

图片 `1705046758982598841-04.jpg`：canonical link href后出现accesskey=X onclick=alert(1)属性，依赖属性引号逃逸、具体浏览器访问键行为/用户组合键和CSP；link不可见元素不等同自动执行。仅源码存在无实际点击/键盘或弹框日志，按自有页面上下文最小对照。

来源：[保存帖1](https://x.com/i/status/1705046758982598841)。


## 保存图片中的机制与证据边界（1705417073873113465-02.jpg）：by-type/xss.md

图片 `1705417073873113465-02.jpg`：og:url属性内h1 String原样，og:title/description编码成&lt;h1&gt;；同输入多个上下文处理不同，应逐输出点观察原始HTML与DOM，属性内尖括号并非新标签，编码差异本身未证明XSS。

图片 `1705417073873113465-03.jpg`：og:url meta出现onmouseover和绝对定位全屏style，而og:title/description引号用&quot;。meta是非渲染元素，CSS宽高/事件不保证有可命中区域；即使改用可见元素也需用户鼠标与CSP。保存正文称style tag但图实际为style属性，无执行弹框；不可宣称任何移动必执行。

来源：[保存帖1](https://x.com/i/status/1705417073873113465)。


## 保存图片中的机制与证据边界（1705775309512171667-02.jpg）：by-type/xss.md

图片 `1705775309512171667-02.jpg`：DOM中输入h1string被形成非标准h1string元素并包含span残留，value属性也有同标记；说明重新解析/标签拼接候选，未知元素本身不执行。需source/sink、后继字节完成语法、浏览器修复DOM与CSP对照。

图片 `1705775309512171667-03.jpg`：未闭合img onerror表达式被DOM补成img，后续span片段进入解析区域；载荷不必显式闭合标签是否成立取决于紧随后继字节、引号和解析状态。事件属性存在未显示弹框，DOM Invader定位sink与真实浏览器执行分开，以自有无敏感标记检查。

来源：[保存帖1](https://x.com/i/status/1705775309512171667)。


## 保存图片中的机制与证据边界（1706211558857077247-02.jpg）：by-type/xss.md

图片 `1706211558857077247-02.jpg`：Toxssin演示handler.js会话及登录表单输入监控/事件注入，说明已有浏览器脚本执行后可影响表单交互；图没有初始XSS注入点，工具宣称MITM并非网络中间人证据。用自有隔离页面与虚拟标记说明执行权限/用户交互边界，不收集真实密码/键盘事件；工具会话不证明任意站点初始XSS或服务器RCE。

来源：[保存帖1](https://x.com/i/status/1706211558857077247)。


## 保存图片中的机制与证据边界（1706315116281770379-03.jpg）：by-type/xss.md

图片 `1706315116281770379-03.jpg`：document.write用Proxy apply记录参数并Reflect.apply(...arguments)转发，截图同时讲临时/解包扩展注入。需要page/main world、运行时序、frame、原生方法receiver/返回/异常一致及限定获准页面，不能无界all webpages记录秘密；调用sink不证明不可信可控输入或执行。只保存自有沙箱标记，未安装扩展或运行脚本。

来源：[保存帖1](https://x.com/i/status/1706315116281770379)。


## 保存图片中的机制与证据边界（1706862473184215453-02.jpg）：by-type/xss.md

图片 `1706862473184215453-02.jpg`：script内configureParams['query']赋值单引号字符串含h1 String，未成为HTML元素，需JavaScript字符串上下文检查，不应套HTML标签载荷。受信code/不可信值边界与单双引号编码、换行和脚本结束标记分开。

图片 `1706862473184215453-03.jpg`：同赋值显示'-confirm(1)//样式退出字符串并用减号触发表达式/注释尾部，只有代码截图无弹框；有效性依赖准确引号/后续换行/JS语法与CSP，不需要新script标签但不意味着普遍可执行。自有页面标记和原响应/解析后代码对照。

来源：[保存帖1](https://x.com/i/status/1706862473184215453)。


## 保存图片中的机制与证据边界（1707334475741635032-02.jpg）：by-type/xss.md

图片 `1707334475741635032-02.jpg`：Mattermost 1502099/CVE-2023-1421 文字列出 OAuth complete 路由，base64 state 的 redirect_to 进入输出的候选；图中本地 GitLab 登录启用与 mobile action 是前提，截断部分没有实际弹窗。分别验证 state 的会话绑定及 redirect_to 的输出上下文编码；无效 code 错误分支、CSP、实际浏览器执行须单独记录，base64 不提供完整性。

来源：[保存帖1](https://x.com/i/status/1707334475741635032)。


## CakePHP 历史异常页须定位输出上下文

正文标注 CakePHP 2.2 stack error 和路径中的引号、标签事件候选，无实际异常响应或执行。比较正常路径和唯一标记路径，定位错误模板编码，再记录 DOM、CSP 和浏览器执行。版本及路径回显不是 XSS，也不能推广所有当前实例。

来源：[保存帖1](https://x.com/i/status/1705235344235327932)。


## 保存图证0192-21-xss：机制与验证条件

保存图片 `1708865379601117434-02.jpg`：本地 PHP8.2.10 返回 text/xml;charset=UTF-8，p 参数 inject 标签被放在 aaa/bbb 与尾部杂项中；这说明反射，不证明合法 XML、HTML 解析或脚本执行。比较 MIME、字节、根元素及 parser 行为，不能仅因任意 markup 被保留称 XSS。

保存图片 `1708865379601117434-03.jpg`：同一本地 XML 页面显示 Document is empty/首个错误且没有脚本结果，正文也承认前置垃圾阻止解析。保留失败反例与浏览器/MIME 上下文；不能把解析错误渲染当恶意标签执行，未保存后续解决方案不补造。

来源：[保存帖1](https://x.com/i/status/1708865379601117434)。


## 保存图证0192-49-xss：机制与验证条件

保存图片 `1709399734673145885-02.png`：mobile-header/anchor href 中 String 标记和 URL 编码参数，appID路径/查询片段混合；静态源码呈现的 <h1> 与属性关系不能独立证明最终 DOM 或事件执行。对照 desktop/mobile 实际渲染、viewport、UA、原始响应及数据流，定位框架 v-show 仅可见性还是不同模板；不把设备模拟当真实移动端所有浏览器覆盖。

保存图片 `1709399734673145885-03.jpg`：DevTools responsive614x810截图显示移动红色header中的 String 与编码appid片段，无脚本结果。和源码图保持同一输入比较真实DOM/渲染分支，字符显示或h1变化只能支持注入候选，需独立记录CSP、实际事件与受控执行标记。

来源：[保存帖1](https://x.com/i/status/1709399734673145885)。


## 保存图证0192-70-xss：机制与验证条件

保存图片 `1709810787370643659-02.jpg`：Informatica39069历史2014/Firefox34.0.5例子search.jspa?q含闭合script再新script，2014报告与2023披露不同。缺少实际响应和弹窗，闭合标签需匹配原始上下文与CSP；历史浏览器PoC不能证明当前所有站点。自有局部标记比较源、DOM与执行。

来源：[保存帖1](https://x.com/i/status/1709810787370643659)。


## 保存图证0192-85-xss：机制与验证条件

保存图片 `1710100686862467372-02.png`：新增 message[subject] 到原有message[body]请求，编码文本示意script/getScript第三方地址；只展示参数构造，管理员查看后触发是正文声称，无callback/浏览器结果。先查server允许写字段、持久化与管理员独立渲染sink，预填UI不保护后端，回调须区分解析抓取和脚本执行；自有隔离标记不加载外部脚本。

来源：[保存帖1](https://x.com/i/status/1710100686862467372)。


## 保存图证0192-88-xss：机制与验证条件

保存图片 `1710125222337065162-02.png`：过滤区button title与可见内容都反射h1/String，前者属性文本、后者HTML候选上下文；相同字符串跨上下文编码要求不同。按响应/DOM及输入比较，title内标签不自动创建元素，现有onclick属于页面自身也非注入执行证据。

保存图片 `1710125222337065162-03.png`：变体 img/src/onerror=.1|alert 出现在title及button内容，只有源字符串，无浏览器结果。斜杠分隔、位或表达式与 .1 数值需按实际HTML/JS解析核对；匹配规则变化不等于WAF绕过或事件执行，cookie告警不用敏感值，以自有标记验证。

来源：[保存帖1](https://x.com/i/status/1710125222337065162)。


## 保存图证0192-100-xss：机制与验证条件

保存图片 `1710497677228802258-02.png`：DOM图显示img src及onerror与独立字面 \x20 属性，不能把 HTML 中 \x20 当真正U+0020空格；JS字符串解码与HTML词法是不同层。逐层记录原始字节、解码、DOM事件属性与实际CSP执行，静态DOM存在onerror不证明过滤绕过或弹窗，正文javascript:在事件值中也不等同导航scheme。

来源：[保存帖1](https://x.com/i/status/1710497677228802258)。


## 保存图证0192-112-xss：机制与验证条件

保存图片 `1710861825749733809-02.jpg`：保存源码有anchor href javascript片段与span中iframe srcdoc内script，域/后半裁剪且无执行结果。srcdoc嵌套HTML需要双层属性编码和sandbox/CSP/继承origin检查，外层链接与内层frame是不同sink；静态标签不证明跨用户可达及执行，使用本地标记比较。

来源：[保存帖1](https://x.com/i/status/1710861825749733809)。


## 保存图证0192-123-xss：机制与验证条件

保存图片 `1711245237811872195-02.jpg`：IRCCloud1887917明确启用Chat&embeds/Embed social media links，用户发Mastodon toot链接后client从[domain]/api/v1/statuses/[id]取canonical URL，第三方instance数据可恶意javascript URL。链接404仍可能API请求，表示展示页和metadata请求独立；下方JSON最终危险url与执行未保存，不能复述cookie被实际窃取。核对协议白名单、每个重定向/渲染sink、CSP和自有受控instance无害标记，不连接历史目标。

来源：[保存帖1](https://x.com/i/status/1711245237811872195)。


## 保存图证0192-125-xss：机制与验证条件

保存图片 `1711335836334309664-02.jpg`：Acronis1940788历史15.0.31791步骤：自有plan+validdevice，plan name持久化img事件，Stop再Confirm后临时消息渲染。保存文本声称执行而无实际弹窗；说明正常列表与确认通知sink不同，回归需覆盖所有渲染路径及产品版本。只用自有隔离可停设备标记，不停止生产计划；编码按上下文处理，不能简单禁止全部特殊字符。

来源：[保存帖1](https://x.com/i/status/1711335836334309664)。


## 保存正文0192：AEM childrenlist 的反射须匹配渲染上下文

正文给childrenlist.html路径中的编码img/event候选，没有响应或执行。检查selector/extension、path输入进入具体HTML/属性的解码与编码链；例中alert(domain)也需变量实际定义。以自有标记比较DOM与CSP，不把URL中标签或产品名当通用XSS。

来源：[保存帖1](https://x.com/i/status/1708836732366405956)。


## 保存正文0192：eval(name) 依赖可控浏览器上下文

script eval(name)只是执行sink示例，需先有脚本注入和对应window.name可控值、同源导航/浏览器行为及CSP。记录赋值来源、目标上下文与实际执行，空name/不受控字符串/策略拒绝都是反例；短payload不自动证明WAF绕过，不读取用户数据。

来源：[保存帖1](https://x.com/i/status/1708926601059061825)。


## 保存正文0192：搜索词进入路径或页面不证明命令执行

正文whoami反射到/whoami.php仅提出疑问。词语同时是命令名不说明被执行；分别跟踪路由拼接、HTML文本/属性输出及后端命令sink，保存实际响应和数据流。没有shell调用或受控结果不能认定RCE，回显不能独立证明XSS。

来源：[保存帖1](https://x.com/i/status/1709257507162489070)。


## 保存正文0192：returnTo 协议校验与脚本 sink

正文称login returnTo=javascript:值后登录弹窗，图片只有奖励卡。URL返回地址要独立核对scheme白名单、每层解码、导航API和浏览器/CSP，不把登录成功等同XSS。自有沙箱比较https/拒绝协议及实际调用结果，保留登录/用户操作前提，不发送真实token。

来源：[保存帖1](https://x.com/i/status/1710702033949364554)。


## 保存正文0192：混合闭合字符串必须匹配实际上下文

保存payload混合JS注释、script闭合、引号和alert片段，图仅Resolved。逐层分析原始字节、HTML词法、JS字符串/注释和DOM/CSP，找到受控输入至实际sink后做最小比较；所谓polyglot不在所有上下文有效，状态和标签不能证明浏览器执行。

来源：[保存帖1](https://x.com/i/status/1711833468345430155)。


## 保存正文0192：iframe srcdoc 需要嵌套上下文检查

正文给iframe srcdoc中的script示例，另保存图有anchor/span嵌套iframe候选。外层属性编码、srcdoc独立HTML解析、sandbox/CSP和origin继承必须分别核对；标签字符串出现不证明可控输入可达、跨用户影响或实际执行。自有局部标记对照渲染与事件，不能把所有iframe都当clickjacking或脚本自动执行。

来源：[保存帖1](https://x.com/i/status/1709814406052233662)、[保存帖2](https://x.com/i/status/1710861825749733809)。


## 保存正文0193：Unicode、Hex 和 HTML 实体须按解码层拆分

正文推荐Unicode/Hex/HTML实体和CyberChef。编码是候选表示，必须先识别输入经过URL、JSON、HTML或JS哪个解析器及次数，再比较原始字节与实际sink；实体只在相应HTML位置还原，JS标识符转义与字符串转义不同，不能称任何编码都绕过过滤。

来源：[保存帖1](https://x.com/i/status/1712103290022805665)。


## 保存正文0193：额外 on0x 属性与真实事件执行分开

正文声称WordPress DOM XSS绕Cloudflare并给img src=x on0x=1 onerror示例。on0x并非执行事件；验证链是受控输入到HTML sink、图片错误触发onerror、原页面origin内执行，再独立比较WAF原始请求403与变体响应。只有DOM属性存在不足证明执行，额外属性不是通用绕过。

来源：[保存帖1](https://x.com/i/status/1712674268486512919)。


## 保存正文0193：多层编码事件载荷需按实际解析顺序验证

正文details含%0A、onToGgle、co\u006efirm别名、%28及HTML字符引用；同帖保存拒绝页与确认框两图。识别URL解码→HTML空白/属性与实体→JS标识符和表达式，每层保持原始字节做单变量对照。只有输入落在实际HTML事件上下文才可能执行，不据字符串称通用WAF绕过。

来源：[保存帖1](https://x.com/i/status/1713783215305949614)。


## 保存图证0193-30-xss：机制、前提与最小验证

已查看的原始图片：1712674268486512919-02.jpg、1712674268486512919-03.jpg。DOM图产品未找到段落+h1 String/p，证HTML结构插入候选无JS弹窗；追实际输入到HTMLsink、固定上下文对比，Elements可编辑截图不是来源证明。

产品未找到p中img src=x on0x=1 onerror=alert(document.cookie)已形成DOM事件属性，未保存弹窗/网络对照；on0x只是额外属性，不是执行事件。云WAF声明需请求403/过检及实际sink执行各自证据。

来源：[保存帖1](https://x.com/i/status/1712674268486512919)。


## 保存图证0193-37-xss：机制、前提与最小验证

已查看的原始图片：1712815758844314010-02.jpg。TVA smpwservices.fcc USERNAME含展示为\u003c等img/onerror/confirm(document.domain)，SMAUTHREASON=7；H1显示转义序列不等服务器解码，附件仅链接。逐层确认URL传输/输出/HTML解析/执行，自有标记不外推盗cookie/RCE。

来源：[保存帖1](https://x.com/i/status/1712815758844314010)。


## 保存图证0193-63-xss：机制、前提与最小验证

已查看的原始图片：1713194634753573206-02.jpg。手机Safari自定义alert可见、URL遮盖，无payload/输入源/执行来源。只有弹窗不区分反射存储DOM或同源注入；需原始请求→sink→另一会话标记对照，不将手机本身视绕过。

来源：[保存帖1](https://x.com/i/status/1713194634753573206)。


## 保存图证0193-73-xss：机制、前提与最小验证

已查看的原始图片：1713283675289493618-02.jpg。ImpressCMS1.4.2 PHP7.2.24 Firefox85，admin.php POST memberslist_id/memberslist_uname[]未过滤且无CSRF token允许授权用户访问恶页发请求；图仅表单起始history.pushState不等全PoC。分开证cookie/SameSite/Origin/令牌、用户控制输出HTML执行；匿名/缺cookie/有token/编码对照。

来源：[保存帖1](https://x.com/i/status/1713283675289493618)。


## 保存图证0193-90-xss：机制、前提与最小验证

已查看的原始图片：1713556041386926551-02.png。Beeceptor/profile application/json截图name含<h1>test</h1>浏览器显示JSON字面文本，无HTML解析/执行；正确JSON类型是负例非JSON XSS。API JSON→客户端innerHTML另一个sink需独证；ACAO*无凭据读秘密证明。

来源：[保存帖1](https://x.com/i/status/1713556041386926551)。


## 保存图证0193-104-xss：机制、前提与最小验证

已查看的原始图片：1713783215305949614-03.jpg。keyword URL details%0Aopen%0AonToGgle…Unicode标识符+HTML字符引用表达式，站点confirm xss可见；与-02blocked是两个状态而非完整传输字节记录。逐层URL解码→HTML事件属性→JS词法，confirm别名执行需上下文；实体/Unicode/url不是任意互换，不外推所有WAF。

来源：[保存帖1](https://x.com/i/status/1713783215305949614)。


## 保存图证0193-138-xss：机制、前提与最小验证

已查看的原始图片：1714582274862440476-02.jpg。LinkedIn LeadGen Company/ProductName允许strong em a仅HTTPS ul ol sub br sup，先保存名字→ContactSales表单；报告摘要叫XSS但明确JavaScript不可能且script不允许。属于受限HTML/链接注入/界面欺骗，要另一用户看到与点击影响；不推脚本/ATO。

来源：[保存帖1](https://x.com/i/status/1714582274862440476)。


## 0194：混合编码事件属性的解析前提

正文 details/onToggle 候选同时使用百分号、JavaScript Unicode 标识符转义和 HTML 数字实体。必须逐层确定 URL 解码、HTML 属性分界、实体处理、事件触发及 JS 求值的位置；各层不能随意交换或无限解码。用无敏感标记和被转义的文本对照验证实际 DOM 与事件执行。AFW00F 所谓 WAF 指纹及一个候选字符串不证明 ASP.NET 部署可绕过。

来源：[保存帖1](https://x.com/i/status/1715116400224743807)。


## 0194：DOM sink 要按解析与导航语义区分

正文列举 location、innerHTML、eval，图片显示 redirecturl=javascript:... 和弹窗。导航、HTML 解析和 JS 求值需要不同输入上下文、scheme、CSP、事件条件与 origin。使用自有无敏感标记从 source 追到真实调用点，比较普通文本、禁止 scheme 和可信值。cookie 弹窗不证明 HttpOnly 数据可读或账户接管；图缺 sink 代码，DOM/反射分类不能只凭标题。

来源：[保存帖1](https://x.com/i/status/1716436296875258252)、[保存帖2](https://x.com/i/status/1716436536521048436)。


## 0194：搜索 query 的事件触发与 DOM 标签的证据

TD 搜索截图给出包含标签及 onmouseover 的 query，需要实际 HTML 插入和悬停。比较 source 解码、sink、转义文本、CSP 和交互条件，记录无敏感标记执行所在 origin。报告的 DOM 类别、Medium 和取 cookie 主张没有 sink 代码或弹窗支持，不能推导账户接管。

来源：[保存帖1](https://x.com/i/status/1717254914815283385)。


## 保存图证0194-29-xss：1715307044381859939-02.jpg

Mozillaunsubscribe1913263报告明确IP被封未获得realPoC，只给闭title/script/marqueeURL，script Alert(xss)大小写/未定义变量也需context核。HTML注入与JS实际执行分开，不能据Resolved/Low3.1或附件链接推ATO。

实际保存图：1715307044381859939-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1715307044381859939)。


## 保存图证0194-74-xss：1716436296875258252-02.jpg

浏览器redirecturl=javascript:confirm(document.cookie) activation失败页弹cookie确认框，图无sink代码/网络原始来源。核location赋值或其他导航API及scheme允许、用户控制/实际origin和另一会话。cookie弹窗不证HttpOnlytoken可读/已ATO，DOM与反射来源不能只标题区分。

实际保存图：1716436296875258252-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1716436296875258252)。


## 保存图证0194-109-xss：1717254914815283385-02.jpg

TD 搜索报告截图给出 query 中的 <i> 与带 onmouseover 的 <a>，需要鼠标悬停才能触发该事件。保存图没有实际弹窗或 sink 代码；DOM 标签不等于已证明 DOM source-to-sink。应比较 URL 解码、动态 HTML 插入和文本转义路径，使用无敏感数据的标记，并检查 CSP、交互条件；截图中的窃取或接管主张未展示。

实际保存图：1717254914815283385-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1717254914815283385)。


## 0195：逐参数扩展扫描仍需 source 与 sink 对照

XnlReveal 宣传单参数自动找 XSS；保留原始正常请求和参数来源，每次只改变一个可控输入，观察反射上下文、真实 sink、事件条件及无害执行标记。自动候选与弹窗、CSP、origin 和受影响用户分开，多个参数组合或后台处理也可能不在单参数覆盖内。保存帖没有扩展实现或扫描结果。

来源：[保存帖1](https://x.com/i/status/1718584438014271612)、[保存帖2](https://x.com/i/status/1719356253699502477)。


## 0195：盲回调到支持面板影响需要连续证据

正文自称 blind XSS 后可读所有邮件，图只有 Critical 报告摘要。按授权表单、存储、后端实际渲染用户、origin、会话权限与受控测试数据逐段记录；用唯一无敏感标记关联回调，排除浏览器预览和正常取回。回调不等任意邮件可读，不对所有输入喷洒 payload 或接管实际支持人员会话。

来源：[保存帖1](https://x.com/i/status/1719049904826486817)。


## 0195：htmlspecialchars 的保护取决于输出上下文

正文说代码审查绕 htmlspecialchars 找反射 XSS，没有代码。核实际 flag/字符集与 HTML 文本、属性引号、JS、URL、CSS 等 sink，编码后值是否再解码/重用。用自有无害标记与正确上下文编码比较，不能因函数名推任意 bypass，报道标题不证明 JS 执行。

来源：[保存帖1](https://x.com/i/status/1720835678848917908)。


## 保存图证0195-34-xss：1719051684373213372-02.jpg

8x8报告摘要称已提交付款数据可修改，POST /api/patchPaymentMethod/ID JSON ipAddress含SVG onload，回显端点与32字符随机receipt hash。随机hash不能替代owner授权，修改权限和HTMLrender是独立边界。自有A/B付款fixture比较字段写入权限、读回及真正渲染，无害标记与转义控制；图没有浏览器弹窗，不能据onload字符串或自述isolated推全账户影响。

实际保存图：1719051684373213372-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1719051684373213372)。


## 保存图证0195-59-xss：1719512216393924819-02.jpg

TikTok摘要描述Pangle file_name参数CRLF与未HTMLescape导致反射JS，只有厂商摘要没有原始头/body/PoC。按参数→decode→header分隔→ContentType/body→浏览器sink核每段；CRLF与HTML反射可为不同链，不能由摘要自动推response splitting/任意cookie/XSS执行，使用隔离无害标记与转义/头拒绝控制。

实际保存图：1719512216393924819-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1719512216393924819)。


## 保存图证0195-61-xss：1719539685209313640-02.jpg

Collaborator列表DNS/HTTP与GET /deployment/env/...config.js?_=... UserAgentFirefox、SecFetchModecors/sameorigin，host部分遮盖。浏览器样式取回可佐证资源加载但不独立证明JS执行、CSPbypass或SSRF；关联唯一标记与发起页面/调用栈、实际script MIME/执行无害标记，排除正常fetch/预览。标题P1不代替sink或token获取。

实际保存图：1719539685209313640-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1719539685209313640)。


## 保存图证0195-125-xss：1721051036964569298-02.jpg

DorkKing UI按目标生成FormFinder intext/intitle/inurl、RegisterSignup、Contactus五类，只有按钮未显示查询/结果。五个dork不是所有表单；保留查询site边界、登录态、索引时间与当前入口，发现表单不证明储存/管理端渲染/盲XSS，更不授权每处spray。

实际保存图：1721051036964569298-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1721051036964569298)。


## 保存图证0195-129-xss：1721141074087780547-02.jpg

第二DorkKing图分辨率不同独立hash，同五个表单候选按钮，未显示完整dork或搜索返回；按当前post绑定像素与来源，保持site边界/索引时间/实际表单及后台sink分离，不以按钮数量证明覆盖。

实际保存图：1721141074087780547-02.jpg。本轮原始像素已阅；图片仅支持上述可见内容。

来源：[保存帖1](https://x.com/i/status/1721141074087780547)。
