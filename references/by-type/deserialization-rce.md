# 反序列化与 RCE

## 触发点
- Java：原生 ObjectInputStream、fastjson、Jackson、SnakeYAML、XStream、Shiro（rememberMe Cookie）、WebLogic、JBoss
- PHP：unserialize()、phpggc gadget（Laravel/ThinkPHP 等）、反序列化入口（cookie/session/参数）
- Python：pickle、PyYAML、django
- .NET：BinaryFormatter、Newtonsoft.Json、ViewState

## 识别特征
- 请求体为 base64 二进制 / `O:8:"stdClass"` PHP 对象串 / `{"@type":...}` fastjson / `a1:"..."` Jackson
- 响应特征：Shiro rememberMe Cookie、WebLogic Console、Actuator env、堆栈含 `ObjectInputStream.readObject`

## 检测方法
- 被动：先抓正常请求，识别序列化数据格式与入口（Cookie、参数、Body、Header）
- 主动：发无害探测，用自建 dnslog 验证 DNS 带外回连
- gadget 探测：通用链（URLDNS/CommonsCollections 老版本）仅做 DNS 验证，不弹 shell

## 利用思路
- 已知框架版本 → 对应已知 gadget（需确认版本 + 在范围内）
- fastjson：`@type` 指定恶意类 → JNDI/LDAP 回连（仅在自建环境演示）
- PHP：phpggc 生成链，配合写文件/时间差验证
- 不出网环境：时间盲验证（sleep）、写文件到可访问目录

## 最小化验证（铁律）
- 用 DNS 带外/时间差证明反序列化执行即可
- 绝不落地真实 webshell、不反弹 shell、不横向移动
- 版本不确定时不盲目打 JNDI 链

## 报告要点
- 入口点 + 数据格式特征、触发证据（DNS 记录/时间差）、受影响组件与版本、影响面
