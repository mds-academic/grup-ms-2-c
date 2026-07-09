Bisa banget. Jadi setelah **Slide 51**, kita masuk ke bagian **Financial Literacy Application** dulu. Slide rangkuman yang tadinya Slide 52 digeser ke akhir.

Menurutku tambahan ini perlu dibuat sebagai **jembatan**:

> “Tadi kita belajar conditional untuk mengambil keputusan. Sekarang kita akan memakai conditional untuk membantu kita membuat keputusan keuangan.”

Berikut tambahan slide-nya.

---

# Tambahan Setelah Slide 51

## Financial Literacy Application with Python

---

## Slide 52 — Dari Coding ke Keputusan Keuangan

Kita sudah belajar bahwa program bisa mengambil keputusan menggunakan:

```python
if
elif
else
```

Sekarang kita akan memakai konsep itu untuk membantu mengambil keputusan saat menggunakan uang.

Contohnya:

Apakah barang ini benar-benar dibutuhkan?
Apakah uangku cukup?
Apakah aku masih punya sisa budget?
Apakah pembelian ini sebaiknya dilakukan sekarang atau ditunda?

---

## Slide 53 — Apa Itu Financial Literacy?

**Financial literacy** adalah kemampuan memahami dan mengatur uang dengan bijak.

Bukan berarti kita tidak boleh membeli barang yang kita suka.

Tapi kita belajar untuk bertanya dulu:

“Apakah ini benar-benar perlu?”
“Apakah uangku cukup?”
“Apakah ada kebutuhan lain yang lebih penting?”

Dalam coding, pertanyaan seperti ini bisa dibuat menjadi kondisi.

---

# Bagian 1

## Kebutuhan vs Keinginan + Python Conditionals

---

## Slide 54 — Apa Itu Kebutuhan?

**Kebutuhan** adalah sesuatu yang penting untuk hidup, belajar, atau menjalankan aktivitas utama.

Contoh kebutuhan:

* Makanan
* Air minum
* Buku sekolah
* Alat tulis
* Transportasi
* Kuota internet untuk belajar

Kebutuhan biasanya harus diprioritaskan dulu.

---

## Slide 55 — Apa Itu Keinginan?

**Keinginan** adalah sesuatu yang kita suka, tapi belum tentu harus dibeli sekarang.

Contoh keinginan:

* Snack tambahan
* Skin game
* Gantungan kunci lucu
* Minuman kekinian
* Stiker
* Aksesoris HP

Keinginan boleh dibeli, tapi sebaiknya setelah kebutuhan utama aman.

---

## Slide 56 — Analogi Sederhana

Bayangkan kamu punya uang Rp50.000.

Kamu ingin membeli:

* Buku tulis Rp15.000
* Makan siang Rp20.000
* Stiker lucu Rp10.000
* Minuman manis Rp15.000

Kalau uang terbatas, kita perlu memilih.

Mana yang harus dibeli dulu?
Mana yang bisa ditunda?

Di sinilah kita belajar membedakan kebutuhan dan keinginan.

---

## Slide 57 — Mengubah Keputusan Keuangan Menjadi Kondisi

Dalam kehidupan nyata:

Kalau barang adalah kebutuhan, prioritaskan.
Kalau barang adalah keinginan, cek dulu sisa uang.
Kalau uang tidak cukup, tunda pembelian.

Dalam Python, ini bisa dibuat seperti:

```python
if category == "kebutuhan":
    print("Prioritaskan pembelian")
elif category == "keinginan":
    print("Cek budget dulu")
else:
    print("Kategori belum jelas")
```

---

## Slide 58 — Program Simple: Cek Kebutuhan atau Keinginan

```python
item = "buku tulis"
category = "kebutuhan"

if category == "kebutuhan":
    print(item, "adalah kebutuhan. Prioritaskan untuk dibeli.")
elif category == "keinginan":
    print(item, "adalah keinginan. Cek budget dulu.")
else:
    print("Kategori barang belum diketahui.")
```

