export const courseData = {
  1: {
    thumbnail: "./thumb_1.png",
    kicker: "Checkpoint 01 · Mulai di sini",
    title: "Membuat dan Memanggil Procedures",
    duration: "Video 1 · Konsep dasar",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 4,
    endSeconds: 794,
    bookmarks: [
      {"time": 10, "label": "Pengenalan Procedures"},
      {"time": 119, "label": "Kebiasaan buruk copy paste"},
      {"time": 286, "label": "Prosedur atau Function"},
      {"time": 442, "label": "Kategori Prosedur"},
      {"time": 541, "label": "Prosedur Do"},
      {"time": 696, "label": "Prosedur Result"},
      {"time": 803, "label": "Mini Project Kalkulator"}
    ],
    quizzes: [
      {
        time: 793,
        resumeTime: 794,
        skipTo: 794,
        title: "Mini Kuis 1 🧠",
        questions: [
          {
            qid: "V1_Q1",
            question: "Kenapa kita menggunakan Procedure di App Inventor?",
            options: [
              "Agar warna aplikasi menjadi lebih bagus.",
              "Untuk mengumpulkan beberapa perintah menjadi satu sehingga bisa dipakai berkali-kali tanpa mengulang.",
              "Untuk membuat baterai HP menjadi hemat 100%."
            ],
            answer: "Untuk mengumpulkan beberapa perintah menjadi satu sehingga bisa dipakai berkali-kali tanpa mengulang.",
            explanation: "Ini membuat kode kita tidak berulang-ulang, sehingga lebih ringan dan rapi."
          }
        ]
      }
    ],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 01</p>
          <h3>Membuat dan Memanggil Procedures</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Apa itu Procedure?</h4>
        <div class="slide-text">
          <p>Saat membuat aplikasi yang besar, ada blok kode yang <strong>sama persis</strong> dan digunakan berulang kali. Copy-Paste membuat aplikasi berat dan membingungkan.</p>
          <div class="quote-box">Solusinya? Kita menggunakan <strong>PROCEDURE</strong> (atau fungsi). Mengumpulkan perintah menjadi satu yang bisa dipanggil berkali-kali.</div>
        </div>
        <h4>Dua Jenis Procedure</h4>
        <div class="slide-text">
          <div class="info-grid">
            <div class="mini-card" style="background-color:#FCE4EC;">
              <h3>Procedure "Do" 🏃</h3>
              <p>Hanya menjalankan perintah tanpa hasil (misal: mengosongkan layar).</p>
            </div>
            <div class="mini-card" style="background-color:#E8F5E9;">
              <h3>Procedure "Result" 🎁</h3>
              <p>Melakukan perhitungan dan <strong>mengembalikan</strong> hasil/jawaban.</p>
            </div>
          </div>
        </div>
      </article>
    `
  },
  2: {
    thumbnail: "./thumb_2.png",
    kicker: "Checkpoint 02 · Mini Project",
    title: "Mini Project Kalkulator",
    duration: "Video 2 · Penjelasan Proyek",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 798,
    endSeconds: 879,
    bookmarks: [
      {"time": 798, "label": "Instruksi Mini Project"}
    ],
    quizzes: [],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Mini Project</p>
          <h3>Tugas Pertama: Kalkulator Cerdas 🛠️</h3>
        </div>
      </header>
      <article class="reading-section">
        <div class="slide-text">
          <p>Tonton instruksi video untuk mengerjakan mini project ini. Ikuti langkah-langkah di bawah ini:</p>
          <ol>
            <li>Buka proyek baru di MIT App Inventor.</li>
            <li>Buat UI dengan 2 TextBox, 1 Label, dan 2 Button (TAMBAH dan RESET).</li>
            <li>Buat Procedure "Do" dengan nama <code>ResetLayar</code> untuk mengosongkan TextBox dan Label.</li>
            <li>Buat Procedure "Result" dengan nama <code>JumlahkanAngka</code> yang menambahkan TextBox1 dan TextBox2.</li>
            <li>Panggil procedure tersebut di masing-masing tombol seperti contoh di video.</li>
          </ol>
        </div>
      </article>
    `
  },
  3: {
    thumbnail: "./thumb_3.png",
    kicker: "Checkpoint 03",
    title: "Optimasi dan Modularisasi Kode",
    duration: "Video 3 · Interaktif",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 883,
    endSeconds: 1194,
    bookmarks: [
      {"time": 883, "label": "Modularisasi"},
      {"time": 991, "label": "Spaghetti Code vs Modular"}
    ],
    quizzes: [
      {
        time: 1193,
        resumeTime: 1194,
        skipTo: 1194,
        title: "Mini Kuis 3 🧠",
        questions: [
          {
            qid: "V3_Q1",
            question: "Mengapa memecah program menjadi modul-modul (procedure) kecil itu sangat membantu saat terjadi error (bug)?",
            options: [
              "Karena kita bisa mengisolasi masalah dan mencari error di satu \"kotak\" modul spesifik.",
              "Karena modul akan secara otomatis menghapus bug tanpa kita suruh.",
              "Karena jika memakai modul, App Inventor tidak akan pernah error."
            ],
            answer: "Karena kita bisa mengisolasi masalah dan mencari error di satu \"kotak\" modul spesifik.",
            explanation: "Kita bisa langsung fokus mencari error di modul yang bermasalah saja, tanpa membaca ribuan baris kode yang lain."
          }
        ]
      }
    ],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 03</p>
          <h3>Optimasi dan Modularisasi Kode</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Apa itu Modularisasi?</h4>
        <div class="slide-text">
          <p>Memecah aplikasi besar menjadi modul-modul kecil yang lebih fokus dan teratur, menghindari kode yang berantakan (Spaghetti Code).</p>
        </div>
        <h4>Manfaat Modularisasi</h4>
        <div class="slide-text">
          <p>Flowchart program menjadi lebih sederhana (contoh: [START] -> Cek Input -> Hitung -> [END]).</p>
          <div class="quote-box">Modularisasi juga berlaku untuk desain UI (contoh: pakai Horizontal Arrangement).</div>
        </div>
      </article>
    `
  },
  4: {
    thumbnail: "./thumb_4.png",
    kicker: "Checkpoint 04",
    title: "Uji Coba dan Debugging",
    duration: "Video 4 · Penyimpanan Lokal",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 1201,
    endSeconds: 1685,
    bookmarks: [
      {"time": 1206, "label": "Membahas bug dan error"},
      {"time": 1307, "label": "Apa itu bug?"},
      {"time": 1402, "label": "Bug/crash tipe data"},
      {"time": 1461, "label": "Deteksi is a number?"},
      {"time": 1525, "label": "Fitur rahasia: Do it"},
      {"time": 1556, "label": "Tiny DB untuk keamanan"}
    ],
    quizzes: [
      {
        time: 1684,
        resumeTime: 1685,
        skipTo: 1685,
        title: "Mini Kuis 4 🧠",
        questions: [
          {
            qid: "V4_Q1",
            question: "Apa fungsi dari blok TinyDB di App Inventor?",
            options: [
              "Menyimpan data kecil secara lokal di handphone pengguna sehingga data tidak hilang saat aplikasi ditutup.",
              "Membagikan foto otomatis ke Instagram pengguna.",
              "Menyimpan gambar ukuran besar yang dibuat dengan MS Paint."
            ],
            answer: "Menyimpan data kecil secara lokal di handphone pengguna sehingga data tidak hilang saat aplikasi ditutup.",
            explanation: "TinyDB menyimpan data secara aman di dalam HP pengguna (penyimpanan lokal)."
          }
        ]
      }
    ],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 04</p>
          <h3>Uji Coba dan Debugging</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Apa itu Bug?</h4>
        <div class="slide-text">
          <p>Kesalahan atau cacat dalam program. Debugging adalah proses memperbaikinya.</p>
        </div>
        <h4>Solusi dan Keamanan</h4>
        <div class="slide-text">
          <ul>
            <li>Validasi Data: Gunakan blok 'is a number?' untuk mencegah crash karena tipe data salah.</li>
            <li>Keamanan Data: Gunakan TinyDB untuk menyimpan data secara aman di memori lokal HP.</li>
          </ul>
        </div>
      </article>
    `
  },
  5: {
    thumbnail: "./thumb_5.png",
    kicker: "Checkpoint 05",
    title: "Presentasi dan Refleksi",
    duration: "Video 5",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 1704,
    endSeconds: 2008,
    bookmarks: [
      {"time": 1704, "label": "Mempresentasikan project"},
      {"time": 1790, "label": "Empat poin presentasi"},
      {"time": 1903, "label": "Persiapan live demo"},
      {"time": 1955, "label": "Menerima feedback"}
    ],
    quizzes: [
      {
        time: 2007,
        resumeTime: 2008,
        skipTo: 2008,
        title: "Mini Kuis 5 🧠",
        questions: [
          {
            qid: "V5_Q1",
            question: "Saat presentasi, kelompok lain memberi kritik: \"Aplikasi kalian keren, tapi teks petunjuknya sulit dibaca karena warnanya gelap.\" Sikap yang tepat adalah:",
            options: [
              "Menyuruh mereka memeriksa mata ke dokter karena teksnya sudah jelas.",
              "Pura-pura mencatat, tapi tidak pernah memperbaiki aplikasinya.",
              "Berterima kasih atas feedback tersebut, dan berjanji akan mengubah warna teks menjadi lebih terang."
            ],
            answer: "Berterima kasih atas feedback tersebut, dan berjanji akan mengubah warna teks menjadi lebih terang.",
            explanation: "Feedback yang membangun harus diterima untuk menyempurnakan aplikasi."
          }
        ]
      }
    ],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 05</p>
          <h3>Presentasi dan Refleksi</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Struktur Presentasi Aplikasi</h4>
        <div class="slide-text">
          <ol>
            <li>Latar Belakang (Mengapa aplikasi dibuat)</li>
            <li>Fitur Utama</li>
            <li>Demo Langsung (Live Demo)</li>
            <li>Tantangan Tersulit</li>
          </ol>
          <div class="quote-box">Umpan balik (feedback) adalah hadiah untuk membuat aplikasi menjadi lebih baik!</div>
        </div>
      </article>
    `
  },
  6: {
    thumbnail: "./thumb_6.png",
    kicker: "Checkpoint 06",
    title: "Merancang Solusi Digital",
    duration: "Video 6 · Tantangan Akhir",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 2018,
    endSeconds: 2261,
    bookmarks: [
      {"time": 2018, "label": "Aplikasi berdampak positif"},
      {"time": 2086, "label": "Mengidentifikasi masalah nyata"},
      {"time": 2189, "label": "Contoh aplikasi alarm ibu"},
      {"time": 2260, "label": "Brainstorming idea"}
    ],
    quizzes: [
      {
        time: 2260,
        resumeTime: 2261,
        skipTo: 2261,
        title: "Mini Kuis 6 🧠",
        questions: [
          {
            qid: "V6_Q1",
            question: "Manakah dari ide aplikasi di bawah ini yang merupakan \"Solusi Digital Berdampak Positif\" untuk memecahkan masalah di sekolah?",
            options: [
              "Game tebak-tebakan artis korea.",
              "Aplikasi pengingat jadwal piket kelas yang terhubung dengan notifikasi harian.",
              "Aplikasi senter yang hanya hidup dan mati secara random."
            ],
            answer: "Aplikasi pengingat jadwal piket kelas yang terhubung dengan notifikasi harian.",
            explanation: "Ini adalah solusi digital yang punya manfaat dan memecahkan masalah nyata."
          }
        ]
      }
    ],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 06</p>
          <h3>Merancang Solusi Digital</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Solusi yang Berdampak Positif</h4>
        <div class="slide-text">
          <p>Programmer terbaik adalah problem solver. Mulailah dari empati (peduli) melihat masalah di sekitar.</p>
          <div class="quote-box">Kamu telah membuktikan dirimu bukan sekadar pengguna HP, tapi PENCIPTA TEKNOLOGI!</div>
        </div>
      </article>
    `
  },
  7: {
    thumbnail: "./thumb_7.png",
    kicker: "Checkpoint 07",
    title: "Merancang Solusi Digital",
    duration: "Mini Project",
    videoId: "P8Ea0v8Gy2o",
    startSeconds: 2267,
    endSeconds: 2303,
    bookmarks: [],
    quizzes: [],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Tugas Akhir</p>
          <h3>Misi Brainstorming Ide Aplikasi! 🚀</h3>
        </div>
      </header>
      <article class="reading-section">
        <div class="slide-text">
          <p>Waktunya menerapkan ilmu yang sudah kamu pelajari untuk memecahkan masalah nyata di sekitarmu.</p>
        </div>
      </article>
    `
  }
};
