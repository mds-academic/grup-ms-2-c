# Deck Python SMA

## Optimasi Algoritma, Advanced Functions, Modular Design, dan Financial Literacy

---

# BAGIAN 1

## Optimasi Algoritma Dasar

---

## Slide 1 — Judul

# Membuat Program yang Lebih Pintar dan Efisien

Hari ini kita akan belajar cara membuat program yang bukan hanya bisa berjalan, tapi juga berjalan dengan cara yang lebih rapi dan efisien.

Kita akan belajar:

* Optimasi algoritma dasar
* Function dengan beberapa parameter
* Function dengan `return`
* Modular design
* Aplikasi financial literacy dengan Python

---

## Slide 2 — Apa Itu Algoritma?

**Algoritma** adalah langkah-langkah untuk menyelesaikan masalah.

Contoh sehari-hari:

Mau membuat mie instan:

1. Rebus air.
2. Masukkan mie.
3. Tunggu matang.
4. Campur bumbu.
5. Sajikan.

Dalam coding, algoritma juga seperti resep langkah demi langkah.

---

## Slide 3 — Algoritma Bisa Berbeda-Beda

Masalah yang sama bisa diselesaikan dengan cara yang berbeda.

Contoh:

Kita ingin mencari nama “Budi” di daftar siswa.

Cara 1:

Cek nama satu per satu dari awal sampai ketemu.

Cara 2:

Kalau datanya sudah rapi atau terurut, kita bisa mencari dengan cara yang lebih cepat.

Jadi, tidak semua algoritma punya jumlah langkah yang sama.

---

## Slide 4 — Apa Itu Optimasi Algoritma?

**Optimasi algoritma** adalah usaha membuat langkah penyelesaian menjadi lebih efisien.

Efisien artinya:

* Langkahnya lebih sedikit
* Waktunya lebih cepat
* Kodenya lebih rapi
* Tidak melakukan hal yang tidak perlu

Sederhananya:

> Program tetap menyelesaikan tugas yang sama, tapi dengan cara yang lebih pintar.

---

## Slide 5 — Analogi Optimasi: Mencari Buku

Bayangkan kamu mencari buku Matematika di rak.

Cara lambat:

Kamu cek semua buku satu per satu dari kiri ke kanan.

Cara lebih cepat:

Kamu langsung cari di bagian buku pelajaran, lalu cari label “Matematika”.

Tujuannya sama: menemukan buku.

Tapi cara kedua lebih efisien karena langkahnya lebih sedikit.

---

## Slide 6 — Apa Itu Step Count?

**Step count** adalah jumlah langkah yang dilakukan oleh algoritma.

Contoh:

Jika program mengecek 5 data satu per satu, maka kurang lebih ada 5 langkah pengecekan.

Kalau program mengecek 100 data satu per satu, maka ada sekitar 100 langkah pengecekan.

Semakin banyak langkah, biasanya program semakin lama berjalan.

---

## Slide 7 — Contoh Step Count Sederhana

Kita punya daftar angka:

```python
numbers = [3, 7, 10, 15, 20]
```

Kita ingin mencari angka `15`.

Program akan mengecek:

1. Apakah 3 adalah 15? Bukan.
2. Apakah 7 adalah 15? Bukan.
3. Apakah 10 adalah 15? Bukan.
4. Apakah 15 adalah 15? Iya.

Step count: 4 pengecekan.

---

## Slide 8 — Contoh Python: Mencari Angka

```python
numbers = [3, 7, 10, 15, 20]
target = 15

steps = 0

for number in numbers:
    steps += 1
    if number == target:
        print("Angka ditemukan!")
        break

print("Jumlah langkah:", steps)
```

Output:

```python
Angka ditemukan!
Jumlah langkah: 4
```

Program berhenti saat angka ditemukan.

---

## Slide 9 — Kenapa Ada `break`?

`break` digunakan untuk menghentikan loop.

Kalau target sudah ditemukan, program tidak perlu lanjut mengecek data berikutnya.

Tanpa `break`, program tetap mengecek sampai akhir.

Padahal jawabannya sudah ditemukan.

Ini contoh optimasi sederhana.

---

## Slide 10 — Algoritma Lambat: Tidak Berhenti Saat Sudah Ketemu

```python
numbers = [3, 7, 10, 15, 20]
target = 15

steps = 0

for number in numbers:
    steps += 1
    if number == target:
        print("Angka ditemukan!")

print("Jumlah langkah:", steps)
```

Output:

```python
Angka ditemukan!
Jumlah langkah: 5
```

Program tetap mengecek sampai akhir, walaupun target sudah ditemukan di langkah ke-4.

---

## Slide 11 — Algoritma Lebih Efisien

