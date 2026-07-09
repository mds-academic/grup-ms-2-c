# Script Presentasi - Basic Pemrograman: Condition
**Target Audiens:** Anak SD
**Panduan:** Script ini merupakan "jalan tengah". Cukup jelas dan santai seperti bercerita, tidak terlalu kaku seperti membaca teks, tapi juga tidak terlalu bertele-tele.

---

## Slide 1: Membuat Program yang Bisa Memilih!
**(Visual: Slide 1 - Judul dan Gambar Robot)**

**Audio (Host / Pengisi Suara):**
"Halo teman-teman! Hari ini kita akan belajar cara membuat program yang bisa memilih. 

Ternyata di dalam coding, program itu tidak hanya berjalan lurus-lurus saja, lho! Kadang program kita harus bisa memilih jalan. 

Coba bayangkan sebuah robot pintar. Dia bisa berpikir: 
*'Kalau kondisinya begini, aku akan lakuin ini deh!'* 
*'Tapi kalau kondisinya beda, aku lakuin yang lain!'* 

Nah, di dunia pemrograman, konsep komputer atau robot untuk bisa memilih jalan ini disebut dengan **Conditional**. Yuk, kita cari tahu lebih lanjut!"

---

## Slide 2: Pernah Ambil Keputusan?
**(Visual: Slide 2 - Gambar payung, burger, baterai HP)**

**Audio (Host / Pengisi Suara):**
"Sebenarnya setiap hari kita pasti sering banget bikin pilihan, kan? 

Contohnya nih:
Pertama, kalau hujan turun, kita pasti bawa payung! 
Kedua, kalau perut keroncongan alias lapar, waktunya kita makan! 
Dan ketiga, kalau baterai HP sisa 5%, wah gawat, buruan di-charge!

Nah, kita membuat keputusan itu berdasarkan sebuah **kondisi**. Kabar baiknya, program komputer juga bisa diajarkan untuk jadi pintar dan melakukan hal yang sama persis seperti kita!"

---

## Slide 3: Apa Itu Condition? 🤔
**(Visual: Slide 3 - Gambar Game: Apel dan Duri)**

**Audio (Host / Pengisi Suara):**
"Lalu, apa sih sebenarnya Condition itu? 

Singkatnya, Condition adalah cara untuk bikin komputer jadi bisa mikir! Sederhananya begini: *Kalau ada sebuah syarat yang benar, komputernya baru akan bergerak.*

Contohnya di dalam sebuah Game: 
Kalau karaktermu makan apel, nyawanya pasti nambah! 
Tapi kalau karakternya kena duri, nyawanya akan berkurang! 

Keren, kan? Dengan menggunakan condition, komputer jadi tahu kapan harus menambah nyawa dan kapan harus mengurangi nyawa!"

---

## Slide 4: Condition Kayak Pintu Penjaga 🚪
**(Visual: Slide 4 - Gambar Kastil dan Kunci Ajaib)**

**Audio (Host / Pengisi Suara):**
"Biar lebih mudah dibayangkan, Condition itu mirip seperti Pintu Penjaga. 

Bayangkan kamu sedang berpetualang dan mau masuk ke kastil harta karun! Kamu cuma bisa masuk ke sana kalau kamu punya Kunci Ajaib. 

Nah, penjaganya akan mengecek: Kalau kamu punya kunci? Pintunya terbuka! 
Tapi kalau kamu tidak punya kunci? Pintu akan tertutup rapat. 

Di dalam coding, 'punya kunci atau tidak' inilah yang disebut dengan **Kondisi**. Program komputer itu akan selalu mengecek: *'Kondisinya terpenuhi gak ya?'*"

---

################################################################

## Slide 5: Conditional Paling Sederhana: `if`
**(Visual: Slide 5 - Kode if)**

**Audio (Host / Pengisi Suara):**
"Di bahasa pemrograman Python, conditional yang paling dasar itu menggunakan perintah `if`. 

Coba perhatikan kode ini. Kita punya umur atau `age` sama dengan 17. 
Lalu ada perintah: `if age >= 17: print("Boleh membuat KTP")`.

Artinya: Kalau nilai `age` lebih besar atau sama dengan 17, maka komputer akan menampilkan teks 'Boleh membuat KTP'. 
Tapi ingat, kalau kondisinya salah, program tidak akan menjalankan isi dari `if` tersebut."

---

## Slide 6: Cara Membaca `if` 📖
**(Visual: Slide 6 - Penjelasan cara membaca if)**

