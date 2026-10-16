# NOESIS Run 208 — frozen exact-extrema audit of uncertified trained RNNs
Frozen 2026-10-17, before Run 208 extremal evaluation. Input data: Run 207 frozen cohort, checkpoint epoch 800, 20 uncertified seeds. Prior observation: 2 of 20 had random heldout errors; remaining 18 had none in heldout256. **No re-training and no selection of seeds based on this run's outcome.**

## One active kernel (001), eight-field contract
1. **Precise question.** Can exact reachable *task-conditioned extrema* distinguish actually incorrect trained scalar recurrent models from merely uncertified ones, and discover first failing words hidden from random finite evaluations?
2. **Frontier.** El-Naggar et al., ICGI 2023 (formal counting conditions in ReLU RNNs); existing neural-network reachability/interval verification. This run's extremal dynamic program is an elementary consequence of monotonicity, **not claimed novel**. Existing all-length two-box inductive proof remains stronger than finite reachability.
3. **One exact success criterion.** For all 20 uncertified epoch-800 scalar tanh checkpoints, report either a first incorrect input of length <=4096 or an interval-certified *absence of any error* for lengths 1..4096, using two independent implementations. Count completed = 20/20. Never interpret finite absence as unbounded correctness.
4. **Strongest competing explanation.** Interval overapproximation or floating-point tie can create spurious errors; or the two-box verifier simply fails on correct networks.
5. **Cheapest falsification.** Exhaustively enumerate words for lengths <=8, compare exact min/max to extremal DP; independently verify any discovered witness with rationalized binary64 weights and outward-rounded interval tanh; require all-shorter-length classification margins or explicit abstention.
6. **Publishable threshold.** Transfer an exact, independent, task-state extremal diagnostic to unseen trained task/architecture, and demonstrate a consequential difference from sampled testing, with priority audit and strong spoof controls.
7. **Learning relevance threshold.** At least one *previously uncertified* gradient-trained checkpoint gains a certified failure witness (or an all-length proof), and its evaluation status changes; no claims of acquisition solely from certificate acceptance.
8. **Kill condition.** If this diagnostic gives no new information on actual learned behavior for three substantive attempts, retire/reformulate it. No broader automata detour.

## Locked computation
- Target recurrence: h_0=0.5; h_{t+1}=tanh(w_{x_t} h_t+b_{x_t}), x in {0,1,2}; task q_{t+1}=0 if x_t=2 else q_t xor [x_t=1]; readout class 1 iff v*h+c>0.
- At each exact length n and task class q, keep min/max reachable hidden state. Each input map is monotone (increasing for w>=0, decreasing otherwise), hence extrema update by considering only source extrema. This is exact as a *real-arithmetic recurrence*; numerical evaluation must be outward-enclosed.
- All 20 uncertified seeds in Run 207's frozen list; no feature fitting. Evaluate through length 4096, stop at first **certified** error; continue/abstain if undecidable.
- Primary metric: number of the 20 checkpoints assigned a rigorously certified first-failure length <=4096 or a rigorously certified clean bound through 4096, independently checked. Target 20/20.
- Secondary: count newly discovered errors among the 18 with zero random heldout256 errors, and smallest certified witnesses.
- No algorithmicity claim from finite-horizon clean status; compare against two-box positive certificates separately.
- Preserve all failed hypotheses, numerical warnings, checker disagreement and provenance.

## Backup kernels (inactive)
1. Cross-architecture full-alphabet inductive certificate transfer.
2. Mechanism-derived precursor under prospectively unseen training trajectories.
