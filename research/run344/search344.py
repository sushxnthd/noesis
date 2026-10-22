#!/usr/bin/env python3
"""Numerical LP discovery provenance only. All scientific claims require run344.py exact proof."""
from pathlib import Path
import json,numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
p=np.array(json.loads((P.parent/'run343/model343.json').read_text())['p'])
A=p[:32].reshape(2,4,4);b=p[32:40].reshape(2,4)
h=np.zeros((1,4));y=np.zeros(1,dtype=np.int8);HH=[];YY=[];records=[]
for length in range(1,16):
 h=np.stack([np.maximum(h@A[x].T+b[x],0) for x in (0,1)],axis=1).reshape(-1,4)
 y=np.stack([y,1-y],axis=1).reshape(-1)
 HH.append(h);YY.append(y)
 if length in (12,13,14,15):
  H=np.concatenate(HH);Y=np.concatenate(YY)
  scale=np.maximum(np.max(np.abs(H),axis=0),1.)
  V=np.column_stack((H/scale,np.ones(len(H))))
  M=np.where(Y[:,None]==1,-V,V)
  res=linprog(np.zeros(5),A_ub=M,b_ub=np.full(len(Y),-1.),bounds=[(None,None)]*5,method='highs')
  records.append({'length':length,'n_words':len(Y),'strict_lp_feasible_numeric':bool(res.success),'solver_status':int(res.status),'message':res.message})
out={'source':'run343/model343.json','solver':'scipy.optimize.linprog(method=highs)','claim_boundary':'LP exploratory; only exact proof is authoritative','rows':records}
(P/'search344_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
