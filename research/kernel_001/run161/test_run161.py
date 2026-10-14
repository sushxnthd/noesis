"""Run161 exact obstruction tests; archived cohort is optional in generic CI."""
import os
from pathlib import Path
from fractions import Fraction
from audit161 import SEEDS,evaluate
from independent161 import evaluate as independently

def test_cohort():
    assert SEEDS==(224,)+tuple(range(226,239))

def test_exact_agreement():
    folder=Path(os.environ.get("NOESIS_RUN161_CHECKPOINTS","research/kernel_001/run161/checkpoints"))
    if not (folder/"CHECKPOINT_SEED_224.json").exists():
        import pytest
        pytest.skip("archived Run154B checkpoints are downloaded by dedicated workflow")
    a=evaluate(folder); b=independently(folder)
    assert a["denominator"]==14 and len(b)==14
    for x,y in zip(a["outcomes"],b):
        assert x["seed"]==y["seed"] and x["sha256"]==y["sha256"]
        assert Fraction(x["min_diagonal_gap"])==Fraction(y["min_diagonal_gap"])
        assert x["structurally_eligible_coordinates"]==y["structural"]
        assert not x["certified"] or bool(y["unit"])
