# NOESIS Kernel 001 — Run 259 frozen protocol (2026-10-19)

## Active question
For independently initialized gradient-trained reset-parity RNN seed 17056, can a **model-specific** invariant over observed parity/activation classes be proved inductive, or can its abstract counterexample be shown spurious and repaired by a measurable partition refinement?

## Frontier
Run 254 proved a model-specific all-length invariant for seed 13037; Run 258 found no transfer of that fixed geometry to independent seed 17056. Standard polyhedral RNN verification is prior art; this run tests applicability to an independently acquired learned representation.

## Primary exact criterion
Find **one exact rational** abstract transition witness violating a candidate parity/activation-class invariant, then either (A) independently replay it as a reachable neural error or (B) prove that it is spurious relative to the exact sampled reachable set and construct a strictly sharper inductive candidate. No success claim from floating-point LP alone.

## Strongest competing explanation
The observed seven parity/activation classes are not inductive because convexification invents unreachable states; a long-delayed neural failure may still exist.

## Cheapest falsification
Use stored float64 parameters from Run 258 (no retraining). Enumerate all words through length 9, build parity/mask hulls, solve constrained transition LPs; exact-check any witness with Python Fraction and a separate checker. Try at most two suffix-memory refinements if the first abstraction fails.

## Publishable threshold
A fully exact all-length certificate for an independently trained model with a distinct learned representation, independently rechecked, plus incorrect-model controls; or a new verified counterexample that changes evaluation practice.

## Learning-system relevance
Only checkpoint 17056, independently trained from random initialization, is eligible for the positive claim; finite-perfect training accuracy is not proof. No model descendants or synthetic automata count.

## Kill
After three substantive model-specific synthesis failures without a new exact certificate or learning-relevant diagnostic, retire/reformulate this active kernel. Negative attempts remain archived.

## Ledgers and controls
Keep THEORY and LEARNING separate; preserve scripts, checkpoint hash, exact witnesses, numerical failures, and CI state. No main writes. No personal compute or paid APIs. Wildcard budget <=10%, separated from frozen evaluation.
