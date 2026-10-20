#!/usr/bin/env python3
"""Independent exact average-rank verification, separate from pairwise AUC."""
import json,sys
from fractions import Fraction
from pathlib import Path
def auc(rows,pos,key):
 a=sorted(rows,key=lambda r:(r[key],r['seed']));s=Fraction(0);i=0
 while i<len(a):
  j=i+1
  while j<len(a) and a[j][key]==a[i][key]:j+=1
  s+=Fraction(i+1+j,2)*sum(r['seed'] in pos for r in a[i:j]);i=j
 p=len(pos);return (s-Fraction(p*(p+1),2))/(p*(len(a)-p))
def check(rows,result):
 known={r['seed'] for r in rows if r['outcome']=='correct'}
 unknown=[r for r in rows if r['outcome']=='unresolved']
 for name,part in [('resolved',[r for r in rows if r['outcome']!='unresolved']),('sampled_perfect_resolved',[r for r in rows if r['outcome']!='unresolved' and r['epoch80_accuracy']==1.0])]:
  for key in ('gauge_score','negative_bce'):
   assert auc(part,known,key)==Fraction(result[name][key]['fraction']),(name,key)
 for name,sortkey in [('G','gauge_score'),('L','negative_bce')]:
  chosen={r['seed'] for r in sorted(unknown,key=lambda r:(-r[sortkey],r['seed']))[:40]}
  assert sorted(chosen)==result['completions'][name]['hypothetical_positive_seeds']
  for key in ('gauge_score','negative_bce'):
   assert auc(rows,known|chosen,key)==Fraction(result['completions'][name]['scores'][key]['fraction']),(name,key)
 print('INDEPENDENT301: eight exact rank-sum checks PASSED')
if __name__=='__main__':
 check(json.loads(Path(sys.argv[1]).read_text()),json.loads(Path(sys.argv[2]).read_text()))
