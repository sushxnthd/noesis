"""Run frozen in-family holdout; torch and numpy required."""
import json,hashlib
from pathlib import Path
from research.kernel_001.neural_spoof import exact_enumeration,train_control
p=Path(__file__).with_name("FROZEN_PREDICTION.json")
data=p.read_bytes()
assert hashlib.sha256(data).hexdigest()=="38b3f1dd56b18c800561f8a554612cc2243b7f2f237919c4331df5dbf692f5fe"
spec=json.loads(data)
exact=[exact_enumeration(c) for c in spec["holdout_caps"]]
trained=[train_control(s) for s in spec["holdout_seeds"]]
assert [r["shortest_failure_length"] for r in exact]==spec["predicted_shortest_failure_lengths"]
for r in trained:
    assert r["max_cap_gradient"]==0 and r["final_cap"]==12
    assert r["first_bad_length_le_14"]==13 and r["train_mse"]<1e-9
print(json.dumps({"all_predictions_passed":True,"exact":exact,"training":trained},indent=2))
