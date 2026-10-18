# CI state and provenance
Run255 protocol committed before training. Local training used torch 2.10.0+cpu, deterministic CPU; raw checkpoint JSON SHA256 e699e374493d152a3bd755dec45b29986567b094c4dc527bceb805e7cc7f7baf.
Local exact replay of all 16 witness words passed. The original frozen adversarial search reported one unresolved; this was later resolved by exploratory beam, never backfilled into the frozen result.
Public GitHub Actions training and artifact-upload workflow creation was rejected by connector safety checks. A syntax-only workflow is included as infrastructure evidence, not as independent experimental reproduction. Full original evidence is retained in the accompanying archive.
