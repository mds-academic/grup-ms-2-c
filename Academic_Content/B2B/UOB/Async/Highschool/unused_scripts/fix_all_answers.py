import re

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    content = f.read()

# 1. Fix submitOrderAnswers
content = re.sub(
r'''  if \(isCorrect\) \{\s*quizState\.value\.choicesDisabled = true;\s*quizState\.value\.quizFeedbackType = 'success';\s*quizState\.value\.quizFeedback = "Tepat sekali! Kamu menyusun kalimat masalah dengan sempurna\.";\s*revealQuizNext\(\);\s*\}''',
r'''  if (isCorrect) {
    quizState.value.choicesDisabled = true;
    quizState.value.quizFeedbackType = 'success';
    quizState.value.quizFeedback = "Tepat sekali! Kamu menyusun kalimat masalah dengan sempurna.";
    recordQuestionAttempt(item.qid, JSON.stringify(arrangeFlowAnswers.value), true);
    revealQuizNext();
  }''', content)

# 2. Fix submitMatchPairs
content = re.sub(
r'''  if \(isCorrect\) \{\s*quizState\.value\.choicesDisabled = true;\s*quizState\.value\.quizFeedbackType = 'success';\s*quizState\.value\.quizFeedback = "Luar biasa! Semua fitur terpasang dengan tepat\.";\s*revealQuizNext\(\);\s*\}''',
r'''  if (isCorrect) {
    quizState.value.choicesDisabled = true;
    quizState.value.quizFeedbackType = 'success';
    quizState.value.quizFeedback = "Luar biasa! Semua fitur terpasang dengan tepat.";
    recordQuestionAttempt(item.qid, JSON.stringify(matchPairsAnswers.value), true);
    revealQuizNext();
  }''', content)

# 3. Fix submitFeasibilityBuckets (Part 2)
content = re.sub(
r'''    if \(isCorrect\) \{\s*quizState\.value\.choicesDisabled = true;\s*quizState\.value\.quizFeedbackType = 'success';\s*quizState\.value\.quizFeedback = "Kalimat masalahmu sudah lengkap dan benar!";\s*revealQuizNext\(\);\s*\}''',
r'''    if (isCorrect) {
      quizState.value.choicesDisabled = true;
      quizState.value.quizFeedbackType = 'success';
      quizState.value.quizFeedback = "Kalimat masalahmu sudah lengkap dan benar!";
      recordQuestionAttempt(item.qid, JSON.stringify({p1: feasibilityAnswers.value, p2: arrangeFlowAnswers.value}), true);
      revealQuizNext();
    }''', content)

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'w') as f:
    f.write(content)

