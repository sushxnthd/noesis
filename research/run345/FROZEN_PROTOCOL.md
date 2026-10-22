# NOESIS Run 345 — frozen replication protocol (2026-10-22)

Single active kernel: 001-S, readout-repairability acquisition.
SOURCE: original Run342 gradient-trained width-four parity trajectories, SHA256 c20f44b3bd56893880974c638b6202ad75a5ea253b64f72eeaa094e8d973112e.
Exclude seed 31089, used for Run344 discovery. Examine seeds 31000..31127 in increasing order. No new training, no personal compute.

Question: Does a second original gradient-trained network exhibit an exact affine-readout irreparability transition on fixed long-word probes, despite preserved short-horizon parity accuracy?

Frozen probe family: every nonempty binary word of length 1..12 for original short-accuracy eligibility; for readout hull collisions, all words of the form 1 + 0^a + 1 + 0^b (a,b>=0, total length <=16), and 1+0^k (0<=k<=15), plus the single word 1. Include both parities and deduplicate; no probe additions after endpoint inspection.

For each eligible endpoint (epoch200 correct through length12), in ascending seed order:
(1) evaluate fixed probes with binary64 inference; find convex-hull intersections of opposite-parity hidden states using SciPy HiGHS feasibility LP;
(2) convert a basic feasible LP solution into an EXACT rational convex-combination witness using float64 coefficients interpreted as dyadic rationals, with Python Fraction arithmetic; independently recheck with SymPy; reject all near-singular/nonpositive or inconsistent candidates;
(3) for each exact endpoint witness, scan all original epochs in increasing order for a consecutive pair (e,e+1) with both original-readout exact accuracy through length 12 and with the SAME witness word set strictly affine separable at e but exactly inseparable at e+1. Exact verification of short accuracy is required only for a qualifying transition; numeric prescreen is allowed.
Primary scalar success: >=1 new seed with exact witness and exact consecutive training transition satisfying (3).
If none, report failure, do not modify family/threshold. Independently verify every claimed exact certificate. Preserve numerical negatives and failures.

Strongest competing explanation: the Run344 one-step collapse is idiosyncratic to seed 31089 or witness selection. Cheapest falsification: reanalyse existing trajectories, no retraining. Publishable threshold: independent exact checker, mechanism-derived prospective prediction on unseen model/task, adversarial spoof controls, priority audit. Learning relevance: original gradient-trained checkpoints, exact change in output-only repairability at constant short-range correctness. Kill: invalid rational certificate or three substantive independent failures. Backups: none.

NOTE: Frozen *before* endpoint analysis. This branch is not a new cohort preregistration; source trajectories were already trained and prior outcomes known. Retrospective exploratory replication only.
