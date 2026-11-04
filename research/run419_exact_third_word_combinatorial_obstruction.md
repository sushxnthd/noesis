# NOESIS R419 — exact heldout third-word obstruction (negative)

**Frozen symbolic feasibility FAILED: 5/9 complete DFA states eligible versus frozen ≥7/9.** No neural third-word certification, no new training, no retrospective threshold rescue, and no R418 checkpoint selected using outcome information. This is an exact design-specific combinatorial obstruction, **not** a novel neural-network theorem.

## Pre-outcome freezes

- Symbolic design SHA256 `c7bc9ba02ac726b9ba69526e999626875afb5e3dc9aecc6acfae20ccb9902a14`.
- Retrospective neural protocol SHA256 `49785b369a6e03f10fa006e3184cb90eb813d50f9d2d23d3a70a0c73bddfee90`.
- Immutable R418 prefixes and distinct 20-bit full-DFA-neutral words `u,v`; a third `w` had to preserve exact overlapping 1–5-gram counts and first/last four bits, preserve complete DFA state, be absent from R415–R418 word sets, and be lexicographically first eligible. No relaxed control permitted.
- Gate: at least seven of nine complete DFA states eligible **before** neural certificate testing. Failed; all 108 intended model/state contexts remain unevaluated for R419 neural outcomes.

## Exact integer results

| DFA state | Distinct words with exact 5-grams and fixed boundaries | New third words | Exact 4-gram matched words |
|---|---:|---:|---:|
| Task A 0 | 2 | 0 | 48 |
| Task A 1 | 2 | 0 | 6 |
| Task A 2 | 2 | 0 | 8 |
| Task B 0\|0 | 8 | 6 | 12 |
| Task B 0\|1 | 2 | 0 | 6 |
| Task B 1\|0 | 8 | 6 | 10 |
| Task B 1\|1 | 9 | 7 | 9 |
| Task B 2\|0 | 6 | 4 | 18 |
| Task B 2\|1 | 8 | 6 | 18 |

For **all three Task-A states and Task-B state 0|1**, the complete 20-bit fixed-boundary, exact-5-gram equivalence class consists of exactly the two existing `u,v`. A third word meeting the frozen controls **does not exist** for those four states. This is not a general impossibility for other word lengths or pairs.

An exact integer Euler-trail dynamic program on the 4-gram de Bruijn multigraph counted all nine equivalence classes. An independent brute-force implementation enumerated all **36,864** fixed-boundary middle-string candidates (4096 per state), reproducing all nine counts and matching-word SHA256 hashes. Candidate-level raw flags and negative results are archived.

## Separately frozen mathematical audit

Post-failure secondary freeze SHA256 `0906ba86bb24a8b6da8de94e4f1ca9c2d3c81c0106ceec7dc86b1b30cf`; exact-theorem audit freeze SHA256 `79faa4ba0ed61219b7b9115824de7edf13231779163ddc60bb8deebfe56bfeb1`.

**Elementary classical lemma:** If two equal-length binary words have the same first/last `k−1` symbols and identical overlapping `(k−1)`-gram histograms (`k≥2`), the L1 distance between their `k`-gram histograms is a multiple of **4**. If different, distance is at least 4.

Proof: write `D(vb)` for the difference in `k`-gram counts on directed edge `vb`, with `v` a `(k−1)`-gram. Equal lower-order counts and terminal boundary give `D(v0)+D(v1)=0`; let `t_v=D(v0)=-D(v1)`. Incoming conservation and the initial boundary imply `t_{0s}+t_{1s}=0` for each `(k−2)`-gram `s`. Hence `||D||_1=2 Σ_v|t_v|=4 Σ_s|t_{0s}|`.

For all four states without an exact third word, the minimum 5-gram L1 mismatch among third words matching 1–4-grams and boundaries is exactly **4**. This is a descriptive relaxation audit, **not** a R419 rescue. An independent exhaustive finite audit checked **36,164** eligible word pairs across lengths 9 and 10 and `k=2,3,4,5`, finding zero counterexamples. The identity is classical de Bruijn flow conservation; no novelty claim.

## Interpretation, preservation and next direction

The R419 frozen third-word generalization challenge is **structurally infeasible** across both tasks under the selected exact lexical controls, before neural computation. R418's previously successful two-word graph certificate primary is unchanged. Do not retune k=5 to k=4 and reclassify R419. Next: independently characterize complete neutral-word equivalence classes and finite-data semigroup identifiability, freezing any new neural mechanism separately only after cross-task feasibility.

Full reproducibility archive includes original frozen protocols, exact DP, all 36,864 raw candidate records, independent enumeration, 36,164-pair audit, error/recovery log, negatives, source, and immutable R418 archive with prior checkpoints. Raw files stay off GitHub. No personal spend, no user-laptop access, no new branch/PR, no force push/merge.