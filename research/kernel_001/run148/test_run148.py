from fractions import Fraction as F
from all_alphabet_certificate import run, word_of
from independent_exact import exact_word
from independent_global_bound import verify

def test_witnesses():
    for word in ("0022222222222", "0202222222222"):
        assert exact_word(word) > F(1, 10)

def test_training_horizon():
    assert abs(exact_word("002222")) < F(1, 10)

def test_global_shortest():
    result = run(13)
    assert result["rows"][11]["words"] == 531441
    assert result["rows"][11]["maximum_abs_error_upper_bound"] < .1
    assert result["rows"][12]["words"] == 1594323
    assert [x["word"] for x in result["rows"][12]["witnesses"]] == [
        "0022222222222", "0202222222222"]

def test_independent_global_bound():
    rows = verify()
    assert len(rows) == 12
    assert rows[-1][1] + rows[-1][2] < .1

def test_word_decode():
    assert word_of(0, 3) == "000"
    assert word_of(3**3-1, 3) == "222"
