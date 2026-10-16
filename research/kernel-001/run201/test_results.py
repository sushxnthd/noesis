#!/usr/bin/env python3
"""Frozen exact criterion and independent proof-output agreement."""
import json,hashlib
from pathlib import Path
p=Path(__file__).parent
a=json.loads((p/'PRIMARY_RESULTS.json').read_text())
b=json.loads((p/'INDEPENDENT_RESULTS.json').read_text())
sha=hashlib.sha256((p/'CHECKPOINTS.json').read_bytes()).hexdigest()
assert sha=='5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32'
assert a['source_sha256']==b['checkpoint_sha256']==sha
assert a['frozen_protocol_commit']=='448ef7e285b29e7f3ab7e5e0f03c4751e11ba712'
assert len(a['comparisons'])==30
assert a['primary_count']==b['independent_decimal_primary_count']==26
for s,x in a['comparisons'].items():
    truth=s.count('1')%3
    assert x['truth']==truth and x['epoch400']==truth and x['epoch800']==(truth+1)%3
    for epoch in ('400','800'):
        v=a['raw_phases'][epoch][s]
        assert len(v['phase_classes'])==14
        assert all(c==x['epoch'+epoch] for c in v['phase_classes'])
        assert b['epochs'][epoch]['suffixes'][s]['class']==x['epoch'+epoch]
print('RUN201 FROZEN CRITERION AND INDEPENDENT CROSS-CHECK PASS')
