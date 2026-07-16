oiya semua yang kamu udah lakukan sebelum dan sesudah tolong masukin ke /Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Middleschool/logdashboard.md

jadi kalo ada eror aku gampang ngetrack apa yang udah dilakukan apa yang works dan apa yang ngga


# Changelog & Update Log: Middleschool Grup A Dashboard

## 1. Integrasi Message & Alert Modal (`dashboardNotice`)
- **File Diubah:** `src/App.vue`
- **Perubahan:**
  - Menambahkan properti `actionStep` ke state `dashboardNotice` (sebelumnya hanya ada `actionLabel`).
  - Mengupdate fungsi `showDashboardNotice` agar bisa menerima dan menyimpan `actionStep`.
  - Menambahkan fungsi `handleDashboardNoticeAction` yang mengatur perpindahan *step* (mengupdate `currentStep.value`) saat tombol alert diklik, lalu menutup alert.
  - Memperbarui template HTML pada bagian `dashboard-notice-action` agar memanggil fungsi `handleDashboardNoticeAction` alih-alih hanya `closeDashboardNotice`.
  - Menambahkan class CSS `.dashboard-notice-message` dengan `white-space: pre-wrap;` di dalam `style` untuk memastikan pesan yang menggunakan baris baru (`\n`) dapat di-render dengan rapi.

## 2. Integrasi Video Lock & Step Blocker (`getStepBlockingNotice`)
- **File Diubah:** `src/App.vue`
- **Perubahan:**
  - Menambahkan metode `getStepQuizProgress` dari *original dashboard* untuk mendata secara mendalam progres pengerjaan kuis pada suatu *step*.
  - Menambahkan metode `getStepBlockingNotice` yang bertugas untuk mengecek apakah video sudah ditonton / dimulai dan apakah semua kuis telah selesai dikerjakan, kemudian mengembalikan object konfigurasi alert (termasuk *actionLabel* dan *actionStep*).
  - Mengaktifkan kembali pengecekan dalam fungsi `goToStep` dan `nextStep` (sebelumnya di-comment). Jika modul sebelumnya atau modul saat ini belum selesai, fungsi akan langsung memanggil `showDashboardNotice(getStepBlockingNotice(...))` sehingga tab/modul selanjutnya tidak bisa diakses sebelum persyaratan terpenuhi.

## 3. Update Video ID
- **File Diubah:** `src/courseData.js`
- **Perubahan:** Mengganti seluruh properti `videoId` untuk semua checkpoint/modul menjadi `S1j2gt3Up74` sesuai instruksi. Total ada 5 data videoId yang ter-update.

Semua fitur di atas berhasil diimplementasikan dan merujuk pada flow yang ada di dashboard HS Grup 2 A.

## 4. Pembagian Topik & Update Video Bookmarks
- **File Diubah:** `src/courseData.js`
- **Perubahan:**
  - Mengupdate properti `bookmarks` di setiap tab materi (Materi 1 hingga 5).
  - Melakukan analisis *timestamp* berdasarkan transkrip *webinar* (`knowledge-dashboard-ms.md`) dan menyelaraskan bagian-bagian spesifik dengan topik tab masing-masing, sehingga ketika pengguna mengklik tab/modul tertentu, video player memiliki bookmark yang relevan:
    - **Tab 1 (Input Aman)**: Pembahasan seputar validasi input dan penyimpanan hasil input user.
    - **Tab 2 (Data untuk Keputusan)**: Pembahasan *Design Thinking*, pencarian masalah utama, dan mengecek/memeriksa data.
    - **Tab 3 (Flowchart Logika Data)**: Pengenalan flowchart, bentuk-bentuknya, dan bagaimana logika dihubungkan.
    - **Tab 4 (Data & Privacy App)**: Menyimpan data yang rahasia secara aman, dan mengelola kebutuhan pengguna.
    - **Tab 5 (Finansial & Transaksi Digital)**: Menambah transaksi, cek riwayat keuangan, serta sisa saldo.

## 5. Pembaruan Video Transcript dan Link Video (Middle School - Group A)
- Mengganti video link dari `S1j2gt3Up74` ke `UhutS4BVKhk` di `courseData.js`.
- Memperbarui timestamp dan bookmark pada array `bookmarks` di `courseData.js` berdasarkan transkrip video yang baru (MIT App Inventor, Input Aman, Keputusan Data, Flowchart, Privacy, Finansial).
- Waktu yang di-mapping ulang:
  - Materi 1 (Input Aman): [00:00:14], [00:04:15], [00:07:01], [00:09:11]
  - Materi 2 (Data untuk Keputusan): [00:13:24], [00:13:41], [00:19:01], [00:22:45]
  - Materi 3 (Flowchart Logika Data): [00:23:44], [00:24:59], [00:29:54], [00:33:57]
  - Materi 4 (Data & Privacy App): [00:35:18], [00:38:57], [00:42:07], [00:43:11]
  - Materi 5 (Finansial & Transaksi Digital): [00:43:52], [00:44:24], [00:53:48], [00:58:11]

## 6. Perbaikan Konfigurasi Path Vite (Grup A - D)
- Mengganti property `base` di `vite.config.js` dari `/grup-hs-2-a/` menjadi path yang sesuai dengan grup Middle School.
- Group A: `/grup-ms-2-a/`
- Group B: `/grup-ms-2-b/`
- Group C: `/grup-ms-2-c/`
- Group D: `/grup-ms-2-d/`
- Memperbarui nama pada header `README.md` masing-masing grup agar sesuai dengan nama grupnya masing-masing.

## 7. Perbaikan UI dan CSS Margin Materi (Grup A - D)
- **Problem**: Margin antar elemen (div, p, dll) di bagian materi di bawah video terlalu rapat ("mepet mepet") dan style `block-badge` (seperti `[TextBox]`) hilang karena tidak terbawa di `style.css`.
- **Action**:
  - Menambahkan baris CSS khusus untuk kelas `.block-badge` (beserta `.block-ui`, `.block-control`, `.block-logic`, `.block-math`, `.block-text`) untuk styling elemen blok ala MIT App Inventor.
  - Memperbesar `margin-bottom` pada elemen `p` di dalam `.slide-text` dari `15px` menjadi `24px` dan meningkatkan `line-height` ke `1.8`.
  - Memperlebar dan menambah margin pada `.quote-box` menjadi `margin: 40px 0;` dan padding `24px 32px` agar tulisan lebih rapi dan terlihat terpisah dari teks di atas/bawahnya.
- **Status**: Berhasil diaplikasikan ke keempat `style.css` grup MS.

## 8. Perbaikan Jarak (Margin) Antar Komponen (Grup A - D)
- **Problem**: Area `bookmarks-container` (tombol waktu di bawah video) terlalu rapat dengan kotak materi di bawahnya. Area tombol navigasi ("Modul Berikutnya") juga menempel langsung di bawah kotak materi karena class CSS yang tidak selaras (`.navigation` di CSS vs `.nav-buttons` di Vue).
- **Action**:
  - Menambahkan `margin-bottom: 36px;` pada `.bookmarks-container`.
  - Memperbaiki nama class pada CSS dari `.navigation` menjadi `.nav-buttons` (sesuai template Vue) dan memberikan `margin-top: 40px;` beserta `padding-top: 22px;`.
- **Status**: Selesai untuk Grup A - D. Jarak atas-bawah komponen utama sekarang lebih proporsional.

