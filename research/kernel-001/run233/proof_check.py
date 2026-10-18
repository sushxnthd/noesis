"""Two independent exact-real checkers: mpmath.iv and directed Decimal."""
import json,hashlib
from pathlib import Path
from mpmath import iv
import decimal_interval as dec
R=Path(__file__).parent;iv.dps=65
D=json.load(open(R/'CHECKPOINTS.json'));ROWS={(r['seed'],r['epoch']):r for r in D['rows']}
C=json.load(open(R/'CANDIDATES.json'))['results']
CAND={(r['seed'],r['epoch']):r['result'] for r in C if r['result']['status']=='CANDIDATE'}
WIT=json.load(open(R/'NUMERIC_WITNESSES.json'))
WORDS={(r['seed'],r['epoch']):r['word'] for r in WIT if r['status']=='NUMERIC_CANDIDATE'}
def nextq(q,t):return 0 if t==2 else (1 if t==1 else q)
def iv_exact(x):
 n,d=float(x).as_integer_ratio();return iv.mpf(n)/iv.mpf(d)
def iv_tanh(x):
 def pt(z):
  e=iv.exp(2*z);return (e-1)/(e+1)
 return iv.mpf([pt(x.a).a,pt(x.b).b])
def parse_key(k):
 a,b=k.split(':');return int(a),tuple(map(int,b))
def setup(row,mode):
 p=row['params'];exact=iv_exact if mode=='iv' else dec.exact
 I=(lambda x,y=None:iv.mpf([x,y]) if y is not None else iv.mpf(x)) if mode=='iv' else (lambda x,y=None:dec.I(x,y))
 tanh=iv_tanh if mode=='iv' else dec.tanh_interval
 lo=(lambda x:x.a) if mode=='iv' else (lambda x:x.lo)
 hi=(lambda x:x.b) if mode=='iv' else (lambda x:x.hi)
 W=[[[exact(x) for x in rr] for rr in M] for M in p['W']]
 b=[[exact(x) for x in rr] for rr in p['b']]
 v=[exact(x) for x in p['v']];c=exact(p['c'])
 def step(h,t):
  return [tanh(sum((W[t][j][k]*h[k] for k in range(3)),b[t][j])) for j in range(3)]
 def logit(h):return sum((v[j]*h[j] for j in range(3)),c)
 def good(q,h):
  z=logit(h);return hi(z)<0 if q==0 else lo(z)>0
 return I,lo,hi,step,logit,good
def evaluate(row,mode,word):
 I,lo,hi,step,logit,good=setup(row,mode)
 h=[I('.5'),I('-.5'),I('.25')];q=0
 for t in word:q=nextq(q,t);h=step(h,t)
 z=logit(h)
 return dict(q=q,lo=str(lo(z)),hi=str(hi(z)),wrong=(lo(z)>0 if q==0 else hi(z)<0),correct=good(q,h))
def check_candidate(row,mode,cert):
 I,lo,hi,step,logit,good=setup(row,mode);k=cert['k']
 inv={parse_key(key):[I(rec['lo'][j],rec['hi'][j]) for j in range(3)] for key,rec in cert['boxes'].items()}
 for length in range(1,k+1):
  for n in range(3**length):
   word=tuple((n//3**(length-1-j))%3 for j in range(length))
   h=[I('.5'),I('-.5'),I('.25')];q=0
   for t in word:q=nextq(q,t);h=step(h,t)
   if not good(q,h):return dict(status='ABSTAIN',reason='prefix')
   if length==k:
    key=(q,word)
    if key not in inv:return dict(status='ABSTAIN',reason='missing_base')
    for j in range(3):
     if not (lo(h[j])>=lo(inv[key][j]) and hi(h[j])<=hi(inv[key][j])):
      return dict(status='ABSTAIN',reason='base')
 for (q,word),h in inv.items():
  if not good(q,h):return dict(status='ABSTAIN',reason='output')
  for t in range(3):
   dest=(nextq(q,t),word[1:]+(t,))
   if dest not in inv:return dict(status='ABSTAIN',reason='missing_dest')
   z=step(h,t)
   for j in range(3):
    if not (lo(z[j])>=lo(inv[dest][j]) and hi(z[j])<=hi(inv[dest][j])):
     return dict(status='ABSTAIN',reason='closure')
 return dict(status='CERTIFIED',k=k,cells=len(inv),obligations=len(inv)*9)
results=[]
for (seed,epoch),row in ROWS.items():
 if (seed,epoch) in CAND:
  a=check_candidate(row,'iv',CAND[seed,epoch]);b=check_candidate(row,'decimal',CAND[seed,epoch])
  status='CORRECT' if a['status']==b['status']=='CERTIFIED' else 'UNRESOLVED'
 elif (seed,epoch) in WORDS:
  word=WORDS[seed,epoch];a=evaluate(row,'iv',word);b=evaluate(row,'decimal',word)
  status='INCORRECT' if a['wrong'] and b['wrong'] else 'UNRESOLVED'
 else:status='UNRESOLVED';a=b={}
 results.append(dict(seed=seed,epoch=epoch,status=status,primary=a,independent=b,word=WORDS.get((seed,epoch))))
 print(seed,epoch,status,flush=True)
(R/'PROOFS.json').write_text(json.dumps(dict(checkpoint_sha256=hashlib.sha256((R/'CHECKPOINTS.json').read_bytes()).hexdigest(),results=results),indent=2)+'\n')