```python
numbers = [3, 7, 10, 15, 20]
target = 15

steps = 0

for number in numbers:
    steps += 1
    if number == target:
        print("Angka ditemukan!")
        break

print("Jumlah langkah:", steps)
```

Output:

```python
Angka ditemukan!
Jumlah langkah: 4
```

Dengan `break`, program berhenti lebih cepat.

---

## Slide 12 — Membandingkan Dua Algoritma

Algoritma A:

Mengecek semua data sampai akhir.

Algoritma B:

Berhenti saat data sudah ditemukan.

Jika target ada di tengah daftar, algoritma B lebih efisien.

Karena algoritma B tidak melakukan pengecekan yang tidak perlu.

---

## Slide 13 — Mini Activity: Hitung Step Count

Perhatikan daftar ini:

```python
numbers = [5, 8, 12, 20, 25, 30]
target = 20
```

Jika program mencari dari kiri ke kanan dan berhenti saat ketemu, berapa step count-nya?

Jawaban:

```python
4
```

Karena program mengecek 5, 8, 12, lalu 20.

---

## Slide 14 — Latihan: Tebak Output

```python
numbers = [2, 4, 6, 8, 10]
target = 6

steps = 0

for number in numbers:
    steps += 1
    if number == target:
        break

print(steps)
```

Apa output-nya?

Jawaban:

```python
3
```

Karena angka 6 ditemukan pada pengecekan ke-3.

---

## Slide 15 — Contoh Optimasi: Menghindari Kode Berulang

Kode lambat atau kurang rapi:

```python
print("Halo, Andi")
print("Halo, Budi")
print("Halo, Citra")
print("Halo, Dina")
```

Kalau jumlah namanya banyak, kita harus menulis banyak baris.

Versi lebih efisien:

```python
names = ["Andi", "Budi", "Citra", "Dina"]

for name in names:
    print("Halo,", name)
```

Kode lebih pendek dan mudah diubah.

---

## Slide 16 — Kenapa Loop Bisa Membantu Optimasi?

Loop membantu kita melakukan aksi yang sama berkali-kali tanpa menulis kode berulang.

Jika datanya bertambah, kita cukup mengubah isi list.

Bukan menambah banyak baris `print()`.

Program menjadi:

* Lebih rapi
* Lebih mudah dirawat
* Lebih mudah dikembangkan

---

## Slide 17 — Algoritma Lambat: Menjumlah Manual

```python
total = 10 + 20 + 30 + 40 + 50

print(total)
```

Ini masih mudah kalau angkanya sedikit.

Tapi kalau angkanya 100 data, cara ini melelahkan.

---

## Slide 18 — Algoritma Lebih Efisien: Menggunakan Loop

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print(total)
```

Output:

```python
150
```

Program bisa dipakai untuk jumlah data yang lebih banyak.

---

## Slide 19 — Lebih Efisien Lagi: Menggunakan `sum()`

Python sudah punya function bawaan bernama `sum()`.

```python
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print(total)
```

Output:

```python
150
```

Ini lebih singkat dan mudah dibaca.

---

## Slide 20 — Membandingkan 3 Cara

| Cara    | Contoh                  | Kapan Cocok         |
| ------- | ----------------------- | ------------------- |
| Manual  | `10 + 20 + 30`          | Data sangat sedikit |
| Loop    | `for number in numbers` | Ingin paham proses  |
| `sum()` | `sum(numbers)`          | Ingin kode ringkas  |

Semua bisa benar.

Tapi konteksnya berbeda.

---

## Slide 21 — Optimasi Tidak Selalu Berarti Kode Terpendek

Kode pendek belum tentu paling mudah dipahami.

Optimasi yang baik biasanya mempertimbangkan:

* Jumlah langkah
* Kecepatan
* Kerapian kode
* Kemudahan membaca kode
* Kemudahan memperbaiki bug

Jadi, pilih algoritma yang cocok dengan konteks.

---

## Slide 22 — Latihan: Pilih Algoritma yang Lebih Efisien

Kasus:

Kamu ingin menghitung total nilai dari 30 siswa.

Cara A:

Menulis semua nilai satu per satu dalam operasi tambah.

Cara B:

Menyimpan nilai dalam list, lalu memakai loop atau `sum()`.

Mana yang lebih efisien?

Jawaban:

Cara B.

Karena data lebih mudah diatur dan program tidak perlu ditulis panjang.

---

## Slide 23 — Latihan: Perbaiki Kode Lambat

Kode awal:

```python
print("Item 1")
print("Item 2")
print("Item 3")
print("Item 4")
print("Item 5")
```

Ubah menjadi lebih efisien dengan loop.

Jawaban:

```python
for i in range(1, 6):
    print("Item", i)
