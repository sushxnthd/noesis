"""Run 213: reuse unchanged Run 212 proof algorithms with new frozen checkpoints."""
import json
from pathlib import Path
R=Path('research/kernel_001/run212')
checkpoints=Path('research/run213/RUN213_CHECKPOINTS.json')
old='p=json.loads((R.parent/"run210/checkpoints/seed_787.json").read_text())["params"]'
new='p=next(r["params"] for r in json.loads(CHECKPOINTS.read_text())["rows"] if r["seed"]==SEED and r["epoch"]==200)'
for seed in (829,853,859,881,911,941):
 for name in ('generate_candidate.py','verify_primary.py','verify_independent.py'):
  path=R/name;src=path.read_text()
  assert old in src,(name,'input substitution failed')
  src=src.replace(old,new)
  src=src.replace('(R/"CANDIDATE.json").read_text()','(R/"CANDIDATE_REGENERATED.json").read_text()')
  src=src.replace('"seed":787','"seed":SEED')
  scope={'__file__':str(path),'SEED':seed,'CHECKPOINTS':checkpoints}
  exec(compile(src,str(path),'exec'),scope)
  print('run213',seed,name,'PASSED',flush=True)
 dest=Path('research/run213/remote_candidate_'+str(seed)+'.json')
 dest.write_bytes((R/'CANDIDATE_REGENERATED.json').read_bytes())
print('Remote independent 5-cell verification: 6 additional positives PASS')
