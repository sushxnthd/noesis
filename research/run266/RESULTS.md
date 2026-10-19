# Run266 — full-alphabet switch falsification

Frozen cohort: 16 of 37 length-20 finite-perfect checkpoints with no certified wrong attractor in Run265. Input generator: all 244 words of length 2–5 containing both SET and RESET, each followed by at most 2048 HOLD tokens; check every intermediate output. All 16 are independently initialized, gradient-trained 2D ReLU latch networks from Run264. Exact binary64 coefficient semantics, ideal real arithmetic.

**Result: 10/16 newly falsified**, spanning **7 independent training seeds**, all first errors after position 20. Both independent exact-integer and Fraction checkers agree on every witness. Frozen scalar success criterion (>=5 new witnesses across >=3 seeds) MET. Delayed error lengths: 31, 33, 33, 34, 42, 44, 51, 216, 239, **1338**. The longest witness is seed 18440 epoch600, word [RESET,SET,SET,SET,SET] then 1333 HOLD operations. It is minimal only within the fixed generator for that checkpoint; no global shortest-witness claim.

**Six abstentions:** 18405 epochs300/600, 18409 epochs100/300/600, 18454 epoch100. No numeric counterexample within the frozen generator is not a proof of all-length correctness. Run265's 21 wrong-attractor certificates concern a disjoint set of 21 checkpoints; thus 31/37 finite-perfect checkpoint instances now have either a prior exact failure certificate or a new exact switch witness. This does not establish all 31 distinct seeds.

**THEORY ledger.** A sublanguage attractor diagnostic's abstention does not imply full-alphabet correctness. Exact switch witnesses rule out all-length correctness for the specific stored networks. No universal law or positive certificate established. All 10 exact witnesses use both SET and RESET, not only HOLD.

**LEARNING ledger.** Finite-perfect gradient-trained RNNs can fail on delayed cross-symbol sequences. Seed18454 was not falsified at epoch100 by this generator but was exactly falsified at epochs300/600; do NOT infer that epoch100 was correct. No new training was conducted in this run; this is a frozen adversarial evaluation on previously trained checkpoints.

**Limitations.** Exact binary64 parameters interpreted as rationals; ideal-real inference, not physical floating-point deployment. 6 null results are search-horizon abstentions. 244 prefixes and 2048 holds are a fixed finite generator. No second architecture/task and no primary-literature novelty established. Prior frontier: Ryou et al. CAV2021 polyhedral RNN verification; Van Rossem and Saxe ICML2025 streaming parity algorithm development.

**Next kernel.** Target a model-specific full-alphabet inductive certificate on surviving checkpoints (especially 18409) with strict no-leakage train/test partition; kill K001 after 3 substantive failed attempts. Do not merge while claim boundaries remain unstable.

**Provenance.** Frozen protocol was committed before local enumeration; source candidate SHA256: 74cb0aaa22605ba2d263719b1078a4603e435bf0977723481e6c1ab15d780b72. Full local archive includes raw 244x16 first-error matrix, source scripts, training checkpoint subset, independent checker logs, and hashes. GitHub CI independently replays the 10 witnesses and regenerates the numerical matrix as an artifact.
