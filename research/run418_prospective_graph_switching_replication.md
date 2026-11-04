# NOESIS R418 — prospective graph-directed neutral-switching replication

**2026-10-25. Frozen prospective primary PASSED (10/10 conjunctive gates). No publication-grade novelty.**

## Pre-outcome freeze and cohort

Design SHA256 `82ddf32b58dd08f89b3daf4800a07748b3b8f4599c775cf19f27629ac7c97104`; protocol SHA256 `9e7877c30091f04910dcd452518aea0d8d2b0bb7676ba4cf2d2ec4c99f7e88ea`, both frozen **before new training**. Twenty-four fresh float64 ERM LSTM/GRU/MGU-style networks × two DFA tasks × four disjoint seeds 99960–99963, all ITT. Fifty Adam steps, 196 length-8 strings, every architecture-task mean short accuracy >=0.95. New 14-bit prefixes and two distinct 20-bit full-DFA-neutral words per complete DFA state, disjoint from R415–R417, exactly matched 1..5gram and four-bit boundaries. All three Task-A and six Task-B complete states represented.

Four history boxes `uu/uv/vu/vv`, radius scales 2/8/32 frozen. Directed 1024-bit MPFR RNDD/RNDU, exact binary64-dyadic serialized weights and centers, exact-zero entry enclosures after **prefix+u^16** and **prefix+u^14+v^2**, oracle-correct suffix-1 readout throughout all boxes, and eight uniform interval-Jacobian/residual edge inclusions. Classical graph induction gives arbitrary infinite switching safety over the two words **for the ideal exact-real network conditional on MPFR/backend correctness and only after either specified entry**. Not an IEEE/Torch repeated-execution theorem, not an arbitrary-prefix theorem.

## Primary and finite results

**24/108 graph certificates; 84 negatives; all ten frozen gates passed.** Task A 20, Task B 4; LSTM 15, GRU 5, MGU 4; seeds 99960:5, 99961:6, 99962:3, 99963:10. All positives used frozen smallest radius scale 2. Naive direct-interval graph-edge inclusion passed 5/108 on the same geometry, all a subset of the 24; edge-only baseline, not complete entry/readout certification or a frozen statistical superiority test.

All 108 contexts × two entries × six switching patterns were evaluated at **n0..512**, preserving 1,296 full trajectories and **664,848** Numba float64 classifications, neural states, margins, cross-entropies, odd/even and first errors. **Zero finite contradictions** in 288 certified-case trajectories. Nineteen trajectories first failed at n>=3, spanning eight cases; n0..2 was not a perfect finite failure predictor.

## Independent checks and exact negative controls

Independent stdlib audits passed 45 kgram, nine boundary, 18 neutral-word, 32,274 switched DFA-state and 4,599 suffix-1 oracle checks. MPFR directed arithmetic selftests **3,741/3,741**. Frozen selected six architecture-task cases × two entries × n0/n1/n2/n16 yielded **48/48** matching Numba/NumPy/Torch/120/160/220-digit labels; separate late n0/64/256/512 selection matched **8/8** phases. Independent 320-digit mpmath.iv post-primary audit matched **12/12 selected MPFR decisions** and **64/64 positive graph edges**, not all 24 positives.

Two **posthoc discovered** Task-B networks showed u-only and v-only finite readout retention through n512 but mixed switching errors from the same entry: GRU seed99962 state 2|0 hash-a first wrong n3 and still wrong n512; LSTM seed99963 state 2|0 alternating-vu first wrong n2. Separately frozen 120/160/220-digit checks matched finite results **162/162**; directed MPFR confirmed exact-real wrong-class readout at n3/n2. **The stronger posthoc requirement to certify BOTH pure-word trajectories safe for all future cycles FAILED 0/2** (GRU only u certified; LSTM only v). No exact-real infinite-pure-safety counterexample was proved. These outcome-selected observations are descriptive, not the prospective primary, and no thresholds were changed.

## Novelty, provenance and next direction

Four-node De Bruijn and path-complete graph certificates are classical: Ahmadi–Jungers–Parrilo–Roozbehani, *SIAM J. Control Optim.* (2014), DOI 10.1137/110855272; Angeli et al. (2016/17), arXiv:1612.03983; Philippe et al., *IEEE TAC* (2018), DOI 10.1109/TAC.2018.2863380. The result is **fresh prospective computational architecture replication of conditional exact-real certificates**, not a novel theorem, a neural-memory causal mechanism, a demonstrated predictor advantage, or IEEE execution proof. Task-B positives remain sparse.

Complete **201-entry SHA256-verified local archive** `NOESIS_R418_Reproducibility.zip`: `9ad71eaecaef5281d381b076cbad0c44df1854ee55d8578b54303bfc450be0c9`. Includes 24 new checkpoints, full raw, negatives, frozen protocols, source, independent checks, preserved initial errors, and immutable R417 dependency. Clean recursive rehydration of 12 nested archives and independent rerun of frozen primary analysis passed. **Full raw/checkpoints NOT on GitHub.** Zero personal spend; never user laptop; no new branch, PR, merge, or force-push.

**Next:** a separately frozen heldout **third neutral word** switching/graph-extension challenge with non-ceiling Task-B incidence and independent directed interval verification. Do not rescue the failed both-pure-all-future gate or recycle retired mechanisms.
