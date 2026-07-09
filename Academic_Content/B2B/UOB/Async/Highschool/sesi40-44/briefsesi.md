# Deck Python SMA

## Designing & Building Financial Literacy App

---

## Slide 1

**Header:** PYTHON PROJECT
**Subheader:** Financial Literacy App

# Dari Ide Menjadi Aplikasi

Sebelumnya kita sudah belajar membuat program yang bisa:

* Mencatat transaksi
* Memvalidasi input
* Menggunakan `try-except`
* Menyimpan data dengan dictionary
* Menghitung ringkasan keuangan
* Menganalisis data sederhana

Sekarang kita akan belajar cara merancang aplikasi finansial sebelum membuat kodenya.

---

## Slide 2

**Header:** PYTHON PROJECT
**Subheader:** Learning Goals

# Apa yang Akan Kita Pelajari?

Hari ini kita akan belajar:

1. Membuat problem statement.
2. Membuat ide solusi berdasarkan kebutuhan pengguna.
3. Membuat flow aplikasi.
4. Membuat use case diagram sederhana.
5. Menghubungkan user interaction ke function Python.
6. Membuat rekomendasi finansial berdasarkan data.
7. Mengintegrasikan function, loop, dan dictionary.

---

# BAGIAN 1

## Design Thinking untuk Aplikasi Financial Literacy

---

## Slide 3

**Header:** DESIGN THINKING
**Subheader:** Problem First

# Apa Itu Design Thinking?

**Design thinking** adalah cara membuat solusi dengan memahami masalah pengguna terlebih dahulu.

Sederhananya:

> Jangan langsung bikin aplikasi. Pahami dulu masalah siapa yang ingin dibantu.

Contoh:

Bukan langsung bilang:

“Aku mau bikin aplikasi catatan uang.”

Tapi mulai dari:

“Banyak siswa tidak sadar uang sakunya habis untuk apa.”

---

## Slide 4

**Header:** DESIGN THINKING
**Subheader:** Analogi Sederhana

# Design Thinking Seperti Membuat Bekal

Bayangkan kamu ingin membuat bekal untuk teman.

Kamu tidak langsung memasak apa saja.

Kamu perlu tahu dulu:

* Temanmu suka makan apa?
* Dia alergi apa?
* Dia butuh makan berat atau snack?
* Bekalnya dibawa ke mana?

Aplikasi juga begitu.

Sebelum membuat fitur, kita perlu memahami pengguna.

---

## Slide 5

**Header:** DESIGN THINKING
**Subheader:** User Problem

# Siapa Pengguna Aplikasi Kita?

Untuk project ini, pengguna aplikasi kita adalah:

**Siswa SMA yang ingin mengatur uang saku dengan lebih baik.**

Masalah yang mungkin mereka alami:

* Sering lupa mencatat pengeluaran
* Tidak tahu uang paling banyak habis untuk apa
* Sulit membedakan kebutuhan dan keinginan
* Tidak punya target tabungan
* Sering membeli barang impulsif

---

## Slide 6

**Header:** DESIGN THINKING
**Subheader:** Problem Statement

# Apa Itu Problem Statement?

**Problem statement** adalah kalimat yang menjelaskan masalah utama yang ingin diselesaikan.

Format sederhana:

```text
Pengguna mengalami [masalah] karena [penyebab], sehingga [dampak].
```

Contoh:

```text
Siswa sering kehabisan uang saku sebelum akhir minggu karena tidak mencatat pengeluaran, sehingga sulit menabung.
```

Problem statement membantu kita fokus.

---

## Slide 7

**Header:** DESIGN THINKING
**Subheader:** Contoh Problem Statement

# Contoh Masalah Aplikasi Finansial

Contoh 1:

```text
Siswa sulit mengetahui pengeluaran terbesar karena transaksi tidak dicatat secara rapi.
```

Contoh 2:

```text
Siswa sering membeli keinginan karena tidak mengecek sisa budget sebelum belanja.
```

Contoh 3:

```text
Siswa ingin menabung, tetapi tidak tahu apakah pengeluarannya masih aman.
```

Setiap problem statement bisa menghasilkan fitur aplikasi yang berbeda.

---

## Slide 8

**Header:** DESIGN THINKING
**Subheader:** Solution Idea

