#!/usr/bin/env python3
"""Frozen Run203: reachable quotient counterexample screen."""
import hashlib,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'CHECKPOINTS.json'
SHA='5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32'
def find(row,max_len=14):
 p={k:np.asarray(v,dtype=np.float64) for k,v in row['params'].items()}
 width=len(p['b']);h=np.zeros((1,width));seen={};best=None;counts=[]
 def advance(h,a):return np.tanh(h@p['W'].T+p['U'][a]+p['b'])
 def classify(h):
  z=h@p['V'].T+p['c'];y=np.argmax(z,axis=1)
  m=z[np.arange(len(z)),y]-np.partition(z,-2,axis=1)[:,-2]
  return y,m
 def one(w):
  h=np.zeros((1,width))
  for a in w:h=advance(h,int(a))
  y,m=classify(h)
  return {'word':w,'predicted':int(y[0]),'truth':w.count('1')%3,'margin':float(m[0]),'correct':int(y[0])==w.count('1')%3}
 for length in range(1,max_len+1):
  h=np.stack((advance(h,0),advance(h,1)),axis=1).reshape((-1,width))
  y,m=classify(h);y0,m0=classify(advance(h,0));y1,m1=classify(advance(h,1))
  counts.append({'length':length,'n':len(h),'min_output_margin':float(min(m.min(),m0.min(),m1.min()))})
  candidates=[]
  for n in range(len(h)):
   u=format(n,f'0{length}b')
   for a,yn in ((0,int(y0[n])),(1,int(y1[n]))):
    key=(int(y[n]),a);bynext=seen.setdefault(key,{})
    for oldy,v in bynext.items():
     if oldy!=yn:
      aa,bb=sorted((u,v))
      candidates.append((max(len(aa),len(bb)),len(aa)+len(bb),aa,bb,str(a)))
    bynext.setdefault(yn,u)
  if candidates:
   _,_,u,v,a=min(candidates);four=[one(w) for w in (u,v,u+a,v+a)]
   assert four[0]['predicted']==four[1]['predicted']
   assert four[2]['predicted']!=four[3]['predicted']
   best={'u':u,'v':v,'symbol':a,'max_prefix_length':max(len(u),len(v)),'total_prefix_length':len(u)+len(v),'four_words':four}
   break
 return {'seed':row['seed'],'epoch':row['epoch'],'max_length':max_len,'screen_counts':counts,'witness':best}
if __name__=='__main__':
 assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SHA
 rows=json.loads(SOURCE.read_text())['rows']
 result=[find(next(r for r in rows if (r['seed'],r['epoch'])==(307,e))) for e in (400,800)]
 (ROOT/'SCREEN203.json').write_text(json.dumps(result,indent=2)+'\n')
 print([(r['seed'],r['epoch'],r['witness']) for r in result])