Output:

```python
buku tulis adalah kebutuhan. Prioritaskan untuk dibeli.
```

---

## Slide 59 — Menambahkan Harga dan Uang

Sekarang kita buat program yang lebih realistis.

Program akan mengecek:

Apakah barang termasuk kebutuhan atau keinginan?
Apakah uang cukup untuk membeli barang itu?

```python
item = "buku tulis"
category = "kebutuhan"
price = 15000
money = 50000

if category == "kebutuhan" and money >= price:
    print("Beli", item)
elif category == "kebutuhan" and money < price:
    print("Uang belum cukup, cari alternatif lebih murah")
elif category == "keinginan" and money >= price:
    print("Boleh beli, tapi pastikan kebutuhan utama sudah aman")
else:
    print("Tunda pembelian")
```

---

## Slide 60 — Cara Membaca Programnya

```python
if category == "kebutuhan" and money >= price:
```

Artinya:

Kalau barang adalah kebutuhan
dan uang cukup,
maka barang boleh dibeli.

```python
elif category == "keinginan" and money >= price:
```

Artinya:

Kalau barang adalah keinginan
dan uang cukup,
barang boleh dibeli, tapi tetap harus hati-hati.

---

## Slide 61 — Program dengan Input dari Pengguna

Agar program lebih interaktif, kita bisa memakai `input()`.

```python
item = input("Nama barang: ")
category = input("Kategori barang (kebutuhan/keinginan): ")
price = int(input("Harga barang: "))
money = int(input("Uang yang kamu punya: "))

if category == "kebutuhan" and money >= price:
    print("Rekomendasi: Beli", item)
elif category == "kebutuhan" and money < price:
    print("Rekomendasi: Cari pilihan yang lebih murah atau menabung dulu")
elif category == "keinginan" and money >= price:
    print("Rekomendasi: Boleh dipertimbangkan, tapi cek kebutuhan lain dulu")
else:
    print("Rekomendasi: Tunda dulu pembelian", item)
```

---

## Slide 62 — Kenapa Program Ini Berguna?

Program ini membantu kita berpikir sebelum membeli sesuatu.

Bukan hanya bertanya:

“Uangku cukup atau tidak?”

Tapi juga bertanya:

“Barang ini kebutuhan atau keinginan?”

Karena uang cukup belum tentu berarti harus langsung dibelanjakan.

---

## Slide 63 — Mini Activity: Tentukan Kategori

Tentukan apakah barang berikut termasuk kebutuhan atau keinginan.

| Barang                            | Kebutuhan / Keinginan |
| --------------------------------- | --------------------- |
| Buku tulis                        | Kebutuhan             |
| Air minum                         | Kebutuhan             |
| Skin game                         | Keinginan             |
| Snack tambahan                    | Keinginan             |
| Pulsa internet untuk kelas online | Kebutuhan             |
| Gantungan kunci                   | Keinginan             |

Setelah itu, pilih 3 barang dan masukkan ke dalam program Python.

---

# Bagian 2

## Budgeting & Perencanaan Pengeluaran + Variabel

---

## Slide 64 — Apa Itu Budgeting?

**Budgeting** adalah membuat rencana penggunaan uang.

Tujuannya agar uang tidak habis tanpa sadar.

Contoh:

Kamu punya uang Rp100.000.

Kamu bisa membaginya menjadi:

* Makan: Rp40.000
* Transportasi: Rp20.000
* Alat sekolah: Rp25.000
* Tabungan: Rp15.000

Dengan budget, kita tahu uang akan digunakan untuk apa.

---

## Slide 65 — Budgeting Itu Seperti Membagi Kotak

Bayangkan uangmu seperti satu kotak besar.

Lalu kamu membaginya ke beberapa kotak kecil:

Kotak makan.
Kotak transportasi.
Kotak sekolah.
Kotak tabungan.
Kotak hiburan.

Dalam Python, setiap kotak bisa disimpan dalam **variable**.

---

## Slide 66 — Mengingat Lagi: Apa Itu Variable?

