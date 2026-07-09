import os
import glob
import re

directories = [
    "../sesi25-26/grup-hs-2-a/src",
    "../sesi27-29/grup-hs-2-b/src",
    "../sesi30-32/grup-hs-2-c/src",
    "../sesi40-44/grup-hs-2-d/src"
]

for d in directories:
    app_vue_path = os.path.join(d, "App.vue")
    if not os.path.exists(app_vue_path):
        continue
    
    with open(app_vue_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update handleStandardAnswer
    content = re.sub(
        r'quizState\.value\.quizFeedback\s*=\s*"Sudah 3 kali mencoba\. Modul berikutnya tetap terkunci\. Silakan ulangi bagian video ini untuk mencoba lagi\.";',
        'quizState.value.quizFeedback = "<strong>Sudah 3 kali mencoba.</strong><br>Kamu boleh lanjut dulu. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya.";\n      revealQuizNext("Lanjut →");',
        content
    )
    
    # 2. Update registerFailedInputAttempt
    content = re.sub(
        r'attemptStatus\.innerHTML\s*=\s*"<strong>Sudah 3 kali mencoba\.</strong><br>Modul berikutnya tetap terkunci\. Silakan ulangi bagian video ini untuk mencoba lagi\.";',
        'attemptStatus.innerHTML = "<strong>Sudah 3 kali mencoba.</strong><br>Kamu boleh lanjut dulu. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya.";\n    revealQuizNext("Lanjut →");',
        content
    )

    # 3. Update window.checkGuess / custom HTML feedback
    content = re.sub(
        r'feedback\.innerHTML\s*\+=\s*`<br><strong>Sudah 3 kali mencoba\.</strong> Modul berikutnya tetap terkunci\. Silakan ulangi bagian video ini untuk mencoba lagi\.`;',
        'feedback.innerHTML += `<br><strong>Sudah 3 kali mencoba.</strong> Kamu boleh lanjut dulu. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya.`;\n        revealQuizNext("Lanjut →");',
        content
    )

    # 4. Update submitInputAnswer / submitEssayAnswer if they don't have revealQuizNext("Lanjut →")
    # This was already done for grup-hs-2-b, but we need to do it for a, c, d
    # Old logic:
    # } else {
    #   registerTypedWrongAttempt(item, input);
    # }
    content = re.sub(
        r'\} else \{\s*registerTypedWrongAttempt\(item, input\);\s*\}',
        '} else {\n    const isLimitReached = registerTypedWrongAttempt(item, input);\n    if (isLimitReached) revealQuizNext("Lanjut →");\n  }',
        content
    )
    
    with open(app_vue_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {app_vue_path}")
