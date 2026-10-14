# Run 158 protocol

Frozen inputs: Run 157 seed 222 and seed 239 checkpoints, no training or parameter changes.

Frozen input family: 0^n 2^m, n>=1,m>=0. Alphabet semantics: 0 increments, 1 decrements with floor at zero, 2 is neutral.

Success: prove a closed form for all n,m, find the smallest m on the n=1 slice with absolute output error strictly greater than 0.1, and reproduce independently.

Strongest spoof: PR #1 capped counter; relative error on unary strings tends to 1 for a fixed cap, whereas linear gain error remains constant. Neither is an all-alphabet certificate.

Prior art: https://proceedings.mlr.press/v217/el-naggar23a.html and https://www.sri.inf.ethz.ch/publications/ryou2021scalable.
