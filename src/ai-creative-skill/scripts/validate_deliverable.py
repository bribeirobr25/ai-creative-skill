#!/usr/bin/env python3
"""V2.4 deterministic shape validator; not an LLM/semantic/host/provider validation."""
import json, sys
from pathlib import Path
CANDIDATES=[Path(__file__).resolve().parents[1]/'contracts/deliverable_contracts_v0.1.json',Path(__file__).resolve().parents[1]/'skills/ai-creative-skill/contracts/deliverable_contracts_v0.1.json']
CATALOG=next((path for path in CANDIDATES if path.exists()),CANDIDATES[0])

def inspect(deliverable_type, item, triggers=None, scope='FULL'):
    spec=json.loads(CATALOG.read_text())['types'][deliverable_type]
    triggers=set(triggers or [])
    if scope!='FULL':return {'result':'BOUNDED_SCOPE','missing':[],'note':'No guarantee of a full deliverable'}
    needed=list(spec['required'])
    for condition, fields in spec['conditional'].items():
        if condition in triggers:needed+=fields
    missing=[k for k in needed if k not in item or item[k] is None or (isinstance(item[k],str) and not item[k].strip()) or item[k]==[] or item[k]=={}]
    return {'result':'PASS_STRUCTURAL' if not missing else 'FAIL_STRUCTURAL', 'missing':missing, 'checked':len(needed),'semantic_verified':False}

if __name__=='__main__':
    data=json.load(sys.stdin)
    typ=data['type'];items=data.get('items') or [data['item']]
    results=[inspect(typ,it,data.get('triggers'),data.get('scope','FULL')) for it in items]
    print(json.dumps({'item_count':len(results),'results':results,'all_structural_pass':all(x['result']=='PASS_STRUCTURAL' for x in results)},ensure_ascii=False))
