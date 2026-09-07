import re

MAGIC_PATH = r"c:\Users\ABHIJIT\Downloads\ccic web\templates\magic_members.html"

with open(MAGIC_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# --- 3rd Year Magic Members Replacement ---
third_year_replacement = """<!-- SECTION 2: 3rd Year Magic Members (Core R&D and Project Leads) -->
<section class="w-full bg-surface-container-low px-margin-mobile md:px-margin-tablet lg:px-margin-desktop py-space-2xl shadow-sm">
<div class="max-w-7xl mx-auto flex flex-col gap-space-xl">
<!-- Section Header -->
<div class="flex flex-col lg:flex-row lg:items-end justify-between gap-space-md">
<div class="flex flex-col gap-space-2xs">
<div class="flex items-center gap-space-2xs text-secondary">
<span class="material-symbols-outlined text-[18px]">memory</span>
<span class="font-label-sm text-label-sm uppercase tracking-widest font-bold">Research &amp; Core Prototyping</span>
</div>
<h2 class="font-headline-lg text-headline-lg text-on-surface font-bold tracking-tight">
3rd Year Magic Members
</h2>
<p class="font-body-md text-body-md text-on-surface-variant max-w-xl">
Experienced upperclassmen guiding autonomous agents, edge neural inference engines, and leading intercollegiate AI hack teams.
</p>
</div>
<div class="inline-flex items-center gap-space-xs bg-surface-container px-space-md py-space-xs rounded-xl self-start lg:self-auto">
<span class="w-2.5 h-2.5 rounded-full bg-secondary animate-pulse"></span>
<span class="font-label-sm text-label-sm text-on-surface font-semibold">5 Designated Core Leads</span>
</div>
</div>
<!-- 3rd Year Member Cards Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-space-md" id="third-year-grid">
<!-- Card 1: Mukesh Babu -->
<div class="member-card bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container flex items-center justify-center">
<div class="w-full h-full bg-gradient-to-br from-blue-900 to-slate-900 flex flex-col items-center justify-center text-white p-3 text-center">
<span class="material-symbols-outlined text-4xl text-blue-300 mb-1">psychology</span>
<span class="font-headline-sm font-bold text-sm">Mukesh Babu</span>
</div>
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-label-sm px-space-2xs py-1 rounded">
Yr 3 • AIDS
</span>
</div>
<div>
<div class="flex items-center justify-between">
<span class="font-label-sm text-label-sm font-bold text-secondary uppercase">🧠 Master Mind</span>
<span class="material-symbols-outlined text-[18px] text-secondary">psychology</span>
</div>
<h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-space-2xs">Mukesh Babu</h4>
<p class="font-body-md text-body-md text-on-surface-variant mt-1 text-xs line-clamp-2">
Strategic Artificial Intelligence &amp; Data Science architectures.
</p>
</div>
</div>
<div class="mt-space-md pt-space-xs flex items-center justify-between border-t border-slate-100">
<span class="font-label-sm text-label-sm text-secondary font-semibold">3rd Year – AIDS</span>
<span class="font-label-sm text-label-sm text-outline-variant">Core</span>
</div>
</div>
<!-- Card 2: Jayaganesh -->
<div class="member-card bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container">
<img class="w-full h-full object-cover" alt="Jayaganesh" src="/static/images/jayaganesh.jpg">
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-label-sm px-space-2xs py-1 rounded">
Yr 3 • AIML
</span>
</div>
<div>
<div class="flex items-center justify-between">
<span class="font-label-sm text-label-sm font-bold text-secondary uppercase">⚖️ Advocate</span>
<span class="material-symbols-outlined text-[18px] text-secondary">gavel</span>
</div>
<h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-space-2xs">Jayaganesh</h4>
<p class="font-body-md text-body-md text-on-surface-variant mt-1 text-xs line-clamp-2">
Model governance, neural compliance &amp; academic advocacy.
</p>
</div>
</div>
<div class="mt-space-md pt-space-xs flex items-center justify-between border-t border-slate-100">
<span class="font-label-sm text-label-sm text-secondary font-semibold">3rd Year – AIML</span>
<span class="font-label-sm text-label-sm text-outline-variant">Core</span>
</div>
</div>
<!-- Card 3: Megha Mithra -->
<div class="member-card bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container flex items-center justify-center">
<div class="w-full h-full bg-gradient-to-br from-indigo-900 to-slate-900 flex flex-col items-center justify-center text-white p-3 text-center">
<span class="material-symbols-outlined text-4xl text-indigo-300 mb-1">explore</span>
<span class="font-headline-sm font-bold text-sm">Megha Mithra</span>
</div>
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-label-sm px-space-2xs py-1 rounded">
Yr 3 • AIML
</span>
</div>
<div>
<div class="flex items-center justify-between">
<span class="font-label-sm text-label-sm font-bold text-secondary uppercase">🧭 Guide</span>
<span class="material-symbols-outlined text-[18px] text-secondary">explore</span>
</div>
<h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-space-2xs">Megha Mithra</h4>
<p class="font-body-md text-body-md text-on-surface-variant mt-1 text-xs line-clamp-2">
Student cohort mentorship, research trajectory &amp; project guidance.
</p>
</div>
</div>
<div class="mt-space-md pt-space-xs flex items-center justify-between border-t border-slate-100">
<span class="font-label-sm text-label-sm text-secondary font-semibold">3rd Year – AIML</span>
<span class="font-label-sm text-label-sm text-outline-variant">Core</span>
</div>
</div>
<!-- Card 4: Rishi -->
<div class="member-card bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container">
<img class="w-full h-full object-cover" alt="Rishi" src="/static/images/rishi.jpg">
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-label-sm px-space-2xs py-1 rounded">
Yr 3 • ECE
</span>
</div>
<div>
<div class="flex items-center justify-between">
<span class="font-label-sm text-label-sm font-bold text-secondary uppercase">📢 Influencer</span>
<span class="material-symbols-outlined text-[18px] text-secondary">campaign</span>
</div>
<h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-space-2xs">Rishi</h4>
<p class="font-body-md text-body-md text-on-surface-variant mt-1 text-xs line-clamp-2">
Hardware AI outreach, IoT edge communication &amp; intercollegiate drive.
</p>
</div>
</div>
<div class="mt-space-md pt-space-xs flex items-center justify-between border-t border-slate-100">
<span class="font-label-sm text-label-sm text-secondary font-semibold">3rd Year – ECE</span>
<span class="font-label-sm text-label-sm text-outline-variant">Core</span>
</div>
</div>
<!-- Card 5: Oviya -->
<div class="member-card bg-surface-container-lowest p-space-md rounded-xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between group">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container">
<img class="w-full h-full object-cover" alt="Oviya" src="/static/images/oviya.jpg">
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-label-sm text-label-sm px-space-2xs py-1 rounded">
Yr 2 • CSE
</span>
</div>
<div>
<div class="flex items-center justify-between">
<span class="font-label-sm text-label-sm font-bold text-secondary uppercase">💬 Communicator</span>
<span class="material-symbols-outlined text-[18px] text-secondary">forum</span>
</div>
<h4 class="font-headline-sm text-headline-sm font-bold text-on-surface mt-space-2xs">Oviya</h4>
<p class="font-body-md text-body-md text-on-surface-variant mt-1 text-xs line-clamp-2">
Technical publications, event dispatch &amp; institutional liaison.
</p>
</div>
</div>
<div class="mt-space-md pt-space-xs flex items-center justify-between border-t border-slate-100">
<span class="font-label-sm text-label-sm text-secondary font-semibold">2nd Year – CSE</span>
<span class="font-label-sm text-label-sm text-outline-variant">Core</span>
</div>
</div>
</div>
</div>
</section>"""

# --- 2nd Year Magic Members Replacement ---
second_year_replacement = """<!-- SECTION 3: 2nd Year Magic Members (Emerging Talent Cohort) -->
<section class="w-full px-margin-mobile md:px-margin-tablet lg:px-margin-desktop py-space-2xl bg-surface">
<div class="max-w-7xl mx-auto flex flex-col gap-space-xl">
<div class="flex flex-col md:flex-row md:items-end justify-between gap-space-md">
<div class="flex flex-col gap-space-2xs">
<div class="flex items-center gap-space-2xs text-secondary">
<span class="material-symbols-outlined text-[18px]">rocket_launch</span>
<span class="font-label-sm text-label-sm uppercase tracking-widest font-bold">Emerging Cadre • Sophomore Cohort</span>
</div>
<h2 class="font-headline-lg text-headline-lg text-on-surface font-bold tracking-tight">
2nd Year Magic Members
</h2>
<p class="font-body-md text-body-md text-on-surface-variant max-w-xl">
Rising developers, event architects, algorithm competitors, and creative evangelists driving day-to-day operations and sandbox prototypes.
</p>
</div>
<div class="inline-flex items-center gap-space-xs bg-surface-container px-space-md py-space-xs rounded-xl self-start md:self-auto">
<span class="w-2.5 h-2.5 rounded-full bg-secondary animate-pulse"></span>
<span class="font-label-sm text-label-sm text-on-surface font-semibold">Cohort 2024-2028 • 5 Active Leads</span>
</div>
</div>
<!-- 2nd Year Grid (5 Cards) -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-space-md">
<!-- 1. Oviya (Master Mind) -->
<div class="bg-surface-container-low p-space-md rounded-xl flex flex-col justify-between hover:bg-surface-container transition-all group shadow-sm">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container">
<img class="w-full h-full object-cover" alt="Oviya" src="/static/images/oviya.jpg">
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">
SEC25CS113
</span>
</div>
<div class="flex flex-col min-w-0">
<span class="font-label-sm text-label-sm text-secondary font-bold uppercase truncate">🧠 Master Mind</span>
<h5 class="font-title-md text-title-md font-bold text-on-surface truncate">Oviya</h5>
<span class="font-label-sm text-label-sm text-on-surface-variant font-mono">SEC25CS113 • 2nd Year</span>
<p class="text-xs text-slate-500 mt-1 line-clamp-2">Core logic architecture, neural model workflows &amp; system innovation.</p>
</div>
</div>
<div class="mt-space-sm pt-space-xs flex items-center justify-between text-on-surface-variant border-t border-slate-200/60">
<span class="font-label-sm text-label-sm font-medium">CSE Department</span>
<span class="material-symbols-outlined text-[18px] text-secondary">psychology</span>
</div>
</div>
<!-- 2. Dhanasekaran (Advocate) -->
<div class="bg-surface-container-low p-space-md rounded-xl flex flex-col justify-between hover:bg-surface-container transition-all group shadow-sm">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container flex items-center justify-center">
<div class="w-full h-full bg-gradient-to-br from-slate-800 to-blue-950 flex flex-col items-center justify-center text-white p-3 text-center">
<span class="material-symbols-outlined text-4xl text-amber-300 mb-1">balance</span>
<span class="font-headline-sm font-bold text-sm">Dhanasekaran</span>
</div>
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">
SEC25AM090
</span>
</div>
<div class="flex flex-col min-w-0">
<span class="font-label-sm text-label-sm text-secondary font-bold uppercase truncate">⚖️ Advocate</span>
<h5 class="font-title-md text-title-md font-bold text-on-surface truncate">Dhanasekaran</h5>
<span class="font-label-sm text-label-sm text-on-surface-variant font-mono">SEC25AM090 • 2nd Year</span>
<p class="text-xs text-slate-500 mt-1 line-clamp-2">Ethical AI frameworks, open source standards &amp; model verification.</p>
</div>
</div>
<div class="mt-space-sm pt-space-xs flex items-center justify-between text-on-surface-variant border-t border-slate-200/60">
<span class="font-label-sm text-label-sm font-medium">AIML Department</span>
<span class="material-symbols-outlined text-[18px] text-secondary">balance</span>
</div>
</div>
<!-- 3. Kalai Arasi K (Guide) -->
<div class="bg-surface-container-low p-space-md rounded-xl flex flex-col justify-between hover:bg-surface-container transition-all group shadow-sm">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container">
<img class="w-full h-full object-cover" alt="Kalai Arasi K" src="/static/images/kalai.jpg">
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">
SEC25CS085
</span>
</div>
<div class="flex flex-col min-w-0">
<span class="font-label-sm text-label-sm text-secondary font-bold uppercase truncate">🧭 Guide</span>
<h5 class="font-title-md text-title-md font-bold text-on-surface truncate">Kalai Arasi K</h5>
<span class="font-label-sm text-label-sm text-on-surface-variant font-mono">SEC25CS085 • 2nd Year</span>
<p class="text-xs text-slate-500 mt-1 line-clamp-2">Technical cohort coordination, peer learning &amp; repository structure.</p>
</div>
</div>
<div class="mt-space-sm pt-space-xs flex items-center justify-between text-on-surface-variant border-t border-slate-200/60">
<span class="font-label-sm text-label-sm font-medium">CSE Department</span>
<span class="material-symbols-outlined text-[18px] text-secondary">explore</span>
</div>
</div>
<!-- 4. Abhijit (Influencer) -->
<div class="bg-surface-container-low p-space-md rounded-xl flex flex-col justify-between hover:bg-surface-container transition-all group shadow-sm">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container flex items-center justify-center">
<div class="w-full h-full bg-gradient-to-br from-blue-900 to-indigo-950 flex flex-col items-center justify-center text-white p-3 text-center">
<span class="material-symbols-outlined text-4xl text-cyan-300 mb-1">campaign</span>
<span class="font-headline-sm font-bold text-sm">Abhijit</span>
</div>
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">
SEC25AM112
</span>
</div>
<div class="flex flex-col min-w-0">
<span class="font-label-sm text-label-sm text-secondary font-bold uppercase truncate">📢 Influencer</span>
<h5 class="font-title-md text-title-md font-bold text-on-surface truncate">Abhijit</h5>
<span class="font-label-sm text-label-sm text-on-surface-variant font-mono">SEC25AM112 • 2nd Year</span>
<p class="text-xs text-slate-500 mt-1 line-clamp-2">Hackathon evangelism, AI community engagement &amp; technology sprints.</p>
</div>
</div>
<div class="mt-space-sm pt-space-xs flex items-center justify-between text-on-surface-variant border-t border-slate-200/60">
<span class="font-label-sm text-label-sm font-medium">AIML Department</span>
<span class="material-symbols-outlined text-[18px] text-secondary">campaign</span>
</div>
</div>
<!-- 5. Sanjana (Communicator) -->
<div class="bg-surface-container-low p-space-md rounded-xl flex flex-col justify-between hover:bg-surface-container transition-all group shadow-sm">
<div class="flex flex-col gap-space-sm">
<div class="relative w-full aspect-square rounded-lg overflow-hidden bg-surface-container">
<img class="w-full h-full object-cover" alt="Sanjana" src="/static/images/sanjana.jpg">
<span class="absolute top-2 right-2 bg-surface-container-highest/90 backdrop-blur-sm text-on-surface font-mono text-[11px] px-1.5 py-0.5 rounded font-bold">
SEC25EC020
</span>
</div>
<div class="flex flex-col min-w-0">
<span class="font-label-sm text-label-sm text-secondary font-bold uppercase truncate">💬 Communicator</span>
<h5 class="font-title-md text-title-md font-bold text-on-surface truncate">Sanjana</h5>
<span class="font-label-sm text-label-sm text-on-surface-variant font-mono">SEC25EC020 • 2nd Year</span>
<p class="text-xs text-slate-500 mt-1 line-clamp-2">Club communications, interface documentation &amp; creative media.</p>
</div>
</div>
<div class="mt-space-sm pt-space-xs flex items-center justify-between text-on-surface-variant border-t border-slate-200/60">
<span class="font-label-sm text-label-sm font-medium">ECE Department</span>
<span class="material-symbols-outlined text-[18px] text-secondary">forum</span>
</div>
</div>
</div>
</div>
</section>"""

# Find Section 2 start and Section 4 start
sec2_start = content.find("<!-- SECTION 2: 3rd Year Magic Members")
sec4_start = content.find("<!-- SECTION 4: Interactive Callout")

if sec2_start != -1 and sec4_start != -1:
    content = content[:sec2_start] + third_year_replacement + "\n" + second_year_replacement + "\n" + content[sec4_start:]
    with open(MAGIC_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully replaced Section 2 and Section 3 in magic_members.html")
else:
    print(f"Error locating sections: sec2={sec2_start}, sec4={sec4_start}")
