# Run289: gauge spoof of Run288 diagnostic
Frozen before testing: commit d5ca7f7f806a08b8314095f9c58342d4244e9a68.
PRIMARY FALSIFICATION: G=diag(8,1/8) is a function-preserving positive ReLU conjugacy. 184/256 actual gradient-trained checkpoints changed LP score >1e-6; max absolute change 13.76247. Certifiability ROC-AUC 0.81594 -> 0.75527; 7543/32619 pairwise score rankings inverted. Original and transformed models produce identical logits on every finite word under exact-real arithmetic. Independent Fraction checker passed.
THEORY: ReLU(Gz)=G ReLU(z), A'=GAG^-1, b'=Gb, v'=vG^-1. Standard gauge symmetry, not a novel theorem. Raw score cannot be a representation-invariant model-agnostic certificate.
LEARNING: 256 previously trained Adam/BCE RNNs; no retraining and no new acquisition transitions. Future certifiability labels unchanged. Raw score may still be a useful coordinate-dependent predictor.
EXPLORATORY posthoc: Bias-column maxabs normalization d_i=1/max_x|b[x,i]| yields identical canonical scores across all tested gauges, AUC 0.79640. Not prospectively validated.
LIMITS: Positive diagonal ReLU gauges only; exact-real not indefinite IEEE-754; same verifier-family endpoint; 209 noncertificates are unknown, not incorrect. No field-level breakthrough.
PRIOR ART: Neyshabur et al., Path-SGD, NeurIPS 2015; Buitrago & Gu, Understanding and Improving Length Generalization in Recurrent Models, ICML 2025.
