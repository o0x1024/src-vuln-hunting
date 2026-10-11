# Android 应用与系统权限边界

适用信号：授权 APK/源码、Manifest、外部组件/链接、WebView、IPC、敏感存储/网络/更新、系统权限或原生代码线索。小米项目另读 [MiSRC §4.3](../policies/xiaomi-misrc.md)；iOS 读 [独立专题](mobile-ios.md)，不把 HyperOS 分级移植过去。

## 环境与攻击身份

保存 APK 来源/哈希/签名、包名/版本、targetSdk、设备型号、系统构建指纹/补丁日期、WebView 版本及权限设置。最新版要求、厂商/原生/三方组件、开发/稳定 ROM 按项目核对；只有旧版本证据时不声称最新版受影响。模拟器结果不能覆盖未具备的硬件、TEE、基带和厂商服务。

区分研究准备与攻击前提：ADB、调试证书、代理 CA、Frida、root/解锁 bootloader 可以帮助观察，但最终需记录普通第三方应用/网页/近场/物理攻击者实际能获得什么。准备者关闭校验后抓到自己的流量，不证明原版客户端漏洞；观察工具的存在也不能否定在默认环境独立复现的真实缺陷。

## 检查与最小实验

离线解析已授权 APK，记录包名、签名、版本、targetSdk 与组件权限。用 Manifest→导出组件→入口参数→敏感代码建立候选表，再选有具体边界线索的入口在自建设备/模拟器验证。

对 APK 容器直接运行字符串检索只适合快速产生候选。压缩条目、编译资源、字符编码和动态构造可能使地址/配置未出现在该视图；无命中不代表包内没有相关引用。需要补证时在离线、有限大小的已授权样本中解析具体资源与代码位置，保留条目、转换方式和原件哈希；匹配 Firebase/S3 名称不直接证明云权限或秘密泄露。

深链接核对 scheme/host、App Links 验证、参数校验和应用内认证状态。显式 Intent 能打开 Activity 与能绕过其内部权限不同；ADB/shell 身份可能比普通第三方应用有更多能力，最终证据应匹配实际攻击者身份。

## 证据与反例

exported=true 可以是正常产品需求；风险在普通外部调用者获得被禁止的数据/操作。启动器组件、正常深链接、离线发现敏感类名都不是接管证明。

## 其他条件分支

| 入口/线索 | 最小对照与证据 | 不应推导的结论 |
|---|---|---|
| Provider、Service、Broadcast、Binder/URI grant | 跟随调用者 UID、组件权限、授权 URI 与资源所有者；用无特殊权限测试 App 对比合法身份对受控数据/动作的访问 | shell 调用成功不等于任意 App 可利用；组件启动不等于内部鉴权失效 |
| WebView/JS Bridge、消息通道 | 关联可控页面/iframe→桥方法→原生敏感能力，核对来源/导航/角色与真实结果；正常可信页作对照 | 加载任意网页不等于任意代码执行；桥存在不等于恶意页面能到达 |
| 存储、日志、备份、截图/通知/剪贴板 | 找到实际可读者和受保护数据，用合成私有标记验证对应系统版本下的可达性 | 自己私有目录中的明文、root 后读取或 allowBackup 配置本身不证明越权 |
| TLS、身份凭据和请求签名 | 保留原版证书/信任配置与网络前提；在获准环境对照正常连接与不受信任连接，观察身份凭据是否实际泄露/被错误接受 | 缺 pinning、用户安装 CA 或 Frida 关闭校验不自动成立；客户端签名可计算不等于后端授权缺陷 |
| 更新、动态加载、文件导入或 native 解析器 | 从真实可控输入跟到验签/加载/执行；隔离环境以无害标记观察实际能力和进程权限 | 下载 HTTP、缺混淆、重打包、单次 crash/CVE 名称不直接证明代码执行 |
| 应用锁、系统权限、特权服务、SELinux/TEE | 列出初始身份、用户交互、权限域和被突破的规则；已有获准最小结果与正常拒绝对照 | 普通 App 权限不等于 system/root；解锁自有测试机不证明远程锁屏绕过或 TEE 数据访问 |

App 调后端产生的越权按 [访问控制](idor-access-control.md) 验证服务端身份与状态；不因入口来自 APK 重复创建客户端漏洞。近场协议/设备侧问题按 [IoT](iot-security.md) 或项目系统专题处理，原生内存/驱动线索需要对应版本的专门分析与获准隔离环境，不能仅从崩溃断言可利用性。

设备名称、联系人、应用反馈等可写字段还可能同步到 Web 控制台、邮件或客服后台。用唯一无害标记跟踪客户端写入→云端存储→实际展示消费者，分别记录写入身份和查看角色；客户端本地转义不能证明后台也安全，尚未到达消费者也不能确认 XSS。具体上下文按 [XSS](xss.md) 核对。

## 推进、停止与交付

先按静态位置筛选一个可达入口，再用正常环境建立基线、普通攻击身份做一个有判定结果的实验。只解析 APK 时覆盖为静态分析，缺设备/身份/日志的动态项保留 blocked；其他已获准分支继续。无稳定结果时定位版本、会话、时序或观察限制，不无限重试。

记录每次权限弹窗、点击、安装与网络条件，不把测试准备交互混进受害者实际交互，也不能省略攻击所需安装。任何设置、测试 App 和代理变更仅在既有许可内进行并记录恢复；不为证明等级制造设备不可用或访问真实隐私。

报告包括调用链、初始/最终权限域、受控数据/状态证据、版本/签名、复现条件及平台所需 PoC/源码/APK/视频。技术已确认但小米强制视频/版本材料缺失时，保留 confirmed，提交材料为 needs_evidence，不假装附件已经生成。

## Agent 行为

X 帖子提供“静态筛选后动态验证”的线索，相关工具本身未评估，不执行帖子给出的未知软件。解包/反编译可自动化，操作参数和影响仍要核对。本专题提供按线索选分支的方法，不代表已覆盖全部移动端或已具备原生/硬件利用能力。

## 调研来源