**Audio (Host / Pengisi Suara):**
"Bagaimana sih cara membaca kode `if` tadi? 

Cara membacanya gampang banget: 
*'Jika umur lebih dari atau sama dengan 17, maka tampilkan pesan.'*

Nah, bagian `age >= 17` ini adalah **kondisi** yang dicek oleh program. 
Sedangkan perintah `print("Boleh membuat KTP")` adalah **aksi** yang dilakukan kalau kondisinya benar."

---

## Slide 7: Kondisi Menghasilkan True atau False ⚖️
**(Visual: Slide 7 - True atau False)**

**Audio (Host / Pengisi Suara):**
"Setiap kondisi yang kita buat di Python selalu punya dua kemungkinan jawaban: Antara **True** alias Benar, atau **False** alias Salah. 

Contohnya begini: 
Kalau kita punya `age = 17`, lalu kita cek `print(age >= 17)`. 

Kira-kira apa hasilnya? Hasil yang keluar pasti adalah **True**. Kenapa? Karena angka 17 memang benar lebih besar atau sama dengan 17!"

---

## Slide 8: Kalau Kondisinya Salah? ❌
**(Visual: Slide 8 - Contoh False)**

**Audio (Host / Pengisi Suara):**
"Terus, bagaimana kalau kondisinya salah? 

Coba lihat contoh ini: `age = 15`. 
Lalu program akan mengecek: *Apakah 15 lebih besar atau sama dengan 17?* 

Tentu saja jawabannya adalah **False** atau Salah. 
Nah, karena kondisinya salah, maka pesan di dalam `if` tersebut **tidak akan muncul** di layar."

---

################################################################

## Slide 10: Menambahkan Pilihan Lain dengan `else` 🔀
**(Visual: Slide 10 - Menambahkan else)**

**Audio (Host / Pengisi Suara):**
"Bagaimana kalau program kita perlu melakukan sesuatu yang lain ketika kondisinya salah? 

Untuk melakukannya, kita bisa menambahkan perintah **`else`**. 
Coba perhatikan kodenya. 

Artinya:
Kalau umurnya minimal 17, program mencetak 'Boleh membuat KTP'. 
Tapi kalau tidak (atau *else*), program akan mencetak 'Belum boleh membuat KTP'. 

Jadi, `else` ini bisa dibilang seperti rencana cadangan kalau kondisi `if`-nya tidak terpenuhi!"

---

## Slide 11: `if else` Itu Seperti Dua Jalan 🛣️
**(Visual: Slide 11 - Persimpangan jalan)**

**Audio (Host / Pengisi Suara):**
"Untuk gampangnya, `if else` itu ibarat kamu sampai di sebuah persimpangan jalan. 

Kalau jalan ke kiri terbuka, kamu bisa lewat kiri. Kalau tidak, kamu harus lewat kanan. 
Sama seperti di program: Kalau kondisinya benar, jalankan bagian `if`. 
Tapi kalau kondisinya salah, jalankan bagian `else`. 

Ingat ya teman-teman: Program itu cuma bisa memilih **salah satu jalan** saja, tidak akan pernah bisa jalan di dua-duanya sekaligus!"

---

## Slide 12: Contoh `if else` di Program Game 🎮
**(Visual: Slide 12 - Kode jawaban benar/salah)**

**Audio (Host / Pengisi Suara):**
"Coba kita lihat contoh `if else` di dalam program game. 

Misalnya jawaban benarnya adalah 'A'. 
Maka kodenya: `if answer == "A"`, program akan bilang 'Jawaban benar!'. 
Tapi kalau bukan (atau `else`), program akan bilang 'Jawaban salah.'. 

Jadi, kalau isi jawabannya benar-benar 'A', yang muncul adalah 'Jawaban benar!'. 
Tapi kalau isi jawabannya bukan 'A', yang muncul pasti 'Jawaban salah.'."

---
################################################################

## Slide 16: Urutan yang Benar 🎯
**(Visual: Slide 16 - Contoh urutan kondisi yang benar)**

**Audio (Host / Pengisi Suara):**
"Nah, supaya tidak salah urutan, kita harus mulai mengecek dari syarat yang tertinggi dulu! 

Coba perhatikan kodenya. Pertama, kita cek apakah nilainya 90 ke atas. Kalau tidak, baru turun ke 75, lalu ke 60, dan seterusnya. 

Dengan urutan yang benar seperti ini, kalau nilai kita 95, hasil yang keluar pasti 'Sangat Baik'. 
Jadi ingat ya, kalau kondisinya ada banyak, urutannya harus kalian pikirkan dengan hati-hati!"

