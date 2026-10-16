# Run 195 frozen outcome (local; remote CI pending)

Frozen source commit: c03840820a9f070c6d3f248901eb17ec05d663cb.
Seeds: 197,199,211,223,227,229,233,239. Success scalar: **0**. Only 223 and 233 passed exhaustive length-12 evaluation at both checkpoints; neither yielded a grammar, beam or random sign disagreement through length 24. Do not claim an all-length algorithm.

All-seed rows (seed: eligible; grammar first depth; drift beam first depth; random hits /100):
197: no;9;9;27
199: no;none;none;8
211: no;10;10;6
223: yes;none;none;0
227: no;none;none;0
229: no;12;10;46
233: yes;none;none;0
239: no;10;9;76

**Exact counterexample (secondary):** seed 199, epochs 300/600, agree on every word length 1..13 (16,382 words) under outward-rounded 42-digit interval checking. On word `00000001001110` length 14, epoch 300 output is positive (~1.53018) and epoch 600 output negative (~-0.380715). This establishes shortest separator length exactly 14. Grammar and width-32 beam both missed the witness through length 24; uniform random found disagreements in 8/100 matched trials. One-seed post-hoc counterexample, not a prospective primary success.

Source and training outputs preserved in local reproducibility archive; GitHub Actions configured to regenerate raw checkpoints and all 800 random trials. CI status must be checked before claiming remote reproduction.
