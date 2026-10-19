# THEORY ledger — Run269
The frozen prefix-(HOLD)^n-terminal-switch generator returned no errors for the unresolved trained checkpoint seed 18605 at epoch 600, with 247 prefixes and n=0..4096. This negative bounded result is not a correctness certificate.

A separate exploratory full-alphabet breadth-first enumeration found errors at length 14. An exact dyadic-integer C++ checker subsequently enumerated all 7,174,452 nonempty words of lengths 1..14 (sum of 3^1 through 3^14): zero errors for lengths 1..13 and exactly three errors at length 14. The first lexicographic witness is 11111111112000 (ten SETs, RESET, three HOLDs). Two other length-14 witnesses are 11111111120000 and 11111111200000. An independently implemented Python Fraction replay verified all three and rejected false first-error claims at position 13.

This is a shortest counterexample under the exact stored binary64 parameters and stated zero-state latch semantics, not a proof about the pre-rounding optimizer state or any other model. The result demonstrates that a short-prefix hold/switch generator can miss a failure that exhaustive all-symbol search discovers. Exhaustive enumeration, finite-horizon closure, and asymptotic attractor analysis must not be confused with unrestricted correctness certification.

Primary-priority caveat: exhaustive model checking and RNN verification are established methods (e.g. Ryou et al., CAV 2021). The specific trained-checkpoint witness is a negative experimental result, not a new general theorem.
