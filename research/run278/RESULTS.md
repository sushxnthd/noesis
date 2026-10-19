# Run 278 — locally verified; GitHub CI pending

11/11 previously incorrect gradient-trained checkpoints were converted to unrestricted-correct models by post-training changes to at most two recurrent parameters. Eight required one coordinate and three required two. All 11 exact rational and float64-representable repairs passed an independently implemented SymPy image-inclusion checker. Sampled accuracy remained 3396/3396 for all 11 before and after intervention (283 sequences x 12 positions). Random-coordinate matched-L1/cardinality controls: 24/352 certified (6.8%). Same-coordinate random-sign controls: 125/352 (35.5%). Frozen criterion >=9/11 passed. This is a retrospective, architecture-specific proof-directed intervention, not a general algorithm-acquisition law.

Source Run277 checkpoint SHA256: 91fab4550b037a475673fe7d07b4c2ef73bb87b6ecb1c16565f0e884c71ae79b.
Local pre-run protocol SHA256: 364c5adcaec312db839538ed621913327f77f8f7ee7fdb5dc2e5fde1cfd29189.
Run277 metadata incorrectly says training length 20; executable train277.py uses T=12. Run278 follows the executable training code and preserves the discrepancy.
