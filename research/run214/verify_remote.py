import json,sys
from mpmath import iv
sys.path.insert(0,'research/run214')
from verify_run210 import check,ex,th
D=json.load(open('research/run214/RUN214_CHECKPOINTS.json'))
rows={r['seed']:r for r in D['rows'] if r['epoch']==200}
positive=(977,991,997,1019,1021,1031,1033,1051,1063,1097,1103,1117,1129,1163)
for seed in positive:
 status=check(rows[seed])['status'];print('positive',seed,status,flush=True)
 assert status=='CERTIFIED'
words={1009:'100000000001',1013:'1000001',1049:'1'+'0'*77+'1',1061:'10000001',1069:'100000001',1093:'101',1123:'1000000',1151:'000'}
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
print('Remote interval proof checks: 14 positive, 8 negative PASS')
