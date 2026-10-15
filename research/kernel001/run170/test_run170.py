"""Run170 certificate and independent checker on stored trained checkpoint."""
import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
CP=ROOT.parent/'run169'/'checkpoints'/'w3_seed406.json'
def test_exact():
 p=subprocess.run([sys.executable,str(ROOT/'run170_cert.py'),str(CP)],capture_output=True,text=True,check=True)
 x=json.loads(p.stdout)
 assert x['first_failure_cycle']==7901 and x['all_masks_proven'] and x['strict_monotonicity_proven']
def test_independent():
 p=subprocess.run([sys.executable,str(ROOT/'run170_independent.py'),str(CP)],capture_output=True,text=True,check=True)
 x=json.loads(p.stdout)
 assert x['first_failure']==7901 and x['mask_changes']==0
