# R410 — Frozen neutral-word training-objective intervention: failed prospective primary

**Scope:** ONE NOESIS kernel, causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. This is a falsification of this *specific training objective under the frozen protocol*, not of all consistency learning. No publication-grade discovery.

## Frozen design and arms

Pilot design SHA256 `4b832253048d585cdd182384138cf875c94ee6b3b9855a03c43cf01a1f8575fb`; protocol `f6591f836be1674a40cc97030af5ea36efd8a9d3c5c793357e3e93812520c105`. Fresh confirm design `a8385664eddb9db85dbd10c02a02cde4329d7042fc71d53204ec3fa5123b3665`; confirm protocol `a88e322d44acc769b5185d9d100f8408b29ba9de4a42198d256c9d23fa1ce289`. Each frozen **before** its fresh training and outcomes. Pilot seeds 99820–99825, confirm seeds 99840–99847, disjoint auxiliary/holdout prefixes and words.

Compared identical-initialization, same-data, same-45-Adam-step ERM, placebo logit-energy regularization, and neutral-word symmetric softmax-KL consistency. All arms evaluated the same auxiliary input strings. Auxiliary gradient norms targeted 30% of CE gradient norm, with coefficient cap 10; directions, actual backward compute and optimizer paths are **not** matched. All seeds ITT. LSTM/GRU/MGU-style, both tasks, all complete states, heldout 20bit full-neutral exact 1..5gram/boundary-matched words and unseen 10/14bit prefixes. Short supervised data were 196 length-eight strings.

Pilot: 108 fresh networks, 2592 contexts; both-task non-ceiling incidence gates passed, no pilot efficacy rescue. Confirm: 144 additional fresh networks, 3456 contexts, 673920 n0..64 classifications and 332424 preselected n0..512 classifications (NOT all contexts through n512).

## Frozen prospective result — FAILED

| Confirm ITT | Task A ones | Task B substring01 |
|---|---:|---:|
| ERM oracle-error fraction n1..64 | .119412 | .473938 |
| Placebo error fraction | .183228 | .471354 |
| **Neutral consistency error fraction** | **.261922** | **.516317** |
| Neutral minus ERM | **+.142510** | **+.042379** |
| Neutral minus placebo | **+.078695** | **+.044963** |
| ERM short accuracy | .989663 | .986368 |
| Neutral short accuracy | **.935002** | .952487 |
| ERM n0..2 negative-margin fraction | .087963 | .395255 |
| Neutral n0..2 negative-margin fraction | **.221354** | **.461516** |

Frozen primary required taskB absolute error reduction >=.10 against BOTH controls; taskA nonnegative reductions; exact eight-seed one-sided p<.05; positive improvements across all six architecture/task cells; short accuracy noninferiority and early n0..2 noninferiority. **17/18 subgates failed**. Frozen improvement p-values vs ERM: taskA .996094, taskB .75; vs placebo: taskA .882813, taskB .808594. No threshold retuning or favorable-seed selection.

Posthoc descriptive reverse-direction taskA neutral-vs-ERM harm exact signflip p=.0078125, seed-bootstrap95 [.0600,.2328]; NOT the frozen directional primary and NOT a universal theorem. TaskB descriptive harm p=.25390625.

## Independent verification and exact boundary

Independent stdlib DFA, exact fivegram, neutral/suffix oracle, all 6048 raw-case counts/first errors, and all 1134 late/early overlaps passed. Identical initial parameter SHA256 across three arms per seed: zero mismatches. Frozen HP selection SHA256 `d96816565b886347452ee1c04eecb6732c0ab2be2f1585897dd62671aa291de7`: 18 selected contexts ×3 arms, all 54 finite label traces agree across Numba, independent NumPy, Torch and 120/160/220-digit mpmath (6 cases n0..8, 12 n0..2). Max HP220/Numba margin discrepancy 2.22e-14. No directed interval or n512 exact-real proof.

**Classical exact identifiability limit:** softmax(z)=softmax(z') iff z'-z=c(1,1,1). Constant zero logits achieve zero auxiliary consistency loss on every neutral word but cannot distinguish differing DFA oracle classes. Thus softmax readout consistency does not entail hidden-state invariance or correct DFA retention. This is an elementary counterexample, not a new theorem; it does not prove observed models collapsed.

Pilot/confirm training interruptions were recovered by preserving complete shards and training only missing shards. Confirmatory analysis-only NumPy-bool JSON serialization failure was fixed without recalculating raw trajectories. Git DNS failed in the container; connector used for this note. All raw, checkpoints, source, frozen manifests, negative results and failure logs are in the archive, **not** GitHub.

## Reproducibility and decision

SHA256-verified **105-entry** archive: `NOESIS_R410_Reproducibility.zip`, SHA256 `242bcb1f4ef69ee9f095885f03f65b5cc6f06f71491318e24b5f9611ac2a9b0c`. Complete report `NOESIS_R410_Research_Note.md` inside. The specific softmax-consistency objective is rejected as a successful repair under this protocol; **one** training-objective primary has failed. R411 should prospectively test informative intermediate *complete DFA-state* supervision or quotient-state contrastive learning with fresh disjoint seeds, controls, frozen early-accuracy noninferiority and n0..512 checks. If second objective primary fails, change mechanism. Prior art includes Dan/Bastani/Roth ICML2022 auxiliary DFA-state supervision and Wang/Niepert ICML2019 state-regularized RNNs. No new branches/PRs/merges/force pushes, zero user spending, no user laptop.
