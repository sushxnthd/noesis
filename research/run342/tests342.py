import json,unittest
from pathlib import Path
from score342 import auc,deficit
P=Path(__file__).resolve().parent
class TestRun342(unittest.TestCase):
 def test_protocol(self):
  d=json.loads((P/'trajectories342.json').read_text())
  self.assertEqual(d['seeds'],list(range(31000,31128)))
  self.assertEqual(len(d['rows']),128*201)
 def test_frozen_failure(self):
  m=json.loads((P/'outcomes342.json').read_text())['metrics']
  self.assertEqual((m['n_positive'],m['n_negative'],m['n_ambiguous']),(88,40,0))
  self.assertAlmostEqual(m['delta_auc'],-.11875,places=9)
  self.assertFalse(m['frozen_success'])
 def test_exact_witnesses(self):
  d=json.loads((P/'exact_failures342.json').read_text())
  self.assertEqual(d['verified_count'],40)
  self.assertEqual(sum(x['length']>=9 for x in d['records']),4)
 def test_auc_ties(self):self.assertEqual(auc([0],[0]),.5)
 def test_deficit(self):self.assertEqual(deficit([0.]*45),1000.)
if __name__=='__main__':unittest.main()
