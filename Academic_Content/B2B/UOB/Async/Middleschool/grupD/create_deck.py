import json
import os

html_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MIT App Inventor SMP - Procedures & Impact</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --yellow: #FFE500;
            --blue: #00C6FF;
            --black: #1A1A1A;
            --white: #FFFFFF;
            --bg-light: #E8E8E8;
            --green: #00E676;
            --pink: #FF9DE2;
            --red: #FF0055;
            --orange: #FF9800;
            --purple: #B388FF;
            --brown: #a52a2a;
        }

        body {
            background-color: var(--bg-light);
            background-image: radial-gradient(#bcbcbc 2px, transparent 2px);
            background-size: 30px 30px;
            font-family: 'Fredoka', sans-serif;
            color: var(--black);
            overflow: hidden;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .app-container {
            position: relative; z-index: 10;
            width: 98vw; max-width: 1400px;
            height: 98vh; max-height: 900px;
            display: flex; flex-direction: column;
        }

        .header {
            display: flex; justify-content: flex-start; align-items: flex-start;
            padding: 30px 50px 10px; position: relative; width: 100%;
        }
        
        .banner-container { 
            position: absolute; top: 25px; left: 0; width: 100%;
            text-align: center; display: flex; flex-direction: column; align-items: center; 
            z-index: 10; pointer-events: none;
        }
        
        .banner-shape {
            background-color: var(--blue); padding: 12px 60px;
            border: 4px solid var(--black); border-radius: 12px;
            box-shadow: 6px 6px 0px var(--black); display: inline-block;
        }
        
        .banner-text { 
            font-size: 28px; font-weight: 700; letter-spacing: 2px; color: var(--white); 
            text-shadow: 2px 2px 0px var(--black), -1px -1px 0px var(--black), 1px -1px 0px var(--black), -1px 1px 0px var(--black), 1px 1px 0px var(--black);
        }
        
        .banner-subtitle {
            background-color: var(--yellow); color: var(--black); 
            padding: 8px 40px; font-size: 16px; font-weight: 700;
            border: 3px solid var(--black); border-radius: 20px; 
            margin-top: -15px; text-transform: uppercase; letter-spacing: 1px;
            box-shadow: 4px 4px 0px var(--black); display: inline-block;
        }

        .slides-area {
            flex: 1; position: relative; margin: 30px 50px 0; perspective: 1200px;
            min-height: 0; 
        }

        .slide {
            position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            display: none;
        }
        
        .slide.active {
            display: block;
            animation: slideIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        }

        @keyframes slideIn {
            from { transform: translateY(50px) rotateX(-10deg); opacity: 0; }
            to { transform: translateY(0) rotateX(0); opacity: 1; }
        }

        .content-card {
            background-color: var(--white); border: 5px solid var(--black);
            border-radius: 20px; height: 100%; box-shadow: 10px 10px 0px var(--black);
            overflow-y: auto; overflow-x: hidden; scroll-behavior: smooth;
        }
        
        .content-card::-webkit-scrollbar { width: 14px; }
        .content-card::-webkit-scrollbar-track { background: var(--bg-light); border-left: 3px solid var(--black); border-radius: 0 15px 15px 0; }
        .content-card::-webkit-scrollbar-thumb { background: var(--pink); border: 3px solid var(--black); border-radius: 10px; }
        
        .inner-content { padding: 50px; padding-top: 60px; }
        
        .slide-title { font-size: 36px; margin-bottom: 25px; color: var(--black); border-bottom: 4px dashed var(--blue); padding-bottom: 15px; }
        .slide-text { font-size: 22px; line-height: 1.6; color: #333; }
        .slide-text p { margin-bottom: 20px; }
        .slide-text ul, .slide-text ol { margin-left: 30px; margin-bottom: 20px; }
        .slide-text li { margin-bottom: 10px; }

        .analogy-box {
            background-color: var(--yellow); border: 4px solid var(--black);
            border-radius: 15px; padding: 25px; margin: 30px 0;
            box-shadow: 6px 6px 0px var(--black); transform: rotate(-1deg);
            transition: transform 0.3s;
        }
        .analogy-box:hover { transform: rotate(1deg) scale(1.02); }
        .analogy-box h3 { color: var(--black); margin-bottom: 15px; font-size: 28px; display: flex; align-items: center; gap: 10px; }

        .info-box {
            background-color: var(--blue); border: 4px solid var(--black);
            border-radius: 15px; padding: 25px; margin: 30px 0; color: var(--white);
            box-shadow: 6px 6px 0px var(--black);
        }
        
        .info-box.pink { background-color: var(--pink); color: var(--black); }
        .info-box.green { background-color: var(--green); color: var(--black); }

        /* Quiz Styles */
        .quiz-container { margin-top: 30px; }
        .quiz-option {
            background-color: var(--white); border: 3px solid var(--black);
            border-radius: 12px; padding: 15px 20px; margin-bottom: 15px;
            cursor: pointer; font-size: 20px; font-weight: 600;
            transition: all 0.2s; box-shadow: 4px 4px 0px var(--black);
            display: flex; align-items: center;
        }
        .quiz-option:hover { background-color: var(--bg-light); transform: translateY(-2px); box-shadow: 6px 6px 0px var(--black); }
        .quiz-option.correct-ans { background-color: var(--green) !important; color: var(--black) !important; }
        .quiz-option.wrong-ans { background-color: var(--red) !important; color: var(--white) !important; }
        
        /* App Inventor Mockups - Designer */
        .ai2-phone {
            width: 320px; height: 500px; border: 12px solid var(--black);
            border-radius: 30px; background-color: white; margin: 20px auto;
            position: relative; overflow: hidden; box-shadow: 8px 8px 0px var(--black);
        }
        .ai2-phone-header {
            background-color: #eee; border-bottom: 2px solid #ccc; padding: 10px;
            font-size: 16px; font-weight: bold; text-align: center; color: #555;
        }
        .ai2-comp {
            margin: 10px; padding: 12px; font-size: 16px; border-radius: 5px;
            border: 2px solid #ccc; font-family: sans-serif;
        }
        .ai2-comp.btn { background-color: #ddd; text-align: center; font-weight: bold; cursor: pointer; box-shadow: 0 4px 0 #bbb; }
        .ai2-comp.btn:active { transform: translateY(4px); box-shadow: 0 0 0; }
        .ai2-comp.txt { background-color: white; color: #777; font-style: italic; }
        .ai2-comp.lbl { border: none; font-weight: bold; padding: 5px 10px; }

        /* App Inventor Mockups - Blocks */
        .ai2-workspace {
            background-color: #fff; border: 4px solid var(--black); border-radius: 12px;
            padding: 20px; margin: 20px 0; font-family: Arial, sans-serif;
            box-shadow: 6px 6px 0px var(--black); overflow-x: auto;
        }
        .blk {
            padding: 6px 12px; color: white; font-size: 15px; font-weight: bold;
            position: relative; box-shadow: inset -1px -1px 2px rgba(0,0,0,0.1), 2px 2px 4px rgba(0,0,0,0.2);
            text-shadow: 1px 1px 1px rgba(0,0,0,0.3); cursor: default; white-space: nowrap;
        }
        .blk-c {
            border-radius: 8px 8px 0 0; padding: 8px 12px;
            display: inline-flex; flex-direction: column; margin-bottom: 10px;
        }
        .blk-c-header { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; }
        .blk-c-body {
            margin-left: 20px; padding-left: 10px; min-height: 20px;
            border-left: 12px solid; display: flex; flex-direction: column; gap: 4px;
        }
        .blk-stack {
            border-radius: 4px; display: inline-flex; align-items: center; gap: 6px; margin-bottom: 2px;
        }
        .blk-val {
            border-radius: 14px; display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px;
        }
        .dropdown {
            background: rgba(255,255,255,0.9); color: #333; padding: 2px 8px; border-radius: 4px; font-size: 13px; text-shadow: none; display: inline-flex; align-items: center; border: 1px solid rgba(0,0,0,0.2);
        }
        .dropdown::after { content: ' ▼'; font-size: 9px; margin-left: 6px; color: #666; }

        /* Block Colors exactly matching AI2 */
        .c-event { background-color: #c4993a; border-left-color: #c4993a; }
        .c-proc { background-color: #744b91; border-left-color: #744b91; }
        .c-proc-call { background-color: #8c7abf; border-left-color: #8c7abf;}
        .c-set { background-color: #1e6d42; border-left-color: #1e6d42;}
        .c-get { background-color: #5da569; }
        .c-text { background-color: #b72b5d; }
        .c-math { background-color: #3b50ad; }
        .c-logic { background-color: #7bb23e; }
        .c-ctrl { background-color: #bfa346; border-left-color: #bfa346;}

        .nav-container {
            display: flex; justify-content: space-between; align-items: center;
            padding: 20px 50px 30px;
        }
        .nav-btn {
            background-color: var(--white); border: 4px solid var(--black);
            border-radius: 12px; padding: 15px 30px; font-size: 20px;
            font-weight: 700; font-family: 'Fredoka', sans-serif; cursor: pointer;
            box-shadow: 6px 6px 0px var(--black); transition: all 0.2s; text-transform: uppercase;
        }
        .nav-btn:hover:not(:disabled) { transform: translateY(-3px); box-shadow: 8px 8px 0px var(--black); background-color: var(--yellow); }
        .nav-btn:disabled { opacity: 0.5; cursor: not-allowed; box-shadow: 4px 4px 0px var(--black); }

        .counter-group { display: flex; flex-direction: column; align-items: center; gap: 8px; flex: 1; }
        .slide-counter { font-size: 24px; font-weight: 700; background-color: var(--white); padding: 8px 20px; border: 3px solid var(--black); border-radius: 20px; box-shadow: 4px 4px 0px var(--black); }
        .progress-bar-bg { width: 60%; height: 15px; background-color: var(--white); border: 3px solid var(--black); border-radius: 10px; overflow: hidden; }
        .progress-bar { height: 100%; background-color: var(--pink); width: 0%; transition: width 0.3s ease; }
    </style>
</head>
<body>

    <div class="app-container">
        
        <div class="header">
            <div class="banner-container">
                <div class="banner-shape">
                    <h1 class="banner-text" id="banner-title">APP INVENTOR</h1>
                </div>
                <div class="banner-subtitle" id="banner-subtitle">Materi</div>
            </div>
        </div>

        <div class="slides-area">
            {SLIDES_HTML}
        </div>

        <div class="nav-container">
            <button class="nav-btn" id="btn-prev" onclick="prevSlide()" disabled>◀ KEMBALI</button>
            <div class="counter-group">
                <span class="slide-counter"><span id="current-count">1</span> / <span id="total-count">X</span></span>
                <div class="progress-bar-bg"><div class="progress-bar" id="progress-bar"></div></div>
            </div>
            <button class="nav-btn" id="btn-next" onclick="nextSlide()">LANJUT ▶</button>
        </div>
    </div>

    <script>
        const slides = document.querySelectorAll('.slide');
        const btnPrev = document.getElementById('btn-prev');
        const btnNext = document.getElementById('btn-next');
        const counter = document.getElementById('current-count');
        const totalCounter = document.getElementById('total-count');
        const bar = document.getElementById('progress-bar');
        
        let currentSlide = 0;
        totalCounter.innerText = slides.length;

        function showSlide(index) {
            slides[currentSlide].classList.remove('active');
            currentSlide = index;
            slides[currentSlide].classList.add('active');
            
            const contentCard = slides[currentSlide].querySelector('.content-card');
            if(contentCard) contentCard.scrollTop = 0;
            
            btnPrev.disabled = currentSlide === 0;
            btnNext.disabled = currentSlide === slides.length - 1;
            
            counter.innerText = currentSlide + 1;
            bar.style.width = ((currentSlide + 1) / slides.length * 100) + '%';
            
            const activeSlide = slides[currentSlide];
            document.getElementById('banner-title').innerText = activeSlide.getAttribute('data-title') || 'APP INVENTOR';
            document.getElementById('banner-subtitle').innerText = activeSlide.getAttribute('data-subtitle') || 'Materi';
        }

        function nextSlide() { if (currentSlide < slides.length - 1) showSlide(currentSlide + 1); }
        function prevSlide() { if (currentSlide > 0) showSlide(currentSlide - 1); }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') { if (currentSlide < slides.length - 1) showSlide(currentSlide + 1); } 
            else if (e.key === 'ArrowLeft') { if (currentSlide > 0) showSlide(currentSlide - 1); }
        });

        function checkQuiz(element, isCorrect, feedbackText) {
            const container = element.parentElement;
            container.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('correct-ans', 'wrong-ans'));
            let fb = container.querySelector('.quiz-feedback');
            if(!fb) {
                fb = document.createElement('div');
                fb.className = 'quiz-feedback';
                fb.style.marginTop = '15px'; fb.style.padding = '12px'; fb.style.border = '3px solid var(--black)';
                fb.style.borderRadius = '8px'; fb.style.fontWeight = 'bold'; fb.style.fontSize = '16px';
                container.appendChild(fb);
            }
            fb.style.display = 'block';
            if(isCorrect) {
                element.classList.add('correct-ans');
                fb.innerHTML = '✅ BENAR! ' + feedbackText;
                fb.style.backgroundColor = 'var(--green)'; fb.style.color = 'var(--black)';
            } else {
                element.classList.add('wrong-ans');
                fb.innerHTML = '❌ SALAH! ' + feedbackText;
                fb.style.backgroundColor = 'var(--red)'; fb.style.color = 'var(--white)';
            }
        }

        showSlide(0);
    </script>
</body>
</html>
"""

def create_slide(title, subtitle, content, is_active=False):
    active_class = " active" if is_active else ""
    return f'''
            <div class="slide{active_class}" data-title="{title}" data-subtitle="{subtitle}">
                <div class="content-card">
                    <div class="inner-content">
                        <h2 class="slide-title">{subtitle}</h2>
                        <div class="slide-text">
{content}
                        </div>
                    </div>
                </div>
            </div>
'''

slides_data = []

# ==========================================
# SECTION 1: PROCEDURES
# ==========================================
slides_data.append(("PROCEDURES", "Selamat Datang! 🚀", """
<div style="text-align: center; margin-top: 50px;">
    <h1 style="font-size: 56px; margin-bottom: 20px; color: var(--black); text-shadow: 2px 2px 0px var(--pink);">Petualangan Kode Lanjutan!</h1>
    <p style="font-size: 28px; font-weight: 600; color: #555; margin-bottom: 40px;">Procedures, Modularisasi, Debugging, & Solusi Berdampak</p>
    <p>Di level ini, kita tidak hanya sekadar membuat aplikasi. Kita akan membuat aplikasi yang <strong>Profesional, Rapi, Bebas Bug, dan Bermanfaat!</strong></p>
</div>
"""))

slides_data.append(("PROCEDURES", "Apa itu Procedure? 📦", """
<p>Saat membuat aplikasi yang besar, kamu akan menyadari bahwa ada blok-blok kode yang <strong>sama persis</strong> dan digunakan berulang kali di tempat yang berbeda.</p>
<p>Menulis kode yang berulang-ulang (Copy-Paste) adalah kebiasaan <strong>BURUK</strong> seorang programmer karena:</p>
<ul>
    <li>Aplikasi menjadi lebih berat dan lambat.</li>
    <li>Membingungkan saat dibaca.</li>
    <li>Jika ada yang salah, kamu harus memperbaiki di banyak tempat sekaligus!</li>
</ul>
<p>Solusinya? Kita menggunakan <strong>PROCEDURE</strong> (atau fungsi).</p>
"""))

slides_data.append(("PROCEDURES", "Analogi: Resep Rahasia Koki 🧑‍🍳", """
<div class="analogy-box">
    <h3>👨‍🍳 Memasak Tanpa Procedure vs Dengan Procedure</h3>
    <p>Bayangkan kamu seorang koki yang jualan 3 menu: Pizza, Spaghetti, dan Lasagna. Semuanya butuh <em>Saus Tomat Spesial</em>.</p>
    <br>
    <p><strong>Tanpa Procedure:</strong> Di buku resep Pizza, kamu nulis cara bikin saus. Di buku Spaghetti, kamu nulis lagi cara bikin saus dari awal. Capek kan?</p>
    <br>
    <p><strong>Dengan Procedure:</strong> Kamu bikin 1 halaman khusus berjudul "Cara Bikin Saus Tomat". Lalu di resep Pizza, kamu cuma nulis: <em>"Panggil halaman Saus Tomat"</em>. Praktis!</p>
</div>
"""))

slides_data.append(("PROCEDURES", "Dua Jenis Procedure ✌️", """
<p>Dalam MIT App Inventor, Procedure ada di kategori blok berwarna <strong>UNGU (Procedures)</strong>. Ada dua jenis utama:</p>
<div class="info-box pink">
    <h3>1. Procedure "Do" (Melakukan Sesuatu) 🏃</h3>
    <p>Hanya menjalankan sederet perintah. Tidak memberikan hasil jawaban. Cocok untuk aksi seperti mengosongkan layar, mengubah warna, atau memutar suara.</p>
</div>
<div class="info-box green">
    <h3>2. Procedure "Result" (Menghasilkan Jawaban) 🎁</h3>
    <p>Melakukan proses perhitungan dan <strong>mengembalikan (return)</strong> sebuah hasil/data. Cocok untuk menghitung diskon, menghitung skor, dll.</p>
</div>
"""))

slides_data.append(("PROCEDURES", "Mari Kita Coba di Designer! 📱", """
<p>Mari kita buat aplikasi "Kalkulator Sederhana" yang menggunakan Procedure "Do" untuk mereset (mengosongkan) layar.</p>
<p>Desain aplikasimu di bagian Designer seperti ini:</p>
<div class="ai2-phone">
    <div class="ai2-phone-header">Kalkulator App</div>
    <div class="ai2-comp txt">TextBox1 (Hint: Angka 1)</div>
    <div class="ai2-comp txt">TextBox2 (Hint: Angka 2)</div>
    <div class="ai2-comp btn">btnHitung (Text: HITUNG)</div>
    <div class="ai2-comp lbl">lblHasil (Text: 0)</div>
    <div class="ai2-comp btn" style="background-color: #ffcccc;">btnReset (Text: RESET)</div>
</div>
"""))

slides_data.append(("PROCEDURES", "Membuat Procedure 'Do' 🧩", """
<p>Masuk ke bagian <strong>Blocks</strong>. Kita akan mendefinisikan sebuah procedure bernama <code>KosongkanLayar</code>.</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-proc">
        <div class="blk-c-header">
            <span style="font-size:16px;">⚙️</span> to <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">KosongkanLayar</span> do
        </div>
        <div class="blk-c-body">
            <div class="blk blk-stack c-set">
                set <span class="dropdown">TextBox1</span> . <span class="dropdown">Text</span> to 
                <div class="blk blk-val c-text">" "</div>
            </div>
            <div class="blk blk-stack c-set">
                set <span class="dropdown">TextBox2</span> . <span class="dropdown">Text</span> to 
                <div class="blk blk-val c-text">" "</div>
            </div>
            <div class="blk blk-stack c-set">
                set <span class="dropdown">lblHasil</span> . <span class="dropdown">Text</span> to 
                <div class="blk blk-val c-text">"0"</div>
            </div>
        </div>
    </div>
</div>
<p>Dengan membuat blok ini, kita baru <em>mengajari</em> aplikasi cara mereset layar. Blok ini belum berjalan sampai dia "dipanggil".</p>
"""))

slides_data.append(("PROCEDURES", "Memanggil Procedure 'Do' 📞", """
<p>Sekarang, bagaimana cara memanggilnya saat tombol Reset ditekan?</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-event">
        <div class="blk-c-header">
            when <span class="dropdown">btnReset</span> .Click
        </div>
        <div class="blk-c-body">
            <div class="blk blk-stack c-proc-call">
                call <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">KosongkanLayar</span>
            </div>
        </div>
    </div>
</div>
<p>Lihat kan betapa pendeknya kode di dalam tombol klik tersebut? Jika nanti kamu mau membersihkan layar di kejadian lain, kamu cukup pakai blok Procedure lagi!</p>
"""))

slides_data.append(("PROCEDURES", "Procedure 'Result' 🎁", """
<p>Sekarang kita coba jenis kedua: <strong>Procedure Result</strong>. Kita buat procedure untuk menghitung Total Belanja ditambah Pajak.</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-proc">
        <div class="blk-c-header">
            <span style="font-size:16px;">⚙️</span> to <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">HitungPajak</span> result
        </div>
        <div class="blk-c-body" style="padding-top:8px;">
            <div class="blk blk-val c-math">
                <div class="blk blk-val c-get"><span class="dropdown">TextBox1</span> . <span class="dropdown">Text</span></div> 
                + 
                <div class="blk blk-val c-math">1000</div>
            </div>
        </div>
    </div>
</div>
<p>Nah, procedure ini bisa kita masukkan ke dalam sebuah Text/Label, karena dia <em>menghasilkan</em> data berupa hasil dari penjumlahannya!</p>
"""))

slides_data.append(("PROCEDURES", "Memanggil Procedure 'Result' 📞", """
<p>Kita panggil procedure yang menghasilkan nilai tersebut dan menaruh hasilnya ke dalam Label.</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-event">
        <div class="blk-c-header">
            when <span class="dropdown">btnHitung</span> .Click
        </div>
        <div class="blk-c-body">
            <div class="blk blk-stack c-set">
                set <span class="dropdown">lblHasil</span> . <span class="dropdown">Text</span> to 
                <div class="blk blk-val c-proc-call">
                    call <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">HitungPajak</span>
                </div>
            </div>
        </div>
    </div>
</div>
<p>Karena <code>call HitungPajak</code> menghasilkan angka, dia bisa langsung dipasang ke dalam setelan teks sebagai nilai yang ditampilkan.</p>
"""))

slides_data.append(("PROCEDURES", "Mini Quiz 1 🧠", """
<p>Kenapa kita menggunakan Procedure di App Inventor?</p>
<div class="quiz-container">
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Procedure tidak ada hubungannya dengan warna layar.')">A. Agar warna aplikasi menjadi lebih bagus.</div>
    <div class="quiz-option" onclick="checkQuiz(this, true, 'Benar! Ini membuat kode kita tidak berulang-ulang, sehingga lebih ringan dan rapi.')">B. Untuk mengumpulkan beberapa perintah menjadi satu sehingga bisa dipakai berkali-kali tanpa mengulang.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Procedure tidak membuat handphone baterainya hemat secara langsung.')">C. Untuk membuat baterai HP menjadi hemat 100%.</div>
</div>
"""))

slides_data.append(("PROCEDURES", "Mini Project: Kalkulator Cerdas 🛠️", """
<div class="info-box">
    <h3>Tugas Pertama!</h3>
    <ol>
        <li>Buka proyek baru di MIT App Inventor.</li>
        <li>Buat UI dengan 2 TextBox, 1 Label, dan 2 Button (TAMBAH dan RESET).</li>
        <li>Buat Procedure "Do" dengan nama <code>ResetLayar</code> untuk mengosongkan TextBox dan Label.</li>
        <li>Buat Procedure "Result" dengan nama <code>JumlahkanAngka</code> yang menambahkan TextBox1 dan TextBox2.</li>
        <li>Panggil procedure tersebut di masing-masing tombol seperti contoh di slide sebelumnya!</li>
    </ol>
</div>
"""))

# ==========================================
# SECTION 2: OPTIMASI DAN MODULARISASI
# ==========================================
slides_data.append(("MODULARISASI", "Apa Itu Modularisasi? 🧹", """
<p>Selamat! Kamu sudah tahu cara membuat Procedure. Sekarang kita naik ke level berikutnya: <strong>Modularisasi Kode</strong>.</p>
<p>Modularisasi adalah proses memecah aplikasi yang besar menjadi "modul-modul" atau potongan kecil yang lebih fokus dan teratur.</p>
<div class="analogy-box pink">
    <h3>🗄️ Analogi: Merapikan Kamar Tidur</h3>
    <p>Pakaian, buku, dan mainan yang berserakan di kasur pasti bikin pusing. Solusinya?</p>
    <ul>
        <li>📦 Modul 1: Kotak Khusus Mainan</li>
        <li>📚 Modul 2: Rak Khusus Buku</li>
        <li>👕 Modul 3: Lemari Khusus Pakaian</li>
    </ul>
    <p>Di App Inventor, kotak/rak ini adalah kumpulan blok <em>Procedure</em>!</p>
</div>
"""))

slides_data.append(("MODULARISASI", "Optimasi: Sebelum vs Sesudah 🔄", """
<p>Mari kita lihat perbandingan blok kode yang "Berantakan" vs "Modular".</p>
<p><strong>Sebelum (Spaghetti Code):</strong></p>
<div class="ai2-workspace" style="opacity:0.8;">
    <div class="blk blk-c c-event">
        <div class="blk-c-header">when <span class="dropdown">btnHitung</span> .Click</div>
        <div class="blk-c-body">
           <div class="blk blk-c c-ctrl" style="margin-bottom:2px;">
               <div class="blk-c-header">if <div class="blk blk-val c-logic">...</div> then</div>
               <div class="blk-c-body">
                   <div class="blk blk-stack c-set">set <span class="dropdown">Label1</span> . <span class="dropdown">Text</span> to ...</div>
               </div>
           </div>
           <div class="blk blk-stack c-proc-call">call <span class="dropdown">Sound1</span> .Play</div>
        </div>
    </div>
</div>
<p>Semua ditaruh di satu tempat. Bayangkan kalau kodenya sampai 100 baris, pasti sangat rumit melacaknya! 🤯</p>
"""))

slides_data.append(("MODULARISASI", "Optimasi: Sebelum vs Sesudah 🔄", """
<p><strong>Sesudah (Modular):</strong></p>
<div class="ai2-workspace">
    <div class="blk blk-c c-event">
        <div class="blk-c-header">when <span class="dropdown">btnHitung</span> .Click</div>
        <div class="blk-c-body">
           <div class="blk blk-stack c-proc-call">call <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">CekDataKosong</span></div>
           <div class="blk blk-stack c-proc-call">call <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">HitungTotal</span></div>
           <div class="blk blk-stack c-proc-call">call <span class="dropdown" style="background:transparent; color:white; border:none; font-weight:bold;">MainkanSuara</span></div>
        </div>
    </div>
</div>
<p>Sangat rapi! Kita tahu persis urutannya. Dan setiap procedure menyembunyikan detail kerjanya (logika if dan perhitungan panjangnya) di tempat lain yang terpisah.</p>
"""))

slides_data.append(("MODULARISASI", "Flowchart Logic (Aliran Program) 🗺️", """
<p>Saat kodingan kita menjadi modular, <strong>Flowchart</strong> (diagram alir) aplikasi kita juga berubah menjadi lebih sederhana di level atas.</p>
<div style="background-color: var(--white); border: 4px solid var(--black); padding: 20px; border-radius: 12px; margin: 20px 0;">
    <h4 style="margin-bottom: 10px;">Contoh Flowchart Modular:</h4>
    <p><strong>[START]</strong> ➡️ User Klik Tombol ➡️ <strong>[Sub-Proses: Cek Input]</strong> ➡️ <strong>[Sub-Proses: Hitung]</strong> ➡️ <strong>[END]</strong></p>
</div>
<p>Setiap <em>Sub-Proses</em> dalam flowchart diwakili oleh sebuah Procedure di App Inventor.</p>
"""))

slides_data.append(("MODULARISASI", "Praktek UI Refactoring 🎨", """
<p>Terkadang, modularisasi juga berlaku untuk desain UI (User Interface) di layar Designer. Jika kamu punya banyak tombol berjejer...</p>
<div class="ai2-phone">
    <div class="ai2-phone-header">Horizontal Arrangement</div>
    <div style="display:flex; justify-content:space-around; margin-top:20px; background-color:#e1bee7; padding:10px; border:2px dashed #9c27b0;">
        <div class="ai2-comp btn" style="width:40%;">Btn1</div>
        <div class="ai2-comp btn" style="width:40%;">Btn2</div>
    </div>
    <p style="text-align:center; font-size:12px; margin-top:5px; color:#555;">Kotak ungu muda adalah Horizontal Arrangement</p>
</div>
<p>Kumpulkan mereka ke dalam <strong>Layout (Horizontal Arrangement)</strong> agar rapi dan mudah diatur posisinya secara kolektif.</p>
"""))

slides_data.append(("MODULARISASI", "Mini Quiz 3 🧠", """
<p>Mengapa memecah program menjadi modul-modul (procedure) kecil itu sangat membantu saat terjadi error (bug)?</p>
<div class="quiz-container">
    <div class="quiz-option" onclick="checkQuiz(this, true, 'Tepat! Kita bisa langsung fokus mencari error di modul yang bermasalah saja, tanpa membaca ribuan baris kode yang lain.')">A. Karena kita bisa mengisolasi masalah dan mencari error di satu "kotak" modul spesifik.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Modul tidak menghapus bug secara ajaib, tapi memudahkan kitalah yang mencarinya.')">B. Karena modul akan secara otomatis menghapus bug tanpa kita suruh.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Error tetap bisa terjadi jika logika kita salah.')">C. Karena jika memakai modul, App Inventor tidak akan pernah error.</div>
</div>
"""))

slides_data.append(("MODULARISASI", "Mini Project: Refactoring Game 🛠️", """
<div class="info-box">
    <h3>Tugas Refactoring (Merombak Kode)!</h3>
    <p>Buka kembali aplikasi yang pernah kamu buat sebelumnya (misalnya kalkulator atau game). Tugasmu:</p>
    <ol>
        <li>Cari blok kode yang panjang menumpuk di bawah blok "Button Click" atau "Timer".</li>
        <li>Buat Procedure baru dan pindahkan blok panjang tersebut ke dalamnya (beri nama yang sesuai).</li>
        <li>Ganti blok panjang tadi dengan blok "Call [NamaProcedure]".</li>
        <li>Pastikan aplikasinya masih berjalan normal! Jika masih normal, artinya kamu berhasil melakukan <strong>Refactoring & Modularisasi</strong>!</li>
    </ol>
</div>
"""))

# ==========================================
# SECTION 3: UJI COBA DAN DEBUGGING
# ==========================================
slides_data.append(("DEBUGGING", "Uji Coba & Debugging 🐛", """
<p>Kode yang sudah sangat rapi BUKAN berarti bebas dari masalah. Saat orang lain memakai aplikasimu, mereka mungkin melakukan hal yang tidak terduga!</p>
<div class="analogy-box" style="background-color: var(--blue); color: white;">
    <h3 style="color: white; text-shadow: 1px 1px 0px var(--black);">🧁 Analogi: Mencicipi Kue</h3>
    <p>Sebelum menjual kue buatanmu, kamu pasti akan mencicipinya dulu, kan?</p>
    <p>Jika kurang manis (Error/Bug), kamu akan menambahkan gula (Debugging). Proses memberikan kue ke teman untuk dicoba disebut <strong>User Testing</strong>!</p>
</div>
"""))

slides_data.append(("DEBUGGING", "Apa Itu Bug? 🕷️", """
<p><strong>Bug:</strong> Kesalahan, cacat, atau error dalam sebuah program yang membuatnya tidak berjalan semestinya atau bahkan Force Close (Crash).</p>
<p><strong>Debugging:</strong> Proses investigasi mencari sarang si "Bug" tersebut dan membasminya (memperbaikinya)!</p>
<p>Tahukah kamu? Kata "Bug" pertama kali populer saat ditemukan ada serangga sungguhan (ngengat) yang nyangkut di dalam mesin komputer raksasa di tahun 1947!</p>
"""))

slides_data.append(("DEBUGGING", "Penyebab Crash Paling Umum 💥", """
<p>Di App Inventor, aplikasimu sering tiba-tiba keluar (crash) karena masalah <strong>Tipe Data</strong>.</p>
<p>Contoh: Kamu punya TextBox untuk "Umur". Lalu pengguna usil mengetik huruf: <code>Sepuluh Tahun</code>.</p>
<p>Saat aplikasimu mencoba menjumlahkan <code>"Sepuluh Tahun" + 5</code>... BOOM! 💥 Matematika tidak bisa dicampur huruf, aplikasimu akan Crash menampilkan layar error warna merah!</p>
"""))

slides_data.append(("DEBUGGING", "Solusi: Validasi Data (Keamanan) 🛡️", """
<p>Untuk memastikan aplikasimu aman, kita harus menggunakan blok <strong>Logic (If/Then)</strong> dan blok <strong>is a number?</strong>.</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-ctrl">
        <div class="blk-c-header">
            if 
            <div class="blk blk-val c-logic">
                not <div class="blk blk-val c-math">is a number? <div class="blk blk-val c-get"><span class="dropdown">TextBox1</span> . <span class="dropdown">Text</span></div></div>
            </div>
            then
        </div>
        <div class="blk-c-body">
            <div class="blk blk-stack c-proc-call">
                call <span class="dropdown">Notifier1</span> .ShowAlert notice 
                <div class="blk blk-val c-text">"Harus Angka!"</div>
            </div>
        </div>
    </div>
</div>
<p>Ini adalah teknik perlindungan! Jika bukan angka, jangan dihitung. Tampilkan peringatan saja.</p>
"""))

slides_data.append(("DEBUGGING", "Praktek Testing di App Inventor 📱", """
<p>Selalu gunakan <strong>MIT AI2 Companion</strong> di HP-mu untuk mengetes. Jika terjadi error, HP-mu akan bergetar dan menampilkan pesan layar merah (Runtime Error).</p>
<div class="info-box pink">
    <h3>Fitur Rahasia: "Do It"</h3>
    <p>Jika kamu bingung blok mana yang salah, klik kanan pada sebuah blok, lalu pilih <strong>Do It</strong>.</p>
    <p>Ini akan mengetes HANYA blok tersebut tanpa harus memencet tombol di HP. Jawabannya akan muncul di layar komputer. Sangat ampuh untuk melacak bug!</p>
</div>
"""))

slides_data.append(("DEBUGGING", "Keamanan Data Pengguna (TinyDB) 💾", """
<p>Sebagai pembuat aplikasi, kamu wajib menjaga <strong>Keamanan Data</strong> penggunamu. Gunakan <code>TinyDB</code> untuk menyimpan data penting secara lokal di memori HP, bukan di server publik.</p>
<div class="ai2-workspace">
    <div class="blk blk-stack c-proc-call">
        call <span class="dropdown">TinyDB1</span> .StoreValue 
        tag <div class="blk blk-val c-text">"NamaPlayer"</div> 
        valueToStore <div class="blk blk-val c-get"><span class="dropdown">TextBox_Nama</span> . <span class="dropdown">Text</span></div>
    </div>
</div>
<p>Blok di atas akan mengamankan dan menyimpan input nama pemain agar tidak hilang walau aplikasinya ditutup secara paksa (crash).</p>
"""))

slides_data.append(("DEBUGGING", "Mengambil Data (TinyDB) 💾", """
<p>Cara memanggilnya kembali (misal saat Screen1 dibuka):</p>
<div class="ai2-workspace">
    <div class="blk blk-stack c-set" style="align-items:flex-start;">
        set <span class="dropdown">Label_Nama</span> . <span class="dropdown">Text</span> to 
        <div class="blk blk-val c-proc-call" style="flex-direction:column; align-items:flex-start; padding:10px;">
            call <span class="dropdown">TinyDB1</span> .GetValue <br>
            tag <div class="blk blk-val c-text">"NamaPlayer"</div> <br>
            valueIfTagNotThere <div class="blk blk-val c-text">"Tamu"</div>
        </div>
    </div>
</div>
<p>Ini memastikan bahwa jika sebelumnya tidak ada data yang tersimpan, aplikasinya tidak akan error dan secara otomatis memakai nama "Tamu".</p>
"""))

slides_data.append(("DEBUGGING", "Mini Quiz 4 🧠", """
<p>Apa fungsi dari blok TinyDB di App Inventor?</p>
<div class="quiz-container">
    <div class="quiz-option" onclick="checkQuiz(this, true, 'Benar! TinyDB menyimpan data secara aman di dalam HP pengguna (penyimpanan lokal).')">A. Menyimpan data kecil secara lokal di handphone pengguna sehingga data tidak hilang saat aplikasi ditutup.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! TinyDB tidak membagikan data ke Instagram.')">B. Membagikan foto otomatis ke Instagram pengguna.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! TinyDB bukan untuk membuat gambar.')">C. Menyimpan gambar ukuran besar yang dibuat dengan MS Paint.</div>
</div>
"""))

slides_data.append(("DEBUGGING", "Mini Project: Bug Hunter 🕵️‍♂️", """
<div class="info-box">
    <h3>Misi: Memburu Bug!</h3>
    <ol>
        <li>Buka aplikasi Kalkulatormu yang sebelumnya.</li>
        <li>Sambungkan ke MIT AI2 Companion.</li>
        <li>Coba masukkan teks (huruf) ke kolom input angka, lalu tekan tombol Hitung. (Pasti akan muncul pesan Error merah!)</li>
        <li>Tugasmu: Tambahkan komponen <strong>Notifier</strong>, lalu perbaiki blokmu dengan logika <code>if ... is a number?</code> yang sudah diajarkan.</li>
        <li>Tes lagi. Jika muncul peringatan rapi dari Notifier dan aplikasi tidak keluar, MISI BERHASIL!</li>
    </ol>
</div>
"""))

# ==========================================
# SECTION 4: PRESENTASI DAN REFLEKSI
# ==========================================
slides_data.append(("PRESENTASI", "Presentasi & Refleksi 🎤", """
<p>Kode yang ajaib akan percuma jika tidak ada yang tahu kegunaannya. Di tahap ini, kamu harus menunjukkan karya aplikasimu kepada dunia!</p>
<div class="analogy-box">
    <h3>🦸‍♂️ Analogi: Menceritakan Pahlawan Super</h3>
    <p>Jika kamu menggambar superhero, kamu pasti antusias bercerita: "Dia bisa terbang! Dia baik hati! Ini senjatanya!"</p>
    <p>Sama halnya dengan aplikasimu! Kamu harus presentasi: <strong>Apa fungsinya? Siapa penggunanya? Apa keunggulannya?</strong></p>
</div>
"""))

slides_data.append(("PRESENTASI", "Struktur Presentasi Aplikasi 📊", """
<p>Bingung mau ngomong apa saat presentasi? Ikuti 4 poin sakti ini:</p>
<ol>
    <li><strong>Latar Belakang:</strong> "Saya membuat aplikasi ini karena..."</li>
    <li><strong>Fitur Utama:</strong> "Di aplikasi ini pengguna bisa melakukan A, B, dan C..."</li>
    <li><strong>Demo Langsung (Live Demo):</strong> Tunjukkan HP-mu, atau buka Emulator/Mirroring, lalu praktekkan secara nyata cara kerjanya.</li>
    <li><strong>Tantangan Tersulit:</strong> Ceritakan bug paling lucu atau paling susah yang berhasil kamu atasi (Debugging).</li>
</ol>
"""))

slides_data.append(("PRESENTASI", "Persiapan Live Demo 📱", """
<p>Cara terbaik mempresentasikan aplikasi App Inventor adalah dengan <strong>Live Demo</strong> (Demo Langsung).</p>
<p>Ada dua cara yang bisa kamu pakai saat presentasi di depan kelas:</p>
<ul>
    <li><strong>Menggunakan Emulator:</strong> Tampilkan layar komputermu di proyektor, lalu jalankan Android Emulator bawaan MIT.</li>
    <li><strong>Mirroring Layar HP:</strong> Hubungkan aplikasimu di HP lewat AI2 Companion, lalu tampilkan layar HP-mu ke laptop menggunakan aplikasi Screen Mirroring.</li>
</ul>
<p>Peringatan: Selalu pastikan internet lancar agar demo tidak terhambat!</p>
"""))

slides_data.append(("PRESENTASI", "Menerima Umpan Balik (Feedback) 👂", """
<p>Saat presentasi, audiens (atau kelompok lain) pasti akan memberikan komentar. Ada yang memuji, ada yang mengkritik.</p>
<div class="info-box green">
    <h3>Umpan Balik adalah HADIAH! 🎁</h3>
    <p>Jika ada yang bilang: <em>"Tombol kembalinya terlalu kecil"</em> atau <em>"Warnanya bikin sakit mata"</em>, jangan marah!</p>
    <p>Catat masukannya. Aplikasi terbaik di dunia seperti Instagram dan TikTok juga selalu update dan berubah karena mendengarkan feedback dari penggunanya.</p>
</div>
"""))

slides_data.append(("PRESENTASI", "Mini Quiz 5 🧠", """
<p>Saat presentasi, kelompok lain memberi kritik: <em>"Aplikasi kalian keren, tapi teks petunjuknya sulit dibaca karena warnanya gelap."</em> Sikap yang tepat adalah:</p>
<div class="quiz-container">
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Kita tidak boleh beralasan menyalahkan mata orang lain.')">A. Menyuruh mereka memeriksa mata ke dokter karena teksnya sudah jelas.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Masukan yang baik tidak boleh diabaikan.')">B. Pura-pura mencatat, tapi tidak pernah memperbaiki aplikasinya.</div>
    <div class="quiz-option" onclick="checkQuiz(this, true, 'Benar! Feedback yang membangun harus diterima untuk menyempurnakan aplikasi.')">C. Berterima kasih atas feedback tersebut, dan berjanji akan mengubah warna teks menjadi lebih terang.</div>
</div>
"""))

slides_data.append(("PRESENTASI", "Mini Project: Demo Day! 🎪", """
<div class="info-box pink">
    <h3>Tugas: Latihan Pitching</h3>
    <ol>
        <li>Cari teman kelompokmu atau keluargamu.</li>
        <li>Siapkan aplikasi terakhir yang sudah kamu buat.</li>
        <li>Lakukan presentasi selama <strong>3 menit</strong> menggunakan struktur yang sudah diajarkan (Latar Belakang, Fitur, Live Demo, Tantangan).</li>
        <li>Minta 1 masukan jujur dari mereka! Catat masukan tersebut.</li>
    </ol>
</div>
"""))

# ==========================================
# SECTION 5: SOLUSI BERDAMPAK POSITIF
# ==========================================
slides_data.append(("SOLUSI DIGITAL", "Solusi yang Berdampak Positif 🌍", """
<p>Skill coding yang hebat tidak ada gunanya jika tidak dipakai untuk hal yang bermanfaat.</p>
<p>Programmer terbaik dunia bukan hanya pembuat game; mereka adalah <strong>Pemecah Masalah (Problem Solver)</strong>!</p>
<div class="analogy-box" style="background-color: var(--green);">
    <h3>🌉 Analogi: Membangun Jembatan</h3>
    <p>Jika warga desa susah menyeberang sungai, insinyur akan membuatkan jembatan.</p>
    <p>Jika teman sekelasmu susah membagi uang jajannya, kamu (Programmer) akan membuatkan <em>Aplikasi Catatan Keuangan</em>! Itu namanya solusi digital!</p>
</div>
"""))

slides_data.append(("SOLUSI DIGITAL", "Mengidentifikasi Masalah Nyata 👁️", """
<p>Semuanya dimulai dari rasa peduli (empati). Lihatlah lingkungan sekitarmu, rumahmu, dan sekolahmu.</p>
<ul>
    <li>Ibumu sering lupa jadwal menyiram tanaman? (Ide Aplikasi: Alarm Pengingat Tanaman)</li>
    <li>Teman sebangkumu boros? (Ide Aplikasi: Target Tabungan Harian)</li>
    <li>Adikmu malas belajar matematika? (Ide Aplikasi: Game Kuis Matematika Seru)</li>
</ul>
<p>Masalah yang nyata + Koding = Aplikasi yang Bermanfaat!</p>
"""))

slides_data.append(("SOLUSI DIGITAL", "UI Design Solusi Digital 🎨", """
<p>Mari rancang UI (User Interface) aplikasi Alarm Tanaman yang sederhana tapi efektif:</p>
<div class="ai2-phone">
    <div class="ai2-phone-header">Aplikasi Pengingat Siram</div>
    <div class="ai2-comp lbl" style="text-align:center;">Pilih Tanamanmu:</div>
    <div class="ai2-comp btn" style="background-color:#c8e6c9;">Tombol_Kaktus (1 Minggu)</div>
    <div class="ai2-comp btn" style="background-color:#f8bbd0;">Tombol_Anggrek (1 Hari)</div>
    <div class="ai2-comp txt" style="text-align:center; background:#eee; font-style:normal;">*Non-visible: Clock1, Sound1, Notifier1</div>
</div>
"""))

slides_data.append(("SOLUSI DIGITAL", "Mulai Koding Solusinya! 💻", """
<p>Jika pengguna menekan tombol Kaktus, kita mulai timernya (Clock):</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-event">
        <div class="blk-c-header">when <span class="dropdown">Tombol_Kaktus</span> .Click</div>
        <div class="blk-c-body">
            <div class="blk blk-stack c-set">
                set <span class="dropdown">Clock1</span> . <span class="dropdown">TimerInterval</span> to 
                <div class="blk blk-val c-math">604800000</div>
            </div>
            <div class="blk blk-stack c-set">
                set <span class="dropdown">Clock1</span> . <span class="dropdown">TimerEnabled</span> to 
                <div class="blk blk-val c-logic">true</div>
            </div>
            <div class="blk blk-stack c-proc-call">
                call <span class="dropdown">Notifier1</span> .ShowAlert notice 
                <div class="blk blk-val c-text">"Pengingat Aktif!"</div>
            </div>
        </div>
    </div>
</div>
"""))

slides_data.append(("SOLUSI DIGITAL", "Aksi Saat Waktu Habis ⏰", """
<p>Lalu, jika waktunya habis (Timer mencapai angka 0), aplikasi membunyikan alarm:</p>
<div class="ai2-workspace">
    <div class="blk blk-c c-event">
        <div class="blk-c-header">when <span class="dropdown">Clock1</span> .Timer</div>
        <div class="blk-c-body">
            <div class="blk blk-stack c-proc-call">
                call <span class="dropdown">Sound1</span> .Play
            </div>
            <div class="blk blk-stack c-proc-call" style="align-items:flex-start;">
                call <span class="dropdown">Notifier1</span> .ShowMessageDialog <br>
                message <div class="blk blk-val c-text">"Waktunya Siram Kaktus!"</div>
            </div>
        </div>
    </div>
</div>
"""))

slides_data.append(("SOLUSI DIGITAL", "Mini Quiz 6 🧠", """
<p>Manakah dari ide aplikasi di bawah ini yang merupakan "Solusi Digital Berdampak Positif" untuk memecahkan masalah di sekolah?</p>
<div class="quiz-container">
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Meskipun seru, ini bukan solusi pemecahan masalah sekolah.')">A. Game tebak-tebakan artis korea.</div>
    <div class="quiz-option" onclick="checkQuiz(this, true, 'Hebat! Ini adalah solusi digital yang punya manfaat dan memecahkan masalah nyata.')">B. Aplikasi pengingat jadwal piket kelas yang terhubung dengan notifikasi harian.</div>
    <div class="quiz-option" onclick="checkQuiz(this, false, 'Salah! Ini sama sekali tidak memecahkan masalah, malah membuang waktu.')">C. Aplikasi senter yang hanya hidup dan mati secara random.</div>
</div>
"""))

slides_data.append(("SOLUSI DIGITAL", "Mini Project Akhir: Ide Solusi! 💡", """
<div class="info-box pink">
    <h3>Tugas Akhir: Brainstorming Ide</h3>
    <p>Ambil kertas dan pulpen. Jawablah 3 pertanyaan ini:</p>
    <ol>
        <li>Sebutkan 1 masalah nyata yang ada di sekolah, rumah, atau lingkungan teman-temanmu.</li>
        <li>Tuliskan nama dan ide aplikasimu yang akan menjadi "Solusi Digital" dari masalah tersebut!</li>
        <li>Gambarkan 1 sketsa layar (UI Designer) dari aplikasimu, misal ada Tombol apa saja dan Label apa saja.</li>
    </ol>
    <p>Diskusikan ide hebatmu dengan teman sekelompokmu!</p>
</div>
"""))

slides_data.append(("KESIMPULAN", "Kamu Adalah Pembuat Perubahan! 🌟", """
<div style="text-align: center; margin-top: 30px;">
    <span style="font-size: 80px;">🚀💡🏆</span>
    <p style="font-size: 24px; font-weight: bold; margin-top: 20px; line-height: 1.6;">
        Dari belajar <strong>Procedures</strong>, melakukan <strong>Modularisasi</strong>, membasmi <strong>Bug</strong>, berani melakukan <strong>Presentasi</strong>, hingga menciptakan <strong>Solusi Berdampak</strong>...
    </p>
    <p style="font-size: 24px; margin-top: 20px; color: var(--red); font-weight: bold;">
        Kamu telah membuktikan dirimu bukan sekadar pengguna HP, tapi PENCIPTA TEKNOLOGI!
    </p>
    <p style="margin-top: 20px;">Selamat berkarya dengan kodingmu!</p>
</div>
"""))


html_slides = ""
for idx, (title, subtitle, content) in enumerate(slides_data):
    html_slides += create_slide(title, subtitle, content, is_active=(idx == 0))

final_html = html_template.replace("{SLIDES_HTML}", html_slides)

with open("/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Middleschool/grupD/slide_deck_part1.html", "w") as f:
    f.write(final_html)

print(f"Berhasil menggenerate {len(slides_data)} slides!")
