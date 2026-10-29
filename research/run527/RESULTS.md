# NOESIS R527 — prospective interleaved-transition falsifier

**Decision:** Four new independent seeds 52701–52704 passed all 26 prospectively frozen functional gates and all independent numerical/oracle checks. **Pilot only**, not a 32-seed confirmation, hidden-state mediation, emergent DFA discovery, or new theorem.

## Distinct experiment
Source-faithful Howe DeltaProduct d112 n_h1, 40 epochs, 4,000 balanced length32 training words per seed, Adam .003, dense running DFA-state supervision. New 18-arm physical experiment: outer N/C/S blocks, middle N/C 45-bit bridge, second outer N/C/S block, exact 1–5-gram matching across all 18 arms, identical physical prefix/suffix, length512. 45-bit outer NC versus CN have equal full DFA action; 60-bit outer NC versus CN have different action when separated by the transposition bridge. The middle N/C bridge changes action; N/S shams do not. All three designated prefix states and no-cycle controls.

22,504 new physical words, globally disjoint from 374,588 earlier; 192 eighteen-arm groups, exact full-action/oracle/lexical/nonrecurrent scan/duplicate checks zero failures. Label-exposure maximum disparity .002523 (<.02).

| seed | +b original512 | +b global Wbzero512 | trained -b512 | globalzero 18-arm joint | 45 NC/CN TV | 60 NC/CN TV | bridge N/C TV | non-ceiling true-p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 52701 | .3333 | 1 | 1 | 1 | .00000082 | .61477 | .60529 | .69551 |
| 52702 | .3333 | 1 | 1 | 1 | .00000181 | .60413 | .59429 | .67048 |
| 52703 | .3333 | 1 | 1 | 1 | .00000149 | .56630 | .57249 | .70650 |
| 52704 | .3333 | 1 | 1 | 1 | .00000165 | .61723 | .62666 | .72680 |

Original additive-on cycle accuracy .3090–.3507; global ablation and trained additive-off 100%. Local span, individual outer-slot, and bridge-only ablations did not recover performance. 30,888 raw predictions; independent FP64 checker examined 408 rows, zero categorical errors, max probability error 3.15714e-5 (<.002), normalized logit error .00016902 (<.0005). Absolute logit max .00112511 descriptive only. **R518–R521 strict <=.001 absolute-logit gate remains FAILED 7/3584; not repaired.** Exact isolated seed52704 +b replay matched all model tensors, optimizer, and 40 losses. An interrupted seed52701 +b attempt after epoch20 without checkpoint was logged and restarted from the frozen seed.

Pre-neural protocol SHA256: 21632723aca5eaaaf6f2d1912d2833ced9e2a184a7193b8006048cbed7af17a3.
Primary SHA: ad7eab54bd44f6ae2e291f83bfa624e7701227429b6630100f7eae738dcddad3.
Independent SHA: 9210fbc018a958b67589e6af0d3e8dea8dad981c522ca74f183b2d870016d833.
Corpus SHA: b484fffd4a855ddf4c537073694a60cd730efa7c56f041bece4cf7fef7aa3254.
Full SHA256-verified archive: NOESIS_R527_Reproducibility.zip, SHA256 5e27a17f8faa0abe201294ddec9b5e2bbd8fcdbde072a720ee123320341ebde9, 117 verified payloads, immutable nested R526 verified, ZIP CRC pass.

Four-of-four hypothetical one-sided p0=.5 floor .0625. A new, separately frozen disjoint >=32-seed confirmation is needed. Published Howe additive-path effect is prior art; nonrecurrent associative/permutation scan remains a viable alternative. No spending or user laptop access.
