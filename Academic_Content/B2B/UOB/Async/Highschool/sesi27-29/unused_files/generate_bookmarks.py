import sys
import re
import json
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Silakan install bs4 dulu: pip install beautifulsoup4")
    sys.exit(1)

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("Silakan install youtube_transcript_api dulu: pip install youtube-transcript-api")
    sys.exit(1)

HTML_FILE = "/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2B/UOB/Async/Highschool/sesi27-29/slide_deck_part1.html"
VIDEO_IDS = ["RnyYn2SzFVU", "hP6MSkerx9A"]

def parse_slide_deck(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    slides = soup.find_all('div', class_='slide')
    slide_data = []
    
    for i, slide in enumerate(slides):
        title_el = slide.find(class_='slide-title')
        if not title_el:
            # Some slides have h1 instead
            title_el = slide.find('h1')
            
        title = title_el.get_text(strip=True) if title_el else f"Slide {i+1}"
        
        # Get python code
        code_blocks = slide.find_all('div', class_='code-block')
        codes = [c.get_text(strip=True) for c in code_blocks]
        
        # Get text concepts
        text_blocks = slide.find_all(class_='slide-text')
        texts = [t.get_text(strip=True) for t in text_blocks]
        
        slide_data.append({
            'index': i + 1,
            'title': title,
            'codes': codes,
            'texts': texts
        })
        
    return slide_data

def get_transcripts(video_ids):
    transcripts = {}
    for vid in video_ids:
        try:
            # Mengambil transcript dalam bahasa Indonesia
            transcript = YouTubeTranscriptApi.get_transcript(vid, languages=['id'])
            transcripts[vid] = transcript
        except Exception as e:
            print(f"Gagal mengambil transcript untuk video {vid}: {e}")
            try:
                # Coba ambil auto-generated jika manual tidak ada
                transcript_list = YouTubeTranscriptApi.list_transcripts(vid)
                transcript = transcript_list.find_generated_transcript(['id']).fetch()
                transcripts[vid] = transcript
            except Exception as e2:
                print(f"Juga gagal mengambil auto-generated transcript: {e2}")
    return transcripts

def format_time(seconds):
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

def match_slides_to_transcript(slide_data, transcripts):
    # Flatten transcript into an easily searchable list
    # For simplicity, we just look for keywords from slide titles
    
    for vid, transcript in transcripts.items():
        print(f"\n{'='*50}")
        print(f"VIDEO ID: {vid}")
        print(f"{'='*50}")
        
        for slide in slide_data:
            # Bersihkan judul slide dari emoji dan simbol
            clean_title = re.sub(r'[^\w\s]', '', slide['title']).lower()
            keywords = [w for w in clean_title.split() if len(w) > 3]
            
            if not keywords:
                continue
                
            # Cari di transcript
            matches = []
            for entry in transcript:
                text = entry['text'].lower()
                # Cek apakah ada keyword slide yang diucapkan
                if any(kw in text for kw in keywords):
                    matches.append(entry)
                    
            if matches:
                # Ambil kemunculan pertama sebagai perkiraan mulai
                start_time = matches[0]['start']
                print(f"[{format_time(start_time)}] Slide {slide['index']}: {slide['title']}")
                print(f"   > Konteks ucapan: \"{matches[0]['text']}\"")
                
                # Cek jika ada kode python
                if slide['codes']:
                    print(f"   > Kode Python yang relevan: {slide['codes'][0][:50]}...")

if __name__ == "__main__":
    print(f"Memproses {HTML_FILE}...")
    slides = parse_slide_deck(HTML_FILE)
    print(f"Ditemukan {len(slides)} slide.")
    
    print("Mengunduh transcript video dari YouTube...")
    transcripts = get_transcripts(VIDEO_IDS)
    
    print("Mencocokkan materi dengan ucapan di video...")
    match_slides_to_transcript(slides, transcripts)
    print("\nSelesai! Kamu bisa menggunakan timestamp di atas untuk memperbarui bookmarks.")
