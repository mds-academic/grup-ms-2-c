# Deck Python SMA

## Safe Finance Tracker: Input Validation, Error Handling, Debugging, dan Financial Data

---

## Slide 1

**Header:** PYTHON BASICS
**Subheader:** Safe Finance Tracker

# Membuat Program Keuangan yang Lebih Aman

Dalam program Python, kita sering meminta data dari pengguna.

Contoh:

* Nama transaksi
* Jenis transaksi
* Nominal uang
* Kategori pengeluaran
* Jumlah saldo

Tapi input dari pengguna bisa salah.

Hari ini kita akan belajar cara membuat program yang lebih aman, tidak mudah error, dan bisa membantu mencatat data keuangan.

---

## Slide 2

**Header:** PYTHON BASICS
**Subheader:** Learning Goals

# Apa yang Akan Kita Pelajari?

Hari ini kita akan belajar:

1. Mengecek input pengguna agar tidak sembarangan diproses.
2. Membersihkan input dengan sanitasi sederhana.
3. Menangani error dengan `try-except`.
4. Melakukan debugging pada program dengan beberapa function.
5. Mencatat transaksi menggunakan list dan dictionary.
6. Menganalisis data finansial sederhana.

---

# BAGIAN 1

## Input Validation & Data Safety

---

## Slide 3

**Header:** INPUT VALIDATION
**Subheader:** Data dari Pengguna

# Apa Itu Input?

**Input** adalah data yang dimasukkan pengguna ke dalam program.

Contoh:

```python id="qrnw4s"
name = input("Nama transaksi: ")
amount = input("Nominal transaksi: ")
transaction_type = input("Jenis transaksi: ")
```

Input membuat program menjadi interaktif.

Tapi input juga bisa menjadi sumber masalah kalau tidak dicek.

---

## Slide 4

**Header:** INPUT VALIDATION
**Subheader:** Masalah Input

# Input Pengguna Tidak Selalu Benar

Pengguna bisa saja memasukkan data yang salah.

Contoh:

```python id="c3xwdy"
""
```

Input kosong.

```python id="g7mopi"
"abc"
```

Padahal program meminta angka.

```python id="npy02v"
-50000
```

Nominal uang negatif.

```python id="58jylc"
" pengeluaran "
```

Ada spasi berlebih.

```python id="eqi1v2"
"PEMASUKAN"
```

Huruf kapital semua.

Program perlu mengecek dan membersihkan input seperti ini.

---

## Slide 5

**Header:** INPUT VALIDATION
**Subheader:** Konsep Dasar

# Apa Itu Validasi Input?

**Validasi input** adalah proses mengecek apakah input pengguna sudah sesuai aturan.

Sederhananya:

> Program tidak langsung percaya pada input pengguna.

Program perlu mengecek:

* Apakah input kosong?
* Apakah input berupa angka?
* Apakah angka masuk akal?
* Apakah nominal tidak negatif?
* Apakah kategori sesuai pilihan?

---

## Slide 6

**Header:** DATA SAFETY
**Subheader:** Analogi Sederhana

# Validasi Input Seperti Petugas Penjaga

Bayangkan kamu masuk ke wahana permainan.

Petugas akan mengecek:

* Apakah kamu punya tiket?
* Apakah tinggi badanmu cukup?
* Apakah kamu mengikuti aturan keamanan?

Program juga begitu.

Sebelum memproses data, program perlu mengecek apakah data tersebut aman untuk digunakan.

---

## Slide 7

**Header:** INPUT SANITIZATION
**Subheader:** Membersihkan Data

# Apa Itu Sanitasi Input?

**Sanitasi input** adalah proses membersihkan input agar lebih rapi sebelum dipakai.

Contoh masalah:

Pengguna mengetik:

```python id="4z2udl"
"  pemasukan  "
```

Program bisa membersihkan spasi di depan dan belakang.

```python id="zy6e4l"
transaction_type = transaction_type.strip()
```

Hasilnya menjadi:

```python id="4tsang"
"pemasukan"
```

---

## Slide 8

**Header:** INPUT SANITIZATION
**Subheader:** `.strip()`

# Membersihkan Spasi dengan `.strip()`

```python id="2d22hn"
name = input("Nama transaksi: ")
name = name.strip()

print(name)
```

Kalau pengguna mengetik:

```python id="uw64zq"
"   Beli Buku   "
```

Maka hasilnya menjadi:

```python id="sh1ycx"
"Beli Buku"
```

`.strip()` membantu menghapus spasi yang tidak diperlukan.

---

## Slide 9

**Header:** INPUT SANITIZATION
**Subheader:** `.lower()`

# Menyamakan Huruf dengan `.lower()`

Kadang pengguna mengetik:

```python id="w6akqh"
"PEMASUKAN"
```

atau:

```python id="17fqa9"
"Pemasukan"
```

Agar lebih mudah dicek, kita bisa ubah menjadi huruf kecil semua.

```python id="hh0boh"
transaction_type = input("Jenis transaksi: ")
transaction_type = transaction_type.strip().lower()

print(transaction_type)
```

Output:

```python id="0l00un"
pemasukan
```

---

## Slide 10

**Header:** INPUT VALIDATION
**Subheader:** Sanitasi vs Validasi

# Sanitasi dan Validasi Itu Berbeda

| Konsep   | Fungsi                                  | Contoh                                   |
| -------- | --------------------------------------- | ---------------------------------------- |
| Sanitasi | Membersihkan input                      | `.strip()`, `.lower()`                   |
| Validasi | Mengecek input boleh dipakai atau tidak | tidak kosong, harus angka, tidak negatif |

