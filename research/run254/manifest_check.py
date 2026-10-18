#!/usr/bin/env python3
# Run254 exact-certificate replay entrypoint. The complete archive includes
# independent_exact_checker.py and EXACT_DUAL_CERTIFICATE.json.
import json
from pathlib import Path
p=Path(__file__).resolve().parent
f=p/'EXACT_DUAL_CERTIFICATE.json'
if not f.exists():
    raise SystemExit('BLOCKED: exact dual certificate missing from public branch')
c=json.loads(f.read_text())
assert c['run']==254 and c['counts']=={'feasible':32,'infeasible':352,'facets':686}
print('Manifest loaded; execute independent_exact_checker.py for proof, not this manifest test')
