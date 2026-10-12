"""Independent narrow validation; not the official PyYAML validator."""
import re,json
from pathlib import Path
from recover import T
s=(T/'SKILL.md').read_text()
m=re.match(r'^---\n(.*?)\n---(?:\n|$)',s,re.S);assert m
lines=m[1].splitlines()
assert len(lines)==2 and lines[0].startswith('name: ') and lines[1].startswith('description: ')
name=lines[0][6:].strip();description=lines[1][13:].strip()
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) and len(name)<=64
assert description and len(description)<=1024 and not any(c in description for c in '<>\n')
assert not description.startswith('[TODO:')
# The saved frontmatter uses two plain single-line scalar values.
assert all(not re.search(r'[:][ \t]|[ \t]#',v) and not v.startswith(('[','{','&','*','!','|','>','@','`','"',"'")) for v in (name,description))
marker=None;n=0
for line in s[m.end():].splitlines():
 f=re.match(r'^[ \t]*(?:(?:[-+*]|\d+[.)])[ \t]+)?(`{3,}|~{3,})(.*)$',line)
 if f:
  if marker is None:marker=f[1][0];n=len(f[1])
  elif f[1][0]==marker and len(f[1])>=n and not f[2].strip():marker=None;n=0
 elif marker is None:assert not re.fullmatch(r'[ ]{0,3}\[TODO:[^\n]*\][ \t]*',line)
assert marker is None
print(json.dumps(dict(frontmatter='two plain scalars valid',name=name,description_length=len(description),unfinished_TODO=False,fences='balanced',official_quick_validate='unavailable: ModuleNotFoundError yaml'),ensure_ascii=False))