**Variable** adalah tempat untuk menyimpan data.

Contoh:

```python
money = 100000
food_budget = 40000
transport_budget = 20000
school_budget = 25000
saving_budget = 15000
```

Artinya:

Program sedang menyimpan nilai uang ke dalam beberapa nama variable.

---

## Slide 67 — Contoh Variable untuk Budget

```python
total_money = 100000

food_budget = 40000
transport_budget = 20000
school_budget = 25000
saving_budget = 15000
```

Setiap variable punya tugas masing-masing.

`total_money` menyimpan jumlah uang utama.
`food_budget` menyimpan anggaran makan.
`transport_budget` menyimpan anggaran transportasi.
`school_budget` menyimpan anggaran kebutuhan sekolah.
`saving_budget` menyimpan anggaran tabungan.

---

## Slide 68 — Menghitung Total Budget

Kita bisa menjumlahkan semua budget.

```python
total_money = 100000

food_budget = 40000
transport_budget = 20000
school_budget = 25000
saving_budget = 15000

total_budget = food_budget + transport_budget + school_budget + saving_budget

print("Total budget:", total_budget)
```

Output:

```python
Total budget: 100000
```

---

## Slide 69 — Mengecek Apakah Budget Aman

Program bisa mengecek apakah total budget melebihi uang yang dimiliki.

```python
total_money = 100000

food_budget = 40000
transport_budget = 20000
school_budget = 25000
saving_budget = 15000

total_budget = food_budget + transport_budget + school_budget + saving_budget

if total_budget <= total_money:
    print("Budget aman")
else:
    print("Budget melebihi uang yang dimiliki")
```

Karena total budget sama dengan uang yang dimiliki, maka hasilnya:

```python
Budget aman
```

---

## Slide 70 — Kalau Budget Terlalu Besar

Contoh:

```python
total_money = 100000

food_budget = 50000
transport_budget = 30000
school_budget = 30000
saving_budget = 20000

total_budget = food_budget + transport_budget + school_budget + saving_budget

if total_budget <= total_money:
    print("Budget aman")
else:
    print("Budget melebihi uang yang dimiliki")
```

Total budget:

```python
50000 + 30000 + 30000 + 20000 = 130000
```

Padahal uang hanya Rp100.000.

Maka program menampilkan:

```python
Budget melebihi uang yang dimiliki
```

---

## Slide 71 — Menambahkan Sisa Uang

Kita juga bisa menghitung sisa uang.

```python
total_money = 100000

food_budget = 40000
transport_budget = 20000
school_budget = 25000
saving_budget = 10000

total_budget = food_budget + transport_budget + school_budget + saving_budget
remaining_money = total_money - total_budget

print("Total budget:", total_budget)
print("Sisa uang:", remaining_money)
```

Output:

```python
Total budget: 95000
Sisa uang: 5000
```

---

## Slide 72 — Program Budget dengan Kondisi

Sekarang kita gabungkan variable dan conditional.

```python
total_money = 100000

food_budget = 40000
transport_budget = 20000
school_budget = 25000
saving_budget = 10000

total_budget = food_budget + transport_budget + school_budget + saving_budget
remaining_money = total_money - total_budget

if total_budget > total_money:
    print("Budget terlalu besar")
elif remaining_money == 0:
    print("Budget pas, tidak ada sisa uang")
elif remaining_money > 0:
    print("Budget aman, masih ada sisa uang")
else:
    print("Cek ulang budget")
```

---

## Slide 73 — Membuat Skenario Belanja

Sekarang kita buat contoh skenario.

Kamu punya uang Rp100.000.
Kamu ingin membeli:

* Makan siang Rp25.000
* Buku Rp30.000
* Minuman Rp15.000
* Stiker Rp10.000

Program akan menghitung total belanja dan sisa uang.

```python
money = 100000

lunch = 25000
book = 30000
drink = 15000
sticker = 10000

total_spending = lunch + book + drink + sticker
remaining_money = money - total_spending

print("Total belanja:", total_spending)
print("Sisa uang:", remaining_money)
```