---

## Slide 17: Apa Itu Nested Condition? 🪆
**(Visual: Slide 17 - Pengenalan Nested Condition)**

**Audio (Host / Pengisi Suara):**
"Selain percabangan yang banyak, ada satu lagi nih yang namanya **Nested Condition**. Apa itu? 

Nested condition adalah kondisi di dalam kondisi. Sederhananya, setelah program mengecek satu syarat, dia akan mengecek syarat lain di dalamnya. 

Contohnya kalau kamu mau nonton di bioskop. Syarat pertama, kamu harus punya tiket. Tapi setelah masuk, petugasnya mengecek lagi: 'Apakah umurmu cukup untuk menonton film ini?' 
Nah, pengecekan berlapis inilah yang disebut Nested Condition!"

---

## Slide 18: Analogi Nested Condition 🏢
**(Visual: Slide 18 - Analogi masuk gedung)**

**Audio (Host / Pengisi Suara):**
"Biar lebih gampang dibayangkan, coba bayangkan kamu mau masuk ke sebuah gedung rahasia. 

Di pintu pertama, penjaganya akan mengecek: 'Apakah kamu punya kartu akses?' Kalau iya, kamu boleh masuk ke dalam. 
Lalu di dalam, ada pintu kedua yang mengecek lagi: 'Apakah kamu punya izin masuk ruangan khusus?' 

Jadi, kamu harus lolos syarat yang pertama dulu, baru deh kamu bisa diperiksa untuk syarat yang kedua."

---

## Slide 19: Contoh Nested Condition di Python 🐍
**(Visual: Slide 19 - Kode Nested Condition tiket bioskop)**

**Audio (Host / Pengisi Suara):**
"Sekarang kita lihat contoh penulisannya di Python. 

Program pertama kali akan mengecek variabel `has_ticket`. *Apakah dia punya tiket?* 
Kalau jawabannya iya, program tidak langsung menyuruh masuk, tapi dia akan mengecek lagi di dalamnya: *Apakah umurnya minimal 13 tahun?* 

Kalau umurnya cukup, baru deh akan dicetak 'Boleh masuk studio'. 
Tapi kalau tidak punya tiket dari awal, program akan langsung bilang 'Harus punya tiket dulu'."

---

## Slide 20: Cara Membaca Nested Condition 🧐
**(Visual: Slide 20 - Penjelasan indentasi)**

**Audio (Host / Pengisi Suara):**
"Cara membaca kodenya juga sangat gampang! 
Kamu tinggal baca begini: *'Kalau dia punya tiket, maka coba cek lagi umurnya.'* 

Satu hal yang paling penting: Coba perhatikan kode `if` yang kedua. Letaknya lebih menjorok ke dalam, kan? 
Nah, penulisan yang menjorok (atau indentasi) ini sangat penting di Python agar komputernya tahu kalau itu adalah kondisi di dalam kondisi!"

---


## Slide 21: Nested Condition di Program Game 🎮
**(Visual: Slide 21 - Contoh game level bonus)**

**Audio (Host / Pengisi Suara):**
"Di dalam game, Nested Condition ini juga sering dipakai, lho! 

Misalnya, pemain cuma bisa masuk ke Level Bonus jika dia sudah menyelesaikan level 1, **dan** dia punya minimal 100 koin. 
Jadi program gamenya akan mengecek dulu: *Apakah level 1 sudah selesai?* Kalau sudah, baru dicek lagi: *Apakah koinnya ada 100 atau lebih?* 

Nah, kalau dua-duanya terpenuhi, barulah pemain bisa masuk ke Level Bonus!"

---

################################################################


## Slide 25: Contoh `and` di Python 🐍
**(Visual: Slide 25 - Kode contoh penggunaan and)**

**Audio (Host / Pengisi Suara):**
"Coba kita lihat contoh penggunaannya di Python. 

Di sini kita punya tiga syarat yang semuanya bernilai True: `registered`, `paid`, dan `submitted`. 
Lalu di bawahnya, kita pakai `and` untuk menggabungkan ketiganya: `if registered and paid and submitted:`

Artinya, program hanya akan menampilkan tulisan 'Boleh ikut lomba' kalau ketiga-tiganya benar. 
Kalau ada satu saja yang belum dipenuhi, misalnya belum membayar, maka program akan bilang 'Belum bisa ikut lomba'!"

---

## Slide 26: Operator `or` 🤷‍♂️
**(Visual: Slide 26 - Penjelasan operator or)**

