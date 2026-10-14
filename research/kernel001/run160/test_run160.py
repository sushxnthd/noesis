from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec

HERE=Path(__file__).parent
def load(name):
    spec=spec_from_file_location(name,HERE/f'{name}.py')
    mod=module_from_spec(spec);spec.loader.exec_module(mod);return mod

def test_exact_inductive_repair():
    c=load('certify160')
    r=c.run()
    assert [(x['seed'],x['changed_scalar_count']) for x in r]==[(222,5),(239,6)]

def test_all_alphabet_short_words():
    c=load('certify160')
    for seed,k in c.SEEDS.items():
        p,_=c.load(seed);q,_=c.project(p,k)
        for word in ((1,),(2,),(1,2,1),(0,1,2,0,1),(0,0,1,2,1)):
            h,y,count=c.forward(q,word)
            assert y==count
            assert h[k]==q['E'][0][k]*count

def test_originals_not_exact():
    c=load('certify160')
    for seed,k in c.SEEDS.items():
        p,_=c.load(seed)
        word=(0,2) if seed==222 else (2,)
        _,y,count=c.forward(p,word)
        assert y!=count

def test_independent_decimal_checker():
    v=load('independent160')
    for seed,k in ((222,2),(239,4)):
        r=v.verify(seed,k)
        assert r['checked_words']==3280
        assert r['status'].startswith('PASS')
