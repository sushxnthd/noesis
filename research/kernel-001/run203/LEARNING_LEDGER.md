# LEARNING ledger — Run203
The two evaluated checkpoints are actual Adam-trained streaming count-mod-three width-12 tanh RNNs from the fixed Run199/Run202 source artifact. Both attained 100% training accuracy. Run202 independently certified each checkpoint correct for all-zero inputs of arbitrary length.

**New mixed-input failure:** epoch400 first violates the output-congruence screen at max prefix depth 7, with the length-8 word `11100010` classified as 2 instead of 1. Epoch800 first violates it at max prefix depth 8, with length-9 word `110100010` classified as 2 instead of 1. These are separate checkpoint-specific witnesses, not a certified acquisition transition. The result explains why all-zero infinite-tail proofs do not imply full-alphabet algorithm acquisition.

**Unresolved:** no proof that either checkpoint is correct on every other word, no causal training intervention, no model-agnostic algorithm certificate.
