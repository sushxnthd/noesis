# Run 316 frozen protocol

Question: Does finite-horizon task-opposed hidden-state collision clearance during gradient training imply correctness?

Cohort: Run315 seeds 22600–22695, epochs 20 and 80. Exact rational arithmetic. Horizon 6. Criterion: at least one trajectory with an epoch-20 collision, no epoch-80 collision through length 6, and a verified epoch-80 error. No tuning or horizon changes after analysis. Retrospective failure-mode audit, not prospective prediction.

THEORY: distinguishability is necessary, not sufficient. LEARNING: test on original trained checkpoints. Kill if no qualifying case. Strongest alternative: finite separation does not guarantee indefinite memory or correct readout. Publishable only after independent checker and primary-literature audit.
