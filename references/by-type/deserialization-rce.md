# 反序列化与不安全对象处理

## 适用信号与前提

序列化请求体、Cookie、对象类型标记、服务端调用栈或获准源码中的反序列化入口。Java/PHP/Python/.NET 各有不同格式和危险条件；Base64、rememberMe、库名本身不是漏洞。

## 最小实验

先记录正常请求的格式、组件/版本和可达调用路径。优先用无害格式变更与应用错误对照识别解析，不将其直接确认为执行。

有具体数据流和组件依据、且动作获准时，选择本地验证过且不写文件的最小探针。带外只用唯一随机标记与受控接收端；不得盲目发送会加载远程代码的 JNDI/gadget 链。必要时仅在自建隔离环境研究链条适用性。

## 确认与反例

把“不安全反序列化”“类型实例化”“网络解析”“任意命令执行”分开判定；分别提供违反预期规则的证据。DNS 事件可以支持触发了某解析行为，不自动证明 RCE。自建环境成功不证明目标使用相同配置或依赖。

排除正常数据校验、允许的类型、版本差异、类不可达、出站代理/安全扫描触发和旧带外标记。报错或解析失败只能保留线索。

## 下一步、停止与报告

缺少组件/链条件时转被动分析或待补证，不扩大试链集合。禁止落地文件、后门、反弹连接和内部横向操作；不为回显读取敏感数据。

报告说明入口、格式、组件依据、实际触发能力、带外归因及环境差异；执行类结论使用 [验证标准](../verification.md)。

## 调研补充：可执行检查点

- 先确认格式、解码包装、签名位置与实际反序列化库；Base64、JSON 或 Java 魔数仅是线索。错误栈也不证明对象已被不安全实例化。
- 优先用自建对象的无害属性变化检查是否影响不应受客户端控制的状态；完整性验证必须在危险对象恢复前生效。
- gadget 可用性取决于运行时、依赖和触发方法；组件版本命中不能代替可达性。需要执行链时先在匹配的隔离环境验证无副作用路径。
- 不运行未知 gadget 包、无差别链枚举或有删除/联网/持久化行为的现成 PoC。证据只支持属性篡改时就报告该影响。

## 调研来源

