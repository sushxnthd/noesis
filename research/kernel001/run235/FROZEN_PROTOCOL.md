# NOESIS Kernel 001 — Run 235 PROSPECTIVELY FROZEN PROTOCOL

Frozen before any Run235 training or evaluation. Branch: `research/kernel-001-run235-frozen-exact-graph`.
Run234's exact finite-reachability method was post-hoc; this is its first prospective transfer.

## Eight-field kernel contract
1. **Precise question:** On unseen, gradient-trained 3D hardtanh reset-latch RNNs, does exact finite-state reachability produce sound all-length certificates and independently witnessed incorrect-to-correct acquisition transitions, while abstaining on unclosed graphs?
2. **Primary-literature frontier:** RNN formal verification and finite-state representation formation/infinite generalization are established; neither a finite graph certificate nor a transition alone establishes a novel model-agnostic law. Run234 post-hoc evidence: 4/16 certified at epoch200; suffix-box verifier 0/16.
3. **One exact success criterion:** At least TWO independent seeds with a strict incorrectness witness at epoch0 and a sound exact finite-graph all-length certificate at epoch200; at least FOUR epoch200 incorrect seeds; ZERO corrupted-control false acceptances; complete independent checker agreement. Count unresolved as ABSTAIN.
4. **Strongest competing explanation:** Hardtanh clipping produces accidental finite reachable graphs for selected seeds; this may not transfer to smooth recurrent networks, unseen tasks, or arbitrary precision semantics.
5. **Cheapest decisive falsification:** Fresh fixed seeds + exact enumeration under precommitted resource limits; an independent checker mismatch, incorrect accepted graph, or corrupt control acceptance falsifies soundness. Fewer than two positive transitions fails prospective utility criterion.
6. **Publishable threshold:** New prospective replication PLUS a mechanism-derived unseen-condition prediction and a substantive diagnostic beyond known exact reachability; this run alone does NOT meet publication novelty.
7. **Learning relevance threshold:** At least two independent, actually gradient-trained incorrect-to-certified-correct transitions with raw checkpoint files, full training configs, exact witnesses and independent graph checker.
8. **Kill condition:** Three substantive prospective failures to establish useful new diagnostic or prediction => retire/reformulate; no retrospective tuning of primary criterion.

## Locked training
- Task: ternary reset-latch. Input 0=hold, 1=set, 2=reset; output label after each token.
- Network: 3D fully coupled recurrent hardtanh, h'=clip(W[token] h+b[token], -1,1); linear logit v·h+c. Initial hidden state (0.5,-0.5,0.25).
- Seeds: 2901..2912 Adam lr=0.03; 3001..3004 Adam lr=0.001. All are unseen and distinct from Run234.
- Float64 PyTorch; deterministic algorithms; CPU 1 thread; 729 ternary strings of length six, prefix-wise BCE loss; 200 optimizer updates; checkpoints at epochs 0,50,100,200.
- Never tune seed set, architecture, training loss, epoch, or learning rates after outcomes.

## Locked verification
- Interpret each saved float64 parameter as its exact binary64 dyadic rational. Network recurrence uses exact real arithmetic with rational clipping; **not** IEEE rounding at each recurrent operation.
- Breadth-first exact reachable graph from initial state, tracking target reset-latch state. All outgoing 3 transitions of every reached state must have strict correct output signs. If graph closes, output CERTIFIED; if a reachable wrong-sign state appears, output INCORRECT with shortest BFS witness; otherwise ABSTAIN.
- Hard limits: 2500 visited states, maximum BFS depth 15 (no expansions from depth 15). No changes after results.
- Independent checker: integer dyadic arithmetic without Fraction or torch, independently enumerating each checkpoint and comparing status, witnesses, and graph cardinality.
- Adversarial controls: for the first up to four certified epoch200 checkpoints, flip the final readout sign (v,c)->(-v,-c), require all to be rejected (INCORRECT or ABSTAIN, never CERTIFIED).
- Exactness controls: on any certified checkpoint independently verify every stored state/edge/output; enumerate all words through length six with the independent checker (not a proof, merely a regression test).
- Report all 64 checkpoints and all abstentions; report frozen primary result regardless of success.

## Secondary prediction, frozen before data
High learning-rate cohort (12 seeds, lr=.03) has higher epoch200 all-length certification frequency than low learning-rate cohort (4 seeds, lr=.001). Descriptive only; no significance claim at small n.

## Ledgers and integrity
THEORY: proof status and precise arithmetic semantics. LEARNING: training/acquisition status, including failures. Preserve source, raw checkpoints, hashes, outputs, controls, tests, CI logs, failure provenance, and the smallest claim. No main-branch experiment or merge. Public CPU/GitHub runners only, zero user expense.