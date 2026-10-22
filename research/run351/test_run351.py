"""NOESIS Run351 regression checks; run after reproduction."""
import json
from pathlib import Path
R=Path(__file__).parent
def test_frozen_negative_transfer():
 d=json.loads((R/'outcomes.json').read_text())
 assert len(d['rows'])==64 and d['eligible']==29 and d['N']==0
 assert sum(r.get('gain18',0)>0 for r in d['rows'])==1
 assert sum(r.get('gain18',0)<0 for r in d['rows'])==4
def test_exact_audits():
 d=json.loads((R/'exact_outcomes.json').read_text())
 assert len(d['audits'])==12
 assert d['adversarial_word']=='01110101010'
 assert d['adversarial_logit_positive_exact']
def test_strongest_other_coordinates():
 d=json.loads((R/'outcomes.json').read_text())
 assert next(r for r in d['rows'] if r['seed']==32034)['best']==[8]
 assert next(r for r in d['rows'] if r['seed']==32046)['best']==[17]
