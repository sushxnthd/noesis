"""Corrupted-certificate negative controls, both arithmetic engines."""
import json,copy
from pathlib import Path
R=Path(__file__).parent
ns={'__name__':'proof_lib','__file__':str(R/'proof_check.py')}
s=(R/'proof_check.py').read_text()
exec(compile(s[:s.index('\nresults=[]')],str(R/'proof_check.py'),'exec'),ns)
certs=[r for r in json.load(open(R/'PROOFS.json'))['results'] if r['status']=='CORRECT']
cands={(r['seed'],r['epoch']):r['result'] for r in json.load(open(R/'CANDIDATES.json'))['results']}
assert len(certs)>=4
out=[]
for r in certs:
 c=copy.deepcopy(cands[r['seed'],r['epoch']]);key=sorted(c['boxes'])[0]
 c['boxes'][key]['lo']=['-1']*3;c['boxes'][key]['hi']=['1']*3
 a=ns['check_candidate'](ns['ROWS'][r['seed'],r['epoch']],'iv',c)
 b=ns['check_candidate'](ns['ROWS'][r['seed'],r['epoch']],'decimal',c)
 assert a['status']==b['status']=='ABSTAIN',(r,a,b)
 out.append({'seed':r['seed'],'epoch':r['epoch'],'iv':a,'decimal':b})
(R/'CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(out),'corrupt controls')
