"""Run332 frozen G64 scores. Usage: python score332.py checkpoints326.json outcomes329.json > scores332.json"""
import hashlib,json,sys
ck,lab=[open(x,'rb').read() for x in sys.argv[1:3]]
assert hashlib.sha256(ck).hexdigest()=='628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e'
assert hashlib.sha256(lab).hexdigest()=='108d462f64cbc925b0420db3fa10f121926506623062518976d02d96c355782f'
def gap(p):
 h0=[0.]*3;h1=[0.]*3;g=float('inf')
 for k in range(65):
  x1=int(k==0)
  h0=[max(0.,sum(p[3*i+j]*h0[j] for j in range(3))+p[18+i]) for i in range(3)]
  h1=[max(0.,sum(p[9*x1+3*i+j]*h1[j] for j in range(3))+p[18+3*x1+i]) for i in range(3)]
  z1=sum(p[24+i]*h1[i] for i in range(3))+p[27]
  z0=sum(p[24+i]*h0[i] for i in range(3))+p[27]
  g=min(g,z1-z0)
 return g
out={r['seed']:r['outcome'] for r in json.loads(lab)['rows']}
rows=[{'seed':r['seed'],'score':gap(r['p']),'loss':-r['bce'],'outcome':out[r['seed']],'split':'dev' if r['seed']%2==0 else 'heldout'} for r in json.loads(ck)['rows'] if r['epoch']==20]
print(json.dumps({'run':332,'rows':rows},sort_keys=True))