## 9. Penambahan Pop-up Quiz di Menit 22:17 (Tab 1)
- **Problem**: Pengguna menginginkan ada kuis pop-up (Mini Quiz 1: Form Aman) yang muncul pada menit 22:17, dan video berhenti pada titik tersebut agar siswa tidak lanjut menonton sebelum menjawab. Selain itu, UI kuis membutuhkan styling HTML pada pertanyaan (seperti `<span class="slide-title">`) namun bawaan `App.vue` hanya menggunakan teks biasa.
- **Action**:
  - Memperbarui `App.vue` (pada Grup A - D) di bagian `.quiz-question` dari `{{ currentQuestion.question }}` menjadi `v-html="currentQuestion.question"` agar format HTML seperti judul kuning (`slide-title`) bisa dirender.
  - Menambahkan data kuis ke dalam array `quizzes` di `courseData.js` pada Modul 1 dengan konfigurasi:
    - `time: 1337` (menit 22:17).
    - `resume: false` (agar video tidak otomatis berlanjut setelah kuis).
    - Memasukkan pilihan ganda (A, B, C) sesuai screenshot dengan jawaban yang benar pada `TextBoxNama.Text = ""`.
- **Status**: Selesai. Kuis sekarang akan muncul pada detik 1337 (22:17) dengan format styling (judul kuning) yang sesuai dengan desain UI.

## 10. Pemotongan Durasi Video & Tab Mini Project (Grup A)
- **Problem**: Player video masih menampilkan keseluruhan durasi (63:54) padahal pengguna ingin video terpotong dan berhenti di menit akhir materi. Pengguna juga ingin menambahkan tab "Mini project" setelah Tab 1.
- **Action**:
  - Mengubah cara `App.vue` menghitung durasi progress video. Menambahkan dukungan konfigurasi `endSeconds` dari `courseData.js` agar video memiliki "batas akhir virtual".
  - Jika `endSeconds` dikonfigurasi, durasi total yang ditampilkan player adalah (`endSeconds - startSeconds`), bukan durasi mentah video asli. Video juga akan tertahan dan otomatis pause bila menyentuh batas `endSeconds`.
  - Mengupdate `courseData.js` Grup A dengan:
    - Tab 1 diberikan batas `startSeconds: 14` dan `endSeconds: 1338` (22:18).
    - Menambahkan Tab 2 baru: "Mini Project Form Aman" dengan rentang video `startSeconds: 1349` (22:29) sampai `endSeconds: 1392` (23:12).
    - Menggeser urutan tab lama (2 ke 3, 3 ke 4, dst).
- **Status**: Selesai untuk Grup A. Tab 1 sekarang hanya menampilkan durasi sampai menit 22:18, dan ada Tab 2 khusus untuk Mini project.

## 11. Penyesuaian Video Tab 3 (Flowchart) & Fix Waktu Mulai Tab 1
- **Problem**: Pengguna ingin Tab 3 (Flowchart) khusus menampilkan rentang video dari menit 23:14 sampai 34:39. Selain itu, Tab 1 sebelumnya terpotong di awal karena start pada detik 14.
- **Action**:
  - Mengubah `startSeconds` di Tab 1 menjadi `0` agar video utuh mulai dari awal (0:00).
  - Mengupdate konfigurasi di `courseData.js` untuk Tab 3 ("Flowchart Logika Data") dengan `startSeconds: 1394` (23:14) dan `endSeconds: 2079` (34:39).
- **Status**: Selesai. Tab 1 sekarang mulai dari awal, dan Tab 3 menampilkan durasi 11 menit 25 detik sesuai potongan video.

## 12. Fix UI Pop-up Quiz & Logika Kesempatan Menjawab (Grup A)
- **Problem**: Pengguna merasa layout popup kuis aneh karena ada header biru (dengan ikon kuning "?") dan ada notifikasi "Sudah 3 kali mencoba..." meskipun baru klik 1 kali. Pengguna ingin kalau salah bisa langsung lanjut.
- **Action**: 
  - Membatalkan penghapusan `<header class="quiz-header">` (header biru dikembalikan karena ternyata bukan itu yang dimaksud).
  - Menghapus badge `<span class="slide-title">Mini Quiz: Form Aman</span>` (kotak kuning) dari teks pertanyaan di `courseData.js` sesuai maksud dari user.
  - Mengubah fungsi `handleStandardAnswer` dan `registerFailedInputAttempt` di `App.vue` sehingga pengguna cukup salah **1 kali** saja untuk memunculkan tombol "Lanjut" (tidak perlu ditahan sampai 3 kali mencoba).
- **Status**: Selesai untuk Grup A. Layout popup kuis sekarang lebih rapi tanpa header, dan pengguna bisa langsung lanjut meskipun salah menjawab.

## 13. Fitur Upload Project (Tab 2) & Console Debugging Progress
- **Problem**: Pengguna ingin siswa bisa mengumpulkan Mini Project di Tab 2 melalui link galeri MIT App Inventor atau file .aia. Selain itu, ada kendala dimana Tab selanjutnya tidak mau terbuka meskipun popup kuis dan video sudah selesai.
- **Action**:
  - Menambahkan UI khusus di `App.vue` (muncul di bawah video pada Tab 2) yang memuat input form untuk link galeri atau upload file `.aia`.
  - Memperbarui `Code.gs` untuk Grup `gms2a` agar bisa menguraikan data `base64` dan membuat file tersebut di Google Drive yang ditentukan (`1LShQpFJ_aAQ1sFmVSGbULd90XIx4aUnR`) dengan nama terformat (`siswa_sekolah_grupA_mini project A_nama file.aia`).
  - Menambahkan kolom header baru `Project1_Code` di Apps Script untuk menyimpan *link* file Drive atau link galeri.
  - Menambahkan output `console.log` di dalam `isStepFinished()` di `App.vue` (`[Step X Debug] Video Watched: ... Quizzes Completed: ...`) persis seperti di format sesi 25-26 Highschool untuk memudahkan proses *debugging* *bug* tab tidak bisa di-klik.
- **Status**: Selesai. Komponen unggah project sudah terpasang di Tab 2 dan log debug progress sudah jalan.

## 14. Perbaikan Bug Video Watched Status & Kuis Tidak Muncul
- **Problem**: Pengguna melaporkan bahwa saat mereka *scrub* (menggeser) video sampai akhir, status video tidak ter-update menjadi selesai, kuis tidak muncul (padahal sudah waktunya), dan meminta info *CurrentTime* dihilangkan dari *console log* agar lebih ringkas. Selain itu, kuis tidak mau muncul jika video di-replay tanpa di-refresh halamannya.
- **Action**:
  - Menghapus output `CurrentTime` dari *console log* sehingga hanya menampilkan status "Video Watched" dan "Quizzes".
  - Mengubah fungsi `enforceVideoStartBoundary` di `App.vue`: Ketika video dipaksa berhenti (*pause*) karena menyentuh batas akhir durasi (`endBoundary`), sistem sekarang akan secara eksplisit menandai `videoWatchedStatus` menjadi `true`, mencetak *log*, lalu segera memanggil `checkVideoQuizzes` agar kuis yang berada di detik akhir tetap terpicu.
  - Memindahkan *state tracking* status kemunculan kuis dari properti data mentah `courseData.js` (`quiz.shown`) ke dalam sistem reaktif Vue di `App.vue` (`quizState.shownQuizzes`). Dengan demikian, sistem akan dengan mulus mendeteksi kuis setiap kali status diperbarui (atau *hot-reloaded*).
- **Status**: Selesai. Log telah bersih dan kuis pada video 1 (detik 1337) sudah bisa terbuka saat video menyentuh garis akhir (detik 1338).

