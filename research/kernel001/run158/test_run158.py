from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

HERE=Path(__file__).parent

def load(name):
    spec=spec_from_file_location(name,HERE/f"{name}.py")
    mod=module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def test_rational_first_failures():
    c=load("certify158")
    assert c.check(222)["first_neutral_suffix_failure"]==3090553
    assert c.check(239)["first_neutral_suffix_failure"]==28802732784

def test_independent_decimal_first_failures():
    c=load("independent158")
    assert c.check(222,2)["first_neutral_suffix_failure"]==3090553
    assert c.check(239,4)["first_neutral_suffix_failure"]==28802732784

def test_small_relative_increment_defects():
    from fractions import Fraction as F
    c=load("certify158")
    for seed in (222,239):
        assert F(c.check(seed)["increment_relative_error_all_n"])<F(1,1000000)

def test_capped_baseline():
    from fractions import Fraction as F
    m=load("cap_baseline158")
    assert m.normalized_cap_error(12,12)==0
    assert m.normalized_cap_error(12,120)==F(9,10)
    assert m.normalized_cap_error(12,1200)==F(99,100)
