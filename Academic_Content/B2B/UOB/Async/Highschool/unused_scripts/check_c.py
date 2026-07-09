import os
import re

with open('sesi30-32/grup-hs-2-c/src/courseData.js', 'r') as f:
    content = f.read()

# find all questions
qs = re.findall(r'\{\s*(html: `.*?`|question: ".*?")\s*\}', content, re.DOTALL)
for q in qs:
    if 'html: `' in q:
        html = re.search(r'html: `(.*?)`', q, re.DOTALL).group(1)
        if 'check' not in html and 'answer-opt-btn' not in html and 'onclick' not in html:
            print("Found potential info slide in C:")
            print(html[:100].strip())
            print("---")
