"""Public CI regression: exact wrong-attractor polygons."""
import subprocess,sys
from pathlib import Path
def test_run265_exact_invariant_subset():
 root=Path(__file__).resolve().parents[1]
 script=root/'research'/'run265'/'verify_ci_invariant_v2.py'
 p=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True,timeout=120)
 assert p.returncode==0,p.stdout+'\n'+p.stderr
 assert p.stdout.count('PASS exact invariant')==3,p.stdout
