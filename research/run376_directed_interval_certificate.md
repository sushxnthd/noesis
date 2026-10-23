# NOESIS R376 — directed-interval LSTM neutral-cycle certificate (23 Oct 2026)

**Scientific decision: the frozen n256 coverage gate FAILED.** The protocol fixed R374 indices 0,177,600,754; n=48/64/96/128/192/256; 80/160/320 decimal-digit outward-rounded interval arithmetic; success required >=2/4 certified baseline-and-perturbed n256 pairs. **Observed 0/4** at n256.

| Digits | n48 | n64 | n96 | n128 | n192 | n256 |
|---:|---:|---:|---:|---:|---:|---:|
| 80 | 3 | 1 | 0 | 0 | 0 | 0 |
| 160 | 4 | 4 | 2 | 0 | 0 | 0 |
| 320 | 4 | 4 | 4 | 3 | 1 | 0 |

**Bounded interval-certified transient witness:** R374 index 177, count-ones-mod3, LSTM seed 44004, neutral cycle `111010010010`, prefix `0`, forget-gate shift +4 after cycle 32, 10^-9 state perturbation at cycle 48: at n64 the baseline/perturbed readout classes are **(0,2)**; at n96 **(2,2)**. Both class pairs are certified at 320 digits by nonlinear interval enclosure; independently implemented Decimal120/160 recurrence matches. Thus an intervention-induced class split can disappear later under the same cycle. This is **not** proof of algorithm acquisition or a general dynamical law.

A second frozen row (754) certifies (0,2) at n96 and (1,2) at n128. Across all four cases, **60 certified individual class labels** agreed with independently implemented Decimal120; zero disagreements. A constant-readout LSTM sanity model was certified through n256 at 80 digits.

**Method:** mpmath.iv outward-rounded interval propagation of the complete nonlinear LSTM recurrence with exact serialized binary64 parameter values, exact real epsilon=10^-9, and strict separation of all three readout-logit intervals. Wide enclosures are terminated and marked **UNRESOLVED**, never treated as false or impossible. No n256 certificate was obtained for the four learned models. The interval implementation depends on the correctness of the mpmath.iv rounding library; no independent interval-library audit yet.

**Reproducibility:** frozen protocol SHA256 `e2d339cc5a303166bc69f065641cc6825c86b7f916d0aadd6cbbcaab3c5fed99`. Complete self-contained local archive includes R374 checkpoints and raw data, protocol, interval and independent Decimal code, all interval endpoints, guards, independent checks, negative logs, figure and manifest. **Raw artifacts are not uploaded to GitHub by this note.**

**Priority:** Ryou et al. (2020, arXiv:2005.13300), Zhang et al. (ECAI 2020, DOI 10.3233/FAIA200281), and Engelken et al. (PRR 2023, DOI 10.1103/PhysRevResearch.5.043044) predate this on recurrent verification/stability. No novelty claim for interval propagation.

**Next kernel intervention:** centered Taylor/affine interval enclosures with validated Jacobian remainder and reconditioning, then prospective n256/n512 coverage on unseen trained networks. No revival of R350–362 coordinate repair, no new branch, no merge.