```

---

## Slide 24 — Mini Project Optimasi

Buat program yang mencari nama dalam daftar siswa.

Program harus:

1. Menyimpan daftar nama.
2. Mencari satu nama target.
3. Menghitung jumlah langkah pencarian.
4. Berhenti jika nama sudah ditemukan.
5. Menampilkan apakah nama ditemukan atau tidak.

Starter code:

```python
students = ["Alya", "Bima", "Caca", "Dion", "Eka"]
target = "Dion"

steps = 0
found = False

for student in students:
    steps += 1
    if student == target:
        found = True
        break

if found:
    print("Nama ditemukan")
else:
    print("Nama tidak ditemukan")

print("Jumlah langkah:", steps)
```

---

# BAGIAN 2

## Function Secara General

---

## Slide 25 — Apa Itu Function?

**Function** adalah kumpulan perintah yang diberi nama.

Kalau kita butuh menjalankan perintah itu lagi, kita cukup memanggil namanya.

Sederhananya:

> Function itu seperti tombol otomatis.

Sekali ditekan, beberapa perintah langsung berjalan.

---

## Slide 26 — Analogi Function: Mesin Jus

Bayangkan ada mesin jus.

Kita masukkan buah, lalu mesin memprosesnya, lalu keluar jus.

Di coding:

* Input: bahan yang masuk
* Proses: langkah-langkah di dalam function
* Output: hasil yang keluar

Function membantu program bekerja lebih rapi.

---

## Slide 27 — Function Seperti Resep

Resep membuat roti punya langkah-langkah:

1. Siapkan bahan.
2. Campur adonan.
3. Panggang.
4. Sajikan.

Daripada menulis semua langkah berulang-ulang, kita bisa memberi nama:

**buat_roti**

Saat butuh membuat roti, kita cukup menjalankan:

```python
buat_roti()
```

---

## Slide 28 — Kenapa Function Berguna?

Function berguna karena:

* Kode tidak berulang-ulang
* Program lebih rapi
* Program lebih mudah dibaca
* Bagian program lebih mudah diperbaiki
* Function bisa dipakai ulang

Function membuat program besar terasa seperti kumpulan bagian kecil.

---

## Slide 29 — Function dalam Kehidupan Sehari-Hari

Contoh function dalam kehidupan:

| Function      | Input         | Output          |
| ------------- | ------------- | --------------- |
| Mesin jus     | Buah          | Jus             |
| Kalkulator    | Angka         | Hasil hitung    |
| Mesin ATM     | Kartu dan PIN | Akses akun      |
| Aplikasi maps | Lokasi tujuan | Rute perjalanan |

Function menerima sesuatu, memprosesnya, lalu bisa menghasilkan sesuatu.

---

# BAGIAN 3

## Function di Python

---

## Slide 30 — Bentuk Dasar Function di Python

Di Python, function dibuat menggunakan `def`.

```python
def greet():
    print("Halo!")
```

Untuk menjalankan function, kita panggil namanya:

```python
greet()
```

Output:

```python
Halo!
```

---

## Slide 31 — Cara Membaca Function

```python
def greet():
    print("Halo!")
```

Cara membacanya:

“Buat function bernama `greet`. Saat function dipanggil, tampilkan teks `Halo!`.”

Bagian ini adalah nama function:

```python
greet
```

Bagian ini adalah isi function:

```python
print("Halo!")
```

---

## Slide 32 — Function Harus Dipanggil

Kalau function hanya dibuat tapi tidak dipanggil, isinya tidak akan berjalan.

```python
def greet():
    print("Halo!")
```

Kode di atas belum menampilkan apa-apa.

Agar berjalan, kita harus memanggil:

```python
greet()
```

---

## Slide 33 — Latihan: Tebak Output

```python
def say_hello():
    print("Selamat pagi!")

say_hello()
say_hello()
```

Apa output-nya?

Jawaban:

```python
Selamat pagi!
Selamat pagi!
```

Karena function dipanggil dua kali.

---

## Slide 34 — Function dengan Parameter

**Parameter** adalah data yang dikirim ke dalam function.

Analogi:

Kalau function adalah mesin jus, parameter adalah buah yang dimasukkan.

Contoh:

```python
def greet(name):
    print("Halo,", name)
```

`name` adalah parameter.

---

## Slide 35 — Contoh Function dengan Parameter

```python
def greet(name):
    print("Halo,", name)

greet("Alya")
greet("Bima")
```

Output:

```python
Halo, Alya
Halo, Bima
```

Function-nya sama, tapi datanya berbeda.

---

## Slide 36 — Function dengan Multiple Parameters

Function juga bisa punya lebih dari satu parameter.

Contoh:

```python
def introduce(name, age):
    print("Namaku", name)
    print("Umurku", age)
