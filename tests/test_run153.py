from fractions import Fraction
from research.kernel_001.run153.exact_witness import error
from research.kernel_001.run153.beam_search import search,neutral_control
def test_run153_exact_witnesses():
    cases=[(208,"0000000011111110000000000"),(210,"00000000000011111111"),(214,"0000000022")]
    for seed,word in cases:
        assert abs(error(seed,word))>Fraction(1,10)
def test_run153_new_beam_witnesses():
    for seed,depth in [(208,25),(210,20),(214,10)]:
        result=search(seed)
        assert result is not None and result['depth']==depth
        assert abs(error(seed,result['word']))>Fraction(1,10)
def test_run153_neutral_controls():
    for seed,depth in [(208,83),(210,28),(214,25)]:
        result=neutral_control(seed)
        assert result is not None and result['depth']==depth
        assert abs(error(seed,result['word']))>Fraction(1,10)
def test_run153_no_witness_is_inconclusive():
    for seed in (209,211,212,213,215):
        assert search(seed) is None
