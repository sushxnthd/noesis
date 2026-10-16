import json
from pathlib import Path
import numpy as np
import torch
from run197 import Net,params,advance,logits
from spoof_control import verify
R=Path(__file__).resolve().parent

def test_frozen_rows():
    rows=json.loads((R/'CHECKPOINTS.json').read_text())['rows']
    assert [(r['seed'],r['epoch']) for r in rows]==[(s,e) for s in (241,251,257,263) for e in (400,800)]
    assert all(r['train_accuracy']==1.0 for r in rows)

def test_independent_result():
    r=json.loads((R/'INDEPENDENT_INTERVAL.json').read_text())
    assert r['minimality']=={'max_verified_length':14,'prefixes_checked':32766,
         'all_correct':True,'precision_decimal_digits':45}
    assert r['witness']['certified_wrong']
    assert r['witness']['witness']=='000000101010000'

def test_cross_task_abstention():
    r=json.loads((R/'RESULTS.json').read_text())
    assert len(r['rows'])==8
    assert all(all(t['reason']=='abstain' for t in x['certification_screens']) for x in r['rows'])
    assert next(x for x in r['rows'] if x['seed']==257 and x['epoch']==800)['finite']['length_64_random_all_prefix_correct']==128

def test_negative_control():
    assert verify()['length7_failures']==128

def test_torch_numpy_checkpoint():
    row=next(x for x in json.loads((R/'CHECKPOINTS.json').read_text())['rows'] if x['seed']==257 and x['epoch']==800)
    model=Net()
    with torch.no_grad():
        for name,p in model.named_parameters():p.copy_(torch.tensor(row['params'][name],dtype=torch.float64))
        x=torch.tensor([[int(c) for c in '000000101010000']],dtype=torch.long)
        z=model(x)[0,-1].numpy()
    p=params(row);h=np.zeros(12)
    for bit in x[0].tolist():h=advance(h,p,bit)
    np.testing.assert_allclose(logits(h,p),z,rtol=1e-12,atol=1e-12)
    assert int(np.argmax(z))==1