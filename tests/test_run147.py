from research.kernel_001.run147.exact_rollout import check as rollout
from research.kernel_001.run147.cone_check import check as cone
from research.kernel_001.run147.spoof_check import check as spoof
def test_eight_unseen_exact_rational_rollouts():
 for seed in range(208,216):rollout(seed)
def test_three_learned_inductive_cones():
 for seed in (210,214,215):assert cone(seed)
def test_finite_mask_spoof():
 assert spoof()