Contoh sanitasi:

```python id="3dlpre"
category = category.strip().lower()
```

Contoh validasi:

```python id="s1t8rg"
if category == "pemasukan":
    print("Valid")
```

Biasanya, input dibersihkan dulu, baru divalidasi.

---

## Slide 11

**Header:** INPUT VALIDATION
**Subheader:** Input Kosong

# Validasi Input Kosong

```python id="mjmcm6"
name = input("Nama transaksi: ")
name = name.strip()

if name == "":
    print("Nama transaksi tidak boleh kosong.")
else:
    print("Nama transaksi:", name)
```

Kalau pengguna langsung menekan Enter, program akan menampilkan:

```python id="17mkva"
Nama transaksi tidak boleh kosong.
```

---

## Slide 12

**Header:** INPUT VALIDATION
**Subheader:** Kategori Transaksi

# Validasi Jenis Transaksi

Dalam program keuangan, jenis transaksi biasanya hanya:

* `pemasukan`
* `pengeluaran`

Contoh validasi:

```python id="6bfkbr"
transaction_type = input("Jenis transaksi: ")
transaction_type = transaction_type.strip().lower()

if transaction_type == "pemasukan" or transaction_type == "pengeluaran":
    print("Jenis transaksi valid")
else:
    print("Jenis transaksi harus pemasukan atau pengeluaran")
```

---

## Slide 13

**Header:** DATA SAFETY
**Subheader:** Keamanan Dana

# Kenapa Validasi Penting di Program Keuangan?

Program keuangan berhubungan dengan data uang.

Kalau input salah, hasil program bisa ikut salah.

Contoh:

```python id="0aeb46"
amount = -50000
```

Kalau program menerima angka negatif sebagai pengeluaran, saldo bisa jadi salah.

Karena itu, nominal transaksi harus dicek.

---

## Slide 14

**Header:** INPUT VALIDATION
**Subheader:** Nominal Transaksi

# Validasi Nominal Tidak Boleh Negatif

```python id="w1onfq"
amount = int(input("Nominal transaksi: "))

if amount <= 0:
    print("Nominal harus lebih dari 0.")
else:
    print("Nominal valid:", amount)
```

Nominal transaksi sebaiknya lebih dari 0.

Karena transaksi Rp0 atau negatif biasanya tidak masuk akal dalam pencatatan sederhana.

---

## Slide 15

**Header:** INPUT VALIDATION
**Subheader:** Pesan Error

# Pesan Error Harus Jelas

Pesan error yang kurang membantu:

```python id="6fpqu0"
Error!
```

Pesan error yang lebih baik:

```python id="08s6vm"
Nominal harus lebih dari 0. Masukkan angka positif.
```

Pesan yang baik menjelaskan:

1. Apa yang salah.
2. Apa yang harus diperbaiki.

---

## Slide 16

**Header:** INPUT VALIDATION
**Subheader:** Function Validasi

# Membuat Function `clean_text()`

Agar sanitasi bisa dipakai berulang kali, kita bisa membuat function.

```python id="cp276i"
def clean_text(text):
    return text.strip().lower()
```

Contoh penggunaan:

```python id="7pxtw8"
category = clean_text("  PEMASUKAN  ")

print(category)
```

Output:

```python id="t81x70"
pemasukan
```

---

## Slide 17

**Header:** INPUT VALIDATION
**Subheader:** Function Validasi

# Membuat Function `validate_type()`

```python id="k02d49"
def validate_type(transaction_type):
    transaction_type = clean_text(transaction_type)

    if transaction_type == "pemasukan" or transaction_type == "pengeluaran":
        return True
    else:
        return False
```

Function ini mengecek apakah jenis transaksi valid.

Hasilnya berupa:

```python id="g66jzj"
True
```

atau:

```python id="pfh8hn"
False
```

---

## Slide 18

**Header:** INPUT VALIDATION
**Subheader:** Function Validasi

# Membuat Function `validate_amount()`

```python id="v8gn7l"
def validate_amount(amount):
    if amount > 0:
        return True
    else:
        return False
```

Contoh:

```python id="szci2e"
print(validate_amount(50000))
print(validate_amount(-10000))
```

Output:

```python id="z3upj6"
True
False
```

---

## Slide 19

**Header:** INPUT VALIDATION
**Subheader:** Latihan

# Latihan: Tebak Output

```python id="b6tbt5"
def clean_text(text):
    return text.strip().lower()

category = clean_text("  PENGELUARAN  ")

print(category)
```

Apa output-nya?

Jawaban:

```python id="if1zyv"
pengeluaran
```

Karena `.strip()` menghapus spasi dan `.lower()` mengubah huruf menjadi kecil.

---

## Slide 20

**Header:** INPUT VALIDATION
**Subheader:** Latihan

# Latihan: Lengkapi Validasi

Lengkapi kode berikut agar input kosong ditolak.

```python id="yx5jem"
name = input("Nama transaksi: ")
name = name.strip()

if ______:
    print("Nama tidak boleh kosong")
else:
    print("Nama:", name)
```

Jawaban:

```python id="dk1bo2"
if name == "":
```

---

## Slide 21

**Header:** INPUT VALIDATION
**Subheader:** Latihan

# Latihan: Lengkapi Function

Lengkapi function berikut.

```python id="n9zcvf"
def validate_amount(amount):
    if amount ______ 0:
        return False
    else:
        return True
```

Jawaban:

```python id="568b8q"
<=
```

Karena nominal harus lebih dari 0.

