# NOESIS R411 — Information-matched complete-DFA-probe supervision: frozen confirmation failed

**25 October 2026.** Same single scientific kernel: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. Second failed training-objective primary after R410; **retire this mechanism** for cross-task readout retention. No novelty or invariant-set claim.

## Pre-outcome freezes

- Pilot design SHA256 `f38ac74c241b12a27b401c4ff9c236b56ae6e8f31c448faa4c14e62e09f05b02`; pilot protocol `464561bed3ad8ecd83aeab46ba4fc6751a344650b3a7274655bdfcc67`.
- Fresh confirm design SHA256 `3b2c9bcbf1fb4fec7846ed416037ef7fc297a0c91fadfa95e1d42b5d034443d5`; protocol `9f007aa3c8cd46068735376c934aa624102c6f65f28a1973084a1d13982c1bfa`.
- HP selection frozen before HP SHA256 `071f82c378301375d4538cb1b3c39a9c283ef1bc53a68d55b229689a6d2ff5c3`; independent exact audit frozen `c3bede505887261628ee82dbd4c406642e9613b833321e5e633d2fbf2ba9287b`.

## Causal design

108 fresh pilot models (6 seeds 99900–99905) and 144 independently frozen confirmation models (8 seeds 99920–99927), across LSTM/GRU/MGU-style and both DFA tasks. Arms: (i) ERM, (ii) auxiliary oracle-probe CE, (iii) the **same labeled probe inputs and targets** plus symmetric KL consistency. Each auxiliary full-state-neutral prefix/word pair was supervised with suffix probes 0 and 1, which jointly distinguish the complete DFA states. Approximate auxiliary gradient-norm matching at 0.30 of ordinary CE, with cap10; gradient directions and optimizer trajectories not matched. ERM received fewer oracle labels, so information-matched causal contrast is (iii) versus (ii), not versus ERM. All seeds ITT. Fresh heldout 20bit neutral words exact 1–5gram/four-bit-boundary matched, unseen 10/14bit prefixes, all complete states. Float64 50-step Adam on 196 length8 training strings.

Frozen pilot non-ceiling gates **PASSED** (2,592 contexts; both tasks, >=2 architectures/3 seeds, all arm-task mean short accuracy >=.94). Before fresh confirmation, the conjunctive primary fixed task-A information-matched reduction >=0; task-B >=.04; one-sided exact 8-seed p<.05 both tasks; all six architecture-task means positive; structured-arm short accuracy >=.95 and noninferior within .01 to probe CE; n0–2 error noninferiority; and task-B >=.04 improvement over ERM.

## Fresh confirmatory outcome: PRIMARY FAILED

3,456 heldout contexts, 673,920 complete n0–64 classifications, 648 preselected n0–512 arm continuations (332,424 classifications). All 144 models retained.

| Task | ERM error n1–64 | Probe CE | Probe CE + KL | CE minus CE+KL | exact 8-seed p |
|---|---:|---:|---:|---:|---:|
| A (ones) | .063314 | .079861 | **.085069** | **−.005208** (worse) | **.75** |
| B (01) | .423692 | .412821 | **.380500** | **+.032322** (< frozen .04) | **.3203125** |

Task-B architecture contrasts: LSTM −.043030, GRU +.071818, MGU +.068176; no cross-architecture replication. Task-A n0–2 oracle-error rate probe CE .082176 versus structured .086806, failing early noninferiority. Short accuracy taskA ERM .994287, probe .948794, structured .950229; taskB .982488/.988255/.988627. Although task-B structured beat ERM by .043193, this isolated gate does **not** rescue the failed conjunctive primary. No posthoc threshold retuning, seed selection, or confirmatory re-training.

## Exact mathematics and independent checks

Two suffix probes 0,1 identify the complete taskB state (q,prev): outputs (q,q+1 mod3) for prev0 and (q,q) for prev1. For paired 3-class predictions P,Q with common true label y and average CE E=−(log P_y+log Q_y)/2, **TV(P,Q) <= 1−exp(−2E)**; if E<ln2/2, both argmax classes are already correct and agree without a KL term. This is classical finite-pair supervision mathematics, not an unseen-word guarantee or novel RNN theorem. Independent exact rational enumeration passed **138,549** checks.

Separate stdlib DFA/ngram checker validated all **6,048** raw contexts, all 84 shared-seed initial-weight matches, pilot/confirm disjointness, and **1,134** late-early arm continuations. Outcome-frozen HP selection: 18 cases ×3 arms = **54** pointwise continuations agreed across independent NumPy, Numba, PyTorch and 120/160/220-digit calculations (six confirmatory cases n0–8, remaining n0–2). No directed intervals or n512 exact-real proof. Analysis-only NumPy bool JSON serialization failed after raw completion; corrected without changing outcomes, with failed log/pre-fix source retained. Training interruptions resumed only at completed shards.

**Complete 38-entry SHA256-verified archive** (full raw/checkpoints/source/negative results, not on GitHub): `/mnt/data/NOESIS_R411_Reproducibility.zip`, SHA256 `7290a98a686808dcde601a7cf17cdfe686fbf8ca1edbd6f96ac6d9f89e573994`. Immutable dependency: R410 archive SHA256 `242bcb1f4ef69ee9f095885f03f65b5cc6f06f71491318e24b5f9611ac2a9b0c`.

**Decision:** R410 and R411 are two failed prospective training-objective primaries. Change mechanism; do not recycle retired approaches. Next do exact finite-data/transition-semigroup identifiability science before freezing a genuinely distinct prospective causal mechanism. No publication-grade discovery.
