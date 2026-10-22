import json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'run340'))
from cert340 import find,check
from independent340 import verify
for seed,epoch in [(29034,37),(29067,72),(29091,50)]:
 p=json.loads((P/'checkpoints'/f'{seed}_epoch{epoch}.json').read_text())['p']
 support=find(p)
 assert support is not None and check(p,support)[0] and verify(p,support)
 print(seed,epoch,'unrestricted parity correctness independently certified',support)
