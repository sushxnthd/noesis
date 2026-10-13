"""Frozen exact-rational recurrent-cap training and shortest witness search."""
import json,hashlib
from fractions import Fraction as Q
from pathlib import Path
from core import gd_step,shortest_zero_failure
from independent_check import verify
HERE=Path(__file__).parent
raw=(HERE/"PROTOCOL.json").read_bytes()
protocol=json.loads(raw)
rows=[]
for k in protocol["k_values"]:
    M=Q(k)-Q(2,3)
    witness=[1]*(k+1)+[-1]*k
    prefix=[1]*(k+1)
    Mf,lf,gf=gd_step(witness,M)
    Mp,lp,gp=gd_step(prefix,M)
    before=shortest_zero_failure(M)
    after=shortest_zero_failure(Mp)
    assert (before["length"],after["length"])==(2*k+1,2*k+3)
    assert (lf,gf,gp)==(Q(1),Q(0),Q(-10,3))
    assert Mp==Q(k)+Q(1,6)
    _,lb,gb=gd_step([1]*(k+1)+[-1]*(k+1),M)
    assert lb==gb==0
    rows.append({"k":k,"initial_cap":str(M),"shortest_before":before,
        "final_only_loss":str(lf),"final_only_gradient":str(gf),
        "final_only_cap":str(Mf),"prefix_loss":str(lp),
        "prefix_gradient":str(gp),"prefix_cap":str(Mp),
        "shortest_after_prefix":after,
        "balanced_final_loss":str(lb),"balanced_final_gradient":str(gb)})
results={"protocol_sha256":hashlib.sha256(raw).hexdigest(),
    "exact_arithmetic":"fractions.Fraction","rows":rows,
    "independent_verification":verify(rows),
    "claim":"The shortest zero-test witness has zero final-only cap gradient; prefix supervision shifts finite failure horizon +2, not to infinity."}
(HERE/"RESULTS.json").write_text(json.dumps(results,indent=2,sort_keys=True)+"\n")
print(json.dumps({"cases":len(rows),"independent":results["independent_verification"]}))
