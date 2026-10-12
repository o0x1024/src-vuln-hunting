0|g5 包内URL grep建议；字符类只抽样、缺完整scheme和编码/转义，原文件位置和解析后归属需保留。
1|g7 BlackHeart双终端仅nc监听4545空白，没有连接/权限/绕过效果。
2|g11 PowerShell徽标，无独立技术细节。
3|g11 事件403状态停止及800管线/EncodedCommand/ExecutionPolicy Bypass；启动参数与日志观察，不证明无日志或远程执行漏洞。
4|g13 API工具/词表名称清单，无请求响应或漏洞链。
5|g17 GSHELL帮助，IP/端口/语言、reverse和bind方向、base64/32/16/url编码；生成器依赖既有执行条件，不是RCE证明。
6|g18 Web IDOR修复后检查iOS/Android入口同对象权限，建议非结果。
7|g19 CantHide地图2位置标记，仅展示个人位置界面，没有归属/准确性/隐私泄漏证明。
8|g20 Shelly生成器展示bash回连模板和URL编码，已有执行/出站前提，无目标漏洞结果。
9|g23 Apache Tomcat scanner logo，无细节。
10|g26 上传黑/白名单变体：多扩展大小写、双后缀、NUL/空格CRLF/点/斜杠/.html；均依赖真实解析链，不保证执行。
11|g26 文件名XSS、SVG脚本/重定向例；须证用户界面编码、实际SVG消费方式源/CSP，独立域直接导航不能等同业务XSS或服务端重定向。
12|g26 上传后消费者清单：文件名路径/SQL/命令、URL取图SSRF、ImageTragick模板、SVG外部实体；路径例本身无读取证明，用户浏览器取图≠服务端SSRF，先定位解析器与版本，短延迟对照不采用10秒或回连。
13|g28 accountsboard userid替换两次200，必须核对comment对象归属、内容及会话，状态码不足IDOR。
14|g29 WordPress20路径候选含重复signup及若干并非标准路由；只字典不代表暴露或秘密。
15|g29 同一WordPress图跨另一post，已实际阅读，同一facet绑定两来源。
16|g31 dig短输出grepIPv4 head1丢多A/AAAA/CNAME，逐域关联/全部地址/TTL/失败时间保留，正则不是IP有效性证明。
17|g32 子域正则和maps key赋值正则混列，贪婪匹配/合法字符/跨行局限；解析器验证候选，key非漏洞。
18|g36 GitHub contributors->repo dork流水线含错误http脚本路径/协议过滤不一致；SDK结构化repo identity分页token保护限速，不照抄执行。
19|g40 PHP username拼接SQL，取首行hash严格===md5(password)；SQL结构与密码比对独立，图不足成功，参数绑定/自有账户证据。
20|g41 VAmPI logo无细节。
21|g42 安全主题插画无技术信息。
22|g43 Apache编译信息默认error_log/根目录/模块配置，路径不是对外可读证明，受保护日志敏感内容需最小样本。
23|g44 TCP后门本地主动启动Handler/Backdoor后私网回连，已有代码执行条件，无初始漏洞。
24|g44 后门help与sysinfo/ps已有会话，无新漏洞。
25|g44 后门截图/上传下载/cwd操作结果，依赖已有后门执行，不蒸馏数据窃取操作。
26|g46 tlsx GitHub介绍TLS数据收集，功能卡无测试。
27|g47 DFShell fifo创建后www-data whoami，只已建立会话，不证明入口或提权。
28|g51 NetHunt标志，无技术细节。
29|g52 Nokia Hall of Fame人员致谢/prime规则，荣誉无漏洞过程。
30|g54 Vulnerable-AD部署靶场宣传，无配置细节。
31|g56 client_secret/connectionstring/db_password/dotfiles/encryption_key/firebase等搜索关键词，仅候选名不是有效泄露。
32|g59 绿字终端趣味引言，无机制。
33|g60 newsletter广告，周一更新主题，无独立技术。
34|g61 CantHide历史搜索界面，无真实越权或归属。
35|g61 同用户名跨社交站候选链接，同名不证明同人，非技术漏洞。
36|g63 100美元奖励邮件没有DNS或接管机制。
37|g64 cPanel登录画面；入口发现不等于弱口令/越权，body非标端口线索可合并。
38|g65 repo_hunter按redteam主题克隆列表，来源下载不证明审计覆盖；不运行脚本。
39|g68 BeatRev Stage0/1磁盘和Stage2内存分阶段解密/反射加载流程，已有恶意代码执行，非最初漏洞。
40|g71 TheSprayer需域/DC/可枚举策略的账户，用户密码列表/剩余次数/连续/Force选项；策略信息不足保证不锁定，禁强制轮巡，授权自有账户预算。
41|g72 Shodan-Dork ssl/org生成产品/默认密码/面板/CVE候选菜单，没有漏洞证据和归属确认。
42|g73 Netlas查询字段tag/geo/ISP/CVE/domain/port/protocol证书，索引提示不是当前实测或scope。
43|g74 SetOutlookSignatures logo，无技术细节。
44|g79 SMB已认证SYSVOL递归listing含AccessDenied；不同路径权限单独，不能将失败算空结果/覆盖，截图凭据不抄。
45|g79 管理员会话dump8files/15dirs示例，无未授权读证明，只有必要最小授权文件样本。
46|g84 Solidity withdraw检查余额后外部call再扣账，存在重入窗口候选；编译版本/回调gas/全局guard/失败回滚/实际余额不变量须隔离测试，单图不证实金额盗取。
47|g85 Cambridge致谢信exposed file permissions无可复現细节。
48|g88 Pyramid logo无机制。
49|g89 Gorilla字典生成/变异功能卡，无算法或漏洞。
50|g91 CERT-EU HOF姓名荣誉无机制。
51|g92 BOFHound logo无过程。
52|g94 已注册邮箱/用户名重复注册409返回ref UUID，账户枚举/标识泄露候选与IDOR分开，双自有账户验证ref确为对象键与后续拒绝/允许读取。
53|g97 Connect logo无机制。
54|g100 SubEvil help HTTP/HTTPS/status/title/useragent，过滤结果保留scheme/redirect/auth/body证据，非漏洞。
55|g101 ADSearch带已有凭据LDAPS查询SPN，目录服务可读对象不是未授权。
56|g101 LDAP objectCategory/person&class/user限定属性cn/DN/groupID，查询身份/范围/分页/有效权限保留，不等于提权。
57|g105 JSON200 output.code与cellphone OTP泄露候选，不能抄实际code，验证响应接收者/challenge/expiry/finalownsession授权，200不能证ATO。
58|g106 XXE图实体/文件路径/展开概念，无OOB链或结果，外链缺失豁免。
59|g108 Awesome Web Security目录漏洞类别，书单无测试机制。
60|g109 WhatsMyName logo无查询机制。
61|g111 GitHub dork关键词和文件过滤UI候选，无实际秘密、命中有效性、repo归属。
62|g112 noPac输出已有域账户创建计算机/改名/TGT/S4U2Self/清理失败；不复制凭据和修改步骤，票据得到≠任意服务权限/清理成功，历史版本先验证。
63|g117 Uosint忍者插画无技术。
64|g117 公开多社交档案与NotFound输出，只同名线索非同一人证明/目标范围。
65|g118 Cloudflare blocked页面，仅否定基线，不能与正文SVG判断成功。
66|g118 确认对话框域名和内容遮挡，显示JS提示但缺响应/注入上下文，不能普遍WAF bypass。
67|g118 cloudflare.com测试字符串阻挡画面，候选匹配。
68|g118 加Only变体正常首页没有弹窗，可证明阻挡差异截图但不证明脚本执行。
69|g120 ASCII banner无机制。
70|g124 DragonMS菜单含metasploit/network/telnet brute，只有选择菜单不采用DDoS或口令攻击。
71|g126 WebOSINT menu Whois/IP/reverseIP/DNS/CT/reputation/subdomain/history，各源时间/共享IP/域归属必须区分。
72|g130 Tracer只正在查询162sites两个用户名，无完成命中验证。
73|g131 浏览器alert被遮挡，AngularorderBy正文为客户端表达式候选；弹窗不证明服务端模板执行。
74|g132 Microsoft两笔3000美元P2未解决奖励无漏洞机制。
75|g132 奖励邮件明确奖励不代表修复或披露许可，没有技术过程。
76|g133 Coercer banner含认证材料，不复制，不证明relay/提权。
77|g135 DNSX logo无新技术。
78|g140 Appwrite感谢/swag码，确认邮件无机制。
79|g142 httpx title/length/status多站200301404，筛选错误页/跳转保留链及内容，不是权限结果。
80|g143 fsociety工具菜单无执行过程。
81|g148 Infoooze logo无技术。
82|g148 Infoooze菜单混个人OSINT与域/DNS/headers/URL扩展/端口/EXIF；聚合≠归属，短链逐跳scope，EXIF为源元数据。
83|g148 Infoooze CLI help重述功能，无查询完成证据。
84|g148 WHOIS历史记录/联系信息输出，注册信息时间与现有owner/policy分开，不复制个人资料。
85|g149 500美元openredirect奖励无跳转链。
86|g150 GET reach编码路径403对照，仅拒绝基线无成功请求。
87|g151 subfinder->gau blacklist->gf sqli->sqlmap risk3 batch整批，候选不授权自动高风险测试；筛选无法保证请求/会话完整，先单请求低影响对照预算。
88|g152 Pcap geo工具去私网后分析IP/exported，无定位准确性/人归属。
89|g154 ATO P2 unresolved摘要，无JWT签名/重置执行证据。
90|g157 CantHide location/social/Photoshop宣称广告，没有模型准确性或资产漏洞。
91|g158 Darc队列hostname/requests/selenium，缓存check->crawl/parse/save/submit数据库/robots/sitemap/hosts，API回写下一轮；每阶段身份/页码/dedup/contenthash/scope不能只crawler完成。
92|g159 Linux文件命令表含read/write/delete/link，不自动运行，命令速查无漏洞。
93|g163 黑客插画无机制。
94|g165 Ngoto工具分类菜单枚举/hash/shell/WiFi等，无执行证据。
95|g166 女王去世新闻截图，非安全技术内容。
96|g167 chaos->dnsprobe->httprobe->nuclei takeover模板仅Loaded输出，没有命中或可接管证明，DNS/provider/account三个条件。
97|g168 Curl logo无OSINT细节。
98|g169 httpfy -f urls -Sc命令无结果，协议存活不证明资产完整。
99|g176 Cobra sudo安装及22工具菜单；自动安装/执行没覆盖证明或信任，当前仅功能界面。
100|g180 Hawk banner配置文件路径无机制。
101|g180 Hawk子域输出未见来源/DNS时间/完成状态，发现列表非活性或授权范围，结合其它数据源交叉证据。
102|g180 Hawk vulscan port NTP/SSH协议/算法/主机key，指纹候选版本无CVE确认/资产归属。
103|g183 wappalyzergo检测库介绍，无漏洞证据。
104|g184 iOS测试视频封面，无指南正文可见，外链豁免。
105|g186 Gohide本机client/server隧道与HTTP/Wireshark/uidroot，root来自预置执行上下文，画面不能验证AESGCM安全或远端漏洞。
106|g187 Subfinder各第三方来源逐域输出，保留源/时间/分页/解析证据，不自动纳入所有子域授权。
107|g189 VMass自动扫描/上传shell统计及随机大网段工具界面，不作为批准范围/漏洞证据，不复制随机扫描或上传流程。
108|g189 VMass全菜单包括env提取/SMTP/Twilio测试/Telegram转发；属于有副作用或敏感数据操作，不纳入默认发现，统计不能替代请求级验证。
109|g190 PostgreSQL SQL训练本地登录页面无攻击证据。
110|g190 本地os-shell终端文件内容与训练页，缺输入/DBrole/版本/链，不能把Postgres SQLi直接等同RCE。
111|g192 通用script alert XSS插画无独立过程。
112|g193 .zshrc定义sudo函数委派另一路径程序；已有本地写权限/会话执行前提，凭据拦截不是无需权限提权，不运行或复制盗取实现。
113|g197 Android antiFrida仅默认27042端口检查可换port的建议；已具设备debug前提，与服务器授权/密码不关联，bind只隔离loopback。
114|g199 Redis带密码INFO输出遮挡，只已有凭据访问；GitHub泄露正文候选须repo归属/凭据有效权限，不能抄图或验证真实秘密。
115|g201 EvilStorm fakeAP功能海报，无漏洞机制/授权无线实验。
116|g202 GraphCrawler schema mutation读取错误、12queries/0sensitive、_service授权与3CoreVideo路径；schema路径存在非字段权限绕过，逐角色同自有对象query固定，工具Criticality非严重度。
117|g205 like-dbg ARM64内核源码/反汇编/线程SIGINT/trace，已有debug环境非漏洞；源码符号版本匹配。
118|g208 DuckySploit Roblox脚本执行UI notattached，无漏洞过程。
119|g209 图Zimbra已有admin凭据成功登录并上传JSP回显，但正文CVE-2022-36804与Zimbra链接冲突，不给编号定性，缺上传请求/版本/权限边界；不复制凭据/session或webshell。
120|g215 file://本地游戏HOLD ENTER页，缺Chrome读取env或漏洞流程。
121|g217 gh/github/npm/oauth/ldap/mail/privatekey/preprod等关键词清单，候选需repo/commit/owner/权限，不使用真实密钥。
122|g218 NimRunPE手动本地启动映射section/IAT弹calc，初始本地执行已具备，不是远端RCE/提权。
123|g220 WESNG help systeminfo/CVEcsv更新/已知exploit/隐藏filter，建议候选需补丁替代/架构/权限/有效版本，不执行。
124|g221 Ohm Android RAT logo功能卡，无安装或远端漏洞。
125|g222 请求路径重复斜杠/..与返回passwd示例，URL部分遮挡/响应状态缺，未知Nginx alias和上游链不能所有Nginx通用；自有canary证明实际读边界。
126|g223 ATO四类检查清单：重置多收件人/bcc/重复email参数或响应token；socialsignon手填email；更改password/email；重复注册或phone后链接未验证email，独立server绑定/验证最终自有账户不变量，非保证成功。
127|g224 JetBrains SSRF命令截图仅启动参数本机URL/email/urlsfile，没有OOB或响应。
128|g227 X-requested-with WAITFOR delay 5秒图404耗时约19.698秒，单时间不证SQLi，正文毫秒叙述不符；短时对照预算及503停止。
129|g230 Android hardening封面插图无具体配置。
130|g231 BruteX功能卡自动各服务口令攻击，无实际证据，不自动采用。
131|g233 浏览器8085/etc/passwd显示文件内容，入口/错误/服务配置缺，非所有该端口漏洞，自有canary/read权限边界确认。
132|g236 Pwntools logo无机制。
133|g237 遮挡域名对话框69，未有DOM/响应/消费方式，正文img style dataSVG畸形候选不普遍成立。
134|g242 Infoooze WHOIS图与148同内容另一像素文件已独立读，注册信息线索同nativefacet绑定本post。
135|g243 EyeBinder GUI native/managed/fakeerror/delay/runadmin/Defenderexclusions，选项不证明绕过/权限提升，预先授权执行条件。
136|g250 comb word×domain带dot生成子域名候选，不已存在；FQDN格式/重复/预算/DNS/owner验证。
137|g250 gee uniq替换域模板同候选输出，注入占位不是执行测试，保留原词+scope。
