# Run287 frozen loss-of-correctness audit — negative
Targets: gradient-trained seeds 20828 and 20872. Both had exact all-length certificates at epoch80 and 100% sampled accuracy at epoch80 and epoch120. At epoch120 neither was certified by the restricted Run286 two-box search.
Frozen hypothesis: >=1 exact incorrect epoch120 word on either target. FAILED.
Float64 exhaustive screening of all 2^(d) binary words at each length d<=18 found no incorrect output for either model. Targeted pure TOGGLE lengths<=512, RESET+TOGGLE^n+RESET for n<=128, and TOGGLE^n+RESET+TOGGLE^m for n,m<=128 found no candidate errors. No all-length correctness conclusion is possible from this finite search; no exact negative witness was produced.
Strongest competing explanation (certificate-search incompleteness) remains viable. A lost sufficient certificate is NOT proof of lost algorithmicity.
THEORY ledger: Two-box certificate feasibility is nonmonotone across gradient checkpoints but may be incomplete; no theorem of behavioral forgetting.
LEARNING ledger: Both models are ordinary gradient-trained and remain sampled-perfect; no verified incorrect-after-correct transition.
Run285 prefix anchoring failed; Run286 prospective classifier underpowered; Run287 forgetting probe failed. Three consecutive substantive attempts did not strengthen the acquisition-law claim. REFORMULATE K001, rather than recycle current predictor or claim breakthrough.
Infrastructure: frozen protocol committed before audit; complete local archive contains scripts, checkpoint JSON, negative outcomes, independent proof. Full raw evidence not yet mirrored. PR creation blocked by safety checks.
