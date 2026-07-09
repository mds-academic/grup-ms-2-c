import os
import re

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    print(f"--- {repo} ---")
    filepath = os.path.join(repo, 'src/courseData.js')
    with open(filepath, 'r') as f:
        content = f.read()
        types = set(re.findall(r'type:\s*["\']([^"\']+)["\']', content))
        print(types)
