import os
import re
import json

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = os.path.join(repo, 'src/courseData.js')
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Find blocks of `{ html: \`...\` }` that don't have `type: "info"` and don't have buttons
    # Actually, in grup-hs-2-a, the "Selesai Menonton!" slide is fixed. Are there others?
    htmls = re.findall(r'(\{\s*html:\s*`(.*?)`\s*\})', content, re.DOTALL)
    for full_match, html in htmls:
        if 'answer-opt-btn' not in html and 'check' not in html and 'onclick' not in html and 'type:' not in full_match:
            print(f"[{repo}] Found info slide without type!")
            print(html[:50])
            new_match = full_match.replace('html: `', 'type: "info",\n            html: `')
            content = content.replace(full_match, new_match)

    with open(filepath, 'w') as f:
        f.write(content)

print("Done")