## 15. Perbaikan Teks Debug Log yang Bernilai "undefined"
- **Problem**: Saat kuis muncul dan status di *console log* dicetak, angkanya menjadi `undefined/undefined` (misalnya `Quizzes: undefined/undefined`). Pengguna juga meminta agar format log disamakan persis dengan milik Highschool sesi 25-26.
- **Action**:
  - Mengecek fungsi `getStepQuizProgress()` yang digunakan untuk menghitung progres kuis. Ternyata properti yang di-*return* adalah `recordedCompletedCount` dan `total`, BUKAN `completedCount` dan `totalQuizzes`.
  - Mengubah pemanggilan nama variabel di dua tempat *console.log* dalam file `App.vue`:
    1. Di fungsi `updateVideoControls`: Dari `${quizProgress.completedCount}/${quizProgress.totalQuizzes}` menjadi `${quizProgress.recordedCompletedCount}/${quizProgress.total}`.
    2. Di fungsi `isStepFinished`: Dari `Quizzes Completed: ${quizProgress.completedCount} / ${quizProgress.totalQuizzes}` menjadi `Quizzes Completed: ${quizProgress.recordedCompletedCount} / ${quizProgress.total}`.
- **Status**: Selesai. Format log sudah sama persis dengan sistem Highschool dan nilainya dapat dicetak dengan benar.

## 16. Mendesain Ulang UI Area Pengumpulan Project
- **Problem**: Desain area pengumpulan project (Tab 2) terlihat kaku, *margin* atas dan bawahnya jelek (kelihatan terpisah dengan materi bacaan), serta *copywriting* dan tombolnya kurang elegan.
- **Action**:
  - Memindahkan posisi kotak upload dari luar ke **dalam** elemen `reading-container` persis di bawah ringkasan *Mini Project*, sehingga secara semantik dan visual menyatu dengan blok materi biru muda.
  - Merombak *copywriting* menjadi lebih rapi dan jelas (cth: "Kumpulkan Mini Project", "Pilih metode untuk mengumpulkan kreasi aplikasi MIT App Inventor milikmu.").
  - Memperbaiki desain *form* secara signifikan menggunakan desain *premium* (seperti efek batas *dashed* pada kotak utama, dua tombol besar yang responsif untuk memilih "Link" atau "File" lengkap dengan *subtext* dan efek *hover*, serta desain tombol *submit* bergaya pil (*rounded-full*) dengan bayangan halus).
  - Menyederhanakan tampilan tautan tutorial video ke bagian bawah formulir (dengan gaya teks *inline* panah) agar terlihat lebih estetik.
- **Status**: Selesai. Form pengumpulan project sekarang menyatu dengan materi bacaan dan memiliki desain UI premium yang jauh lebih memanjakan mata.

## 17. Memperbaiki Teks Unreadable pada Form Upload Project
- **Problem**: Desain Form Upload yang baru saja ditambahkan ternyata teksnya tidak terbaca (hitam/gelap di atas *background* transparan bintang-bintang). Hal ini karena kode sebelumnya memakai variabel CSS dari versi *Highschool* (`--color-surface`, `--color-primary-dark`, `--color-text-light`) yang sama sekali **tidak ada** (*undefined*) di sistem *Middleschool*. Akibatnya, *background* menjadi transparan dan warna teks kembali ke *default*.
- **Action**: 
  - Mengubah semua referensi variabel CSS di blok `project-upload-area` agar sinkron dengan variabel yang ada di `style.css` Middleschool.
  - Memakai `var(--paper)` untuk membuat kotaknya menjadi putih pekat sehingga teks di atasnya sangat jelas dan terbaca.
  - Memakai `var(--navy)`, `var(--ink)`, dan `var(--muted)` untuk warna teks, serta `var(--blue)` untuk interaksi utama (tombol, *hover*, dan *border*).
- **Status**: Selesai. Kotak *upload* sekarang akan selalu memiliki *background* putih solid sehingga tulisan apapun di dalamnya tetap cerah dan sangat *readable*.

## 18. Mengatur Logika Kunci Modul (90%/95% Watch Time & Wajib Upload Project)
- **Problem**: Pengguna bisa lanjut ke modul berikutnya tanpa benar-benar menonton durasi video atau mengumpulkan *mini project* di tab 2. 
- **Action**:
  - Mengubah cara aplikasi menandai video selesai ditonton. Jika tab memiliki kuis, siswa wajib menonton **90%** dari durasi. Jika tidak ada kuis, siswa wajib menonton **95%** dari durasi. Status `videoWatchedStatus` otomatis aktif saat batas ini tersentuh.
  - Menambahkan pengecekan khusus pada fungsi `isStepFinished` untuk tab 2 (Mini Project). Siswa sekarang wajib men-submit project (link/file) hingga `Project1_Code` tersimpan sebelum bisa mengakses modul berikutnya.
  - Memperbarui `getStepBlockingNotice` untuk memunculkan pesan peringatan khusus "kamu belum mengumpulkan form project (link atau file .aia)" jika syarat *upload* belum dipenuhi.
- **Status**: Selesai. Sistem sekarang jauh lebih ketat mengawasi progres menonton dan pengumpulan project sebelum memperbolehkan siswa pindah ke materi selanjutnya.

## 19. Menonaktifkan Sementara Kewajiban Pengumpulan Project
- **Problem**: Kewajiban pengumpulan *project* mengganggu kelancaran proses *testing* secara keseluruhan karena tester harus terus-menerus men-submit file/link untuk pindah ke tab 3.
- **Action**: Mematikan (meng-*comment-out*) logika validasi `studentProgress.value['Project1_Code']` di dalam fungsi `isStepFinished` dan pesan blokirannya. Terdapat komentar `// TODO: Buka komentar ini saat akan push ke Git` sebagai pengingat.
- **Status**: Selesai. Saat testing, *user* dapat melompat dari tab 2 ke tab 3 hanya dengan menyelesaikan *watch-time* 95% saja.

## 20. Memperbaiki Bug Progress Bar Video Selalu Kembali ke Awal
- **Problem**: Saat *user* menggeser (`scrub`) *time bar* pada *custom video control*, video tidak pindah ke titik yang dituju, melainkan selalu mengulang/meloncat ke titik awal mula pemotongan (`startBoundary`).
- **Action**: Memperbaiki rumus kalkulasi di `onSeekInput`. Sebelumnya aplikasi langsung memasukkan persentase durasi ke dalam fungsi `seekTo()` milik YouTube. Karena pemotongan *startBoundary* bisa saja tidak di detik 0, maka persentase durasi harus ditambahkan dengan `startBoundary` tersebut (`startBoundary + offsetTime`).
- **Status**: Selesai. *Progress bar* video di seluruh modul kini berjalan sinkron dan akurat saat digeser.

## 21. Menambahkan Pop-Up Quiz "Urutan Flowchart" di Tab 3
- **Problem**: Tab 3 (Flowchart) perlu ditambahkan kuis pop-up interaktif pada detik-detik terakhir video (menit 34:39 / detik 2079) sesuai dengan materi yang diberikan.
- **Action**: Memasukkan objek konfigurasi kuis ke dalam *array* `quizzes` milik modul 3 di `courseData.js`. Pop-up kuis akan otomatis menahan video pada detik ke-2079 dan menyajikan pertanyaan tentang urutan pembuatan program (Input -> Proses -> Output).
- **Status**: Selesai. Kuis otomatis muncul dengan persis sesuai gambar yang diminta pada penghujung pemutaran Tab 3.

## 22. Menyesuaikan Durasi Tab 4 dan Menambahkan Pop-Up Quiz "Data Privacy"
- **Problem**: Video untuk Tab 4 (Data & Privacy App) belum dipotong durasinya dan belum dipasangi *pop-up quiz* di akhir videonya.
- **Action**:
  - Menambahkan batas awal pemotongan (`startSeconds: 2096` / 34:56) dan batas akhir (`endSeconds: 2572` / 42:52) ke dalam konfigurasi modul 4 di `courseData.js`.
  - Menambahkan *pop-up quiz* pilihan ganda tentang "Data Privacy" yang dimunculkan 5 detik sebelum video selesai (tepatnya di detik ke-2567).
