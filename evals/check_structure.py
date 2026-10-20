#!/usr/bin/env python3
"""Skill 结构守卫：把评审发现的三类退化固化为可执行断言。

硬性失败（退出码 1）：
  1. depth      任何 md 路径段数 > 3。skill 加载器硬限 max depth 3，
                超出后 list_files 与 read_file 直接报错，文件等于不存在。
  2. orphan     存在无任何入链的 md（SKILL.md 与 evals/ 除外）。
  3. broken     相对 .md 链接指向不存在的文件。
  4. leaf_size  references/by-type/*.md 超过 15 KB（判例应下沉 research）。

软性告警（不失败）：
  - template    by-type 未覆盖四节模板；仅统计，避免对存量做强改。
  - leaf_warn   叶子超过 12 KB 的预警线。

用法：python3 evals/check_structure.py [--root <skill dir>]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_DEPTH = 3
LEAF_HARD_KB = 15
LEAF_WARN_KB = 12
TEMPLATE_SECTIONS = ("适用信号与前提", "最小实验", "确认与反例", "下一步、停止与报告")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def rel(p: Path, root: Path) -> str:
    return str(p.relative_to(root))


def collect(root: Path):
    md = [p for p in root.rglob("*.md")
          if ".git" not in p.parts and "_out" not in p.parts]
    return sorted(md)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="skill 结构守卫")
    ap.add_argument("--root", type=Path,
                    default=Path(__file__).resolve().parent.parent)
    args = ap.parse_args(argv)
    root = args.root.resolve()
    files = collect(root)
    texts = {p: p.read_text(encoding="utf-8", errors="ignore") for p in files}

    fails: list[str] = []
    warns: list[str] = []

    # 1) 深度上限
    deep = [rel(p, root) for p in files if len(p.relative_to(root).parts) > MAX_DEPTH]
    if deep:
        fails.append(f"depth: {len(deep)} 个文件超过 {MAX_DEPTH} 段，加载器不可读")
        for d in deep[:10]:
            fails.append(f"  - {d}")

    # 2) 断链（仅相对 .md）
    broken = []
    for p, t in texts.items():
        for m in LINK_RE.finditer(t):
            target = m.group(1).split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not target.endswith(".md"):
                continue
            if not (p.parent / target).resolve().exists():
                broken.append(f"{rel(p, root)} -> {target}")
    if broken:
        fails.append(f"broken: {len(broken)} 条相对 md 链接失效")
        for b in broken[:10]:
            fails.append(f"  - {b}")

    # 3) 孤儿（无入链）
    orphans = []
    for p in files:
        if p.name == "SKILL.md" or p.parent.name == "evals":
            continue
        name = p.name
        if not any(name in t for q, t in texts.items() if q != p):
            orphans.append(rel(p, root))
    if orphans:
        fails.append(f"orphan: {len(orphans)} 个文件无任何入链")
        for o in orphans[:10]:
            fails.append(f"  - {o}")

    # 4) 叶子体积
    leaves = sorted((root / "references" / "by-type").glob("*.md"))
    over = []
    for p in leaves:
        kb = p.stat().st_size / 1024
        if kb > LEAF_HARD_KB:
            over.append(f"{p.name} {kb:.1f} KB")
        elif kb > LEAF_WARN_KB:
            warns.append(f"leaf_warn: {p.name} {kb:.1f} KB（> {LEAF_WARN_KB} KB）")
    if over:
        fails.append(f"leaf_size: {len(over)} 个叶子超过 {LEAF_HARD_KB} KB")
        for o in over:
            fails.append(f"  - {o}")

    # 5) 模板覆盖（软）
    missing = {}
    for sec in TEMPLATE_SECTIONS:
        hit = sum(1 for p in leaves if sec in texts[p])
        if hit < len(leaves):
            missing[sec] = hit
    if missing:
        warns.append("template: 四节模板覆盖不足（软告警，非失败）")
        for sec, hit in missing.items():
            warns.append(f"  - {sec}: {hit}/{len(leaves)}")

    print(f"检查 {len(files)} 个 md（根：{root}）")
    print(f"叶子 {len(leaves)} 个，最大 {max((p.stat().st_size / 1024 for p in leaves), default=0):.1f} KB")
    for w in warns:
        print(f"[WARN] {w}")
    if fails:
        for f in fails:
            print(f"[FAIL] {f}")
        return 1
    print("[OK] depth / orphan / broken / leaf_size 全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
