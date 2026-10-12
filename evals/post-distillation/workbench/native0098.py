"""Append this batch's reviewed prose; never execute post material."""
from collections import defaultdict
from pathlib import Path
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
facets=[
('by-type/sql-injection.md','PDO数据参数与动态排序标识符','''旧帖说PDO不能绑定列名/ORDER BY列。沿真实查询模板区分值参数、标识符、排序方向和任意SQL片段；调用prepare不保护已经拼入模板的外来语法。[PHP PDO::prepare说明](https://www.php.net/manual/en/pdo.prepare.php)限定参数只能代表完整数据字面量，不能代表关键字、标识符或任意查询片段，且模拟prepare不与服务器通信（2026-10-10核读官方说明，不采用户评论作为保证）。

动态列/方向选择可映射到服务器明确允许的已知语法，值仍参数化；不能把“禁止任意列名”误写为所有合法排序功能都不准接受用户选择。绑定实际驱动、版本、模拟模式、模板构造点和执行消费者，未知保留。优先获准源码/合成查询结构对照，不执行源帖查询、枚举数据库或由某个报错声称SQL控制。来源：[保存帖](https://x.com/i/status/1397597402891177993)。'''),
('by-type/graphql.md','关闭内省后的候选schema与模型完整性','''clairvoyance旧宣传称内省关闭仍可输出供Voyager/InQL使用的JSON。将正常操作、客户端字段、校验错误/建议和工具推断分别标明来源；内省配置、候选字段可发现性和resolver权限是三个问题。JSON格式能被工具接受不证明所有字段/参数/输入类型都恢复，也不说明与当前部署一致。

从已有获准操作及错误构建与当前消费者相关的小模型，记录版本/身份/时点、已见字段和未知部分，再与真实schema契约核对；字段名猜测不当完整模型，公开接口描述不自动泄密。不执行工具枚举、生成全部操作或继承工具的complete宣称，完整仓库与外部工具教程未读。来源：[保存帖](https://x.com/i/status/1397613730016505863)。'''),
('by-type/graphql.md','批处理中的挑战身份与验证次数','''旧帖将单包多邮箱/密码及全部2FA值直接称限流绕过。传输层数组batch、单个operation的多个别名和实际验证调用不同，是否支持需目标处理器证据。一个HTTP请求可触发多次业务尝试，但不保证所有实现接收、共用挑战或只扣一次计数。

沿每个元素/字段记录账号规范化身份、挑战ID/代际、验证消费者、失败次数/锁定/消费状态和会话签发，以获准隔离正常/拒绝回执确认请求级与业务级预算；每次逻辑尝试均计数。拒绝batch、逐次限额、已消费挑战拒绝和合法独立批次作反例，不尝试真实密码/2FA空间或制造耗尽，外部Wallarm文章全文未读。来源：[保存帖](https://x.com/i/status/1397628837970784258)。'''),
('by-type/xss.md','对话框、动态求值与文档写入的不同消费者','''alert关键词被过滤后改confirm/prompt/eval/write，只是候选调用名称改变；这些API不具有相同参数、返回值或安全作用域。先确认输入已进入JS语法及实际函数绑定，再区分对话框观察、字符串求值和document等对象的写入消费者；单独出现eval或非限定write不保证执行或等于alert效果。

保留输出语境、净化后字节、真实对象/函数及策略，使用隔离合成无害标记解释消费，不从关键词未拦截推XSS或普遍WAF绕过。正常纯文本/不可调用值/不存在对象及拒绝策略作为反例，控制台原本可执行也不证明目标输入链。来源：[保存帖](https://x.com/i/status/1397760287353098241)。'''),
('by-type/xss.md','字符串替换回调与已取得的JavaScript执行','''旧帖把replace传入alert函数称“在RegExp中执行”。实际函数是替换回调：搜索值有Symbol.replace时由该消费者处理，可调用replacer接收匹配片段、捕获及位置/原字符串等参数。[ECMAScript RegExp替换算法](https://tc39.es/ecma262/multipage/text-processing.html#sec-regexp.prototype-%symbol.replace%)明确可调用替换值的调用步骤（2026-10-10核读）；这不是正则文本自动执行脚本。

源表达式要求先能执行JS并取得函数引用；要另证外来输入如何突破正常数据语境。document.cookie只是JS可见cookie，不包括HttpOnly秘密，空Safari控制台截图没有执行结果，更不证明所有浏览器测试。以已有脱敏源码解释调用/参数/返回即可，不求值源代码、读真实Cookie或将新语法同义变体独立计为漏洞。来源：[保存帖](https://x.com/i/status/1398828431278690304)。'''),
('by-type/waf-bypass.md','旧百分号u表示与Unicode外观和HTML标签开头','''旧ASP span示例把%u003C、%u3008和%uFF1C并列。表示形式、解码器接受情况、最终码点和后续映射不同：U+003C是ASCII小于号，U+3008/U+FF1C外观近似却不是同一字符。不能把旧%u形式当标准UTF-8百分号编码，也不能默认每个ASP/代理/浏览器都作同一解码。

[HTML Data state](https://html.spec.whatwg.org/multipage/parsing.html#data-state)以U+003C切换tag open，其他普通字符直接发出字符token（2026-10-10核读）。若最终字符仍是U+3008/U+FF1C，需另证真实上游转换或其他消费者才可推标签形成。保留每层字节→解码/映射→过滤→输出→DOM/事件与策略；span回显、历史P3 Triaged/仍评估截图不补执行证据，不发送载荷或将全部变体写成通用ASP绕过。来源：[保存帖](https://x.com/i/status/1399268822062829571)。'''),
('by-type/ssrf.md','自动化文字命中与服务端取址的因果','''旧1/4脚本把参数替换为云metadata hostname路径，grep到compute.internal便标VULNERABLE；2/4改为interactsh标记。响应文本可能来自静态页面、缓存、错误/反射或其他请求；DNS、HTTP回连、返回内容、内网读取和云凭据是不同能力，不能以一行grep定论。

固定原始参数、实际取址消费者、请求身份/时点、解析/连接轨迹与独立唯一合成标记观察，先排除工具自身流量及访问者加载。当前IMDS方法/token配置沿既有元数据条目核对，旧GET地址不适用于所有部署。只分析获准离线日志/合成轨迹，不访问云元数据/内网或启动公共回连；保存内容仅1/4、2/4及一张脚本图，未保存的3/4、4/4仍未知。来源：[保存帖](https://x.com/i/status/1397944303511474177)。'''),
('discovery/records-and-incremental.md','多阶段URL流水线的集合、解析与总量','''SSRF组合图串枚举→httpx活性筛选→gau/wayback→URL去重→参数替换→curl/ffuf，分别列500、30或200等并发。前段筛掉的域/失败结果不在后段分母；anew累积文件可能混入旧轮次，不同query/顺序被归并也不保证是同一消费者。原URL、候选来源/时点、每段输入输出/拒绝失败/实际运行范围分别保存。

URL字符串经xargs替换再嵌入bash -c时，还要核对shell引用与真实argv；显示的一整行不证明按预想原样处理。延迟参数不是聚合速率/总请求上限，各阶段/嵌套并发及追加文件共同影响负载。用自己的有限合成清单静态核对集合与制品，不运行来源脚本或拼入真实URL；ffuf正文header是占位，图里UA不补齐缺失线程。来源：[保存帖](https://x.com/i/status/1397944306011312132)。'''),
('discovery/records-and-incremental.md','站点树过滤、任务暂停与观察分母','''旧Burp图显示only parameterized、hide not-found，4xx/CSS/图片/二进制被隐藏，only in-scope没有勾选，且task execution paused/site map will not be populated。这些是当前视图/记录入口状态，不是所有页面、所有请求或测试动作的完成情况；非参数化路径、被隐藏拒绝与未填充条目不可从分母抹掉。

关联该版本过滤配置、原始捕获、发起工具及任务状态，区分未发现、未请求、已请求未观察、过滤、失败和未完成。只在获准既有日志中核对显示集合和真实出站，不改范围控制来补视图、不从空表推阴性；full methodology外部文章没有从单图补齐。来源：[保存帖](https://x.com/i/status/1397978215810019331)。'''),
('by-type/desktop-client.md','系统代理协议选择与项目scope和制品身份','''桌面测试旧帖建议OS proxy/Burp scope/pinning patch；图里macOS只勾HTTP到本机8080，HTTPS未勾，并有local/link-local bypass，另一图是Burp advanced scope的Any协议、单host与空Port/File。项目scope、视图过滤、实际系统代理协议、直连/自定义网络栈和出站控制不同，配置画面不证明流量全部经过或HTTPS已解密。

把制品hash/签名、平台/进程/网络库、CA信任或patch状态与捕获证据关联；修改pinning成功不等于原始客户端在普通攻击条件下失效。优先已获准正常请求/日志区分未启用、绕过、TLS失败及过滤，不从空Burp记录推功能不存在，也不把部分URL匹配当完整主机授权。只审图片/既有材料，不改变系统代理、安装CA、patch二进制或拦截他人通信。来源：[保存帖](https://x.com/i/status/1398450971198509062)。'''),
('by-type/api-property-pollution.md','Rails历史指南与实际许可字段的绑定','''旧帖链接Rails3.2.9并称mass assignment仍普遍存在，accepted/奖金图缺字段与版本，不能推广当前所有Rails。[当前Rails Strong Parameters指南](https://guides.rubyonrails.org/action_controller_overview.html#strong-parameters)说明批量赋值前显式许可字段，并警示permit!及expect空hash可放开当前/未来属性（2026-10-10核读相关段落）。实际版本/API支持仍以目标代码为准。

沿控制器绑定、允许字段/结构、模型赋值和敏感属性消费者核对；存在Strong Parameters不保证许可集合或每个业务权限正确。用自有合成对象/已有源码确认字段拒绝、忽略、合法编辑及权威能力变化，不把模型字段可读当可写或prepare式命名当安全保证；旧指南全文未读，不根据奖励补成特定提权。来源：[保存帖](https://x.com/i/status/1398620157291859970)。'''),
('by-type/api-property-pollution.md','申请状态字段与审批转换的权威结果','''pending0→1或PENDING→Accepted只是字段候选，不同产品枚举/状态含义不同。将对象所属身份、字段写权限、当前状态、审批者资格、允许转换/前置条件和服务端权威状态分开；保存或回显Accepted可能没有触发真正审批及下游权益。

在隔离合成申请或获准源码/日志中比较正常申请、合法审批、普通角色字段更新与拒绝条件，关联状态版本/原子转换、审批来源和实际受保护能力。可自改草稿/撤回、未知字段忽略、严格拒绝及未触发权益作反例；不批准真人申请/支付/权限变更，accepted奖励图不补全审批链。来源：[保存帖](https://x.com/i/status/1398622552851845123)。'''),
('cloud/cloud-misconfiguration.md','APK中的Firestore线索与主动规则检查','''FireStorePwn示例图先反编译APK、从Manifest/strings/smali取项目与Tweets集合，再提示查询费用、询问permission checks并显示readable/not writable。静态项目/集合线索与主动访问规则核查不同，工具界面的y不提供项目授权；返回样例也没证明请求匿名、当前规则错误或所有集合都读写开放。

沿制品版本/hash→项目/产品→collection/document路径→请求主体→操作规则→允许受众核对，读与create/update/delete分别保留结果及未知。公开样例、合法认证读与不可写是反例；调用次数与费用属于真实操作成本，不能以“scanner”名义忽略。优先已有脱敏配置/日志/合成样例，不执行APK/反编译器/工具、枚举数据库或修改云对象；整仓库实现未读。来源：[保存帖](https://x.com/i/status/1397904544999391232)。'''),
('by-type/authn-session.md','IMAP凭据工具中的配置、连接与认证失败','''IMAPLoginTester截图把invalid email、missing config、IPv6代理不支持、超时与Login FAILED放在同一输出，最后working logins0/4。未到认证消费者的地址/配置/连接失败，不能计作服务端已拒绝该密码；0/4不说明四次独立有效验证或凭据均错误。

分别保存输入解析、域到服务配置、代理/地址族、连接/TLS、认证消费者及结果、账户/身份/时点和实际尝试数；仅最终认证拒绝与正确正常对照才能支持该分支结论。工具示例中的口令/邮件不成为可用凭据，未成功连通也不证明无认证缺陷。只静态审图/获准诊断，不用外来凭据登录、读取邮箱或绕失败继续猜密码。来源：[保存帖](https://x.com/i/status/1398765388566077442)。'''),
('expert-reasoning.md','Windows工具图中的跳转、执行与横向权限','''HookDump图列ntdll函数/JMP地址，但没有基准字节、模块归属、权限/系统版本；跳转存在不独立证明恶意hook或保护可绕过。CheesePS图左边已compromised低权限用户，右边有另一PC的本地admin凭据，再串远程runspace/模块/保护patch/执行箭头；这些前提不是工具自动取得的新漏洞能力。

将已有控制、进程/线程身份、远程登录资格、具体策略/版本与每条执行边的实际回执分别记录；概念图、tried command日志、反复转载不作独立复现。保护功能名称相同不保证同一实现/绕过结果，缺少一条必要边就保留该缺口。仅审提供材料，不执行安全产品绕过、下载模块、修改进程或横向登录；工具整仓库未读。来源：[检测输出帖](https://x.com/i/status/1398402907243003904)、[工作流帖](https://x.com/i/status/1398991770663403521)。'''),
]
grouped=defaultdict(list)
for f,title,body in facets:
 p=T/'references'/f
 assert p.is_file() and ('## '+title) not in p.read_text(),title
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
print('Added',len(facets),'native facets and community routes to',len(grouped),'topic files')
