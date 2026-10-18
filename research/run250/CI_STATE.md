# Run250 CI and provenance
- Research branch created before local experiment.
- Original local protocol, trainer, and independent GitHub replay source have matching Git blob hashes.
- Failed CI: https://github.com/sushxnthd/noesis/actions/runs/39152826897 — checkpoint SHA mismatch, while exact witness counts matched. Raw failure artifact retained.
- Passing CI: https://github.com/sushxnthd/noesis/actions/runs/39152989877 — 24 models, 66 exact witnesses, frozen counts 23/15/4/24, independent checker agreement.
- Failed-run checkpoints differed from local at ~1e-16 in parameter values; outcome counts remained identical. Passing-run checkpoint SHA matched local exactly.
- Local complete archive SHA256 f0bfddda187a48f1d2336bfd79ea09e91aaf1a70b27f23ed862353140523300f.
- Draft PR creation attempted twice and blocked by connector safety checks; branch commits and CI are public. No merge.
