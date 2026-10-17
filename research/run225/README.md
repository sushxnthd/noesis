# Run225 result

Eleven previously trained, all-length-certified reset-parity networks retain their exact predictions when a permanently zero fourth recurrent coordinate is appended. Changing one newly added token bias by 2^-20, with fourth-coordinate readout coefficient 2^24, reverses the decision on input 0 for all eleven checkpoints. Two local interval implementations verified the sign change. The original fixed-architecture robustness certificates remain valid. This is not an acquisition predictor.

Primary references: Dinh et al. (ICML 2017), van Rossem and Saxe (ICML 2025), Ryou et al. (CAV 2021). The general reparameterization observation is not novel.

The complete eleven-checkpoint evidence archive is delivered separately. One exact trained checkpoint is staged here for GitHub reproduction. Previous direct file uploads were blocked and are retained as provenance in THEORY_LEARNING.md.
