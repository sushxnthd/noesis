"""Independent numpy replay of trained float64 tanh recurrence on frozen heldout words."""
from pathlib import Path
import json,itertools,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parent

def eval_words(row,x):
    p=row['params'];W=np.asarray(p['W']);U=np.asarray(p['U']);b=np.asarray(p['b']);v=np.asarray(p['v']);c=p['c'];
    h=np.zeros((len(x),len(v)));acc=np.ones(len(x),dtype=bool);first=np.zeros(len(x),dtype=int)
    parity=np.zeros(len(x),dtype=np.int64)
    for t in range(x.shape[1]):
        parity^=x[:,t]
        h=np.tanh(h@W.T+U[x[:,t]]+b)
        good=((h@v+c)>0)==(parity==1)
        first[(first==0)&(~good)]=t+1
        acc&=good
    return {'whole_sequence_accuracy':float(np.mean(acc)),'final_symbol_accuracy':float(np.mean(((h@v+c)>0)==(parity==1))),
            'first_failure_min':int(min(first[first>0])) if np.any(first>0) else None,
            'failures':int(np.sum(~acc)),'n':len(x)}

def main():
    rows=json.loads((ROOT/'TRAINED.json').read_text())['rows']
    x12=np.array(list(itertools.product((0,1),repeat=12)),dtype=np.int64)
    rng=np.random.default_rng(187)
    x128=rng.integers(0,2,size=(128,128),dtype=np.int64)
    out=[]
    for row in rows:
        a=eval_words(row,x12);b=eval_words(row,x128)
        out.append({'seed':row['seed'],'epoch':row['epoch'],'train_acc':row['train_accuracy'],'len12':a,'len128':b})
        print(row['seed'],row['epoch'],'12',a['whole_sequence_accuracy'],'128',b['whole_sequence_accuracy'],flush=True)
    (ROOT/'HELDOUT.json').write_text(json.dumps({'trained_sha256':hashlib.sha256((ROOT/'TRAINED.json').read_bytes()).hexdigest(),'rng_seed':187,'results':out},indent=2)+'\n')
if __name__=='__main__':main()