**Audio (Host / Pengisi Suara):**
"Selanjutnya ada operator **`or`** atau 'atau'. 

Berbeda dengan `and` yang mengharuskan semuanya benar, `or` ini jauh lebih santai. Dia akan bekerja kalau **salah satu saja** kondisinya benar! 

Contohnya saat kamu mau login ke sebuah aplikasi. Kamu bisa login pakai Email, **atau** pakai Username, **atau** pakai Nomor HP. 
Tidak perlu memasukkan ketiganya sekaligus, kan? Cukup salah satu saja yang benar, dan kamu sudah bisa masuk!"

---

## Slide 27: Contoh `or` di Python 🐍
**(Visual: Slide 27 - Kode contoh penggunaan or)**

**Audio (Host / Pengisi Suara):**
"Nah, begini contoh penulisan `or` di Python. 

Kita lihat di sini, `use_email` dan `use_phone` nilainya False, tapi `use_username` nilainya True. 
Lalu program mengecek: `if use_email or use_username or use_phone:`

Kira-kira apa hasilnya? Yap, hasilnya adalah 'Bisa login'! 
Walaupun ada yang False, tapi karena ada **satu** yang True, maka gabungan kondisi ini dianggap benar."

---

## Slide 28: Operator `not` 🔄
**(Visual: Slide 28 - Penjelasan operator not)**

**Audio (Host / Pengisi Suara):**
"Yang ketiga adalah operator **`not`** atau 'tidak'. 

Kalau `not`, tugasnya sangat unik: dia akan **membalikkan** nilai! Kalau awalnya True, dibalik jadi False. Begitu juga sebaliknya. 

Misalnya begini: Kalau **tidak** hujan, kita bisa bermain di luar. 
Nah, di Python kita tulisnya: `if not is_raining:`
Artinya, kalau kondisi hujannya False, program malah mengizinkan kita bermain di luar!"

---

## Slide 29: Menggabungkan 3+ Kondisi 🤯
**(Visual: Slide 29 - Kode menggabungkan and, or, dan not)**

**Audio (Host / Pengisi Suara):**
"Bagaimana kalau kita punya banyak sekali syarat yang mau digabungkan? 

Tenang saja, di Python kita bebas menggabungkan lebih dari tiga kondisi sekaligus, bahkan kita bisa mencampur `and`, `or`, dan `not`! 

Misalnya, siswa boleh ikut kelas lanjutan **jika**: 
Nilainya 75 ke atas, **dan** tugasnya sudah selesai, **dan tidak** sedang remedial. 
Dengan Python, kita bisa menuliskannya dalam satu baris panjang yang rapi!"

---

## Slide 30: Cara Membaca Kondisi Kompleks 🧐
**(Visual: Slide 30 - Penjelasan cara membaca kondisi panjang)**

**Audio (Host / Pengisi Suara):**
"Lalu bagaimana cara membaca kode yang panjang itu? Gampang kok! 
`score >= 75 and task_done and not remedial`

Kita baca satu-satu: Nilai minimal 75 (True), tugas sudah selesai (True), dan siswa tidak remedial (True). 
Karena semuanya dipisahkan dengan `and`, maka **semua syarat** ini wajib bernilai True. 

Ingat ya teman-teman, kalau ada satu saja yang False, maka seluruh kondisi panjang ini akan ikut bernilai False!"

---

## Slide 32: Gunakan Tanda Kurung 📝
**(Visual: Slide 32 - Penggunaan tanda kurung dalam kondisi)**

**Audio (Host / Pengisi Suara):**
"Walaupun Python punya aturan sendiri, ada satu trik yang bisa kita pakai supaya kodenya lebih gampang dibaca, yaitu menggunakan **tanda kurung**! 

Coba lihat kode ini: `(score >= 75 and task_done) or has_bonus`. 
Tanda kurung ini fungsinya mirip seperti di pelajaran matematika. Python akan selalu mengecek apa yang ada di dalam tanda kurung terlebih dahulu. 

Jadi, Python akan memastikan nilai dan tugasnya dulu, baru setelah itu mengecek bonusnya. 
Tanda kurung ini ibarat pahlawan penyelamat yang bikin kode kita jadi tidak membingungkan!"

---

## Slide 33: Truth Table `and` 🤝
**(Visual: Slide 33 - Tabel kebenaran untuk and)**

**Audio (Host / Pengisi Suara):**
"Untuk membantu kalian mengingat, kita punya tabel rahasia nih! Namanya Truth Table atau Tabel Kebenaran. 