# Dari Masalah ke Ide Solusi

Kalau masalahnya:

```text
Siswa tidak tahu uangnya habis untuk apa.
```

Ide solusinya bisa:

```text
Aplikasi pencatat transaksi yang menampilkan total pengeluaran dan kategori terbesar.
```

Kalau masalahnya:

```text
Siswa sulit menabung.
```

Ide solusinya bisa:

```text
Aplikasi yang mengecek target tabungan dan memberi rekomendasi pengeluaran.
```

---

## Slide 9

**Header:** DESIGN THINKING
**Subheader:** User Needs

# Solusi Harus Berdasarkan Kebutuhan Pengguna

Fitur yang dibuat harus menjawab kebutuhan pengguna.

| Kebutuhan Pengguna              | Fitur Aplikasi               |
| ------------------------------- | ---------------------------- |
| Ingin mencatat uang masuk       | Tambah transaksi pemasukan   |
| Ingin mencatat uang keluar      | Tambah transaksi pengeluaran |
| Ingin tahu saldo                | Ringkasan saldo              |
| Ingin tahu pengeluaran terbesar | Analisis max expense         |
| Ingin mendapat saran            | Rekomendasi finansial        |

Fitur yang baik bukan hanya keren, tapi berguna.

---

## Slide 10

**Header:** DESIGN THINKING
**Subheader:** Feasibility

# Apa Itu Feasibility?

**Feasibility** artinya apakah fitur mungkin dibuat dengan kemampuan dan waktu yang kita punya.

Contoh:

Fitur yang cukup feasible:

* Menambah transaksi
* Menghitung saldo
* Menampilkan total pengeluaran
* Memberi rekomendasi sederhana

Fitur yang belum feasible untuk tahap ini:

* Login akun online
* Database cloud
* Grafik interaktif kompleks
* AI financial advisor otomatis

Kita mulai dari fitur yang bisa dibuat dulu.

---

## Slide 11

**Header:** DESIGN THINKING
**Subheader:** Latihan

# Latihan: Buat Problem Statement

Lengkapi kalimat berikut.

```text
Siswa mengalami __________ karena __________, sehingga __________.
```

Contoh jawaban:

```text
Siswa mengalami kesulitan menabung karena tidak mencatat pengeluaran, sehingga uang sering habis tanpa sadar.
```

---

## Slide 12

**Header:** DESIGN THINKING
**Subheader:** Latihan

# Latihan: Masalah ke Fitur

Pasangkan masalah dengan fitur yang cocok.

| Masalah                           | Fitur yang Cocok                    |
| --------------------------------- | ----------------------------------- |
| Tidak tahu saldo                  | Ringkasan pemasukan dan pengeluaran |
| Sering lupa catat uang keluar     | Fitur tambah transaksi              |
| Pengeluaran makanan terlalu besar | Analisis kategori                   |
| Sulit menabung                    | Target tabungan dan rekomendasi     |

---

## Slide 13

**Header:** DESIGN THINKING
**Subheader:** Mini Activity

# Mini Activity: Rancang Ide Aplikasi

Buat rancangan singkat aplikasi finansialmu.

Isi 4 bagian ini:

1. Nama aplikasi
2. Masalah pengguna
3. Solusi utama
4. Fitur utama

Contoh:

```text
Nama aplikasi: Money Buddy
Masalah: Siswa sering tidak sadar uang saku habis.
Solusi: Aplikasi mencatat transaksi dan memberi ringkasan.
Fitur: tambah transaksi, cek saldo, analisis pengeluaran.
```

---

# BAGIAN 2

## Use Case Diagram & Program Flow

---

## Slide 14

**Header:** PROGRAM DESIGN
**Subheader:** User Interaction

# Apa Itu Use Case?

**Use case** adalah aktivitas yang bisa dilakukan pengguna dalam aplikasi.

Sederhananya:

> Pengguna bisa ngapain saja di aplikasi ini?

Contoh use case aplikasi keuangan:

* Menambah transaksi
* Melihat ringkasan saldo
* Melihat analisis pengeluaran
* Mendapat rekomendasi
* Keluar dari program

---

## Slide 15

**Header:** PROGRAM DESIGN
**Subheader:** Use Case Diagram

# Use Case Diagram Sederhana

