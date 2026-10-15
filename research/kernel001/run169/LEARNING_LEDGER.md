# LEARNING — Run 169

32 **new** CPU-trained recurrent ReLU checkpoints: widths 3,7; seeds 400..415; exact Run167 training procedure (Adam 1200 steps, all ternary length-6 strings, neutral regularizer). Training and scoring code ran locally without user laptop/API spend.

Frozen before training: commit 85e166e986e1f51be6af6adb67660c9ddf332c1d.

At k<=8192 cycles, 12/32 checkpoints failed (including 5 early failures at k<=32). Frozen delayed-failure label count: 7/32. Predefined fit+32-cycle matched subset: n=21, 1 delayed failure, 20 nonfailures (width3 1/12; width7 0/9). **Primary predictive criterion INCONCLUSIVE**, not passed or falsified, because preregistered minimum was 5 failures and 5 nonfailures with both classes in each width. Matched AUC 1.0 values are meaningless with a single positive and are not evidence of superiority.

Unmatched descriptive delayed-failure AUC: frozen observable-risk 0.800; training MSE 0.829; one-cycle error 0.857; 32-cycle probe 0.800. No demonstrated incremental prediction.

**Independent checks.** Outward-rounded Decimal interval checker certifies first failure k=7901 for width3 seed406 with no activation-mask changes. Separate gauge checker verified eight checkpoints under D[0,0]=1000, all 32-cycle outputs and score components within prespecified numerical tolerances.

**Decision.** Retire *instantaneous* propagated-defect as a sufficient certificate (theorem counterexample). Do not declare predictive scalar falsified under the underpowered frozen matched test. Reformulate same Kernel001 around accumulated task-observable drift with region-invariance obligations. Preserve all negative results and the underpowered design.

**Infrastructure.** Archive includes all 32 checkpoints and raw results; GitHub branch must contain code/results/protocol and the trained witness. CI status tracked separately.