---

## Slide 22

**Header:** INPUT VALIDATION
**Subheader:** Mini Project

# Mini Project: Safe Transaction Input

Buat program input transaksi yang aman.

Program harus:

1. Meminta nama transaksi.
2. Menolak nama kosong.
3. Meminta jenis transaksi.
4. Menolak jenis transaksi selain `pemasukan` atau `pengeluaran`.
5. Meminta nominal transaksi.
6. Menolak nominal 0 atau negatif.
7. Menampilkan data transaksi jika semua valid.

---

## Slide 23

**Header:** INPUT VALIDATION
**Subheader:** Starter Code

# Starter Code: Safe Transaction Input

```python id="6rgprf"
def clean_text(text):
    return text.strip().lower()

def validate_type(transaction_type):
    transaction_type = clean_text(transaction_type)
    return transaction_type == "pemasukan" or transaction_type == "pengeluaran"

def validate_amount(amount):
    return amount > 0

name = input("Nama transaksi: ").strip()
transaction_type = clean_text(input("Jenis transaksi: "))
amount = int(input("Nominal transaksi: "))

if name == "":
    print("Nama transaksi tidak boleh kosong.")
elif not validate_type(transaction_type):
    print("Jenis transaksi tidak valid.")
elif not validate_amount(amount):
    print("Nominal harus lebih dari 0.")
else:
    transaction = {
        "name": name,
        "type": transaction_type,
        "amount": amount
    }

    print("Transaksi valid:")
    print(transaction)
```

Catatan:

Program ini sudah melakukan validasi, tapi masih bisa error kalau nominal diisi huruf.

Masalah itu akan kita selesaikan dengan `try-except`.

---

# BAGIAN 2

## Error Handling dengan `try-except`

---

## Slide 24

**Header:** ERROR HANDLING
**Subheader:** Program Tidak Berhenti Saat Error

# Apa Itu Error?

**Error** adalah kondisi ketika program tidak bisa menjalankan perintah dengan benar.

Contoh:

* Input huruf saat program meminta angka
* Membagi angka dengan nol
* Menggabungkan angka dan teks dengan cara yang salah

Kalau tidak ditangani, program bisa berhenti tiba-tiba.

---

## Slide 25

**Header:** ERROR HANDLING
**Subheader:** Jenis Error

# Error yang Sering Muncul

| Error               | Penyebab                                          |
| ------------------- | ------------------------------------------------- |
| `ValueError`        | Data tidak bisa diubah ke tipe yang diminta       |
| `TypeError`         | Operasi dilakukan pada tipe data yang tidak cocok |
| `ZeroDivisionError` | Program membagi angka dengan nol                  |

Kita perlu mengenali jenis error agar bisa menanganinya dengan tepat.

---

## Slide 26

**Header:** ERROR HANDLING
**Subheader:** ValueError

# Contoh `ValueError`

```python id="p2qch1"
amount = int(input("Nominal transaksi: "))
print(amount)
```

Kalau pengguna mengetik:

```python id="c552db"
lima ribu
```

Program akan terkena `ValueError`.

Karena teks `"lima ribu"` tidak bisa diubah menjadi angka.

---

## Slide 27

**Header:** ERROR HANDLING
**Subheader:** TypeError

# Contoh `TypeError`

```python id="5dlm0z"
amount = 50000
message = "Nominal transaksi: " + amount

print(message)
```

Kode ini error karena Python tidak bisa langsung menggabungkan teks dan angka.

Solusinya:

```python id="fpyknx"
amount = 50000
message = "Nominal transaksi: " + str(amount)

print(message)
```

---

## Slide 28

**Header:** ERROR HANDLING
**Subheader:** ZeroDivisionError

# Contoh `ZeroDivisionError`

```python id="sj3nx9"
total_money = 100000
people = 0

result = total_money / people

print(result)
```

Kode ini error karena angka tidak bisa dibagi dengan nol.

---

## Slide 29

**Header:** ERROR HANDLING
**Subheader:** try-except

# Apa Itu `try-except`?

`try-except` digunakan untuk menangani error.

Sederhananya:

> Coba jalankan kode ini. Kalau error, jangan berhenti. Jalankan pesan cadangan.

Bentuk dasarnya:

```python id="mvwmxb"
try:
    # kode yang mungkin error
except:
    # kode saat error terjadi
```

---

## Slide 30

**Header:** ERROR HANDLING
**Subheader:** Analogi

# `try-except` Seperti Rencana Cadangan

Bayangkan kamu mencoba membuka pintu.

Kalau pintu terbuka, kamu masuk.

Kalau pintu terkunci, kamu tidak menabrak pintu.

Kamu mencari pintu lain atau meminta bantuan.

`try-except` membuat program punya rencana cadangan saat terjadi error.

---

## Slide 31

**Header:** ERROR HANDLING
**Subheader:** ValueError Handling

# Menangani Input Huruf Saat Diminta Angka

```python id="osbk8k"
try:
    amount = int(input("Nominal transaksi: "))
    print("Nominal:", amount)

except ValueError:
    print("Nominal harus berupa angka.")
```

Kalau pengguna mengetik huruf, program tidak berhenti.

Program akan menampilkan pesan yang lebih jelas.

---

## Slide 32

**Header:** ERROR HANDLING
**Subheader:** Multiple Except

# Menangani Beberapa Error

```python id="6rmqsq"
try:
    total = 100000
    people = int(input("Jumlah orang: "))

    result = total / people
    print("Masing-masing mendapat:", result)

except ValueError:
    print("Jumlah orang harus berupa angka.")

except ZeroDivisionError:
    print("Jumlah orang tidak boleh 0.")
```

