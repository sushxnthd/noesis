# NOESIS Kernel 001 — Run 162: numerical-semantics falsification

## Decisive result (prospectively frozen before evaluation)
The exact-rational all-length counter certificates for the Run 160 *repaired* networks do not transfer to binary32 execution. The first increment-only absolute counting errors exceeding 0.1 are:

| Original Adam checkpoint | First binary32 failure | Readout | Signed error |
|---|---:|---:|---:|
| seed 222 | 3679 | 3678.89990234375 | -0.10009765625 |
| seed 239 | 3582 | 3582.10009765625 | +0.10009765625 |

Both are first crossings under the declared arithmetic order (each product/add rounded to binary32; no fused multiply-add). Independent NumPy full-matrix checker agrees. The binary64 scalar control did not cross 0.1 through two million increments. These are **restricted-language** results, not globally shortest all-alphabet failures.

### THEORY ledger
The Run 160 exact rational inductive proof is not refuted. Finite precision is a different transition system. In particular, the invariant ray remains active but rounding of the repeated increment creates cumulative error. This result demonstrates why a certificate must specify execution semantics, threshold, and horizon. The general observation is well known; **no novel theorem is claimed**.

### LEARNING ledger
Both starting weights came from actual gradient training; Run 160 then applied a task-aware exact repair. These outcomes describe the repaired models only. They do **not** show that training acquired an exact algorithm or that a learned heuristic was finite-range. No new training was performed.

### Active kernel contract (exactly one)
1. **Question:** Can a task-coupled, representation-agnostic, execution-aware diagnostic predict when unchanged gradient-trained systems acquire reusable algorithms rather than finite-range heuristics?
2. **Frontier:** El-Naggar et al., ICGI 2023, https://proceedings.mlr.press/v217/el-naggar23a.html (exact ReLU counting conditions and training failures); El-Naggar et al., EACL SRW 2023, https://aclanthology.org/2023.eacl-srw.15/ (exact linear-RNN conditions); Park et al., Neural Networks 2024, DOI 10.1016/j.neunet.2024.106297 (floating-point expressive-power differences).
3. **Single scalar success criterion:** >=75% prospective classifications on 16 frozen independently trained networks, with zero false-positive all-length certificates against cap spoofs.
4. **Strongest competitor:** post-hoc task-semantic injection, architecture-specific conditions, numerical artifacts, and selection bias.
5. **Cheapest falsification:** test every candidate on finite-cap spoof and a delayed-activation trained counter; reject any false positive.
6. **Publishable threshold:** independent checker, primary-literature novelty audit, unseen task/architecture prediction, and frozen training-transition evidence.
7. **Learning relevance threshold:** predictions must apply to *unchanged* trained weights and correlate with or predict acquisition/generalization transitions, not only repaired systems.
8. **Kill:** any false-positive all-length certificate, or three substantive failures to strengthen the current candidate; reformulate without hiding negatives.

**Inactive backups (two):** training-time transition intervention; alternative task quotient.

### Reproduce
Run `python research/kernel_001/run162/audit162.py`, then `python research/kernel_001/run162/independent162.py`. Both archived checkpoints and JSON outputs are in this directory. The Run 160 exact rational repair is recreated in the audit. `python -m pytest -q research/kernel_001/run162/test_run162.py` tests the frozen outcomes.

### Provenance and limits
The frozen protocol was committed before computing results. The previous Run 161 research workflow failed because pytest was not installed; that failure is preserved. A workflow fix is included in this branch. No new field-level breakthrough.
