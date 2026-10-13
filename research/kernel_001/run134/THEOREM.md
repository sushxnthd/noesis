# Restricted two-word certificate — Run 134
For h'=ReLU(Ah+b_s), h0=0, output y=w^T h, assume v=b_+>0, b_-=-v, b_H=0, w>0, w^T v=1, and Av+v>=0 coordinatewise. Then exact outputs y(++)=2 and y(+-)=0 imply Av=v, hence h(word)=v times the reflected counter for every finite word.

Proof: y(++)=w^T(Av+v)=2 gives w^T(Av-v)=0. y(+-)=w^T ReLU(Av-v)=0 with w>0 gives Av-v<=0 coordinatewise. A nonpositive vector with strictly positive weighted sum zero must vanish. Thus Av=v. Induct using b_+=v, b_-=-v, b_H=0. QED.

Gradient intervention: (i) singleton squared-output loss, LR 1/||w||², normalizes learned v; (ii) cancellation and hold squared hidden-state losses, LR 1; (iii) state-composition loss ||Av-v||²/2, LR 1/||v||². The final matrix is nonidentity with an exact eigenvalue-1 ray. All 16 initial matrices have det(A-I)!=0. The scalar ++-only control uses LR 1/(||w||²||v||²) and fits ++ exactly but fails +-.

Independent checks: 625 small rational 2x2 matrices (9 satisfying the two-word antecedent), 16 exact trained checkpoints, 192 history-gated counterexamples rejected by b_H=0 *scope precondition*. A signed-readout wildcard w=(2,-1), A=diag(2,3), v=(1,1) spoofs ++ and +- but fails +++: positivity is necessary.

This is a sufficient, incomplete, architecture-specific invariant certificate. The training objective is engineered and uses hidden-state composition; it does not establish spontaneous task-only or model-agnostic algorithm acquisition. The theorem is elementary and novelty is not claimed.
