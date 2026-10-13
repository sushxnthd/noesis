from research.kernel_001.run139.verify_compact import evaluate

def test_run139_trained_rays():
    rows=evaluate()
    assert len(rows)==8
    assert all(r['first_failure'] is not None for r in rows)
    assert {r['dim'] for r in rows}=={2,3}
    assert {r['dtype'] for r in rows}=={'torch.float32','torch.float64'}
