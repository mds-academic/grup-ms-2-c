Bisa. Untuk topik ini, alurnya jangan langsung masuk ke `nested condition`, karena anak bisa kaget. Lebih aman dibuat bertahap seperti ini:

**Conditional dasar → if → if else → elif / multi-branch → nested condition → logical operators → complex condition → simplify condition**

Berikut draft isi deck-nya.

---

# Deck: Nested Condition & Multi-Branch Decisions

## Python Basics SMA

---

## Slide 1 — Judul

# Membuat Program yang Bisa Mengambil Keputusan

Dalam coding, program tidak hanya berjalan lurus dari atas ke bawah.

Kadang program harus bisa memilih:

“Kalau kondisinya begini, lakukan ini.”
“Tapi kalau kondisinya begitu, lakukan yang lain.”

Di Python, konsep ini disebut **conditional**.

---

## Slide 2 — Pernah Mengambil Keputusan?

Dalam kehidupan sehari-hari, kita sering membuat keputusan.

Contoh:

Kalau hujan, bawa payung.
Kalau lapar, makan.
Kalau baterai HP tinggal 5%, charge HP.
Kalau nilai ujian tinggi, lanjut ke level berikutnya.

Kita membuat keputusan berdasarkan **kondisi**.

Program juga bisa melakukan hal yang sama.

---

## Slide 3 — Apa Itu Conditional?

**Conditional** adalah cara membuat program memilih tindakan berdasarkan kondisi tertentu.

Sederhananya:

> Kalau sesuatu benar, program akan melakukan sesuatu.

Contoh di kehidupan nyata:

Kalau lampu merah, kendaraan berhenti.
Kalau lampu hijau, kendaraan jalan.

Dalam program:

Kalau jawaban benar, skor bertambah.
Kalau password salah, login gagal.

---

## Slide 4 — Conditional Itu Seperti Pintu Pilihan

Bayangkan kamu sedang berdiri di depan pintu.

Pintunya hanya terbuka kalau kamu punya kunci.

Kalau punya kunci → boleh masuk.
Kalau tidak punya kunci → tidak bisa masuk.

Di coding, “punya kunci” adalah **kondisi**.

Program akan mengecek:

Apakah kondisinya benar?

Kalau benar, program menjalankan perintah tertentu.

---

## Slide 5 — Conditional Paling Sederhana: `if`

Di Python, conditional paling dasar menggunakan `if`.

```python
age = 17

if age >= 17:
    print("Boleh membuat KTP")
```

Artinya:

Kalau `age` lebih besar atau sama dengan 17, tampilkan teks `"Boleh membuat KTP"`.

Kalau kondisinya salah, program tidak menjalankan isi `if`.

---

## Slide 6 — Cara Membaca `if`

```python
if age >= 17:
    print("Boleh membuat KTP")
```

Cara membacanya:

“Jika umur lebih dari atau sama dengan 17, maka tampilkan pesan.”

Bagian ini adalah kondisi:

```python
age >= 17
```

Bagian ini adalah aksi yang dilakukan jika kondisi benar:

```python
print("Boleh membuat KTP")
```

---

## Slide 7 — Kondisi Menghasilkan True atau False

Setiap kondisi di Python akan menghasilkan salah satu dari dua jawaban:

```python
True
```

atau

```python
False
```

Contoh:

```python
age = 17

print(age >= 17)
```

Hasilnya:

```python
True
```

Karena 17 memang lebih besar atau sama dengan 17.

---

## Slide 8 — Kalau Kondisinya Salah?

Contoh:

```python
age = 15

if age >= 17:
    print("Boleh membuat KTP")
```

Program akan mengecek:

Apakah `15 >= 17`?

Jawabannya:

```python
False
```

Karena kondisinya salah, maka pesan tidak akan muncul.

---

## Slide 9 — Menambahkan Pilihan Lain dengan `else`

Kadang program perlu melakukan sesuatu kalau kondisi salah.

Untuk itu, kita bisa menggunakan `else`.

```python
age = 15

if age >= 17:
    print("Boleh membuat KTP")
else:
    print("Belum boleh membuat KTP")
```

Artinya:

