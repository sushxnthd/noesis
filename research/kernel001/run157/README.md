# NOESIS Kernel 001 — Run 157 (2026-10-14)

**Precise question:** Can gradient-trained counters maintain the same ReLU activation mask for thousands of increment-only steps yet eventually exceed the fixed counting-error threshold?

**Frontier:** El-Naggar et al. (ICGI 2023) give exact one-cell ReLU counting conditions; Ryou et al. (CAV 2021) address recurrent polyhedral verification. No general novelty is asserted.

**Scalar criterion:** Rigorous first threshold crossing for at least one unchanged trained checkpoint, with an independent implementation.

**Competing explanation:** Float accumulation or an activation-mask change, rather than genuine learned computational drift.

**Cheapest falsification:** Outward-rounded Decimal interval recurrence on stored decimal parameters; every earlier increment-only prefix must have error strictly < 0.1.

**Publishable threshold:** Strongest spoof baselines, all-alphabet verification, frozen predictions on unseen architectures, independent check, primary priority audit. Not met.

**Learning relevance:** Two untouched Adam-trained, width-four ReLU models (1200 steps, all ternary length-six strings, latent neutral penalty 0.1) have exact-real late increment-only failures. This changes evaluation practice, not a universal law.

**Kill condition:** After three failed strengthening attempts, retire or reformulate the task-coupled all-alphabet candidate.

**THEORY ledger:** Seed 217 first increment-only failure at n=10783; seed 221 at n=16745. Directed-rounding interval certificates establish every earlier increment-only word below 0.1. Neither mask changes along the tested trajectory. Not globally shortest ternary failures or all-length proofs.

**LEARNING ledger:** Train MSE seed217=3.482043686249675e-15; seed221=8.156092400481022e-18. Frozen original checkpoint SHA256 hashes included. Retrospective two-checkpoint result, one architecture; no prospective prediction.

**Run:** `python research/kernel001/run157/certify157.py research/kernel001/run157/RUN157_SEED_217.json research/kernel001/run157/RUN157_SEED_221.json --output RESULT157.json`

Independent cross-check: `pip install mpmath && python research/kernel001/run157/independent157.py research/kernel001/run157/RUN157_SEED_217.json research/kernel001/run157/RUN157_SEED_221.json`

**Smallest supported claim:** Stable finite-prefix activation masks cannot certify algorithmic counting even when a gradient-trained model generalizes thousands of times beyond training length. Not a field-level breakthrough.