- **Status**: Selesai. Tab 4 sekarang hanya memutar materi yang relevan, dan *pop-up quiz* otomatis muncul sebelum video berakhir.

## 23. Membuat Tab 5 Baru (Mini Project Cek Pesan Aman) & Update Upload Area
- **Problem**: Pengguna menginginkan tab khusus (Tab 5) untuk *Mini Project* berikutnya, dengan video instruksi pada menit 43:04 - 43:38 dan ada tempat upload project persis seperti di Tab 2.
- **Action**:
  - Mengubah urutan Tab 5 lama ("Finansial & Transaksi Digital") menjadi Tab 6 di `courseData.js`.
  - Membuat konfigurasi Tab 5 baru untuk "Mini Project Cek Pesan Aman" dengan potongan video mulai dari `startSeconds: 2584` hingga `endSeconds: 2618`.
  - Memodifikasi `App.vue` agar form *upload area* yang tadinya hanya terbuka di `currentStep === 2`, sekarang juga tampil untuk `currentStep === 5`.
  - Menyesuaikan kode penyimpan data (`saveProgress` dan `submitProject`) sehingga project Tab 5 otomatis tersimpan di kolom data Sheets terpisah (menggunakan `Final_Project_Code` sesuai *schema* yang ada).
  - Membuat logika navigasi tombol "Selanjutnya" bisa menyesuaikan secara dinamis berapapun jumlah total tab yang ada.
- **Status**: Selesai. Tab 5 sekarang siap dipakai untuk mengumpulkan Mini Project kedua, dan materi Finansial aman tergeser ke Tab 6.

## 24. Menyesuaikan Judul dan Durasi Tab 6
- **Problem**: Materi Finansial (sekarang Tab 6) perlu dibatasi videonya sesuai topik analisis data finansial, dengan judul tab yang lebih pas dan tanpa pop-up kuis.
- **Action**:
  - Mengubah judul Tab 6 di `courseData.js` menjadi "Menganalisis Data Finansial".
  - Menambahkan pemotongan durasi video mulai menit 43:41 (`startSeconds: 2621`) sampai 47:24 (`endSeconds: 2844`).
  - Memastikan *array* `quizzes` dikosongkan (`[]`) agar tidak ada kuis pop-up yang muncul di tab ini.
- **Status**: Selesai. Tab 6 kini sudah sesuai instruksi dengan durasi yang tepat.

## 25. Membuat Tab 7 Baru (Mini Project C) & Menambah Kolom Spreadsheet
- **Problem**: Perlu tab baru (Tab 7) untuk mengumpulkan "Mini Project C" dengan video instruksi pada menit 47:27 - 50:00. Format nama file dan komponen upload harus sama seperti Mini Project A (Tab 2) dan Mini Project B (Tab 5).
- **Action**:
  - Menambahkan kolom baru `Project2_Code` (untuk Tab 5) dan `Project3_Code` (untuk Tab 7) pada daftar *headers* di file `Code.gs` untuk Grup `gms2a`. Hal ini dilakukan agar data masing-masing *project* tidak saling menimpa.
  - Membuat objek konfigurasi Tab 7 di `courseData.js` dengan judul "Mini Project C" dan potongan durasi `startSeconds: 2847` hingga `endSeconds: 3000`.
  - Mengubah logika penyimpanan di `App.vue` (`submitProject`) sehingga secara dinamis akan menggunakan penamaan khusus:
    - Tab 2 → `mini project A`, tersimpan di kolom `Project1_Code`
    - Tab 5 → `mini project B`, tersimpan di kolom `Project2_Code`
    - Tab 7 → `mini project C`, tersimpan di kolom `Project3_Code`
  - Memastikan validasi kunci progres (`isStepFinished` dan notifikasi pemblokiran) mengenali Tab 7 sebagai kewajiban *upload* baru.
- **Status**: Selesai. Form upload sekarang sudah muncul di Tab 2, 5, dan 7 dengan format penamaan file (`siswa_sekolah_grupA_mini project C_nama file.aia`) serta kolom penyimpanan yang sesuai.

## 26. Membuat Tab 8 (Keamanan dalam Bertransaksi Digital) dengan Pop-up Quiz
- **Problem**: Pengguna meminta tab baru (Tab 8) untuk materi "Keamanan dalam Bertransaksi Digital", dengan video yang dibatasi dari menit 52:35 hingga 1:01:23, dan ditambahkan kuis keamanan di akhir videonya.
- **Action**:
  - Menambahkan konfigurasi Tab 8 di `courseData.js` dengan memotong video pada `startSeconds: 3155` dan `endSeconds: 3683`.
  - Memasang pop-up quiz baru berjudul "Mini Quiz: Finansial & Keamanan" di detik terakhir video (detik 3683). Pilihan ganda dan teks pertanyaannya dibuat sesuai draf gambar.
- **Status**: Selesai. Tab 8 berhasil ditambahkan dengan durasi pemutaran yang sesuai dan kuis keamanan otomatis muncul di bagian akhir video.

## 27. Membuat Tab 9 (Final Project)
- **Problem**: Pengguna meminta tab khusus untuk mengumpulkan Final Project, dengan video instruksi yang berawal di menit 1:01:40 sampai selesai. Fitur upload harus disamakan dengan mini project sebelumnya, dan nama file diubah dengan format final project.
- **Action**:
  - Membuat objek konfigurasi Tab 9 di `courseData.js` dengan `startSeconds: 3700`.
  - Mengupdate form unggah project di `App.vue` agar ikut muncul ketika berada di Tab 9 (`currentStep === 9`).
  - Mengubah logika penyimpanan nama file dan destinasi kolom untuk Tab 9:
    - Format nama file: `siswa_sekolah_grupA_final project_nama file.aia`
    - Tersimpan di kolom: `Final_Project_Code` (yang sudah ada secara *default* di `Code.gs` untuk `gms2a`).
  - Menambahkan pengenalan Tab 9 di logika validasi wajib unggah (`isStepFinished` dan `getStepBlockingNotice`).
- **Status**: Selesai. Tab 9 siap digunakan untuk keperluan instruksi dan pengumpulan Final Project.

## 28. Menampilkan Sandbox Instruksi Final Project di Tab 9
- **Problem**: Pengguna ingin agar instruksi Final Project (yang diambil dari file presentasi HTML utama) bisa dibaca langsung oleh siswa di dalam materi Tab 9.
- **Action**: 
  - Mengekstrak *Slide 43 sampai 45* (Tantangan Akhir, Langkah Praktik, dan Rubrik Penilaian) dari `slide_deck_part1.html` menjadi file HTML baru yang ringan (`sandbox_finalproject.html`) yang khusus menyajikan instruksi.
  - Memasangkan *file* presentasi mini ini ke dalam tab `summaryHtml` di Tab 9 menggunakan tag `<iframe>` dengan *styling* yang disesuaikan dengan tema aplikasi.
- **Status**: Selesai. Instruksi presentasi untuk tugas akhir sudah langsung tertanam di bawah video Tab 9.

## 29. Finalisasi Koneksi Data ke Google Sheets (`Code.gs`)
- **Problem**: Konfigurasi kolom (header) di `Code.gs` untuk Grup `gms2a` masih menyimpan banyak kolom tidak relevan dari grup lain (seperti `V2_Q10`, `V6_IDE`, dll.), dan ada *bug* kecil di mana setiap upload file `.aia` akan menimpa kolom `Project1_Code` tanpa memedulikan di tab mana siswa sedang berada.
- **Action**:
  - Merevisi `headers` array untuk `gms2a` di dalam `Code.gs`. Sekarang hanya menyimpan data riwayat spesifik yang benar-benar ada di modul ini: 
    - **Kuis**: `V1_Q1`, `V3_Q1`, `V4_Q1`, dan `V8_Q1` (kolom `_Ans` dan `_Att`).
    - **Project**: `Project1` (Tab 2), `Project2` (Tab 5), `Project3` (Tab 7), dan `Final_Project` (Tab 9).
  - Memperbaiki `handleFileUpload` di `App.vue` agar kolom yang disimpan saat siswa mengunggah file menyesuaikan dengan variabel `fileCol` yang sedang aktif di tab terkait, bukan di-*hardcode* ke `Project1_Code`.
