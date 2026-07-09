import re

with open('sesi25-26/grup-hs-2-a/src/App.vue', 'r') as f:
    content = f.read()
    
match = re.search(r'const submitStandardAnswer = .*?};', content, re.DOTALL)
if match:
    print("Standard:", match.group(0))

match = re.search(r'const submitInputAnswer = .*?};', content, re.DOTALL)
if match:
    print("Input:", match.group(0))
