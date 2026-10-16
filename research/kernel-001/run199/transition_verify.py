import json
from pathlib import Path
from mpmath import iv
from verify_core import q
iv.dps=70
def classify(p,w):
 W=[[q(v) for v in a] for a in p['W']]
 U=[[q(v) for v in a] for a in p['U']]
 V=[[q(v) for v in a] for a in p['V']]
 b=list(map(q,p['b']));c=list(map(q,p['c']))
 h=[iv.mpf(0)]*12
 for x in w:
  h=[2/(1+iv.exp(-2*(b[i]+U[int(x)][i]+sum(W[i][j]*h[j] for j in range(12)))))-1 for i in range(12)]
 z=[c[i]+sum(V[i][j]*h[j] for j in range(12)) for i in range(3)]
 return [i for i in range(3) if all(i==j or z[i].a>z[j].b for j in range(3))]
if __name__=='__main__':
 rows=json.loads((Path(__file__).parent/'CHECKPOINTS.json').read_text())['rows']
 for epoch,want in [(400,1),(800,2)]:
  row=next(x for x in rows if x['seed']==307 and x['epoch']==epoch)
  assert classify(row['params'],'1110001010100010')==[want]
 print('CERTIFIED_TRANSITION_PASS')
