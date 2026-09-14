# 文件包含与路径穿越

## 类型
- LFI：`?page=../../../../etc/passwd`、PHP include 本地文件包含
- 路径穿越：`?file=../../`、下载功能 filename 参数
- 任意文件读取：readfile/file_get_contents/download 接口
- 目录遍历：备份文件、日志、源码读取

## 发现点
- 参数名特征：file、path、page、template、lang、download、filename、img、doc
- 功能入口：下载、预览、导出、模板渲染、日志查看、语言切换
- 报错泄露：路径信息、include 路径回显

## 利用技巧
- 基础：`../../../../etc/passwd`（试深度）、`/etc/passwd`、Windows 下 `C:\windows\win.ini`
- 编码绕过：`../` 编码 `%2e%2e%2f`、双写 `....//`、URL 编码、路径归一化差异
- 日志投毒：访问 `/var/log/apache/access.log` 注入 PHP 代码（需能写日志 + 无 WAF）
- PHP 伪协议：`php://filter/convert.base64-encode/resource=index.php` 读源码、`data://` 执行、`php://input`
- 配合上传：图片马 + include（见 file-upload.md）
- 会话文件包含：`/tmp/sess_<sessionid>`（可控 session 内容）

## 验证
- 读 `/etc/passwd` 或应用配置文件证明（不读真实用户数据）
- 伪协议读源码时只取少量行证明
- 目录枚举不批量拉取

## 报告要点
- 触发 URL + 参数 + payload、读取到的文件内容样例（脱敏）、可达敏感文件清单
