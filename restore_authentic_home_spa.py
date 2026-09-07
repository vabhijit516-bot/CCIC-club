import os
import re

# Read the raw, pristine Step 33 (Home Stitch screen)
with open(r"C:\Users\ABHIJIT\.gemini\antigravity-ide\brain\4bedf0fd-8c82-4466-a618-a9f3506d0a2a\.system_generated\steps\33\content.md", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

# Find start of HTML
html_start = 0
for i, line in enumerate(raw_lines):
    if "<!DOCTYPE html" in line or "<html" in line:
        html_start = i
        break

stitch_home_html = "".join(raw_lines[html_start:])

# 1. Update <head> to include SheetJS and smooth scroll styles
sheetjs_script = '<script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>'
custom_styles = '''
<link rel="stylesheet" href="/static/css/transitions.css">
<style>
  section { scroll-margin-top: 5rem; }
  .nav-active {
    background-color: #0057c0 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
  }
</style>
'''

if "xlsx.full.min.js" not in stitch_home_html:
    stitch_home_html = stitch_home_html.replace("</head>", f"{sheetjs_script}\n{custom_styles}\n</head>")

# 2. Modernize the Header to be sticky and contain direct navigation to all sections
old_header_start = stitch_home_html.find("<header")
old_header_end = stitch_home_html.find("</header>") + 9

new_header = '''<header class="sticky top-0 left-0 w-full z-50 shadow-sm bg-surface/95 backdrop-blur-md border-b border-outline-variant/30">
  <!-- Top Institutional Ribbon -->
  <div class="w-full bg-primary-container text-on-primary-container px-space-md py-space-2xs text-center border-b border-slate-800">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-center gap-x-space-md gap-y-space-2xs font-label-sm text-label-sm uppercase tracking-wider">
      <span class="text-on-primary-fixed-variant font-bold text-blue-300">Sri Sairam Engineering College</span>
      <span class="opacity-40">•</span>
      <span class="text-primary-fixed">Department of CSE (Artificial Intelligence &amp; Machine Learning)</span>
      <span class="opacity-40">•</span>
      <span class="text-on-primary-fixed-variant text-amber-400 font-semibold">Autonomous Institution</span>
    </div>
  </div>

  <!-- Navigation Bar -->
  <div class="h-20 px-margin-mobile md:px-margin-tablet lg:px-margin-desktop">
    <div class="max-w-7xl mx-auto h-full flex items-center justify-between gap-space-md">
      <!-- Logo & Title -->
      <a href="#home" class="flex items-center gap-space-sm group">
        <img alt="CCIC Logo" class="h-10 w-10 object-cover rounded-full border border-outline-variant/50 shadow-sm transition group-hover:scale-105" src="/static/images/ccic_logo.jpg">
        <div class="flex flex-col">
          <div class="flex items-center gap-2">
            <span class="font-headline-sm text-headline-sm tracking-tight text-on-surface font-bold leading-none">CCIC</span>
            <span class="font-label-sm text-[10px] bg-secondary/10 text-secondary px-1.5 py-0.5 rounded font-bold uppercase">AIML Club</span>
          </div>
          <span class="font-label-sm text-label-sm text-on-surface-variant font-medium hidden sm:inline-block leading-tight">Computational and Cognitive Intelligence Club</span>
        </div>
      </a>

      <!-- Desktop Nav Items with smooth anchors -->
      <nav class="hidden xl:flex items-center gap-space-xs font-label-md text-label-md">
        <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 bg-secondary-container text-on-secondary font-bold" href="#home">Home</a>
        <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#events-showcase">Events</a>
        <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#magic-members">Magic Members</a>
        <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#scope-members">Scope Members</a>
        <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-on-surface-variant hover:bg-surface-container hover:text-on-surface" href="#register">Register</a>
        <a class="nav-link px-space-sm py-space-2xs rounded-lg transition-all duration-200 text-amber-700 bg-amber-50 hover:bg-amber-100 flex items-center gap-1 font-bold" href="#admin">
          <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
          <span>Admin Board</span>
        </a>
      </nav>

      <!-- Quick Actions -->
      <div class="flex items-center gap-space-sm">
        <!-- Download Excel Header Shortcut -->
        <button onclick="downloadExcelData()" class="hidden md:inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-md text-xs font-headline font-bold shadow-sm transition">
          <span class="material-symbols-outlined text-[16px]">file_download</span>
          <span>Download Excel</span>
        </button>
        <a href="#register" class="px-3.5 py-1.5 text-xs font-headline font-bold rounded-md bg-secondary text-white hover:bg-blue-700 transition shadow-sm">
          Apply Now
        </a>
        <!-- Mobile Menu Hamburger -->
        <button id="mobile-menu-btn" class="xl:hidden p-2 text-on-surface hover:bg-surface-container rounded-lg">
          <span class="material-symbols-outlined text-[24px]">menu</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Dropdown Menu -->
  <div id="mobile-menu" class="hidden xl:hidden bg-surface border-b border-outline-variant/30 px-6 py-4 flex flex-col gap-2 shadow-xl">
    <a href="#home" class="py-2 text-sm font-headline font-semibold text-on-surface hover:text-secondary">Home</a>
    <a href="#events-showcase" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Activities &amp; Events</a>
    <a href="#magic-members" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Magic Members</a>
    <a href="#scope-members" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Scope Members</a>
    <a href="#register" class="py-2 text-sm font-headline font-semibold text-on-surface-variant hover:text-secondary">Student Registration</a>
    <a href="#admin" class="py-2 text-sm font-headline font-bold text-amber-700 hover:text-amber-800 flex items-center gap-1">
      <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
      Administrator Board
    </a>
    <div class="pt-2 border-t border-outline-variant/20 flex flex-col gap-2">
      <button onclick="downloadExcelData()" class="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg flex items-center justify-center gap-2 transition shadow-sm">
        <span class="material-symbols-outlined text-[16px]">file_download</span>
        Download Excel Spreadsheet (.xlsx)
      </button>
    </div>
  </div>
</header>'''

stitch_home_html = stitch_home_html[:old_header_start] + new_header + stitch_home_html[old_header_end:]

# Wrap the main home section in <section id="home">
main_start = stitch_home_html.find("<main")
tag_end = stitch_home_html.find(">", main_start) + 1
stitch_home_html = stitch_home_html[:tag_end] + '\n<section id="home">\n' + stitch_home_html[tag_end:]

# Replace fixed images to local images if available
stitch_home_html = stitch_home_html.replace("https://lh3.googleusercontent.com/aida/AEtjO1X5Zf7wbgy7q5keOlpodNfu2DAkYz2HozRjFIEJ1AzHzN7yiN1iiE2XlfBQTXIZn0z7SieiAb0XJA4zu3bXXHzPpZuo6yTEio1J1pQeua4HeSgt6ZTrqoHg51Bm0EQtEq4jebVIkqDSUsvxsl4PDvsuBQFiOD8UdgZicIHzJNDpEjv_PJITteekQEj4nYdov7w7jM44duyDIBAJMwAsM6M_jxLw0wIw2-HKU5ljIaNqx48EKccXZVGnLbSonXTNVoJSYxeU4m6yvA", "/static/images/ccic_logo.jpg")

# Replace CTAs to anchor smoothly to their respective single-page sections
stitch_home_html = stitch_home_html.replace('href="#events-showcase"', 'href="#events-showcase"')
stitch_home_html = stitch_home_html.replace('href="#leadership-mentors"', 'href="#leadership-mentors"')
stitch_home_html = stitch_home_html.replace('href="#join-modal"', 'href="#register"')
stitch_home_html = stitch_home_html.replace("document.getElementById('membership-panel').scrollIntoView({behavior: 'smooth'})", "document.getElementById('register').scrollIntoView({behavior: 'smooth'})")

# Close the home section before we add the other sections
# In Step 33, `membership-panel` was the last section before the script tag.
# We will insert the Magic Members, Scope Members, Registration Form, and Admin Board right after membership-panel!
insert_point = stitch_home_html.find("<!-- Interactive Telemetry Counter Vanilla Script -->")

# Additional Sections: Magic Members, Scope Members, Registration Form, Admin Board
extra_sections = '''
</section>
<!-- END SECTION 1: HOME -->

<!-- ========================================== -->
<!-- SECTION 2: MAGIC MEMBERS ROSTER            -->
<!-- ========================================== -->
<section id="magic-members" class="w-full py-space-3xl px-margin-mobile md:px-margin-tablet lg:px-margin-desktop bg-surface-container-low border-t border-outline-variant/30">
  <div class="max-w-7xl mx-auto flex flex-col gap-space-2xl">
    <div class="text-center max-w-2xl mx-auto">
      <div class="inline-flex items-center gap-space-2xs text-secondary font-bold mb-1">
        <span class="material-symbols-outlined text-[20px]">stars</span>
        <span class="font-label-md text-label-md uppercase tracking-wider">Executive Student Vanguard</span>
      </div>
      <h2 class="font-headline-lg text-headline-lg text-on-surface font-bold">Magic Members &amp; Student Leads</h2>
      <p class="font-body-md text-body-md text-on-surface-variant mt-2">
        Student coordinators, neural model architects, and technology evangelists across the 3rd Year and 2nd Year cohorts.
      </p>
    </div>

    <!-- Student Coordinators (Dual Feature Cards) -->
    <div>
      <h3 class="font-headline-md text-headline-md text-on-surface font-bold mb-space-md flex items-center gap-2">
        <span class="material-symbols-outlined text-secondary">stars</span>
        Lead Student Coordinators
      </h3>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-space-lg">
        <!-- S L HARI PRIYAN -->
        <div class="bg-surface-container-lowest p-space-xl rounded-2xl shadow-md flex flex-col sm:flex-row gap-space-lg items-center relative overflow-hidden group hover:shadow-xl transition">
          <div class="w-32 h-32 rounded-xl p-1 bg-gradient-to-tr from-secondary to-tertiary-fixed-dim shadow-md shrink-0">
            <img class="w-full h-full object-cover rounded-lg" alt="S L HARI PRIYAN" src="/static/images/haripriyan.jpg">
          </div>
          <div class="flex flex-col flex-1 text-center sm:text-left min-w-0">
            <div class="inline-flex items-center gap-space-2xs self-center sm:self-start bg-secondary-container/10 text-secondary px-space-xs py-space-2xs rounded-md">
              <span class="material-symbols-outlined text-[14px]">psychology</span>
              <span class="font-label-sm text-label-sm uppercase font-bold tracking-wider">Lead Student Co-ordinator</span>
            </div>
            <h4 class="font-headline-md text-headline-md text-on-surface font-bold mt-space-xs truncate">S L HARI PRIYAN</h4>
            <p class="font-label-md text-label-md text-on-surface-variant font-medium">Department of CSE (AIML) • Final Year</p>
            <div class="mt-space-sm flex flex-wrap gap-space-2xs justify-center sm:justify-start">
              <span class="bg-surface-container-high text-on-surface px-space-xs py-space-2xs rounded text-label-sm font-label-sm">Cognitive Systems</span>
              <span class="bg-surface-container-high text-on-surface px-space-xs py-space-2xs rounded text-label-sm font-label-sm">Multi-Agent Systems</span>
              <span class="bg-surface-container-high text-on-surface px-space-xs py-space-2xs rounded text-label-sm font-label-sm">IEEE Student Branch</span>
            </div>
          </div>
        </div>

        <!-- K GURU PRAKASH -->
        <div class="bg-surface-container-lowest p-space-xl rounded-2xl shadow-md flex flex-col sm:flex-row gap-space-lg items-center relative overflow-hidden group hover:shadow-xl transition">
          <div class="w-32 h-32 rounded-xl p-1 bg-gradient-to-tr from-tertiary-container to-secondary shadow-md shrink-0">
            <img class="w-full h-full object-cover rounded-lg" alt="K GURU PRAKASH" src="/static/images/guru.jpg">
          </div>
          <div class="flex flex-col flex-1 text-center sm:text-left min-w-0">
            <div class="inline-flex items-center gap-space-2xs self-center sm:self-start bg-secondary-container/10 text-secondary px-space-xs py-space-2xs rounded-md">
              <span class="material-symbols-outlined text-[14px]">neurology</span>
              <span class="font-label-sm text-label-sm uppercase font-bold tracking-wider">Co-lead Student Co-ordinator</span>
            </div>
            <h4 class="font-headline-md text-headline-md text-on-surface font-bold mt-space-xs truncate">K GURU PRAKASH</h4>
            <p class="font-label-md text-label-md text-on-surface-variant font-medium">Department of CSE (AIML) • Final Year</p>
            <div class="mt-space-sm flex flex-wrap gap-space-2xs justify-center sm:justify-start">
              <span class="bg-surface-container-high text-on-surface px-space-xs py-space-2xs rounded text-label-sm font-label-sm">Robotics &amp; Vision</span>
              <span class="bg-surface-container-high text-on-surface px-space-xs py-space-2xs rounded text-label-sm font-label-sm">Edge Hardware</span>
              <span class="bg-surface-container-high text-on-surface px-space-xs py-space-2xs rounded text-label-sm font-label-sm">Operations</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3rd Year Magic Members -->
    <div>
      <div class="flex items-center justify-between mb-space-md">
        <h3 class="font-headline-md text-headline-md text-on-surface font-bold flex items-center gap-2">
          <span class="material-symbols-outlined text-secondary">memory</span>
          3rd Year Magic Members
        </h3>
        <span class="font-label-sm text-label-sm px-space-xs py-1 rounded bg-surface-container-high text-on-surface font-semibold">5 Designated Core Leads</span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-space-md">
        <!-- Mukesh Babu -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Mukesh Babu" src="/static/images/mukesh.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-[11px] px-2 py-0.5 rounded font-bold">Yr 3 • AIDS</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">🧠 Master Mind</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Mukesh Babu</h4>
            <p class="font-body-md text-xs text-on-surface-variant mt-1 line-clamp-2">Strategic AI &amp; Data Science architectures.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-secondary">
            <span>3rd Year – AIDS</span>
            <span class="text-outline-variant font-normal">Core</span>
          </div>
        </div>

        <!-- Jayaganesh -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Jayaganesh" src="/static/images/jayaganesh.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-[11px] px-2 py-0.5 rounded font-bold">Yr 3 • AIML</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">⚖️ Advocate</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Jayaganesh</h4>
            <p class="font-body-md text-xs text-on-surface-variant mt-1 line-clamp-2">Neural compliance, ethics &amp; student advocacy.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-secondary">
            <span>3rd Year – AIML</span>
            <span class="text-outline-variant font-normal">Core</span>
          </div>
        </div>

        <!-- Megha Mithra -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Megha Mithra" src="/static/images/meghamithra.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-[11px] px-2 py-0.5 rounded font-bold">Yr 3 • AIML</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">🧭 Guide</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Megha Mithra</h4>
            <p class="font-body-md text-xs text-on-surface-variant mt-1 line-clamp-2">Cohort mentorship, guidance &amp; project incubation.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-secondary">
            <span>3rd Year – AIML</span>
            <span class="text-outline-variant font-normal">Core</span>
          </div>
        </div>

        <!-- Rishi -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Rishi" src="/static/images/rishi.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-[11px] px-2 py-0.5 rounded font-bold">Yr 3 • ECE</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">📢 Influencer</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Rishi</h4>
            <p class="font-body-md text-xs text-on-surface-variant mt-1 line-clamp-2">Hardware outreach &amp; edge AI evangelism.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-secondary">
            <span>3rd Year – ECE</span>
            <span class="text-outline-variant font-normal">Core</span>
          </div>
        </div>

        <!-- Oviya -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Oviya" src="/static/images/oviya.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-[11px] px-2 py-0.5 rounded font-bold">Yr 2 • CSE</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">💬 Communicator</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Oviya</h4>
            <p class="font-body-md text-xs text-on-surface-variant mt-1 line-clamp-2">Documentation, event dispatch &amp; publications.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-secondary">
            <span>2nd Year – CSE</span>
            <span class="text-outline-variant font-normal">Core</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 2nd Year Magic Members -->
    <div>
      <div class="flex items-center justify-between mb-space-md">
        <h3 class="font-headline-md text-headline-md text-on-surface font-bold flex items-center gap-2">
          <span class="material-symbols-outlined text-secondary">rocket_launch</span>
          2nd Year Magic Members
        </h3>
        <span class="font-label-sm text-label-sm px-space-xs py-1 rounded bg-surface-container-high text-on-surface font-semibold">Cohort 2024–2028 • 5 Active Leads</span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-space-md">
        <!-- 1. Oviya -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Oviya" src="/static/images/oviya.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">SEC25CS113</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">🧠 Master Mind</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Oviya</h4>
            <p class="font-label-sm text-xs text-on-surface-variant font-mono">SEC25CS113 • 2nd Year</p>
            <p class="text-xs text-on-surface-variant mt-1 line-clamp-2">Core logic architecture &amp; neural workflows.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-on-surface-variant">
            <span>CSE Department</span>
            <span class="material-symbols-outlined text-[16px] text-secondary">psychology</span>
          </div>
        </div>

        <!-- 2. Dhanasekaran -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Dhanasekaran" src="/static/images/dhanasekaran.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">SEC25AM090</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">⚖️ Advocate</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Dhanasekaran</h4>
            <p class="font-label-sm text-xs text-on-surface-variant font-mono">SEC25AM090 • 2nd Year</p>
            <p class="text-xs text-on-surface-variant mt-1 line-clamp-2">Model governance &amp; ethical AI standards.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-on-surface-variant">
            <span>AIML Department</span>
            <span class="material-symbols-outlined text-[16px] text-secondary">balance</span>
          </div>
        </div>

        <!-- 3. Kalai Arasi K -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Kalai Arasi K" src="/static/images/kalai.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">SEC25CS085</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">🧭 Guide</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Kalai Arasi K</h4>
            <p class="font-label-sm text-xs text-on-surface-variant font-mono">SEC25CS085 • 2nd Year</p>
            <p class="text-xs text-on-surface-variant mt-1 line-clamp-2">Technical peer learning &amp; repository structures.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-on-surface-variant">
            <span>CSE Department</span>
            <span class="material-symbols-outlined text-[16px] text-secondary">explore</span>
          </div>
        </div>

        <!-- 4. Abhijit -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Abhijit" src="/static/images/abhijit.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">SEC25AM112</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">📢 Influencer</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Abhijit</h4>
            <p class="font-label-sm text-xs text-on-surface-variant font-mono">SEC25AM112 • 2nd Year</p>
            <p class="text-xs text-on-surface-variant mt-1 line-clamp-2">AI community engagement &amp; hackathon sprints.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-on-surface-variant">
            <span>AIML Department</span>
            <span class="material-symbols-outlined text-[16px] text-secondary">campaign</span>
          </div>
        </div>

        <!-- 5. Sanjana -->
        <div class="bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition flex flex-col justify-between group">
          <div>
            <div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container mb-3">
              <img class="w-full h-full object-cover group-hover:scale-105 transition" alt="Sanjana" src="/static/images/sanjana.jpg">
              <span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">SEC25EC020</span>
            </div>
            <span class="font-label-sm text-label-sm font-bold text-secondary uppercase">💬 Communicator</span>
            <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-1">Sanjana</h4>
            <p class="font-label-sm text-xs text-on-surface-variant font-mono">SEC25EC020 • 2nd Year</p>
            <p class="text-xs text-on-surface-variant mt-1 line-clamp-2">Interface documentation &amp; creative media design.</p>
          </div>
          <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-on-surface-variant">
            <span>ECE Department</span>
            <span class="material-symbols-outlined text-[16px] text-secondary">forum</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- SECTION 3: SCOPE MEMBERS (FACULTY LEADS)   -->
<!-- ========================================== -->
<section id="scope-members" class="w-full py-space-3xl px-margin-mobile md:px-margin-tablet lg:px-margin-desktop bg-surface border-t border-outline-variant/30">
  <div class="max-w-7xl mx-auto flex flex-col gap-space-2xl">
    <div class="text-center max-w-2xl mx-auto">
      <div class="inline-flex items-center gap-space-2xs text-secondary font-bold mb-1">
        <span class="material-symbols-outlined text-[20px]">supervised_user_circle</span>
        <span class="font-label-md text-label-md uppercase tracking-wider">Faculty Leadership &amp; Advisory</span>
      </div>
      <h2 class="font-headline-lg text-headline-lg text-on-surface font-bold">Faculty Scope Members Roster</h2>
      <p class="font-body-md text-body-md text-on-surface-variant mt-2">
        Academic mentors steering strategic compliance, AI research labs, and IEEE publishing standards.
      </p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-space-lg">
      <!-- 1. Dr. R. Geetha -->
      <div class="bg-surface-container-lowest p-space-lg rounded-2xl shadow-sm hover:shadow-md transition border border-outline-variant/30 flex items-start gap-space-md">
        <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDyOcOpbd19Zc1vSSsnCdGfKKedjQdYHjcKEJZ1iH61GG9-5SB5ATwNg3RfZcmiEqTlGQ99-qe60HkgYHdtt2jyoS9bjkOynoYH-X9TJ4U-4I6Csj2lmIp4xMQP36dlgxV2w6OzC4YjCMcDEZHSlQysHiHb_qSHl-E6uy_WDkYghi1tqkxzuiVPKrcigs4KNtsjF7LItMtJGEq5SMC5dS9a4_qqhidqDzJ7A0ee7HudoRylABVkpBA_IOMZoFaltfiIQA" alt="Dr. R. Geetha" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-200" onerror="this.src='/static/images/ccic_logo.jpg'">
        <div>
          <span class="font-label-sm text-[10px] font-bold uppercase text-secondary">Strategist</span>
          <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface">Dr. R. Geetha</h4>
          <p class="text-xs text-on-surface-variant">Assistant Professor • SEC, CSE (AI&amp;ML)</p>
          <p class="text-[11px] text-on-surface-variant font-medium mt-1">Healthcare ML &amp; Neuro-Symbolic AI</p>
        </div>
      </div>

      <!-- 2. Dr. V. Lalitha -->
      <div class="bg-surface-container-lowest p-space-lg rounded-2xl shadow-sm hover:shadow-md transition border border-outline-variant/30 flex items-start gap-space-md">
        <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDvB7eDfvF1s6J0K1L2M3N4P5Q6" alt="Dr. V. Lalitha" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-200" onerror="this.src='/static/images/ccic_logo.jpg'">
        <div>
          <span class="font-label-sm text-[10px] font-bold uppercase text-secondary">Captain</span>
          <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface">Dr. V. Lalitha</h4>
          <p class="text-xs text-on-surface-variant">Associate Professor • SEC, CSE (AI&amp;ML)</p>
          <p class="text-[11px] text-on-surface-variant font-medium mt-1">Agentic Systems &amp; Autonomous Intelligence</p>
        </div>
      </div>

      <!-- 3. Ms. Mathupriya -->
      <div class="bg-surface-container-lowest p-space-lg rounded-2xl shadow-sm hover:shadow-md transition border border-outline-variant/30 flex items-start gap-space-md">
        <img src="/static/images/mathupriya.jpg" alt="Ms. Mathupriya" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-200">
        <div>
          <span class="font-label-sm text-[10px] font-bold uppercase text-secondary">Organizer</span>
          <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface">Ms. Mathupriya</h4>
          <p class="text-xs text-on-surface-variant">Assistant Professor • SEC</p>
          <p class="text-[11px] text-on-surface-variant font-medium mt-1">Event Coordination &amp; Operations</p>
        </div>
      </div>

      <!-- 4. Mrs. S. Ebenezer Roselin -->
      <div class="bg-surface-container-lowest p-space-lg rounded-2xl shadow-sm hover:shadow-md transition border border-outline-variant/30 flex items-start gap-space-md">
        <img src="/static/images/ebenezer.jpg" alt="Mrs. S. Ebenezer Roselin" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-200">
        <div>
          <span class="font-label-sm text-[10px] font-bold uppercase text-secondary">Propagator</span>
          <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface">Mrs. S. Ebenezer Roselin</h4>
          <p class="text-xs text-on-surface-variant">Assistant Professor • SIT, CSE (Cyber Security)</p>
          <p class="text-[11px] text-on-surface-variant font-medium mt-1">Inter-Institutional AI &amp; Security</p>
        </div>
      </div>

      <!-- 5. Ms. M. Anitha -->
      <div class="bg-surface-container-lowest p-space-lg rounded-2xl shadow-sm hover:shadow-md transition border border-outline-variant/30 flex items-start gap-space-md">
        <img src="/static/images/anitha.jpg" alt="Ms. M. Anitha" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-200">
        <div>
          <span class="font-label-sm text-[10px] font-bold uppercase text-secondary">Executor</span>
          <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface">Ms. M. Anitha</h4>
          <p class="text-xs text-on-surface-variant">Assistant Professor • SIT, AI-DS</p>
          <p class="text-[11px] text-on-surface-variant font-medium mt-1">Data Science &amp; Technical Execution</p>
        </div>
      </div>

      <!-- 6. Student Coordinators -->
      <div class="bg-surface-container-lowest p-space-lg rounded-2xl shadow-sm hover:shadow-md transition border border-outline-variant/30 flex items-start gap-space-md">
        <div class="w-16 h-16 rounded-xl bg-secondary-container text-on-secondary flex items-center justify-center font-bold text-2xl shrink-0">
          <span class="material-symbols-outlined text-[28px]">groups</span>
        </div>
        <div>
          <span class="font-label-sm text-[10px] font-bold uppercase text-secondary">Student Coordinators</span>
          <h4 class="font-headline-sm text-headline-sm font-bold text-on-surface">Hari Priyan &amp; Guru Prakash</h4>
          <p class="text-xs text-on-surface-variant">Final Year Cohort • CSE (AIML)</p>
          <p class="text-[11px] text-on-surface-variant font-medium mt-1">Executive Student Coordination</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- SECTION 4: REGISTRATION FORM               -->
<!-- ========================================== -->
<section id="register" class="w-full py-space-3xl px-margin-mobile md:px-margin-tablet lg:px-margin-desktop bg-surface-container-low border-t border-outline-variant/30">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-10">
      <div class="inline-flex items-center gap-space-2xs text-secondary font-bold mb-1">
        <span class="material-symbols-outlined text-[20px]">app_registration</span>
        <span class="font-label-md text-label-md uppercase tracking-wider">Candidate Application</span>
      </div>
      <h2 class="font-headline-lg text-headline-lg text-on-surface font-bold">Apply for CCIC AIML Club Membership</h2>
      <p class="font-body-md text-body-md text-on-surface-variant max-w-xl mx-auto mt-2">
        Join specialized research tracks in Generative AI, Autonomous Robotics, and Multi-Agent Workflows.
      </p>
    </div>

    <div class="bg-surface-container-lowest rounded-2xl shadow-xl border border-outline-variant/40 p-6 sm:p-10">
      <div id="form-alert" class="hidden mb-6 p-4 rounded-xl text-xs border font-medium"></div>

      <form id="ccic-registration-form" class="space-y-8">
        <!-- Step 1: Candidate Identity -->
        <div>
          <h3 class="font-headline-md text-headline-md text-on-surface font-bold border-b border-outline-variant/30 pb-2 flex items-center gap-2">
            <span class="material-symbols-outlined text-secondary">person</span>
            1. Candidate Identity
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
            <div>
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Full Name (as in College Records) <span class="text-error">*</span>
              </label>
              <input type="text" id="name" required placeholder="e.g. Abhijit V" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
            </div>
            <div>
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Roll Number / Register Number <span class="text-error">*</span>
              </label>
              <input type="text" id="roll_no" required placeholder="e.g. SEC25AM112" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition font-mono uppercase bg-surface-container-low">
            </div>
            <div>
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Institutional Email Address <span class="text-error">*</span>
              </label>
              <input type="email" id="email" required placeholder="your.name@sairam.edu.in" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
            </div>
            <div>
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                WhatsApp / Contact Number <span class="text-error">*</span>
              </label>
              <input type="tel" id="phone" required placeholder="+91 98765 43210" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
            </div>
          </div>
        </div>

        <!-- Step 2: Academic Affiliation -->
        <div>
          <h3 class="font-headline-md text-headline-md text-on-surface font-bold border-b border-outline-variant/30 pb-2 flex items-center gap-2">
            <span class="material-symbols-outlined text-secondary">school</span>
            2. Academic Affiliation
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
            <div>
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Department <span class="text-error">*</span>
              </label>
              <select id="department" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
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
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Year of Study <span class="text-error">*</span>
              </label>
              <select id="year" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
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
          <h3 class="font-headline-md text-headline-md text-on-surface font-bold border-b border-outline-variant/30 pb-2 flex items-center gap-2">
            <span class="material-symbols-outlined text-secondary">memory</span>
            3. Technical Specialization &amp; Statement
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
            <div class="sm:col-span-2">
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Primary Domain of Interest <span class="text-error">*</span>
              </label>
              <select id="domain" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
                <option value="Computer Vision &amp; Generative AI">Computer Vision &amp; Generative AI</option>
                <option value="Natural Language Processing">Natural Language Processing &amp; LLM Agents</option>
                <option value="Deep Reinforcement Learning &amp; Robotics">Deep Reinforcement Learning &amp; Autonomous Robotics</option>
                <option value="Machine Learning &amp; Data Science">Machine Learning &amp; Data Science Core</option>
                <option value="Edge AI &amp; IoT Systems">Edge AI &amp; TinyML Systems</option>
                <option value="AI Ethics, Safety &amp; Governance">AI Ethics, Safety &amp; Governance</option>
              </select>
            </div>
            <div class="sm:col-span-2">
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                GitHub / LinkedIn / Portfolio URL
              </label>
              <input type="url" id="linkedin_github" placeholder="https://github.com/your-username" class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
            </div>
            <div class="sm:col-span-2">
              <label class="block text-xs font-headline font-semibold text-on-surface mb-1">
                Motivation &amp; Research Statement
              </label>
              <textarea id="motivation" rows="3" placeholder="Briefly explain what projects you want to build or what excites you about CCIC..." class="w-full px-3.5 py-2 text-sm rounded-lg border border-outline-variant/60 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low"></textarea>
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="pt-4 border-t border-outline-variant/30 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p class="text-[11px] text-on-surface-variant font-mono">
            Submissions automatically synchronize with the CCIC Admin Board and downloadable Excel archives.
          </p>
          <button type="submit" id="submit-btn" class="w-full sm:w-auto py-3 px-8 bg-secondary hover:bg-blue-700 text-white font-headline font-bold text-sm rounded-xl transition-all shadow-md flex items-center justify-center gap-2">
            <span id="btn-spinner" class="hidden material-symbols-outlined animate-spin text-[18px]">progress_activity</span>
            <span id="btn-text">Submit Application</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</section>

<!-- ========================================== -->
<!-- SECTION 5: ADMIN BOARD & EXCEL EXPORT      -->
<!-- ========================================== -->
<section id="admin" class="w-full py-space-3xl px-margin-mobile md:px-margin-tablet lg:px-margin-desktop bg-surface border-t border-outline-variant/30">
  <div class="max-w-7xl mx-auto flex flex-col gap-space-xl">
    <!-- Header Title & Controls -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-headline font-bold bg-amber-500 text-slate-900 uppercase tracking-wider">
            <span class="material-symbols-outlined text-[13px]">shield</span>
            Administrator Board
          </span>
          <span class="text-xs text-on-surface-variant font-mono">• Live Roster Engine</span>
        </div>
        <h2 class="font-headline-lg text-headline-lg text-on-surface font-bold">
          Application Database &amp; Real-Time Submissions
        </h2>
        <p class="text-xs sm:text-sm text-on-surface-variant mt-1">
          Review candidate registrations, approve domain tracks, and export real-time Excel spreadsheets.
        </p>
      </div>

      <!-- Export Action Buttons -->
      <div class="flex flex-wrap items-center gap-3">
        <!-- Download CSV -->
        <button onclick="downloadCSVData()" class="inline-flex items-center gap-2 px-4 py-2.5 bg-surface-container-lowest hover:bg-surface-container text-on-surface text-xs font-headline font-bold rounded-lg border border-outline-variant/50 shadow-sm transition">
          <span class="material-symbols-outlined text-emerald-600 text-[18px]">table_chart</span>
          <span>Download CSV</span>
        </button>

        <!-- Download Excel (.xlsx) -->
        <button onclick="downloadExcelData()" class="inline-flex items-center gap-2 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg shadow-md transition">
          <span class="material-symbols-outlined text-white text-[18px]">file_download</span>
          <span>Download Excel (.xlsx)</span>
        </button>

        <!-- Refresh Button -->
        <button onclick="initSubmissionsData()" class="p-2.5 bg-surface-container-lowest hover:bg-surface-container text-on-surface rounded-lg border border-outline-variant/50 shadow-sm transition" title="Refresh records">
          <span class="material-symbols-outlined text-[18px] block">sync</span>
        </button>
      </div>
    </div>

    <!-- Metric KPI Cards -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="bg-surface-container-lowest p-5 rounded-xl border border-outline-variant/40 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-headline font-semibold text-on-surface-variant uppercase tracking-wider">Total Applicants</span>
          <span class="material-symbols-outlined text-secondary text-[20px]">groups</span>
        </div>
        <div id="stat-total" class="font-headline text-3xl font-bold text-on-surface">-</div>
        <div class="text-[11px] text-outline mt-1">Across all departments</div>
      </div>

      <div class="bg-surface-container-lowest p-5 rounded-xl border border-outline-variant/40 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-headline font-semibold text-on-surface-variant uppercase tracking-wider">Pending Review</span>
          <span class="material-symbols-outlined text-amber-500 text-[20px]">pending_actions</span>
        </div>
        <div id="stat-pending" class="font-headline text-3xl font-bold text-amber-600">-</div>
        <div class="text-[11px] text-outline mt-1">Awaiting coordinator review</div>
      </div>

      <div class="bg-surface-container-lowest p-5 rounded-xl border border-outline-variant/40 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-headline font-semibold text-on-surface-variant uppercase tracking-wider">Approved Members</span>
          <span class="material-symbols-outlined text-emerald-600 text-[20px]">verified</span>
        </div>
        <div id="stat-approved" class="font-headline text-3xl font-bold text-emerald-600">-</div>
        <div class="text-[11px] text-outline mt-1">Enrolled in CCIC research labs</div>
      </div>

      <div class="bg-surface-container-lowest p-5 rounded-xl border border-outline-variant/40 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-headline font-semibold text-on-surface-variant uppercase tracking-wider">AI Domains</span>
          <span class="material-symbols-outlined text-purple-600 text-[20px]">hub</span>
        </div>
        <div id="stat-domains" class="font-headline text-3xl font-bold text-purple-600">-</div>
        <div class="text-[11px] text-outline mt-1">Specialization categories</div>
      </div>
    </div>

    <!-- Filter & Search Controls -->
    <div class="bg-surface-container-lowest p-4 rounded-xl border border-outline-variant/40 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="relative w-full md:w-80">
        <span class="material-symbols-outlined absolute left-3 top-2.5 text-on-surface-variant text-[18px]">search</span>
        <input type="text" id="search-input" placeholder="Search by name, roll no, email..." class="w-full pl-9 pr-3 py-2 text-xs rounded-lg border border-outline-variant/50 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-surface-container-low">
      </div>

      <div class="flex flex-wrap items-center gap-3 w-full md:w-auto">
        <select id="filter-domain" class="text-xs py-2 px-3 rounded-lg border border-outline-variant/50 bg-surface-container-low font-medium text-on-surface outline-none focus:border-secondary">
          <option value="All">All Domains</option>
          <option value="Computer Vision &amp; Generative AI">Computer Vision &amp; Generative AI</option>
          <option value="Natural Language Processing">Natural Language Processing</option>
          <option value="Deep Reinforcement Learning &amp; Robotics">Deep Reinforcement Learning &amp; Robotics</option>
          <option value="Machine Learning &amp; Data Science">Machine Learning &amp; Data Science</option>
          <option value="Edge AI &amp; IoT Systems">Edge AI &amp; TinyML Systems</option>
        </select>

        <select id="filter-status" class="text-xs py-2 px-3 rounded-lg border border-outline-variant/50 bg-surface-container-low font-medium text-on-surface outline-none focus:border-secondary">
          <option value="All">All Statuses</option>
          <option value="Pending">Pending</option>
          <option value="Reviewed">Reviewed</option>
          <option value="Approved">Approved</option>
        </select>

        <span id="results-count" class="text-xs font-mono text-on-surface-variant ml-auto">
          Loading records...
        </span>
      </div>
    </div>

    <!-- Submissions Table -->
    <div class="bg-surface-container-lowest rounded-xl border border-outline-variant/40 shadow-sm overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="bg-surface-container-high text-on-surface-variant text-[11px] font-headline uppercase tracking-wider border-b border-outline-variant/30">
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
              <td colspan="8" class="text-center py-10 text-on-surface-variant font-medium">
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

<!-- Details & Success Modals -->
<div id="details-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
  <div class="bg-surface-container-lowest rounded-2xl p-6 max-w-lg w-full shadow-2xl border border-outline-variant/30">
    <div id="details-modal-content"></div>
    <div class="mt-6 pt-3 border-t border-outline-variant/30 text-right flex justify-end gap-2">
      <button onclick="closeDetailsModal()" class="px-4 py-2 bg-surface-container-high hover:bg-surface-container text-on-surface text-xs font-headline font-semibold rounded-lg transition">
        Close Details
      </button>
    </div>
  </div>
</div>

<div id="success-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
  <div class="bg-surface-container-lowest rounded-2xl p-8 max-w-md w-full text-center shadow-2xl border border-outline-variant/30">
    <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4">
      <span class="material-symbols-outlined text-4xl">verified</span>
    </div>
    <h3 class="font-headline text-xl font-bold text-on-surface mb-2">Application Received!</h3>
    <p class="text-xs text-on-surface-variant mb-6 leading-relaxed">
      Thank you for applying to the CCIC AIML Club. Your credentials have been logged into the Admin Board and Excel archive.
    </p>
    <div class="flex flex-wrap gap-2.5 justify-center">
      <a href="#admin" onclick="document.getElementById('success-modal').classList.add('hidden')" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-primary-container text-white text-xs font-headline font-semibold rounded-lg hover:bg-slate-800 transition shadow-sm">
        <span class="material-symbols-outlined text-[16px] text-amber-400">admin_panel_settings</span>
        <span>View in Admin Board</span>
      </a>
      <button onclick="downloadExcelData(); document.getElementById('success-modal').classList.add('hidden')" class="inline-flex items-center gap-1.5 px-3.5 py-2 bg-emerald-600 text-white text-xs font-headline font-semibold rounded-lg hover:bg-emerald-700 transition shadow-sm">
        <span class="material-symbols-outlined text-[16px]">file_download</span>
        <span>Download Excel</span>
      </button>
      <button onclick="document.getElementById('success-modal').classList.add('hidden')" class="px-3.5 py-2 bg-surface-container-high text-on-surface text-xs font-headline font-semibold rounded-lg hover:bg-surface-container transition">
        Close
      </button>
    </div>
  </div>
</div>
'''

stitch_home_html = stitch_home_html[:insert_point] + extra_sections + stitch_home_html[insert_point:]

# Add unified app script before </body>
script_tag = '<script src="/static/js/unified-app.js"></script>\n<script src="/static/js/smooth-scroll.js"></script>\n</body>'
stitch_home_html = stitch_home_html.replace("</body>", script_tag)

# Write to root index.html (for Vercel deployment)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(stitch_home_html)

# Write to templates/index.html (for local Flask dev server)
with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(stitch_home_html)

print("Authentic Stitch Home single-page website restored and generated successfully!")
