import os

TEMPLATES_DIR = r"c:\Users\ABHIJIT\Downloads\ccic web\templates"
CSS_INJECT = '<link rel="stylesheet" href="/static/css/transitions.css">\n'
JS_INJECT = '<script src="/static/js/smooth-scroll.js"></script>\n'

for fname in os.listdir(TEMPLATES_DIR):
    if not fname.endswith(".html"):
        continue
    fpath = os.path.join(TEMPLATES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False
    if "/static/css/transitions.css" not in content:
        if "</head>" in content:
            content = content.replace("</head>", f"{CSS_INJECT}</head>")
            modified = True
        else:
            content = CSS_INJECT + content
            modified = True

    if "/static/js/smooth-scroll.js" not in content:
        if "</body>" in content:
            content = content.replace("</body>", f"{JS_INJECT}</body>")
            modified = True
        else:
            content = content + JS_INJECT
            modified = True

    if modified:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added transitions to {fname}")
    else:
        print(f"Already present in {fname}")
