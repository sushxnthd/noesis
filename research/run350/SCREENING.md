# Run 350 screening and numerical-failure ledger

Protocol frozen before new cohort training: edea92b80cdabaaf54703aa794345c47c338a4a3.

The numerical proposal search evaluated all earlier training-perfect, length-8-correct checkpoints of the ten epoch-200-certified seeds. The fast search used the 2,644-word length-at-most-23 subset of the unchanged 7,006-word deep generator; every exact witness found belongs to the full 7,006-word generator. Therefore the observed two qualifying seeds are a lower bound on the number of deep-family positives, not an exhaustive count across all words of lengths up to 72.

seed | train-perfect | short-correct numeric | shallow separable numeric | deep23 nonseparable numeric | exact collisions | numeric false alarms
33005 | 162 | 162 | 161 | 0 | 0 | 0
33046 | 163 | 163 | 129 | 0 | 0 | 0
33053 | 170 | 170 | 170 | 1 | 1 | 0
33068 | 145 | 145 | 145 | 1 | 1 | 0
33094 | 123 | 123 | 123 | 0 | 0 | 0
33105 | 174 | 174 | 174 | 157 | 0 | 157
33135 | 165 | 164 | 164 | 0 | 0 | 0
33146 | 143 | 143 | 143 | 0 | 0 | 0
33154 | 167 | 167 | 166 | 0 | 0 | 0
33171 | 180 | 180 | 180 | 0 | 0 | 0

At seed 33105, 157 numerical LP collision proposals were rejected by exact rational checking, often because a numerically proposed two-state equality was not exact. Do not interpret numerical LP nonseparability as a mathematical certificate. The successful cases were independently verified with SymPy and Fraction and exact positive affine margins. The first certified epoch was 76 for seed 33053 and 72 for seed 33068.

Limits: selection conditioned on endpoint certificate; only ten certified endpoints were screened for early obstructions; unselected networks could also have relevant transitions. This does not measure population prevalence or prove a model-agnostic predictor.
