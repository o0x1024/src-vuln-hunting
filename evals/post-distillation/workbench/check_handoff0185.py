import json,re
from pathlib import Path
from urllib.parse import unquote
from recover import W
p=W/"HANDOFF.md";s=p.read_text()
s=re.sub(r"\x60\x60\x60[^\n]*\n.*?\x60\x60\x60","",s,flags=re.S)
s=re.sub(r"\x60[^\x60]*\x60","",s)
n=0;bad=[]
for m in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)",s):
 d=m.group(1).strip().strip("<>")
 if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:",d) and not d.startswith("/"):continue
 d=unquote(d.split("#",1)[0])
 if not d:continue
 d=re.sub(r":\d+$","",d)
 target=Path(d) if d.startswith("/") else p.parent/d
 n+=1
 if not target.exists():bad.append(d)
assert not bad,bad
print(json.dumps(dict(handoff_links=n,broken=len(bad))))
