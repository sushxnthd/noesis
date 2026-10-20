# Run295 independently checked invariant
# For every input, z1'=relu(a*z1+1), z2'=relu(b*z2+3), g'=relu(z1-z2-1).
# Divergent (a,b)=(2,4), stable (a,b)=(1/2,1/2).
# Invariant I: 0<=z1<=z2 and g=0.
# Initial (z1,z2,g)=(0,0,0) satisfies I.
# Divergent difference: (4*z2+3)-(2*z1+1)=4*z2-2*z1+2 >= 0.
# Stable difference: (z2-z1)/2+2 >=0.
# Gate successor relu(z1-z2-1)=0. Therefore I is inductive.
# Old 3 coordinates have no incoming connections from added coordinates;
# output coefficient on g=1, on z1/z2=0. Hence exact-real outputs equal
# for every finite input word. The proof applies to all trained base weights.
# Full independent executable checker is retained in Run295 evidence archive.
