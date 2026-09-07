import os
import re
import urllib.request

WORKSPACE = r"c:\Users\ABHIJIT\Downloads\ccic web"
STEPS_DIR = r"C:\Users\ABHIJIT\.gemini\antigravity-ide\brain\4bedf0fd-8c82-4466-a618-a9f3506d0a2a\.system_generated\steps"

TEMPLATES_DIR = os.path.join(WORKSPACE, "templates")
STATIC_IMG_DIR = os.path.join(WORKSPACE, "static", "images")
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(STATIC_IMG_DIR, exist_ok=True)

files_to_extract = [
    ("33", "index.html"),
    ("41", "events.html"),
    ("45", "magic_members.html"),
    ("47", "scope_members.html"),
]

for step, filename in files_to_extract:
    content_file = os.path.join(STEPS_DIR, step, "content.md")
    if os.path.exists(content_file):
        with open(content_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Find start of HTML
        html_start_idx = 0
        for i, line in enumerate(lines):
            if "<!DOCTYPE html" in line or "<html" in line:
                html_start_idx = i
                break
        html_content = "".join(lines[html_start_idx:])
        
        target_path = os.path.join(TEMPLATES_DIR, filename)
        with open(target_path, "w", encoding="utf-8") as out:
            out.write(html_content)
        print(f"Extracted {filename} ({len(html_content)} bytes)")
    else:
        print(f"File not found: {content_file}")

# Download assets
images = {
    "ccic_logo.jpg": "https://lh3.googleusercontent.com/aida/AEtjO1X5Zf7wbgy7q5keOlpodNfu2DAkYz2HozRjFIEJ1AzHzN7yiN1iiE2XlfBQTXIZn0z7SieiAb0XJA4zu3bXXHzPpZuo6yTEio1J1pQeua4HeSgt6ZTrqoHg51Bm0EQtEq4jebVIkqDSUsvxsl4PDvsuBQFiOD8UdgZicIHzJNDpEjv_PJITteekQEj4nYdov7w7jM44duyDIBAJMwAsM6M_jxLw0wIw2-HKU5ljIaNqx48EKccXZVGnLbSonXTNVoJSYxeU4m6yvA",
    "ccic_banner.jpg": "https://lh3.googleusercontent.com/aida/AEtjO1XmF_JQUp5ZrvWXq86_Kl9010YZCrw9ijsXcK0dGEszxSNUxexp5OeZM5Z1suq9fEUoPyniSAIiCaxreNYdPXF4GrXf1kBTIUjooa1GCJcggIYkSid3QaeBri8_-3SRYPcm_QTE8K9lnlsu7mGt7l1XLX2eCwFkKUXDL9AAcv8YL8i-p7rSnt7yxUuQF5jeQmWfE8V-nyuHbyaSBMwGoOUUBUIzS4vpY1n9ZDZZLAG52ai6oPEXa1O0cYqZcxAbXchNSEMdh-E4XA",
    "ccic_group.jpg": "https://lh3.googleusercontent.com/aida/AEtjO1Uq2liu7iRkgM9iCZ2Qm-tNCU1idYXQbJJD0b3lc6AWL0JL7Ss5Hhdz0GDH71wabWu7rFIiA2x-E0jhNs_Xo6S9Yj8OAJEm1gvMnJw4pd4X7v2B9JM00EvvAfKc_GodFM1aj0lzhKyEmuc9Gy2XA4TDto4M8egRuH0wZKR82AyE1bVPaAsFf0Mf720cUqyRbyHWyCVwwBy83ueFhDOtKvFumoUXU4MM4nHmyMb1n6f9Wgiu0-jjRTJ2oC3Cv0IaeL0sCG-BJRb3Ig"
}

for img_name, url in images.items():
    img_path = os.path.join(STATIC_IMG_DIR, img_name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(img_path, 'wb') as out_f:
            out_f.write(resp.read())
        print(f"Downloaded {img_name}")
    except Exception as e:
        print(f"Failed to download {img_name}: {e}")
