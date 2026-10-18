"""Exhaustive two-engine shortest-error proof for trained finite-horizon spoofs."""
import json
from pathlib import Path
from itertools import product
R=Path(__file__).parent
ns={'__name__':'proof_lib','__file__':str(R/'proof_check.py')}
s=(R/'proof_check.py').read_text()
exec(compile(s[:s.index('\nresults=[]')],str(R/'proof_check.py'),'exec'),ns)
def oracle(word):
 d=[t for t in word if t in (1,2)]
 return int(bool(d) and d[-1]==1)
out=[]
for seed,L,word in [(2507,7,(0,1,0,0,0,0,0)),(2508,8,(1,0,0,0,0,0,0,0))]:
 row=ns['ROWS'][seed,200];n=0
 for k in range(1,L):
  for w in product(range(3),repeat=k):
   for mode in ('iv','decimal'):
    r=ns['evaluate'](row,mode,w)
    assert r['q']==oracle(w) and r['correct'],(seed,w,mode,r)
   n+=1
 a=ns['evaluate'](row,'iv',word);b=ns['evaluate'](row,'decimal',word)
 assert a['q']==b['q']==oracle(word)==1 and a['wrong'] and b['wrong']
 out.append(dict(seed=seed,verified_shorter=n,first_wrong_length=L,witness=list(word),iv=a,decimal=b))
 print('PASS',seed,n,'shorter words; wrong length',L,flush=True)
(R/'FINITE_HORIZON_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