```

Memanggil function:

```python
introduce("Alya", 16)
```

Output:

```python
Namaku Alya
Umurku 16
```

---

## Slide 37 — Parameter Itu Seperti Formulir

Bayangkan kamu mengisi formulir:

* Nama
* Umur
* Kelas

Function juga bisa menerima beberapa data sekaligus.

```python
def student_info(name, grade, school):
    print(name)
    print(grade)
    print(school)
```

Setiap parameter menyimpan satu informasi.

---

## Slide 38 — Latihan: Lengkapi Function

Lengkapi kode berikut agar function bisa menampilkan nama dan skor.

```python
def show_score(_____, _____):
    print("Nama:", name)
    print("Score:", score)

show_score("Dina", 90)
```

Jawaban:

```python
def show_score(name, score):
    print("Nama:", name)
    print("Score:", score)

show_score("Dina", 90)
```

---

## Slide 39 — Apa Itu `return`?

`return` digunakan untuk mengembalikan hasil dari function.

Kalau `print()` hanya menampilkan hasil ke layar, `return` memberikan hasil agar bisa dipakai lagi oleh program.

Sederhananya:

`print()` = menunjukkan hasil.
`return` = memberikan hasil untuk dipakai lagi.

---

## Slide 40 — Analogi `return`: Mesin Kasir

Bayangkan mesin kasir menghitung total belanja.

Kalau mesin hanya bicara “Totalnya 50.000”, itu seperti `print()`.

Tapi kalau mesin memberikan struk yang bisa dipakai untuk pembayaran, itu seperti `return`.

`return` membuat hasil function bisa diproses lagi.

---

## Slide 41 — Function dengan `print()`

```python
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)
```

Output:

```python
8
```

Program menampilkan hasil, tapi hasilnya tidak disimpan untuk dipakai lagi.

---

## Slide 42 — Function dengan `return`

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)

print(result)
```

Output:

```python
8
```

Sekarang hasil `5 + 3` disimpan ke variable `result`.

---

## Slide 43 — Kenapa `return` Penting?

Dengan `return`, hasil function bisa digunakan untuk proses berikutnya.

Contoh:

```python
def add_numbers(a, b):
    return a + b

total = add_numbers(5, 3)
final_score = total * 10

print(final_score)
```

Output:

```python
80
```

Hasil function dipakai lagi untuk menghitung `final_score`.

---

## Slide 44 — `print()` vs `return`

| `print()`                              | `return`                            |
| -------------------------------------- | ----------------------------------- |
| Menampilkan hasil ke layar             | Mengembalikan hasil                 |
| Cocok untuk pesan                      | Cocok untuk perhitungan             |
| Hasil sulit dipakai lagi               | Hasil bisa disimpan                 |
| Tidak selalu cocok untuk program besar | Cocok untuk program yang lebih rapi |

---

## Slide 45 — Latihan: Print atau Return?

Kasus 1:

Function hanya menampilkan pesan “Selamat datang”.

Lebih cocok pakai:

```python
print()
```

Kasus 2:

Function menghitung total harga dan hasilnya mau dipakai untuk menghitung diskon.

Lebih cocok pakai:

```python
return
```

---

## Slide 46 — Function dengan Multiple Parameters dan Return

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total

total_payment = calculate_total(15000, 3)

print("Total bayar:", total_payment)
```

Output:

```python
Total bayar: 45000
```

Function menerima harga dan jumlah barang, lalu mengembalikan total.

---

## Slide 47 — Latihan: Lengkapi Return

Lengkapi kode berikut.

```python
def calculate_area(length, width):
    area = length * width
    ______ area

result = calculate_area(10, 5)

print(result)
```

Jawaban:

```python
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(10, 5)

print(result)
```

Output:

```python
50
```

---

## Slide 48 — Function Bisa Dipakai di Program Lebih Besar

```python
def calculate_total(price, quantity):
    return price * quantity

def apply_discount(total):
    return total * 0.9

total = calculate_total(20000, 3)
final_price = apply_discount(total)

print("Harga akhir:", final_price)
```

Output:

```python
Harga akhir: 54000.0
```

Satu function menghitung total.
Function lain menghitung diskon.

---

# BAGIAN 4

## Modular Design

---

## Slide 49 — Apa Itu Modular Design?

**Modular design** adalah cara membagi program besar menjadi bagian-bagian kecil.

Setiap bagian punya tugas sendiri.

Dalam Python, bagian-bagian kecil ini biasanya dibuat sebagai function.

Sederhananya:

> Program besar dipecah menjadi potongan kecil agar lebih mudah dibuat dan diperbaiki.

---

## Slide 50 — Analogi Modular Design: Restoran

Di restoran, semua pekerjaan tidak dilakukan oleh satu orang.

Ada bagian:

* Kasir
* Koki
* Pelayan
* Petugas kebersihan

Setiap bagian punya tugas.

Program juga bisa begitu.

Setiap function punya tugas masing-masing.

---

## Slide 51 — Program Tanpa Modular Design

```python
name = input("Nama: ")
price = int(input("Harga barang: "))
quantity = int(input("Jumlah barang: "))

