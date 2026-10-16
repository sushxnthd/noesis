# Kernel 001 / Run 199
1. Question: Can task-margin search detect errors in unseen trained modulo-three RNNs?
2. Frontier: van Rossem & Saxe (ICML 2025); Weiss et al. (ICML 2018).
3. Criterion: median (1+adaptive errors)/(1+strongest baseline errors) >= 1.5 over 8 checkpoints.
4. Rival: local error clustering, not algorithm structure.
5. Falsifier: frozen seeds 283,293,307,311 at epochs 400/800; 455 queries per method.
6. Publishable: cross-task/architecture, independent proof, prospective transition prediction.
7. Learning relevance: actual Adam-trained width-12 tanh RNNs, failure detection only.
8. Kill: third failed transfer kills adaptive finite-query diagnostic.

Outcome: PASS (1.832167832). Keep finite-query search only as an auxiliary. No all-length certificate or field-level breakthrough.
