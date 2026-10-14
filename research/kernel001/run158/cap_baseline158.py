from fractions import Fraction as F

def normalized_cap_error(cap,n):
    assert cap>=1 and n>=1
    return F(n-min(n,cap),n)

def test_baseline():
    assert normalized_cap_error(12,12)==0
    assert normalized_cap_error(12,13)==F(1,13)
    assert normalized_cap_error(12,120)==F(9,10)
    assert normalized_cap_error(12,1200)==F(99,100)
