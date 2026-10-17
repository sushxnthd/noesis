"""Independent stdlib-only verifier of Run219 final-sign results."""
import json,sys,math,itertools
P=(1019,1063,1087,1171)
N=(1009,1013,1049,1061,1069,1093,1123,1151)
def truth(w):
 q=0
 for x in w:
  if x==2:q=0
  elif x==1:q=1-q
 return q
def pred(p,w):
 h0,h1=.5,-.5
 for t in w:
  W=p['W'][t];b=p['b'][t]
  h0,h1=math.tanh(W[0][0]*h0+W[0][1]*h1+b[0]),math.tanh(W[1][0]*h0+W[1][1]*h1+b[1])
 return int(p['v'][0]*h0+p['v'][1]*h1+p['c']>0)
def auc(s,pos=P):
 neg=set(P+N)-set(pos)
 return sum(1 if s[p]>s[n] else .5 if s[p]==s[n] else 0 for p in pos for n in neg)/(len(pos)*len(neg))
def check(data):
 from reproduce import run,words
 expected=run(data); ch,rb,rt,rp=words()
 scores={k:{} for k in expected['scores']}
 count=0
 for row in data['rows']:
  if row['epoch']!=100 or row['seed'] not in P+N:continue
  s=row['seed'];p=row['params']
  for k,seq in [('challenge',ch),('random_pairs',rp)]:
   scores[k][s]=sum(all(pred(p,w)==truth(w) for w in pair) for pair in seq)/12
   count+=24
  for k,seq in [('binary',rb),('ternary',rt)]:
   scores[k][s]=sum(pred(p,w)==truth(w) for w in seq)/24
   count+=24
  scores['loss'][s]=-row['loss'];scores['accuracy'][s]=row['train_accuracy']
  for k in scores:assert abs(scores[k][s]-expected['scores'][k][s])<1e-12,(s,k)
 a={k:auc(v) for k,v in scores.items()}
 for k in a:assert abs(a[k]-expected['auroc'][k])<1e-12
 d=a['challenge']-max(v for k,v in a.items() if k!='challenge')
 perms=list(itertools.combinations(sorted(P+N),4))
 p=sum(auc(scores['challenge'],pos)-max(auc(v,pos) for k,v in scores.items() if k!='challenge')>=d-1e-12 for pos in perms)/len(perms)
 print(json.dumps(dict(independent='PASS',decisions=count,auroc=a,delta=d,permutations=len(perms),one_sided_permutation_tail=p),indent=2))
if __name__=='__main__':check(json.load(open(sys.argv[1])))
