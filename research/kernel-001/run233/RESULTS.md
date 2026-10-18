# Run 233 local results
Frozen primary criterion: PASS. New reset-latch task, 20 Adam-trained 3D tanh RNNs.

Three epoch0 incorrect -> epoch200 all-length certified transitions: 2506, 2512, 2513. Six persistent incorrect seeds: 2507, 2508, 2601, 2602, 2603, 2604. Five certified checkpoints, 44 strict incorrectness witnesses, 31 abstentions across 80 snapshots. Both independent interval checkers agreed. Five corrupted certificates rejected.

All 16 lr=.03 models achieved 100% finite training accuracy. Yet seed 2507 fails on 0100000 at length 7 after exact verification of all 1092 shorter words; seed 2508 fails on 10000000 at length 8 after exact verification of all 3279 shorter words. Both arithmetic engines agree.

THEORY: all-length inductive certificates transfer to reset-latch; finite horizon does not suffice.
LEARNING: three new trained acquisition transitions and two trained finite-horizon heuristics. No universal predictor established.

Full local evidence archived; GitHub complete evidence and remote CI not yet confirmed.
