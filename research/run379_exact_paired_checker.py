"""Run 379 exact paired sign-flip test on frozen eligible-seed outcomes.

This file verifies the negative result from the complete local reproducibility archive.
Eligibility: 6 of 8 predetermined fresh LSTM seeds achieved first-perfect
short-training accuracy. Do not silently replace the two ineligible seeds.
"""
from itertools import product

# Per-seed interaction: (transition_shift4 - transition_shift0)
#                       - (identity_shift4 - identity_shift0)
observed = [0, +1, 0, -1, 0, 0]
active = [x for x in observed if x != 0]
obs_mean = sum(observed) / len(observed)
null_means = [sum(x*s for x, s in zip(active, signs))/len(observed)
              for signs in product((-1, 1), repeat=len(active))]
p_one_sided = sum(x <= obs_mean + 1e-12 for x in null_means)/len(null_means)
assert obs_mean == 0.0
assert p_one_sided == 0.75
assert len(observed) == 6 < 8
print({"eligible": 6, "prespecified": 8,
       "observed_interaction": obs_mean,
       "exact_one_sided_p": p_one_sided,
       "frozen_primary": "FAILED"})
