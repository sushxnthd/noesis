# NOESIS R505: final-label-only complex-conjugate recurrent learning

## Scope and frozen protocol
Historical R382–R504 and primary literature audited; all old checkpoints retired. TaskC generators: symbol 0 swaps states 0/1, symbol 1 swaps 1/2. Physical cycles N=000110001111100 and C=000111110001100 match exact 1..5-gram spectra, length/ones/endpoints, Hamming6 but have different state actions. Same-action shams SN=001111100110000 and SC=001111000111000 match 1..3-grams and Hamming6, NOT 4..5-grams. Exact permutation scan remains perfect classical alternative.

Frozen BEFORE neural outcomes: protocol SHA256 cc5f9ab9d053c65ce71b9bbe3d25df47908d1abc5c9a2fe457197bd572600cc6; primary source c9942a6ca191ed1511145d5d9e0fd07abff761e6b79fdb05722ca71f02ab5597; independent checker acff19d0768abaeec8128e60752dd8b1ac64d4ca09562435b5e3734c870996c7. Original primary failed before neural outcomes from a missing grams(C,5) argument. Original source/traceback retained; pre-outcome count-only recovery source SHA bbb516a8e7baba2588eed99d30b52738a9dd099b7ba9c420ccf2baaf6795145e.

## Prospective disjoint pilot: FAILED
Four NEW seeds 50501–50504, fixed-width 2D complex-conjugate recurrence h_t=exp(i theta_b) conj(h_(t-1)), learned symbol angles/initial state/linear readout. Final sequence labels ONLY; no intermediate DFA-state labels. This model imposes a dihedral/S3 representation by design, not an unconstrained neural automaton discovery. Fixed 1,400 Adam steps, no retuning. Each seed: 2,400 q-balanced train, 300 validation, 300 no-cycle test words length10..29, plus 768 physical matched-cycle evaluations length29. 15,072 globally unique words.

Train/validation/no-cycle test/length29 and N/C paired both-correct accuracy were 100% in all 4 seeds. Learned phase differences were within 0.00353–0.00808 radians of ±2π/3. BUT frozen non-ceiling neutral true-label probability gate (0.55..0.95) FAILED 0/4: 0.999848..0.999868. Frozen N/C JS gate (0.03..0.55 nats) FAILED 0/4: observed 0.69233..0.69238. Same-action sham JS=0; baseline and locality gates passed, but locality ratio is numerically inflated by zero sham denominator. Overall feasibility FAILED, no 32-seed confirmation, no learned causal mediation.

## Independent and postprimary checks
Pre-frozen NumPy checker physically iterated all 15,072 saved words, maximum logit difference 2.665e-14, zero classification/oracle/permutation-scan/lexical/action errors. One isolated full four-seed deterministic replay matched 14/14 scientific hashes.

Separately frozen POSTPRIMARY exploratory hidden-state audit: 48 natural q0/q1 prefixes per seed; 100% prefix+cycle labels, but max neutral-return/changing-distance ratios 0.08516, 0.07088, 0.11409, 0.05282, failing exploratory <=0.05 gate 0/4. Same-action sham displacement ~1e-16. Independent checker verified 768 physical prefix/cycle hidden states, max algebraic-vs-literal error 3.775e-15, zero oracle/action errors. Output correctness does not force exact pointwise hidden q-neutral return in this nonminimal learned group representation; this is not a new general theorem or hidden-state causal mediation.

## Preservation and next direction
Complete SHA256-verified NOESIS_R505_Reproducibility.zip SHA f35c36b600a6f810240b0c7c253b8ed18bf236b153f993603e995feb4986c3b0; 60 local payload hashes, immutable nested R504 archive with 49 independently verified payloads, ZIP CRC PASS. All checkpoints/raw/corpora/optimizer logs/frozen protocols/negative results/recovery/independent checks preserved.

R506: RETIRE R505 architecture/seeds/checkpoints; do not retune calibration, temperature, thresholds or old seeds. Seek genuinely DISTINCT identifiable non-ceiling on-support causal transition effect or sharp neural-specific necessary condition with independent checker, matched sham/no-cycle/lexical/q-changing controls and exact permutation-scan baseline. No off-support hidden-do/path mediation overclaim. Prospective >=32 NEW seeds only after disjoint pre-frozen pilot passes all gates and exact power design. Zero spend/laptop, no routine notifications.
