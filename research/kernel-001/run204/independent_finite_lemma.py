"""Exact combinatorial enumeration of all 3**6 short classifiers."""
from itertools import product
WORDS=("0","1","00","01","10","11")
def enumerate_all():
 n=0;violations=0;perfect=0
 for values in product(range(3),repeat=len(WORDS)):
  n+=1;f=dict(zip(WORDS,values))
  correct=all(f[w]==w.count("1")%3 for w in WORDS)
  if correct:perfect+=1
  bad=any(f[u]==f[v] and f[u+a]!=f[v+a] for u in ("0","1") for v in ("0","1") for a in "01")
  if bad:
   violations+=1
   assert not correct
 assert (n,perfect)==(729,1)
 return {"classifiers":n,"perfect":perfect,"quotient_violations":violations,"violations_with_perfect_labels":0}
if __name__=="__main__":print(enumerate_all())
