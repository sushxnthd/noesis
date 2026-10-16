"""Independent interval classification of all length-15 inputs for run197."""
import json,time
from pathlib import Path
from independent_check import advance,output,is_correct
from mpmath import iv

count=0
wrong=[]
ambiguous=[]
t0=time.time()

def walk(h,cls,depth,word):
    global count
    if depth==15:
        count+=1
        z=output(h)
        if is_correct(z,cls):return
        winner=[j for j in range(3) if all(j==k or bool((z[j]-z[k]).a>0) for k in range(3))]
        if len(winner)==1:wrong.append({'word':word,'true':cls,'predicted':winner[0]})
        else:ambiguous.append(word)
        return
    for bit in (0,1):walk(advance(h,bit),(cls+bit)%3,depth+1,word+str(bit))

walk([iv.mpf(0)]*12,0,0,'')
assert count==32768
assert not ambiguous
assert wrong==[{'word':'000000101010000','true':0,'predicted':1}],wrong
result={'exact_length':15,'inputs_checked':count,'wrong_count':len(wrong),'wrong':wrong,
        'ambiguous':len(ambiguous),'precision_decimal_digits':45,'independent_interval':True,
        'elapsed_seconds':round(time.time()-t0,2)}
Path('EXACT_LENGTH15.json').write_text(json.dumps(result,indent=1)+'\n')
print(json.dumps(result,indent=1))
