from pathlib import Path
import json,sys
P=Path(__file__).resolve().parents[1]/'research'/'kernel001'/'run322'
sys.path.insert(0,str(P))
from run322 import parse,step,audit
from fractions import Fraction as F

def test_original_checkpoint_tail_failures():
 data=json.loads((P/'witness_checkpoints.json').read_text())
 for seed,n in [('22601',22),('22643',23)]:
  p=data[seed]
  a=audit(p)
  assert a['first_error']['n']==n and a['first_error']['class']==0
  A,b,w,c=parse(p)
  h=(F(0),)*3
  for t in range(1,n+1):
   h=step(h,A,b,0)
   s=sum((w[i]*h[i] for i in range(3)),c)
   assert (s>0)==(t==n)

def test_negative_controls():
 data=json.loads((P/'witness_checkpoints.json').read_text())
 for seed,n in [('22601',22),('22643',23)]:
  A,b,w,c=parse(data[seed])
  h=(F(0),)*3
  for t in range(1,n+1):h=step(h,A,b,0)
  s=sum((w[i]*h[i] for i in range(3)),c)
  assert s>0 and s-F(1,2**80)>0
