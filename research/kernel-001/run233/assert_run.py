"""Frozen primary criterion, with unresolved checkpoints explicitly retained."""
import json,collections
from pathlib import Path
R=Path(__file__).parent
rows=json.load(open(R/'PROOFS.json'))['results']
by={(r['seed'],r['epoch']):r['status'] for r in rows}
trans=[s for s in range(2501,2605) if (s,0) in by and by[s,0]=='INCORRECT' and by[s,200]=='CORRECT']
persistent=[s for s in range(2501,2605) if (s,0) in by and by[s,0]==by[s,200]=='INCORRECT']
counts=dict(collections.Counter(r['status'] for r in rows))
controls=json.load(open(R/'CONTROLS.json'))
assert len(rows)==80 and len(controls)>=4
assert len(trans)>=3 and len(persistent)>=4,(trans,persistent,counts)
print('FROZEN_PASS',len(trans),'acquisitions',len(persistent),'persistent',counts)
(R/'SUMMARY.json').write_text(json.dumps(dict(transitions=trans,persistent=persistent,status_counts=counts,criterion='PASS'),indent=2)+'\n')
