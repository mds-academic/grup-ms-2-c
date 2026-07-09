const fs = require('fs');
const html = fs.readFileSync('slide_deck_part1.html', 'utf-8');

const slideTitles = [
    "Sanitasi dan Validasi itu Berbeda!", // Quiz 1
    "Mini Project: Safe Transaction Input", // Mini Task 1
    "Lengkapi Blok Try-Except", // Quiz 2 (Try-Except)
    "Mini Project: Transaksi Anti-Crash", // Mini Task 2
    "Tebak Error Part 1", // Quiz 3 (Debugging) - Wait, "Tebak Error" is Try-Except, what is Debugging? "Latihan: Di Mana Letak Bug-nya?"
    "Perbaiki Bug-nya!", // Latihan Cari Error
    "Kuis Cepat: Tipe Data Transaksi", // Quiz 4 (Dictionary)
    "Analisis Data: Total Pemasukan", // Quiz 5 (Analisis Data)
    "Mini Project: Rekap Transaksi" // Mini Project Expenses - wait, maybe "Rekap"
];

const slides = html.split('<div class="slide"');
slideTitles.forEach(title => {
    const slide = slides.find(s => s.includes(title));
    if (slide) {
        console.log(`FOUND: ${title}`);
    } else {
        console.log(`NOT FOUND: ${title}`);
    }
});
