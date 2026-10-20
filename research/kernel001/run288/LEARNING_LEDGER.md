# LEARNING ledger — K001 Run288
- 256 new neutral-Gaussian initialized width-two ReLU recurrent networks, ordinary Adam lr 0.025 and BCE on 164 length-six training strings per seed, no task-biased initialization. Seeds 20928–21183, 15 trainable float64 parameters, epochs 0..120. No user laptop.
- Epoch20: 18 sampled-perfect, 7 exactly certified. Epoch80: 127 sampled-perfect, 47 exactly certified; 132 exact wrong-word witnesses across all models; 77 unclassified by either sound endpoint.
- Four actual natural transitions from epoch20 sampled-perfect, exact incorrect to epoch80 certified: seeds 20977, 21000, 21012, 21113; early exact witness lengths 17, 30, 10, 14. The frozen >=5-transition learning threshold FAILED.
- The frozen score predicts certificate onset, but does not establish that an unverified model remains heuristic. Only three epoch80 sampled-perfect models have confirmed exact wrong words. No all-length incorrectness claim for unknowns.
- Independent exact checker: 141 certificates, 378 witnesses across snapshots; fresh-process training checkpoint SHA256 identical.
- Next highest-information falsification: precommit cross-architecture (e.g. GRU or Transformer) correctness endpoint and matched non-certificate verifier; do not claim a universal law from this architecture-specific LP score.
