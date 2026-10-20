#!/usr/bin/env python3
import unittest,json
from pathlib import Path
from audit301 import evaluate
from independent301 import check
class Test301(unittest.TestCase):
 def setUp(self):
  p=Path(__file__).resolve().parent
  self.rows=json.loads((p/'input/rows300_public.json').read_text())
 def test_exact_sign_flip(self):
  self.assertTrue(evaluate(self.rows)['sign_flip'])
 def test_independent(self):
  check(self.rows,evaluate(self.rows))
 def test_known_labels_unchanged(self):
  r=evaluate(self.rows)
  self.assertEqual((r['known_correct'],r['known_incorrect'],r['unresolved']),(17,175,192))
 def test_same_hypothetical_prevalence(self):
  r=evaluate(self.rows)
  for k in ('G','L'):self.assertEqual(len(r['completions'][k]['hypothetical_positive_seeds']),40)
if __name__=='__main__':unittest.main()
