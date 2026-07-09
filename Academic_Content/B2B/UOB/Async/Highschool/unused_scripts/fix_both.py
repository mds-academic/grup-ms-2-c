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

    # 1. Remove isStepFinished block from goToStep
    # goToStep looks like:
    # const goToStep = (step) => { ... for (let i = 1; i < step; i++) { if (!isStepFinished(i)) { ... } } ... }
    go_to_step_pattern = r'const goToStep = \(step\) => \{[\s\S]*?\n\s*currentStep\.value = step;\n\};'
    
    def repl_go_to_step(m):
        return '''const goToStep = (step) => {
  currentStep.value = step;
};'''
    content = re.sub(go_to_step_pattern, repl_go_to_step, content)
    
    # 2. Remove isStepFinished block from nextStep
    next_step_pattern = r'const nextStep = \(\) => \{[\s\S]*?if \(!isStepFinished\(currentStep\.value\)\) \{[\s\S]*?return;\n\s*\}[\s\S]*?if \(currentStep\.value < totalSteps\) \{'
    
    def repl_next_step(m):
        return '''const nextStep = () => {
  if (currentStep.value < totalSteps) {'''
    content = re.sub(next_step_pattern, repl_next_step, content)

    # 3. Reset intro state on video end
    if repo == 'sesi25-26/grup-hs-2-a':
        ended_pattern = r'if \(event\.data === window\.YT\.PlayerState\.ENDED\) \{[\s\S]*?return;\n\s*\}'
        ended_replacement = '''if (event.data === window.YT.PlayerState.ENDED) {
    videoWatchedStatus.value[stepId] = true;
    checkVideoQuizzes(stepId);
    
    restartVideoFromBoundary(stepId, false);
    
    introPlayed.value[stepId] = false;
    playerStates.value[stepId].hasStarted = false;
    playerStates.value[stepId].isPlaying = false;
    
    return;
  }'''
        content = re.sub(ended_pattern, ended_replacement, content)
    else:
        # B, C, D use enforceVideoBoundaries
        enforce_pattern = r'\} else if \(endBoundary > 0 && currentTime >= endBoundary\) \{[\s\S]*?\}'
        enforce_replacement = '''} else if (endBoundary > 0 && currentTime >= endBoundary - 0.5) {
    player.seekTo(startBoundary > 0 ? startBoundary : 0, true);
    player.pauseVideo();
    videoWatchedStatus.value[stepId] = true;
    
    introPlayed.value[stepId] = false;
    if (playerStates.value[stepId]) {
      playerStates.value[stepId].hasStarted = false;
      playerStates.value[stepId].isPlaying = false;
    }
  }'''
        content = re.sub(enforce_pattern, enforce_replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {repo}")

