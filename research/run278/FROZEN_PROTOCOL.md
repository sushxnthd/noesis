# NOESIS Kernel 001 — Run 278 protocol

Status: locally frozen before calculation (SHA256 364c5adcaec312db839538ed621913327f77f8f7ee7fdb5dc2e5fde1cfd29189). GitHub publication followed the local experiment; this is not a public preregistration.

1. Question: can <=2 certificate-directed parameter edits turn sampled-perfect but exact-witness-wrong gradient-trained networks into unrestricted-correct ones without reducing sampled accuracy?
2. Primary frontier: van Rossem & Saxe (ICML 2025) on learned infinite generalization; Jacoby et al. (ATVA 2020) and Ryou et al. (CAV 2021) on RNN invariant verification.
3. Exact success: >=9/11 fixed checkpoints certified with <=2 changed recurrent parameters, preserving 3396/3396 sampled predictions.
4. Strongest competitor: architecture-specific projection into a known sufficient invariant; no learned-algorithm law.
5. Cheapest falsification: exact rational repair, independent SymPy interval-image proof, original witness and sampled-set replay; matched random controls.
6. Publishable threshold: independent held-out task or architecture, statistically meaningful matched-control advantage, full priority audit.
7. Learning relevance: 9/11 real BCE/Adam-trained checkpoints repaired without retraining, original sampled accuracy intact.
8. Kill: <9 repairs, unsound positive proof, or sampled-accuracy loss.

Frozen seeds: 19900, 19937, 19948, 19956, 19959, 19970, 19974, 20049, 20095, 20120, 20138. Original epochs and exact IEEE754 parameters in checkpoints_part*.csv. Only a[0], b[0], a[2] may change; project HOLD region and RESET sign as specified by core.py. Controls: 32 seeded matched-L1/cardinality random-coordinate edits plus 32 stronger same-coordinate random-sign edits per model. Report all failures. No other active kernel.
