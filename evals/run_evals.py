#!/usr/bin/env python3
"""evals 目录统一入口：结构校验、回归测试、盲评判读清单、按 checks 评分。

子命令：
  validate   校验 5 个用例文件与 expected.json 的结构、编号连续性、覆盖与词表问题
  structure  校验 skill 目录结构：深度上限、孤儿文件、相对链接、叶子体积
  run        运行全部 test_*.py（unittest，确定性离线回归，零网络请求）
  checklist  生成评分者对照表 _out/checklist.md（含 checks，自带预期结论，不可交给执行者）
  brief      生成盲评材料 _out/brief.md（只有题面与证据，不含 checks 与 expected）
  score      按每条 checks 对结果文件评分
  all        validate + run + brief + checklist

结果文件 schema（score 用，UTF-8 JSON）：
{
  "C01": {"prediction": "confirmed", "checks": ["通过", "未通过", "未评"]},
  "C02": {"checks": {"确认具体跨租户私有文件读取": true}}
}
checks 支持三种写法：按序状态列表、按文本布尔映射、整例布尔。
状态取值：true/pass/通过/yes → 通过；false/fail/未通过/no → 未通过；其余 → 未评。
缺失的用例计为未评。prediction 仅做参考统计：expected 字段不是受控词表，
其中 stage_aware_decision 等 4 个值实为分组标签而非判定结论，不可当答案匹配。
"""
from __future__ import annotations

import argparse
import collections
import json
import subprocess
import sys
from pathlib import Path

EVALS = Path(__file__).resolve().parent
CASE_FILES = (
    "cases.json",
    "cases-discovery-and-reasoning.json",
    "cases-targeted-fuzzing.json",
    "cases-business-context.json",
    "cases-ai-and-devices.json",
)
REQUIRED_FIELDS = ("case_id", "user_request", "context", "evidence")
GROUP_LABEL_HINT = {
    "stage_aware_decision",
    "expert_reasoning_decision",
    "targeted_fuzzing_decision",
    "domain_and_policy_decision",
}
PASS_STATES = {True, "pass", "passed", "通过", "yes", "true"}
FAIL_STATES = {False, "fail", "failed", "未通过", "no", "false"}


def load(cases_dir: Path = EVALS):
    cases, order, per_file = {}, [], {}
    for name in CASE_FILES:
        doc = json.loads((cases_dir / name).read_text(encoding="utf-8"))
        items = doc["cases"]
        per_file[name] = [c.get("case_id") for c in items]
        for case in items:
            cid = case.get("case_id")
            cases.setdefault(cid, case)
            order.append(cid)
    expected_doc = json.loads((cases_dir / "expected.json").read_text(encoding="utf-8"))
    expected = {e.get("case_id"): e for e in expected_doc["cases"]}
    return cases, order, per_file, expected


def _num(cid: str) -> int:
    digits = "".join(ch for ch in str(cid) if ch.isdigit())
    return int(digits) if digits else -1


def _fmt(num: int) -> str:
    return f"C{num:02d}"


