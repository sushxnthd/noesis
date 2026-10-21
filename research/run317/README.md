# NOESIS Run317: recurrent repair of a trained finite-memory heuristic

Original gradient-trained seed 22642 epoch80: opposite-label words 00000000000 and 10000000000 have exactly equal hidden states. Output-bias-only calibration cannot fix this memory collision.

Exploratory intervention: keep all original trained weights except A0[0,0] := 11/10 and output bias := -1/100. Exact induction on C = {h1=0, h0>=1, 0<=h2<=3*h0} proves unrestricted latch correctness for every finite input sequence. Positive logit margin >=1.239969841179, negative margin =0.01. Independent SymPy vertex/ray checker agrees.

Reproduce: pip install sympy==1.13.3; python research/run317/test317.py. Original 28-scalar float64 checkpoint is included. Original Run315 full checkpoints SHA256: 72a273a42258e55f1092dc26664fd91777a8d2e56d6d598469e2abc0e63fab20.

**Limits:** One hand-selected gradient-trained network; coefficient chosen after observing its collapse. This is a post-training engineered repair, NOT natural learned acquisition, minimal parameter-edit proof, held-out validation, or general law. Negative-control test failure and corrected mutation are preserved in the local full archive.

Prior art: Weiss et al. ICML 2018 (automata extraction), Jacoby et al. ATVA 2020 (invariant verification). No general novelty claim.
