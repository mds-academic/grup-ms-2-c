const fs = require('fs');

const files = [
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi27-29/grup-hs-2-b/src/App.vue',
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi25-26/grup-hs-2-a/src/App.vue',
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi30-32/hrup-hs-2-c/src/App.vue'
];

for (const file of files) {
  if (fs.existsSync(file)) {
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace the button class="video-center-play" with both the button and the spinner
    content = content.replace(
      /<button class="video-center-play" type="button" v-show="!playerStates\[(\d+)\]\?\.isPlaying" @click="togglePlay\(\1\)">▶<\/button>/g,
      `<button class="video-center-play" type="button" v-show="!playerStates[$1]?.isPlaying && !playerStates[$1]?.isBuffering && (playerStates[$1]?.isReady || !playerStates[$1]?.hasStarted)" @click="togglePlay($1)">▶</button>
            <div class="video-loading-overlay" v-show="playerStates[$1]?.isBuffering || (playerStates[$1]?.hasStarted && !playerStates[$1]?.isReady)">
              <div class="spinner"></div>
            </div>`
    );

    fs.writeFileSync(file, content);
  }
}
console.log("Template Patched!");
