"""Run 209 frozen seeds; use exact Run 206 trainer from canonical repository."""
import json, sys
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/"run206"))
import train
SEEDS=(659,661,673,677,683,691,701,709,719,727,733,739)
def main():
    rows=[]
    for seed in SEEDS:
        rows.extend(train.train(seed))
        row=rows[-1]
        print(seed,row["loss"],row["train_accuracy"],row["heldout256"]["errors"],flush=True)
    (R/"RUN209_CHECKPOINTS.json").write_text(json.dumps({"seeds":SEEDS,"epochs":train.EPOCHS,"rows":rows},indent=2)+"\n")
if __name__=="__main__":main()
