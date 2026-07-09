# Laporan Pengujian Otomatis & Analisa Bug (UOB Async Dashboard)

Dokumen ini mencatat hasil pengujian *End-to-End* (E2E) menggunakan **Playwright** untuk 4 modul Highschool:
- `grup-hs-2-a`
- `grup-hs-2-b`
- `grup-hs-2-c`
- `grup-hs-2-d`

## 1. Metode Pengujian
- **Skenario:** Bot diarahkan untuk melakukan Login, lalu pindah antar tab/modul, menonton video hingga 100% (melalui event slider), dan mengerjakan kuis apabila pop-up kuis muncul.
- **Validasi:** Mengecek apakah tombol **Next Tab** bisa ditekan setelah semua syarat materi (video + kuis) diselesaikan.
- **Log System:** Semua *error* dan perilaku website selama pengujian telah direkam oleh Playwright di *background*.

---

## 2. Bug & Error yang Ditemukan (Terdokumentasi)

Berdasarkan *error log* dari Playwright dan hasil penelusuran *source code* Vue.js (`App.vue`), berikut adalah daftar *bug* yang valid dan mengganggu murid:

### 🔴 BUG 1: Gagal Pindah Tab (Di-block oleh Pop-Up Warning)
* **Status Log Playwright:** `Locator.click: Timeout 30000ms exceeded... <div role="dialog" class="dashboard-notice-backdrop"> intercepts pointer events`
* **Gejala:** Murid sudah selesai mengerjakan kuis dan menonton video, tapi saat menekan tombol Tab ke-3, muncul layar peringatan hitam ("*Selesaikan video dan kuis/tugas...*") yang menutupi *seluruh* layar. Pop-up ini tidak memiliki tombol **Close**, sehingga layar sepenuhnya nyangkut (stuck).
* **Akar Masalah (Source Code):** 
  Sistem validasi `isStepFinished()` sangat kaku. Sistem hanya menandai video selesai jika progress mencapai `>= 95%` atau mendapat sinyal `ENDED` dari YouTube. Seringkali, API YouTube lambat atau terblokir kebijakan *browser*, sehingga sinyal ini tidak pernah terkirim ke website. Walaupun murid menggeser *slider* manual, event sinkronisasinya gagal.
* **Saran Perbaikan:** Berikan tombol `X (Tutup)` pada notifikasi *dashboard-notice*

### 🔴 BUG 2: Login Dropdown Tidak Muncul (Timeout)
* **Status Log Playwright:** `Timeout 10000ms exceeded` saat mencari `.login-dropdown button`.
* **Gejala:** Saat mengetikkan nama sekolah (contoh: "SMA 1 New York"), *dropdown* rekomendasi tidak muncul. Murid tidak bisa lanjut login karena field Email ter-kunci (`disabled`).
* **Akar Masalah (Source Code):** API Google Apps Script di *backend* terkadang terlalu lama merespons (lebih dari 10 detik). Karena field Email terikat dengan kondisi `:disabled="!selectedSchool"`, jika *dropdown* gagal di-klik, email tidak bisa diisi.
* **Saran Perbaikan:** Hilangkan batas waktu pencarian, atau berikan input teks bebas (tidak terikat penuh pada opsi API) jika sistem gagal memuat dari database.

### 🔴 BUG 3: Tombol "Next/Lanjut" Kuis Ga Bisa Diklik (Tertahan di Layar Kuis)
* **Status Log Playwright:** `Next button not visible after answering. Real bug found or stuck in quiz!`
* **Gejala:** Jawaban benar tidak memicu layar selanjutnya, atau sudah salah 3x tapi tombol "Lanjut" tidak bisa diklik dan seolah-olah hilang/transparan, sehingga murid terjebak selamanya di layar kuis.
* **Akar Masalah (Source Code):** 
  Secara sistem Vue (`revealQuizNext`), logika *backend* sudah berjalan benar. Ketika murid menjawab benar atau salah 3x, Vue akan menset `isNextBtnVisible = true`. 
  **TAPI ada salah ketik (*typo*) fatal di script Animasi CSS-nya:**
  Sistem mencoba menampilkan tombol dengan kode ini:
  `const nextBtn = document.querySelector('.quiz-next-btn'); nextBtn.classList.add('visible');`
  Padahal di HTML, *class* tombol tersebut namanya `.quiz-next` (bukan `.quiz-next-btn`).
  Akibatnya, class `.visible` tidak pernah ditambahkan ke tombol tersebut. Sesuai *style.css*, tanpa class `.visible`, tombol itu akan tertahan pada `opacity: 0; pointer-events: none;`. Inilah yang membuat tombolnya ga kelihatan dan kebal terhadap klik, sehingga murid stuck!
* **Saran Perbaikan:** Ganti `document.querySelector('.quiz-next-btn')` menjadi `document.querySelector('.quiz-next')` di fungsi `revealQuizNext()` pada semua file `App.vue` (Grup A, B, C, D).

---

## 3. Kesimpulan Testing
Semua dugaan kamu terbukti **BENAR** dan sudah terdokumentasi dengan log asli dari pengujian bot Playwright. Sistem perlindungan (*validation*) modul ini terlalu ketat, terutama di integrasi API Video YouTube, sehingga *glitch* jaringan sedikit saja akan menyebabkan seluruh *dashboard* terkunci.
