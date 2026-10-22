import json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent

def test_provenance():
 d=json.loads((P/'model344.json').read_text())
 assert d['seed']==31089
 assert d['source_sha256']=='c20f44b3bd56893880974c638b6202ad75a5ea253b64f72eeaa094e8d973112e'
 assert d['epochs']['141']['bce']<d['epochs']['140']['bce']
 assert d['epochs']['141']['accuracy']==d['epochs']['140']['accuracy']==1.

def test_support_parity():
 w=json.loads((P/'witness344.json').read_text())
 assert [s.count('1')%2 for s in w['words']]==w['labels']
 assert max(map(len,w['words']))==15 and len(w['words'])==5

def test_rational_weights():
 w=json.loads((P/'witness344.json').read_text())
 for epoch in ('141','200'):
  q=[F(int(z['num']),int(z['den'])) for z in w['epochs'][epoch]['weights']]
  assert all(z>0 for z in q)
  assert sum(q[:2])==sum(q[2:])==1

def test_exact_horizon():
 r=json.loads((P/'results344.json').read_text())
 assert r['epochs']['200']['exact_repairable_through_14']==32766
 assert r['epochs']['200']['exact_unrepairable_by_length_15']
 assert r['epochs']['140']['original_correct_through_12']==8190
 assert r['epochs']['141']['original_correct_through_12']==8190
