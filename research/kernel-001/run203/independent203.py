"""Run203 independent directed-Decimal witness verification."""
import json,hashlib
from pathlib import Path
from decimal203_core import D,qfloat
R=Path(__file__).parent
def check_word(row,word):
 p={k:[[qfloat(v) for v in a] for a in row['params'][k]] if k in ('W','U','V') else [qfloat(v) for v in row['params'][k]] for k in ('W','U','V','b','c')}
 h=[D(0) for _ in range(12)]
 for bit in word:
  h=[(p['b'][i]+p['U'][int(bit)][i]+sum((p['W'][i][j]*h[j] for j in range(12)),D(0))).tanh() for i in range(12)]
 z=[p['c'][i]+sum((p['V'][i][j]*h[j] for j in range(12)),D(0)) for i in range(3)]
 wins=[i for i in range(3) if all((z[i]-z[j]).lo>0 for j in range(3) if i!=j)]
 assert len(wins)==1
 i=wins[0]
 return {'word':word,'predicted':i,'truth':word.count('1')%3,'min_gap_lower':str(min((z[i]-z[j]).lo for j in range(3) if j!=i))}
if __name__=='__main__':
 path=R/'CHECKPOINTS.json'
 assert hashlib.sha256(path.read_bytes()).hexdigest()=='5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32'
 rows={(x['seed'],x['epoch']):x for x in json.loads(path.read_text())['rows']}
 out=[]
 for s in json.loads((R/'SCREEN203.json').read_text()):
  w=s['witness'];words=[w['u'],w['v'],w['u']+w['symbol'],w['v']+w['symbol']]
  checks=[check_word(rows[s['seed'],s['epoch']],word) for word in words]
  assert checks[0]['predicted']==checks[1]['predicted']
  assert checks[2]['predicted']!=checks[3]['predicted']
  out.append({'seed':s['seed'],'epoch':s['epoch'],'witnesses':checks,'status':'PASS'})
 (R/'INDEPENDENT203.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out)
