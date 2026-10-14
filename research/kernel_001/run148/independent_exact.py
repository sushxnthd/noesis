"""Independent exact-rational scalar rollout for trained checkpoint 214."""
from pathlib import Path
from fractions import Fraction as F
import json

HERE = Path(__file__).resolve().parent
CHECKPOINT = HERE.parent/"run147"/"checkpoints"/"214.json"

def exact_word(word, checkpoint=CHECKPOINT):
    p = json.loads(Path(checkpoint).read_text())
    A = [[F.from_float(v) for v in row] for row in p["A"]]
    E = [[F.from_float(v) for v in row] for row in p["E"]]
    w = [F.from_float(v) for v in p["w"]]
    h = [F(0)]*4
    q = 0
    for t in word:
        j = int(t)
        assert j in (0, 1, 2)
        q = max(0, q + (1 if j == 0 else -1 if j == 1 else 0))
        h = [max(F(0), sum((a*x for a, x in zip(row, h)), F(0)) + E[j][i])
             for i, row in enumerate(A)]
    y = sum((a*x for a, x in zip(w, h)), F(0))
    return y-q

if __name__ == "__main__":
    for word in ("0022222222222", "0202222222222"):
        e = exact_word(word)
        assert e > F(1, 10)
        print(word, float(e))
