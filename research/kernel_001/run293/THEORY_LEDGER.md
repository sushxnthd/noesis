# THEORY ledger — Run293
KNOWN (proved): If h_j=alpha*h_i initially, alpha>0, and for every symbol x, incoming row A[x,j,:]=alpha*A[x,i,:] and bias b[x,j]=alpha*b[x,i], then ReLU preserves the relation for every finite word. Eliminating j by adding alpha times outgoing column j into column i and alpha*v_j into v_i yields an exactly equivalent lower-dimensional recurrence on reachable states. This is an elementary known-style quotient, not a new law.
KNOWN (checked): Two augmentation families satisfy A'_x E=E A_x, b'_x=E b_x, v'E=v for all 241 trained models, independently in Fraction arithmetic.
LIMIT: exact-real semantics only; finite-precision trajectories, near-duplicates and arbitrary nonlinear conjugacies not certified.
