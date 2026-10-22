# NOESIS Run 344 — Exact affine-readout horizon and training-induced representation collapse

**Status:** One original gradient-trained width-four ReLU parity RNN; exact proof locally verified with Python Fraction and independent SymPy. This is a retrospective mechanism study, not an unseen-model predictive validation.

## Active kernel 001-S: eight fields
1. Question: Can exact hidden-state separability identify a *non-repairable* finite-range neural heuristic and track its change during training?
2. Frontier: Weiss, Goldberg & Yahav (ICML 2018) automata extraction; Jacoby, Barrett & Katz (ATVA 2020) invariant-based RNN verification; classical convex-hull duality.
3. Run 344 success criterion (frozen): at least one exact rational convex-hull intersection on original trained seed 31089 epoch 200 with words length <=16. **Passed.**
4. Alternative: only the trained output readout is defective, and the hidden representation can be fixed by readout-only retraining.
5. Cheapest falsification: exact affine-separability feasibility and dual witness on fixed original hidden states.
6. Publishable threshold: independent exact verification, adversarial baselines, priority audit, prospective unseen-model mechanism prediction, and broader trained-system replication.
7. Learning relevance: original gradient-trained epoch 140, 141 and 200 checkpoints; no modification to recurrent parameters.
8. Kill: any exact checker disagreement invalidates the certificate; if a readout can classify the five conflicting words, retract. No backups active.

## THEORY ledger: exact proof
For the epoch-200 trained checkpoint, an explicit rational affine readout correctly classifies **all 32,766 nonempty binary words through length 14**, with exact signed margin >=1. This is verified by exhaustive Fraction arithmetic, not by float64 testing.

At length 15, two odd-parity and three even-parity words have **exactly intersecting hidden-state convex hulls**. Positive rational convex weights sum to one on each side, and the weighted hidden vectors are equal. Consequently no affine output readout can classify these five words simultaneously (even with arbitrary readout weights), so none can classify every word through length 15. The selected five-word support is irreducible; global minimum number of words is not claimed.

Thus the **maximum exactly readout-repairable exhaustive horizon is 14** for this particular trained hidden representation, under dyadic-exact recurrence semantics.

Five-word witness, parity labels respectively (1,1,0,0,0):
- 1
- 100000000000000
- 11001000000100
- 100000000000001
- 100000000000010

The original output readout remains the same as Run 343, where an infinite family of longer errors was proved. The new theorem rules out *all* readout-only repairs, not merely that specific output readout.

## LEARNING ledger: a one-optimizer-step representational transition
Both original checkpoints at epochs 140 and 141 correctly classify all **8,190 nonempty words through length 12** by exact arithmetic. Both have training accuracy 1.0. Yet:
- Epoch 140: a rational affine readout strictly separates the five frozen witness words.
- Epoch 141: their parity-class convex hulls intersect exactly, so **no affine readout can classify all five**.
- Training BCE nevertheless falls from **0.01630776129933451** to **0.01622239818863201**.

This is a retrospective example of gradient training destroying *long-horizon affine readout repairability* while preserving short-horizon correctness. It does **not** show a loss of unrestricted correctness at that exact step, nor prove an all-model law.

## Verification, provenance, limits
Run `python research/run344/run344.py` then `python research/run344/independent344.py` and `python -m pytest -q research/run344/test_run344.py`. The first script emits exact rational `witness344.json` and `results344.json`; CI uploads both as artifacts.

Original Run342 full trajectories SHA256: `c20f44b3bd56893880974c638b6202ad75a5ea253b64f72eeaa094e8d973112e`. Original epochs 140/141 parameters and train metrics are committed in `model344.json`; epoch 200 parameters are inherited unchanged from `research/run343/model343.json`. The full cohort trajectories remain in the Run342/343 evidence archives, not permanent Git blobs.

The fixed source checkpoint was known from Run343. The exact length-14 lower bound and epoch-140/141 comparison were post-hoc strengthening, not preregistered independent tests. Numerical LP exploration was used for candidate discovery only; the reported conclusions rest on exact proofs.

**Novelty boundary:** Linear separability and convex-hull duality are classical, and RNN verification/extraction have substantial prior art. This single learned-network example is a useful mechanistic negative result, not a model-agnostic breakthrough.

Primary sources:
- https://proceedings.mlr.press/v80/weiss18a.html
- https://theory.stanford.edu/~barrett/pubs/JBK20-abstract.html