Program bisa menangani dua masalah:

1. Input bukan angka.
2. Input angka 0.

---

## Slide 33

**Header:** ERROR HANDLING
**Subheader:** Latihan

# Latihan: Tebak Error

```python id="qzt6wz"
number = int("abc")
```

Error apa yang terjadi?

Jawaban:

```python id="6qni6m"
ValueError
```

Karena teks `"abc"` tidak bisa diubah menjadi angka.

---

## Slide 34

**Header:** ERROR HANDLING
**Subheader:** Latihan

# Latihan: Lengkapi `try-except`

```python id="57uxk2"
try:
    amount = int(input("Nominal: "))
    print(amount)
except ______:
    print("Nominal harus berupa angka.")
```

Jawaban:

```python id="5zvtif"
except ValueError:
```

---

## Slide 35

**Header:** ERROR HANDLING
**Subheader:** Mini Project

# Mini Project: Safe Input with Error Handling

Sekarang kita upgrade program transaksi tadi.

Program harus bisa:

1. Membersihkan input teks.
2. Memvalidasi nama transaksi.
3. Memvalidasi jenis transaksi.
4. Memvalidasi nominal.
5. Menangani error jika nominal diisi huruf.

---

## Slide 36

**Header:** ERROR HANDLING
**Subheader:** Starter Code

# Starter Code: Safe Input with `try-except`

```python id="8jciru"
def clean_text(text):
    return text.strip().lower()

def validate_type(transaction_type):
    transaction_type = clean_text(transaction_type)
    return transaction_type == "pemasukan" or transaction_type == "pengeluaran"

def validate_amount(amount):
    return amount > 0

name = input("Nama transaksi: ").strip()
transaction_type = clean_text(input("Jenis transaksi: "))

try:
    amount = int(input("Nominal transaksi: "))

    if name == "":
        print("Nama transaksi tidak boleh kosong.")
    elif not validate_type(transaction_type):
        print("Jenis transaksi tidak valid.")
    elif not validate_amount(amount):
        print("Nominal harus lebih dari 0.")
    else:
        transaction = {
            "name": name,
            "type": transaction_type,
            "amount": amount
        }

        print("Transaksi berhasil disimpan:")
        print(transaction)

except ValueError:
    print("Nominal harus berupa angka.")
```

---

# BAGIAN 3

## Analisis Kode Kompleks & Debugging

---

## Slide 37

**Header:** DEBUGGING
**Subheader:** Mencari dan Memperbaiki Bug

# Apa Itu Debugging?

**Debugging** adalah proses mencari dan memperbaiki bug dalam program.

Bug adalah kesalahan yang membuat program:

* Error
* Menghasilkan output salah
* Berjalan tidak sesuai harapan
* Berhenti tiba-tiba

Debugging dilakukan langkah demi langkah, bukan hanya menebak.

---

## Slide 38

**Header:** DEBUGGING
**Subheader:** Analogi

# Debugging Seperti Mengecek Lampu Mati

Bayangkan lampu kamar tidak menyala.

Kita cek satu per satu:

1. Apakah saklar sudah dinyalakan?
2. Apakah lampunya rusak?
3. Apakah listriknya menyala?
4. Apakah kabelnya bermasalah?

Debugging juga begitu.

Kita menelusuri sumber masalah satu per satu.

---

## Slide 39

**Header:** DEBUGGING
**Subheader:** Banyak Function

# Debugging Program dengan Banyak Function

Program besar biasanya punya banyak function.

Contoh:

```python id="7lptwf"
def get_total(price, quantity):
    return price * quantity

def get_discount(total):
    return total * 0.1

def get_final_price(total, discount):
    return total - discount
```

Kalau hasil akhir salah, kita perlu mencari function mana yang bermasalah.

---

## Slide 40

**Header:** DEBUGGING
**Subheader:** Dependency

# Apa Itu Dependency Antar Function?

**Dependency** artinya satu bagian program bergantung pada bagian lain.

Contoh:

```python id="usqdra"
total = get_total(price, quantity)
discount = get_discount(total)
final_price = get_final_price(total, discount)
```

`get_discount()` membutuhkan hasil dari `get_total()`.

`get_final_price()` membutuhkan hasil dari `get_discount()`.

Kalau `get_total()` salah, hasil berikutnya bisa ikut salah.

---

## Slide 41

**Header:** DEBUGGING
**Subheader:** Debug Step-by-Step

# Cara Debugging Step-by-Step

Saat program salah, lakukan langkah ini:

1. Baca pesan error.
2. Cari baris yang disebut error.
3. Cek input dan tipe data.
4. Tambahkan `print()` sementara.
5. Cek function satu per satu.
6. Perbaiki bagian yang salah.
7. Jalankan ulang program.

---

## Slide 42

**Header:** DEBUGGING
**Subheader:** Print Debugging

# Debugging dengan `print()`

Kita bisa menambahkan `print()` untuk melihat isi variable.

```python id="234v1g"
def get_total(price, quantity):
    print("DEBUG price:", price)
    print("DEBUG quantity:", quantity)
    return price * quantity
```

`print()` ini membantu kita melihat apakah data yang masuk sudah benar.

---

## Slide 43

**Header:** DEBUGGING
**Subheader:** Bug Example

# Contoh Bug pada Function

```python id="e08dye"
def get_total(price, quantity):
    return price + quantity

total = get_total(10000, 3)

print(total)
```

Output:

