# NOESIS Run 398: prospective interval-validated neutral-cycle period-two dynamics (24 October 2026)

**One kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Frozen conjunctive primary FAILED; do not retune.** No novel general theorem or publication-ready claim.

## Prospective protocol and fresh holdout

Frozen symbolic design SHA256 `fd2ea83a34e787a8a2fc2260b2e4ab125d6637c3af6f2a76add071ab780ebb99`; frozen protocol SHA256 `54a078a889cc9f47df13fa833190d62196735d75c3782353475992e7f7466a75`, both written before new model training. Archived R397 cases were used only for separate interval-method pilot calibration.

Trained **48 fresh LSTM/GRU/MGU-style models** across two DFA tasks and eight shared seeds 99000–99007; 47/48 short-perfect, all ITT. Evaluated **5,184 new full-state-neutral n0..64 trajectories** with novel 10-bit prefixes and 40-bit word compositions exactly matched on overlapping 1–5-grams and four-bit endpoints. Full raw labels, margins, weights, source, negative results and frozen protocols are in the local archive, **not GitHub**.

Frozen screening found eight alternating cases across three seeds. At most one per architecture/task/seed was selected, yielding three candidates. The frozen interval proof used a 2^-80 infinity box and required strict F²-inclusion, a uniform Jacobian contraction bound below 0.5, F(X) disjoint from X, and different strictly separated suffix-one readout classes.

| Fresh candidate | Directed interval ||D(F²)||∞ upper | Frozen certificate |
|---|---:|---|
| LSTM, task B, seed 99002 | 0.0440937924320483 | **PASS** |
| LSTM, task B, seed 99003 | 4.41536774594e-9 | **PASS** |
| MGU-style, task A, seed 99000 | 2.00812073015e18 (wrapping at frozen radius) | **FAIL** |

All three predetermined stable-label controls failed the two-class period-two criterion. **Only 2/3 certificates passed, both LSTM/task B; required >=3 and >=2 architectures and tasks. Conjunctive primary FAILED.** An **exploratory post-failure** MGU certificate passes at radius 2^-90 (bound 0.0696757), but is NOT a frozen-primary success.

## Narrow mathematical result: an indefinitely alternating learned readout

For the fresh **LSTM task-B seed99002**, an independently checked directed interval propagation **from the exact zero state through the 10-bit prefix and 64 neutral 40-bit cycles** enters the certified 2^-80 attracting box. The enclosure is verified at 90 and 120 interval digits. On this box, F² maps strictly into itself and has ||D(F²)||∞ < 0.044094; F(X) and X are disjoint, and suffix-one readout classes are rigorously 0 and 2 respectively. By the classical Banach contraction theorem, a genuine attracting full-state period-two orbit exists, and the **specific zero-initialized prefix trajectory alternates classes 0 and 2 forever from cycle 64** under exact real evaluation of the frozen binary64 weights. The symbolic DFA suffix-one oracle is always class 0. This is a **case-specific, conditional computer-assisted infinite-horizon counterexample**, not a new universal theorem.

The second LSTM and exploratory MGU have local orbit-existence certificates but **no certified prefix-to-basin entry**; natural interval propagation inflated. All claims are conditional on the mpmath.iv outward interval backend. Independent Arb/MPFI revalidation remains outstanding.

## Checks and limitations

- 540 independent full-state-neutrality and 540 overlapping five-gram-family equivalence checks, zero failures.
- Independent pure NumPy vs Numba: **96/96** selected labels agree; PyTorch autograd Jacobians lie within interval derivative bounds.
- All **9/9** selected 120/160/220-digit finite n512 continuations match Numba. High-precision traces alone are not orbit proofs.
- **Important audit:** an initial pilot used default 15-digit mp endpoint arithmetic, invalidating tiny-box construction. Corrected final proofs use independent mp.mp.dps>=120 and mpmath.iv.dps>=90, include center-rounding uncertainty, and were rerun. Invalid pilot outputs are preserved and flagged in the archive.
- Prior art includes Casey 1996, Tino/Horne/Giles 1995/1998, Omlin/Giles 1996, and classical validated periodic-orbit proofs. **No novelty or publication readiness claimed.**

**Full 141-file SHA256-verified local archive:** `NOESIS_R398_Reproducibility.zip`, SHA256 `bafa758767aa7cc80fd259c8f21eafa856874084d63d8c85d317b960b1525f6c`. Full note: `NOESIS_R398_Research_Note.md` in archive.

**Next:** a separately frozen R399 fresh-seed test may use R398 only as disclosed pilot to fix tighter interval radii, require independent interval backend, cross-architecture/task replication and prefix-to-basin reachability. After a second failed primary, change mechanism. Keep PR #21 DRAFT and unmerged.
