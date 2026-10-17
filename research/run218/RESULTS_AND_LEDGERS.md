# Run 218 — frozen outcome (2026-10-17)

**Status: PASS** for the *negative* diagnostic criterion frozen in `research/run218/FROZEN_PROTOCOL.md` at commit `4398eb7f35efec2f31ca29fb13c5164b8fdaece8`.

- Source: twelve previously gradient-trained 2D tanh RNN epoch-100 checkpoints, four later independently certified acquisition transitions and eight persistent failures, nine fixed probe words totaling 54 prefixes.
- Original signed minimum / maximum absolute logit ratio AUROC: **0.75000**.
- Across 32 SHA256-fixed, label-blind per-model sign-preserving output-power warps: **min 0.46875, max 0.84375, span 0.37500**; threshold >=0.10.
- Both independent local implementations agreed on all **384 warped scores** and **32 AUROCs**. Source snapshot SHA256: `69d5abe0ce328f85d26aeec9d729a3f12457193974d29c31290727e279c9898e`.
- Exact mathematical invariant: for every real z and p>0, `sign(sign(z)*abs(z)**p) = sign(z)`. All binary prefix decisions and all-length correctness labels remain unchanged; only real-valued output calibration changes.
- This **falsifies intrinsic classifier-invariance of the proposed ratio** under permitted sign-preserving output calibration changes. It does **not** show that the ratio is useless under fixed readout calibration.
- **No new trained models or prospective prediction.** Do not claim a universal algorithm-acquisition law or a field-level breakthrough.

## THEORY ledger
The output ratio depends on magnitudes, not solely on the learned decision function. A post-training readout activation can alter AUROC without altering any learned binary prediction. The theorem is elementary and is not presented as novel.

## LEARNING ledger
Previously verified acquisition/failure labels were held fixed. The output score's ranking instability changes evaluation practice: any cross-architecture acquisition diagnostic using logits must declare and control readout calibration or be defined on decisions. A prospective sign-only probe remains unvalidated.

## Infrastructure provenance
Frozen protocol commit succeeded. Attempted upload of exact executable primary proof/experiment via the GitHub connector was blocked by a safety check; the local scripts, snapshot, full 32-trial raw JSON, and independent checker remain in the run package. GitHub-hosted reproduction and a draft PR remain outstanding. Do not treat remote CI as passed.

## Decision
Retire **function-level logit ratio as an intrinsic acquisition diagnostic**. Retain Kernel 001 only as a learning-linked, behavior-based predictive-certificate program; stop incremental calibration-spoof variants and next test a sign-only behavioral diagnostic prospectively on unseen trained trajectories.
