# Run 338: protocol frozen locally before training

Original protocol SHA256: cc8774fe43cd74bf89f9c6cdb599fa019b7be07202cc19c415c1dde8e8840c63

Question: Can the exact orthant parity certificate generalize to unseen gradient-training seeds and capture a transition from bounded correctness with an exact longer failure to unrestricted correctness?

Success criterion: at least one of 192 heldout seeds must have (i) a certified epoch-200 checkpoint, (ii) an earlier checkpoint exactly correct on all 510 binary words through length eight, and (iii) a longer exact counterexample at length 9 through 18.

Frozen training: seeds 28000 through 28191; width two; ReLU recurrence with two input-conditioned affine transitions; binary prefix parity; 192 random length-eight sequences plus four fixed motifs per seed; float64 Adam with learning rate 0.025 and 200 updates; initialization from generator seed plus 51000.

Frozen certificate: even singleton zero and odd unbounded orthant with one learned coordinate lower bound. Use exact dyadic arithmetic, output margin 0.00001, independent SymPy checker, and a finite-horizon spoof baseline.

Competing explanation: coordinate alignment and sufficient-but-incomplete proof template.
Primary frontier: Jacoby, Barrett, Katz (ATVA 2020); Michalenko et al. (2019); Fan, Chi, Rudnicky (2023).
Publishable threshold: independent proofs, adversarial controls, unseen architecture, priority audit.
Learning relevance: only original gradient-trained checkpoints.
Kill: any unsound certificate or three failed strengthening approaches.

The complete frozen document was created locally before training. GitHub protocol upload was blocked until after the experiment; therefore this GitHub commit alone does not establish preregistration.
