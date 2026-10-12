# coding: utf-8
"""Own offline bookkeeping only; no archive source execution."""
import ast,json
from recover import W
fs=json.loads((W/'facets0120.json').read_text());assert len(fs)==61
old=(W/'native0119.py').read_text()
node=next(n for n in ast.parse(old).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))
lines=old.splitlines(keepends=True)
s=''.join(lines[:node.lineno-1])+'facets = '+json.dumps(fs,ensure_ascii=False,indent=2)+'\n'+''.join(lines[node.end_lineno:])
s=s.replace('batch-0119.json','batch-0120.json').replace('assert len(urls)==109','assert len(urls)==107')
ast.parse(s);assert not (W/'native0120.py').exists();(W/'native0120.py').write_text(s)
p=(W/'precheck0119.py').read_text().replace('0119','0120').replace('==253','==251').replace('posts=253','posts=251').replace('==90','==93').replace('range(90)','range(93)').replace('media=90','media=93').replace('==66','==61').replace('facets=66','facets=61').replace('==109','==107')
ast.parse(p);assert not (W/'precheck0120.py').exists();(W/'precheck0120.py').write_text(p)
print('Prepared native0120/precheck0120; no native knowledge or review ledger mutation')

