# LEARNING ledger: Run 350

Frozen scan: 24 individual parameter replacements and four fixed blocks from the original gradient update (seed 32135, epochs 82 to 83). Only single coordinate 18 succeeds, as does block b0; the epoch-83 endpoint is a positive control and epoch-82 endpoint a negative control. Parameter 18, the input-zero bias for hidden coordinate zero, changes 0.11926709043401072 -> 0.07560443732456557.

With the **original epoch-82 output head unchanged**, exact results on 2,644 frozen words are epoch82 2556, one-coordinate intervention 2644, epoch83 2623 correct. Posthoc extension: 2766/2766 on the fixed generator through length 25; float64 exhaustive 2,097,150/2,097,150 nonempty words through length 20. Nonetheless the exact infinite family 1010^n fails for n>=23.

This is a genuine causal improvement in finite-horizon behavior and readout repairability of an originally gradient-trained representation. It is **not algorithm acquisition**. This one-seed intervention was selected after examining a prior training trajectory; cross-seed replication is required.