```python id="me8o7h"
10003
```

Padahal seharusnya:

```python id="qz8g9d"
30000
```

Bug-nya ada pada operator `+`.

Seharusnya memakai `*`.

---

## Slide 44

**Header:** DEBUGGING
**Subheader:** Latihan

# Latihan: Temukan Bug

```python id="l4j9ke"
def get_total(price, quantity):
    return price + quantity

def get_discount(total):
    return total * 0.1

def get_final_price(total, discount):
    return total - discount

total = get_total(20000, 3)
discount = get_discount(total)
final_price = get_final_price(total, discount)

print(final_price)
```

Pertanyaan:

Bug ada di function mana?

Jawaban:

Bug ada di `get_total()`.

Seharusnya:

```python id="vkco5c"
return price * quantity
```

---

## Slide 45

**Header:** DEBUGGING
**Subheader:** Latihan

# Latihan: Perbaiki Dependency

Kode awal:

```python id="f6cgy8"
def get_total(price, quantity):
    return price * quantity

def get_discount(total):
    return total * 10

def get_final_price(total, discount):
    return total - discount
```

Masalah:

Diskon terlalu besar.

Perbaikan:

```python id="gme3fp"
def get_discount(total):
    return total * 0.1
```

Karena 10% ditulis sebagai `0.1`, bukan `10`.

---

## Slide 46

**Header:** DEBUGGING
**Subheader:** Mini Project

# Mini Project: Debugging Program Belanja

Perbaiki program berikut.

```python id="rtumog"
def get_total(price, quantity):
    return price + quantity

def get_discount(total, member):
    if member:
        return total * 10
    else:
        return 0

def get_final_price(total, discount):
    return discount - total

price = 25000
quantity = 2
member = True

total = get_total(price, quantity)
discount = get_discount(total, member)
final_price = get_final_price(total, discount)

print("Total:", total)
print("Diskon:", discount)
print("Harga akhir:", final_price)
```

Bug yang harus ditemukan:

1. Total harus `price * quantity`.
2. Diskon 10% harus `total * 0.1`.
3. Harga akhir harus `total - discount`.

---

## Slide 47

**Header:** DEBUGGING
**Subheader:** Jawaban Mini Project

# Jawaban Debugging

```python id="7iwqff"
def get_total(price, quantity):
    return price * quantity

def get_discount(total, member):
    if member:
        return total * 0.1
    else:
        return 0

def get_final_price(total, discount):
    return total - discount

price = 25000
quantity = 2
member = True

total = get_total(price, quantity)
discount = get_discount(total, member)
final_price = get_final_price(total, discount)

print("Total:", total)
print("Diskon:", discount)
print("Harga akhir:", final_price)
```

Output:

```python id="z3q33k"
Total: 50000
Diskon: 5000.0
Harga akhir: 45000.0
```

---

# BAGIAN 4

## Transaksi & Pencatatan Keuangan + Data Structures

---

## Slide 48

**Header:** FINANCIAL LITERACY
**Subheader:** Transaction Recorder

# Apa Itu Transaksi?

**Transaksi** adalah aktivitas keluar atau masuknya uang.

Contoh transaksi:

* Dapat uang saku
* Membeli makanan
* Membayar transportasi
* Menabung
* Membeli alat tulis

Dalam program, transaksi bisa dicatat sebagai data.

---

## Slide 49

**Header:** DATA STRUCTURES
**Subheader:** Dictionary

# Apa Itu Dictionary?

**Dictionary** adalah struktur data untuk menyimpan pasangan `key` dan `value`.

Sederhananya:

> Dictionary seperti kartu data yang punya label dan isi.

Contoh:

```python id="zp6ddr"
transaction = {
    "name": "Beli buku",
    "type": "pengeluaran",
    "amount": 25000
}
```

---

## Slide 50

**Header:** DATA STRUCTURES
**Subheader:** Key dan Value

# Membaca Dictionary

```python id="vdoj79"
transaction = {
    "name": "Beli buku",
    "type": "pengeluaran",
    "amount": 25000
}

print(transaction["name"])
print(transaction["type"])
print(transaction["amount"])
```

Output:

```python id="xfhqgy"
Beli buku
pengeluaran
25000
```

---

## Slide 51

**Header:** DATA STRUCTURES
**Subheader:** List of Dictionary

# Menyimpan Banyak Transaksi

Kalau ada banyak transaksi, kita bisa menyimpannya dalam list.

```python id="gg4r9e"
transactions = [
    {"name": "Uang saku", "type": "pemasukan", "amount": 50000},
    {"name": "Beli makan", "type": "pengeluaran", "amount": 20000},
    {"name": "Beli buku", "type": "pengeluaran", "amount": 15000}
]
```

List menyimpan banyak transaksi.

Setiap transaksi disimpan sebagai dictionary.

---

## Slide 52

**Header:** FINANCIAL LITERACY
**Subheader:** Ringkasan Transaksi

# Menghitung Total Pemasukan dan Pengeluaran

```python id="uddb5k"
income = 0
expense = 0

for transaction in transactions:
    if transaction["type"] == "pemasukan":
        income += transaction["amount"]
    elif transaction["type"] == "pengeluaran":
        expense += transaction["amount"]

print("Total pemasukan:", income)
print("Total pengeluaran:", expense)
print("Saldo:", income - expense)
```

Program menghitung:

* Total pemasukan
* Total pengeluaran
* Saldo akhir

---

## Slide 53

**Header:** FINANCIAL LITERACY
**Subheader:** Output

# Output Ringkasan Transaksi

