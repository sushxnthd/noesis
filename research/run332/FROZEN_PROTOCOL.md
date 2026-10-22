# NOESIS Run332 frozen protocol
Score: minimum over k=0..64 of logit(1 followed by k zeros) minus logit(k+1 zeros), from epoch20 trained checkpoints.
Success: odd-seed heldout AUROC advantage >=0.05 versus epoch20 negative BCE, adjudicated endpoints only. Report exact unresolved-label bounds. Failure counts as third predictor failure and kills Kernel 001-R.
Dev-only delta +0.0465346534653466; heldout odd seeds untouched at freeze. Checkpoint SHA256 628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e. Outcome SHA256 108d462f64cbc925b0420db3fa10f121926506623062518976d02d96c355782f.
