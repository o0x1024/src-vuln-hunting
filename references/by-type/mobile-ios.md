# iOS 应用条件专题

触发：获准 IPA、源码、entitlements、正常流量或测试设备。先记录 Bundle ID、签名/Team、版本/构建号、iOS/设备、包来源/哈希、调试/重签/越狱状态。不能用 HyperOS 的核心业务、补丁字段或守护计划资格为 iOS 定级；小米项目具体适用性未知时记 rule_review。

## 从材料到最小验证

| 线索 | 假设与对照 | 必要限制 |
|---|---|---|
| URL scheme、Universal Link、文件/分享扩展 | 外部输入是否绕过内部登录/对象授权；用自建链接和两个受控身份对照最终数据/状态 | 打开页面不是绕过；关联域声明需结合实际系统路由/应用版本，未读取线上文件不声称已验证关联 |
| WKWebView 与原生消息桥 | 跟可控来源、导航、消息参数到敏感原生方法，在获准版本中观察无害结果 | 桥存在/允许 JS 不证明可达利用；不能为触发而重签修改原权限后隐去准备条件 |
| Keychain、App Groups、共享容器、文件保护 | 核对 entitlement、共享身份、锁定状态、真实调用者能否读取合成私有标记 | 合法同组共享或越狱 root 读取不自动是跨 App 漏洞；不同保护配置只是线索 |
| 网络信任/ATS、token 与会话 | 用原版配置核对正常与不受信任连接及实际敏感后果；服务端权限单独验证 | 缺 pinning/ATS 例外、自己安装 CA 后可抓包不自动成立 |
| 本地认证、注销与敏感操作 | 确认保护的是 UI、密钥访问还是服务器动作；比较授权前后/注销后的真实结果 | 在调试器中把返回值改为 true 不证明普通攻击身份可跳过保护 |
| 解析器/native crash | 保存获准输入、版本、调用链和隔离环境结果，再查对应版本机制 | 崩溃不等于 RCE；模拟器/越狱结果不能自动推广正常真机 |

普通第三方应用受沙箱和签名 entitlement 约束，因此研究者的观测权限必须与攻击者前提分开。包加密、无符号或无设备只阻塞所依赖的分析/动态分支，不以“无发现”代替未测。静态可疑配置先形成候选，已有服务端 API 证据可继续独立评估。

每轮选择一个真实可达输入及正常对照；保留调用者、原版环境、操作前后状态和实际交互。测试账号/标记、有限请求与恢复规则沿用 [实验设计](../experiment-design.md)。不自行重签、越狱或修改用户设备；已有明确许可的准备记录如实保留。

交付版本/签名、设备与 OS、实际入口/调用链、entitlements 证据、攻击与准备权限、复现材料及未覆盖模块。受理、奖励、技术影响分别判断。隐私合规线索需要对应地区/业务的有效规则，不把一般隐私建议直接认定为法律违规或安全漏洞。

