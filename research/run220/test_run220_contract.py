import json
from pathlib import Path
R=Path(__file__).parent
def test_frozen_run220_contract():
    p=(R/"FROZEN_DETAILS.txt").read_text()
    assert "1301" in p and "1483" in p
    assert "Adam" in p and "0.03" in p
    report=(R/"RESULTS.md").read_text()
    assert "INCONCLUSIVE" in report
    assert "1301, 1319, 1427, 1451" in report
    assert "0.000" in report
def test_learning_claim_not_overstated():
    learning=(R/"LEARNING_LEDGER.md").read_text()
    assert "18 unresolved" in learning
    assert "not publishable" in learning
