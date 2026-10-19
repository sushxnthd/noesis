# THEORY ledger — Run265

Exact conditional failure criterion: for a fixed checkpoint, one-symbol prefix s in {SET, RESET} followed by HOLD, if the exact post-prefix trajectory enters a forward-invariant convex polygon inside a single ReLU mask, the restricted affine HOLD map has strict Jury stability, and its unique fixed point has task-incorrect output sign, then the trained network must eventually fail on that prefix+hold language. This is a sound negative certificate, not a sufficient positive certificate of a reusable full-alphabet algorithm.

Run265 froze SHA256 b69c0db0ee4bfa7c01b633285a8b7e13773f662b4f65c5822945e12e7cc58856 before replay. 74 pairs; 40 certificates independently exact-verified (21 wrong, 19 correct-attractor); 34 abstentions. Five deliberately corrupted proofs rejected. Among 21 wrong-attractor predictions, 19 first errors independently exact replayed; two later numeric candidates were not newly exact-replayed (the proof of eventual failure still independently passed).

Novelty unestablished; compare RNN polyhedral verification and formal-language generalization. A stable wrong attractor can be a preexisting trained failure rather than a new learning transition. No model-agnostic law or positive algorithm acquisition claim.
