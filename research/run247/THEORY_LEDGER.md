# THEORY ledger — Run247
KNOWN: Run246 had 30/48 exactly witnessed incorrect endpoints and 18 exact-search abstentions.
NEW KNOWN: 11 of those 18 have concrete exact-dyadic failure witnesses at lengths 8–12. Each was checked by two separately implemented exact evaluators. Consequently 41/48 endpoints are now proved incorrect (30 prior + 11 new).
UNKNOWN: the remaining seven checkpoints. Finite candidate scanning through length 12 does not establish correctness, nor completeness of exact search.
LIMIT: float64 scan generates candidate sequences; exact rational arithmetic verifies only candidate counterexamples. We make no shortest-exact-witness or universal claim.
PRIOR ART: van Rossem & Saxe ICML2025 (https://proceedings.mlr.press/v267/van-rossem25a.html); Dave et al. NeSy2025 (https://proceedings.mlr.press/v284/dave25a.html); Dankowiakowski & Ronca NeurIPS2025 (https://proceedings.nips.cc/paper_files/paper/2025/hash/c03c2e3e2ad8057aefc3da880476784d-Abstract-Conference.html).
Smallest supported claim: adversarial finite-length testing resolved 11 of 18 verifier abstentions as incorrect on genuinely gradient-trained ReLU models. No model-agnostic acquisition law follows.
