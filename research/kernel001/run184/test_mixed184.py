from research.kernel001.run184.mixed184 import certify
from research.kernel001.run184.mixed_independent184 import check

def test_exact_arbitrary_generator_compositions():
    p=certify()
    assert p['all_concatenations']
    assert p['sign_inequalities']==420 and p['output_inequalities']==60

def test_independent_four_block_enumeration():
    assert check()==81