Dalam bentuk teks, use case diagram bisa ditulis seperti ini:

```text
User
 ├── Tambah transaksi
 ├── Lihat ringkasan keuangan
 ├── Analisis pengeluaran
 ├── Lihat rekomendasi
 └── Keluar aplikasi
```

Diagram ini membantu kita melihat fitur dari sudut pandang pengguna.

---

## Slide 16

**Header:** PROGRAM DESIGN
**Subheader:** Dari Use Case ke Function

# Memetakan Use Case ke Function

Setiap use case bisa diubah menjadi function.

| Use Case             | Function Python            |
| -------------------- | -------------------------- |
| Tambah transaksi     | `add_transaction()`        |
| Lihat ringkasan      | `summarize_transactions()` |
| Analisis pengeluaran | `analyze_expenses()`       |
| Lihat rekomendasi    | `give_recommendation()`    |
| Membersihkan input   | `clean_text()`             |

Dengan mapping ini, kita lebih mudah membuat struktur kode.

---

## Slide 17

**Header:** PROGRAM DESIGN
**Subheader:** Program Flow

# Apa Itu Program Flow?

**Program flow** adalah urutan langkah program dari awal sampai akhir.

Contoh flow sederhana:

```text
Mulai
↓
Tampilkan menu
↓
User memilih fitur
↓
Program menjalankan function
↓
Tampilkan hasil
↓
Kembali ke menu atau selesai
```

Flow membantu kita tahu program harus berjalan seperti apa.

---

## Slide 18

**Header:** PROGRAM DESIGN
**Subheader:** Flow Aplikasi Finansial

# Contoh Flow Safe Finance Tracker

```text
Mulai
↓
Tampilkan menu
↓
Pilih 1: Tambah transaksi
Pilih 2: Lihat ringkasan
Pilih 3: Analisis pengeluaran
Pilih 4: Rekomendasi
Pilih 5: Keluar
↓
Jalankan fitur sesuai pilihan
↓
Kembali ke menu
```

Menu membuat program terasa seperti aplikasi.

---

## Slide 19

**Header:** PROGRAM DESIGN
**Subheader:** Menu Program

# Contoh Menu di Python

```python id="oagxip"
print("=== SAFE FINANCE TRACKER ===")
print("1. Tambah transaksi")
print("2. Lihat ringkasan")
print("3. Analisis pengeluaran")
print("4. Rekomendasi")
print("5. Keluar")

choice = input("Pilih menu: ")
```

Input `choice` nanti dipakai untuk menentukan function mana yang dijalankan.

---

## Slide 20

**Header:** PROGRAM DESIGN
**Subheader:** Choice to Function

# Menghubungkan Pilihan ke Function

```python id="6uz0zt"
if choice == "1":
    add_transaction()
elif choice == "2":
    summarize_transactions()
elif choice == "3":
    analyze_expenses()
elif choice == "4":
    give_recommendation()
elif choice == "5":
    print("Terima kasih!")
else:
    print("Pilihan tidak valid.")
```

Ini adalah contoh user interaction yang dipetakan ke function.

---

## Slide 21

**Header:** PROGRAM DESIGN
**Subheader:** Struktur Awal Kode

# Struktur Awal Program

```python id="9itc6j"
transactions = []

def add_transaction():
    pass

def summarize_transactions():
    pass

def analyze_expenses():
    pass

def give_recommendation():
    pass

def show_menu():
    pass
```

`pass` artinya function belum diisi.

Kita bisa membuat kerangka program dulu, lalu mengisi function satu per satu.

---

## Slide 22

**Header:** PROGRAM DESIGN
**Subheader:** Latihan

# Latihan: Cocokkan Use Case dan Function

Pasangkan use case dengan function yang tepat.

| Use Case                | Function                   |
| ----------------------- | -------------------------- |
| Membersihkan teks input | `clean_text()`             |
| Mengecek nominal        | `validate_amount()`        |
| Menambah transaksi      | `add_transaction()`        |
| Menampilkan saldo       | `summarize_transactions()` |
| Memberi saran           | `give_recommendation()`    |

---

## Slide 23

**Header:** PROGRAM DESIGN
**Subheader:** Latihan

# Latihan: Lengkapi Menu

Lengkapi kode berikut.

