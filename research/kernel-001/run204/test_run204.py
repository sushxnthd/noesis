from independent_finite_lemma import enumerate_all
def test_combinatorial():
 assert enumerate_all()=={"classifiers":729,"perfect":1,"quotient_violations":216,"violations_with_perfect_labels":0}
def test_source_imports():
 import ast
 from pathlib import Path
 for f in ("check_first_error.py","verify_interval_first_errors.py"):
  ast.parse((Path(__file__).parent/f).read_text())
