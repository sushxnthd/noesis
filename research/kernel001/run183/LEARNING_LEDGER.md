# LEARNING ledger — Run183
Source: unchanged Adam-trained ReLU checkpoints from Run181, training on exhaustive length-six reflected-counter traces. 30 fit-qualified checkpoints screened; 2880 short-horizon pairs, 256 prospectively selected (128 predicted pass/128 predicted fail).
Observed: 129 correct through 2048 repetitions, 127 fail; baseline errors 1. 189 within-checkpoint mixed-outcome pairs have early maxima within 20%, but their extrapolated slopes can differ; this is NOT predictive improvement.
Independent 100-digit Decimal full recurrence reproduced 31 sampled outcomes with no mismatch.
Decision: Retain one-word exact proof as falsification of naive linear extrapolation. Continue only if a new diagnostic improves prospectively over the strongest simple baseline on unseen checkpoints, not by increasing the number of easy cases.