```python id="p06d0x"
choice = input("Pilih menu: ")

if choice == "1":
    add_transaction()
elif choice == "2":
    __________
elif choice == "3":
    analyze_expenses()
else:
    print("Pilihan tidak valid")
```

Jawaban:

```python id="x6v06e"
summarize_transactions()
```

---

## Slide 24

**Header:** PROGRAM DESIGN
**Subheader:** Mini Activity

# Mini Activity: Buat Flow Aplikasi

Buat flow aplikasi finansialmu dalam bentuk teks.

Minimal punya:

1. Mulai
2. Tampilkan menu
3. Tambah transaksi
4. Lihat ringkasan
5. Analisis data
6. Keluar

Contoh:

```text
Mulai → Menu → Pilih fitur → Jalankan function → Tampilkan hasil → Menu lagi
```

---

# BAGIAN 3

## Evaluasi Data untuk Keputusan Finansial

---

## Slide 25

**Header:** FINANCIAL DATA
**Subheader:** Data to Decision

# Data Bisa Membantu Membuat Keputusan

Program finansial bukan hanya mencatat data.

Program juga bisa membantu pengguna mengambil keputusan.

Contoh:

Kalau pengeluaran terlalu besar, program bisa memberi saran.

Kalau saldo masih aman, program bisa memberi pesan positif.

Kalau target tabungan belum tercapai, program bisa memberi rekomendasi.

---

## Slide 26

**Header:** FINANCIAL DATA
**Subheader:** Insight

# Apa Itu Insight?

**Insight** adalah kesimpulan yang kita dapat setelah membaca data.

Data:

```text
Pengeluaran makanan = 80.000
Pengeluaran transportasi = 20.000
Pengeluaran hiburan = 10.000
```

Insight:

```text
Pengeluaran terbesar ada di makanan.
```

Keputusan:

```text
Coba kurangi snack atau bawa bekal.
```

---

## Slide 27

**Header:** FINANCIAL DATA
**Subheader:** Dari Data ke Rekomendasi

# Data → Insight → Rekomendasi

Urutannya:

```text
Data
↓
Insight
↓
Rekomendasi
```

Contoh:

Data:

```text
Saldo tersisa 5.000
```

Insight:

```text
Saldo hampir habis.
```

Rekomendasi:

```text
Tunda pembelian keinginan.
```

---

## Slide 28

**Header:** FINANCIAL DATA
**Subheader:** Contoh Logika Rekomendasi

# Membuat Rekomendasi dengan `if`

```python id="7d9u2h"
balance = 5000

if balance < 10000:
    print("Rekomendasi: Tunda pembelian keinginan.")
elif balance < 30000:
    print("Rekomendasi: Hati-hati, saldo mulai terbatas.")
else:
    print("Rekomendasi: Saldo masih cukup aman.")
```

Program menggunakan data saldo untuk memberi saran.

---

## Slide 29

**Header:** FINANCIAL DATA
**Subheader:** Pola Pengeluaran

# Membaca Pola Pengeluaran

```python id="9xuic9"
category_total = {
    "makanan": 80000,
    "transportasi": 20000,
    "hiburan": 10000
}
```

Dari data ini, terlihat bahwa pengeluaran terbesar adalah:

```python id="ra8v41"
makanan
```

Program bisa memberi insight:

```text
Pengeluaran makanan paling besar.
```

---

## Slide 30

**Header:** FINANCIAL DATA
**Subheader:** Mencari Kategori Terbesar

# Program Mencari Pengeluaran Terbesar

```python id="fy3rdu"
category_total = {
    "makanan": 80000,
    "transportasi": 20000,
    "hiburan": 10000
}

largest_category = max(category_total, key=category_total.get)

print("Kategori terbesar:", largest_category)
print("Jumlah:", category_total[largest_category])
```

Output:

```python id="vb5z35"
Kategori terbesar: makanan
Jumlah: 80000
```

---

## Slide 31

**Header:** FINANCIAL DATA
**Subheader:** Rekomendasi Berdasarkan Kategori

# Memberi Rekomendasi dari Insight

