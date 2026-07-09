import os

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = os.path.join(repo, 'src/App.vue')
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Old: if (!q.qid || q.type === 'info') continue;
    # New: if (!q.qid || q.type === 'info' || q.continueOnly === true) continue;
    content = content.replace("if (!q.qid || q.type === 'info') continue;", "if (!q.qid || q.type === 'info' || q.continueOnly === true) continue;")

    with open(filepath, 'w') as f:
        f.write(content)