Kalau umur minimal 17, boleh membuat KTP.
Kalau tidak, belum boleh membuat KTP.

---

## Slide 10 — `if else` Itu Seperti Dua Jalan

Bayangkan kamu sampai di persimpangan.

Kalau jalan kiri terbuka, lewat kiri.
Kalau tidak, lewat kanan.

Dalam coding:

Kalau kondisi benar → jalankan bagian `if`.
Kalau kondisi salah → jalankan bagian `else`.

Program hanya memilih salah satu jalan.

---

## Slide 11 — Contoh `if else` di Program Game

```python
answer = "A"

if answer == "A":
    print("Jawaban benar!")
else:
    print("Jawaban salah.")
```

Kalau isi `answer` adalah `"A"`, program menampilkan:

```python
Jawaban benar!
```

Kalau isi `answer` bukan `"A"`, program menampilkan:

```python
Jawaban salah.
```

---

## Slide 12 — Saat Pilihannya Lebih dari Dua

Tidak semua keputusan hanya punya dua pilihan.

Contoh nilai:

90–100 → Sangat Baik
75–89 → Baik
60–74 → Cukup
Di bawah 60 → Perlu latihan lagi

Kalau pilihannya banyak, kita bisa memakai:

```python
elif
```

`elif` artinya:

“Kalau kondisi sebelumnya salah, coba cek kondisi ini.”

---

## Slide 13 — Multi-Branch Decision

**Multi-branch decision** adalah keputusan dengan banyak cabang pilihan.

Seperti memilih jalan:

Kalau nilai 90 ke atas → Sangat Baik
Kalau nilai 75 ke atas → Baik
Kalau nilai 60 ke atas → Cukup
Kalau tidak masuk semua → Perlu latihan lagi

Di Python, kita bisa membuatnya dengan:

```python
if
elif
elif
else
```

---

## Slide 14 — Contoh Multi-Branch di Python

```python
score = 82

if score >= 90:
    print("Sangat Baik")
elif score >= 75:
    print("Baik")
elif score >= 60:
    print("Cukup")
else:
    print("Perlu latihan lagi")
```

Hasilnya:

```python
Baik
```

Karena 82 belum mencapai 90, tapi sudah mencapai 75.

---

## Slide 15 — Kenapa Urutan Kondisi Penting?

Lihat contoh ini:

```python
score = 95

if score >= 60:
    print("Cukup")
elif score >= 75:
    print("Baik")
elif score >= 90:
    print("Sangat Baik")
```

Hasilnya:

```python
Cukup
```

Padahal skornya 95.

Kenapa?

Karena Python membaca dari atas ke bawah.
Saat menemukan kondisi pertama yang benar, Python langsung menjalankan bagian itu dan melewati sisanya.

---

## Slide 16 — Urutan yang Benar

Untuk kategori nilai, kita perlu mulai dari syarat tertinggi.

```python
score = 95

if score >= 90:
    print("Sangat Baik")
elif score >= 75:
    print("Baik")
elif score >= 60:
    print("Cukup")
else:
    print("Perlu latihan lagi")
```

Hasilnya:

```python
Sangat Baik
```

Jadi, dalam multi-branch decision, urutan kondisi harus dipikirkan dengan hati-hati.

---

## Slide 17 — Apa Itu Nested Condition?

**Nested condition** adalah conditional di dalam conditional.

Sederhananya:

> Setelah program mengecek satu kondisi, program mengecek kondisi lain di dalamnya.

Contoh kehidupan nyata:

Kalau kamu punya tiket, kamu boleh masuk bioskop.
Tapi setelah itu dicek lagi:
Kalau umurmu cukup, kamu boleh menonton filmnya.

Jadi ada pengecekan di dalam pengecekan.

---

## Slide 18 — Analogi Nested Condition

Bayangkan kamu masuk ke gedung.

Pintu pertama mengecek:

Apakah kamu punya kartu akses?

Kalau iya, kamu masuk ke pintu kedua.

Pintu kedua mengecek:

Apakah kamu punya izin masuk ruangan khusus?

Jadi, kamu harus lolos kondisi pertama dulu sebelum masuk ke kondisi kedua.