资料：[Apple 运行时安全](https://support.apple.com/en-au/guide/security/sec15bfe098e/web)（读取沙箱与 entitlements 部分）、[MASVS](https://mas.owasp.org/MASVS/)（读取控制组概览）。这些仅支持边界与覆盖方向，具体 OS/API 行为在执行前按目标版本核对；未宣称已读所有关联域、Keychain 或 ATS API 文档。[来源登记](../research/sources.json)，2026-09-17。

## 历史IPA获取与制品观察

历史桌面工具截图提出下载/导出IPA并解包，但不能由解包成功认定取得完整可读源码、解密成功或动态测试覆盖。只处理获准且来源可核对的制品，记录包哈希、版本、成员与可读范围，区分资源/配置、可分析二进制和仍受加密/设备条件限制的分支。旧工具名称、菜单路径及TestFlight支持断言保留为历史信息，未核对当前官方能力时不安装工具或承诺任意应用均能导出；独立的正常流量/API证据仍按自己的覆盖记录判断。

## 深链导航与WebView能力

深链把url参数导航到外部网页，首先证明导航行为和调用者可达性；没有转发认证请求头，只能说明这一项未观察到，不能排除Cookie、脚本注入、消息通道、原生bridge或其他应用状态，也不能反过来认定这些能力已泄露。

记录真实应用/OS版本、外部入口、初始与重定向后的URL/origin、WebView配置和原生授权操作。每个导航/读取/消息/原生动作分别接边，只有权限或秘密跨越了不允许的边界才升级影响。截图New/Still being assessed只证明报告状态，不证明账号接管；没有受控能力证据时如实交付导航限制，不诱导用户打开深链或强行构造数据外传。

## 兼容规范化产生路径分隔符的Host-Split候选

源文将iOS13Memo链接中的℅转换称NKFD，正确形式名为NFKD。用自写离线Unicode字符串转换核对：aapl.c℅在NFKC和NFKD均变为aapl.cc/o，NFC/NFD保留原字符。[UAX15](https://www.unicode.org/reports/tr15/)区分兼容与规范分解（2026-10-09核读相关说明）。这是纯文本转换证据，不是iOS实际算法/导航行为证据。

关联自动链接识别、显示内容、规范化时点、authority/path拆分、复制/预览与实际打开URL；若先对整串做兼容转换，新增斜杠可能改变主机/路径划分，而先按组件解析后拒绝非法字符有不同结果。原图仅Memo地址和CVE编号，无厂商产品/版本绑定证据，未读取视频全过程。不测试用户设备/导航外站或把旧iOS声明归为当前浏览器普遍漏洞。


## Mach-O规则匹配与真实注入的证据层

MaliciousBitHunter结构图从FAT/ARM/ARM64、头、加载命令、类/方法/字符串、符号到签名与导入导出，并用CLlocationManager、method_implementation、hooklbs等作规则线索。匹配字符串或显示某结构不证明该架构实际加载、运行时方法替换或恶意行为；图列签名字段也不等于验证通过。

先绑定获准制品哈希、来源/签名身份、架构切片、解析器版本与完整性，和可信同版本基线比较，再用既有受控动态证据定位实际加载/调用。合法SDK、调试符号、未使用字符串和解析失败分别作反例/未知项，不能把未匹配计安全。本批仅审结构图，没有执行应用、动态钩子或签名工具。来源：[保存帖](https://x.com/i/status/1403702804355637249)。


## iOS扫码入口的URL分派与脚本消费者

二维码提示本身不证明iOS扫码应用会导航javascript scheme。先区分扫描器返回文本、调用方URL过滤、打开外部应用以及WKWebView实际导航/脚本消费者，不能借Android推断iOS权限。

仅在获准制品材料中绑定系统/SDK版本、用户交互、实际origin和bridge暴露；文本展示、scheme拒绝或系统外部浏览器是反例。两张同类提示图均已看，仍不补实际设备测试，本次未扫码或执行脚本。

来源：[保存帖1](https://x.com/i/status/1411287363112902656)、[保存帖2](https://x.com/i/status/1645396728357564418)。


## 同一消息在Web与iOS WebView的渲染差异

正文称消息过滤后Web未触发，却在iOS App WebView触发。存储字段相同不保证所有客户端使用相同净化、HTML解析和权限环境。

关联受控消息ID/原始与保存字节、各读者的版本、模板/sink、origin、脚本开关和native bridge能力；比较同份输入。不同消息、普通文本、仅打开UI或无原始链条是反例；脚本触发不自动等于native权限、任意文件或接管，未操作设备。

来源：[保存帖1](https://x.com/i/status/1425674198605721606)。


## iOS采集层与哈希输出选项的证据合同

MEAT帮助分别列logical AFC jailed和filesystem path，以及md5/sha1和输出选项。

先记录设备授权、采集访问层、路径与时间、每制品hash和完整性限制；选项存在、单文件hash、jailed视图或缺受保护路径是反例。不能把logical采集自动计完整设备/密钥链提取，未连接设备或采集用户数据。

来源：[保存帖1](https://x.com/i/status/1431968519407771649)。


## iOS 思维导图的客户端与服务端权限

完整图列本地文件、备份/日志、Keychain、URL schemes、WebView、认证、第三方库与通信，资源卡标July2020。

按当前版本/构建和实际消费者审查每类数据的存储、读取身份、外部调用与服务器保护能力。客户端patch或关闭pinning仅改变自有设备行为，不证明服务端越权；正常本地数据、模拟环境、正确验证和历史教程失效为反例。只提方法，不改设备、抓第三方凭据或执行旧教程。

来源：[保存帖1](https://x.com/i/status/1460981739338170369)、[保存帖2](https://x.com/i/status/1461123750733221899)。


## 生物认证 boolean 与服务器凭据

正文建议Objection把本地False改True，没有实际服务端动作。

追踪本地UI决策、Keychain/受保护密钥操作、secure enclave及服务器credential验证，在自有测试App比较显示与真实能力。只界面解锁、服务端拒绝、密钥操作依然受限为反例；本地控制不自动证明账号接管，不注入真实App或使用密钥。

来源：[保存帖1](https://x.com/i/status/1479127910476763141)。


## iOS 测试主题清单与可解密流量证据分开

正文列架构、样例app、proxy/jailbreak、检测/pinning与敏感暴露方向，没有证书、配置、请求响应或绕过结果。

离线自有应用按OS/app版本、测试身份、代理路径、信任链、pinning实现、数据存储和允许行为建证据清单。代理启动/菜单选项不等解密，越狱也不保证绕过pinning；未可见流量/无敏感字段为反例，不修改真实设备或读取私人数据。

来源：[保存帖1](https://x.com/i/status/1501709418068680706)。


## iOS 静态检查按具体数据消费者建模

保存图的静态项包括 React/Flutter 生态、混淆、client ID/token/key/password/device UUID、MD5/SHA-1、SQL/反序列化、WebView JS/debug/证书错误、URI handler、备份/日志、检测/pinning、资源/权限/第三方库、Info.plist、Universal Links、UIActivity/UIPasteboard、扩展/键盘及 ATS。记录自有包签名/版本、配置与各字段的实际消费者，区分公开 ID、测试值与秘密，哈希的用途不能只由算法名判危。静态可见配置需与实际授权/存储行为对应，代码混淆、客户端检测和 pinning 不能代替服务端身份校验；不安装图列未知工具或执行包代码来补造结果。

来源：[保存帖1](https://x.com/i/status/1611803315565891584)。

已实际查看保存图片 `1611803315565891584-02.jpg`：完整iOS图静态：React/Flutter生态、混淆、clientID/bearer/APIkey/password/auth/deviceUUID、MD5/SHA1用途、SQL参数化/反序列化、WebviewJS/debug/SSLerrors、URIhandler/backup/logs/rootdetect/pinning/assets/permissions/thirdpartylibs/Info.plist/universal links/UIActivity/UIPasteboard/extensions/keyboards/ATS。动态logs/jailbreak/pinning/TouchFaceID/hiddenfunc/keyboardcache/screenshots/URLdeep links/runtime/Webview/input/access/storage/encryption/copypaste。工具MobSF/Hopper/idb/iFunbox/otool/libimobiledevice/BinaryCookie/Backupextractor/Xcode/codesign/ipainstaller；Frida/Objection/Burp/ondevice/CodeShare/Clutch/strings/Snoop/Filza和jailbreaktweak列表。Dios候选→确切版本/配置/消费者/身份/服务端边界，自有样本无安装未知tweak/运行原脚本，不把clientID/MD5/绕过客户端检测等同服务器认证旁路。


## iOS 动态检查分清设备解锁与服务端权限

保存图的动态项是模拟器日志、越狱/pinning/TouchID/FaceID、隐藏功能、键盘缓存、截图、URL schemes/deep links、运行时/WebView、输入/访问、存储/加密与复制粘贴；工具仅是观察手段。以自有测试身份和合成数据记录设备状态、OS/应用版本、入口及最终操作，分别验证本地门禁、敏感视图、秘密句柄和服务器授权的正负例。绕过本地检测、存在缓存/剪贴板或能调试并不自动产生远端接管；不获取他人设备数据或安装未知越狱 tweak，图中工具列表不作为今天可用性/必要性声明。

来源：[保存帖1](https://x.com/i/status/1611803315565891584)。

已实际查看保存图片 `1611803315565891584-02.jpg`：完整iOS图静态：React/Flutter生态、混淆、clientID/bearer/APIkey/password/auth/deviceUUID、MD5/SHA1用途、SQL参数化/反序列化、WebviewJS/debug/SSLerrors、URIhandler/backup/logs/rootdetect/pinning/assets/permissions/thirdpartylibs/Info.plist/universal links/UIActivity/UIPasteboard/extensions/keyboards/ATS。动态logs/jailbreak/pinning/TouchFaceID/hiddenfunc/keyboardcache/screenshots/URLdeep links/runtime/Webview/input/access/storage/encryption/copypaste。工具MobSF/Hopper/idb/iFunbox/otool/libimobiledevice/BinaryCookie/Backupextractor/Xcode/codesign/ipainstaller；Frida/Objection/Burp/ondevice/CodeShare/Clutch/strings/Snoop/Filza和jailbreaktweak列表。Dios候选→确切版本/配置/消费者/身份/服务端边界，自有样本无安装未知tweak/运行原脚本，不把clientID/MD5/绕过客户端检测等同服务器认证旁路。


## iOS 自定义 URL scheme 与授权码消费者的分离

历史Shop报告把iOS Xcode登记scheme与Android intent并列；自定义scheme声明不是唯一所有权保证，但是否劫持要看实际系统路由/用户选择、Universal Link验证和交易上下文。用自有测试app确认callback抵达谁、code能否被错误verifier消费及token主体，区别链接可接收与账户资源可访问；存档无当前OS/应用版本，不称当前普适接管。

来源：[保存帖1](https://x.com/i/status/1631414207223672832)。

现有图片证据 `1631414207223672832-02.jpg`：Shopify Shop/Outlook历史摘要称恶意app可截取自定义deeplink授权code，工程师加PKCE缓解；依赖callback劫持与code兑换，普通URL可见不等于可兑换。


## iOS AES hook 失败要定位运行时实际调用点

正文只是Frida hook crypto/AES三天失败求助，没有代码或异常。先在许可自有应用确认架构、符号/模块、ObjC/Swift/原生桥与是否走硬件/封装实现，记录调用栈、参数生命周期和受控测试向量。没有hook命中可能是错误进程/路径/时机，不证明无加密或可解密全部流量，不收集真实密钥。

来源：[保存帖1](https://x.com/i/status/1635324871889793025)。


## 群聊非法密钥的崩溃条件要落到客户端消费者

LINE摘要称无效E2EGroupKey在群内共享，再收到用该key加密的消息使iOS客户端崩溃，引用历史CVE-2022-41568。核对版本、入群权限、密钥/消息校验、异常处理与恢复边界，用隔离测试状态审查。截图当前Low及历史High变更都不证明服务端DoS或当前仍受影响，缺具体key不构造负载。

来源：[保存帖1](https://x.com/i/status/1640889303059275777)。

现有图片证据 `1640889303059275777-02.jpg`：LINE iOS 群聊摘要：非法 E2EGroupKey 与使用该 key 加密的消息使客户端崩溃，引用 CVE-2022-41568；当前截图 Low、300 美元，历史有 High 变更。缺具体 key、版本与恢复路径，不推定服务端 DoS。


## Android 线索迁移到 iOS 要重建客户端及后端边界

保存帖建议在 iOS 重复 Android 的发现，续篇并不完整。把原线索视为假设，核对 iOS 构建、账号/对象、后端路由与请求字段，以及沙箱、系统权限、WebView/链接处理等实际消费者。两平台同品牌或外观功能相同不证明接口、权限和状态机一致；需要自有账户/设备动作及请求结果，不能复制原参数就宣称跨平台成立，也不补造未保存的前序步骤。

来源：[保存帖1](https://x.com/i/status/1648342426548047873)。


## iOS bundle、容器与插桩返回值的身份边界

保存 iOS 表列 bundle ID、应用 bundle/data UUID 目录、Frida/Objection、文件观察和 NSLog。UUID 容器路径与 bundle ID 不同，动态注入要求设备/进程权限，方法返回值替换仅改变本地客户端。保留二进制 hash、签名/entitlement、设备权限和原行为对照；要证明认证漏洞仍需服务端受保护请求，不安装归档 repo、不把 root 下操作推广普通设备。

来源：[保存帖1](https://x.com/i/status/1653808994270736384)。

保存图片 `1653808994270736384-03.jpg`：iOS forensiccheatsheet USB备份加密/解密Manifest.db映射与data/log/network/config artifacts；自设备权限、加密口令与提取时间分别记录，无备份取得≠远程漏洞。 本段只使用已保存且实际查看的内容。

保存图片 `1653808994270736384-04.jpg`：iOSassessment root/Fridaappinfo/container paths/Objection返回值替换/NSLog；UUID目录非bundleID，插桩修改返回值非serverauthbreak。 本段只使用已保存且实际查看的内容。


## iOS 备份取证先绑定加密、时间和 Manifest 映射

保存 forensics 表区分 USB 备份、加密/解密、Manifest.db 及 data/network/config/log artifacts。仅对自有或明确授权设备备份，以 Manifest 映射、domain/path、文件 hash 与采集时间关联最小证据，保护密码和个人数据。具备设备信任与备份口令的提取不等远程泄露；不同版本路径/字段可能变化，历史配置或访问记录不是当前活动事实。

来源：[保存帖1](https://x.com/i/status/1653808994270736384)。


## 跨 frame 原生桥接须验证调用 origin、UI 提示和最终脚本上下文

Brave iOS 历史报告描述三个条件：跨源 subframe 可直接调用 U2F.postMessage；FIDO 提示显示顶层 frame 的 origin；消息 version 未转义进入 evaluateJavaScript。组合后可能让子 frame 控制顶层执行内容。记录真实调用 frame、origin、桥接权限、字符串转义、UI 所示身份与最终执行 frame，用自有跨源测试页和无害标记逐层对照；设备触碰及注册流程是原文前提，不能改写为零交互。图仅归档旧版本摘要、无演示视频，不能推到当前所有 iOS 浏览器；保持 origin 绑定或安全参数传递会切断链条。

保存图证 `1672310299909562382-02.jpg`：历史 U2F 桥接摘要同时涉及子 frame、提示 origin、未转义 version 和设备触碰。

来源：[保存帖1](https://x.com/i/status/1672310299909562382)。


## 解包 IPA 的模板命中需验证秘密用途

正文建议解包 ipa/decrypted.ipa 后用 mobile Nuclei 模板找硬编码敏感数据。先确定合法获取的应用版本、包与可读代码/资源范围，记录扫描路径、模板版本、未解密部分和结果；字符串前缀或 SDK 公开标识不等可用秘密，权限/绑定须来自明确业务证据，不用泄露材料登录服务。仓库和模板全文未保存，不补配置或覆盖声明。

来源：[保存帖1](https://x.com/i/status/1686286463367843840)。


## 移动工具按静态动态代理及设备权限选择：iOS（2023保存案例）

移动测试工具图将静态分析/逆向APKTool/Qark/MobSF、动态Frida/Droidbox、代理Burp/Ratproxy、ADB和iOS日志/流量/动态工具混列；称APKiD检测恶意包不准确，指纹识别不等同恶意判断。先按包/平台/系统版本/测试目的选择，再验证实际可观察行为，ADB/内存dump需自有设备及权限，不运行远控工具。

图片证据：`1689974539009347585-02.png`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689974539009347585)。


## 保存图证0188-106-ios：机制与验证条件

PowerShell脚本用Frida列PID/Identifier并要求目标Identifier，底部注入/返回裁切。需自有设备/指定进程和具体检测函数对照；枚举进程不证明Universal越狱检测绕过，也不是服务端认证绕过。 可用原图：`1695888020577333656-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1695888020577333656)。


## 本地越狱检测与解密应用来源的验证范围（0188）

Frida/PowerShell 可先选择自有设备中具体 bundle/process，再比较检测函数返回和应用行为；列 PID 不证明全部机制可绕过，更不代替服务端鉴权。下载站提供的解密应用链接没有保存构建/来源证明，应优先合法持有的原始应用、版本和字节摘要；不安装、运行或信任未知包，不将站点存在当已完成逆向。

来源：[保存帖1](https://x.com/i/status/1695888020577333656)、[保存帖2](https://x.com/i/status/1696517581879095350)。
