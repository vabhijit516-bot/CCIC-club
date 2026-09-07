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

# Read head and navbar from templates/index.html
with open("templates/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

head_start = index_html.find("<head>")
head_end = index_html.find("</head>")
head_content = index_html[head_start+6:head_end]

# Ensure SheetJS is in head
sheetjs_tag = '<script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>'
if "xlsx.full.min.js" not in head_content:
    head_content += "\n" + sheetjs_tag

# Unified Navbar
unified_nav = '''
    <header class="sticky top-0 left-0 w-full z-50 shadow-[0_1px_8px_rgba(0,0,0,0.04)] bg-surface">
      <div class="w-full bg-primary-container text-on-primary-container px-space-md py-space-2xs text-center">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-center gap-x-space-md gap-y-space-2xs font-label-sm text-label-sm uppercase tracking-wider">
          <span class="text-on-primary-fixed-variant">Sri Sairam Engineering College</span>
          <span class="opacity-40">•</span>
          <span class="text-primary-fixed">Department of CSE (Artificial Intelligence &amp; Machine Learning)</span>
          <span class="opacity-40">•</span>
          <span class="text-on-primary-fixed-variant">Autonomous Institution</span>
        </div>
      </div>
      <div class="h-20 bg-surface/90 backdrop-blur-md px-margin-mobile md:px-margin-tablet lg:px-margin-desktop">
        <div class="max-w-7xl mx-auto h-full flex items-center justify-between gap-space-md">
          <a href="#home" class="flex items-center gap-space-sm">
            <img alt="CCIC Logo" class="h-9 w-auto object-contain rounded-full" src="/static/images/ccic_logo.jpg">
            <div class="flex flex-col">
              <span class="font-headline-sm text-headline-sm tracking-tight text-on-surface font-bold leading-none">CCIC</span>
              <span class="font-label-sm text-label-sm text-on-surface-variant font-medium hidden sm:inline-block leading-tight">Computational and Cognitive Intelligence Club</span>
            </div>
          </a>
          <nav class="hidden xl:flex items-center gap-space-xs font-label-md text-label-md">
            <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 bg-secondary-container text-on-secondary font-bold" href="#home">Home</a>
            <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#events">Activities &amp; Events</a>
            <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#magic-members">Magic Members</a>
            <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#scope-members">Scope Members</a>
            <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#register">Register</a>
            <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-amber-700 font-semibold hover:bg-amber-50 flex items-center gap-1" href="#admin">
              <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
              <span>Admin Board</span>
            </a>
          </nav>
          <div class="flex items-center gap-space-sm">
            <!-- One-click Excel Download on header -->
            <button onclick="downloadExcelData()" class="hidden md:inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-md text-xs font-headline font-bold shadow-sm transition">
              <span class="material-symbols-outlined text-[16px]">file_download</span>
              <span>Download Excel</span>
            </button>
            <a href="#register" class="px-3.5 py-1.5 text-xs font-headline font-bold rounded-md bg-secondary text-white hover:bg-blue-700 transition shadow-sm">
              Apply Now
            </a>
            <!-- Mobile Menu Toggle Button -->
            <button id="mobile-menu-btn" class="xl:hidden p-2 text-on-surface hover:bg-surface-container rounded-lg">
              <span class="material-symbols-outlined text-[24px]">menu</span>
            </button>
          </div>
        </div>
      </div>
      <!-- Mobile Dropdown Menu -->
      <div id="mobile-menu" class="hidden xl:hidden bg-surface border-b border-outline-variant/30 px-6 py-4 flex flex-col gap-2 shadow-lg">
        <a href="#home" class="py-2 text-sm font-headline font-semibold text-on-surface hover:text-secondary">Home</a>
        <a href="#events" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Activities &amp; Events</a>
        <a href="#magic-members" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Magic Members</a>
        <a href="#scope-members" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Scope Members</a>
        <a href="#register" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Register</a>
        <a href="#admin" class="py-2 text-sm font-headline font-bold text-amber-700 hover:text-amber-800 flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
          Admin Board
        </a>
        <div class="pt-2 border-t border-outline-variant/20 flex flex-col gap-2">
          <button onclick="downloadExcelData()" class="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg flex items-center justify-center gap-2 transition">
            <span class="material-symbols-outlined text-[16px]">file_download</span>
            Download Submissions Excel (.xlsx)
          </button>
        </div>
      </div>
    </header>
'''

# Extract main sections
home_inner = extract_main_inner("index")
events_inner = extract_main_inner("events")
magic_inner = extract_main_inner("magic_members")
scope_inner = extract_main_inner("scope_members")
register_inner = extract_main_inner("register")
admin_inner = extract_main_inner("admin")

# Clean internal page links into hash anchors
def clean_links(html):
    html = re.sub(r'href=["\']/events["\']', 'href="#events"', html)
    html = re.sub(r'href=["\']/magic-members["\']', 'href="#magic-members"', html)
    html = re.sub(r'href=["\']/scope-members["\']', 'href="#scope-members"', html)
    html = re.sub(r'href=["\']/register["\']', 'href="#register"', html)
    html = re.sub(r'href=["\']/admin["\']', 'href="#admin"', html)
    html = re.sub(r'href=["\']/["\']', 'href="#home"', html)
    return html

home_inner = clean_links(home_inner)
events_inner = clean_links(events_inner)
magic_inner = clean_links(magic_inner)
scope_inner = clean_links(scope_inner)
register_inner = clean_links(register_inner)
admin_inner = clean_links(admin_inner)

# Extract footer from index.html
foot_start = index_html.find("<footer")
foot_end = index_html.find("</footer>") + 9
footer_html = index_html[foot_start:foot_end] if foot_start != -1 else ""
footer_html = clean_links(footer_html)

# Extract modals
# Success modal from register.html
with open("templates/register.html", "r", encoding="utf-8") as f:
    reg_full = f.read()

m_s = reg_full.find('<div id="success-modal"')
m_e = reg_full.find('</div>\n    </div>\n\n    <!-- Footer -->')
if m_s != -1 and m_e != -1:
    success_modal_html = reg_full[m_s:m_e+13]
else:
    success_modal_html = '''
    <div id="success-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl p-8 max-w-md w-full text-center shadow-2xl border border-outline-variant/30">
            <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4">
                <span class="material-symbols-outlined text-4xl">verified</span>
            </div>
            <h3 class="font-headline text-xl font-bold text-slate-900 mb-2">Application Received!</h3>
            <p class="text-xs text-slate-600 mb-6 leading-relaxed">
                Thank you for applying to the CCIC AIML Club. Your credentials have been logged into our database and Excel archive.
            </p>
            <div class="flex flex-wrap gap-2.5 justify-center">
                <a href="#admin" onclick="document.getElementById('success-modal').classList.add('hidden')" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-slate-900 text-white text-xs font-headline font-semibold rounded-lg hover:bg-slate-800 transition shadow-sm">
                    <span class="material-symbols-outlined text-[16px] text-amber-400">admin_panel_settings</span>
                    <span>View in Admin Board</span>
                </a>
                <button onclick="downloadExcelData(); document.getElementById('success-modal').classList.add('hidden')" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-emerald-600 text-white text-xs font-headline font-semibold rounded-lg hover:bg-emerald-700 transition shadow-sm">
                    <span class="material-symbols-outlined text-[16px]">file_download</span>
                    <span>Download Excel</span>
                </button>
                <button onclick="document.getElementById('success-modal').classList.add('hidden')" class="px-3.5 py-2 bg-slate-100 text-slate-700 text-xs font-headline font-semibold rounded-lg hover:bg-slate-200 transition">
                    Close
                </button>
            </div>
        </div>
    </div>
    '''

# Admin details modal
details_modal_html = '''
    <div id="details-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
        <div class="bg-white rounded-2xl p-6 max-w-lg w-full shadow-2xl border border-slate-200">
            <div id="details-modal-content"></div>
            <div class="mt-6 pt-3 border-t text-right flex justify-end gap-2">
                <button onclick="closeDetailsModal()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-headline font-semibold rounded-lg transition">
                    Close Details
                </button>
            </div>
        </div>
    </div>
'''

# Assemble Master Document
master_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  {head_content}
</head>
<body class="bg-background font-body-md text-on-surface antialiased relative selection:bg-secondary selection:text-on-secondary">
  <div class="fixed inset-0 pointer-events-none z-0 flex items-center justify-center opacity-[0.04]">
    <img alt="CCIC Watermark" class="w-[600px] h-[600px] max-w-[80vw] max-h-[80vh] object-contain filter grayscale" src="/static/images/ccic_logo.jpg">
  </div>

  {unified_nav}

  <main class="w-full pt-0 relative z-10 bg-transparent min-h-screen">
    <!-- SECTION 1: HOME & LEADERSHIP -->
    <section id="home" class="scroll-mt-20">
      {home_inner}
    </section>

    <!-- SECTION 2: ACTIVITIES & EVENTS -->
    <section id="events" class="scroll-mt-20 border-t border-outline-variant/30">
      {events_inner}
    </section>

    <!-- SECTION 3: MAGIC MEMBERS -->
    <section id="magic-members" class="scroll-mt-20 border-t border-outline-variant/30">
      {magic_inner}
    </section>

    <!-- SECTION 4: SCOPE MEMBERS -->
    <section id="scope-members" class="scroll-mt-20 border-t border-outline-variant/30">
      {scope_inner}
    </section>

    <!-- SECTION 5: REGISTRATION APPLICATION FORM -->
    <section id="register" class="scroll-mt-20 border-t border-outline-variant/30 py-16 bg-surface-container-low">
      <div class="max-w-4xl mx-auto px-4 sm:px-6">
        <div class="text-center mb-10">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-headline font-semibold bg-secondary/10 text-secondary border border-secondary/20 mb-3">
            <span class="material-symbols-outlined text-[16px]">app_registration</span>
            <span>Student Membership Application 2026</span>
          </span>
          <h2 class="font-headline text-2xl sm:text-4xl font-bold text-slate-900 tracking-tight">
            Apply to Join the CCIC AIML Club
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 max-w-xl mx-auto mt-2 leading-relaxed">
            Collaborate on cutting-edge research in Generative AI, Robotics, and Cognitive Systems with Sri Sairam Engineering College scholars.
          </p>
        </div>

        <div class="bg-white rounded-2xl shadow-xl border border-outline-variant/40 p-6 sm:p-10">
          <div id="form-alert" class="hidden mb-6 p-4 rounded-xl text-xs border font-medium"></div>
          
          <form id="ccic-registration-form" class="space-y-8">
            <!-- Step 1: Candidate Identity -->
            <div>
              <h3 class="font-headline text-base sm:text-lg font-bold text-slate-900 border-b border-outline-variant/30 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary">person</span>
                1. Candidate Identity
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Full Name (as in College Records) <span class="text-red-500">*</span>
                  </label>
                  <input type="text" id="name" required placeholder="e.g. Abhijit V" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Roll Number / Register Number <span class="text-red-500">*</span>
                  </label>
                  <input type="text" id="roll_no" required placeholder="e.g. SEC25AM112" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition font-mono uppercase bg-slate-50/50">
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Institutional Email Address <span class="text-red-500">*</span>
                  </label>
                  <input type="email" id="email" required placeholder="your.name@sairam.edu.in" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    WhatsApp / Contact Number <span class="text-red-500">*</span>
                  </label>
                  <input type="tel" id="phone" required placeholder="+91 98765 43210" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
              </div>
            </div>

            <!-- Step 2: Academic Affiliation -->
            <div>
              <h3 class="font-headline text-base sm:text-lg font-bold text-slate-900 border-b border-outline-variant/30 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary">school</span>
                2. Academic Affiliation
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Department <span class="text-red-500">*</span>
                  </label>
                  <select id="department" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                    <option value="CSE (AI &amp; ML)" selected>CSE (Artificial Intelligence &amp; Machine Learning)</option>
                    <option value="Computer Science &amp; Engineering">Computer Science &amp; Engineering (CSE)</option>
                    <option value="Information Technology">Information Technology (IT)</option>
                    <option value="Artificial Intelligence &amp; Data Science">AI &amp; Data Science (AIDS)</option>
                    <option value="Electronics &amp; Communication">Electronics &amp; Communication (ECE)</option>
                    <option value="Electrical &amp; Electronics">Electrical &amp; Electronics (EEE)</option>
                    <option value="Mechanical Engineering">Mechanical Engineering</option>
                    <option value="Other Department">Other Department</option>
                  </select>
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Year of Study <span class="text-red-500">*</span>
                  </label>
                  <select id="year" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                    <option value="1st Year">1st Year (Freshman)</option>
                    <option value="2nd Year" selected>2nd Year (Sophomore)</option>
                    <option value="3rd Year">3rd Year (Junior)</option>
                    <option value="4th Year">4th Year (Senior)</option>
                    <option value="Postgraduate / Research">Postgraduate / Research Scholar</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- Step 3: Domain & Background -->
            <div>
              <h3 class="font-headline text-base sm:text-lg font-bold text-slate-900 border-b border-outline-variant/30 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary">memory</span>
                3. Technical Specialization &amp; Statement
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
                <div class="sm:col-span-2">
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Primary Domain of Interest <span class="text-red-500">*</span>
                  </label>
                  <select id="domain" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                    <option value="Computer Vision &amp; Generative AI">Computer Vision &amp; Generative AI</option>
                    <option value="Natural Language Processing">Natural Language Processing &amp; LLM Agents</option>
                    <option value="Deep Reinforcement Learning &amp; Robotics">Deep Reinforcement Learning &amp; Autonomous Robotics</option>
                    <option value="Machine Learning &amp; Data Science">Machine Learning &amp; Data Science Core</option>
                    <option value="Edge AI &amp; IoT Systems">Edge AI &amp; TinyML Systems</option>
                    <option value="AI Ethics, Safety &amp; Governance">AI Ethics, Safety &amp; Governance</option>
                  </select>
                </div>
                <div class="sm:col-span-2">
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    GitHub / LinkedIn / Portfolio URL
                  </label>
                  <input type="url" id="linkedin_github" placeholder="https://github.com/your-username" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
                <div class="sm:col-span-2">
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Motivation &amp; Research Statement
                  </label>
                  <textarea id="motivation" rows="3" placeholder="Briefly explain what projects you want to build or what excites you about CCIC..." class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50"></textarea>
                </div>
              </div>
            </div>

            <!-- Submit Button & Disclaimer -->
            <div class="pt-4 border-t border-outline-variant/30 flex flex-col sm:flex-row items-center justify-between gap-4">
              <p class="text-[11px] text-slate-500 font-mono">
                Submissions automatically synchronize with the CCIC Admin Board and downloadable Excel archives.
              </p>
              <button type="submit" id="submit-btn" class="w-full sm:w-auto py-2.5 px-6 bg-secondary hover:bg-blue-700 text-white font-headline font-bold text-sm rounded-lg transition-all shadow-md flex items-center justify-center gap-2">
                <span id="btn-spinner" class="hidden material-symbols-outlined animate-spin text-[18px]">progress_activity</span>
                <span id="btn-text">Submit Application</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>

    <!-- SECTION 6: ADMIN BOARD & EXCEL DOWNLOAD -->
    <section id="admin" class="scroll-mt-20 border-t border-outline-variant/30 py-16 bg-slate-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <!-- Admin Title and Export Controls -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-headline font-bold bg-amber-500 text-slate-900 uppercase tracking-wider">
                <span class="material-symbols-outlined text-[13px]">shield</span>
                Administrator Board
              </span>
              <span class="text-xs text-slate-400">• Live Roster Engine</span>
            </div>
            <h2 class="font-headline text-2xl sm:text-3xl font-bold text-slate-900">
              Application Database &amp; Real-Time Submissions
            </h2>
            <p class="text-xs sm:text-sm text-slate-500 mt-1">
              Monitor applicant registrations in real time, adjust review statuses, and export instant Excel spreadsheets.
            </p>
          </div>

          <!-- Download Action Buttons -->
          <div class="flex flex-wrap items-center gap-3">
            <!-- Download CSV -->
            <button onclick="downloadCSVData()" class="inline-flex items-center gap-2 px-4 py-2.5 bg-white hover:bg-slate-100 text-slate-700 text-xs font-headline font-bold rounded-lg border border-slate-300 shadow-sm transition">
              <span class="material-symbols-outlined text-emerald-600 text-[18px]">table_chart</span>
              <span>Download CSV</span>
            </button>

            <!-- Download Excel (.xlsx) -->
            <button onclick="downloadExcelData()" class="inline-flex items-center gap-2 px-4 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg shadow-sm transition">
              <span class="material-symbols-outlined text-white text-[18px]">file_download</span>
              <span>Download Excel (.xlsx)</span>
            </button>

            <!-- Refresh Button -->
            <button onclick="initSubmissionsData()" class="p-2.5 bg-white hover:bg-slate-100 text-slate-600 rounded-lg border border-slate-300 shadow-sm transition" title="Refresh records">
              <span class="material-symbols-outlined text-[18px] block">sync</span>
            </button>
          </div>
        </div>

        <!-- Metric KPI Cards -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          <div class="bg-white p-5 rounded-xl border border-slate-200/80 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">Total Applicants</span>
              <span class="material-symbols-outlined text-blue-600 text-[20px]">groups</span>
            </div>
            <div id="stat-total" class="font-headline text-3xl font-bold text-slate-900">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Across all departments</div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-slate-200/80 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">Pending Review</span>
              <span class="material-symbols-outlined text-amber-500 text-[20px]">pending_actions</span>
            </div>
            <div id="stat-pending" class="font-headline text-3xl font-bold text-amber-600">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Awaiting coordinator decision</div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-slate-200/80 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">Approved Members</span>
              <span class="material-symbols-outlined text-emerald-600 text-[20px]">verified</span>
            </div>
            <div id="stat-approved" class="font-headline text-3xl font-bold text-emerald-600">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Enrolled in CCIC research labs</div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-slate-200/80 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">AI Domains</span>
              <span class="material-symbols-outlined text-purple-600 text-[20px]">hub</span>
            </div>
            <div id="stat-domains" class="font-headline text-3xl font-bold text-purple-600">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Research specializations</div>
          </div>
        </div>

        <!-- Filter & Search Controls -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm mb-6 flex flex-col md:flex-row items-center justify-between gap-4">
          <!-- Search Bar -->
          <div class="relative w-full md:w-80">
            <span class="material-symbols-outlined absolute left-3 top-2.5 text-slate-400 text-[18px]">search</span>
            <input type="text" id="search-input" placeholder="Search by name, roll no, email..." class="w-full pl-9 pr-3 py-2 text-xs rounded-lg border border-slate-200 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition">
          </div>

          <!-- Filter Dropdowns -->
          <div class="flex flex-wrap items-center gap-3 w-full md:w-auto">
            <select id="filter-domain" class="text-xs py-2 px-3 rounded-lg border border-slate-200 bg-white font-medium text-slate-700 outline-none focus:border-secondary">
              <option value="All">All Domains</option>
              <option value="Computer Vision &amp; Generative AI">Computer Vision &amp; Generative AI</option>
              <option value="Natural Language Processing">Natural Language Processing</option>
              <option value="Deep Reinforcement Learning &amp; Robotics">Deep Reinforcement Learning &amp; Robotics</option>
              <option value="Machine Learning &amp; Data Science">Machine Learning &amp; Data Science</option>
              <option value="Edge AI &amp; IoT Systems">Edge AI &amp; IoT Systems</option>
            </select>

            <select id="filter-status" class="text-xs py-2 px-3 rounded-lg border border-slate-200 bg-white font-medium text-slate-700 outline-none focus:border-secondary">
              <option value="All">All Statuses</option>
              <option value="Pending">Pending</option>
              <option value="Reviewed">Reviewed</option>
              <option value="Approved">Approved</option>
            </select>

            <span id="results-count" class="text-xs font-mono text-slate-500 ml-auto">
              Loading records...
            </span>
          </div>
        </div>

        <!-- Live Submissions Table -->
        <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-slate-50 text-slate-600 text-[11px] font-headline uppercase tracking-wider border-b border-slate-200">
                  <th class="px-4 py-3">ID</th>
                  <th class="px-4 py-3">Applicant Details</th>
                  <th class="px-4 py-3">Roll No</th>
                  <th class="px-4 py-3">Dept &amp; Year</th>
                  <th class="px-4 py-3">AI Domain</th>
                  <th class="px-4 py-3">Submitted</th>
                  <th class="px-4 py-3">Status</th>
                  <th class="px-4 py-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody id="submissions-tbody">
                <tr>
                  <td colspan="8" class="text-center py-10 text-slate-400 font-medium">
                    <span class="material-symbols-outlined animate-spin text-3xl block mb-2">progress_activity</span>
                    Loading submissions...
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  </main>

  {details_modal_html}
  {success_modal_html}
  {footer_html}

  <!-- SheetJS & Application Scripts -->
  <script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>
  <script src="/static/js/unified-app.js"></script>
  <script src="/static/js/smooth-scroll.js"></script>
</body>
</html>
'''

# Write to root index.html (for Vercel deployment)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(master_html)

# Also write to templates/index.html (for local Flask server)
with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(master_html)

print("Unified index.html and templates/index.html generated successfully!")
