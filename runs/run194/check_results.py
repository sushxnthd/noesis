"""Validate Run 194 reproduction without assuming identical training environments."""
import json
from pathlib import Path
r=json.loads(Path(__file__).with_name('CI_RESULTS.json').read_text())
assert [x['seed'] for x in r['rows']]==[137,139,149,151]
for x in r['rows']:
    b=x['beam']
    assert b['evaluations']==sum(b['per_depth'])
    assert len(x['baseline_witnesses'])==100
    assert b['evaluations']<=2430
    if b['witness']:
        assert len(b['witness'])==b['depth']
        assert x['interval_signs'] in ([1,-1],[-1,1])
    else:
        assert x['interval_signs'] is None
print('Run 194 independent checks passed')
