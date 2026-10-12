# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
facets = [
  [
    "targeted-fuzzing.md",
    "Burp Sniper 单密码位置和 spray 会话基线分开",
    "保存Burp图是wp-login POST、Sniper一个密码位置及现有Cookie/CSRF字段，正文另列spraying/session/revalidation/SSL主题；界面未开始运行。\n\n离线请求模型分账号轴与密码轴，固定一次操作身份并标出CSRF取值及会话过期；记录哪字段改变、每账号计数与实际认证后的身份。只有请求重复或200登录表单不是成功，也不能由SniperUI推断spray或TLS被剥离。不提交密码尝试。\n\n来源：[保存帖1](https://x.com/i/status/1503747849326059522)。"
  ],
  [
    "by-type/mobile-android.md",
    "DirtyPipe 手机演示要核内核构建与有效 uid",
    "正文称Pixel6/S22受影响，但保存图只有手机和sh5.1提示，无可辨型号、内核构建、有效uid或完整步骤。\n\n在自有隔离模型记录设备构建、内核补丁、原身份及前后实际uid，区分本地写入前提与远程入口；root样式提示符或另一型号名称不是特权提升证据。不连接设备、执行PoC或修改系统文件。\n\n来源：[保存帖2](https://x.com/i/status/1503766361369346050)。"
  ],
  [
    "by-type/idor-access-control.md",
    "X Client IP 回环线索要跟随入口与后端同资源",
    "正文重复127.0.0.1头绕403提示，没有保存响应。\n\n固定角色、对象和路径，在本地代理模型比较无头、可信代理字段和不可信客户端自填字段，确认后端最终信任值以及对象权限；若入口移除字段、只返回公开页或身份不变则无越权。状态码差异不替代受限内容或操作证据。\n\n来源：[保存帖3](https://x.com/i/status/1503786956458627073)。"
  ],
  [
    "by-type/xss.md",
    "自动属性 XSS 的 Collaborator token 不等账号接管",
    "正文将HTML属性注入、无交互与criticalATO关联；图有DNS/HTTP交互及GET t参数，token大部遮蔽。未保存源HTML、自动事件、回连主体及token消费。\n\n隔离追输入→属性DOM→事件触发→同源认证消费者，比较正常文本/事件禁用/CSP阻断及无登录读者；留唯一标记与产生者。DNS或HTTP可能来自渲染服务、安全扫描器或预览，不直接证明浏览器XSS或可用认证token，不主动回连。\n\n来源：[保存帖7](https://x.com/i/status/1503816543381209088)。"
  ],
  [
    "source-audit.md",
    "IDA 二进制补丁 UI 要绑定字节与重定位",
    "Patching图可辨call exit、地址和机器字节，保存正文只工具简介。\n\n对自有合成二进制绑定原hash、架构、文件偏移与加载地址，记录修改前后字节、指令边界、重定位和本地行为对照；内存patch不等持久文件patch，NOP或改call不能推出远程漏洞。图中短代码不执行，不借工具名称补写未保存实现。\n\n来源：[保存帖11](https://x.com/i/status/1503978009925197826)、[保存帖14](https://x.com/i/status/1503996149161553920)。"
  ],
  [
    "by-type/authn-session.md",
    "password 弱密码报告文字仍需真实认证身份",
    "2500故事图写password和dashboard/projects及登录附件，但账号和URL遮蔽、未保存认证交换。\n\n自有模型用已知测试凭据区分表单接受、会话签发、登录后用户/权限；报告需说明默认/弱密码生命周期和账号归属。仅字段值、附件或跳到dashboard不证明P1或RCE，不尝试保存账号。\n\n来源：[保存帖12](https://x.com/i/status/1503985938048827394)。"
  ],
  [
    "by-type/info-secrets.md",
    "Git 敏感路径清单要分元文件和可恢复对象",
    "清单包括gitHEAD/index/logs与gitattributes/gitkeep/modules/review、svnentries/ignore；它们敏感程度不同。\n\n以离线合成仓库比较元数据、对象与历史实际内容，保持文件路径、hash、提交关联和secret目的；一个gitkeep或普通ignore不证明源码恢复/凭据泄露。可恢复对象也需最小字段归属，不能仅200判敏感或扩展到整库。\n\n来源：[保存帖16](https://x.com/i/status/1504007366081134594)、[保存帖49](https://x.com/i/status/1504461608554094595)、[保存帖214](https://x.com/i/status/1507701393909432320)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "WMEye 项目创建日志和横向执行分开",
    "图可辨目标IP/用户名凭据输入、连接及ShellcodeProjectcreated日志，正文描述WMIEventFilter/MSBuild横向移动；缺远端实际执行或对象访问。\n\n自有本地模拟将项目生成、连接授权、触发事件及远端效果分阶段绑定，比较触发/未触发与权限不足；生成目录不能继承执行结论。凭据不复制使用，不创建生产事件订阅或执行shellcode。\n\n来源：[保存帖23](https://x.com/i/status/1504068657575510025)。"
  ],
  [
    "by-type/xss.md",
    "innerText 写入文本不能代替所有上下文防护",
    "正文建议innerText代替innerHTML且不要eval/newFunction，又将HTML编码表述为总能缓解。\n\ninnerText适用于文本消费节点，不能保护后续URL、属性、JS源码或再转innerHTML的链。离线比较同字符串在文本节点、HTML、引用属性与代码消费者中的结果，记录每次转义顺序和后续读取；一次文本安全写入不证明整个页面安全。\n\n规范核对：[MDN innerText](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText)。\n\n来源：[保存帖26](https://x.com/i/status/1504117309140516867)、[保存帖112](https://x.com/i/status/1505935118900281344)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Osmedeus 模块工具表不是各阶段成功回执",
    "图列subdomain/probing/SSame/spider/fingerprint/sto/ipspace/vulnscan/portscan/dirbscan及各工具；另一图只有厂商logo。\n\n保留域→IP→HTTPHost→站点结构→指纹→检查输出关系、版本、错误与未跑阶段。SSame内容相同可能不同身份业务，不宜丢所有对象；工具名或logo不能证明top100漏洞、全资产覆盖或执行完。\n\n来源：[保存帖17](https://x.com/i/status/1504012141518487558)、[保存帖27](https://x.com/i/status/1504129198663016452)。"
  ],
  [
    "by-type/info-secrets.md",
    "Git 删除 secret 文件仍需历史与撤销证据",
    "Git图说明提交删除后旧history仍可见、需要revoke/rotate，并用SolarWinds故事示意。\n\n自有离线仓库比较tip不存在与祖先对象可读，记录受影响refs/克隆副本与撤销记录；删除文件不等历史清理，重写历史不等旧secret失效。示意中的账号不使用、故事不推广成当前事件；最小报告说明secret类别与可见范围。\n\n来源：[保存帖35](https://x.com/i/status/1504287525682167808)。"
  ],
  [
    "by-type/csrf.md",
    "CORS 读权限与 CSRF 状态修改是两个门",
    "正文称攻击域带credentials可造成CSRF，但无保存浏览器请求或修改结果。\n\n分别记录浏览器能发送的请求、Cookie条件、后端Origin/token检查、状态变化，以及响应能否被攻击域读。简单表单可发送而响应不可读，CORS允许读也未必能修改；preflight被拒和后端拒绝都为反例。用隔离模型核对，不向真实账号发请求。\n\n规范核对：[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)。\n\n来源：[保存帖36](https://x.com/i/status/1504309125932777478)。"
  ],
  [
    "discovery/passive-and-services.md",
    "公司名反向 WHOIS 与版权模板需要独立归属证据",
    "PrettyRecon结果列域名/创建日期/registrar，菜单明示maynotowned；另一图建议copyright/disclaimer/favicon关联域。\n\n离线候选保留匹配类型、provider与时间，再按官方资产说明/可验证控制关系分归属未知与scope允许。共同registrar、品牌文字或favicon可能模板、供应商或冒用，不能由搜索结果继承授权。\n\n来源：[保存帖37](https://x.com/i/status/1504320991584915460)、[保存帖80](https://x.com/i/status/1505162177946206211)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Recon 小中范围流程须先约束 seeds 与账号",
    "四图Before公司/范围/多账号/业务政策→After子域ASN服务目录，frameworkv2把ASN收购、证书、Git/JS、HTTP、端口与扫描连接；small指定域，medium宣称所有subs。\n\n以授权seed为边界保留每次扩展来源和未确认归属，分候选、可达、检查运行及影响。Git/JS手审不宜被自动过滤消除；allports与credentialbrutespray不能从图中任务名称继承许可。流程图无回执，不能证明已经完整扫描。\n\n来源：[保存帖62](https://x.com/i/status/1504676850110713857)、[保存帖47](https://x.com/i/status/1504442094076715009)、[保存帖51](https://x.com/i/status/1504463703135371264)。"
  ],
  [
    "discovery/web-and-api.md",
    "HTTP 方法矩阵要保持对象与业务不变量",
    "正文建议GETPOSTPUTDELETEPATCH和INVENTED，未有结果。\n\n在本地只读/合成状态模型固定对象与身份，核路由是否共用处理器、权限与状态；405/200/意外信息需真实内容对比，unknown方法处理不等绕过。写入、删除和实际生产状态变化不能只为比较而发起。\n\n来源：[保存帖44](https://x.com/i/status/1504421204777611264)。"
  ],
  [
    "targeted-fuzzing.md",
    "Astra 检测类别介绍不证明 API 检查覆盖",
    "正文列SQLi/XSS/CSRF/unlimitedusage/JWT，图片仅仓库卡。\n\n本地API用明确角色、对象、方法、认证生命周期建立测试矩阵，记录规则版本和每项真正consumer/matcher；工具支持声明不等实际运行，不存在自动标签直接确证所有类别的证据。分类或星数不是发现率。\n\n来源：[保存帖52](https://x.com/i/status/1504491500494680068)。"
  ],
  [
    "by-type/waf-bypass.md",
    "Form feed 原字节与推文替代点必须区别",
    "正文明确0x0c且提醒•只是平台不能显示时的替代点；图只有JSFiddle封面。\n\n离线保存字节、编码层和HTMLtokenizer位置，比较空格被剥离、FF保留、被规范化三种结果及最终事件属性。FF在指定解析状态可分隔，不表示任何JS或引用属性都可突破；复制•、控制字符被删或最终文本显示是反例。\n\n规范核对：[HTML 属性解析](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(unquoted)-state)。\n\n来源：[保存帖60](https://x.com/i/status/1504574674021277696)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "SQL 候选管道的 sqli 文件名须一致",
    "正文五步sublist3r→httpx→waybackurls→gf输出sqli，最后sqlmap读sqli.txt；输入文件已不一致，tee-a也混旧结果。\n\n离线合成每步输入/输出类型、实际版本、退出状态与来源；检查gf规则标记不是注入确认。只有URL匹配或数据库枚举命令文本无基线/时间差或实际返回，不执行保存sqlmap命令。\n\n来源：[保存帖61](https://x.com/i/status/1504639239820279808)、[保存帖237](https://x.com/i/status/1508138092343234560)。"
  ],
  [
    "by-type/csrf.md",
    "改密码 token 检查不当必须落到服务端结果",
    "正文称CSRF致ATO，图仅passwordchangeP3Triaged；未保存token检查或改密交换。\n\n隔离测试模型固定受害者身份，比较正常/空/无/错token和跨来源条件，记录后端确实改密与旧新凭据的生命周期。响应200、前端消息或P3标签不等改密，更不自动证明接管。\n\n来源：[保存帖64](https://x.com/i/status/1504778412317159438)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Nmap verbose 发现行不能套用 grepable 格式解释",
    "正文awk按Discoveredopenport取末字段和第四字段，图又描述-oG；这两种格式不能混作同一契约。\n\n离线合成含协议、关闭/过滤、多个IP、不同空白与无命中行，核字段与域IP关联；保留结构输出及错误而非只字符串拼hostport。空文件可能解析失败不等全无开放，重复行不等独立服务。\n\n规范核对：[Nmap 输出格式](https://nmap.org/book/man-output.html)。\n\n来源：[保存帖67](https://x.com/i/status/1504845979371061273)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "visualRecon 固定 foo 目录与多源去重须可复核",
    "图中mkdirfoo/cd、sublist3r输出subs、assetfinder追加、sort-u再probeaquatone；没有运行回执。\n\n本地模型每seed独立临时路径，检查目录进入成功、覆盖/追加语义及输出类型；固定foo失败后仍执行可能污染已有结果，域去重也会丢provider信息。截图生成路径不是网页内容已检查，不执行归档网络命令。\n\n来源：[保存帖69](https://x.com/i/status/1504872762883678208)。"
  ],
  [
    "by-type/waf-bypass.md",
    "svg on onload 图片只证明保存的有限浏览器现象",
    "同源帖对比scriptblocked与svgononload弹domain，另有marqueeonstart/animateonbegin；图缺请求链、规则和版本。\n\n隔离浏览器模型分过滤输入、HTML属性解析、事件触发、CSP和读者身份，固定同请求对象对照；多写一个on属性与不同事件名可能避开特定规则，但不能推出当前Cloudflare通用绕过。无浏览器执行或仅公开页弹框不等认证影响。\n\n来源：[保存帖71](https://x.com/i/status/1504927074477387780)、[保存帖159](https://x.com/i/status/1506574645658787842)、[保存帖164](https://x.com/i/status/1506635313787121665)、[保存帖188](https://x.com/i/status/1507050759170531337)。"
  ],
  [
    "by-type/xss.md",
    "freq 标签及 h1 字符串匹配要分反射和执行",
    "wayback→gf→uro→qsreplace→freq图有Vulnerable/Not标签；另一行把端口/协议/每等号改写后httpx匹配h1字符串。\n\n离线保持原URL、参数结构与每次改写，比较纯文本、编码HTML与真实事件消费。强制https或全等号替换会换目标/破坏参数，uro会合并有意义值。输出标签或h1存在只到反射/markup候选，须实际浏览器consumer与最小影响。\n\n来源：[保存帖72](https://x.com/i/status/1504932805431767046)、[保存帖195](https://x.com/i/status/1507282836394590231)。"
  ],
  [
    "by-type/oauth-oidc.md",
    "正常 signup 与 OAuth signup 需要同一身份状态比较",
    "正文提醒两入口注册不同，图只有WeakRegistration150奖励。\n\n隔离模型对比新旧账号、verifiedemail、provider subject、tenant、邀请/组织加入以及碰撞处理，保持可验证邮箱归属；入口差异只有在服务端赋予错误身份或权限时才构成漏洞。奖励通知和跳转页面无绑定链，不借OAuth名称推接管。\n\n来源：[保存帖74](https://x.com/i/status/1505045199805812738)。"
  ],
  [
    "discovery/passive-and-services.md",
    "Censys 证书 names 查询要保留历史与租户关系",
    "正文给services.tls.certificates.leaf_data.names查询并称更多子域，无保存结果。\n\n离线证书候选保留SAN值、观测时间、provider与实际服务证书对应，比较通配符、过期、共享托管和离线证书；更多名称不是当前解析或公司控制，更不证明所有查询比别的强。\n\n来源：[保存帖75](https://x.com/i/status/1505072128416264194)。"
  ],
  [
    "by-type/lfi-path-traversal.md",
    "图片 filename 返回 passwd 字节与 MIME 标签分开",
    "保存GETimagefilename点目录到passwd及200响应ContentTypeimagejpeg，正文外链只目录穿越标题；另一tpl请求也返回passwd文本。\n\n在自有合成reader固定身份、根目录与正常文件，记录解码/规范化后实际路径、目标字节hash与禁用reader对照。200或imagejpeg不能证明图像解析，文本片段可被fixture/回显伪造；存在保存读取样本不等当前生产范围或可执行代码。Cookie和系统字段不复制使用。\n\n来源：[保存帖76](https://x.com/i/status/1505119425556467718)、[保存帖199](https://x.com/i/status/1507377148222664707)。"
  ],
  [
    "discovery/web-and-api.md",
    "phpMyAdmin setup 空 servers UI 不足以定 critical",
    "图可辨setupoverview、noconfiguredservers和SaveLoadDelete按钮，没有版本、后端操作或DB权限。\n\n隔离模型先界定页面暴露、配置读写、实际持久化及认证身份；只空页面或按钮可见不证明文件可写、可连数据库或命令执行。严格保留作者未解问题，不能点击生产配置保存来补证据。\n\n来源：[保存帖77](https://x.com/i/status/1505124224054267906)。"
  ],
  [
    "by-type/file-upload.md",
    "PHP 短标签绕过上传过滤仍受解释器条件约束",
    "正文把正常php标签阻断、短标签放行称CloudflareRCE绕过，没有保存上传/执行响应。\n\n独立区分WAF是否允许字节、存储路径/后缀、实际PHP解释器和short_open_tag配置；离线比较解析启闭与静态下载。短标签被接收不等可执行，关闭配置/无PHPhandler都是反例；不上传执行图中system调用。\n\n规范核对：[PHP tags](https://www.php.net/basic-syntax.phptags)。\n\n来源：[保存帖81](https://x.com/i/status/1505182628433088517)。"
  ],
  [
    "by-type/authn-session.md",
    "2FA 类别清单不等各入口共享验证边界",
    "列bruteforce/OAuth/race/reset/response manipulation，未有具体流程。\n\n隔离身份模型分别跟踪primaryauth→challenge→verifiedsession及OAuth/reset入口，比较未完成challenge的同一后端操作。改响应、挑战UI消失或重放无权限会话均不能确证；必须确认服务端越过独立认证因子，不进行猜码或账号尝试。\n\n来源：[保存帖84](https://x.com/i/status/1505359578493779968)。"
  ],
  [
    "by-type/idor-access-control.md",
    "删除 API 路径租户段的 200 不等同一对象越权",
    "多帖api数字users403变api双斜杠/反斜杠200，另列json、问号、斜杠、v2、accountdetail和OriginalURL。\n\n固定身份与资源，追前代理/路由规范化与最终tenant/object绑定。删除租户可能返回公开列表、默认租户或catchall；v1字母l混写、版本改变也需核请求字节。状态码须有同对象受限内容或能力差异，不能继承全部列法都有效。\n\n来源：[保存帖86](https://x.com/i/status/1505451015742816258)、[保存帖87](https://x.com/i/status/1505451017831612418)、[保存帖89](https://x.com/i/status/1505546109598707716)、[保存帖238](https://x.com/i/status/1508141987752734721)。"
  ],
  [
    "cloud/cloud-misconfiguration.md",
    "S3 read write delete 标签需要各自对象回执",
    "S3Sec图只是三个标注bucket位置，没展示对象内容、写入或删除回应。\n\n离线policy模型按principal/action/resource分别比较匿名读、受控测试对象写和删，不以list/read继承write/delete。打印标签或bucket公共名字无具体对象证据；不写删生产存储，也不复制图中名称尝试权限。\n\n来源：[保存帖88](https://x.com/i/status/1505509373774372869)、[保存帖91](https://x.com/i/status/1505580378329071617)。"
  ],
  [
    "discovery/passive-and-services.md",
    "JFScan 全端口结果的 403 标题不等业务授权",
    "JFScan1.0.3图有全端口、自定义resolver、10threads、nmapXML，几个80/443openOpenResty403及Cloudflare400；无整体结束状态。\n\n离线保留seed→解析IP→协议port→Host/SNI与服务标题，核grep子串目标是否误带共享基础设施；开放端口不是服务可用身份，403不是后续越权。全端口参数不授权扫描全部共享IP，不执行图中任务。\n\n来源：[保存帖90](https://x.com/i/status/1505554930060476429)。"
  ],
  [
    "by-type/csrf.md",
    "JSON CSRF 的 simple complex 示例还缺语法和凭据条件",
    "simple图设置textplain却未withCredentials；complexapplicationjson设置withCredentials。两图roleadmin字符串/引号不完整，不能视作可直接执行的PoC。\n\n离线先审JS字符串与JSON格式，再按ContentType、凭据、SameSite和预检建立发送矩阵，确认后端解析/Origin/token检查与角色实际变化。simple可发送不等携带身份，complex被preflight拒绝不等role改变，API无token也可能有其他有效防护。\n\n规范核对：[MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)。\n\n来源：[保存帖106](https://x.com/i/status/1505818821818417153)。"
  ],
  [
    "by-type/authn-session.md",
    "O365 valid email 输出须有响应差异和归属",
    "Oh365UserFinder1.0.0列valid/invalid并称发现3个登录账号，未保存验证API交换。\n\n本地合成存在/不存在账号对照原状态、body、时间与provider错误，区分邮箱格式验证、tenant发现和账号存在。标签可能缓存/阈值误判，不能推出凭据或可登录；不探测图中邮箱。\n\n来源：[保存帖108](https://x.com/i/status/1505871774617112578)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Avatar deleteImage 的 JS id 消费者不能确证删除越权",
    "Avatarjs显示deleteAvatar把id放FormData、POSTUser/deleteImage、parseJSON和msg.success判分支；没有后端授权或删除结果。\n\n离线用两测试主体和不同归属对象检查session到serverlookup绑定，比较作者/非作者/不存在对象且追状态，分前端隐藏modal和实际持久化。id可控不是充分证据，successfalse分支不等权限绕过，不请求删除或执行归档JS。\n\n来源：[保存帖110](https://x.com/i/status/1505899815406022657)。"
  ],
  [
    "by-type/authn-session.md",
    "重置十三类清单要转为交付绑定与生命周期实验",
    "图列rate/expiry/email/referer/token response/跨账号token/selfXSS/poisoning等，重复图片排版不同；无具体结果。\n\n隔离模型绑定请求主体、被重置账号、token接收者与消费后session，比较过期/已用/错账号/未授权来源。可读响应token必须归属和可消费，自XSS未跨读者不足接管；修改Referer未进入真实邮件则无poisoning。重用token不天然错误，要核产品定义。\n\n来源：[保存帖111](https://x.com/i/status/1505932315629088772)、[保存帖116](https://x.com/i/status/1505939278198894592)、[保存帖145](https://x.com/i/status/1506311746679500802)。"
  ],
  [
    "targeted-fuzzing.md",
    "vaf fuzz 位置介绍与参数覆盖结果分开",
    "正文只描述Nim跨平台fuzzer可URL/POST自定义wordlist，无运行日志。\n\n离线请求模型标定URL路径、query、编码与body字段，保留正常请求、插入点、状态/长度差异；POST词表支持不等认证/业务路径已测，异常响应须具体consumer证据。工具简介不扩大已检查覆盖。\n\n来源：[保存帖120](https://x.com/i/status/1505982576481214464)。"
  ],
  [
    "discovery/web-and-api.md",
    "cdn proxy 建站副本不能继承生产 CDN WAF 结论",
    "正文声称工具创建禁用CDN/WAF的目标副本，没保存实现或同站证据。\n\n本地副本应绑定静态/后端版本、路由、HostSNI、认证和代理配置，比较同请求到原链与受控副本的差异；去WAF只能研究应用consumer，副本成功不能代表生产可达、漏洞或源站绕过。不能由复制能力推许可或请求未知origin。\n\n来源：[保存帖121](https://x.com/i/status/1506002579154608129)。"
  ],
  [
    "experiment-design.md",
    "VPS 与 wordlist 环境笔记不能预设内存总是瓶颈",
    "保存笔记列Ubuntu2vCPU4GB/60GB、16GB笔记本、128GB桌面及下载旧工具词表；价格和主张仅历史。\n\n自有离线小规模工作负载保留工具/词表hash与版本，观测CPU/RAM/IO/队列及输入规模，分复用结果和新运行。速率限制、CPU或网络都可能瓶颈，硬件规格不保证任务覆盖；不下载执行归档依赖或扩大扫描。\n\n来源：[保存帖123](https://x.com/i/status/1506023216040472581)、[保存帖124](https://x.com/i/status/1506023895517700096)、[保存帖131](https://x.com/i/status/1506145991744909314)。"
  ],
  [
    "discovery/passive-and-services.md",
    "短暂子域覆盖要记录来源时间和遗漏原因",
    "正文批评单脚本/证书库遗漏短暂子域，提多scraping/brute/permutation/reverseSSL。\n\n离线候选按provider和时间窗口保留seed、名称、解析与去重来源，比较互补来源命中，记录不可取/陈旧/wildcard过滤。多来源也可能同缓存，速度与总数量不能证明全历史或实际ownership；任何新域须独立scope。\n\n来源：[保存帖128](https://x.com/i/status/1506122195625422848)。"
  ],
  [
    "by-type/race-conditions.md",
    "Intruder null payload 重发不证明请求并发重叠",
    "正文建议nullpayload发送同请求测race，没有调度、时序或业务结果。\n\n在自有合成状态机比较串行、受控同时到达及幂等key变化，保留前后状态、事务边界和每操作身份，确认超过一次性约束。重复发送可能全串行或返回缓存，200多次也可能只提交一次；不发生产交易或资源消耗。\n\n来源：[保存帖133](https://x.com/i/status/1506165372533174275)。"
  ],
  [
    "by-type/info-secrets.md",
    "Findsecret 正则目录要核分组语义与 secret 目的",
    "图有JSON规则authbasic/bearer/HTTPuserpass/AWSclientid/keys/ARN/secret；部分前缀组合与字符类/组语义容易误配。\n\n离线造合成格式、边界、假阳性和换行样本，按regex引擎版本核匹配跨度与类别。IP/bucket/ARN常是标识不等secret，格式匹配也不证明权限或生效；图规则不直接执行，输出须脱敏且最小证据。\n\n来源：[保存帖136](https://x.com/i/status/1506180538993811460)。"
  ],
  [
    "by-type/info-secrets.md",
    "signup 重定向后 CSV 候选与注册 PII 字节分开",
    "正文signup→signup/→csvfuzz→signup/signup.csv称全部注册PII；图仅P1TriagedDuplicate。\n\n保存重定向解析路径、wordlist与reader身份，在离线样本比较普通csv/错误页和确属受限字段，绑定受影响账号/行数而非全部推断。词表命中、状态标签或重复票不能证明所有用户；不枚举下载生产档案。\n\n来源：[保存帖137](https://x.com/i/status/1506205080583823360)。"
  ],
  [
    "by-type/api-property-pollution.md",
    "重复 company_id 管理员添加须核实际 JSON 解析",
    "图正常company_id自己、构造重复company_id另一值，声称添加admin即可storetakeover；没有HTTP请求、响应或角色结果。\n\n离线模拟网关鉴权与应用JSONparser，比较first/last/reject以及字段去重前后绑定到同tenant。重复member行为不一致是线索，不是必定lastwins；最终员工归属与权限须服务端证据。新增role并不自动店铺接管，不创建真实员工。\n\n规范核对：[RFC8259 对象成员名](https://www.rfc-editor.org/rfc/rfc8259.html#section-4)。\n\n来源：[保存帖140](https://x.com/i/status/1506277015371980800)。"
  ],
  [
    "discovery/web-and-api.md",
    "API mindmap 要把文档对象与实际消费端连接",
    "图含版本v1v2v3、RESTSOAPGraphQL、WADLWSDL/公开文档、认证ID、比较文档、行为映射、objects/actions/端点和BurpPostmanSoapUIfuzz路径；小字保持限度。\n\n离线矩阵按版本×角色×对象×操作关联原请求/响应和schema来源，记录文档未实现、隐藏操作与deprecated路由。GraphQLintrospection/visualization只到结构，REST路径edit不证明写权限；集合导入和可视化不是全覆盖。\n\n来源：[保存帖142](https://x.com/i/status/1506284573491175442)、[保存帖229](https://x.com/i/status/1507985090428936193)。"
  ],
  [
    "by-type/csrf.md",
    "CSRF checklist 的双提交修改要核攻击者 cookie 控制",
    "图列GETPOST、空缺token、同长变字、重用、decode、double submit cookie+param、跨账号token。\n\n隔离模型用服务器绑定session的预期token，逐项比较状态而非回显。改cookie和param只有真实攻击来源能影响对应cookie时才有意义；token可decode或可重用不天然失败，一次性定义与验证范围需核。自动“workedmosttime”没有保存统计证据。\n\n来源：[保存帖143](https://x.com/i/status/1506300802008510465)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "五十 seeds 的 validated 说法要展开验证谓词",
    "日记称hunter.sh50seeds输出dedupvalidatedsubs并启动contentdiscovery，先最隐蔽seed；无实际结果。\n\n保留seed范围、候选来源、DNS/HTTP验证谓词、过期时间和未跑阶段。名称去重不证明资产归属，validated可能仅解析而不是漏洞；opaque种子优先是策略选择，不代表最易发现或覆盖所有。mindmap仍须关联证据。\n\n来源：[保存帖152](https://x.com/i/status/1506514570357063682)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "checkLink localhost 管道 id 返回须有执行因果",
    "图可见checkLink的url编码localhost与管道id，200JSONstatuserror/message有uid0字符串；另一文章截图catIFS与回连passwd行。没有基线和执行主机归属。\n\n离线合成命令消费者比较字面URL、shell拼接与参数化调用，绑定安全固定标记、退出/错误路径与真实产生进程。回显fixture或历史callback不证明当前执行，HTTPfetch与shell是不同sink；缺consumer不得由SSRF自动推RCE，不执行命令或回连。\n\n来源：[保存帖153](https://x.com/i/status/1506522201255657475)、[保存帖175](https://x.com/i/status/1506892646442168324)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "curl grep URL 提取不能代替 HTML 或 JS 解析",
    "图输出有w3namespace、external库、截断CSS参数和目标URL，正文regex仅限定字符类。\n\n离线页面比较relative链接、实体、引号、fragment、query及脚本生成路径，保留原文本偏移、消费者类型和targetorigin过滤。字符集漏符号会截断URL、代码字符串不等请求、namespace不等endpoint；sort-u会丢出现位置。声明提取近似候选而非完整爬取。\n\n来源：[保存帖162](https://x.com/i/status/1506628887786430470)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Actuator env 双斜杠 200 还需环境字段证据",
    "正文单斜杠403/双斜杠200，图仅像素化env页面；不能读出密钥或用户。\n\n本地网关模型对照前置ACL与后端路由规范化，固定身份并比较同env对象是否受限；公开/脱敏/envdisabled或catchall是反例。Spring端点名称、JSON长度及状态码不证明secret或当前版本RCE，不发生产请求。\n\n来源：[保存帖163](https://x.com/i/status/1506634826874757124)。"
  ],
  [
    "by-type/info-secrets.md",
    "phpPgAdmin 与 bash history 明文要分读暴露和登录能力",
    "图phpPgAdmin显示postgres身份/测试DB，bashhistory可见psql连接用户名密码；缺未认证基线及因果登录交换。\n\n离线历史样本核公开reader、字段目的、账号/服务绑定与脱敏最小证据，区分浏览器已有session、过期密码与真正可用认证。psql命令存在不等远程DB可达，更不授权登录或下载历史。\n\n来源：[保存帖165](https://x.com/i/status/1506644098748502021)。"
  ],
  [
    "source-audit.md",
    "RFC diff errata 是实现假设来源而非漏洞证明",
    "正文建议SecurityConsiderations、旧RFC、Rfcdiff和Errata，无具体规范差分。\n\n明确实现使用的规范版本与被替代关系，核errata状态及修订的安全假设，再在自有parser模型以合成输入比较实际行为。旧规范仍被产品契约选择不必有漏洞，diff文本不是实施差异；标准建议和真实数据flow分开，不追未保存外链全文。\n\n来源：[保存帖166](https://x.com/i/status/1506646952196386818)。"
  ],
  [
    "reporting.md",
    "证据补充能改变影响判断但不能凭数据量升严重度",
    "正文称足够数据/客户影响低可升高，另图有validhighesttier1000并请求invoice；三P2Unresolved各2500合7500。\n\n围绕明确角色、对象、权限变化、复现和影响范围补最小证据，区分severity、accepted、dup、fix和待付。金额/字数/三个票不是三独立根因，invoice请求也不是已到账；不发票或联络第三方，已保存支付信息不复用。\n\n来源：[保存帖167](https://x.com/i/status/1506665803412049920)、[保存帖208](https://x.com/i/status/1507615124713984000)、[保存帖216](https://x.com/i/status/1507707049513140224)。"
  ],
  [
    "by-type/mobile-android.md",
    "M1 Android Studio ARM 下载项不等测试环境就绪",
    "保存图2021.1.1.22包列表含MacARM和hash，正文说M1配置困难；无安装或代理证据。\n\n自有离线环境记录host架构、SDK/AVD或设备构建、工具hash和依赖版本，按adb连通、可解密代理、pinning/root权限分别验条件。ARM包名称不保证全部工具兼容，更不证明捕获真实流量；不下载旧包或连接设备。\n\n来源：[保存帖168](https://x.com/i/status/1506678213929488384)。"
  ],
  [
    "by-type/info-secrets.md",
    "staging 域 env 泄露到 production 的链须独立归属",
    "正文水平recon→stg域→GitHubenv→developer凭据→production，无保存搜索/secret/登录交换。\n\n离线跟踪候选域归属、代码仓库控制关系、secret目的、生产权限和生命周期，每步保留证据而非由品牌推关联；demo值/旧凭据/第三方托管或不同tenant是反例。发现凭据也不授权使用，不登录生产或查询仓库外链全文。\n\n来源：[保存帖169](https://x.com/i/status/1506693234193485829)、[保存帖109](https://x.com/i/status/1505893022445232130)。"
  ],
  [
    "by-type/open-redirect.md",
    "多斜杠 next 要核解析后的实际导航 origin",
    "两个正文给next多斜杠evil字符串，没有实际Location或导航。\n\n离线URL模型保留原输入、服务器Location、相对解析基址、浏览器归一化后schemehostport，比较单斜杠相对路径、协议相对和多斜杠。字符串含evil不一定外跳，拒绝/变成本站路径均反例；不导航未知目标，不称任何URLconsumer都可绕过。\n\n来源：[保存帖173](https://x.com/i/status/1506833579644694534)、[保存帖193](https://x.com/i/status/1507235426490527744)。"
  ],
  [
    "by-type/idor-access-control.md",
    "manage admin 参数改变状态须核服务器赋权",
    "manage.php403→admin1参数200提示，无保存响应。\n\n自有模型固定角色和操作，比较参数只改变展示、路由还是后端授权，读取服务端实际权限与业务状态。客户端admin位可控而未被信任并无提升；公开帮助页或cachehit200不等管理能力。\n\n来源：[保存帖174](https://x.com/i/status/1506838160126496771)。"
  ],
  [
    "by-type/business-logic.md",
    "currency_code 改币种必须同时核价格与结算单位",
    "正文USD300改PKR300称被扣更低价值，无保存订单/支付回执。\n\n隔离账本模型把商品价格、currency、minorunits、服务器换算、支付provideramount和履约记录相连，对照预期币种价格及重试/缓存。展示币种变了但服务端重算、结算仍原金额或未成交是反例；历史汇率只故事背景，不作为当前价格，不创建真实支付。\n\n来源：[保存帖181](https://x.com/i/status/1506951423975690246)。"
  ],
  [
    "discovery/client-and-cloud.md",
    "AD Explorer snapshot 对话框不证明完整图已导入",
    "图snapshotpath空、throttle100%；正文描述解析给BloodHound和全对象NDJSON。\n\n离线合成快照绑定文件hash、schema、timestamp、objects/edges与缺失对象，核解析错误及图查询与主体权限；只dialog或输出格式介绍不能代表实际导出、完整或最新关系，更不证明任何可行攻击路径。不要连接AD、生成真实全库或导入敏感快照。\n\n来源：[保存帖182](https://x.com/i/status/1506958943146422272)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Osmedeus cloud chunk 调度要有每片与合并回执",
    "图4.0.3、63600行、chunk3、三instance、其中SSHrefused后日志继续running与UIreport；没有全部完成或合并。\n\n离线调度模型绑定seedfilehash、分片范围、实例/operationID、重试与每片最终状态，比较失败后未重跑和重复运行。linecount不是uniquehosts，初始化账单token/SSH成功不等扫描完成，图中余额/机器不授权使用云或删除实例。\n\n来源：[保存帖184](https://x.com/i/status/1507005684252299270)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Amass 到 Nmap 仍需域输入和解析服务边界",
    "正文一句quickscan所有发现子域，无图或运行结果。\n\n离线验证输出只域还是含日志，保留域IPHostSNI、DNS变化、端口协议与范围过滤。解析共享IP不把全部端口资产归目标，quick无版本/时间预算不等覆盖；不运行网络扫描。\n\n来源：[保存帖186](https://x.com/i/status/1507010347420438528)。"
  ],
  [
    "experiment-design.md",
    "应用 DoS 类别要对应成本曲线和可恢复边界",
    "图列长password/comment/uploadname、xmlrpcbrute、imagesize、cookiebomb/pixelflood、noratelimit/loadscript/cachepoisoning。\n\n在自有隔离服务以低上限合成输入测成本、队列、内存与响应时间及恢复，比较正常/限额/拒绝路径；长串、无rate或cookie增加不直接证明用户可用性受损，更不把标签当DoS确认。不能在生产施压。\n\n来源：[保存帖191](https://x.com/i/status/1507095574021287936)。"
  ],
  [
    "by-type/ssrf.md",
    "IPv6 unspecified 与 loopback 不应混成同一绕过",
    "两个正文列http[::]:80及未加括号0000::1:80，没有保存fetch结果。\n\nRFC3986规定URI IPv6字面host需括号，RFC4291将全零和::1分别定义为unspecified与loopback。离线核每层URLparser、规范化、allowlist和实际连接目的；解析拒绝/非URLIPv6/目的不可达或不进入fetcher均反例。[::]不能天然等同环回，不进行内部连接。\n\n规范核对：[RFC3986 host](https://www.rfc-editor.org/rfc/rfc3986.html#section-3.2.2)、[RFC4291 地址](https://www.rfc-editor.org/rfc/rfc4291.html#section-2.5.2)。\n\n来源：[保存帖194](https://x.com/i/status/1507250837206499329)、[保存帖205](https://x.com/i/status/1507566133955637249)。"
  ],
  [
    "discovery/passive-and-services.md",
    "DNS hierarchy 图需区别委派权与缓存解析",
    "图root→TLD→zone举例，正文无查询。图是简化模型，root并非含一切主机地址。\n\n离线区分authoritativezone/NSdelegation与recursivecache、负缓存/TTL，保留最终答复及来源时间；某NS回答或resolver缓存不能独立证明域控制，更不能证明同IP全归目标。层级图不等真实配置证据。\n\n来源：[保存帖196](https://x.com/i/status/1507285470551867394)。"
  ],
  [
    "by-type/info-secrets.md",
    "Wayback 敏感 URL 历史版本与现有泄漏分开",
    "两个正文把404config.js交waybackurls-getversions称可返回旧文件；图仅LowInfoDisclosure标签。\n\n离线候选保留原URL、存档时间/内容hash和当前404，同域/路径版本差异与数据目的分开。列出历史URL不保证有内容或有效secret，未验证的选项语法需实际版本契约，不能把存档旧值等同当前泄漏。\n\n来源：[保存帖200](https://x.com/i/status/1507391830627065856)、[保存帖206](https://x.com/i/status/1507566600668409860)。"
  ],
  [
    "by-type/ssrf.md",
    "历史 url 参数筛选只定位潜在 fetcher",
    "assetfinder→waybackurls→grepurl=被称五分钟SSRF，未有实现或交换。\n\n离线保持域输入格式、archiveprovider、URL与参数语义，核url消费者是浏览器跳转、文本保存还是服务器抓取；旧endpoint、空值或无网络consumer为反例。候选数量不等SSRF、更不直接敏感影响，不发回连。\n\n来源：[保存帖207](https://x.com/i/status/1507570538104836099)。"
  ],
  [
    "by-type/authn-session.md",
    "隐藏 Signup 的员工角色须独立验证邮箱与功能",
    "保存图描述internalportal无signup链接，手改Signup用公司格式邮箱未验mail/admin可employee登入，列共享存储团队PII但admin失败。\n\n隔离注册模型比较已验证员工/外部同后缀/未验证账号、邀请与实际服务端角色；前端隐藏不是关闭接口。域后缀字符串不能证明邮箱所有权，employee成功也不等admin，结果须原请求/角色和受限功能对照，不创建真实员工。\n\n来源：[保存帖210](https://x.com/i/status/1507676203423256576)。"
  ],
  [
    "by-type/authn-session.md",
    "register 页猜密主张要验证是否共享认证计数",
    "图称login限速可去register猜密码，通常没保护；无实际请求/身份。\n\n本地账号模型分新注册、已存在冲突、密码正确/错误及login计数键，确认注册路径真的验证旧凭据并产生该用户session；注册只检测存在或总拒绝时无法猜旧密码。入口速率不一致需真实业务状态，不批量猜账号或凭据。\n\n来源：[保存帖213](https://x.com/i/status/1507698895211667462)。"
  ],
  [
    "by-type/cmd-injection-rce.md",
    "Spring routing expression 错误栈和计算器不能确证 RCE",
    "图本机POSTlocalhost带spring.cloud.function.routing-expression，返回500SpelEvaluationException，背景源码和已开calculator；正文是SPEL0day标题。\n\n离线辨客户端可控expression→版本具体路由求值→受限方法/执行consumer，比较正常与固定安全标记、进程产生时间和权限。500可仅语法/访问限制，计算器另开窗口不证明因果；没有版本/完整表达式不借CVE名填实现，不执行payload。\n\n来源：[保存帖215](https://x.com/i/status/1507705465471262723)。"
  ],
  [
    "by-type/idor-access-control.md",
    "文件尾分号斜杠要核 ACL 与 reader 路径一致",
    "正文三项奖励并称semicolon/slash内容发现常有效，没有真实例子。\n\n隔离路径模型记录代理、框架路由、filesystem或静态reader最终path，固定身份与文件，比较标准/尾字符/拒绝。路径改变可能另一公开资源或错误页，parser差异需受限对象能力；三P2各金额不证明机制成立，不请求生产端点。\n\n来源：[保存帖216](https://x.com/i/status/1507707049513140224)、[保存帖101](https://x.com/i/status/1505785860754935808)。"
  ],
  [
    "by-type/xss.md",
    "引用 value 中实体解码不直接重开 HTML 标签",
    "正文inputsearch的value含quot/lt/imggt，询问绕过；没有后续DOM消费者或执行。\n\n按HTML引用属性状态区分源引号结束与字符引用得到的值，实体解析出来的引号/尖括号不会自动当源代码重新分词。离线比较一次属性值读取、二次innerHTML和JS拼接，只有后续不安全consumer才新增边界；显示文本或无二次解析是反例。\n\n规范核对：[HTML double quoted attribute](https://html.spec.whatwg.org/multipage/parsing.html#attribute-value-(double-quoted)-state)。\n\n来源：[保存帖219](https://x.com/i/status/1507754748518182914)。"
  ],
  [
    "reporting.md",
    "composer lock 版本公开与可利用泄漏需分开",
    "正文问为什么informative，图只是标题，没保存lockfile实际字段。\n\n版本通常只是组件候选，报告需绑定部署版本、可达功能、角色/配置和具体影响；可能仅开发依赖或未部署。若文件真有私仓URL/token等另按secret目的审，不能仅“版本andstuff”定高危或填当前CVE。\n\n来源：[保存帖224](https://x.com/i/status/1507808720247562247)。"
  ],
  [
    "by-type/request-smuggling.md",
    "Te Cl 错 chunk 六十秒延迟只能作为 desync 候选",
    "RequestSmuggler图打印possibleTeCl、wrongchunk60174ms对usual65ms，显示ContentLength/TransferEncoding转义文本；无原始连接复用/队列差异。\n\n离线双解析器模型记录准确字节与边界、连接生命周期、下一请求关联，比较正常长度、拒绝和超时。单次六十秒可超时/限速/忙服务，scanner标签不确证前后端分歧，不发生产队列污染请求。\n\n来源：[保存帖225](https://x.com/i/status/1507828333677064206)、[保存帖228](https://x.com/i/status/1507975372717314050)。"
  ],
  [
    "by-type/jwt.md",
    "弱 JWT hash 猜测与服务端签名政策分开",
    "正文描述HashCat找hash后重新设计token即可authenticated，无token算法/验证响应。\n\n隔离HMAC模型固定允许alg/key/issuer/audience/expiry，使用自造弱测试key对照签名及真实授权声明。摘要不是密码hash，强key或非对称算法不按同猜法；本地算对签名未必通过claims或赋权。不破解保存凭据、使用真token或尝试生产身份。\n\n来源：[保存帖227](https://x.com/i/status/1507958444854509568)。"
  ],
  [
    "by-type/ssrf.md",
    "Collaborator ping 与内部扫描成功都需独立影响证据",
    "正文回连后建议内网port/assets/file/LFI，另一帖称192168范围有效而localhost/rebind不行；图只P2Triaged。\n\n离线fetcher模型绑定唯一标记、产生进程、目的及可读结果，比较DNSonly/代理预览/实际HTTP取回与受限文件reader。网络差异不证明内部所有端口可扫，文件fetch也不自动LFI执行；不得扩大生产内网探测或为证据发未知回连。\n\n来源：[保存帖233](https://x.com/i/status/1508076071270371333)、[保存帖240](https://x.com/i/status/1508180310932004874)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Findomain ports NULL 和截图文件名不是内容检查",
    "图列域IPURL端口或NULL及jpeg目录，正文仅集成能力和Discord推广。\n\n离线记录每阶段成功、错误/无结果含义、服务协议和实际截图hash；NULL可能未跑/失败/无端口不能统一closed，jpeg存在不等页面可达或有效截图。多域共享IP/虚拟主机需单独HostSNI，不执行图命令。\n\n来源：[保存帖236](https://x.com/i/status/1508116636288520194)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "dnsgen anew 和 tee append 取决于记录身份定义",
    "正文一律建议anew替tee-a，没有输入/版本/结果。\n\n离线按hostname、解析时间、provider与候选/确认状态定义去重键，比较重复写入与新增集合；anew以行相等去重不能替业务等价，tee保留重复有时用于来源。盲去重会失掉DNS变化或provider证据，不能由工具选择推覆盖提升。\n\n来源：[保存帖239](https://x.com/i/status/1508157367413846016)。"
  ],
  [
    "discovery/records-and-incremental.md",
    "Ostorlab 多 agent install scan 命令未到运行结果",
    "图只多agentOpenVAS/Nmap/Tsunami/Nuclei和install/scan一个IP行，无输出；正文称可扩展分布式平台。\n\n离线编排模型绑定输入范围、组件版本、job与每agent状态、相同事件去重和原证据。安装成功、任务提交或全工具列名不等执行完，更不证明漏洞；不得因示例公共IP启动扫描/安装。\n\n来源：[保存帖242](https://x.com/i/status/1508190742467993613)、[保存帖243](https://x.com/i/status/1508284414060797956)。"
  ],
  [
    "by-type/info-secrets.md",
    "Rivals follow 422 中用户字段与三百五十万泄漏分开",
    "Yahoo故事称350万，图实际followPOST422notallowed、body仍嵌user/phone/provider/认证metadata等多字段，部分请求身份遮蔽。\n\n隔离对象模型保持同身份和userID，比较自己/其他受限用户与拒绝响应字段，确认错误分支仍序列化哪些不该公开信息。一个响应不证明350万/全部用户或跨权限；已有自己的session与公开字段是反例，不复制/枚举PII或cookie。\n\n来源：[保存帖247](https://x.com/i/status/1508384789253918724)。"
  ],
  [
    "by-type/business-logic.md",
    "unsubscribe 历史链接要核接收身份与订阅状态",
    "正文邮件子域→Wayback称其他付费用户取消P3，图只TripAdvisorfooter。\n\n自有订阅模型比较账号token/匿名管理链接、期限与服务端取消记录，核操作是否绑定正确收件者。邮件底栏、存档URL或paid字样不证明别人的订阅被取消；无状态变化/有效单人token为反例，不点击真实取消链接。\n\n来源：[保存帖250](https://x.com/i/status/1508430921099272194)。"
  ],
  [
    "experiment-design.md",
    "本地工具 help 文件与零检测标签须保留独立证据",
    "PSRansom图help描述加解密/C2key/plaintext，Shellcode图本机HelloWorldMessageBox，LsassDump图Administrator、dmpfile/Defenderenabled与0of26，Nimcrypt图下载行/旧定义。都是不同有限现象。\n\n只在离线合成产物分析中绑定文件hash、原身份、版本、扫描器对象及时间、前后内容和复现范围；help不等执行、dmp存在不等可读认证secret，0of26不保证无害或免杀，MessageBox不证明远程入口。没有相同hash和真实检测对照不合并因果；不下载运行、提取凭据、加密文件或向C2发数据。\n\n来源：[保存帖97](https://x.com/i/status/1505645320587390982)、[保存帖160](https://x.com/i/status/1506595320330866689)、[保存帖222](https://x.com/i/status/1507784264242323464)、[保存帖232](https://x.com/i/status/1508070037613129732)。"
  ],
  [
    "by-type/idor-access-control.md",
    "Microsoft seller users JSON 的角色字段不证明跨租户读权限",
    "保存图partner站点GET seller路径users，响应含sellerId/email/roles/roleAssignments和部分principalId；大量Cookie遮蔽。正文称全部ISV用户，却没保存改变前后ID或自身tenant基线。\n\n隔离API模型把请求者session、seller对象归属和字段可见规则绑定，对照同主体自有/受限seller及不存在对象。roleDefinitionId等常量只说明返回数据，不证明赋角色或管理员登录；自己的数据、公开用户表或fixture均反例。保留可读字段类别及遮蔽限度，不复制PII/凭据或枚举用户。\n\n来源：[保存帖](https://x.com/i/status/1505811821197811713)。"
  ],
  [
    "by-type/ssrf.md",
    "apiUrl 空响应与 DNS HTTP 回连必须追唯一产生者",
    "保存图apiUrl含Collaborator地址、服务200但ContentLength0，旁列DNS/HTTP并显示AAA查询；未有内部内容。它独立于同帖tpl读passwd，不能把两项自动拼成任意文件或RCE链。\n\n在离线fetcher模型保留唯一测试nonce、准确字节、入站operation、触发进程、解析与HTTP取回各阶段，比较未触发/预览/缓存及禁fetch情况。DNS可能独立lookup，HTTP也可能经代理或扫描器产生；空响应不证明抓取结果可读，更无内网影响或规模。图中callback不得请求或复用。\n\n来源：[保存帖](https://x.com/i/status/1507377148222664707)。"
  ]
]
ids={pid for row in json.loads((W/"batch-0125.json").read_text()) for pid in row["post_ids"]}
urls=[pid for _,_,body in facets for pid in re.findall(r"https://x\.com/i/status/(\d+)",body)]
assert len(urls)==120 and all(pid in ids for pid in urls)
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

