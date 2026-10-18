# LEARNING ledger — Run249

48 independently initialized shared-transition ReLU RNNs trained by gradient descent (Adam) on all length-five reset-latch sequences, seed range 11001..11048. 35/48 achieved perfect finite training accuracy. First 24 eligible models: 24/24 have exact incorrectness witnesses from 256 deterministic hold-tail probes; 23/24 also from 256 hold-biased random probes, 8/24 from 256 uniform random probes. The networks are learned systems, not hand-constructed automata. No learning intervention or acquisition prediction was established.
