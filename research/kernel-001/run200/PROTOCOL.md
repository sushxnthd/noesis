# NOESIS Run 200 — post-hoc infinite zero-tail training transition

Status: **post-hoc discovery, exact verification pending**. This branch is isolated from main. Source checkpoints: Run199 `CHECKPOINTS.json`, SHA256 `5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32`, originally prospectively frozen for a DIFFERENT task.

## Eight-field active Kernel 001
1. **Question:** Can exact interval induction establish a training-dependent, infinite family of mod-3 prefix errors in stored gradient-trained checkpoints?
2. **Literature frontier:** Prior RNN verification, automata extraction, and neural parity acquisition already establish finite-state and model-specific certificates; no model-agnostic algorithm-acquisition law is claimed.
3. **Success:** independently executable directed-interval proof of every `0^k` classification at both epochs for seed 283, with a finite exact transition length K and an invariant for all k>=N.
4. **Competing explanation:** float64 periodic orbit or a finite-run transient mistaken for a genuine all-length property.
5. **Cheapest falsification:** exact stored-parameter interval evaluation of prefixes and interval-Taylor induction on an attracting periodic orbit.
6. **Publishable threshold:** independently checked theorem plus new mechanism-derived prediction on unseen model/architecture, beyond known verification.
7. **Learning threshold:** both checkpoints from one documented gradient-training trajectory, exact change in an infinite behavior family, and held-out finite diagnostic results reported separately.
8. **Kill condition:** if sound induction cannot be established, or if exact signs contradict the candidate, record negative and do not assert an infinite theorem.

## Audit boundary
The target (seed 283, epochs 400/800, repeated zero input) was selected **after** inspecting Run199 outcomes. It is NOT a frozen prospective hypothesis. Numerical scans suggested epoch 400 is correct for every positive zero-prefix and epoch 800 becomes incorrect at length 15. These are **unverified candidate claims** until the proof code passes.

Use rational intervals for the stored binary64 weights, explicit finite prefix checks, a rational center, and a sound Taylor-remainder bound for a power of the zero-input transition. Keep THEORY and LEARNING ledgers distinct. Preserve failed attempts and code revisions.
