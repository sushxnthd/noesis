# NOESIS Run 202 — frozen held-out induction transfer

Source: Run199 CHECKPOINTS.json SHA256 5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32. Discovery seed 283 excluded.

| Seed | Epoch | Frozen screen | mpmath proof | Independent Decimal | Certified all-zero behavior |
|---|---:|---|---|---|---|
| 293 | 400 | pass | pass | pass | correct k=1..26, wrong (class 1) for all k>=27 |
| 293 | 800 | **fail** (state 14-step delta 0.7240) | abstain | not applicable | numerical class 0 through k=320; **not certified** |
| 307 | 400 | pass | pass | pass | correct (class 0) for every k>=1 |
| 307 | 800 | pass | pass | pass | correct (class 0) for every k>=1 |
| 311 | 400 | pass | pass | pass | correct k=1..9, wrong (class 1) for all k>=10 |
| 311 | 800 | pass | pass | pass | correct k=1..10, wrong (class 1) for all k>=11 |

All five successful all-length proofs use 95-digit outward interval arithmetic, exact binary64 parameter interpretation, 240 certified finite prefixes and 14-step rational-box induction (radius 1e-9). Five independent directed-Decimal checks passed locally. The sixth checkpoint failed the *precommitted numerical candidate gate* and was not assigned an all-length class.

**Frozen primary criterion: FAIL.** Five of six certified (threshold three), but no certified within-seed **eventual class** change (required one). Do not count the numerical seed293 epoch800 class as certified. No model-agnostic algorithm-acquisition claim.

**Additional exact training observation:** seed311 epoch400 fails all-zero strings starting at length 10, while epoch800 fails starting at length 11. Optimization repaired exactly one all-zero input length (10), but left the entire infinite tail k>=11 incorrect. Both have 100% training accuracy. This is an independently checked model-specific change, not an unbounded algorithm-acquisition transition.

**Decision:** Kill zero-tail phase proof as the primary acquisition diagnostic under the frozen kill condition. Preserve it as a sound auxiliary model-specific verifier. Reformulate active Kernel 001 toward task-quotient invariants that can certify output behavior despite noncontractive hidden-state dynamics. That reformulation is a hypothesis, not yet validated. One active kernel only.

**Reproduction provenance:** GitHub Actions Run199 evidence artifact `noesis-run199-evidence`, run 38894405432, artifact 12043032970, available until 2027-01-14. Local full certificate files, original and independent proof scripts, and failure traces are preserved in the Run202 evidence archive. The Run202 GitHub branch must not be merged until CI reproduces both proofs and complete artifact persistence is established.
