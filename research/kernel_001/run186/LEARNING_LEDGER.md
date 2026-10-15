# LEARNING ledger — Run 186
29 eligible unchanged gradient-trained Run181 checkpoints (widths 3 and 7), 16 held-out balanced words, 464 pairs. Previously mined checkpoint width7 seed409 epoch200 and four earlier evaluated words excluded.
At horizon 8192: 110 pass, 354 fail; 32-cycle linear and saturation-aware hybrid each classify 461/464 correctly (99.35%). The hybrid's frozen improvement is zero.
Three 8192-horizon false-fails occur on the same width3 seed409 epoch800 checkpoint; directed interval verification proves all fail at repetition 8623.
No demonstrated algorithm-acquisition transition, no superiority to simple short-horizon baselines, no generalization across independent architecture families.
Decision: retire this particular saturation-aware hybrid. Preserve all negative results and pursue genuinely matched-difficulty training transitions under Kernel 001.