---

## Slide 74 — Mengevaluasi Skenario Belanja

Tambahkan kondisi:

```python
money = 100000

lunch = 25000
book = 30000
drink = 15000
sticker = 10000

total_spending = lunch + book + drink + sticker
remaining_money = money - total_spending

if total_spending > money:
    print("Belanja melebihi uang yang dimiliki")
elif remaining_money >= 20000:
    print("Belanja aman, masih ada sisa cukup")
elif remaining_money > 0:
    print("Belanja masih aman, tapi sisa uang sedikit")
else:
    print("Uang habis, tidak ada sisa")
```

---

## Slide 75 — Menggabungkan Kebutuhan, Keinginan, dan Budget

Sekarang program bisa menjadi lebih pintar.

Program tidak hanya mengecek harga, tapi juga kategori barang.

Contoh:

```python
money = 50000

item = "stiker"
category = "keinginan"
price = 10000
need_budget_left = 15000

if category == "kebutuhan" and money >= price:
    print("Beli karena ini kebutuhan")
elif category == "keinginan" and money >= price and need_budget_left > 0:
    print("Boleh beli, tapi pastikan kebutuhan tetap aman")
elif category == "keinginan" and money < price:
    print("Tunda dulu, uang belum cukup")
else:
    print("Cek ulang keputusan")
```

---

## Slide 76 — Kenapa Kita Pakai Data?

Dalam program, keputusan dibuat berdasarkan data.

Contoh data:

* Nama barang
* Kategori barang
* Harga barang
* Jumlah uang
* Sisa budget
* Apakah barang termasuk kebutuhan
* Apakah barang bisa ditunda

Kalau datanya berubah, keputusan program juga bisa berubah.

---

## Slide 77 — Contoh Analisis Keputusan

Misalnya:

```python
money = 50000
item = "minuman kekinian"
category = "keinginan"
price = 25000
need_budget_left = 10000
```

Program mungkin memberi rekomendasi:

```python
Lebih baik ditunda
```

Kenapa?

Karena barang tersebut adalah keinginan, harganya cukup besar, dan uang untuk kebutuhan masih harus dijaga.

---

Iya, ini penting banget karena topik **Risiko Finansial + Nested Condition** justru nyambung banget dengan materi sebelumnya.

Posisi paling enak:

**Setelah Slide 77 — Contoh Analisis Keputusan**
**Sebelum Slide 78 — Simple Project: Shopping Decision Checker**

Jadi alurnya jadi:

1. Conditional dasar
2. Nested condition
3. Logical operators
4. Kebutuhan vs keinginan
5. Budgeting
6. **Risiko finansial low–medium–high**
7. Simple project
8. Tugas besar kehadiran

Berikut tambahan slide-nya.

---

# Tambahan Materi

## Risiko Finansial + Nested Condition

---

## Slide 78 — Apa Itu Risiko Finansial?

**Risiko finansial** adalah kemungkinan uang kita berkurang, habis, atau tidak menghasilkan sesuai harapan.

Contoh sederhana:

Kalau kita menyimpan uang di tempat aman, risikonya kecil.
Kalau kita memakai uang untuk sesuatu yang hasilnya belum pasti, risikonya lebih besar.

Dalam kehidupan sehari-hari, kita perlu memahami:

“Apakah keputusan ini aman?”
“Apakah ada kemungkinan rugi?”
“Apakah aku siap kalau hasilnya tidak sesuai harapan?”

---

## Slide 79 — Risiko Itu Seperti Level Kesulitan

Bayangkan kamu bermain game.

Ada level:

* Easy
* Normal
* Hard

Dalam keuangan, risiko juga bisa dibayangkan seperti level:

* **Low risk**
* **Medium risk**
* **High risk**

Semakin tinggi risikonya, semakin besar kemungkinan hasilnya berubah-ubah.

---

## Slide 80 — Low Risk

**Low risk** artinya risiko rendah.

