const fs = require('fs');

const data = {
  1: {
    kicker: "Materi 01",
    title: "Input, Masalah Input User, dan Konsep Validasi",
    duration: "12 Menit",
    videoId: "pKYN1E60xtU",
    startSeconds: 9,
    endSeconds: 756,
    bookmarks: [
      { time: 9, label: "Apa yang Akan Kita Pelajari? 🎯" },
      { time: 60, label: "Apa Itu Input? 📥" },
      { time: 180, label: "Input Pengguna Tidak Selalu Benar! 🤯" },
      { time: 300, label: "Apa Itu Validasi Input? 🚦" }
    ],
    quizzes: []
  },
  2: {
    kicker: "Materi 02",
    title: "Sanitasi & Validasi Input dalam Program Keuangan",
    duration: "15 Menit",
    videoId: "pKYN1E60xtU",
    startSeconds: 761,
    endSeconds: 1693,
    bookmarks: [
      { time: 761, label: "Validasi Input Kosong 📭" },
      { time: 900, label: "Validasi Jenis Transaksi 🔄" },
      { time: 1200, label: "Validasi Nominal 💸" },
      { time: 1500, label: "Mini Project: Safe Transaction 🛡️" }
    ],
    quizzes: [
      {
        time: 1584,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Quiz pemahaman Sanitasi & Validasi Input",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Quiz pemahaman Sanitasi & Validasi Input ⚖️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Waktunya kuis! Silakan perhatikan pertanyaan di layar video dan jawab untuk melanjutkan.</p>
              </div>
            `,
            choices: ["Saya sudah paham!"],
            correct: "Saya sudah paham!",
            explanation: "Mari kita lanjutkan belajarnya!"
          }
        ]
      },
      {
        time: 1600,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Task: Safe Transaction Input",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Task: Safe Transaction Input 🛡️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Saatnya praktik! Gunakan kode awal di video untuk membuat input transaksi yang aman.</p>
              </div>
            `,
            choices: ["Sudah saya kerjakan!"],
            correct: "Sudah saya kerjakan!",
            explanation: "Bagus! Terus semangat coding-nya."
          }
        ]
      }
    ]
  },
  3: {
    kicker: "Materi 03",
    title: "Try-Except dan Debugging Program Python",
    duration: "21 Menit",
    videoId: "pKYN1E60xtU",
    startSeconds: 1714,
    endSeconds: 2997,
    bookmarks: [
      { time: 1714, label: "Jenis Error yang Sering Muncul 🐛" },
      { time: 1900, label: "Mengenal Penyelamat: try-except 🛡️" },
      { time: 2200, label: "Debugging Bagaikan Memperbaiki Lampu 💡" },
      { time: 2600, label: "Cara Debugging Step-by-Step 🕵️‍♂️" }
    ],
    quizzes: [
      {
        time: 2298,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Quiz pemahaman Try-Except / Error Handling",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Quiz pemahaman Try-Except / Error Handling 🛡️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Perhatikan pertanyaan tentang Try-Except di layar video.</p>
              </div>
            `,
            choices: ["Saya sudah paham!"],
            correct: "Saya sudah paham!",
            explanation: "Lanjutkan!"
          }
        ]
      },
      {
        time: 2310,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Project: Input dengan sanitasi, validasi, try-except",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Project: Input dengan try-except 🛡️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Gabungkan semua yang sudah kamu pelajari untuk membuat input transaksi yang kebal error!</p>
              </div>
            `,
            choices: ["Sudah saya kerjakan!"],
            correct: "Sudah saya kerjakan!",
            explanation: "Luar biasa!"
          }
        ]
      },
      {
        time: 2972,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Quiz Debugging Python",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Quiz Debugging Python 🔎</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Tonton video dengan seksama dan pahami cara menemukan bug pada kode.</p>
              </div>
            `,
            choices: ["Lanjut!"],
            correct: "Lanjut!",
            explanation: "Sip!"
          }
        ]
      },
      {
        time: 2980,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Cari error pada kode debugging",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Latihan Cari Error 🛠️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Ayo coba temukan error pada kode belanja di video dan perbaiki!</p>
              </div>
            `,
            choices: ["Error sudah diperbaiki!"],
            correct: "Error sudah diperbaiki!",
            explanation: "Mantap!"
          }
        ]
      }
    ]
  },
  4: {
    kicker: "Materi 04",
    title: "Dictionary dan List Transaksi",
    duration: "15 Menit",
    videoId: "pKYN1E60xtU",
    startSeconds: 2998,
    endSeconds: 3897,
    bookmarks: [
      { time: 2998, label: "Apa Itu Dictionary di Python? 📖" },
      { time: 3200, label: "Menyimpan Banyak Transaksi 🗂️" },
      { time: 3500, label: "Menghitung Ringkasan Data 🧮" },
      { time: 3700, label: "Mini Project: Transaction Recorder 📝" }
    ],
    quizzes: [
      {
        time: 3893,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Quiz latihan Dictionary & List Transaction",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Quiz latihan Dictionary & List Transaction 📖</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Jawab quiz yang ada di video sebelum melanjutkan.</p>
              </div>
            `,
            choices: ["Saya sudah paham!"],
            correct: "Saya sudah paham!",
            explanation: "Hebat!"
          }
        ]
      }
    ]
  },
  5: {
    kicker: "Materi 05",
    title: "Analisis Data Keuangan dengan Python",
    duration: "9 Menit",
    videoId: "pKYN1E60xtU",
    startSeconds: 3932,
    endSeconds: 4473,
    bookmarks: [
      { time: 3932, label: "Dataset Pengeluaran Bulanan 📝" },
      { time: 4050, label: "Menghitung Total dengan sum() ➕" },
      { time: 4150, label: "Menganalisis Berdasarkan Kategori 📂" },
      { time: 4300, label: "10 Fitur Wajib Program 📋" }
    ],
    quizzes: [
      {
        time: 4406,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Quiz pemahaman Analisis Data Keuangan",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Quiz pemahaman Analisis Data Keuangan 📊</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Berapa total pemasukannya? Jawab kuis di video!</p>
              </div>
            `,
            choices: ["Saya sudah paham!"],
            correct: "Saya sudah paham!",
            explanation: "Yuk lanjut ke Final Project!"
          }
        ]
      },
      {
        time: 4425,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Project: Analisis expenses",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Project: Analisis expenses 💸</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Waktunya menerapkan semua hal yang dipelajari ke dalam Aplikasi Pencatat Transaksi yang lengkap!</p>
              </div>
            `,
            choices: ["Saya siap!"],
            correct: "Saya siap!",
            explanation: "Semangat ngerjain Mini Project-nya!"
          }
        ]
      }
    ]
  }
};

const output = `export const courseData = ${JSON.stringify(data, null, 2)};\n`;
fs.writeFileSync('/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi30-32/grup-hs-2-c/src/courseData.js', output);
console.log('courseData.js updated successfully.');
