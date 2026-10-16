NOESIS ACTIVE KERNEL 001 / RUN 206
1 Question: Does two-box inductive simulation transfer to gradient-trained resettable parity over alphabet {0,1,reset}?
2 Literature frontier: El-Naggar et al. ICGI 2023 (RNN counting); Ryou et al. CAV 2021 (RNN verification); van Rossem and Saxe ICML 2025 (neural algorithm acquisition). Method components have prior art.
3 Frozen scalar criterion: at least 2 of 8 endpoint checkpoints (4 seeds times epochs400/800) certified all-length, plus one certified earlier error preceding a certified endpoint. PASSED.
4 Competing explanation: input-gated scalar tanh architecture makes the task unusually easy; no general mechanism established.
5 Cheapest falsification: check all three-symbol inductive obligations, especially reset from both parity states; test same-architecture finite-horizon spoof.
6 Publishable threshold: independent remote proof, cross-task reproducibility, strongest spoofs, unseen prospective prediction, rigorous novelty audit, limits.
7 Learning relevance threshold: a gradient-trained checkpoint must change from verified wrong to certified all-length correct. Seed337 epoch50 to100 passes.
8 Kill condition: three substantive failures to strengthen full-alphabet transfer trigger reformulation; preserve all abstentions and failures.
Backups inactive: representation sensitivity; pre-certificate margin predictor. One active kernel only.
