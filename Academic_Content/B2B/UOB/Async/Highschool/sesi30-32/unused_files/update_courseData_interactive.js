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
            title: "Kuis Kilat: Sanitasi vs Validasi ⚖️",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Kuis Kilat: Manakah yang termasuk tindakan VALIDASI?</h3>
                </div>
              </div>
            `,
            choices: [
              "Mengubah input 'PENGELUARAN' menjadi 'pengeluaran'",
              "Memastikan nominal tidak boleh negatif (<= 0)",
              "Membuang spasi kosong di depan dan belakang kata"
            ],
            correct: "Memastikan nominal tidak boleh negatif (<= 0)",
            explanation: "Memastikan nominal negatif adalah pengecekan aturan (Validasi), sedangkan sisanya mengubah format data (Sanitasi)."
          }
        ]
      },
      {
        time: 1600,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Project: Safe Transaction Input 🛡️",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Project: Safe Transaction Input 🛡️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Sekarang, saatnya kamu membuat program pencatatan transaksi yang aman dan anti-kotor!</p>
                <div style="background-color: rgba(0, 198, 255, 0.15); border: 4px solid var(--black); padding: 25px; border-radius: 16px; box-shadow: 6px 6px 0px var(--black); margin: 20px 0;">
                    <h3 style="margin-bottom: 10px; font-size: 20px;">Aturan Program:</h3>
                    <ol style="padding-left: 25px; font-size: 18px; line-height: 1.6;">
                        <li>Minta input nama transaksi (tolak jika kosong).</li>
                        <li>Minta jenis transaksi (hanya boleh "pemasukan" atau "pengeluaran").</li>
                        <li>Minta nominal (harus lebih besar dari 0).</li>
                        <li>Jika terjadi kesalahan, beri pesan error yang spesifik dan batalkan transaksi.</li>
                        <li>Gunakan function untuk membantu sanitasi dan validasi.</li>
                    </ol>
                </div>
              </div>
            `,
            choices: ["Siap Mengerjakan!"],
            correct: "Siap Mengerjakan!",
            explanation: "Semangat coding-nya!"
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
            type: "input",
            title: "Latihan: Lengkapi Blok `try-except` 🧩",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Latihan: Lengkapi Blok \`try-except\` 🧩</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Ketik potongan kode yang harus mengisi bagian kuning di bawah ini:</p>
                <div class="code-block" style="background-color: #1a1a1a; padding: 24px; border-radius: 16px; font-family: 'Courier New', Courier, monospace; font-size: 16px; margin-bottom: 24px; border: 3px solid #ffe600; box-shadow: 4px 4px 0px #ffe600; color: #f8f8f2; line-height: 1.6; font-weight: bold; text-align: left;">
<span style="color: #ff79c6;">try</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;amount <span style="color: #ff79c6;">=</span> <span style="color: #8be9fd;">int</span>(<span style="color: #8be9fd;">input</span>(<span style="color: #f1fa8c;">"Nominal: "</span>))<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #8be9fd;">print</span>(amount)<br>
<span style="color: #ff79c6;">except</span> <span style="background-color: #ffe600; color: #1a1a1a; padding: 2px 10px; border-radius: 4px;">____________________</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #8be9fd;">print</span>(<span style="color: #f1fa8c;">"Nominal harus berupa angka."</span>)
                </div>
              </div>
            `,
            correct: ["ValueError", "valueerror"],
            explanation: "Benar! ValueError digunakan untuk menangkap error karena isi datanya tidak sesuai (misal: huruf diubah ke angka)."
          }
        ]
      },
      {
        time: 2310,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Project: Safe Input with Error Handling 🛡️",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Project: Safe Input with Error Handling 🛡️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Gabungkan Sanitasi, Validasi, dan Error Handling!</p>
                <div style="background-color: rgba(0, 198, 255, 0.15); border: 4px solid var(--black); padding: 25px; border-radius: 16px; box-shadow: 6px 6px 0px var(--black); margin: 20px 0;">
                    <ul style="padding-left: 25px; font-size: 18px; line-height: 1.6;">
                        <li>Ambil program dari Mini Project pertama.</li>
                        <li>Gunakan blok <code>try-except</code> di sekitar input <code>amount = int(input(...))</code>.</li>
                        <li>Tangkap <code>ValueError</code> jika input pengguna tidak bisa diubah ke angka (misal huruf).</li>
                        <li>Cetak pesan: "Error: Nominal harus berupa angka bulat!"</li>
                    </ul>
                </div>
              </div>
            `,
            choices: ["Siap Mengerjakan!"],
            correct: "Siap Mengerjakan!",
            explanation: "Luar biasa!"
          }
        ]
      },
      {
        time: 2972,
        resume: false,
        questions: [
          {
            type: "input",
            title: "Latihan: Temukan Bug! 🔎🐛",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Latihan: Temukan Bug! 🔎🐛</h3>
                </div>
                <p style="font-size: 18px; margin-bottom: 15px;">Kamu melacak hasil <code style="background-color: #E0E0E0; padding: 3px 6px; border-radius: 4px;">print</code> pada setiap function dan mendapati hasil ini:</p>
                <ul style="font-size: 18px; margin-bottom: 20px;">
                    <li><code>get_total()</code> mencetak <strong>150000</strong> (Benar)</li>
                    <li><code>get_discount()</code> mencetak <strong>0</strong> (Salah, harusnya dapat diskon)</li>
                    <li><code>get_final_price()</code> mencetak <strong>150000</strong> (Salah karena diskonnya 0)</li>
                </ul>
                <p style="font-size: 18px; font-weight: bold;">Ketik nama function tempat letak sumber masalah (bug) yang harus kamu perbaiki!</p>
              </div>
            `,
            correct: ["get_discount", "get_discount()", "get discount"],
            explanation: "Tepat sekali! Karena error berawal dari get_discount yang mengembalikan 0."
          }
        ]
      },
      {
        time: 2980,
        resume: false,
        questions: [
          {
            type: "input",
            title: "Latihan: Perbaiki Nilai Diskon 🛠️",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Latihan: Perbaiki Nilai Diskon 🛠️</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Ternyata programmer salah menulis nilai diskon 10% menjadi <code style="background-color: #E0E0E0; padding: 3px 6px; border-radius: 4px; color:#000;">10</code>, padahal dalam program yang menggunakan desimal, itu membuat perhitungannya error!</p>
                <p style="font-size: 18px;">Ketik angka desimal yang benar untuk mewakili diskon 10%:</p>
              </div>
            `,
            correct: ["0.1", "0.10", ".1"],
            explanation: "Mantap! 10% sama dengan 10/100 alias 0.1 di Python."
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
            type: "input",
            title: "Latihan: Tebak Output Dictionary 🧩",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Latihan: Tebak Output Dictionary 🧩</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Perhatikan kode berikut:</p>
                <div class="code-block" style="background-color: #1a1a1a; padding: 24px; border-radius: 16px; font-family: 'Courier New', Courier, monospace; font-size: 16px; margin-bottom: 24px; border: 3px solid #ffe600; box-shadow: 4px 4px 0px #ffe600; color: #f8f8f2; line-height: 1.6; font-weight: bold; text-align: left;">
<span style="color: #f8f8f2;">transaction = {</span><br>
<span style="color: #f8f8f2;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #f1fa8c;">"name"</span><span style="color: #f8f8f2;">: </span><span style="color: #f1fa8c;">"Beli snack"</span><span style="color: #f8f8f2;">,</span><br>
<span style="color: #f8f8f2;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #f1fa8c;">"type"</span><span style="color: #f8f8f2;">: </span><span style="color: #f1fa8c;">"pengeluaran"</span><span style="color: #f8f8f2;">,</span><br>
<span style="color: #f8f8f2;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #f1fa8c;">"amount"</span><span style="color: #f8f8f2;">: </span><span style="color: #bd93f9;">10000</span><br>
<span style="color: #f8f8f2;">}</span><br><br>
<span style="color: #8be9fd;">print</span><span style="color: #f8f8f2;">(transaction[</span><span style="color: #f1fa8c;">"amount"</span><span style="color: #f8f8f2;">])</span>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Ketik nilai output yang akan dicetak oleh kode di atas:</p>
              </div>
            `,
            correct: ["10000", "10.000", "'10000'", '"10000"'],
            explanation: "Benar sekali! Karena kita meminta data 'amount', yang dikembalikan adalah 10000."
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
            type: "input",
            title: "Latihan: Menghitung Total Pemasukan 📊",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #ffe600; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Latihan Statistik 📊</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Jika diketahui expenses = [12000, 18000, 25000, 10000, 15000]</p>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Berapa jumlah Totalnya?</p>
              </div>
            `,
            correct: ["80000", "80.000"],
            explanation: "Tepat sekali! Totalnya adalah 80.000."
          }
        ]
      },
      {
        time: 4425,
        resume: false,
        questions: [
          {
            type: "custom",
            title: "Mini Project: Financial Data Analyzer 📊🔍",
            html: `
              <div style="text-align: left; font-family: 'Outfit', sans-serif;">
                <div style="display: inline-block; background-color: #00c6ff; padding: 10px 24px; border-radius: 12px; border: 3px solid #1a1a1a; box-shadow: 4px 4px 0px #1a1a1a; margin-bottom: 24px; margin-top: 10px;">
                  <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #1a1a1a;">Mini Project: Financial Data Analyzer 📊🔍</h3>
                </div>
                <p style="font-weight: 800; font-size: 18px; color: #1a1a1a; margin-bottom: 16px;">Buat program penganalisis data pengeluaran sederhana.</p>
                <div style="background-color: rgba(0, 198, 255, 0.15); border: 4px solid var(--black); padding: 25px; border-radius: 16px; box-shadow: 6px 6px 0px var(--black); margin: 20px 0;">
                    <ul style="padding-left: 25px; font-size: 18px; line-height: 1.6;">
                        <li>Menerima list data pengeluaran <code>expenses = [20000, 15000, 10000, 30000, 5000]</code>.</li>
                        <li>Menghitung total, nilai terbesar, terkecil, dan rata-rata.</li>
                        <li>Menampilkan kesimpulan otomatis: jika rata-rata pengeluaran > 20000, print "Pengeluaran tinggi", jika tidak print "Pengeluaran aman".</li>
                    </ul>
                </div>
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