total = price * quantity
discount = total * 0.1
final_price = total - discount

print("Halo", name)
print("Total:", total)
print("Diskon:", discount)
print("Harga akhir:", final_price)
```

Kode ini masih bisa berjalan.

Tapi semua proses bercampur di satu tempat.

---

## Slide 52 — Program dengan Modular Design

```python
def get_total(price, quantity):
    return price * quantity

def get_discount(total):
    return total * 0.1

def get_final_price(total, discount):
    return total - discount

price = 20000
quantity = 3

total = get_total(price, quantity)
discount = get_discount(total)
final_price = get_final_price(total, discount)

print("Harga akhir:", final_price)
```

Kode lebih rapi karena setiap function punya tugas.

---

## Slide 53 — Kenapa Modular Design Berguna?

Modular design membantu kita:

* Membaca program lebih mudah
* Mengubah satu bagian tanpa merusak semuanya
* Menggunakan function berulang kali
* Mencari bug lebih cepat
* Membuat proyek lebih besar dengan lebih teratur

---

## Slide 54 — Reusable Code

**Reusable code** adalah kode yang bisa dipakai ulang.

Contoh:

```python
def calculate_total(price, quantity):
    return price * quantity
```

Function ini bisa dipakai untuk:

* Menghitung total belanja makanan
* Menghitung total pembelian alat tulis
* Menghitung total modal usaha
* Menghitung total pembayaran tiket

Sekali dibuat, bisa dipakai berkali-kali.

---

## Slide 55 — Debugging Program Modular

Kalau program modular error, kita bisa cek function satu per satu.

Contoh:

```python
def get_total(price, quantity):
    return price + quantity
```

Kode di atas salah karena total harga seharusnya:

```python
price * quantity
```

Dengan modular design, kita bisa langsung cek function `get_total`.

---

## Slide 56 — Latihan Debugging

Ada bug di function berikut.

```python
def calculate_total(price, quantity):
    return price + quantity

total = calculate_total(10000, 3)
print(total)
```

Output yang benar harusnya:

```python
30000
```

Perbaiki function-nya.

Jawaban:

```python
def calculate_total(price, quantity):
    return price * quantity
```

---

## Slide 57 — Struktur File Sederhana

Untuk proyek yang lebih besar, kita bisa membagi file.

Contoh struktur sederhana:

```python
project/
│
├── main.py
├── calculator.py
└── helper.py
```

`main.py` berisi alur utama program.
`calculator.py` berisi function perhitungan.
`helper.py` berisi function bantuan.

---

## Slide 58 — Contoh Isi `calculator.py`

```python
def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(total, discount_rate):
    return total * discount_rate
```

File ini khusus menyimpan function perhitungan.

---

## Slide 59 — Contoh Isi `main.py`

```python
from calculator import calculate_total, calculate_discount

price = 20000
quantity = 3

total = calculate_total(price, quantity)
discount = calculate_discount(total, 0.1)

print("Total:", total)
print("Diskon:", discount)
```

`main.py` memakai function dari file lain.

---

## Slide 60 — Mini Project Coding: Modular Shopping Calculator

Buat program belanja sederhana dengan function.

Program harus punya:

1. Function menghitung total.
2. Function menghitung diskon.
3. Function menghitung harga akhir.
4. Function menampilkan hasil.

Starter code:

```python
def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(total, discount_rate):
    return total * discount_rate

def calculate_final_price(total, discount):
    return total - discount

price = 25000
quantity = 4
discount_rate = 0.1

total = calculate_total(price, quantity)
discount = calculate_discount(total, discount_rate)
final_price = calculate_final_price(total, discount)

