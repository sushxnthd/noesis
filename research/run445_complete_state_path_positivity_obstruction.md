# NOESIS R445 — complete-DFA-state path positivity obstruction

Date: 2026-10-26. Kernel: causal transition dynamics of learned DFA-state retention under per-designated-complete-state-neutral cycles.

**Result: exact classical necessary-condition theorem and negative control, not a neural breakthrough.** Frozen protocol SHA256 `9b5bf0f2b323ec9fc85945184ac53309ac81f2839a60b683304867f7ec63b558`; primary source SHA256 `53a6262af51d04f8cc68ffbdc57201fa77ec24a8ec26c475813ce94c6054ddc3`.

For any binary DFA with distinct outgoing successor states for 0 and 1 at every complete state, a complete state trajectory from known initial state uniquely identifies the entire input word. Hence two different physically realizable neutral words **cannot hold the full intermediate oracle DFA path fixed**. This is a structural positivity obstruction to lexical contrasts conditioned on identical full DFA paths, NOT a prohibition on valid endpoint-neutral total-input effects.

For equal-length words, H=input Hamming distance, D=number of differing complete DFA states at intermediate positions. Task A (ones modulo 3) obeys sharp `D >= ceil(H/2)`. Task B (01-count modulo 3 plus previous bit) obeys sharp `D >= H`, since each differing symbol forces differing previous-bit components. Alternating binary words attain Task-A equality for every H; all-0 vs all-1 attain Task-B equality. Elementary automata theory, no novelty claim.

The nine immutable R418 u/v 20-bit designated-state-neutral pairs have (H,D) Task A: (8,5),(2,4),(8,6); Task B: (6,7),(2,2),(2,3),(6,6),(6,8),(2,2). All 18 words preserve their **own designated** complete state; none of the nine pairs has an identical complete prefix-state path. This does not change R418 certification scope or imply global Task-B neutrality.

Independent Fraction/SymPy/direct-prefix-count checks: 18/18 designated words, 9/9 pair metrics, 2,286/2,286 unique state-path signatures over all nine states and lengths 1..7, 16/16 sharp witnesses, and 24/24 Task-B previous-bit checks. Separately frozen postprimary exhaustive falsification: 24,003 distinct pairs of words of lengths 1..6 over all nine states, including 897 both-endpoint-neutral pairs; **0** theorem violations. All 12 frozen exact-audit gates passed.

Retrospective negative control uses the **unchanged** R441 logits and R425 early baselines, all 108 R418 model-state contexts. For n16/32 and 28 suffixes of lengths2/3/4, 12,096 scored records: 35/108 model-state contexts have any late classification error (Task A1/36, Task B34/72), 2,090 individual erroneous records. In 7/9 task-state groups, the exact same word-pair path mismatch coexists with error and no-error checkpoints across 12 models. Thus the DFA path-mismatch count alone is **not sufficient** to determine neural late-error behavior. Checkpoints, not repeated states/suffixes/cycles, are replication units; no population p-values or neural causal mediation inference.

Prior art: deterministic automata transition tables, Myhill–Nerode, Waga (2023) on automata characterization; mediation positivity; earlier NOESIS R431/R444. No training, hidden-state surgery, prospective model or new readout predictor. Task-A readout floor and R425 early-baseline ceiling remain unresolved.

Reproducibility: complete 26-entry/25-payload SHA256-verified local archive `NOESIS_R445_Reproducibility.zip`, SHA256 `0dac39e2569615a230bae46e0facb5cc3af7c34e4fdbbdc31a6d66a714941022`; independent clean rehydration 25/25 payloads and 5/5 deterministic output replays passed. Nested immutable R444->R418 checkpoints included. R444 complete dependency SHA256 is `d1b49b535b9d50e3bb17e63c4f480795ebcb5444e94ba9c066f82097278aab3a` (previous task summary inadvertently omitted its final character). No personal spending or user-laptop access.

Next R446: retire the impossible fully path-matched lexical contrast, keep physical total-input effects and the strongest early controls; seek a genuinely distinct non-ceiling neural prediction, or separately freeze another exact necessary-condition experiment. No retuning of prior failed tests.