Kita mulai dari `and`. Seperti yang sudah kita bahas, `and` ini sangat ketat. 
Coba perhatikan tabelnya: Kalau Kondisi A True dan Kondisi B True, barulah hasilnya True! 

Tapi kalau ada satuuu saja yang False, mau itu di A, di B, atau dua-duanya, hasil akhirnya pasti False. 
Cara gampang mengingatnya: `and` itu artinya **semua harus lengkap**!"

---

## Slide 34: Truth Table `or` 🤷‍♂️
**(Visual: Slide 34 - Tabel kebenaran untuk or)**

**Audio (Host / Pengisi Suara):**
"Sekarang kita bandingkan dengan tabel kebenaran untuk `or`. 

Tabel `or` ini jauh lebih santai. Coba lihat, warna True-nya lebih banyak kan? 
Itu karena `or` hanya akan menghasilkan False kalau **kedua kondisinya** benar-benar False. 

Kalau ada satu saja yang True, entah itu di A atau di B, maka hasil akhirnya sudah pasti True. 
Cara gampang mengingatnya: `or` itu artinya **salah satu saja cukup**!"

---

## Slide 36: Mengevaluasi Kondisi Kompleks 🕵️‍♂️
**(Visual: Slide 36 - Cara mengevaluasi kondisi kompleks satu per satu)**

**Audio (Host / Pengisi Suara):**
"Sekarang mari kita berlatih mengevaluasi kondisi yang panjang ini bersama-sama! 

Coba lihat baris paling bawah: `score >= 75 and task_done and not remedial`
Pertama, kita cek nilainya. 80 memang lebih dari 75, jadi hasilnya True. 
Kedua, `task_done` memang isinya True. 
Dan yang ketiga, variabel `remedial` isinya False, tapi karena ada kata `not`, maka dibalik menjadi True. 

Nah, karena ketiga bagian ini hasilnya True, True, dan True, maka digabungkan dengan `and` hasil akhirnya juga pasti True!"

---

## Slide 37: Nested Condition vs Logical Operators 🥊
**(Visual: Slide 37 - Perbandingan kode nested dan logical operators)**

**Audio (Host / Pengisi Suara):**
"Kalian mungkin bertanya-tanya: 'Lalu lebih baik pakai Nested Condition atau Logical Operators?' 

Jawabannya: Tergantung kebutuhan! Tapi untuk banyak kasus, Logical Operators bisa bikin kode kita jadi jauh lebih rapi. 
Coba lihat contoh kode di atas. Karena ada tiga syarat, penulisannya jadi bertingkat-tingkat dan menjorok sangat jauh ke dalam. 

Sedangkan di kode bawahnya, dengan bantuan `and`, kita bisa menyatukan semua syarat tadi ke dalam satu baris saja. 
Hasilnya? Kode jadi jauh lebih pendek, tidak membuat pusing, dan tentu saja lebih gampang dibaca!"

---

## Slide 39: Kapan Pakai Logical Operators? 💡
**(Visual: Slide 39 - Penjelasan kapan menggunakan logical operators)**

**Audio (Host / Pengisi Suara):**
"Lalu, kapan kita sebaiknya menggunakan Logical Operators? 

Logical Operators ini sangat cocok dipakai kalau **beberapa syarat bisa dicek sekaligus** tanpa harus bergantung satu sama lain. 
Contohnya, untuk masuk ke menu khusus, kamu harus sudah login **dan** peranmu adalah admin. Dua syarat ini bisa langsung digabung dengan `and`! 

Intinya: Kalau kamu cuma butuh mengecek 'Apakah semua syarat ini sudah lengkap?', maka langsung saja gabungkan dengan Logical Operators!"

---

## Slide 40: Contoh Kasus: Sistem Diskon 🏷️
**(Visual: Slide 40 - Kode contoh sistem diskon toko)**

**Audio (Host / Pengisi Suara):**
"Mari kita lihat contoh kasus yang seru, yaitu Sistem Diskon di sebuah toko! 

Misalkan tokonya punya aturan begini: Pelanggan bisa dapat diskon kalau total belanjanya minimal Rp100.000 **dan** dia adalah seorang member. 
**Atau**, dia bisa tetap dapat diskon asalkan dia punya kupon khusus! 

Wah, lumayan panjang ya aturannya? Tapi dengan Python, kita bisa merangkum semua syarat ini ke dalam satu baris kode yang sangat rapi menggunakan tanda kurung, `and`, dan `or`."

---

## Slide 41: Membaca Sistem Diskon 🕵️‍♂️
**(Visual: Slide 41 - Penjelasan cara membaca alur diskon)**