print("Total:", total)
print("Diskon:", discount)
print("Harga akhir:", final_price)
```

---

# BAGIAN 5

## Financial Literacy: Menabung & Bunga Tunggal + Functions

---

## Slide 61 — Masuk ke Financial Literacy

Sekarang kita akan memakai function untuk membuat kalkulator keuangan sederhana.

Topik pertama:

# Menabung dan Bunga Tunggal

Kita akan membuat program yang bisa menghitung pertumbuhan tabungan.

---

## Slide 62 — Apa Itu Menabung?

**Menabung** adalah menyimpan sebagian uang agar bisa digunakan di masa depan.

Contoh tujuan menabung:

* Membeli buku
* Membeli laptop
* Dana darurat
* Modal project
* Biaya kegiatan sekolah

Dengan menabung, kita belajar menunda keinginan untuk mencapai tujuan yang lebih besar.

---

## Slide 63 — Apa Itu Bunga?

**Bunga** adalah tambahan uang yang bisa didapat dari tabungan atau pinjaman.

Dalam materi ini, kita fokus ke tabungan.

Contoh sederhana:

Kamu menabung Rp100.000.
Setelah beberapa waktu, uangmu bertambah menjadi Rp105.000.

Tambahan Rp5.000 itu bisa disebut bunga.

---

## Slide 64 — Apa Itu Bunga Tunggal?

**Bunga tunggal** adalah bunga yang dihitung dari uang awal saja.

Rumus sederhananya:

```python
bunga = uang_awal * bunga_per_tahun * lama_menabung
```

Contoh:

Uang awal: Rp100.000
Bunga per tahun: 5%
Lama menabung: 2 tahun

Bunga:

```python
100000 * 0.05 * 2 = 10000
```

Total akhir:

```python
100000 + 10000 = 110000
```

---

## Slide 65 — Kenapa Cocok Pakai Function?

Menghitung bunga bisa dilakukan berkali-kali dengan angka yang berbeda.

Daripada menulis rumus berulang-ulang, kita buat function.

Input function:

* Uang awal
* Persentase bunga
* Lama menabung

Output function:

* Jumlah bunga
* Total akhir tabungan

---

## Slide 66 — Function Kalkulator Bunga Tunggal

```python
def calculate_simple_interest(principal, rate, years):
    interest = principal * rate * years
    return interest

interest = calculate_simple_interest(100000, 0.05, 2)

print("Bunga:", interest)
```

Output:

```python
Bunga: 10000.0
```

---

## Slide 67 — Function untuk Total Tabungan

```python
def calculate_total_saving(principal, rate, years):
    interest = principal * rate * years
    total = principal + interest
    return total

total = calculate_total_saving(100000, 0.05, 2)

print("Total tabungan:", total)
```

Output:

```python
Total tabungan: 110000.0
```

---

## Slide 68 — Membuat Function Lebih Lengkap

```python
def calculate_saving(principal, rate, years):
    interest = principal * rate * years
    total = principal + interest
    return interest, total

interest, total = calculate_saving(100000, 0.05, 2)

print("Bunga:", interest)
print("Total akhir:", total)
```

Output:

```python
Bunga: 10000.0
Total akhir: 110000.0
```

Function bisa mengembalikan lebih dari satu nilai.

---

## Slide 69 — Cara Membaca Parameter

```python
def calculate_saving(principal, rate, years):
```

Artinya function menerima tiga input:

`principal` = uang awal
`rate` = bunga per tahun
`years` = lama menabung

Kalau kita memanggil:

```python
calculate_saving(100000, 0.05, 2)
```

Artinya:

Uang awal 100.000, bunga 5%, selama 2 tahun.

---

## Slide 70 — Membandingkan Beberapa Skenario

```python
def calculate_total_saving(principal, rate, years):
    interest = principal * rate * years
    total = principal + interest
    return total

scenario_1 = calculate_total_saving(100000, 0.05, 1)
scenario_2 = calculate_total_saving(100000, 0.05, 3)
scenario_3 = calculate_total_saving(100000, 0.05, 5)

print("1 tahun:", scenario_1)
print("3 tahun:", scenario_2)
print("5 tahun:", scenario_3)
```

Output:

```python
1 tahun: 105000.0
3 tahun: 115000.0
5 tahun: 125000.0
```

---

## Slide 71 — Latihan: Lengkapi Function Bunga Tunggal

Lengkapi kode berikut.

```python
def simple_interest(principal, rate, years):
    interest = principal * rate * years
    ______ interest

result = simple_interest(200000, 0.05, 2)
print(result)
```

Jawaban:

```python
def simple_interest(principal, rate, years):
    interest = principal * rate * years
    return interest
```

---

## Slide 72 — Latihan: Tebak Output

```python
def simple_interest(principal, rate, years):
    return principal * rate * years

interest = simple_interest(100000, 0.1, 3)

