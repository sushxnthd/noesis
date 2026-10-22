import json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run340'))
from cert340 import certificate,verify
from independent340 import check
for seed,epoch in [(29034,37),(29067,72),(29091,50)]:
 p=json.loads((P/'checkpoints'/f'{seed}_epoch{epoch}.json').read_text())['p']
 support=certificate(p)
 assert support is not None and verify(p,support) and check(p,support)
 print(seed,epoch,'unrestricted parity correctness independently certified',support)
