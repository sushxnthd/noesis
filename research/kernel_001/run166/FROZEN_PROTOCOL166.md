# NOESIS Kernel 001 — Run 166 frozen protocol (pre-outcome)

**Question.** Does a one-cycle, task-coupled affine transition extrapolation identify a delayed failure beyond the previous 1024-cycle evaluation horizon in *unchanged gradient-trained* ReLU counters, with an exact first-failure certificate and stable activation masks?

**Primary literature frontier.** El-Naggar et al., ICGI 2023, https://proceedings.mlr.press/v217/el-naggar23a.html, proves single-cell counter indicator conditions and reports learned near-counters failing; El-Naggar et al., EACL SRW 2023, https://aclanthology.org/2023.eacl-srw.15/, studies linear-counter conditions. Stability/extrapolation are not presumed novel.

**Preselection (outcome-free for new horizon).** Run 165's 28-model table was inspected. Both independent seed-224 checkpoints had no failure through 1024 cycles and had the highest frozen affine-risk scores among 1024-cycle nonfailures in their respective 14-model cohorts. Selection is conditional on this existing data, **not** a random held-out test. Exact source files: `checkpoints/checkpoints_local/CHECKPOINT_SEED_224.json` and `checkpoints/remote_checkpoints/CHECKPOINT_SEED_224.json` in the Run 165 archive. No checkpoint changes.

**One exact success criterion.** 2/2 checkpoints have first failure on `0^6 (01)^k` for integer `1025 <= k <= 20000` at strict `|output-6| > 0.1`, with a provably constant pair of ReLU masks through the first failure and an affine recurrence predicting **the same first failure k**. The first-failure claim must use interval-enclosed arithmetic for exact decimal-parameter semantics (all previous cycles certified safe), not float64 alone.

**Strongest competing explanation.** The trivial baseline of linearly extrapolating initial one-cycle error and initial offset may predict the same clock; this run cannot establish superior AUC or a general algorithm-acquisition law. Report its clock alongside the affine prediction, whether better or worse.

**Cheapest decisive falsification.** Independently simulate the two frozen checkpoints for 20,000 cycles with float64, check every activation mask; verify threshold crossings with an outward-rounded integer fixed-point interval implementation using all JSON weights as exact decimal rationals, and a separately coded high-precision decimal checker.

**Publishable threshold.** At least two genuinely unseen architectures/tasks or training distributions, frozen mechanism-derived predictions, strong spoof baselines, independent checkers, primary-priority audit, and remote CI. Run 166 alone does not meet this.

**Learning relevance threshold.** Both models must be *unchanged gradient-trained* checkpoints. The result must revise how long-range generalization of trained systems is evaluated, rather than merely establish an automata identity.

**Kill condition.** Kill this delayed-clock subhypothesis if either checkpoint changes mask before failure, does not fail by 20,000 cycles, or the interval checker cannot certify first crossing. If successful but trivial linear extrapolation is equally accurate, do not promote the affine diagnostic; retain only the evaluation-horizon counterexample. Three consecutive failures to strengthen the active kernel force reformulation.

**Execution semantics.** Exact decimal rational weights from JSON; recurrence `h <- ReLU(Ah+E[token])`; `h0=0`; output `w·h`; 0 increments, 1 decrements, 2 neutral. The fixed-point interval checker encloses the exact real dynamics. Separate float64 and decimal controls must be labelled as numerical evidence, not exact proofs.

**Ledgers.** THEORY: interval-certified first failure and masks only within the specified language. LEARNING: evaluation-horizon failure on unchanged trained checkpoints, not proof of exact algorithm acquisition.

**Backup kernels (inactive):** (i) task-quotient bisimulation obligations; (ii) interval-certified multi-token gain bound. Wildcard probes cannot affect this frozen evaluation.
