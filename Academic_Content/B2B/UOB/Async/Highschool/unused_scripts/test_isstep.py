import re

with open('sesi25-26/grup-hs-2-a/src/App.vue', 'r') as f:
    content = f.read()
    
match = re.search(r'const isStepFinished = .*?};', content, re.DOTALL)
if match:
    print("GRUP A:", match.group(0))

with open('sesi30-32/grup-hs-2-c/src/App.vue', 'r') as f:
    content = f.read()
    
match = re.search(r'const isStepFinished = .*?};', content, re.DOTALL)
if match:
    print("GRUP C:", match.group(0))