def validate(cases_dir: Path = EVALS) -> int:
    cases, order, per_file, expected = load(cases_dir)
    problems, warnings = [], []

    dup = [cid for cid, n in collections.Counter(order).items() if n > 1]
    if dup:
        problems.append(f"case_id 重复：{sorted(dup)}")

    for cid, case in cases.items():
        missing = [f for f in REQUIRED_FIELDS if f not in case]
        if missing:
            problems.append(f"{cid} 缺少字段：{missing}")

    nums = sorted(_num(c) for c in cases)
    if nums:
        gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]
        if gaps:
            problems.append(f"编号不连续，缺口：{gaps[:20]}")

    no_expect = sorted(set(cases) - set(expected), key=_num)
    extra_expect = sorted(set(expected) - set(cases), key=_num)
    if no_expect:
        problems.append(f"缺少预期：{no_expect}")
    if extra_expect:
        problems.append(f"预期无对应用例：{extra_expect}")

    for cid, entry in expected.items():
        checks = entry.get("checks")
        if not isinstance(checks, list) or not checks:
            problems.append(f"{cid} 的 checks 为空或非列表")
            continue
        if any(not isinstance(c, str) or not c.strip() for c in checks):
            problems.append(f"{cid} 的 checks 含空项或非字符串")
        if len(set(checks)) != len(checks):
            problems.append(f"{cid} 的 checks 有重复项")

    labels = collections.Counter(e.get("expected") for e in expected.values())
    groupish = {k: v for k, v in labels.items() if k in GROUP_LABEL_HINT}
    if groupish:
        warnings.append(
            "expected 中有 4 个取值实为分组标签而非判定结论，共 "
            f"{sum(groupish.values())} 例：{groupish}；这些例子的 `expected` 不能当答案匹配。"
        )
    if len(labels) > 20:
        warnings.append(
            f"expected 共 {len(labels)} 种取值，其中 {sum(1 for v in labels.values() if v == 1)} 种只出现 1 次："
            "该字段是自由文本，不是受控词表，评分必须走 checks 逐项判定。"
        )

    total_checks = sum(len(e.get("checks") or []) for e in expected.values())
    print(f"用例文件 {len(CASE_FILES)} 个，用例 {len(cases)} 例（编号 {_fmt(nums[0])}..{_fmt(nums[-1])}）")
    for name in CASE_FILES:
        ids = per_file[name]
        span = f"{_fmt(_num(ids[0]))}..{_fmt(_num(ids[-1]))}" if ids else "-"
        print(f"  {name:34s} {len(ids):3d} 例  {span}")
    print(f"预期 {len(expected)} 条，checks 合计 {total_checks} 项（每例 2–5 项）")

    for w in warnings:
        print(f"[注意] {w}")
    if problems:
        print(f"\n[失败] {len(problems)} 项：")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\n[通过] 结构、编号、覆盖、checks 均无问题")
    return 0


def run(cases_dir: Path = EVALS) -> int:
    cmd = [
        sys.executable, "-m", "unittest", "discover",
        "-s", str(cases_dir), "-t", str(cases_dir), "-p", "test_*.py", "-v",
    ]
    print("$ " + " ".join(cmd), flush=True)
    return subprocess.run(cmd, cwd=str(cases_dir), text=True).returncode


def brief(cases_dir: Path = EVALS) -> int:
    """只输出题面与证据，供盲评使用；不含判定项与评分预期。"""
    cases, order, per_file, expected = load(cases_dir)
    out_dir = cases_dir / "_out"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "brief.md"
    lines = [
        "# 盲评材料",
        "",
        "只含题面与证据，不含判定项与评分结论。交给执行者时连同当前 skill 与允许读取的参考文件。",
        "要求输出见 protocol.md：case_id / hypothesis_status / coverage_status / run_status / status_scope /",
        "已证明事实 / 限制 / 证据 ID / 下一步 / 拟发请求数量。",
        "",
    ]
    for name in CASE_FILES:
        lines += [f"## {name}（{len(per_file[name])} 例）", ""]
        for cid in per_file[name]:
            case = cases[cid]
            lines += [f"### {cid}", "", f"题面：{case.get('user_request', '')}", ""]
            context = case.get("context")
            if context:
                lines += ["上下文：", "", "```json",
                          json.dumps(context, ensure_ascii=False, indent=1), "```", ""]
            evidence = case.get("evidence") or []
            if evidence:
                lines += ["证据：", "", "```json",
                          json.dumps(evidence, ensure_ascii=False, indent=1), "```", ""]
    out.write_text("\n".join(lines), encoding="utf-8")

    # 自检：任一条判定项都不得出现在盲评材料里，防止日后改坏而静默泄漏答案。
    text = out.read_text(encoding="utf-8")
    leaked = [c for e in expected.values() for c in (e.get("checks") or []) if c in text]
    if leaked:
        print(f"[失败] 盲评材料泄漏 {len(leaked)} 条判定项，例如：{leaked[0][:40]}")
        return 1

    print(f"已生成 {out}（{len(order)} 例，无判定项，泄漏自检通过）")
    return 0


