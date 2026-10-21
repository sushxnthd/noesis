# THEORY ledger — Run313

Epoch-20 trained recurrence is a width-3 ReLU RNN with exact binary64 parameters. The all-zero state is fixed under input 0, and h(100000)=h(000000)=(0,0,0). Exhaustive exact enumeration rules out earlier positive-vs-negative equal-length collisions at lengths 1–5. Since a deterministic recurrence maps identical states under identical future suffixes, h(100000s)=h(000000s) for **every** suffix s. These strings have different latch labels. Thus no deterministic readout of final hidden state and length can implement persistent latch for this early representation.

Epoch-80 invariant C={h1=0, 0<=h0<=7*h2/10, h2>=2}: first 1 enters C; both symbol transitions preserve C; every state in C has positive output. Zero-only strings stay at zero with negative output. The lower bound on positive logit is 4783624843499999/2251799813685248. All inequalities are checked using exact binary64-rational arithmetic. The independent checker uses vertices/rays and separately implemented state dynamics.

This is a proof about one trained network pair, not a universal acquisition law or a new polyhedral verification method. It cannot establish the acquisition epoch between 20 and 80.
