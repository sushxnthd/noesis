# NOESIS R498: complete-state-selective same-word crossover (negative feasibility)

**Kernel:** learned DFA-state retention under per-designated-complete-state-neutral cycles. Four NEW GRU hidden16 seeds 49801–49804, 90 epochs, q-balanced natural words at lengths 14/18/21/25. Frozen protocol SHA256 `7a6446ef97cbc1c50403e56f2f9234267bb23e9ef25fbcdeb1f41c3c3145dbea`.

**Physical causal contrast:** N=1101010 is q-neutral from natural prefixes ending 0 but q+2 from those ending 1; C=1111000 is q+1 from ending 0 but neutral from ending 1. Both length7/four ones/start1/end0, Hamming2. N_SHAM=1011010 shares N's state-conditional action. 576 heldout prefixes in 288 q/ones-matched last-bit-opposed pairs; 11,520 physical evaluation words, 4,608 disjoint q-balanced training words. All evaluated lengths are in training support.

**Frozen gates (>=3/4 seeds):** no-cycle baseline 4/4 PASS; four-cell crossover shift accuracy 4/4 PASS; same-action lexical sham 4/4 PASS; genuinely non-ceiling circular true-shift correlation 0/4 FAIL (0.997462,0.998181,0.998110,0.981509, above max0.95). **Overall feasibility FAIL**; no 32-seed confirmation, no learned causal mediation, no neural necessity or novelty claim.

**Independent verification:** 11,520/11,520 categorical and DFA/parallel-scan checks pass, but pre-frozen float32-vs-independent-float64 logit max-error <=1e-4 FAILS at 1.594212e-4. Postprimary separately frozen native double PyTorch GRUCell agrees with independent manual double to 2.394e-13, 0 flips; original numerical gate remains FAILED. Exact postprimary corpus audit 0 errors. Two isolated full four-seed deterministic training replays each matched 11/11 scientific hashes.

**Preservation:** full SHA256-verified local archive NOESIS_R498_Reproducibility.zip, SHA256 `d50d1e6d485510b40b3e4102d554f37534ab24129605065ddb7ef81e8a4ed31d`, 65 verified payloads and immutable nested R497 archive; ZIP CRC pass. Includes frozen sources, protocols, all checkpoints, corpora, 11,520 raw logits, 360 epoch records, independent numerical failure, postprimary diagnostics, and both replays.

**Next:** retire this fully supervised near-ceiling crossover pilot. Prioritize a distinct sharp neural-specific necessary-condition/impossibility or independently feasible non-ceiling experiment, not another small GRU/LSTM supervision or lexical variation.