Itulah nested condition.

---

## Slide 19 — Contoh Nested Condition di Python

```python
has_ticket = True
age = 16

if has_ticket:
    if age >= 13:
        print("Boleh masuk studio")
    else:
        print("Umur belum cukup")
else:
    print("Harus punya tiket dulu")
```

Program pertama mengecek:

Apakah punya tiket?

Kalau iya, baru program mengecek:

Apakah umur minimal 13?

---

## Slide 20 — Cara Membaca Nested Condition

```python
if has_ticket:
    if age >= 13:
        print("Boleh masuk studio")
```

Cara membacanya:

Kalau punya tiket, cek lagi umurnya.
Kalau umurnya 13 atau lebih, boleh masuk studio.

Jadi kondisi kedua hanya dicek kalau kondisi pertama benar.

---

## Slide 21 — Nested Condition di Program Game

Contoh dalam game:

Pemain hanya bisa masuk level bonus jika:

Pemain sudah menyelesaikan level 1.
Dan pemain punya minimal 100 koin.

Dengan nested condition:

```python
level_complete = True
coin = 120

if level_complete:
    if coin >= 100:
        print("Masuk level bonus")
    else:
        print("Koin belum cukup")
else:
    print("Selesaikan level dulu")
```

---

## Slide 22 — Masalah Nested Condition

Nested condition bisa berguna.

Tapi kalau terlalu banyak, kodenya bisa terlihat menjorok terlalu dalam dan sulit dibaca.

Contoh:

```python
if login:
    if verified:
        if balance >= price:
            print("Pembelian berhasil")
```

Kode seperti ini masih bisa dibaca, tapi kalau terlalu panjang bisa membingungkan.

Karena itu, kita perlu belajar **logical operators**.

---

## Slide 23 — Menggabungkan Kondisi dengan Logical Operators

Kadang kita ingin mengecek beberapa kondisi sekaligus.

Di Python, kita bisa memakai:

```python
and
or
not
```

Ketiganya disebut **logical operators**.

Logical operators membantu program membuat keputusan yang lebih kompleks.

---

## Slide 24 — Operator `and`

`and` digunakan kalau semua kondisi harus benar.

Contoh kehidupan nyata:

Kamu boleh ikut lomba kalau:

Sudah daftar.
Sudah membayar.
Sudah mengumpulkan karya.

Kalau salah satu belum, belum boleh ikut.

---

## Slide 25 — Contoh `and` di Python

```python
registered = True
paid = True
submitted = True

if registered and paid and submitted:
    print("Boleh ikut lomba")
else:
    print("Belum bisa ikut lomba")
```

Program akan menampilkan `"Boleh ikut lomba"` hanya kalau ketiga kondisi bernilai `True`.

---

## Slide 26 — Operator `or`

`or` digunakan kalau cukup salah satu kondisi benar.

Contoh kehidupan nyata:

Kamu bisa login kalau menggunakan:

Email, atau username, atau nomor HP.

Tidak harus semuanya. Salah satu saja cukup.

---

## Slide 27 — Contoh `or` di Python

```python
use_email = False
use_username = True
use_phone = False

if use_email or use_username or use_phone:
    print("Bisa login")
else:
    print("Pilih salah satu cara login")
```

Hasilnya:

```python
Bisa login
```

Karena salah satu kondisi, yaitu `use_username`, bernilai `True`.

---

## Slide 28 — Operator `not`

`not` digunakan untuk membalik nilai kondisi.

Kalau awalnya `True`, menjadi `False`.
Kalau awalnya `False`, menjadi `True`.

Contoh kehidupan nyata:

Kalau belum hujan, kita bisa bermain di luar.

Dalam Python:

```python
is_raining = False

if not is_raining:
    print("Boleh bermain di luar")
```

Artinya:

Kalau tidak sedang hujan, boleh bermain di luar.

---

## Slide 29 — Menggabungkan 3+ Kondisi

Sekarang kita bisa membuat kondisi yang lebih lengkap.

Contoh:

Siswa bisa ikut kelas lanjutan jika:

Nilai minimal 75.
Sudah menyelesaikan tugas.
Tidak sedang remedial.

