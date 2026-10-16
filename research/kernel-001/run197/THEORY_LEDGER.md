# THEORY ledger — NOESIS run 197

**Sound result:** An independent 45-decimal-digit outward-interval checker verified that the stored float64 weights of a gradient-trained 12-unit tanh RNN (seed 257, epoch 800) classify all 32,766 nonempty binary words of lengths <=14 correctly for prefix sum modulo 3, and misclassify exactly one of the 32,768 length-15 words, namely `000000101010000` (true residue 0, predicted residue 1). Thus its **shortest incorrect input length is exactly 15** under exact-real evaluation of stored binary64 parameters. This is not an all-length theorem.

**Certificate transfer result:** The frozen Run 196 residue/suffix coordinatewise interval-box template was applied without adaptation at k=6 and k=8 to all eight new modulo-3 checkpoints. All 16 screens closed but lost output separation; minimum floating output margins were negative. **Certified positives: 0/8.** These are proof abstentions, not proofs of algorithm failure. No rigorous box verification was invoked on non-positive candidates.

**Competing explanations:** (1) actual learned modulo-3 behavior is finite-range; at least seed 257 epoch 800 has a certified failure at length 15; (2) fixed interval-box abstractions are too coarse to certify even networks that may be correct for all lengths. The current experiment does not distinguish these for the other checkpoints.

**Adversarial spoof:** a length-6 capped modulo-3 function passes all 126 nonempty training-horizon words and fails all 128 length-7 words. This is an evaluation control, not a neural learning result.

**Novelty:** No claim of novel RNN certification theorem. Learned parity and RNN verification have substantial prior art. The precise model-specific shortest-failure witness is new to this experiment but not a field-level advance.
