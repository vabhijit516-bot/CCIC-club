import os
import sqlite3
from datetime import datetime
import pandas as pd
from config import Config

def get_db_connection():
    conn = sqlite3.connect(Config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Submissions table for registrations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_no TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        department TEXT NOT NULL,
        year TEXT NOT NULL,
        domain TEXT NOT NULL,
        linkedin_github TEXT,
        motivation TEXT,
        status TEXT DEFAULT 'Pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT UNIQUE,
        email TEXT UNIQUE NOT NULL,
        display_name TEXT,
        role TEXT DEFAULT 'member',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    
    # Seed initial test data if table is completely empty
    cursor.execute("SELECT COUNT(*) FROM submissions")
    count = cursor.fetchone()[0]
    if count == 0:
        seed_sample_data(cursor)
        conn.commit()
        
    conn.close()
    
    # Sync files
    sync_csv_and_excel()

def seed_sample_data(cursor):
    sample_records = [
        ("Aravind Swaminathan", "21AM012", "aravind.s@sairam.edu.in", "+91 98401 23456", "CSE (AI & ML)", "3rd Year", "Computer Vision & Generative AI", "github.com/aravind-ai", "Passionate about building state-of-the-art vision models for healthcare diagnosis.", "Approved"),
        ("Divya Krishnan", "22AM045", "divya.k@sairam.edu.in", "+91 97102 34567", "CSE (AI & ML)", "2nd Year", "Natural Language Processing", "linkedin.com/in/divyakrishnan", "Eager to contribute to CCIC NLP research labs and open-source LLM agents.", "Pending"),
        ("Karthik Raja", "21CS089", "karthik.r@sairam.edu.in", "+91 94440 98765", "Computer Science", "3rd Year", "Deep Reinforcement Learning & Robotics", "github.com/karthik-robolab", "Building autonomous robotics algorithms and edge AI controllers.", "Approved"),
        ("Sneha Ramesh", "23AM078", "sneha.r@sairam.edu.in", "+91 98841 54321", "CSE (AI & ML)", "1st Year", "Machine Learning & Data Science", "github.com/sneha-codes", "Enthusiastic beginner in ML eager to learn and participate in national hackathons.", "Reviewed"),
        ("Rahul Varman", "22IT033", "rahul.v@sairam.edu.in", "+91 98412 67890", "Information Technology", "2nd Year", "Edge AI & IoT Systems", "linkedin.com/in/rahulvarman", "Developing low-latency TinyML applications for industrial edge sensors.", "Pending")
    ]
    cursor.executemany("""
    INSERT INTO submissions (name, roll_no, email, phone, department, year, domain, linkedin_github, motivation, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_records)

def add_submission(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO submissions (name, roll_no, email, phone, department, year, domain, linkedin_github, motivation, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Pending')
    """, (
        data.get("name"),
        data.get("roll_no"),
        data.get("email"),
        data.get("phone"),
        data.get("department"),
        data.get("year"),
        data.get("domain"),
        data.get("linkedin_github", ""),
        data.get("motivation", "")
    ))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    # Automatically update CSV and Excel
    sync_csv_and_excel()
    return new_id

def get_all_submissions(search=None, domain_filter=None, status_filter=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM submissions WHERE 1=1"
    params = []
    
    if search:
        query += " AND (name LIKE ? OR roll_no LIKE ? OR email LIKE ? OR department LIKE ?)"
        wildcard = f"%{search}%"
        params.extend([wildcard, wildcard, wildcard, wildcard])
        
    if domain_filter and domain_filter != "All":
        query += " AND domain = ?"
        params.append(domain_filter)
        
    if status_filter and status_filter != "All":
        query += " AND status = ?"
        params.append(status_filter)
        
    query += " ORDER BY id DESC"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    submissions = [dict(row) for row in rows]
    conn.close()
    return submissions

def update_submission_status(submission_id, new_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE submissions SET status = ? WHERE id = ?", (new_status, submission_id))
    conn.commit()
    conn.close()
    sync_csv_and_excel()
    return True

def get_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM submissions")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT status, COUNT(*) FROM submissions GROUP BY status")
    status_counts = dict(cursor.fetchall())
    
    cursor.execute("SELECT domain, COUNT(*) FROM submissions GROUP BY domain")
    domain_counts = dict(cursor.fetchall())
    
    cursor.execute("SELECT department, COUNT(*) FROM submissions GROUP BY department")
    dept_counts = dict(cursor.fetchall())
    
    cursor.execute("SELECT year, COUNT(*) FROM submissions GROUP BY year")
    year_counts = dict(cursor.fetchall())
    
    conn.close()
    return {
        "total": total,
        "status": status_counts,
        "domains": domain_counts,
        "departments": dept_counts,
        "years": year_counts
    }

def sync_csv_and_excel():
    """Reads all submissions from SQLite and exports cleanly to CSV and Excel."""
    try:
        conn = get_db_connection()
        df = pd.read_sql_query("SELECT id, name, roll_no, email, phone, department, year, domain, linkedin_github, motivation, status, created_at FROM submissions ORDER BY id DESC", conn)
        conn.close()
        
        # Friendly column names for Excel and CSV
        df_export = df.rename(columns={
            "id": "Application ID",
            "name": "Full Name",
            "roll_no": "Roll Number",
            "email": "Email Address",
            "phone": "Phone Number",
            "department": "Department",
            "year": "Year of Study",
            "domain": "Domain of Interest",
            "linkedin_github": "Portfolio / GitHub / LinkedIn",
            "motivation": "Motivation / Statement",
            "status": "Application Status",
            "created_at": "Submission Date & Time"
        })
        
        # Save CSV
        df_export.to_csv(Config.CSV_PATH, index=False, encoding="utf-8")
        
        # Save Excel with formatting
        with pd.ExcelWriter(Config.EXCEL_PATH, engine="openpyxl") as writer:
            df_export.to_excel(writer, sheet_name="CCIC Registrations", index=False)
            
        return True
    except Exception as e:
        print(f"Error syncing CSV/Excel: {e}")
        return False
