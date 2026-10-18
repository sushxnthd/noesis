import sys,json,math,copy
from pathlib import Path
from collections import Counter
R=Path(__file__).parent
sys.path.insert(0,str(R.parent/'run238'))
from verify import check as check_a
from independent import check as check_b
C=json.load(open(R/'CHECKPOINTS.json'))['rows']
rows={(r['seed'],r['arm'],r['epoch']):r for r in C}
assert len(rows)==384
arms=('baseline','saturation','confidence','anti_saturation')
E={}
for seed in range(4101,4125):
 for arm in arms:
  for epoch in (0,200):
   row=rows[seed,arm,epoch];a=check_a(row);b=check_b(row)
   assert a['status']==b['status']
   assert a['status']!='CERTIFIED' or a['states']==b['states']
   assert a['status']!='INCORRECT' or a['witness']==b['witness']
   E[seed,arm,epoch]=a
   print(seed,arm,epoch,a['status'],flush=True)
(R/'EXACT.json').write_text(json.dumps([dict(seed=s,arm=a,epoch=e,**v) for (s,a,e),v in E.items()],indent=2))
rescues=[s for s in range(4101,4125) if E[s,'saturation',200]['status']=='CERTIFIED' and all(E[s,a,200]['status']=='INCORRECT' for a in arms if a!='saturation') and all(rows[s,a,200]['train_accuracy']==1.0 for a in arms)]
gains=[s for s in range(4101,4125) if E[s,'baseline',200]['status']!='CERTIFIED' and E[s,'saturation',200]['status']=='CERTIFIED']
losses=[s for s in range(4101,4125) if E[s,'baseline',200]['status']=='CERTIFIED' and E[s,'saturation',200]['status']!='CERTIFIED']
n=len(gains)+len(losses);p=sum(math.comb(n,k) for k in range(len(gains),n+1))/2**n if n else 1.
manip=[s for s in range(4101,4125) if rows[s,'saturation',200]['mean_abs_h']>rows[s,'anti_saturation',200]['mean_abs_h']]
controls=[]
for s in range(4101,4125):
 if E[s,'saturation',200]['status']=='CERTIFIED':
  r=copy.deepcopy(rows[s,'saturation',200]);r['params']['v']=[-x for x in r['params']['v']];r['params']['c']=-r['params']['c']
  a=check_a(r)['status'];b=check_b(r)['status']
  controls.append((s,a,b))
  if len(controls)==4:break
passed=len(rescues)>=2 and p<=.05 and len(manip)>=18 and len(controls)==4 and all(a!='CERTIFIED' and b!='CERTIFIED' for _,a,b in controls)
result=dict(frozen_primary_pass=passed,rescues=rescues,gains=gains,losses=losses,sign_p=p,manipulation_count=len(manip),controls=controls,independent_agreement=len(E),counts={a:dict(Counter(E[s,a,200]['status'] for s in range(4101,4125))) for a in arms})
(R/'ANALYSIS.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
