# Run295 infrastructure and failure provenance
- Initial GitHub contents-API protocol write blocked by connector safety checks. Protocol blob/tree/commit created, but update_ref blocked; a new research branch was created directly from the frozen commit before untouched evaluation.
- Pilot only seeds 21440,21441,21442; excluded from primary.
- First monolithic local evaluation timed out after reaching index 160; no primary result was reported from that partial run. Exact unchanged evaluation was rerun in three disjoint chunks 0:80, 80:160, 160:242; all raw partial files preserved.
- Frozen primary criterion failed: stable control changed 49/242 scores. Do not alter the threshold or reclassify as a pass.
- Independent rational proof checker passed 484 exact inductions and rejected 3 mutations.
- Source/checkpoint digest recorded; full local evidence archive retained. Public dedicated CI pending until workflow source is committed and run completes.
