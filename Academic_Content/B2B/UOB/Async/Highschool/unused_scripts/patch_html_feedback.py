import re
import os

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

old_text1 = 'attemptStatus.innerHTML = "<strong>Sudah 3 kali mencoba.</strong><br>Kamu boleh lanjut dulu. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya.";'
new_text1 = 'attemptStatus.innerHTML = "<strong>Sudah 3 kali salah.</strong><br>Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";'

old_text2 = 'feedback.innerHTML += `<br><strong>Sudah 3 kali mencoba.</strong> Kamu boleh lanjut dulu. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya.`;'
new_text2 = 'feedback.innerHTML += `<br><strong>Sudah 3 kali salah.</strong> Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.`;'

old_text3 = 'quizState.value.quizFeedback = "Sudah 3 kali mencoba. Kamu boleh lanjut dulu, tapi perhatikan lagi videonya sebelum masuk ke bagian berikutnya.";'
new_text3 = 'quizState.value.quizFeedback = "Sudah 3 kali salah. Nilai checkpoint ini menjadi 0 dan modul berikutnya tetap terkunci.";'


for repo in repos:
    filepath = f"{repo}/src/App.vue"
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    content = content.replace(old_text1, new_text1)
    content = content.replace(old_text2, new_text2)
    content = content.replace(old_text3, new_text3)
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Patched HTML feedback in {repo}")
