# Run 193 CI and write-through status

- Isolated branch: research/kernel-001-run193-shortest-checkpoint-separator.
- Local exhaustive 45-dps interval DFS: PASS, 262142 binary words through length 17, 255.84 seconds.
- Local independent directed 80-digit Decimal checker: PASS, two witnesses.
- Research workflow: .github/workflows/noesis-run193.yml (branch-scoped).
- Remote workflow execution: NOT YET CONFIRMED; do not represent as passed.
- Draft PR: two GitHub create_pull_request attempts blocked by safety checks. No draft PR created.
- Original Run 192 files and failures inherited unchanged; branch remains unmerged.
- Previous exploratory broad BFS at depth 14 was terminated by resource/time pressure; replaced with memory-bounded DFS, preserving the earlier log in local reproducibility archive.
