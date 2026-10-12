# coding: utf-8
"""Own offline bookkeeping generation; never execute archive source."""
import ast,json
from recover import W
fs=json.loads((W/'facets0119.json').read_text())
assert len(fs)==66
old=(W/'native0118.py').read_text()
node=next(n for n in ast.parse(old).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
lines=old.splitlines(keepends=True)
s=''.join(lines[:node.lineno-1])+'facets = '+json.dumps(fs,ensure_ascii=False,indent=2)+'\n'+''.join(lines[node.end_lineno:])
s=s.replace('batch-0118.json','batch-0119.json').replace('assert len(urls)==93','assert len(urls)==109')
ast.parse(s)
assert not (W/'native0119.py').exists()
(W/'native0119.py').write_text(s)
p=(W/'precheck0118.py').read_text().replace('0118','0119').replace('==254','==253').replace('posts=254','posts=253').replace('==93','==90').replace('range(93)','range(90)').replace('media=93','media=90').replace('==54','==66').replace('facets=54','facets=66')
p=p.replace('assert len(urls)==90','assert len(urls)==109')
ast.parse(p)
assert not (W/'precheck0119.py').exists()
(W/'precheck0119.py').write_text(p)
print('Prepared native0119/precheck0119; no knowledge or ledger mutated')

