from research.kernel001.run185.enumerate185 import balanced, classify

def test_shortest_split():
    assert all(classify(word)['classification']=='fails' for length in (2,4) for word in balanced(length))
    rows=[classify(word) for word in balanced(6)]
    assert len(rows)==20
    assert sum(row['classification']=='safe_infinite' for row in rows)==2
