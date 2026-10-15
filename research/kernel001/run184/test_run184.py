from research.kernel001.run184.proof184 import prove
from research.kernel001.run184.independent184 import check

def test_exact_cyclic_clocks():
    assert prove()==[None,186,87,57,87,186,None,186,None,148]

def test_independent_replay():
    assert check()==prove()
