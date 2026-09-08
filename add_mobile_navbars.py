import os
import re

PAGE_CONFIG = {
    'index.html': 'home',
    'templates/index.html': 'home',
    'about.html': 'about',
    'templates/about.html': 'about',
    'events.html': 'events',
    'templates/events.html': 'events',
    'magic_members.html': 'magic',
    'magic-members.html': 'magic',
    'templates/magic_members.html': 'magic',
    'templates/magic-members.html': 'magic',
    'scope_members.html': 'scope',
    'scope-members.html': 'scope',
    'templates/scope_members.html': 'scope',
    'templates/scope-members.html': 'scope',
}

def make_mobile_dropdown(active_page):
    def link(page_key, href, icon, text, is_admin=False):
        if is_admin:
            cls = "px-4 py-2.5 rounded-lg transition-all duration-200 text-amber-700 font-semibold hover:bg-amber-50 flex items-center gap-2"
        elif page_key == active_page:
            cls = "px-4 py-2.5 rounded-lg transition-all duration-200 bg-secondary-container text-on-secondary font-bold flex items-center gap-2"
        else:
            cls = "px-4 py-2.5 rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface font-medium flex items-center gap-2"
        return f'<a class="{cls}" href="{href}"><span class="material-symbols-outlined text-[20px]">{icon}</span> {text}</a>'

    links = [
        link('home', '/', 'home', 'Home'),
        link('about', '/about', 'info', 'About'),
        link('events', '/events', 'event', 'Activities &amp; Events'),
        link('magic', '/magic-members', 'groups', 'Magic Members'),
        link('scope', '/scope-members', 'school', 'Scope Members'),
        link('register', '/register', 'how_to_reg', 'Register'),
        link('admin', '/admin', 'admin_panel_settings', 'Admin Portal', is_admin=True)
    ]
    links_html = '\n'.join(links)

    return f'''<!-- Mobile Navigation Drawer -->
<div id="mobileNavDropdown" class="hidden xl:hidden border-t border-outline-variant/15 bg-surface/98 backdrop-blur-xl shadow-xl transition-all duration-200">
<div class="max-w-7xl mx-auto px-margin-mobile py-3 flex flex-col gap-1 font-label-md text-label-md">
{links_html}
</div>
</div>'''

toggle_btn_html = '<button id="mobileNavToggle" onclick="toggleMobileMenu()" aria-label="Toggle navigation menu" class="xl:hidden p-2 rounded-lg text-on-surface hover:bg-surface-container focus:outline-none focus:ring-2 focus:ring-secondary transition-colors"><span class="material-symbols-outlined text-[26px] block" id="mobileNavIcon">menu</span></button>'

for filepath, active_page in PAGE_CONFIG.items():
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up previous insertions
    content = re.sub(r'<!-- Mobile Navigation Drawer -->\s*<div id="mobileNavDropdown".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button id="mobileNavToggle".*?</button>', '', content, flags=re.DOTALL)

    dropdown_html = make_mobile_dropdown(active_page)

    # Insert toggle button INSIDE the action div right after ccic-nav-auth
    # Pattern: <div class="flex items-center gap-space-..."><div class="ccic-nav-auth ...">...</div></div>
    action_pattern = r'(<div class="flex items-center gap-space-[^"]*"><div class="ccic-nav-auth[^>]*>.*?</div>)\s*</div>'
    content = re.sub(action_pattern, r'\1' + toggle_btn_html + '</div>', content, count=1, flags=re.DOTALL)

    # Insert dropdown right before </header>
    if '</header>' in content:
        content = content.replace('</header>', f'{dropdown_html}\n</header>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

# Update register.html & templates/register.html
for reg_path in ['register.html', 'templates/register.html']:
    if not os.path.exists(reg_path):
        continue
    with open(reg_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'<!-- Mobile Navigation Drawer -->\s*<div id="mobileNavDropdown".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="mobileNavDropdown".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button id="mobileNavToggle".*?</button>', '', content, flags=re.DOTALL)

    reg_toggle = '<button id="mobileNavToggle" onclick="toggleMobileMenu()" aria-label="Toggle navigation menu" class="md:hidden p-2 rounded-lg text-white hover:bg-white/10 focus:outline-none focus:ring-2 focus:ring-secondary transition-colors"><span class="material-symbols-outlined text-[26px] block" id="mobileNavIcon">menu</span></button>'
    
    reg_dropdown = '''<!-- Mobile Navigation Drawer -->
<div id="mobileNavDropdown" class="hidden md:hidden border-t border-slate-800 bg-[#07132b]/98 backdrop-blur-xl shadow-xl transition-all duration-200">
<div class="max-w-7xl mx-auto px-6 py-3 flex flex-col gap-1 font-headline text-sm">
<a class="px-4 py-2.5 rounded-lg transition-colors text-slate-300 hover:text-white hover:bg-white/10 flex items-center gap-2" href="/"><span class="material-symbols-outlined text-[20px]">home</span> Home</a>
<a class="px-4 py-2.5 rounded-lg transition-colors text-slate-300 hover:text-white hover:bg-white/10 flex items-center gap-2" href="/about"><span class="material-symbols-outlined text-[20px]">info</span> About</a>
<a class="px-4 py-2.5 rounded-lg transition-colors text-slate-300 hover:text-white hover:bg-white/10 flex items-center gap-2" href="/events"><span class="material-symbols-outlined text-[20px]">event</span> Activities &amp; Events</a>
<a class="px-4 py-2.5 rounded-lg transition-colors text-slate-300 hover:text-white hover:bg-white/10 flex items-center gap-2" href="/magic-members"><span class="material-symbols-outlined text-[20px]">groups</span> Magic Members</a>
<a class="px-4 py-2.5 rounded-lg transition-colors text-slate-300 hover:text-white hover:bg-white/10 flex items-center gap-2" href="/scope-members"><span class="material-symbols-outlined text-[20px]">school</span> Scope Members</a>
<a class="px-4 py-2.5 rounded-lg transition-colors text-secondary font-bold bg-white/10 flex items-center gap-2" href="/register"><span class="material-symbols-outlined text-[20px]">how_to_reg</span> Registration</a>
<a class="px-4 py-2.5 rounded-lg transition-colors text-amber-400 font-semibold hover:bg-white/10 flex items-center gap-2" href="/admin"><span class="material-symbols-outlined text-[20px]">admin_panel_settings</span> Admin Portal</a>
</div>
</div>'''

    reg_action_pattern = r'(<div class="ccic-nav-auth[^>]*>.*?</div>)'
    content = re.sub(reg_action_pattern, r'\1' + reg_toggle, content, count=1, flags=re.DOTALL)
    content = content.replace('</header>', f'{reg_dropdown}\n</header>', 1)

    with open(reg_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {reg_path}")