Biasanya lebih aman, tetapi hasilnya juga tidak terlalu besar.

Contoh sederhana:

* Menabung
* Menyimpan uang untuk kebutuhan penting
* Membeli barang yang benar-benar dibutuhkan
* Membuat dana cadangan

Low risk cocok untuk uang yang tidak boleh hilang atau uang yang akan dipakai dalam waktu dekat.

---

## Slide 81 — Medium Risk

**Medium risk** artinya risiko sedang.

Masih bisa dipertimbangkan, tetapi perlu lebih hati-hati.

Contoh sederhana:

* Membeli barang untuk dijual lagi
* Mengikuti project kecil yang butuh modal
* Membeli perlengkapan untuk membuat produk
* Mencoba ide usaha kecil

Medium risk cocok kalau kita sudah punya rencana dan masih punya sisa uang aman.

---

## Slide 82 — High Risk

**High risk** artinya risiko tinggi.

Kemungkinan untung bisa ada, tetapi kemungkinan rugi juga lebih besar.

Contoh sederhana:

* Menggunakan hampir semua uang untuk satu hal
* Membeli barang mahal yang belum tentu berguna
* Ikut tren hanya karena takut ketinggalan
* Mengeluarkan modal tanpa rencana

High risk perlu dipikirkan dengan sangat hati-hati.

---

## Slide 83 — Cara Sederhana Menilai Risiko

Kita bisa menilai risiko dengan beberapa pertanyaan:

1. Apakah uang ini akan dipakai untuk kebutuhan penting?
2. Apakah uang yang dipakai terlalu besar?
3. Apakah masih ada sisa uang setelah keputusan ini?
4. Apakah keputusan ini punya hasil yang belum pasti?
5. Apakah kita punya rencana cadangan?

Semakin banyak jawaban yang membuat kita ragu, semakin tinggi risikonya.

---

## Slide 84 — Contoh Penilaian Risiko

Contoh 1:

Kamu punya uang Rp100.000.
Kamu membeli buku sekolah Rp25.000.

Risiko: **Low risk**

Karena buku sekolah adalah kebutuhan dan uang masih tersisa.

---

Contoh 2:

Kamu punya uang Rp100.000.
Kamu membeli bahan untuk jualan Rp60.000.

Risiko: **Medium risk**

Karena ada peluang berguna, tetapi hasil jualannya belum pasti.

---

Contoh 3:

Kamu punya uang Rp100.000.
Kamu memakai Rp95.000 untuk membeli barang tren yang belum tentu dipakai.

Risiko: **High risk**

Karena hampir semua uang habis untuk sesuatu yang belum tentu penting.

---

## Slide 85 — Mengubah Risiko Menjadi Kondisi Python

Dalam Python, kita bisa membuat program yang mengecek level risiko.

Contoh data yang dipakai:

```python id="72k4oa"
money = 100000
price = 25000
category = "kebutuhan"
has_plan = True
```

Program bisa mengecek:

Apakah barang kebutuhan atau keinginan?
Apakah harga terlalu besar?
Apakah masih ada sisa uang?
Apakah pengguna punya rencana?

---

## Slide 86 — Kenapa Cocok Menggunakan Nested Condition?

Risiko sering tidak bisa dicek hanya dengan satu pertanyaan.

Kadang program perlu bertanya bertahap.

Contoh:

Pertama, cek dulu kategorinya.

Kalau kebutuhan, cek apakah uang cukup.
Kalau keinginan, cek apakah sisa uang masih aman.
Kalau untuk usaha, cek apakah ada rencana.

Karena pengecekannya bertahap, kita bisa memakai **nested condition**.

---

## Slide 87 — Program Simple: Cek Risiko Berdasarkan Kategori

