from research.kernel_001.run134.reproduce import report
from research.kernel_001.run134.independent_check import verify

def test_run134_exact_gradient_transition():
    assert len(report())==16

def test_run134_independent_checker():
    r=verify()
    assert r['antecedent']==9 and r['history_spoofs_rejected_by_scope']==192
