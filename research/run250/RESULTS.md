# Run250: frozen model-conditioned diagnostic versus strong ablation

48 newly gradient-trained 4D tied-transition ReLU RNNs; 34 perfect finite-fit, first 24 eligible tested. Sixteen candidate queries per arm. Independently exact-replayed incorrectness witnesses: model-conditioned Jacobian 23/24; hold-biased random 15/24; uniform random 4/24; **fixed-tail nonadaptive 24/24**.

Prespecified random-control advantage (23-15)/24=0.33333 passes the >=0.25 threshold, but the fixed-tail ablation strictly beats the purported model-conditioned mechanism. **No model-specific mechanistic superiority established.** This is a prospective evaluation pitfall: weak random baselines exaggerate apparent value.

Seed 12018: surrogate chose lengths [10,8,12,16,6,20,24,32] and missed its long-horizon error. Independent exact arithmetic: input 1+0^91 is correct; input 1+0^92 is incorrect. Fixed-tail discovers a witness at length 128. This is a boundary within one word family, not a globally minimal counterexample.

Local archive SHA256 5b16890dc28037ef212ca1a55dbd9f7c2e92e917e8c02b96dcf0dda1837bb366. No all-length certificates or acquisition transitions established.