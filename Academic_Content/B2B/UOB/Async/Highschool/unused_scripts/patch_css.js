const fs = require('fs');

const files = [
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi27-29/grup-hs-2-b/src/style.css',
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi25-26/grup-hs-2-a/src/style.css',
  '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi30-32/hrup-hs-2-c/src/style.css'
];

const cssToAdd = `
.video-loading-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 3;
  width: 88px;
  height: 72px;
  display: grid;
  place-items: center;
  background: var(--blue);
  border: 4px solid var(--ink);
  border-radius: 20px;
  box-shadow: 7px 7px 0 var(--yellow);
  transform: translate(-50%, -50%);
}

.spinner {
  width: 32px;
  height: 32px;
  border: 4px solid var(--light);
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  100% { transform: rotate(360deg); }
}
`;

for (const file of files) {
  if (fs.existsSync(file)) {
    let content = fs.readFileSync(file, 'utf8');
    if (!content.includes('.video-loading-overlay')) {
      content += cssToAdd;
      fs.writeFileSync(file, content);
    }
  }
}
console.log("CSS Patched!");
