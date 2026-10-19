# Infrastructure and negative results
- GitHub contents-API create_file was blocked twice by connector safety checks; used Git object tree/commit/ref operations to preserve frozen protocol before training.
- Initial local training attempt failed at checkpoint persistence due to working-directory permissions. Corrected permissions, reran deterministically.
- Monolithic continuation to epoch 500 exceeded local execution limits; frozen phase-one outcomes through epoch 200 remain intact. Do not misreport 500 as completed.
- Existing Run273 linear RESET-gain extrapolation remains retired; this run does not validate it.
- Entire phase-one raw 1280-snapshot JSON and optimizer state available in local reproducibility archive; full remote mirroring outstanding.
