# Active kernel: output-coupled simulation

1. Question: Can all-reachable-state simulation distinguish a correct trained readout from a capped decoy?
2. Frontier: El-Naggar (ICGI 2023), Geirhos (2020), Ryou (CAV 2021).
3. Success: sound checker accepts y=u and rejects y=v for every cap M.
4. Alternative: fixed hidden recurrence already implements the counter.
5. Falsification: find a head that passes the checker but fails on a reachable input.
6. Publication: independent proof, strong spoofs, prior art, unseen-family test.
7. Learning relevance: prospective transition in trained recurrent dynamics.
8. Kill: after three substantive failures, reformulate.

Inactive backups: counterexample-guided readout training; learned quotient coordinates.
