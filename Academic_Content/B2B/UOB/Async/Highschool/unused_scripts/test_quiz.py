import re

with open('sesi30-32/grup-hs-2-c/src/App.vue', 'r') as f:
    content = f.read()
    
match = re.search(r'const checkVideoQuizzes = .*?};', content, re.DOTALL)
if match:
    print(match.group(0))
