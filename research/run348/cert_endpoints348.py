import json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run340'))
from cert340 import certificate
rows=json.loads((P/'trajectories348.json').read_text())['rows']
end=[r for r in rows if r['epoch']==200]
cert=[{'seed':r['seed'],'support':list(certificate(r['p']))} for r in end if certificate(r['p']) is not None]
assert len(end)==192
assert [r['seed'] for r in cert]==[32098,32135,32158,32187]
(P/'endpoint348.json').write_text(json.dumps({'certified':cert,'n':len(end)},indent=2)+'\n')
print('certified',cert)
