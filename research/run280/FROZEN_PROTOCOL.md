# Run 280 frozen protocol
Date: 2026-10-20.
Question: Does a strict-margin all-length correctness certificate transfer from gradient-trained latch networks to separately trained RESET/TOGGLE parity networks?
Frozen cohort: 96 seeds 20400..20495, length 10, 256 seeded random sequences plus 4 length-2 prefixes padded with RESET, Adam lr 0.025, BCE, float64, 160 epochs. Snapshots 0,20,40,80,120,160.
Success: At least one sampled-perfect but exact witness-wrong trained model admits a repair of at most 2 coordinates, preserves all sampled predictions, and has independently checked all-length correctness for simultaneous parameter perturbations of radius 2^-12.
Competing explanation: parity-aware initialization and hand-crafted sufficient intervals.
Falsification: exact rational search to length 64, independent checker and box verification.
Publishable threshold: independently reproduced cross-task results and strong baselines beyond known parity generalization and RNN verification.
Learning relevance: all six weights gradient-trained; no synthetic models as replacements.
Kill: if no witness-wrong sampled-perfect model or no robust repair, record negative result; after three failures reformulate.
Repair rule: if v>0 and b_toggle>0, set a_toggle=-2 when outside [-2.5,-1.5]; if needed set a_reset=-0.5. Never change b_toggle,b_reset,v,c. Certificate regions E=[0,b_toggle/8], O=[3*b_toggle/4,5*b_toggle/4]. Strict readout and all-symbol region preservation for the full six-dimensional parameter box.
Literature: Van Rossem & Saxe, ICML 2025; Ryou et al., CAV 2021.
