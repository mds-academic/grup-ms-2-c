import re

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    content = f.read()

# Replace the setTimeout block in submitFeasibilityBuckets
bad_block = """      if (attempts >= 3) {
        quizState.value.choicesDisabled = true;
        markQuestionFailed(item.qid);
        quizState.value.quizFeedback = "Sudah 3 kali salah. Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";
        setTimeout(() => {
          isFeasibilityFollowUp.value = true;
          quizState.value.quizFeedback = "";
          quizState.value.quizFeedbackType = "";
        }, 2500);
      }"""

good_block = """      if (attempts >= 3) {
        quizState.value.choicesDisabled = true;
        markQuestionFailed(item.qid);
        quizState.value.quizFeedback = "Sudah 3 kali salah. Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";
      }"""

# Actually, the string replacement in previous script might not have added choicesDisabled and markQuestionFailed!
# Let's just do a regex replace to make it exactly what the user had.
content = re.sub(
    r'if\s*\(attempts\s*>=\s*3\)\s*\{\s*quizState\.value\.quizFeedback\s*=\s*"Sudah 3 kali salah.*?modul berikutnya tetap terkunci\.";\s*setTimeout\(\(\)\s*=>\s*\{\s*isFeasibilityFollowUp\.value\s*=\s*true;\s*quizState\.value\.quizFeedback\s*=\s*"";\s*quizState\.value\.quizFeedbackType\s*=\s*"";\s*\},\s*2500\);\s*\}',
    r'if (attempts >= 3) {\n        quizState.value.choicesDisabled = true;\n        markQuestionFailed(item.qid);\n        quizState.value.quizFeedback = "Sudah 3 kali salah. Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";\n      }',
    content,
    flags=re.DOTALL
)

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'w') as f:
    f.write(content)
