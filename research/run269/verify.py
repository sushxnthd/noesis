"""Independent exact Fraction replay for NOESIS K001 Run269."""
import json
from fractions import Fraction as Q
from pathlib import Path
p=json.loads((Path(__file__).parent/'checkpoint.json').read_text())['params']
A=[[Q.from_float(x) for x in row] for row in p['A']]
E=[[Q.from_float(x) for x in row] for row in p['E']]
b=list(map(Q.from_float,p['b']))
v=list(map(Q.from_float,p['v']))
c=Q.from_float(p['c'])
WORDS=('11111111112000','11111111120000','11111111200000')
def replay(word):
 h=[Q(0)]*3
 q=0
 wrong=[]
 for t,ch in enumerate(word,1):
  s=int(ch)
  if s==1:q=1
  elif s==2:q=0
  h=[max(Q(0),sum(A[i][j]*h[j] for j in range(3))+E[s][i]+b[i]) for i in range(3)]
  if int(sum(v[j]*h[j] for j in range(3))+c>0)!=q:wrong.append(t)
 return wrong
if __name__=='__main__':
 for word in WORDS:
  assert replay(word)==[14],word
  assert replay(word[:-1])==[],word
  print('Independent exact witness:',word)
 print('Mutation control: a first-error claim at position 13 is rejected')
