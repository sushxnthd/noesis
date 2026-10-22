# NOESIS Run 351 — frozen coordinate-18 transfer falsification

**Branch:** `research/kernel-001-run351-bias18-transfer`  
**Protocol frozen first:** commit `dff59294bdc4742beb39c1568918f513c18b48dd`.  
**Input provenance:** Run348 original gradient-trained trajectory SHA256 `c74d2821ae8ae6ea568c1fee80fa11f704efcc62d31416b0d436fc4d1ca60403`.  
**Fixed generator:** 2,644 words, SHA256 `401dcad6e544fcf455687caa444394e4ba2014c9a7009cd17778586855354e90`.

## Frozen result

64 prespecified previously trained seeds (32000–32063); 29 had a first training-perfect checkpoint at epoch <200 and therefore an eligible next-step gradient update. The remaining 35 are reported as ineligible, not silently replaced.

For each eligible seed, the experiment evaluated the original readout with the baseline, full next-epoch update, and all 24 individual recurrent-coordinate replacements. **Primary scalar N=0**, below the frozen success threshold of 3. No seed showed a unique-best coordinate-18 gain of at least 27 correctly classified words. Among the 29 eligible seeds, coordinate 18 improved the fixed family for **one** seed (+9), worsened **four**, and was unchanged for **24**.

Selected outcomes (correct classifications out of 2,644):

| Seed | First training-perfect epoch | Baseline | Full update | Coordinate 18 | Strongest other single coordinate |
| --- | ---: | ---: | ---: | ---: | --- |
| 32046 | 15 | 2626 | 2644 | 2635 (+9) | coordinate 17: 2644 (+18) |
| 32034 | 84 | 2533 | 2644 | 2533 (0) | coordinate 8: 2640 (+107) |
| 32026 | 71 | 2432 | 2639 | 2423 (-9) | coordinate 5: 2530 (+98) |
| 32035 | 12 | 2562 | 2644 | 2549 (-13) | coordinate 7: 2580 (+18) |

Independent binary64-as-exact-rational evaluation matched all 2,644 decisions for **12 original/counterfactual variants** across these four seeds. A separate SymPy computation confirmed the adversarial sign below. An initial checker failure due to `int(sympy.BooleanTrue)` was retained in the local archive, fixed by `int(bool(...))`, and rerun successfully.

## Adversarial spoof after apparent complete repair

Seed 32046, epoch 15, with only coordinate 17 replaced from epoch 16, correctly classifies **all 2,644 fixed words**. Posthoc exhaustive float64 search found two errors at length 11, with no errors at lengths 1–10. The lexicographically first is `01110101010`, whose true parity is 0 but whose exact-rational output logit is strictly positive. The exact sign was checked independently in SymPy. This demonstrates that a finite-family-perfect intervention is **not** an unrestricted algorithm certificate.

## Claim boundaries

This is a preregistered **negative transfer** result for the *specific coordinate-18 mechanism* from Run350, not a proof that no single-parameter interventions work. The other coordinates were compared only on a fixed finite family; no claim of unrestricted correctness follows. No new neural models were trained in the local Run351 analysis; the checkpoints were original gradient-trained Run348 networks. Full cohort training can be reproduced by `research/run348/train348.py`; the GitHub workflow regenerates the trajectories and stores them as a workflow artifact (retention-limited).

**Decision:** kill/demote the fixed-coordinate-18 transfer hypothesis; retain Kernel 001-S only for a representation-robust diagnostic tied to independent generalization or inductive correctness. Do not call this a field-level breakthrough.

## Active kernel specification (001-S)

1. **Precise question:** Can an invariant-based, representation-robust diagnostic predict actual unrestricted algorithm acquisition in gradient-trained networks rather than certificate-specific geometry?
2. **Frontier:** Existing RNN inductive verification, automata extraction, and convex readout obstructions; novelty priority unresolved.
3. **Next scalar success:** prospectively frozen AUROC improvement >0.05 over training loss on independently evaluated unseen architectures/tasks, plus exact spoof rejection; avoid the failed Run341 circular certificate endpoint.
4. **Strongest competitor:** architecture/representation-specific geometry and finite-range memorization.
5. **Cheapest falsification:** test an invariant-derived score on existing heldout trained checkpoints and adversarial zero-run families before training more.
6. **Publishable threshold:** primary-literature priority, exact proof or frozen evidence, independent checker, strongest spoof, mechanism-derived unseen prediction, smallest claim.
7. **Learning relevance:** original gradient-trained networks with an independently measured generalization transition, not automata in isolation.
8. **Kill condition:** three substantive independent failures of the reformulated mechanism, or one unsound claimed certificate.

**THEORY ledger:** Finite-family accuracy remains spoofable; Run350 coordinate identity is not a transferable certificate.  
**LEARNING ledger:** Gradient-trained networks exhibit heterogeneous causal coordinate responses; single-coordinate interventions can improve, worsen, or leave bounded generalization unchanged.
