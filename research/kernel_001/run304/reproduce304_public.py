#!/usr/bin/env python3
"""NOESIS K001 Run304: exact paired-checkpoint audit."""
import json,itertools,hashlib
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
SEEDS=(22227,22246,22272,22281,22311,22340,22349,22354,22389,22390,22403,22416,22417,22424,22438,22540,22567,22580)
def unpack(p):
 a=[Q.from_float(float(z)) for z in p]
 assert len(a)==28
 return ([[[a[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)],[[a[18+3*x+i] for i in range(3)] for x in (0,1)],a[24:27],a[27])
def certificate(p):
 A,b,v,c=unpack(p)
 if c>=0 or any(z>0 for z in b[0]) or any(z<0 for z in v) or not any(v):return None
 lo,hi=max(Q(0),-c),sum(v[i]*max(Q(0),b[1][i]) for i in range(3));mus=[]
 for x in (0,1):
  q=[sum(v[i]*A[x][i][j] for i in range(3)) for j in range(3)]
  if any(v[j]==0 and q[j]<0 for j in range(3)):return None
  mu=min(q[j]/v[j] for j in range(3) if v[j]>0)
  if mu<0:return None
  mus.append(mu);beta=sum(v[i]*b[x][i] for i in range(3))
  if mu==1:
   if beta<0:return None
  elif mu>1:lo=max(lo,-beta/(mu-1))
  else:hi=min(hi,beta/(1-mu))
 if lo>hi or hi<=-c or hi<=0:return None
 return {'T':str(hi),'mu':[str(z) for z in mus]}
def hidden_score(A,b,v,word):
 h=[Q(0)]*3
 for x in word:h=[max(Q(0),sum(A[x][i][j]*h[j] for j in range(3))+b[x][i]) for i in range(3)]
 return sum(v[i]*h[i] for i in range(3))
def audit_early(p):
 A,b,v,c=unpack(p);mx=None;mn=None;wrong=None
 for n in range(1,7):
  for w in itertools.product((0,1),repeat=n):
   s=hidden_score(A,b,v,w);y=bool(any(w))
   if (s+c>0)!=y and wrong is None:wrong=''.join(map(str,w))
   if y:mn=s if mn is None else min(mn,s)
   else:mx=s if mx is None else max(mx,s)
 return wrong,mx<mn
def main():
 raw=(P.parent/'run300'/'checkpoints300_repro.json').read_bytes()
 by={(r['seed'],r['epoch']):r for r in json.loads(raw)['rows']}
 assert len(by)>=768
 selected=[];rows=[]
 for seed in SEEDS:
  e=by[seed,20];l=by[seed,80];proof=certificate(l['p'])
  assert proof is not None,('missing exact certificate',seed)
  wrong,rescue=audit_early(e['p'])
  selected.append({'seed':seed,'epoch20':e,'epoch80':l})
  rows.append({'seed':seed,'early_witness':wrong,'epoch80_certificate':proof,'bias_only_len6_rescue':rescue})
 summary={'run':304,'selected':len(rows),'exact_transition_pairs':sum(r['early_witness'] is not None for r in rows),'bias_only_len6_rescue':sum(r['bias_only_len6_rescue'] for r in rows),'retrospective':True,'frozen_primary_pass':sum(r['early_witness'] is not None for r in rows)>=12,'source_reproduction_sha256':hashlib.sha256(raw).hexdigest()}
 (P/'selected_checkpoints304.json').write_text(json.dumps(selected,sort_keys=True,separators=(',',':'))+'\n')
 (P/'results304.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2,sort_keys=True)+'\n')
 print('RUN304',json.dumps(summary,sort_keys=True),flush=True)
 assert summary['selected']==18 and summary['exact_transition_pairs']==18 and summary['bias_only_len6_rescue']==12
if __name__=='__main__':main()
