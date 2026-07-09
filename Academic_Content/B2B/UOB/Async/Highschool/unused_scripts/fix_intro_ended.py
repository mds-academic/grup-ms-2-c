import re
import os

repos = [
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = os.path.join(repo, 'src', 'App.vue')
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace the bad onIntroEnded logic
    old_logic = """const onIntroEnded = (stepId) => {
  introPlayed.value[stepId] = true;
  playerStates.value[stepId].introPlaying = false;
  
  const p = players.value[stepId];
  if (p && typeof p.playVideo === 'function') {
    p.playVideo();
  } else {
    pendingPlay.value[stepId] = true;
    initYouTubePlayer(stepId);
  }
};"""

    new_logic = """const onIntroEnded = (stepId) => {
  playerStates.value[stepId].introPlaying = false;
  introPlayed.value[stepId] = true;
  
  const player = players[stepId];
  if (!player || typeof player.getPlayerState !== "function") {
    initializeYouTubePlayer(stepId);
    setTimeout(() => {
      if (players[stepId] && typeof players[stepId].playVideo === 'function') {
         players[stepId].playVideo();
      }
    }, 500);
  } else {
    player.playVideo();
  }
};"""

    if old_logic in content:
        content = content.replace(old_logic, new_logic)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {repo}")
    else:
        print(f"Old logic not found in {repo}")

