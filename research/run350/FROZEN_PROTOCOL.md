# NOESIS Run 350 — Frozen causal readout-order intervention protocol

**Active kernel:** 001-S (learned algorithm acquisition), sole active kernel. **Protocol frozen before executing the intervention scan.** Run 349 already established the four-word affine obstruction at seed 32135 epoch 82 and exact affine separation on 2,644 fixed generator words at epoch 83; these facts are prior observations, not new heldout discoveries.

## Precise question
Can a restricted subset of the *actual epoch-82 to epoch-83 gradient update* causally eliminate the exact hidden-representation obstruction without retraining, and does the repair extend to the previously frozen 2,644-word generator?

## Fixed inputs and controls
- Original Run 348 trajectory SHA256: `c74d2821ae8ae6ea568c1fee80fa11f704efcc62d31416b0d436fc4d1ca60403`.
- Seed 32135 epochs 82 and 83, parameter-vector JSON compact SHA256 respectively `1e183912b602c3e9c9780f328a9f6443686becdfd24c07fe34bfa101c532e485` and `b249e7f21e714b330f7419125bef2cb06ef3328fb529e15272d92cec218b8c3d`.
- Fixed Run349 word generator: all nonempty binary words length <=10 plus specified long sparse/zero-run families, filtered length <=23 (2,644 words).
- Original exact four-word witness at epoch 82 from Run349; no substitutions.
- Exact-real ReLU inference with stored float64 weights interpreted as rationals. Affine readout can be freely replaced, but recurrent parameters only change through specified counterfactuals.
- Test 24 individual-coordinate replacements from epoch 83 into epoch 82, and four block replacements `A0=[0,9)`, `A1=[9,18)`, `b0=[18,21)`, `b1=[21,24)`. Do not combine or optimize changes.
- For each candidate first compute all 2,644 hidden states, solve the *fixed* affine separator feasibility problem with unit margin using SciPy HiGHS, and independently check any proposed separator on every word using exact rational arithmetic. When a separator is not found, do not claim impossibility without an exact convex witness.
- Independently verify exact signs of all preactivations on the four witness words for epoch 82 and epoch 83; compare masks. Exact convex-collision witness is the negative control, epoch-83 exact separator is the positive control.

## One scalar success criterion
**S=1** if at least one of the 24 *single-coordinate* replacements yields an exact rational affine separator with strictly positive margin for all 2,644 frozen words, while the unchanged epoch-82 checkpoint retains its exact four-word convex obstruction; otherwise **S=0**. Block outcomes and four-word-only repairs are exploratory secondary outcomes, not grounds to change S.

## Frontier and competing explanation
RNN verification by inductive invariants, convex separation, and automata extraction are established; the claim here is restricted to a causal intervention on an original gradient-trained trajectory, not a new convexity theorem. Competing explanation: the representation recovers only through a coordinated multi-parameter gradient step; a single parameter cannot restore the full evaluation family.

## Cheapest decisive falsification
Enumerate the frozen 24 single-coordinate and four block counterfactuals; independently exact-check any separator, and verify epoch-82/83 controls. No new training, no additional model selection.

## Publishable threshold
A reproducible causal intervention, exact independent checker, mechanistic account tied to the original training update, further unseen-seed replication, and a priority audit. This one-seed experiment alone is not publishable as a universal law.

## Learning-system relevance threshold
At least one exact change in representational repairability caused by a coordinate or block of the actual gradient update in the original trained network. A result on hand-built states alone does not qualify.

## Kill condition
If exact controls fail, reject this run. If no single-coordinate intervention repairs the full family, kill the single-coordinate sufficiency hypothesis; preserve block and negative outcomes. After three failed substantive approaches to a representation-robust diagnostic, reformulate Kernel 001-S.

## Ledgers and provenance
Maintain THEORY (geometric obstruction / exact separator) and LEARNING (effect of actual training-update coordinates), raw results, selected checkpoints, executable code, independent verification, tests and CI. Never rewrite earlier negative results. No paid compute or user laptop.
