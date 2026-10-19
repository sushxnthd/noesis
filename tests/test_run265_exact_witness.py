"""NOESIS Run265: public CI exact-integer replay of representative witnesses."""
import subprocess
import sys
from pathlib import Path

def test_run265_exact_witness_subset():
    root=Path(__file__).resolve().parents[1]
    script=root/'research'/'run265'/'verify_ci_subset.py'
    completed=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True,timeout=60)
    assert completed.returncode==0,completed.stdout+'\n'+completed.stderr
    assert completed.stdout.count('PASS')==3,completed.stdout
