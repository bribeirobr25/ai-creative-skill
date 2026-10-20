"""Source preservation and bounded UI dependency invalidation; not browser acceptance."""
from pathlib import Path
import hashlib,json,re
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup

def digest(text):return hashlib.sha256(text.encode()).hexdigest()

def snapshot(root,regions):
    root=Path(root).resolve();soup=BeautifulSoup((root/'index.html').read_text(),'html.parser')
    result={'sections':{},'global_files':{},'limitations':[]}
    for name in regions:
        element=soup.select_one('section.hero') if name=='hero' else soup.find(id=name)
        result['sections'][name]=digest(str(element)) if element is not None else None
    dependencies=result['global_files'];seen=set();descriptors=[]
    def limitation(value):
        if value not in result['limitations']:result['limitations'].append(value)
    def visit(ref,base=root,kind=None):
        try:parsed=urlsplit(ref)
        except ValueError:limitation('Malformed dependency URL');return
        if parsed.scheme or parsed.netloc:
            if parsed.scheme not in ('data',):limitation('External dependency content unverified')
            return
        if not parsed.path:return
        path=(root/unquote(parsed.path).lstrip('/') if parsed.path.startswith('/') else base/unquote(parsed.path)).resolve()
        if not path.is_relative_to(root):limitation('Dependency outside project root');return
        key=path.relative_to(root).as_posix()
        visit_key=(key,kind)
        if visit_key in seen:return
        if len(seen)>=256:limitation('Dependency graph exceeds 256 files');return
        seen.add(visit_key)
        if not path.is_file():dependencies[key]='MISSING';limitation('Missing dependency');return
        content=path.read_bytes();dependencies[key]=hashlib.sha256(content).hexdigest()
        if kind=='style' or path.suffix=='.css':
            css=re.sub(r'/\*.*?\*/','',content.decode('utf-8',errors='replace'),flags=re.S)
            refs=re.findall(r'url\(\s*[\'"]?([^\s\)\'\"]+)',css)
            for child in refs:visit(child,path.parent)
            for child in re.findall(r'@import\s+(?:url\(\s*)?[\'"]?([^\s;\)\'\"]+)',css):visit(child,path.parent,'style')
        elif kind=='script' or path.suffix in ('.js','.mjs'):
            js=content.decode('utf-8',errors='replace')
            refs=re.findall(r'\b(?:import|export)\s+(?:[^;\n]*?\bfrom\s*)?[\'"]([^\'\"]+)',js)
            refs+=re.findall(r'\bimport\s*\(\s*[\'"]([^\'\"]+)[\'"]\s*\)',js)
            for child in refs:
                if child.startswith(('.', '/')) or urlsplit(child).scheme:visit(child,path.parent,'script')
                else:limitation('Bare module specifier requires host resolution')
            if re.search(r'\b(?:fetch|Worker|require)\s*\(|\bimport\s*\(\s*[^\s\'\"]',js):
                limitation('Dynamic dependency requires browser inspection')
    for node in soup.find_all(True):
        refs=[];tag=node.name
        if tag=='script':
            descriptors.append(str(node))
            if node.get('src'):refs.append((node['src'],'script'))
            elif node.get_text(strip=True):limitation('Inline script dependencies require browser inspection')
        elif tag=='style':
            descriptors.append(str(node))
            for ref in re.findall(r'url\(\s*[\'"]?([^\s\)\'\"]+)|@import\s+[\'"]([^\'\"]+)',node.get_text()):refs.append((ref[0] or ref[1],None))
        elif tag=='link' and node.get('href'):
            descriptors.append(str(node));refs.append((node['href'],'style' if 'stylesheet' in node.get('rel',[]) else None))
        elif tag in ('img','source','video','audio','iframe','embed','input','object','use','image'):
            attrs={k:v for k,v in node.attrs.items() if k in ('src','srcset','href','xlink:href','poster','data','type','sizes','media')}
            if attrs:descriptors.append(json.dumps([tag,attrs],sort_keys=True))
            for attr in ('src','href','xlink:href','poster','data'):
                if node.get(attr):refs.append((node[attr],None))
            if node.get('srcset'):
                if 'data:' in node['srcset']:limitation('Embedded srcset requires browser inspection')
                else:refs.extend((part.strip().split()[0],None) for part in node['srcset'].split(',') if part.strip())
        if tag in ('iframe','object','embed'):limitation('Embedded document requires browser inspection')
        if tag=='base':descriptors.append(str(node));limitation('Base URL requires browser inspection')
        inline={k:v for k,v in node.attrs.items() if k=='style' or k.startswith('on')}
        if inline:
            descriptors.append(json.dumps(inline,sort_keys=True))
            for ref in re.findall(r'url\(\s*[\'"]?([^\s\)\'\"]+)',node.get('style','')):refs.append((ref,None))
        for ref,kind in refs:visit(ref,kind=kind)
    dependencies['@entry_dependencies']=digest(json.dumps(descriptors,sort_keys=True))
    # Changes outside named regions can affect layout even without a resource change.
    for name in dict.fromkeys(regions):
        element=soup.select_one('section.hero') if name=='hero' else soup.find(id=name)
        if element is not None:
            placeholder=soup.new_tag('template');placeholder['data-reviewed-region']=name
            element.replace_with(placeholder)
    dependencies['@document_shell']=digest(str(soup))
    result['limitations'].sort()
    return result

def compare(before_root,after_root,preserved,changed):
    b=snapshot(before_root,preserved+changed);a=snapshot(after_root,preserved+changed)
    preserved_diffs=[r for r in preserved if b['sections'][r] is None or a['sections'][r] is None or b['sections'][r]!=a['sections'][r]]
    changed_missing=[r for r in changed if b['sections'][r] is None or b['sections'][r]==a['sections'][r]]
    globals_changed=[f for f in sorted(set(b['global_files'])|set(a['global_files'])) if b['global_files'].get(f)!=a['global_files'].get(f)]
    limitations=sorted(set(b['limitations']+a['limitations']))
    retest=bool(globals_changed or limitations)
    return {'protected_regions_unchanged':not preserved_diffs,'preservation_failures':preserved_diffs,
        'target_regions_unchanged':changed_missing,'shared_css_js_changed':globals_changed,
        'dependency_limitations':limitations,'browser_retest_required':retest,'human_approval_not_inferred':True,
        'status':'FAIL' if preserved_diffs or changed_missing else ('PARTIAL' if retest else 'SOURCE_PRESERVATION_PASS')}
