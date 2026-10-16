"""Reproduce Run190 new-seed parity training using the original Run187 architecture."""
import sys, json, hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parents[1]/"research"/"kernel_001"/"run187"))
from train187 import RNN,make_data,export
import torch,numpy as np
SEEDS=(137,139,149,151)
def run():
    torch.set_num_threads(1)
    x,y=make_data()
    rows=[]
    for seed in SEEDS:
        torch.manual_seed(seed)
        model=RNN()
        optimizer=torch.optim.Adam(model.parameters(),lr=.02)
        rows.append(export(model,seed,0,x,y))
        for epoch in range(1,601):
            optimizer.zero_grad()
            loss=torch.nn.functional.binary_cross_entropy_with_logits(model(x),y)
            loss.backward();optimizer.step()
            if epoch in (300,600):
                rows.append(export(model,seed,epoch,x,y))
    payload={'protocol_sha256':"491400e1334560fddfef35dc0885901ec8874ced9e1eba0c87e97f3bbeb8eac0",'torch':torch.__version__,'numpy':np.__version__,'rows':rows}
    target=R/"TRAINED.json"
    if target.exists():raise RuntimeError("Refuse to overwrite training artifacts")
    target.write_text(json.dumps(payload,indent=1)+"\n")
    digest=hashlib.sha256(target.read_bytes()).hexdigest()
    print("TRAINED_SHA256",digest)
    for r in rows:
        if r['epoch']:print(r['seed'],r['epoch'],r['loss'],r['train_accuracy'])
if __name__=="__main__":run()
