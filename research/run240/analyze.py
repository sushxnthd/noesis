"""Frozen ROC-AUC and abstention-aware pass/fail."""
import json,hashlib
from pathlib import Path
from sklearn.metrics import roc_auc_score
R=Path(__file__).parent
out=json.load(open(R/'PREDICTIONS.json'))
resolved=[r for r in out if r['final_status']!='ABSTAIN'];y=[int(r['final_status']=='CERTIFIED') for r in resolved]
def auc(key):
 return float(roc_auc_score(y,[r[key] for r in resolved])) if len(set(y))==2 else None
s=auc('score');t=auc('train_accuracy');c=auc('train_confidence')
coverage=len(resolved)/len(out)
primary=(coverage>=.70 and sum(y)>=3 and len(y)-sum(y)>=3 and s is not None and s>=.80 and s-t>=.15 and s-c>=.15)
summary=dict(frozen_primary_pass=primary,auc=s,training_accuracy_auc=t,confidence_auc=c,resolved=len(resolved),total=len(out),positive=sum(y),negative=len(y)-sum(y),coverage=coverage,auc_improvement_over_training=s-t if s is not None else None,auc_improvement_over_confidence=s-c if s is not None else None,counts={arm:{status:sum(r['arm']==arm and r['final_status']==status for r in out) for status in ('CERTIFIED','INCORRECT','ABSTAIN')} for arm in ('baseline','saturation')},training_checkpoint_sha256=hashlib.sha256((R/'CHECKPOINTS.json').read_bytes()).hexdigest())
(R/'ANALYSIS.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
