"""Run299 public exact proof regression (no external dependencies)."""
import subprocess
import sys
from pathlib import Path

def test_three_exact_trained_latch_certificates():
    root = Path(__file__).resolve().parents[1]
    script = root / "research/kernel_001/run299/verify_witnesses299.py"
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, check=True)
    assert result.stdout.count("EXACT_CERTIFIED") == 3
    assert "21832" in result.stdout and "21903" in result.stdout and "21926" in result.stdout
