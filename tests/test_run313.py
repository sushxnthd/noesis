"""Run313 regression tests run by the base GitHub Actions workflow."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'research'/'kernel001'/'run313'
def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/(name+'.py'))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
def test_run313_primary(): assert load('reproduce313').run()
def test_run313_independent(): load('check313').check()
