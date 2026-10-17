import json
from beam_core import search
results={str(k):search(k) for k in (256,384,512)}
assert results["256"]==["20011100","20011101"]
assert results["384"]==[]
assert results["512"]==["20011100","20011101"]
print(json.dumps(results))
