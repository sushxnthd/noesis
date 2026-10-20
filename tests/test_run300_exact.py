"""Independent exact regression on two fresh gradient-trained Run300 endpoints."""
import importlib.util,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
DATA=P/'research/kernel_001/run300/representative_witnesses.json'
CHECK=P/'research/kernel_001/run299/run299_public.py'
def verifier():
    spec=importlib.util.spec_from_file_location('run299_checker',CHECK)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
def test_run300_exact_positive():
    d=json.loads(DATA.read_text())['certified']
    assert d['seed']==22227
    assert verifier().independent(d['p'],d['certificate'])
def test_run300_exact_negative():
    d=json.loads(DATA.read_text())['incorrect']
    assert d['seed']==22201
    assert verifier().wrong(d['p'],d['witness'])
def test_run300_mutated_proof_rejected():
    d=json.loads(DATA.read_text())['certified']
    p=d['p'].copy()
    p[18]=0.1
    assert not verifier().independent(p,d['certificate'])
