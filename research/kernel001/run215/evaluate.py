import json,itertools
from pathlib import Path
P=Path(__file__).resolve().parents[2]/'run214'
H=Path(__file__).resolve().parent
d=json.loads((P/'RUN214_CHECKPOINTS.json').read_text())
rows={r['seed']:r for r in d['rows'] if r['epoch']==100}
v100={r['seed']:r['status'] for r in json.loads((H/'epoch100_labels.json').read_text())['results']}
v200={r['seed']:r['status'] for r in json.loads((P/'RUN214_VERIFIED_LABELS.json').read_text())['results']}
trans=[s for s in rows if v100[s]=='INCORRECT' and v200[s]=='CORRECT']
persist=[s for s in rows if v100[s]=='INCORRECT' and v200[s]=='INCORRECT']
sub=trans+persist
def auc(values,positive):
 p=[values[s] for s in positive];n=[values[s] for s in sub if s not in positive]
 return sum((a>b)+.5*(a==b) for a in p for b in n)/(len(p)*len(n))
scores={
 'generic_prefix':{s:rows[s]['generic_prefix'] for s in sub},
 'generic_final':{s:rows[s]['generic_final'] for s in sub},
 'retention':{s:rows[s]['retention_score'] for s in sub},
 'negative_loss':{s:-rows[s]['loss'] for s in sub},
 'train_accuracy':{s:rows[s]['train_accuracy'] for s in sub},
 'negative_heldout64_errors':{s:-rows[s]['heldout64_prefix_errors'] for s in sub}}
results={k:auc(v,trans) for k,v in scores.items()}
null=[auc(scores['generic_prefix'],set(c)) for c in itertools.combinations(sub,len(trans))]
out={'transition_seeds':trans,'persistent_failure_seeds':persist,'auroc':results,
 'exact_one_sided_permutation_p':sum(x>=results['generic_prefix']-1e-12 for x in null)/len(null),
 'num_permutations':len(null),'pass':len(trans)>=4 and results['generic_prefix']>=.75}
(H/'evaluation_reproduced.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
