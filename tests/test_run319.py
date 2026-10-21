import subprocess,sys
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'research/kernel_001/run319'
def test_exact_gauge_audit():
 for script in ('orbit319.py','conjugacy319.py'):
  subprocess.run([sys.executable,str(p/script)],check=True)
