import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location('run149_independent_exact',Path(__file__).with_name('independent_exact.py'))
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
check=mod.check
class TestRun149(unittest.TestCase):
    def test_original_witness_fails(self):self.assertTrue(check(214,'0022222222222')['error_gt_tenth'])
    def test_intervention_witness_rescued(self):self.assertFalse(check(214,'0022222222222',3)['error_gt_tenth'])
    def test_transfer_counterexample(self):self.assertTrue(check(210,'02',3)['error_gt_tenth'])
    def test_control_without_clamp(self):self.assertFalse(check(210,'02')['error_gt_tenth'])
if __name__=='__main__':unittest.main()