```python id="u071i7"
largest_category = "makanan"

if largest_category == "makanan":
    print("Coba kurangi snack atau bawa bekal.")
elif largest_category == "transportasi":
    print("Coba rencanakan perjalanan agar lebih hemat.")
elif largest_category == "hiburan":
    print("Batasi pengeluaran hiburan minggu ini.")
else:
    print("Cek kembali budget tiap kategori.")
```

Rekomendasi harus punya alasan yang masuk akal.

---

## Slide 32

**Header:** FINANCIAL DATA
**Subheader:** Reasoning

# Rekomendasi Harus Ada Alasannya

Program yang baik tidak hanya berkata:

```text
Hemat ya!
```

Tapi memberi alasan:

```text
Pengeluaran terbesar kamu ada di makanan, jadi coba kurangi snack atau bawa bekal.
```

Alasan membuat rekomendasi lebih mudah dipercaya.

---

## Slide 33

**Header:** FINANCIAL DATA
**Subheader:** Latihan

# Latihan: Data ke Insight

Diberikan data:

```python id="9o21hu"
category_total = {
    "makanan": 30000,
    "sekolah": 70000,
    "hiburan": 20000
}
```

Pertanyaan:

Kategori mana yang paling besar?

Jawaban:

```python id="oswa33"
sekolah
```

Insight:

```text
Pengeluaran terbesar ada di kategori sekolah.
```

---

## Slide 34

**Header:** FINANCIAL DATA
**Subheader:** Latihan

# Latihan: Buat Rekomendasi

Data:

```text
Saldo tersisa 8.000
Target tabungan belum tercapai
```

Buat rekomendasi yang masuk akal.

Contoh jawaban:

```text
Sebaiknya tunda pembelian keinginan karena saldo tinggal sedikit dan target tabungan belum tercapai.
```

---

## Slide 35

**Header:** FINANCIAL DATA
**Subheader:** Mini Project

# Mini Project: Recommendation Engine

Buat function yang memberi rekomendasi berdasarkan saldo.

```python id="iydr8x"
def give_balance_recommendation(balance):
    if balance < 10000:
        return "Tunda pembelian keinginan."
    elif balance < 30000:
        return "Hati-hati, saldo mulai terbatas."
    else:
        return "Saldo masih cukup aman."

recommendation = give_balance_recommendation(8000)
print(recommendation)
```

Output:

```python id="nz591c"
Tunda pembelian keinginan.
```

---

# BAGIAN 4

## Integrasi Functions–Loops–Dictionary

---

## Slide 36

**Header:** APP INTEGRATION
**Subheader:** Combining Concepts

# Menggabungkan Semua Konsep

Sekarang kita akan menggabungkan:

* Function
* Loop
* Dictionary
* List
* Conditional
* Input validation
* Error handling

Semua konsep ini dipakai untuk membuat aplikasi finansial yang lebih lengkap.

---

## Slide 37

**Header:** APP INTEGRATION
**Subheader:** Peran Setiap Konsep

# Fungsi Masing-Masing Konsep

| Konsep      | Peran dalam Aplikasi                 |
| ----------- | ------------------------------------ |
| Function    | Membagi fitur menjadi bagian kecil   |
| Loop        | Mengulang menu dan membaca transaksi |
| Dictionary  | Menyimpan satu transaksi             |
| List        | Menyimpan banyak transaksi           |
| Conditional | Memilih aksi dan memberi rekomendasi |
| Validation  | Mencegah input salah                 |

---

## Slide 38

**Header:** APP INTEGRATION
**Subheader:** Program Structure

# Struktur Program yang Rapi

```python id="851vbc"
transactions = []

def clean_text(text):
    return text.strip().lower()

def add_transaction():
    pass

def summarize_transactions():
    pass

def analyze_by_category():
    pass

def give_recommendation():
    pass

def show_menu():
    pass
```

Struktur ini membuat program mudah dikembangkan.

---

## Slide 39

**Header:** APP INTEGRATION
**Subheader:** Loop Menu

# Membuat Menu Berulang dengan Loop

```python id="ugmury"
while True:
    print("1. Tambah transaksi")
    print("2. Ringkasan")
    print("3. Analisis kategori")
    print("4. Rekomendasi")
    print("5. Keluar")

    choice = input("Pilih menu: ")

    if choice == "5":
        print("Terima kasih!")
        break
```

`while True` membuat menu terus muncul sampai pengguna memilih keluar.

---

