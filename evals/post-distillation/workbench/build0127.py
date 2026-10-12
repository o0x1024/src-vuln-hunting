"""Own offline bookkeeping after actual complete text and pixel review."""
import json,re,ast,collections
from recover import W
fs=json.loads((W/'facets0127.json').read_text())
assert len(fs)==75 and len({f for f,_,_ in fs})==30
urls=sum(len(re.findall(r'https://x\.com/i/status/(\d+)',body)) for _,_,body in fs)
assert urls==108
template=(W/'native0126.py').read_text()
tail=template[template.index('\nids={pid'):].replace('0126','0127').replace('len(urls)==128','len(urls)==108')
native=template[:template.index('facets = ')]+'facets = '+repr(fs)+tail
assert next(ast.literal_eval(n.value) for n in ast.parse(native).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))==fs
assert not (W/'native0127.py').exists()
(W/'native0127.py').write_text(native)
(W/'media-actual-0127.json').write_text((W/'actual-0127.json').read_text())
bm=json.loads((W/'body-map0127.json').read_text())
for i in [56,65,77,84,121,150,177,226,240]:
 assert str(i) in bm
 bm[str(i)]['dis']='merged'
 bm[str(i)]['note']+='；重复/相近线索并入本批同一方法，保留各原帖来源。'
(W/'body-map0127.json').write_text(json.dumps(bm,ensure_ascii=False,indent=2)+'\n')
txt=(W/'body-display-0127.txt').read_text()
parts={int(m.group(1)):m.group(2) for m in re.finditer(r'\n\[(\d+)\] ids=[^\n]+\n(.*?)(?=\n\[\d+\] ids=|\Z)',txt,re.S)}
assert len(parts)==250
rows=[]
for i in range(1,251):
 if str(i) in bm:
  v=bm[str(i)];dis=v['dis'];ts=v['targets'];note=v['note']
 else:
  dis='excluded';ts=''
  first=next((l.strip() for l in parts[i].splitlines() if l.strip()),'空正文')
  first=re.sub(r'https?://\S+','[外链]',first).replace('|','｜')[:165]
  note='完整保存正文/有意义替代文字已实际读完；'+first+'；仅外链题名、工具/课程宣传、未保存续篇、奖励/排名/状态或无独立可提炼机制；缺失图片及外链全文依用户按覆盖，不补造。'
 note=note.replace('|','｜').replace('\n',' ')
 rows.append(f'{i}|{dis}|{ts}|{note}')
(W/'spec0127.txt').write_text('\n'.join(rows)+'\n')
pre=(W/'precheck0126.py').read_text().replace('0126','0127').replace('==255','==252').replace('posts=255','posts=252').replace('==116','==106').replace('range(116)','range(106)').replace('media=116','media=106').replace('==79','==75').replace('facets=79','facets=75').replace('==128','==108')
(W/'precheck0127.py').write_text(pre)
print('Built0127:75 facets/30 topics/108 URLs, 250 body specs and106 actual media; no native or ledger append')
