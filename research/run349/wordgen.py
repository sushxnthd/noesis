"""Frozen Run349 deterministic binary-word generator."""
def generate(L=65):
    words={format(i,f'0{n}b') for n in range(1,min(10,L)+1) for i in range(2**n)}
    for n in range(65):
        for w in ('1'+'0'*n,'0'*n+'1'):
            if len(w)<=L: words.add(w)
    for a in range(65):
        for b in range(65-a):
            for w in ('1'+'0'*a+'1'+'0'*b,'0'*a+'1'+'0'*b):
                if len(w)<=L: words.add(w)
    for k in range(1,9):
        for n in range(65):
            for w in ('1'*k+'0'*n,'0'*n+'1'*k):
                if len(w)<=L: words.add(w)
    words.discard('')
    return sorted(words,key=lambda w:(len(w),w))
if __name__=='__main__':
    assert len(generate(17))==2326
    assert len(generate(18))==2374
    assert len(generate(22))==2586
    assert len(generate(23))==2644
    assert len(generate())==7006
    print('word generator PASS')
