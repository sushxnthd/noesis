"""Metadata and source-integrity checks; no claims about remote training replay."""
import ast
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def test_source_parses():
    ast.parse((HERE/'independent_reproduction.py').read_text())

def test_frozen_negative_result():
    d=json.loads((HERE/'RUN181_SUMMARY.json').read_text())
    assert d['total_snapshots']==48
    assert d['fit_matched']==30
    assert (d['positives'],d['negatives'])==(9,21)
    assert d['auc']['neutral_probe_D']==d['auc']['baseline_B']==d['auc']['train_mse']==1.
    assert d['auc_improvement']==0.
    assert not d['primary_success']
    assert len(d['fail_to_pass_transitions'])==5
    assert d['independent_mismatches']==0
