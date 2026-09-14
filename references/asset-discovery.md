# 阶段 2：资产测绘与信息收集

SRC 挖洞的上限由资产发现决定：面越全，机会越多。

## 子域名与域名资产
- 证书透明度：crt.sh、censys
- 子域名收集：subfinder、oneforall、amass
- 测绘平台：FOFA、Quake、鹰图、Zoomeye（注意数据版权与合规）
- 子域名接管检测：解析到可注册/已过期服务商（经典漏洞）

## 端口与服务
- masscan 快速全端口 → nmap -sV 指纹
- 关注非 80/443 端口：管理口、数据库、消息队列、调试服务

## Web 指纹与技术栈
- whatweb / wappalyzer：框架、CMS、中间件版本 → 关联历史 CVE
- 404/报错页特征、HTTP 头、cookie 特征辅助识别

## 目录与接口
- feroxbuster/dirsearch 字典枚举：后台、管理接口、.git、.svn、备份文件
- 常见：/api、/admin、/swagger-ui.html、/actuator、/console、/wp-content、/.git/config

## JS 文件分析
- 提取 API 端点、路由、硬编码密钥（AK/SK、token、appSecret）
- 工具：LinkFinder、jsfinder、浏览器 DevTools Sources

## 移动端与小程序
- APP：反编译（jadx）、抓包（Burp + 代理）、native 层关注签名与密钥
- 小程序：wxapkg 解包、抓包，常存在比 Web 更粗糙的接口

## 信息泄露渠道
- GitHub/Gitee 代码搜索（企业名+关键字）
- Git 泄露：/.git 目录还原源码（git-dumper）
- 备份文件：.bak/.zip/.sql、Swagger/API 文档
- 网盘/文库/招聘信息泄露（员工手册、运维文档）

## 云资产
- 存储桶：OSS/S3 开放读写、Bucket 接管
- CDN 回源 IP 绕过
- 云密钥泄露（AK/SK 出现在 GitHub/JS 中）

## 资产清单模板
| 资产 | 类型 | IP | 指纹/技术栈 | 接口/端点 | 是否在范围 | 备注 |