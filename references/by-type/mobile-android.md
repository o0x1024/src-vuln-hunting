# Android 导出组件与深链接

适用信号：授权 APK、Manifest、exported 组件、App Links 或外部 Intent

## 检查与最小实验

离线解析已授权 APK，记录包名、签名、版本、targetSdk 与组件权限。用 Manifest→导出组件→入口参数→敏感代码建立候选表，再选有具体边界线索的入口在自建设备/模拟器验证。

深链接核对 scheme/host、App Links 验证、参数校验和应用内认证状态。显式 Intent 能打开 Activity 与能绕过其内部权限不同；ADB/shell 身份可能比普通第三方应用有更多能力，最终证据应匹配实际攻击者身份。

## 证据与反例

exported=true 可以是正常产品需求；风险在普通外部调用者获得被禁止的数据/操作。启动器组件、正常深链接、离线发现敏感类名都不是接管证明。

## Agent 行为

X 帖子提供“静态筛选后动态验证”的线索，相关工具本身未评估，不执行帖子给出的未知软件。解包/反编译可自动化，操作参数和影响仍要核对。仅覆盖此专题，不能据此宣称完成 iOS、原生内存或全部移动端测试。

## 调研来源

- [Android-exported · android:exported](https://developer.android.com/privacy-and-security/risks/android-exported)
- [Android-links · Unsafe use of deep links](https://developer.android.com/privacy-and-security/risks/unsafe-use-of-deeplinks)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
