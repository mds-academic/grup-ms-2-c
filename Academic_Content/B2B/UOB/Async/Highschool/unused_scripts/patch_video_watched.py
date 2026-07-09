import os
import re

directories = [
    "../sesi25-26/grup-hs-2-a/src",
    "../sesi27-29/grup-hs-2-b/src",
    "../sesi30-32/grup-hs-2-c/src",
    "../sesi40-44/grup-hs-2-d/src"
]

for d in directories:
    app_vue_path = os.path.join(d, "App.vue")
    if not os.path.exists(app_vue_path):
        continue
    
    with open(app_vue_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update enforceVideoEndBoundary
    if 'videoWatchedStatus.value[stepId] = true;' not in content.split('const enforceVideoEndBoundary')[1].split('}')[0]:
        content = re.sub(
            r'(const enforceVideoEndBoundary\s*=\s*\(stepId\)\s*=>\s*{[^}]+?if\s*\([^)]+\)\s*{)',
            r'\1\n    videoWatchedStatus.value[stepId] = true;',
            content,
            count=1
        )
    
    # 2. Update updateVideoControls
    # Look for: playerStates.value[stepId].currentTimeFormatted = formatVideoTime(currentTime);
    if 'if (playerStates.value[stepId].progress >= 98)' not in content:
        replacement = """  playerStates.value[stepId].currentTimeFormatted = formatVideoTime(currentTime);

  if (playerStates.value[stepId].progress >= 98) {
    videoWatchedStatus.value[stepId] = true;
  }"""
        content = content.replace("  playerStates.value[stepId].currentTimeFormatted = formatVideoTime(currentTime);", replacement)
    
    with open(app_vue_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated {app_vue_path}")
