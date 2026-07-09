import re
import os

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = os.path.join(repo, 'src', 'App.vue')
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the <video> tag that has :src="introVideoSrc" and remove the "controls" attribute from it.
    
    def repl(match):
        video_tag = match.group(0)
        # Remove 'controls' or 'controls ' or '\ncontrols' 
        # But be careful not to break HTML.
        # It's safer to just replace 'controls' surrounded by whitespace/newlines
        new_tag = re.sub(r'\bcontrols\b\s*', '', video_tag)
        return new_tag

    # Match <video ... > that contains :src="introVideoSrc"
    pattern = r'<video[^>]*:src="introVideoSrc"[^>]*>'
    
    content = re.sub(pattern, repl, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {repo}")

