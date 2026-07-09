const fs = require('fs');

const html = fs.readFileSync('slide_deck_part1.html', 'utf-8');
const slides = html.split('<div class="slide"');

const keywords = [
    "Sanitasi dan Validasi itu Berbeda", // Quiz 1
    "Mini Project: Safe Transaction Input", // Mini Task 1
    "Tebak Jenis Error", // Quiz Try-Except?
    "Lengkapi Blok `try-except`", // Quiz Try-Except? Let's check both
    "Mini Project: Safe Input with Error Handling", // Mini Task 2
    "Latihan: Temukan Bug", // Quiz Debugging
    "Latihan: Perbaiki Nilai Diskon", // Latihan Cari Error
    "Kuis Cepat: Tipe Data Transaksi", // Quiz Dictionary
    "Latihan: Menghitung Total Pemasukan", // Quiz Analisis Data
    "Analisis Data: Total Pemasukan", // Maybe this is it?
    "Mini Project: Debugging Program Belanja", // wait, what was the mini project for debugging?
    "Mini Project: Aplikasi Pencatat Transaksi" // Mini Project Expenses
];

keywords.forEach((kw, i) => {
    const s = slides.find(sl => sl.includes(kw));
    if (s) {
        fs.writeFileSync(`slide_${i}.html`, s);
        console.log(`Saved slide_${i}.html for "${kw}"`);
    } else {
        console.log(`NOT FOUND: "${kw}"`);
    }
});
