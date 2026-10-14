"""Is the first adversarial witness entering unseen ReLU activation masks?"""
import itertools,json
import numpy as np
from .beam_search import load
def mask_novelty(seed,word):
 p=load(seed);A=np.asarray(p['A']);E=np.asarray(p['E'])
 seen=set()
 for prefix in itertools.product(range(3),repeat=6):
  h=np.zeros(4)
  for a in prefix:
   h=np.maximum(0,A@h+E[a]);seen.add(tuple(map(int,h>0)))
 h=np.zeros(4);novel=[]
 for t,a in enumerate(map(int,word),1):
  h=np.maximum(0,A@h+E[a])
  if tuple(map(int,h>0)) not in seen:novel.append(t)
 return {'training_masks':len(seen),'novel_positions':novel}
if __name__=='__main__':
 for seed,word in [(208,'0000000011111110000000000'),(210,'00000000000011111111'),(214,'0000000022')]:
  print(seed,mask_novelty(seed,word))
