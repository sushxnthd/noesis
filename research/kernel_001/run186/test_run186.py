from proof186 import prove

def test_three_first_failure_clocks():
    for word in ("011100","101010","110001"):
        result=prove(word)
        assert result["first_failure"]==8623
        assert result["previous"][0]==8622
        assert float(result["interval_at_8192"][1])<0.1
        assert float(result["failure_interval"][0])>0.1
