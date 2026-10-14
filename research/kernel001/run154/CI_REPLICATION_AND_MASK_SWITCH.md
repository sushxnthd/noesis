# Run 154 — independent CI reproduction and platform variance

GitHub Actions run 38576881242 completed successfully on 2026-10-14. It retrained all 24 seeds and uploaded all 24 checkpoint JSON files as artifact 11901540700 (expires 2027-01-12). The CI replay independently found a length-22 failure for seed 225 and a length-27 failure for seed 216. Thus the local diagnostic's false-negative mechanism persists under a different training environment.

IMPORTANT: CI checkpoints are NOT byte-identical to the local frozen checkpoints. For seed 216, local training MSE was 4.47e-9 and CI MSE was 1.55e-8. Seed 230 had a local length-14 witness but no CI beam witness through 128. Therefore the CI results are a *new training replication*, not an exact checkpoint re-execution. The original frozen local holdout remains failed; do not substitute CI labels to change its success gate.

For the original local seed-225 checkpoint, exact rational arithmetic shows that repeated increments retain activation mask (0,1,0,0,0) through length 15, switch to (0,1,0,0,1) at length 16, and first exceed 0.1 output error at length 22. Errors: length 15 5.87843e-7; length 17 0.00906869; length 21 0.09284958; length 22 0.12024758. This is an exact result for the increment-only word family, not a global shortest-witness theorem.

CI artifacts are time-limited. The complete original local checkpoint and raw-outcome package has a separate SHA256 recorded in the repository manifest. The diagnostic is retired as a certificate and current predictor; Kernel 001 is reformulated around verified reachable activation regions and task-coupled all-alphabet simulation.