print(interest)
```

Apa output-nya?

Jawaban:

```python
30000.0
```

Karena:

```python
100000 * 0.1 * 3 = 30000
```

---

# BAGIAN 6

## Financial Literacy: Bunga Majemuk + Loops

---

## Slide 73 — Apa Itu Bunga Majemuk?

**Bunga majemuk** adalah bunga yang ikut bertambah setiap periode.

Sederhananya:

Pada tahun pertama, uang awal mendapat bunga.

Pada tahun kedua, bunga dihitung dari uang awal + bunga tahun pertama.

Jadi uangnya bisa tumbuh lebih cepat dibanding bunga tunggal.

---

## Slide 74 — Analogi Bunga Majemuk

Bayangkan kamu menanam pohon.

Bunga tunggal seperti pohon yang tumbuh dengan tambahan tinggi yang sama setiap tahun.

Bunga majemuk seperti pohon yang makin besar, lalu pertumbuhannya juga makin besar karena batang dan cabangnya bertambah.

Dalam keuangan, uang yang bertambah bisa ikut menghasilkan tambahan lagi.

---

## Slide 75 — Bunga Tunggal vs Bunga Majemuk

Bunga tunggal:

Bunga dihitung dari uang awal saja.

Bunga majemuk:

Bunga dihitung dari total uang yang terus bertambah.

Contoh sederhana:

Uang awal Rp100.000
Bunga 10% per tahun
Durasi 3 tahun

Bunga tunggal:

Tiap tahun tambah Rp10.000.

Bunga majemuk:

Tahun berikutnya bunga dihitung dari total uang yang sudah bertambah.

---

## Slide 76 — Kenapa Pakai Loop?

Untuk bunga majemuk, kita menghitung pertumbuhan uang tahun demi tahun.

Karena prosesnya berulang, kita bisa memakai loop.

Contoh:

Tahun 1: hitung bunga
Tahun 2: hitung bunga lagi
Tahun 3: hitung bunga lagi

Loop membantu program mengulang perhitungan secara otomatis.

---

## Slide 77 — Program Bunga Majemuk dengan Loop

```python
money = 100000
rate = 0.1
years = 3

for year in range(1, years + 1):
    interest = money * rate
    money = money + interest
    print("Tahun", year, ":", money)
```

Output:

```python
Tahun 1 : 110000.0
Tahun 2 : 121000.0
Tahun 3 : 133100.0
```

---

## Slide 78 — Cara Membaca Program

Awalnya:

```python
money = 100000
```

Setiap tahun:

```python
interest = money * rate
money = money + interest
```

Artinya:

Program menghitung bunga berdasarkan uang saat ini, lalu menambahkan bunga ke uang tersebut.

Karena uang bertambah setiap tahun, bunga tahun berikutnya juga ikut berubah.

---

## Slide 79 — Membuat Function Bunga Majemuk

```python
def calculate_compound_interest(principal, rate, years):
    money = principal

    for year in range(1, years + 1):
        interest = money * rate
        money = money + interest

    return money

total = calculate_compound_interest(100000, 0.1, 3)

print("Total akhir:", total)
```

Output:

```python
Total akhir: 133100.0
```

---

## Slide 80 — Menampilkan Tabel Simulasi

```python
def show_compound_table(principal, rate, years):
    money = principal

    print("Tahun | Total Uang")
    print("------------------")

    for year in range(1, years + 1):
        interest = money * rate
        money = money + interest
        print(year, "|", money)

show_compound_table(100000, 0.1, 3)
```

Output:

```python
Tahun | Total Uang
------------------
1 | 110000.0
2 | 121000.0
3 | 133100.0
```

---

## Slide 81 — Membandingkan Bunga Tunggal dan Majemuk

```python
def simple_interest_total(principal, rate, years):
    interest = principal * rate * years
    return principal + interest

def compound_interest_total(principal, rate, years):
    money = principal

    for year in range(1, years + 1):
        money = money + (money * rate)

    return money

simple = simple_interest_total(100000, 0.1, 3)
compound = compound_interest_total(100000, 0.1, 3)

print("Bunga tunggal:", simple)
print("Bunga majemuk:", compound)
```

Output:

```python
Bunga tunggal: 130000.0
Bunga majemuk: 133100.0
```

---

## Slide 82 — Kenapa Hasilnya Berbeda?

Bunga tunggal:

```python
100000 + 10000 + 10000 + 10000 = 130000
```

Bunga majemuk:

Tahun 1:

```python
100000 + 10000 = 110000
```

Tahun 2:

```python
110000 + 11000 = 121000
```

Tahun 3:

```python
121000 + 12100 = 133100
```

Karena bunga majemuk menghitung bunga dari uang yang sudah bertambah.

---

## Slide 83 — Latihan: Tebak Hasil Tahun Pertama

```python
money = 200000
rate = 0.05

interest = money * rate
money = money + interest

print(money)
```

Apa output-nya?

Jawaban:

```python
210000.0
```

Karena 5% dari 200.000 adalah 10.000.

---

## Slide 84 — Latihan: Lengkapi Loop

Lengkapi kode berikut agar simulasi berjalan selama 5 tahun.

```python
money = 100000
rate = 0.1

for year in range(1, _____):
    interest = money * rate
    money = money + interest
    print(year, money)
