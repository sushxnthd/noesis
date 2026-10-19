"""CI smoke tests for exact full-alphabet trained-network certificates."""
from research.kernel_001.run270.independent_check import verify,replay

CERTIFIED_CONTROL_19000={
    "a":[1.888458397949069,1.69381526296076,-0.3363850665421695],
    "b":[-0.26261214843793645,3.7166228041032454,-0.3804281160625871],
    "v":3.113926885069735,"c":-4.990365425219455}
CERTIFIED_INTERVENTION_19015={
    "a":[1.6857969210703603,1.555977192300417,-0.20857758305116647],
    "b":[-0.10968221032625743,3.1825666429158885,-0.2792833369017352],
    "v":3.6508635356185875,"c":-5.139354564768708}
UNCERTIFIED_CONTROL_19015={
    "a":[0.023056890302595206,0.028336334245639583,-0.20913812604432336],
    "b":[-0.16191738484645807,-0.1388690278007003,-0.27074660815561813],
    "v":0.3611230417009839,"c":-0.08789096188185434}

def test_gradient_trained_checkpoints_exact():
    for p in (CERTIFIED_CONTROL_19000,CERTIFIED_INTERVENTION_19015):
        assert verify(p)
        for word in ([1]+[0]*256+[2],[2]+[0]*256+[1],
                     [1,2,1,0]*64,[2,1,2,0]*64):
            assert replay(p,word) is None
    assert not verify(UNCERTIFIED_CONTROL_19015)

def test_delayed_switch_spoof_family():
    for K in (8,16,32,64,128):
        p={"a":[2,1,2.**(-K)],"b":[-1,2,-1],"v":1,"c":-1}
        assert not verify(p)
        assert replay(p,[1,1]+[0]*(K-1)+[2]) is None
        assert replay(p,[1,1]+[0]*K+[2])==K+3

def test_mutated_certificates_rejected():
    p={"a":[2,1,-1],"b":[-1,2,-1],"v":1,"c":-1}
    assert verify(p)
    assert not verify(dict(p,a=[2,1,1]))
    assert not verify(dict(p,b=[-3,2,-1]))
    assert not verify(dict(p,v=-1))
