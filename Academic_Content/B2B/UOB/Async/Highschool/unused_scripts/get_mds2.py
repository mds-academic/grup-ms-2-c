import re
with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    c = f.read()
match = re.search(r'window\.mdsCallback = \(.*?\) => \{.*?\}', c, re.DOTALL)
if match: print(match.group(0))
else: print("Not found!")
