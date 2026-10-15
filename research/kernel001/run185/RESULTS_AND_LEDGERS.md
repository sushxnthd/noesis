# Run 185 — exact minimal balanced-word phase split

Frozen protocol commit: e66f448dd8f3b3ae9cacc4802bfd1960cd8ad6c3.
Source: original Run181 trained checkpoint width=7 seed=409 epoch=200, unchanged. Prefix 000000; target count 6; threshold 0.1. Every tested word is balanced and repeated.

| Length | Words | Exact all-k safe | Exact eventually fail | Mask-unclassified | All first 32 pass |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 2 | 0 | 2 | 0 | 2 |
| 4 | 6 | 0 | 6 | 0 | 6 |
| 6 | 20 | 2 | 18 | 0 | 20 |
| 8 | 70 | 5 | 65 | 0 | 70 |
| 10 | 252 | 14 | 237 | 1 | 252 |

**Exact shortest split: length 6.** The two all-length safe words are 110010 and 101100. The word 000111 first fails at repetition **119**, with error at 118 = -0.09984945484829977 and error at 119 = -0.10069838934933311. All 20 length-six words have an exact-rational one-active-neuron invariant over the initial-to-fixed-point interval. All 20 pass repetitions 1..32. Every length-two and length-four balanced word is proved eventually failing, so length six is minimal in this finite word class. The single non-invariant length-ten word is not classified by this proof, and does not affect length-six minimality.

**Stronger exact result:** The two safe words have token-prefix correctness for every repetition, not merely block-boundary correctness. For each safe word, exact-rational endpoint checks establish all 12 preactivation/output steps, block-invariance, maximum absolute token error < 0.020225 and positive activation margin > 0.08733. The true counter stays within [4,6], so a finite-cap counter spoofs this restricted language.

**Independent check:** Direct nonlinear seven-dimensional replay with 90-digit Decimal and original parameters: both safe words pass 4096 repetitions with no mask changes; 000111 fails at exactly 119 and retains the same mask through 2048. Numerical replay is not an independent exact proof.

**THEORY ledger:** This is an exact finite-length minimization of a phase-sensitive counterexample within one fixed trained checkpoint. Elementary affine contraction and fixed-point methods are not new. No general algorithm-acquisition certificate is established.

**LEARNING ledger:** The witness is a previously gradient-trained ReLU RNN. The 32-cycle correctness screen accepts all 28 balanced words of lengths <=6, while 26 are eventually wrong and only 2 are correct for all repetitions. This is an evaluation spoof/failure mode, not evidence that the network learned an unbounded algorithm. The 32-cycle linear extrapolation baseline is not claimed to be defeated here.

**Next kernel:** Test this exact fixed-point phase diagnostic prospectively on unseen trained checkpoints and a second architecture, against MSE and short-horizon slope. Kill if no added predictive information.

**Artifacts:** Full raw 350-row JSON, source scripts, token-level exact checker, independent Decimal replay and hashes are in the Run185 reproducibility package; remote code upload status is tracked separately.
