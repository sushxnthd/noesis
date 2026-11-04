# NOESIS R428 — exact phase-segment sparse readout obstruction

**2026-10-26. Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **FROZEN CONJUNCTIVE PRIMARY FAILED (4/9 gates)**. Retrospective, no new training, graph/radius/seed/word retuning, IEEE execution guarantee, or publication-grade neural novelty.

## Frozen design

Before reading R425 per-cut neural raw outcomes, the classical theorem, exact symbolic algorithm, 108-case quantitative protocol, and source/input hashes were frozen. Protocol SHA256 `1e0c635946a6d09eb9c6ebbb40a329b5ecb396db7715d7b2588f2d718ad84919`. All 108 immutable R418/R425 contexts ITT: 24 networks (LSTM/GRU/MGU, both DFA tasks, seeds99960..99963), all nine complete DFA states, existing 20-bit matched-gram full-neutral u/v words, n0/1/2 vs n16/32/512, 27,216 archived readouts. Fixed R427 outcome-blind oracle-greedy k=1/2/3/5 proper cuts with free t0/t20 boundaries.

## Exact classical sufficient condition and restricted lower bound

On an oracle-constant segment with correct class y, define competing gap `g_j(t)=z_y(t)-z_j(t)`. If verified adjacent variation bounds are `|g_j(t+1)-g_j(t)|<=L_{j,t}`, then `g_j(t)>=g_j(s)-sum L_{j,e}` for an observed anchor s in the SAME oracle-constant segment. Strictly positive bounds for all competitors certify that phase. **Do not interpolate across oracle-label changes.** Exact rational sharp examples and a changing-label counterexample verified (629 Fraction checks). For these zero-initialized LSTM/GRU/MGU hidden outputs, `h in [-1,1]^w`, giving a conservative exact-real, exact-dyadic-weight global bound `|g_j(t)-g_j(s)|<=2||R_y-R_j||_1`. This is a hidden-cube bound, not a tight neural reachability claim.

For the restricted segment-local sampled-anchor method, each oracle-constant segment requires a sampled phase (unless another independent bound is supplied). Exact minimum proper-cut hitting-set budgets, with t0/t20 free: TaskA states0/1/2 **8/12/8**; TaskB states0|0,0|1,1|0,1|1,2|0,2|1 **5/5/2/5/5/5**. Original frozen R427 greedy k5 cuts hit all segments in **only one of nine states**, TaskB1|0; none in TaskA. Independent streaming DFA 378 phase checks and exhaustive **643,672** smaller-cardinality cut sets confirmed the exact minima. These are lower bounds only for this restricted segment-local rule, NOT universal lower bounds for all sparse or cross-label neural verification methods.

## Frozen 108-case numerical feasibility: failed

All 108 cases evaluated; no new neural training. Number of phase readouts *candidate covered* by the conservative exact-dyadic readout-weight bound versus an explicitly **outcome-leaking** optimistic adjacent-variation bound, out of 27,216:

| k | Conservative candidate | Leaky optimistic |
|---|---:|---:|
| 1 | 3,211 | 7,700 |
| 2 | 4,235 | 9,930 |
| 3 | 5,268 | 12,154 |
| 5 | 7,376 | 15,337 |

**Zero** of 108 cases had all early n0..2 or all late n16/32/512 phase readouts candidate-covered by the conservative k5 bound. Even the outcome-leaking optimistic bound fully covered just 1/108 early and 1/108 late. Exhaustive all-cut observations show 70/108 early-all-correct and 72/108 late-all-correct. Zero observed false covered phase labels, but no full trajectory. Frozen gates **4 pass / 5 fail**. The conservative counts compare an exact-dyadic universal weight bound against **float64** anchor margins, so they are feasibility screens only, NOT directed-MPFR exact-real certificates. The optimistic comparison reads all unsampled phases and is NOT a sparse certificate.

## Independent audit, prior art, and next direction

Independent exact brute oracle/minimum-cut audit: 378 phase labels, 643,672 smaller subsets. Independent PyTorch recurrent implementation: 60/60 selected archived labels across both tasks/three architectures, max shifted-logit difference 1.9984e-15. No directed MPFR anchor validation was performed after the exact symbolic k<=5 cross-task obstruction. Prior art includes Lipschitz-margin neural certification (Tsuzuku et al. 2018, arxiv:1802.04034; Fazlyab et al. NeurIPS 2023), interval reachability and automata test design; no novelty claim.

**Decision:** retire this exact k<=5 segment-local sparse interpolation method; do not retune after seeing failures. Next R429 should investigate a distinct, pre-frozen causal neutral-transition-semigroup identifiability bound, not repeat R412/R423/R424 or enlarge graph geometry without mechanism evidence.

**Complete raw preservation:** `/mnt/data/NOESIS_R428_Reproducibility.zip`, SHA256 `45a2b599b4aec8bdd1d6d9b0f3145065ff3098cd7d4bcd761b560834d1689d60`, 21 SHA256-verified ZIP entries, including frozen protocols, source, all108 case results/negatives, exact and independent checks, logs, and immutable full R425 dependency with earlier nested checkpoints. Only this scientific note is committed to GitHub; raw archive remains local. No personal spend/laptop.