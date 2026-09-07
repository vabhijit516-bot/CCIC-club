import urllib.request

res = urllib.request.urlopen('http://127.0.0.1:5000/')
html = res.read().decode('utf-8')
print('Status:', res.status)
print('Page size in bytes:', len(html))

sections = ['home', 'events', 'magic-members', 'scope-members', 'register', 'admin']
for s in sections:
    found = f'id="{s}"' in html
    print(f'Section #{s} found: {found}')

scripts = ['xlsx.full.min.js', 'unified-app.js', 'smooth-scroll.js']
for sc in scripts:
    found = sc in html
    print(f'Script {sc} present: {found}')

images = ['ccic_logo.jpg', 'mukesh.jpg', 'dhanasekaran.jpg', 'abhijit.jpg', 'ebenezer.jpg', 'anitha.jpg', 'mathupriya.jpg', 'haripriyan.jpg', 'guru.jpg']
for img in images:
    found = img in html
    print(f'Image {img} present: {found}')
