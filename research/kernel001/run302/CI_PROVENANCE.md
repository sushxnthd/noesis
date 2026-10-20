# Run302 CI provenance
Generic CI failures: runs 39492487849 and 39492498381. The metadata regression test expected a key absent from the compact witness artifact (KeyError: new_exact_incorrect). Failed logs are retained by GitHub. Follow-up commit c93816ee0aacb15fb22ec06d1bab0c460c2a4d73 fixes the test schema.
Generic CI tests metadata only; the independent exact witness verifier requires Run300 checkpoints, which are supplied in the complete local Run302 evidence archive but not yet mirrored to GitHub. Do not call a generic green CI run public exact reproduction.
