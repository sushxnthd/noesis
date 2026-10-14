"""Exact rational post-training ray repair for two archived Adam-trained counters."""
import copy,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
SEEDS={222:2,239:4}
BASE=Path(__file__).resolve().parents[1]/'run157'

def load(seed):
    raw=(BASE/f'RUN157_SEED_{seed}.json').read_bytes()
    item=json.loads(raw,parse_float=str)[0]
    assert item['seed']==seed and item['variant']=='latent'
    p=item['parameters']
    return ({key: [[F(x) for x in row] for row in p[key]] if key!='w'
             else [F(x) for x in p[key]] for key in ('A','E','w')},
            hashlib.sha256(raw).hexdigest())

def project(p,k):
    q=copy.deepcopy(p); A,E,w=q['A'],q['E'],q['w']; d=len(w); u=E[0][k]
    assert u>0 and A[k][k]==1
    assert all(A[j][k]<=0 and E[0][j]<=0 for j in range(d) if j!=k)
    edits=[]
    def change(group,idx,val):
        target=q[group]
        old=target[idx] if isinstance(idx,int) else target[idx[0]][idx[1]]
        if old==val:return
        if isinstance(idx,int):target[idx]=val
        else:target[idx[0]][idx[1]]=val
        name=group+'['+','.join(map(str,idx if isinstance(idx,tuple) else (idx,)))+']'
        edits.append(dict(parameter=name,before=str(old),after=str(val),delta=str(val-old)))
    change('E',(1,k),-u);change('E',(2,k),F(0));change('w',k,1/u)
    for t in (1,2):
        for j in range(d):
            if j!=k and E[t][j]>0:change('E',(t,j),F(0))
    return q,edits

def prove(q,k):
    A,E,w=q['A'],q['E'],q['w'];u=E[0][k];d=len(w)
    assert u>0 and A[k][k]==1 and E[1][k]==-u and E[2][k]==0
    assert w[k]*u==1
    assert all(A[j][k]<=0 for j in range(d) if j!=k)
    assert all(E[t][j]<=0 for t in range(3) for j in range(d) if j!=k)
    # Inductively h=u*c*e_k for every word. ReLU maps active coordinate
    # to u*max(0,c+delta_t); all off-ray preactivations are nonpositive.
    return True

def forward(q,word):
    A,E,w=q['A'],q['E'],q['w'];d=len(w);h=[F(0)]*d;c=0
    for t in word:
        h=[max(F(0),sum(A[j][i]*h[i] for i in range(d))+E[t][j]) for j in range(d)]
        c=max(0,c+(1 if t==0 else -1 if t==1 else 0))
    return h,sum(w[i]*h[i] for i in range(d)),c

def run():
    out=[]
    for seed,k in SEEDS.items():
        p,sha=load(seed);q,edits=project(p,k)
        assert prove(q,k)
        assert len(edits)==(5 if seed==222 else 6)
        u=q['E'][0][k]
        for word in itertools.product(range(3),repeat=6):
            h,y,c=forward(q,word)
            assert h==[u*c if i==k else F(0) for i in range(len(h))]
            assert y==c
        witness=(0,2) if seed==222 else (2,)
        _,oldy,c=forward(p,witness)
        assert oldy!=c
        for e in edits:
            broken=copy.deepcopy(q)
            group,indices=e['parameter'].split('[')
            idx=tuple(int(z) for z in indices[:-1].split(','))
            if len(idx)==1:broken[group][idx[0]]=F(e['before'])
            else:broken[group][idx[0]][idx[1]]=F(e['before'])
            try:prove(broken,k)
            except AssertionError:pass
            else:raise AssertionError('unnecessary edit '+e['parameter'])
        out.append(dict(seed=seed,original_checkpoint_sha256=sha,width=len(q['w']),
                        active_coordinate=k,changed_scalar_count=len(edits),
                        max_abs_parameter_change=str(max(abs(F(e['delta'])) for e in edits)),
                        exact_length_six_words_checked=729,
                        original_nonexact_witness=''.join(map(str,witness)),
                        original_witness_error=str(oldy-c),
                        all_alphabet_all_length_exact_rational_certificate=True,
                        support_minimality_scope='fixed A,E[0], same one-ray representation',
                        edits=edits))
    return out

if __name__=='__main__':
    out=run()
    Path(__file__).with_name('RESULT160.json').write_text(json.dumps(out,indent=2)+'\n')
    print([(x['seed'],x['changed_scalar_count']) for x in out])
