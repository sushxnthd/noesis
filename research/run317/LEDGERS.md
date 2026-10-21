# Run317 THEORY and LEARNING ledgers

THEORY: Exact rational proof: after first 1, the polyhedron h1=0, h0>=1, 0<=h2<=3*h0 is inductive for the edited recurrent network. All-zero words stay at zero and have negative logit. Positive words stay in the invariant and have positive logit with margin at least 1.239969841179. The original trained recurrent core has an exact length-11 opposite-label state collision; output-bias calibration cannot repair it. The mathematical technique is classical.

LEARNING: Seed 22642 epoch80 comes from gradient training on length-six latch examples. Only recurrent parameter A0[0,0] and output bias are changed in the intervention. The original trained network is NOT certified and the repair was designed retrospectively from its observed dynamics. This is a causal post-training intervention, not natural gradient acquisition or a model-agnostic certificate.

Initial mutation-control failure: setting b1[0]=+1 did not invalidate the certificate; this was a strengthening edit. It was replaced by b1[0]=-1 in local mutation tests; the failed assertion is preserved in the downloadable archive. Do not misreport all mutations as necessarily adversarial.

Single active kernel: distinguishing learned unrestricted algorithms from finite-range heuristics. The prior frozen retention predictor failed against loss. A new seed-disjoint prospective predictor is still required. Kill/reformulate after three substantive failures.
