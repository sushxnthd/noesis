from run197 import params, advance, logits, WIDTH
import json
import numpy as np
rows=json.load(open('CHECKPOINTS.json'))['rows']
p=params(next(r for r in rows if r['seed']==257 and r['epoch']==800))
h=np.zeros((1,WIDTH)); labels=np.zeros(1,dtype=int)
for length in range(1,16):
    h=np.concatenate((advance(h,p,0),advance(h,p,1)))
    labels=np.concatenate((labels,(labels+1)%3))
    wrong=np.flatnonzero(logits(h,p).argmax(axis=1)!=labels)
    print(length,len(wrong))
    if len(wrong):break
