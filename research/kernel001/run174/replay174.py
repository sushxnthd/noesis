import itertools,json
from pathlib import Path
import numpy as np
P=Path(__file__).parent
words=[''.join(t) for L in (2,4,6,8) for t in itertools.product('01',repeat=L) if t.count('0')==L//2]
assert len(words)==98
def run(cp):
 p=cp['parameters'];A=np.array(p['A'],float);E=np.array(p['E'],float);w=np.array(p['w'],float);n=len(w);res={}
 for word in words:
  h=np.zeros(n)
  for _ in range(6):h=np.maximum(A@h+E[0],0)
  first=None;e1=None;e32=None
  for k in range(1,8193):
   for c in word:h=np.maximum(A@h+E[int(c)],0)
   e=float(w@h-6)
   if k==1:e1=e
   if k==32:e32=e
   if first is None and (not np.isfinite(e) or abs(e)>.1):first=k
   if k>=32 and first is not None:break
  res[word]=[first,e1,e32]
 return res
if __name__=='__main__':
 out={}
 for width in (3,7):
  for seed in range(400,416):
   cp=json.loads((P/'checkpoints'/f'w{width}_seed{seed}.json').read_text())[0]
   out[f'{width}-{seed}']=run(cp)
 (P/'replay174_out.json').write_text(json.dumps(out,indent=2))