- **Status**: Selesai. Semua *progress* quiz dan project dipastikan akan masuk ke kolom yang tepat di *Spreadsheet*.

---

# Changelog & Update Log: Middleschool Grup B Dashboard

## 30. Sinkronisasi Data Video & Modul Grup B
- **File Diubah:** `src/courseData.js`
- **Perubahan:**
  - Mengubah seluruh `videoId` menjadi `cWfbcaSg7Eo` sesuai referensi Grup B.
  - Memperbarui `courseData.js` dengan membagi materi ke dalam 5 Tab berdasarkan transkrip, yakni Eksplorasi Data Pribadi, Etika Digital, Konsep TinyDB, CRUD TinyDB, dan diakhiri dengan Mini Project Tiny DB.
  - Mengubah parameter durasi `startSeconds` dan `endSeconds` yang spesifik pada masing-masing tab serta _bookmarks_ berdasarkan transkrip.
  - Karena instruksi pengguna menyatakan kuis _pop-up_ akan dimasukkan perlahan sambil di-QC nanti, untuk sementara kuis tidak dimunculkan di dalam _array_ `quizzes`.
- **Status**: Selesai.

## 31. Replikasi Fitur Utama dari Grup A ke Grup B
- **File Diubah:** `src/App.vue`
- **Perubahan:**
  - Melakukan replikasi file `App.vue` terbaru dari Grup A ke Grup B agar seluruh fitur unggulan (video UI lock 95%, form _submit project_ premium, _progress bar bug fix_, dsb) ikut terbawa.
  - Mengubah seluruh penyebutan label statis "Grup A" menjadi "Grup B".
  - Mengubah kondisi _tab mapping_ untuk _upload_ agar area _upload project_ hanya dimunculkan di **Tab 5** (sesuai posisi "Mini Project Tiny DB").
  - Menyelaraskan logika validasi perpindahan _step_ dan blokir notifikasi (melalui modifikasi `isStepFinished`) agar mengecek _submission_ `Project1_Code` pada Step 5 saja.
- **Status**: Selesai. Form project submission berfungsi dan terpusat di Tab 5.

## 32. Penambahan Konfigurasi Spreadsheet untuk Grup B Middle School
- **File Diubah:** `Code.gs`
- **Perubahan:** Menambahkan blok inisialisasi `if (group === 'gms2b')` untuk mengarahkan pengumpulan data progress Grup B ke _sheet_ bernama `ops-student-result-gms2b`.
- **Header Didaftarkan**: `Timestamp`, `Students_Name`, `Students_School`, `Students_Email`, `Project1_Code`, `Project1_Attempts`, `Project1_Score`. 
## 33. Penambahan Log Status Tracking UI (Console Debug)
- **File Diubah:** `src/App.vue`
- **Perubahan:**
  - Menambahkan *explicit console logs* agar instruktur/developer dapat melacak alur *user journey* langsung dari Console Browser (*Developer Tools*), menjawab kebutuhan monitoring "kapan pop-up muncul, kapan tugas dikerjakan, progres disinkronkan, hingga tab berikutnya terbuka".
  - Log yang ditambahkan meliputi:
    1. `[DEBUG] Pop-up kuis muncul. Mode Resume: ...` di dalam fungsi `openQuiz`.
    2. `[DEBUG] File project ... berhasil diunggah ...` di dalam fungsi `submitProject` untuk melacak pengiriman jawaban.
    3. `[DEBUG] Progress berhasil dikirim (sync) ke Google Sheets ...` di dalam fungsi `syncToSheets`.
    4. `[DEBUG] Tab berpindah dari Materi [X] ke Materi [Y].` di dalam fungsi `nextStep`.
- **Status**: Selesai. *Tracking status UI* ini terpasang secara seragam untuk seluruh interaksi kritis pengguna.

## 34. Penambahan Materi Bacaan Terstruktur di Bawah Video Grup B
- **File Diubah:** `src/courseData.js`
- **Perubahan:**
  - Menghapus rencana pembuatan file HTML terpisah (`sandbox_materi*.html`). Sebagai gantinya, langsung merangkum seluruh teks dari slide presentasi (`slide_deck_part1.html`) milik Grup B.
  - Memasukkan rangkuman materi tersebut secara manual ke dalam objek `summaryHtml` di `courseData.js` untuk kelima tab (Eksplorasi Data Pribadi, Etika, TinyDB, Mengelola Data, dan Mini Project).
  - Menerapkan format struktur HTML yang seragam dan elegan bergaya *native* seperti Grup A, dengan komponen seperti `<header class="reading-header">`, `<article class="reading-section">`, `<div class="info-grid">`, `<div class="mini-card">`, dan `<span class="block-badge block-ui">`.
- **Status**: Selesai. Seluruh instruksi dan materi bacaan kini ditanamkan langsung dalam kode (sama seperti struktur Group A) sehingga lebih mulus dan ringan.

## 35. Hotfix: CSS Tampilan Accordion Materi Bacaan di Mobile/Tablet
- **File Diubah:** `grupA/dashboard/src/style.css` dan `grupB/dashboard/src/style.css`
- **Perubahan:**
  - Menemukan *bug* desain di mana blok CSS untuk `details.lesson-reading-accordion` sebelumnya terperangkap (nested) di dalam aturan media query `@media (max-width: 650px)`.
  - Hal ini menyebabkan tampilan pada layar *tablet* atau *mobile* dengan *viewport width* > 650px (termasuk saat mode *landscape* atau resolusi *device* tinggi) menjadi transparan. Pengguna tidak menyadari bahwa tulisan "► Buka Materi Bacaan" adalah tombol, karena desain kotaknya (*background* putih, *border*) hilang sepenuhnya.
  - Memindahkan blok CSS tersebut menjadi aturan gaya bawaan (*global/base styles*) di luar *media query* tersebut. Kini elemen `<details>` materi bacaan akan selalu memiliki bingkai kotak (*card*) putih yang jelas dan bisa diklik oleh *user* di perangkat apapun dengan mulus.
- **Status**: Selesai. Masalah visibilitas UI di tampilan mobile/tablet telah ditangani untuk Grup A dan Grup B.

