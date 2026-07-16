import puppeteer from 'puppeteer';
import fs from 'fs';

const titles = [
  "Membuat dan Memanggil Procedures",
  "Mini Project Kalkulator",
  "Optimasi dan Modularisasi Kode",
  "Uji Coba dan Debugging",
  "Presentasi dan Refleksi",
  "Merancang Solusi Digital",
  "Brainstorming Ide Aplikasi"
];

const generateHtml = (index, title) => `
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1280, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --yellow: #FFE500;
            --blue: #00C6FF;
            --black: #1A1A1A;
            --white: #FFFFFF;
            --bg-light: #E8E8E8;
        }
        body {
            background-color: var(--bg-light);
            background-image: radial-gradient(#bcbcbc 2px, transparent 2px);
            background-size: 30px 30px;
            font-family: 'Fredoka', sans-serif;
            color: var(--black);
            width: 1280px;
            height: 720px;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .content-card {
            background-color: var(--white);
            border: 6px solid var(--black); 
            border-radius: 30px;
            padding: 60px 80px; 
            box-shadow: 16px 16px 0px var(--black);
            width: 80%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
            text-align: center;
        }
        .content-card::after {
            content: '';
            position: absolute;
            top: -20px; right: 40px;
            width: 60px; height: 60px;
            background-color: var(--yellow);
            border: 4px solid var(--black);
            border-radius: 50%;
            box-shadow: 6px 6px 0px var(--black);
        }
        .slide-kicker {
            background-color: var(--yellow); 
            color: var(--black); 
            padding: 10px 30px; 
            font-size: 24px; font-weight: 700;
            border: 4px solid var(--black);
            border-radius: 20px; 
            margin-bottom: 30px; 
            text-transform: uppercase; letter-spacing: 2px;
            box-shadow: 6px 6px 0px var(--black);
            display: inline-block;
        }
        .slide-title {
            font-size: 64px; font-weight: 700; color: var(--black); 
            line-height: 1.2;
            text-shadow: 3px 3px 0px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="content-card">
        <div class="slide-kicker">VIDEO ${index}</div>
        <h1 class="slide-title">${title}</h1>
    </div>
</body>
</html>
`;

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });

  for (let i = 0; i < titles.length; i++) {
    const html = generateHtml(i + 1, titles[i]);
    await page.setContent(html, { waitUntil: 'load' });
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({ path: "public/thumb_" + (i + 1) + ".png" });
    console.log("Saved thumb_" + (i + 1) + ".png");
  }

  await browser.close();
})();
