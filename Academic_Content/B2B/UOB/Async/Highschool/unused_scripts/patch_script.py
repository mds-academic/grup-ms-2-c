import os
import re

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

# Function to patch a repo
def patch_repo(repo_path):
    app_vue_path = os.path.join(repo_path, 'src/App.vue')
    if not os.path.exists(app_vue_path):
        return
    with open(app_vue_path, 'r') as f:
        content = f.read()

    # 1. Replace isStepFinished logic
    # Find the block and replace the condition
    content = re.sub(
        r"ans === undefined \|\|\s*ans === null \|\|\s*ans === '' \|\|\s*ans === '-' \|\|\s*ans === '0' \|\|\s*studentProgress\.value\[`\${q\.qid}_Failed`\] === true",
        r"ans === undefined ||\n          ans === null ||\n          ans === ''",
        content
    )
    
    # In some repos, it might be simpler:
    content = re.sub(
        r"ans === undefined \|\|\s*ans === null \|\|\s*ans === '' \|\|\s*ans === '-' \|\|\s*ans === '0'",
        r"ans === undefined ||\n          ans === null ||\n          ans === ''",
        content
    )

    # 2. Patch registerFailedInputAttempt (custom inputs)
    old_register = r"""const registerFailedInputAttempt = \(btn, feedback\) => \{
\s*const qid = currentQuestion\.value\?\.qid;
\s*const attempts = qid \? studentProgress\.value\[`\${qid}_Att`\] \|\| 1 : 1;
\s*if \(attempts >= 3\) \{
\s*markQuestionFailed\(qid\);
\s*feedback\.innerHTML \+= `<br><strong>Sudah 3 kali mencoba\.</strong> Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci\.`;
\s*\} else \{
\s*buttons\.forEach\(b => \{
\s*b\.disabled = false;
\s*b\.style\.opacity = '1';
\s*\}\);
\s*\}
\};"""
    new_register = """const registerFailedInputAttempt = (btn, feedback) => {
    const qid = currentQuestion.value?.qid;
    const attempts = qid ? studentProgress.value[`${qid}_Att`] || 1 : 1;
    if (attempts >= 3) {
      markQuestionFailed(qid);
      feedback.innerHTML = `❌ <strong>Kesempatan habis.</strong> Lain kali perhatikan video ya.`;
      revealQuizNext();
    } else {
      let remaining = 3 - attempts;
      feedback.innerHTML += `<br><em>Sisa ${remaining} kesempatan.</em>`;
      // We don't enable buttons because this is an inline input, the user can just type again.
    }
  };"""
    # Wait, the old register doesn't exactly match. I will use regex properly.
    
    with open(app_vue_path, 'w') as f:
        f.write(content)

for repo in repos:
    patch_repo(repo)

