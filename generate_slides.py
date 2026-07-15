import os

html_template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MIT App Inventor SMP - Grup C</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --yellow: #FFE500; --blue: #00C6FF; --black: #1A1A1A;
            --white: #FFFFFF; --bg-light: #E8E8E8; --green: #00E676;
            --pink: #FF9DE2; --red: #FF0055; --orange: #FFA500;
        }
        body {
            background-color: var(--bg-light);
            background-image: radial-gradient(#bcbcbc 2px, transparent 2px);
            background-size: 30px 30px;
            font-family: 'Fredoka', sans-serif;
            color: var(--black); overflow: hidden; height: 100vh;
            display: flex; justify-content: center; align-items: center;
        }
        .app-container {
            position: relative; z-index: 10; width: 98vw; max-width: 1400px;
            height: 98vh; max-height: 900px; display: flex; flex-direction: column;
        }
        .header { display: flex; justify-content: flex-start; align-items: flex-start; padding: 30px 50px 10px; position: relative; width: 100%; }
        .banner-container { position: absolute; top: 25px; left: 0; width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; z-index: 10; pointer-events: none; }
        .banner-shape { background-color: var(--blue); padding: 12px 60px; border: 4px solid var(--black); border-radius: 12px; box-shadow: 6px 6px 0px var(--black); display: inline-block; }
        .banner-text { font-size: 28px; font-weight: 700; letter-spacing: 2px; color: var(--white); text-shadow: 2px 2px 0px var(--black), -1px -1px 0px var(--black), 1px -1px 0px var(--black), -1px 1px 0px var(--black), 1px 1px 0px var(--black); }
        .banner-subtitle { background-color: var(--yellow); color: var(--black); padding: 8px 40px; font-size: 16px; font-weight: 700; border: 3px solid var(--black); border-radius: 20px; margin-top: -15px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 4px 4px 0px var(--black); display: inline-block; }
        .slides-area { flex: 1; position: relative; margin: 30px 50px 0; perspective: 1200px; min-height: 0; }
        .slide { position: absolute; top: 0; left: 0; right: 0; bottom: 0; display: none; }
        .slide.active { display: block; animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
        @keyframes popIn { from { opacity: 0; transform: scale(0.95) translateY(20px); } to { opacity: 1; transform: scale(1) translateY(0); } }
        .content-card { background-color: var(--white); border: 4px solid var(--black); border-radius: 24px; padding: 40px 60px; box-shadow: 12px 12px 0px var(--black); width: 100%; height: 100%; overflow-y: auto; display: flex; position: relative; }
        .content-card::-webkit-scrollbar { width: 14px; }
        .content-card::-webkit-scrollbar-track { background: var(--bg-light); border-left: 3px solid var(--black); border-radius: 0 20px 20px 0; }
        .content-card::-webkit-scrollbar-thumb { background: var(--orange); border: 3px solid var(--black); border-radius: 10px; }
        .content-card::after { content: ''; position: absolute; top: -15px; right: 30px; width: 40px; height: 40px; background-color: var(--yellow); border: 3px solid var(--black); border-radius: 50%; box-shadow: 4px 4px 0px var(--black); z-index: 5; }
        .inner-content { max-width: 900px; margin: auto; width: 100%; position: relative; z-index: 10; }
        .slide-title { font-size: 32px; font-weight: 700; color: var(--black); margin-bottom: 25px; line-height: 1.3; background-color: var(--yellow); display: inline-block; padding: 10px 25px; border: 3px solid var(--black); border-radius: 12px; box-shadow: 5px 5px 0px var(--black); }
        .slide-text { font-size: 22px; line-height: 1.6; color: var(--black); font-weight: 600; }
        .slide-text p { margin-bottom: 20px; }
        .slide-text ul { padding-left: 40px; margin-bottom: 20px; }
        .slide-text li { margin-bottom: 15px; position: relative; list-style-type: none; }
        .slide-text li::before { content: '▶'; color: var(--orange); position: absolute; left: -35px; font-size: 20px; -webkit-text-stroke: 1px var(--black); }
        .slide-text strong { color: var(--black); background-color: var(--yellow); padding: 2px 12px; border: 3px solid var(--black); border-radius: 8px; font-weight: 700; box-shadow: 3px 3px 0px var(--black); display: inline-block; transform: rotate(-1deg); }
        .quote-box { background-color: var(--blue); border: 4px solid var(--black); padding: 20px 30px; border-radius: 16px; margin: 30px 0; font-weight: 700; color: var(--white); font-size: 24px; box-shadow: 8px 8px 0px var(--black); position: relative; text-shadow: 1px 1px 0px var(--black); }
        
        /* Realistic App Inventor Blocks CSS */
        .ai-block { display: inline-flex; font-family: 'Roboto', sans-serif; font-size: 15px; font-weight: 500; color: white; align-items: center; margin: 2px 0; box-shadow: 1px 1px 3px rgba(0,0,0,0.3); }
        .ai-event { background-color: #B7872A; flex-direction: column; align-items: stretch; border-radius: 8px 8px 0 0; padding: 2px 0 0 2px; }
        .ai-event-header { display: flex; align-items: center; gap: 6px; padding: 4px 8px; }
        .ai-event-do { padding: 0 8px 2px 8px; font-size: 13px; margin-top: -2px; }
        .ai-event-body { display: flex; flex-direction: column; align-items: flex-start; border-left: 16px solid #B7872A; padding-left: 2px; min-height: 24px; border-bottom: 8px solid #B7872A; border-bottom-left-radius: 6px; }
        .ai-control { background-color: #B18E35; flex-direction: column; align-items: stretch; border-radius: 8px 8px 0 0; padding: 2px 0 0 2px; }
        .ai-control > .ai-event-body { border-left: 16px solid #B18E35; border-bottom: 8px solid #B18E35; border-bottom-left-radius: 6px; }
        .ai-set { background-color: #13953B; border-radius: 8px; padding: 4px 8px; gap: 6px; }
        .ai-get { background-color: #E5801A; border-radius: 12px 4px 4px 12px; padding: 2px 8px; }
        .ai-math { background-color: #3F71B5; border-radius: 12px 4px 4px 12px; padding: 2px 8px; gap: 4px; }
        .ai-logic { background-color: #77C738; border-radius: 12px 4px 4px 12px; padding: 2px 8px; }
        .ai-text { background-color: #B32D5E; border-radius: 12px 4px 4px 12px; padding: 2px 8px; }
        .ai-join { background-color: #B32D5E; border-radius: 8px; padding: 4px 8px; gap: 6px; flex-direction: column; align-items: flex-start; }
        .ai-dropdown { background-color: rgba(0,0,0,0.15); padding: 1px 6px; border-radius: 4px; display: inline-flex; align-items: center; gap: 4px; }
        .ai-dropdown::after { content: "▼"; font-size: 8px; }
        .ai-mutator { background-color: #3F71B5; width: 18px; height: 18px; border-radius: 4px; display: inline-flex; align-items: center; justify-content: center; font-size: 14px; margin-right: 4px; border: 1px solid rgba(255,255,255,0.5); }
        .ai-mutator::before { content: "⚙"; }

        /* Real Flowchart Shapes */
        .fc-container { display: flex; flex-direction: column; align-items: center; margin: 15px 0; }
        .fc-row { display: flex; align-items: center; justify-content: center; }
        .fc-node { background-color: var(--white); border: 3px solid var(--black); padding: 10px 20px; font-size: 16px; font-weight: 700; text-align: center; box-shadow: 4px 4px 0px var(--black); position: relative; z-index: 2; min-width: 140px; color: var(--black); }
        .fc-oval { border-radius: 50px; background-color: #E3F2FD; }
        .fc-rect { border-radius: 8px; background-color: #FFF8E1; }
        .fc-diamond-wrapper { position: relative; width: 140px; height: 110px; margin: 5px 0; display: flex; align-items: center; justify-content: center; }
        .fc-diamond { position: absolute; width: 80px; height: 80px; background-color: #FCE4EC; border: 3px solid var(--black); transform: rotate(45deg); box-shadow: 4px 4px 0px var(--black); z-index: 1; }
        .fc-diamond-text { position: relative; z-index: 2; font-size: 15px; font-weight: 700; text-align: center; padding: 5px; max-width: 120px; color: var(--black); }
        .fc-arrow-down { width: 4px; height: 15px; background-color: var(--black); position: relative; margin: 2px 0; }
        .fc-arrow-down::after { content: ''; position: absolute; bottom: -5px; left: -6px; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 10px solid var(--black); }
        .fc-arrow-right { width: 25px; height: 4px; background-color: var(--black); position: relative; margin: 0 5px; }
        .fc-arrow-right::after { content: ''; position: absolute; right: -5px; top: -6px; border-top: 8px solid transparent; border-bottom: 8px solid transparent; border-left: 10px solid var(--black); }
        .fc-arrow-left { width: 25px; height: 4px; background-color: var(--black); position: relative; margin: 0 5px; }
        .fc-arrow-left::after { content: ''; position: absolute; left: -5px; top: -6px; border-top: 8px solid transparent; border-bottom: 8px solid transparent; border-right: 10px solid var(--black); }

        /* Phone Simulator (Designer View) */
        .phone-mockup { width: 300px; height: 500px; border: 12px solid var(--black); border-radius: 30px; background-color: #f0f0f0; position: relative; overflow: hidden; box-shadow: 10px 10px 0px var(--black); margin: 0 auto; display: flex; flex-direction: column; }
        .phone-mockup::before { content: ''; position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 100px; height: 20px; background: var(--black); border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; }
        .phone-screen { flex: 1; margin-top: 30px; padding: 15px; display: flex; flex-direction: column; gap: 10px; background: white; }
        .ui-comp { border: 2px solid var(--black); border-radius: 6px; padding: 10px; font-size: 16px; text-align: center; box-shadow: 3px 3px 0px var(--black); font-weight: bold; }
        .ui-btn { background-color: #E0E0E0; cursor: pointer; }
        .ui-txt { background-color: white; color: #888; text-align: left; font-weight: normal; font-style: italic; }
        .ui-lbl { border: none; box-shadow: none; text-align: left; padding: 5px; }
        
        .designer-container { display: flex; gap: 40px; align-items: center; justify-content: center; }
        .properties-panel { background: #fff; border: 4px solid var(--black); border-radius: 16px; padding: 20px; width: 350px; box-shadow: 6px 6px 0px var(--black); }
        .prop-item { display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 2px dashed #ccc; padding-bottom: 5px; }

        .nav-container { padding: 25px 50px 35px; display: flex; justify-content: space-between; align-items: center; min-height: 100px; }
        .nav-btn { background-color: var(--yellow); border: 4px solid var(--black); color: var(--black); padding: 12px 35px; border-radius: 30px; cursor: pointer; font-family: 'Fredoka', sans-serif; font-weight: 700; font-size: 18px; transition: all 0.1s; display: flex; align-items: center; gap: 8px; box-shadow: 6px 6px 0px var(--black); }
        .nav-btn:hover:not(:disabled) { transform: translate(-2px, -2px); box-shadow: 8px 8px 0px var(--black); background-color: #FFF033; }
        .nav-btn:active:not(:disabled) { transform: translate(4px, 4px); box-shadow: 2px 2px 0px var(--black); }
        .nav-btn:disabled { background-color: #e0e0e0; color: #888; border-color: #888; box-shadow: 2px 2px 0px #888; transform: translate(4px, 4px); cursor: not-allowed; }
        .counter-group { display: flex; flex-direction: column; align-items: center; gap: 10px; background: var(--white); padding: 12px 30px; border: 4px solid var(--black); border-radius: 24px; box-shadow: 6px 6px 0px var(--black); transform: rotate(1deg); }
        .slide-counter { font-size: 18px; font-weight: 700; color: var(--black); }
        .progress-bar-bg { width: 200px; height: 18px; background-color: var(--bg-light); border: 3px solid var(--black); border-radius: 10px; overflow: hidden; box-shadow: inset 2px 2px 0px rgba(0,0,0,0.1); }
        .progress-bar { height: 100%; background-color: var(--orange); border-right: 3px solid var(--black); transition: width 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .quiz-option { background-color: var(--white); border: 3px solid var(--black); border-radius: 12px; padding: 15px 20px; margin: 10px 0; font-weight: 700; cursor: pointer; box-shadow: 4px 4px 0px var(--black); transition: all 0.1s; display: flex; align-items: center; justify-content: space-between; }
        .quiz-option:hover { transform: translate(-2px, -2px); box-shadow: 6px 6px 0px var(--black); background-color: #f7f7f7; }
        .quiz-option.correct { background-color: var(--green); color: var(--black); }
        .quiz-option.wrong { background-color: var(--red); color: var(--white); }
        .mini-project-card { background-color: #FFF9C4; border: 4px dashed var(--orange); padding: 25px; border-radius: 16px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">
            <div class="banner-container">
                <div class="banner-shape">
                    <div id="banner-title" class="banner-text">MATERI APP INVENTOR</div>
                </div>
                <div id="banner-subtitle" class="banner-subtitle">SMP</div>
            </div>
        </div>
        <div class="slides-area">
            {slides_html}
        </div>
        <div class="nav-container">
            <button class="nav-btn" id="prev-btn" onclick="prevSlide()" disabled><span>◀</span> SEBELUMNYA</button>
            <div class="counter-group">
                <div class="slide-counter"><span id="current-slide">1</span> / <span id="total-slides">X</span></div>
                <div class="progress-bar-bg"><div class="progress-bar" id="progress-bar" style="width: 0%;"></div></div>
            </div>
            <button class="nav-btn" id="next-btn" onclick="nextSlide()">SELANJUTNYA <span>▶</span></button>
        </div>
    </div>
    <script>
        const slides = document.querySelectorAll('.slide');
        let currentSlideIndex = 0;
        document.getElementById('total-slides').textContent = slides.length;
        
        function updateUI() {
            slides.forEach((slide, index) => {
                if(index === currentSlideIndex) {
                    slide.classList.add('active');
                    const title = slide.getAttribute('data-title') || 'APP INVENTOR & KEUANGAN';
                    const subtitle = slide.getAttribute('data-subtitle') || 'SMP';
                    document.getElementById('banner-title').textContent = title;
                    document.getElementById('banner-subtitle').textContent = subtitle;
                } else {
                    slide.classList.remove('active');
                }
            });
            document.getElementById('current-slide').textContent = currentSlideIndex + 1;
            const progress = ((currentSlideIndex) / (slides.length - 1)) * 100;
            document.getElementById('progress-bar').style.width = progress + '%';
            document.getElementById('prev-btn').disabled = currentSlideIndex === 0;
            document.getElementById('next-btn').disabled = currentSlideIndex === slides.length - 1;
        }
        
        function nextSlide() { if (currentSlideIndex < slides.length - 1) { currentSlideIndex++; updateUI(); } }
        function prevSlide() { if (currentSlideIndex > 0) { currentSlideIndex--; updateUI(); } }
        
        function checkQuiz(button, isCorrect, explanation) {
            const parent = button.parentElement;
            const options = parent.querySelectorAll('.quiz-option');
            options.forEach(opt => opt.style.pointerEvents = 'none');
            if (isCorrect) button.classList.add('correct');
            else {
                button.classList.add('wrong');
                options.forEach(opt => { if(opt.getAttribute('data-correct') === 'true') opt.classList.add('correct'); });
            }
            let feedback = parent.querySelector('.quiz-feedback');
            if (!feedback) {
                feedback = document.createElement('div');
                feedback.className = 'quiz-feedback';
                feedback.style.marginTop = '15px'; feedback.style.padding = '12px';
                feedback.style.border = '3px solid #1A1A1A'; feedback.style.borderRadius = '8px';
                feedback.style.fontWeight = 'bold'; feedback.style.fontSize = '16px';
                parent.appendChild(feedback);
            }
            feedback.style.display = 'block';
            feedback.style.backgroundColor = isCorrect ? '#C8E6C9' : '#FFCDD2';
            feedback.innerHTML = (isCorrect ? '✅ BENAR! ' : '❌ SALAH! ') + explanation;
        }
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        });
        updateUI();
    </script>
</body>
</html>
"""

def slide_title(topic, subtitle, title_text, desc, color1, color2):
    return f"""
    <div class="slide" data-title="{topic}" data-subtitle="{subtitle}">
        <div class="content-card" style="align-items: center; justify-content: center; background: radial-gradient(circle, {color1} 0%, {color2} 100%); color: var(--white); border-color: var(--black);">
            <div class="inner-content" style="text-align: center;">
                <h1 style="font-size: 50px; font-weight: 700; margin-bottom: 15px; text-shadow: 4px 4px 0px var(--black); line-height: 1.2;">{title_text}</h1>
                <p style="font-size: 24px; font-weight: 600; text-shadow: 2px 2px 0px var(--black); color: var(--yellow); margin-bottom: 40px;">{desc}</p>
            </div>
        </div>
    </div>
    """

def slide_theory(topic, subtitle, title, text_html):
    return f"""
    <div class="slide" data-title="{topic}" data-subtitle="{subtitle}">
        <div class="content-card">
            <div class="inner-content">
                <h2 class="slide-title">{title}</h2>
                <div class="slide-text">
                    {text_html}
                </div>
            </div>
        </div>
    </div>
    """

def slide_quiz(topic, subtitle, title, question, options_list):
    opts_html = ""
    for opt in options_list:
        corr_attr = 'data-correct="true"' if opt['correct'] else ''
        opts_html += f"""
        <div class="quiz-option" {corr_attr} onclick="checkQuiz(this, {'true' if opt['correct'] else 'false'}, '{opt['exp']}')">
            <span>{opt['text']}</span>
        </div>
        """
    return slide_theory(topic, subtitle, title, f"<p>{question}</p><div style='margin-top: 20px;'>{opts_html}</div>")

def slide_designer(topic, subtitle, title, desc, phone_components, properties_list):
    comp_html = ""
    for c in phone_components:
        cls = "ui-comp "
        if c['type'] == 'btn': cls += "ui-btn"
        elif c['type'] == 'txt': cls += "ui-txt"
        elif c['type'] == 'lbl': cls += "ui-lbl"
        comp_html += f'<div class="{cls}">{c["text"]}</div>'
    prop_html = ""
    for p in properties_list:
        prop_html += f'<div class="prop-item"><strong>{p[0]}</strong><span>{p[1]}</span></div>'
    html = f"""
    <p>{desc}</p>
    <div class="designer-container" style="margin-top: 30px;">
        <div class="phone-mockup">
            <div class="phone-screen">
                <div style="background:#ddd; padding:5px; text-align:center; font-size:12px; font-weight:bold; border-radius:4px; margin-bottom:10px;">Screen1</div>
                {comp_html}
            </div>
        </div>
        <div class="properties-panel">
            <h3 style="margin-bottom:15px; border-bottom:3px solid var(--black); padding-bottom:5px;">⚙️ Properties</h3>
            {prop_html}
        </div>
    </div>
    """
    return slide_theory(topic, subtitle, title, html)

slides = []

################################################################################
# MATERI 1: LOGIKA PERCABANGAN GANDA DI DUNIA NYATA
################################################################################
topic1 = "PERCABANGAN GANDA"
sub1 = "Logika di Dunia Nyata"

slides.append(slide_title(topic1, sub1, "Pilihan di Kehidupan Nyata 🔀", "Mengenal Logika If-Then-Else dalam Kehidupan Sehari-hari", "var(--orange)", "#FF8C00"))

slides.append(slide_theory(topic1, sub1, "Ribuan Pilihan Setiap Hari 🤯", """
<p>Tahukah kamu bahwa otak kita membuat ribuan pilihan setiap harinya?</p>
<ul>
    <li>Jam berapa harus bangun?</li>
    <li>Baju apa yang harus dipakai?</li>
    <li>Makan ayam atau ikan?</li>
</ul>
<p>Proses memilih inilah yang dalam ilmu komputer disebut <strong>Logika Percabangan</strong>.</p>
"""))

slides.append(slide_theory(topic1, sub1, "Apa Itu Percabangan? 🤔", """
<p>Percabangan berarti menentukan jalan berdasarkan suatu <strong>kondisi</strong>.</p>
<div class="quote-box">"Jika (IF) hari ini hujan, maka (THEN) aku bawa payung." ☔</div>
<p>Jika kondisi "hujan" benar, maka instruksi "bawa payung" dilakukan. Ini adalah contoh percabangan tunggal.</p>
"""))

slides.append(slide_theory(topic1, sub1, "Kelemahan Kondisi Tunggal 🛑", """
<p>Bayangkan robot penjaga dengan perintah: <strong>"Jika ada tamu, bukakan pintu."</strong></p>
<p>Apa yang terjadi jika tamu itu adalah pencuri yang tidak dikenal? Robot tetap membukakan pintu!</p>
<p>Ini karena robot hanya punya satu kondisi tanpa jalan keluar alternatif.</p>
"""))

slides.append(slide_theory(topic1, sub1, "If-Then-Else (Ganda) 🔀", """
<p>Untuk membuat robot cerdas, kita gunakan <strong>Else (Selain itu)</strong>.</p>
<ul>
    <li><strong>Jika (If)</strong> tamu adalah orang yang dikenal, <strong>Maka (Then)</strong> bukakan pintu.</li>
    <li><strong>Selain itu (Else)</strong>, bunyikan alarm peringatan! 🚨</li>
</ul>
<p>Sekarang robot tahu harus berbuat apa di kedua situasi.</p>
"""))

slides.append(slide_theory(topic1, sub1, "Analogi: Lampu Lalu Lintas 🚥", """
<div style="background: #C8E6C9; padding: 20px; border: 3px solid var(--black); border-radius: 12px;">
    <strong>Logika Lampu Pejalan Kaki</strong><br><br>
    <strong>Jika (If)</strong> tombol ditekan oleh pejalan kaki,<br>
    <strong>Maka (Then)</strong> Nyalakan lampu merah untuk mobil.<br>
    <strong>Selain itu (Else)</strong>,<br>
    Biarkan lampu hijau menyala untuk mobil.
</div>
"""))

slides.append(slide_theory(topic1, sub1, "Analogi: Game Over 🎮", """
<div style="background: #FFF9C4; padding: 20px; border: 3px solid var(--black); border-radius: 12px;">
    <strong>Logika Nyawa Pemain</strong><br><br>
    <strong>Jika (If)</strong> nyawa pemain habis (0),<br>
    <strong>Maka (Then)</strong> Tampilkan layar "Game Over".<br>
    <strong>Selain itu (Else)</strong>,<br>
    Lanjutkan permainan seperti biasa.
</div>
"""))

slides.append(slide_theory(topic1, sub1, "Menggambar Logika (Flowchart) 🗺️", """
<p>Programmer menjelaskan logika ini ke dalam gambar yang disebut <strong>Flowchart</strong>.</p>
<ul>
    <li><strong>Oval:</strong> Mulai / Selesai (Start/End)</li>
    <li><strong>Persegi:</strong> Proses / Tindakan / Perintah</li>
    <li><strong>Belah Ketupat 🔷:</strong> Pertanyaan Kondisi (Bercabang 2 jalan: YA dan TIDAK)</li>
</ul>
"""))

slides.append(slide_theory(topic1, sub1, "Contoh Flowchart Hujan 🔷", """
<div class="fc-container">
    <div class="fc-node fc-oval">Mulai</div>
    <div class="fc-arrow-down"></div>
    <div class="fc-diamond-wrapper">
        <div class="fc-diamond"></div>
        <div class="fc-diamond-text">Apakah<br>Hujan?</div>
    </div>
    
    <div class="fc-row" style="margin-top: 5px;">
        <div style="text-align:right; margin-right: 5px; font-weight:bold; color:var(--red);">TIDAK</div>
        <div class="fc-arrow-left" style="transform: scaleX(-1);"></div>
        <div style="width: 100px;"></div>
        <div class="fc-arrow-right"></div>
        <div style="text-align:left; margin-left: 5px; font-weight:bold; color:var(--green);">YA</div>
    </div>
    
    <div class="fc-row" style="gap: 20px; margin-top: 5px;">
        <div class="fc-node fc-rect" style="background-color:#FFCDD2;">Pakai Topi</div>
        <div class="fc-node fc-rect" style="background-color:#C8E6C9;">Bawa Payung</div>
    </div>
</div>
"""))

slides.append(slide_quiz(topic1, sub1, "Kuis Flowchart", "Simbol apakah yang digunakan untuk membuat percabangan kondisi (IF) dalam flowchart?", [
    {"text": "A. Persegi", "correct": False, "exp": "Persegi digunakan untuk menuliskan proses."},
    {"text": "B. Belah Ketupat", "correct": True, "exp": "Tepat! Belah ketupat (Diamond) digunakan untuk percabangan (Ya/Tidak)."},
    {"text": "C. Lingkaran/Oval", "correct": False, "exp": "Oval untuk Start/End."}
]))

slides.append(slide_quiz(topic1, sub1, "Kuis Logika Dasar", "Apa fungsi dari blok ELSE?", [
    {"text": "A. Mengakhiri seluruh program", "correct": False, "exp": "Bukan, itu fungsi blok penutup."},
    {"text": "B. Menjalankan perintah jika IF bernilai SALAH", "correct": True, "exp": "Benar! Else adalah jalan alternatif/kedua."},
    {"text": "C. Menjalankan perintah berulang-ulang tanpa henti", "correct": False, "exp": "Itu fungsi Loop (Perulangan)."}
]))

slides.append(slide_theory(topic1, sub1, "Tugas Mandiri 🕵️‍♂️", """
<div class="mini-project-card">
    <h3>Detektif Flowchart!</h3>
    <p>1. Amati sistem lampu taman yang menyala malam hari.<br>
    2. Gambarkan flowchart <strong>If-Then-Else</strong> di kertasmu.<br>
    3. Tentukan pertanyaan di dalam Belah Ketupat (Misal: Apakah sudah gelap?).<br>
    4. Tentukan aksi jika YA, dan jika TIDAK.</p>
</div>
"""))

################################################################################
# MATERI 2: LOGIKA PERCABANGAN GANDA DI APP INVENTOR
################################################################################
topic2 = "APP INVENTOR"
sub2 = "Percabangan Blok"

slides.append(slide_title(topic2, sub2, "Logika di App Inventor 📱", "Praktik If-Then-Else dalam Pemrograman Blok", "var(--blue)", "#0056b3"))

slides.append(slide_theory(topic2, sub2, "Blok IF di App Inventor 🧩", """
<p>Di App Inventor, logika percabangan bersembunyi di laci <strong>Control</strong> yang berwarna coklat.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-control">
        <div class="ai-event-header">
            <span class="ai-mutator"></span> if <div class="ai-block ai-math"> </div>
        </div>
        <div class="ai-event-do">then</div>
        <div class="ai-event-body">
            
        </div>
    </div>
</div>
<p>Perhatikan bahwa bentuk blok ini seperti penjepit (bracket) yang bisa memeluk blok lainnya di dalam <code>then</code>.</p>
"""))

slides.append(slide_theory(topic2, sub2, "Memunculkan ELSE dengan Mutator ⚙️", """
<p>Awalnya, blok IF hanya punya "Then". Tidak ada "Else" sama sekali.</p>
<p>Untuk menambah Else, kamu HARUS mengklik ikon <strong>Roda Gigi (Mutator) ⚙️</strong> kecil warna biru di sudut kiri atas blok tersebut.</p>
<p>Sebuah pop-up kecil akan muncul, tarik blok <code>else</code> dan gabungkan ke blok <code>if</code> di dalam pop-up tersebut.</p>
"""))

slides.append(slide_theory(topic2, sub2, "Blok Lengkap If-Then-Else 🔀", """
<p>Setelah menarik blok else, blok aslimu akan berubah menjadi seperti ini:</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-control">
        <div class="ai-event-header">
            <span class="ai-mutator"></span> if <div class="ai-block ai-math"> </div>
        </div>
        <div class="ai-event-do">then</div>
        <div class="ai-event-body"></div>
        <div class="ai-event-do">else</div>
        <div class="ai-event-body"></div>
    </div>
</div>
<p>Sekarang kamu punya 2 tempat kosong untuk diisi aksi yang berbeda!</p>
"""))

slides.append(slide_designer(topic2, sub2, "UI Designer: Aplikasi Kelulusan 🎨", "Mari kita siapkan tampilan layar aplikasi di halaman Designer terlebih dahulu.", 
    [
        {"type": "lbl", "text": "Masukkan Nilai Ujian:"},
        {"type": "txt", "text": "Hint: 80"},
        {"type": "btn", "text": "CEK KELULUSAN"},
        {"type": "lbl", "text": "Hasil: ???", "color": "black"}
    ],
    [
        ("TextBox1", "Rename jadi txtNilai"),
        ("Button1", "Rename jadi btnCek"),
        ("Label2", "Rename jadi lblHasil")
    ]
))

slides.append(slide_theory(topic2, sub2, "Koding Blok Event (When Click) 👆", """
<p>Pertama, kita ambil blok kejadian (event) berwarna emas dari laci <strong>btnCek</strong>.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            
        </div>
    </div>
</div>
<p>Ini artinya: "Ketika tombol btnCek diklik, lakukan apa yang ada di dalam pelukanku".</p>
"""))

slides.append(slide_theory(topic2, sub2, "Menambahkan Logika & Kondisi 🧠", """
<p>Lalu kita masukkan blok IF dan kondisi matematika (biru) dari laci Math.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            <div class="ai-block ai-control">
                <div class="ai-event-header">
                    <span class="ai-mutator"></span> if <div class="ai-block ai-math"><div class="ai-dropdown">txtNilai</div> .Text &ge; 75</div>
                </div>
                <div class="ai-event-do">then</div>
                <div class="ai-event-body"></div>
                <div class="ai-event-do">else</div>
                <div class="ai-event-body"></div>
            </div>
        </div>
    </div>
</div>
"""))

slides.append(slide_theory(topic2, sub2, "Mengisi Aksi (Set Label Text) ✏️", """
<p>Terakhir, kita gunakan blok hijau tua dari laci lblHasil untuk mengubah teks sesuai kondisi!</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event" style="transform: scale(0.9); transform-origin: top left;">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            <div class="ai-block ai-control">
                <div class="ai-event-header">
                    <span class="ai-mutator"></span> if <div class="ai-block ai-math"><div class="ai-dropdown">txtNilai</div> .Text &ge; 75</div>
                </div>
                <div class="ai-event-do">then</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblHasil</div> .Text to <div class="ai-block ai-text">"Kamu Lulus!"</div>
                    </div>
                </div>
                <div class="ai-event-do">else</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblHasil</div> .Text to <div class="ai-block ai-text">"Belajar Lagi!"</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""))

slides.append(slide_quiz(topic2, sub2, "Kuis Fungsi Mutator", "Apa yang harus diklik untuk memunculkan pilihan ELSE?", [
    {"text": "A. Klik Kanan > Add Else", "correct": False, "exp": "Tidak ada klik kanan seperti itu."},
    {"text": "B. Ikon roda gigi biru di blok IF", "correct": True, "exp": "Tepat sekali! Roda gigi ini disebut Mutator."}
]))

slides.append(slide_theory(topic2, sub2, "Latihan Mandiri 🚀", """
<div class="mini-project-card">
    <h3>Aplikasi Cek Suhu</h3>
    <p>1. Buat aplikasi sederhana dengan input Suhu (TextBox).<br>
    2. <strong>If (Suhu > 30)</strong>, then set label jadi "Panas Sekali!"<br>
    3. <strong>Else</strong>, set label jadi "Cuaca Nyaman."<br>
    4. Test di Companion!</p>
</div>
"""))

################################################################################
# MATERI 3: LITERASI KEUANGAN - UANG DIGITAL
################################################################################
topic3 = "LITERASI KEUANGAN"
sub3 = "Uang Digital"

slides.append(slide_title(topic3, sub3, "Uang di Era Digital 💸", "Pendapatan, Pengeluaran, E-Wallet & QRIS", "var(--green)", "#00B259"))

slides.append(slide_theory(topic3, sub3, "Sejarah Uang Singkat ⏳", """
<p>Ribuan tahun lalu, orang bertukar barang langsung (Barter). Lalu muncul koin emas, kemudian uang kertas yang mudah dibawa.</p>
<p>Hari ini? Uang bahkan tidak terlihat bentuknya. Hanya berupa angka di sistem komputer!</p>
<p>Itulah yang disebut dengan Era Uang Digital.</p>
"""))

slides.append(slide_theory(topic3, sub3, "Pendapatan (Income) 📥", """
<p><strong>Pendapatan</strong> = Semua uang yang mengalir masuk ke kantongmu.</p>
<div class="quote-box" style="background-color: var(--blue);">Sebutkan 3 sumber pendapatanmu saat ini! 💰</div>
<p>Mungkin dari uang saku mingguan orang tua, amplop lebaran, atau hasil jualan stiker di kelas.</p>
"""))

slides.append(slide_theory(topic3, sub3, "Pengeluaran (Expense) 📤", """
<p><strong>Pengeluaran</strong> = Uang yang keluar untuk ditukar dengan barang/jasa.</p>
<p>Membeli makanan, bayar ongkos angkot, hingga top-up diamond game adalah pengeluaran.</p>
<p>Jika pengeluaran lebih besar dari pendapatan? Kamu akan berhutang!</p>
"""))

slides.append(slide_theory(topic3, sub3, "Tabungan (Savings) 🐷", """
<p><strong>Rumus Sakti: Tabungan = Pendapatan - Pengeluaran</strong></p>
<p>Tabungan berfungsi sebagai "benteng pertahanan" ketika ada hal darurat atau ketika kamu ingin membeli sesuatu yang mahal di masa depan tanpa harus meminjam uang.</p>
"""))

slides.append(slide_theory(topic3, sub3, "E-Wallet (Dompet Digital) 📱", """
<p>Sama seperti dompet kulit, tapi di dalam handphone.</p>
<div style="background-color: #E3F2FD; padding: 20px; border: 3px solid var(--black); border-radius: 12px; margin: 15px 0;">
    Aplikasi seperti Gopay, OVO, Dana, LinkAja bertugas menjaga "saldo" digital kita. Uang fisik kita diserahkan ke sistem mereka, ditukar dengan saldo digital.
</div>
"""))

slides.append(slide_theory(topic3, sub3, "QRIS Bikin Semua Mudah ⬛⬜", """
<p><strong>QRIS</strong> (Quick Response Code Indonesian Standard)</p>
<p>Di balik kotak-kotak hitam putih QRIS, tersimpan data rekening penjual. Saat kameramu memindainya, aplikasi e-wallet langsung tahu ke mana uang harus ditransfer dalam hitungan detik!</p>
"""))

slides.append(slide_quiz(topic3, sub3, "Kuis Digital 1", "Menerima transfer hadiah Rp 50.000 ke akun Dana disebut?", [
    {"text": "A. Pengeluaran digital", "correct": False, "exp": "Uang masuk, bukan keluar."},
    {"text": "B. Pendapatan digital", "correct": True, "exp": "Benar! Saldo e-wallet mu bertambah."}
]))

slides.append(slide_quiz(topic3, sub3, "Kuis Digital 2", "Scan QRIS di kasir minimarket termasuk tindakan...", [
    {"text": "A. Menabung digital", "correct": False, "exp": "Uangmu berkurang, bukan tersimpan."},
    {"text": "B. Pengeluaran digital", "correct": True, "exp": "Benar! Kamu membayar barang belanjaan."}
]))

slides.append(slide_theory(topic3, sub3, "Diskusi Kelompok 🗣️", """
<div class="mini-project-card">
    <h3>Bahaya Uang Digital?</h3>
    <p>Apakah uang digital membuat orang lebih boros?<br>
    Karena kita tidak melihat uang fisiknya berkurang, kadang kita terus men-scan QRIS sampai saldo habis.<br>
    Diskusikan dengan temanmu bagaimana cara mengatasinya!</p>
</div>
"""))

################################################################################
# MATERI 4: PERENCANAAN KEUANGAN PRIBADI
################################################################################
topic4 = "LITERASI KEUANGAN"
sub4 = "Needs vs Wants"

slides.append(slide_title(topic4, sub4, "Perencanaan Keuangan 📝", "Kebutuhan vs Keinginan", "var(--pink)", "#D81B60"))

slides.append(slide_theory(topic4, sub4, "Jebakan Batman Finansial 🦇", """
<p>Banyak orang kehabisan uang bukan karena pendapatannya kecil, tapi karena mereka tidak bisa membedakan mana yang <strong>BUTUH</strong> dan mana yang <strong>INGIN</strong>.</p>
<p>Ini adalah jebakan terbesar dalam mengelola uang saku!</p>
"""))

slides.append(slide_theory(topic4, sub4, "Kebutuhan (Needs) 🍞", """
<p>Kebutuhan (Needs) adalah hal yang <strong>HARUS</strong> dipenuhi.</p>
<ul>
    <li>Tanpanya, kita sakit (Makanan pokok)</li>
    <li>Tanpanya, kita dihukum (Seragam sekolah)</li>
    <li>Tanpanya, kita tidak bisa belajar (Alat tulis, Kuota tugas)</li>
</ul>
"""))

slides.append(slide_theory(topic4, sub4, "Keinginan (Wants) 🎮", """
<p>Keinginan (Wants) adalah hal yang dipengaruhi nafsu atau gengsi.</p>
<ul>
    <li>Kamu sudah punya sepatu yang bagus, tapi ingin beli sepatu merk Hypebeast.</li>
    <li>Kamu sudah minum air putih, tapi ingin beli Thai Tea Boba yang mahal.</li>
</ul>
<p>Keinginan tidak salah, tapi <strong>harus ditunda</strong> sampai uang lebih.</p>
"""))

slides.append(slide_theory(topic4, sub4, "Aturan 50-30-20 📊", """
<p>Salah satu cara membagi uang saku:</p>
<div style="background-color: #FFF9C4; padding: 20px; border: 3px solid var(--black); border-radius: 12px;">
    <strong>50%</strong> untuk Kebutuhan (Needs)<br>
    <strong>30%</strong> untuk Keinginan (Wants)<br>
    <strong>20%</strong> untuk Tabungan (Savings)
</div>
<p>Tentu saja porsi Tabungan bisa lebih besar jika kamu sedang hemat!</p>
"""))

slides.append(slide_theory(topic4, sub4, "Aturan Tunggu 24 Jam 🛑", """
<div class="quote-box" style="background-color: var(--black); color: var(--pink);">Jangan beli langsung! Tunggu 1 hari!</div>
<p>Seringkali, keinginan membeli (impulsive buying) akan hilang setelah kita tidur satu malam.</p>
<p>Jika besoknya kamu merasa tidak butuh lagi, selamat! Kamu baru saja menghemat uang.</p>
"""))

slides.append(slide_quiz(topic4, sub4, "Kuis Prioritas 1", "Membeli paket internet agar bisa mengirim tugas presentasi besok pagi termasuk...", [
    {"text": "A. Kebutuhan (Needs)", "correct": True, "exp": "Benar! Ini wajib dipenuhi untuk kewajiban sekolahmu."},
    {"text": "B. Keinginan (Wants)", "correct": False, "exp": "Bukan, ini berhubungan dengan kelancaran sekolah, bukan sekadar hiburan."}
]))

slides.append(slide_quiz(topic4, sub4, "Kuis Prioritas 2", "Membeli gacha/top-up diamond agar karakter game-mu lebih keren adalah...", [
    {"text": "A. Kebutuhan mutlak", "correct": False, "exp": "Salah! Hidupmu tetap aman tanpa diamond game."},
    {"text": "B. Keinginan (Wants)", "correct": True, "exp": "Tepat! Ini murni untuk kesenangan dan gengsi sesaat."}
]))

slides.append(slide_theory(topic4, sub4, "Latihan: Buat Budgetmu 📝", """
<div class="mini-project-card">
    <h3>Jadilah Menteri Keuangan!</h3>
    <p>1. Anggap uang sakumu minggu ini Rp 50.000.<br>
    2. Tulis di kertas: 2 Needs (Kebutuhan) yang pasti dibeli.<br>
    3. Tulis 1 Wants (Keinginan) yang ingin dibeli jika sisa uang cukup.<br>
    4. Tulis alokasi Tabungan! (Minimal Rp 5.000)</p>
</div>
"""))

################################################################################
# MATERI 5: APP INVENTOR + FINANSIAL
################################################################################
topic5 = "APP INVENTOR + FINANSIAL"
sub5 = "Aplikasi Kalkulator Keuangan"

slides.append(slide_title(topic5, sub5, "Koding untuk Uangmu! 💻💸", "Membuat Kalkulator Tabungan", "var(--black)", "#333333"))

slides.append(slide_theory(topic5, sub5, "Mengapa Komputer & Uang? 🤖", """
<p>Manusia sering lapar mata dan salah hitung. Komputer tidak pernah bohong!</p>
<p>Kita bisa menggabungkan <strong>Logika IF</strong> dengan <strong>Matematika Keuangan</strong> di App Inventor untuk menjaga kita tetap disiplin berhemat.</p>
"""))

slides.append(slide_designer(topic5, sub5, "UI Designer: Aplikasi Nabung 🎨", "Kita buat desain Kalkulator Target Tabungan.", 
    [
        {"type": "lbl", "text": "Harga Barang Impian (Rp):"},
        {"type": "txt", "text": "Misal: 50000"},
        {"type": "lbl", "text": "Tabungan Saat Ini (Rp):"},
        {"type": "txt", "text": "Misal: 20000"},
        {"type": "btn", "text": "CEK BISA BELI?"},
        {"type": "lbl", "text": "Status: ???", "color": "black"}
    ],
    [
        ("TextBox_Harga", "Input tipe: Numbers Only"),
        ("TextBox_Tabungan", "Input tipe: Numbers Only"),
        ("Label_Status", "Font: Bold, Size: 18")
    ]
))

slides.append(slide_theory(topic5, sub5, "Menyusun Blok Logika Keuangan 🧩", """
<p>Gunakan operasi perbandingan (&ge;) dari laci Math.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-event" style="transform: scale(0.9); transform-origin: top left;">
        <div class="ai-event-header">
            when <div class="ai-dropdown">btnCek</div> .Click
        </div>
        <div class="ai-event-do">do</div>
        <div class="ai-event-body">
            <div class="ai-block ai-control">
                <div class="ai-event-header">
                    <span class="ai-mutator"></span> if <div class="ai-block ai-math"><div class="ai-dropdown">txtTabungan</div> .Text &ge; <div class="ai-dropdown">txtHarga</div> .Text</div>
                </div>
                <div class="ai-event-do">then</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblStatus</div> .Text to <div class="ai-block ai-text">"Uang Cukup! Boleh Beli!"</div>
                    </div>
                </div>
                <div class="ai-event-do">else</div>
                <div class="ai-event-body">
                    <div class="ai-block ai-set">
                        set <div class="ai-dropdown">lblStatus</div> .Text to <div class="ai-block ai-text">"Nabung lagi ya!"</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""))

slides.append(slide_theory(topic5, sub5, "Menghitung Kekurangan (-) ➖", """
<p>Jika uang tidak cukup (Else), aplikasinya bisa menghitung kekurangan!</p>
<p>Ambil blok <strong>Math Minus (-)</strong>.</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-math">
        <div class="ai-dropdown">txtHarga</div> .Text - <div class="ai-dropdown">txtTabungan</div> .Text
    </div>
</div>
<p>Ini adalah logika pengurangan dasar: Harga Barang dikurangi Tabungan kita.</p>
"""))

slides.append(slide_theory(topic5, sub5, "Blok Join (Menggabung Teks) 🔗", """
<p>Untuk membuat kalimat seperti "Kurang Rp 30000", kita butuh blok <code>join</code> dari laci Text (Pink/Merah Muda).</p>
<div style="margin: 20px 0;">
    <div class="ai-block ai-join" style="background-color: #C2185B;">
        <div style="display:flex; gap:5px; align-items:center;">
            <div style="margin-right:5px;">join</div>
            <div class="ai-block ai-text">"Kurang Rp "</div>
        </div>
        <div style="display:flex; gap:5px; align-items:center; margin-left:30px;">
            <div class="ai-block ai-math"> <div class="ai-dropdown">txtHarga</div> .Text - <div class="ai-dropdown">txtTabungan</div> .Text</div>
        </div>
    </div>
</div>
<p>Masukkan hasil Join ini ke <code>set Label_Status.Text to</code> pada blok Else!</p>
"""))

slides.append(slide_quiz(topic5, sub5, "Kuis Blok Keuangan", "Blok warna apa yang digunakan untuk operasi pengurangan (-)?", [
    {"text": "A. Coklat/Emas (Control)", "correct": False, "exp": "Control untuk logika If-Else."},
    {"text": "B. Biru (Math)", "correct": True, "exp": "Tepat! Semua perhitungan hitung-hitungan ada di laci Math biru."},
    {"text": "C. Merah Muda (Text)", "correct": False, "exp": "Text untuk memanipulasi kata/kalimat."}
]))

slides.append(slide_theory(topic5, sub5, "Mini Project Final 🏆", """
<div class="mini-project-card">
    <h3>Aplikasi Target Tabungan!</h3>
    <p>Praktik di MIT App Inventor sekarang!</p>
    <ol>
        <li>Buat desain UI (TextBox Tabungan, TextBox Harga, Tombol Cek).</li>
        <li>Susun blok If-Then-Else membandingkan nilai keduanya.</li>
        <li>Tambahkan blok Math dan Join di bagian Else agar aplikasi memberi tahu berapa selisih kekurangannya.</li>
        <li>Jalankan di HP dengan MIT Companion dan tunjukkan hasilnya!</li>
    </ol>
</div>
"""))

# Generate final HTML string
slides_html_str = "\n".join(slides)
final_html = html_template.replace('{slides_html}', slides_html_str)

with open('/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Middleschool/grupC/slide_deck_grupC.html', 'w') as f:
    f.write(final_html)

print(f"Generated {len(slides)} refined slides successfully!")