## Slide 40

**Header:** APP INTEGRATION
**Subheader:** Avoid Redundant Code

# Menghindari Kode Berulang

Kode kurang rapi:

```python id="m0yddy"
print("1. Tambah transaksi")
print("2. Ringkasan")
print("3. Analisis kategori")
print("4. Rekomendasi")
print("5. Keluar")
```

Kalau menu sering dipakai, lebih baik dibuat function:

```python id="7lp87k"
def show_menu():
    print("1. Tambah transaksi")
    print("2. Ringkasan")
    print("3. Analisis kategori")
    print("4. Rekomendasi")
    print("5. Keluar")
```

Lalu panggil:

```python id="7zjp8s"
show_menu()
```

---

## Slide 41

**Header:** APP INTEGRATION
**Subheader:** Add Transaction

# Function `add_transaction()`

```python id="v5osjz"
transactions = []

def add_transaction():
    name = input("Nama transaksi: ").strip()
    transaction_type = input("Jenis (pemasukan/pengeluaran): ").strip().lower()
    category = input("Kategori: ").strip().lower()

    try:
        amount = int(input("Nominal: "))

        if name == "":
            print("Nama transaksi tidak boleh kosong.")
        elif transaction_type != "pemasukan" and transaction_type != "pengeluaran":
            print("Jenis transaksi tidak valid.")
        elif amount <= 0:
            print("Nominal harus lebih dari 0.")
        else:
            transaction = {
                "name": name,
                "type": transaction_type,
                "category": category,
                "amount": amount
            }

            transactions.append(transaction)
            print("Transaksi berhasil ditambahkan.")

    except ValueError:
        print("Nominal harus berupa angka.")
```

---

## Slide 42

**Header:** APP INTEGRATION
**Subheader:** Summary Function

# Function `summarize_transactions()`

```python id="6vtbxz"
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

    return balance
```

Function ini mengembalikan `balance` agar bisa dipakai function lain.

---

## Slide 43

**Header:** APP INTEGRATION
**Subheader:** Category Analysis

# Function `analyze_by_category()`

```python id="pv086b"
def analyze_by_category():
    category_total = {}

    for transaction in transactions:
        if transaction["type"] == "pengeluaran":
            category = transaction["category"]
            amount = transaction["amount"]

            if category not in category_total:
                category_total[category] = 0

            category_total[category] += amount

    print(category_total)

    return category_total
```

Function ini menghitung total pengeluaran per kategori.

---

## Slide 44

**Header:** APP INTEGRATION
**Subheader:** Recommendation Function

# Function `give_recommendation()`

```python id="2zlv4g"
def give_recommendation():
    balance = summarize_transactions()
    category_total = analyze_by_category()

    if balance < 10000:
        print("Rekomendasi: Tunda pembelian keinginan.")
    elif balance < 30000:
        print("Rekomendasi: Hati-hati, saldo mulai terbatas.")
    else:
        print("Rekomendasi: Saldo masih cukup aman.")

    if len(category_total) > 0:
        largest_category = max(category_total, key=category_total.get)
        print("Kategori pengeluaran terbesar:", largest_category)
```

Function ini memakai hasil dari function lain.

---

## Slide 45

**Header:** APP INTEGRATION
**Subheader:** Main Program

# Menghubungkan Semua Function

```python id="g0z25l"
def show_menu():
    print("=== SAFE FINANCE TRACKER ===")
    print("1. Tambah transaksi")
    print("2. Ringkasan")
    print("3. Analisis kategori")
    print("4. Rekomendasi")
    print("5. Keluar")

while True:
    show_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        summarize_transactions()
    elif choice == "3":
        analyze_by_category()
    elif choice == "4":
        give_recommendation()
    elif choice == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
```

Inilah alur utama aplikasi.

---

## Slide 46

**Header:** APP INTEGRATION
**Subheader:** Latihan

# Latihan: Lengkapi Function Call

Lengkapi kode berikut.

```python id="4s7a9s"
if choice == "1":
    __________
elif choice == "2":
    summarize_transactions()
```

Jawaban:

```python id="kfn5uu"
add_transaction()
```

Karena pilihan 1 digunakan untuk menambah transaksi.

---

## Slide 47

**Header:** APP INTEGRATION
**Subheader:** Latihan

