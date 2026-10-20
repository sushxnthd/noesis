import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'research/kernel001/run302'
def test_frozen_cohort_and_witness_metadata():
 f=json.loads((ROOT/'FROZEN_PROTOCOL302.json').read_text())
 r=json.loads((ROOT/'witnesses302.json').read_text())
 selected=f['selected_seeds']
 assert len(selected)==len(set(selected))==64
 assert len(r['witnesses'])==r['new_exact_incorrect']==6
 assert not r['primary_pass']
 assert all(s in selected and n>12 for s,n,_ in r['witnesses'])
 assert r['still_unresolved']==58 if 'still_unresolved' in r else True
