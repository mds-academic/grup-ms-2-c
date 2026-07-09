import re

with open('sesi40-44/grup-hs-2-d/src/courseData.js', 'r') as f:
    content = f.read()
    
print("qid in courseData:", "qid:" in content or "qid :" in content or "'qid'" in content or '"qid"' in content)
