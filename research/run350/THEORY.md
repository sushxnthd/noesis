# THEORY ledger: Run 350

At epoch 82, four original hidden states provide an exact affine-readout obstruction. Odd-parity states have intercepts (a,0) and (0,c); even-parity states have (b,0) and (0,d), with exact 0<a<b and 0<d<c. Their opposite-label line segments intersect. This is a classical convexity result, not a new theorem.

Replacing only recurrent parameter 18 with its epoch-83 value permits exact affine separation on all 2,644 fixed generator words through length 23. It is a sufficient finite-family repair, not an unrestricted certificate.

An exact infinite counterexample remains. After input 1010^23, the intervened model is in (x0,0,0), where 0<x0<b/(1-a), 0<a<1, b>0. The zero transition maps (x,0,0) to (a*x+b,0,0), preserving [x0,b/(1-a)]. Its unchanged affine output is strictly positive throughout, although every 1010^n has even parity. Thus **all n>=23 fail**. Proof uses stored float64 weights interpreted as exact dyadic rationals.
