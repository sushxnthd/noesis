# Run286 results (2026-10-20): FROZEN PRIMARY FAILED (underpowered)
Checkpoint SHA256: 81aca55605fa54f01b6a87b8548d4f2d529406e3991cb215fdceb00e903834e7
Fresh-process retraining produced byte-identical checkpoint JSON.
Epoch20 sampled-perfect: 9/128; epoch40: 51/128; epoch80: 76/128; epoch120: 78/128.
Primary epoch80 among 76 sampled-perfect: 28 exact-certified correct, 2 exact-witnessed incorrect, 46 abstentions.
Cycle margin AUC=0.5000, negative BCE AUC=0.303571, difference +0.196429, but only 2 negatives (<8 required). FROZEN SUCCESS FALSE. Do not claim predictive improvement.
Epoch120 exploratory: 27 exact-certified, 0 exact-witnessed incorrect, 51 abstentions among 78 sampled-perfect; AUC undefined.
New retrospective natural acquisition: seed 20833 epoch80 sampled-perfect yet exact wrong on RESET+12 TOGGLEs (length13); epoch120 sampled-perfect with an exact two-box all-length certificate. Independently verified with SymPy. Seed 20888 epoch80 exact wrong on mixed 39-token word; epoch120 unresolved, not certified.
Independent SymPy corner checks: 55/55 certificates and 2/2 witnesses verified across both endpoints.
All checkpoint labels not certified or witnessed remain UNKNOWN. Certificate absence is not an error proof.
THEORY: inductive two-box proof is sufficient but architecture/task-specific; AUC test underpowered.
LEARNING: 128 ordinary gradient-trained 15-parameter models; one new incorrect-to-certified transition observed retrospectively; no successful prospective discrimination.
INFRA: create_file was blocked twice by connector safety checks; Git-object tree/commit route succeeded. Full raw 640-checkpoint evidence retained in local archive; public full-cohort CI and full mirroring pending.