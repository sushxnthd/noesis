# NOESIS Run 341 — FROZEN PROTOCOL (before new training)
Date: 2026-10-22. Kernel: 001-S, learned-state inductive certificates.
Branch: research/kernel-001-run341-prospective-deficit.

## Precise question
Can a proof-obligation deficit at epoch 30 predict which *new* width-three, gradient-trained parity RNNs become inductively certifiable by epoch 200 better than contemporaneous training loss?

## Development vs test
Method designed using ONLY even seeds from existing Run339 cohort (29000..29191), n=96, two certified at epoch 200. No Run341 endpoint checkpoints have been generated at freezing time.
Prospective evaluation: seeds 30000..30191 inclusive (192 independent seeds). Same width-three ReLU recurrent parity task and optimizer as Run339. 200 Adam epochs, float64, learning rate .025, training sequences length 8; per-seed 192 random plus four fixed sequences, initialized using torch.randn(28)*.5 with seed+51000. No manual exclusions or retraining. Record ALL epochs and exact config, versions and checkpoint hashes. Run341 uses no paid compute.

## Frozen score
Let p denote the 28-vector of model parameters at epoch 30, interpreted as float64 numbers. For each candidate even-support mask S_E subset of {0,1,2}, derive S_O={i:b_1[i]>0}, L_i=b_1[i] for i in S_O. If S_O empty set deficit=1000.
For each mask, sum positive-part violations of the following support-cone proof obligations with eps=1e-5:
(1) c<=-eps; v_i<=0 on S_E; v_i>=0 on S_O; c+sum_{i in S_O}v_i L_i>=eps.
(2) For source parity q=0 or 1 and input bit x=0 or 1, source support S_q and source lower bounds l_i=0 on S_E, l_i=L_i on S_O, target S_{q xor x}; each target-outside coordinate i requires b_x[i]+sum_{j in S_q} A_x[i,j]l_j<=0 and A_x[i,j]<=0 for all j in S_q; each target-inside odd coordinate i requires b_x[i]+sum A_x[i,j]l_j>=L_i and A_x[i,j]>=0 for all j in S_q. Target-inside even coordinates are unrestricted.
Divide the sum of positive parts by max(1,max_i |p_i|). D(p) is the minimum over all 8 masks. Frozen diagnostic score is -D(p). No fitted weights.
Comparator score: -mean binary cross entropy at epoch 30 on training data.
Outcome: exact rational support-cone certificate (same Run340 check, independent SymPy checker) at epoch 200, NOT finite-horizon accuracy.
Primary metric: paired AUROC difference AUROC(-D)-AUROC(-BCE) over all 192 seeds; ties 0.5. Success iff >= +0.05 AND at least three certified positives. No endpoint-based score modifications. If fewer than three positives, primary criterion fails as underpowered.
Secondary learning-system relevance: at least one prospective seed with an earlier epoch <=100 perfect on all 510 nonempty binary words of lengths <=8, an independently exact longer-word failure, and a later all-length certificate; this is necessary for publishability, not sufficient for primary metric.
Negative controls: all Run340 witnessed-incorrect checkpoints must remain uncertified. Exact certificate checker must reject all known wrong controls; any false acceptance is an immediate stop.
Prior art: invariant-based RNN verification and automata extraction predate NOESIS. Novelty, if any, must be in predictive acquisition, not proof templates.

## Strongest competing explanation
D is a template-specific near-certificate distance that predicts satisfaction of the same template, not genuine algorithm acquisition; results may be seed/task-specific and certificate-negative models may still be correct.

## Falsification / kill
Primary AUROC improvement <.05, fewer than three endpoint positives, or unsound proof are negative. Three distinct failed invariant-synthesis approaches or any uncorrected unsoundness kills/reformulates Kernel 001-S.

## Publishable threshold
Independent exact checker, robust spoof rejection, mechanism-derived prediction prospectively frozen before endpoints, multiple task/architecture transfers, proof boundaries and priority audit. This single Run341 cannot establish field-level breakthrough.

## Ledgers and provenance
THEORY and LEARNING separately; preserve all negative runs, failures, raw trajectories, config, software versions, tests, checker agreement, CI logs. Never merge active experiment into main.
