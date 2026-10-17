"""Recheck Run215 epoch100 classifications with two interval implementations."""
import json,sys
from pathlib import Path
H=Path(__file__).resolve().parent
P=H.parents[1]/'run214'
sys.path[:0]=[str(P),str(P/'run210')]
from verify_run210 import certify
import verify_decimal as D
import verify_run214 as V
import refine_run214 as R
rows={r['seed']:r for r in json.loads((P/'RUN214_CHECKPOINTS.json').read_text())['rows'] if r['epoch']==100}
labels=json.loads((H/'epoch100_labels.json').read_text())['results']
for entry in labels:
 row=rows[entry['seed']]
 if entry['word'] is not None:
  a=V.witness_iv(row,entry['word']);b=V.witness_decimal(row,entry['word'])
  status='INCORRECT' if a['status']==b['status']=='INCORRECT' else 'UNRESOLVED'
 else:
  a=certify(row)
  if a['status']=='CERTIFIED':
   b=D.check(row,a['rational_invariant_boxes'])
  else:
   c=R.candidate(row['params'])
   if c['status']=='CANDIDATE':
    a=V.five_cell_iv(row,c);b=V.five_cell_decimal(row,c)
   else:b={'status':'ABSTAIN'}
  status='CORRECT' if a['status']==b['status']=='CERTIFIED' else 'UNRESOLVED'
 assert status==entry['status'],(entry['seed'],status,entry['status'])
 print(entry['seed'],status,flush=True)
