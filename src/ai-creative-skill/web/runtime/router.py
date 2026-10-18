"""Deterministic pre-router for portable web deliverables; not an LLM semantic judge."""
from dataclasses import dataclass
from typing import Optional

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

def resolve(text: str, intent: Optional[str]=None, deep:bool=False)->Route:
    """Explicit intent beats lexical heuristic. Unknown text does not authorize build."""
    if intent:
        if intent not in ROUTES: raise ValueError('Unknown route: '+intent)
        r=intent; reason='explicit_intent'
    else:
        t=text.casefold()
        if any(x in t for x in ('publiqu','deploy','coloque no ar','put it live','domínio')) and any(x in t for x in ('site','website','landing','página','page')):
            r='WEB_PUBLICATION'
        elif any(x in t for x in ('mude apenas','altere apenas','edite','refine','corrija o hero','update the hero')) and any(x in t for x in ('site','página','landing','hero','website')):
            r='WEB_EDIT'
        elif any(x in t for x in ('analise','pesquise','benchmark','audite','compare referências','research')) and any(x in t for x in ('site','página','landing','website','ux')):
            r='WEB_RESEARCH_ONLY'
        elif any(x in t for x in ('wireframe','roteiro de site','conceito visual','estrutura de landing','sitemap')) and not any(x in t for x in ('construa','crie um site','faça um site')):
            r='WEB_CONCEPT_ONLY'
        elif any(x in t for x in ('crie uma landing','criar um website','construa um site','monte um website','build a website','create a landing','crie um site')):
            r='WEB_PREVIEW'
        else:
            raise ValueError('Ambiguous request; explicit intent or clarification needed')
        reason='deterministic_text_triage_not_final_semantic_authority'
    build,auth=ROUTES[r]
    return Route(r,'DEEP' if deep else 'FAST',reason,build,auth)
