import json
from pathlib import Path

def test_frozen_seed_count():
    d=json.loads((Path(__file__).parent/'EPOCH800_COMPACT.json').read_text())
    assert len(d['rows'])==12
    assert [r[0] for r in d['rows']]==[659,661,673,677,683,691,701,709,719,727,733,739]
