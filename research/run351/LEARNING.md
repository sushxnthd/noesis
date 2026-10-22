# LEARNING ledger — Run351

**Training provenance:** Run348 gradient-trained width-three ReLU prefix-parity networks, original 192-seed trajectories; fixed intervention cohort 32000–32063, 64 seeds. No new models trained for local Run351 analysis.

**Selection:** Earliest training-perfect epoch before 200; 29 eligible, 35 ineligible. One next-step gradient-update coordinate is substituted at a time, with the original readout unchanged.

**Measured causal effects:** Coordinate 18 improves the 2,644-word heldout family for 1 eligible seed (+9 words), worsens 4, and is unchanged for 24. It is never uniquely best with >=27 additional correct words. Other coordinates can be substantially more effective: seed 32034 coordinate 8 improves 107 words; seed 32026 coordinate 5 improves 98 words. Seed 32046 coordinate 17 repairs all 2,644 frozen words but fails on a length-11 adversarial input.

**Conclusion:** The Run350 coordinate-18 intervention is not a generalizable cross-seed acquisition mechanism. Future diagnostics must predict independent correctness rather than the same template used to define success.