- [Android-exported · android:exported](https://developer.android.com/privacy-and-security/risks/android-exported)
- [Android-links · Unsafe use of deep links](https://developer.android.com/privacy-and-security/risks/unsafe-use-of-deeplinks)
- [Android WebView native bridges](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges)
- [OWASP MASVS 控制组](https://mas.owasp.org/MASVS/) 用于查覆盖缺口，不能把每个加固项当成 SRC 漏洞。

导出组件/链接资料核对日期：2026-09-14；桥接与 MASVS 核对日期：2026-09-17。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

混合应用的离线资产可能提供单独的脚本 bundle。对获准样本记录归档条目、原始哈希、实际内容类型与构建版本，再选择只读提取/格式化并保留位置映射；文件名或扩展名不保证内容是可读脚本，格式化成功不证明恢复了全部客户端逻辑或后端实现。截图中的特定 assets 路径与工具版本仅为该样本线索，不作为所有 React Native APK 的固定布局或无需验证的两步流程。

代理中未见 PIN 校验请求，先保留观察缺口并检查获准的真实流量/代码路径，不能据此推断 PIN 必存本地。若发现本地状态文件，记录默认权限、实际读写者、缺失/修改后的消费者和受保护能力；root/调试身份删除自己的文件属于实验准备能力，不证明普通外部主体能解锁原版应用。只在隔离自有数据上核对并恢复，不以删除生产状态替代边界证据。

卸载再安装后仍显示登录状态，先区分本地页面/数据库、系统备份恢复、SSO重新签发和原凭据仍有效；清缓存后变成登录页也只说明某客户端状态改变。[Android Auto Backup恢复时序](https://developer.android.com/identity/data/autobackup#RestoreSchedule)（2026-10-09核对）说明应用安装时可能恢复符合配置的数据；记录设备/系统/目标SDK、备份与迁移配置及实际恢复路径，不能把所有重装视为无状态新客户端。仅在自有测试环境核对原凭据和新凭据的归属及服务器受保护操作，不清真实设备数据；服务端撤销继续按[认证生命周期](authn-session.md)判定。

历史APK用于恢复已被新版隐藏的端点/字段/凭据线索时，按版本保留来源、原件哈希/签名、组件与引用位置，形成旧/新客户端到当前后端契约的对应表。离线字符串或旧版可安装不证明端点当前可达、凭据有效或最新版受影响；优先比较获准源码/流量和自有账号的有效基线，再对同一对象、操作和保证做版本差异对照。旧协议仍可用可能是合法兼容，需明确服务端要求失效或已禁止的能力。旧包分发可信度、下载/安装许可和动态实验环境另核，不使用遗留生产秘密，不按作者P1/周耗时补影响。

## 原生库strings与端点授权线索

APK的lib目录中.so字节可含URL、IP、字段或疑似token，但strings结果是静态候选，不能据“unauthenticated endpoint”标题认定当前接口免认证。保留获准制品哈希、应用/架构版本、库来源、字符串偏移与调用关联，区分示例文本、失效值、普通标识和真实凭据；正则不能恢复全部网络协议或运行时拼接。

源命令把http://libapp.so写作输入，不能默默当已存在的本地库文件或下载它。只有当前获准流量/源码能绑定调用、实际身份和端点受众时再提出有限权限对照；不消费提取到的未知token、不连接图中IP或仅因反编译成功登记越权。

## 动态钩子与应用原有加载能力

hook File.exists只观察被仪器化进程检查的路径，不证明该文件实际存在、可被普通攻击主体写入或会被加载执行。看到.so字符串与ZipFile调用也不能独立建立“任意代码执行”；源帖停在2.1，后续路径、对象来源和加载过程未提供。

在获准源码/已有脱敏轨迹中关联压缩包来源与可控性、条目到规范化落点、写入主体/目录权限、真实加载器/时点及应用身份。root、Frida/Xposed或重打包后的仪器权限与未修改应用的攻击能力分开；没有后续证据就保留缺口，不修改用户设备、注入进程、写恶意.so或运行未知动态库。

## CharSequence携带样式的消费边界

TextView.setText接收CharSequence时，输入可能是普通String，也可能携带Spanned样式。[Android样式资源](https://developer.android.com/topic/architecture/views/resources/string-resource-views#StylingWithHTML)展示Html.fromHtml得到Spanned；[Spans说明](https://developer.android.com/develop/ui/views/text-and-emoji/spans)区分文字与标记并说明样式可含点击行为（2026-10-09核对）。这不是浏览器HTML/JS解释器。

跟外部调用者→导出组件/权限→Intent extra实际类型及IPC转换→保留的span→TextView/链接处理器与敏感动作。源帖单行getCharSequenceExtra不能证明普通外部App可达，也不能自动认定XSS/任意代码执行。用自有隔离样本的无害文字/样式观察是否能改变受保护UI或跳转，记录系统/目标SDK、真实交互和处理器；不构造可执行恶意span或调用用户设备。

## 反编译匹配行与真正网络消费者

APK提取图的file:line:match混合文件路径、SDK/广告库、示例域名、网络候选及/proc等本地资源；每一行不是同等的实际API入口。保留原APK哈希/版本、反编译阶段、文件/行号、所属模块、字段角色与引用关系，不把底部裁切、旧工具banner或decompile complete当全部覆盖。

先以获准本地制品和已有运行日志确认匹配字符串是否到达真实网络调用、配置替换及用户可达分支；再独立核对服务当前归属/授权。示例、死代码、第三方SDK及本地文件路径是必要反例；不运行来源工具、解包未知下载、读取设备私密文件或将所有字符串批量请求。

## BROWSABLE类别与实际入口解析

Manifest含BROWSABLE只给出一个intent类别条件；还须检查action、data的scheme/host/path、exported、权限、真实调用方式与最终URL消费者。[Android intent过滤说明](https://developer.android.com/guide/components/intents-filters)区分类别匹配和显式intent，并说明action/data/category测试及导出边界（2026-10-09核读相关段落）。浏览器可达、任意外部组件可达和能触发敏感动作是不同结论。

从已有同版Manifest/代码跟踪解析后的输入、登录主体、WebView/导航或业务处理器，再用获准隔离普通链接验证单一分支。反编译后的类别搜索不证明每个入口都可利用；设备安装、ADB调用和真实账号动作不从静态审查继承许可。

## 全局代理设置与实际应用网络路径

ADB修改global http_proxy属于设备状态写入，不是读取流量或授予测试许可。代理地址端口设置成功与应用实际采用该配置分开；记录应用网络库/进程、直连或代理路由、TLS信任链、主机名校验、证书固定及观察端的对应请求，不由无日志判定无网络请求或证书验证可靠。

只在获准隔离设备的具体动作计划中保存原值、有效范围、证书配置与恢复方式；shell/调试身份和未修改客户端的普通攻击能力分开。本次仅提炼命令语义，不调用ADB、修改用户全局代理或安装CA。

## 有效TrustManager与主机名校验分支

空checkServerTrusted或异常被吞掉是证书链验证候选，但要先确认该TrustManager被实际连接工厂/网络库使用，而非死代码/调试分支。证书链、主机名校验、固定策略及攻击者可达网络位置分别核对；改包、hook或准备者关闭校验之后抓到流量不证明原客户端缺陷。

[Android TLS说明](https://developer.android.com/privacy-and-security/security-ssl)指出无检查TrustManager的风险，并说明直接使用SSLSocket时主机名验证要独立处理（2026-10-09核读相关段落）。在获准同版源码和既有脱敏轨迹中绑定原版实际消费者、合成数据和校验结果；历史论文链接与IoT类比不是所有设备当前受影响的证据，不拦截真人凭据。

## Android堆转储的身份、时点与秘密消费者

源图将进程列表中的PID传给am dumpheap，再pull一个hprof文件；只能证明该图所示采集动作和输出文件，未展示其中存在密码、算法密钥或可用凭据。关联应用包/进程及其代际、构建/调试条件、采集身份权限、采集时点和文件完整性，再区分测试常量、短期缓存、密码输入、真正加密密钥和当前会话秘密。

优先审查获准既有脱敏转储/源码中的对象来源、生命周期、使用API和可重用的权限，不凭文本匹配认定堆字符串就是有效密钥。调试/root权限读取与普通远程攻击者能力分别记录；实际秘密是否应能抵御该权限按应用契约判定。只静态提炼截图，不连接设备、dump进程、导出真人内存或尝试秘密解密。

## 离线重启的应用挑战与服务端因素状态

源图叙述断网、强制停止、重启、恢复网络后没有再次显示2FA。先区分本地应用锁/提示、已有已验证会话的缓存、挑战生命周期及服务端真正MFA策略；消失的对话框不自动代表新的未认证身份绕过因素。

在获准离线材料或隔离自有样本中关联重启前凭据、持久化字段、进程/挑战代际、离线与重连状态、后台刷新及新受保护API的真实接受结果。若仍用已合法签发的会话或仅浏览缓存页面，应按实际契约描述；需要新的服务端因素却被未验证身份取得能力才支持该边界。此次不连接/强停用户设备、改变网络或真人安全设置。

## Flutter流量与泛用TLS钩子的观察缺口

旧图代理中有Dart/2.10的GET，旁边泛用Android脚本多数pinning类not found，仅显示TrustManagerImpl bypass。类别没找到只描述该观察器所查路径，不能证明应用没有证书固定，也不证明Flutter的真正连接被这些Java钩子覆盖。

绑定APK/引擎构建、进程/ABI、真实网络库、路由/代理与TLS消费者；一条请求还须关联合法UI动作、时间和原版信任行为。已有获准源码/脱敏轨迹用来辨别Java与原生路径及观察遗漏，准备者改校验后抓到流量不当原客户端漏洞。文章全部实现未读，不安装CA、运行Frida脚本、重打包或修改用户设备。

## 非root注入Gadget与被改变的APK

旧帖frida-non-root将Gadget注入APK并要求更新/res。无需root不等于无需重打包、签名变更、加载路径或ABI适配；被研究者改造后的应用是新的观察制品，不能仅由它可Hook认定原版普通外部攻击者可获得同样能力。

在获准已有材料记录原件与改造件哈希/签名、包/版本、Gadget版本/ABI与加载点、平台策略和观察前后差异。与环境/攻击身份条目合用，部署/应用信任变化另记。来源链接全部实现未读，不安装Gadget、修改APK、运行Frida或改变用户设备；CiLocks图的猜码/root/Reset Data菜单也不证明所有OS支持，更不作为准备动作默认许可。


## APKLeaks候选、制品版本与正式资产范围

APKLeaks图以jq/LinkFinder提取链接并建议添加targetscope及比对旧版本。每个字符串绑定APK哈希、版本/签名、提取位置及解析规则，区分第三方SDK、示例/废弃地址与真正运行时网络消费者；工具名或secret标签不证明凭据有效。

静态找到域名只扩候选，需独立核对当前归属及正式允许资产/动作，不能直接扩大范围。旧版本差异需可信完整制品及归一规则，不把多尺寸同图算独立发现。本批没有下载APK、运行反编译工具、访问候选或复制秘密。来源：[原帖](https://x.com/i/status/1403316204337520647)、[转述](https://x.com/i/status/1403328432939966466)。


## CA转换、设备写入身份与应用信任

旧图导出Burp DER、转换PEM、计算subject_hash_old，再用样例文件名复制system cacerts并remount/reboot。哈希输出对应文件名需当前证书，不能硬抄示例；主机命令与设备shell权限不同，图中混合调用也不能默认都在已授权root设备上成功。

固定Android/设备版本、真实证书指纹、有效信任库位置、应用网络安全配置/TLS栈、代理链和pinning行为。安装成功、系统信任、应用信任和可见明文分别核对，现代只读分区/有效证书库布局也需实际环境；只审图，不挂载分区、推证书、重启设备或绕过应用校验。来源：[保存帖](https://x.com/i/status/1405160059399671811)。


## Flutter kernel制品与strings输出的源码分母

图展示assets/flutter_assets/kernel_blob.bin与strings输出文件output.dart；扩展名并不把可打印字符串重建成完整Dart源码，像素模糊的代码行也不能恢复秘密。[Flutter构建模式](https://docs.flutter.dev/testing/build-modes)区分调试与优化/去调试信息的发布模式，但不能由文件名断言所有制品模式或格式。

绑定获准包哈希/签名/版本、构建模式、架构与实际格式，区分结构解析、字符串片段、生成代码和完整源码集合；发现键名/地址还需真实消费者及当前能力。没有运行strings、反编译、下载应用或调用秘密。来源：[保存帖](https://x.com/i/status/1407266795916972034)。


## APK URL正则排除与候选来源的保全

apktool后正则提URL、删引号并排除google/github等词的管线，得到的是某一规则筛后的字符串集合。匹配语法、转义/截断、子串排除会漏掉合法目标或保留非运行地址，去重不能补来源与漏项。

绑定获准包的哈希/签名/版本、文件位置/解析方式，保留原始值、变换和每个排除理由，再区分示例/第三方库、旧地址和当前运行消费者。被排除域名也可能是业务入口，命中不自动扩Scope；本批没有下载APK、执行反编译或访问候选。来源：[保存帖](https://x.com/i/status/1408206143323836417)。


## 二维码文本到scheme分派和WebView权限的链条

两帖QR提示扫码javascript确认，但图没有实际设备或扫码结果。二维码解码出文本、应用接受URL scheme、进入WebView或其他消费者以及执行时origin/原生bridge权限是各自条件。

在获准自有制品中绑定扫码入口、分派策略、实际URL和WebView配置/调用点，记录被当文本、被scheme白名单拒绝、转外部应用及不同origin等反例。不能从可生成二维码认任意Android应用XSS，本次未解码执行二维码或操作设备。

来源：[保存帖1](https://x.com/i/status/1411287363112902656)、[保存帖2](https://x.com/i/status/1645396728357564418)。


## DEX内存采集的进程选择与完整性范围

frida-dexdump帮助说明默认前台、未指定PID时可能dump全部进程，并提供spawn、delay和deep选择。这些选项影响采集主体和时点，deep更慢也不代表找回所有有效DEX。

保留获准包/进程PID、启动代际、采集配置、片段字节哈希和后续格式校验；区分未采集、不可读、截断/重复映射与真实不存在。内存片段、完整代码或敏感数据仍需各自证明，不能从工具帮助算移动漏洞已测。本次未运行Frida或导出设备内存。

来源：[保存帖1](https://x.com/i/status/1411675318281199618)。


## ADB代理intent与有效网络及应用流量

ProxySetter命令给的是代理配置意图，没有设备端生效及实际流量收据。SSID、当前网络、设备用户、系统代理、应用网络栈与TLS信任需要分别确认。

关联受控设备/应用版本、配置前后值、连接网络与同次请求在代理历史中的来源。应用忽略系统代理、走蜂窝/独立栈或TLS拒绝都可能造成无流量；配置成功不代表HTTPS内容可见，代理进程监听也不代表完整采集。

来源：[保存帖1](https://x.com/i/status/1413932483427586057)。


## 设备名进入后台读者与2FA动作的独立关系

Android/iOS设备名BXSS建议把改设备名与所有应用开启2FA连在一起。设备名必须实际被对应客户端上传、保存并送至HTML/脚本消费者，2FA开关不自动构成这条数据流。

固定受控设备、平台/应用版本、上传字段、持久化位置、真实后台读者和输出上下文；不同平台与应用分别建立证据。仅OS名称变化、应用不发送或安全文本显示都是反例；不要以2FA流程标题补盲脚本回连。

来源：[保存帖1](https://x.com/i/status/1414572032897929224)。


## APK发布版本与签名及变体覆盖

dapk图5页138 releases只显示四个版本下载行。镜像列表、组织名称和文件名不是全部官方有效制品或已完成下载的证明。

关联包名、版本号/构建号、签名、ABI/渠道、原始来源时点及制品hash，保留分页终止、下载失败和重复变体。只有日志、缺hash或缺版本变体是反例；旧APK发现不授权安装和登录，也不推当前服务仍匹配旧客户端。

来源：[保存帖1](https://x.com/i/status/1421462801357418505)。


## Android代理TLS失败与pinning绕过成功的界限

教程题为Frida/Burp/GenyMotion绕pinning，图却有多域SSL negotiation fatal alert、0请求和手机offline。失败症状不足定位单一原因。

按网络可达、代理路径、CA信任、TLS版本/协议、应用栈、hook加载与实际HTTP记录分阶段；多域同时失败还需独立正常端点对照。空history、offline、只启动hook或未出现请求是反例，不能算绕过完成，未修改设备或运行hook。

来源：[保存帖1](https://x.com/i/status/1430079529171701790)。


## 恢复客户端参数构造与服务端挑战绑定

Android Java图向auth/flashcall_account_recovery构造cuid、encrypted_phone_numbers和cli等字段，缺服务端回复/校验。

将源码版本、调用链、字段类型、发起身份、目标账号、电话challenge、服务端签发及最终兑换绑定；静态HashMap、客户端可改、合法加密值或服务端拒绝是反例。请求构造不证明信任客户端导致ATO，未发送恢复请求或验证码。

来源：[保存帖1](https://x.com/i/status/1435568040112898049)。


## 反编译HTTP注解与动态路由和真实请求

jadx grep图列GET/POST注解、路径变量和动态{url}，方法名涉及app/store；正文只按Java文件搜注解。

保留APKhash/版本、完整baseURL/环境、注解库、callsite、字符串构造和实际请求，合并静态/动态入口；混淆遗漏、native网络、运行时URL、未调用方法或别的版本是反例。grep能给候选，不提供全部API/认证行为，未反编译或运行来源APK。

来源：[保存帖1](https://x.com/i/status/1437829983674712074)。


## Manifest静态声明与运行组件权限的独立证据

jadx图app-debug manifest列targetSDK25、网络/storage/calendar、singleInstance及receiver exported=false；另图历史MobileTop10分类。

绑定APKhash/构建类型、OS/SDK版本、具体组件/intent、权限默认/实际授予、调用者和业务对象；debug包、声明但未用、exportedfalse组件不可外达、runtime拒绝或仅分类图是反例。静态列表不等外部可利用/全移动风险覆盖，未部署APK或改设备。

来源：[保存帖1](https://x.com/i/status/1439695423556435968)。


## Twitter intent 启动输出与崩溃因果

adb 图含 retweet intent 的启动行和较早的解析异常，没有可绑定的应用崩溃栈。

区分 intent 被调度、URI 解析失败、应用 handler 异常与可由其他应用/链接触发的稳定崩溃。记录包/版本、导出边界、冷暖启动、异常进程、时间与无害对照；启动命令及截断 stackTrace 不能直接判 Android RCE 或远程 DoS。

来源：[保存帖1](https://x.com/i/status/1447474740398997510)。


## 长字段跨 Web 同步到 Android 的可用性链

正文称长字段会使 Android 卡顿或崩溃，线程后续没有保存。

按自有数据的长度/编码、Web 接受、存储、同步、移动读取和渲染逐层记录。资源预算、设备/版本、ANR/崩溃栈、恢复方式与持久状态需分别证明；大字符串、一次卡顿和不在图中的后续步骤不能称稳定跨平台 DoS。保持有界无害样本，不运行失控输入。

来源：[保存帖1](https://x.com/i/status/1451415044416159749)、[保存帖2](https://x.com/i/status/1451818398141194241)。


## Nanobrok 管理画面的设备与初始连接

图显示Genymobile设备、Android10、emulator、无线信息/日志与no locations found，未见注册或权限取得过程。

设备展示、命令发出、接收、受保护动作是不同回执，记录自有设备身份/构建、应用权限、连接来源与时间。预置agent、模拟器权限、无位置结果或未执行命令为反例，远程管理界面不自动构成Android入口漏洞。不连接设备、取位置/IMEI或发控制指令。

来源：[保存帖1](https://x.com/i/status/1463979655329951747)。


## Frida 练习变量与服务器保护能力

正文列修改硬编码变量、函数返回、实时变量和PIN爆破，图是教程封面与资源索引。

练习要绑定自有实验app/构建、实际函数、输入约束和允许权限，区分本地客户端改变与服务器真实授权。实验固定PIN、预置instrumentation、服务端拒绝或没运行教程为反例；不从本地patch推断远程ATO，不执行PIN尝试、连接设备或注入脚本。

来源：[保存帖1](https://x.com/i/status/1465349835570176000)、[保存帖2](https://x.com/i/status/1466074610810732566)、[保存帖3](https://x.com/i/status/1466437086353969164)。


## IP 转发标题与证书绑定证据

相关文章标题称iptables/IP forwarding绕过SSL pinning，现有图仅VirtualBox GooglePixel PoweredOff和硬件/磁盘配置，无TLS验证代码或握手。

把模拟器准备、路由、代理连接、信任证书和应用pin校验分别记录；需要实际应用/版本、证书校验路径及自有请求能否被解密的对照。未启动VM、只改路由、未解密或服务器拒绝均不证明绕过，不修改设备/防火墙。

来源：[保存帖1](https://x.com/i/status/1468136375266340870)、[保存帖2](https://x.com/i/status/1468490060496576514)、[保存帖3](https://x.com/i/status/1468498038477901825)。


## 反编译 SQLite 凭据示例与真实可读性

VSCode DIVA样例可见SQLite创建user/password列、INSERT拼接和saved toast，右侧代码截断。

静态记录样本哈希、函数、数据库位置、明文形态和调用来源；实际风险需要数据产生、存储权限、备份/日志受众。只实验样例、未执行方法、权限拒绝或无数据为反例；拼接SQL也需可控输入/执行证据。工具能显示多类型反编译结果不保证语义等价，不执行样本。

来源：[保存帖1](https://x.com/i/status/1468957624775315464)。


## APK 解密到 GitLab 权限链的逐段身份

两长图叙述APK→.jsc→XXTEA→JS→IP/端口→GitLab自注册/枚举/绕限/管理员→源码，续图再写Redis/管理登录/RCE，缺每段原始交换。

静态记录包/构建、加密格式、材料来源和消费者，下一阶段重新核资产、主体、动作与授权；用自有合成材料区分本地解密、发现服务、有效认证及权限改变。仅解密字符串、旧地址、无服务端状态或不同主机为反例，不下载全部源码、破解密码或使用真实秘密。

来源：[保存帖1](https://x.com/i/status/1480990799399735296)。


## DIVA 改进计划与 InsecureShop 训练入口

正文一条只是DIVA refinement计划，另一条介绍Kotlin InsecureShop的19+练习，未存实现或完成记录。

把训练目标映射为输入、存储/IPC/WebView/权限等实际消费者和自有离线小样本；版本、环境、合法/拒绝与观察结果分别记。课程/应用名、计划、练习计数或没有运行收据为反例；靶场能力不等真实App漏洞。

来源：[保存帖1](https://x.com/i/status/1488866480355745794)、[保存帖2](https://x.com/i/status/1488905046691569668)。


## WebView 可加载 URL 与桥接特权须分层

保存正文只有WebView checklist主题和任意URL影响方向，没有WebView代码、配置、加载来源或JS bridge。外链全文按豁免。

离线自有移动模型区分可控URL、origin、脚本/文件访问配置、消息/bridge校验、宿主权限与无害结果。能加载网页不自动得到宿主权限/敏感文件；无bridge、禁止脚本或正确origin限制为反例，不安装来源app或访问真实设备。

来源：[保存帖1](https://x.com/i/status/1501679218471620619)。


## DirtyPipe 手机演示要核内核构建与有效 uid

正文称Pixel6/S22受影响，但保存图只有手机和sh5.1提示，无可辨型号、内核构建、有效uid或完整步骤。

在自有隔离模型记录设备构建、内核补丁、原身份及前后实际uid，区分本地写入前提与远程入口；root样式提示符或另一型号名称不是特权提升证据。不连接设备、执行PoC或修改系统文件。

来源：[保存帖2](https://x.com/i/status/1503766361369346050)。


## M1 Android Studio ARM 下载项不等测试环境就绪

保存图2021.1.1.22包列表含MacARM和hash，正文说M1配置困难；无安装或代理证据。

自有离线环境记录host架构、SDK/AVD或设备构建、工具hash和依赖版本，按adb连通、可解密代理、pinning/root权限分别验条件。ARM包名称不保证全部工具兼容，更不证明捕获真实流量；不下载旧包或连接设备。

来源：[保存帖168](https://x.com/i/status/1506678213929488384)。


## Android 五项检查应分客户端入口与服务端状态

正文列导出 Activity、硬编码 token/password、SQLite 敏感数据、旧版本绕过和不失效 API 会话。

自有样本分别追导出组件的调用者/权限、凭据实际消费者、存储访问主体、旧客户端到相同服务端操作、token 撤销与到期。仅 exported、字符串或旧 APK 存在并不证明越权；要记录前后服务端身份和受限状态，不把五项拼成一条已验证攻击链。

来源：[保存帖1](https://x.com/i/status/1508499964275552259)。


## 旧 APK 的接口线索需与服务端当前入口对照

图用旧/新版客户端是否含 login_insecure 说明移除前端入口后后端可能仍在。

离线比较自有版本的端点、参数和认证方式，区分客户端不再调用与服务端已经关闭。旧代码只提供候选；当前服务端是否可达、是否仍执行相同操作及是否缺失身份/对象检查才决定问题。版本示意不证明实际目标存在该缺陷。

来源：[保存帖1](https://x.com/i/status/1512757224602578959)。


## Flutter TLS 验证源码不是 pinning 绕过完成证据

图片展示证书链存在性、verify store、主机名及 verify callback 设置的源码，正文提到 Ghidra 修改二进制。

区分信任链、服务身份校验与应用额外 pinning；看到返回 false 或回调位置不证明补丁正确。自有样本应保留二进制版本、ABI、实际控制流与补丁前后连接结果；可以解密抓到请求也需说明调试 CA/配置/样本条件，不能一概声称绕过所有 Flutter pinning。

来源：[保存帖1](https://x.com/i/status/1513532321860919311)。


## 动态广播接收器的实际发送者边界

保存 Talk Android 摘要指出 registerReceiver 未配置 broadcastPermission。核对动态和 Manifest 注册、导出标记、Android API/目标 SDK、发送者身份、action 与消息字段，并追踪接收事件最终可触发什么操作。用两个自有测试应用分别发合法和未授权合成广播，验证服务端或业务状态而非只看接收日志。缺一个参数、单个广播到达或旧摘要不足以证明当前版本存在任意操作权限。

来源：[保存帖1](https://x.com/i/status/1608151380547493888)。

已实际查看保存图片 `1608151380547493888-02.jpg`：TalkAndroid registerReceiver缺broadcastPermission摘要，无实际receiver动作；manifest/dynamic export/api version、sender身份/权限、intentextras和敏感动作边界，普通广播可见不等于完整控制，仅自有两app验证。


## 设备 APK 获取要绑定包标识和签名版本

保存 ADB 导出 APK 的说明和使用示例，脚本全文未保存。区分应用 package ID 与普通 HTTP URL，记录自有设备、包名、版本、签名、完整/拆分 APK 和导出时间，静态审阅的文件须确为该部署版本。只使用已授权设备已有的导出能力，不安装未知 App 或执行外链脚本；获得 APK 不证明获得服务器权限，缺拆分内容也不能被当完整源码覆盖。

来源：[保存帖1](https://x.com/i/status/1611305196990119938)。


## 消息通知入口也必须经过本地应用锁

保存 Talk Android 15.0.2 RC1 情形为 A 在 web 发消息、B 已登录手机并开 passcode，点通知进入内容。审计冷启动、通知/深链、前后台切换、恢复与已解锁视图的统一门禁，用自有两身份与合成消息比较锁定/未锁、拒绝和实际内容权限。记录设备物理可访问前提和版本；这是本地已登录会话保护，不能由通知截图推成服务端 MFA 或远程匿名旁路，也不只看 passcode UI 是否出现。

来源：[保存帖1](https://x.com/i/status/1612341298156998656)。

已实际查看保存图片 `1612341298156998656-02.jpg`：NextcloudTalkAndroid15.0.2RC1notificationclick绕passcode，两用户Aweb/Bphone启保护→通知进入，无runtimevideo；Dandroid物理可访问已登录device/launch-deeplink-resume统一passcodegate，非服务器MFA远程旁路，记录具体版本前台后台锁状态并用合成消息。


## APK file 模板匹配 URL 与 Email 需要区分业务及依赖来源

图为解包APK静态匹配，路径含libflutter、AndroidX、Room、strings.xml，结果为Email/URL/Firebase info。记录APK包名/签名/版本、文件位置及规则，把第三方库链接、示例邮箱和业务配置分开；以自有已知标记资源作为正例、库文档链接为反例。Firebase域或公开API标识不是secret或数据库开放证据；实际权限需要独立批准的最小验证，模板命中数不能当漏洞数。

来源：[保存帖1](https://x.com/i/status/1614005687255814154)。

已实际查看保存图片 `1614005687255814154-02.jpg`：APK解包Nuclei file info匹配email/URL/firebase；libflutter和AndroidX等第三方噪声，public数据库地址不等于可读秘密。


## ownCloud 外部文件 Activity 的 URI 路径必须约束应用内部存储

保存摘要针对ReceiveExternalFilesActivity、第三方组件上传和android.intent.extra.STREAM，指出路径验证不足可读写internal storage。先确认exported/intent过滤、URI grant及ContentResolver/文件路径转换，按规范化后的根目录与文件所有者校验；不能仅做字符串前缀。自有测试app以无敏感标记文件、合法共享URI和拒绝内部路径对照，观察实际源/目的文件。GHSL-2022-060及旧修复摘要不补造未保存代码或当前受影响版本。

来源：[保存帖1](https://x.com/i/status/1615028092023472145)。

已实际查看保存图片 `1615028092023472145-02.jpg`：ownCloud Android ReceiveExternalFilesActivity外部路径未妥善验证，android.intent.extra.STREAM读写内部storage；旧修复旁路摘要未见完整代码。


## KAYAK deeplink 摘要只给历史会话泄漏风险与版本

图称Android161.1恶意deeplink可窃session，161.2初修；未保存handler或URI链。审计manifest/exported/app links、参数解码、目标URL信任、WebView/网络凭据与导航边界，区分可打开链接和凭据跨源发送。自有app/模拟会话以无敏感canary对照允许/拒绝目的及实际请求，绝不提取真实cookie。版本与奖励只保存历史，不能推出现在一点击ATO。

来源：[保存帖1](https://x.com/i/status/1616148860941762568)。

已实际查看保存图片 `1616148860941762568-02.jpg`：KAYAK Android161.1 deeplink窃session摘要及161.2历史初修，无URI/handler代码；仅最小own canary，不偷cookie。


## Activity 的可调用性与每个 WebView 消费者要逐项核验

图从 Manifest/Activity 指向 exported、permissions、auth、DeepLinks/WebView，并列 JS、loadUrl/loadData、JavascriptInterface、content/file 访问配置。先固定 APK/签名/版本、调用方身份与组件权限；用同包允许调用与外部自有测试应用的受限调用对照，跟踪 Intent/URI 到真实业务动作。exported 本身不是漏洞，Activity 内仍可校验身份/对象；图示数据窃取、redirect、CSRF 仅是影响候选，缺实现、原始请求及结果不能确认任意越权。

来源：[保存帖1](https://x.com/i/status/1622191391328669701)。

现有图片证据 `1622191391328669701-02.jpg`：AndroidManifest Activity exported权限/auth DeepLinks/WebView图，allowUniversalFileURLs/JS/loadUrl/loadData/JSInterface/contentAccess作为线索，图箭头非必然漏洞。


## WebView 文件与脚本能力须证明不可信内容实际可达

将 allowUniversalAccessFromFileURLs、JS 开关、loadUrl/loadData、JS interface、content access 分成能力、来源和消费者。核主机/应用实际配置及版本、URI 规范化、文件/内容提供者权限和桥接暴露方法；用自有合法页面与拒绝来源、可读测试文件与不可读文件比较实际载入/执行及数据流。开启某个开关或找到类名不保证第三方可控内容进入，也不自动取得任意文件或 Java 能力；图只有流程关联，没有配置/设备实测。

来源：[保存帖1](https://x.com/i/status/1622191391328669701)。


## 加密移动 API 双代理：观测层转换与服务端校验边界

保存图描述客户端密文先进入 mitmproxy 解密，再送到 Burp 编辑明文，再由另一 mitmproxy 加密并送服务端，正文提到硬编码 key/IV。提炼时记录包体格式、加密层位置、字段编码及响应逆向处理，保证原始密文、明文和重新封装的测试请求可关联。仅掌握 key/IV 不代表可以伪造有效业务请求；算法、模式、认证标签、签名、nonce、时间戳与 replay 检查仍需确认。先做无修改往返对照，再用自有无害字段比较修改后服务端行为。图未给出算法/MAC 或权限结果，不把代理图当作验证成功。

来源：[保存帖1](https://x.com/i/status/1624053071314849792)。

现有图片证据 `1624053071314849792-02.jpg`：AndroidAES diagramAppencrypted→mitmproxy1decrypt→Burpplaintext→mitmproxy2encrypt→server，算法模式padding/authnonce及keys缺失，双向比完整包/MAC不是图证明。


## Android 存储与备份：路径名只是暴露候选

现有攻击图列出文件路径/XML、外部存储、Firebase 配置、SQLite 以及备份/共享路径。为每个候选定位实际写入的敏感数据、文件读者、sandbox 和备份/共享导出流程；测试数据应来自自有账号并确认另一个未授权身份能否读到。FileProvider 的 root/external 路径配置还要结合 exported、grant 与可调用入口，不能只凭 broad path 宣称任意文件读取。Firebase JSON、普通数据库或私有目录中保存数据本身不等于秘密外泄；保存图没有实际文件内容或读取结果。

来源：[保存帖1](https://x.com/i/status/1624816518755409922)。

现有图片证据 `1624816518755409922-02.jpg`：Android全图：storagefile_paths broadroot external/Firebase.json/sqlite、CBC/staticIV/hardkey/XOR、APIheaders/sharedtoken、exports/WebView/deeplink/SDKorigin/pluginpermission，各有消费者/版本/权限条件。


## Android 硬编码 key 与 IV：保密性和伪造性要分开

攻击图含 CBC、静态 IV、硬编码 key、XOR 及 API 共享 token。先识别数据用途、密钥由谁可获得、模式和完整性保护，再用自有样本确认可重复解密或伪造；静态 IV 的影响依模式、消息重复和攻击者可观察性而定。配置 key、客户端共享标识或算法名字不能直接当作高权限凭据；有效性、服务端权限与绑定条件需要最小授权操作验证。没有服务端签名、认证标签和请求验证信息时，不能从“能读明文”推导“能任意修改业务”。

来源：[保存帖1](https://x.com/i/status/1624816518755409922)。


## Android IPC 与 WebView：入口导出和数据消费者逐段检查

保存图及教程题目涉及 Intent/filter、BroadcastReceiver、ContentProvider、WebView、deep link、ADB 和 SDK/插件。先列可从其他应用调用的真实 exported 组件、权限和 URI/grant 约束，再追踪 extras、URL 或消息进入文件/数据库/脚本/native bridge 的消费者。自有测试应用与正常调用作对照，以未授权读取、操作或 bridge 能力为确认点。ACTION_TIMEZONE_CHANGED 的 Toast 演示和 emulator 设置只说明训练场景，不能证明第三方任意 Intent 可达；WebView 加载链接也需 origin、JS 和桥接权限才能讨论具体影响。

来源：[保存帖1](https://x.com/i/status/1624816518755409922)、[保存帖2](https://x.com/i/status/1625021500528160769)、[保存帖3](https://x.com/i/status/1625024372976263168)。

现有图片证据 `1625021500528160769-02.jpg`：AndroidtutorialBroadcastReceiverTIMEZONE_CHANGED Toast和emulatorsettings，无exportpermission/第三方Intent/consumer结果。


## jadx 静态还原：输出要回到实际 APK 与动态消费者

现有 Session03 图示 jadx -d 指定输出路径及 GUI 反编译，正文列静态/动态分析。记录 APK hash、package/version、反编译误差和关联 class/resource，区分静态存在的 key、URL、组件与运行中实际被调用者。动态验证用自有设备/账户确认可达入口、身份及权限结果，不能由反编译出现代码推导漏洞已利用。图的终端小字有限且未保存动态过程，封面或命令成功不说明全部 classes 完整还原。

来源：[保存帖1](https://x.com/i/status/1627559784563220482)。

现有图片证据 `1627559784563220482-02.jpg`：Android101staticanalysisjadx -d destination APK与GUI选择说明，命令/截图小字部分不清，无dynamic执行或漏洞。


## Frida 与代理证书准备不等于 Android 解密成功

教程图片展示adb推送frida-server与权限设置、导出Burp DER并按脚本约定命名；这是准备步骤，没有启动server、进程连接、hook命中或代理解密证明。授权模拟器需核对CPU/Frida版本、应用进程、CA信任层与具体pinning库；每一步以日志和自有请求验证，保留无hook及错误证书的反例。解密后接口仍须独立检验认证授权，SSL unpinning本身不等于服务端漏洞；外部Gist封面没有代码可蒸馏。

来源：[保存帖1](https://x.com/i/status/1629488644846424066)、[保存帖2](https://x.com/i/status/1629555370514432000)、[保存帖3](https://x.com/i/status/1629982794246938626)、[保存帖4](https://x.com/i/status/1630604741586698242)。

现有图片证据 `1629488644846424066-02.jpg`：Frida Android 教程片段展示推送 frida-server、chmod、导出 Burp DER 证书重命名；没有启动/连接/hook/解密流量证明。


## APKHunt 静态 MASVS 线索与动态权限确认

帮助图说明APKHunt单APK/目录与日志选项、Linux及jadx/dex2jar/go/grep依赖，没有扫描结果。静态MASVS/cheatsheet应绑定包版本、manifest/代码位置、数据流和规则适用条件；工具提示是候选，需授权设备上验证组件权限、数据存储或网络行为。帮助命令运行不等于分析完成；本轮未下载/安装外链工具，历史依赖不作当前兼容性保证。

来源：[保存帖1](https://x.com/i/status/1630572184790769668)、[保存帖2](https://x.com/i/status/1630619509496352770)。

现有图片证据 `1630572184790769668-02.png`：APKHunt帮助页声明MASVS静态分析、-p单APK/-m目录/-l日志，Linux及jadx/dex2jar/go/grep依赖；只帮助页，没有扫描输出或动态确认。


## Android 回调 intent 路由与 OAuth 会话各自验证

移动回调审查先确认自定义scheme/intentfilter、系统实际解析到哪一测试app及App Link验证，再确认OAuth交易绑定。恶意app需要安装是独立前提，系统弹出选择与自动路由影响触发条件；不同移动系统不能互相套用。自有设备/测试客户端记录解析和PKCE兑换拒绝，不能用deep link文字就推定读取真实邮件。

来源：[保存帖1](https://x.com/i/status/1631414207223672832)。

现有图片证据 `1631414207223672832-02.jpg`：Shopify Shop/Outlook历史摘要称恶意app可截取自定义deeplink授权code，工程师加PKCE缓解；依赖callback劫持与code兑换，普通URL可见不等于可兑换。


## APKHunt 帮助与 MASVS 标题不等于审计完成

图显示-p单APK、-m目录、-l日志，Linux验证及jadx/dex2jar/go/grep依赖。记录APK hash/版本、规则/工具版本、结果文件行与相关配置，然后以动态许可实验确认可达性/权限。帮助页、Logo、联系人或MASVS字样不证明工具已运行、标准完整覆盖或漏洞真实；不联系作者或安装运行归档脚本。

来源：[保存帖1](https://x.com/i/status/1634064036932321283)。

现有图片证据 `1634064036932321283-02.png`：APKHunt帮助：-p单APK/-m目录/-l日志，Linux测试，依赖jadx/dex2jar/go/grep；MASVS标题不是完整覆盖或漏洞确认，需APK hash/版本、规则、文件行定位及运行复核。


## APK 关键词命中须区分练习数据与真实秘密

accesskey/admin/AES/API/password/pinning/token/TrustManager等grep只定位代码。图来自diva-beta练习，setText示例、SQLite初始化与字符串拼接不同用途；记录APK hash、路径/行、来源与实际调用/权限，脱敏保留必要类型。样例密码/关键字不证明有效生产秘密、TLS绕过或SQLi，需可达消费者与受控对照。

来源：[保存帖1](https://x.com/i/status/1635636899640655872)。

现有图片证据 `1635636899640655872-02.jpg`：grep lab diva-beta列APICredsActivity setText/SQLite拼接/练习初始化insert，含样例密钥/密码不可复制；训练样例和匹配关键词不证明真实生产秘密/可用凭证。


## BROWSABLE activity 还需验证 exported 与 URL 策略

AndroidManifest BROWSABLE是深链接候选，核对exported/permission、action/data scheme/host/path及运行时Intent/嵌套URL处理。许可自有应用比较匹配/不匹配链接和外部caller，记录实际WebView/browser及origin/桥接权限。仅category字样不证明任意URL可打开，更不等WebView执行或接管；不安装adb/jadx或运行归档目标。

来源：[保存帖1](https://x.com/i/status/1636359161679151105)。


## Android 工具词表按源码、运行与组件验证分工

正文重复Dex2JAR并列JADX/JD-GUI/ByteCodeView、Baksmali/ApkTool、Drozer、AndroGuard、QARK/AndroBugs、AppMon/MobSF。按APK版本哈希、反编译/静态分析、运行观测和组件调用分别组织证据；反编译结果和规则告警需回到实际数据流/配置/权限。工具列表不是MASVS覆盖或真实应用漏洞证明，不下载/安装。

来源：[保存帖1](https://x.com/i/status/1637892377334390832)。


## APK pull、反编译与重打包是不同分析阶段

正文 Apk.sh 描述 pull/decode/rebuild/patch 工具功能，没有样本或执行结果。冻结应用包/版本/签名与自有设备权限，区分静态manifest/代码审查和修改后测试产物；重签名/patch可能改变运行条件，不证明原应用存在漏洞或能安装到生产设备，不执行安装或下载未保存脚本。

来源：[保存帖1](https://x.com/i/status/1641066346539622401)。


## QR 导航的 UXSS 要证明跨 origin 执行而非普通弹窗

Brave图列Android13及历史stable/nightly/beta/Chromium版本，称扫描QR后在所有打开domain执行；QR和步骤截断。记录QR解码后的原值、scheme、导航/JS消费者、触发交互与当前页面origin，在隔离两自有origin核对脚本能力边界。标题UXSS和作者宣称不提供跨域证据；Edge的CVE-2022-23258引用不能直接认作Brave同一CVE，未读或执行QR。

来源：[保存帖1](https://x.com/i/status/1645909964584525826)。

现有图片证据 `1645909964584525826-02.jpg`：BraveAndroid13QR扫描UXSS报告：版本stable1.48.164/nightly1.50.53/beta1.49.106/Chromium110.5481.100，作者称跨全部domain执行；QR截断不可读，无跨origin证明，CVE2022-23258引用Edge案例不能据此归为Brave同编号。


## FileContentProvider 的 SQL 注入要保留本地调用前提

ownCloudAndroid历史图称exported FileContentProvider含SQLi，同设备恶意app/用户可取内部信息；manifest/SQL代码截断。审查具体APK版本、exported与permission、callerUID、URI匹配、selection/projection/sort输入和参数绑定，在隔离测试应用用自建数据核对越界查询。GHSL-2022-059/Medium4.2不替代源码和可达证据，不能把同设备provider缺陷扩写成远程WebSQLi。

来源：[保存帖1](https://x.com/i/status/1646174208215449600)。

现有图片证据 `1646174208215449600-02.jpg`：ownCloudAndroidFileContentProvider exported manifest及SQLi摘要：同设备恶意app/用户可取内部信息，GHSL2022-059/Medium4.2/$300；下方代码截断，需manifest权限/URI匹配/selection拼接/SQL参数与callerUID，不能当远程webSQLi。


## 移动工具菜单和 MobSF 功能要映射到实际分析阶段

QuadraInspect 图片展示 APKLeaks、AndroPass、MobSF、RMS 等菜单与本地启动；另帖介绍 MobSF 静态/动态分析角色。按自有 APK、包标识、构建版本、静态反编译线索、受控设备行为和后端接口建立证据链，保留实际工具输出及版本。菜单、安装成功或 localhost 服务启动并非完成 APK 分析；静态搜索的密钥/URL 需验证用途与当前权限，动态结论则需实际动作、网络及权限边界，不能以工具合集宣称全面覆盖。

来源：[保存帖1](https://x.com/i/status/1646588465654517773)、[保存帖2](https://x.com/i/status/1648026461180432384)。

现有图片证据 `1646588465654517773-02.png`：QuadraInspecthelp SETtarget/安装/APKLeaks/AndroPass/Mobfs/RMS分类，示例输入fake,apk且RMS1.5.15仅启动127.0.0.1:5000，无APK结果；动态/静态菜单命名与真实分析证据分开。


## ADB 工具功能以配对、设备权限和既有访问为前置

PhoneSploit Pro 菜单显示连接、shell、截图、文件/应用及 Metasploit 动作，没有实际设备结果。核对自有设备、调试开关、配对/连接认证、允许账户与动作，分别区分正常开发权限和未授权暴露。能看到菜单或已有 ADB shell 不证明新漏洞、Meterpreter 成功或提权；不连接外部设备、安装 APK、读取文件或执行后渗透功能。

来源：[保存帖1](https://x.com/i/status/1651575597250883586)。

现有图片证据 `1651575597250883586-02.png`：PhoneSploitPro1.42菜单含连接/list/shell/镜像/截图/文件/installAPKs/MetasploitHackDevice等，无实际配对认证/设备操作结果；已获ADB访问不等初始漏洞，未接设备或执行。


## 配套移动应用 TLS 验证与设备链分开

Ray-Ban 配套 app 的缺少证书验证只是保存正文的声明。需要在自有设备/测试账号与授权网络中对可信证书、错误主机名、非可信链的连接行为作对照，定位 Android 网络栈与业务端点。代理可见流量可能源于用户安装信任证书或调试设置，不能推断所有设备固件也不验 TLS。

来源：[保存帖1](https://x.com/i/status/1651889049165070337)。


## Android 静态目录、改签与组件权限分别审计

保存速查表列 APK 的 manifest/DEX/lib/assets、数据目录、签名、重打包、provider 和 activity。固定包版本/hash、组件 exported/permission、调用 UID 与用户同意，用普通第三方测试 app 和 ADB shell 分别对照。自有调试设备可查数据或改签安装不是原签名权限绕过；修改/删除 provider 数据、重打包或签名只在自控样本，不能把工具运行当漏洞证明。

来源：[保存帖1](https://x.com/i/status/1653808994270736384)。

保存图片 `1653808994270736384-02.jpg`：Androidcheatsheet静态APK/META-INF/lib/DEX/manifest、data isolation/repackage/sign/provider/activity；adbshell权限与第三方app不同，改签自安装不等于原签名权限绕过。 本段只使用已保存且实际查看的内容。

保存图片 `1653808994270736384-05.jpg`：AndroidPWN GDB/LLDB断点/内存/attach/ADBforward与PatchELF替换lib/interpreter；调试既有权限与patch样本不是原应用可利用证明。 本段只使用已保存且实际查看的内容。


## 本地调试与 ELF 修改建立可复现崩溃证据

PWN 表列 GDB/LLDB attach、断点、内存观察、ADB forward、AFL/QEMU 与 PatchELF。记录自控二进制/hash、架构、输入、调试权限和错误位置，最小复现加修复后反例；debugger/ADB 既有权限、替换解释器/依赖库或本地 patch 成功并不证明未授权代码执行。只提炼流程，不运行归档命令或暴露调试端口。

来源：[保存帖1](https://x.com/i/status/1653808994270736384)。


## deep link 入口需要复核本地 PIN 守卫

Nextcloud Android 报告标题称第三方生成 deep links 可绕本地 PIN，截图没有 intent/操作序列。用自控测试 app 比较正常启动与导出入口，在冷启动、后台恢复、账号切换状态下记录 PIN gate 与受保护数据。该本地锁与服务端登录/会话权限不同，已解锁会话显示不证明完整认证绕过，不能补造未保存步骤。

来源：[保存帖1](https://x.com/i/status/1654040872835592194)。

保存图片 `1654040872835592194-02.jpg`：Nextcloud AndroidPIN第三方deeplink标题及severity变化历史，无intent/数据访问步骤；组件生命周期守卫与本地PIN不等serverlogin。 本段只使用已保存且实际查看的内容。


## APK 关联以二进制 hash 区分同包名版本

Koodous 输出同 com.brata.rat/1.0 名称却有多个 SHA/大小。记录样本来源、具体 hash、签名/权限、版本和标签来源，把包名/数据库分类与实际行为区分。相同名字不等同同一 binary，标签不证明本次已观察恶意网络/功能；不下载、安装或执行样本。

来源：[保存帖1](https://x.com/i/status/1659759710487166976)。

保存图片 `1659759710487166976-02.png`：KoodousFinder同com.brata.rat/版本1.0名BRATARAT多不同SHA/0.67MB，hash才标识具体二进制；数据库标签/包名不证明安装包来源/实际恶意行为，无执行APK。 本段仅使用实际查看的保存原图，不补未保存内容。


## 链接触发崩溃需要版本与异常轨迹

WhatsApp 的 wa.me/settings 字段截图只展示输入，缺少完整崩溃栈、版本和恢复验证。以获准合成深链追踪 URI 解析、路由及异常边界，保存受影响组件和可逆恢复；标题不能证明传播、所有版本或永久失效，删除聊天的建议也不保证恢复。不向真实联系人发送崩溃内容。

来源：[保存帖1](https://x.com/i/status/1665212650547195910)。

保存图片 `1665212650547195910-03.jpg`：WhatsApp输入wa.me/settings字段，titlecrash但无crashtrace/版本/refactor证明，URL消费者canonicaltype异常夹具不传播crashmsg本段仅使用实际查看的保存原图，不补未保存内容。


## Android 深链写入与回包出口分开检查

保存 Basecamp 公开摘要关联 com.basecamp.bc3 3.26.3：路径穿越影响应用私有目录写入，恶意 intent/custom deeplink 还可把服务端敏感响应发给第三方应用。分别核对路径规范化及目录边界、调用者/组件暴露、回调目标与响应数据权限，以本地合成文件及非敏感响应验证。摘要未给具体 extra、handler 或完整 PoC，不补成任意私有文件读取、RCE 或当前版本行为。

来源：[保存帖1](https://x.com/i/status/1666475555535962115)。

保存图片 `1666475555535962115-02.jpg`：Basecamp Android com.basecamp.bc3 3.26.3 公开摘要：路径穿越可写app私有目录，恶意intent/customdeeplink可使serverreply敏感信息给第三方app。High8.8Resolved；标题未给具体extra/path/handler，两个边界独立验，不推断任意app文件读或RCE。本段仅使用实际查看的保存原图，不补未保存内容。


## 导出 Activity 到 WebView 和本地 token 分环验证

正文给出 exported activity、WebView 与 SharedPreferences 的接管链名。分别核对组件暴露/调用权限、intent 输入、WebView origin/桥接能力、本地存储可读条件及 token 的真实授权消费者。SharedPreferences 文件存在不代表其他普通应用可直接读取，奖励邮件没有 manifest/代码/请求证据，不补成所有 Android app 的接管方法。

来源：[保存帖1](https://x.com/i/status/1668339185990909952)。


## 关闭检测提示不等于设备状态或授权边界改变

Android 模块图片显示开发者相关检测开关及模块内 Test Off。运行时隐藏某个 API 返回值或应用提示，与系统开发者状态、调试能力、完整性证明和银行操作权限分别属于不同消费者。只在自有应用中比较实际系统状态、所调用 API、检测结果和受保护操作；单个模块自测不能证明所有应用检测都被绕过。若服务端仍验证完整性或操作需额外授权，提示消失不改变权限；不安装模块或操作真实银行账号。

保存图证 `1670859873062363138-02.jpg`：模块自测与开关状态没有受保护应用或系统状态对照。

来源：[保存帖1](https://x.com/i/status/1670859873062363138)。


## MetaMask 深链触发下载与写入执行分开证明

归档描述深链打开钱包内置浏览器后，攻击页能立即发起下载且缺确认。先核对深链入口、浏览器上下文和用户确认，再记录实际文件落点、文件名、重复下载和后续消费者。下载启动本身不能说明任意路径写入、覆盖代码、钱包状态改变或命令执行；保存材料没有这些后续证据。最小验证用自有无害文件，不导入真实钱包、密钥或执行下载内容。

来源：[保存帖1](https://x.com/i/status/1677347356184834049)。

保存图证 `1677347356184834049-02.jpg`：MetaMask Android 历史官方摘要：deeplink 到应用内浏览器后立即下载攻击者文件、缺确认提示；未见具体路径选择或覆盖内容，任意下载不自动证明任意目录覆盖、代码执行或钱包资产影响。


## 生物识别代际变化的解锁状态应按保险库绑定

Bitwarden 历史报告已在 Android 验证，iOS 仅推测：主保险库的生物识别变化后应强制重认证，解锁第二保险库再切回却可能改变主库解锁状态。保存前提含物理访问并能解锁手机、原启用生物识别，第三前提与后续内容裁剪不补造。按库、账号、生物识别代际及锁定/重认证状态记录，用自有离线状态样例比较，不能由另一库合法解锁代替主库验证，不改用户指纹或访问真实密码库。

来源：[保存帖1](https://x.com/i/status/1681635179738304512)、[保存帖2](https://x.com/i/status/1682002710932094976)、[保存帖3](https://x.com/i/status/1682004812181950466)。

保存图证 `1681635179738304512-02.jpg`：Bitwarden Android已验证/iOS仅might：主保险库生物识别变化后BiometricIntegrityValid false应重认证，添加/解锁第二库再切换可用生物识别解主库；需物理访问可解手机、原启用生物识别，第三条件下半截未保存，不补造/不改用户指纹。状态应按库和生物识别代际绑定。

保存图证 `1682002710932094976-02.jpg`：同Bitwarden报告另一ID/不同字节截图，保留跨库解锁、Android验证/iOS未验证和裁剪边界，不算第二独立漏洞。

保存图证 `1682004812181950466-02.png`：社交帖缩略图和卡片再次显示Bitwarden跨两个保险库、生物识别变化后状态及Android验证/iOS可能；字很小、下半前提仍裁剪，保留转载来源并合并不当新漏洞。


## Android 包搜索结果需绑定实际 APK 和代码证据

保存 KoodousFinder package 查询只说明按包名/样本标签检索。核对检索语法、包名与签名、APK 哈希/版本、来源时间以及实际可达代码/配置；同包名、malware 标签或工具概述不能确认当前应用的权限和漏洞。没有下载样本或分析输出时保留候选，不安装 APK、访问账户或运行移动工具。

来源：[保存帖1](https://x.com/i/status/1683246849551921152)。


## 主题深链到执行的链需保留安装和用户交互门槛

Huawei ThemeManager 截图明确要求安装自定义主题，远程需用户动作，礼物/二维码/hwt deep link 是诱导入口，主题审核还会限制使用。应分别核对主题来源、校验/审核、安装、代码消费者、版本与执行身份。保存部分没有具体加载根因或执行输出，不能扩大为零点击、手机 root 或审核已被绕过；不安装主题、送礼或补抓全文。

来源：[保存帖1](https://x.com/i/status/1684209461567668224)。

保存图证 `1684209461567668224-02.jpg`：Huawei ThemeManager文章截图明确需安装自定义theme，远程需用户交互、礼物/二维码/hwt deeplink触发安装且主题审核会限制；没有代码加载根因/版本/执行身份，不推零点击/手机root或实际审核绕过，不送礼/安装主题。


## 移动工具按静态动态代理及设备权限选择：Android（2023保存案例）

移动测试工具图将静态分析/逆向APKTool/Qark/MobSF、动态Frida/Droidbox、代理Burp/Ratproxy、ADB和iOS日志/流量/动态工具混列；称APKiD检测恶意包不准确，指纹识别不等同恶意判断。先按包/平台/系统版本/测试目的选择，再验证实际可观察行为，ADB/内存dump需自有设备及权限，不运行远控工具。

图片证据：`1689974539009347585-02.png`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1689974539009347585)。


## APKiD保护指纹不等同恶意或漏洞判定（2023保存案例）

APKiD2.0测试APK输出anti_vm、anti_debug、compiler dx、manipulator dexmerge、packer Naga和anti_disassembly。规则指纹辅助选择静态/动态验证方式，不证明恶意、漏洞或绕过成功；需包hash/规则版本与运行时对照，合法保护也会匹配。

图片证据：`1690460342374092801-02.jpg`（已核对原图；裁切或遮挡范围不补造）。

来源：[保存帖1](https://x.com/i/status/1690460342374092801)。


## 导出Receiver到私有偏好访问需完整调用链

导出广播接收器仅代表某种可达性，仍需Manifest权限、调用者限制、Intent extra类型、反序列化类路径和最终私有状态使用。用自有测试App发送无害对象比较外部/内部调用以及拒绝类型，审阅SharedPreferences读写与认证绑定。组件公开不自动允许任意对象反序列化，也不证明账号接管。

来源：[保存帖1](https://x.com/i/status/1689116792818630656)。


## Android iframe不能普遍同时造成LFI与Stored XSS

iframe指向/etc/hosts需要真实WebView渲染、有效file基准URL/文件访问设置和可读权限，且储存及其他用户可达性另需证明。比较textContent/HTML插入、HTTP与file来源、禁用文件访问及自有标记文件；相对路径可能访问站点/etc/hosts而非设备文件。文件呈现与脚本执行分别确认，不默认等同存储XSS。

来源：[保存帖1](https://x.com/i/status/1689326423696187397)、[保存帖2](https://x.com/i/status/1689745937831546883)。


## 包名识别不能代替Android备份权限验证

aapt dump badging应指向实际APK文件，保存命令abc.ap可能是扩展名误写。包名仅定位对象，非root备份还取决于系统版本、应用allowBackup/导出规则、数据排除与开发选项。用自有包核对Manifest和可备份标记数据，不能从识别包名直接推断/data目录可读或可导出私有数据。

来源：[保存帖1](https://x.com/i/status/1689536054762848256)。


## 保存图证0188-126-android：机制与验证条件

Rayder0.0.4 APK threads.apk经Apktool2.5.0解析资源/manifest/dex后抽URL，输出含Android文档/Apple/Wikipedia/FB/第三方。静态字串混SDK/示例/第三方且可能缺动态拼接，需包hash/version/sourcecallsite归属，不执行APK/扫所有域。 可用原图：`1696170735570432362-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1696170735570432362)。


## Firebase Remote Config 的客户端可见性与真正秘密（0188）

Remote Config 通常要向移动客户端提供配置；检查 APK 和已有应用流量中的配置键、版本及用途，辨别公开功能开关、测试值与本应服务端保管的秘密。客户端能读取配置不等于未授权敏感泄露。以自有应用的正常读取和脱敏样本确认权限边界，不使用发现的 API 密钥或扩大到其他 Firebase 服务。

来源：[保存帖1](https://x.com/i/status/1693653452704858304)。


## 保存图证0189-115-android：机制与验证条件

Cloudflare WARP Android 2043885/CVE2023-3747：管理员禁止禁用WARP但可发临时override code；本地可访问设备者调设备日期时间延长断开时限，摘要称缺服务端验证。复用时间信任边界：墙钟回拨/向前/重启/恢复联网与服务器有效期、单调时钟计时/回放比较，授权自有管理设备上确认真实隧道与策略状态，不能仅UI倒计时。需先有有效override及本地控制，不是远程无认证接管，不在用户实际设备改时钟。 可用原图：`1699769630632665134-02.jpg`（保存帖 1699769630632665134）。

来源：[保存帖1](https://x.com/i/status/1699769630632665134)。


## 保存图片中的机制与证据边界（1704641887104098496-02.png）：by-type/mobile-android.md

图片 `1704641887104098496-02.png`：ARM64反汇编显示svc 0x0及w8=0x38、寄存器设定，提示可能通过直接syscall绕过仅libc层hook的观测；图缺上下文函数/返回值/路径，不证明实际root检测绕过。区分libc封装与指令级调用，在自有测试APK静态调用点、ABI和运行分支最小标记对照；不臆造寄存器值含义/支持所有版本。

来源：[保存帖1](https://x.com/i/status/1704641887104098496)。


## 保存图片中的机制与证据边界（1704915539108282415-02.jpg）：by-type/mobile-android.md

图片 `1704915539108282415-02.jpg`：QuadraInspect帮助菜单SET target及START install_tools/apkleaks/andropass/mobfs/rms，fake.apk与RMS1.5.15本地5000服务启动。框架集成静态/动态入口，启动不是实际APK漏洞检测；输入副本、工具版本、路径/来源和动态沙箱要核对，静态告警与运行证据分别保存。不执行安装、APK或开启服务。

来源：[保存帖1](https://x.com/i/status/1704915539108282415)。


## 保存图片中的机制与证据边界（1705547136434106470-02.jpg）：by-type/mobile-android.md

图片 `1705547136434106470-02.jpg`：Frida16.1.3 -U -l root_bypass.js -f遮蔽包，Pixel连接/Spawn恢复后右侧注册页；只表明插桩启动和可见UI，不显示脚本hook内容、JailMonkey版本或业务后端结果。比较自有APK正常root警告与同环境插桩后完整状态、hook返回及服务端敏感功能，不能由注册UI宣称全局安全绕过。

图片 `1705547136434106470-03.jpg`：另一图Device Non-Compliant/rooted警告且App disabled，未显示root_bypass脚本或与前图统一设备/配置。可作为候选基线；客户端root检测不是服务端权限，保留同设备、构建、会话和单变量对照，不能凭两图时间顺序证明绕过成功。

来源：[保存帖1](https://x.com/i/status/1705547136434106470)。


## 0195：Frida 与系统证书配置是测试环境前提

Pen-Andro 宣传安装应用、frida server 与移动 Burp 证书。绑定自有设备/模拟器、Android/应用版本、root 权限、CA 信任来源及应用 pinning，比较未修改和受控配置后是否实际出现可解密请求。文件已放目录或 Frida 已启动不是捕获成功，也不是真实生产环境无需权限的漏洞；未安装或改设备配置。

来源：[保存帖1](https://x.com/i/status/1718723571323945458)。
