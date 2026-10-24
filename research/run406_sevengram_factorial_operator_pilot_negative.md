# NOESIS R406 — Seven-gram-matched factorial neutral-word operator pilot: frozen primary FAILED

**25 October 2026.** Same scientific kernel and persistent branch; authorized draft PR #22. This is a separate prospectively frozen **PILOT**, not a confirmatory replication. No new branches/PRs, force-push or merge.

## Prospective design and estimand

Before fresh training, froze `FROZEN_R406_DESIGN.json` SHA256 `fa54507a23591cfaefa3ab0e6f44e7f164e2d1c25170676bbb61514a8b89569c` and `FROZEN_R406_PROTOCOL.json` SHA256 `5f79985e0043ec917a6cf1d8e7477041d87e3ecdb4d0e418c249c1045deb70d1`.

For each model, exact prefix-end state x and two distinct 40-bit full-DFA-neutral words u,v, intervene with four 80-bit compositions uu, uv, vu, vv. Measure the complete factorial readout and latent interaction `I=Y_uu-Y_uv-Y_vu+Y_vv`. All four compositions have **exact overlapping 1–7-gram counts**, identical six-bit boundaries and full-DFA action. The signed contrast cancels any additive individual-position binary effect and any linear seven-gram-histogram response. It is an identifiable *two-slot word-composition causal interaction*, NOT a symbolic-path-only mediated effect: higher-order lexical and positional interactions remain confounded.

Trained 36 NEW LSTM/GRU/MGU-style networks × both DFA tasks × six disjoint shared seeds 99720–99725; 85 Adam updates, 196 matched length-eight strings, **36/36 short-perfect**, all ITT. Two unseen neutral word pairs per complete DFA state and two unseen prefixes/state. 648 paired contexts, 2,592 complete n0..512 trajectories, **1,329,696** suffix-one labels plus all signed margins, first-error horizons and n1 hidden/cell endpoints.

## Frozen pilot gate: FAILED, no confirmation

Conjunctive frozen feasibility required >=10% eligible n1 readout interactions with `|I_margin|>=0.01` **in each task**, >=2 architectures and >=3 seeds per task, >=12 task-A positive pairs, and >=8 task-B n1..64 class-discordant oracle-error cases across >=2 architectures/3 seeds.

* **Task A:** 9/216 (4.17%) margin-positive, **GRU only, seed 99724 only**, and four class-discordant oracle-error cases. Fails fraction, architecture, seed and 12-case gates.
* **Task B:** 77/432 (17.82%) margin-positive across all three architectures/six seeds; 84 class-discordant oracle-error cases. Passes task-B gates, but conjunctive primary still fails.

No threshold retuning or new confirmatory cohort. The original evaluator was interrupted after 492 in-memory cases, with 432 persisted. A deterministic key-based resume completed the remaining 216 without recalculating persisted keys; both implementations and logs are preserved.

## Independent evidence and exact negative identifiability result

Independent stdlib checks: 648/648 panels matched overlapping k-gram histograms for **each k=1..7**, 51,840/51,840 signed per-position contrasts exactly zero, 2,592/2,592 complete-DFA-neutral and oracle checks, 648/648 boundary checks. Frozen post-outcome verification selection SHA256 `ed639bf229f9b36a5f5189efa9db2b83c5afe4d7b70534661e938391e1d803b5`: independent pure NumPy reproduced 24/24 selected arms' n0..8 labels (max margin discrepancy 1.25e-14); pointwise mpmath at 120/160/220 digits reproduced **48/48** selected arm/precision n0..1 sequences (max margin discrepancy 6.67e-15). Not directed intervals, long-horizon exact-real arbitration or an invariant-set proof.

Separate **post-failure exploratory** operator audit protocol SHA256 `a01c24a772c0f3e450c8e4d3cb65b9c5d5d2563cec44dc37681d65d87aed5f75`. For maps `F_u,F_v` and `D=F_u-F_v`, exact `I_state(x)=D(F_u(x))-D(F_v(x))`, hence `||I||<=Lip(D)||F_u(x)-F_v(x)||` on the relevant segment. Crucial classical counterexample: affine scalar `F_u(x)=x/2+1`, `F_v(x)=x/4-1`, `x=0` gives factorial interaction **1/2** exactly. Thus nonzero interaction does **not** establish neural nonlinearity or DFA-memory mechanism.

Descriptive **in-sample task-B** AUROC: fixed-competitor margin interaction 0.9421, latent interaction 0.9535, n1 signed-margin baseline 0.9223, n0 margin 0.5351. This was computed **after the frozen pilot failed**, has contemporaneous four-arm access and no unseen predictive validation; not a new prospective success. Task A mostly has near-zero n1 interactions, so no cross-task replication.

## Decision, archive, next scientific step

First operator-factorial feasibility attempt **FAILED**. The exact factorial estimand is identified, but robust cross-task readout effects and novelty are not. A separately frozen next pilot could test shorter k=7-equivalent neutral words (minimum length 14, giving 28-bit rather than 80-bit compositions) on fresh disjoint seeds to test saturation as a possible task-A failure mechanism. After a second substantive failure, change mechanism; no posthoc rescue.

**Full 30-entry SHA256-verified local archive:** `/mnt/data/NOESIS_R406_Reproducibility.zip`; SHA256 `5ad74a9c38e045c21604d8763e922bf7771782112c509084d75979d72decc0fc`. Contains frozen protocols, 36 checkpoints and init hashes, all raw n0..512 labels/margins, original and resume scripts/logs, negatives, independent checks, operator counterexample and the exact R405 dependency ZIP. Raw is **not** on GitHub. Zero personal spend, no user's laptop. No publication-grade novelty.
