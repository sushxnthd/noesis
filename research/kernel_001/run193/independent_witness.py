import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/"run192"))
from independent_decimal import load,step,out,I
WORDS=("00111100000000011","01111000000000001")
P=[load(300),load(600)]
for w in WORDS:
 h=[[I(0)]*8,[I(0)]*8]
 for bit in w:
  h=[step(h[i],P[i],int(bit)) for i in range(2)]
 a,b=[out(h[i],P[i]) for i in range(2)]
 s0=1 if a.a>0 else -1 if a.b<0 else 0
 s1=1 if b.a>0 else -1 if b.b<0 else 0
 truth=1 if w.count("1")%2 else -1
 assert s0==-truth and s1==truth,(w,a.a,a.b,b.a,b.b)
 print(json.dumps({"word":w,"truth":truth,"epoch300_sign":s0,"epoch600_sign":s1,
  "epoch300_interval":[str(a.a),str(a.b)],"epoch600_interval":[str(b.a),str(b.b)]}))
