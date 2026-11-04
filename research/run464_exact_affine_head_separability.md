# NOESIS R464: exact affine-head obstruction in frozen R418 neural representations

**Status:** Decisive checkpoint-specific neural-relevant falsification of affine-head-only repair, not a general neural theorem, prospective replication, or identified neutral-cycle mechanism.

Frozen before new hidden-state outcomes: primary protocol SHA256 `0178256e11c9e23a37358643740cade6a803974ea06c02b697dd98a10ae584a2`; original source SHA256 `da775d08f21f04cabb22de8797da89e2387fa2e12a90306914504a8cea837f23`. Original R418 frozen models: both DFA tasks, LSTM/GRU/MGU, seeds 99960–99963, all 256 physically realizable eight-bit inputs. Three sets per model: original unique training support, training plus frozen R462 neutral panel, and full 256. No training or hidden-state intervention.

## Exact result

For a fixed binary64 recurrent representation h(x), strict three-class affine separability requires (W_y-W_j)h(x)+(b_y-b_j)>0 for every selected physical input x and wrong class j. The primary LP fixed class 2 to zero, bounded the other coefficients in [-1,1], and maximized common margin. Independently verified exact rational positive-margin head witnesses certify **22/24 models in each of all three sets** (66 cases); minimum certified normalized margin >0.2028048586.

The remaining **2/24 models**, Task B LSTM seeds **99961 and 99962**, are rigorously **not** affine-separable even on their original training support. Independently checked exact rational convex-hull intersections of differently labeled frozen hidden states certify all six negative set-level cases:

- Seed 99961, training support: class 0 inputs 00000000, 10101010, 10101011, 11111000 and class 1 inputs 01010101, 11111010, 11111101 have equal exact rational convex combinations in all five hidden coordinates. Smallest positive barycentric coefficient ~0.00710757.
- Seed 99962, training support: class 0 inputs 00000000, 01010011, 01010100 and class 2 inputs 00101110, 01000011, 01000111, 01010000 have equal exact rational convex combinations. Smallest coefficient ~0.00605277.

No affine head, regardless of optimization, can strictly classify both oracle classes at an identical convex-hull point. Thus R463's bias-only no-go is strengthened to an **arbitrary affine-head no-go for these two original checkpoints**. Other 22 checkpoints, including Task B LSTM seed 99963, are strictly separable on the full universe.

## Independent controls and numerical robustness

Independent pure NumPy recurrence verified all 6144 Torch original physical readouts, maximum hidden-coordinate difference 5.84255e-15 and maximum logit difference 1.82077e-14. All 66 positive cases were rechecked with exact binary64 rational inequalities. Nine exact convex-intersection witnesses across six negative cases were independently reconstructed. Separately frozen postprimary robustness protocol fixed entrywise hidden-coordinate perturbation epsilon=1e-10; exact inverse-norm perturbation certificates passed **9/9**, including both training-support obstructions. Three isolated deterministic clean replays passed **12/12** output SHA256 comparisons.

Original primary implementation failed at JSON serialization after completing all outcomes; the original error/source are preserved. The correction changed only NumPy integer serialization, not protocols, thresholds, inputs or scientific calculations.

## Interpretation and limitations

This is a *fixed-representation linear-readout expressivity* falsification, not a demonstration that insufficient training caused the geometry, not proof of any particular recurrent transition failure, and not evidence of a novel causal neutral-cycle effect. Nonlinear heads and recurrent retraining remain possible. Multiple words within a seed are not independent replications. Original training length eight versus longer physical neutral-cycle evaluations remains a confound.

Prior art: Dankowiakowski and Ronca, NeurIPS 2025, https://papers.nips.cc/paper_files/paper/2025/hash/c03c2e3e2ad8057aefc3da880476784d-Abstract-Conference.html ; Buitrago Ruiz and Gu, ICML 2025, https://proceedings.mlr.press/v267/buitrago25a.html ; Brandoit et al., September 2026, https://arxiv.org/abs/2609.32447 . Linear separability and convex-hull obstruction are classical; checkpoint-specific pre-frozen exact diagnosis is the contribution.

Complete immutable reproducibility archive: `NOESIS_R464_Reproducibility.zip`, SHA256 `36679be52cc2e5ea59079748c7075b451ee2ff184d093f48c066623d8afcbb2f`. 31/31 local payload hashes, 29/29 nested R463 payload hashes, ZIP CRC and 12/12 replay output hashes passed. Archive includes all original/frozen sources, raw hidden states, complete certificates, original errors, independent checks and R463->historical checkpoint chain.

**Next R465:** Retire affine-head obstruction as a neutral-cycle breakthrough. Seek a genuinely distinct frozen, physically realizable, non-ceiling causal readout prediction on original short-input transition-pair geometry with proper independent-seed controls. No retuning, hidden off-support interventions, or mediation attribution.
