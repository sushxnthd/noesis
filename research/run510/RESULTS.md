# NOESIS R510: exact k<=5 neutral/changing/same-action sham control triples

R382–R509 historical guardrails and primary prior art audited before frozen candidate outcomes. The previous R507–R509 TaskC same-action shams matched neutral/changing words only through 3-grams. R510 constructs an improved **three-arm physically realizable control** in which all three distinct words have identical 1–5-gram count spectra, length, first/last four bits, and substantial Hamming separation.

Frozen protocol SHA256 `4253e371abdd772336bf685e9429a30b48fe104fdad9644e44bc54e12a6367fe`; primary source `074948f66933851ceaee94b72e134d881f91fff9ac37835ffa94000b05e6c3da`; independent preoutcome checker `338774748fa7e586a7cb88728843fedeed0461fb028f269aa2ebfd5e38fd773d`.

Eight bounded seeded Eulerian k5-multigraph searches yielded eight independently generated valid triples: four length45 and four length60. One length45 example:
- N `000111100011111110001100011000011110000001100`
- C `000111110001100001100000011111000111110001100`
- S `000110001111100001100011000111100000011111100`

All length45, prefix `0001`, suffix `1100`, exact 1..5gram counts equal. Hamming N/C=18, N/S=28, C/S=18. Complete-state actions N=(0,2,1), C=(1,0,2), S=(0,2,1). Thus N and S are the SAME full DFA action, and C changes designated q0; this removes the previous k4/k5 sham mismatch. Minimum Hamming across all eight independently verified triples was 12. Length15 fixed-boundary k5-equivalence class contained exactly the original N/C pair, no third; no global minimality claimed.

Independent preoutcome checker verified 22,695 physical q0-prefix/common-suffix triples (68,085 full words), zero lexical/oracle errors. Separately frozen postprimary binary-tree nonrecurrent permutation-scan checker verified all eight distinct triples and 12,096 further physical triples, zero errors. Two isolated deterministic replays each reproduced all three scientific SHA256 hashes. The exact nonrecurrent scan remains a perfect classical baseline.

Complete local archive `NOESIS_R510_Reproducibility.zip` SHA256 `0e84a05f4bcabfefe02571ac6ff38f99760d05de167b53479ca13088a7b3de5b`, 21 local SHA256-verified payloads, immutable nested R509 archive SHA `176d3711330e79b2f4fe1e2ded9818cee9c0e05b43e9ad7cc09d6feecba795d7` with 37 verified hashes, ZIP CRC pass.

**Scope:** Classical control-design improvement only, NOT a novel general theorem, learned neural mediation, neural-specific falsification or prospective external replication. No neural training or 32-seed confirmation. Next R511 should use this exact k<=5 matched N/C/S control resource in a separately frozen genuinely neural-specific on-support within-architecture experiment with non-ceiling functional effect/locality, matched no-cycle and q-changing controls, and exact permutation-scan alternative. Retire R509 checkpoints. Zero personal spend, laptop access, branch/PR creation, force push or merge.
