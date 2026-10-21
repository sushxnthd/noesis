from pathlib import Path
import subprocess,sys
def test_run320_exact():
    script=Path(__file__).resolve().parents[1]/'research/kernel_001/run320/run320.py'
    p=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True)
    assert 'PASS 24/24' in p.stdout
