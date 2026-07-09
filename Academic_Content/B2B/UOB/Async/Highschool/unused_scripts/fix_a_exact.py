with open('sesi25-26/grup-hs-2-a/src/courseData.js', 'r') as f:
    content = f.read()

idx = content.find('<h2 class="slide-title">Selesai Menonton! 🎉</h2>')
if idx != -1:
    # find the preceding "html: `"
    html_idx = content.rfind('html: `', 0, idx)
    if html_idx != -1:
        # replace it with type: "info", html: `
        content = content[:html_idx] + 'type: "info",\n            ' + content[html_idx:]

with open('sesi25-26/grup-hs-2-a/src/courseData.js', 'w') as f:
    f.write(content)
