# NOESIS Kernel 001 / Run 194: prospective beam diagnostic
Status: frozen before evaluation of Run 190 holdout checkpoint pairs.

1. Question: Can a gradient-free paired-state search detect differences in trained-model predictions that random finite-horizon evaluation misses?
2. Frontier: Runs 184–193 expose finite-horizon spoofing and model-specific all-length inductive certificates. Neural parity acquisition is established prior art. This diagnostic is NOT an algorithmicity certificate.
3. Scalar success: At least one heldout seed pair has a beam-discovered sign disagreement by depth 24 in <=4096 paired forward evaluations, while matched-budget random search finds one in <=5/100 trials.
4. Competing explanation: Score merely selects large output drift; random search is equally effective, or detected drift is irrelevant to learning.
5. Falsification: On Run 190 seeds 137,139,149,151, compare epoch 300 vs 600. Width-64 beam, score abs(logit300-logit600), stable descending sort, binary children 0 then 1. At each depth test all children for opposite output signs before pruning; stop on first witness, max depth 24. Random baseline: 100 independent trials, RNG seeds 194000..194099, same number of sampled words at each depth as beam; sample uniformly with replacement. Confirm witnesses by >=45-dps directed interval evaluation with binary64 checkpoint parameters interpreted as exact rationals.
6. Publishable threshold: prospective advantage plus independent all-length algorithmic change evidence and cross-architecture transfer; priority audit required.
7. Learning relevance: checkpoints are Adam-trained tanh RNNs; record true parity correctness for every found witness and whether short-horizon behavior changed.
8. Kill condition: no rare holdout witness, comparable random performance, or three unsuccessful substantive transfers. Retire this beam hypothesis, retain negative evidence.

Development pair: seed 163 epochs 300/600 from Run 192, excluded from success; width-64 beam found a length-17 disagreement in 1534 paired prefix evaluations. Holdout method was frozen after that development result. Run 190 summaries already discuss some seed-137 failures and seed-151 certificates, so this is not fully blind to qualitative checkpoint behavior. No model training, personal spending, or user-device compute.
