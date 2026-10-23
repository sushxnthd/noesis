# NOESIS Run 373 — third-architecture precision falsification (23 Oct 2026)

**Single active kernel:** learned DFA-state retention under neutral cycles. **Scientific decision:** prespecified +2 numerical-instability-window transfer to a third gated architecture **FAILED**. Long-horizon precision sensitivity **replicated**, but neither a novel law nor architecture-level causation is established.

## Frozen experiment
- Frozen protocol SHA256: `a564f45049444035a7bd5423cfe0eddc8ad8400d3794f8d7c58d2da14eef9d93`; 16 unseen neutral cycles SHA256 `875657a8cf07d8d71295b17cc3429fb81c577fb7e00e47f9be137f49c6061b32`.
- 32 **fresh**, first-perfect symbol-conditioned LSTMs (16 per task), width 5, 258 parameters, 196 8-bit training strings/seed, Adam lr 0.035; all 32 reached perfect short-training accuracy. Two DFA tasks: count-ones mod 3 and count-'01' mod 3.
- Eight unseen 12-bit neutral cycles/task, three DFA-state representatives/cycle, forget-gate shifts 0,+1,+2,+3,+4 after n32. Independent Numba/NumPy float64, PyTorch float64 and PyTorch float32; 1,280 model-cycle-shift cases, 3,840 prefix trajectories, endpoints n32/n48/n256/n512.

## Prespecified primary FAILED
Float64 NumPy-vs-PyTorch n256 discordance per 384 task-B prefix trajectories:
- Shift 0: 0; +1: 16; **+2: 33**; +3: 46; **+4: 54**.
- Frozen claim required +2 exceed +4 by >=3 percentage points and seed-paired exact sign-test p<0.05. Observed **−5.46875 pp** (opposite direction), 3 seeds favor +2, 8 favor +4, 5 ties; one-sided exact **p=0.96728515625**.
- Task A n256 float64 discordances by shift 0..4: 0,12,22,15,14.
- This refutes transfer of the exploratory R372 +2 peak under the *specified LSTM forget-gate intervention*, not an architecture-invariant causal law. GRU/MGU update-gate and LSTM forget-gate interventions are not equivalent.

## Independently converged precision evidence
- Across both tasks, n256 independent float64 implementations disagreed in **212/3,840** prefix cases; n512 **252/3,840**. Baseline shift 0 had zero disagreements at both endpoints.
- 48 frozen-rule-selected/index-selected n256 cases agreed at **120 and 160 decimal digits**, as did 6 additional explicitly post-hoc task-B discordances (54/54 total). Six selected n512 cases also agreed at 120/160 digits. These are convergence checks, not universal exact-arithmetic certificates.
- Of the 24 frozen-selected float64-discordant n256 cases, Numba disagreed with converged high precision in 16, PyTorch float64 in 10; **two cases had a third, distinct high-precision class**. Two further three-way cases appeared in the six post-hoc task-B checks.
- Example: task A seed 42003, prefix `0`, neutral cycle `000000100110`, forget shift +2, n256: **Numba class 2, PyTorch float64 class 0, 120/160-digit class 1**.

## Reproducibility and limitations
Complete local archive: `NOESIS_R373_Reproducibility.zip`, SHA256 `8e02b7473e6b87b3a7da0461eca7e1381a04fee53717f45bd65925c51db6affa`. It contains frozen protocol/word list, source, all 32 checkpoints, full raw float64/float32 results, independent 120/160-digit checks, exact paired statistics, failed commands/corrections, vector figures and SHA256 manifest. **Raw evidence is not asserted to be in GitHub.**

Novelty unestablished. Existing finite-precision state-tracking, Lyapunov/RNN, automata-extraction and length-generalization work must be treated as strong prior art (Weiss 2018; Dan 2022; Muskardin 2024; Vogt 2024; Buitrago & Gu 2025; Metric Automata Theory 2025; Brandoit et al. 2026).

**Next within the same kernel:** retire universal +2-window hypothesis. Freeze a prospective *non-vacuous, precision-invariant finite-time perturbation-growth certificate* and test it against raw d32, readout margin, state coverage, local Jacobian, full-cycle cocycle singular values and DFA oracle on fresh seeds. No force push, no merge, no new branch.
