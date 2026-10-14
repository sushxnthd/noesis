from fractions import Fraction
from research.kernel_001.run153.exact_witness import error
def test_run153_exact_witnesses():
    cases=[(208,"0000000011111110000000000"),(210,"00000000000011111111"),(214,"0000000022")]
    for seed,word in cases:
        assert abs(error(seed,word))>Fraction(1,10)
def test_run153_known_margins():
    assert abs(float(error(208,"0000000011111110000000000")))-.1>.002
    assert abs(float(error(210,"00000000000011111111")))-.1>.006