```

Jawaban:

```python
for year in range(1, 6):
```

Karena `range(1, 6)` menghasilkan angka 1 sampai 5.

---

## Slide 85 — Mini Project Financial Literacy

# Saving Growth Simulator

Buat program Python yang membandingkan bunga tunggal dan bunga majemuk.

Program harus:

1. Meminta input uang awal.
2. Meminta input persentase bunga.
3. Meminta input durasi tahun.
4. Menghitung total dengan bunga tunggal.
5. Menghitung total dengan bunga majemuk.
6. Menampilkan tabel pertumbuhan bunga majemuk tahun per tahun.
7. Menampilkan mana yang hasilnya lebih besar.

---

## Slide 86 — Starter Code Mini Project

```python
def simple_interest_total(principal, rate, years):
    interest = principal * rate * years
    return principal + interest

def compound_interest_total(principal, rate, years):
    money = principal

    for year in range(1, years + 1):
        money = money + (money * rate)

    return money

def show_compound_table(principal, rate, years):
    money = principal

    print("Tahun | Total Uang")
    print("------------------")

    for year in range(1, years + 1):
        money = money + (money * rate)
        print(year, "|", money)

principal = int(input("Uang awal: "))
rate_percent = float(input("Bunga per tahun (%): "))
years = int(input("Durasi tahun: "))

rate = rate_percent / 100

simple_total = simple_interest_total(principal, rate, years)
compound_total = compound_interest_total(principal, rate, years)

print("\n=== SIMULASI BUNGA MAJEMUK ===")
show_compound_table(principal, rate, years)

print("\n=== HASIL AKHIR ===")
print("Bunga tunggal:", simple_total)
print("Bunga majemuk:", compound_total)

if compound_total > simple_total:
    print("Bunga majemuk menghasilkan total lebih besar.")
elif compound_total == simple_total:
    print("Hasilnya sama.")
else:
    print("Bunga tunggal menghasilkan total lebih besar.")
```

---

## Slide 87 — Challenge Tambahan

Kalau sudah selesai, coba upgrade programmu.

Pilih minimal 1 upgrade:

1. Tambahkan target tabungan.
2. Tampilkan apakah target tercapai atau belum.
3. Tambahkan simulasi untuk 2 pilihan bunga berbeda.
4. Buat function khusus untuk format rupiah.
5. Tambahkan rekomendasi: “lanjut menabung”, “target hampir tercapai”, atau “perlu tambah durasi”.

---

## Slide 88 — Kriteria Completion / Kehadiran

Tugas dihitung selesai jika program:

| Kriteria                                       | Wajib |
| ---------------------------------------------- | ----- |
| Menggunakan function dengan beberapa parameter | Ya    |
| Menggunakan `return`                           | Ya    |
| Menggunakan loop untuk bunga majemuk           | Ya    |
| Menghitung bunga tunggal                       | Ya    |
| Menghitung bunga majemuk                       | Ya    |
| Menampilkan tabel pertumbuhan uang             | Ya    |
| Membandingkan hasil bunga tunggal dan majemuk  | Ya    |
| Menampilkan kesimpulan akhir                   | Ya    |

---

## Slide 89 — Rangkuman Coding

Hari ini kita belajar:

* Algoritma adalah langkah-langkah menyelesaikan masalah.
* Optimasi algoritma membuat program lebih efisien.
* Step count membantu membandingkan jumlah langkah.
* Function adalah kumpulan perintah yang diberi nama.
* Parameter adalah data yang masuk ke function.
* `return` mengembalikan hasil agar bisa dipakai lagi.
* Modular design membagi program besar menjadi function kecil.
* Loop membantu proses yang berulang.

---

## Slide 90 — Rangkuman Financial Literacy

Dalam financial literacy, kita belajar:

* Menabung berarti menyimpan uang untuk tujuan masa depan.
* Bunga adalah tambahan dari tabungan.
* Bunga tunggal dihitung dari uang awal saja.
* Bunga majemuk dihitung dari uang yang terus bertambah.
* Function bisa dipakai untuk membuat kalkulator bunga.
* Loop bisa dipakai untuk simulasi pertumbuhan uang tahun demi tahun.
* Program bisa membantu membandingkan beberapa skenario keuangan.

---

## Slide 91 — Exit Ticket

Jawab 5 pertanyaan ini:

1. Apa itu optimasi algoritma?
2. Apa fungsi `return` dalam Python?
3. Apa bedanya `print()` dan `return`?
4. Kenapa program besar sebaiknya dibagi menjadi beberapa function?
5. Apa bedanya bunga tunggal dan bunga majemuk?

Contoh jawaban:

Optimasi algoritma adalah membuat program menyelesaikan tugas dengan langkah yang lebih efisien.
`return` mengembalikan hasil function agar bisa dipakai lagi.
`print()` hanya menampilkan hasil, sedangkan `return` memberikan hasil ke program.
Program besar dibagi menjadi function agar lebih rapi dan mudah diperbaiki.
Bunga tunggal dihitung dari uang awal, sedangkan bunga majemuk dihitung dari uang yang terus bertambah.

---
