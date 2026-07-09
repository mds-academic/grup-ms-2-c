import os

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

    # We will search for:
    # playerStates.value[stepId].currentTimeFormatted = formatVideoTime(
    # Because sometimes it's formatVideoTime(currentTime) and sometimes formatVideoTime(playerStates.value[stepId].currentTime)
    
    lines = content.split('\n')
    new_lines = []
    already_patched = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        if 'if (playerStates.value[stepId].progress >= 95)' in line:
            already_patched = True
        
        if 'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(' in line and 'updateVideoControls' in content[:content.find(line)]:
            # Add our logic right after this line
            if not already_patched:
                new_lines.append("  if (playerStates.value[stepId].progress >= 95) {")
                new_lines.append("    videoWatchedStatus.value[stepId] = true;")
                new_lines.append("  }")
    
    # We should only add it once per file, but the check above should work if we just joined it
    # Wait, 'updateVideoControls' might appear multiple times or updateVideoControls is just a function.
    
    # Let's use a simpler regex or direct replacement.
    
    with open(app_vue_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if 'progress >= 95' not in content:
        # Find the end of updateVideoControls
        # We can just replace the line that formats the current time.
        if 'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(currentTime);' in content:
            content = content.replace(
                'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(currentTime);',
                'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(currentTime);\n  if (playerStates.value[stepId].progress >= 95) {\n    videoWatchedStatus.value[stepId] = true;\n  }'
            )
        elif 'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(playerStates.value[stepId].currentTime);' in content:
            content = content.replace(
                'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(playerStates.value[stepId].currentTime);',
                'playerStates.value[stepId].currentTimeFormatted = formatVideoTime(playerStates.value[stepId].currentTime);\n  if (playerStates.value[stepId].progress >= 95) {\n    videoWatchedStatus.value[stepId] = true;\n  }'
            )
            
        with open(app_vue_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {app_vue_path}")
    else:
        print(f"Already patched {app_vue_path}")
