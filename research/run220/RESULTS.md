# Run220 — frozen 3D transfer: INCONCLUSIVE

Frozen protocol: commits 070d001c and 544efbf. New fully coupled 3D tanh RNNs, 24 deterministic CPU-trained seeds, exhaustive ternary reset-parity length-six training, epochs 50 and 200.

Two independent outward-rounded mathematical checkers (mpmath.iv and directed Decimal) locally verified:
- Four incorrect-to-all-length-correct transitions: seeds **1301, 1319, 1427, 1451**.
- One all-length-correct already at epoch 50: **1409**.
- One persistent incorrect model: **1429**.
- One additional model all-length correct at epoch 200 but epoch-50 status unresolved: **1327**.
- Eighteen unresolved transition classifications, primarily due to endpoint proof abstentions. Abstention does NOT imply incorrectness.
- Eighteen independently checked epoch-50 incorrect witnesses; one independently checked epoch-200 incorrect witness.
- Six all-length epoch-200 positive certificates and one epoch-50 positive certificate.

Frozen sign-only suffix AUROC: 0.750; equal-length random: 0.750; histogram-shuffled: 0.625; delta **0.000**. Only one persistent failure (four required); 18 unresolved (maximum eight). **Primary result INCONCLUSIVE**, not a positive predictor validation.

Checkpoint SHA256: 4cc24de3636fa8aaf98bbd96470d8e9f3509b2c16b7fcce021cd6d681b542dd8. Proof record SHA256: 748b32839217ebd035823546a88f105658f01e11fdcdbf139ad179c35e163196.

Exact checkpoint training source is in research/run220/train.py. The complete locally generated checkpoint and interval-proof package is preserved separately because connector writes of workflow and large artifacts are blocked. Do not merge this branch until all source/artifacts and remote proof reproduction are uploaded.
