from fractions import Fraction as F

def test_run273_exact_thresholds():
    for a,b,v,c,n in [
        ([1.3152369299783537,1.1601919619208452,0.00024414062458318894],[-0.23516822759601694,3.403993965366687,-1.3639167201680862],3.471500041091313,-5.187659260823268,31),
        ([1.567522997916733,0.8846029647720239,0.00024414701927295493],[-0.19616908385560564,3.5263300894392082,-1.2449349925479019],3.2305676094771374,-5.018317239969839,19)]:
        a=list(map(F.from_float,a));b=list(map(F.from_float,b));v=F.from_float(v);c=F.from_float(c)
        h=max(F(0),b[1]);fixed=-b[0]/(a[0]-1)
        assert a[0]>1 and fixed>=0 and h>fixed and a[2]>0 and v>0 and c<0
        for _ in range(n-1):h=a[0]*h+b[0]
        assert v*max(F(0),a[2]*h+b[2])+c<=0
        h=a[0]*h+b[0]
        assert v*max(F(0),a[2]*h+b[2])+c>0
