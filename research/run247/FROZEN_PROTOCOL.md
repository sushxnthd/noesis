# NOESIS Run 247 — frozen before evaluation

Active kernel K001: sound certification and falsification of algorithms in gradient-trained recurrent neural systems. Previous Run246 transfer failure 1/3.

1. Question: are 18 previously unresolved epoch-200 ReLU networks actually incorrect, rather than correct but unprovable by the box verifier?
2. Literature frontier: van Rossem & Saxe (ICML 2025), Dave et al. (NeSy 2025), Dankowiakowski & Ronca (NeurIPS 2025). Finite generalization is not a proof of infinite correctness.
3. Primary scalar: >=8 newly proven incorrect trained networks among the 18, with zero invalid exact witnesses.
4. Strongest competitor: these 18 are correct infinite-state networks and the verifier is incomplete.
5. Cheapest decisive falsification: enumerate ternary strings of lengths 1–12 in lexicographic order using batched float64; independently replay each proposed witness with exact dyadic rationals from the original binary64 checkpoint.
6. Publishable threshold: >=8 exact new falsifications, independently checked and reproducible, with minimized/short witnesses, priority audit and explicit limitations.
7. Learning threshold: each new counterexample comes from an actual gradient-trained network with 100% finite training accuracy, not a constructed automaton.
8. Kill condition: any invalid claimed exact witness or unsound positive certificate; after three unsuccessful substantive K001 tests reformulate or retire.

Frozen inputs: Run246 epoch-200 networks with exact status ABSTAIN, no new training or parameter changes. Freeze is in GitHub commit 4fff024a96634cb6bf87dfc1670cfec6da40b371 before local search. The original freeze was short; this expanded version documents the same unchanged criterion and method after evaluation, not a retroactive change.

The exact checkers use two separately coded Fraction conversions; float64 is only a candidate oracle. A no-witness result means only that this finite candidate scan found no error; it is NOT a certificate. The first proposed error is lexicographically earliest at its length under the float64 scan, not necessarily globally shortest under exact arithmetic if float64 disagrees near zero.

Inactive backups: relational invariants for ReLU, and invariant-margin intervention (only after a sound diagnostic). No user compute or paid API.
