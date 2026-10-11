# JavaScript 原型污染

适用信号：递归合并、路径赋值、配置对象或查询解析

## 检查与最小实验

追踪输入源→解析/合并→原型变化→读取该属性的具体代码。先在匹配库版本的隔离环境用唯一无害属性检查，区分对象自身属性与其他新对象继承的属性。

浏览器端检查污染的生命周期及可达 sink；服务端污染可能持续影响进程中的其他请求，因此缺少隔离与恢复能力时只做代码/本地验证。不能把删除测试字段当作完整恢复全部原型状态。

## 证据与反例

JSON 中有 `__proto__`、响应回显该键、对象有同名自身属性都不等于全局原型被污染；污染成立也不自动证明可利用 gadget 或 RCE。具体影响需绑定实际属性读取和受控行为变化。

## Agent 行为

把污染源与 gadget 作为两个假设存证。禁止线上试改认证、全局超时或进程关键配置来找效果；使用隔离进程的清理/重启能力核对恢复。

## 调研来源

- [PS-proto · Prototype pollution](https://portswigger.net/web-security/prototype-pollution)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。


## 原型检测标记、否定匹配与失败分母

旧自动化管线查询中写testparam值exploit/，JS判断却与exploit比较；grep VULNERABLE还会保留NOT VULNERABLE，配图两种输出确实同列。先逐字核对URL生成→实际query解码→属性值→判断→结构化结果，避免正负共享子串。[URL query state](https://url.spec.whatwg.org/#query-state)及编码集合保留查询里的普通斜线语义；图未显示应用额外去尾斜线处理，不能无证据补齐值差异（2026-10-10核读）。

window属性相等仅定位观察，还需排除自身属性/页面预置值，确认原型变化、隔离生命周期及真实gadget读取；污染不自动XSS/RCE。stderr重定向隐藏错误，不能把超时/解析失败计阴性或已完成；grep后的列表也不是有效漏洞数。用自己的有限合成正/负/错误记录核对判定，原来源脚本、无头浏览器/JS和外联请求均未执行。来源：[保存帖](https://x.com/i/status/1402906185301323776)。


## 本地污染fixture与控制台主动原型写的差别

Plution图对本地fixture输出Vulnerable；JSPanda图控制台直接defineProperty Object.prototype后显示CLOSURE_BASE_PATH Polluted。

绑定应用控制入口、实际原型写、属性读/gadget和权限/后果，每次实验隔离并恢复；scanner标签、自有console写入、无应用source、没有gadget或非真实目标是反例。主动写入是实验动作，不证明应用允许攻击者污染或已XSS，本轮未执行图中JS。

来源：[保存帖1](https://x.com/i/status/1438476371408343040)、[保存帖2](https://x.com/i/status/1441149046068940801)。


## 原型污染库定位与gadget分开的数据库复用

图DetectionSelenium/extension/CodeQL→关键词/断点/阻断JS定位库→sourcegadget，再存librarygadget库和被动regex检索。

记录库hash/版本、可控合并输入、实际prototype写入、具体gadget读属性到sink与受害origin，用移除库/禁source/无害marker对照；关键词、网站引入库、断点或主动屏蔽导致页面坏掉是反例。数据库匹配与污染、污染与XSS各单独取证，作者18/80/1000自述不当当前确认数。

来源：[保存帖1](https://x.com/i/status/1445403406571614214)。


## PPScan 到 XSS 的 gadget 缺口

正文说ppmap把prototype pollution升级为XSS，图片为工具封面。

需要可控的原型写入、污染传播、实际gadget、活动DOM消费者及浏览器执行条件；检测器存在不代表目标具备整条链。自身属性覆盖、冻结原型、无消费者、安全文本输出和CSP限制为反例，不自动把PP报告升级XSS，也不运行扩展或payload。

来源：[保存帖1](https://x.com/i/status/1461205450146271238)。


## Plution 十一案例不能等于所有原型污染

完整正文称headless Chrome用硬编码payload检测十一种已列案例，没有具体目标的数据传播或实际sink。案例数是样例覆盖，不是全部对象写入。

离线自有JS模型比较普通属性、原型写入、后续gadget读取、可达sink、隔离world/权限与防护；记录工具版本、触发和误报/遗漏。单payload命中、对象污染而无消费者或只console为反例，不能直接推XSS/账号影响，不执行源扫描器。

来源：[保存帖1](https://x.com/i/status/1494703262724988933)。


## Rocket.Chat 管理员原型污染与托管宿主权限边界

CVE-2023-23917历史摘要明确原型污染到RCE在admin账户下，用户能自建云server当admin，可能影响云基础设施；没有source/gadget代码。应用管理员、应用进程执行和宿主隔离是三层权限，不能把管理员动作自动视为获得宿主root，也不能按“管理员本来全权”忽略托管边界。源码审查需污染入口、继承读取和危险sink；隔离夹具以无害标记证实，云影响须独立权限证据。

来源：[保存帖1](https://x.com/i/status/1632093694017896451)。

现有图片证据 `1632093694017896451-02.jpg`：Rocket.Chat CVE-2023-23917历史摘要称admin账户原型污染到RCE、用户自建云server取得admin可能影响云基础设施；无污染source/gadget，管理员应用权限与宿主隔离应分开。


## EJS gadget 题名不足以证明污染到执行

SSPP→EJS RCE外链仅题名，需分别确认可控对象合并/原型写入、受影响属性实际消费、EJS版本/配置和生成代码权限。固定受控污染/不污染及属性隔离对照，记录实际结果；gadget存在不等入口可达或所有模板可利用，未保存文章不补造代码链。

来源：[保存帖1](https://x.com/i/status/1636684863603449856)。


## 服务端原型污染工具候选需分离写入原语与利用消费者

SSPP 工具卡片及简介用于定位服务端原型污染。保存的品牌/功能说明不能证明目标污染成立；实际验证需核对对象写入路径、合并方式、是否可改变原型、受控状态及清理/隔离，再定位利用该状态的消费者。检测信号、错误或工具宣称支持 RCE 不等于可执行代码；持久化污染与跨请求影响需独立证据，并避免破坏共享进程状态。

来源：[保存帖1](https://x.com/i/status/1647590162908725250)。


## DOM 跳转候选不自动推出原型污染 XSS

保存正文建议从 DOM Open Redirect 入口继续测试原型污染。两者是独立假设：先证明输入影响导航，再定位对象写入、原型/继承与自有属性差异，最后找实际读取污染值的 gadget/sink。仅路由、跳转或参数名称不能确认污染与执行；保存材料无代码、对象状态或浏览器结果，不补成万能递进流程或运行候选。

来源：[保存帖1](https://x.com/i/status/1682065347015311360)。


## 保存图证0189-75-proto：机制与验证条件

运行时日志列 [PP][Prop delimiter/depth/ignoreQueryPrefix/interpretNumericEntities/parameterLimit/parseArrays/plainObjects/strictNullHandling] qs/lib/parse.js，Express locals/_all、body-parser _body/body、type-is transfer-encoding/content-length、etag time、fresh if-modified-since 等属性/元素访问及行号。可复用插桩追踪原型继承键到实际消费者的传播，区分读取与写入/污染源；日志并无污染请求或可利用sink，不能将每次prop读取等同SSPP。受控干净进程比较own-property/原型来源、依赖版本、输入源及无害副作用，防跨测试状态残留。 可用原图：`1698503479239598559-02.jpg`（保存帖 1698503479239598559）。

来源：[保存帖1](https://x.com/i/status/1698503479239598559)。
