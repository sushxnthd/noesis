# LEARNING — Kernel 001 / Run 282

Frozen before training: held-out seeds 20496..20591, two 96-network arms with identical samples and ordinary Adam/BCE, all six parameters trained. Neutral arm initializes all six weights iid N(0,0.5^2), no task-specific offsets. Biased arm reproduces Run280 initialization.

**Observed:** At epoch160, neutral 25/96 sampled-perfect and 25/96 exactly certified; all 25 have independently verified incorrect initial models (23 shortest initial witnesses length1, two length2). Biased 96/96 sampled-perfect and certified at epoch40. Neutral exact certification: 0/96 epoch0, 1/96 epoch20, 12/96 epoch40, 23/96 epoch80, 24/96 epoch120, 25/96 epoch160.

**Stronger natural transitions:** Five neutral-start models were sampled-perfect but exactly wrong at earlier checkpoints, then became all-length certified with continued gradient training. Seeds/epochs/witness lengths: 20575 (20->40,14), 20531 (40->80,17), 20547 (40->80,9), 20561 (80->120,36), 20567 (120->160,244). The last counterexample is 244 consecutive TOGGLEs, far beyond the length-10 training data. These five were identified after training, not prospectively predicted.

**Competing explanation:** Exact quotient is unusually easy for this task/architecture, and only 25/96 neutral-start networks fit training perfectly. The result is not architecture transfer. Do not equate 25 successes with 25 finite-perfect heuristic-to-algorithm transitions; five meet the stronger criterion. The full checkpoint dataset and optimizer state must be retained as workflow artifacts.
