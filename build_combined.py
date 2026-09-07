import os
import re

def extract_main_inner(filename):
    with open(f"templates/{filename}.html", "r", encoding="utf-8") as f:
        content = f.read()
    m_start = content.find("<main")
    if m_start == -1:
        return ""
    tag_end = content.find(">", m_start) + 1
    m_end = content.find("</main>")
    return content[tag_end:m_end].strip()

home_main = extract_main_inner("index")
events_main = extract_main_inner("events")
magic_main = extract_main_inner("magic_members")
scope_main = extract_main_inner("scope_members")
register_main = extract_main_inner("register")
admin_main = extract_main_inner("admin")

print(f"Home length: {len(home_main)}")
print(f"Events length: {len(events_main)}")
print(f"Magic length: {len(magic_main)}")
print(f"Scope length: {len(scope_main)}")
print(f"Register length: {len(register_main)}")
print(f"Admin length: {len(admin_main)}")
