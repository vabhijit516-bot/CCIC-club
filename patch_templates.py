import os
import re

TEMPLATES_DIR = r"c:\Users\ABHIJIT\Downloads\ccic web\templates"

PAGES = [
    ("index.html", "home"),
    ("events.html", "activities-&-events"),
    ("magic_members.html", "magic-members"),
    ("scope_members.html", "scope-members")
]

# Shared scripts to inject before </body>
SCRIPTS_SNIPPET = """
<!-- Firebase Client SDK & CCIC Authentication -->
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-auth-compat.js"></script>
<script src="/static/js/firebase-config.js"></script>
<script src="/static/js/auth.js"></script>
</body>
"""

for filename, active_page in PAGES:
    filepath = os.path.join(TEMPLATES_DIR, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace logo URLs with local asset
    content = re.sub(r'https://lh3\.googleusercontent\.com/aida/AEtjO1X5Zf7wbgy7q5keOlpodNfu2DAkYz2HozRjFIEJ1AzHzN7yiN1iiE2XlfBQTXIZn0z7SieiAb0XJA4zu3bXXHzPpZuo6yTEio1J1pQeua4HeSgt6ZTrqoHg51Bm0EQtEq4jebVIkqDSUsvxsl4PDvsuBQFiOD8UdgZicIHzJNDpEjv_PJITteekQEj4nYdov7w7jM44duyDIBAJMwAsM6M_jxLw0wIw2-HKU5ljIaNqx48EKccXZVGnLbSonXTNVoJSYxeU4m6yvA', '/static/images/ccic_logo.jpg', content)

    # 2. Build responsive navigation bar
    nav_pattern = r'<nav class="hidden xl:flex items-center gap-space-xs"[^>]*>.*?</nav>'
    
    home_class = "bg-secondary-container text-on-secondary font-bold" if active_page == "home" else "text-on-surface-variant hover:bg-surface-container hover:text-on-surface"
    scope_class = "bg-secondary-container text-on-secondary font-bold" if active_page == "scope-members" else "text-on-surface-variant hover:bg-surface-container hover:text-on-surface"
    magic_class = "bg-secondary-container text-on-secondary font-bold" if active_page == "magic-members" else "text-on-surface-variant hover:bg-surface-container hover:text-on-surface"
    events_class = "bg-secondary-container text-on-secondary font-bold" if active_page == "activities-&-events" else "text-on-surface-variant hover:bg-surface-container hover:text-on-surface"

    replacement_nav = f"""<nav class="hidden xl:flex items-center gap-space-xs font-label-md text-label-md">
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 {home_class}" href="/">Home</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 {events_class}" href="/events">Activities & Events</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 {magic_class}" href="/magic-members">Magic Members</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 {scope_class}" href="/scope-members">Scope Members</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="/register">Register</a>
<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-amber-700 font-semibold hover:bg-amber-50" href="/admin">Admin</a>
</nav>"""

    content = re.sub(nav_pattern, replacement_nav, content, flags=re.DOTALL)

    # 3. Replace user avatar container with ccic-nav-auth
    auth_container_pattern = r'<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center shadow-sm"><span class="material-symbols-outlined text-on-primary text-\[18px\]">person</span></div>'
    replacement_auth = """<div class="ccic-nav-auth flex items-center gap-2">
<a href="/login" class="px-3 py-1.5 text-xs font-semibold rounded-md border border-outline-variant text-on-surface hover:bg-surface-container transition">Sign In</a>
<a href="/register" class="px-3 py-1.5 text-xs font-semibold rounded-md bg-secondary text-white hover:bg-opacity-90 transition shadow-sm">Join</a>
</div>"""
    content = re.sub(auth_container_pattern, replacement_auth, content)

    # 4. Inject Firebase & auth scripts before </body> if not present
    if "static/js/auth.js" not in content:
        content = content.replace("</body>", SCRIPTS_SNIPPET)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Patched {filename}")
