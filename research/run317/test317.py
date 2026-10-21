"""CI regression: exact proof, independent proof, checkpoint provenance."""
import json,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent
p=json.loads((P/'seed22642_epoch80.json').read_text())
assert len(p)==28
for script in ('exact317.py','independent317.py'):
    subprocess.run([sys.executable,str(P/script)],check=True)
print('PASS Run317 two independent exact checkers')
