# Exact zero-test failure law for the two-ReLU counter spoof

For integer M>=1 and tokens x in {-1,+1}, define T_x(h)=max(0,h+x) and S_x(h)=ReLU(h+x)-ReLU(h+x-M), with initial state zero. The output is the predicate h==0.

**Theorem (exact, elementary).** The shortest input word on which the two zero-test outputs differ has length **2M+1**, attained by `+^(M+1) -^M`. The target ends at state 1, while the capped network ends at state 0.

**Proof.** Until the first cap activation the states coincide. To activate the cap requires first reaching state M and then applying '+', hence at least M+1 input symbols. Immediately after the first cap activation the spoof state is exactly M. It can decrease by at most one per subsequent input, so it takes at least M further tokens before the spoof state can reach zero. Since the capped state never exceeds the true state, the only possible zero-test mismatch is spoof zero with target positive. Hence any mismatch requires at least (M+1)+M=2M+1 symbols. The stated witness achieves this bound. QED.

**Independent verification.** BFS over product states (reference, spoof), without importing the original experiment code, returned exactly 2M+1 for every M=1..12. For M=12, the shortest zero-test witness is 25 tokens.

**Trained-model relevance.** The explicit 25-token witness `+^13 -^12` also caused zero-test failure under the 0.5 threshold for all 12 trained float64 models (8 exploratory, 4 frozen holdout). This is a constructed witness, **not** a proven globally shortest failure for approximate learned weights.

**Boundary.** The exact result applies to this particular capped recurrent architecture and reflected counter semantics, not general neural architectures. This is a diagnostic spoof, not a claimed novel theorem or a positive learned-algorithm certificate.
