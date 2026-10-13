"""Exact finite-horizon spoof construction for NOESIS Kernel 001.

This is a baseline falsification utility, not a novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Verification:
    horizon: int
    observed_transition_checks: int
    observed_composition_checks: int
    first_divergence_state: int
    passed: bool


def target_step(state: int) -> int:
    """Unbounded counter transition."""
    if state < 0:
        raise ValueError("state must be non-negative")
    return state + 1


def spoof_step(state: int, horizon: int) -> int:
    """Finite-range heuristic that matches increment through `horizon`.

    It agrees with target_step for every observed input 0..horizon and then
    saturates at horizon + 1. Thus the first divergent transition is from
    state horizon + 1.
    """
    if horizon < 0 or state < 0:
        raise ValueError("state and horizon must be non-negative")
    if state <= horizon:
        return state + 1
    return horizon + 1


def iterate(step, state: int, steps: int) -> int:
    if steps < 0:
        raise ValueError("steps must be non-negative")
    out = state
    for _ in range(steps):
        out = step(out)
    return out


def verify_horizon(horizon: int) -> Verification:
    if horizon < 1:
        raise ValueError("horizon must be >= 1")

    transition_checks = 0
    for state in range(horizon + 1):
        assert spoof_step(state, horizon) == target_step(state)
        transition_checks += 1

    composition_checks = 0
    # Only test compositions whose entire target trajectory remains within
    # the observed input domain 0..horizon. This models a finite evaluation
    # that never queries the transition at the first unseen state H+1.
    for start in range(horizon + 1):
        max_steps = horizon - start
        for left in range(max_steps + 1):
            for right in range(max_steps - left + 1):
                spoof = lambda s: spoof_step(s, horizon)
                lhs = iterate(spoof, iterate(spoof, start, left), right)
                rhs = iterate(spoof, start, left + right)
                target = start + left + right
                assert lhs == rhs == target
                composition_checks += 1

    first_unseen = horizon + 1
    assert spoof_step(first_unseen, horizon) != target_step(first_unseen)

    return Verification(
        horizon=horizon,
        observed_transition_checks=transition_checks,
        observed_composition_checks=composition_checks,
        first_divergence_state=first_unseen,
        passed=True,
    )


def sweep(horizons: Iterable[int]) -> list[Verification]:
    return [verify_horizon(h) for h in horizons]


if __name__ == "__main__":
    import json
    from dataclasses import asdict

    results = sweep(range(1, 65))
    print(json.dumps([asdict(r) for r in results], indent=2, sort_keys=True))
