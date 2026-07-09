import re
with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    c = f.read()
match = re.search(r'window\.mdsCallback = function\(btn, isCorrect, explanation, qid\) \{.*?\}', c, re.DOTALL)
if match: print(match.group(0))
else: print("Not found! Maybe it's not a function?")
