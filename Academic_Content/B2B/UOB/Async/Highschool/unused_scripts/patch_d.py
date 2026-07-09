import re

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    content = f.read()

# 1. Patch isStepFinished
content = re.sub(
    r"ans === undefined \|\|\s*ans === null \|\|\s*ans === '' \|\|\s*ans === '-' \|\|\s*ans === '0' \|\|\s*studentProgress\.value\[`\${q\.qid}_Failed`\] === true",
    r"ans === undefined ||\n          ans === null ||\n          ans === ''",
    content
)

# 2. Patch submitMatchPairs, submitClassifyProblem, submitFeasibilityBuckets, submitOrderAnswers
# I will just replace the "Sudah 3 kali salah/mencoba" strings.
content = re.sub(
    r'"Sudah 3 kali mencoba\. Kamu boleh lanjut dulu, tapi perhatikan lagi videonya sebelum masuk ke bagian berikutnya\."',
    r'"❌ Jawaban salah. Kesempatan habis. Lain kali perhatikan video ya."',
    content
)
content = re.sub(
    r'"Tepat sekali! Kamu menyusun kalimat masalah dengan sempurna\."',
    r'"✅ Luar biasa! Semua urutan sudah benar."',
    content
)

# Replace the "Percobaan X/3" with "Sisa N kesempatan"
def repl_feedback(m):
    return r'let remaining = 3 - attempts; quizState.value.quizFeedback = `❌ Jawaban salah. Sisa ${remaining} kesempatan.`;'

content = re.sub(
    r'quizState\.value\.quizFeedback = `.*?\(Percobaan \$\{attempts\}/3\)`\s*;',
    repl_feedback,
    content
)

# 3. Patch registerFailedInputAttempt
content = re.sub(
    r'attemptStatus\.innerHTML = "<strong>Sudah 3 kali mencoba\.</strong><br>Kamu boleh lanjut dulu\. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya\.";',
    r'attemptStatus.innerHTML = "❌ <strong>Kesempatan habis.</strong> Lain kali perhatikan video ya.";',
    content
)
content = re.sub(
    r'attemptStatus\.textContent = `Percobaan \$\{attempts\} dari 3\. Periksa kembali kode atau jawabanmu sebelum mencoba lagi\.`;',
    r'let remaining = 3 - attempts; attemptStatus.innerHTML = `❌ Jawaban salah. Sisa ${remaining} kesempatan.`;',
    content
)

# 4. Patch window.checkGuess
content = re.sub(
    r'const attempts = qid \? studentProgress\.value\[`\${qid}_Att`\] \|\| 1 : 1;\s*if \(attempts >= 3\) \{\s*markQuestionFailed\(qid\);\s*feedback\.innerHTML \+= `<br><strong>Sudah 3 kali mencoba\.</strong> Kamu boleh lanjut dulu\. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya\.`;\s*\} else \{\s*buttons\.forEach\(b => \{\s*b\.disabled = false;\s*b\.style\.opacity = \'1\';\s*\}\);\s*\}',
    r'markQuestionFailed(qid);\n      revealQuizNext();',
    content
)

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'w') as f:
    f.write(content)

