# THEORY ledger — Run 158

Exact rational theorem for two archived trained ReLU RNNs: every input 0^n 2^m, n>=1,m>=0, has hidden state h=max(0,n*u+m*v)e_k. Proof: increment-ray conditions A_kk=1, A_jk<=0, E_0j<=0 for j!=k; neutral-ray conditions E_2j<=0 when v<0, or A_jk*u+E_2j<=0 when v>0. Thus f=w_k max(0,n*u+m*v).

For n=1 the output error is monotone in m. Exact rational floor formulas certify the first error greater than 0.1. Independent Decimal binary search agrees.

The same checkpoints satisfy f(0^n)=n(1+delta) for all n>=1. Consequently normalized unary error is |delta| for all lengths despite finite absolute-error failure horizons.

This is a restricted-language negative certificate, not an all-alphabet positive certificate. The exact conditions and the phenomenon of imperfect learned counters have substantial prior art.
