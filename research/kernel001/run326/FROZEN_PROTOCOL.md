# Run 326 frozen protocol

Question: Does an epoch-20 head-independent representation-separation score predict exact epoch-80 algorithm correctness beyond epoch-20 BCE?

New seeds: 24000..24383, Run315 training configuration. Score: class-balanced linear SVM on RMS-normalized hidden states for all binary prefixes lengths 1..6; signed minimum class-conditional 10th-percentile margin on lengths 7..8 divided by training decision-score standard deviation. Endpoint: original epoch-80 exact all-length certificate or exact wrong-sign witness; unresolved excluded. Success: AUROC improvement >=0.05 versus negative early BCE with >=10 certified positives and >=30 witnessed negatives. No outcome-dependent tuning. Gauge and delayed-memory spoof controls required. Three failed substantive attempts kill K001-R. THEORY and LEARNING ledgers separate. Never equate finite separation with unrestricted correctness.
