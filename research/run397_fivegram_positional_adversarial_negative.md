# NOESIS R397 — Five-gram and position-balanced neutral-word adversary (negative)

24 October 2026. **Second prospective adversarial-neutral-word robustness primary FAILED.** This is not a novel theorem or publication-ready result. Complete raw evidence, all 48 checkpoints, pilot, independent source/checkers, full trajectories and SHA256 manifest remain in the separate reproducibility archive; do not put raw data on GitHub.

## Frozen independence
- Symbolic design frozen before archived-model pilot: SHA256 `c26386a5dd6ae9f98fba36015997efeefb2c442a1316cbdf07c07ad168b99a36`.
- Independent pilot: only R396 seeds 97000–97001, two pilot prefixes per complete DFA state, 12 novel triples of 20-bit neutral words per state. Selection frozen SHA256 `929fc90a1447f4b03e903fc90ed14fa6973a4f5706c13aa214f2769b09307773`.
- Confirmatory protocol frozen before fresh training: SHA256 `d496b4a105ec7dc244a4084877b944bc534e0f068c1dd04c2188acbaa9d9e9be`.
- Each 40-bit composition `uv` vs `uw` matches exact **overlapping 1–5-gram histograms**, identical four-bit endpoints and complete DFA action. Adversarial/control assignments reversed across two independent holdout prefixes of the **same complete state**, yielding exact **aggregate 40-position bit marginals** in each two-prefix panel. This does not match individual-string positions, 6-grams or joint positional distributions.
- Frozen conjunctive task-B n2 error primary: adversarial minus control >=+5pp, exact one-sided 8-shared-seed signflip p<.05, nonnegative every architecture, >=100 eligible cases/architecture, and pilot net task-B error difference >=10. The independent pilot yielded **5**, already failing the last gate. No posthoc change.

## Fresh-seed experiment
48 **new** networks: LSTM width5/258 params, GRU width6/273, MGU-style width7/248, two DFA tasks, eight shared seeds 98000–98007, matched 196 length8 strings, 160 Adam updates, 47/48 short-perfect, **all retained ITT**. Evaluated 864 paired cases, 1,728 complete n0..512 trajectories and 886,464 per-cycle suffix1 classifications. Task-B eligible 570/576 n0-correct pairs.

| Task-B architecture | Eligible | Adversarial n2 errors | Control n2 errors | Difference |
|---|---:|---:|---:|---:|
| LSTM | 186 | 65 | 68 | -1.613 pp |
| GRU | 192 | 61 | 60 | +0.521 pp |
| MGU-style | 192 | 32 | 32 | 0.000 pp |
| **Total** | **570** | **158** | **160** | **-0.3509 pp** |

Exact one-sided 8-seed signflip **240/256 = p 0.9375**. Seed bootstrap 95% **[-7.103,+2.778]pp**. **CONJUNCTIVE PRIMARY FAILED**, including effect direction, magnitude, p-value, architecture and pilot adequacy. Unlike R393, the holdout was non-ceiling (about 28% n2 error). No delayed-error prediction superiority established.

## Independent checks and limited high-precision witnesses
- Pure stdlib checker: 36 paired compositions, 180 overlapping gram checks, 72 independent DFA-neutrality checks, 18 exact positional panel checks, all passed; independent exact signflip reproduced 240/256.
- Pure NumPy independently recomputed 21 selected paired cases from zero recurrent state through n512, **294/294** selected classifications matching Numba.
- One outcome-selected n2 class-discordant pair per architecture, six arm trajectories total: **120/160/220-digit convergence 6/6**, agreeing with float64, plus **6/6 conditional 100-digit directed interval finite-n2 readout certificates** from exactly serialized binary64 prefix-end states. Not full-panel certification.
- Three **posthoc** selected late-alternating readout witnesses, one per architecture (LSTM taskB seed98000, GRU taskA seed98004, MGU-style taskA seed98001), converged at 120/160/220 digits at n32/33/34/255/256/257/511/512 with large margins. **Not prospective replication**, and neither period-two orbit existence nor attraction was formally certified. Even n256=n512 agreement cannot prove invariant classification.

## Decision
**Retire the pilot-selected adversarial word-composition/readout-margin flagship after R396+R397 two failed frozen primaries.** Keep the same DFA-state retention kernel, but change mechanism to **validated periodic-orbit and transition-map reachability theory**: on separate pilot networks locate candidate full-state-neutral two-cycles, freeze a prospective interval-Newton/Krawczyk or invariant-neighborhood certification test before fresh seeds, include both tasks/three architectures and negative controls, and require true interval existence/attraction/readout separation proofs. Pointwise Jacobian spectra or finite 220-digit trajectories alone are insufficient. Prior-art novelty audit remains incomplete; no publication claim.

**Reproducibility archive:** `NOESIS_R397_Reproducibility.zip` (66 files, verified) SHA256 `a2b06775f6dace2c14f0865f6473b3aedf0b8e353bb6c39c3bb064e807868066`. All raw/checkpoints/source remain local, not GitHub. No paid compute, user's laptop, new branch/PR, force push or merge.
