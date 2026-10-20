# THEORY ledger
Original trained RNN h'=ReLU(A_x h+b_x), output v.h+c, h0=0. Extend to (h,z) with z'=ReLU(2z+1), z0=0, zero readout weight for z, and no z-to-h coupling. For every finite word w, h_ext(w)=h_orig(w), z(w)=2^|w|-1, and output_ext(w)=output_orig(w). This is an exact-real inductive proof, not finite sampling. Stable control uses z'=ReLU(z/2+1).

The bounded-box LP can change under this extension, even after Run293 proportional-neuron quotient. Backward output-ancestor graph pruning (retain nonzero-readout units and all their recurrent predecessors) exactly removes this irrelevant clock: omitted units cannot affect retained transitions or output. This is elementary observability pruning, not a new theorem.

Limits: exact-real semantics of stored binary64 weights; no claim about indefinitely rounded execution, complete minimization, or algorithm acquisition.
