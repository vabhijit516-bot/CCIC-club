import os
from dotenv import load_dotenv

load_dotenv()

import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if os.environ.get("VERCEL"):
    DATA_DIR = "/tmp/data"
    DATABASE_DIR = "/tmp/database"
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(DATABASE_DIR, exist_ok=True)
    src_db = os.path.join(BASE_DIR, "database", "ccic.db")
    tmp_db = os.path.join(DATABASE_DIR, "ccic.db")
    if os.path.exists(src_db) and not os.path.exists(tmp_db):
        try:
            shutil.copy2(src_db, tmp_db)
        except Exception:
            pass
else:
    DATA_DIR = os.path.join(BASE_DIR, "data")
    DATABASE_DIR = os.path.join(BASE_DIR, "database")
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(DATABASE_DIR, exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "ccic-sairam-aiml-portal-secret-key-2026")
    DB_PATH = os.path.join(DATABASE_DIR, "ccic.db")
    CSV_PATH = os.path.join(DATA_DIR, "submissions.csv")
    EXCEL_PATH = os.path.join(DATA_DIR, "submissions.xlsx")
    
    # Designated admin emails
    ADMIN_EMAILS = [
        "admin@sairam.edu.in",
        "ccic.aiml@sairam.edu.in",
        "admin@ccic.org",
        "coordinator@sairam.edu.in",
        "abhijit@sairam.edu.in"
    ]
    
    # Optional Firebase service account key path
    FIREBASE_CREDENTIALS = os.environ.get("FIREBASE_CREDENTIALS", None)
