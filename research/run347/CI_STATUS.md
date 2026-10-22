# Run 347 CI provenance
Frozen protocol commit: c71ce6f3d38db2998b4e01345ef561ab42620d0f.
Research results commit: 8c1541ea98d48618fa254ea55ca8fe67a88bdde1.
Initial CI 39785860836 FAILED at later-certificate import mismatch (find/check absent from committed Run340 API). Earlier exact witness, independent SymPy, 510-short-word checks and 618-probe negative control all passed. The failed run is retained.
Fix commit fb606fd9e457a7ccadb4bac8f477f5987f116bdd corrected imports only, without changing protocol, selected checkpoints or mathematical conditions.
Follow-up CI 39786137448 PASSED all five exact checks, including both unrestricted later certificates.
Draft PR creation was attempted twice but blocked by connector safety checks. Branch remains unmerged.
Original full 38,592-checkpoint Run339 trajectory is in the evidence archive; selected original checkpoints and exact verifiers are committed.
