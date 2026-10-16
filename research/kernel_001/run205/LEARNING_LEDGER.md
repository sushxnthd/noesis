# LEARNING ledger — Run 205

Frozen seeds: 211,223,227,229. Torch float64 Adam 0.03, all-prefix BCE on all 64 binary length-6 words, 800 epochs. Checkpoints 0,20,50,100,200,400,800. CPU only.

Seed 211: never certified; epoch800 training accuracy 0.58333, 4007/8192 held-out length-64 prefix errors.
Seed 223: epoch0 training accuracy .5 and not certified; from epoch20 through 800, training accuracy 1.0, zero long-prefix errors and all-length certified.
Seed 227: epoch50 training accuracy .671875 and not certified; epochs 100..800 certified, train accuracy 1.0, zero long-prefix errors.
Seed 229: epoch50 training accuracy .6640625 and not certified; epochs 100..800 certified, train accuracy 1.0, zero long-prefix errors.

Across 28 checkpoints: 14 certified and 14 abstentions. Among frozen epoch400/800 endpoints, 6/8 certified, meeting primary criterion. Transitions are bracketed between checkpoint snapshots, NOT timed precisely; certificate abstention is not a proof of failure. Long-prefix tests: 128 sequences x64 and 32 sequences x256 per checkpoint, with prefix accuracy. All-length certificates are stronger than these samples.

Limit: The input-gated scalar architecture can express parity naturally. A positive result on this architecture is not evidence of a model-agnostic law or transferable acquisition certificate. No causal intervention established.
