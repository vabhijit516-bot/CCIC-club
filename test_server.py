import os
import json
import pandas as pd
from app import app
from database.db import get_all_submissions, sync_csv_and_excel
from config import Config

def run_tests():
    client = app.test_client()
    print("Testing CCIC Web Application...")
    
    # 1. Page Routes
    pages = ["/", "/events", "/magic-members", "/scope-members", "/register", "/login", "/admin"]
    for page in pages:
        res = client.get(page)
        assert res.status_code == 200, f"Page {page} returned status {res.status_code}"
        print(f"  [PASS] Page {page} (Status: {res.status_code})")
        
    # 2. Form Submission API
    test_candidate = {
        "name": "Harish Kumar",
        "roll_no": "22AM099",
        "email": "harish.k@sairam.edu.in",
        "phone": "+91 98409 11223",
        "department": "CSE (AI & ML)",
        "year": "3rd Year",
        "domain": "Natural Language Processing",
        "linkedin_github": "https://github.com/harish-nlp",
        "motivation": "Excited to work with LLM architectures and automated reasoning agents in CCIC."
    }
    
    reg_res = client.post("/api/register", data=json.dumps(test_candidate), content_type="application/json")
    assert reg_res.status_code == 201, f"POST /api/register failed with {reg_res.status_code}"
    reg_data = json.loads(reg_res.data)
    assert reg_data.get("success") is True, "Registration response success was not True"
    candidate_id = reg_data.get("id")
    print(f"  [PASS] POST /api/register created Application #{candidate_id}")
    
    # 3. Verify SQLite records
    all_subs = get_all_submissions()
    found = any(s["email"] == "harish.k@sairam.edu.in" for s in all_subs)
    assert found, "New submission was not found in SQLite"
    print(f"  [PASS] SQLite record verified (Total submissions: {len(all_subs)})")
    
    # 4. Verify CSV and Excel files
    assert os.path.exists(Config.CSV_PATH), "CSV file does not exist"
    assert os.path.exists(Config.EXCEL_PATH), "Excel file does not exist"
    
    with open(Config.CSV_PATH, "r", encoding="utf-8") as f:
        csv_text = f.read()
    assert "harish.k@sairam.edu.in" in csv_text, "Candidate not found in CSV file"
    print("  [PASS] Real-time CSV file updated and verified")
    
    df_excel = pd.read_excel(Config.EXCEL_PATH)
    assert "harish.k@sairam.edu.in" in df_excel["Email Address"].values, "Candidate not found in Excel file"
    print("  [PASS] Real-time Excel (.xlsx) file updated and verified")
    
    # 5. Admin Download Endpoints
    csv_dl = client.get("/api/admin/export/csv")
    assert csv_dl.status_code == 200, f"CSV download failed with {csv_dl.status_code}"
    assert "text/csv" in csv_dl.content_type, f"Unexpected CSV mime: {csv_dl.content_type}"
    print("  [PASS] Admin CSV Download Endpoint (HTTP 200, text/csv)")
    
    excel_dl = client.get("/api/admin/export/excel")
    assert excel_dl.status_code == 200, f"Excel download failed with {excel_dl.status_code}"
    assert "spreadsheet" in excel_dl.content_type, f"Unexpected Excel mime: {excel_dl.content_type}"
    print("  [PASS] Admin Excel (.xlsx) Download Endpoint (HTTP 200, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)")
    
    # 6. Status Update API
    update_res = client.post("/api/admin/update-status", data=json.dumps({"id": candidate_id, "status": "Approved"}), content_type="application/json")
    assert update_res.status_code == 200
    assert json.loads(update_res.data).get("success") is True
    print(f"  [PASS] Application #{candidate_id} status updated to Approved")
    
    # 7. Stats API
    stats_res = client.get("/api/stats")
    assert stats_res.status_code == 200
    stats = json.loads(stats_res.data)
    assert stats["total"] >= 6
    print(f"  [PASS] Stats API verified: {stats['total']} total applicants")
    
    print("\nALL SYSTEM TESTS PASSED SUCCESSFULLY! [OK]")

if __name__ == "__main__":
    run_tests()
