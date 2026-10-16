"""Independent directed-interval checker for the held-out Run198 checkpoint."""
import json
from pathlib import Path
from fractions import Fraction
from mpmath import iv
iv.dps=40
R=Path(__file__).resolve().parent
rows=json.loads((R/'CI_CHECKPOINTS.json').read_text())['rows']
p=next(x['params'] for x in rows if x['seed']==269 and x['epoch']==800)
def q(x):
 f=Fraction.from_float(float(x));return iv.mpf(f.numerator)/iv.mpf(f.denominator)
W=[[q(x) for x in v] for v in p['W']]
U=[[q(x) for x in v] for v in p['U']]
b=[q(x) for x in p['b']]
V=[[q(x) for x in v] for v in p['V']]
c=[q(x) for x in p['c']]
def step(h,bit):
 z=[sum((W[i][j]*h[j] for j in range(12)),U[bit][i]+b[i]) for i in range(12)]
 return [1-2/(1+iv.exp(2*x)) for x in z]
def classify(h):
 z=[sum((V[i][j]*h[j] for j in range(12)),c[i]) for i in range(3)]
 return [i for i in range(3) if all(i==j or bool((z[i]-z[j]).a>0) for j in range(3))]
count=0;wrong=[];ambiguous=[]
def walk(h,d,ones,word):
 global count
 if ones>3 or ones+15-d<3:return
 if d==15:
  count+=1;pred=classify(h)
  if len(pred)!=1:ambiguous.append(word)
  elif pred[0]!=0:wrong.append(word)
  return
 for bit in (0,1):walk(step(h,bit),d+1,ones+bit,word+str(bit))
walk([iv.mpf(0)]*12,0,0,'')
word='111001110011000'
h=[iv.mpf(0)]*12
for bit in word:h=step(h,int(bit))
pred=classify(h);true=word.count('1')%3
result={'seed':269,'epoch':800,'probe_checked':count,'probe_wrong':wrong,'probe_ambiguous':ambiguous,'witness':word,'true':true,'predicted':pred,'witness_wrong':len(pred)==1 and pred[0]!=true}
(R/'CI_INTERVAL.json').write_text(json.dumps(result,indent=1)+'\n')
assert count==455 and not wrong and not ambiguous and result['witness_wrong'],result
print(result)
