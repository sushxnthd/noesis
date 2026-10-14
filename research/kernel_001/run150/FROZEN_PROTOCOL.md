# NOESIS Run 150 frozen protocol
Date: 2026-10-14
Question: Does a neutral-token hidden-state consistency penalty improve out-of-distribution counting after gradient training?
Seeds: 208 through 215. Architecture: 4-state ReLU recurrent model. Data: all length-six ternary sequences. Optimizer: Adam, 1200 steps, learning rate 0.025. Variants: baseline; hidden-state consistency penalty 0.1; output consistency penalty 0.1. Identical initialization per seed.
Primary endpoint: maximum absolute error over all 729 six-token prefixes followed by 1 to 64 neutral tokens, then median over eight seeds. Primary ratio: latent median divided by baseline median. Success requires ratio <= 0.5, at least 6/8 improved seeds, training MSE <= 1e-4, and latent median <= 0.8 output-control median.
Competing explanation: generic added neutral supervision rather than learned transition invariance.
Falsification: paired training and fixed heldout neutral suffixes.
Publication threshold: replicate across architectures and tasks with independent verification and prior-art audit.
Learning relevance: actual gradient-trained model weights, not post-hoc ablation.
Kill: any success gate fails or mixed-token generalization materially worsens.
Theory ledger and learning ledger must be maintained. One active kernel only. No new architecture tuning or seed selection.
