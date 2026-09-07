import os
from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
from config import Config
from database.db import init_db, add_submission, get_all_submissions, update_submission_status, get_stats, sync_csv_and_excel

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)

# Ensure database and files are initialized on app startup
with app.app_context():
    init_db()

# --- Page Routes ---

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/events")
@app.route("/events.html")
def events():
    return render_template("events.html")

@app.route("/magic-members")
@app.route("/magic-members.html")
@app.route("/magic_members")
@app.route("/magic_members.html")
def magic_members():
    return render_template("magic_members.html")

@app.route("/scope-members")
@app.route("/scope-members.html")
@app.route("/scope_members")
@app.route("/scope_members.html")
def scope_members():
    return render_template("scope_members.html")

@app.route("/register")
@app.route("/register.html")
def register_page():
    return render_template("register.html")

@app.route("/login")
@app.route("/login.html")
def login_page():
    return render_template("login.html")

@app.route("/admin")
@app.route("/admin.html")
def admin_page():
    return render_template("admin.html")

# --- API Endpoints ---

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "Invalid request payload"}), 400
    
    required_fields = ["name", "roll_no", "email", "phone", "department", "year", "domain"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"success": False, "error": f"Field '{field}' is required"}), 400
            
    try:
        new_id = add_submission(data)
        return jsonify({
            "success": True,
            "id": new_id,
            "message": "Application submitted successfully! Our coordinators will review your submission."
        }), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/admin/submissions", methods=["GET"])
def admin_submissions():
    search = request.args.get("search")
    domain = request.args.get("domain")
    status = request.args.get("status")
    
    try:
        submissions = get_all_submissions(search, domain, status)
        return jsonify({"success": True, "submissions": submissions})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/admin/update-status", methods=["POST"])
def admin_update_status():
    data = request.get_json()
    if not data or "id" not in data or "status" not in data:
        return jsonify({"success": False, "error": "ID and Status are required"}), 400
        
    try:
        success = update_submission_status(data["id"], data["status"])
        return jsonify({"success": success})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/stats", methods=["GET"])
def stats():
    try:
        data = get_stats()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- CSV & Excel Download Endpoints ---

@app.route("/api/admin/export/csv", methods=["GET"])
def export_csv():
    sync_csv_and_excel()
    if not os.path.exists(Config.CSV_PATH):
        return jsonify({"error": "CSV file not found"}), 404
        
    return send_file(
        Config.CSV_PATH,
        mimetype="text/csv",
        as_attachment=True,
        download_name="CCIC_AIML_Submissions.csv"
    )

@app.route("/api/admin/export/excel", methods=["GET"])
def export_excel():
    sync_csv_and_excel()
    if not os.path.exists(Config.EXCEL_PATH):
        return jsonify({"error": "Excel file not found"}), 404
        
    return send_file(
        Config.EXCEL_PATH,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="CCIC_AIML_Submissions.xlsx"
    )

# --- Session / Auth Endpoints ---

@app.route("/api/auth/session", methods=["POST"])
def sync_session():
    data = request.get_json() or {}
    session["user"] = data
    return jsonify({"success": True, "user": session.get("user")})

@app.route("/api/auth/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify({"success": True})

@app.route("/api/auth/current", methods=["GET"])
def current_user():
    return jsonify({"user": session.get("user")})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f">> CCIC AIML Club Portal server running at http://localhost:{port}")
    print(f">> Localhost link: http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
