# NOESIS Run 190 — independent retention transfer (2026-10-16)

Primary criterion FAILED: none of four previously untrained seeds (137,139,149,151) has independently certified all-length parity at epoch 300 and a verified parity failure at epoch 600 with reduced training loss.

**New positive theorem:** seed 151 width-8 float64 tanh RNN, Adam-trained on all 64 length-six parity strings, has independently checked all-length prefix-parity correctness at epochs 300 AND 600. Parity+six-bit-suffix inductive invariants each use 128 boxes. Two independent interval checkers pass both proofs. Epoch 300 minimum output margin 3.40805425, epoch 600 margin 5.03825100. The all-length guarantee assumes exact-real evaluation of the stored binary64 weights.

**New negative witness:** seed 137 passes all 4096 length-12 strings at both checkpoints but fails input 1010010000000000000000 at epoch 300 (length 22) and 10100100000000000000 at epoch 600 (length 20). Both wrong-sign outputs were checked with 70-digit intervals. Short-horizon correctness is insufficient.

Learning: seed 137 losses 0.00368512 -> 0.00089793, seed 139 0.00589993 -> 0.00191830, seed 149 0.46616562 -> 0.46585896, seed 151 0.00924207 -> 0.00220822. Epoch 600 length-12 correct sequence counts: 4096,3131,1,4096 respectively. Seed 151 retained the certified algorithm as loss decreased.

Local protocol SHA256 491400e1334560fddfef35dc0885901ec8874ced9e1eba0c87e97f3bbeb8eac0. TRAINED.json SHA256 540afe1a1e8e27a6b445c367179ed120e626cb33399980b17b415a111c0cc51f. Local reproducibility 4/4 tests pass. The initial protocol could not be committed before training: GitHub create_file safety block. Do NOT claim remote preregistration. The complete raw evidence archive exists outside GitHub; this commit does not include full checkpoints or proofs. This is not a field-level breakthrough.

THEORY: sound model-specific all-length retention proof; no general algorithm-acquisition law.
LEARNING: one verified retention trajectory, no new certified-loss trajectory.
