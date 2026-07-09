with open('sesi25-26/grup-hs-2-a/src/courseData.js', 'r') as f:
    content = f.read()
    
old_html = """{
            html: `
              <h2 class="slide-title">Selesai Menonton! 🎉</h2>"""
new_html = """{
            type: "info",
            html: `
              <h2 class="slide-title">Selesai Menonton! 🎉</h2>"""

content = content.replace(old_html, new_html)

with open('sesi25-26/grup-hs-2-a/src/courseData.js', 'w') as f:
    f.write(content)
