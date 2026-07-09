import re

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    content = f.read()
    
match = re.search(r'const isStepFinished = .*?};', content, re.DOTALL)
if match:
    print(match.group(0))
