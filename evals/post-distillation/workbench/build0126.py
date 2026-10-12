import json,re,ast
from recover import W
fs=json.loads(__import__('pathlib').Path('/private/tmp/facets0126-final.json').read_text())
(W/'facets0126.json').write_text(json.dumps(fs,ensure_ascii=False,indent=2)+'\n')
template=(W/'native0125.py').read_text()
tail=template[template.index('\nids={pid'):].replace('0125','0126').replace('len(urls)==120','len(urls)==128')
native=template[:template.index('facets = ')]+'facets = '+repr(fs)+tail
assert next(ast.literal_eval(n.value) for n in ast.parse(native).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))==fs
(W/'native0126.py').write_text(native)
(W/'media-actual-0126.json').write_text((W/'actual-0126.json').read_text())
bm=json.loads((W/'body-map0126.json').read_text())
text=(W/'body-display-0126.txt').read_text()
parts={int(m.group(1)):m.group(2) for m in re.finditer(r'\n\[(\d+)\] ids=[^\n]+\n(.*?)(?=\n\[\d+\] ids=|\Z)',text,re.S)}
assert len(parts)==250
rows=[]
for i in range(1,251):
 if str(i) in bm:
  v=bm[str(i)]; dis=v['dis'];ts=v['targets'];note=v['note']
 else:
  dis='excluded';ts=''
  first=next((l.strip() for l in parts[i].splitlines() if l.strip()),'空正文')
  first=re.sub(r'https?://\S+','[外链]',first)
  first=first.replace('|','｜')[:165]
  note='完整保存正文/替代文字已读；'+first+'；仅外链题名、工具/文章宣传、未保存续篇、成绩/状态或无独立可提炼机制；缺失图片和外链全文依用户按覆盖，不补造。'
 note=note.replace('|','｜').replace('\n',' ')
 rows.append(f'{i}|{dis}|{ts}|{note}')
(W/'spec0126.txt').write_text('\n'.join(rows)+'\n')
pre=(W/'precheck0125.py').read_text().replace('0125','0126').replace('==253','==255').replace('posts=253','posts=255').replace('==96','==116').replace('range(96)','range(116)').replace('media=96','media=116').replace('==83','==79').replace('facets=83','facets=79').replace('==120','==128')
(W/'precheck0126.py').write_text(pre)
print('Built0126 native/spec/precheck; no target or ledger mutation')

