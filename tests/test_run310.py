"""Lightweight Run310 mathematical regression; full 19-pair replay remains separate."""
import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'research'/'kernel001'/'run310'
def load(name):
    spec=importlib.util.spec_from_file_location(name,P/(name+'.py'))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_run310_synthetic_certificate():
    discover=load('experiment310')
    independent=load('independent310')
    p=[0.0]*28
    p[8]=1.0
    p[17]=1.0
    p[23]=1.0
    p[26]=1.0
    p[27]=-0.5
    cert=discover.cone_search(p)
    assert cert is not None
    assert independent.check(p,cert[0])
    broken=p.copy()
    broken[18]=1.0
    assert not independent.check(broken,cert[0])

def test_run310_exact_collision():
    discover=load('experiment310')
    independent=load('independent310')
    p=[0.0]*28
    hit=discover.collision(p)
    assert hit is not None
    assert independent.state(p,hit['negative'])==independent.state(p,hit['positive'])
