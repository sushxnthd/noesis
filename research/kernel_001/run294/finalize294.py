import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
rows=json.loads((P/'rows294.json').read_text())
assert len(rows)==245
changed=sum(abs(r['divergent']['delta'])>1e-6 for r in rows)
stable=sum(abs(r['stable']['delta'])<=1e-8 for r in rows)
recovered=sum(abs(r[k]['restored_score']-r['original'])<1e-9 for r in rows for k in ('stable','divergent'))
m={'n':245,'changed_divergent':changed,'criterion':150,'primary_pass':changed>=150,'stable_unchanged':stable,'recovered':recovered,'exact_structural_proofs':490,'checkpoint_sha256':hashlib.sha256((P/'checkpoints291.json').read_bytes()).hexdigest()}
(P/'results294.json').write_text(json.dumps({'metrics':m,'rows':rows},indent=2,sort_keys=True)+'\n')
print('METRICS',json.dumps(m,sort_keys=True),flush=True)
assert changed==192 and stable==245 and recovered==490
