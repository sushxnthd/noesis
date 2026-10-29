# NOESIS R517: prospective disjoint four-seed Householder additive-path pilot (2026-10-29)

**All prospectively frozen gates passed 4/4 new seed clusters 51701–51704.** This is a limited independent TaskC architecture-transfer replication of Howe's *published* additive-input-path failure and global-ablation recovery, not full original-task replication, unsupervised state discovery, hidden-state mediation or 32-seed confirmation.

Audit: R382–R516 and primary Metric Automata Theory (NeurIPS 2025), Buitrago/Gu (ICML 2025), Brandoit (arXiv 2609.32447), Geiger (JMLR 2025), Sutter, Howe (arXiv 2609.18966), Lee, PD-SSM, Omlin/Giles, Karhumäki/Saarela/Zamboni. Pinned Howe source commit 3f74e9dd8e31cda31323caf6942ed8f697884c63, model blob 4d8dce7d20d1c2fca7bbadf6bedcbc7903f8485f. Dense-prefix supervised, Householder width112 n_h1, 40 epochs, 4000 length32 train words, batch512 Adam .003; no hardcoded transition table. All 19,624 new physical words disjoint from each other and 10,376 R516 words; R510 exact k=1..5 matched N/C/S q0/q1/q2, 48 groups/seed, length512 no-cycle and exact nonrecurrent scan.

Pre-outcome protocol SHA256 5dfc131432dbd3d5f6243beb56eca437c44885b86dcdb6ca7093e2f4bcee2847; primary source 027336c4d82c81c24d5ffc46307c883840b084f3ccf976628f7ff5c31109f6ea; independent checker 8385ea2e9379df59f7f1d99306b2e101b73cfae878248b642e33550b46767a48.

| New seed | +b test32 | +b test512 | -b trained test512 | trained +b global Wb=0 test512 | global-zero N/C/S | global-zero neutral true-p | N/C TV | N/S TV | cycle-local Wb=0 N/C/S |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 51701 | 1.0000 | .3333 | 1.0000 | 1.0000 | 48/48 | .76608 | .64640 | 8.42e-7 | 0/48 |
| 51702 | 1.0000 | .3333 | 1.0000 | 1.0000 | 48/48 | .63490 | .54932 | 5.76e-7 | 0/48 |
| 51703 | .9967 | .3333 | 1.0000 | 1.0000 | 48/48 | .66142 | .60730 | 5.20e-7 | 0/48 |
| 51704 | 1.0000 | .3333 | 1.0000 | 1.0000 | 48/48 | .76365 | .65065 | 8.12e-7 | 0/48 |

No-cycle512 original +b 1/3 and local Wb=0 1/3, but global Wb=0 1.0 in every seed; this supports a global-path causal contrast, NOT cycle-specific hidden mediation. Trained -b was saturated and excluded from non-ceiling claim. All 17 pre-frozen per-seed gates passed.

Independent NumPy checker: 19,624 words exact oracle and binary-tree scan, zero lexical/duplicate errors; 8,136 saved raw predictions; 448 independent neural replays, max logit difference 0.000628931 below frozen tolerances, zero categorical or numerical tolerance failures. Seed51704 both arms replayed model tensors, optimizer and 40 losses exactly. Original multi-arm shell timeout and mixed-length evaluation batching failure preserved; separately frozen pre-evaluation recovery changed only batching key to include length, no science changes.

Full SHA256-verified local archive NOESIS_R517_Reproducibility.zip SHA256 e8e7be93c4d7873b9a9f7f4edcafcfbe2602db10ac1ca2b835a16b69ae89db57, 103 payload hashes, immutable R516 predecessor 105 hashes verified, CRC PASS.

**Not a 32-seed confirmation.** Under hypothetical p0=.5, 4/4 one-sided p=.0625. Pre-registered next 32 *new disjoint* seed clusters 51801–51832, threshold >=26/32, p0=.5 binomial tail .0002675264, power .96415 at ptrue=.9; no threshold/seed changes allowed. Do not claim emergent hidden-state mechanism, neural mediation or full original S4/A5/S5 replication. No spend or laptop access.