```python
score = 80
task_done = True
remedial = False

if score >= 75 and task_done and not remedial:
    print("Boleh ikut kelas lanjutan")
else:
    print("Belum boleh ikut kelas lanjutan")
```

---

## Slide 30 — Cara Membaca Kondisi Kompleks

```python
score >= 75 and task_done and not remedial
```

Bacanya:

Nilai harus minimal 75.
Tugas harus sudah selesai.
Siswa tidak sedang remedial.

Karena memakai `and`, semua syarat harus benar.

Kalau ada satu saja yang salah, hasil akhirnya menjadi `False`.

---

## Slide 31 — Prioritas Operator Logika

Python punya urutan dalam membaca operator logika.

Urutannya:

1. `not`
2. `and`
3. `or`

Artinya, Python akan mengecek `not` dulu, lalu `and`, lalu `or`.

Contoh:

```python
True or False and False
```

Python membaca bagian `and` dulu:

```python
False and False
```

Hasilnya `False`.

Lalu:

```python
True or False
```

Hasil akhirnya:

```python
True
```

---

## Slide 32 — Gunakan Tanda Kurung agar Lebih Jelas

Walaupun Python punya urutan sendiri, kita bisa memakai tanda kurung agar kode lebih mudah dibaca.

Contoh:

```python
if (score >= 75 and task_done) or has_bonus:
    print("Lolos")
```

Dengan tanda kurung, kita tahu bahwa Python harus mengecek ini dulu:

```python
score >= 75 and task_done
```

Lalu hasilnya dibandingkan dengan:

```python
has_bonus
```

Tanda kurung membuat kondisi lebih jelas.

---

## Slide 33 — Truth Table Sederhana untuk `and`

`and` hanya menghasilkan `True` kalau semua kondisi benar.

| Kondisi A | Kondisi B | A and B |
| --------- | --------- | ------- |
| True      | True      | True    |
| True      | False     | False   |
| False     | True      | False   |
| False     | False     | False   |

Cara mengingat:

`and` itu seperti “semua harus lengkap”.

---

## Slide 34 — Truth Table Sederhana untuk `or`

`or` menghasilkan `True` kalau minimal satu kondisi benar.

| Kondisi A | Kondisi B | A or B |
| --------- | --------- | ------ |
| True      | True      | True   |
| True      | False     | True   |
| False     | True      | True   |
| False     | False     | False  |

Cara mengingat:

`or` itu seperti “salah satu saja cukup”.

---

## Slide 35 — Truth Table Sederhana untuk `not`

`not` membalik nilai.

| Kondisi | not Kondisi |
| ------- | ----------- |
| True    | False       |
| False   | True        |

Cara mengingat:

`not` itu seperti tombol pembalik.

---

## Slide 36 — Mengevaluasi Kondisi Kompleks

Contoh:

```python
score = 80
task_done = True
remedial = False

score >= 75 and task_done and not remedial
```

Kita cek satu per satu.

```python
score >= 75
```

Hasilnya:

```python
True
```

```python
task_done
```

Hasilnya:

```python
True
```

```python
not remedial
```

Karena `remedial = False`, maka:

```python
not remedial
```

menjadi:

```python
True
```

Jadi:

```python
True and True and True
```

Hasil akhirnya:

```python
True
```

---

## Slide 37 — Dari Nested Condition ke Logical Operators

Kode nested:

```python
if level_complete:
    if coin >= 100:
        if not game_over:
            print("Masuk level bonus")
```

Bisa disederhanakan menjadi:

```python
if level_complete and coin >= 100 and not game_over:
    print("Masuk level bonus")
```

Kode kedua lebih pendek dan lebih mudah dibaca.

---

## Slide 38 — Kapan Pakai Nested Condition?

Pakai nested condition kalau pengecekan memang bertahap.

Contoh:

Pertama cek login.
Kalau login benar, baru cek role user.
Kalau role admin, tampilkan menu admin.

```python
if login:
    if role == "admin":
        print("Tampilkan menu admin")
    else:
        print("Tampilkan menu user")
else:
    print("Silakan login dulu")
```

Nested cocok kalau setiap tahap punya pesan atau aksi yang berbeda.