Jika datanya:

```python id="mmibsm"
transactions = [
    {"name": "Uang saku", "type": "pemasukan", "amount": 50000},
    {"name": "Beli makan", "type": "pengeluaran", "amount": 20000},
    {"name": "Beli buku", "type": "pengeluaran", "amount": 15000}
]
```

Output-nya:

```python id="3z9fyo"
Total pemasukan: 50000
Total pengeluaran: 35000
Saldo: 15000
```

---

## Slide 54

**Header:** DATA STRUCTURES
**Subheader:** Update Data

# Menambahkan Transaksi Baru

```python id="hlc7ez"
transactions = []

new_transaction = {
    "name": "Uang saku",
    "type": "pemasukan",
    "amount": 50000
}

transactions.append(new_transaction)

print(transactions)
```

`append()` digunakan untuk menambahkan data baru ke dalam list.

---

## Slide 55

**Header:** FUNCTIONS
**Subheader:** Reusable Code

# Function untuk Menambah Transaksi

```python id="o85opt"
transactions = []

def add_transaction(name, transaction_type, amount):
    transaction = {
        "name": name,
        "type": transaction_type,
        "amount": amount
    }

    transactions.append(transaction)

add_transaction("Uang saku", "pemasukan", 50000)
add_transaction("Beli makan", "pengeluaran", 20000)

print(transactions)
```

Function membuat kode lebih rapi dan bisa dipakai ulang.

---

## Slide 56

**Header:** FUNCTIONS
**Subheader:** Summary Function

# Function Ringkasan Transaksi

```python id="y1qk7g"
def summarize_transactions(transactions):
    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "pemasukan":
            income += transaction["amount"]
        elif transaction["type"] == "pengeluaran":
            expense += transaction["amount"]

    balance = income - expense

    print("Pemasukan:", income)
    print("Pengeluaran:", expense)
    print("Saldo:", balance)
```

Function ini menghitung ringkasan dari data transaksi.

---

## Slide 57

**Header:** DATA STRUCTURES
**Subheader:** Latihan

# Latihan: Tebak Output

```python id="n2n8sa"
transaction = {
    "name": "Beli snack",
    "type": "pengeluaran",
    "amount": 10000
}

print(transaction["amount"])
```

Apa output-nya?

Jawaban:

```python id="4ec9vf"
10000
```

---

## Slide 58

**Header:** DATA STRUCTURES
**Subheader:** Mini Project

# Mini Project: Transaction Recorder

Buat program pencatat transaksi sederhana.

Program harus:

1. Menyimpan transaksi dalam list.
2. Setiap transaksi berbentuk dictionary.
3. Memiliki function `add_transaction`.
4. Memiliki function `summarize_transactions`.
5. Menampilkan total pemasukan, pengeluaran, dan saldo.

---

## Slide 59

**Header:** DATA STRUCTURES
**Subheader:** Starter Code

# Starter Code: Transaction Recorder

```python id="us42d7"
transactions = []

def add_transaction(name, transaction_type, amount):
    transaction = {
        "name": name,
        "type": transaction_type,
        "amount": amount
    }
    transactions.append(transaction)

def summarize_transactions(transactions):
    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "pemasukan":
            income += transaction["amount"]
        elif transaction["type"] == "pengeluaran":
            expense += transaction["amount"]

    balance = income - expense

    print("Total pemasukan:", income)
    print("Total pengeluaran:", expense)
    print("Saldo:", balance)

add_transaction("Uang saku", "pemasukan", 50000)
add_transaction("Beli makan", "pengeluaran", 20000)
add_transaction("Beli buku", "pengeluaran", 15000)

summarize_transactions(transactions)
```

---

# BAGIAN 5

## Analisis Data Finansial

---

## Slide 60

**Header:** FINANCIAL DATA
**Subheader:** Data Analysis

# Apa Itu Analisis Data Finansial?

**Analisis data finansial** adalah membaca data keuangan untuk memahami pola penggunaan uang.

Contoh pertanyaan:

* Total pengeluaran berapa?
* Pengeluaran terbesar apa?
* Pengeluaran terkecil berapa?
* Rata-rata pengeluaran berapa?
* Kategori apa yang paling banyak menghabiskan uang?

---

## Slide 61

**Header:** FINANCIAL DATA
**Subheader:** Dataset Kecil

# Contoh Dataset Pengeluaran

```python id="kc7i1q"
expenses = [20000, 15000, 10000, 30000, 5000]
```

Setiap angka mewakili satu transaksi pengeluaran.

Dengan data ini, kita bisa menghitung:

* Total
* Nilai terbesar
* Nilai terkecil
* Rata-rata

---

## Slide 62

**Header:** FINANCIAL DATA
**Subheader:** Total

# Menghitung Total Pengeluaran

```python id="2wrhbg"
expenses = [20000, 15000, 10000, 30000, 5000]

total = sum(expenses)

print("Total pengeluaran:", total)
```

Output:

```python id="l40g3a"
Total pengeluaran: 80000
```

---

## Slide 63

**Header:** FINANCIAL DATA
**Subheader:** Min dan Max

# Mencari Pengeluaran Terbesar dan Terkecil

```python id="xtrypt"
expenses = [20000, 15000, 10000, 30000, 5000]

highest = max(expenses)
lowest = min(expenses)

print("Pengeluaran terbesar:", highest)
print("Pengeluaran terkecil:", lowest)
```

Output:

```python id="l5jv7n"
Pengeluaran terbesar: 30000
Pengeluaran terkecil: 5000
```

---

