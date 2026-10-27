"""DQB-03 font pool writer: same files for every run, family order shuffled per run (typography confounder control).
usage: python3 font_pack.py <shared_fonts_dir> <out_fonts_dir> <seed>"""
import random,re,shutil,sys,pathlib
src,dst,seed=pathlib.Path(sys.argv[1]),pathlib.Path(sys.argv[2]),sys.argv[3]
FAMILIES={ # family: (file stem, category)
 'Fraunces':('fraunces','serif'),'Newsreader':('newsreader','serif'),'Playfair Display':('playfair-display','serif'),
 'DM Serif Display':('dm-serif-display','serif'),'Cormorant Garamond':('cormorant-garamond','serif'),
 'Inter':('inter','sans'),'Instrument Sans':('instrument-sans','sans'),'Manrope':('manrope','sans'),
 'Outfit':('outfit','sans'),'Archivo':('archivo','sans'),'Space Grotesk':('space-grotesk','sans'),
 'Bricolage Grotesque':('bricolage-grotesque','sans'),'Syne':('syne','sans'),'IBM Plex Mono':('ibm-plex-mono','mono')}
files=sorted(p.name for p in (src/'files').iterdir())
def faces(fam,stem):
    out=[]
    for f in files:
        if not f.startswith(stem+'-latin-'):continue
        m=re.match(re.escape(stem)+r'-latin-(wght|\d+)-(normal|italic)\.woff2$',f)
        if not m:continue
        w,style=m.groups();weight='100 900' if w=='wght' else w
        out.append(f'@font-face{{font-family:"{fam}";src:url("files/{f}") format("woff2");font-weight:{weight};font-style:{style};font-display:swap}}')
    return out
order=list(FAMILIES);random.Random(seed).shuffle(order)
dst.mkdir(parents=True,exist_ok=True)
shutil.copytree(src/'files',dst/'files',dirs_exist_ok=True);shutil.copytree(src/'licenses',dst/'licenses',dirs_exist_ok=True)
css=['/* Shared font pool: SIL Open Font License 1.1 families, self-hosted, latin subset. Use any subset; none is required. */']
md=['# Font pool','','Self-hosted SIL OFL families (licenses in `licenses/`). Load with `<link rel="stylesheet" href="fonts/fonts.css">`. Use any subset; none is required. Listed in no particular order.','']
for fam in order:
    stem,cat=FAMILIES[fam];css+=faces(fam,stem);md.append(f'- {fam} ({cat})')
(dst/'fonts.css').write_text('\n'.join(css)+'\n');(dst/'FONTS.md').write_text('\n'.join(md)+'\n')
print(order)
