from fractions import Fraction as F
import json
from pathlib import Path
p=[F.from_float(x) for x in json.loads((Path(__file__).parent/'seed22242_epoch80.json').read_text())]
a=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in range(2)]
b=[[p[18+3*x+i] for i in range(3)] for x in range(2)]
w=p[24:27];c=p[27];k=F(7,10);T=F(2)
def ge(u,v,d):return min(d+v*T,d+(u*k+v)*T,v,u*k+v)>=0