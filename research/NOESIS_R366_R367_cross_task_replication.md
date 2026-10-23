# NOESIS Runs 366–367 — Cross-task neutral-suffix retention replication

Date: 2026-10-23. Research evidence, not a novelty or all-length certificate.

## Prospective question

Does the gated-versus-ungated neutral-suffix retention contrast from count-ones-mod3 transfer to the distinct six-state count-'01'-occurrences-mod3 DFA? Can it survive equal learning rate and matched short-training cross-entropy?

DFA representatives: '1' (class 0), '01' (class 1), '0101' (class 2). Appending 1^n preserves all three labels.

## Run 366: same training strings and Adam learning rate

48 width-10 ungated Elman networks (253 parameters) trained from independent initializations on the identical per-seed 196 length-eight strings as 48 existing width-6 gated networks (273 parameters), with Adam lr=0.035 in both cohorts. All 48 Elman models reached perfect short-prefix training accuracy.

Among 22 pairs jointly eligible (at least two of three diagnostic prefixes correct at suffix length 32), 11 gated models acquired a new error by suffix length 256 and 0 Elman models did. Paired excess failure risk +50.0 percentage points; 95% paired seed-bootstrap CI [+27.3,+68.2] pp; exact one-sided discordant-pair p=0.00048828125. The frozen primary gate passed.

## Run 367: stronger short-CE matching

Retrained all 48 gated models from their original initialization and Adam state. For each seed, selected the earliest post-perfect checkpoint whose short-training CE was <= its paired Elman first-perfect CE. All 48 matched; original first-perfect epochs reproduced 48/48. Mean gated CE 0.01456 versus Elman CE 0.02148.

Among 22 jointly eligible seed pairs, the result persisted unchanged: 11 gated-only new failures, 0 Elman-only, 11 neither. Paired risk difference +50.0 pp, CI [+27.3,+68.2] pp, exact p=0.00048828125. The frozen primary gate passed. Independent NumPy/Numba/PyTorch checkers matched 672 predictions across 16 seed pairs, maximum checked gated hidden-state discrepancy 2.96e-13.

## Interpretation and limitations

This is now a replicated architecture-dependent retention contrast on TWO distinct DFA tasks, with identical per-seed training inputs, near-matched parameter counts, equal Adam learning rate on the second task, and short-training CE matching on both tasks.

It does NOT establish that gating itself causes the effect. Width, recurrence parameterization, optimization trajectories and eligibility selection remain confounds. Only one neutral suffix family per task and finite 256/512 horizons were tested. A prior pilot-frozen hidden-distance ratio diagnostic failed to transfer to ungated Elman models. Publication-level novelty remains unestablished.

Full frozen protocols, raw trajectories, model checkpoints, per-seed results, statistical analysis, independent checkers and vector figures are preserved in the NOESIS R363–R367 reproducibility archive generated during the research run. Do not merge until the full raw archive is uploaded and independently reviewed.