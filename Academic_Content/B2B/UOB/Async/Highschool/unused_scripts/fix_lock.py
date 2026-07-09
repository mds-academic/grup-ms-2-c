import os
import re

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

    # Restore goToStep
    go_to_step_pattern = r'const goToStep = \(step\) => \{\n\s*currentStep\.value = step;\n\};'
    go_to_step_replacement = '''const goToStep = (step) => {
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
};'''
    content = re.sub(go_to_step_pattern, go_to_step_replacement, content)
    
    # Restore nextStep
    next_step_pattern = r'const nextStep = \(\) => \{\n\s*if \(currentStep\.value < totalSteps\) \{'
    next_step_replacement = '''const nextStep = () => {
  if (!isStepFinished(currentStep.value)) {
    alert(`Mohon selesaikan video dan kuis/tugas di modul ini terlebih dahulu.`);
    return;
  }

  if (currentStep.value < totalSteps) {'''
    content = re.sub(next_step_pattern, next_step_replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {repo}")

