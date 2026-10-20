# Run288 public reproduction — PASS
Public workflow https://github.com/sushxnthd/noesis/actions/runs/39382193835 completed successfully on 2026-10-20. All stages passed: 256-model CPU training, early-score digest, held-out exact certification evaluation, independent SymPy verification, and artifact upload.

**Byte-identical cross-environment results:** checkpoint SHA256 d525a26b8858a0e3ce1edbc1a0b1174c1a57a9335624c0d691bbcf55b5a8e858; early-score SHA256 d1fa94298a74ae79f59da22fc239d3e451cc2432a970e0d533bc4bb3245fed8a; outcomes SHA256 ed1d9bce0105c34762403322e0a0cf5d2aac904af87b785811e4b122de7a9a02. All three public artifact files were independently downloaded and byte-compared against local evidence. Independent checker passed 141 certificates and 378 wrong-word witnesses.

Public artifact: https://github.com/sushxnthd/noesis/actions/runs/39382193835/artifacts/12245637089 (checkpoints, optimizer state, early scores, outcomes). Earlier run https://github.com/sushxnthd/noesis/actions/runs/39381957147 failed solely on Python-version differences in secondary norm control; preserved in INFRA.md and repaired in follow-up commit 7cd7dee.

**Claim boundary:** frozen certification-prediction criterion PASSED (AUC 0.81594 vs BCE 0.43256); learning relevance threshold FAILED (4 natural transitions, required 5). Noncertified networks remain unknown unless an exact wrong-word witness exists. No cross-architecture or model-agnostic breakthrough established. Draft PR creation blocked by connector safety checks twice; branch remains unmerged.
