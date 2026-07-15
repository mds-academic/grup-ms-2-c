export const courseData = {
  1: {
    kicker: "Checkpoint 01 · Logika di Dunia Nyata",
    title: "PERCABANGAN GANDA",
    duration: "Video 1 · Logika di Dunia Nyata",
    videoId: "tDkIcceTzII",
    startSeconds: 3,
    endSeconds: 472,
    bookmarks: [{"time":10,"label":"Pendahuluan"},{"time":60,"label":"Logika Percabangan"},{"time":120,"label":"If-Then-Else"},{"time":300,"label":"Flowchart"}],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 01</p>
          <h3>PERCABANGAN GANDA: Logika di Dunia Nyata</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Ribuan Pilihan Setiap Hari 🤯</h4>
<div class="slide-text">
<p>Tahukah kamu bahwa otak kita membuat ribuan pilihan setiap harinya?</p>
<ul>
    <li>Jam berapa harus bangun?</li>
    <li>Baju apa yang harus dipakai?</li>
    <li>Makan ayam atau ikan?</li>
</ul>
<p>Proses memilih inilah yang dalam ilmu komputer disebut <strong>Logika Percabangan</strong>.</p>
</div>

        <h4>Apa Itu Percabangan? 🤔</h4>
<div class="slide-text">
<p>Percabangan berarti menentukan jalan berdasarkan suatu <strong>kondisi</strong>.</p>
<div class="quote-box">"Jika (IF) hari ini hujan, maka (THEN) aku bawa payung." ☔</div>
<p>Jika kondisi "hujan" benar, maka instruksi "bawa payung" dilakukan. Ini adalah contoh percabangan tunggal.</p>
</div>

        <h4>Kelemahan Kondisi Tunggal 🛑</h4>
<div class="slide-text">
<p>Bayangkan robot penjaga dengan perintah: <strong>"Jika ada tamu, bukakan pintu."</strong></p>
<p>Apa yang terjadi jika tamu itu adalah pencuri yang tidak dikenal? Robot tetap membukakan pintu!</p>
<p>Ini karena robot hanya punya satu kondisi tanpa jalan keluar alternatif.</p>
</div>

        <h4>If-Then-Else (Ganda) 🔀</h4>
<div class="slide-text">
<p>Untuk membuat robot cerdas, kita gunakan <strong>Else (Selain itu)</strong>.</p>
<ul>
    <li><strong>Jika (If)</strong> tamu adalah orang yang dikenal, <strong>Maka (Then)</strong> bukakan pintu.</li>
    <li><strong>Selain itu (Else)</strong>, bunyikan alarm peringatan! 🚨</li>
</ul>
<p>Sekarang robot tahu harus berbuat apa di kedua situasi.</p>
</div>

        <h4>Analogi: Lampu Lalu Lintas 🚥</h4>
<div class="slide-text">
<div style="background: #C8E6C9; padding: 20px; border: 3px solid var(--black); border-radius: 12px;">
    <strong>Logika Lampu Pejalan Kaki</strong><br><br>
    <strong>Jika (If)</strong> tombol ditekan oleh pejalan kaki,<br>
    <strong>Maka (Then)</strong> Nyalakan lampu merah untuk mobil.<br>
    <strong>Selain itu (Else)</strong>,<br>
    Biarkan lampu hijau menyala untuk mobil.
</div>
</div>

        <h4>Analogi: Game Over 🎮</h4>
<div class="slide-text">
<div style="background: #FFF9C4; padding: 20px; border: 3px solid var(--black); border-radius: 12px;">
    <strong>Logika Nyawa Pemain</strong><br><br>
    <strong>Jika (If)</strong> nyawa pemain habis (0),<br>
    <strong>Maka (Then)</strong> Tampilkan layar "Game Over".<br>
    <strong>Selain itu (Else)</strong>,<br>
    Lanjutkan permainan seperti biasa.
</div>
</div>

        <h4>Menggambar Logika (Flowchart) 🗺️</h4>
<div class="slide-text">
<p>Programmer menjelaskan logika ini ke dalam gambar yang disebut <strong>Flowchart</strong>.</p>
<ul>
    <li><strong>Oval:</strong> Mulai / Selesai (Start/End)</li>
    <li><strong>Persegi:</strong> Proses / Tindakan / Perintah</li>
    <li><strong>Belah Ketupat 🔷:</strong> Pertanyaan Kondisi (Bercabang 2 jalan: YA dan TIDAK)</li>
</ul>
</div>

        <h4>Contoh Flowchart Hujan 🔷</h4>
<div class="slide-text">
<div class="fc-container">
    <div class="fc-node fc-oval">Mulai</div>
    <div class="fc-arrow-down"></div>
    <div class="fc-diamond-wrapper">
        <div class="fc-diamond"></div>
        <div class="fc-diamond-text">Apakah<br>Hujan?</div>
    </div>
    
    <div class="fc-row" style="margin-top: 5px;">
        <div style="text-align:right; margin-right: 5px; font-weight:bold; color:var(--red);">TIDAK</div>
        <div class="fc-arrow-left" style="transform: scaleX(-1);"></div>
        <div style="width: 100px;"></div>
        <div class="fc-arrow-right"></div>
        <div style="text-align:left; margin-left: 5px; font-weight:bold; color:var(--green);">YA</div>
    </div>
    
    <div class="fc-row" style="gap: 20px; margin-top: 5px;">
        <div class="fc-node fc-rect" style="background-color:#FFCDD2;">Pakai Topi</div>
        <div class="fc-node fc-rect" style="background-color:#C8E6C9;">Bawa Payung</div>
    </div>
</div>
</div>

        <h4>Tugas Mandiri 🕵️‍♂️</h4>
<div class="slide-text">
<div class="mini-project-card">
    <h3>Detektif Flowchart!</h3>
    <p>1. Amati sistem lampu taman yang menyala malam hari.<br>
    2. Gambarkan flowchart <strong>If-Then-Else</strong> di kertasmu.<br>
    3. Tentukan pertanyaan di dalam Belah Ketupat (Misal: Apakah sudah gelap?).<br>
    4. Tentukan aksi jika YA, dan jika TIDAK.</p>
</div>
</div>
      </article>`,
    quizzes: [
      {
        time: 331,
        resumeTime: 336,
        skipTo: 336,
        title: "Kuis Logika Dasar 🧠",
        questions: [
          {
            qid: "V1_Q1",
            question: "Apa fungsi dari blok ELSE?",
            options: [
              "A. Mengakhiri seluruh program",
              "B. Menjalankan perintah jika IF bernilai SALAH",
              "C. Menjalankan perintah berulang-ulang tanpa henti"
            ],
            answer: "B. Menjalankan perintah jika IF bernilai SALAH",
            explanation: "ELSE digunakan untuk mengeksekusi aksi alternatif jika kondisi pada blok IF tidak terpenuhi atau bernilai SALAH."
          }
        ]
      },
      {
        time: 472,
        title: "Kuis Flowchart 🧠",
        questions: [
          {
            qid: "V1_Q2",
            question: "Simbol apakah yang digunakan untuk membuat percabangan kondisi (IF) dalam flowchart?",
            options: [
              "A. Persegi",
              "B. Belah Ketupat",
              "C. Lingkaran/Oval"
            ],
            answer: "B. Belah Ketupat",
            explanation: "Simbol belah ketupat digunakan untuk merepresentasikan keputusan (decision) atau percabangan dalam suatu flowchart."
          }
        ]
      }
    ]
  },
  2: {
    kicker: "Checkpoint 02 · Percabangan Blok",
    title: "APP INVENTOR",
    duration: "Video 2 · Percabangan Blok",
    videoId: "tDkIcceTzII",
    startSeconds: 484,
    endSeconds: 721,
    bookmarks: [{"time":490,"label":"App Inventor"},{"time":540,"label":"UI Designer"},{"time":600,"label":"Blok Event"},{"time":700,"label":"Logika"}],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 02</p>
          <h3>APP INVENTOR: Percabangan Blok</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Blok IF di App Inventor 🧩</h4>
<div class="slide-text">
<p>Di App Inventor, logika percabangan bersembunyi di laci <strong>Control</strong> yang berwarna coklat.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-control">
        <div class="ai-event-header">
            <span class="ai-mutator"></span> if <div class="ai-block ai-math"> </div>
        </div>
        <div class="ai-event-do">then</div>
        <div class="ai-event-body">
            
        </div>
    </div>
</div>
<p>Perhatikan bahwa bentuk blok ini seperti penjepit (bracket) yang bisa memeluk blok lainnya di dalam <code>then</code>.</p>
</div>

        <h4>Memunculkan ELSE dengan Mutator ⚙️</h4>
<div class="slide-text">
<p>Awalnya, blok IF hanya punya "Then". Tidak ada "Else" sama sekali.</p>
<p>Untuk menambah Else, kamu HARUS mengklik ikon <strong>Roda Gigi (Mutator) ⚙️</strong> kecil warna biru di sudut kiri atas blok tersebut.</p>
<p>Sebuah pop-up kecil akan muncul, tarik blok <code>else</code> dan gabungkan ke blok <code>if</code> di dalam pop-up tersebut.</p>
</div>

        <h4>Blok Lengkap If-Then-Else 🔀</h4>
<div class="slide-text">
<p>Setelah menarik blok else, blok aslimu akan berubah menjadi seperti ini:</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-control">
        <div class="ai-event-header">
            <span class="ai-mutator"></span> if <div class="ai-block ai-math"> </div>
        </div>
        <div class="ai-event-do">then</div>
        <div class="ai-event-body"></div>
        <div class="ai-event-do">else</div>
        <div class="ai-event-body"></div>
    </div>
</div>
<p>Sekarang kamu punya 2 tempat kosong untuk diisi aksi yang berbeda!</p>
</div>

        <h4>UI Designer: Aplikasi Kelulusan 🎨</h4>
<div class="slide-text">
<p>Mari kita siapkan tampilan layar aplikasi di halaman Designer terlebih dahulu.</p>
    <div class="designer-container" style="margin-top: 30px;">
        <div class="phone-mockup">
            <div class="phone-screen">
                <div style="background:#ddd; padding:5px; text-align:center; font-size:12px; font-weight:bold; border-radius:4px; margin-bottom:10px;">Screen1</div>
                <div class="ui-comp ui-lbl">Masukkan Nilai Ujian:</div><div class="ui-comp ui-txt">Hint: 80</div><div class="ui-comp ui-btn">CEK KELULUSAN</div><div class="ui-comp ui-lbl">Hasil: ???</div>
            </div>
        </div>
        <div class="properties-panel">
            <h3 style="margin-bottom:15px; border-bottom:3px solid var(--black); padding-bottom:5px;">⚙️ Properties</h3>
            <div class="prop-item"><strong>TextBox1</strong><span>Rename jadi txtNilai</span></div><div class="prop-item"><strong>Button1</strong><span>Rename jadi btnCek</span></div><div class="prop-item"><strong>Label2</strong><span>Rename jadi lblHasil</span></div>
        </div>
    </div>
</div>

        <h4>Koding Blok Event (When Click) 👆</h4>
<div class="slide-text">
<p>Pertama, kita ambil blok kejadian (event) berwarna emas dari laci <strong>btnCek</strong>.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            
        </div>
    </div>
</div>
<p>Ini artinya: "Ketika tombol btnCek diklik, lakukan apa yang ada di dalam pelukanku".</p>
</div>

        <h4>Menambahkan Logika & Kondisi 🧠</h4>
<div class="slide-text">
<p>Lalu kita masukkan blok IF dan kondisi matematika (biru) dari laci Math.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            <div class="ai-block ai-control">
                <div class="ai-event-header">
                    <span class="ai-mutator"></span> if <div class="ai-block ai-math"><div class="ai-dropdown">txtNilai</div> .Text ≥ 75</div>
                </div>
                <div class="ai-event-do">then</div>
                <div class="ai-event-body"></div>
                <div class="ai-event-do">else</div>
                <div class="ai-event-body"></div>
            </div>
        </div>
    </div>
</div>
</div>

        <h4>Mengisi Aksi (Set Label Text) ✏️</h4>
<div class="slide-text">
<p>Terakhir, kita gunakan blok hijau tua dari laci lblHasil untuk mengubah teks sesuai kondisi!</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event" style="transform: scale(0.9); transform-origin: top left;">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            <div class="ai-block ai-control">
                <div class="ai-event-header">
                    <span class="ai-mutator"></span> if <div class="ai-block ai-math"><div class="ai-dropdown">txtNilai</div> .Text ≥ 75</div>
                </div>
                <div class="ai-event-do">then</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblHasil</div> .Text to <div class="ai-block ai-text">"Kamu Lulus!"</div>
                    </div>
                </div>
                <div class="ai-event-do">else</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblHasil</div> .Text to <div class="ai-block ai-text">"Belajar Lagi!"</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

        <h4>Latihan Mandiri 🚀</h4>
<div class="slide-text">
<div class="mini-project-card">
    <h3>Aplikasi Cek Suhu</h3>
    <p>1. Buat aplikasi sederhana dengan input Suhu (TextBox).<br>
    2. <strong>If (Suhu &gt; 30)</strong>, then set label jadi "Panas Sekali!"<br>
    3. <strong>Else</strong>, set label jadi "Cuaca Nyaman."<br>
    4. Test di Companion!</p>
</div>
</div>
      </article>`,
    quizzes: [
      {
        time: 721,
        title: "Kuis Fungsi Mutator 🧠",
        questions: [
          {
            qid: "V2_Q1",
            question: "Apa yang harus diklik untuk memunculkan pilihan ELSE?",
            options: [
              "A. Klik Kanan > Add Else",
              "B. Ikon roda gigi biru di blok IF"
            ],
            answer: "B. Ikon roda gigi biru di blok IF",
            explanation: "Ikon roda gigi biru (mutator) pada blok IF di App Inventor digunakan untuk menambahkan opsi ELSE atau ELSE IF."
          }
        ]
      }
    ]
  },
  3: {
    kicker: "Checkpoint 03 · Uang Digital",
    title: "LITERASI KEUANGAN",
    duration: "Video 3 · Uang Digital",
    videoId: "tDkIcceTzII",
    startSeconds: 733,
    endSeconds: 1173,
    bookmarks: [{"time":740,"label":"Literasi Keuangan"},{"time":840,"label":"Uang Digital"},{"time":900,"label":"E-Wallet"},{"time":1100,"label":"QRIS"}],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 03</p>
          <h3>LITERASI KEUANGAN: Uang Digital</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Sejarah Uang Singkat ⏳</h4>
<div class="slide-text">
<p>Ribuan tahun lalu, orang bertukar barang langsung (Barter). Lalu muncul koin emas, kemudian uang kertas yang mudah dibawa.</p>
<p>Hari ini? Uang bahkan tidak terlihat bentuknya. Hanya berupa angka di sistem komputer!</p>
<p>Itulah yang disebut dengan Era Uang Digital.</p>
</div>

        <h4>Pendapatan (Income) 📥</h4>
<div class="slide-text">
<p><strong>Pendapatan</strong> = Semua uang yang mengalir masuk ke kantongmu.</p>
<div class="quote-box" style="background-color: var(--blue);">Sebutkan 3 sumber pendapatanmu saat ini! 💰</div>
<p>Mungkin dari uang saku mingguan orang tua, amplop lebaran, atau hasil jualan stiker di kelas.</p>
</div>

        <h4>Pengeluaran (Expense) 📤</h4>
<div class="slide-text">
<p><strong>Pengeluaran</strong> = Uang yang keluar untuk ditukar dengan barang/jasa.</p>
<p>Membeli makanan, bayar ongkos angkot, hingga top-up diamond game adalah pengeluaran.</p>
<p>Jika pengeluaran lebih besar dari pendapatan? Kamu akan berhutang!</p>
</div>

        <h4>Tabungan (Savings) 🐷</h4>
<div class="slide-text">
<p><strong>Rumus Sakti: Tabungan = Pendapatan - Pengeluaran</strong></p>
<p>Tabungan berfungsi sebagai "benteng pertahanan" ketika ada hal darurat atau ketika kamu ingin membeli sesuatu yang mahal di masa depan tanpa harus meminjam uang.</p>
</div>

        <h4>E-Wallet (Dompet Digital) 📱</h4>
<div class="slide-text">
<p>Sama seperti dompet kulit, tapi di dalam handphone.</p>
<div style="background-color: #E3F2FD; padding: 20px; border: 3px solid var(--black); border-radius: 12px; margin: 15px 0;">
    Aplikasi seperti Gopay, OVO, Dana, LinkAja bertugas menjaga "saldo" digital kita. Uang fisik kita diserahkan ke sistem mereka, ditukar dengan saldo digital.
</div>
</div>

        <h4>QRIS Bikin Semua Mudah ⬛⬜</h4>
<div class="slide-text">
<p><strong>QRIS</strong> (Quick Response Code Indonesian Standard)</p>
<p>Di balik kotak-kotak hitam putih QRIS, tersimpan data rekening penjual. Saat kameramu memindainya, aplikasi e-wallet langsung tahu ke mana uang harus ditransfer dalam hitungan detik!</p>
</div>

        <h4>Diskusi Kelompok 🗣️</h4>
<div class="slide-text">
<div class="mini-project-card">
    <h3>Bahaya Uang Digital?</h3>
    <p>Apakah uang digital membuat orang lebih boros?<br>
    Karena kita tidak melihat uang fisiknya berkurang, kadang kita terus men-scan QRIS sampai saldo habis.<br>
    Diskusikan dengan temanmu bagaimana cara mengatasinya!</p>
</div>
</div>
      </article>`,
    quizzes: [
      {
        time: 1173,
        title: "Kuis Digital 1 🧠",
        questions: [
          {
            qid: "V3_Q1",
            question: "Menerima transfer hadiah Rp 50.000 ke akun Dana disebut?",
            options: [
              "A. Pengeluaran digital",
              "B. Pendapatan digital"
            ],
            answer: "B. Pendapatan digital",
            explanation: "Setiap uang yang masuk atau menambah saldo kita disebut sebagai pendapatan (income)."
          }
        ]
      }
    ]
  },
  4: {
    kicker: "Checkpoint 04 · Needs vs Wants",
    title: "LITERASI KEUANGAN",
    duration: "Video 4 · Needs vs Wants",
    videoId: "tDkIcceTzII",
    startSeconds: 1181,
    endSeconds: 1593,
    bookmarks: [{"time":1190,"label":"Needs vs Wants"},{"time":1300,"label":"Kebutuhan & Keinginan"},{"time":1400,"label":"Aturan 50-30-20"}],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 04</p>
          <h3>LITERASI KEUANGAN: Needs vs Wants</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Jebakan Batman Finansial 🦇</h4>
<div class="slide-text">
<p>Banyak orang kehabisan uang bukan karena pendapatannya kecil, tapi karena mereka tidak bisa membedakan mana yang <strong>BUTUH</strong> dan mana yang <strong>INGIN</strong>.</p>
<p>Ini adalah jebakan terbesar dalam mengelola uang saku!</p>
</div>

        <h4>Kebutuhan (Needs) 🍞</h4>
<div class="slide-text">
<p>Kebutuhan (Needs) adalah hal yang <strong>HARUS</strong> dipenuhi.</p>
<ul>
    <li>Tanpanya, kita sakit (Makanan pokok)</li>
    <li>Tanpanya, kita dihukum (Seragam sekolah)</li>
    <li>Tanpanya, kita tidak bisa belajar (Alat tulis, Kuota tugas)</li>
</ul>
</div>

        <h4>Keinginan (Wants) 🎮</h4>
<div class="slide-text">
<p>Keinginan (Wants) adalah hal yang dipengaruhi nafsu atau gengsi.</p>
<ul>
    <li>Kamu sudah punya sepatu yang bagus, tapi ingin beli sepatu merk Hypebeast.</li>
    <li>Kamu sudah minum air putih, tapi ingin beli Thai Tea Boba yang mahal.</li>
</ul>
<p>Keinginan tidak salah, tapi <strong>harus ditunda</strong> sampai uang lebih.</p>
</div>

        <h4>Aturan 50-30-20 📊</h4>
<div class="slide-text">
<p>Salah satu cara membagi uang saku:</p>
<div style="background-color: #FFF9C4; padding: 20px; border: 3px solid var(--black); border-radius: 12px;">
    <strong>50%</strong> untuk Kebutuhan (Needs)<br>
    <strong>30%</strong> untuk Keinginan (Wants)<br>
    <strong>20%</strong> untuk Tabungan (Savings)
</div>
<p>Tentu saja porsi Tabungan bisa lebih besar jika kamu sedang hemat!</p>
</div>

        <h4>Aturan Tunggu 24 Jam 🛑</h4>
<div class="slide-text">
<div class="quote-box" style="background-color: var(--black); color: var(--pink);">Jangan beli langsung! Tunggu 1 hari!</div>
<p>Seringkali, keinginan membeli (impulsive buying) akan hilang setelah kita tidur satu malam.</p>
<p>Jika besoknya kamu merasa tidak butuh lagi, selamat! Kamu baru saja menghemat uang.</p>
</div>

        <h4>Latihan: Buat Budgetmu 📝</h4>
<div class="slide-text">
<div class="mini-project-card">
    <h3>Jadilah Menteri Keuangan!</h3>
    <p>1. Anggap uang sakumu minggu ini Rp 50.000.<br>
    2. Tulis di kertas: 2 Needs (Kebutuhan) yang pasti dibeli.<br>
    3. Tulis 1 Wants (Keinginan) yang ingin dibeli jika sisa uang cukup.<br>
    4. Tulis alokasi Tabungan! (Minimal Rp 5.000)</p>
</div>
</div>
      </article>`,
    quizzes: [
      {
        time: 1593,
        title: "Kuis Prioritas 1 🧠",
        questions: [
          {
            qid: "V4_Q1",
            question: "Membeli paket internet agar bisa mengirim tugas presentasi besok pagi termasuk...",
            options: [
              "A. Kebutuhan (Needs)",
              "B. Keinginan (Wants)"
            ],
            answer: "A. Kebutuhan (Needs)",
            explanation: "Paket internet untuk mengirim tugas adalah kebutuhan (needs) karena wajib dipenuhi untuk kegiatan belajarmu."
          }
        ]
      },
      {
        time: 1593,
        title: "Kuis Prioritas 2 🧠",
        questions: [
          {
            qid: "V4_Q2",
            question: "Membeli gacha/top-up diamond agar karakter game-mu lebih keren adalah...",
            options: [
              "A. Kebutuhan mutlak",
              "B. Keinginan (Wants)"
            ],
            answer: "B. Keinginan (Wants)",
            explanation: "Top-up game merupakan keinginan (wants) karena hanya untuk kesenangan dan bukan hal yang harus dipenuhi segera."
          }
        ]
      }
    ]
  },
  5: {
    kicker: "Checkpoint 05 · Aplikasi Kalkulator Keuangan",
    title: "APP INVENTOR + FINANSIAL",
    duration: "Video 5 · Aplikasi Kalkulator Keuangan",
    videoId: "tDkIcceTzII",
    startSeconds: 1605,
    endSeconds: 1908,
    bookmarks: [{"time":1620,"label":"App Keuangan"},{"time":1700,"label":"UI Nabung"},{"time":1800,"label":"Blok Keuangan"}],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 05</p>
          <h3>APP INVENTOR + FINANSIAL: Aplikasi Kalkulator Keuangan</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Mengapa Komputer & Uang? 🤖</h4>
<div class="slide-text">
<p>Manusia sering lapar mata dan salah hitung. Komputer tidak pernah bohong!</p>
<p>Kita bisa menggabungkan <strong>Logika IF</strong> dengan <strong>Matematika Keuangan</strong> di App Inventor untuk menjaga kita tetap disiplin berhemat.</p>
</div>

        <h4>UI Designer: Aplikasi Nabung 🎨</h4>
<div class="slide-text">
<p>Kita buat desain Kalkulator Target Tabungan.</p>
    <div class="designer-container" style="margin-top: 30px;">
        <div class="phone-mockup">
            <div class="phone-screen">
                <div style="background:#ddd; padding:5px; text-align:center; font-size:12px; font-weight:bold; border-radius:4px; margin-bottom:10px;">Screen1</div>
                <div class="ui-comp ui-lbl">Harga Barang Impian (Rp):</div><div class="ui-comp ui-txt">Misal: 50000</div><div class="ui-comp ui-lbl">Tabungan Saat Ini (Rp):</div><div class="ui-comp ui-txt">Misal: 20000</div><div class="ui-comp ui-btn">CEK BISA BELI?</div><div class="ui-comp ui-lbl">Status: ???</div>
            </div>
        </div>
        <div class="properties-panel">
            <h3 style="margin-bottom:15px; border-bottom:3px solid var(--black); padding-bottom:5px;">⚙️ Properties</h3>
            <div class="prop-item"><strong>TextBox_Harga</strong><span>Input tipe: Numbers Only</span></div><div class="prop-item"><strong>TextBox_Tabungan</strong><span>Input tipe: Numbers Only</span></div><div class="prop-item"><strong>Label_Status</strong><span>Font: Bold, Size: 18</span></div>
        </div>
    </div>
</div>

        <h4>Menyusun Blok Logika Keuangan 🧩</h4>
<div class="slide-text">
<p>Gunakan operasi perbandingan (≥) dari laci Math.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event" style="transform: scale(0.9); transform-origin: top left;">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            <div class="ai-block ai-control">
                <div class="ai-event-header">
                    <span class="ai-mutator"></span> if <div class="ai-block ai-math"><div class="ai-dropdown">txtTabungan</div> .Text ≥ <div class="ai-dropdown">txtHarga</div> .Text</div>
                </div>
                <div class="ai-event-do">then</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblStatus</div> .Text to <div class="ai-block ai-text">"Uang Cukup! Boleh Beli!"</div>
                    </div>
                </div>
                <div class="ai-event-do">else</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblStatus</div> .Text to <div class="ai-block ai-text">"Nabung lagi ya!"</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

        <h4>Menghitung Kekurangan (-) ➖</h4>
<div class="slide-text">
<p>Jika uang tidak cukup (Else), aplikasinya bisa menghitung kekurangan!</p>
<p>Ambil blok <strong>Math Minus (-)</strong>.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-math">
        <div class="ai-dropdown">txtHarga</div> .Text - <div class="ai-dropdown">txtTabungan</div> .Text
    </div>
</div>
<p>Ini adalah logika pengurangan dasar: Harga Barang dikurangi Tabungan kita.</p>
</div>

        <h4>Blok Join (Menggabung Teks) 🔗</h4>
<div class="slide-text">
<p>Untuk membuat kalimat seperti "Kurang Rp 30000", kita butuh blok <code>join</code> dari laci Text (Pink/Merah Muda).</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-join" style="background-color: #C2185B;">
        <div style="display:flex; gap:5px; align-items:center;">
            <div style="margin-right:5px;">join</div>
            <div class="ai-block ai-text">"Kurang Rp "</div>
        </div>
        <div style="display:flex; gap:5px; align-items:center; margin-left:30px;">
            <div class="ai-block ai-math"> <div class="ai-dropdown">txtHarga</div> .Text - <div class="ai-dropdown">txtTabungan</div> .Text</div>
        </div>
    </div>
</div>
<p>Masukkan hasil Join ini ke <code>set Label_Status.Text to</code> pada blok Else!</p>
</div>

        <h4>Mini Project Final 🏆</h4>
<div class="slide-text">
<div class="mini-project-card">
    <h3>Aplikasi Target Tabungan!</h3>
    <p>Praktik di MIT App Inventor sekarang!</p>
    <ol>
        <li>Buat desain UI (TextBox Tabungan, TextBox Harga, Tombol Cek).</li>
        <li>Susun blok If-Then-Else membandingkan nilai keduanya.</li>
        <li>Tambahkan blok Math dan Join di bagian Else agar aplikasi memberi tahu berapa selisih kekurangannya.</li>
        <li>Jalankan di HP dengan MIT Companion dan tunjukkan hasilnya!</li>
    </ol>
</div>
</div>
      </article>`,
    quizzes: [
      {
        time: 1908,
        title: "Kuis Blok Keuangan 🧠",
        questions: [
          {
            qid: "V5_Q1",
            question: "Blok warna apa yang digunakan untuk operasi pengurangan (-)?",
            options: [
              "A. Coklat/Emas (Control)",
              "B. Biru (Math)",
              "C. Merah Muda (Text)"
            ],
            answer: "B. Biru (Math)",
            explanation: "Blok operasi matematika seperti pengurangan (-) berada di dalam laci Math yang berwarna biru di App Inventor."
          }
        ]
      }
    ]
  },
  6: {
    kicker: "Checkpoint 06 · Mini Project",
    title: "FINAL PROJECT",
    duration: "Tugas Pengganti Kehadiran",
    videoId: "tDkIcceTzII",
    startSeconds: 1922,
    bookmarks: [{"time": 1930, "label": "Mini Project"}],
    summaryHtml: `
      <header class="reading-header">
        <div>
          <p class="label">Materi Bacaan 06</p>
          <h3>Tugas Akhir: Pengganti Kehadiran</h3>
        </div>
      </header>
      <article class="reading-section">
        <h4>Aplikasi Target Tabungan! 🏆</h4>
        <div class="slide-text">
          <div class="mini-project-card">
              <p>Praktik di MIT App Inventor sekarang!</p>
              <ol>
                  <li>Buat desain UI (TextBox Tabungan, TextBox Harga, Tombol Cek).</li>
                  <li>Susun blok If-Then-Else membandingkan nilai keduanya.</li>
                  <li>Tambahkan blok Math dan Join di bagian Else agar aplikasi memberi tahu berapa selisih kekurangannya.</li>
                  <li>Jalankan di HP dengan MIT Companion dan tunjukkan hasilnya!</li>
              </ol>
              <p style="margin-top:20px;"><strong>Submit link/screenshot aplikasi kamu pada form di bawah ini sebagai bukti kehadiran.</strong></p>
          </div>
        </div>
      </article>`,
    quizzes: []
  },
};
