# THEORY ledger — Run 201 (2026-10-16)

**Frozen before suffix evaluation:** protocol commit `448ef7e285b29e7f3ab7e5e0f03c4751e11ba712`.

## Proven, conditional on exact archived trained parameters
Let `g_e(x)` be the strict argmax output class of the width-12 tanh RNN (seed 283, epoch e) after consuming x, and let `r(s) = number_of_ones(s) mod 3`.

For every integer `k >= 240` and **every** binary suffix `s` of length `1 <= |s| <= 4`:

- `g_400(0^k s) = r(s)`
- `g_800(0^k s) = (r(s)+1) mod 3`.

This is 30 infinite cylinder families, including 26 suffixes with at least one 1. It is stronger than the Run200 all-zero family, but remains a finite-suffix and one-training-trajectory theorem. **No global algorithm certificate.**

## Proof
Reuse and recheck Run200's all-zero exact-parameter interval proof: 240 finite prefixes; 14-step rational-box inductive closure, radius 1e-9; 14 output-separated phases. Each state after 0^k, k>=240, belongs to one of 14 certified phase boxes. From each box propagate each of 30 suffixes using outward-rounded interval arithmetic. All 840 epoch-by-phase-by-suffix cases have strict winning-class margins. There are no abstentions.

Independent checker uses Python Decimal directed rounding at 75 digits and exp enclosures from 115-digit correctly-rounded exp with +/-2 ulp safety, including independent base invariant verification. Minimum suffix margins across all phases/suffixes: epoch400 >4.3026, epoch800 >5.0905.

## Boundary
The base invariant was chosen post-hoc in Run200. Suffix enumeration and success criterion were frozen before Run201 suffix evaluation; this is not a held-out seed/architecture, and no novelty priority claim has been made. This result does not imply all-length correctness on arbitrary strings or a model-agnostic certificate.