- [PS-deserialize · Insecure deserialization](https://portswigger.net/web-security/deserialization)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。

## 归档案例补充：调用点与输入类型

JSON 外层解析、对象恢复和后续转换可能分别触发不同逻辑；记录真实调用点、重载、依赖、str/bytes 与中间规范化。检查器接受或拒绝与恢复器不同只是线索，类加载不等于执行。CTF 人为添加的 gadget 和配置只作为前提，不能迁移为部署结论。见 [K12](../research/crawl-xz-patterns.md)。

## PHAR 元数据的版本与调用边界

`file_exists`、PHAR 引用或可上传归档不等于反序列化执行链。先固定 PHP 版本、实际流包装/归档调用、攻击者可控元数据、对象恢复位置及可达类/触发方法；将路径可达、元数据解码、对象实例化和命令执行分开证明。[PHP 8.0 迁移说明](https://www.php.net/manual/en/migration80.incompatible.php#migration80.incompatible.phar)明确记录 PHAR 元数据不再自动反序列化的变更，不能将旧版本材料的隐式触发条件直接套到 8.0 部署；显式恢复元数据或业务自定义处理仍需跟实际调用。官方资料核对日期：2026-10-09；未生成或运行恶意归档。

若对象恢复链只支持文件删除，报告先限定于可控路径、执行身份、实际消费者与删除范围。优先分析源码/隔离副本中自建文件的生命周期和恢复结果，不删生产配置或访问控制文件去提升影响；缺失.htaccess等配置是否改变保护取决于真实部署，不能凭文件名升级为执行或接管。

## 空文件名IO错误与对象反序列化消费者

空文件名导致java.io栈错误，只能定位某个文件/IO处理路径；java.io包名不证明该入口调用对象反序列化或存在可用gadget链。沿真实文件名/内容解析、异常来源、ObjectInputStream或其他对象解码器、信任边界、依赖版本/classpath、过滤配置及后续危险消费者追踪。

已有获准源码/脱敏异常中区分文件不存在/合法拒绝、信息暴露与攻击者可控字节进入对象构造；再判断能否越过对象类型/资源限制，不能由包名跨跳推RCE。源文未给反序列化调用链，不运行ysoserial、上传序列化载荷或读取系统文件来补证。


## 反序列化标题与PHP命令字段及Node解析栈的分离

同帖的PHP图直接POST cmd并显示www-data输出，未显示序列化对象；Node图出现JSON.parse/unserialize与500 Unexpected end JSON。前者不能由标题改称反序列化漏洞，后者只定位输入/解码候选，尚未补对象构造或危险调用。

Cookie图同时Welcome Admin和Please Login，不能计认证完成；扫描图与请求图私网IP/日期不同，需先绑定实例/制品/时点再关联。PHP Content-Length与可见正文不一致也不能静默修成可重放PoC。无原始材料的gadget、root与接管均保留未证，本次未执行代码或复制Cookie。

来源：[保存帖1](https://x.com/i/status/1411248538005082113)。


## Orion ViewContext JSON 的 Objects 设置与外部来源

ParseViewContext 图设置 TypeNameHandling=1 并反序列化 AlertingActionContext。

Json.NET 官方枚举的 1 是 Objects，Auto 是 4；非 None 处理外部 JSON 应验证输入类型，官方提示自定义 SerializationBinder。继续追 ViewContextJsonString 控制者、签名/保存过程、兼容类型和真实副作用。配置一行、内部可信 JSON 或无可利用兼容类型都不能证 RCE，不构造 gadget。[Json.NET 枚举](https://www.newtonsoft.com/json/help/html/T_Newtonsoft_Json_TypeNameHandling.htm)。

来源：[保存帖1](https://x.com/i/status/1452833644834217986)。


## Django debug 与 Pickle 会话的实际入口

正文给Debug/PickleSerializer候选，未保存目标session配置或受控反序列化输入。

先看实际sessionengine、serializer版本、cookie/服务器存储边界、签名验证、secret来源与调用者。debug开启不直接等于pickle消费，可信服务器存储、不同serializer或签名拒绝为反例。历史类名不证明当前可用或所有Django受影响；不构造pickle或提取秘密。

来源：[保存帖1](https://x.com/i/status/1454661107759689733)。


## SOAP 序列化字段与 Java 类探测不能直接推出 RCE

SOAP 图片包含实体令牌、Cookie 和长序列化样式字段；另一正文介绍类路径探测工具。

先定位传输字段、真实解码/反序列化消费者和适用版本，再区分类是否存在、对象是否实例化、方法是否可达及最终动作。可见格式或探测回调不证明完整 gadget 链和代码执行，截断图片与未保存实现不补全。

来源：[保存帖1](https://x.com/i/status/1524876410204086300)、[保存帖2](https://x.com/i/status/1526578285244825601)。


## 序列化 Cookie 与 dump 题名不能证明秘密或 RCE

一图只显示 API 请求的认证标志和长 data Cookie，正文另称 Java dump 暴露秘密；另一正文列多种 Ruby 解析器。

先确定真实编码、格式、解析 API 和安全模式，追类型实例化与字段如何进入身份判断。客户端标志不能当服务端可信状态，编码字符串也不是 dump 内容；没有响应、秘密字段或执行产物时不补造完整链。

来源：[保存帖1](https://x.com/i/status/1531289327069712385)、[保存帖2](https://x.com/i/status/1531546977246162944)。


## JNDI 元数据回调与任意代码执行分别定级

正文展示通过目录服务回调携带环境属性的思路。只有实际收到并能归属该请求的参数，才支持对应信息/出站连接；DNS 解析、LDAP 到达、环境字段替换与执行器加载分属不同证据。不能因回调含系统字样就判 RCE，需明确运行时版本、允许的解析机制和部署影响，本轮不运行归档表达式。

来源：[保存帖1](https://x.com/i/status/1538249538993004545)。


## 历史反序列化通告需区分写文件与可执行落点

保存Full Disclosure目录和SoListingTabs通告片段描述数据库、会话及Twig文件系统对象链。目录题名只用于发现；实际判断需绑定目标版本、序列化输入入口、可达对象与配置。文件写入、可执行Web目录、处理器映射和真正触发是不同阶段，写到临时目录不等于Web执行。只以自有无害标记证明边界，不照搬Webshell、磁盘耗尽或未知历史载荷。

来源：[保存帖1](https://x.com/i/status/1555621441877442562)、[保存帖2](https://x.com/i/status/1556199179177033728)。


## LDAP主机名回调只证明被观察到的求值层

正文给包含hostname的LDAP/OOB候选。先确定受影响组件、当前版本/配置、用户字段到查找函数的真实路径；使用自有非敏感关联标记区分DNS解析、LDAP连接、表达式展开和后续代码执行。仅收到网络请求不证明RCE、反序列化或任意文件读取，不把档案字符串当自动探测脚本，也不泄露真实主机名。

来源：[保存帖1](https://x.com/i/status/1566475677573996545)。


## 反序列化类型转换发生在对象读取之后

截图概述readObject在最终类型检查前可能执行对象逻辑，条件包括实际不可信字节进入反序列化及可达类路径。代码审计需从入口/认证、serializer、allowlist、构造/读取方法到可达副作用逐段连接，用隔离自有无害标记验证；最终cast、CVE名字或某库存在不证明目标RCE，未保存产品路径不补造。

来源：[保存帖1](https://x.com/i/status/1582416676775157763)。


## Java RMI lookup 响应 readObject 是需审计的反序列化入口

图片代码显示 lookup 将名称 writeObject 给远端，取返回流时 readObject 后强转 java.rmi.Remote。类型转换发生在读取之后，审计应追踪数据来源、注册表可信边界、对象过滤与可达类，不只检查最终接口类型。用隔离自建注册表和无害对象比较正常引用、拒绝类型及过滤日志；看到 readObject 不自动意味着 gadget 可达或代码执行，截图并未给完整恶意对象与调用结果。

来源：[保存帖1](https://x.com/i/status/1586723184480501761)。


## Kafka connector 的 JAAS 配置可把配置写权引向类加载

保存图描述 MySqlConnector 的 producer sasl.jaas.config 被设为 JndiLoginModule 后进入 LDAP/反序列化路径；末端被截断。追踪租户配置写权、允许 LoginModule、网络出口、加载类及实际反序列化消费者，在隔离自建配置比较允许模块与拒绝非预期模块。JNDI/LDAP 交互不等命令执行，gadget/类/配置必须实际存在；配置控制与初始攻击权限分开，不从未保存外链补造链。

来源：[保存帖1](https://x.com/i/status/1589869535594774528)。


## SSRF 到 SVNBridge 反序列化需要控制实际缓存字节

GitHubEnterprise保存摘要将SSRF、可控被反序列化数据、memcached/SVNBridge与潜在RCE连接，列历史修复版本但无具体入口/gadget。审计网络可达、缓存写/读键、序列化类型与消费者身份，隔离用无害对象比较可信来源与拒绝不可信数据。能请求内网不等能写任意缓存或加载gadget，缺连接证据不能补造完整执行，历史版本不替代当前advisory。

来源：[保存帖1](https://x.com/i/status/1592995021845938176)。


## JNDI 表达式与回连：日志消费、网络交互、执行三级证据

1593675056475000833-02.jpg 保存 URL 参数中的 JNDI LDAP 表达式和 hostName 回连主张。可迁移线索是参数是否进入日志组件及解析器；在授权隔离环境区分输入保存、日志求值、DNS/LDAP 交互和最终执行，每级需独立证据。一次回连不能证明任意命令执行；历史 Log4J/CVE 标签也不能确定当前版本、配置或可达性。

来源：[保存帖1](https://x.com/i/status/1593675056475000833)。


## JSON 类型选择到 Spring XML：类实例化与生命周期消费者

1595484816623173632-02.jpg 展示 JSON 指定 FileSystemXmlApplicationContext，再引用含 ProcessBuilder 生命周期的 XML。可复用审计边界是多态类型策略、可加载类/依赖、远程配置解析、bean 生命周期与进程权限。形式为 JSON/XML 不代表没有反序列化风险，类名存在也不代表可达；用隔离代码审计或无副作用 mock 逐段验证，不运行图中的 shell/数据外传命令，也不从海报统计推断语言漏洞分布。

来源：[保存帖1](https://x.com/i/status/1595484816623173632)。


## PHAR 包装器与元数据反序列化触发点应分别审计

保存正文只有 phar:// 与 PHP 反序列化到 RCE 的入口线索，BlackHat 2018 封面没有完整链。追踪可控文件路径、实际 PHP/扩展版本、触发的文件 API、元数据加载/反序列化与可达对象方法，区分普通文件访问和对象恢复；RCE 还需可达 gadget/sink 及其权限。仅对自有无害对象做离线源码与正负实验，不执行归档、载荷或假定任何 phar:// 调用都反序列化/执行。

来源：[保存帖1](https://x.com/i/status/1611782714293907456)。


## 不可信 PHP unserialize 调用与 gadget 触发之间

表情图给unserialize($_GET[param1])，外链源码未保存。该输入到对象恢复函数是审查线索，还须可用类/自动加载、magic method、属性数据流和实际危险sink；不能从调用名直接宣称RCE。以本地无害对象对照允许类、类型验证及副作用日志，区分普通数据解码、对象注入和代码执行。图没有执行结果。

来源：[保存帖1](https://x.com/i/status/1630901737182879744)、[保存帖2](https://x.com/i/status/1630895910153596928)。

现有图片证据 `1630901737182879744-02.jpg`：PHP serialize/unserialize表情图末行unserialize($_GET[param1])提示不可信输入，但没有gadget或执行，不能从调用直接推出RCE。


## 反序列化标题下误贴的 HRS 定义须纠正

Day53封面写不安全反序列化，但正文是前后HTTP服务器处理请求不同的解释，属于请求走私机制。反序列化应证明不可信对象数据进入相应解码器、允许类型/gadget及实际副作用；HRS则看代理链字节边界及连接复用。不要把二者概念混用，封面与错误定义均没有具体复现。

来源：[保存帖1](https://x.com/i/status/1634077935224123394)。


## PHP 自定义 gadget RCE 案例明确要求已有权限

ExpressionEngine摘要明确登录控制面板且有权限后构造链，最终High8.5，缺代码。追踪不可信序列化对象、可达类/魔术方法、链触发和进程权限，区分已授权操作能力与新增边界。不能从题名写成匿名Critical或给出未保存gadget，不执行对象payload。

来源：[保存帖1](https://x.com/i/status/1640836475158773761)。

现有图片证据 `1640836475158773761-02.jpg`：ExpressionEngine 报告摘要明确研究者已登录控制面板且具备权限，构建自定义 gadget 链到 RCE，最终 High 8.5；无 gadget 代码。反序列化需要可控对象、触发方法、可达链和进程权限，不能写成匿名 Critical。


## 反序列化清单中的类型和签名控制需绑定对象图及解析时机

二十五项图覆盖输入/类型/类过滤、对象图/长度、签名、沙箱、行为、日志、依赖与培训。评估实际入口、序列化格式、可达类及 gadget、运行权限和解析器配置；强类型语言、匹配 Content-Type 或宣称有签名都不自动安全。签名要可信密钥且在解析前验证，白名单须限制实际类/对象图并配合资源边界。用隔离样本证明可达消费者及负例，清单完成和组件名不能替代可利用性结果。

来源：[保存帖1](https://x.com/i/status/1648314484744769536)。

现有图片证据 `1648314484744769536-02.png`：反序列化25项检查清单；强类型、内容类型、签名本身不能排除可达gadget，签名要可信密钥并在解析前验证；需要类白名单、对象图/长度限制、运行时权限和实际消费点。


## Kubernetes Java YAML 库的风险需证明下游可达

图提 Kubernetes Java Client 17.0.0 的 Dynamics 将不可信 YAML 转 DynamicKubernetesObject 与 SnakeYAML/CVE-2022-1471，作者未找到测试之外下游使用。核对实际入口、构造/类型限制、类路径与运行权限，在隔离无害样本验证消费链。依赖出现、公共 API 或裁切 JAR 代码不证明部署可被远程利用，不能概括全部 Kubernetes/JVM 或自动认定命令执行。

来源：[保存帖1](https://x.com/i/status/1650922774062301188)。

现有图片证据 `1650922774062301188-02.jpg`：KubernetesJavaClient17.0.0 Dynamics反序列化不可信YAML到DynamicKubernetesObject，SnakeYAML/CVE2022-1471/JVM执行摘要，作者未找到下游使用，JARcode开头裁切；依赖可达性/类加载/运行权限必需，不是全K8s远程RCE。


## XMLRPC 序列化限制不能替代反序列化类限制

Ruby XMLRPC0.3.2 图在 create.rb 以 ENABLE_MARSHALLING/Marshallable 限制序列化，但 parser struct(hash) 读取 __class__ 的反序列化限制不足。分别跟踪来自 request 或 response 的 XML/hash 到类解析、实例构造和副作用，确认 marshalling 配置与可达性；XML 解析并不自动构成 XXE，任意类名也不自动等于 RCE。下部代码裁切，未见 gadget 与实际执行不补造；图状态 Informative 与 High 自评独立。

来源：[保存帖1](https://x.com/i/status/1686640752393363456)。

已审阅原图 `1686640752393363456-02.jpg`：RubyXMLRPC0.3.2 create.rb Config ENABLE_MARSHALLING和XMLRPC::Marshallable序列化限制，但parser struct(hash)读取__class__反序列化类不限制；上下半代码裁切，需反序列化分支可达/对象副作用独立证明，不把XML等同XXE。


## 保存图证0187-70-deser：条件与证明边界

Kredis JSON历史CVE2023-27531，特制JSON可产生意外对象，Fixed1.3.0.1，截图VersionsAffectedAll是公告当时概括。JSON名义格式不保证只构造基础值，追踪decoder/object hooks和不可信来源，比较标量/普通对象/受限类解析；未展示可达gadget或RCE。 可用原图：`1691555623689994397-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1691555623689994397)。


## 保存图证0187-81-deser：条件与证明边界

H1Disclosed转发Kredis JSON公告，小图可读固定1.3.0.1、特制JSON可能产生意外对象，未增加gadget/RCE条件。是同历史CVE摘要的不同来源截图，需与实际JSON.load源码区分，图无新增运行结果。 可用原图：`1691714219656556905-02.png`。

来源：[保存帖1](https://x.com/i/status/1691714219656556905)。


## 保存图证0187-84-deser：条件与证明边界

Kredis v1.3.0 type/json.rb可读cast_value(value)直接JSON.load(value)，报告指出意外class反序列化CVE2023-27531。追踪不可信value与库对象恢复功能，比较纯基础类型解析和禁用class恢复；PoC下部被截断，无完整gadget或执行结果。 可用原图：`1691736763226902915-02.jpg`。

来源：[保存帖1](https://x.com/i/status/1691736763226902915)。


## JSON.load 与 gadget 链的实际可到达条件（0187）

Kredis CVE-2023-27531 图证展示旧版类型转换中的 `JSON.load(value)`，公告指出构造 JSON 可恢复意外对象，修复为 1.3.0.1。跟踪外部输入如何进入 Redis 值并到达该调用，确认对象恢复行为和可用类；`JSON.parse`、配置不同或不可控值是反例。Apache Commons、Jackson、ysoserial/phpggc 名称只提示调查方向，RCE 还要求可到达反序列化入口及匹配 gadget，不执行生成的攻击链。

来源：[保存帖1](https://x.com/i/status/1691555623689994397)、[保存帖2](https://x.com/i/status/1691714219656556905)、[保存帖3](https://x.com/i/status/1691736763226902915)、[保存帖4](https://x.com/i/status/1693578696597045726)。


## 重复图片中的 Kredis 历史 JSON 公告（0188）

本帖正文只介绍转发账号内容变化，可用旧图 `1695672845760893260-03.png` 仍展示 Kredis CVE-2023-27531 特制 JSON 可能恢复意外对象及修复 1.3.0.1。复用此前完整图像审阅，不再次计数；公告摘要与具体 JSON.load 可达输入及 gadget 执行条件不同，不能从图推导完整 RCE。

来源：[保存帖1](https://x.com/i/status/1695672845760893260)。


## 保存图证0189-135-deser：机制与验证条件

Airflow Spark provider CVE2023-40195/2127968摘要 before4.1.3：已装Spark provider且用户有配置Spark hooks/connection权限，把连接指向恶意Spark服务器使pyspark客户端处理不可信反序列化数据，Airflow节点可能执行代码。4.1.3主要增加明确文档警告，建议该配置权只给完全可信用户；不能称升级后允许非可信任者配置任意Spark服务器即安全，Airflow core版本与provider分开。图无gadget字节/执行回显，用隔离mock服务器及无害数据流标记验证配置→连接→解码/权限边界，不部署恶意服务。 可用原图：`1700147117245829526-02.jpg`（保存帖 1700147117245829526）。

来源：[保存帖1](https://x.com/i/status/1700147117245829526)。
