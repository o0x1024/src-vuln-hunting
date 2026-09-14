# CI/CD 与构建信任边界

适用信号：获准仓库、workflow、外部 PR、构建制品、runner

## 检查与最小实验

先离线画触发者→不可信输入→执行 job→令牌/密钥/制品消费者。检查 PR 文本或外部代码进入 shell 的方式，第三方 action 的版本固定和实际来源，以及自托管 runner 是否与其他作业共享状态。

区分只读 PR 检查与能获取写权限/秘密的后续阶段；在本地复刻或项目提供的隔离 runner 用无害标记证明输入进入执行/发布路径。仅有高权限事件名或可移动 tag 是风险线索，仍需可达链。

## 证据与反例

公开构建日志、action 未固定 SHA、runner 自托管都不能单独推断供应链接管。应指出攻击者可控制什么、在哪一阶段跨过信任边界以及实际权限。

## Agent 行为

不向第三方仓库提交 PR 触发生产 job，不发布同名包、污染公共 registry 或读取真实构建秘密。仓库读取许可不自动包含触发流水线/发布许可；证据足够时交付可复核路径而非制造供应链事件。

## 调研来源

- [GH-actions · Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)

资料核对日期：2026-09-14。来源的证据层级与历史日期见 [来源登记](../research/sources.json)；实验安排是本 skill 的综合设计，不表示已在当前目标复现。
