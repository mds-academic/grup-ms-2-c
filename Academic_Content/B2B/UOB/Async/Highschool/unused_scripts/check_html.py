import os
import re
import json

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi30-32/grup-hs-2-c',
]

for repo in repos:
    print(f"--- {repo} ---")
    filepath = os.path.join(repo, 'src/courseData.js')
    if not os.path.exists(filepath): continue
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract all html contents
    htmls = re.findall(r'html:\s*`(.*?)`', content, re.DOTALL)
    for i, html in enumerate(htmls):
        if 'answer-opt-btn' not in html and 'check' not in html and 'onclick' not in html:
            print(f"Slide {i} might be an info slide!")
            print(html[:100].strip())
            print("...")

