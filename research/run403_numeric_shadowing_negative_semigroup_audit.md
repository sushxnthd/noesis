# NOESIS R403 — disjoint-seed numerical-shadowing pilot negative; exact semigroup audit

Date: 2026-10-24. One kernel: causal DFA-state retention under full-state-neutral cycles. **Pilot only, no confirmatory claim.**

## Frozen before any new training or outcomes

- Fresh word/prefix design SHA256 `4464972821660b4d510d16ddf4d10bffcbed09c4a5fac8af16e6e41426b6ca24`.
- Fresh-seed numerical protocol SHA256 `3166a7ba10135eb0af7b39930552fb62e03336920dbc324a2354ba51ee5aa8be`.
- New seeds 99500–99503; 3 architectures (LSTM/GRU/MGU-style), both DFA tasks, all complete states; 24 trained networks, 19/24 short-perfect, all ITT. Same 196 length-8 strings and 60 Adam updates.
- New 10/14-bit prefixes and 20/40-bit neutral word compositions; exactly matched overlapping 1..5grams and four-bit boundaries, **not** individual-position or six-gram matched.
- Five frozen numerical arms: binary64; binary64 with recurrent state rounded to binary32 after each symbol; binary32-quantized weights with binary64 operations; quantized weights plus rounded recurrent states; per-operation binary32 emulation with float32 nonlinearities. State-rounding and weight-only arms are **not true float32**.
- Frozen feasibility required >=8 class divergences vs binary64 for the per-operation arm, both tasks, >=2 architectures, >=3 seeds, >=2 per task, and >=3 HP arbitrations.

## Results

**0/864** trajectories diverged in suffix-1 readout class through cycle 64 for **any** of the four interventions relative to binary64. All 280,800 labels (864 trajectories × 5 arms × 65 cycles) preserved. All feasibility gates failed, so **no confirmatory cohort was trained** and AUROC is undefined (zero positives). No retuning.

Despite class agreement, all 864 per-operation binary32 trajectories had nonzero cycle-64 hidden-state drift; maximum observed infinity-norm drift across cycles was **0.2851534384**, task-B LSTM seed99503 at n55. This is numerical observation, **not** an exact-real certified bound.

Frozen HP selection SHA256 `3596393b349dff9f268ff00837ff8128544d852a1cd3451df7f9c182a4cae290`: zero positives and six deterministic architecture/task negative controls. All six n0..8 trajectories agree at 120/160/220-digit mpmath pointwise precision; pure NumPy, original Numba and HP agree on 54/54 selected binary64 labels. Independent PyTorch CPU float32 matches the Numba per-operation binary32 labels on **390/390** selected n0..64 labels; selected logit differences up to 8.35e-7. **No directed interval certificates or shadowing theorem.** All 432 five-gram pairs, 864 neutral and 864 oracle checks passed. Initial import failure and pre-evaluation Numba typing correction and MGU candidate-gate implementation audit are preserved, with no changes to frozen design/thresholds.

## Separate exact semigroup/word-order science

A separately frozen exhaustive symbolic audit SHA256 `8a81ab2dd33214bc74c31a4555328b04c0c9f54d7bccad2eb8740856c6f0adf4` enumerated all binary words of lengths 5..17 under identical overlapping five-gram histograms and first/last four bits. No nonidentical equivalent words exist for lengths <=9. At length10, **`0010010100` and `0010100100`** are exactly five-gram/boundary matched and complete-state-neutral for **both** count-ones-mod3 and count-01-mod3 DFAs (with previous bit 0), but their intermediate complete DFA-state paths differ starting at position 5 and reconverge at the end. An independent Counter/DFA checker verified this. At length17, 22,502 task-A and 22,862 task-B neutral equivalent unordered pairs differ in intermediate DFA-state paths. This is an **elementary finite de Bruijn/Euler-trail combinatorial fact**, not a novel theorem or evidence of a learned neural mechanism.

## Decision and integrity

R402 and R403 are two failed numerical-shadowing feasibility pilots: **retire numerical-shadowing flagship**. Next scientific target, within the same kernel, is prospectively testing **intermediate DFA-transition-path order under neutral five-gram-equivalent words** against lexical, early margin, CE, and latent-drift controls. Do not recycle R403 outcomes as confirmation or claim universal float32 robustness.

Full **159-entry** local SHA256-verified reproducibility archive: `NOESIS_R403_Reproducibility.zip`, outer SHA256 `975f198c0b8b549f97e55dc5269f1e6281ac7c759c51e3538ef3abf063e5d546`. Contains all fresh model parameters, seeds, raw trajectories/logits, negatives, frozen protocols, independent HP/Torch/NumPy checks, symbolic enumeration and source dependencies; **raw/checkpoints are not uploaded to GitHub by this note**. Zero user spending; never used user's laptop.