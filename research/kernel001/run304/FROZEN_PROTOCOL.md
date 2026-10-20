# NOESIS Kernel 001 — Run 304 frozen retrospective transition audit

Commit this protocol before running the Run304 checker. This is **retrospective** because late-epoch certificate-positive seeds were already discovered in Runs 300–303. Do not describe it as prospective prediction.

## One active kernel: learned latch algorithm acquisition
1. **Precise question:** Among the 18 previously exactly certified all-length-correct epoch-80 gradient-trained latch RNNs, how many have an independently exact incorrectness witness at epoch 20, establishing an actual within-trajectory correctness transition?
2. **Literature frontier:** RNN inductive invariants and reachability verification are established (Jacoby, Barrett & Katz, ATVA 2020; Khmelnitsky et al., ATVA 2021). Neural length-generalization studies distinguish extrapolation from algorithm learning. This audit is not a novel general verifier.
3. **One exact success criterion:** At least **12** of the 18 epoch-80 certified networks have a **rational-arithmetic wrong-output prefix of length at most 6 at epoch 20**, and each epoch-80 certificate is independently checked over the original binary64 weights.
4. **Strongest competing explanation:** Late-epoch certification selects an easy architectural subset; early error merely reflects normal loss minimization. This audit cannot establish a predictor or mechanism.
5. **Cheapest decisive falsification:** Independent exact check of all 18 late certificates plus lexicographic exhaustive early-prefix search over {0,1}^1..6, comparing every prefix output to persistent-latch targets.
6. **Publishable threshold:** Not publishable alone. Needs a new mechanism-derived prediction prospectively frozen on unseen training conditions, primary-literature priority audit, spoof controls, independent reproduction, and improvement beyond training loss.
7. **Learning-system relevance threshold:** Same-seed, unmodified epoch-20/80 gradient-training checkpoints, with one exact early counterexample and an exact all-length late proof for each transition.
8. **Kill condition:** Fewer than 12 valid pairs, any false late certificate, or provenance mismatch. After three substantive failures to strengthen this active kernel, reformulate/kill.

## Frozen sources and method
- Source Run303 archive: `NOESIS_kernel001_run303_continuous_cone_exact_transition.tar.gz`.
- `source_checkpoints300_early.json`: SHA256 `0aa10a00406a6316d2808a7d1424022724c7ce75a5cbbdc741dd0ad44ef2f6a1`.
- `source_checkpoints300_late.json`: SHA256 `71f384d19e4e5ae95198b6bce2ec35f29f547b166ba293ffae60fe8a2d2d6f8d`.
- `source303.json`: SHA256 `5e4dabeb53f478a14ef2f26df1bd3af78f48c33a890d251c566801f11717b7b1`.
- Model: width-3 ReLU recurrent binary-input latch, 28 float64 parameters per checkpoint, initial hidden state zero, output bit 1 iff logit > 0. Targets latch of whether a 1 has occurred in prefix.
- Selection: exactly all 18 epoch-80 networks satisfying Run303 fixed-readout scalar-cone sufficient condition. No further selection on early outcome.
- Enumerate all nonempty words of lengths 1..6, shortest first, lexicographic tie-break; compute exact binary64-rational recurrence and first mismatched prefix. If none found, record **unresolved**, not correct.
- Verify each late certificate independently, not importing the search function; perturbation controls must fail. Preserve per-seed raw checkpoint pairs and all negative/unresolved results.
- THEORY and LEARNING ledgers separate. Report transition count, early witness lengths, and late proof status without asserting a general acquisition law.

## Controlled wildcard
Only if cheap after the primary test: inspect whether the earliest exact failure for each selected early checkpoint is a zero-only versus latch-retention failure. This does not change the frozen criterion.
