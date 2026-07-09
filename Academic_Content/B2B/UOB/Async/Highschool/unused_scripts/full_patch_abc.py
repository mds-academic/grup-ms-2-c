import os
import re

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c'
]

notice_css = """
<style>
.dashboard-notice-backdrop {
  position: fixed;
  inset: 0;
  z-index: 10000;
  display: grid;
  place-items: center;
  padding: 24px;
  background: rgba(26, 26, 26, 0.42);
  backdrop-filter: blur(6px);
}

.dashboard-notice-card {
  width: min(440px, 100%);
  display: grid;
  grid-template-columns: 56px 1fr;
  gap: 16px;
  align-items: start;
  padding: 22px;
  background: #fff7d8;
  border: 4px solid #1a1a1a;
  border-radius: 18px;
  box-shadow: 10px 10px 0 #1a1a1a;
  color: #1a1a1a;
  animation: dashboard-notice-in 180ms ease-out both;
}

.dashboard-notice-card.success {
  background: #dcffe9;
}

.dashboard-notice-icon {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border: 3px solid #1a1a1a;
  border-radius: 14px;
  background: #ffce4a;
  box-shadow: 4px 4px 0 #1a1a1a;
  font-weight: 900;
  font-size: 24px;
}

.dashboard-notice-card.success .dashboard-notice-icon {
  background: #27c881;
}

.dashboard-notice-copy {
  min-width: 0;
}

.dashboard-notice-kicker {
  margin: 0 0 6px;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0;
  text-transform: uppercase;
  color: #5b5b5b;
}

.dashboard-notice-copy h3 {
  margin: 0 0 8px;
  font-size: 24px;
  line-height: 1.05;
}

.dashboard-notice-copy p:last-child {
  margin: 0;
  font-size: 16px;
  line-height: 1.45;
  font-weight: 700;
}

.dashboard-notice-action {
  grid-column: 1 / -1;
  justify-self: end;
  min-width: 132px;
  padding: 12px 18px;
  border: 3px solid #1a1a1a;
  border-radius: 12px;
  background: #1f6bff;
  color: #ffffff;
  box-shadow: 4px 4px 0 #1a1a1a;
  font: inherit;
  font-weight: 900;
  cursor: pointer;
}

.dashboard-notice-action:hover {
  transform: translate(-1px, -1px);
  box-shadow: 5px 5px 0 #1a1a1a;
}

@keyframes dashboard-notice-in {
  from {
    opacity: 0;
    transform: translateY(14px) scale(0.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@media (max-width: 520px) {
  .dashboard-notice-card {
    grid-template-columns: 44px 1fr;
    gap: 12px;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 7px 7px 0 #1a1a1a;
  }

  .dashboard-notice-icon {
    width: 42px;
    height: 42px;
    border-radius: 11px;
    font-size: 19px;
  }

  .dashboard-notice-copy h3 {
    font-size: 21px;
  }

  .dashboard-notice-action {
    justify-self: stretch;
  }
}
</style>
"""

notice_html = """
  <div
    v-if="dashboardNotice.isOpen"
    class="dashboard-notice-backdrop"
    role="dialog"
    aria-modal="true"
    aria-labelledby="dashboardNoticeTitle"
    @click.self="closeDashboardNotice"
  >
    <section class="dashboard-notice-card" :class="dashboardNotice.type">
      <div class="dashboard-notice-icon" aria-hidden="true">{{ dashboardNoticeIcon }}</div>
      <div class="dashboard-notice-copy">
        <p class="dashboard-notice-kicker">Checkpoint belajar</p>
        <h3 id="dashboardNoticeTitle">{{ dashboardNotice.title }}</h3>
        <p>{{ dashboardNotice.message }}</p>
      </div>
      <button type="button" class="dashboard-notice-action" @click="closeDashboardNotice">
        {{ dashboardNotice.actionLabel }}
      </button>
    </section>
  </div>
"""