**Audio (Host / Pengisi Suara):**
"Bagaimana cara komputer membaca aturan diskon yang panjang tadi? 

Pertama, komputer akan mengecek bagian di dalam kurung dulu: Apakah belanjanya 100 ribu ke atas? Dan apakah dia member? Kalau iya, hore! Dapat diskon. 
Tapi, kalau ternyata syarat di dalam kurung tidak terpenuhi, komputer masih punya jalur kedua. 

Komputer akan mengecek kata `or`: Apakah pelanggan punya kupon? Kalau punya, dia tetap akan diberikan diskon. Jadi ada dua jalan berbeda untuk bisa dapat diskon!"

---

## Slide 42: Contoh Kasus: Akses Aplikasi 📱
**(Visual: Slide 42 - Kode contoh pengecekan login aplikasi)**

**Audio (Host / Pengisi Suara):**
"Kasus berikutnya: Memberi akses masuk ke sebuah aplikasi. 

Misalkan ada tiga syarat wajib supaya pengguna bisa masuk: Username harus benar, Password harus benar, dan akunnya **tidak** sedang diblokir. 
Coba perhatikan kodenya! Kita memakai `and` untuk memastikan username dan password benar. Lalu kita tambahkan `and not blocked` untuk memastikan bahwa status akunnya tidak diblokir. 

Ingat, karena memakai `and`, kalau ada satuuu saja yang salah, misalnya ternyata akunnya diblokir, maka login-nya pasti akan langsung ditolak."

---

## Slide 43: Kasus: Rekomendasi Aktivitas 🏃‍♂️
**(Visual: Slide 43 - Contoh program rekomendasi aktivitas)**

**Audio (Host / Pengisi Suara):**
"Terakhir, ini adalah contoh program pintar yang bisa memberi rekomendasi aktivitas berdasarkan cuaca dan waktu. 

Di sini kita kembali menggunakan percabangan `elif`, tapi sekarang kita gabungkan dengan Logical Operators! 
Kalau cuaca cerah **dan** waktunya pagi, program bilang 'Jogging di taman'. 
Tapi kalau cuacanya cerah **dan** waktunya siang, rekomendasinya langsung berubah jadi 'Minum es dan istirahat'. 

Nah, dari contoh ini kalian bisa lihat kan, program komputer bisa jadi sangat cerdas hanya dengan merangkai syarat-syarat yang sederhana!"

---

## Slide 45: Kesalahan Umum 2: Kondisi Panjang 🥵
**(Visual: Slide 45 - Memperbaiki kondisi yang terlalu panjang)**

**Audio (Host / Pengisi Suara):**
"Kesalahan kedua yang sering terjadi adalah membuat satu baris kondisi yang jauuuh dan panjang sekali sampai layar harus digeser! 

Meskipun program bisa membaca kodenya, tapi mata kita akan sangat pusing melihatnya. 
Nah, cara cerdas untuk merapikannya adalah dengan menggunakan **variabel**. Kita bisa menyimpan setiap kondisi di dalam variabelnya masing-masing terlebih dahulu. 

Setelah itu, barulah kita gabungkan nama-nama variabel tersebut di dalam `if`. Hasilnya? Kode jadi jauh lebih rapi dan sangat gampang dibaca!"

---

## Slide 46: Kesalahan Umum 3: Salah Urutan `elif` 📉
**(Visual: Slide 46 - Memperbaiki urutan elif yang salah)**

**Audio (Host / Pengisi Suara):**
"Kesalahan umum yang ketiga: Salah mengatur urutan saat menggunakan `elif`. 

Coba lihat kode yang salah ini: Kalau skornya 92, karena urutan pertamanya adalah mengecek `score >= 60`, program akan langsung bilang 'Cukup' dan berhenti! Padahal kan seharusnya 'Sangat Baik'. 

Nah, aturan emasnya adalah: Selalu mulai dari kondisi yang **paling spesifik** atau yang memiliki kriteria **paling tinggi** terlebih dahulu. Mulai dari ngecek angka 90, baru turun ke 75, baru ke 60. Dengan begitu, programmu akan berjalan dengan sempurna!"

---

## Slide 47: Mini Activity: Baca Kode 🧐
**(Visual: Slide 47 - Aktivitas membaca output dari kode)**

**Audio (Host / Pengisi Suara):**
"Sekarang kita coba lakukan aktivitas seru: Membaca Kode! 

