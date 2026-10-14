# Run 157 extension — all-length fixed-mask negative certificates

**Exact theorem.** For a trained ReLU recurrence h'=ReLU(Ah+E[s]), h(0)=0, suppose for increment symbol 0 there is an index k with A[k,k]=1, E[0,k]=u>0, and A[j,k]<=0, E[0,j]<=0 for all j!=k. Then for every n>=0, h(0^n)=n*u*e_k and readout error is n*(w[k]*u-1). Proof: induct on n. The active coordinate increases by u; every other preactivation is nonpositive. This is a sufficient *negative certificate* when the drift is nonzero, not a novel universal counting theorem.

**THEORY:** Archived gradient-trained seed222 (width 4, k=2) has exact drift 2867239603229041020385921/50000000000000000000000000000000 per increment, hence the first increment-only error strictly greater than 0.1 occurs at **1,743,838**. Seed239 (width 6, k=4) has exact drift 110411946954539124853909/50000000000000000000000000000000 and first crossing at **45,284,955**. Every earlier increment-only word is below threshold; every subsequent one exceeds it. No ReLU activation-mask changes occur for any increment-only length.

**LEARNING:** Both unchanged checkpoints were trained by Adam on all length-six ternary sequences (1200 steps, neutral latent regularization 0.1); training MSE 2.991490071416634e-15 and 5.198301033232786e-17. This retrospective discovery does not demonstrate a new training transition or positive algorithm-acquisition certificate.

**Scope:** Not a globally shortest all-alphabet failure. These are restricted-language, all-length *negative* certificates. Known exact-counting conditions in El-Naggar et al. (ICGI 2023) limit novelty. The failure mechanism is a tiny persistent readout-scale defect with a perfectly stable neural activation pattern, not delayed activation.

**Reproduce:** `python research/kernel001/run157/certify157_closed_form.py research/kernel001/run157/RUN157_SEED_222.json research/kernel001/run157/RUN157_SEED_239.json`; independently `python research/kernel001/run157/independent157_closed_form.py research/kernel001/run157/RUN157_SEED_222.json research/kernel001/run157/RUN157_SEED_239.json`. Exact proof checks full-dimensional recurrence for 100 steps as a regression test and derives the all-length identity by induction.

**Decision:** Keep Kernel 001 focused on task-coupled all-alphabet simulation. A fixed activation mask, even for all lengths, does not imply correct learned algorithmic behavior. No field-level breakthrough.
