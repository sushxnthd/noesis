# LEARNING ledger

Exact full-batch GD on all 63 words length <=5, M=8: Q=61/21, eta=21/244, initial loss 61/84, final loss 0.

- (-1/4,3/4) -> (0,1): finite-cap heuristic, first count error length 9, zero-test error length 17.
- (3/4,-1/4) -> (1,0): exact all-length count.
- Both have the same gradient (-61/21,-61/21). Since training features u=v, readout difference b-a is conserved under equal-step vanilla GD.
- Negative result: fixed recurrent transition contains a correct algorithm already; only the output head is trained. Initializations are deliberately selected. No spontaneous algorithm acquisition.
- Wildcard: min-norm (1/2,1/2) fails count but passes all-length zero test. The task output specification matters.
