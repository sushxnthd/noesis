# Run 194 — frozen negative transfer result

Protocol commit c1f2cae4047500b394e3ecca5f260544481b2dc4 preceded holdout evaluation. Source checkpoint SHA256 540afe1a1e8e27a6b445c367179ed120e626cb33399980b17b415a111c0cc51f. Full raw local result SHA256 5457c6eea04c4e5fbb7fbb507ec76c3038be7e9082331455562d37bf4f9f2572.

| Seed | Beam first difference | Beam evaluations | Random successful trials / 100 |
| --- | --- | ---: | ---: |
| 137 | none through 24 | 2430 | 8 |
| 139 | length 10, 1010101011 | 638 | 92 |
| 149 | length 4, 0010 | 30 | 65 |
| 151 | none through 24 | 2430 | 0 |

Frozen success criterion FAILED: 0/4 qualifying seed pairs. Local tests 5/5 passed. Directed interval checking confirmed the two beam witnesses. Random trial 25 found seed-137 length-15 word 100000000000001, with epoch-300 negative (correct even parity) and epoch-600 positive (incorrect); exact-parameter interval signs verified. The drift beam missed this behavioral change despite 2430 evaluations. Post-hoc alternative scores also failed seed 137, excluded from frozen result.

THEORY: no new all-length certificate. Finite-horizon drift cannot certify learned algorithmicity.
LEARNING: continued gradient training changed some longer-prefix correctness while drift beam failed to detect it. This is a concrete diagnostic failure, not proof of all-length algorithm loss.

Retire absolute-logit-drift beam as a useful algorithmicity diagnostic. Preserve negative result. Complete raw outcomes and original checkpoint JSON are in the Run 194 local reproducibility archive; GitHub-hosted retraining workflow should independently regenerate checkpoints and raw trials.
