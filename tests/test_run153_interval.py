from research.kernel_001.run153.interval_neutral import certify
def test_neutral_exact_first_failure():
    for seed,depth in [(208,83),(210,28),(214,25)]:
        assert certify(seed,depth)>.1
