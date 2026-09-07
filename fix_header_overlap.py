import os

TEMPLATES = [
    r"c:\Users\ABHIJIT\Downloads\ccic web\templates\index.html",
    r"c:\Users\ABHIJIT\Downloads\ccic web\templates\events.html",
    r"c:\Users\ABHIJIT\Downloads\ccic web\templates\magic_members.html",
    r"c:\Users\ABHIJIT\Downloads\ccic web\templates\scope_members.html"
]

for tpath in TEMPLATES:
    if not os.path.exists(tpath):
        continue
    with open(tpath, "r", encoding="utf-8") as f:
        c = f.read()

    # Change fixed header to sticky header
    c = c.replace(
        '<header class="fixed top-0 left-0 w-full z-50 shadow-[0_1px_8px_rgba(0,0,0,0.04)]">',
        '<header class="sticky top-0 left-0 w-full z-50 shadow-[0_1px_8px_rgba(0,0,0,0.04)] bg-surface">'
    )

    # Change main pt-20 to pt-0 so content naturally starts right below sticky header
    c = c.replace(
        '<main class="w-full pt-20 relative z-10 bg-transparent min-h-screen">',
        '<main class="w-full pt-0 relative z-10 bg-transparent min-h-screen">'
    )

    with open(tpath, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Updated {os.path.basename(tpath)}")

# Update static/css/transitions.css to enforce proper sticky header positioning and no overlap
CSS_PATH = r"c:\Users\ABHIJIT\Downloads\ccic web\static\css\transitions.css"
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css_content = f.read()

header_fix = """
/* Fix Header Sticking & Prevent Content Behind the Bar from being Clipped */
header.sticky {
    position: sticky !important;
    top: 0 !important;
    z-index: 50 !important;
}

header.sticky + main,
main.pt-0 {
    padding-top: 0 !important;
}
"""

if "Fix Header Sticking" not in css_content:
    css_content += header_fix
    with open(CSS_PATH, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated transitions.css with sticky header fix")
