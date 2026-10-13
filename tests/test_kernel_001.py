from research.kernel_001.finite_horizon_spoof import (
    spoof_step,
    sweep,
    target_step,
    verify_horizon,
)


def test_spoof_matches_observed_range_and_diverges_afterward():
    for horizon in (1, 2, 4, 8, 16, 32, 64):
        for state in range(horizon + 1):
            assert spoof_step(state, horizon) == target_step(state)
        assert spoof_step(horizon + 1, horizon) != target_step(horizon + 1)


def test_exact_composition_verification():
    result = verify_horizon(12)
    assert result.passed
    assert result.first_divergence_state == 13
    assert result.observed_transition_checks == 13
    assert result.observed_composition_checks > 0


def test_preregistered_sweep():
    results = sweep(range(1, 65))
    assert len(results) == 64
    assert all(r.passed for r in results)
    assert [r.first_divergence_state for r in results] == list(range(2, 66))
