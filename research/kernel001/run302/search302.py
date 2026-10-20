import json,hashlib
from pathlib import Path
from scan302 import search_one
P=Path(__file__).parent
f=json.loads((P/'FROZEN_PROTOCOL302.json').read_text())
raw=(P/'checkpoints300_late.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='71f384d19e4e5ae95198b6bce2ec35f29f547b166ba293ffae60fe8a2d2d6f8d'
models={r['seed']:r['p'] for r in json.loads(raw)['rows']}
found=[]
for seed in f['selected_seeds']:
 r=search_one(models[seed])
 if r:found.append((seed,r[0],len(r[1])))
print('WITNESSES',sorted(found))
assert len(found)==6
