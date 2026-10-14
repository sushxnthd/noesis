from .certificate import run,load,power
from .independent_check import check

def test_exact_raw_matrix_stability():
 A,_,_=load()
 assert max(sum(abs(x) for x in row) for row in power(A,32))<1

def test_expanding_active_cone():
 assert run()["cone_expansion_epsilon"]>0

def test_exact_first_failure():
 assert run()["first_plus_error_gt_0.1"]==141

def test_independent():
 assert check()["first_plus_failure"]==141
