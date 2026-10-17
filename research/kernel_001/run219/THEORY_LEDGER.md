# THEORY — Run219

The finite suffix score is invariant to every strictly sign-preserving output reparameterization, unlike raw/normalized/logit-ratio diagnostics falsified in Runs216–218. It is **not** a sufficient all-length correctness certificate: arbitrary finite sets can be spoofed outside their tested horizon.

For scalar input-gated tanh recurrence h'=tanh(w_x h+b_x), exact-real binary64 parameters were certified via outward-rounded interval reachability. Seven epoch100 incorrect checkpoints have first-error lengths 2 or 5; 5 epoch100 positive checkpoints have two-class inductive invariants. Both independent proof methods passed locally. Source proof checker: preserved Run208 verify_exact.py / verify_independent.py / run208_verify.py / run208_decimal_check.py, with source provenance in Run209 archive.

No new general theorem. The frozen superiority criterion FAILED.