---

## Slide 39 — Kapan Pakai Logical Operators?

Pakai logical operators kalau beberapa syarat bisa dicek sekaligus.

Contoh:

```python
if login and role == "admin":
    print("Tampilkan menu admin")
```

Ini cocok kalau program hanya perlu tahu:

Apakah semua syarat terpenuhi?

Kalau iya, jalankan aksi.

---

## Slide 40 — Contoh Kasus: Sistem Diskon

Sebuah toko memberi diskon jika pelanggan:

Total belanja minimal 100.000
Dan pelanggan adalah member
Atau pelanggan punya kupon

Contoh kode:

```python
total = 120000
is_member = True
has_coupon = False

if (total >= 100000 and is_member) or has_coupon:
    print("Mendapat diskon")
else:
    print("Tidak mendapat diskon")
```

Tanda kurung penting supaya kondisi mudah dipahami.

---

## Slide 41 — Membaca Sistem Diskon

```python
(total >= 100000 and is_member) or has_coupon
```

Artinya:

Pelanggan mendapat diskon jika:

Total belanja minimal 100.000 dan dia member.

Atau:

Pelanggan punya kupon.

Jadi ada dua jalur untuk mendapat diskon.

---

## Slide 42 — Contoh Kasus: Akses Aplikasi

Seseorang boleh masuk aplikasi jika:

Username benar.
Password benar.
Akun tidak diblokir.

```python
username_correct = True
password_correct = True
blocked = False

if username_correct and password_correct and not blocked:
    print("Login berhasil")
else:
    print("Login gagal")
```

Karena memakai `and`, semua syarat utama harus benar.

Karena memakai `not blocked`, akun harus tidak diblokir.

---

## Slide 43 — Contoh Kasus: Rekomendasi Aktivitas

Program akan memberi rekomendasi aktivitas berdasarkan cuaca dan waktu.

```python
weather = "cerah"
time = "pagi"

if weather == "cerah" and time == "pagi":
    print("Jogging di taman")
elif weather == "cerah" and time == "siang":
    print("Minum es dan istirahat")
elif weather == "hujan":
    print("Aktivitas di rumah")
else:
    print("Cek kondisi lagi")
```

Ini contoh multi-branch decision dengan kondisi gabungan.

---

## Slide 44 — Kesalahan Umum 1: Lupa Tanda `==`

Dalam Python:

`=` dipakai untuk menyimpan data.
`==` dipakai untuk membandingkan data.

Salah:

```python
if password = "12345":
    print("Login")
```

Benar:

```python
if password == "12345":
    print("Login")
```

---

## Slide 45 — Kesalahan Umum 2: Kondisi Terlalu Panjang

Contoh kondisi yang terlalu panjang:

```python
if score >= 75 and task_done == True and remedial == False and attendance >= 80:
    print("Lolos")
```

Bisa dibuat lebih rapi:

```python
passed_score = score >= 75
completed_task = task_done
not_remedial = not remedial
good_attendance = attendance >= 80

if passed_score and completed_task and not_remedial and good_attendance:
    print("Lolos")
```

Kode lebih panjang sedikit, tapi lebih mudah dibaca.

---

## Slide 46 — Kesalahan Umum 3: Salah Urutan `elif`

Salah:

```python
score = 92

if score >= 60:
    print("Cukup")
elif score >= 75:
    print("Baik")
elif score >= 90:
    print("Sangat Baik")
```

Benar:

```python
score = 92

if score >= 90:
    print("Sangat Baik")
elif score >= 75:
    print("Baik")
elif score >= 60:
    print("Cukup")
else:
    print("Perlu latihan lagi")
```

Mulai dari kondisi yang paling spesifik atau paling tinggi.

---

## Slide 47 — Mini Activity: Baca Kode

Perhatikan kode berikut:

```python
score = 85
task_done = True
late_submission = False

if score >= 80 and task_done and not late_submission:
    print("Excellent")
else:
    print("Keep trying")
```

Pertanyaan:

Apa output dari program ini?

Jawaban:

```python
Excellent
```

Karena:

`score >= 80` bernilai `True`
`task_done` bernilai `True`
`not late_submission` juga bernilai `True`

