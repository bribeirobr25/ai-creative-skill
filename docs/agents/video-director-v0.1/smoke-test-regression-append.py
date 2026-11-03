"""append.py <agent_output_jsonl> <conversation.md> <User|Assistant> — append the agent's final message; strip a trailing END line and report it."""
import json, sys
src, conv, role = sys.argv[1:4]
last = None
for line in open(src):
    try: o = json.loads(line)
    except Exception: continue
    m = o.get('message') or {}
    if m.get('role') == 'assistant' and isinstance(m.get('content'), list):
        t = '\n'.join(c.get('text', '') for c in m['content'] if isinstance(c, dict) and c.get('type') == 'text').strip()
        if t: last = t
end = False
lines = last.rstrip().split('\n')
if lines and lines[-1].strip() == 'END':
    end = True; last = '\n'.join(lines[:-1]).rstrip()
with open(conv, 'a') as f:
    f.write(f'\n## {role}\n\n{last}\n')
print('END' if end else 'continue', len(last.split()), 'words', ('NEXT STEP' in last) and 'has NEXT STEP' or '')