## 36. Implementasi Pop-up Kuis dan Fast-Forward pada Video 1 Grup B
- **File Diubah:** `grupB/dashboard/src/App.vue` dan `grupB/dashboard/src/courseData.js`
- **Perubahan:**
  - Menambahkan *property* baru `skipTo` di dalam data kuis. Modifikasi logika pada fungsi `enforceVideoStartBoundary` di `App.vue` agar video akan secara otomatis melompat (*skip*) ke batas akhir rentang waktu kuis apabila pengguna mencoba menarik mundur (*rewind*/*seek backwards*) ke dalam rentang durasi kuis yang sudah dilewati.
  - Mengubah durasi aktif Video 1 menjadi **00:02 (detik ke-2)** hingga **14:47 (detik ke-887)**.
  - Memasukkan 3 Pop-up Kuis interaktif pada titik-titik waktu berikut:
    - **Kuis 1:** Muncul di `08:03`. Setelah dijawab, video akan di-*fast-forward* ke `08:08` (rentang `08:03 - 08:08` tidak bisa diputar ulang).
    - **Kuis 2:** Muncul di `12:15`. Setelah dijawab, video di-*fast-forward* ke `12:20` (rentang `12:15 - 12:20` di-*skip*).
    - **Kuis 3:** Muncul di bagian akhir video yaitu `14:47`.
- **Status**: Selesai. Fitur ini memaksa *student* berinteraksi saat belajar, menyingkirkan bagian kuis versi statis di video, dan mencegah mereka kembali menonton bagian statis kuis yang sudah digantikan oleh *pop-up*.

## 37. Implementasi Pop-up Kuis dan Praktik Interaktif pada Video 2 Grup B
- **File Diubah:** `grupB/dashboard/src/App.vue` dan `grupB/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 2 (Etika & Tanggung Jawab Digital) menjadi **14:59 (detik ke-899)** hingga **28:21 (detik ke-1701)**.
  - Menambahkan *global function* baru `window.checkPasswordGuess` di dalam `App.vue` untuk memvalidasi latihan pembuatan *password* kuat secara interaktif dengan *Regex* (huruf besar, huruf kecil, angka, simbol khusus, minimal 8 karakter).
  - Memasukkan 4 sesi interaktif pada titik-titik waktu berikut:
    - **Kuis 4:** Muncul di `21:13`. Setelah dijawab, video di-*fast-forward* ke `21:18`.
    - **Latihan Praktik (Sandbox):** Muncul di `23:28`. Menggunakan input *text* kustom yang terhubung ke validasi sandi rahasia. Setelah lolos, video di-*fast-forward* ke `23:33`.
    - **Kuis 5:** Muncul di `25:48`. Setelah dijawab, video di-*fast-forward* ke `25:53`.
    - **Kuis 6:** Muncul di akhir video yaitu `28:20`.
- **Status**: Selesai. Fitur latihan membuat *password* kuat kini menjadi bagian dari presentasi secara organik.

## 38. Hotfix: Tombol Pilihan Ganda Kuis Hilang
- **File Diubah:** `grupA/dashboard/src/App.vue` dan `grupB/dashboard/src/App.vue`
- **Perubahan:**
  - Memperbaiki fungsi pembaca data `getQuestionChoices` di dalam `App.vue`. Sebelumnya, *engine* kuis hanya secara kaku mencari *key* `choices` dari data sumber, sementara kuis baru kita memakai standar *key* `options`.
  - Hal ini menyebabkan tombol *multiple choice* (A, B, C) tidak di-*render* sama sekali karena terdeteksi kosong.
  - Memperbarui fungsi rendering agar bisa membaca format `question.choices` maupun `question.options` sekaligus.
- **Status**: Selesai. Tombol opsi pada seluruh kuis pop-up kini sudah muncul kembali.

## 39. Implementasi Pop-up Kuis pada Video 3 Grup B
- **File Diubah:** `grupB/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 3 (Mengenal Database Lokal) menjadi **28:35 (detik ke-1715)** hingga **42:27 (detik ke-2547)**.
  - Memasukkan 2 sesi Pop-up Kuis interaktif pada titik-titik waktu berikut:
    - **Kuis 7:** Muncul di `34:50` (Konsep TinyDB/To-Do List). Setelah dijawab, video di-*fast-forward* ke `34:52`.
    - **Kuis 8:** Muncul di akhir video yaitu `42:26` (Fungsi 'Tag' dalam TinyDB).
- **Status**: Selesai. Video 3 sekarang sudah dilengkapi dengan asesmen otomatis yang mengunci video sampai siswa selesai menjawab.

## 40. Hotfix: Menyesuaikan Waktu Mulai Video 3
- **File Diubah:** `grupB/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengembalikan titik awal (*start time*) Video 3 ke `28:35` (detik ke-1715) sesuai instruksi awal yang sudah memperhitungkan *intro* 4 detik sebelum sapaan "Halo teman-teman".
- **Status**: Selesai. Video 3 kini diputar tepat dari `28:35`.

## 41. Implementasi Pop-up Kuis pada Video 4 Grup B
- **File Diubah:** `grupB/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 4 (Mengelola Data Aman di TinyDB) menjadi **42:35 (detik ke-2555)** hingga **54:32 (detik ke-3272)**.
  - Memasukkan 2 sesi Pop-up Kuis interaktif pada titik-titik waktu berikut:
    - **Kuis 9:** Muncul di `48:12` (Logika penimpaan data StoreValue). Setelah dijawab, video di-*fast-forward* ke `48:16`.
    - **Kuis 10:** Muncul di `50:41` (Penggunaan blok ClearTag). Setelah dijawab, video di-*fast-forward* ke `50:50`.
- **Status**: Selesai. Video 4 sekarang memiliki durasi dan kuis yang tepat.

## 42. Penyesuaian Durasi Video 5 Grup B
- **File Diubah:** `grupB/dashboard/src/courseData.js`
- **Perubahan:**
  - Menetapkan batas pemutaran (*play bounds*) untuk Video 5 (Mini Project Tiny DB) mulai dari **54:45 (detik ke-3285)** hingga **55:23 (detik ke-3323)**.
  - Memperbarui waktu *bookmark* "Instruksi Mini Project" ke detik ke-3285.
- **Status**: Selesai. Video 5 sekarang sudah tayang sesuai instruksi.

## 43. Desain Thumbnail Baru (Grup B)
- **Proses:** Membuat sebuah *script* otomatis berbasis Node.js (`generate_thumbs.js`) yang me-render desain HTML *thumbnail* dengan *style* yang mirip dengan PPT materi asli, lalu di-*screenshot* secara otomatis menggunakan Puppeteer.
- **File Diubah:** `grupB/dashboard/src/courseData.js` dan menambahkan `thumb_1.png` hingga `thumb_5.png` ke folder `public/`.
- **Perubahan:**
  - Thumbnail 1: Eksplorasi Data Pribadi
  - Thumbnail 2: Etika dan Tanggung Jawab Digital
  - Thumbnail 3: Penyimpanan Data dengan TinyDB
  - Thumbnail 4: Mengelola Data Aman di TinyDB
  - Thumbnail 5: Mini Project Tiny DB
  - Memasukkan atribut `thumbnail` baru ke masing-masing *step* video di `courseData.js`.
- **Status**: Selesai. Semua thumbnail sekarang tampil lebih cantik dan relevan dengan judul video.

## 44. Perbaikan Deployment Github Pages (Grup A & Grup B)
- **Masalah:** Halaman *dashboard* Github Pages tidak dapat diakses (404 Not Found) setelah kode di-*push*.
- **Penyebab:** 
  1. File `deploy.yml` berada di dalam folder `dashboard/`, sehingga *workflow* Github Actions tidak terdeteksi oleh Github.
  2. Saat *workflow* dipindahkan ke *root*, Github menolak proses *deploy* karena aturan proteksi *environment* `github-pages` secara *default* hanya mengizinkan deploy dari *branch* `main` (sedangkan repositori sebelumnya menggunakan `master`).
- **Penyelesaian:**
  - Memindahkan folder `.github` ke *root* repositori.
  - Menyesuaikan konfigurasi direktori `working-directory: ./dashboard` di `deploy.yml` agar perintah Node berjalan di folder yang tepat.
  - Memaksa pembaruan *branch* dari `master` menjadi `main` di repositori jarak jauh (`grup-ms-2-a` dan `grup-ms-2-b`).
- **Status:** Selesai. *Workflow* Actions berjalan dengan lancar dan Github Pages berhasil di-deploy.

---

# Changelog & Update Log: Middleschool Grup C Dashboard

## 45. Initial Setup Course Data Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Melakukan mapping transkrip materi grup C (dari rentang 00:00:10 hingga 00:32:06) ke dalam 6 modul tab dashboard.
  - Mengekstrak `summaryHtml` secara dinamis dari `slide_deck_grupC_extended.html`.
  - Mengupdate properti durasi dan *bookmarks* untuk 6 modul: 
    - Modul 1: Logika di Dunia Nyata
    - Modul 2: Percabangan Blok
    - Modul 3: Uang Digital
    - Modul 4: Needs vs Wants
    - Modul 5: Aplikasi Kalkulator Keuangan
    - Modul 6: Final Project (Pengganti Kehadiran)
- **Status**: Selesai. Konfigurasi struktur data materi Grup C sudah disiapkan.

## 46. Update Desain UI Rangkuman Materi (Grup C)
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah *template* HTML dari properti `summaryHtml` pada semua modul agar secara struktur identik dengan format yang dipakai di Grup B (contoh: pemisahan `<header class="reading-header">` dan `<article class="reading-section">`).
  - Menghapus otomatis *slide* yang bertipe kuis pop-up dari bacaan materi sehingga teks di bawah video murni berisi materi/rangkuman tanpa adanya teks "Kuis ...".
- **Status**: Selesai. Tampilan materi di bawah video sekarang rapi dan elegan, konsisten dengan Grup B.

## 47. Implementasi Pop-up Kuis pada Video 1 Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 1 (Modul 1: Logika di Dunia Nyata) menjadi **00:03 (detik ke-3)** hingga **07:52 (detik ke-472)**.
  - Memasukkan 2 Pop-up Kuis interaktif pada titik-titik waktu berikut:
    - **Kuis 1 (Logika Dasar):** Muncul di `05:31`. Setelah dijawab, video akan di-*fast-forward* ke `05:36` (rentang `05:31 - 05:36` tidak bisa diputar ulang).
    - **Kuis 2 (Flowchart):** Muncul di bagian akhir video yaitu `07:52`.
- **Status**: Selesai. Pop-up kuis Modul 1 sudah aktif dan menggantikan tayangan kuis statis pada video.

## 48. Implementasi Pop-up Kuis pada Video 2 Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 2 (Modul 2: Percabangan Blok / Logic in App Inventor) menjadi **08:04 (detik ke-484)** hingga **12:01 (detik ke-721)**.
  - Memasukkan Pop-up Kuis interaktif pada akhir tayangan:
    - **Kuis 1 (Fungsi Mutator):** Muncul tepat di menit `12:01`.
- **Status**: Selesai. Video 2 sekarang sudah tersinkronisasi durasinya beserta soal ujian kelulusan Modul 2.

## 49. Implementasi Pop-up Kuis pada Video 3 Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 3 (Modul 3: Uang Digital) menjadi **12:13 (detik ke-733)** hingga **19:33 (detik ke-1173)**.
  - Memasukkan Pop-up Kuis interaktif pada akhir tayangan:
    - **Kuis 1 (Digital 1):** Muncul tepat di menit `19:33`. Kuis ini menguji pemahaman membedakan transfer hadiah dana masuk sebagai "Pendapatan Digital".
- **Status**: Selesai. Video 3 sudah selesai dan pop-up di akhir video sudah dikonfigurasi.

## 50. Bugfix: Pembaruan Indikator Bar Waktu Video (Custom Progress Bar)
- **File Diubah:** `grupC/dashboard/src/App.vue`
- **Perubahan:**
  - Memperbarui fungsi `updateVideoControls` agar durasi (duration) dan waktu berjalan (current time) dihitung berdasarkan panjang segmen (batas waktu modul) saja, bukan lagi total durasi video asli (yang bisa mencapai 30+ menit).
  - Mengubah logika di `onSeekInput` supaya ketika siswa menggeser titik waktu di *slider* (progress bar), perhitungan posisi lompatannya didasarkan pada proporsi segment durasi yang baru ditambahkan batas awal (`startBoundary`).
- **Status**: Selesai. Progress bar video kini sepenuhnya memvisualisasikan durasi mulai (00:00) hingga batas waktu potongan per tab, dan bar yang tidak berhubungan (sebelum/sesudah durasi tab) sudah dihilangkan secara visual dari navigasi.

## 51. Implementasi Pop-up Kuis pada Video 4 Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 4 (Modul 4: Needs vs Wants) menjadi **19:41 (detik ke-1181)** hingga **26:33 (detik ke-1593)**.
  - Memasukkan 2 Pop-up Kuis interaktif sekaligus pada akhir tayangan (menit `26:33`):
    - **Kuis 1 (Prioritas 1):** Kuis membedakan pembelian paket data untuk tugas presentasi sebagai Kebutuhan (*Needs*).
    - **Kuis 2 (Prioritas 2):** Kuis membedakan pembelian top-up *diamond* game sebagai Keinginan (*Wants*).
- **Status**: Selesai. Tayangan Modul 4 dan 2 kuis penutup sudah beroperasi.

## 52. Implementasi Pop-up Kuis pada Video 5 Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`
- **Perubahan:**
  - Mengubah durasi aktif Video 5 (Modul 5: Aplikasi Kalkulator Keuangan) menjadi **26:45 (detik ke-1605)** hingga **31:48 (detik ke-1908)**.
  - Memasukkan Pop-up Kuis interaktif pada akhir tayangan (menit `31:48`):
    - **Kuis 1 (Blok Keuangan):** Kuis mengenai warna blok operasi pengurangan (-) di MIT App Inventor (jawaban: Biru/Math).
- **Status**: Selesai. Video 5 sudah dikonfigurasi beserta kuis penutupnya.

## 53. Integrasi Penugasan Mini Project di Modul 6 Grup C
- **File Diubah:** `grupC/dashboard/src/courseData.js`, `grupC/dashboard/src/App.vue`
- **Perubahan:**
  - `courseData.js`: Mengatur durasi aktif Video 6 (Modul 6: Final Project) untuk mulai pada **32:02 (detik ke-1922)** tanpa batas akhir waktu (karena merupakan sesi penutup video).
  - `App.vue`: Mengimplementasikan komponen pengumpulan form (Project Upload Area) berupa input *Radio Button* interaktif.
  - Form memungkinkan peserta memilih:
    - Opsi 1: Menautkan *link* Galeri MIT App Inventor (divalidasi berformat `https://gallery.appinventor.mit.edu/?galleryid`).
    - Opsi 2: Mengunggah ekstensi file `.aia` secara lokal.
  - Menghubungkan fungsi `submitProject()` agar menyimpan URL/kode biner melalui `fetch` (CORS bypassed) ke *Google Apps Script* untuk disinkronisasikan ke kolom `Project1_Code` dengan kategori `gms2c`.
- **Status**: Selesai. Sistem unggah file pada *Mini Project Final* (Tab 6) Grup C kini beroperasi seutuhnya.

## 54. Bugfix: Indikator Waktu Video dan Visibilitas Kuis Grup C
- **File Diubah:** `grupC/dashboard/src/App.vue`
- **Perubahan:**
  - Menghapus baris `return; // DISABLE QUIZZES` yang sebelumnya mencegah pop-up kuis untuk muncul di Grup C. 
  - Memperbaiki logika `updateVideoControls` pada tampilan indikator waktu *progress bar*. Waktu *slider* (panjang bar) tetap menampilkan porsi segment yang dipotong dari tab bersangkutan (menghilangkan bar yang berlebih), namun label teks (*currentTimeFormatted* dan *durationFormatted*) kini dikonversi kembali ke waktu asli video agar sesuai dengan catatan durasi yang telah diberikan.
- **Status**: Selesai. Kuis kini muncul secara otomatis, dan angka indikator waktu sesuai dengan spesifikasi aslinya.

## 55. Bugfix: Pilihan Ganda (Opsi) Kuis Tidak Muncul di Grup C
- **File Diubah:** `grupC/dashboard/src/App.vue`
- **Perubahan:** Memperbarui logika fungsi `getQuestionChoices` yang bertugas untuk merender tombol-tombol pilihan ganda pada layar. Sebelumnya, sistem hanya membaca *key* berawalan `choices` dari data kuis. Sementara di dalam data course Grup C, variabel tersebut bernama `options`. Fungsi dimodifikasi agar dapat membaca `question.options` sebagai prioritas alternatif apabila `question.choices` tidak ditemukan.
- **Status**: Selesai. Seluruh pertanyaan *pop-up* kuis pada Grup C kini telah memunculkan tombol pilihan jawaban dengan normal.

## 56. Bugfix: Video Terus Berputar Melewati Batas Waktu di Grup C
- **File Diubah:** `grupC/dashboard/src/App.vue`
- **Perubahan:** Mengganti fungsi `enforceVideoStartBoundary` menjadi `enforceVideoBoundaries`. Menambahkan validasi `endBoundary` agar pemutar video (YouTube Player) secara otomatis ter-*pause* (berhenti) ketika durasi tontonan menyentuh waktu akhir (batas) dari tab/modul yang ditentukan di `courseData.js`, lalu memicu verifikasi penyelesaian modul/kuis.
- **Status**: Selesai. Tayangan video sekarang tidak akan tembus/"bocor" melanjutkan ke materi selanjutnya jika waktu akhirnya sudah habis.

## 57. Penyesuaian Fitur Kuis (Menghilangkan Syarat 3 Kesempatan)
- **File Diubah:** `grupC/dashboard/src/App.vue`
- **Perubahan:** Mengubah sistem evaluasi pada fungsi `handleStandardAnswer`. Berhubung semua soal di Grup C berwujud pilihan ganda, sistem jatah 3x nyawa/kesempatan menjawab dihapuskan. Jika siswa memilih jawaban yang keliru, kotak opsi langsung terkunci (*disabled*) dan sistem akan seketika memberikan *feedback*/pembahasan serta memunculkan tombol "Lanjut" untuk beralih ke aktivitas berikutnya.
- **Status**: Selesai. Kuis kini beroperasi jauh lebih cepat dan tidak membebani siswa untuk mencoba ulang pada opsi-opsi sisa (pilihan ganda).

---

# Changelog & Update Log: Middleschool Grup D Dashboard

## 58. Replikasi Pengaturan UI dan Logika dari Grup B ke Grup D
- **File Diubah:** `grupD/dashboard/src/App.vue`, `grupD/dashboard/src/style.css`
- **Perubahan:** Menyalin struktur kerangka utama (seperti *settings*, cara kerja pop-up kuis, logika *video blocking*, *progress bar*, dan pesan peringatan) secara identik dari Grup B ke Grup D.
- **Status**: Selesai. Seluruh fitur canggih kini diwarisi oleh Grup D.

## 59. Penyesuaian Data Materi, Durasi, dan Kuis Grup D (Tab 1 & 2)
- **File Diubah:** `grupD/dashboard/src/courseData.js`, `grupD/dashboard/src/App.vue`
- **Perubahan:** 
  - Mengubah video ID menjadi `P8Ea0v8Gy2o` sesuai materi Grup D.
  - **Tab 1:** Memotong durasi video mulai detik 00:04 hingga 13:14. Menambahkan "Mini Quiz 1" pada detik 13:13.
  - **Tab 2 (Baru):** Menambahkan tab khusus "Mini Project Kalkulator Cerdas" tepat setelah Tab 1. Durasi video 13:18 hingga 14:39. Instruksi tugas dimasukkan ke dalam teks bacaan, dan *form* pengumpulan tugas (upload file `.aia` / link) di-render spesifik di Tab 2.
- **Status**: Selesai.

## 60. Penyesuaian Data Materi Grup D (Tab 3)
- **File Diubah:** `grupD/dashboard/src/courseData.js`
- **Perubahan:** 
  - **Tab 3:** Memotong durasi video mulai detik 14:43 hingga 19:54.
  - Menambahkan "Mini Quiz 3" pada detik 19:53 yang menanyakan tentang keuntungan modularisasi kode sesuai referensi gambar.
- **Status**: Selesai.

## 61. Penyesuaian Data Materi Grup D (Tab 4)
- **File Diubah:** `grupD/dashboard/src/courseData.js`
- **Perubahan:** 
  - **Tab 4:** Memperbarui durasi akhir video menjadi menit 28:05 (detik 1685).
  - Menyesuaikan kemunculan "Mini Quiz 4" menjadi pada detik 1684 (28:04) yang membahas tentang blok TinyDB sesuai instruksi.
- **Status**: Selesai.

## 62. Penyesuaian Data Materi Grup D (Tab 5)
- **File Diubah:** `grupD/dashboard/src/courseData.js`
- **Perubahan:** 
  - **Tab 5:** Memperbarui durasi awal dan akhir video menjadi dari menit 28:24 (detik 1704) sampai 33:28 (detik 2008).
  - Menyesuaikan kemunculan "Mini Quiz 5" menjadi pada detik 2007 (33:27) sesuai instruksi dan screenshot (Sikap saat menerima feedback).
- **Status**: Selesai.

## 63. Penyesuaian Data Materi Grup D (Tab 6)
- **File Diubah:** `grupD/dashboard/src/courseData.js`
- **Perubahan:** 
  - **Tab 6:** Memperbarui durasi awal dan akhir video menjadi dari menit 33:38 (detik 2018) sampai 37:41 (detik 2261).
  - Menyesuaikan kemunculan "Mini Quiz 6" menjadi pada detik 2260 (37:40) tentang Solusi Digital Berdampak Positif, sesuai instruksi dan gambar referensi.
- **Status**: Selesai.

## 64. Pembuatan Tab 7: Mini Project "Merancang Solusi Digital"
- **File Diubah:** `grupD/dashboard/src/courseData.js`, `grupD/dashboard/src/App.vue`, `Code.gs`
- **Perubahan:** 
  - **Tab 7:** Menambahkan tab baru sebagai checkpoint terakhir dengan durasi video 37:47 (detik 2267) sampai 38:23 (detik 2303).
  - Mengembangkan UI formulir pengumpulan ide yang baru di dalam `App.vue` yang mencakup:
    - Text Box 1: Observasi Lingkungan
    - Text Box 2: Penemu Solusi Digital
    - Upload File Gambar: UI Designer (khusus format JPG/PNG)
  - Menyambungkan form input dengan logika penyimpanan backend via `Code.gs` dengan menambahkan kolom `Idea_Obs`, `Idea_Sol`, dan `Idea_UI_Code` di Google Sheets (pada grup `ghs2d`).
- **Status**: Selesai. Seluruh mekanisme form input, *placeholder* text, validasi khusus gambar (JPG/PNG), hingga pengiriman ke sheet sudah berfungsi.

## 65. Generate Thumbnail Otomatis (Grup D)
- **Proses:** 
  - Membuat *script* `generate_thumbs.js` berbasis Node.js dan Puppeteer khusus untuk Grup D.
  - Menyesuaikan 7 judul spesifik materi Grup D (mulai dari "Membuat dan Memanggil Procedures" hingga "Brainstorming Ide Aplikasi").
  - Menjalankan *script* untuk merender HTML secara otomatis menjadi 7 file gambar (`thumb_1.png` hingga `thumb_7.png`) dengan desain bergaya *neo-brutalism* yang sama seperti Grup B.
- **Status**: Selesai. Semua *thumbnail* telah di-generate dan tersimpan di folder `public/`, dan *dashboard* Grup D kini memiliki tampilan *thumbnail* video yang cantik dan rapi.
