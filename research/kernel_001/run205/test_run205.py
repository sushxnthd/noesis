"""Proof checker smoke tests; run from run205 directory."""
import csv,unittest
from pathlib import Path
from verify_logic import verify
R=Path(__file__).resolve().parent
class ProofTests(unittest.TestCase):
 def test_frozen_certificate_count(self):
  self.assertEqual(len(list(csv.DictReader((R/'CERTIFICATES.csv').open()))),14)
 def test_unsound_box_rejected(self):
  r=dict(w0='1',w1='-1',b0='-0.0001',b1='0.0001',v='-1',c='0')
  c=dict(even_lo='0.01',even_hi='0.9',odd_lo='-0.9',odd_hi='-0.01')
  with self.assertRaises(AssertionError):verify(r,c)
if __name__=='__main__':unittest.main()
