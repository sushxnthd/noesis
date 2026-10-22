def words():
    one=['1'+'0'*k for k in range(128)]
    two=['1'+'0'*a+'1'+'0'*b for a in range(64) for b in range(64)]
    assert len(set(one+two))==4224
    return one+two
