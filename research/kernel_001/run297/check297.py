"""Run297 cross-platform audit: preserve all primary frozen fields and outcomes."""
import hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
assert hashlib.sha256((P/'checkpoints297.json').read_bytes()).hexdigest()=='620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473'
rows=json.loads((P/'FROZEN_EARLY_SCORES297.json').read_text())
primary=[{k:r[k] for k in ('seed','gauge_score','negative_bce','early_accuracy')} for r in rows]
raw=json.dumps(primary,sort_keys=True,separators=(',',':'))+'\n'
assert hashlib.sha256(raw.encode()).hexdigest()=='4778f083e08ef86bbed1f83317291d496c7d30607e6e215dc5fdff6bac0ae7da'
print('PRIMARY_SCORES_FROZEN',len(rows),hashlib.sha256(raw.encode()).hexdigest())
print('FULL_SCORES_HASH',hashlib.sha256((P/'FROZEN_EARLY_SCORES297.json').read_bytes()).hexdigest())
out=json.loads((P/'rows297_compact.json').read_text())
assert len(out)==128
assert sum(r['status']=='incorrect' for r in out)==70
assert sum(r['sampled_perfect'] for r in out)==63
assert sum(r['status']=='incorrect' and r['sampled_perfect'] for r in out)==5
print('OUTCOME_COUNTS_RECHECKED')
