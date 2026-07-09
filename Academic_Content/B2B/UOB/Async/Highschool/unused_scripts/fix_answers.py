import re

with open('sesi40-44/grup-hs-2-d/src/App.vue', 'r') as f:
    content = f.read()

# Fix submitMatchPairs
content = content.replace(
'''  if (isCorrect) {
    quizState.value.choicesDisabled = true;
    quizState.value.quizFeedbackType = 'success';
    quizState.value.quizFeedback = "Luar biasa! Semua fitur terpasang dengan tepat.";
    revealQuizNext();
  }''',
'''  if (isCorrect) {
    quizState.value.choicesDisabled = true;
    quizState.value.quizFeedbackType = 'success';
    quizState.value.quizFeedback = "Luar biasa! Semua fitur terpasang dengan tepat.";
    studentProgress.value[`${item.qid}_Ans`] = JSON.stringify(matchPairsAnswers.value);
    studentProgress.value[`${item.qid}_Failed`] = false;
    localStorage.setItem('mds_student_progress', JSON.stringify(studentProgress.value));
    revealQuizNext();
  }''')

# Let's check others by printing them!
