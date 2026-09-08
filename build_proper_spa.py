import os

# Create the clean, professionally architected Single Page Application
html_content = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CCIC • Center for Computational Intelligence and Cognition | Sri Sairam Engineering College</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "surface-dim": "#d2d9f4",
            "outline": "#75777e",
            "secondary": "#0057c0",
            "secondary-container": "#006ff0",
            "on-secondary": "#ffffff",
            "surface": "#faf8ff",
            "surface-container": "#eaedff",
            "surface-container-high": "#e2e7ff",
            "surface-container-low": "#f2f3ff",
            "surface-container-lowest": "#ffffff",
            "on-surface": "#131b2e",
            "on-surface-variant": "#45464d",
            "primary-container": "#07132b",
            "on-primary-container": "#7983a1",
            "outline-variant": "#c6c6ce"
          },
          fontFamily: {
            headline: ["Space Grotesk", "sans-serif"],
            body: ["Plus Jakarta Sans", "sans-serif"]
          }
        }
      }
    };
  </script>

  <!-- SheetJS for Client-Side Excel Export on Vercel -->
  <script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>

  <!-- Transitions and Smooth Scroll -->
  <link rel="stylesheet" href="/static/css/transitions.css">
  <style>
    /* Section smooth scrolling offset */
    section { scroll-margin-top: 5rem; }
    .nav-active {
      background-color: #0057c0 !important;
      color: #ffffff !important;
      font-weight: 700 !important;
    }
  </style>
