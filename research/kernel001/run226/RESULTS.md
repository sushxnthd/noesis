# Run226 results

Phase A: no new counterexample labels from numeric enumeration to length nine. Phase B: five beam widths x eighteen checkpoints (17 unresolved + one known-positive control), 90 trials. Zero newly verified failures among the 17 unresolved late checkpoints. Control seed 1429 at epoch 200: width 64 found 200011100 at length nine, width 128 missed through length 256, widths 256/512/1024 found 20011100 at length eight. Both words independently verified incorrect by mpmath.iv and directed Decimal locally. Absence of beam detection is NOT correctness. Frozen AUROC result remains inconclusive; success criterion not met.

Reproduction: archived checkpoint SHA256 4cc24de3636fa8aaf98bbd96470d8e9f3509b2c16b7fcce021cd6d681b542dd8. Numeric candidate JSON SHA256 af38fd26712b83544a920e5f880c8be268ce9d1929a9fe43b60763343ad62645. Beam raw JSON SHA256 e3d59a900179e09b28c072e56d4fb3c8755f9b8c2a6d6769baffde1ffb5add87. Remote CI not confirmed.
