# LEARNING ledger — Run221
The analyzed parameters are a frozen epoch-200 checkpoint of a gradient-trained fully coupled 3D tanh RNN (seed 1429). The network had perfect finite training accuracy on length-six resettable parity but has two rigorously confirmed failures at length eight.
A wider beam search (384 versus 256) misses the failures, demonstrating that trained-model evaluation cannot treat absence of a beam-found witness as correctness. No additional models were trained.
