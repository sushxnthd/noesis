from pathlib import Path
import runpy

def test_run292_exact_neuron_duplication():
    p = Path(__file__).resolve().parents[1] / 'research/kernel_001/run292/test_run292.py'
    runpy.run_path(str(p))['test_run292_exact_neuron_duplication']()
