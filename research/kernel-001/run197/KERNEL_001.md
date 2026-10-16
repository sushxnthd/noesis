# Active Kernel 001 — trained algorithm acquisition versus finite-horizon heuristics

1. **Question:** Can an automatically generated task-aligned inductive simulation relation certify unbounded correctness in unmodified gradient-trained networks and prospectively discriminate learned algorithms from finite-range heuristics across tasks?
2. **Primary frontier:** van Rossem & Saxe (ICML 2025) analyze streaming parity acquisition; Weiss et al. (ACL 2018) automata extraction; Jacoby, Barrett & Katz (ATVA 2020) invariant inference; Ryou et al. (CAV 2021) polyhedral RNN verification; Dankowiakowski & Ronca (NeurIPS 2025) metric automata theory. All-length verification itself is not claimed novel; full cross-task priority audit remains incomplete.
3. **Scalar:** For Run 197, number of certified modulo-3 checkpoints among 8, with success >=1. **Observed 0/8 (FAIL).**
4. **Competing explanation:** coordinatewise interval boxes may be too coarse; finite behavior may actually be heuristic.
5. **Cheapest decisive falsification:** freeze four new seeds and two checkpoints, fixed suffix depths k=6,8, independent interval check of any proposed positive, and adversarial exact witness search on strongest finite performer.
6. **Publishable threshold:** sound prospectively frozen cross-task/architecture certificates or predictive improvement over matched finite baselines, spoof resistance, independent reproduction and primary-literature priority audit.
7. **Learning relevance threshold:** diagnostic must apply to unmodified gradient-trained checkpoints and predict or expose a learning/generalization transition. Run 197 meets the failure-mode gate but not positive certification.
8. **Kill condition:** retire after three consecutive substantive failures to improve prospective transfer or transition prediction. Run 197 is failure 1/3 under this reformulation.

At most two backups: (A) architecture-independent abstract interpretation using learned coordinate transformations; (B) pre-transition certificate-margin predictors. Neither is active.
