import json
from pathlib import Path
P=Path(__file__).resolve().parent
word='010011001100100'
p=json.loads((P.parent/'run210/checkpoints/seed_773.json').read_text())['params']
print(word, p['c'])