notice_js = """
const dashboardNotice = reactive({
  isOpen: false,
  type: 'warning',
  title: '',
  message: '',
  actionLabel: 'Mengerti'
});
const dashboardNoticeIcon = computed(() => ({
  success: 'OK',
  warning: '!',
  error: '!'
})[dashboardNotice.type] || '!');
const showDashboardNotice = ({ type = 'warning', title = 'Perhatian', message = '', actionLabel = 'Mengerti' } = {}) => {
  dashboardNotice.type = type;
  dashboardNotice.title = title;
  dashboardNotice.message = message;
  dashboardNotice.actionLabel = actionLabel;
  dashboardNotice.isOpen = true;
};
const closeDashboardNotice = () => {
  dashboardNotice.isOpen = false;
};
"""

for repo in repos:
    filepath = os.path.join(repo, 'src/App.vue')
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Inject HTML
    if 'dashboardNotice.isOpen' not in content:
        content = content.replace('</template>', notice_html + '\n</template>')
    
    # 2. Inject CSS
    if '.dashboard-notice-backdrop' not in content:
        if '</style>' in content:
            content = content.replace('</style>', notice_css.replace('<style>\n', '').replace('\n</style>\n', '') + '\n</style>')
        else:
            content += '\n' + notice_css
            
    # 3. Inject JS
    if 'const dashboardNotice =' not in content:
        # inject right after const showLoginError = ref(false);
        content = re.sub(r'(const showLoginError = ref\(false\);.*?)\n', r'\1\n' + notice_js, content)
        
    # 4. Replace alerts
    content = re.sub(
        r'alert\(`Mohon selesaikan video dan kuis/tugas di Modul \$\{i\} terlebih dahulu\.`\);',
        r"showDashboardNotice({ type: 'warning', title: 'Modul belum selesai', message: `Selesaikan video dan kuis/tugas di Modul ${i} terlebih dahulu sebelum membuka modul berikutnya.` });",
        content
    )
    content = re.sub(
        r'alert\(`Mohon selesaikan video dan kuis/tugas di modul ini terlebih dahulu\.`\);',
        r"showDashboardNotice({ type: 'warning', title: 'Modul belum selesai', message: 'Selesaikan video dan kuis/tugas di modul ini terlebih dahulu sebelum lanjut.' });",
        content
    )
    content = re.sub(
        r'alert\("✅ Tugas berhasil dikumpulkan! Progress kamu otomatis tersimpan di server. Selamat kamu telah menyelesaikan Misi Safe Finance Tracker!"\);',
        r"showDashboardNotice({ type: 'success', title: 'Tugas tersimpan', message: 'Progress kamu otomatis tersimpan di server. Selamat, kamu telah menyelesaikan Misi Safe Finance Tracker.' });",
        content
    )
    
    # 5. Patch registerFailedInputAttempt
    content = re.sub(
        r'attemptStatus\.innerHTML = "<strong>Sudah 3 kali mencoba\.</strong><br>Kamu boleh lanjut dulu\. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya\.";',
        r'attemptStatus.innerHTML = "❌ <strong>Kesempatan habis.</strong> Lain kali perhatikan video ya.";',
        content
    )
    content = re.sub(
        r'attemptStatus\.textContent = `Percobaan \$\{attempts\} dari 3\. Periksa kembali kode atau jawabanmu sebelum mencoba lagi\.`;',
        r'let remaining = 3 - attempts; attemptStatus.innerHTML = `❌ Jawaban salah. Sisa ${remaining} kesempatan.`;',
        content
    )
    
    # 6. Patch window.checkGuess (multiple choice)
    content = re.sub(
        r'const attempts = qid \? studentProgress\.value\[`\${qid}_Att`\] \|\| 1 : 1;\s*if \(attempts >= 3\) \{\s*markQuestionFailed\(qid\);\s*feedback\.innerHTML \+= `<br><strong>Sudah 3 kali mencoba\.</strong> Kamu boleh lanjut dulu\. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya\.`;\s*\} else \{\s*buttons\.forEach\(b => \{\s*b\.disabled = false;\s*b\.style\.opacity = \'1\';\s*\}\);\s*\}',
        r'markQuestionFailed(qid);\n      revealQuizNext();',
        content
    )
    
    with open(filepath, 'w') as f:
        f.write(content)

