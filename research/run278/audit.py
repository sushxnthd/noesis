import csv,glob,json,math
from fractions import Fraction as F
from pathlib import Path
from core import cert,repair,witness_wrong
from controls import controls
ROOT=Path(__file__).resolve().parent

def rows():
 files=sorted(glob.glob(str(ROOT/'checkpoints_part*.csv')))
 assert len(files)==4
 lines=''.join(Path(p).read_text() for p in files).splitlines()
 return list(csv.DictReader(lines))

def dyadic(original,edited):
 q=edited.copy()
 for i,(o,e) in enumerate(zip(original,edited)):
  if o==e:continue
  f=float(e);exact=F.from_float(f)
  if i==0 and exact<e:f=math.nextafter(f,math.inf)
  if i==3 and exact>e:f=math.nextafter(f,-math.inf)
  q[i]=F.from_float(f)
 return q

def main():
 out=[]
 for row in rows():
  seed=int(row['seed']);p=[F.from_float(float(row[k])) for k in ('a0','a1','a2','b0','b1','b2','v','c')]
  q=repair(p);d=dyadic(p,q);edits=[i for i in range(8) if p[i]!=q[i]]
  n=int(row['n']);sym=int(row['symbol']) if row['symbol'] else None
  assert not cert(p) and cert(q) and cert(d)
  assert witness_wrong(p,row['family'],n,sym) and not witness_wrong(q,row['family'],n,sym)
  assert len(edits)<=2
  r,s=controls(p,q,seed)
  out.append({'seed':seed,'epoch':int(row['epoch']),'original':[str(x) for x in p],
   'repaired':[str(x) for x in q],'dyadic':[str(x) for x in d],
   'edits':edits,'family':row['family'],'n':n,'symbol':sym,
   'random_controls':r,'same_coordinate_controls':s})
 summary={'models':len(out),'certified':len(out),'one_edit':sum(len(x['edits'])==1 for x in out),
 'two_edits':sum(len(x['edits'])==2 for x in out),
 'random_control_certified':sum(sum(x['random_controls']) for x in out),
 'same_coordinate_control_certified':sum(sum(x['same_coordinate_controls']) for x in out)}
 assert summary=={'models':11,'certified':11,'one_edit':8,'two_edits':3,'random_control_certified':24,'same_coordinate_control_certified':125},summary
 (ROOT/'derived_results.json').write_text(json.dumps({'summary':summary,'models':out},indent=2)+'\n')
 print(summary)
if __name__=='__main__':main()
