# LEARNING ledger
- Trainable recurrent parameter: cap M (not just readout).
- Frozen 12 initial caps k-2/3, k=3,...,14.
- Final-only shortest-witness training: 12/12 loss=1, gradient=0, no cap change.
- Prefix-supervised intervention: 12/12 gradient=-10/3, cap becomes k+1/6, shortest zero-test failure length increases by 2.
- High-depth balanced final-output control: 12/12 loss=0, gradient=0 despite cap exposure.
- Independent rational BFS and central finite differences: 12/12 pass.
- Unbounded algorithm acquisition: 0/12; no field-level breakthrough.

