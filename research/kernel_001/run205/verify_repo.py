import csv
from pathlib import Path
from verify_logic import verify
R=Path(__file__).resolve().parent
rows={}
for path in R.glob('CHECKPOINTS_*.csv'):
 seed=int(path.name.split('_')[1].split('.')[0])
 for r in csv.DictReader(path.open()):rows[seed,int(r['epoch'])]=r
cert=list(csv.DictReader((R/'CERTIFICATES.csv').open()))
for c in cert:assert verify(rows[int(c['seed']),int(c['epoch'])],c) is None
print('EXACT_CERTIFICATES_PASSED',len(cert))
