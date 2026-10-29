# R417: graph-directed neutral-word switching certificate — retrospective feasibility

**2026-10-25 | SAME NOESIS kernel | Retrospective only | No publication-grade novelty**

Frozen protocol SHA256: `1fd8e252c72a149a269abd0d501376300c8936a75208b3ac902023e10e595e90`. Exactly 18 immutable R415 trained-RNN contexts (3 architectures × 2 DFA tasks × 3 seeds 99940–99942), with all complete DFA states covered in aggregate, and distinct 20-bit full-state-neutral words matched on overlapping 1..5-grams and boundaries. No new training or outcome-dependent threshold changes.

## The classical graph-directed certificate

Construct four neural-state boxes `B_uu,B_uv,B_vu,B_vv` around states reached from the exact-zero prefix after `u^14` followed by the indicated two-word histories. For each `a,b,c ∈ {u,v}`, certify the edge `F_c(B_ab) ⊂ int(B_bc)` using 1024-bit directed MPFR exact-dyadic weights, uniform interval Jacobians and mean-value residual inequalities. Require strict correct-oracle suffix-1 readout throughout all four boxes. Exact-MPFR entry is checked for `prefix+u^16` in `B_uu` and `prefix+u^14+v^2` in `B_vv`. This does **not** certify entry after `prefix+v^16`.

Under these conditions, induction on the two-word suffix proves correct readout under **every infinite switching sequence** after either specified entry, for the exact-real maps conditional on the MPFR backend. This is a classical graph-invariant-set theorem, not a new neural-memory theorem or an IEEE/Torch floating-point execution guarantee.

## Frozen pilot

**PASS 4/18**, with 14 negatives retained. Task A 3, Task B 1; LSTM 3, GRU 0, MGU-style 1; all three seeds represented. All predeclared gates passed at their minimum. Four positives:
- `lstm|ones|99941|1`, scale 2
- `lstm|ones|99942|2`, scale 2
- `lstm|substring01|99942|1|0`, scale 8 (scale 2 failure preserved)
- `mgu|ones|99940|0`, scale 2

Comparator: R416 single-common-box pilot certified **0/18** on these identical cases. Three graph positives had both R415 pure-word certificates; the Task-B graph positive had neither. Different certificate expressivity is not proof of novel retention dynamics.

## Independent checks

- Pure stdlib: 90 exact 1..5-gram matches, 18 boundary matches, 36 neutral-word checks, 64,548 switched-state checks and 9,198 suffix-1 oracle checks, zero failures.
- All 18 × 2 entry histories × 6 switching patterns × n0..512 = **216 full trajectories, 110,808 classifications**. All four certified cases yielded **48/48 error-free finite trajectories**. No errors after n2 first appeared in this finite cohort; early n0..2 readout baselines already distinguish observed failures.
- Six SHA-selected case IDs × two entries × four phases: **48/48** NumPy/PyTorch/120/160/220-digit labels agree (Numba also agrees at early phases), maximum Torch–220digit state difference 1.45e-15.
- Separate post-primary frozen independent 320-digit mpmath.iv audit: **6/6** selected positive/negative decisions and **32/32** graph-positive edges agree with directed 1024-bit MPFR. The audit is descriptive and not a fresh prospective cohort.
- Existing MPFR arithmetic selftests: **3,741/3,741** pass.

**Preserved descriptive-only checker error:** first finite checker used pre-suffix rather than suffix-1 DFA oracle, creating spurious contradictions. Its full invalid raw/summary/source/log and the corrected run are retained in the reproducibility archive. Frozen MPFR graph outcomes were unaffected. Initial import failures and resumed unique-key graph run also preserved.

## Prior art, limitations, and next test

Graph-labeled switching certificates and interval mean-value enclosures are classical; see Ahmadi et al. (2011), arXiv:1111.3427; Angeli et al. (2016), arXiv:1612.03983; Lee, Dullerud & Hu (2020), Automatica 116:108923. No novel neural mechanism, prospective fresh-model replication, or publication-grade result is claimed.

Next R418: freeze fresh disjoint seeds, neutral words and prefixes **before training**; test graph certificates across both DFA tasks, all complete states, three architectures, and seed clusters, with predeclared positive/negative incidence and comparison against pure-word, common-box, early-margin/CE/d32 and finite switching baselines. No retuning if frozen primary fails.

**Full raw, source, checkpoints via immutable R416→R415 dependency, negatives, frozen protocols and audits are NOT in GitHub.** Complete 73-entry SHA256-verified local archive: `/mnt/data/NOESIS_R417_Reproducibility.zip`; SHA256 `f2e1eba129db5b1a346b872a7621eb2f0b2834f9e1350949c4d7555de282e70c`. Zero personal spend or user-laptop access.
