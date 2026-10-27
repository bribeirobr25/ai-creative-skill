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
# Natural build requests ("crie o website descrito", "faca um site", "build me a landing page"). The site noun must be
# the direct object of the build verb: an article, at most one listed adjective, then the noun. Weak verbs (faca,
# make, quero...) only count with an indefinite article, so "make my page faster" or "faca o site mais rapido" (edits)
# do not build. Questions and social-network pages never build.
SITE_NOUN=(r'(?:site|sites|website|websites|landing\s*pages?|landings?|landingpages?|paginas?|pages?|homepages?'
  r'|loja\s+(?:virtual|online)|lojas\s+(?:virtuais|online)|e-?commerce)')
ADJECTIVE=(r'(?:(?:novo|nova|novos|novas|new|simples|simple|pequeno|pequena|small|institucional|primeiro|primeira|first'
  r'|completo|completa|complete|one-page|single-page|unica|unico)\s+)?')
POLITE=r'(?:,?\s*(?:por favor|pfv|please),?\s+|\s+)'
DETERMINER=r'(?:um|uma|uns|umas|o|a|os|as|meu|minha|nosso|nossa|seu|sua|esse|essa|este|esta|an|the|my|our|this|that)\s+'
STRONG_VERB=(r'(?:crie|criar|cria|construa|construir|monte|montar|desenvolva|desenvolver|gere|gerar|elabore|elaborar'
  r'|produza|produzir|desenhe|programe|build|create|develop|generate|put together)')
# Portuguese "a" is a definite article, so English and Portuguese weak verbs take their own indefinites.
WEAK_PT=r'(?:faca|fazer|faz|quero|preciso de)(?:\s+me)?'+POLITE+r'(?:um|uma|uns|umas|novo|nova)\s+'
WEAK_EN=r'(?:make|i want|i need|we need|we want)(?:\s+me)?'+POLITE+r'(?:a|an|new)\s+'
SOCIAL=r'(?!(?:\s+\w+){0,3}\s+(?:instagram|facebook|linkedin|tiktok|youtube|twitter|pinterest|threads|whatsapp)\b)'
ACTIONS['WEB_PREVIEW']=(ACTIONS['WEB_PREVIEW'][:-3]+r'|(?:'+STRONG_VERB+r'(?:\s+me)?'+POLITE+DETERMINER+r'|'
  +WEAK_PT+r'|'+WEAK_EN+r')'+ADJECTIVE+SITE_NOUN+r'\b'+SOCIAL+r')\b')
QUESTION=(r'\?|^\s*(?:como|how|quanto|quantos|qual|quais|what|why|por que|porque|onde|where|quando|when'
  r'|voce consegue|consegue|voce pode|can you|could you|is it possible|e possivel)\b')
NEGATION=r"\b(?:nao|nunca|nem|never|not|don't|dont|do not|sem|without|evite|avoid)\s+(?:\w+\s+){0,2}$"

def action_state(text,pattern):
    positive=negative=False
    for match in re.finditer(pattern,text):
        # Only the nearby clause matters; bounding the prefix keeps long inputs linear.
        prefix=re.split(r'[;,.!?\n]|\b(?:mas|but|and|e|entao|then)\b',text[max(0,match.start()-240):match.start()])[-1]
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
        if not re.search(r'\b(?:'+SITE_NOUN+r'|hero|ux|dominio|domain|wireframe|sitemap)\b',text):
            raise ValueError('Ambiguous request; explicit intent or clarification needed')
        positive={route for route,(yes,no) in states.items() if yes and not no}
        if any(yes and no for yes,no in states.values()):
            raise ValueError('Conflicting positive and negative requests')
        # An informational question about publication is not an execution request.
        if 'WEB_RESEARCH_ONLY' in positive and re.search(r'\b(?:como|how|sobre|about)\b',text) and not re.search(r'\b(?:depois|then|e (?:publique|crie|construa|edite)|and (?:publish|deploy|build|create|edit))\b',text):
            positive={'WEB_RESEARCH_ONLY'}
        # A question about building ("como criar um site?") asks for information, not a build.
        if 'WEB_PREVIEW' in positive and re.search(QUESTION,text):positive.discard('WEB_PREVIEW')
        if len(positive)!=1:raise ValueError('Ambiguous or multi-operation request; explicit intent needed')
        r=next(iter(positive));reason='deterministic_text_triage_not_final_semantic_authority'
    build,auth=ROUTES[r]
    return Route(r,'DEEP' if deep else 'FAST',reason,build,auth)
