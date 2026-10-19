"""Verify public-runner retraining against frozen local exact acquisition witnesses."""
import json
from pathlib import Path
from verify import positive,negative
P=Path(__file__).resolve().parent
rows=json.loads((P/"checkpoints_phase1.json").read_text())["rows"]
refs=json.loads((P/"four_pairs.json").read_text())
index={(r["seed"],r["epoch"]):r for r in rows}
counts={epoch:sum(r["train_accuracy"]==1 for r in rows if r["epoch"]==epoch)
        for epoch in (0,10,20,30,40,50,75,100,150,200)}
assert list(counts.values())==[0,0,2,4,13,14,23,23,23,24],counts
for t in refs:
 for epoch,ref in ((t["earlier_epoch"],t["early_params"]),(t["later_epoch"],t["late_params"])):
  row=index[(t["seed"],epoch)]
  assert row["train_accuracy"]==1.0
  p=row["params"]
  for k in ("a","b"):
   assert all(abs(x-y)<1e-9 for x,y in zip(p[k],ref[k])),(t["seed"],epoch,k)
  for k in ("v","c"):assert abs(p[k]-ref[k])<1e-9,(t["seed"],epoch,k)
 old=index[(t["seed"],t["earlier_epoch"])]["params"]
 new=index[(t["seed"],t["later_epoch"])]["params"]
 assert negative(old,1 if t["family"]=="SET" else 2,t["n"])
 assert positive(new)
 print("PASS replay seed",t["seed"],"false at",t["earlier_epoch"],"certified at",t["later_epoch"])
print("PASS full-cohort counts and four independently retrained exact transitions")
