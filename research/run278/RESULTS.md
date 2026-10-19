# NOESIS Run 278 — exact post-training repairs

**Local and public CI: PASSED.** 11/11 sampled-perfect but exact-witness-wrong Run277 gradient-trained latch RNN checkpoints were repaired by post-training edits to at most two recurrent parameters. Eight needed one edit; three needed two. All rational and IEEE754 binary64 realizations passed independent SymPy all-length verification. Sampled accuracy remained 3396/3396 per checkpoint before and after repair.

Matched L1/cardinality random-coordinate controls: 24/352 certified (6.82%). Stronger same-coordinate random-sign controls: 125/352 certified (35.51%). These perturbations are correlated within 11 models, not 352 independent model trials.

GitHub Actions run 39334491942 PASSED: audit, independent checker, exact sampled-data replay, artifact upload. Repository branch research/kernel-001-run278-causal-repair, commit 4d9590ebee3abe8c5b6f7d5942a44783f7395606. Draft PR creation blocked by safety checks.

Source Run277 checkpoint SHA256 91fab4550b037a475673fe7d07b4c2ef73bb87b6ecb1c16565f0e884c71ae79b. Local pre-run protocol SHA256 364c5adcaec312db839538ed621913327f77f8f7ee7fdb5dc2e5fde1cfd29189. Run277 checkpoint metadata erroneously lists training length 20; executable train277.py uses T=12.

**Smallest claim:** An exact sufficient invariant can guide a one- or two-coordinate post-training intervention to repair all-length correctness in 11 previously gradient-trained scalar symbol-gated ReLU RNNs, without changing their sampled training predictions. This is retrospective, task-specific, and not a model-agnostic acquisition law.
