"""Reproduce frozen 28 checkpoints; use CPU only."""
import json
from pathlib import Path
from train_core import train
EPOCHS=(0,20,50,100,200,400,800)
rows=[]
for seed in (211,223,227,229):
 w,b,v,c,opt,loss=train(seed)
 for epoch in range(801):
  if epoch in EPOCHS:
   z,acc=loss()
   rows.append(dict(seed=seed,epoch=epoch,loss=z.item(),train_accuracy=acc,params=dict(w=w.detach().tolist(),b=b.detach().tolist(),v=v.item(),c=c.item())))
  if epoch==800:break
  opt.zero_grad();z,_=loss();z.backward();opt.step()
 print(seed,rows[-1]['train_accuracy'],flush=True)
Path(__file__).with_name('CHECKPOINTS_REGENERATED.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n')
