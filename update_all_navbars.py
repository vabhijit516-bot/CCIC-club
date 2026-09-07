import os
import re

html_files = [
    'index.html', 'templates/index.html',
    'events.html', 'templates/events.html',
    'magic_members.html', 'magic-members.html', 'templates/magic_members.html', 'templates/magic-members.html',
    'scope_members.html', 'scope-members.html', 'templates/scope_members.html', 'templates/scope-members.html',
    'register.html', 'templates/register.html',
    'admin.html', 'templates/admin.html',
    'login.html', 'templates/login.html',
    'about.html', 'templates/about.html'
]

about_link_inactive = '<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="/about">About</a>'
about_link_active = '<a class="px-space-sm py-space-2xs rounded-lg transition-all duration-200 bg-secondary-container text-on-secondary font-bold" href="/about">About</a>'

top_header_with_socials = '''<div class="w-full bg-primary-container text-on-primary-container px-space-md py-space-2xs text-center"><div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-space-md gap-y-space-2xs font-label-sm text-label-sm uppercase tracking-wider"><div class="flex items-center gap-space-xs mx-auto sm:mx-0"><span class="text-on-primary-fixed-variant">Sri Sairam Engineering College</span><span class="opacity-40">•</span><span class="text-primary-fixed">Department of CSE (AIML)</span></div><div class="hidden sm:flex items-center gap-space-sm"><a href="https://www.instagram.com/ccic_sairam?stkn=MXB2OGdiOTJsNTY3Yw==" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1 text-pink-300 hover:text-white transition"><svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg><span>Instagram</span></a><span class="opacity-40">•</span><a href="https://www.linkedin.com/in/ccic-club-837993428?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1 text-sky-300 hover:text-white transition"><svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg><span>LinkedIn</span></a></div></div></div>'''

footer_social_links = '''<div class="flex items-center gap-3 mt-2">
  <a href="https://www.instagram.com/ccic_sairam?stkn=MXB2OGdiOTJsNTY3Yw==" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1 text-xs font-semibold text-pink-600 hover:text-pink-700 transition">
    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
    <span>@ccic_sairam</span>
  </a>
  <span class="text-slate-400">•</span>
  <a href="https://www.linkedin.com/in/ccic-club-837993428?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" rel="noopener noreferrer" class="flex items-center gap-1 text-xs font-semibold text-sky-700 hover:text-sky-800 transition">
    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
    <span>LinkedIn</span>
  </a>
</div>'''

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Top Ribbon with Social Links if not already there
    old_ribbon_pattern = r'<div class="w-full bg-primary-container text-on-primary-container px-space-md py-space-2xs text-center"><div class="max-w-7xl mx-auto flex flex-wrap items-center justify-center gap-x-space-md gap-y-space-2xs font-label-sm text-label-sm uppercase tracking-wider">.*?</div></div>'
    if re.search(old_ribbon_pattern, content, re.DOTALL):
        content = re.sub(old_ribbon_pattern, top_header_with_socials, content, flags=re.DOTALL)

    # 2. Add About link into navbar right after Home
    if 'href="/about"' not in content:
        # Match Home link
        home_pattern = r'(<a[^>]*href="/"[^>]*>.*?Home.*?</a>)'
        is_about_page = 'about' in filepath.lower()
        about_link = about_link_active if is_about_page else about_link_inactive
        content = re.sub(home_pattern, r'\1\n' + about_link, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
