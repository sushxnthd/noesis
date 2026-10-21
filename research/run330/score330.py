import json,sys
from pathlib import Path
rows=json.loads(Path(sys.argv[1]).read_text())["rows"]
out=[]
for r in rows:
 if r["epoch"]!=20:continue
 p=r["p"];h=[0.]*3
 for x in (1,0,0,0):
  h=[max(0.,sum(p[9*x+3*i+j]*h[j] for j in range(3))+p[18+3*x+i]) for i in range(3)]
 z=sum(p[24+i]*h[i] for i in range(3))+p[27]
 out.append([r["seed"],z,-r["bce"]])
Path(sys.argv[2]).write_text(json.dumps(out))
