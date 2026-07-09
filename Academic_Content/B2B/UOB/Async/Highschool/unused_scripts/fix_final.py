import re
import os

repos = [
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

for repo in repos:
    filepath = os.path.join(repo, 'src', 'App.vue')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl_video(m):
        var_str = m.group(1)
        return f'''<video 
              v-show="playerStates[{var_str}]?.introPlaying"
              :ref="(el) => {{ if (el) introRefs[{var_str}] = el; }}"
              :src="introVideoSrc"
              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 10; background: black;"
              controls
              @ended="onIntroEnded({var_str})"
              @play="onIntroPlay({var_str})"
              @pause="onIntroPause({var_str})"
              playsinline
              preload="auto"
            ></video>'''
            
    content = re.sub(r'<video\s+v-show="playerStates\[([^\]]+)\]\?\.introPlaying"[\s\S]*?</video>', repl_video, content)
    
    if 'playIntroThenVideo(stepId)' not in content:
        content = re.sub(
            r'const togglePlay = \(stepId\) => \{', 
            r'const togglePlay = (stepId) => {\n  if (playerStates.value[stepId] && !introPlayed.value[stepId]) {\n    playIntroThenVideo(stepId);\n    return;\n  }', 
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {repo}")

