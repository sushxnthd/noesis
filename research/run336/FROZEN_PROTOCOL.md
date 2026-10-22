# NOESIS Run 336 — frozen cross-width transfer (2026-10-22)

Active kernel: 001-S (learned-state inductive certificates). This is an unseen **width-2** ReLU recurrent architecture, relative to the width-3 discovery cohort. No new task family is claimed.

## Precise prospective question
Does the exact output-aligned inductive halfspace certificate transfer from width 3 to a newly trained width-2 model, and does its emergence follow a genuinely incorrect but exhaustively short-perfect checkpoint?

## Frozen training
- Seeds: integers 26000..26127 inclusive (128 networks), no selection.
- Recurrence: h[t+1]=ReLU(A[x_t]h[t]+b[x_t]), width 2, h[0]=0; output logit v.h[t]+c, positive iff >0.
- Task: prefix-OR over binary sequences; 160 length-6 Bernoulli samples generated per seed by torch.Generator().manual_seed(seed), plus the four two-bit prefixes padded with zeros.
- Parameter initialization: torch.randn(15,dtype=float64,generator=Generator(seed+51000))*0.5.
- Training: simultaneous independent models, torch.float64, Adam lr=0.025, 80 updates; BCEWithLogits mean across examples and timesteps, summed across seeds; fixed torch CPU deterministic algorithms, one thread.
- Retain epoch 0..80 checkpoints, losses, accuracies, environment/version and SHA256.

## Frozen exact verification
For each original epoch-80 checkpoint, evaluate the width-2 exact-rational halfspace proof with threshold v.h>=-c+1/100000. The all-zero hidden state must be fixed under 0; x=1 from zero must enter P; for both symbols, P must be forward invariant under all ReLU masks. Enumerate exact rational 2D polyhedral vertices and recession rays. A second implementation must independently check every positive certificate.

For any epoch-80 certified seed, find the earliest checkpoint exhaustively correct on **every nonempty binary input through length 6**. On that checkpoint, search all binary strings of lengths 7..12, then frozen families at lengths 13..128 (all-zero, all-one, first/middle/last isolated 1 or 0, alternating, 0^k1^k, 1^k0^k, and 1 followed by zeros). Confirm all claimed failures by exact Fraction and independently by SymPy. Do not silently substitute later epochs or different seeds.

## Single exact success criterion
At least **one** seed with (i) an earlier exhaustively length-6-perfect but exactly incorrect checkpoint and (ii) a later checkpoint with an independently checked unrestricted correctness certificate. Otherwise frozen criterion FAILS. Report certificate yield separately.

## Competing explanation / falsification
A certificate may select only easy width-2 representations, while a bounded-perfect-to-certified transition could be a proof-template artifact. Cheapest falsification is zero qualifying transitions across all 128 seeds, or an exact counterexample to any purported certificate.

## Publishable threshold
Independently verified proof and witnesses, additional unseen task family, adversarial spoof controls, prospective mechanism-derived transition prediction and priority audit. This single width transfer is insufficient for a field-level breakthrough.

## Learning relevance
Only original gradient-trained trajectories count. Hand-designed spoofing networks serve as negative controls, never as acquisition evidence.

## Kill condition
Any soundness failure retires the current certificate immediately. Three substantive failed acquisition/transfer approaches without stronger evidence force reformulation. Preserve negative results.

THEORY ledger: exact soundness and spoof resistance. LEARNING ledger: original training trajectories and measured transition timing. No backup kernel activated.
