# NOESIS K001 Run310 — exact causal block swap, frozen primary FAILED

Protocol committed on isolated branch at 728b983445787caa3bef18b516229e85ed01af1a before computing outcomes.

## THEORY ledger
Eight of 19 constructed hybrids have exact rational sufficient cone certificates for all finite binary sequences. Each hybrid uses epoch80 recurrent parameters (24 coefficients), epoch20 output direction (3 coefficients), and one rational recalibrated scalar output bias. Independent implementation checked all eight proof sets and rejected 24 deliberately corrupted controls. Eleven remaining hybrids are NOT CERTIFIED, not proven wrong.

Frozen conjunctive criterion was >=5 certified hybrids WITH >=1 paired epoch20 equal-length opposite-label hidden-state collision. Only seed 22241 has such a collision among the 19; it is NOT among the eight certified hybrids. Thus **the frozen primary criterion FAILED**, and the prespecified combined sufficiency hypothesis is rejected. No post hoc threshold change.

## LEARNING ledger
The eight exact hybrid certificates show that later recurrent dynamics can support the target algorithm without changing the early readout direction in selected gradient-trained trajectories, if scalar bias recalibration is allowed. They do not establish that SGD discovered a new reusable algorithm or that these interventions explain the actual training path. All 19 pairs were selected for late certification; selection bias is substantial. No prospective predictor or cross-task law.

The eight certified seeds: 22227, 22281, 22311, 22390, 22403, 22424, 22567, 22580. Among these, 22311, 22390, 22424 and 22567 had earlier affine-readout obstructions in Run305, but this overlap is exploratory, not part of the frozen criterion.

## Provenance and limits
Source: Run304 18 paired checkpoints SHA256 5cb41eaefe2957f01d9b306537bf76cdf3a730ae2baf1ab3e007cad34534de71, plus Run309 seed22241 epoch20/80 SHA256 52e0098e3cf59c0ff5c37d6332c687b05efc3f3c6d8fd76f3aae0d4479439669 and 7f8818b31ca106cfa328bac8d9326fac0d856843ccfb472726f32e91c6fe7f96. Exact source and full 19-row outcomes preserved in the local Run310 archive. The GitHub branch currently contains frozen protocol, exact discovery/independent checker source, and eight compact rational proofs, but not yet all raw checkpoint pairs. Public full-cohort reproduction pending; generic CI must not be misrepresented as full proof reproduction.

## Kernel decision
Kill the conjunctive Run310 hypothesis as frozen. Retain K001 but reformulate next run around prospectively measurable recurrent-state information loss and transitions on an unbiased checkpoint cohort. Do not claim a field-level breakthrough.
