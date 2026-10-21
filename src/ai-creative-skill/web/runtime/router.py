"""Bounded deterministic pre-router, never semantic or publication authority."""
from dataclasses import dataclass
from typing import Optional
import re
import unicodedata

@dataclass(frozen=True)
class Route:
    route: str
    mode: str
    reason: str
    build_required: bool
    authority_gate: bool

ROUTES={
  'WEB_RESEARCH_ONLY': (False,False), 'WEB_CONCEPT_ONLY':(False,False),
  'WEB_PREVIEW':(True,False), 'WEB_EDIT':(True,False),'WEB_PUBLICATION':(True,True)
}
ACTIONS={
 'WEB_PUBLICATION':r'\b(?:publique|publicar|publish|deploy|coloque no ar|put it live|go live)\b',
 'WEB_RESEARCH_ONLY':r'\b(?:pesquise|pesquisar|research|analise|analisar|benchmark|audite|compare referencias)\b',
 'WEB_EDIT':r'\b(?:mude apenas|altere apenas|edite|refine|corrija o hero|update the hero)\b',
 'WEB_CONCEPT_ONLY':r'\b(?:wireframe|roteiro de site|conceito visual|estrutura de landing|sitemap)\b',
 'WEB_PREVIEW':r'\b(?:crie uma landing|crie um site|criar um website|construa um site|monte um website|build a website|create a landing)\b'
}
NEGATION=r"\b(?:nao|nunca|nem|never|not|don't|dont|do not|sem|without|evite|avoid)\s+(?:\w+\s+){0,2}$"

def action_state(text,pattern):
    positive=negative=False
    for match in re.finditer(pattern,text):
        prefix=re.split(r'[;,.!?\n]|\b(?:mas|but|and|e|entao|then)\b',text[:match.start()])[-1]
        denied=bool(re.search(NEGATION,prefix) or re.match(r'\s+(?:nada|nothing)\b',text[match.end():]))
        negative|=denied;positive|=not denied
    return positive,negative

def resolve(text: str, intent: Optional[str]=None, deep:bool=False)->Route:
    text=''.join(c for c in unicodedata.normalize('NFKD',text.casefold().replace('’',"'")) if not unicodedata.combining(c))
    states={route:action_state(text,pattern) for route,pattern in ACTIONS.items()}
    if intent:
        if intent not in ROUTES:raise ValueError('Unknown route: '+intent)
        if states[intent][1]:raise ValueError('Explicit intent conflicts with a stated prohibition')
        r=intent;reason='explicit_intent'
    else:
        if not re.search(r'\b(?:site|sites|website|websites|landing|pagina|page|hero|ux|dominio|domain|wireframe|sitemap)\b',text):
            raise ValueError('Ambiguous request; explicit intent or clarification needed')
        positive={route for route,(yes,no) in states.items() if yes and not no}
        if any(yes and no for yes,no in states.values()):
            raise ValueError('Conflicting positive and negative requests')
        # An informational question about publication is not an execution request.
        if 'WEB_RESEARCH_ONLY' in positive and re.search(r'\b(?:como|how|sobre|about)\b',text) and not re.search(r'\b(?:depois|then|e (?:publique|crie|construa|edite)|and (?:publish|deploy|build|create|edit))\b',text):
            positive={'WEB_RESEARCH_ONLY'}
        if len(positive)!=1:raise ValueError('Ambiguous or multi-operation request; explicit intent needed')
        r=next(iter(positive));reason='deterministic_text_triage_not_final_semantic_authority'
    build,auth=ROUTES[r]
    return Route(r,'DEEP' if deep else 'FAST',reason,build,auth)
