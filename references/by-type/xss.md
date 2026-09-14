# XSS 技巧

## 类型与触发点
- 反射型：搜索框、URL 参数、错误信息回显
- 存储型：昵称、评论、签名、富文本、文件上传文件名（优先级最高）
- DOM 型：location.hash、postMessage、URL 参数直接进 sink

## 输出上下文与载荷
- HTML 标签内：`<script>alert(1)</script>`、`<img src=x onerror=alert(1)>`
- 属性内：`" onfocus=alert(1) autofocus="`、`" onmouseover="`
- JS 上下文：`';alert(1);//`、`\';alert(1);//`、模板字符串反引号
- 无尖括号场景：`<svg/onload=alert(1)>`、`<details open ontoggle=alert(1)>`、`javascript:alert(1)`（a href）

## DOM XSS
- Source：location、document.referrer、postMessage、window.name、localStorage
- Sink：innerHTML、document.write、eval、setTimeout/setInterval（字符串）、location 赋值、jQuery `$()`/`.html()`
- 技巧：断点审计前端 JS，追踪参数到 sink 的完整路径

## 编码与变形
- HTML 实体、URL 编码、Unicode（`<`）、JS 十六进制转义、大小写混淆
- 多字节截断、注释截断 `-->`、标签截断重开

## 绕过 CSP
- 检测：响应头 Content-Security-Policy 内容
- unsafe-inline / unsafe-eval 配置错误可直接打
- 白名单域名可 JSONP 劫持、可上传文件域同源、`script-src` 允许 'self' 但存在可控 JSONP 接口
- Angular/Vue 模板注入、`<base>` 标签配合

## 影响评估（SRC 视角）
- 存储型 XSS > 反射型；管理员后台触发 > 普通用户触发
- 可配合 CSRF 提权、窃取敏感操作凭证；HttpOnly 限制 cookie 窃取时转向钓鱼/CSRF 链

## 最小化验证
- 弹窗/打印 cookie（仅自己的）证明执行即可，不窃取真实用户数据
- 记录浏览器与版本、触发条件（是否需登录/特定角色）

## 报告要点
- 完整 URL + 触发参数 + payload、输出点上下文截图、影响面（谁可被攻击）、复现步骤
