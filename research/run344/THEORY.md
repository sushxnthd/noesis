# THEORY ledger — Run 344
**Exact trained-network theorem (single checkpoint, no general law).** For original Run342 seed 31089 epoch200, all 32,766 nonempty parity words length <=14 admit a single rational affine readout with exact signed margin >=1. At length 15, two positive and three negative words have identical convex combinations of exact recurrent hidden states. No affine readout can classify those five simultaneously. Hence the maximum exhaustive affine-readout repairability horizon is exactly 14.

Words: 1; 100000000000000; 11001000000100; 100000000000001; 100000000000010.
Proof: Fraction exact enumeration and exact Gauss-Jordan positive dual; independent SymPy checker. The witness is irreducible among these five words, not necessarily globally shortest.

Classical convex separation is prior art. This is a trained-network diagnostic and evaluation failure, not a novel automata theorem. Earlier Run343 infinite error family remains valid.
