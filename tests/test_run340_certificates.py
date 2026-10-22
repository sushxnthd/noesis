import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research'/'run340'))
from cert340 import certificate,verify
from independent340 import check
D=ROOT/'research'/'run340'/'checkpoints'
def test_certified_endpoints():
 for seed in (29000,29034,29067,29091,29119):
  p=json.loads((D/f'{seed}_epoch200.json').read_text())['p']
  mask=certificate(p)
  assert mask is not None and verify(p,mask) and check(p,mask)
def test_known_bad_rejected():
 p=json.loads((D/'29177_epoch200.json').read_text())['p']
 assert certificate(p) is None
def test_spoof_rejected():
 p=[.9,0,0,0,0,0,0,0,0,-3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,-.3]
 assert certificate(p) is None
