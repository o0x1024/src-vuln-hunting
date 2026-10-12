import json,re,ast
from recover import W
fs=json.loads((W/'facets0210.json').read_text())
assert len(fs)==463 and len({f for f,_,_ in fs})==31
assert sum(len(re.findall(r'https://x\.com/i/status/(\d+)',body)) for _,_,body in fs)==495
template=(W/'native0199.py').read_text()
tail=template[template.index('\nids={pid'):].replace('0199','0210').replace('len(urls)==125','len(urls)==495')
native=template[:template.index('facets = ')]+'facets = '+repr(fs)+tail
assert next(ast.literal_eval(n.value) for n in ast.parse(native).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='facets' for t in n.targets))==fs
assert not (W/'native0210.py').exists()
(W/'native0210.py').write_text(native)
(W/'media-actual-0210.json').write_text((W/'actual-0210.json').read_text())
bm=json.loads((W/'body-map0210.json').read_text());txt=(W/'body-display-0210.txt').read_text()
parts={int(m.group(1)):m.group(2) for m in re.finditer(r'\n\[(\d+)\] ids=[^\n]+\n(.*?)(?=\n\[\d+\] ids=|\Z)',txt,re.S)}
assert len(parts)==200 and len(bm)==78
rows=[]
for i in range(1,201):
 if str(i) in bm:v=bm[str(i)];dis=v['dis'];ts=v['targets'];note=v['note']
 else:
  dis='excluded';ts=''
  first=next((l.strip() for l in parts[i].splitlines() if l.strip()),'空正文')
  first=re.sub(r'https?://\S+','[外链]',first).replace('|','｜')[:165]
  note='完整保存正文/有意义替代文字已实际读完；'+first+'；仅外链题名、宣传、未保存续篇、奖励/排名/状态或无独立可提炼机制；缺失图片及外链全文依用户按覆盖，不补造。'
 note=note.replace('|','｜').replace('\n',' ');rows.append(f'{i}|{dis}|{ts}|{note}')
(W/'spec0210.txt').write_text('\n'.join(rows)+'\n')
actual=json.loads((W/'media-actual-0210.json').read_text());spec={}
for line in (W/'media-spec0210.txt').read_text().strip().splitlines():
 i,dis,ts,note=line.split('|',3);spec[int(i)]=(dis,ts)
assert len(actual)==105 and len(spec)==105
for i,r in enumerate(actual):
 dis,ts=spec[i]
 if dis=='distilled':
  pid=r['name'].split('-')[0]
  for target in ts.split(','):assert any('references/'+f==target and 'https://x.com/i/status/'+pid in body and r['name'] in body for f,t,body in fs),(i,target,pid)
print('Built0210:463facets/31topics/495URLs;200groups205posts;105actualimages; no native/ledger append')
