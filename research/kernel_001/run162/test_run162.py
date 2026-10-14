import json
from pathlib import Path
from audit162 import f32,load,scalar32,full32
def test_seed222():
    p,_=load(222,2)
    n,h,y=scalar32(f32(p['E'][0][2]),f32(p['w'][2]),5000)
    assert n==3679 and full32(p,5000)[0]==n
def test_seed239():
    p,_=load(239,4)
    n,h,y=scalar32(f32(p['E'][0][4]),f32(p['w'][4]),5000)
    assert n==3582 and full32(p,5000)[0]==n
def test_outcomes():
    r=json.loads(Path(__file__).with_name('RESULT162.json').read_text())
    assert r['frozen_primary_success']
    assert [x['binary32_first_increment_failure'] for x in r['outcomes']]==[3679,3582]
