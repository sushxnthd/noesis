# NOESIS Run 245 — FROZEN prospective tied-transition architecture transfer

Status: FROZEN BEFORE TRAINING / no outcomes inspected. Branch: research/kernel-001-run245-tied-elman-transfer.

## Exactly one active kernel: K001 sound neural algorithm certification
1. **Precise question:** Does the fixed Run243/244 task-conditioned interval abstraction soundly certify gradient-trained *tied-transition Elman hardtanh RNNs* (shared recurrent matrix A and token-specific input embeddings), including systems where exact-state closure abstains, and expose genuine incorrect-to-correct training transitions?
2. **Primary literature frontier:** inductive abstract interpretation of recurrent systems and neural finite-state representation formation predate NOESIS. Van Rossem & Saxe, ICML 2025 (https://proceedings.mlr.press/v267/van-rossem25a.html); Oliva & Lago-Fernández 2020 (https://arxiv.org/abs/2006.10828). Architecture transfer is an empirical test, not a new general theorem.
3. **Single scalar/exact success criterion:** number of epoch-200 abstract certificates among checkpoints on which the fixed exact finite-state checker ABSTAINS is at least 2; independently verified certificates and zero certified known-incorrect networks are mandatory soundness gates.
4. **Strongest competitor:** Run244's certificates exploit untied symbol-conditioned matrices; a shared recurrent matrix loses the necessary stable task-state partitions, or boxes are too coarse.
5. **Cheapest decisive falsification:** freeze and train 16 seeds 9001..9016, two arms (BCE baseline; BCE+0.1*(1-mean|h|)), 4D shared A plus input embeddings E[t], reset latch task, 243 length-five ternary strings, 201 deterministic Adam steps at lr=0.03, snapshots epochs 0,50,100,200. Convert to the exact Run244 checker format W[t]=A and b[t]=E[t]+b without changing grid S=1024, suffix length=2, or 256-pass budget. Run exact-state checker with 2500 states / depth 15, then box checker, independent integer checker, adversarial sign controls. No tuning.
6. **Publishable threshold:** >=2 genuinely new certificates on previously untested tied architecture, independent exact checker and adversarial controls, at least one provable infinite reachable orbit, and primary-literature priority audit; otherwise publish as negative transfer result only.
7. **Learning relevance threshold:** >=1 epoch-50 provably INCORRECT checkpoint that becomes epoch-200 all-length CERTIFIED under either sound checker; report both arms and unresolved denominators without converting ABSTAIN into correctness.
8. **Kill condition:** any false certification of a known incorrect model; or three prospective architecture/task transfer failures after Run244. Failure count 0/3 entering this run.

**Protocol locking:** No evaluation of seed 9001..9016 checkpoints before freezing this file. Do not retune hyperparameters or redefine criteria. Full negative outcomes and infrastructure errors are research data. Zero user spend; use hosted CPU only.

THEORY ledger: sound certificates are inductive mathematical claims, not a universal acquisition law.
LEARNING ledger: separately track actual incorrect-to-certified transitions, certificate-only gains, and uncertainty.

Backup kernels (inactive, at most two): (i) signed relational invariant transport, (ii) invariant-margin training intervention.
