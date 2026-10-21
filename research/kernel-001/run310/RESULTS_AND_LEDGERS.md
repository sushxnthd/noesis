# Run310 negative outcome

Four unresolved trained recurrent models (seeds 22242, 22287, 22361, 22573) were evaluated on every binary input of length 1 through 16. Each passed 131070 exact rational checks, 524280 total. The exact checker was independently implemented and agreed with a separate NumPy float64 prefix-tree enumerator. No all-length correctness claim follows. The frozen periodic scan found no finite misclassifications; 22 periodic scans reached float64 overflow and cannot be treated as correctness or incorrectness evidence. Original primary falsification threshold was not met.

THEORY: Disappearance of observed short equal-length collisions is not certified sufficient, but not falsified by these four endpoints. No theorem.
LEARNING: Four unmodified gradient-trained models remain unrestricted-correctness unresolved. No new transition.
