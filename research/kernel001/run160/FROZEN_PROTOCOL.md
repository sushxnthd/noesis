# Run 160 protocol (retrospective)

Source unchanged Run157 archived decimal JSON checkpoints seed222 (k=2) and seed239 (k=4), exact rational parse. Task: symbol 0 increments, 1 decrements with floor zero, 2 neutral. h'=ReLU(Ah+E[t]), h0=0, output w·h.

Hold A and E[0] fixed. Set E[1,k]=-E[0,k], E[2,k]=0, w[k]=1/E[0,k]. Set each positive off-ray entry E[1,j], E[2,j] to zero. No other changes. Prove h=u*c*e_k for all words via exact inequalities. Test all 729 length-six words by Fraction. Independently check all 3,280 words through length seven using 110-digit Decimal. Verify each edited scalar necessary under this fixed-A/E[0] one-ray requirement.

No claim of prospective prediction, autonomous SGD acquisition, or all-length IEEE-754 inference. Archived checkpoint hashes are stored in RESULT160.json.
