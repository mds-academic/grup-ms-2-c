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
        
    # Inject <video> inside video-frame if not exists
    if '<video \n              v-show="playerStates' not in content:
        # We need to find what index variable is used: either a hardcoded number or a loop variable like 'key' or 'i'
        # Let's match: <div class="video-frame"[^>]*>
        # And inject the video tag right after it.
        def inject_video(match):
            full_match = match.group(0)
            # Find the loop variable or index from data-video-step="1" or :data-video-step="key"
            m = re.search(r'data-video-step="([^"]+)"', full_match)
            idx = m.group(1) if m else "1"
            
            # If idx is a number, we use it directly, else we use it as a variable
            if idx.isdigit():
                var_str = idx
            else:
                var_str = idx # usually 'key' or 'i'
                
            video_tag = f"""
            <video 
              v-show="playerStates[{var_str}]?.introPlaying"
              :src="introVideoSrc"
              class="intro-video"
              controls
              @ended="onIntroEnded({var_str})"
              @play="onIntroPlay({var_str})"
              @pause="onIntroPause({var_str})"
              preload="auto"
            ></video>"""
            
            # we want to append video_tag after the video-frame div opening tag
            return match.group(1) + video_tag + match.group(2)
            
        content = re.sub(r'(<div class="video-frame"[^>]*>)(.*?<div [^>]*youtube-player-[^>]*></div>)', inject_video, content, flags=re.DOTALL)
        
    # Fix the video-controls v-show
    # It might be `v-show="playerStates[key]?.hasStarted"`
    content = re.sub(r'(<div class="video-controls"\s+v-show="[^"]+playerStates\[([^\]]+)\]\?.hasStarted)(">)', r'\1 && !playerStates[\2]?.introPlaying\3', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {repo}")
