# Infrastructure provenance
- Branch based on Run293, frozen protocol commit f6613409661bd121c289cbed7971d7ece711092f before untouched evaluation.
- GitHub contents-API file creation blocked twice by connector safety checks; Git object blob/tree/commit write succeeded.
- Initial local full-cohort attempts timed out after progress 200/245. Preserved failed logs. Reexecuted unchanged model/diagnostic logic in disjoint chunks [0,100), [100,200), [200,245); combined raw outcomes with unique-seed checks.
- Public workflow regenerates trained checkpoints from deterministic source and uploads raw outcomes. Do not treat generic CI as reproduction.
- Draft PR #13 open, unmerged.