```python id="7ffxmi"
category = "kebutuhan"
money = 100000
price = 25000

if category == "kebutuhan":
    if money >= price:
        print("Risiko: Low")
        print("Alasan: Barang ini kebutuhan dan uang cukup.")
    else:
        print("Risiko: Medium")
        print("Alasan: Barang ini kebutuhan, tapi uang belum cukup.")
else:
    if price > money * 0.5:
        print("Risiko: High")
        print("Alasan: Harga barang terlalu besar untuk keinginan.")
    else:
        print("Risiko: Medium")
        print("Alasan: Barang ini keinginan, jadi perlu dipertimbangkan.")
```

---

## Slide 88 — Cara Membaca Program Risiko

Bagian pertama:

```python id="7pu4kg"
if category == "kebutuhan":
```

Program mengecek apakah barang termasuk kebutuhan.

Kalau iya, program masuk ke pengecekan berikutnya:

```python id="n12x3d"
if money >= price:
```

Artinya:

Kalau uang cukup, risikonya rendah.

Tapi kalau uang belum cukup, risikonya naik menjadi medium.

---

## Slide 89 — Nested Condition untuk Rekomendasi Multi-Level

Sekarang kita buat rekomendasi dengan 3 level risiko.

```python id="i22b48"
money = 100000
price = 60000
category = "keinginan"

remaining_money = money - price

if category == "kebutuhan":
    if money >= price:
        print("Risiko: Low")
        print("Rekomendasi: Boleh dibeli karena ini kebutuhan.")
    else:
        print("Risiko: Medium")
        print("Rekomendasi: Cari alternatif yang lebih murah.")
else:
    if remaining_money < 10000:
        print("Risiko: High")
        print("Rekomendasi: Tunda dulu karena sisa uang terlalu sedikit.")
    elif price > money * 0.5:
        print("Risiko: Medium")
        print("Rekomendasi: Pertimbangkan lagi karena harganya cukup besar.")
    else:
        print("Risiko: Low")
        print("Rekomendasi: Boleh dipertimbangkan jika kebutuhan sudah aman.")
```

---

## Slide 90 — Menambahkan Faktor Rencana

Untuk keputusan yang berhubungan dengan usaha kecil atau project, kita bisa menambahkan variable:

```python id="vohsyv"
has_plan = True
```

Artinya:

Apakah pengguna punya rencana yang jelas?

Contoh rencana:

* Tahu barangnya untuk apa
* Tahu perkiraan biaya
* Tahu target hasil
* Tahu risiko kalau tidak berhasil

---

## Slide 91 — Program Risiko dengan Rencana

```python id="l63105"
money = 100000
price = 60000
category = "usaha"
has_plan = True

remaining_money = money - price

if category == "usaha":
    if has_plan:
        if remaining_money >= 20000:
            print("Risiko: Medium")
            print("Alasan: Ada rencana dan masih ada sisa uang aman.")
        else:
            print("Risiko: High")
            print("Alasan: Ada rencana, tapi sisa uang terlalu sedikit.")
    else:
        print("Risiko: High")
        print("Alasan: Belum ada rencana yang jelas.")
else:
    print("Gunakan pengecekan kebutuhan atau keinginan.")
```

Ini contoh nested condition karena pengecekannya bertahap:

Pertama cek kategori.
Lalu cek apakah punya rencana.
Lalu cek sisa uang.

---

## Slide 92 — Membuat Alasan Logis dari Program

Program yang baik tidak hanya memberi hasil:

```python id="2rh6fu"
Risiko: High
```

Tapi juga memberi alasan:

```python id="15pcxi"
Alasan: Sisa uang terlalu sedikit setelah membeli barang.
```

Kenapa alasan penting?

Agar pengguna tahu mengapa program memberi rekomendasi tersebut.

Dalam financial literacy, keputusan harus bisa dijelaskan, bukan hanya ditebak.

---

## Slide 93 — Contoh Output Program Risiko

Contoh input/data:

```python id="rdyv2p"
money = 100000
price = 80000
category = "keinginan"
```

Output:

```python id="q5sfwc"
Risiko: High
Rekomendasi: Tunda dulu karena sisa uang terlalu sedikit.
Alasan: Barang ini keinginan dan memakai sebagian besar uang.
```