</head>
<body class="bg-[#faf8ff] font-body text-on-surface antialiased relative selection:bg-secondary selection:text-white">

  <!-- Watermark -->
  <div class="fixed inset-0 pointer-events-none z-0 flex items-center justify-center opacity-[0.03]">
    <img alt="CCIC Watermark" class="w-[600px] h-[600px] max-w-[80vw] max-h-[80vh] object-contain filter grayscale" src="/static/images/ccic_logo.jpg">
  </div>

  <!-- STICKY HEADER & NAVIGATION -->
  <header class="sticky top-0 left-0 w-full z-50 shadow-sm bg-white/95 backdrop-blur-md border-b border-slate-200">
    <!-- Top Institutional Bar -->
    <div class="w-full bg-[#07132b] text-slate-300 px-4 py-1 text-center border-b border-slate-800">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-center gap-x-4 gap-y-1 text-[11px] font-headline uppercase tracking-wider">
        <span class="text-blue-300 font-bold">Sri Sairam Engineering College</span>
        <span class="text-slate-600">•</span>
        <span class="text-slate-200">Department of CSE (Artificial Intelligence &amp; Machine Learning)</span>
        <span class="text-slate-600">•</span>
        <span class="text-amber-400 font-semibold">Autonomous Institution</span>
      </div>
    </div>

    <!-- Main Navigation Bar -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 sm:h-20 flex items-center justify-between gap-4">
      <!-- Logo & Title -->
      <a href="#home" class="flex items-center gap-3 group">
        <img alt="CCIC Logo" class="h-10 w-10 object-cover rounded-full border border-slate-200 shadow-sm transition group-hover:scale-105" src="/static/images/ccic_logo.jpg">
        <div class="flex flex-col">
          <div class="flex items-center gap-2">
            <span class="font-headline font-bold text-lg text-slate-900 leading-none">CCIC</span>
            <span class="text-[10px] font-headline font-bold bg-secondary/10 text-secondary px-1.5 py-0.5 rounded uppercase">AIML Club</span>
          </div>
          <span class="text-[11px] text-slate-500 font-medium hidden sm:inline-block leading-tight">Computational &amp; Cognitive Intelligence</span>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-1 font-headline text-xs font-semibold">
        <a class="nav-link px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100 transition" href="#home">Home</a>
        <a class="nav-link px-3 py-2 rounded-lg text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition" href="#events">Events</a>
        <a class="nav-link px-3 py-2 rounded-lg text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition" href="#magic-members">Magic Members</a>
        <a class="nav-link px-3 py-2 rounded-lg text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition" href="#scope-members">Scope Members</a>
        <a class="nav-link px-3 py-2 rounded-lg text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition" href="#register">Register</a>
        <a class="nav-link px-3 py-2 rounded-lg text-amber-700 bg-amber-50 hover:bg-amber-100 transition flex items-center gap-1 font-bold" href="#admin">
          <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
          Admin Board
        </a>
      </nav>

      <!-- Header Action Buttons -->
      <div class="flex items-center gap-3">
        <!-- One-Click Download Excel Button on Header -->
        <button onclick="downloadExcelData()" class="hidden sm:inline-flex items-center gap-1.5 px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg shadow-sm transition">
          <span class="material-symbols-outlined text-[16px]">file_download</span>
          <span>Download Excel</span>
        </button>

        <a href="#register" class="px-4 py-2 bg-secondary hover:bg-blue-700 text-white text-xs font-headline font-bold rounded-lg shadow-sm transition">
          Apply Now
        </a>

        <!-- Mobile Menu Toggle Button -->
        <button id="mobile-menu-btn" class="lg:hidden p-2 text-slate-700 hover:bg-slate-100 rounded-lg">
          <span class="material-symbols-outlined text-[24px]">menu</span>
        </button>
      </div>
    </div>

    <!-- Mobile Dropdown Menu -->
    <div id="mobile-menu" class="hidden lg:hidden bg-white border-b border-slate-200 px-6 py-4 flex flex-col gap-2 shadow-xl">
      <a href="#home" class="py-2 text-sm font-headline font-semibold text-slate-800 hover:text-secondary">Home</a>
      <a href="#events" class="py-2 text-sm font-headline font-semibold text-slate-600 hover:text-secondary">Activities &amp; Events</a>
      <a href="#magic-members" class="py-2 text-sm font-headline font-semibold text-slate-600 hover:text-secondary">Magic Members</a>
      <a href="#scope-members" class="py-2 text-sm font-headline font-semibold text-slate-600 hover:text-secondary">Scope Members</a>
      <a href="#register" class="py-2 text-sm font-headline font-semibold text-slate-600 hover:text-secondary">Apply for Membership</a>
      <a href="#admin" class="py-2 text-sm font-headline font-bold text-amber-700 hover:text-amber-800 flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[18px]">admin_panel_settings</span>
        Administrator Portal
      </a>
      <div class="pt-3 border-t border-slate-100 flex flex-col gap-2">
        <button onclick="downloadExcelData()" class="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg flex items-center justify-center gap-2 transition shadow-sm">
          <span class="material-symbols-outlined text-[16px]">file_download</span>
          Download Excel Spreadsheet (.xlsx)
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN CONTENT CONTAINER -->
  <main class="w-full relative z-10">

    <!-- ========================================== -->
    <!-- SECTION 1: HERO & INSTITUTIONAL LEADERSHIP -->
    <!-- ========================================== -->
    <section id="home" class="w-full">
      <!-- Accreditation Ribbon -->
      <div class="w-full bg-[#eaedff] py-2 px-4 border-b border-slate-200">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3 text-xs text-slate-700">
          <div class="flex items-center gap-2 font-headline font-bold text-secondary">
            <span class="material-symbols-outlined text-[16px]">verified</span>
            NIRF RANK 157 | ARIIA TOP 25 INNOVATION
          </div>
          <div class="text-[11px] font-medium text-slate-600">
            Affiliated: IEEE EMBS • IEEE Madras Section • AICTE Approved
          </div>
        </div>
      </div>

      <!-- Hero Main Banner -->
      <div class="max-w-7xl mx-auto px-4 sm:px-6 py-12 md:py-20">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-7 flex flex-col items-start gap-6">
            <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-headline font-bold bg-secondary/10 text-secondary border border-secondary/20">
              <span class="material-symbols-outlined text-[16px]">neurology</span>
              Cognitive Neural Academic Initiative
            </span>

            <h1 class="font-headline text-3xl sm:text-5xl lg:text-6xl font-bold text-slate-900 tracking-tight leading-[1.15]">
              Center for <span class="text-secondary">Computational</span> Intelligence and Cognition
            </h1>

            <p class="font-body text-sm sm:text-base text-slate-600 leading-relaxed max-w-2xl">
              Architecting the confluence of cognitive computing, autonomous agents, and enterprise artificial intelligence. Spearheaded by the Department of Computer Science &amp; Engineering (AI &amp; ML) at Sri Sairam Engineering College.
            </p>

            <div class="flex flex-wrap items-center gap-3 pt-2">
              <a href="#register" class="px-6 py-3 bg-secondary hover:bg-blue-700 text-white font-headline font-bold text-sm rounded-xl transition shadow-md flex items-center gap-2">
                <span>Apply for Membership</span>
                <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
              </a>
              <a href="#events" class="px-6 py-3 bg-white hover:bg-slate-50 text-slate-800 font-headline font-semibold text-sm rounded-xl border border-slate-300 shadow-sm transition flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary text-[18px]">calendar_month</span>
                <span>Explore Events</span>
              </a>
              <a href="#admin" class="px-4 py-3 bg-amber-50 hover:bg-amber-100 text-amber-800 font-headline font-semibold text-sm rounded-xl border border-amber-200 transition flex items-center gap-1.5">
                <span class="material-symbols-outlined text-[18px]">table_chart</span>
                <span>Admin Board</span>
              </a>
            </div>

            <!-- Key Metric Counters -->
            <div class="grid grid-cols-3 gap-4 pt-6 border-t border-slate-200 w-full">
              <div>
                <div class="font-headline text-2xl sm:text-3xl font-bold text-slate-900">38+</div>
                <div class="text-xs text-slate-500 font-medium mt-0.5">Active Researchers</div>
              </div>
              <div>
                <div class="font-headline text-2xl sm:text-3xl font-bold text-secondary">14</div>
                <div class="text-xs text-slate-500 font-medium mt-0.5">Agentic Prototypes</div>
              </div>
              <div>
                <div class="font-headline text-2xl sm:text-3xl font-bold text-slate-900">06</div>
                <div class="text-xs text-slate-500 font-medium mt-0.5">Research Labs</div>
              </div>
            </div>
          </div>

          <!-- Hero Image & Group Showcase -->
          <div class="lg:col-span-5 relative">
            <div class="rounded-2xl overflow-hidden shadow-2xl border-4 border-white bg-slate-900 group">
              <img src="/static/images/ccic_group.jpg" alt="CCIC AIML Club Community" class="w-full h-80 sm:h-96 object-cover transition-transform duration-500 group-hover:scale-105">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex flex-col justify-end p-6 text-white">
                <span class="text-xs font-headline font-bold text-amber-400 uppercase tracking-wider">Research Vanguard</span>
                <span class="font-headline text-lg font-bold">CCIC Student Innovation Cohort</span>
                <span class="text-xs text-slate-300">Empowered by IEEE EMBS &amp; Sri Sairam Institutions</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Core Research Domains -->
      <div class="bg-white py-12 border-y border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
          <div class="text-center max-w-2xl mx-auto mb-10">
            <span class="text-xs font-headline font-bold uppercase tracking-widest text-secondary">Strategic Directives</span>
            <h2 class="font-headline text-2xl sm:text-3xl font-bold text-slate-900 mt-1">Core AI Research Domains</h2>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="p-6 rounded-xl bg-slate-50 border border-slate-200 hover:shadow-md transition">
              <div class="w-12 h-12 rounded-xl bg-blue-100 text-secondary flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-2xl">visibility</span>
              </div>
              <h3 class="font-headline font-bold text-base text-slate-900 mb-2">Computer Vision &amp; GenAI</h3>
              <p class="text-xs text-slate-600 leading-relaxed">Medical imaging, diffusion models, generative visual synthesis, and real-time spatial neural architectures.</p>
            </div>

            <div class="p-6 rounded-xl bg-slate-50 border border-slate-200 hover:shadow-md transition">
              <div class="w-12 h-12 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-2xl">chat</span>
              </div>
              <h3 class="font-headline font-bold text-base text-slate-900 mb-2">NLP &amp; LLM Agents</h3>
              <p class="text-xs text-slate-600 leading-relaxed">Multi-agent orchestrations, reasoning engines, RAG pipelines, and neuro-symbolic language models.</p>
            </div>

            <div class="p-6 rounded-xl bg-slate-50 border border-slate-200 hover:shadow-md transition">
              <div class="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-2xl">smart_toy</span>
              </div>
              <h3 class="font-headline font-bold text-base text-slate-900 mb-2">Robotics &amp; DRL</h3>
              <p class="text-xs text-slate-600 leading-relaxed">Deep reinforcement learning, autonomous robot navigation, and physical simulation environments.</p>
            </div>

            <div class="p-6 rounded-xl bg-slate-50 border border-slate-200 hover:shadow-md transition">
              <div class="w-12 h-12 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center mb-4">
                <span class="material-symbols-outlined text-2xl">memory</span>
              </div>
              <h3 class="font-headline font-bold text-base text-slate-900 mb-2">Edge AI &amp; TinyML</h3>
              <p class="text-xs text-slate-600 leading-relaxed">Ultra low-power neural networks, micro-controller inferences, and smart embedded sensor nodes.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Institutional Leadership -->
      <div class="bg-[#faf8ff] py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
          <div class="text-center max-w-2xl mx-auto mb-10">
            <span class="text-xs font-headline font-bold uppercase tracking-widest text-secondary">Academic Governance</span>
            <h2 class="font-headline text-2xl sm:text-3xl font-bold text-slate-900 mt-1">Institutional Leadership Steering Excellence</h2>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Chairman -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center">
              <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBCu_9uYv7R3fP0kK2U0X5M" alt="Dr. Sai Prakash Leo Muthu" class="w-24 h-24 rounded-full object-cover border-2 border-secondary shadow mb-4" onerror="this.src='/static/images/ccic_logo.jpg'">
              <span class="text-[11px] font-headline font-bold uppercase text-secondary tracking-wider">Chief Patron</span>
              <h3 class="font-headline text-lg font-bold text-slate-900 mt-1">Dr. Sai Prakash Leo Muthu</h3>
              <p class="text-xs text-slate-500">Chairman &amp; CEO • Sairam Institutions</p>
            </div>

            <!-- Principal SEC -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center">
              <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCx4r9RGrMNgsJsWaHbvQ1iUeKjPygnmJOCHlw7AtSkGJO8nOWspZ_CcmAGdeb8j9xxAsWPly24QjfGepv9NgTxqvhGyT6XE9_YuihU9WPFoVEmF8547HndH8ACbjSMJnmmPdcf2C6ikfQRklsJ1vxecRUh257KbHFf7eSSz4epa8XAIrBGDGt5r7iCOfm-dksUkqrpO0UWadnh4E4obLKRrqto8CDMh1OtLtiEfon1_5Aet0Mwo-9WoCo1dfr3ebMNKw" alt="Dr. J. Raja" class="w-24 h-24 rounded-full object-cover border-2 border-secondary shadow mb-4" onerror="this.src='/static/images/ccic_logo.jpg'">
              <span class="text-[11px] font-headline font-bold uppercase text-secondary tracking-wider">Academic Leadership</span>
              <h3 class="font-headline text-lg font-bold text-slate-900 mt-1">Dr. J. Raja</h3>
              <p class="text-xs text-slate-500">Principal • Sri Sairam Engineering College (SEC)</p>
            </div>

            <!-- Principal SIT -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center">
              <img src="/static/images/palanikumar.jpg" alt="Dr. Palanikumar K" class="w-24 h-24 rounded-full object-cover border-2 border-secondary shadow mb-4" onerror="this.src='/static/images/ccic_logo.jpg'">
              <span class="text-[11px] font-headline font-bold uppercase text-secondary tracking-wider">Academic Leadership</span>
              <h3 class="font-headline text-lg font-bold text-slate-900 mt-1">Dr. Palanikumar K</h3>
              <p class="text-xs text-slate-500">Principal • Sri Sairam Institute of Technology (SIT)</p>
            </div>

            <!-- HOD -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center">
              <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCLH04SgY8e8FchqgP5n1dVPOBbJqGP0172G4VG11DcZzD5Ixf_wM6x6EMLv8JbuNqaTpWUw72sFulRWym65kp50ALLgjPTA5DxvxYkQIOGQa_vl2kX7UBfs-vEQvMgsuvikiJJe_Q-fj6eh_ET9cg5gIHPt1Wc07LQ1kzZEh0pQYHhjWoSGQeupyDJ5hUs3OalOvn6qVQaAySueBj4hBhDIW0niLT6i1DtQtu4Cyb-oqSTWHuhnNZNZQnQCNia1LVIJw" alt="Dr. E. Priya" class="w-24 h-24 rounded-full object-cover border-2 border-secondary shadow mb-4" onerror="this.src='/static/images/ccic_logo.jpg'">
              <span class="text-[11px] font-headline font-bold uppercase text-secondary tracking-wider">Program Chair</span>
              <h3 class="font-headline text-lg font-bold text-slate-900 mt-1">Dr. E. Priya</h3>
              <p class="text-xs text-slate-500">Head of Department • CSE (AI &amp; ML)</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: ACTIVITIES & EVENTS REGISTRY    -->
    <!-- ========================================== -->
    <section id="events" class="w-full py-16 bg-white border-t border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-10">
          <div>
            <span class="text-xs font-headline font-bold uppercase tracking-widest text-secondary">Assemblies &amp; Hackathons</span>
            <h2 class="font-headline text-2xl sm:text-4xl font-bold text-slate-900 mt-1">Activities &amp; Events Registry</h2>
            <p class="text-xs sm:text-sm text-slate-600 mt-1 max-w-xl">
              Signature tech conclaves, autonomous neural agent bootcamps, and cognitive AI hackathons.
            </p>
          </div>

          <!-- Category Filter Buttons -->
          <div class="flex flex-wrap items-center gap-2" id="event-filters">
            <button class="filter-btn active px-3.5 py-1.5 rounded-lg text-xs font-headline font-bold bg-secondary text-white shadow-sm transition" data-filter="all">All Events</button>
            <button class="filter-btn px-3.5 py-1.5 rounded-lg text-xs font-headline font-semibold text-slate-600 hover:bg-slate-100 transition" data-filter="inauguration">Inauguration</button>
            <button class="filter-btn px-3.5 py-1.5 rounded-lg text-xs font-headline font-semibold text-slate-600 hover:bg-slate-100 transition" data-filter="bootcamp">Bootcamps</button>
            <button class="filter-btn px-3.5 py-1.5 rounded-lg text-xs font-headline font-semibold text-slate-600 hover:bg-slate-100 transition" data-filter="hackathon">Hackathons</button>
          </div>
        </div>

        <div class="space-y-8" id="events-container">
          <!-- Event 1: Inauguration of CCIC -->
          <article class="event-item inauguration bg-slate-50 rounded-2xl border border-slate-200 p-6 sm:p-8 hover:shadow-lg transition">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
              <div class="lg:col-span-5">
                <img src="/static/images/ccic_banner.jpg" alt="CCIC Inauguration Poster" class="w-full h-64 object-cover rounded-xl shadow-md border border-slate-200">
                <p class="text-[11px] text-slate-500 text-center mt-2 font-mono">Record SEC202605CCC01 • Tesla Hall (SEC)</p>
              </div>
              <div class="lg:col-span-7 flex flex-col gap-4">
                <div class="flex items-center gap-2">
                  <span class="px-2.5 py-0.5 rounded-md text-[10px] font-headline font-bold bg-emerald-100 text-emerald-800">Completed Session</span>
                  <span class="text-xs text-slate-500 font-mono">8th May 2026 • Friday</span>
                </div>
                <h3 class="font-headline text-xl sm:text-2xl font-bold text-slate-900">
                  Inauguration of CCIC (Computational and Cognitive Intelligence Club)
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                  Inaugural session establishing the specialized departmental forum bridging neuro-symbolic computational logic, deep cognitive modeling, and enterprise artificial intelligence with collegiate research groups.
                </p>
                <div class="p-4 bg-white rounded-xl border border-slate-200 flex items-center gap-4">
                  <div class="w-12 h-12 rounded-full bg-secondary-container text-white flex items-center justify-center font-bold text-base shrink-0">
                    TR
                  </div>
                  <div>
                    <span class="text-[10px] font-headline font-bold text-secondary uppercase">Distinguished Chief Guest</span>
                    <h4 class="font-headline font-bold text-sm text-slate-900">Mr. THIRUMURUGAN R</h4>
                    <p class="text-xs text-slate-500">AI &amp; ML Engineer • Co-Founder @ Social Eagle</p>
                  </div>
                </div>
              </div>
            </div>
          </article>

          <!-- Event 2: Agent Bootcamp -->
          <article class="event-item bootcamp bg-slate-50 rounded-2xl border border-slate-200 p-6 sm:p-8 hover:shadow-lg transition">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
              <div class="lg:col-span-5">
                <img src="/static/images/ccic_group.jpg" alt="Agent Bootcamp" class="w-full h-64 object-cover rounded-xl shadow-md border border-slate-200">
                <p class="text-[11px] text-slate-500 text-center mt-2 font-mono">Record SEC202605CCC02 • Cognitive Compute Lab</p>
              </div>
              <div class="lg:col-span-7 flex flex-col gap-4">
                <div class="flex items-center gap-2">
                  <span class="px-2.5 py-0.5 rounded-md text-[10px] font-headline font-bold bg-blue-100 text-blue-800">Hands-on Workshop</span>
                  <span class="text-xs text-slate-500 font-mono">Full-Day Intensive</span>
                </div>
                <h3 class="font-headline text-xl sm:text-2xl font-bold text-slate-900">
                  Bootcamp on Content Creation Automation Using AI Agents
                </h3>
                <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                  End-to-end masterclass exploring multi-agent architectures (CrewAI, LangGraph), local LLM workflows, automated visual assets synthesis, and API integration for production-ready content engines.
                </p>
                <div class="flex flex-wrap gap-2 pt-2">
                  <span class="px-2.5 py-1 bg-white border border-slate-200 rounded-md text-xs text-slate-700 font-mono">LangGraph</span>
                  <span class="px-2.5 py-1 bg-white border border-slate-200 rounded-md text-xs text-slate-700 font-mono">Ollama LLMs</span>
                  <span class="px-2.5 py-1 bg-white border border-slate-200 rounded-md text-xs text-slate-700 font-mono">Autonomous Agents</span>
                </div>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: MAGIC MEMBERS ROSTER            -->
    <!-- ========================================== -->
    <section id="magic-members" class="w-full py-16 bg-[#faf8ff] border-t border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="text-xs font-headline font-bold uppercase tracking-widest text-secondary">Student Leadership</span>
          <h2 class="font-headline text-2xl sm:text-4xl font-bold text-slate-900 mt-1">Magic Members &amp; Student Leads</h2>
          <p class="text-xs sm:text-sm text-slate-600 mt-2">
            Chief orchestrators, model architects, and technology evangelists across the 3rd Year and 2nd Year cohorts.
          </p>
        </div>

        <!-- Student Coordinators (Prominent Feature) -->
        <div class="mb-12">
          <h3 class="font-headline text-lg font-bold text-slate-900 mb-6 flex items-center gap-2">
            <span class="material-symbols-outlined text-secondary">stars</span>
            Lead Student Coordinators
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- S L Hari Priyan -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col sm:flex-row items-center gap-6 group hover:shadow-md transition">
              <img src="/static/images/haripriyan.jpg" alt="S L Hari Priyan" class="w-28 h-28 rounded-xl object-cover border-2 border-secondary shadow-sm group-hover:scale-105 transition">
              <div>
                <span class="text-[10px] font-headline font-bold uppercase px-2 py-0.5 rounded bg-secondary/10 text-secondary">Lead Coordinator</span>
                <h4 class="font-headline text-lg font-bold text-slate-900 mt-1">S L HARI PRIYAN</h4>
                <p class="text-xs text-slate-500 font-medium">Department of CSE (AI &amp; ML) • Final Year</p>
                <div class="flex flex-wrap gap-1.5 mt-3">
                  <span class="px-2 py-0.5 bg-slate-100 rounded text-[10px] text-slate-700">Cognitive Systems</span>
                  <span class="px-2 py-0.5 bg-slate-100 rounded text-[10px] text-slate-700">Multi-Agent AI</span>
                  <span class="px-2 py-0.5 bg-slate-100 rounded text-[10px] text-slate-700">IEEE Lead</span>
                </div>
              </div>
            </div>

            <!-- K Guru Prakash -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col sm:flex-row items-center gap-6 group hover:shadow-md transition">
              <img src="/static/images/guru.jpg" alt="K Guru Prakash" class="w-28 h-28 rounded-xl object-cover border-2 border-secondary shadow-sm group-hover:scale-105 transition">
              <div>
                <span class="text-[10px] font-headline font-bold uppercase px-2 py-0.5 rounded bg-amber-500/10 text-amber-700">Co-lead Coordinator</span>
                <h4 class="font-headline text-lg font-bold text-slate-900 mt-1">K GURU PRAKASH</h4>
                <p class="text-xs text-slate-500 font-medium">Department of CSE (AI &amp; ML) • Final Year</p>
                <div class="flex flex-wrap gap-1.5 mt-3">
                  <span class="px-2 py-0.5 bg-slate-100 rounded text-[10px] text-slate-700">Robotics &amp; Vision</span>
                  <span class="px-2 py-0.5 bg-slate-100 rounded text-[10px] text-slate-700">Edge Hardware</span>
                  <span class="px-2 py-0.5 bg-slate-100 rounded text-[10px] text-slate-700">Operations</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3rd Year Magic Members -->
        <div class="mb-12">
          <div class="flex items-center justify-between mb-6">
            <h3 class="font-headline text-lg font-bold text-slate-900 flex items-center gap-2">
              <span class="material-symbols-outlined text-secondary">memory</span>
              3rd Year Magic Members
            </h3>
            <span class="text-xs font-mono text-slate-500">5 Designated Core Leads</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4">
            <!-- Mukesh Babu -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/mukesh.jpg" alt="Mukesh Babu" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">🧠 Master Mind</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Mukesh Babu</h4>
                <p class="text-[11px] text-slate-500">3rd Year – AIDS</p>
              </div>
            </div>

            <!-- Jayaganesh -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/jayaganesh.jpg" alt="Jayaganesh" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">⚖️ Advocate</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Jayaganesh</h4>
                <p class="text-[11px] text-slate-500">3rd Year – AIML</p>
              </div>
            </div>

            <!-- Megha Mithra -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/meghamithra.jpg" alt="Megha Mithra" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">🧭 Guide</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Megha Mithra</h4>
                <p class="text-[11px] text-slate-500">3rd Year – AIML</p>
              </div>
            </div>

            <!-- Rishi -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/rishi.jpg" alt="Rishi" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">📢 Influencer</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Rishi</h4>
                <p class="text-[11px] text-slate-500">3rd Year – ECE</p>
              </div>
            </div>

            <!-- Oviya -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/oviya.jpg" alt="Oviya" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">💬 Communicator</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Oviya</h4>
                <p class="text-[11px] text-slate-500">2nd Year – CSE</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 2nd Year Magic Members -->
        <div>
          <div class="flex items-center justify-between mb-6">
            <h3 class="font-headline text-lg font-bold text-slate-900 flex items-center gap-2">
              <span class="material-symbols-outlined text-secondary">rocket_launch</span>
              2nd Year Magic Members
            </h3>
            <span class="text-xs font-mono text-slate-500">Cohort 2024–2028 • 5 Active Leads</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4">
            <!-- 1. Oviya -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/oviya.jpg" alt="Oviya" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">🧠 Master Mind</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Oviya</h4>
                <p class="text-[11px] font-mono text-slate-500">SEC25CS113 • 2nd Year</p>
              </div>
            </div>

            <!-- 2. Dhanasekaran -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/dhanasekaran.jpg" alt="Dhanasekaran" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">⚖️ Advocate</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Dhanasekaran</h4>
                <p class="text-[11px] font-mono text-slate-500">SEC25AM090 • 2nd Year</p>
              </div>
            </div>

            <!-- 3. Kalai Arasi K -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/kalai.jpg" alt="Kalai Arasi K" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">🧭 Guide</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Kalai Arasi K</h4>
                <p class="text-[11px] font-mono text-slate-500">SEC25CS085 • 2nd Year</p>
              </div>
            </div>

            <!-- 4. Abhijit -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/abhijit.jpg" alt="Abhijit" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">📢 Influencer</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Abhijit</h4>
                <p class="text-[11px] font-mono text-slate-500">SEC25AM112 • 2nd Year</p>
              </div>
            </div>

            <!-- 5. Sanjana -->
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
              <div>
                <div class="aspect-square rounded-lg overflow-hidden mb-3 bg-slate-100">
                  <img src="/static/images/sanjana.jpg" alt="Sanjana" class="w-full h-full object-cover">
                </div>
                <span class="text-[10px] font-headline font-bold text-secondary uppercase">💬 Communicator</span>
                <h4 class="font-headline font-bold text-sm text-slate-900 mt-0.5">Sanjana</h4>
                <p class="text-[11px] font-mono text-slate-500">SEC25EC020 • 2nd Year</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: SCOPE MEMBERS (FACULTY LEADS)   -->
    <!-- ========================================== -->
    <section id="scope-members" class="w-full py-16 bg-white border-t border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="text-xs font-headline font-bold uppercase tracking-widest text-secondary">Faculty Scope &amp; Advisory</span>
          <h2 class="font-headline text-2xl sm:text-4xl font-bold text-slate-900 mt-1">Scope Members Roster</h2>
          <p class="text-xs sm:text-sm text-slate-600 mt-2">
            Academic mentors and faculty coordinators steering strategic research compliance across collegiate labs.
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 1. Dr. R. Geetha -->
          <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm flex items-start gap-4">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDyOcOpbd19Zc1vSSsnCdGfKKedjQdYHjcKEJZ1iH61GG9-5SB5ATwNg3RfZcmiEqTlGQ99-qe60HkgYHdtt2jyoS9bjkOynoYH-X9TJ4U-4I6Csj2lmIp4xMQP36dlgxV2w6OzC4YjCMcDEZHSlQysHiHb_qSHl-E6uy_WDkYghi1tqkxzuiVPKrcigs4KNtsjF7LItMtJGEq5SMC5dS9a4_qqhidqDzJ7A0ee7HudoRylABVkpBA_IOMZoFaltfiIQA" alt="Dr. R. Geetha" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-300" onerror="this.src='/static/images/ccic_logo.jpg'">
            <div>
              <span class="text-[10px] font-headline font-bold uppercase text-secondary">Strategist</span>
              <h4 class="font-headline font-bold text-sm text-slate-900">Dr. R. Geetha</h4>
              <p class="text-xs text-slate-500">Assistant Professor • SEC, CSE (AI &amp; ML)</p>
              <p class="text-[11px] text-slate-600 mt-1.5 font-medium">Healthcare ML &amp; Neuro-Symbolic AI</p>
            </div>
          </div>

          <!-- 2. Dr. V. Lalitha -->
          <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm flex items-start gap-4">
            <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDvB7eDfvF1s6J0K1L2M3N4P5Q6" alt="Dr. V. Lalitha" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-300" onerror="this.src='/static/images/ccic_logo.jpg'">
            <div>
              <span class="text-[10px] font-headline font-bold uppercase text-secondary">Captain</span>
              <h4 class="font-headline font-bold text-sm text-slate-900">Dr. V. Lalitha</h4>
              <p class="text-xs text-slate-500">Associate Professor • SEC, CSE (AI &amp; ML)</p>
              <p class="text-[11px] text-slate-600 mt-1.5 font-medium">Agentic Systems &amp; Autonomous Intelligence</p>
            </div>
          </div>

          <!-- 3. Ms. Mathupriya -->
          <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm flex items-start gap-4">
            <img src="/static/images/mathupriya.jpg" alt="Ms. Mathupriya" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-300">
            <div>
              <span class="text-[10px] font-headline font-bold uppercase text-secondary">Organizer</span>
              <h4 class="font-headline font-bold text-sm text-slate-900">Ms. Mathupriya</h4>
              <p class="text-xs text-slate-500">Assistant Professor • SEC</p>
              <p class="text-[11px] text-slate-600 mt-1.5 font-medium">Event Coordination &amp; Student Operations</p>
            </div>
          </div>

          <!-- 4. Mrs. S. Ebenezer Roselin -->
          <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm flex items-start gap-4">
            <img src="/static/images/ebenezer.jpg" alt="Mrs. S. Ebenezer Roselin" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-300">
            <div>
              <span class="text-[10px] font-headline font-bold uppercase text-secondary">Propagator</span>
              <h4 class="font-headline font-bold text-sm text-slate-900">Mrs. S. Ebenezer Roselin</h4>
              <p class="text-xs text-slate-500">Assistant Professor • SIT, CSE (Cyber Security)</p>
              <p class="text-[11px] text-slate-600 mt-1.5 font-medium">Inter-Institutional AI &amp; Cyber Security</p>
            </div>
          </div>

          <!-- 5. Ms. M. Anitha -->
          <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm flex items-start gap-4">
            <img src="/static/images/anitha.jpg" alt="Ms. M. Anitha" class="w-16 h-16 rounded-xl object-cover shrink-0 border border-slate-300">
            <div>
              <span class="text-[10px] font-headline font-bold uppercase text-secondary">Executor</span>
              <h4 class="font-headline font-bold text-sm text-slate-900">Ms. M. Anitha</h4>
              <p class="text-xs text-slate-500">Assistant Professor • SIT, AI-DS</p>
              <p class="text-[11px] text-slate-600 mt-1.5 font-medium">Data Science &amp; Technical Execution</p>
            </div>
          </div>

          <!-- 6. Student Leads -->
          <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm flex items-start gap-4">
            <div class="w-16 h-16 rounded-xl bg-secondary-container text-white flex items-center justify-center font-bold text-xl shrink-0">
              <span class="material-symbols-outlined text-2xl">groups</span>
            </div>
            <div>
              <span class="text-[10px] font-headline font-bold uppercase text-secondary">Student Coordinators</span>
              <h4 class="font-headline font-bold text-sm text-slate-900">Hari Priyan &amp; Guru Prakash</h4>
              <p class="text-xs text-slate-500">Final Year Cohort • CSE (AIML)</p>
              <p class="text-[11px] text-slate-600 mt-1.5 font-medium">Executive Student Coordination</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: REGISTRATION APPLICATION FORM   -->
    <!-- ========================================== -->
    <section id="register" class="w-full py-16 bg-[#faf8ff] border-t border-slate-200">
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

        <div class="bg-white rounded-2xl shadow-xl border border-slate-200 p-6 sm:p-10">
          <div id="form-alert" class="hidden mb-6 p-4 rounded-xl text-xs border font-medium"></div>

          <form id="ccic-registration-form" class="space-y-8">
            <!-- Step 1: Candidate Identity -->
            <div>
              <h3 class="font-headline text-base sm:text-lg font-bold text-slate-900 border-b border-slate-200 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary">person</span>
                1. Candidate Identity
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Full Name (as in College Records) <span class="text-red-500">*</span>
                  </label>
                  <input type="text" id="name" required placeholder="e.g. Abhijit V" class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Roll Number / Register Number <span class="text-red-500">*</span>
                  </label>
                  <input type="text" id="roll_no" required placeholder="e.g. SEC25AM112" class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition font-mono uppercase bg-slate-50/50">
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Institutional Email Address <span class="text-red-500">*</span>
                  </label>
                  <input type="email" id="email" required placeholder="your.name@sairam.edu.in" class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    WhatsApp / Contact Number <span class="text-red-500">*</span>
                  </label>
                  <input type="tel" id="phone" required placeholder="+91 98765 43210" class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
              </div>
            </div>

            <!-- Step 2: Academic Affiliation -->
            <div>
              <h3 class="font-headline text-base sm:text-lg font-bold text-slate-900 border-b border-slate-200 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary">school</span>
                2. Academic Affiliation
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
                <div>
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Department <span class="text-red-500">*</span>
                  </label>
                  <select id="department" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
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
                  <select id="year" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
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
              <h3 class="font-headline text-base sm:text-lg font-bold text-slate-900 border-b border-slate-200 pb-2 flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary">memory</span>
                3. Technical Specialization &amp; Statement
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-4">
                <div class="sm:col-span-2">
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Primary Domain of Interest <span class="text-red-500">*</span>
                  </label>
                  <select id="domain" required class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
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
                  <input type="url" id="linkedin_github" placeholder="https://github.com/your-username" class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50">
                </div>
                <div class="sm:col-span-2">
                  <label class="block text-xs font-headline font-semibold text-slate-700 mb-1">
                    Motivation &amp; Research Statement
                  </label>
                  <textarea id="motivation" rows="3" placeholder="Briefly explain what projects you want to build or what excites you about CCIC..." class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-300 focus:border-secondary focus:ring-1 focus:ring-secondary outline-none transition bg-slate-50/50"></textarea>
                </div>
              </div>
            </div>

            <!-- Submit Button & Sync Notice -->
            <div class="pt-4 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
              <p class="text-[11px] text-slate-500 font-mono">
                Submissions automatically save to the CCIC Admin Board and downloadable Excel archives.
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
    <!-- SECTION 6: ADMIN BOARD & EXCEL DOWNLOAD   -->
    <!-- ========================================== -->
    <section id="admin" class="w-full py-16 bg-slate-100 border-t border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <!-- Admin Title and Export Controls -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-headline font-bold bg-amber-500 text-slate-900 uppercase tracking-wider">
                <span class="material-symbols-outlined text-[13px]">shield</span>
                Administrator Board
              </span>
              <span class="text-xs text-slate-500 font-mono">• Live Roster Engine</span>
            </div>
            <h2 class="font-headline text-2xl sm:text-3xl font-bold text-slate-900">
              Application Database &amp; Real-Time Submissions
            </h2>
            <p class="text-xs sm:text-sm text-slate-500 mt-1">
              Monitor applicant registrations, review technical specializations, and export real-time Excel spreadsheets.
            </p>
          </div>

          <!-- Download Action Buttons -->
          <div class="flex flex-wrap items-center gap-3">
            <!-- Download CSV -->
            <button onclick="downloadCSVData()" class="inline-flex items-center gap-2 px-4 py-2.5 bg-white hover:bg-slate-50 text-slate-700 text-xs font-headline font-bold rounded-lg border border-slate-300 shadow-sm transition">
              <span class="material-symbols-outlined text-emerald-600 text-[18px]">table_chart</span>
              <span>Download CSV</span>
            </button>

            <!-- Download Excel (.xlsx) -->
            <button onclick="downloadExcelData()" class="inline-flex items-center gap-2 px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg shadow-md transition">
              <span class="material-symbols-outlined text-white text-[18px]">file_download</span>
              <span>Download Excel (.xlsx)</span>
            </button>

            <!-- Refresh Button -->
            <button onclick="initSubmissionsData()" class="p-2.5 bg-white hover:bg-slate-50 text-slate-600 rounded-lg border border-slate-300 shadow-sm transition" title="Refresh records">
              <span class="material-symbols-outlined text-[18px] block">sync</span>
            </button>
          </div>
        </div>

        <!-- Metric KPI Cards -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">Total Applicants</span>
              <span class="material-symbols-outlined text-blue-600 text-[20px]">groups</span>
            </div>
            <div id="stat-total" class="font-headline text-3xl font-bold text-slate-900">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Across all departments</div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">Pending Review</span>
              <span class="material-symbols-outlined text-amber-500 text-[20px]">pending_actions</span>
            </div>
            <div id="stat-pending" class="font-headline text-3xl font-bold text-amber-600">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Awaiting coordinator review</div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">Approved Members</span>
              <span class="material-symbols-outlined text-emerald-600 text-[20px]">verified</span>
            </div>
            <div id="stat-approved" class="font-headline text-3xl font-bold text-emerald-600">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Enrolled in CCIC research labs</div>
          </div>

          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-headline font-semibold text-slate-500 uppercase tracking-wider">AI Domains</span>
              <span class="material-symbols-outlined text-purple-600 text-[20px]">hub</span>
            </div>
            <div id="stat-domains" class="font-headline text-3xl font-bold text-purple-600">-</div>
            <div class="text-[11px] text-slate-400 mt-1">Specialization categories</div>
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

        <!-- Submissions Table -->
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
                    Loading submissions from database...
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- APPLICANT DETAILS MODAL -->
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

  <!-- REGISTRATION SUCCESS MODAL -->
  <div id="success-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
    <div class="bg-white rounded-2xl p-8 max-w-md w-full text-center shadow-2xl border border-slate-200">
      <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4">
        <span class="material-symbols-outlined text-4xl">verified</span>
      </div>
      <h3 class="font-headline text-xl font-bold text-slate-900 mb-2">Application Received!</h3>
      <p class="text-xs text-slate-600 mb-6 leading-relaxed">
        Thank you for applying to the CCIC AIML Club. Your credentials have been logged into the Admin Board and Excel archive.
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

  <!-- FOOTER -->
  <footer class="w-full bg-[#07132b] text-white pt-12 pb-8 px-4 sm:px-6 border-t border-slate-800">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
      <div>
        <div class="flex items-center gap-2 mb-3">
          <img src="/static/images/ccic_logo.jpg" alt="CCIC Logo" class="w-8 h-8 rounded-full border border-white/20">
          <span class="font-headline font-bold text-base text-white">CCIC Sairam</span>
        </div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Center for Computational Intelligence and Cognition. Advancing interdisciplinary research in neuro-symbolic AI and autonomous agents.
        </p>
      </div>
      <div>
        <h4 class="font-headline text-xs font-bold uppercase tracking-wider text-slate-300 mb-3">Quick Navigation</h4>
        <ul class="space-y-2 text-xs text-slate-400">
          <li><a href="#home" class="hover:text-blue-300 transition">Home Portal</a></li>
          <li><a href="#events" class="hover:text-blue-300 transition">Activities &amp; Events</a></li>
          <li><a href="#magic-members" class="hover:text-blue-300 transition">Magic Members</a></li>
          <li><a href="#scope-members" class="hover:text-blue-300 transition">Scope Members</a></li>
          <li><a href="#register" class="hover:text-blue-300 transition">Student Registration</a></li>
          <li><a href="#admin" class="hover:text-amber-400 transition">Admin Dashboard</a></li>
        </ul>
      </div>
      <div>
        <h4 class="font-headline text-xs font-bold uppercase tracking-wider text-slate-300 mb-3">Academic Base</h4>
        <p class="text-xs text-slate-400 leading-relaxed">
          Department of Computer Science &amp; Engineering (AIML)<br>
          Sri Sairam Engineering College (Autonomous)<br>
          Sai Leo Nagar, West Tambaram<br>
          Chennai - 600 044, Tamil Nadu, India
        </p>
      </div>
      <div>
        <h4 class="font-headline text-xs font-bold uppercase tracking-wider text-slate-300 mb-3">Affiliation &amp; Export</h4>
        <p class="text-xs text-slate-400 leading-relaxed mb-3">
          Affiliated with IEEE EMBS &amp; Sri Sairam Institutions.
        </p>
        <button onclick="downloadExcelData()" class="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-headline font-bold rounded-lg transition flex items-center justify-center gap-2">
          <span class="material-symbols-outlined text-[16px]">file_download</span>
          Download Excel (.xlsx)
        </button>
      </div>
    </div>
    <div class="max-w-7xl mx-auto pt-6 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-400 font-mono text-center sm:text-left">
      <span>© 2026 Center for Computational Intelligence and Cognition (CCIC) • Sri Sairam Engineering College</span>
      <span>Autonomous Institution • NIRF Rank 157</span>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="/static/js/unified-app.js"></script>
  <script src="/static/js/smooth-scroll.js"></script>
  <script>
    // Events category filter
    document.addEventListener("DOMContentLoaded", () => {
      const filterBtns = document.querySelectorAll("#event-filters .filter-btn");
      const eventCards = document.querySelectorAll("#events-container .event-item");

      filterBtns.forEach(btn => {
        btn.addEventListener("click", () => {
          filterBtns.forEach(b => {
            b.classList.remove("bg-secondary", "text-white", "shadow-sm");
            b.classList.add("text-slate-600");
          });
          btn.classList.add("bg-secondary", "text-white", "shadow-sm");
          btn.classList.remove("text-slate-600");

          const filter = btn.getAttribute("data-filter");
          eventCards.forEach(card => {
            if (filter === "all" || card.classList.contains(filter)) {
              card.style.display = "";
            } else {
              card.style.display = "none";
            }
          });
        });
      });
    });
  </script>
</body>
</html>
'''

# Write to root index.html (for Vercel deployment)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Write to templates/index.html (for Flask dev server)
with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Proper single-page application created successfully!")
