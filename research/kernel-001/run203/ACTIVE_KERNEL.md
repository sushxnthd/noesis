# Active Kernel001 after Run203
1. **Precise question:** Can a refined *reachable* task-state quotient be automatically synthesized for both input symbols, giving a sound all-length simulation certificate for a gradient-trained count-mod-three RNN?
2. **Primary-literature frontier:** Weiss et al. ICML2018 automata extraction; Jacoby et al. ATVA2020 RNN invariants; Ryou et al. CAV2021 polyhedral RNN verification; van Rossem and Saxe ICML2025 algorithm acquisition. No priority claim for automata extraction or invariant induction alone.
3. **Scalar criterion:** At least one previously unseen trained checkpoint gets an independently checked full-alphabet all-length certificate, with zero cap-spoof false accepts.
4. **Strongest competing explanation:** task-label leakage into a hand-coded automaton, with unreachable or non-inductive regions concealing real mixed-symbol failures.
5. **Cheapest decisive falsification:** Run203 showed the coarse three-output-class partition fails on reachable states at prefix depth 7. Next attempt: split by successor signature, check initial and 0/1 closure, and reject on the first reachable counterexample.
6. **Publishable threshold:** prospective unseen task/architecture transfer, independent proof, strongest spoof controls, mechanism-derived prediction of training transition, primary priority audit.
7. **Learning relevance:** genuinely gradient-trained checkpoints; certificate must predict a frozen out-of-training-range generalization transition, not merely agree on finite probes.
8. **Kill:** any unsound acceptance or three substantive failures of distinct refinement attempts triggers reformulation.
One active kernel; zero backups. Run203 kills only the unrefined output quotient, not Kernel001.