def checklist(cases_dir: Path = EVALS) -> int:
    cases, order, per_file, expected = load(cases_dir)
    out_dir = cases_dir / "_out"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "checklist.md"
    lines = [
        "# 评分者对照表（不可交给执行者）",
        "",
        "本表不含 `expected` 值，但 `checks` 文本本身写明了各例应得结论（例如“管理员分支 blocked”），",
        "因此**不是盲评材料**——交给执行者等于给答案。盲评请用 `run_evals.py brief` 生成 `_out/brief.md`。",
        "评分者在方框内标 `x`（通过）或 `!`（不通过），留空即未评。",
        "",
    ]
    for name in CASE_FILES:
        lines += [f"## {name}（{len(per_file[name])} 例）", ""]
        for cid in per_file[name]:
            case = cases[cid]
            checks = expected[cid].get("checks") or []
            lines.append(f"### {cid}")
            lines.append("")
            lines.append(f"题面：{case.get('user_request', '')}")
            evidence = case.get("evidence") or []
            lines.append(f"证据 {len(evidence)} 条。判定项：")
            lines.append("")
            for check in checks:
                lines.append(f"- [ ] {check}")
            lines.append("")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"已生成 {out}（{len(order)} 例）")
    return 0


def _norm_state(value):
    if value in PASS_STATES:
        return True
    if value in FAIL_STATES:
        return False
    return None


def score(results_path: Path, cases_dir: Path = EVALS) -> int:
    _, order, _, expected = load(cases_dir)
    raw = json.loads(results_path.read_text(encoding="utf-8"))

    per_case, unrated, check_total, check_pass = {}, [], 0, 0
    agree, decide_total = 0, 0
    for cid in order:
        entry = raw.get(cid)
        checks = expected[cid].get("checks") or []
        if not entry:
            unrated.append(cid)
            per_case[cid] = None
            continue
        given = entry.get("checks")
        states = []
        if isinstance(given, dict):
            states = [_norm_state(given.get(c)) for c in checks]
        elif isinstance(given, list):
            states = [_norm_state(v) for v in given[: len(checks)]]
            states += [None] * (len(checks) - len(states))
        elif isinstance(given, bool):
            states = [given] * len(checks)
        else:
            unrated.append(cid)
            per_case[cid] = None
            continue
        passed = sum(1 for s in states if s is True)
        check_total += len(checks)
        check_pass += passed
        per_case[cid] = {"passed": passed, "total": len(checks), "ok": passed == len(checks)}
        pred = entry.get("prediction")
        if pred is not None:
            decide_total += 1
            if pred == expected[cid].get("expected"):
                agree += 1

    rated = [c for c in order if per_case.get(c)]
    full = [c for c in rated if per_case[c]["ok"]]
    print(f"已评 {len(rated)}/{len(order)} 例，未评 {len(unrated)} 例")
    print(f"逐项通过 {check_pass}/{check_total}"
          + (f"（{check_pass / check_total:.1%}）" if check_total else ""))
    print(f"全项通过的用例 {len(full)}/{len(rated)}"
          + (f"（{len(full) / len(rated):.1%}）" if rated else ""))
    if decide_total:
        print(f"prediction 与 expected 文本相同：{agree}/{decide_total}"
              "（仅供参考：expected 非受控词表，含 4 个分组标签）")
    if unrated:
        print(f"未评：{unrated[:20]}{' …' if len(unrated) > 20 else ''}")

    out = cases_dir / "_out" / "score.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(
        {"rated": len(rated), "total": len(order), "checks_passed": check_pass,
         "checks_total": check_total, "cases_full_pass": len(full),
         "unrated": unrated, "per_case": per_case},
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"明细已写入 {out}")
    return 0 if not unrated else 2


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="离线评测集统一入口")
    parser.add_argument("command", choices=("validate", "structure", "run", "checklist", "brief", "score", "all"))
    parser.add_argument("--results", type=Path, help="score 用的结果文件（JSON）")
    args = parser.parse_args(argv)

    if args.command == "validate":
        return validate()
    if args.command == "structure":
        return subprocess.call([sys.executable, str(EVALS / "check_structure.py")])
    if args.command == "run":
        return run()
    if args.command == "checklist":
        return checklist()
    if args.command == "brief":
        return brief()
    if args.command == "score":
        if not args.results:
            parser.error("score 需要 --results <path>")
        return score(args.results)
    rc = validate()
    rc |= subprocess.call([sys.executable, str(EVALS / "check_structure.py")])
    rc |= run()
    rc |= brief()
    rc |= checklist()
    return rc


if __name__ == "__main__":
    sys.exit(main())
