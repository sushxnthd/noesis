# NOESIS Run 221 — verified beam-search failure on a trained neural model

Frozen trained checkpoint: 3D tanh RNN, seed 1429, epoch 200. Original Run 220 checkpoint SHA256: `4cc24de3636fa8aaf98bbd96470d8e9f3509b2c16b7fcce021cd6d681b542dd8`.

Two independent outward-rounded checkers (mpmath.iv and directed Decimal) exhaustively verified all 9,840 nonempty ternary words through length eight. Every word through length seven is correct (3,279 total). Exactly two length-eight words are wrong: `20011100` and `20011101`. Both are globally shortest incorrect words for this frozen network.

The Run 220 sign-margin/diversity beam search behaves **non-monotonically in beam width**: width 256 finds both witnesses; width 384 finds neither; width 512 finds both. At width 384, the lexicographically first witness's ancestor `200111` is pruned at depth six.

This is a failure of an untrusted neural adversarial-search heuristic, not a failure of the independent interval proof. Increasing beam width does not guarantee a superset of explored prefixes under the current nonnested pruning rule.

**Smallest supported claim:** For this one gradient-trained network and this beam-selection algorithm, an apparently stronger search budget produces a false negative. No new model-agnostic acquisition law is established. Run 220's previously recorded incorrect witness remains valid. The diagnostic-prediction transfer remains inconclusive.

This audit was an isolated anomaly probe; no retrospective predictor tuning was performed.