## Slide 64

**Header:** FINANCIAL DATA
**Subheader:** Average

# Menghitung Rata-Rata Pengeluaran

```python id="8n2gf9"
expenses = [20000, 15000, 10000, 30000, 5000]

average = sum(expenses) / len(expenses)

print("Rata-rata pengeluaran:", average)
```

Output:

```python id="xg0khf"
Rata-rata pengeluaran: 16000.0
```

---

## Slide 65

**Header:** FINANCIAL DATA
**Subheader:** Membaca Pola

# Data Membantu Kita Melihat Pola

Dari data:

```python id="9ifshq"
expenses = [20000, 15000, 10000, 30000, 5000]
```

Kita tahu:

* Total pengeluaran: 80.000
* Pengeluaran terbesar: 30.000
* Pengeluaran terkecil: 5.000
* Rata-rata pengeluaran: 16.000

Data membantu kita melihat kebiasaan belanja dengan lebih jelas.

---

## Slide 66

**Header:** FINANCIAL DATA
**Subheader:** Dataset Berkategori

# Dataset dengan Kategori

```python id="m07329"
transactions = [
    {"name": "Makan", "category": "makanan", "amount": 20000},
    {"name": "Buku", "category": "sekolah", "amount": 30000},
    {"name": "Snack", "category": "makanan", "amount": 10000},
    {"name": "Transport", "category": "transportasi", "amount": 15000}
]
```

Dengan kategori, kita bisa tahu uang paling banyak digunakan untuk apa.

---

## Slide 67

**Header:** FINANCIAL DATA
**Subheader:** Category Summary

# Menghitung Pengeluaran per Kategori

```python id="vaob9k"
category_total = {}

for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]

    if category not in category_total:
        category_total[category] = 0

    category_total[category] += amount

print(category_total)
```

Output:

```python id="swwb8u"
{'makanan': 30000, 'sekolah': 30000, 'transportasi': 15000}
```

---

## Slide 68

**Header:** FINANCIAL DATA
**Subheader:** Decision Making

# Menghubungkan Data dengan Keputusan

Kalau data menunjukkan pengeluaran makanan terlalu besar, kita bisa membuat keputusan:

* Mengurangi snack
* Membawa bekal
* Membuat budget makanan
* Mencatat pengeluaran harian

Analisis data membantu kita tidak hanya menebak.

Kita mengambil keputusan berdasarkan data.

---

## Slide 69

**Header:** FINANCIAL DATA
**Subheader:** Latihan

# Latihan: Hitung Statistik

Diberikan data:

```python id="qggfiq"
expenses = [12000, 18000, 25000, 10000, 15000]
```

Tentukan:

1. Total pengeluaran
2. Pengeluaran terbesar
3. Pengeluaran terkecil

Jawaban:

```python id="2l4o5u"
total = 80000
max = 25000
min = 10000
```

---

## Slide 70

**Header:** FINANCIAL DATA
**Subheader:** Mini Project

# Mini Project: Financial Data Analyzer

Buat program yang membaca data pengeluaran sederhana.

Program harus:

1. Menyimpan list pengeluaran.
2. Menghitung total pengeluaran.
3. Menghitung pengeluaran terbesar.
4. Menghitung pengeluaran terkecil.
5. Menghitung rata-rata pengeluaran.
6. Memberikan kesimpulan sederhana.

---

## Slide 71

**Header:** FINANCIAL DATA
**Subheader:** Starter Code

# Starter Code: Financial Data Analyzer

```python id="77vecq"
expenses = [20000, 15000, 10000, 30000, 5000]

total = sum(expenses)
highest = max(expenses)
lowest = min(expenses)
average = total / len(expenses)

print("Total:", total)
print("Terbesar:", highest)
print("Terkecil:", lowest)
print("Rata-rata:", average)

if average > 20000:
    print("Kesimpulan: Pengeluaran rata-rata cukup tinggi.")
else:
    print("Kesimpulan: Pengeluaran rata-rata masih cukup aman.")
```

---

# BAGIAN 6

## Tugas Besar Kehadiran

---

## Slide 72

**Header:** FINAL PROJECT
**Subheader:** Safe Finance Tracker

# Tugas Besar: Safe Finance Tracker

Buat program Python yang membantu pengguna:

* Mencatat transaksi
* Memvalidasi input
* Menangani error
* Menghitung ringkasan keuangan
* Menganalisis data pengeluaran sederhana

Program ini akan dihitung sebagai completion / kehadiran.

---

## Slide 73

**Header:** FINAL PROJECT
**Subheader:** Fitur Wajib

# Fitur Wajib Program

Program harus memiliki fitur:

1. Menambah transaksi.
2. Menyimpan transaksi dalam list of dictionary.
3. Memvalidasi input kosong.
4. Memvalidasi nominal agar angka dan lebih dari 0.
5. Memvalidasi jenis transaksi.
6. Menggunakan `try-except`.
7. Menghitung total pemasukan.
8. Menghitung total pengeluaran.
9. Menghitung saldo.
10. Menampilkan statistik pengeluaran sederhana.

---

## Slide 74

**Header:** FINAL PROJECT
**Subheader:** Struktur Function

# Function yang Disarankan

Program minimal memiliki function:

```python id="mqj16j"
clean_text()
validate_type()
validate_amount()
add_transaction()
summarize_transactions()
analyze_expenses()
```

Setiap function punya tugas sendiri.

Ini membuat program lebih rapi, aman, dan mudah di-debug.

---

## Slide 75

**Header:** FINAL PROJECT
**Subheader:** Starter Code

