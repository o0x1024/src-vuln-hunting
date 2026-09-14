# WAF 绕过技巧

## 识别 WAF
- 拦截响应特征：403/406 页面文案（安全狗/云锁/宝塔/ModSecurity/腾讯云 WAF/阿里云 WAF/长亭雷池）
- 响应头与 Cookie 特征、拦截后跳转/JS 弹窗
- 工具：wafw00f

## 通用绕过思路
### 1. 编码层
- URL 编码、双重编码、UTF-8/Unicode 变体、Hex 编码、HTML 实体
- 关键词部分编码：`s%65lect`、`sel%65ct`

### 2. 空白与注释
- `/**/`、`--+`、`#`、`%0a`/`%0b`/`%09` 换行替代空格
- MySQL 内联注释：`/*!50000select*/`、`/*!select*/`

### 3. 关键字变形
- 字符串拼接：`concat('se','lect')`、`'ad'+'min'`（MSSQL 用 +）
- 等价函数：`substring→mid→substr`、`sleep→benchmark`、`concat→concat_ws`
- 大小写混合、重音符 ```` 包裹表名

### 4. 参数层面
- 参数污染 HPP：`?id=1&id=2`（后端取后一个）
- 同名参数注入、数组参数 `id[]=1` 触发报错
- JSON/XML 提交换 Content-Type，WAF 解析差异

### 5. 协议层
- Chunked 分块传输编码（Transfer-Encoding: chunked）分片绕过
- Content-Type 切换：multipart/form-data、application/json、text/plain
- 请求走私（CL.TE/TE.CL）——影响面大，仅在授权目标上谨慎验证

## 分类型绕过
- SQLi：`information_schema` 换 `sys.schema`/`mysql.innodb_table_stats`、无 select 的报错函数、堆叠前截断
- XSS：事件属性（onerror/onfocus/onmouseover）、无尖括号 DOM、SVG/MathML/iframe srcdoc
- 文件上传：双扩展名 `.php.jpg`、大小写 `.PhP`、`.htaccess`/`.user.ini`、图片马（GIF89a 头）、Content-Type 伪造

## 工具
- sqlmap：`--tamper=space2comment,between,randomcase` 等组合
- Burp 插件：bypass WAF、Param Miner（HPP/隐藏参数）

## 合规
- 绕过仅用于**已授权目标**；探测 WAF 时避免高并发触发封禁、绝不 DDoS
- 验证通过即止，最小化请求数量
