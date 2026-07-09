import re
import os

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = f"{repo}/src/App.vue"
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all if (attempts >= 3) blocks and patch them
    # Since python regex is tricky with nested braces, let's just do targeted replacements
    
    # 1. replace any quizFeedback = "..." after attempts >= 3
    # Actually, let's just do a simple string replacement for known bad feedbacks
    
    # Let's remove revealQuizNext("Lanjut dulu →"); entirely
    content = content.replace('revealQuizNext("Lanjut dulu →");', '')
    content = content.replace("revealQuizNext('Lanjut dulu →');", '')
    
    # Replace the text inside attempts >= 3 blocks
    content = re.sub(
        r'(if\s*\(attempts\s*>=\s*3\)\s*\{.*?quizState\.value\.quizFeedback\s*=\s*).*?([\'"`].*?;)',
        r'\1"Sudah 3 kali salah. Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";',
        content,
        flags=re.DOTALL
    )
    
    # Ensure markQuestionFailed(item.qid) or markQuestionFailed(q.qid) is inside attempts >= 3
    # Wait, some places use `item.qid` and others `q.qid`
    
    # Let's make sure it's fully locked
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Patched feedback in {repo}")
