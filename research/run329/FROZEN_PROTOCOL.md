# NOESIS Run 329 frozen protocol

Input: original Run326 epoch-80 checkpoints, unresolved after Run328 (174 networks). Checkpoint SHA256: 628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e.

Generate candidates using numpy.default_rng(32924000). For lengths 16,32,64,128 and counts of ones 1,2,3,5,8,n//2, sample 64 position subsets uniformly without replacement per cell; deduplicate words in generation order. Generate all candidates before inspecting model outputs. No access to predictor scores during search.

Screen candidates with float64; independently verify any new incorrectness witness with exact IEEE-754 rational arithmetic and SymPy. Only original unmodified gradient-trained checkpoints count. No witness means unresolved. Single success criterion: at least one new exact witness. Record all negative results. Update full-cohort AUROC identification bounds. This is endpoint adjudication, not prospective predictor validation.
