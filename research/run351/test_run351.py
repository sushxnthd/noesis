"""Run351 regression checks; dedicated workflow generates outputs before pytest."""
import json
from pathlib import Path
import pytest
R=Path(__file__).parent
requires_outcomes=pytest.mark.skipif(not (R/'outcomes.json').exists(),reason='requires Run351 reproduction outputs')
requires_exact=pytest.mark.skipif(not (R/'exact_outcomes.json').exists(),reason='requires independent exact reproduction')
@requires_outcomes
def test_frozen_negative_transfer():
 d=json.loads((R/'outcomes.json').read_text())
 assert len(d['rows'])==64 and d['eligible']==29 and d['N']==0
 assert sum(r.get('gain18',0)>0 for r in d['rows'])==1
 assert sum(r.get('gain18',0)<0 for r in d['rows'])==4
@requires_exact
def test_exact_audits():
 d=json.loads((R/'exact_outcomes.json').read_text())
 assert len(d['audits'])==12
 assert d['adversarial_word']=='01110101010'
 assert d['adversarial_logit_positive_exact']
@requires_outcomes
def test_strongest_other_coordinates():
 d=json.loads((R/'outcomes.json').read_text())
 assert next(r for r in d['rows'] if r['seed']==32034)['best']==[8]
 assert next(r for r in d['rows'] if r['seed']==32046)['best']==[17]
