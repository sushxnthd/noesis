"""NOESIS Run248: deterministic longer-horizon counterexample proposals.
Replays are exact. Absence of a witness is never a correctness certificate.
"""
import json, hashlib, itertools, csv
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from research.run247.replay import verify
D=Path(__file__).resolve().parent
ROOT=D.parent
SEEDS=(10005,10013,10019,10031,10032,10037,10042)
LENGTHS=(16,24,32,48,64,96,128,192,256)
def generate():
 seen=set()
 def add(w):
  if 13<=len(w)<=256 and w not in seen:
   seen.add(w);return w
 for n in range(13,257):
  for s in range(3):
   for w in ((s,)*n,(1,)+(0,)*(n-1),(2,)+(0,)*(n-1),
             (0,)*(n-1)+(s,),(1,)+(2,)*(n-1),(2,)+(1,)*(n-1)):
    z=add(w)
    if z is not None:yield z
 block=(1,2,3,4,5,7,8,11,13,16,21,32,34,48,55,64,89,96,128,144,192)
 for a in block:
  for b in range(1,257-a):
   for pre,suf in ((1,0),(2,0),(1,2),(2,1),(0,1),(0,2)):
    z=add((pre,)*a+(suf,)*b)
    if z is not None:yield z
    if len(seen)>=40000:return
 for n in range(13,257):
  for period in ((1,0),(2,0),(1,2),(2,1),(1,0,2,0),(2,0,1,0),
                 (0,0,1),(0,0,2),(1,1,0),(2,2,0)):
   for phase in range(len(period)):
    z=add(tuple(period[(i+phase)%len(period)] for i in range(n)))
    if z is not None:yield z
    if len(seen)>=40000:return
 rng=np.random.default_rng(248)
 while len(seen)<40000:
  n=int(rng.choice(LENGTHS))
  probs=((.90,.05,.05),(.70,.15,.15),(.33,.34,.33))[int(rng.integers(3))]
  z=add(tuple(int(x) for x in rng.choice(3,size=n,p=probs)))
  if z is not None:yield z
def find(row,words):
 p=row['params'];a=np.array(p['A']);e=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 for n in sorted(set(map(len,words))):
  group=[w for w in words if len(w)==n]
  for i in range(0,len(group),1024):
   sub=group[i:i+1024];x=np.array(sub,dtype=np.int8)
   h=np.zeros((len(sub),len(v)));q=np.zeros(len(sub),dtype=np.int8)
   for t in range(n):
    tok=x[:,t];h=np.maximum(0,h@a.T+e[tok]+b)
    q=np.where(tok==2,0,np.where(tok==1,1,q))
   wrong=np.flatnonzero(((h@v+c)>0)!=q)
   if len(wrong):return list(sub[int(wrong[0])])
 return None
def independent(row,word):
 p=row['params'];f=lambda x:Q(*x.as_integer_ratio())
 a=tuple(tuple(map(f,r)) for r in p['A']);e=tuple(tuple(map(f,r)) for r in p['E'])
 b=tuple(map(f,p['b']));v=tuple(map(f,p['v']));c=f(p['c'])
 state=tuple(Q(0) for _ in v);target=0
 for symbol in word:
  nxt=[]
  for j in range(len(v)):
   z=e[symbol][j]+b[j]
   for k in range(len(v)):z+=a[j][k]*state[k]
   nxt.append(z if z>0 else Q(0))
  state=tuple(nxt)
  if symbol==1:target=1
  elif symbol==2:target=0
 z=c
 for w,x in zip(v,state):z+=w*x
 return int(z>0)!=target,target,int(z>0)
def main():
 cp=ROOT/'run246/CHECKPOINTS.json'
 assert hashlib.sha256(cp.read_bytes()).hexdigest()=='b0a31428609da72d9aef54606d61d47d2e22c2bd70dc9412df4f5b3ac7237991'
 rows={r['seed']:r for r in json.loads(cp.read_text())['rows'] if r['epoch']==200}
 words=list(itertools.islice(generate(),40000))
 assert len(words)==40000
 digest=hashlib.sha256(('\n'.join(''.join(map(str,w)) for w in words)+'\n').encode()).hexdigest()
 assert digest=='ecd2358998edb1ee8d611e25467d2e3ffe3f79065ca7f58e92b4afebff7a076e',digest
 expected={int(r['seed']):r['word'] for r in csv.DictReader((D/'WITNESSES.csv').open())}
 out=[]
 for seed in SEEDS:
  row=rows[seed];assert row['train_accuracy']==1.0
  w=find(row,words);assert w is not None
  assert ''.join(map(str,w))==expected[seed],seed
  a=verify(row,w);b=verify(row,w,True);c=independent(row,w)
  assert a==b==c and a[0],(seed,a,b,c)
  out.append({'seed':seed,'word':w,'length':len(w),'target':a[1],'prediction':a[2],'exact_checkers_agree':True})
  print('PASS',seed,len(w),flush=True)
 (D/'OUTCOMES.json').write_text(json.dumps(out,indent=2)+'\n')
 print('RUN248_PASS',len(out),'generator_sha256',digest)
if __name__=='__main__':main()
