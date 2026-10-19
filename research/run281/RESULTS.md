# Run281 results

Eight fixed witness-wrong checkpoints repaired, 6 with one edit and 2 with two. All preserve 2600/2600 sampled token predictions. Eight independent 64-vertex parameter-box certificates passed (radius 2^-12), with 16 corrupted controls rejected.

Important: seven sources are epoch-zero initializations, not trained models. Only seed 20400 epoch 20 is post-training. Seed 20400 epoch 20 has 100% sampled accuracy but fails on 52 consecutive toggles; by epoch 40 it passes an independent all-length robust certificate, without intervention. This is one genuine gradient-training acquisition transition on a second task.

Training reproduced byte-identically (SHA256 1ad489e05732886e1ba0a6f76866ce32a2c59b0213e85df2bfa317ca8c63ad64). Results remain architecture-specific; no model-agnostic law established. Public CI not yet confirmed.
