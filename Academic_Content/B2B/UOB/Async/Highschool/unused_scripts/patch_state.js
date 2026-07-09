const fs = require('fs');

const files = [
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi27-29/grup-hs-2-b/src/App.vue',
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi25-26/grup-hs-2-a/src/App.vue',
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi30-32/hrup-hs-2-c/src/App.vue'
];

for (const file of files) {
  if (fs.existsSync(file)) {
    let content = fs.readFileSync(file, 'utf8');
    
    // Add isBuffering state logic
    content = content.replace(
      'const isPlaying = event.data === window.YT.PlayerState.PLAYING;',
      'const isPlaying = event.data === window.YT.PlayerState.PLAYING;\n  const isBuffering = event.data === window.YT.PlayerState.BUFFERING;\n  playerStates.value[stepId].isBuffering = isBuffering;'
    );
    
    // Add hd1080 playerVars
    if (!content.includes("vq: 'hd1080'")) {
      content = content.replace(
        'controls: 0,',
        "controls: 0,\n      vq: 'hd1080',"
      );
    }
    
    // Set playback quality on ready just in case
    content = content.replace(
      'enforceVideoBoundaries(normalizedStepId);',
      "event.target.setPlaybackQuality('hd1080');\n        enforceVideoBoundaries(normalizedStepId);"
    );

    fs.writeFileSync(file, content);
  }
}
console.log("Patched!");
