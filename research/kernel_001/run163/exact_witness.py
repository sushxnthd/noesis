from fractions import Fraction as F
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("SEED230_REMOTE_TRAINED.json").read_text())
p=d["parameters"]
A=[[F(str(v)) for v in row] for row in p["A"]]
E=[[F(str(v)) for v in row] for row in p["E"]]
w=[F(str(v)) for v in p["w"]]
h=[F(0)]*5
def step(t):
 global h
 h=[max(F(0),sum(a*b for a,b in zip(row,h))+e) for row,e in zip(A,E[t])]
for _ in range(6):step(0)
maximum=F(0)
for n in range(1,495):
 step(2)
 error=sum(a*b for a,b in zip(w,h))-6
 if n<494:maximum=max(maximum,abs(error))
print(n,maximum<=F(1,10),error>F(1,10),float(error))
