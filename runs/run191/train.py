"""Independent GitHub-hosted reproduction of frozen Run191 training."""
import sys,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parents[1]/"research"/"kernel_001"/"run187"))
from train187 import RNN,make_data,export
import torch,numpy as np
SEEDS=(157,163,167,173)
def run():
    torch.set_num_threads(1);x,y=make_data();rows=[]
    for seed in SEEDS:
        torch.manual_seed(seed);model=RNN();opt=torch.optim.Adam(model.parameters(),lr=.02)
        rows.append(export(model,seed,0,x,y))
        for epoch in range(1,601):
            opt.zero_grad();loss=torch.nn.functional.binary_cross_entropy_with_logits(model(x),y)
            loss.backward();opt.step()
            if epoch in (300,600):rows.append(export(model,seed,epoch,x,y))
    out=R/'TRAINED.json'
    if out.exists():raise RuntimeError('refuse overwrite')
    out.write_text(json.dumps({'torch':torch.__version__,'numpy':np.__version__,'rows':rows},indent=1)+'\n')
    for r in rows:
        if r['epoch']:print('TRAIN',r['seed'],r['epoch'],r['loss'],r['train_accuracy'])
    print('TRAINED_SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
if __name__=='__main__':run()
