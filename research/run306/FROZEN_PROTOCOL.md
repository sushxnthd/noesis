# NOESIS K001 Run306 — Frozen nonlinear-readout falsification

**Status:** Protocol committed before running Run306 evaluation. Starting evidence: Run305 exact affine convex-hull obstructions in 9 of 18 epoch-20 gradient-trained latch networks. No endpoint labels are changed.

1. **Precise question:** Does any early recurrent representation with an affine-readout obstruction also fail to support *every quadratic polynomial readout* on a finite set of task-reachable states?
2. **Frontier:** Classical linear separability of lifted polynomial features, convex-hull intersection, and inductive verification are established tools; Run305 proves affine obstruction only. A quadratic obstruction is stronger but is not impossibility for arbitrary nonlinear decoders.
3. **Exact success criterion:** At least 1/9 previously affine-obstructed epoch-20 checkpoints has an independently rational-verified intersection of opposite-label convex hulls in the 10-dimensional quadratic feature map (constant, 3 linear, 6 quadratic monomials).
4. **Strongest competing explanation:** Early recurrent states encode the algorithm but require a nonlinear readout; the late training improvement is readout-calibration compatible.
5. **Cheapest decisive falsification:** Reuse Run304 epoch-20 checkpoints. Generate fixed word families from Run305; solve numeric LP in quadratic feature space; verify any candidate by exact rational arithmetic using stored binary-float parameter values. Exact opposite-label state collisions (which defeat all deterministic readouts) are checked separately.
6. **Publishable threshold:** >=8 independently verified quadratic obstructions on distinct trajectories, with independent training, prospective controls, and primary-priority audit. Otherwise methodological negative result only.
7. **Learning relevance:** Every witness must be from an unmodified gradient-trained epoch-20 network with paired epoch-80 unrestricted-correctness certificate.
8. **Kill condition:** If no quadratic obstruction is verified, count this as one failed mechanism-strengthening attempt. After three failures, kill or reformulate the mechanism kernel.

**Selection:** All nine Run305 affine-obstructed seeds are primary; remaining nine are optional controls. Words: zero-only lengths 1..64; positive words from Run305 (first 1 followed by 0s, delayed 1, and 1-runs). No adaptive checkpoint selection. Discovery may search lengths up to 64; results and nonfindings must be preserved.

**Outcome semantics:** An exact lifted intersection refutes all degree<=2 polynomial readouts on that finite witness set. Failure to find an intersection does NOT certify existence of a universal quadratic readout. A numerical LP result without exact verification is not a result.

**Theory ledger:** polynomial feature intersection gives impossibility of strict quadratic separation. Not a new general theorem.
**Learning ledger:** outcome identifies whether an early trained representation can be rescued by degree<=2 readout alone; late unrestricted correctness remains independently established.
