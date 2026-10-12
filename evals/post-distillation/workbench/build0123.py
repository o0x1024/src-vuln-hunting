"""Own draft generation only; no archive execution."""
import json
from pathlib import Path
w=Path("/Users/len/Library/Application Support/sentinel-ai/skills/src-vuln-hunting/evals/post-distillation/workbench")
fs=json.loads((w/'facets0123.json').read_text())
assert len(fs)==70 and len({f for f,_,_ in fs})==28
template=(w/'native0122.py').read_text()
tail=template[template.index('ids={'):].replace('0122','0123').replace('len(urls)==127','len(urls)==115')
head='''# coding: utf-8
"""Own native distillation; no source execution."""
import json,re
from collections import defaultdict
from recover import T,W
'''
p=w/'native0123.py';assert not p.exists()
p.write_text(head+'facets = '+json.dumps(fs,ensure_ascii=False,indent=2)+'\n'+tail)
print('Generated own native0123 draft; no target references or ledger writes yet')
