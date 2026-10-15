from research.kernel001.run185.token_proof185 import check
from research.kernel001.run185.independent185 import replay

def test_token_proof():
    assert all(check(word)[0]<0.020225 for word in ('110010','101100'))

def test_nonlinear_replay():
    assert replay('110010',4096)==(None,0)
    assert replay('101100',4096)==(None,0)
    assert replay('000111',2048)==(119,0)
