"""Report intake completeness, never infer authentic humans or owner approval."""
import json,sys
from pathlib import Path
DIMENSIONS=('composition','fidelity','message','product','cta','usefulness')
def assess(records):
    ids=set();packets=set();errors=[]
    for i,r in enumerate(records):
        v=r.get('values',{});rid=v.get('reviewer_id','').strip();packet=r.get('packet')
        if not rid or rid in ids:errors.append(f'record {i}: missing/duplicate reviewer id')
        ids.add(rid)
        if packet not in ('R1','R2') or packet in packets:errors.append(f'record {i}: missing/duplicate packet')
        packets.add(packet)
        if r.get('schema')!='creative-quality-human-response/1' or r.get('source')!='SELF_REPORTED_HUMAN_UNVERIFIED':errors.append(f'record {i}: unsupported response provenance')
        for key in ('human','independent','all_media'):
            if v.get(key)!='on':errors.append(f'record {i}: missing attestation {key}')
        for key in ('viewing_context','prior_exposure'):
            if not v.get(key,'').strip():errors.append(f'record {i}: missing {key}')
        for width in (1440,390):
            if v.get(f'{width}_preference') not in ('X','Y','TIE','INSUFFICIENT') or not v.get(f'{width}_reason','').strip():errors.append(f'record {i}: incomplete viewport decision')
            for dim in DIMENSIONS:
                for label in ('X','Y'):
                    if v.get(f'{width}_{dim}_{label}') not in ('1','2','3','4','5','NA'):errors.append(f'record {i}: missing dimension score')
    return {'gate':'AWAITING_HUMAN_REVIEW','submitted_records':len(records),'intake_complete':len(records)==2 and not errors,'intake_errors':errors,'next_step':'Coordinator must verify distinct genuine humans, independence and prior exposure, preserve dissent, then obtain owner acceptance. Form completeness cannot certify preference.','owner_acceptance':'NOT_GIVEN'}
if __name__=='__main__':
    folder=Path(sys.argv[1]);records=[json.loads(f.read_text()) for f in sorted(folder.glob('resposta-*.json'))];print(json.dumps(assess(records),indent=2))
