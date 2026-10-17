import json,sys,numpy as np
P=(1019,1063,1087,1171)
N=(1009,1013,1049,1061,1069,1093,1123,1151)
def truth(w):
 q=0
 for t in w:q=0 if t==2 else q^(t==1)
 return q
def pred(p,w):
 W=np.asarray(p['W']);b=np.asarray(p['b']);v=np.asarray(p['v']);h=np.array([.5,-.5])
 for t in w:h=np.tanh(W[t]@h+b[t])
 return int(h@v+p['c']>0)
def auc(s):return sum((s[p]>s[n])+.5*(s[p]==s[n]) for p in P for n in N)/32
def run(data):
 rng=[np.random.default_rng(s) for s in (219011,219012,219013)]
 words={k:[] for k in ('challenge','binary','ternary','random_pairs')}
 for L in (16,32,64,128,256,512):
  a=([0,0,1,1]*((L+3)//4))[:L-2]
  words['challenge'] += [([0]+[0]*(L-1),[1]+[0]*(L-1)),([0,0]+a,[0,1]+a)]
  words['binary'] += [rng[0].integers(0,2,size=L).tolist() for _ in range(4)]
  words['ternary'] += [rng[1].integers(0,3,size=L).tolist() for _ in range(4)]
  b=rng[2].integers(0,2,size=L-1).tolist();c=rng[2].integers(0,2,size=L-2).tolist()
  words['random_pairs'] += [([0]+b,[1]+b),([0,0]+c,[0,1]+c)]
 scores={k:{} for k in (*words,'loss','accuracy')}
 for r in data['rows']:
  if r['epoch']!=100 or r['seed'] not in P+N:continue
  p=r['params'];s=r['seed']
  for k in ('challenge','random_pairs'):
   scores[k][s]=sum(all(pred(p,w)==truth(w) for w in pair) for pair in words[k])/12
  for k in ('binary','ternary'):
   scores[k][s]=sum(pred(p,w)==truth(w) for w in words[k])/24
  scores['loss'][s]=-r['loss'];scores['accuracy'][s]=r['train_accuracy']
 a={k:auc(v) for k,v in scores.items()}
 return dict(auroc=a,delta=a['challenge']-max(v for k,v in a.items() if k!='challenge'),scores=scores)
if __name__=='__main__':
 d=run(json.load(open(sys.argv[1])));print(json.dumps(d,indent=2))
 assert abs(d['delta']-.21875)<1e-12
