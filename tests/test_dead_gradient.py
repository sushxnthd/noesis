from fractions import Fraction as F
from research.kernel_001.dead_gradient.core import gd_step,shortest_zero_failure

def test_dead_gradient_and_prefix_intervention():
    for k in range(3,15):
        M=F(k)-F(2,3)
        witness=[1]*(k+1)+[-1]*k
        prefix=[1]*(k+1)
        new,loss,grad=gd_step(witness,M)
        assert (new,loss,grad)==(M,F(1),F(0))
        shifted,loss2,grad2=gd_step(prefix,M)
        assert shifted==F(k)+F(1,6)
        assert grad2==F(-10,3)
        assert shortest_zero_failure(M)["length"]==2*k+1
        assert shortest_zero_failure(shifted)["length"]==2*k+3

def test_balanced_exposed_final_zero_gradient():
    for k in range(3,15):
        M=F(k)-F(2,3)
        _,loss,grad=gd_step([1]*(k+1)+[-1]*(k+1),M)
        assert loss==grad==0


def test_frozen_protocol_hash():
    import hashlib,json
    from pathlib import Path
    base=Path(__file__).resolve().parents[1]/"research/kernel_001/dead_gradient"
    assert hashlib.sha256((base/"PROTOCOL.json").read_bytes()).hexdigest()==json.loads((base/"RESULTS.json").read_text())["protocol_sha256"]
