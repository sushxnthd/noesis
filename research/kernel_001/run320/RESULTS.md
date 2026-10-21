# Run 320 outcomes — exact local verification
- Original trained seed22242 epoch80: readout-normalized cone certified.
- All 24 exact hidden-coordinate gauge transformations: 24/24 canonical tuples identical, 24/24 certificates pass, 24/24 exact trace conjugacy checks pass.
- Independent SymPy checker: 24/24 passed; delayed seed rejected; 2 mutated controls rejected.
- Delayed trained seed22642 epoch80: rejected because its readout has 3 positive coefficients, not 2 positive + 1 negative.
- Development-only 96 checkpoint census (Run315): 37/96 canonicalized, 0/96 certified; all 4 previously certified endpoints were rejected by the sign-pattern gate; 43 witnessed-incorrect and 49 unresolved endpoints also rejected.
- No prospective predictive result, no new trained models, and no improvement over training loss. This is a limited proof-alignment diagnostic; the fixed cone/sign gate is killed as a general acquisition predictor.
- Exact source checkpoint SHA256: 9bc2e054c5d9779b8dd616be04768d3f2c1bf97cd140d96f3472a5d1f936c37c
- Exact cohort checkpoint archive SHA256: 72a273a42258e55f1092dc26664fd91777a8d2e56d6d598469e2abc0e63fab20
- Full raw outcomes, cohort checkpoints and independent checker preserved in the downloadable local Run320 archive; not all bulky files are in this branch.
