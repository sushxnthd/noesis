# Run 333 — frozen exact-verification protocol (retrospective selection)

Active K001-S question: Can a task-derived inductive halfspace certify at least three previously unresolved original gradient-trained width-3 ReLU OR-latch networks?

Prior literature: automata extraction from trained recurrent networks (Weiss, Goldberg and Yahav, ICML 2018) and neural verification already use abstraction and inductive invariants. No novelty claim for the proof technique.

Criterion: at least three new all-length certificates from 173 unresolved epoch-80 checkpoints, zero acceptances among 193 witnessed-incorrect controls, independent exact reimplementation.

Strongest competing explanation: only especially simple readout-aligned learned representations satisfy this condition. Cheapest falsification: exact checker across 384 existing trained checkpoints and delayed-clock spoof. Publishable threshold: independent proof verification plus unseen architecture/task and a mechanism-derived prospective learning-transition prediction. Learning relevance: original trained weights; evaluate epoch 0,20,80 without modifying weights. Kill: three distinct failed synthesis approaches or uncorrected unsound acceptance.

The output is 1 iff v.h+c>0, with h_0=0 and h'=ReLU(A_x h+b_x). Set T=-c+1/100000. Require c<0, b_0<=0, v.ReLU(b_1)>=T, and invariant P={h>=0,v.h>=T} under both symbol maps. Exhaustively check eight ReLU activation masks for each symbol, using exact rational vertices and recession rays; independent SymPy exact simplex audit. Binary64 parameters are interpreted as exact dyadic rational numbers.

Selection caveat: an exploratory floating-point LP scan identified seeds 24066,24139,24152,24202,24305 before this protocol was committed. This is retrospective proof discovery, not a frozen heldout prediction. Do not infer an algorithm-acquisition law from these results.
