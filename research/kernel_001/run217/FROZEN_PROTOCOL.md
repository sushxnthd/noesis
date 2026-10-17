# Run 217 frozen protocol

Question: Can a function-preserving dormant recurrent channel spoof output-norm-normalized minimum margin on previously trained models?

Before evaluation, lock 32 label-blind SHA256 trials. For seed s and trial t, choose exponent e = SHA256 first byte of `NOESIS-R217|trial=t|seed=s` modulo 25 minus 8. Set dormant readout K = original readout norm times 2^e. Add a third recurrent coordinate always zero. Compare AUROC on four verified acquisition transitions versus eight persistent failures from Run 215. Success criterion: AUROC range at least 0.10 across trials, exact all-length output identity, and independent checker agreement. Report all trials. A negative result rejects this particular spoof. This is not a new neural learning result or novelty claim.

Prior art: Chen et al., Net2Net (arXiv:1511.05641). Strongest alternative: artificial dormant channels are excluded by fixed minimal architecture. Learning relevance: evaluation of actual gradient-trained checkpoint parameters. Kill if criterion fails; reformulate after three failed strengthening attempts. No paid compute.
