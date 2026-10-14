"""Smoke tests for Run152 executable diagnostic (not 24-checkpoint verification)."""
import importlib.util,json
from pathlib import Path
from fractions import Fraction
HERE=Path(__file__).resolve().parents[1]
P=HERE/'research/kernel_001/run152'
spec=importlib.util.spec_from_file_location('noesis_run152_crossseed',P/'crossseed.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
def test_exact_reflected_counter():
    p={'A':[[1.]],'E':[[1.],[-1.],[0.]],'w':[1.]}
    assert module.exact(p,'001122')==Fraction(0)
    assert module.exact(p,'111000')==Fraction(0)
def test_perfect_counter_passes_full_depth():
    p={'A':[[1.]],'E':[[1.],[-1.],[0.]],'w':[1.]}
    r=module.evaluate(p)
    assert r['first_failure_le14'] is None
    assert r['depth14_max']==0.0
def test_retrospective_summary_boundaries():
    j=json.loads((P/'RESULTS_SUMMARY.json').read_text())
    assert len(j['records'])==24
    assert j['counts_failure_le14']=={'baseline':4,'latent':1,'output':3}
    assert 'retrospective' in j['protocol'].lower()
