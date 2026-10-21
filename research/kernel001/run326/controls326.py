"""Gauge orbit control for the frozen Run326 predictor."""
import itertools,json
import numpy as np
from predictor326 import score
def gauge(p,perm,scales):
 p=np.asarray(p,float);a=p[:18].reshape(2,3,3);b=p[18:24].reshape(2,3);v=p[24:27]
 S=np.zeros((3,3));S[np.arange(3),perm]=scales;Si=np.linalg.inv(S)
 return np.concatenate([np.stack([S@a[x]@Si for x in (0,1)]).ravel(),
  np.stack([S@b[x] for x in (0,1)]).ravel(),v@Si,[p[27]]])
def main():
 raw=json.load(open('checkpoints326.json'));by={(r['seed'],r['epoch']):r for r in raw['rows']}
 p=by[24000,20]['p'];base=score(p);diffs=[]
 for perm in itertools.permutations(range(3)):
  for scales in ((1.,1.,1.),(.5,2.,4.),(3.,.25,1.5),(2.,5.,.1)):
   diffs.append(abs(score(gauge(p,perm,scales))-base))
 assert len(diffs)==24 and max(diffs)<1e-5
 print('GAUGE_CONTROL_PASSED',len(diffs),max(diffs))
 print('SPOOF_WARNING: finite separation is not a certificate; Run316 trained seed 22642 collides at length 11')
if __name__=='__main__':main()
