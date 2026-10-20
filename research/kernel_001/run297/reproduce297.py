"""NOESIS Run297: exact, frozen cross-task failure reproduction on public CPU."""
import hashlib,json,math,types
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
P=Path(__file__).resolve().parent;BASE=P.parent/'run294'
HCK='620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473'
HSC='9db6047ca36e307a9577696187ec0a977060eda793792f6936b4ed452b2af662'

def exact_wrong(p,word):
 z=list(map(Q.from_float,p));h=[Q(0)]*3;q=0
 for bit in word:
  x=int(bit);q|=x
  h=[max(Q(0),sum(z[x*9+i*3+j]*h[j] for j in range(3))+z[18+x*3+i]) for i in range(3)]
  if (sum(z[24+i]*h[i] for i in range(3))+z[27]>0)!=bool(q):return True
 return False

def witness(p):
 a=np.asarray(p[:18]).reshape(2,3,3);b=np.asarray(p[18:24]).reshape(2,3);v=np.asarray(p[24:27]);c=p[27]
 h=np.zeros((1,3));y=np.zeros(1,dtype=int);words=np.zeros(1,dtype=np.int64)
 for n in range(1,13):
  hh=[];yy=[];ww=[]
  for x in (0,1):
   z=np.maximum(0,h@a[x].T+b[x]);t=np.maximum(y,x);w=words*2+x
   for i in np.flatnonzero(((z@v+c)>0)!=t)[:8]:
    s=format(int(w[int(i)]),f'0{n}b')
    if exact_wrong(p,s):return s
   hh.append(z);yy.append(t);ww.append(w)
  h=np.concatenate(hh);y=np.concatenate(yy);words=np.concatenate(ww)
 return None

def main():
 source=(BASE/'train291.py').read_text()
 for old,new in {'W=3;N=256;T=6':'W=3;N=128;T=6','range(21440,21696)':'range(21800,21928)',
  'q=torch.where(x[:,t]==0,0,1-q)':'q=torch.bitwise_or(q,x[:,t])',
  "'checkpoints291.json'":"'checkpoints297.json'"}.items():
  assert source.count(old)==1,old;source=source.replace(old,new)
 exec(compile(source,str(P/'train297.py'),'exec'),{'__file__':str(P/'train297.py'),'__name__':'__main__'})
 ck=P/'checkpoints297.json';d=json.loads(ck.read_text());d['config']['task']='persistent-latch'
 ck.write_text(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n')
 assert hashlib.sha256(ck.read_bytes()).hexdigest()==HCK
 source=(BASE/'diagnostic291.py').read_text();assert source.count('y=0 if x==0 else 1-s')==1
 mod=types.ModuleType('latch_lp');mod.__file__=str(P/'diagnostic297.py')
 exec(compile(source.replace('y=0 if x==0 else 1-s','y=s|x'),mod.__file__,'exec'),mod.__dict__)
 by={(r['seed'],r['epoch']):r for r in d['rows']};early=[]
 for seed in d['config']['seeds']:
  r=by[(seed,20)];p=r['p']
  early.append({'seed':seed,'gauge_score':-mod.lp(mod.canonical(p)),'negative_bce':-r['bce'],
   'early_accuracy':r['accuracy'],'negative_param_norm':-math.sqrt(sum(z*z for z in p))})
 (P/'FROZEN_EARLY_SCORES297.json').write_text(json.dumps(early,sort_keys=True,separators=(',',':'))+'\n')
 assert hashlib.sha256((P/'FROZEN_EARLY_SCORES297.json').read_bytes()).hexdigest()==HSC
 rows=[]
 for seed in d['config']['seeds']:
  r=by[(seed,80)];p=r['p'];candidate=mod.lp(p,certificate=True)
  assert candidate is None,'unverified candidate requires separate exact checker'
  w=witness(p);rows.append({'seed':seed,'status':'incorrect' if w else 'unresolved',
   'witness':w,'sampled_perfect':r['accuracy']==1})
 (P/'rows297_compact.json').write_text(json.dumps(rows,indent=2,sort_keys=True)+'\n')
 wrong=sum(r['status']=='incorrect' for r in rows);perfect=sum(r['sampled_perfect'] for r in rows)
 spoof=sum(r['status']=='incorrect' and r['sampled_perfect'] for r in rows)
 assert (wrong,perfect,spoof)==(70,63,5),(wrong,perfect,spoof)
 print('RUN297 VERIFIED',json.dumps({'trained':128,'certified':0,'exact_wrong':wrong,
  'unresolved':128-wrong,'sampled_perfect':perfect,'sampled_perfect_wrong':spoof,
  'frozen_primary_pass':False,'auc':'undefined (zero certified positives)'}))
if __name__=='__main__':main()