Keputusan ini masuk akal karena uang tersisa hanya Rp20.000.

---

## Slide 94 — Mini Activity: Tentukan Risiko

Tentukan level risiko dari skenario berikut.

| Skenario                                                         | Risiko |
| ---------------------------------------------------------------- | ------ |
| Membeli air minum Rp5.000 dari uang Rp50.000                     | Low    |
| Membeli buku sekolah Rp30.000 dari uang Rp40.000                 | Medium |
| Membeli skin game Rp90.000 dari uang Rp100.000                   | High   |
| Membeli bahan jualan Rp50.000 dari uang Rp100.000 tanpa rencana  | High   |
| Membeli bahan jualan Rp40.000 dari uang Rp100.000 dengan rencana | Medium |

---

## Slide 95 — Mini Activity: Lengkapi Nested Condition

Lengkapi kode berikut.

```python id="443zfl"
money = 100000
price = 70000
category = "keinginan"

remaining_money = money - price

if category == "kebutuhan":
    print("Cek sebagai kebutuhan")
else:
    if remaining_money < 20000:
        print("Risiko: ______")
    else:
        print("Risiko: ______")
```

Jawaban yang mungkin:

```python id="2ihb18"
if category == "kebutuhan":
    print("Cek sebagai kebutuhan")
else:
    if remaining_money < 20000:
        print("Risiko: High")
    else:
        print("Risiko: Medium")
```

---

## Slide 96 — Menghubungkan Risiko dengan Budget

Risiko tidak berdiri sendiri.

Risiko bisa dilihat dari:

* Kategori barang
* Harga barang
* Jumlah uang
* Sisa uang
* Budget yang sudah dibuat
* Apakah ada rencana atau tidak

Jadi semakin lengkap data yang dimiliki program, semakin baik rekomendasi yang bisa diberikan.

---

# Update ke Project Setelah Materi Risiko

Bagian project sebelumnya bisa di-upgrade sedikit.

---

## Slide 97 — Simple Project: Financial Decision Checker

Buat program sederhana yang membantu pengguna mengecek:

1. Apakah barang termasuk kebutuhan atau keinginan.
2. Apakah uang cukup.
3. Berapa sisa uang setelah membeli.
4. Apakah risikonya low, medium, atau high.
5. Apa rekomendasi akhirnya.

---

## Slide 98 — Starter Code Simple Project

```python id="no53rs"
item = input("Nama barang: ")
category = input("Kategori (kebutuhan/keinginan): ")
price = int(input("Harga barang: "))
money = int(input("Uang yang dimiliki: "))

remaining_money = money - price

print("\n=== HASIL ANALISIS ===")

if category == "kebutuhan":
    if money >= price:
        print("Risiko: Low")
        print("Rekomendasi: Beli", item)
        print("Alasan: Barang ini kebutuhan dan uang cukup.")
        print("Sisa uang:", remaining_money)
    else:
        print("Risiko: Medium")
        print("Rekomendasi: Cari alternatif lebih murah")
        print("Alasan: Barang ini kebutuhan, tapi uang belum cukup.")
else:
    if money < price:
        print("Risiko: High")
        print("Rekomendasi: Tunda dulu")
        print("Alasan: Uang belum cukup.")
    elif remaining_money < 10000:
        print("Risiko: High")
        print("Rekomendasi: Tunda dulu")
        print("Alasan: Sisa uang terlalu sedikit.")
    elif price > money * 0.5:
        print("Risiko: Medium")
        print("Rekomendasi: Pertimbangkan lagi")
        print("Alasan: Harga barang cukup besar untuk keinginan.")
    else:
        print("Risiko: Low")
        print("Rekomendasi: Boleh dipertimbangkan")
        print("Alasan: Uang cukup dan sisa uang masih aman.")
        print("Sisa uang:", remaining_money)
```

---

## Slide 99 — Update Tugas Besar Kehadiran

# Tugas Besar: Smart Budget & Risk Planner

