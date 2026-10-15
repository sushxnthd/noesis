# NOESIS Kernel 001 / Run 187 — frozen learning-to-induction challenge

Frozen 2026-10-16 before training. One active kernel: identify a **learned**, task-relevant, inductively closed representation, as opposed to a finite-horizon spoof. This run changes from balanced-counter family to an unseen parity task because bounded-state parity is a reusable algorithm when it works for *all* binary strings. No claim of parity novelty or model-agnostic law.

1. **Question:** Can ordinary gradient training of generic untied tanh RNN on finite parity traces produce a two-region inductive certificate for all binary strings?
2. **Primary frontier:** Weiss et al., ACL 2018 (https://aclanthology.org/P18-2117/); Delétang et al., ICLR 2023 (https://openreview.net/forum?id=De4FYqjFueZ); El-Naggar et al., ICGI 2023 (https://proceedings.mlr.press/v217/el-naggar23a.html).
3. **Exact success:** >=1 of four frozen seeds (101,103,107,109) achieves sound two-box all-word certificate, independently outward-interval checked, output margin >=0.1, no hardcoded transition.
4. **Competitor:** architecture or auxiliary loss hardcodes parity; finite heuristic passes short tests. Use generic tanh RNN, no state-clustering loss.
5. **Cheapest falsification:** Test two-box closure on frozen checkpoints; if no box closes, reject certificate (not learned behavior).
6. **Publishable threshold:** positive proof, two independent checkers, unseen architecture transfer, matched controls, prior-art audit and spoof rejection.
7. **Learning relevance:** demonstrate training checkpoint transition uncertified -> certified, with heldout behavior.
8. **Kill:** three failed substantive attempts -> reformulate.

Frozen model: h[t+1]=tanh(W h[t]+U[x[t]]+b), h0=0; y[t]=v·h[t]+c; odd parity positive. Hidden width 8; float64; exhaustive 64 length-6 words, prefix BCE; Adam lr .02, 1200 steps; save epochs 0,100,300,600,1200; deterministic CPU seeds 101/103/107/109. Supporting evaluation: 4096 length-12 words, 128 deterministic length-128 words per seed. Two boxes seeded from training-state coordinate extrema and h0, iterated under interval image hulls until closure or rejection. Acceptance requires all 4 transition inclusions and whole output margin >=0.1, with exact-binary64 interpretation and independent checker. No threshold relaxation after results.

Controls: untrained snapshots, finite-prefix spoof rejected by all-length condition. Backups inactive: matched-difficulty counter checkpoints; finite-jet spoof audit. No paid compute or laptop.
