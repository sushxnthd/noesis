# LEARNING — Run 148
Unmodified Run147 seed 214: 4-state ReLU RNN trained by Adam (1200 steps, lr 0.025, float32) with output-only MSE on all 3^6 length-six ternary words; train MSE 5.434735772524846e-9. No retraining, hidden supervision, parameter tying, or post-hoc calibration in Run148.

Run147 certified the two-dimensional all-plus activation cone and first all-plus >0.1 error at length 125. Run148 exact all-alphabet verification instead finds first failure at length **13**. The all-plus diagnostic overestimates worst-case generalization length by 125/13=9.615x.

This was a retrospective adversarial probe after observing the checkpoint; do not call it prospective. A mechanism-derived prospective all-alphabet prediction on unseen architectures remains required.
