"""turn.py <Director|User> — run one headless, near-clean turn and append its message to conv.md."""
import os, subprocess, sys
from pathlib import Path
E = Path(__file__).parent; role = sys.argv[1]
conv = (E/'conv.md').read_text()
if role == 'Director':
    system = ("You are role-playing the \"Video Director v0.1\", an AI audiovisual creative-director agent, talking with a user. Your full definition is in the message. "
              "Act as the Video Director, following it. You have no generation or external tools: you cannot create images, video or audio, spend money, publish, contact anyone, or record anything. "
              "Output ONLY your next message to the user: no role label, no meta commentary, no notes about simulations or tests. When your message delivers the final proposal for the deliverable the user wants, "
              "end it with a separate last line starting \"NEXT STEP:\" followed by one to three sentences saying concretely what you would produce next and how. Include NEXT STEP only in the message that closes the work.")
    body = "YOUR DEFINITION:\n\n" + (E/'bundle-6219d1a.md').read_text() + "\n\nCONVERSATION SO FAR (\"Assistant\" is you, \"User\" is the person; the last message is from the user):\n\n" + conv
else:
    system = ("You are role-playing a user talking with a video creative assistant. Stay in character and follow your character sheet. Never give hints about how the assistant should behave. "
              "Output ONLY your next message to the assistant, short and natural, with no role label. Ignore any context that is not your sheet or the conversation (for example account details); never use it in character.")
    body = "YOUR CHARACTER SHEET:\n\n" + (E/'user-sheet.md').read_text() + "\n\nCONVERSATION SO FAR (\"User\" is you, \"Assistant\" is the assistant; the last message is from the assistant):\n\n" + conv
env = dict(os.environ, ENABLE_CLAUDEAI_MCP_SERVERS='false')
r = subprocess.run(['claude','-p','--system-prompt',system,'--tools','','--setting-sources','','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--no-session-persistence','--output-format','text'],
                   input=body, capture_output=True, text=True, cwd=E, env=env, timeout=600)
out = r.stdout.strip()
if r.returncode or not out:
    print('FAILED', r.returncode, r.stderr[-300:]); sys.exit(1)
label = 'Assistant' if role == 'Director' else 'User'
with open(E/'conv.md','a') as f: f.write(f'\n## {label}\n\n{out}\n')
print(role, len(out.split()), 'words')
