import re
import os

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = os.path.join(repo, 'src', 'App.vue')
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_block = """  quizState.value.quizFeedbackType = isCorrect ? 'correct' : 'wrong';
  quizState.value.quizFeedback = feedbackText;
  recordQuestionAttempt(item.qid, input, isCorrect);

  if (isCorrect) {
    quizState.value.choicesDisabled = true;
    revealQuizNext();
  } else {
    // Biarkan tetap bisa mengisi lagi jika salah
    quizState.value.choicesDisabled = false;
  }"""

    new_block = """  quizState.value.quizFeedbackType = isCorrect ? 'correct' : 'wrong';
  recordQuestionAttempt(item.qid, input, isCorrect);
  const attempts = studentProgress.value[item.qid + "_Att"] || 1;

  if (isCorrect) {
    quizState.value.quizFeedback = feedbackText;
    quizState.value.choicesDisabled = true;
    revealQuizNext();
  } else {
    if (attempts >= 3) {
      quizState.value.quizFeedback = "Sudah 3 kali salah. Jawabanmu masih belum tepat, tapi tidak apa-apa. Untuk sekarang kamu boleh lanjut dulu!";
      quizState.value.choicesDisabled = true;
      studentProgress.value[item.qid + "_Ans"] = '-';
      revealQuizNext("Lanjut dulu →");
    } else {
      quizState.value.quizFeedback = feedbackText + ` (Percobaan ${attempts}/3)`;
      quizState.value.choicesDisabled = false;
    }
  }"""

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {repo}")
    else:
        print(f"Old block not found in {repo}")

