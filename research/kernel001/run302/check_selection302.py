# Reproduce Run302 with supplied Run300 archive files.
import json,hashlib
from pathlib import Path
P=Path(__file__).parent
r=json.loads((P/'FROZEN_PROTOCOL302.json').read_text())
data=json.loads((P/'rows300.json').read_text())
assert len(r['selected_seeds'])==64
assert all(next(x for x in data if x['seed']==s)['outcome']=='unresolved' for s in r['selected_seeds'])
print('SELECTION_CHECK_PASS')
