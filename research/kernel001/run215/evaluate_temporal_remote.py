"""Run215 remote AUROC reproduction on independently regenerated parameters."""
import json,itertools
from pathlib import Path
P=Path('research/run214')
d=json.loads((P/'RUN214_REMOTE_EVALUATION.json').read_text())
rows={r['seed']:r for r in d['rows']}
trans=[1019,1063,1087,1171]
persist=[1009,1013,1049,1061,1069,1093,1123,1151]
sub=trans+persist
def auc(key):
 a=[rows[s][key] for s in trans];b=[rows[s][key] for s in persist]
 return sum((x>y)+.5*(x==y) for x in a for y in b)/(len(a)*len(b))
scores={k:auc(k) for k in ['generic_prefix','generic_final','retention','negative_loss','negative_heldout_errors']}
assert abs(scores['generic_prefix']-.75)<1e-9,scores
assert abs(scores['negative_loss']-.59375)<1e-9,scores
print(json.dumps({'transitions':trans,'persistent_failures':persist,'auroc':scores},indent=2))
