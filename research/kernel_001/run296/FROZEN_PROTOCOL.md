# NOESIS Run296 frozen protocol
Date: 2026-10-20. Parent: research/kernel-001-run295-complete.
Question: Can a rationally certified reachable-silent-gate quotient restore function-preserving diagnostic invariance in gradient-trained RNN checkpoints?
Frontier: Jacoby-Barrett-Katz ATVA 2020 invariant inference; Ryou et al CAV 2021 polyhedral verification; Khmelnitsky et al ATVA 2021 property-directed verification. No novelty claimed for invariant reasoning.
Exact success: 548/548 exact reductions to original parameters across 242 stable, 242 divergent, and 64 input-switched augmentations, plus zero false reductions in four activated-gate mutation controls.
Competing explanation: engineered-pattern recognition, not learned algorithmicity.
Falsification: exact Fraction dominance check, score comparison, independent checker.
Publishability: prospective unseen-task trained-system predictive gain, prior-art audit, adversarial baselines, independent reproduction.
Learning relevance: at least 10 of 64 new augmentations must alter raw LP score >1e-6, all must be repaired; no new learning transitions claimed.
Kill: any false positive, failed exact reduction, or three successive failures.
New adversary on first 64 eligible Run295 seeds at epoch20: append u,v,g. Symbol 0: u'=ReLU(3u/4+2), v'=ReLU(v+5); symbol 1: u'=ReLU(2u+1), v'=ReLU(3v+2); g'=ReLU(2u-3v-1). Readout g=1; u,v=0. No feedback to trained core.
Frozen detector: find autonomous u,v with a_v>=a_u>=0 and b_v>=b_u>=0 for each symbol; g preactivation c_u*u+c_v*v+b with c_u>=0, c_v<=-c_u, b<=0, no other incoming terms. Prove v>=u>=0, g=0 inductively, erase g readout and backward-prune. Rational exact checks. LP used only to measure diagnostic.
Theory ledger: restricted exact quotient, not general equivalence.
Learning ledger: trained core with engineered additions, not natural acquisition.
Backups: prospective cross-task onset; causal intervention.