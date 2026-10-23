# Run 377: recentered nonlinear perturbation enclosure (negative result)

**Date:** 2026-10-23  
**Active kernel:** learned DFA-state retention under neutral cycles.  
**Frozen protocol SHA256:** `fc1d94f0f7022be5c543e606321e7a4020481c2409ff0e3b95db4fcc096fa313`

## Precommitted test
Four previously frozen LSTM cases (R374 rows 0, 177, 600, 754), 160 decimal digits, endpoints 48/64/96/128/192/256. Primary success required at least **2/4 paired baseline/perturbed readout certificates at cycle 256**, with no independent Decimal120 disagreements. This was a verification-method experiment, not new training-seed replication.

## Result: FAILED
Paired certified counts at n=48,64,96,128,192,256: **[1, 0, 0, 0, 0, 0]**. The primary was **0/4**. At the same 160-digit precision, the preceding R376 natural interval verifier certified **[4, 4, 2, 0, 0, 0]**. The proposed method was strictly worse at short horizons.

The implementation follows arbitrary-precision center trajectories with outward-rounded, coordinatewise nonlinear perturbation bounds, including local activation derivative bounds and explicit center-local rounding residuals. The positive coordinatewise error recurrence discards cancellation and directional correlation, and rapidly overestimates uncertainty. Uncertified endpoints are **unresolved**, not incorrect network predictions.

Two individually certified labels agreed with an independent Decimal120 implementation (0 disagreements). A constant-readout zero-weight LSTM sanity test certified both trajectories at all six endpoints through n256. No new architecture-level or causal claim is supported.

## Scientific decision
This and R376 are two consecutive failed certificate-strengthening attempts. **Retire naive natural intervals and recentered coordinatewise Lipschitz bounds as flagship approaches.** The next intervention must preserve directional error correlations through validated Taylor/affine models with reconditioning, or dual readout-margin enclosures. Precommit a new coverage/cost gate before testing. If the next certificate attempt fails, reformulate the certificate mechanism.

The complete frozen protocol, source, raw per-case logit enclosures, independent checker comparisons, negative results, and integrity manifest are preserved in the local archive `NOESIS_R377_Reproducibility.zip`. This GitHub note does **not** imply that raw evidence was uploaded to GitHub. No force push or merge.

## Relevant priority controls
Ryou et al. (2020), arXiv:2005.13300; Zhang et al. (ECAI 2020), DOI 10.3233/FAIA200281; Jacoby, Barrett & Katz (ATVA 2020); Verisig 2.0 (CAV 2021). No novelty is claimed for recurrent interval verification or error recentering.
