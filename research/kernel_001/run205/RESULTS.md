# NOESIS Run 205 — prospective full-alphabet certificate transfer

Frozen on research branch before training: four seeds 211/223/227/229, epochs 0,20,50,100,200,400,800; scalar input-gated tanh RNN trained by Adam on all-prefix parity over 64 length-six binary words.

**Primary criterion PASSED:** 6/8 frozen epoch-400/800 checkpoints have exact all-length parity certificates (seeds 223,227,229; seed 211 fails). Across all 28 checkpoints, 14 certificates accepted and independently reproduced by Fraction/Decimal and mpmath.iv verifiers. Both-symbol closure, base inclusion and strict output separation checked. Abstention is not a proof of incorrectness.

Training transitions: seed223 first certified epoch20; seed227 and seed229 first certified epoch100; seed211 never certified. This brackets acquisition in observed snapshots, not precise training time. All 14 certified checkpoints have 100% training accuracy and zero errors on 128 length-64 and 32 length-256 frozen random test sequences (all prefixes).

**Strong in-class negative control:** scalar gated tanh recurrence w=(1,-1), b=(-.0001,.0001), v=-1,c=0, h0=.5. It classifies EVERY binary word through length 803 correctly and misclassifies 0^804. This follows from monotone parity-normalized lower-envelope recurrence and is independently interval-verified. No sound all-length certificate can accept it. Developed after primary frozen test; exploratory control.

Limits: no claim of model-agnostic acquisition law; gating structurally facilitates parity. All-length certificates apply to exact-real evaluation of stored float64 parameters, not hardware floating-point execution. No unseen task transfer or causal intervention. Not a field-level breakthrough.
