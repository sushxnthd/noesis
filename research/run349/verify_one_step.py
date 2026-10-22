from verify_witness import prove,WITNESSES
from verify_horizon import prove_separator
if __name__=='__main__':
    assert all(z>0 for z in prove(82,WITNESSES[82]))
    assert prove_separator(83,23)
    print('Exact one-step readout-repairability transition: epoch 82 impossible; epoch 83 possible on 2644 frozen words.')
