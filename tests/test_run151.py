import sys
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/"research"/"kernel_001"/"run151"
sys.path.insert(0,str(RUN))
from global_horizon import check
from run151_exact import exact_witness
import json

def test_first_failures():
    for variant,depth in (("baseline",13),("latent",10),("output",13)):
        result=check(variant)
        assert result[0]==depth
        p=json.loads((RUN/"checkpoints"/(variant+".json")).read_text())
        assert abs(exact_witness(p,result[1]))>Fraction(1,10)
