"""Independent GitHub Actions replay on the public Run251 checkpoint artifact."""
import hashlib,itertools,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'run251'))
from evaluate import replay_a,replay_b,target
LENS=(8,12,16,24,32,48,64,96,128,192,256,384,512)

def candidates():
    pref=[()]+[x for n in (1,2,3) for x in itertools.product(range(3),repeat=n)]
    periods=[x for n in (1,2,3) for x in itertools.product(range(3),repeat=n)]
    for n in LENS:
        for p in pref:
            for t in periods:
                yield 'periodic_tail',p+tuple(t[(i-len(p))%len(t)] for i in range(len(p),n))
    rng=np.random.default_rng(25213037)
    for i in range(8192):
        n=LENS[i%len(LENS)];h=float(rng.choice([.5,.7,.85,.95]))
        yield 'hold_biased',tuple(map(int,rng.choice(3,size=n,p=[h,(1-h)/2,(1-h)/2])))
    for n in LENS:
        for a in range(0,n,max(1,n//16)):
            for b in range(a+1,n,max(1,n//16)):
                for x,y in ((1,1),(1,2),(2,1),(2,2)):
                    w=[0]*n;w[a]=x;w[b]=y
                    yield 'two_event',tuple(w)

def main():
    cp=HERE/'input'/'CHECKPOINTS.json'
    if not cp.exists():cp=HERE/'REMOTE_RUN251_CHECKPOINTS.json'
    sha=hashlib.sha256(cp.read_bytes()).hexdigest()
    assert sha=='569c57b6ec5d3e208d2f0db47486ed9ade1ebd21df2785bb2c673e8fe342db06',sha
    rows=json.loads(cp.read_text())['rows']
    row=next(r for r in rows if r['seed']==13037 and r['epoch']==200)
    assert row['train_accuracy']==1
    p=row['params'];A=np.array(p['A']);E=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
    seen=set();stats={};count=0;witness=None;batch=[];family=None
    def flush(words,label):
        nonlocal count,witness
        if not words:return False
        h=np.zeros((len(words),4));xs=np.asarray(words,dtype=np.int8)
        for t in range(xs.shape[1]):h=np.maximum(0,h@A.T+E[xs[:,t]]+b)
        pred=(h@v+c)>0
        truth=np.fromiter((target(w) for w in words),dtype=np.int8,count=len(words))
        count+=len(words);stats[label]=stats.get(label,0)+len(words)
        for idx in np.flatnonzero(pred!=truth):
            w=words[int(idx)];a=replay_a(row,w);bb=replay_b(row,w)
            assert a==bb,'independent exact checkers disagree'
            if a[0]!=a[1]:witness={'word':list(w),'length':len(w),'prediction':a[0],'target':a[1]};return True
        return False
    for label,w in candidates():
        if w in seen:continue
        seen.add(w)
        if batch and (label!=family or len(w)!=len(batch[0])):
            if flush(batch,family):break
            batch=[]
        family=label;batch.append(w)
        if len(batch)>=512:
            if flush(batch,family):break
            batch=[]
    else:flush(batch,family)
    result={'seed':13037,'checkpoint_sha256':sha,'evaluated':count,'families':stats,'witness':witness,'no_witness_is_not_certificate':True}
    (HERE/'CI_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    assert count==25322 and witness is None, result
    print('PASS: 25322 probes, no exact witness; status UNRESOLVED',json.dumps(stats))
if __name__=='__main__':main()
