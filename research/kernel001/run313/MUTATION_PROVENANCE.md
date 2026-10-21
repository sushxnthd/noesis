# Run313 exact mutated-model controls

All eight controls were rejected by the primary rational verifier, locally:
epoch20 p[20]=1 (zero state no longer fixed);
epoch20 p[8]=2 (delayed collision invalidated);
epoch20 p[23]=100 (delayed collision invalidated);
epoch80 p[22]=1 (cone entry invalidated);
epoch80 p[27]=1 (zero-only output invalidated);
epoch80 p[8]=-10 (closure invalidated);
epoch80 p[11]=100 (cone ratio closure invalidated);
epoch80 p[26]=-5 (output margin invalidated).

Mutation choices and expected failures were retrospective and do not constitute prospectively frozen adversarial validation.
