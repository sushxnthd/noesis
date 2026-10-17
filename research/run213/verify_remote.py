import json,sys
from mpmath import iv
sys.path.insert(0,'research/kernel_001/run210')
from verify_run210 import check,ex,th
D=json.load(open('research/run213/RUN213_CHECKPOINTS.json'))
rows={r['seed']:r for r in D['rows'] if r['epoch']==200}
positive=(821,823,827,863,877,887,919,929)
for seed in positive:
 status=check(rows[seed])['status'];print('positive',seed,status,flush=True)
 assert status=='CERTIFIED'
words={839:'1000000000001',857:'1000000000',883:'120010000',937:'100000000'}
for seed,word in words.items():
 p=rows[seed]['params']
 W=[[[ex(x) for x in row] for row in mat] for mat in p['W']]
 b=[[ex(x) for x in row] for row in p['b']]
 v=[ex(x) for x in p['v']];c=ex(p['c']);h=[ex(.5),ex(-.5)];q=0
 for ch in word:
  t=int(ch);q=0 if t==2 else q^(t==1)
  h=[th(sum(W[t][j][k]*h[k] for k in range(2))+b[t][j]) for j in range(2)]
 z=sum(v[j]*h[j] for j in range(2))+c
 ok=(q==0 and z.a>0) or (q==1 and z.b<0)
 print('negative',seed,word,'verified',bool(ok),flush=True)
 assert ok
print('Remote interval proof checks: 8 positive, 4 negative PASS')
