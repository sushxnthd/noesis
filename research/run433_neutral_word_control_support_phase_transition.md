# NOESIS R433 — Physical neutral-word control support and sharp Lipschitz ambiguity

**2026-10-26. Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Disposition:** independently verified exact *classical* conditional accessibility theorem and quantitative off-support readout-identifiability bound. **No learned-RNN theorem, prospective replication, or neural causal novelty.**

## Frozen scope and overlap veto

Primary pre-outcome protocol SHA256 `b81f59d499094bbdee5a65667491a946de7ff395de2cc95c8267be1ac858cac8`, exact source `2282e94a428be0df67d7f18187907313b8619033a2e1c6290acf33979dd63511`, independent SymPy source `cb1191561c7a1749457cc95909dd4e084d125b0e9ca371c73916f1b55b19b863`. Audited retired R382–383, R390–391, R404, R406–409, R412, R425, R429–432. Unlike R431's impossible independent DFA-path mediation intervention, R433 restricts **actual physical input controls** to valid complete-state-neutral 20-bit words and asks which auxiliary states can be approached. No R408–409 neural transplant or graph retuning.

Immutable R429 state-conditioned lexical class sizes independently verified: Task A `[2,2,2]`, Task B `[8,2,8,9,6,8]`; **47/47 words** return their complete DFA starting state. The m-dependent theorem is **conditional on postulated scalar affine auxiliary dynamics**, not a fit to R418 weights.

## Exact conditional control-support theorem

At a fixed complete DFA state q with m>=2 physically realizable full-neutral word controls w_j, let the assumed scalar block maps on z in [0,1] be
`T_j(z)=lambda*z+(1-lambda)*j/(m-1)`, 0<lambda<1, initial z=0.
Their reachable closure K is the classical affine IFS attractor. **K=[0,1] iff lambda>=1/m.** If lambda<1/m, the first-level inaccessible gap is
`g=(1-m*lambda)/(m-1)>0`, and its midpoint x* has `dist(x*,K)=g/2` even after infinitely many valid neutral-word interventions.

For an unknown L-Lipschitz readout observed to equal zero on *every* physically reachable state, the **sharp** identified interval at x* is `[-L*g/2,+L*g/2]`, attained by `f_±(z)=±L*dist(z,K)`; minimax absolute error is `L*g/2`. This signed sharp result was separately frozen **post-primary** (protocol SHA256 `c08a0e849470103821fe471098c47fe21dffe5c144920d9aad1af5d46282aa18`) and did not modify the original frozen two-witness gates. For L=3/2 and lambda=1/(m+1), sharp minimax is `3/[4(m²-1)]`: m=2,3,5,6,8,9 give respectively 1/4, 3/32, 1/32, 3/140, 1/84, 3/320. With oracle gap 2+f, all states remain correctly classified globally (margin >=1/2). **The off-support x* probe is hypothetical and not an implementable hidden-state or DFA-path intervention.**

At lambda>=1/m, legal depth-N word controls approximate any target within lambda^N under the assumed known maps. At lambda=1/m, exact depth-N reachable states are `{k/m^N: 0<=k<m^N}`. The endpoint x=1 remains at distance m^{-N}; with zero observed readout on the reachable grid, its sharp L-Lipschitz interval is `[-L/m^N,+L/m^N]`, minimax `L/m^N`. This is finite-horizon **physical control support**, not R412 unknown-map finite-trace ambiguity.

## Frozen verification and negatives

All **7/7** primary exact gates passed: nine lexical class checks; 47/47 full-state returns; 18/18 m/lambda phase regimes for m=2,3,5,6,8,9 and lambda below/at/above 1/m; 6/6 exact unsupported-gap witnesses; 24/24 critical-depth N=1..4 grids; independent SymPy 18/18 regimes, 24/24 grids, 47/47 DFA words; and **8,682 preserved exact Fraction bit-level synthetic neutral-word histories**. The separately frozen signed witness audit passed 30/30 SymPy identities. At lambda=1/m gaps vanish; above threshold adjacent first-level intervals overlap. All negative controls preserved. An initial archive-verifier error caused by the inherited R432 manifest's mapping schema was logged, corrected, and the complete archive reverified.

**Limitations:** No archived LSTM/GRU/MGU has a certified one-dimensional affine conjugacy, common lambda, or required global Lipschitz bound. **No neural cases were evaluated or trained**; no actual learned-network reachability or causal mediation is identified. Prior art is Hutchinson (1981) classical iterated-function systems and Lipschitz extension/optimal recovery. This is a rigorous conditional obstruction, **not new mathematical or neural publication novelty**.

**Full reproducibility:** `/mnt/data/NOESIS_R433_Reproducibility.zip`, SHA256 `e7d828e9c5e27928afd6c5ed46f78f23c1d988cfaeeba22bc2ccb80663ee63c2`, 27 entries, 26 SHA256-manifested payloads, all frozen/source/raw/negative/independent/logs and immutable nested R432→R431→R418 checkpoint dependency. Next R434 must first freeze and audit a *non-affine high-dimensional* reachable-set/observability condition on actual learned neutral-word maps, with strong early n0..2 baselines and no reuse of R408–409 neural transplants; if infeasible, preserve an exact no-go instead of training. No spend/laptop, new branch/PR, force-push or merge.
