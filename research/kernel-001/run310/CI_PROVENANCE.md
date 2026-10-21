# Run310 CI provenance
The generic repository CI passed for the Run310 branch, but it does NOT run the new exact finite checker. An attempt to add a dedicated GitHub Actions workflow was blocked by connector safety checks; no dedicated CI reproduction is claimed.

Public frozen source: GitHub Actions Run304 artifact 12303488724 (run 39508014453), containing checkpoints300_repro.json. Expected SHA256 of this combined file: 750da83715d79f3f6e1aeb9ab7dfbf33087dc7c9f27f8d10a20842df10f4d6f9. The independent public reproduction script can be run as:
python research/kernel-001/run310/reproduce310_ci.py checkpoints300_repro.json

The local archive includes four extracted epoch80 trained parameter vectors, the original Run300 late cohort source SHA256, the complete exact results, independent exact code and periodic discovery outcomes. Public reproduction requires extracting the Run304 artifact. PR creation attempts were blocked; branch changes were committed and remain unmerged.
