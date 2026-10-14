# THEORY — Run 147
FALSIFIED: constant activation mask on finite horizon is a sufficient unbounded algorithm certificate. Exact two-ReLU cap has same mask through step 64 and fails at 65.
PROVED for trained seeds 210,214,215: active 2D cone K={x>=0,Lx<=y<=Ux} contains input b, B maps both extreme rays into K, and all ReLU sign inequalities hold on rays and bias. By induction, h_n on all-plus inputs equals sum_{k=0}^{n-1} B^k b for all n. All inequalities were checked as exact rationals.
NOT PROVED: arbitrary ternary sequences, task-level exact counting, precision robustness, new general mathematical law. The invariant-cone principle is classical.