# Starter Code Tugas Besar

```python id="pe71od"
transactions = []

def clean_text(text):
    return text.strip().lower()

def validate_type(transaction_type):
    transaction_type = clean_text(transaction_type)
    return transaction_type == "pemasukan" or transaction_type == "pengeluaran"

def validate_amount(amount):
    return amount > 0

def add_transaction(name, transaction_type, amount):
    transaction = {
        "name": name,
        "type": transaction_type,
        "amount": amount
    }
    transactions.append(transaction)

def summarize_transactions():
    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "pemasukan":
            income += transaction["amount"]
        elif transaction["type"] == "pengeluaran":
            expense += transaction["amount"]

    balance = income - expense

    print("Total pemasukan:", income)
    print("Total pengeluaran:", expense)
    print("Saldo:", balance)

def analyze_expenses():
    expenses = []

    for transaction in transactions:
        if transaction["type"] == "pengeluaran":
            expenses.append(transaction["amount"])

    if len(expenses) == 0:
        print("Belum ada data pengeluaran.")
    else:
        print("Pengeluaran terbesar:", max(expenses))
        print("Pengeluaran terkecil:", min(expenses))
        print("Total pengeluaran:", sum(expenses))
        print("Rata-rata pengeluaran:", sum(expenses) / len(expenses))

try:
    name = input("Nama transaksi: ").strip()
    transaction_type = clean_text(input("Jenis transaksi (pemasukan/pengeluaran): "))
    amount = int(input("Nominal: "))

    if name == "":
        print("Nama transaksi tidak boleh kosong.")
    elif not validate_type(transaction_type):
        print("Jenis transaksi tidak valid.")
    elif not validate_amount(amount):
        print("Nominal harus lebih dari 0.")
    else:
        add_transaction(name, transaction_type, amount)
        print("Transaksi berhasil ditambahkan.")

except ValueError:
    print("Nominal harus berupa angka.")

summarize_transactions()
analyze_expenses()
```

---

## Slide 76

**Header:** FINAL PROJECT
**Subheader:** Challenge Tambahan

# Challenge Tambahan

Kalau program dasar sudah selesai, pilih minimal 1 upgrade:

1. Tambahkan fitur input 3 transaksi sekaligus.
2. Tambahkan kategori seperti `makanan`, `transportasi`, `sekolah`, `hiburan`.
3. Hitung total pengeluaran per kategori.
4. Tambahkan fitur mencari transaksi terbesar.
5. Tambahkan rekomendasi: “hemat”, “aman”, atau “perlu evaluasi”.
6. Tambahkan menu sederhana dengan pilihan angka.

---

## Slide 77

**Header:** FINAL PROJECT
**Subheader:** Completion Criteria

# Kriteria Completion / Kehadiran

Tugas dihitung selesai jika program:

| Kriteria                                             | Wajib |
| ---------------------------------------------------- | ----- |
| Menggunakan list dan dictionary                      | Ya    |
| Bisa mencatat transaksi                              | Ya    |
| Menggunakan input validation                         | Ya    |
| Menggunakan sanitasi `.strip()` / `.lower()`         | Ya    |
| Menggunakan `try-except`                             | Ya    |
| Menangani minimal `ValueError`                       | Ya    |
| Menghitung pemasukan dan pengeluaran                 | Ya    |
| Menghitung saldo                                     | Ya    |
| Menampilkan analisis min, max, total, atau rata-rata | Ya    |
| Menampilkan pesan error yang jelas                   | Ya    |

---

## Slide 78

**Header:** WRAP UP
**Subheader:** Coding Summary

# Rangkuman Coding

Hari ini kita belajar:

* Input pengguna harus dicek sebelum diproses.
* Sanitasi input membersihkan data agar lebih rapi.
* Validasi input memastikan data boleh dipakai.
* `try-except` membantu program tetap berjalan saat error.
* Debugging dilakukan dengan mengecek program langkah demi langkah.
* Dictionary bisa menyimpan data transaksi.
* List bisa menyimpan banyak transaksi.
* Function membuat program lebih modular dan mudah diperbaiki.

---

## Slide 79

**Header:** WRAP UP
**Subheader:** Financial Literacy Summary

# Rangkuman Financial Literacy

Dalam financial literacy, kita belajar:

* Transaksi bisa berupa pemasukan atau pengeluaran.
* Pencatatan transaksi membantu memahami penggunaan uang.
* Data finansial bisa dianalisis dengan total, min, max, dan rata-rata.
* Input yang salah bisa membuat catatan keuangan tidak akurat.
* Program finansial perlu validasi agar data lebih aman dan masuk akal.

---

## Slide 80

**Header:** EXIT TICKET
**Subheader:** Reflection

# Exit Ticket

Jawab 5 pertanyaan ini:

1. Kenapa input pengguna perlu divalidasi?
2. Apa bedanya sanitasi input dan validasi input?
3. Apa fungsi `try-except`?
4. Kenapa dictionary cocok untuk mencatat transaksi?
5. Bagaimana analisis data bisa membantu keputusan finansial?

Contoh jawaban:

Input perlu divalidasi agar program tidak memproses data yang salah.

Sanitasi membersihkan input, sedangkan validasi mengecek apakah input boleh dipakai.

`try-except` digunakan untuk menangani error agar program tidak berhenti tiba-tiba.

Dictionary cocok karena satu transaksi punya beberapa informasi seperti nama, jenis, dan nominal.

Analisis data membantu kita melihat pola pengeluaran dan membuat keputusan yang lebih bijak.

---
