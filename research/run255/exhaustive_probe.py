import itertools,json,numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent
for m in json.loads((P/'CHECKPOINTS.json').read_text())['rows']:
 if m['epoch']!=200:continue
 p=m['params'];A=np.array(p['A']);E=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 for n in range(1,8):
  w=np.array(list(itertools.product(range(3),repeat=n)),dtype=np.int8)
  h=np.zeros((len(w),4));q=np.zeros(len(w),dtype=np.int8)
  for j in range(n):
   s=w[:,j];h=np.maximum(0,h@A.T+E[s]+b)
   q=np.where(s==2,0,np.where(s==1,1-q if m['task']=='parity' else 1,q))
  bad=np.flatnonzero(((h@v+c)>0)!=q)
  if len(bad):
   print(m['task'],m['seed'],n,w[bad[0]].tolist());break
