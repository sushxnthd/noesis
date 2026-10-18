import json,math,statistics,hashlib,copy
from pathlib import Path
from collections import Counter
from verify import check as verify
from independent import check as independent
R=Path(__file__).parent
C=json.load(open(R/'CHECKPOINTS.json'))['rows'];E=json.load(open(R/'EXACT.json'))
rows={(x['dim'],x['seed'],x['arm'],x['epoch']):x for x in C}
exact={(x['dim'],x['seed'],x['arm'],x['epoch']):x for x in E}
out={}
for dim,seeds in [(3,range(3601,3625)),(4,range(3701,3713))]:
 d={'arms':{},'rescues':{},'paired':{}}
 for arm in ['baseline','saturation','confidence']:
  d['arms'][arm]=dict(counts=dict(Counter(exact[(dim,s,arm,200)]['status'] for s in seeds)),mean_accuracy=statistics.mean(rows[(dim,s,arm,200)]['train_accuracy'] for s in seeds),mean_abs_h=statistics.mean(rows[(dim,s,arm,200)]['mean_abs_h'] for s in seeds))
 for arm in ['saturation','confidence']:
  d['rescues'][arm]=[s for s in seeds if exact[(dim,s,'baseline',200)]['status']=='INCORRECT' and exact[(dim,s,arm,200)]['status']=='CERTIFIED']
  gains=[s for s in seeds if exact[(dim,s,'baseline',200)]['status']!='CERTIFIED' and exact[(dim,s,arm,200)]['status']=='CERTIFIED']
  losses=[s for s in seeds if exact[(dim,s,'baseline',200)]['status']=='CERTIFIED' and exact[(dim,s,arm,200)]['status']!='CERTIFIED']
  n=len(gains)+len(losses);p=sum(math.comb(n,k) for k in range(len(gains),n+1))/2**n if n else 1.
  d['paired'][arm]=dict(gains=gains,losses=losses,p=p)
 out[str(dim)]=d
out['frozen_primary_pass']=len(out['3']['rescues']['saturation'])>=3 and len(out['3']['rescues']['saturation'])-len(out['3']['rescues']['confidence'])>=2
out['checkpoint_sha256']=hashlib.sha256((R/'CHECKPOINTS.json').read_bytes()).hexdigest()
controls=[]
for row in C:
 if row['dim']!=3 or row['arm']!='saturation' or row['epoch']!=200:continue
 if exact[(3,row['seed'],'saturation',200)]['status']!='CERTIFIED':continue
 r=copy.deepcopy(row);r['params']['v']=[-x for x in r['params']['v']];r['params']['c']=-r['params']['c']
 a=verify(r);b=independent(r)
 controls.append(dict(seed=row['seed'],fraction=a,integer=b))
 if len(controls)==4:break
assert len(controls)==4 and all(a['fraction']['status']==a['integer']['status']=='INCORRECT' for a in controls)
(R/'CONTROLS.json').write_text(json.dumps(controls,indent=2)+'\n')
(R/'ANALYSIS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
