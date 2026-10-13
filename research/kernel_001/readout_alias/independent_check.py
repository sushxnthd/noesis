"""Independent checker for NOESIS Kernel 001 readout aliasing."""
from fractions import Fraction
from itertools import product
import json

def trace(bits, limit):
    a=b=0
    for s in bits:
        a=max(0,a+s)
        b=max(0,min(limit,b+s))
    return a,b

def verify():
    tested=0
    for cap in range(1,7):
        for length in range(2*cap+2):
            for bits in product((-1,1), repeat=length):
                a,b=trace(bits,cap)
                if length<2*cap+1:
                    assert (a==0)==(b==0),(cap,bits,a,b)
                if length<=cap:
                    assert a==b,(cap,bits,a,b)
                tested+=1
        witness=(1,)*(cap+1)+(-1,)*cap
        assert trace(witness,cap)==(1,0)
    states=[trace(bits,8)[0] for l in range(6) for bits in product((-1,1),repeat=l)]
    def loss(a,b):
        return sum((a*n+b*n-n)**2 for n in states)/len(states)
    eps=Fraction(1,100)
    a,b=Fraction(-1,4),Fraction(3,4)
    da=(loss(a+eps,b)-loss(a-eps,b))/(2*eps)
    db=(loss(a,b+eps)-loss(a,b-eps))/(2*eps)
    assert da==db==Fraction(-61,21)
    eta=Fraction(21,244)
    assert (a-eta*da,b-eta*db)==(0,1)
    assert loss(0,1)==loss(1,0)==0
    return {'independent_exhaustive_words':tested,'caps':list(range(1,7)),
            'gradient_exact':str(da),'shortcut_after_training':[0,1],
            'algorithm_after_training':[1,0], 'status':'pass'}
if __name__=='__main__': print(json.dumps(verify(),sort_keys=True,indent=2))
