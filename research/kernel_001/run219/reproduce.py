import hashlib,json,math
from pathlib import Path
D=json.loads((Path(__file__).parent/"EPOCH100_PARAMS.json").read_text())["epoch100"]
P=[661,701,733];N=[677,683,691,739]
W=[p+[0]*k+[1] for p in ([1],[2,1],[0,1],[1,1]) for k in range(3,31)]
def rnd(t,i,j):return hashlib.sha256(f"NOESIS-R219|{t}|{i}|{j}".encode()).digest()[0]
U=[[rnd("uniform",i,j)%3 for j in range(len(w))] for i,w in enumerate(W)]
S=[]
for i,word in enumerate(W):
 w=word[:]
 for j in range(len(w)-1,0,-1):
  k=rnd("shuffle",i,j)%(j+1);w[j],w[k]=w[k],w[j]
 S.append(w)
def score(p,words):
 hit=0
 for word in words:
  h=.5;q=0
  for t in word:
   h=math.tanh(p["w"][t]*h+p["b"][t]);q=0 if t==2 else q^(t==1)
  hit+=((p["v"]*h+p["c"]>0)==(q==1))
 return hit/len(words)
def auc(d):return sum((d[a]>d[b])+.5*(d[a]==d[b]) for a in P for b in N)/12
A={key:auc({int(s):score(p,words) for s,p in D.items()}) for key,words in (("suffix",W),("uniform",U),("shuffle",S))}
assert len(W)==112 and sum(map(len,W))==2156
assert abs(A["suffix"]-.75)<1e-12 and abs(A["uniform"]-7/12)<1e-12 and abs(A["shuffle"]-2/3)<1e-12
print(json.dumps({"auroc":A,"delta":A["suffix"]-max(A["uniform"],A["shuffle"]),"frozen":"FAIL"},sort_keys=True))
