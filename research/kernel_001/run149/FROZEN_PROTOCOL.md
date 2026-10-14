# Run 149 frozen causal probe (2026-10-14)

Kernel 001. Hypothesis: the earliest all-alphabet failure of previously trained seed 214 is caused by neutral-token recruitment of hidden coordinate 3 (zero-based), observed first at neutral step 6 on word `0022222222222`. The task-relevant state should be less corrupted if **only on neutral tokens** that coordinate is forcibly reset to zero immediately after the original ReLU transition. No parameters or readout are changed. This is an intervention on a trained system, not a claim the unmodified network learned the full algorithm.

Primary outcome, frozen before evaluation: Delta = max_{|x|<=13}|f_original(x)-q(x)| - max_{|x|<=13}|f_neutral_clamp3(x)-q(x)| over every ternary word (0 increment, 1 decrement with nonnegative clamp, 2 neutral). Hypothesis succeeds only if Delta > 0.025 and intervention has zero tolerance-0.1 failures at all lengths <=13. Falsified if Delta <=0.025 or any intervention word <=13 exceeds tolerance. Exhaustive outward-rounded interval arithmetic is required for success claim; float64 exploratory.

Strongest competing explanation: suppressing coordinate 3 only hides one positive-output mode but breaks other ternary words, or apparent improvement is a generic benefit of removing arbitrary hidden units.

Controls: clamp each other hidden coordinate on neutral tokens (j=0,1,2); evaluate same rule on previously trained seeds 210 and 215 without selecting a new coordinate; record regressions, including earliest failures. Independent exact-rational checker on maximizers and boundary witnesses.

Publishable threshold: mechanism-derived intervention prospectively improves worst-case tolerance horizon on >=2 independent untouched trained checkpoints and beats all three coordinate controls, with independent checker and priority audit. Learning relevance: changes actual frozen gradient-trained model behavior without post-hoc output recalibration, not just a synthetic automaton. Kill intervention if primary fails; retain as negative result.

Literature frontier: exact counting conditions for ReLU RNNs (El-Naggar et al., ICGI 2023), neural algorithmic generalization and state-space/reachability verification; novelty not assumed.
