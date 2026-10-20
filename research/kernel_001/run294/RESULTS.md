# Run 294 — frozen outcome
Untouched cohort: 245 Run291 gradient-trained width-three ReLU RNN epoch-20 checkpoints. Excluded pilot seeds 21450..21455 and previously probed 21494, 21501, 21549, 21585, 21674.

Frozen primary threshold >=150 changed LP scores after an exactly output-preserving divergent fourth recurrent coordinate: **192/245, PASS**. Stable-clock control unchanged **245/245**. Exact output-observability pruning restored scores **490/490**. Independent exact all-word projection checker: **490/490**; 48 exact-word cross-checks and negative mutations passed locally.

Smallest claim: gauge-normalized, proportional-quotient bounded-box LP score is not function-invariant under an unobservable divergent coordinate; backward output-cone pruning repairs this specific spoof. No new learned algorithm or model-agnostic acquisition law.