Perhatikan baik-baik kode yang ada di layar. Variabel `score` isinya 85, `task_done` isinya True, dan `late_submission` isinya False. 
Lalu program akan mengecek: `score >= 80 and task_done and not late_submission`. 

Ayo tebak, tulisan apa yang akan muncul di layar? 
Betul sekali! Jawabannya adalah 'Excellent'. Semua syaratnya terpenuhi, karena 85 lebih dari 80, tugasnya beres, dan dia juga tidak terlambat mengumpulkan tugas!"

---

## Slide 48: Mini Activity: Lengkapi Kondisi ✍️
**(Visual: Slide 48 - Melengkapi kode program pengecekan)**

**Audio (Host / Pengisi Suara):**
"Ayo kita coba satu aktivitas lagi! Coba lengkapi kondisi ini ya. 

Ada tiga syarat supaya seseorang boleh masuk wahana: Umurnya minimal 12 tahun, tingginya minimal 140 cm, dan dia tidak sedang sakit. 
Nah, kalau kita mau gabungkan ketiganya di dalam Python, kira-kira kodenya seperti apa ya? 

Yak, benar sekali! Jawabannya adalah: `if age >= 12 and height >= 140 and not sick`. Keren banget!"

---

## Slide 49: Mini Activity: Ringkas Nested Kode 🧹
**(Visual: Slide 49 - Mengubah nested condition menjadi logical operators)**

**Audio (Host / Pengisi Suara):**
"Aktivitas selanjutnya: Ayo kita ringkas kode yang panjang ini! 

Lihat deh kode awal kita. Wah, sangat bertingkat dan menjorok jauh ke dalam, ya? Ada `if has_account`, lalu di dalamnya ada `if password_correct`, dan di dalamnya lagi ada `if not blocked`. 
Pasti kalian sudah tahu kan cara merangkumnya? 

Betul sekali! Kita pakai saja operator `and`. Jawabannya menjadi: `if has_account and password_correct and not blocked`. Jauh lebih mudah dibaca, kan?"

---

## Slide 50: Mini Project: Smart Checker 👨‍🎓
**(Visual: Slide 50 - Contoh project Smart Checker dengan nested condition)**

**Audio (Host / Pengisi Suara):**
"Sekarang, kita masuk ke Mini Project: Membuat Smart Checker! 

Tugas kita adalah membuat program yang bisa mengecek status belajar siswa. 
Kalau nilainya 85 ke atas dan tugasnya selesai, program bilang 'Siap ikut kelas advance'. 
Kalau nilainya 70 ke atas dan tugas selesai, bilang 'Lanjut latihan level berikutnya'. 
Kalau tugasnya belum selesai, langsung bilang 'Selesaikan tugas dulu'. 
Dan kalau tidak memenuhi itu semua, bilang 'Perlu belajar ulang'. 

Coba perhatikan kodenya. Di sini kita menggunakan Nested Condition. Program mengecek status tugas atau `task_done` dulu, baru kemudian mengecek nilainya satu per satu!"

---

## Slide 51: Versi Lebih Ringkas Mini Project ✨
**(Visual: Slide 51 - Versi Smart Checker dengan elif)**

**Audio (Host / Pengisi Suara):**
"Nah, tahukah kalian kalau Mini Project tadi bisa kita tulis dengan versi yang sedikit lebih ringkas? 

Alih-alih menggunakan Nested Condition, kita bisa langsung menggunakan Multi-Branch atau `elif`! 
Pertama kita cek dulu: kalau tugasnya belum selesai, langsung tampilkan pesannya. 
Kalau ternyata sudah selesai, baru kita urutkan dari nilai 85 ke atas, lalu nilai 70 ke atas. 

Keduanya sama-sama benar kok! Bedanya, versi bertingkat bagus untuk menunjukkan pengecekan tahap demi tahap, sedangkan versi `elif` terlihat lebih rapi karena baris kodenya tidak terlalu menjorok ke dalam."

---

## Slide 54: Apa Itu Financial Literacy? 🧠
**(Visual: Slide 54 - Pengertian Financial Literacy dan contoh pertanyaannya)**

**Audio (Host / Pengisi Suara):**
"Sekarang kita masuk ke topik yang super penting: Financial Literacy! Apa sih itu? 

Financial literacy adalah kemampuan kita untuk memahami dan mengatur uang dengan bijak. 
Ini bukan berarti kita sama sekali tidak boleh membeli barang yang kita suka, ya! Tapi kita belajar untuk berpikir dan bertanya dulu sebelum membeli sesuatu. 

