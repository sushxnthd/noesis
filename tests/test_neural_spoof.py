from research.kernel_001.neural_spoof import exact_enumeration,neural_step
from research.kernel_001.independent_neural_check import certify
def test_independent_bfs_and_exhaustive_enumeration():
    for cap in range(1,11):
        a=exact_enumeration(cap)
        assert a["shortest_failure_length"]==certify(cap)==cap+1
        assert a["enumerated_sequences"]==2**(cap+1)-1
def test_recurrent_relu_saturation():
    assert neural_step(12,1,12)==12
    assert neural_step(12,-1,12)==11