Buat program Python yang membantu pengguna merencanakan pengeluaran dan mengevaluasi risiko keputusan keuangan.

Program harus bisa:

1. Menyimpan jumlah uang pengguna.
2. Menyimpan beberapa kategori budget.
3. Menghitung total budget.
4. Menghitung sisa uang.
5. Mengecek apakah budget aman atau melebihi uang.
6. Mengevaluasi minimal 1 barang sebagai kebutuhan atau keinginan.
7. Mengecek level risiko: `Low`, `Medium`, atau `High`.
8. Memberikan rekomendasi beli, tunda, cari alternatif, atau revisi budget.
9. Menampilkan alasan logis dari rekomendasi.

---

## Slide 100 — Update Ketentuan Program

Program minimal memiliki variable berikut:

```python id="jazbfv"
total_money
food_budget
transport_budget
school_budget
saving_budget
item
category
price
risk_level
```

Program juga harus menggunakan:

```python id="ixp0dz"
if
elif
else
```

Dan wajib menggunakan:

```python id="h0bb89"
nested condition
```

Serta minimal satu logical operator:

```python id="esawxb"
and
or
not
```

---

## Slide 101 — Update Kriteria Kehadiran / Completion

Tugas dihitung selesai jika program:

| Kriteria                                          | Wajib |
| ------------------------------------------------- | ----- |
| Memiliki variable untuk menyimpan uang dan budget | Ya    |
| Menghitung total budget                           | Ya    |
| Menghitung sisa uang                              | Ya    |
| Menggunakan `if`, `elif`, `else`                  | Ya    |
| Menggunakan nested condition                      | Ya    |
| Menggunakan minimal satu logical operator         | Ya    |
| Mengevaluasi kebutuhan atau keinginan             | Ya    |
| Menentukan risiko `Low`, `Medium`, atau `High`    | Ya    |
| Menampilkan rekomendasi akhir                     | Ya    |
| Menampilkan alasan logis                          | Ya    |

---

## Slide 102 — Update Rangkuman Akhir

Hari ini kita belajar bahwa:

**Conditional** membuat program bisa mengambil keputusan.

`if` digunakan untuk mengecek satu kondisi.

`else` digunakan jika kondisi `if` tidak terpenuhi.

`elif` digunakan jika ada banyak pilihan.

**Nested condition** adalah kondisi di dalam kondisi.

`and`, `or`, dan `not` digunakan untuk menggabungkan beberapa kondisi.

Dalam financial literacy, conditional bisa dipakai untuk mengevaluasi:

* kebutuhan vs keinginan
* budget aman atau tidak
* risiko low, medium, atau high
* barang sebaiknya dibeli atau ditunda

Variable bisa dipakai untuk menyimpan:

* jumlah uang
* budget
* harga barang
* total pengeluaran
* sisa uang
* level risiko

---

## Slide 103 — Update Exit Ticket

Jawab 4 pertanyaan ini:

1. Apa fungsi `if` dalam Python?
2. Apa bedanya kebutuhan dan keinginan?
3. Apa bedanya risiko low, medium, dan high?
4. Bagaimana nested condition membantu program memberi rekomendasi?

Contoh jawaban:

`if` digunakan untuk menjalankan perintah kalau sebuah kondisi benar.

Kebutuhan adalah sesuatu yang penting, sedangkan keinginan adalah sesuatu yang bisa ditunda.

Risiko low berarti lebih aman, medium berarti perlu dipertimbangkan, dan high berarti harus sangat hati-hati.

Nested condition membantu program mengecek beberapa hal secara bertahap sebelum memberi keputusan.

---

Catatan penting: untuk level SMA, aku sarankan istilah “instrumen risiko” jangan dulu diarahkan ke investasi spesifik seperti saham, crypto, reksa dana, atau deposito. Lebih aman pakai konteks **keputusan pengeluaran, tabungan, usaha kecil, dan pembelian barang**, supaya tetap financial literacy tanpa masuk ke rekomendasi finansial yang terlalu berat.
