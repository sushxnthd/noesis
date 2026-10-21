# LEARNING ledger — Run313

Seed 22242, width-3 ReLU recurrent network, gradient-trained on persistent-latch. The checkpoint arrays were extracted without modifying weights from the 384-seed Run304 cohort. Epoch20 sampled accuracy was 0.8333333333333334; epoch80 sampled accuracy was 1.0. These sampled values are not used as evidence of unrestricted correctness.

**Exact representation transition:** At epoch20 the network forgets a leading 1 after five trailing zeros: h(100000)=h(000000)=0. This erasure persists under any common suffix, so no readout repair can restore the lost bit. At epoch80 the original model is exactly correct at every finite length. This is a second independently audited trajectory-level representation-acquisition witness alongside seed 22241, not a prospective cross-seed predictor.

No causal learning intervention, training-loss comparison, task-family transfer, or field-level breakthrough is established.
