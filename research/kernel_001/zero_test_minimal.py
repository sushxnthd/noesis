"""Independent BFS shortest zero-test failure for a finite-cap ReLU recurrent counter."""
from collections import deque
import json
def shortest_zero_test_failure(M):
    queue=deque([(0,0,"")])
    seen={(0,0)}
    while queue:
        target,spoof,word=queue.popleft()
        if (target==0)!=(spoof==0):
            return {"cap":M,"length":len(word),"witness":word,
                    "target":target,"spoof":spoof,"states_examined":len(seen)}
        for x,symbol in ((-1,"-"),(1,"+")):
            t=max(0,target+x)
            z=spoof+x
            s=max(0,z)-max(0,z-M)
            if (t,s) not in seen:
                seen.add((t,s))
                queue.append((t,s,word+symbol))
if __name__=="__main__":
    results=[shortest_zero_test_failure(M) for M in range(1,13)]
    assert all(r["length"]==2*r["cap"]+1 for r in results)
    print(json.dumps(results,indent=2))
