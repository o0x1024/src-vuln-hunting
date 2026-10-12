# coding: utf-8
"""Own offline bookkeeping generation; never execute archive source."""
import ast,json
from pathlib import Path
from recover import W
fs=json.loads((W/'facets0118.json').read_text())
assert len(fs)==54
old=(W/'native0117.py').read_text()
tree=ast.parse(old)
node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
lines=old.splitlines(keepends=True)
text=''.join(lines[:node.lineno-1])+'facets = '+json.dumps(fs,ensure_ascii=False,indent=2)+'\n'+''.join(lines[node.end_lineno:])
text=text.replace('batch-0117.json','batch-0118.json').replace('assert len(urls)==99','assert len(urls)==93')
ast.parse(text)
assert not (W/'native0118.py').exists()
(W/'native0118.py').write_text(text)
pre=(W/'precheck0117.py').read_text().replace('0117','0118').replace('==92','==93').replace('range(92)','range(93)').replace('media=92','media=93').replace('==63','==54').replace('facets=63','facets=54').replace('==99','==93')
ast.parse(pre)
assert not (W/'precheck0118.py').exists()
(W/'precheck0118.py').write_text(pre)
print('Prepared native0118 and precheck0118; no knowledge or ledger mutated')

