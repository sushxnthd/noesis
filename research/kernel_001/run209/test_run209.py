import json,runpy,sys
from pathlib import Path
R=Path(__file__).resolve().parent
def test_frozen_seed_count():
 d=json.loads((R/'EPOCH800_COMPACT.json').read_text())
 assert len(d['rows'])==12
def test_interval_proof():
 sys.path.insert(0,str(R))
 runpy.run_path(str(R/'score.py'),run_name='__main__')
