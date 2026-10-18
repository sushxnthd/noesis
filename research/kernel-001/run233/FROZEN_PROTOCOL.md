# Run 233 frozen protocol
Task: reset latch. Token 1 sets state=1; token 2 resets state=0; token 0 leaves state unchanged. Prefix-wise classification.
Architecture: 3D tanh RNN, three token matrices, h0=(0.5,-0.5,0.25), double precision. Adam 200 steps on all 729 length-six ternary words, prefix BCE.
Seeds: 2501–2516 (lr .03), 2601–2604 (lr .001 controls). Snapshots: epochs 0, 50, 100, 200.
Candidate generator: fixed Run232 suffix depths 1–3, max 500 iterations, nine paddings 1e-10 through 1e-2. Witness search through length 8.
Proof acceptance: independent mpmath interval (65 digits) and directed Decimal (90 digits) must accept all base, transition, output obligations for exact binary64 checkpoint parameters. Incorrectness needs strict wrong-sign witness accepted by both.
Primary success: >=3 distinct incorrect(epoch0)->all-length-certified(epoch200) transitions; >=4 persistent incorrect at both; zero corrupted certificates accepted. ABSTAIN is unresolved.
Theory: finite accuracy does not prove all-length correctness. Learning: only certified transitions count.
Kill after three failed transfer attempts. Publishability additionally needs unseen architecture, prior-art audit, strong spoofs and novel predictive/theoretical contribution.
