# THEORY — Run 160

**Exact sufficient induction.** For h'=ReLU(Ah+E[t]), h0=0, readout w·h, reflected counter c, let k,u>0 satisfy A[k,k]=1; E[0,k]=u, E[1,k]=-u, E[2,k]=0; w[k]u=1; A[j,k]<=0 for j!=k; and E[t,j]<=0 for all t and j!=k. Then for every ternary word h=u*c*e_k and output c. Base case zero; inductive step follows from active preactivation u(c+1),u(c-1),uc and nonpositive off-ray preactivations.

**Support minimality restricted:** Holding A,E[0],k fixed and requiring this same ray representation, every repaired scalar independently violates a necessary equality or zero-boundary off-ray inequality. Five and six edits respectively; not global minimal network repair.

**Unrepaired checkpoints:** Not exact; earlier long-horizon failures remain valid. No model-agnostic necessary-and-sufficient theorem claimed. All-length theorem applies only to repaired exact-rational models, not IEEE floating point.
