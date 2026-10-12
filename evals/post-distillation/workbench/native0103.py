"""Append reviewed 0103 facets with provenance, without executing source content."""
from pathlib import Path
from collections import defaultdict
import json,re
T=Path('/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting')
W=T/'evals/post-distillation/workbench'
facets=[
('by-type/authn-session.md','重置验证码状态差与仍被拒绝的并发声明','''重置密码图中一行200/较长响应和多数422，只显示HTTP差异，选中面板还是请求；另一Apple图的UI与JSON明确Too many incorrect verification codes/hasError true。多IP并发成功、任意账号接管均是正文声明，图未补最终认证/重置状态。

把实际验证码格式/挑战、主体、所有认证载体、计数键/窗口、错误语义与最终服务端动作绑定。200可能是重置表单或错误页，频控拒绝也不能单独证明所有主体/窗口都受限；仅分析脱敏既有材料，没有暴力尝试、并发或发送邮件。来源：[重置帖](https://x.com/i/status/1407609013265522694)、[并发帖](https://x.com/i/status/1407617193135599623)。'''),
('discovery/records-and-incremental.md','扫描skip配置与发现和验证的不同分母','''Dalfox管线提示保存输出并使用skip/onlydiscovery选项提速。结果被写入文件、发现候选、实际运行验证和完整覆盖是不同状态；选项名称不能替当前工具版本的真实生效配置或跳过分支。

保存每段输入/输出哈希、实际argv/版本、阶段执行/跳过/失败计数和身份预算，候选需独立追到真实消费者。与默认流程比较时固定集合/时点，不能把更快或少报直接称同等覆盖。只读旧命令文本，未运行assetfinder/gau/dalfox或访问目标。来源：[保存帖](https://x.com/i/status/1407901013978193926)。'''),
('by-type/idor-access-control.md','可编辑响应标志与最终持久写权限','''xx_update_xx=false改true能启用编辑的描述，首先证明的是可控客户端分支候选。前端解锁、发出保存请求、后端接受和权威状态改变须分别确认；金额声明不代替角色规则。

固定操作者、管理员创建的受控对象、不可编辑的权威业务规则与最终写入/读回，核对全部服务端身份载体。正常允许协作者、请求被拒/回滚、仅本地UI变化或旧缓存是反例。本批未修改用户、字段或真实业务对象。来源：[保存帖](https://x.com/i/status/1407945793688903680)。'''),
('targeted-fuzzing.md','CVE标题、info级登录页匹配与执行漏洞','''Nuclei2.3.8图把CVE-2017-7692 RCE写入标题，但实际输出Squirrelmail Login、info等级及login.php URL。工具模板可自行声明名称/等级，识别登录入口不证明受影响实现、版本条件或命令执行。

先绑定有效模板哈希/版本、匹配表达式、原始脱敏响应和正常登录页反例，再沿实际漏洞消费者核对身份/配置。模板源码未保存时保留未知，不补其匹配逻辑；多个URL命中可能只是一套入口。没有运行Nuclei、登录邮件服务或使用漏洞脚本。来源：[保存帖](https://x.com/i/status/1408000479141908480)。'''),
('by-type/idor-access-control.md','参数形状矩阵与解析后的授权对象','''IDOR导图并列重复HTTP参数、重复JSON键、数组/对象包裹、路径/方法/Content-Type、UUID/数字ID、API版本与移动入口。它们改变的是可能的解析/路由或对象选择，不能由一组401/403到200示例认每项通用绕过。

沿每层实际解析结果确认哪个值进入授权检查、哪个对象进入查询/写入，在获准两主体/两对象和同动作下固定其他维度。额外参数被忽略、严格类型拒绝、公开对象、合法继承是反例；错误响应也需和权威写状态区分，不能自动认后台成功。导图不代表完成全部检查，本批未发送变异请求或删除对象。来源：[保存帖](https://x.com/i/status/1408054941445353472)。'''),
('discovery/passive-and-services.md','组织关键词到ASN列表的格式和共享归属','''旧amass管线把org输出按逗号取首列，再用xargs按逗号拆ASN并发调用；结尾还含可疑孤立引号。组织搜索、文本首列、合法ASN、该ASN资产归属及正式范围是各自一层，不能由关键词paypal扩到共享网络所有地址。

保存真实版本、每段格式/分隔、退出错误、有限去重集合与实际下游输入，截图Logo不补查询结果。未正确解析/未查询与不存在分别记；源命令的引号不静默修复。没有执行管线、DNS请求或ASN扫描。来源：[保存帖](https://x.com/i/status/1408205561204707330)。'''),
('by-type/mobile-android.md','APK URL正则排除与候选来源的保全','''apktool后正则提URL、删引号并排除google/github等词的管线，得到的是某一规则筛后的字符串集合。匹配语法、转义/截断、子串排除会漏掉合法目标或保留非运行地址，去重不能补来源与漏项。

绑定获准包的哈希/签名/版本、文件位置/解析方式，保留原始值、变换和每个排除理由，再区分示例/第三方库、旧地址和当前运行消费者。被排除域名也可能是业务入口，命中不自动扩Scope；本批没有下载APK、执行反编译或访问候选。来源：[保存帖](https://x.com/i/status/1408206143323836417)。'''),
('by-type/ssrf.md','CI lint远程include的校验失败与取址副作用','''旧GitLab请求对CI lint提交远程include，响应invalid YAML引用该URL，旁图有A/AAAA/HTTP事件。内容校验失败可能发生在取址之后，但需同一触发/唯一标记/任务归因；事件图遮盖且日期显示异常，不补内部读取或实际云身份。

[GitLab原始CVE记录](https://gitlab.com/gitlab-org/cves/-/raw/master/2021/CVE-2021-22214.json)限定webhook允许内网请求的配置，列10.5至13.10.5之前、13.11至13.11.5之前及13.12至13.12.2之前，不能只取“>=10.5”。核对实际版本、身份、远程消费者/目的地限制与最终内容，不由lint无效或普通公网回连互证全部边。本批没有运行curl、回连服务或访问内网。来源：[请求图帖](https://x.com/i/status/1408218852245135362)、[版本帖](https://x.com/i/status/1408631591044206594)。'''),
('by-type/cmd-injection-rce.md','eval异常通道中的示例输出与执行身份','''Python图以NameError显示eval调用，再以KeyError内uid字符串示意子进程结果；前段变量名还不一致，属于待核的示例材料，不能用绘制的Traceback替代原始执行轨迹。

分开输入可控、实际eval/命名空间、系统调用、结果进入异常输出及有效进程身份，错误页只提供候选位置。无代码消费者、可信常量、异常模板伪造/固定输出或低权限均是反例；root字样不替身份关联。本批未执行Python源PoC、调用系统命令或读取文件。来源：[保存帖](https://x.com/i/status/1408231767212007424)。'''),
('discovery/records-and-incremental.md','PassiveScan回调与扩展额外发出的请求','''403 Directory Bypasser说明PassiveScan默认触发自动扫描，图High/Certain和多个路径200来自扩展自身标签。接收被动回调与随后发出变异HTTP请求是不同动作；名字不保证运行纯被动或无写影响。

核对实际扩展版本/代码、触发条件、生成方法/路径、身份传递、作用域过滤和请求总预算，区分原始流量与扩展追加流量。真正判据是本不应有的保护对象能力，200登录页/公开fallback/重复结果是反例；本批没有导入扩展或运行扫描。来源：[保存帖](https://x.com/i/status/1408266860550709255)。'''),
('by-type/xss.md','Cisco SAML字段与特定VPN界面的浏览器读者','''保存请求写SAMLResponse并配/+CSCOE+/saml/sp/acs页面弹窗，仍需原始POST响应、字段到输出上下文、实际设备/用户界面和交互条件关联。弹窗1不证明取得所有VPN账号或设备OS权限。

[Cisco公告](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-asaftd-xss-multiple-FCB3vPZe.html)限定受影响ASA/FTD版本及特定AnyConnect/WebVPN配置，明确攻击发生在用户的Web服务界面；不能推广所有Cisco设备/当前版本。核对实际消费者/转义、用户身份、补丁/配置与正常拒绝反例，本批没有提交SAML或访问设备。来源：[保存帖](https://x.com/i/status/1408290933322354688)。'''),
('cloud/cloud-misconfiguration.md','Azure管理面枚举与匿名Blob数据面的证据','''BlobHunter图先显示登录主体及两个subscriptions，第一段报告21个storage accounts、2个PUBLIC containers，第二段还在检查。已认证管理面可列资源、工具标公开、匿名读某对象及全任务完成是不同事实。

绑定租户/订阅、实际主体、每个账户/容器及访问策略快照，区分发现、尝试、失败/未完成和数据读取；合法公开内容、无对象权限或仅一段完成为反例。工具标题Public scanner不让登录扫描变匿名。本批未登录Azure、枚举订阅或读取Blob。来源：[保存帖](https://x.com/i/status/1408564837689528320)。'''),
('by-type/ssrf.md','同名URL数组拼接与校验和连接的解释分歧','''原图将重复url参数变数组，再示意逗号拼接与@用户信息产生另一个主机，作者明确不是通用技巧。框架如何收重复值、校验哪一项、如何转字符串和连接器如何解释都须证明，不能静默把示意输入当有效结果。

固定版本/原始字节，记录每层值的类型/顺序、校验依据及最终scheme/authority/host/path，再关联获准目的地和真实任务。严格单值、拒绝数组、校验最终目的地或无连接均为反例；本批未执行JS、发送重复参数或访问网络。来源：[保存帖](https://x.com/i/status/1408639026958004226)。'''),
('cloud/cloud-misconfiguration.md','S3历史ACL清单的资源层与READ_ACP语义','''Pastebin图的bucket_exists、AuthUsers/AllUsers及READ/READACP是旧扫描标签，还有NoSuchBucket异常与后行黏连，不能认当前所有资源或全部对象暴露。[AWS ACL说明](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html)区分桶READ列举、对象READ读取及READ_ACP读取ACL。

保存原始行/操作/时点、桶和对象身份、ACL实际作用层及有效策略；查看ACL不等于读内容，列举也不证明写/执行。合法公开资源、对象拒绝、ACL未参与授权和无法归属的错误分别记；历史名单不提供测试资格。本批没有访问清单资产、调用云API或复制对象。来源：[保存帖](https://x.com/i/status/1408732964104589317)。'''),
('by-type/idor-access-control.md','Autorize长度判定、公开流量与有效主体隔离','''Autorize图含Bypassed/Is enforced?、长度对比及analytics/OPTIONS等公共流量，并显示临时Cookie配置。相似长度或工具标签不等于无权读取，替换一项凭据也可能保留其他有效认证载体。

固定受保护对象/动作与已获准两身份，核对最终服务端主体、Cookie/Authorization/CSRF组合、工具过滤和真实正文/权威写回；公开遥测、预检、错误、缓存和混合身份作为反例。图scope-only未必必选，需实际配置及流量确认；本批没有重放请求或使用截图Cookie。来源：[保存帖](https://x.com/i/status/1408786507855499269)、[身份替换建议](https://x.com/i/status/1408138179593396224)。'''),
('source-audit.md','凭据API hook声明与调用和权限前提','''SharpHook帮助列mstsc/runas/powershell多进程与本地文件输出，说明的是意图和参数。进程名匹配、实际API调用、是否可见明文、hook写入权限及最终凭据用途各自独立，不能由标题认任意账号泄露。

仅对获准隔离合成或现成审计材料绑定进程创建身份/代际、模块/架构/版本、调用时点、句柄权限与数据净化，区分无调用、有效保护和解析失败。主动注入及留存文件有实际状态影响，检测须独立正负例；本批未加载hook、采集密码或写凭据文件。来源：[保存帖](https://x.com/i/status/1408912147392962566)。'''),
('experiment-design.md','网络诱饵事件到poisoner检测的归因','''HoneyCreds图显示SMB/HTTP客户端、诱饵配置、发送事件和Poisoned response日志。模拟解析/连接、收到响应、规则检测及确认恶意者是不同判据，不能把日志自动升级真实凭据泄露或relay成功。

用自己的隔离合成身份和既有脱敏记录绑定名称解析链、协议/来源、唯一标记/时点、collector及检测规则，排除合法代理、旧缓存或其他诱饵事件。网络诱饵并非无请求测试，需有限动作与前后状态；本批没有使用显示凭据、发送SMB/HTTP或部署诱饵。来源：[保存帖](https://x.com/i/status/1409138637262966788)。'''),
('by-type/sql-injection.md','DWR参数类型、延时文本差异与实际测量','''图DWR请求的string参数含pg_sleep(1)，正文却写pg_sleep(10)并使用曲引号/长破折号；这些原字节不能静默转换成ASCII后称原PoC有效。callCount/methodName等也不说明数据库实际执行了输入。

绑定原请求字节、应用类型/方法、查询消费者与真实数据库，再用获准有限合成/既有测量记录核对正常延时、异常、队列/网络噪声及独立对照。只有构造值或950奖信而无测量仍是候选；奖信待修复不补当前复测。本批未发送SQL、调用sleep或导出数据。来源：[保存帖](https://x.com/i/status/1409201772636389387)。'''),
('targeted-fuzzing.md','文件泄露模板命中与统一错误页反例','''私有InterestingLeaks模板图短时输出大量htaccess/htpasswd等路径及Low等级，但未展示matcher源码或实际正文。文件名、200/长度和低等级标签都不能直接证明对应文件存在或秘密内容已泄露。

固定模板/配置哈希、有效匹配规则、每行原始响应及有限合成不存在路径对照，区分统一登录/错误/fallback、缓存与真实文件字节。重复路径/变体不自动计独立问题，秘密有效性与来源身份另证；本批没有执行模板或获取目录文件。来源：[保存帖](https://x.com/i/status/1409205035456548866)。'''),
('cloud/cloud-misconfiguration.md','S3列举的截断信息与HTML对象浏览器origin','''ListBucketResult图有MaxKeys1000、IsTruncated false和images/零字节marker，屏幕下部仍裁切；服务响应的集合边界与截图可见集合不同，目录样式键也不是可浏览真实文件夹。

列表项→对象读取→内容类型/实际托管origin→脚本/HTML消费者与目标用户身份分别核对。旧营销HTML可能公开且无外来输入，SVG文件名/ETag/LastModified不能补XSS执行或当前字节一致；列举权不代对象读取权。没有下载对象、渲染不可信文件或执行脚本。来源：[保存帖](https://x.com/i/status/1409397897955794945)。'''),
('source-audit.md','heap快照变化、地址复用与内存损坏判据','''Heappy图将多个snapshot、next/prev_size等字段和注释并列，可视地址/值变化不证明越界写、UAF或任意写能力。字段标签还依赖分配器版本和真实结构布局。

绑定获准制品/进程身份、架构/分配器、采集时点、分配/释放代际及原始块，分开合法状态变化、地址复用、解析失败与实际不变量破坏。可信基线和生命周期对照需先成立，截图UI不替真实写回/执行；本批没有编辑堆、调试目标或运行二进制。来源：[保存帖](https://x.com/i/status/1409500952630120454)。'''),
('cloud/cloud-misconfiguration.md','实验VPC图的路由、VPN路径与未部署节点','''AWS实验图的public路由指IGW、private仅local，另列WireGuard、SG端口及NACL标签。Docker节点明确to be done；示意图不能计部署完成、实际入出规则或所有私有服务隔离。

沿获准已有配置/日志绑定账号/VPC、有效路由、管理身份、VPN来源、规则方向/CIDR/端口和真实监听，区分公共入口、内网可达与服务认证。NACL allow标签不补SG实际允许，VPN通路也不等于任意第三方权限；本批没有部署、连接云主机或启动实验。来源：[保存帖](https://x.com/i/status/1409636796506415107)。'''),
('discovery/records-and-incremental.md','全局头替换的注入出处与盲通知去重单位','''旧建议在Burp Match/Replace把盲XSS放UA/Referer，另一图称22次执行、Resolved及旧VRT版本。全局规则可影响不同请求/身份/域，触发次数、独立注入点、根因数量和当前修复状态不能互换。

保存实际匹配过滤/生效范围、原始和变换请求、每字段独立合成标记、存储/后台读者与回连时点，排除工具自身页面、安全预取和重复后台阅读。通知URL/trackingID缺入口或身份时保留缺口，避免向第三方收集真实浏览器数据；本批没有注入真实流量、外联或发送消息。来源：[头替换帖](https://x.com/i/status/1409751510850834433)、[通知帖](https://x.com/i/status/1409639729486700546)。'''),
('discovery/web-and-api.md','robots注释、User-Agent分组与路径模式来源','''图中grep Disallow把#注释也收到集合，且去掉User-Agent分组、Allow和原URL。单词包含匹配与有效robots指令不同，通配/末尾$是模式而非已存在的实际端点。

[RFC9309](https://www.rfc-editor.org/rfc/rfc9309.html)定义注释、组和路径匹配，并明确规则不是访问授权。按原文件/哈希/时点、group/product-token、指令与模式保留来源，区分有效规则、注释及无组条目；去重不能丢宿主归属。路径只作正式范围内候选，不证明私密内容可读，本批未执行HTTP管线或读取候选。来源：[保存帖](https://x.com/i/status/1409762861115576322)。'''),
('by-type/xss.md','代理修改响应与服务端反射的证据边','''旧一分钟XSS步骤混写intercept response和在request尾加HTML。若仅在自己代理里改响应，浏览器弹窗可能完全来自本地注入；不能将其作为服务端可控输入到其他读者的证明。

保存修改前后的原请求/响应、实际改动方向/生效规则和不修改响应的正常对照，沿真实输入/输出上下文及读者能力核对。仅调试者看见脚本、本地override或错误页固定模板都是反例；参数名redirect_uri也不自动说明OAuth消费者。本批没有修改浏览器流量或执行载荷。来源：[保存帖](https://x.com/i/status/1409494340020342786)。'''),
]
ids={pid for row in json.loads((W/'batch-0103.json').read_text()) for pid in row['post_ids']}
urls=[pid for _,_,body in facets for pid in re.findall(r'https://x\.com/i/status/(\d+)',body)]
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
