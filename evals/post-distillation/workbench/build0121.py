"""Generate own native and precheck files; no archive code execution."""
import json
from pathlib import Path
w=Path("/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting/evals/post-distillation/workbench")
fs=json.loads((w/"facets0121.json").read_text())
assert len(fs)==72 and len({f for f,_,_ in fs})==27
s=(w/"native0120.py").read_text().replace("0120","0121")
s=s[:s.index("facets = ")]+ "facets = "+json.dumps(fs,ensure_ascii=False,indent=2)+"\n"+s[s.index("ids={"):]
s=s.replace("len(urls)==107","len(urls)==106")
p=w/"native0121.py"; assert not p.exists(); p.write_text(s)
s=(w/"precheck0120.py").read_text().replace("0120","0121").replace("==251","==253").replace("posts=251","posts=253").replace("==93","==86").replace("range(93)","range(86)").replace("media=93","media=86").replace("==61","==72").replace("facets=61","facets=72").replace("==107","==106")
p=w/"precheck0121.py"; assert not p.exists(); p.write_text(s)
print("Generated native0121/precheck0121; no ledger mutations")

