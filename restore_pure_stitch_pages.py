import os
import shutil
import re

WORKSPACE = r"c:\Users\ABHIJIT\Downloads\ccic web"
STEPS_DIR = r"C:\Users\ABHIJIT\.gemini\antigravity-ide\brain\4bedf0fd-8c82-4466-a618-a9f3506d0a2a\.system_generated\steps"

# 1. Read Step 33 (Home Stitch screen)
with open(os.path.join(STEPS_DIR, "33", "content.md"), "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

start = next(i for i, l in enumerate(raw_lines) if "<!DOCTYPE html" in l or "<html" in l)
home_html = "".join(raw_lines[start:])

# Fix header sticky & padding in Home
home_html = home_html.replace(
    '<header class="fixed top-0 left-0 w-full z-50 shadow-[0_1px_8px_rgba(0,0,0,0.04)]">',
    '<header class="sticky top-0 left-0 w-full z-50 shadow-[0_1px_8px_rgba(0,0,0,0.04)] bg-surface">'
)
home_html = home_html.replace(
    '<main class="w-full pt-20 relative z-10 bg-transparent min-h-screen">',
    '<main class="w-full pt-0 relative z-10 bg-transparent min-h-screen">'
)

# Connect navbar links
old_nav_pattern = r'<nav class="hidden xl:flex items-center gap-space-xs".*?</nav>'
new_nav = '''<nav class="hidden xl:flex items-center gap-space-xs font-label-md text-label-md">
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 bg-secondary-container text-on-secondary font-bold" href="/">Home</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="/events">Activities & Events</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="/magic-members">Magic Members</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="/scope-members">Scope Members</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="/register">Register</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-amber-700 font-semibold hover:bg-amber-50" href="/admin">Admin</a>
</nav>'''

home_html = re.sub(old_nav_pattern, new_nav, home_html, flags=re.DOTALL)

# Update right auth button to Register/Sign In
old_user_icon = '<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center shadow-sm"><span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div>'
new_auth_buttons = '''<div class="ccic-nav-auth flex items-center gap-2">
<a href="/login" class="px-3 py-1.5 text-xs font-semibold rounded-md border border-outline-variant text-on-surface hover:bg-surface-container transition">Sign In</a>
<a href="/register" class="px-3 py-1.5 text-xs font-semibold rounded-md bg-secondary text-white hover:bg-opacity-90 transition shadow-sm">Join</a>
</div>'''
home_html = home_html.replace(old_user_icon, new_auth_buttons)

# Add transitions css and smooth scroll js
if "transitions.css" not in home_html:
    home_html = home_html.replace("<head>", '<head><link rel="stylesheet" href="/static/css/transitions.css">')
if "smooth-scroll.js" not in home_html:
    home_html = home_html.replace("</body>", '<script src="/static/js/smooth-scroll.js"></script>\n</body>')

# Replace remote logo with local logo
home_html = home_html.replace("https://lh3.googleusercontent.com/aida/AEtjO1X5Zf7wbgy7q5keOlpodNfu2DAkYz2HozRjFIEJ1AzHzN7yiN1iiE2XlfBQTXIZn0z7SieiAb0XJA4zu3bXXHzPpZuo6yTEio1J1pQeua4HeSgt6ZTrqoHg51Bm0EQtEq4jebVIkqDSUsvxsl4PDvsuBQFiOD8UdgZicIHzJNDpEjv_PJITteekQEj4nYdov7w7jM44duyDIBAJMwAsM6M_jxLw0wIw2-HKU5ljIaNqx48EKccXZVGnLbSonXTNVoJSYxeU4m6yvA", "/static/images/ccic_logo.jpg")

# Write to templates/index.html and root index.html
with open(os.path.join(WORKSPACE, "templates", "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)
with open(os.path.join(WORKSPACE, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)
print("Restored pure Stitch index.html")

# 2. Copy all other templates to root directory for Vercel static serving
pages = [
    ("events.html", "events.html"),
    ("magic_members.html", "magic_members.html"),
    ("scope_members.html", "scope_members.html"),
    ("register.html", "register.html"),
    ("admin.html", "admin.html"),
    ("login.html", "login.html")
]

for src_name, dest_name in pages:
    src_path = os.path.join(WORKSPACE, "templates", src_name)
    dest_path = os.path.join(WORKSPACE, dest_name)
    shutil.copy2(src_path, dest_path)
    print(f"Copied {src_name} to root {dest_name}")

# 3. Create vercel.json with clean rewrites for all pages
vercel_config = '''{
  "version": 2,
  "cleanUrls": true,
  "trailingSlash": false,
  "rewrites": [
    { "source": "/", "destination": "/index.html" },
    { "source": "/events", "destination": "/events.html" },
    { "source": "/magic-members", "destination": "/magic_members.html" },
    { "source": "/scope-members", "destination": "/scope_members.html" },
    { "source": "/register", "destination": "/register.html" },
    { "source": "/admin", "destination": "/admin.html" },
    { "source": "/login", "destination": "/login.html" }
  ]
}
'''

with open(os.path.join(WORKSPACE, "vercel.json"), "w", encoding="utf-8") as f:
    f.write(vercel_config)
print("Updated vercel.json with clean routes for all Stitch pages")
