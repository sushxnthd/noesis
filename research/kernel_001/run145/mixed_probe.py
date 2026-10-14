"""Exploratory non-certifying mixed-word Pareto-frontier search.

Float64 pruning is not a proof. If interrupted, no minimality claim.
Run: python mixed_probe.py (may be slow beyond depth 80).
"""
import json,collections
from pathlib import Path
import numpy as np
p=json.loads((Path(__file__).resolve().parent/'CHECKPOINT.json').read_text())['parameters']
A=np.array(p['A'])[:2,:2];E=np.array(p['E'])[:,:2];w=np.array(p['w'])[:2]
states={0:[(0.,0.,'')]}
for n in range(1,142):
 nxt=collections.defaultdict(list)
 for q,ss in states.items():
  for a,b,word in ss:
   for t,u in enumerate((1,-1,0)):
    h=np.maximum(0,A@np.array([a,b])+E[t])
    nxt[max(0,q+u)].append((float(h[0]),float(h[1]),word+str(t)))
 states={}
 for q,ss in nxt.items():
  hi=[];v=-float('inf')
  for s in sorted(ss,key=lambda z:(-z[0],-z[1])):
   if s[1]>v:hi.append(s);v=s[1]
  lo=[];v=float('inf')
  for s in sorted(ss,key=lambda z:(z[0],z[1])):
   if s[1]<v:lo.append(s);v=s[1]
  states[q]=list({s[:2]:s for s in hi+lo}.values())
 best=max((abs(w@np.array([a,b])-q),q,word) for q,ss in states.items() for a,b,word in ss)
 if n<=15 or n%10==0 or best[0]>.1:print(n,sum(map(len,states.values())),best,flush=True)
 if best[0]>.1:break
