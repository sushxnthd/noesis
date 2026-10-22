import json,numpy as np
from pathlib import Path
from score342 import deficit,auc
P=Path(__file__).resolve().parent
rows=json.loads((P/'trajectories342.json').read_text())['rows']
early={r['seed']:r for r in rows if r['epoch']==30};late={r['seed']:r for r in rows if r['epoch']==200}
seeds=sorted(early);N=len(seeds);W=4
p=np.array([late[s]['p'] for s in seeds]);a=p[:,:32].reshape(N,2,W,W);b=p[:,32:40].reshape(N,2,W);v=p[:,40:44];c=p[:,44]
states=np.zeros((N,1,W));par=np.array([0],dtype=np.int8)
first=[None]*N;min_abs=np.full(N,np.inf);correct=np.ones(N,dtype=bool);ambiguous=np.zeros(N,dtype=bool)
for length in range(1,13):
 s0=np.maximum(np.einsum('nij,nkj->nki',a[:,0],states)+b[:,None,0,:],0)
 s1=np.maximum(np.einsum('nij,nkj->nki',a[:,1],states)+b[:,None,1,:],0)
 states=np.stack((s0,s1),axis=2).reshape(N,-1,W)
 par=np.stack((par,1-par),axis=1).reshape(-1)
 logits=np.einsum('nkj,nj->nk',states,v)+c[:,None]
 bad=(logits>0)!=(par[None,:]==1)
 min_abs=np.minimum(min_abs,np.min(abs(logits),axis=1))
 ambiguous|=np.any(abs(logits)<=1e-9,axis=1)
 for i in range(N):
  if first[i] is None and np.any(bad[i]):
   j=int(np.flatnonzero(bad[i])[0]);first[i]={'length':length,'word':format(j,f'0{length}b'),'logit_numpy':float(logits[i,j]),'expected':int(par[j])}
 correct&=~np.any(bad,axis=1)
obs=[]
for i,s in enumerate(seeds):
 e=early[s];score=-deficit(e['p'])
 obs.append({'seed':s,'epoch30_score':score,'epoch30_bce':e['bce'],'epoch200_train_accuracy':late[s]['accuracy'],'correct_through_12':bool(correct[i]),'ambiguous':bool(ambiguous[i]),'min_abs_logit':float(min_abs[i]),'endpoint_label':int(correct[i] and not ambiguous[i]),'first_failure':first[i]})
pos=[x for x in obs if x['endpoint_label']];neg=[x for x in obs if not x['endpoint_label']]
ad=auc([x['epoch30_score'] for x in pos],[x['epoch30_score'] for x in neg]);al=auc([-x['epoch30_bce'] for x in pos],[-x['epoch30_bce'] for x in neg]);delta=ad-al
metrics={'n':N,'n_positive':len(pos),'n_negative':len(neg),'n_ambiguous':int(sum(ambiguous)),'deficit_auc':ad,'loss_auc':al,'delta_auc':delta,'frozen_success':len(pos)>=10 and len(neg)>=10 and delta>=.05}
(P/'outcomes342.json').write_text(json.dumps({'metrics':metrics,'rows':obs},indent=2)+'\n')
print(json.dumps(metrics,indent=2))