# Latihan: Debug Program Flow

Kode berikut punya bug.

```python id="begwln"
while True:
    show_menu()
    choice = input("Pilih menu: ")

    if choice == "5":
        print("Terima kasih!")
```

Masalah:

Program tidak pernah berhenti walaupun pengguna memilih 5.

Apa yang kurang?

Jawaban:

```python id="6c8f8e"
break
```

Kode benar:

```python id="30cx83"
if choice == "5":
    print("Terima kasih!")
    break
```

---

## Slide 48

**Header:** APP INTEGRATION
**Subheader:** Mini Project

# Mini Project: App Integration

Gabungkan fitur berikut ke dalam satu program:

1. Menu utama
2. Tambah transaksi
3. Ringkasan transaksi
4. Analisis kategori
5. Rekomendasi saldo
6. Keluar program

Gunakan:

* Function
* Loop
* Dictionary
* List
* Conditional
* Input validation

---

# BAGIAN 5

## Final Project

---

## Slide 49

**Header:** FINAL PROJECT
**Subheader:** Finance App Prototype

# Tugas Besar: Finance App Prototype

Buat prototype aplikasi finansial berbasis Python.

Program harus dimulai dari rancangan sederhana, lalu dibuat menjadi kode.

Project ini terdiri dari dua bagian:

1. Planning aplikasi
2. Coding aplikasi

---

## Slide 50

**Header:** FINAL PROJECT
**Subheader:** Part 1 — Planning

# Bagian 1: Planning Aplikasi

Sebelum coding, buat rancangan singkat:

1. Nama aplikasi
2. Problem statement
3. Target pengguna
4. Fitur utama
5. Use case diagram sederhana
6. Program flow
7. Function mapping

---

## Slide 51

**Header:** FINAL PROJECT
**Subheader:** Planning Template

# Template Planning

```text
Nama aplikasi:
Target pengguna:
Problem statement:

Fitur utama:
1.
2.
3.

Use case:
- User bisa ...
- User bisa ...
- User bisa ...

Program flow:
Mulai → ... → Selesai

Function mapping:
- Fitur ... → function ...
- Fitur ... → function ...
```

---

## Slide 52

**Header:** FINAL PROJECT
**Subheader:** Part 2 — Coding

# Bagian 2: Coding Aplikasi

Program Python harus memiliki:

1. Menu utama.
2. Minimal 3 fitur.
3. List untuk menyimpan data transaksi.
4. Dictionary untuk menyimpan satu transaksi.
5. Function untuk setiap fitur.
6. Loop untuk menjalankan menu.
7. Validasi input sederhana.
8. Rekomendasi berdasarkan data.

---

## Slide 53

**Header:** FINAL PROJECT
**Subheader:** Starter Code

# Starter Code Final Project

```python id="tmqb3p"
transactions = []

def clean_text(text):
    return text.strip().lower()

def show_menu():
    print("=== SAFE FINANCE TRACKER ===")
    print("1. Tambah transaksi")
    print("2. Ringkasan")
    print("3. Analisis kategori")
    print("4. Rekomendasi")
    print("5. Keluar")

def add_transaction():
    name = input("Nama transaksi: ").strip()
    transaction_type = clean_text(input("Jenis (pemasukan/pengeluaran): "))
    category = clean_text(input("Kategori: "))

    try:
        amount = int(input("Nominal: "))

        if name == "":
            print("Nama tidak boleh kosong.")
        elif transaction_type != "pemasukan" and transaction_type != "pengeluaran":
            print("Jenis transaksi tidak valid.")
        elif amount <= 0:
            print("Nominal harus lebih dari 0.")
        else:
            transaction = {
                "name": name,
                "type": transaction_type,
                "category": category,
                "amount": amount
            }
            transactions.append(transaction)
            print("Transaksi berhasil ditambahkan.")

    except ValueError:
        print("Nominal harus berupa angka.")

def summarize_transactions():
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

    return balance

def analyze_by_category():
    category_total = {}

    for transaction in transactions:
        if transaction["type"] == "pengeluaran":
            category = transaction["category"]
            amount = transaction["amount"]

            if category not in category_total:
                category_total[category] = 0

            category_total[category] += amount

    print("Pengeluaran per kategori:", category_total)
    return category_total

def give_recommendation():
    balance = summarize_transactions()
    category_total = analyze_by_category()

    if balance < 10000:
        print("Rekomendasi: Tunda pembelian keinginan.")
    elif balance < 30000:
        print("Rekomendasi: Hati-hati, saldo mulai terbatas.")
    else:
        print("Rekomendasi: Saldo masih cukup aman.")

    if len(category_total) > 0:
        largest_category = max(category_total, key=category_total.get)
        print("Kategori pengeluaran terbesar:", largest_category)
        print("Coba evaluasi pengeluaran di kategori tersebut.")

while True:
    show_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        summarize_transactions()
    elif choice == "3":
        analyze_by_category()
    elif choice == "4":
        give_recommendation()
    elif choice == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
```

