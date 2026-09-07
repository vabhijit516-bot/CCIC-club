from database.db import init_db, get_all_submissions, get_stats
import os

init_db()
submissions = get_all_submissions()
print(f"Total count: {len(submissions)}")
print("Stats:", get_stats())
print("CSV exists:", os.path.exists("data/submissions.csv"))
print("Excel exists:", os.path.exists("data/submissions.xlsx"))