Misalnya, 'Apakah barang ini benar-benar aku perlukan?', 'Apakah uang jajanku cukup?', atau 'Apakah ada kebutuhan lain yang lebih penting?'. 
Nah, pertanyaan-pertanyaan ini ternyata bisa kita masukkan ke dalam program Python sebagai *condition*!"

---

## Slide 55: Kebutuhan vs Keinginan + Python Conditionals 📊
**(Visual: Slide 55 - Judul Bagian 1)**

**Audio (Host / Pengisi Suara):**
"Di bagian pertama ini, kita akan belajar membedakan apa itu Kebutuhan dan apa itu Keinginan, lalu kita akan menggabungkan aturannya dengan Python Conditionals yang baru saja kita pelajari. Yuk, kita mulai!"

---

## Slide 56: Apa Itu Kebutuhan? 🛒
**(Visual: Slide 56 - Penjelasan dan contoh kebutuhan)**

**Audio (Host / Pengisi Suara):**
"Pertama-tama, apa sih Kebutuhan itu? 

Kebutuhan adalah sesuatu yang sangat penting untuk hidup, belajar, atau menjalankan aktivitas kita sehari-hari. 
Contohnya makanan, air minum, buku sekolah, alat tulis, transportasi, sampai kuota internet untuk belajar. 

Nah, kebutuhan ini adalah hal yang **harus selalu diprioritaskan** untuk dibeli terlebih dahulu. Jangan sampai uang kita habis untuk hal lain, lalu kebutuhan utama malah tidak terbeli!"

---

## Slide 57: Apa Itu Keinginan? 🎮
**(Visual: Slide 57 - Penjelasan dan contoh keinginan)**

**Audio (Host / Pengisi Suara):**
"Lalu, apa bedanya dengan Keinginan? 

Keinginan adalah sesuatu yang kita sukai, tapi sebenarnya tidak harus kita beli sekarang juga. 
Misalnya snack tambahan, skin game, gantungan kunci lucu, atau minuman kekinian. 

Boleh nggak sih kita membeli keinginan? Tentu saja boleh! Tapi ingat syarat utamanya: belilah keinginan **setelah semua kebutuhan utama kita sudah aman** dan terpenuhi."

---

## Slide 58: Analogi Sederhana ⚖️
**(Visual: Slide 58 - Analogi uang 50 ribu dan pilihan barang)**

**Audio (Host / Pengisi Suara):**
"Supaya lebih jelas, mari kita bayangkan sebuah kasus. 

Misalkan kamu punya uang 50 ribu rupiah. Lalu kamu ingin membeli buku tulis seharga 15 ribu, makan siang 20 ribu, stiker lucu 10 ribu, dan minuman manis 15 ribu. 
Coba perhatikan, kalau ditotal semuanya pasti lebih dari 50 ribu, kan? 

Karena uang kita terbatas, kita tidak bisa membeli semuanya sekaligus. Di sinilah kita harus membuat pilihan: Mana yang merupakan kebutuhan dan harus didahulukan? Dan mana yang cuma keinginan sehingga bisa ditunda dulu?"

---

## Slide 59: Dari Keputusan ke Kondisi 💻
**(Visual: Slide 59 - Konsep kebutuhan dan keinginan dalam if-else)**

**Audio (Host / Pengisi Suara):**
"Nah, cara kita mengambil keputusan tadi ternyata sama persis loh seperti cara kerja program komputer! 

Kalau barang itu adalah kebutuhan, kita prioritaskan. 
Kalau barang itu adalah keinginan, kita cek dulu apakah ada sisa budget. 
Dan kalau uangnya memang tidak cukup, ya kita tunda pembeliannya. 

Coba lihat kode Python di layar. Persis seperti yang biasa kita pikirkan sehari-hari, kan? Kita menggunakan `if`, `elif`, dan `else` untuk mengatur keputusan belanja kita!"

---

## Slide 60: Program Simple: Cek Kategori 🔍
**(Visual: Slide 60 - Contoh program pengecekan kategori barang)**

**Audio (Host / Pengisi Suara):**
"Yuk kita lihat contoh program sederhananya! 

Di sini kita punya barang 'buku tulis' yang kategorinya adalah 'kebutuhan'. 
Lalu program akan mengecek: `if category == 'kebutuhan'`, maka program akan mencetak *'Buku tulis adalah kebutuhan. Prioritaskan untuk dibeli.'* 

Bayangkan kalau komputermu bisa otomatis mengingatkanmu seperti ini setiap kali kamu mau jajan barang yang sebenarnya tidak perlu. Keren banget, kan?"