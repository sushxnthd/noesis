from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
P=Path(__file__).resolve().parent
C=P.parent/'run297'
raw=(C/'checkpoints297.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473'
ck={(r['seed'],r['epoch']):r for r in json.loads(raw)['rows']}
rows=json.loads((P/'rows298.json').read_text())
assert len(rows)==58
n=0
for row in rows:
 w=row['witness']
 if w is None:continue
 assert row['status']=='incorrect' and 13<=len(w['word'])<=256
 p=list(map(Q.from_float,ck[(row['seed'],80)]['p']))
 h=[Q(0)]*3;q=0;first=None
 for t,c in enumerate(w['word'],1):
  x=int(c);q|=x
  h=[max(Q(0),p[18+3*x+i]+sum(p[9*x+3*i+j]*h[j] for j in range(3))) for i in range(3)]
  z=p[27]+sum(p[24+i]*h[i] for i in range(3))
  if (z>0)!=bool(q):first=t;break
 assert first==w['first_exact_failure'] and first>=13
 n+=1
assert n==json.loads((P/'results298.json').read_text())['new_exact_wrong']
print('INDEPENDENT_EXACT_WITNESSES',n)
