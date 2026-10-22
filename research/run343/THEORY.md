# THEORY ledger — Run 343

**Theorem (specific trained model, exact-real inference).** Let `f` be the original Run342 seed-31089 epoch-200 width-four ReLU parity classifier with weights in `model343.json`. Then `f` is correct on every nonempty binary word of length <=12 and wrong on every word `1 0^k` with integer k>=12.

**Proof.** Exhaustively enumerate all 8190 words through length 12 using exact dyadic rational arithmetic. Evaluate lengths 13,14,15 for `1 0^k` exactly; their output signs are negative. At length 16, exact recurrence enters `K={h0>=4,h1>=10h0,h2=h3=0}`. For zero input, show `h0'>=4`, `h1'>=10h0'`, `h2'=h3'=0` by coefficient inequalities in `verify_witness.py`; output logit `v0*h0+v1*h1+c<0` throughout K. Induct on further zero inputs. Every member of the family has odd parity. QED.

The induction is a **failure invariant**, not an algorithmicity certificate. Its exact sufficient inequalities are tailored to one trained checkpoint. It does not establish novelty over existing neural verification methods.

Primary prior art requiring comparison: Weiss, Goldberg & Yahav (ICML 2018) and Jacoby, Barrett & Katz (ATVA 2020). Formal priority audit pending.
