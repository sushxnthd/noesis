# Run148 independent verification and mechanism
Initial executable commit 8003486ac2f0b4af1dbcbf4c880f2f7a2d40058b passed GitHub Actions run 38534056008 on 2026-10-14:
https://github.com/sushxnthd/noesis/actions/runs/38534056008

Two independent checks now accompany the primary exhaustive outward-interval certificate:
(1) scalar Python Fraction verification of the two n=13 witnesses;
(2) a separate exhaustive ordinary-float64 enumerator through n=12 with a conservative, exact-rational global forward-roundoff budget. At n=12 the latter found 0.09471137709839761 maximum observed error and budget <3.124e-11, safely below 0.1.

The repeated-plus invariant uses active coordinates (0,1). On witness 0022222222222, neutral tokens activate coordinate 3 at step 6. The 13 masks are:
1100 1100 1100 1100 1100 1101 1101 0101 0101 0101 1101 1101 1101.
Target remains 2 while error reaches 0.111991 at step 13.

Draft stacked PR creation was attempted twice and blocked by execution safety checks; no Run148 PR is claimed. The isolated research branch and CI logs remain as provenance.
