# Brief Dashboard Asynchronous Learning (Highschool)

Dokumen ini berisi spesifikasi dan aturan (brief) untuk pengembangan Dashboard Asynchronous Learning yang diimplementasikan pada setiap grup (Grup A, B, C, dan D).

## 1. Alur Login (Autentikasi User)
Dashboard wajib memiliki sistem login dengan alur sebagai berikut:
- **Pilih Sekolah:** User harus memasukkan/memilih nama sekolah terlebih dahulu. Sistem akan melakukan filter daftar email/siswa yang tersedia khusus untuk sekolah tersebut.
- **Input Email:** User memasukkan email yang terdaftar di Akademia Ruangguru.
- **Validasi & Batas Percobaan:** Terdapat batas maksimal **3 kali percobaan** login jika email salah. 
  - Sistem dapat memberikan saran (suggestion) jika ada indikasi salah ketik (typo).
  - Jika sudah 3 kali salah, user akan disarankan untuk menghubungi RFO/guru pendamping untuk mengecek email yang terdaftar.

## 2. Konten Utama (Video & Rangkuman)
- Setiap tab/halaman dalam dashboard berisi **Video Pembelajaran** beserta **Teks Rangkuman** dari materi yang dijelaskan di dalam video tersebut.

## 3. Pop-up Quiz dalam Video
Di dalam beberapa video, akan muncul Pop-up Quiz yang sifatnya **wajib dikerjakan** oleh siswa.
- **Waktu Kemunculan Tersembunyi:** Waktu (timestamp) pop-up quiz tidak diberitahukan sebelumnya. Siswa wajib menonton video secara perlahan/menyeluruh untuk menemukan dan menjawab pop-up quiz tersebut.
- **Tombol "Rewatch 30 Detik":** Terdapat fitur/tombol untuk memutar kembali video mundur 30 detik sebelum pop-up muncul, berguna jika siswa bingung dan butuh menonton ulang materi sesaat sebelum kuis.
- **Batas Percobaan Menjawab:** Siswa memiliki kesempatan maksimal **3 kali mencoba** menjawab jika jawabannya salah.
  - Jika sudah salah 3 kali, video baru bisa dilanjutkan, **tetapi** nilai/skor untuk kuis tersebut akan kosong (karena batas percobaan habis).

## 4. Mini Project (Web IDE)
- Pada tab tertentu, terdapat tugas **Mini Project**.
- Khusus jenjang SMA (Highschool), siswa akan diminta untuk memasukkan dan menjalankan kode pada **in-web IDE** sesuai dengan instruksi yang diberikan.
- **Syarat Lanjut:** Kode/project yang dikerjakan harus benar (passed) sebelum siswa bisa melanjutkan ke materi/tab berikutnya.

## 5. Sistem Syarat Progres (Progress Lock)
- Akses ke tab/materi selanjutnya **terkunci**. 
- Siswa hanya bisa mengakses tab selanjutnya apabila seluruh Pop-up Quiz dan/atau Mini Project pada tab saat ini sudah diselesaikan.

## 6. Penyimpanan Data (Google Apps Script - Code.gs)
Seluruh data progres dan nilai akan disimpan ke dalam Google Spreadsheet menggunakan **Code.gs**.
- **Link Spreadsheet Utama:** [https://docs.google.com/spreadsheets/d/1pE_YGmKFZNUz8ow2baGfxw3EMH0PwOQeRmOWVVB9Itg/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1pE_YGmKFZNUz8ow2baGfxw3EMH0PwOQeRmOWVVB9Itg/edit?usp=sharing)
- **Nama Sheet Dinamis:** Nama sheet untuk menyimpan *result* (hasil) akan berbeda berdasarkan jejang dan grupnya (misal: `ops-student-result-ghs2a`, `ops-student-result-ghs2b`, `ops-student-result-ghs2c`, `ops-student-result-ghs2d`).
- **Header Kolom Dinamis:** `Code.gs` harus mampu menulis nama header tabel (nama tab/kuis) secara otomatis. Jika kolom belum ada atau tidak sesuai dengan jumlah kuis/ide project yang ada di dashboard pada masing-masing grup, sistem akan menyesuaikan dan membuat header tersebut secara mandiri. Kolom-kolom mencatat data penting seperti Jawaban (Ans), Percobaan (Att), Kode IDE, dan Skor Final Project.