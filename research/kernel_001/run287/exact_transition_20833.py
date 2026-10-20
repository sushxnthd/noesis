from fractions import Fraction as F
from itertools import product
P80=[-0.6138427093191439,-0.823044931001244,-0.9972897582059238,-1.6378483283617429,-1.5522559684077324,0.4359504961224479,-1.8481931629100599,-0.7660989019378981,-0.14325482151263025,-0.19803091448086377,-0.859690648591787,1.864139612211911,0.876756943261267,1.886940758787096,-1.855126115240311]
P120=[-0.6138427093191439,-0.823044931001244,-0.9972897582059238,-1.6380708094914982,-1.5849487289415358,0.3491844460192427,-1.8844701419824226,-1.399548822612954,-0.14325482151263025,-0.21470440281898054,-0.9260074341990987,2.574765042962899,0.9154532053125559,2.6631034750119404,-2.735661831465868]
L=[[0.,0.],[0.,2.574764042962899]]
U=[[0.,0.],[1000.,2.5747660429628993]]
def step(q,h,x):
 return [max(F(0),q[4*x+2*i]*h[0]+q[4*x+2*i+1]*h[1]+q[8+2*x+i]) for i in range(2)]
def logit(q,h):return q[12]*h[0]+q[13]*h[1]+q[14]
def verify():
 q=[F.from_float(x) for x in P80];h=[F(0),F(0)];s=0;first=None
 for t,x in enumerate([0]+[1]*12,1):
  h=step(q,h,x);s=0 if x==0 else 1-s
  if (logit(q,h)>0)!=bool(s):first=t;break
 assert first==13,first
 q=[F.from_float(x) for x in P120]
 ll=[[F.from_float(x) for x in row] for row in L]
 uu=[[F.from_float(x) for x in row] for row in U]
 assert all(ll[0][i]<=0<=uu[0][i] for i in (0,1))
 for s in (0,1):
  for h in product(*[(ll[s][i],uu[s][i]) for i in (0,1)]):
   assert (logit(q,h)>0)==bool(s) and logit(q,h)!=0
   for x in (0,1):
    y=0 if x==0 else 1-s;hh=step(q,h,x)
    assert all(ll[y][i]<=hh[i]<=uu[y][i] for i in (0,1))
 print('PASS: exact epoch80 counterexample and epoch120 unrestricted certificate')
if __name__=='__main__':verify()
