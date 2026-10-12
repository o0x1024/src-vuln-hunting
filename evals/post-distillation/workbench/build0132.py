"""Own bookkeeping after actual complete body and original image review."""
import json,re,ast
from recover import W,T
fs=json.loads((W/'facets0132.json').read_text())
assert len(fs)==71 and len({f for f,_,_ in fs})==30
assert sum(len(re.findall(r'https://x\.com/i/status/(\d+)',body)) for _,_,body in fs)==98
template=(W/'native0130.py').read_text()
tail=template[template.index('\nids={pid'):].replace('0130','0132').replace('len(urls)==113','len(urls)==98')
native=template[:template.index('facets = ')]+'facets = '+repr(fs)+tail
assert next(ast.literal_eval(n.value) for n in ast.parse(native).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))==fs
assert not (W/'native0132.py').exists()
(W/'native0132.py').write_text(native)
(W/'media-actual-0132.json').write_text((W/'actual-0132.json').read_text())
bm=json.loads((W/'body-map0132.json').read_text())
txt=(W/'body-display-0132.txt').read_text()
parts={int(m.group(1)):m.group(2) for m in re.finditer(r'\n\[(\d+)\] ids=[^\n]+\n(.*?)(?=\n\[\d+\] ids=|\Z)',txt,re.S)}
assert len(parts)==250 and len(bm)==97
rows=[]
for i in range(1,251):
 if str(i) in bm:
  v=bm[str(i)];dis=v['dis'];ts=v['targets'];note=v['note']
 else:
  dis='excluded';ts=''
  first=next((l.strip() for l in parts[i].splitlines() if l.strip()),'空正文')
  first=re.sub(r'https?://\S+','[外链]',first).replace('|','｜')[:165]
  note='完整保存正文/有意义替代文字已实际读完；'+first+'；仅外链题名、宣传、未保存续篇、奖励/排名/状态或无独立可提炼机制；缺失图片及外链全文依用户按覆盖，不补造。'
 note=note.replace('|','｜').replace('\n',' ')
 rows.append(f'{i}|{dis}|{ts}|{note}')
(W/'spec0132.txt').write_text('\n'.join(rows)+'\n')
pre=(W/'precheck0131.py').read_text().replace('0131','0132').replace('==263','==251').replace('posts=263','posts=251').replace('==97','==113').replace('range(97)','range(113)').replace('media=97','media=113').replace('==68','==71').replace('facets=68','facets=71').replace('==102','==98')
(W/'precheck0132.py').write_text(pre)
actual=json.loads((W/'media-actual-0132.json').read_text());spec={}
for line in (W/'media-spec0132.txt').read_text().strip().splitlines():
 i,dis,ts,note=line.split('|',3);spec[int(i)]=(dis,ts)
for i,r in enumerate(actual):
 dis,ts=spec[i]
 if dis=='distilled':
  pid=r['name'].split('-')[0]
  for target in ts.split(','):
   assert any('references/'+f==target and 'https://x.com/i/status/'+pid in body for f,t,body in fs),(i,target,pid)
print('Built0132:71 facets/30 topics/98 batch URLs;250 groups251 posts;113 actual images; no native/ledger append')
