import json
from pathlib import Path
p=Path(__file__).parent
rows=[json.loads((p/'checkpoints'/('seed_'+str(s)+'.json')).read_text()) for s in [751,757,761,769,773,787,797,809]]
(p/'RUN210_CHECKPOINTS.json').write_text(json.dumps({'rows':rows}))
