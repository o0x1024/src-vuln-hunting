"""Generate own drafts; archive code never executed."""
import ast,json
from pathlib import Path
w=Path("/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting/evals/post-distillation/workbench")
plan=json.loads((w/"planned0122.json").read_text())
fs=plan["facets"]
assert len(fs)==84 and len({f for f,_,_ in fs})==31
(w/"facets0122.json").write_text(json.dumps(fs,ensure_ascii=False,indent=2)+"\n")
(w/"spec0122.txt").write_text(plan["body_spec"])
s=(w/"native0121.py").read_text().replace("0121","0122")
s=s[:s.index("facets = ")]+ "facets = "+json.dumps(fs,ensure_ascii=False,indent=2)+"\n"+s[s.index("ids={"):]
s=s.replace("len(urls)==106","len(urls)==127")
p=w/"native0122.py";assert not p.exists();p.write_text(s)
s=(w/"precheck0121.py").read_text().replace("0121","0122").replace("==253","==252").replace("posts=253","posts=252").replace("==86","==92").replace("range(86)","range(92)").replace("media=86","media=92").replace("==72","==84").replace("facets=72","facets=84").replace("==106","==127")
s=s.replace("assert len(fs)==84", 'assert fs==json.loads((W/"facets0122.json").read_text())\nassert len(fs)==84')
p=w/"precheck0122.py";assert not p.exists();p.write_text(s)
print("Own native/precheck0122 generated before target or ledger mutations")
