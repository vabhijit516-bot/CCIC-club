import os
import shutil

SRC_DIR = r"C:\Users\ABHIJIT\.gemini\antigravity-ide\brain\4bedf0fd-8c82-4466-a618-a9f3506d0a2a\.user_uploaded"
DST_DIR = r"c:\Users\ABHIJIT\Downloads\ccic web\static\images"

os.makedirs(DST_DIR, exist_ok=True)

mapping = {
    "media_1788799283754.jpg": "ebenezer.jpg",
    "media_1788799283782.jpg": "anitha.jpg",
    "media_1788799283793.jpg": "mathupriya.jpg",
    "media_1788799362585.jpg": "haripriyan.jpg",
    "media_1788799362596.jpg": "guru.jpg"
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(SRC_DIR, src_name)
    dst_path = os.path.join(DST_DIR, dst_name)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dst_path)
        print(f"Copied {src_name} -> {dst_name} ({os.path.getsize(dst_path)} bytes)")
    else:
        print(f"Not found: {src_path}")