Jadi hasil akhirnya:

```python
True and True and True
```

---

## Slide 48 — Mini Activity: Lengkapi Kondisi

Buat program yang mengecek apakah seseorang boleh masuk wahana.

Syarat:

Umur minimal 12 tahun.
Tinggi minimal 140 cm.
Tidak sedang sakit.

Kode awal:

```python
age = 13
height = 145
sick = False

if __________________:
    print("Boleh masuk wahana")
else:
    print("Belum boleh masuk wahana")
```

Jawaban:

```python
if age >= 12 and height >= 140 and not sick:
```

---

## Slide 49 — Mini Activity: Ubah Nested Menjadi Lebih Ringkas

Kode awal:

```python
if has_account:
    if password_correct:
        if not blocked:
            print("Login berhasil")
```

Ubah menjadi satu kondisi menggunakan logical operators.

Jawaban:

```python
if has_account and password_correct and not blocked:
    print("Login berhasil")
```

---

## Slide 50 — Mini Project: Smart Student Checker

Buat program sederhana yang mengecek status siswa.

Syarat:

Jika nilai minimal 85 dan tugas selesai, tampilkan `"Siap ikut kelas advance"`.

Jika nilai minimal 70 dan tugas selesai, tampilkan `"Lanjut latihan level berikutnya"`.

Jika tugas belum selesai, tampilkan `"Selesaikan tugas dulu"`.

Selain itu, tampilkan `"Perlu belajar ulang"`.

Contoh kode:

```python
score = 82
task_done = True

if task_done:
    if score >= 85:
        print("Siap ikut kelas advance")
    elif score >= 70:
        print("Lanjut latihan level berikutnya")
    else:
        print("Perlu belajar ulang")
else:
    print("Selesaikan tugas dulu")
```

---

## Slide 51 — Versi Lebih Ringkas Mini Project

Kode sebelumnya juga bisa dibuat dengan multi-branch seperti ini:

```python
score = 82
task_done = True

if not task_done:
    print("Selesaikan tugas dulu")
elif score >= 85:
    print("Siap ikut kelas advance")
elif score >= 70:
    print("Lanjut latihan level berikutnya")
else:
    print("Perlu belajar ulang")
```

Keduanya benar.

Bedanya:

Versi nested menunjukkan pengecekan bertahap.
Versi multi-branch terlihat lebih rapi dan tidak terlalu menjorok.

---

## Slide 52 — Rangkuman

Hari ini kita belajar bahwa:

**Conditional** membuat program bisa mengambil keputusan.

`if` digunakan untuk mengecek satu kondisi.

`else` digunakan jika kondisi `if` tidak terpenuhi.

`elif` digunakan jika ada banyak pilihan.

**Nested condition** adalah kondisi di dalam kondisi.

`and`, `or`, dan `not` digunakan untuk menggabungkan beberapa kondisi.

Kondisi yang terlalu panjang bisa disederhanakan agar kode lebih mudah dibaca.

---

## Slide 53 — Exit Ticket

Jawab 3 pertanyaan ini:

1. Apa fungsi `if` dalam Python?

2. Apa bedanya `and` dan `or`?

3. Kapan kita sebaiknya memakai nested condition?

Contoh jawaban:

`if` digunakan untuk menjalankan perintah kalau sebuah kondisi benar.

`and` butuh semua kondisi benar, sedangkan `or` cukup salah satu kondisi benar.

Nested condition dipakai kalau pengecekan perlu dilakukan secara bertahap.

---

## Catatan Alur untuk Deck

Menurutku, urutan paling aman untuk deck SMA Python ini:

1. **Conditional secara umum**
2. **`if`**
3. **`if else`**
4. **`elif` / multi-branch**
5. **Nested condition**
6. **Logical operators**
7. **Truth table**
8. **Prioritas `not`, `and`, `or`**
9. **Menyederhanakan kondisi**
10. **Mini project**

Jadi walaupun topik utamanya “Nested Condition & Multi-Branch Decisions + Complex Logical Operators”, anak tetap punya fondasi dulu sebelum masuk ke kondisi yang lebih kompleks.
