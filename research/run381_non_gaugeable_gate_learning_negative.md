# NOESIS R381 — Frozen gate-learning mechanism fails (24 Oct 2026)

**Scientific status:** Third successive negative gate-intervention test since R378. The prespecified causal direction **FAILED**; retire uniform gate-offset and gate-gradient-freeze interventions as flagship mechanism claims. This does **not** establish a new law of algorithm acquisition.

## Prospective, non-gaugeable intervention

The frozen protocol SHA256 is `ccb79718d01e27d66897454f37a391844ae03c20eda650bfd939e0271fb79372`. Independently trained 16 matched seed triplets (8 count-ones-mod3, 8 count-'01'-mod3). Each triplet has exactly identical 258-parameter initial LSTM functions, training strings, hidden width, Adam schedule, and 160 updates. Arms: control; zero forget-gate weight/bias gradients for updates 0–39; or zero input-gate gradients for updates 0–39. Both masks affect 60 coordinates and are released after update 40. All seeds retained, including non-first-perfect.

Holdout: 3 DFA-state representatives/task × 3 new frozen full-state-preserving neutral cycles/representative × 3 arms × 16 seeds = 432 model-cycle conditions, evaluated to n256. Symbolic full-state preservation verified independently.

**Frozen primary:** Forget-mask nontrivial-cycle accuracy minus input-mask accuracy <= -0.08, negative seed-bootstrap CI, exact paired one-sided p<.05, and per-task mean short-CE difference <=.01. Conjunctive.

**Observed:** Forget minus input = **+0.0625** (95% paired seed bootstrap **[+0.0104,+0.1250]**), exact one-sided p for the predicted negative direction **1.0000**. Control/forget/input correct on nontrivial cycles: **87/96, 92/96, 86/96**. Count-ones task was ceiling 48/48 in every arm; all differences were on count-'01'. Short-CE matching passed at per-task mean level, but some individual seed CE differences remain. Posthoc reverse-direction one-sided p=0.0625; **not confirmatory**.

## Independent verification and limits

- 432 full Numba float64 conditions × 257 complete-cycle endpoints = 111,024 predictions.
- Independent PyTorch recurrence disagreed on one n256 classification; high-precision 120/160/220/300 digits agreed with Numba (input-mask class 0, PyTorch class 1), demonstrating another model-specific numerical discrepancy.
- 18 prespecified stratified conditions and 30 separately identified posthoc treatment/implementation-discordant conditions were recomputed at 120/160 digits; all 48 agreed between precisions and with Numba at n256. Six prespecified 220-digit checks and one adversarial 300-digit witness also agreed.
- Independent torch.nn.LSTMCell check: 2,880 single-step comparisons, max absolute hidden/cell discrepancy 8.88e-16.
- **Only 48/432 n256 conditions have 120/160-digit checks**; full-panel statistics remain numerically provisional. No interval-certification or new theorem is claimed here.

**Decision:** R379, R380, and R381 are three successive failed mechanism-strengthening attempts. Retire this intervention family, preserve the overarching DFA-retention kernel, and reformulate around full-cycle-map basin capture and readout-invariant regions. The next prospective design must distinguish contraction/separation theory already developed by Brandoit et al. (2026), and must test a specific causal boundary or sharp certificate rather than posthoc gate correlations.

The **complete frozen protocol, source, checkpoints, raw data, independent checkers, exact statistics, logs, negative results, and figure are preserved in the separately SHA256-verified local reproducibility archive**. The raw archive is not uploaded to GitHub. No force push or merge. Existing branch and draft PR #21 only.
