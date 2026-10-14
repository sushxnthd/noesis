import sys
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"research"/"kernel_001"/"run151"))
from global_horizon import check
from independent_exact import exact_witness
import json

P=Path(__file__).resolve().parents[1]/"research"/"kernel_001"/"run151"/"checkpoints"

def test_first_failures():
    for variant,depth in (("baseline",13),("latent",10),("output",13)):
        result=check(variant)
        assert result[0]==depth
        p=json.loads((P/(variant+".json")).read_text())
        assert abs(exact_witness(p,result[1]))>Fraction(1,10)
