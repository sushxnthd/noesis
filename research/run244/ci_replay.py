import json,sys,hashlib
from pathlib import Path
sys.path.insert(0,"research/run244")
from box_latch_reimplementation import run
from checker_latch import check
def find(name,sha):
 matches=[p for p in Path("incoming").rglob(name) if hashlib.sha256(p.read_bytes()).hexdigest()==sha]
 assert len(matches)==1
 return json.loads(matches[0].read_text())
data=find("CHECKPOINTS.json","28c294606e4bd1f68e3f8d06caaa890736037095304d9eba7e3a897e48af50dd")
exact=find("EXACT.json","9f9f8263107c188bb0efe47035f2028435e5579e24e921d92a6369297a3172c8")
old={(r["seed"],r["arm"]):r["status"] for r in exact if r["epoch"]==200}
out=[]
for row in data["rows"]:
 if row["epoch"]!=200:continue
 result=run(row)
 if result["status"]=="CERTIFIED":assert check(row,result["certificate"])
 out.append({"seed":row["seed"],"arm":row["arm"],"old":old[row["seed"],row["arm"]],**result})
new=sum(r["old"]=="ABSTAIN" and r["status"]=="CERTIFIED" for r in out)
false=sum(r["old"]=="INCORRECT" and r["status"]=="CERTIFIED" for r in out)
assert len(out)==96 and new==11 and false==0
Path("run244_ci_results.json").write_text(json.dumps(out,indent=2))
print("PASS",len(out),new,false)
