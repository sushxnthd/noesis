# Run288 CI failure provenance
Run 39381957147: training reproduced the frozen checkpoint SHA256 exactly. The early-score digest assertion failed. Inspecting the uploaded artifact showed all 256 primary LP scores, BCE baselines and accuracies matched; 59 secondary parameter-norm controls differed by approximately one ULP between Python 3.11 and 3.13 due to sum() accumulation.
Fix in follow-up: use math.fsum for the secondary norm. No primary metric, seed, protocol or certificate logic changed. Preserve failed run as provenance. Draft PR creation blocked on two attempts.
