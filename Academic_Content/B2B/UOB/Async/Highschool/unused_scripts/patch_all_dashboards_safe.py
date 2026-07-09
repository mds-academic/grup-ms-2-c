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
        
    # 1. Update isStepFinished
    is_step_finished_regex = r'const isStepFinished = \(stepId\) => \{.*?\n\};'
    new_is_step_finished = """const isStepFinished = (stepId) => {
  if (courseData[stepId]?.videoId) {
    if (!videoWatchedStatus.value[stepId]) return false;
  }

  const stepQuizzes = courseData[stepId]?.quizzes;
  if (stepQuizzes && stepQuizzes.length > 0) {
    for (let quiz of stepQuizzes) {
      for (let q of quiz.questions) {
        if (!q.qid) continue;
        const ans = studentProgress.value[`${q.qid}_Ans`];
        if (
          ans === undefined ||
          ans === null ||
          ans === '' ||
          ans === '-' ||
          ans === '0' ||
          studentProgress.value[`${q.qid}_Failed`] === true
        ) return false;
      }
    }
  }

  return true;
};"""
    content = re.sub(is_step_finished_regex, new_is_step_finished, content, flags=re.DOTALL)
    
    # 2. Modify goToStep, handleStepSelect, prevStep, nextStep
    nav_functions = """const goToStep = (step) => {
  if (step <= currentStep.value) {
    currentStep.value = step;
    return;
  }
  for (let i = 1; i < step; i++) {
    if (!isStepFinished(i)) {
      alert(`Mohon selesaikan video dan kuis/tugas di Modul ${i} terlebih dahulu.`);
      return;
    }
  }
  currentStep.value = step;
};

const handleStepSelect = (event) => {
  const requestedStep = Number(event.target.value);
  goToStep(requestedStep);
  event.target.value = String(currentStep.value);
};

const prevStep = () => {
  if (currentStep.value > 1) {
    currentStep.value--;
  }
};

const nextStep = () => {
  if (!isStepFinished(currentStep.value)) {
    alert(`Mohon selesaikan video dan kuis/tugas di modul ini terlebih dahulu.`);
    return;
  }
  if (currentStep.value < Object.keys(courseData).length) {
    currentStep.value++;
  }
};"""
    
    # Remove existing prevStep and nextStep
    content = re.sub(r'const prevStep = \(\) => \{.*?\n\};\n*', '', content, flags=re.DOTALL)
    content = re.sub(r'const nextStep = \(\) => \{.*?\n\};\n*', '', content, flags=re.DOTALL)
    content = re.sub(r'const goToStep = \(\w+\) => \{.*?\n\};\n*', '', content, flags=re.DOTALL)
    content = re.sub(r'const handleStepSelect = \(\w+\) => \{.*?\n\};\n*', '', content, flags=re.DOTALL)
    
    # Insert new nav functions right after isStepFinished
    content = content.replace(new_is_step_finished, new_is_step_finished + "\n\n" + nav_functions)
    
    # 3. Update template navigation elements
    content = content.replace('v-model="currentStep"', ':value="currentStep" @change="handleStepSelect"')
    content = re.sub(r'@click="currentStep\s*=\s*Number\(key\)"', '@click="goToStep(Number(key))"', content)
    content = re.sub(r'@click="currentStep\s*--"', '@click="prevStep()"', content)
    content = re.sub(r'@click="currentStep\s*\+\+"', '@click="nextStep()"', content)
    
    # 4. Remove revealQuizNext from markQuestionFailed
    content = re.sub(r'(syncToSheets\(\);)\s*revealQuizNext\(\);', r'\1', content)
    
    # 5. Replace explicit strings
    target_text = 'quizState.value.quizFeedback = "Sudah 3 kali salah. Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";'
    
    replacements = [
        'quizState.value.quizFeedback = "Sudah 3 kali mencoba. Kamu boleh lanjut dulu, tapi perhatikan lagi videonya sebelum masuk ke bagian berikutnya.";',
        'quizState.value.quizFeedback = "Sudah 3 kali salah. Jawabanmu masih belum tepat, tapi tidak apa-apa. Untuk sekarang kamu boleh lanjut dulu!";',
        'quizState.value.quizFeedback = "Sudah 3 kali mencoba. Urutannya masih belum tepat. Boleh lanjut dulu!";',
        'quizState.value.quizFeedback = "Sudah 3 kali salah. Ada yang kurang pas dengan kebutuhan user. Boleh lanjut dulu!";',
        'quizState.value.quizFeedback = "Sudah 3 kali salah kamar. Tidak apa-apa, ayo coba pertanyaan bagian kedua!";',
        'quizState.value.quizFeedback = "Sudah 3 kali salah. Kalimat masalah belum tepat. Boleh lanjut dulu!";'
    ]
    
    for r in replacements:
        content = content.replace(r, target_text)

    # 6. Remove revealQuizNext from failure blocks
    content = content.replace('revealQuizNext("Lanjut dulu →");', '')
    content = content.replace("revealQuizNext('Lanjut dulu →');", '')
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Patched strictly in {repo}")
