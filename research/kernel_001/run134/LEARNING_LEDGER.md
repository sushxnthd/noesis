# LEARNING ledger — Run 134
- 16 deterministic 2D ReLU models start with det(A-I)!=0, incorrect singleton/hold outputs and no exact counter mode.
- Four exact rational gradient updates alter embeddings and recurrent A, producing an eigenvalue-1 reachable ray and all-length correct output.
- 16 scalar-output-only controls still fail at length two.
- Auxiliary hidden-state composition is explicitly engineered; not spontaneous sequence-only learning.
- Next: ordinary task-only training on an unseen 2D architecture; kill after three failures.
