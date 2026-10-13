from research.kernel_001.run134.reproduce import report
from research.kernel_001.run134.independent_check import verify
from research.kernel_001.run134.check_checkpoints import verify as verify_checkpoints

def test_run134_exact_gradient_transition():
    assert len(report())==16

def test_run134_independent_checker():
    r=verify()
    assert r['antecedent']==9 and r['history_spoofs_rejected_by_scope']==192

def test_run134_independent_checkpoint_reimplementation():
    assert verify_checkpoints()==16
