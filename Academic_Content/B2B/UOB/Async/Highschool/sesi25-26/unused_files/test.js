    const courseData = {
      1: {
        kicker: "Checkpoint 01 · Mulai di sini",
        title: "Bagaimana Program Bisa Memilih?",
        duration: "Video 1 · Konsep dasar",
        videoId: "MLgrQoRo2oo",
        quizzes: []
      },
      2: {
        kicker: "Checkpoint 02 · Saatnya praktik",
        title: "Menulis Conditional di Python",
        duration: "Video 2 · Praktik kode",
        videoId: "-hYK440Vlr8",
        quizzes: [
          {
            time: 300,
            shown: false,
            resume: true,
            resumeTime: 306,
            questions: [
              {
                question: "Syarat dalam pemrograman yang bernilai benar disebut dengan True.",
                answer: true,
                explanation: "Benar. True berarti kondisi tersebut terpenuhi."
              },
              {
                question: "Keputusan dalam pemrograman mirip seperti kita memilih tindakan di kehidupan nyata berdasarkan suatu syarat.",
                answer: true,
                explanation: "Benar. Keduanya memakai pola: jika syarat terpenuhi, lakukan aksi."
              },
              {
                question: "Komputer akan tetap menjalankan perintah di dalam 'if' walaupun syaratnya bernilai False.",
                answer: false,
                explanation: "Salah. Jika syarat bernilai False, perintah di dalam blok if akan dilewati."
              },
              {
                question: "Dalam membuat syarat (kondisi), kita tidak bisa membandingkan angka.",
                answer: false,
                explanation: "Salah. Kita bisa menggunakan operator perbandingan seperti >, <, ==, dll pada angka."
              }
            ]
          },
          {
            time: 617,
            shown: false,
            resume: true,
            resumeTime: 620,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Tebak Output 1 🕵️‍♂️</h2>
                  <div class="slide-text">
                  <p>Perhatikan kode berikut:</p>
                  <div class="code-block">
<span class="keyword">weather</span> <span class="operator">=</span> <span class="string">"hujan"</span><br><br>
<span class="keyword">if</span> weather <span class="operator">==</span> <span class="string">"cerah"</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Main bola di luar!"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Main game di rumah."</span>)
                  </div>
                  <p>Apa yang akan dicetak oleh program di atas?</p>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkGuess(this, false, 'Karena <code>weather</code> adalah <code>&quot;hujan&quot;</code>, maka kondisi <code>if</code> bernilai <b>False</b>, jadi program pindah ke <code>else</code>.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Main bola di luar!</button>
                      <button onclick="checkGuess(this, true, 'Karena <code>weather</code> adalah <code>&quot;hujan&quot;</code>, maka kondisi <code>if</code> bernilai <b>False</b>, jadi program pindah ke <code>else</code>.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Main game di rumah.</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              },
              {
                html: `
                  <h2 class="slide-title">Tebak Output 2 🕵️‍♂️</h2>
                  <div class="slide-text">
                  <p>Perhatikan kode berikut:</p>
                  <div class="code-block">
<span class="keyword">score</span> <span class="operator">=</span> <span class="string">80</span><br><br>
<span class="keyword">if</span> score <span class="operator">&gt;</span> <span class="string">75</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Kamu Lulus!"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Coba lagi tahun depan."</span>)
                  </div>
                  <p>Apa yang akan dicetak oleh program di atas?</p>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkGuess(this, true, 'Karena <code>80</code> memang lebih besar dari <code>75</code>, maka kondisi bernilai <b>True</b>.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Kamu Lulus!</button>
                      <button onclick="checkGuess(this, false, 'Karena <code>80</code> memang lebih besar dari <code>75</code>, maka kondisi bernilai <b>True</b>.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Coba lagi tahun depan.</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              },
              {
                html: `
                  <h2 class="slide-title">Tebak Output 3 🕵️‍♂️</h2>
                  <div class="slide-text">
                  <p>Perhatikan kode berikut:</p>
                  <div class="code-block">
<span class="keyword">is_hungry</span> <span class="operator">=</span> <span class="keyword">False</span><br><br>
<span class="keyword">if</span> is_hungry <span class="operator">==</span> <span class="keyword">True</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Waktunya makan!"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Lanjut belajar."</span>)
                  </div>
                  <p>Apa yang akan dicetak oleh program di atas?</p>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkGuess(this, false, 'Karena <code>is_hungry</code> adalah <b>False</b>, pengecekan <code>False == True</code> bernilai salah, jadi pindah ke <code>else</code>.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Waktunya makan!</button>
                      <button onclick="checkGuess(this, true, 'Karena <code>is_hungry</code> adalah <b>False</b>, pengecekan <code>False == True</code> bernilai salah, jadi pindah ke <code>else</code>.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Lanjut belajar.</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          },
          {
            time: 617,
            shown: false,
            resume: false,
            questions: [
              {
                question: "Multi-branch decision adalah keputusan dengan banyak cabang pilihan yang dapat dieksekusi bersamaan.",
                answer: false,
                explanation: "Salah. Program hanya akan menjalankan satu cabang yang kondisinya pertama kali terpenuhi, tidak bersamaan."
              },
              {
                question: "Dalam Python, kita dapat membuat percabangan yang lebih dari dua jalan menggunakan kata kunci 'elif'.",
                answer: true,
                explanation: "Benar. 'elif' (else if) memungkinkan kita mengecek kondisi baru jika kondisi sebelumnya bernilai salah."
              },
              {
                question: "Urutan kondisi pada if-elif sangat penting karena Python membaca dari atas ke bawah dan berhenti pada kondisi pertama yang benar.",
                answer: true,
                explanation: "Benar. Python akan mengeksekusi blok kode dari kondisi pertama yang True dan mengabaikan pengecekan di bawahnya."
              }
            ]
          }
        ]
      },
      3: {
        kicker: "Checkpoint 03 · Logika Tambahan",
        title: "Multi Branch Conditionals",
        duration: "Video 3 · Cabang & Operator",
        videoId: "_jm2p3pstrM",
        quizzes: [
          {
            time: 594,
            shown: false,
            resume: false,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan 1: Lengkapi Kode! 🧩</h2>
                  <div class="slide-text">
                  <p>Instruksi: Program mengecek kategori usia. Jika usia 18 tahun ke atas dianggap "Dewasa", kalau di bawah 18 tahun masih "Biasa aja".</p>
                  <p>Lengkapi bagian yang kosong dengan mengetik <strong>keyword percabangan</strong> dan <strong>kondisi pengecekannya</strong> secara manual!</p>
                  <div class="code-block" style="font-size: 16px;">
<span class="keyword">age</span> <span class="operator">=</span> <span class="string">15</span><br><br>
<span class="keyword">if</span> age <span class="operator">&gt;=</span> <span class="string">18</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Dewasa"</span>)<br>
<input type="text" id="mb1-kw" placeholder="keyword" style="width: 90px; font-family: monospace; font-size: 16px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> <input type="text" id="mb1-cond" placeholder="kondisinya..." style="width: 150px; font-family: monospace; font-size: 16px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Biasa aja"</span>)
                  </div>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkMB1QGuess(document.getElementById('mb1-kw').value, document.getElementById('mb1-cond').value, this, 'Tepat Sekali! Kita memakai <code>elif</code> untuk mengecek kondisi <code>age &lt; 18</code>.')" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Cek Kode Saya!</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              },
              {
                html: `
                  <h2 class="slide-title">Latihan 2: Perbaiki Bug! 🐛</h2>
                  <div class="slide-text">
                  <p>Ada bug (kesalahan) di kode ini! Siswa dengan nilai 95 harusnya dapat "A", tapi dia malah dapat "B" karena urutannya salah.</p>
                  <p>Ketik langsung angka yang benar pada kotak untuk memperbaiki urutan prioritas pengecekannya!</p>
                  <div class="code-block" style="font-size: 16px;">
<span class="keyword">score</span> <span class="operator">=</span> <span class="string">95</span><br><br>
<span class="keyword">if</span> score <span class="operator">&gt;=</span> <input type="text" id="mb2-val1" placeholder="angka" style="width: 80px; font-family: monospace; font-size: 16px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"A"</span>)<br>
<span class="keyword">elif</span> score <span class="operator">&gt;=</span> <input type="text" id="mb2-val2" placeholder="angka" style="width: 80px; font-family: monospace; font-size: 16px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"B"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"C"</span>)
                  </div>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px; flex-wrap: wrap;">
                      <button onclick="checkMB2QGuess(document.getElementById('mb2-val1').value, document.getElementById('mb2-val2').value, this, 'Mantap! Syarat yang paling sulit (&gt;= 90) harus ditaruh paling atas agar dicek lebih dulu.')" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Cek Kode Saya!</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              },
              {
                html: `
                  <h2 class="slide-title">Latihan 3: Tebak Output 🕵️‍♂️</h2>
                  <div class="slide-text">
                  <p>Perhatikan baik-baik kode berikut:</p>
                  <div class="code-block">
<span class="keyword">hari</span> <span class="operator">=</span> <span class="string">"Rabu"</span><br><br>
<span class="keyword">if</span> hari <span class="operator">==</span> <span class="string">"Sabtu"</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Bermain"</span>)<br>
<span class="keyword">elif</span> hari <span class="operator">==</span> <span class="string">"Minggu"</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Jalan-jalan"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Sekolah"</span>)
                  </div>
                  <p>Menurutmu apa yang akan dicetak di layar?</p>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkGuess(this, false, 'Salah! Hari yang dicek bukan Sabtu.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Bermain</button>
                      <button onclick="checkGuess(this, false, 'Salah! Hari yang dicek bukan Minggu.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Jalan-jalan</button>
                      <button onclick="checkGuess(this, true, 'Benar! Karena bukan Sabtu dan bukan Minggu, program akan menjalankan <code>else</code> dan mencetak Sekolah.')" style="background-color: #FFFFFF; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Sekolah</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          }
        ]
      },
      4: {
        kicker: "Checkpoint 04 · Bersarang",
        title: "Nested Conditionals",
        duration: "Video 4 · Kondisi dalam kondisi",
        videoId: "_e3hs1nWuME",
        quizzes: [
          {
            time: 649,
            shown: false,
            resume: true,
            resumeTime: 652,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan: Kurung Penyelamat! 🛡️</h2>
                  <div class="slide-text">
                  <p><strong>Skenario Game Online:</strong> Seorang pemain bisa login jika password-nya benar <strong>DAN</strong> (dia adalah admin <strong>ATAU</strong> pemain premium).</p>
                  <ul>
                      <li><strong>Instruksi:</strong> Tuliskan logika yang tepat di dalam kotak. Jangan lupa gunakan <strong>tanda kurung</strong> agar pengecekan "admin atau premium" didahulukan!</li>
                  </ul>
                  <div class="code-block" style="font-size: 18px;">
<span class="keyword">password_ok</span> <span class="operator">=</span> <span class="keyword">True</span><br>
<span class="keyword">is_admin</span> <span class="operator">=</span> <span class="keyword">False</span><br>
<span class="keyword">is_premium</span> <span class="operator">=</span> <span class="keyword">True</span><br><br>
<span class="keyword">if</span> <input type="text" id="paren-input" placeholder="ketik kondisinya..." style="width: 450px; font-family: monospace; font-size: 18px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Welcome back, Player!"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Akses ditolak."</span>)
                  </div>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkParenGuess(document.getElementById('paren-input').value, this, 'Tepat Sekali! Tanda kurung memastikan sistem mengecek status admin/premium lebih dulu, sebelum menggabungkannya dengan syarat password.')" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Cek Kode Saya!</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          }
        ]
      },
      5: {
        kicker: "Checkpoint 05 · Logika Kombinasi",
        title: "Logical Operator",
        duration: "Video 5 · Menggabungkan kondisi",
        videoId: "_iRZY0-_skc",
        quizzes: [
          {
            time: 326,
            shown: false,
            resume: true,
            resumeTime: 330,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan: Logika <code>and</code> 🧩</h2>
                  <div class="slide-text">
                  <p><strong>Instruksi:</strong> Lengkapi program beasiswa berikut agar berjalan dengan benar!</p>
                  <ul>
                      <li>Syarat Beasiswa: Nilai harus lebih dari 80 <strong>dan</strong> aktif organisasi bernilai True.</li>
                      <li>Ketik operator logika dan variabel kondisi yang tepat di dalam kotak.</li>
                  </ul>
                  <div class="code-block">
<span class="keyword">nilai</span> <span class="operator">=</span> <span class="string">85</span><br>
<span class="keyword">aktif_organisasi</span> <span class="operator">=</span> <span class="keyword">True</span><br><br>
<span class="keyword">if</span> nilai <span class="operator">&gt;</span> <span class="string">80</span> <input type="text" id="and-input" placeholder="ketik kondisinya..." style="width: 350px; font-family: monospace; font-size: 20px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Selamat, kamu dapat beasiswa!"</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Belum memenuhi syarat."</span>)
                  </div>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkAndGuess(document.getElementById('and-input').value, this, 'Tepat Sekali! Kamu menggunakan <code>and</code> untuk memastikan kedua syarat (nilai dan organisasi) sama-sama terpenuhi.')" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Cek Kode Saya!</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          },
          {
            time: 535,
            shown: false,
            resume: true,
            resumeTime: 539,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan: Logika <code>or</code> 🧩</h2>
                  <div class="slide-text">
                  <p><strong>Instruksi:</strong> Lengkapi program diskon berikut!</p>
                  <ul>
                      <li>Syarat Diskon: Pembeli adalah pelajar <strong>atau</strong> memiliki kupon diskon.</li>
                      <li>Ketik operator logika dan variabel kondisi yang tepat di dalam kotak.</li>
                  </ul>
                  <div class="code-block">
<span class="keyword">status</span> <span class="operator">=</span> <span class="string">"umum"</span><br>
<span class="keyword">ada_kupon</span> <span class="operator">=</span> <span class="keyword">True</span><br><br>
<span class="keyword">if</span> status <span class="operator">==</span> <span class="string">"pelajar"</span> <input type="text" id="or-input" placeholder="ketik kondisinya..." style="width: 250px; font-family: monospace; font-size: 20px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Hore! Kamu dapat diskon."</span>)<br>
<span class="keyword">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Harga normal."</span>)
                  </div>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkOrGuess(document.getElementById('or-input').value, this, 'Tepat Sekali! Kamu menggunakan <code>or</code>, jadi diskon tetap berlaku karena dia punya kupon walaupun bukan pelajar.')" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Cek Kode Saya!</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          },
          {
            time: 1097,
            shown: false,
            resume: true,
            resumeTime: 1101,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan: Nested ke Logical 🛠️</h2>
                  <div class="slide-text">
                  <p>Ubah kode bercabang yang ribet ini menjadi satu baris kondisi dengan operator logika!</p>
                  <div class="code-block" style="font-size: 16px; margin-bottom: 10px;">
<span style="color: #6c757d; font-style: italic;"># Kode Awal (Ribet):</span><br>
<span class="keyword">if</span> hari <span class="operator">==</span> <span class="string">"sabtu"</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> cuaca <span class="operator">==</span> <span class="string">"cerah"</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Main bola"</span>)
                  </div>
                  <div class="code-block" style="font-size: 16px;">
<span style="color: #6c757d; font-style: italic;"># Kode Barumu (Singkat):</span><br>
<span class="keyword">if</span> hari <span class="operator">==</span> <span class="string">"sabtu"</span> <input type="text" id="logical-input" placeholder="ketik kelanjutannya..." style="width: 250px; font-family: monospace; font-size: 16px; padding: 5px; border: 3px solid #1A1A1A; border-radius: 8px; color: #1A1A1A;"> :<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function">print</span>(<span class="string">"Main bola"</span>)
                  </div>
                  
                  <div style="display: flex; gap: 20px; justify-content: center; margin-top: 20px;">
                      <button onclick="checkNestedToLogicalGuess(document.getElementById('logical-input').value, this, 'Keren! Dengan <code>and</code>, kamu bisa mengecek dua syarat sekaligus tanpa harus membuat <code>if</code> di dalam <code>if</code>.')" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Cek Kode Saya!</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          }
        ]
      },
      6: {
        kicker: "Checkpoint 06 · Financial Literacy",
        title: "Needs vs Wants & Risks",
        duration: "Video 6 · Financial Literacy",
        videoId: "bMsKBaRsKmc",
        quizzes: [
          {
            time: 176,
            shown: false,
            resume: true,
            resumeTime: 176,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan 1: Kebutuhan Siswa 📚</h2>
                  <div class="slide-text">
                  <p>Apa contoh <strong>Kebutuhan</strong> kamu sebagai seorang siswa/i (selain yang disebutkan di video)?</p>
                  <p>Tuliskan 5 contoh di bawah ini:</p>
                  <div style="display: flex; flex-direction: column; gap: 10px; align-items: center;">
                    <input type="text" class="needs-input" placeholder="Kebutuhan 1..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="needs-input" placeholder="Kebutuhan 2..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="needs-input" placeholder="Kebutuhan 3..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="needs-input" placeholder="Kebutuhan 4..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="needs-input" placeholder="Kebutuhan 5..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                  </div>
                  
                  <div style="display: flex; justify-content: center; margin-top: 20px;">
                      <button onclick="checkNeedsWantsGuess('needs-input', this)" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Kumpulkan</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          },
          {
            time: 220,
            shown: false,
            resume: true,
            resumeTime: 220,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Latihan 2: Keinginan Siswa 🎮</h2>
                  <div class="slide-text">
                  <p>Nah, sekarang apa contoh <strong>Keinginan</strong> yang mau kamu beli yang masih berkaitan dengan sekolah?</p>
                  <p>Tuliskan 5 contoh di bawah ini:</p>
                  <div style="display: flex; flex-direction: column; gap: 10px; align-items: center;">
                    <input type="text" class="wants-input" placeholder="Keinginan 1..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="wants-input" placeholder="Keinginan 2..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="wants-input" placeholder="Keinginan 3..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="wants-input" placeholder="Keinginan 4..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                    <input type="text" class="wants-input" placeholder="Keinginan 5..." style="width: 80%; font-family: 'Fredoka', sans-serif; font-size: 16px; padding: 10px; border: 3px solid #1A1A1A; border-radius: 8px;">
                  </div>
                  
                  <div style="display: flex; justify-content: center; margin-top: 20px;">
                      <button onclick="checkNeedsWantsGuess('wants-input', this)" style="background-color: #FFE500; border: 4px solid #1A1A1A; border-radius: 16px; padding: 15px 30px; font-size: 20px; font-family: 'Fredoka', sans-serif; font-weight: bold; cursor: pointer; box-shadow: 6px 6px 0px #1A1A1A; transition: transform 0.1s;">Kumpulkan</button>
                  </div>
                  <div class="guess-feedback" style="display: none; padding: 15px; border-radius: 12px; border: 3px solid #1A1A1A; font-size: 20px; font-weight: bold; text-align: center; margin-top: 20px; line-height: 1.4;"></div>
                  </div>`
              }
            ]
          },
          {
            time: 772,
            shown: false,
            resume: true,
            resumeTime: 785,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Mini Activity: Tentukan Kategori 🎯</h2>
                  <div class="slide-text">
                  <p>Pilih 3 barang dari tabel ini dan buat program Python untuk mengecek Kategorinya (Kebutuhan/Keinginan)!</p>
                  <table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 14px; margin-bottom: 15px;">
                      <thead>
                          <tr style="background-color: var(--blue); color: var(--white);">
                              <th style="padding: 5px; border: 2px solid var(--black);">Barang</th>
                              <th style="padding: 5px; border: 2px solid var(--black);">Kategori</th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr><td style="padding: 5px; border: 1px solid var(--black);">Buku tulis</td><td style="padding: 5px; border: 1px solid var(--black);">Kebutuhan</td></tr>
                          <tr><td style="padding: 5px; border: 1px solid var(--black);">Air minum</td><td style="padding: 5px; border: 1px solid var(--black);">Kebutuhan</td></tr>
                          <tr><td style="padding: 5px; border: 1px solid var(--black);">Skin game</td><td style="padding: 5px; border: 1px solid var(--black);">Keinginan</td></tr>
                          <tr><td style="padding: 5px; border: 1px solid var(--black);">Snack tambahan</td><td style="padding: 5px; border: 1px solid var(--black);">Keinginan</td></tr>
                          <tr><td style="padding: 5px; border: 1px solid var(--black);">Pulsa internet kelas online</td><td style="padding: 5px; border: 1px solid var(--black);">Kebutuhan</td></tr>
                          <tr><td style="padding: 5px; border: 1px solid var(--black);">Gantungan kunci</td><td style="padding: 5px; border: 1px solid var(--black);">Keinginan</td></tr>
                      </tbody>
                  </table>
                  
                  <textarea id="python-ide-6" spellcheck="false" placeholder="# Tulis programmu di sini" style="width: 100%; height: 180px; background-color: #1e1e1e; color: #d4d4d4; font-family: monospace; font-size: 14px; padding: 10px; border-radius: 8px; border: 1px solid #444; margin-bottom: 10px;"></textarea>
                  
                  <div style="display: flex; gap: 10px; justify-content: center; margin-bottom: 10px;">
                      <button onclick="runPyodideCode('python-ide-6', 'ide-output-6')" style="background-color: var(--green); border: 2px solid #1A1A1A; border-radius: 8px; padding: 8px 16px; font-weight: bold; cursor: pointer;">Jalankan Kode</button>
                      <button onclick="checkIde6Guess(this)" style="background-color: #FFE500; border: 2px solid #1A1A1A; border-radius: 8px; padding: 8px 16px; font-weight: bold; cursor: pointer;">Kumpulkan</button>
                  </div>
                  
                  <div id="ide-output-6" style="background-color: black; color: white; padding: 10px; border-radius: 8px; min-height: 50px; font-family: monospace; white-space: pre-wrap; font-size: 12px; margin-bottom: 10px;">Output program akan muncul di sini...</div>
                  
                  <div class="guess-feedback" style="display: none; padding: 10px; border-radius: 8px; border: 2px solid #1A1A1A; font-weight: bold; text-align: center;"></div>
                  </div>`
              }
            ]
          },
          {
            time: 2123,
            shown: false,
            resume: false,
            resumeTime: 2127,
            questions: [
              {
                html: `
                  <h2 class="slide-title">Selesai Menonton! 🎉</h2>
                  <div class="slide-text">
                  <p>Kamu sudah menyelesaikan Video 6!</p>
                  <p>Mari kita ulas sebentar: Mengelola keuangan itu soal membuat keputusan. Kamu harus menimbang antara Kebutuhan dan Keinginan, serta Level Risiko dari setiap pengeluaran.</p>
                  <p>Silakan lanjut ke Tab 7 untuk mengerjakan <strong>Tugas Akhir</strong> misi Conditional ini.</p>
                  </div>
                `
              }
            ]
          }
        ]
      },
      7: {
        kicker: "Mandatory Assignment",
        title: "Smart Budget & Risk Planner",
        duration: "Tugas Akhir Misi Conditional",
        videoId: "bMsKBaRsKmc",
        startSeconds: 2137,
        quizzes: []
      }
    };

    const stepPanels = document.querySelectorAll(".step-panel");
    const lessonTabs = document.querySelectorAll(".lesson-tab");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    const lessonKicker = document.getElementById("lessonKicker");
    const lessonTitle = document.getElementById("lessonTitle");
    const durationPill = document.getElementById("durationPill");
    const progressText = document.getElementById("progressText");
    const progressFill = document.getElementById("progressFill");
    const quizOverlay = document.getElementById("quizOverlay");
    const quizQuestion = document.getElementById("quizQuestion");
    const quizFeedback = document.getElementById("quizFeedback");
    const quizNext = document.getElementById("quizNext");
    const quizProgress = document.getElementById("quizProgress");
    const answerButtons = document.querySelectorAll(".answer-button");
    const completionToast = document.getElementById("completionToast");
    const videoFrames = document.querySelectorAll(".video-frame");
    const playButtons = document.querySelectorAll(".video-play, .video-center-play, .play-pause");
    const muteButtons = document.querySelectorAll(".video-mute");
    const fullscreenButtons = document.querySelectorAll(".video-fullscreen");
    const seekInputs = document.querySelectorAll(".video-seek");

    let currentStep = 1;
    const totalSteps = Object.keys(courseData).length;
    
    // Dynamic player tracking
    const players = {};
    const videoWatchedStatus = { 1: false, 2: false, 3: false, 4: false, 5: false, 6: false, 7: false };
    const timeCheckers = {};
    
    // Global Quiz Feedback Functions for Custom HTML
    window.checkGuess = function(btn, isCorrect, explanation) {
        const container = btn.parentElement;
        const feedback = container.nextElementSibling;
        const buttons = container.querySelectorAll('button');
        buttons.forEach(b => {
            b.disabled = true;
            b.style.opacity = '0.5';
        });
        btn.style.opacity = '1';
        
        feedback.style.display = 'block';
        if (isCorrect) {
            feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
            feedback.style.backgroundColor = "#00E676";
            feedback.style.color = "var(--black)";
        } else {
            feedback.innerHTML = `❌ <strong>SALAH!</strong><br>${explanation}`;
            feedback.style.backgroundColor = "#FF0055";
            feedback.style.color = "white";
        }
        document.getElementById("quizNext").classList.add("visible");
    };

    window.checkMB1QGuess = function(kwVal, condVal, btn, explanation) {
        const container = btn.parentElement;
        const feedback = container.nextElementSibling;
        let kw = kwVal.replace(/\s+/g, '').toLowerCase();
        let cond = condVal.replace(/\s+/g, '').toLowerCase();
        
        feedback.style.display = 'block';
        if (kw === 'elif' && (cond === 'age<18' || cond === 'age<=17')) {
            feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
            feedback.style.backgroundColor = "#00E676";
            feedback.style.color = "var(--black)";
            btn.disabled = true;
            btn.style.opacity = '0.5';
            document.getElementById('mb1-kw').disabled = true;
            document.getElementById('mb1-cond').disabled = true;
        } else {
            feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Coba periksa lagi kondisi di Slide 17. Apa sintaks untuk cabang kedua? Dan bagaimana mengecek umur di bawah 18?`;
            feedback.style.backgroundColor = "#FF0055";
            feedback.style.color = "white";
        }
        document.getElementById("quizNext").classList.add("visible");
    };

    window.checkNeedsWantsGuess = function(className, btn) {
        const inputs = document.querySelectorAll('.' + className);
        let allFilled = true;
        inputs.forEach(input => {
            if (input.value.trim() === '') allFilled = false;
        });

        const container = btn.parentElement;
        const feedback = container.nextElementSibling;
        
        if (!allFilled) {
            feedback.style.display = 'block';
            feedback.innerHTML = `❌ Lengkapi kelima contohnya terlebih dahulu ya!`;
            feedback.style.backgroundColor = "#FF0055";
            feedback.style.color = "white";
            return;
        }

        btn.disabled = true;
        btn.style.opacity = '0.5';
        
        feedback.style.display = 'block';
        feedback.innerHTML = `✅ <strong>Tersimpan!</strong><br>Terima kasih sudah membagikan pemikiranmu.`;
        feedback.style.backgroundColor = "#00E676";
        feedback.style.color = "var(--black)";
        document.getElementById("quizNext").classList.add("visible");
    };

    window.checkIde6Guess = function(btn) {
        const code = document.getElementById('python-ide-6').value.toLowerCase();
        const keywords = ['buku tulis', 'air minum', 'skin game', 'snack tambahan', 'pulsa', 'gantungan kunci'];
        let matchCount = 0;
        
        keywords.forEach(kw => {
            if (code.includes(kw)) matchCount++;
        });

        const container = btn.parentElement;
        const feedback = container.nextElementSibling.nextElementSibling; // the feedback div
        
        feedback.style.display = 'block';
        if (matchCount >= 3) {
            feedback.innerHTML = `✅ <strong>Bagus!</strong> Kamu sudah memakai setidaknya 3 barang dari tabel.`;
            feedback.style.backgroundColor = "#00E676";
            feedback.style.color = "var(--black)";
            btn.disabled = true;
            btn.style.opacity = '0.5';
            document.getElementById("quizNext").classList.add("visible");
        } else {
            feedback.innerHTML = `❌ Kamu baru memasukkan ${matchCount} barang dari tabel di kodemu. Minimal butuh 3 barang (misal: "Buku tulis", "Skin game", dsb).`;
            feedback.style.backgroundColor = "#FF0055";
            feedback.style.color = "white";
        }
    };

    // Pyodide Integration
    let pyodideReadyPromise;
    async function initPyodide() {
        pyodideReadyPromise = loadPyodide();
        await pyodideReadyPromise;
        console.log("Pyodide Ready");
    }
    // Only call if loadPyodide is available
    if (typeof loadPyodide !== 'undefined') {
        initPyodide();
    }

    window.runPyodideCode = async function(inputId, outputId) {
        const code = document.getElementById(inputId).value;
        const output = document.getElementById(outputId);
        output.innerHTML = "Menjalankan...";
        output.style.color = "white";

        try {
            let pyodide = await pyodideReadyPromise;
            // Clear previous outputs
            pyodide.setStdout({ batched: (msg) => {
                if (output.innerHTML === "Menjalankan...") output.innerHTML = "";
                output.innerHTML += msg + "\n";
            }});
            
            await pyodide.runPythonAsync(code);
            if (output.innerHTML === "Menjalankan...") output.innerHTML = "Program selesai tanpa output teks.";
        } catch (err) {
            output.innerHTML = err;
            output.style.color = "#FF4444";
        }
    };

    window.runAssignmentCode = function() {
        runPyodideCode('python-ide-7', 'ide-output-7');
    };

    window.submitAssignmentCode = function() {
        alert("✅ Tugas berhasil dikumpulkan! Selamat kamu telah menyelesaikan Misi Conditional!");
    };

    window.checkMB2QGuess = function(val1, val2, btn, explanation) {
        const container = btn.parentElement;
        const feedback = container.nextElementSibling;
        let v1 = val1.replace(/\s+/g, '');
        let v2 = val2.replace(/\s+/g, '');
        
        feedback.style.display = 'block';
        if (v1 === '90' && v2 === '80') {
            feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
            feedback.style.backgroundColor = "#00E676";
            feedback.style.color = "var(--black)";
            btn.disabled = true;
            btn.style.opacity = '0.5';
            document.getElementById('mb2-val1').disabled = true;
            document.getElementById('mb2-val2').disabled = true;
        } else {
            feedback.innerHTML = `❌ <strong>URUTAN MASIH SALAH!</strong><br>Ingat, kondisi paling ketat/sulit (nilai &gt;= 90 untuk A) harus dicek paling atas!`;
            feedback.style.backgroundColor = "#FF0055";
            feedback.style.color = "white";
        }
        document.getElementById("quizNext").classList.add("visible");
    };
    
    // Quiz state
    let shuffledQuestions = [];
    let currentQuestionIdx = 0;
    let resumeVideoAfterQuiz = false;
    let resumeVideoTime = null;
    let requestedFullscreenFrame = null;

    // Initialize tracking status for all steps
    Object.keys(courseData).forEach(stepId => {
      videoWatchedStatus[stepId] = false;
    });

    function showStep(step) {
      if (!courseData[step]) return;

      currentStep = step;
      stepPanels.forEach((panel, index) => {
        panel.hidden = index + 1 !== step;
      });

      lessonTabs.forEach((tab) => {
        const isActive = Number(tab.dataset.step) === step;
        tab.classList.toggle("active", isActive);
        if (isActive) {
          tab.setAttribute("aria-current", "step");
        } else {
          tab.removeAttribute("aria-current");
        }
      });

      lessonKicker.textContent = courseData[step].kicker;
      lessonTitle.textContent = courseData[step].title;
      durationPill.textContent = courseData[step].duration;
      progressText.textContent = step + " dari " + totalSteps;
      progressFill.style.width = (step / totalSteps * 100) + "%";

      // Navigation logic
      if (step === 1) {
        prevButton.disabled = true;
      } else {
        prevButton.disabled = false;
      }

      if (step === totalSteps) {
        nextButton.innerHTML = "Tandai selesai <span aria-hidden=\"true\">✓</span>";
        nextButton.disabled = false; // DEV MODE: !videoWatchedStatus[step];
      } else {
        nextButton.innerHTML = "Lanjut ke video " + (step + 1) + " <span aria-hidden=\"true\">→</span>";
        nextButton.disabled = false; // DEV MODE: !videoWatchedStatus[step];
      }

      // Pause all other videos
      Object.keys(players).forEach(id => {
        if (Number(id) !== step && players[id] && typeof players[id].pauseVideo === "function") {
          players[id].pauseVideo();
        }
      });

      document.querySelector(".dashboard").scrollIntoView({ behavior: "smooth", block: "start" });
    }

    lessonTabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        const targetStep = Number(tab.dataset.step);
        // Ensure sequential progression: can only click targetStep if (targetStep - 1) is watched
        // DEV MODE: if (targetStep > 1 && !videoWatchedStatus[targetStep - 1]) return;
        showStep(targetStep);
      });
    });

    prevButton.addEventListener("click", () => showStep(currentStep - 1));

    nextButton.addEventListener("click", () => {
      if (currentStep < totalSteps) {
        showStep(currentStep + 1);
        return;
      }

      progressText.textContent = totalSteps + " dari " + totalSteps + " · selesai";
      progressFill.style.width = "100%";
      completionToast.classList.add("show");
      window.setTimeout(() => completionToast.classList.remove("show"), 3800);
    });

    function shuffle(items) {
      const result = [...items];
      for (let i = result.length - 1; i > 0; i--) {
        const randomIndex = Math.floor(Math.random() * (i + 1));
        [result[i], result[randomIndex]] = [result[randomIndex], result[i]];
      }
      return result;
    }

    // Pass the specific quiz's questions array to openQuiz
    function openQuiz(questionsArray, shouldResumeVideo = false, seekTime = null) {
      const fullscreenElement = getFullscreenElement() || requestedFullscreenFrame;
      if (fullscreenElement && fullscreenElement.classList.contains("video-frame")) {
        fullscreenElement.appendChild(quizOverlay);
      }
      resumeVideoAfterQuiz = shouldResumeVideo;
      resumeVideoTime = seekTime;
      shuffledQuestions = shuffle(questionsArray);
      currentQuestionIdx = 0;
      quizOverlay.classList.add("open");
      document.body.style.overflow = "hidden";
      renderQuestion();
      window.setTimeout(() => document.querySelector(".answer-button.true").focus(), 50);
    }

    function closeQuiz(resumeVideo = false, seekTime = null) {
      quizOverlay.classList.remove("open");
      document.body.style.overflow = "";
      if (resumeVideo && players[currentStep]) {
        if (seekTime !== null && typeof players[currentStep].seekTo === "function") {
          players[currentStep].seekTo(seekTime, true);
        }
        if (typeof players[currentStep].playVideo === "function") {
          players[currentStep].playVideo();
        }
      }
      if (!getFullscreenElement() && quizOverlay.parentElement !== document.body) {
        document.body.appendChild(quizOverlay);
      }
    }

    function formatVideoTime(value) {
      const totalSeconds = Number.isFinite(value) ? Math.max(0, Math.floor(value)) : 0;
      const minutes = Math.floor(totalSeconds / 60);
      const seconds = String(totalSeconds % 60).padStart(2, "0");
      return minutes + ":" + seconds;
    }

    function getFullscreenElement() {
      return document.fullscreenElement || document.webkitFullscreenElement;
    }

    function updateVideoControls(stepId) {
      const player = players[stepId];
      if (!player || typeof player.getCurrentTime !== "function") return;

      const duration = player.getDuration() || 0;
      const currentTime = player.getCurrentTime() || 0;
      const seekInput = document.querySelector('.video-seek[data-step="' + stepId + '"]');
      const timeLabel = document.querySelector('.video-time[data-step="' + stepId + '"]');

      if (seekInput && !seekInput.matches(":active")) {
        seekInput.value = duration ? (currentTime / duration * 100) : 0;
      }
      if (timeLabel) {
        timeLabel.textContent = formatVideoTime(currentTime) + " / " + formatVideoTime(duration);
      }
    }

    playButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const stepId = button.dataset.step;
        const player = players[stepId];
        if (!player || typeof player.getPlayerState !== "function") return;

        if (player.getPlayerState() === YT.PlayerState.PLAYING) {
          player.pauseVideo();
        } else {
          player.playVideo();
        }
      });
    });

    muteButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const player = players[button.dataset.step];
        if (!player || typeof player.isMuted !== "function") return;

        if (player.isMuted()) {
          player.unMute();
          button.textContent = "🔊";
          button.setAttribute("aria-label", "Matikan suara");
        } else {
          player.mute();
          button.textContent = "🔇";
          button.setAttribute("aria-label", "Nyalakan suara");
        }
      });
    });

    seekInputs.forEach((input) => {
      input.addEventListener("input", () => {
        const player = players[input.dataset.step];
        if (!player || typeof player.seekTo !== "function") return;
        const duration = player.getDuration() || 0;
        player.seekTo(duration * Number(input.value) / 100, true);
      });
    });

    fullscreenButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const frame = document.querySelector('.video-frame[data-video-step="' + button.dataset.step + '"]');
        if (!frame) return;

        if (getFullscreenElement()) {
          const exitFullscreen = document.exitFullscreen || document.webkitExitFullscreen;
          if (exitFullscreen) exitFullscreen.call(document);
          return;
        }

        const requestFullscreen = frame.requestFullscreen || frame.webkitRequestFullscreen;
        if (requestFullscreen) {
          requestedFullscreenFrame = frame;
          Promise.resolve(requestFullscreen.call(frame)).catch(() => {
            requestedFullscreenFrame = null;
          });
        }
      });
    });

    function handleFullscreenChange() {
      const fullscreenElement = getFullscreenElement();
      requestedFullscreenFrame = fullscreenElement && fullscreenElement.classList.contains("video-frame")
        ? fullscreenElement
        : null;
      fullscreenButtons.forEach((button) => {
        const frame = document.querySelector('.video-frame[data-video-step="' + button.dataset.step + '"]');
        const isFullscreen = fullscreenElement === frame;
        button.textContent = isFullscreen ? "✕" : "⛶";
        button.setAttribute("aria-label", isFullscreen ? "Keluar dari layar penuh" : "Tampilkan layar penuh");
      });

      if (!fullscreenElement && !quizOverlay.classList.contains("open") && quizOverlay.parentElement !== document.body) {
        document.body.appendChild(quizOverlay);
      }
    }

    document.addEventListener("fullscreenchange", handleFullscreenChange);
    document.addEventListener("webkitfullscreenchange", handleFullscreenChange);

    function renderProgress() {
      quizProgress.innerHTML = "";
      shuffledQuestions.forEach((_, index) => {
        const dot = document.createElement("span");
        dot.className = "quiz-dot";
        if (index < currentQuestionIdx) dot.classList.add("done");
        if (index === currentQuestionIdx) dot.classList.add("active");
        quizProgress.appendChild(dot);
      });
    }

    function renderQuestion() {
      if (currentQuestionIdx >= shuffledQuestions.length) {
        quizQuestion.textContent = "Checkpoint selesai. Kamu siap melanjutkan pembelajaran.";
        quizQuestion.style.display = "block";
        document.getElementById("answerRow").style.display = "none";
        quizFeedback.className = "quiz-feedback correct";
        quizFeedback.textContent = "Bagus. Semua pertanyaan sudah kamu jawab.";
        quizFeedback.style.display = "block";
        quizNext.textContent = "Lanjut belajar →";
        quizNext.classList.add("visible");
        
        let customHtml = document.getElementById("quizCustomHtml");
        if (customHtml) customHtml.style.display = "none";
        
        renderProgress();
        return;
      }

      const item = shuffledQuestions[currentQuestionIdx];

      if (item.html) {
        quizQuestion.style.display = "none";
        document.getElementById("answerRow").style.display = "none";
        quizFeedback.style.display = "none";
        
        let customHtml = document.getElementById("quizCustomHtml");
        if (!customHtml) {
          customHtml = document.createElement("div");
          customHtml.id = "quizCustomHtml";
          quizQuestion.parentNode.insertBefore(customHtml, document.getElementById("answerRow"));
        }
        customHtml.innerHTML = item.html;
        customHtml.style.display = "block";
        quizNext.textContent = "Soal berikutnya →";
        quizNext.classList.remove("visible");
      } else {
        let customHtml = document.getElementById("quizCustomHtml");
        if (customHtml) customHtml.style.display = "none";
        quizQuestion.style.display = "block";
        document.getElementById("answerRow").style.display = "grid";
        quizQuestion.textContent = item.question;
        quizFeedback.style.display = "block";
        quizFeedback.className = "quiz-feedback";
        quizFeedback.textContent = "";
        quizNext.textContent = "Soal berikutnya →";
        quizNext.classList.remove("visible");
        answerButtons.forEach((button) => {
          button.disabled = false;
        });
      }
      
      renderProgress();
    }

    function checkAnswer(answer) {
      const item = shuffledQuestions[currentQuestionIdx];
      const isCorrect = answer === item.answer;
      answerButtons.forEach((button) => {
        button.disabled = true;
      });
      quizFeedback.className = "quiz-feedback " + (isCorrect ? "correct" : "wrong");
      quizFeedback.textContent = (isCorrect ? "Tepat. " : "Belum tepat. ") + item.explanation;
      quizNext.classList.add("visible");
      quizNext.focus();
    }

    answerButtons.forEach((button) => {
      button.addEventListener("click", () => checkAnswer(button.dataset.answer === "true"));
    });

    quizNext.addEventListener("click", () => {
      if (currentQuestionIdx >= shuffledQuestions.length) {
        closeQuiz(resumeVideoAfterQuiz, resumeVideoTime);
        return;
      }
      currentQuestionIdx += 1;
      renderQuestion();
    });

    // Preview button for step 2 (hardcoded in HTML, mapped to the first quiz of step 2)
    const openQuizBtn = document.getElementById("openQuizButton");
    if (openQuizBtn) {
      openQuizBtn.addEventListener("click", () => {
        if (players[currentStep] && typeof players[currentStep].pauseVideo === "function") players[currentStep].pauseVideo();
        openQuiz(courseData[2].quizzes[0].questions, false);
      });
    }

    // Quiz checking functions
    function checkParenGuess(userVal, btn, explanation) {
      const container = btn.parentElement;
      const feedback = container.nextElementSibling;
      
      let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
      
      feedback.style.display = 'block';
      if (normalizedUser === 'password_okand(is_adminoris_premium)' || normalizedUser === '(is_adminoris_premium)andpassword_ok' || normalizedUser === 'password_ok==trueand(is_admin==trueoris_premium==true)') {
          feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
          feedback.style.backgroundColor = "#00E676";
          feedback.style.color = "#1A1A1A";
          btn.disabled = true;
          btn.style.opacity = '0.5';
          document.getElementById('paren-input').disabled = true;
      } else {
          feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Pastikan kamu menggabungkan 'is_admin or is_premium' di dalam tanda kurung (), lalu gunakan 'and password_ok'.`;
          feedback.style.backgroundColor = "#FF0055";
          feedback.style.color = "white";
      }
    }

    // Dynamic YouTube Player Initialization
    function onYouTubeIframeAPIReady() {
      Object.keys(courseData).forEach(stepId => {
        const playerId = "youtube-player-" + stepId;
        const domEl = document.getElementById(playerId);
        
        if (domEl) {
          players[stepId] = new YT.Player(playerId, {
            host: "https://www.youtube-nocookie.com",
            videoId: courseData[stepId].videoId,
            playerVars: {
              playsinline: 1,
              rel: 0,
              controls: 0,
              disablekb: 1,
              fs: 0,
              iv_load_policy: 3,
              start: courseData[stepId].startSeconds || 0
            },
            events: {
              onReady: (event) => {
                const iframe = event.target.getIframe();
                iframe.removeAttribute("allowfullscreen");
                iframe.setAttribute("tabindex", "-1");
                iframe.setAttribute("aria-hidden", "true");
                updateVideoControls(stepId);
              },
              onStateChange: (event) => handlePlayerStateChange(stepId, event)
            }
          });
        }
      });
    }

    function handlePlayerStateChange(stepId, event) {
      // 1. Mark as watched if ended
      if (event.data === YT.PlayerState.ENDED) {
        videoWatchedStatus[stepId] = true;
        // If this is the current step, we might need to enable the Next button
        if (Number(stepId) === currentStep) {
          nextButton.disabled = false;
        }
      }

      const isPlaying = event.data === YT.PlayerState.PLAYING;
      document.querySelectorAll('.video-play[data-step="' + stepId + '"], .play-pause[data-step="' + stepId + '"]').forEach((playButton) => {
        playButton.textContent = isPlaying ? "❚❚" : "▶";
        playButton.setAttribute("aria-label", isPlaying ? "Jeda video" : "Putar video");
      });
      document.querySelectorAll('.video-center-play[data-step="' + stepId + '"]').forEach((playButton) => {
        playButton.classList.toggle("is-playing", isPlaying);
      });
      updateVideoControls(stepId);

      // 2. Handle quiz timing loop
      window.clearInterval(timeCheckers[stepId]);
      
      if (event.data === YT.PlayerState.PLAYING) {
        timeCheckers[stepId] = window.setInterval(() => {
          updateVideoControls(stepId);
          checkVideoQuizzes(stepId);
        }, 300);
      }
    }

    function checkVideoQuizzes(stepId) {
      const player = players[stepId];
      if (!player || typeof player.getCurrentTime !== "function") return;
      
      const currentTime = player.getCurrentTime();
      const stepConfig = courseData[stepId];
      
      if (!stepConfig || !stepConfig.quizzes) return;

      for (let quiz of stepConfig.quizzes) {
        if (!quiz.shown && currentTime >= quiz.time) {
          quiz.shown = true;
          player.pauseVideo();
          window.clearInterval(timeCheckers[stepId]);

          const shouldResume = quiz.resume !== undefined ? quiz.resume : true;
          openQuiz(quiz.questions, shouldResume, quiz.resumeTime);
          break; // Stop checking other quizzes for now, one at a time
        }
      }
    }

    function checkAndGuess(userVal, btn, explanation) {
      const container = btn.parentElement;
      const feedback = container.nextElementSibling;
      let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
      
      feedback.style.display = 'block';
      if (normalizedUser === 'andaktif_organisasi==true' || normalizedUser === 'andaktif_organisasi' || normalizedUser === 'and(aktif_organisasi==true)') {
          feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
          feedback.style.backgroundColor = "#00E676";
          feedback.style.color = "#1A1A1A";
          btn.disabled = true;
          btn.style.opacity = '0.5';
          document.getElementById('and-input').disabled = true;
      } else {
          feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Coba lagi! Kamu butuh operator logika 'and' diikuti dengan kondisi pengecekan variabel aktif_organisasi.`;
          feedback.style.backgroundColor = "#FF0055";
          feedback.style.color = "white";
      }
    }

    function checkOrGuess(userVal, btn, explanation) {
      const container = btn.parentElement;
      const feedback = container.nextElementSibling;
      let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
      
      feedback.style.display = 'block';
      if (normalizedUser === 'orada_kupon==true' || normalizedUser === 'orada_kupon' || normalizedUser === 'or(ada_kupon==true)') {
          feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
          feedback.style.backgroundColor = "#00E676";
          feedback.style.color = "#1A1A1A";
          btn.disabled = true;
          btn.style.opacity = '0.5';
          document.getElementById('or-input').disabled = true;
      } else {
          feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Coba lagi! Kamu butuh operator logika 'or' diikuti dengan kondisi pengecekan variabel ada_kupon.`;
          feedback.style.backgroundColor = "#FF0055";
          feedback.style.color = "white";
      }
    }

    function checkNestedToLogicalGuess(userVal, btn, explanation) {
      const container = btn.parentElement;
      const feedback = container.nextElementSibling;
      let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
      
      feedback.style.display = 'block';
      if (normalizedUser === 'andcuaca=="cerah"' || normalizedUser === "andcuaca=='cerah'") {
          feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
          feedback.style.backgroundColor = "#00E676";
          feedback.style.color = "#1A1A1A";
          btn.disabled = true;
          btn.style.opacity = '0.5';
          document.getElementById('logical-input').disabled = true;
      } else {
          feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Pastikan kamu menggunakan operator 'and' lalu cek apakah 'cuaca == "cerah"'.`;
          feedback.style.backgroundColor = "#FF0055";
          feedback.style.color = "white";
      }
    }

    window.onYouTubeIframeAPIReady = onYouTubeIframeAPIReady;
