from research.kernel_001.zero_test_minimal import shortest_zero_test_failure
def test_minimal_zero_test_witness_independent_bfs():
    for M in range(1,13):
        r=shortest_zero_test_failure(M)
        assert r["length"]==2*M+1
        assert r["witness"]=="+"*(M+1)+"-"*M
        assert (r["target"],r["spoof"])==(1,0)
