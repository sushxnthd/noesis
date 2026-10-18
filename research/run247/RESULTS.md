# NOESIS Run247 — successful adversarial falsification

The prospectively frozen threshold of >=8 new exact counterexamples passed: 11/18 previously unresolved, gradient-trained 4D ReLU networks were proved incorrect on ternary inputs of lengths 8–12. All 11 had 100% finite training accuracy. Two independent exact-dyadic implementations agreed for each witness. Total known incorrect Run246 endpoints increased from 30/48 to 41/48; seven remain unresolved. This changes evaluation interpretation: many box-verifier abstentions reflected learned finite-range heuristics rather than correct infinite-state implementations.

Public CI replay PASSED: https://github.com/sushxnthd/noesis/actions/runs/39137985957 . Raw outputs: GitHub Actions artifact 12140950307; durable witness manifest and exact replay code in this branch. Source checkpoints SHA256 b0a31428609da72d9aef54606d61d47d2e22c2bd70dc9412df4f5b3ac7237991 .

Limitations: float64 enumerates candidates; exact fractions validate only proposed counterexamples. No all-length correctness, no model-agnostic law, and no guarantee that the seven no-witness models are correct even through length 12 in exact arithmetic. Draft PR creation rejected by connector checks. This is an evaluation-method result, not a field-level breakthrough.
