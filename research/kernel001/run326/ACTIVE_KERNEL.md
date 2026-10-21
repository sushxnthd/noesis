# Active kernel K001-R after Run326

1. Question: Can task-observable inductive separation in an early gradient-trained recurrent representation predict later all-length algorithm acquisition, beyond early loss?
2. Primary frontier: Weiss, Goldberg & Yahav (ACL 2018), Jacoby, Barrett & Katz (ATVA 2020), Deletang et al. (ICLR 2023); finite-precision expressivity, invariant verification and length generalization are established. Novelty target is prospective prediction, not verification itself.
3. Scalar success: prospectively frozen AUROC improvement >=0.05 over negative early BCE with >=10 independently certified positives and >=30 exact witnessed negatives.
4. Competitor: representation score proxies training loss, readout calibration, or architectural/coordinate biases.
5. Cheapest falsification: exact gauge-orbit and delayed-memory spoof tests, then seed-disjoint frozen training and endpoint adjudication.
6. Publishable: replicate prospectively across a second architecture/task family, independent exact checking, spoof controls and honest unresolved accounting.
7. Learning relevance: only actual gradient-trained checkpoints and predictions before endpoint evaluation; no post-training readout calibration.
8. Kill: three substantive K001-R predictor failures. Run326 is failure 1; no threshold retuning on Run326 outcomes.

THEORY: finite-separation score survives positive gauge transformations but is spoofable; it is not a correctness certificate.
LEARNING: Run326 384 new networks; AUROC delta -0.12618, FAIL. 189 endpoints unresolved.
Backups, inactive: task-conditional quotient observables; architecture-independent local expansion/contraction regime.
