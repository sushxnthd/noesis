import json,hashlib
from pathlib import Path
from mpmath import iv
from proof203_core import q,step,cls
R=Path(__file__).parent
def check(row,w):
 p={k:([[q(x) for x in a] for a in row['params'][k]] if k in ('W','U','V') else [q(x) for x in row['params'][k]]) for k in ('W','U','V','b','c')}
 depth=w['max_prefix_length'];hs=[([iv.mpf(0)]*12,'')];labels={}
 for n in range(1,depth+2):
  nxt=[]
  for h,word in hs:
   for a in (0,1):
    ww=word+str(a);hh=step(h,p,a);labels[ww]=cls(hh,p);nxt.append((hh,ww))
  hs=nxt
 for n in range(1,depth+1):
  seen={};collision=False
  for length in range(1,n+1):
   for k in range(2**length):
    word=format(k,f'0{length}b')
    for a in '01':
     key=(labels[word],a)
     if key in seen and seen[key]!=labels[word+a]:collision=True
     else:seen.setdefault(key,labels[word+a])
  assert collision==(n==depth)
 u,v,a=w['u'],w['v'],w['symbol']
 assert labels[u]==labels[v] and labels[u+a]!=labels[v+a]
 return {'seed':row['seed'],'epoch':row['epoch'],'shortest_max_prefix_depth':depth,'verified_words':sum(2**n for n in range(1,depth+2)),'labels':{x:labels[x] for x in (u,v,u+a,v+a)},'status':'PASS'}
if __name__=='__main__':
 path=R/'CHECKPOINTS.json'
 assert hashlib.sha256(path.read_bytes()).hexdigest()=='5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32'
 rows={(x['seed'],x['epoch']):x for x in json.loads(path.read_text())['rows']}
 results=[check(rows[s['seed'],s['epoch']],s['witness']) for s in json.loads((R/'SCREEN203.json').read_text())]
 (R/'PROOF203.json').write_text(json.dumps(results,indent=2)+'\n')
 print(results)