---

## Slide 54

**Header:** FINAL PROJECT
**Subheader:** Challenge Tambahan

# Challenge Tambahan

Kalau program dasar sudah selesai, pilih minimal 1 upgrade:

1. Tambahkan target tabungan.
2. Tambahkan fitur cek apakah target tercapai.
3. Tambahkan fitur rekomendasi berdasarkan kategori terbesar.
4. Tambahkan input beberapa transaksi sekaligus.
5. Tambahkan validasi kategori tidak boleh kosong.
6. Tambahkan format output yang lebih rapi.
7. Tambahkan fitur mencari transaksi terbesar.

---

## Slide 55

**Header:** FINAL PROJECT
**Subheader:** Completion Criteria

# Kriteria Completion / Kehadiran

Tugas dihitung selesai jika:

| Kriteria                             | Wajib |
| ------------------------------------ | ----- |
| Membuat problem statement            | Ya    |
| Membuat use case sederhana           | Ya    |
| Membuat program flow                 | Ya    |
| Menggunakan function                 | Ya    |
| Menggunakan loop                     | Ya    |
| Menggunakan dictionary               | Ya    |
| Menggunakan list transaksi           | Ya    |
| Memiliki minimal 3 fitur             | Ya    |
| Memberi rekomendasi berdasarkan data | Ya    |
| Kode tidak terlalu redundant         | Ya    |

---

## Slide 56

**Header:** WRAP UP
**Subheader:** Coding Summary

# Rangkuman Coding

Hari ini kita belajar:

* Design thinking membantu kita memahami masalah sebelum membuat aplikasi.
* Problem statement membuat tujuan aplikasi lebih jelas.
* Use case membantu memetakan aktivitas pengguna.
* Program flow membantu menyusun alur aplikasi.
* Function membuat fitur lebih rapi.
* Loop membuat menu bisa berjalan berulang.
* Dictionary menyimpan satu transaksi.
* List menyimpan banyak transaksi.
* Data bisa dipakai untuk memberi rekomendasi.

---

## Slide 57

**Header:** WRAP UP
**Subheader:** Financial Literacy Summary

# Rangkuman Financial Literacy

Dalam financial literacy, kita belajar:

* Aplikasi finansial harus menjawab kebutuhan pengguna.
* Data transaksi bisa membantu melihat pola pengeluaran.
* Insight membantu pengguna memahami kondisi keuangan.
* Rekomendasi harus dibuat berdasarkan data.
* Keputusan finansial yang baik perlu alasan yang jelas.

---

## Slide 58

**Header:** EXIT TICKET
**Subheader:** Reflection

# Exit Ticket

Jawab 5 pertanyaan ini:

1. Apa itu problem statement?
2. Kenapa use case penting sebelum coding?
3. Apa hubungan user interaction dengan function?
4. Bagaimana data transaksi bisa menghasilkan rekomendasi?
5. Kenapa function, loop, dan dictionary perlu digabung dalam aplikasi?

Contoh jawaban:

Problem statement adalah kalimat yang menjelaskan masalah utama pengguna.

Use case penting agar kita tahu fitur apa saja yang perlu dibuat.

User interaction bisa dipetakan menjadi function, misalnya “Tambah transaksi” menjadi `add_transaction()`.

Data transaksi bisa menunjukkan pola pengeluaran dan membantu memberi saran.

Function, loop, dan dictionary perlu digabung agar aplikasi bisa menyimpan data, menjalankan menu, dan mengatur fitur dengan rapi.

---
