// Unified Application Controller for CCIC AIML Club Portal (Vercel & Local Ready)

// Seed default applicants if localStorage is empty
const DEFAULT_SUBMISSIONS = [
  {
    id: 1,
    name: "Aravind Swaminathan",
    roll_no: "21AM012",
    email: "aravind.s@sairam.edu.in",
    phone: "+91 98401 23456",
    department: "CSE (AI & ML)",
    year: "3rd Year",
    domain: "Computer Vision & Generative AI",
    linkedin_github: "https://github.com/aravind-ai",
    motivation: "Passionate about building state-of-the-art vision models for healthcare diagnosis.",
    status: "Approved",
    created_at: "2026-09-01 10:15:00"
  },
  {
    id: 2,
    name: "Divya Krishnan",
    roll_no: "22AM045",
    email: "divya.k@sairam.edu.in",
    phone: "+91 97102 34567",
    department: "CSE (AI & ML)",
    year: "2nd Year",
    domain: "Natural Language Processing",
    linkedin_github: "https://linkedin.com/in/divyakrishnan",
    motivation: "Eager to contribute to CCIC NLP research labs and open-source LLM agents.",
    status: "Pending",
    created_at: "2026-09-02 11:30:00"
  },
  {
    id: 3,
    name: "Karthik Raja",
    roll_no: "21CS089",
    email: "karthik.r@sairam.edu.in",
    phone: "+91 94440 98765",
    department: "Computer Science",
    year: "3rd Year",
    domain: "Deep Reinforcement Learning & Robotics",
    linkedin_github: "https://github.com/karthik-robolab",
    motivation: "Building autonomous robotics algorithms and edge AI controllers.",
    status: "Approved",
    created_at: "2026-09-03 14:45:00"
  },
  {
    id: 4,
    name: "Sneha Ramesh",
    roll_no: "23AM078",
    email: "sneha.r@sairam.edu.in",
    phone: "+91 98841 54321",
    department: "CSE (AI & ML)",
    year: "1st Year",
    domain: "Machine Learning & Data Science",
    linkedin_github: "https://github.com/sneha-codes",
    motivation: "Enthusiastic beginner in ML eager to learn and participate in national hackathons.",
    status: "Reviewed",
    created_at: "2026-09-04 16:20:00"
  },
  {
    id: 5,
    name: "Rahul Varman",
    roll_no: "22IT033",
    email: "rahul.v@sairam.edu.in",
    phone: "+91 98412 67890",
    department: "Information Technology",
    year: "2nd Year",
    domain: "Edge AI & IoT Systems",
    linkedin_github: "https://linkedin.com/in/rahulvarman",
    motivation: "Developing low-latency TinyML applications for industrial edge sensors.",
    status: "Pending",
    created_at: "2026-09-05 09:10:00"
  },
  {
    id: 6,
    name: "Rithanya Shree",
    roll_no: "22AM105",
    email: "rithanya.s@sairam.edu.in",
    phone: "+91 99401 88776",
    department: "CSE (AI & ML)",
    year: "2nd Year",
    domain: "Computer Vision & Generative AI",
    linkedin_github: "https://github.com/rithanya-vision",
    motivation: "Excited to train generative diffusion models in CCIC!",
    status: "Pending",
    created_at: "2026-09-07 17:23:23"
  }
];

// Storage helpers
function getLocalSubmissions() {
  try {
    const raw = localStorage.getItem("ccic_submissions");
    if (!raw) {
      localStorage.setItem("ccic_submissions", JSON.stringify(DEFAULT_SUBMISSIONS));
      return DEFAULT_SUBMISSIONS;
    }
    return JSON.parse(raw);
  } catch (e) {
    return DEFAULT_SUBMISSIONS;
  }
}

function saveLocalSubmissions(subs) {
  try {
    localStorage.setItem("ccic_submissions", JSON.stringify(subs));
  } catch (e) {
    console.warn("LocalStorage save failed:", e);
  }
}

let activeSubmissions = [];

// Initialize application on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  initNavigation();
  initSubmissionsData();
  initRegistrationForm();
  initAdminFilters();
  handleUrlDeepLink();
});

// Deep linking to sections based on hash or path
function handleUrlDeepLink() {
  const hash = window.location.hash;
  if (hash) {
    const target = document.querySelector(hash);
    if (target) {
      setTimeout(() => {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 200);
    }
  } else {
    // If URL pathname is /events, /register, /admin, scroll there
    const path = window.location.pathname.replace(/^\/+|\/+$/g, '');
    if (path) {
      const target = document.getElementById(path);
      if (target) {
        setTimeout(() => {
          target.scrollIntoView({ behavior: "smooth", block: "start" });
        }, 200);
      }
    }
  }
}

// Navigation bar highlighting and mobile menu
function initNavigation() {
  const mobileBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener("click", () => {
      mobileMenu.classList.toggle("hidden");
    });
    // Close on link click
    mobileMenu.querySelectorAll("a").forEach(a => {
      a.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
      });
    });
  }

  // Smooth scroll links with active pill updates
  const navLinks = document.querySelectorAll('nav a[href^="#"], #mobile-menu a[href^="#"]');
  navLinks.forEach(link => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (href && href.startsWith("#")) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: "smooth", block: "start" });
          history.pushState(null, null, href);
        }
      }
    });
  });

  // IntersectionObserver to highlight current active nav item
  const sections = document.querySelectorAll("section[id]");
  window.addEventListener("scroll", () => {
    let currentId = "";
    const scrollPos = window.scrollY + 120;
    sections.forEach(sec => {
      if (sec.offsetTop <= scrollPos) {
        currentId = sec.getAttribute("id");
      }
    });

    if (currentId) {
      document.querySelectorAll("nav a").forEach(a => {
        const href = a.getAttribute("href");
        if (href === "#" + currentId) {
          a.classList.add("bg-secondary-container", "text-on-secondary", "font-bold");
          a.classList.remove("text-on-surface-variant");
        } else if (href && href.startsWith("#")) {
          a.classList.remove("bg-secondary-container", "text-on-secondary", "font-bold");
          a.classList.add("text-on-surface-variant");
        }
      });
    }
  });
}

// Load Submissions (tries backend first, then merges with localStorage)
async function initSubmissionsData() {
  let loadedFromBackend = false;
  try {
    const res = await fetch("/api/admin/submissions");
    if (res.ok) {
      const data = await res.json();
      if (data.success && Array.isArray(data.submissions) && data.submissions.length > 0) {
        activeSubmissions = data.submissions;
        loadedFromBackend = true;
        // Also save to localStorage as backup
        saveLocalSubmissions(activeSubmissions);
      }
    }
  } catch (e) {
    // Static mode / Vercel without backend
  }

  if (!loadedFromBackend) {
    activeSubmissions = getLocalSubmissions();
  }

  renderAdminBoard();
}

// Render Admin Board table and KPI statistics
function renderAdminBoard() {
  renderAdminStats();
  filterAndRenderSubmissions();
}

function renderAdminStats() {
  const totalEl = document.getElementById("stat-total");
  const pendingEl = document.getElementById("stat-pending");
  const approvedEl = document.getElementById("stat-approved");
  const domainsEl = document.getElementById("stat-domains");

  const total = activeSubmissions.length;
  const pending = activeSubmissions.filter(s => s.status === "Pending").length;
  const approved = activeSubmissions.filter(s => s.status === "Approved").length;
  const uniqueDomains = new Set(activeSubmissions.map(s => s.domain)).size;

  if (totalEl) totalEl.textContent = total;
  if (pendingEl) pendingEl.textContent = pending;
  if (approvedEl) approvedEl.textContent = approved;
  if (domainsEl) domainsEl.textContent = uniqueDomains;
}

function initAdminFilters() {
  const searchInput = document.getElementById("search-input");
  const domainFilter = document.getElementById("filter-domain");
  const statusFilter = document.getElementById("filter-status");

  if (searchInput) searchInput.addEventListener("input", filterAndRenderSubmissions);
  if (domainFilter) domainFilter.addEventListener("change", filterAndRenderSubmissions);
  if (statusFilter) statusFilter.addEventListener("change", filterAndRenderSubmissions);
}

function filterAndRenderSubmissions() {
  const search = (document.getElementById("search-input")?.value || "").toLowerCase().trim();
  const domain = document.getElementById("filter-domain")?.value || "All";
  const status = document.getElementById("filter-status")?.value || "All";

  const filtered = activeSubmissions.filter(item => {
    const matchesSearch = !search ||
      (item.name && item.name.toLowerCase().includes(search)) ||
      (item.roll_no && item.roll_no.toLowerCase().includes(search)) ||
      (item.email && item.email.toLowerCase().includes(search)) ||
      (item.department && item.department.toLowerCase().includes(search));

    const matchesDomain = (domain === "All") || (item.domain === domain);
    const matchesStatus = (status === "All") || (item.status === status);

    return matchesSearch && matchesDomain && matchesStatus;
  });

  const tbody = document.getElementById("submissions-tbody");
  const countEl = document.getElementById("results-count");
  if (countEl) countEl.textContent = `${filtered.length} applicant${filtered.length === 1 ? '' : 's'} found`;

  if (!tbody) return;

  if (filtered.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="8" class="text-center py-12 text-slate-500 font-medium">
          <span class="material-symbols-outlined text-4xl text-slate-400 block mb-2">folder_off</span>
          No registration records match your filter criteria.
        </td>
      </tr>
    `;
    return;
  }

  tbody.innerHTML = filtered.map((sub, index) => {
    let badgeClass = "bg-amber-100 text-amber-800 border-amber-200";
    if (sub.status === "Approved") badgeClass = "bg-emerald-100 text-emerald-800 border-emerald-200";
    if (sub.status === "Reviewed") badgeClass = "bg-blue-100 text-blue-800 border-blue-200";
    if (sub.status === "Rejected") badgeClass = "bg-rose-100 text-rose-800 border-rose-200";

    const displayId = sub.id || (index + 1);

    return `
      <tr class="hover:bg-slate-50/80 transition-colors border-b border-slate-100 text-xs text-slate-700">
        <td class="px-4 py-3.5 font-mono font-semibold text-slate-500">#${displayId}</td>
        <td class="px-4 py-3.5">
          <div class="font-headline font-bold text-slate-900">${escapeHtml(sub.name)}</div>
          <div class="text-[11px] text-slate-500 flex items-center gap-1 mt-0.5">
            <span class="material-symbols-outlined text-[13px] text-slate-400">mail</span>
            <a href="mailto:${escapeHtml(sub.email)}" class="hover:underline hover:text-secondary">${escapeHtml(sub.email)}</a>
          </div>
          <div class="text-[10px] text-slate-400 flex items-center gap-1">
            <span class="material-symbols-outlined text-[12px]">phone</span>
            ${escapeHtml(sub.phone || "—")}
          </div>
        </td>
        <td class="px-4 py-3.5 font-mono font-bold text-slate-800">
          <span class="px-2 py-0.5 bg-slate-100 rounded border border-slate-200">${escapeHtml(sub.roll_no)}</span>
        </td>
        <td class="px-4 py-3.5">
          <div class="font-medium text-slate-800">${escapeHtml(sub.department)}</div>
          <div class="text-[11px] text-slate-500 font-mono">${escapeHtml(sub.year)}</div>
        </td>
        <td class="px-4 py-3.5">
          <span class="inline-block px-2.5 py-1 rounded-md bg-blue-50 text-blue-700 text-[11px] font-medium border border-blue-100/80">
            ${escapeHtml(sub.domain)}
          </span>
        </td>
        <td class="px-4 py-3.5 text-slate-500 text-[11px] font-mono whitespace-nowrap">
          ${(sub.created_at || "Recent").substring(0, 16)}
        </td>
        <td class="px-4 py-3.5">
          <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-headline font-bold border ${badgeClass}">
            ${escapeHtml(sub.status || "Pending")}
          </span>
        </td>
        <td class="px-4 py-3.5 text-right whitespace-nowrap">
          <div class="flex items-center justify-end gap-1.5">
            <button onclick="viewApplicantDetails('${escapeHtml(String(displayId))}')" class="p-1.5 text-slate-500 hover:text-secondary hover:bg-blue-50 rounded transition" title="View Application Statement">
              <span class="material-symbols-outlined text-[16px]">visibility</span>
            </button>
            <button onclick="updateStatus('${escapeHtml(String(displayId))}', 'Approved')" class="px-2 py-1 bg-emerald-50 text-emerald-700 hover:bg-emerald-600 hover:text-white rounded border border-emerald-200 text-[11px] font-semibold transition" title="Approve applicant">
              Approve
            </button>
            <button onclick="updateStatus('${escapeHtml(String(displayId))}', 'Reviewed')" class="px-2 py-1 bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white rounded border border-blue-200 text-[11px] font-semibold transition" title="Mark as reviewed">
              Review
            </button>
          </div>
        </td>
      </tr>
    `;
  }).join("");
}

// Update submission status
async function updateStatus(idStr, newStatus) {
  const item = activeSubmissions.find(s => String(s.id) === String(idStr));
  if (item) {
    item.status = newStatus;
    saveLocalSubmissions(activeSubmissions);
    renderAdminBoard();

    // Try backend sync if available
    try {
      await fetch("/api/admin/update-status", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: item.id, status: newStatus })
      });
    } catch (e) {}
  }
}

// View candidate details modal
function viewApplicantDetails(idStr) {
  const item = activeSubmissions.find(s => String(s.id) === String(idStr));
  if (!item) return;

  const modal = document.getElementById("details-modal");
  const content = document.getElementById("details-modal-content");
  if (!modal || !content) return;

  content.innerHTML = `
    <div class="flex items-center gap-3 border-b border-slate-200 pb-3 mb-4">
      <div class="w-10 h-10 rounded-full bg-secondary-container text-white flex items-center justify-center font-bold text-lg">
        ${(item.name || "A")[0].toUpperCase()}
      </div>
      <div>
        <h3 class="font-headline text-lg font-bold text-slate-900">${escapeHtml(item.name)}</h3>
        <p class="text-xs text-slate-500 font-mono">${escapeHtml(item.roll_no)} • ${escapeHtml(item.department)} (${escapeHtml(item.year)})</p>
      </div>
    </div>
    
    <div class="space-y-3 text-xs text-slate-700">
      <div>
        <span class="font-headline font-bold text-slate-900 block text-[11px] uppercase tracking-wider mb-0.5">Target AI Domain:</span>
        <span class="px-2.5 py-1 rounded bg-blue-50 text-secondary font-medium inline-block">${escapeHtml(item.domain)}</span>
      </div>

      <div>
        <span class="font-headline font-bold text-slate-900 block text-[11px] uppercase tracking-wider mb-0.5">Portfolio / GitHub / Profile:</span>
        ${item.linkedin_github ? `<a href="${escapeHtml(item.linkedin_github)}" target="_blank" class="text-secondary hover:underline break-all font-mono">${escapeHtml(item.linkedin_github)}</a>` : '<span class="text-slate-400">Not provided</span>'}
      </div>

      <div>
        <span class="font-headline font-bold text-slate-900 block text-[11px] uppercase tracking-wider mb-0.5">Motivation & Research Statement:</span>
        <p class="p-3 bg-slate-50 rounded-lg border border-slate-200/80 leading-relaxed text-slate-800 whitespace-pre-wrap">
          ${escapeHtml(item.motivation || "No statement provided.")}
        </p>
      </div>

      <div class="pt-2 flex items-center justify-between text-[11px] text-slate-500">
        <span>Contact: <strong>${escapeHtml(item.email)}</strong> | <strong>${escapeHtml(item.phone)}</strong></span>
        <span>Status: <strong class="text-secondary">${escapeHtml(item.status || "Pending")}</strong></span>
      </div>
    </div>
  `;

  modal.classList.remove("hidden");
}

function closeDetailsModal() {
  const modal = document.getElementById("details-modal");
  if (modal) modal.classList.add("hidden");
}

// Registration Form Handler
function initRegistrationForm() {
  const form = document.getElementById("ccic-registration-form");
  if (!form) return;

  const alertBox = document.getElementById("form-alert");
  const submitBtn = document.getElementById("submit-btn");
  const btnSpinner = document.getElementById("btn-spinner");
  const btnText = document.getElementById("btn-text");

  function showAlert(message, type = "error") {
    if (!alertBox) return;
    alertBox.classList.remove("hidden", "bg-red-50", "text-red-700", "border-red-200", "bg-green-50", "text-green-700", "border-green-200");
    if (type === "success") {
      alertBox.classList.add("bg-green-50", "text-green-700", "border-green-200");
      alertBox.innerHTML = `
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-green-600">check_circle</span>
          <span>${message}</span>
        </div>
      `;
    } else {
      alertBox.classList.add("bg-red-50", "text-red-700", "border-red-200");
      alertBox.innerHTML = `
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-red-600">error</span>
          <span>${message}</span>
        </div>
      `;
    }
    alertBox.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
      name: document.getElementById("name").value.trim(),
      roll_no: document.getElementById("roll_no").value.trim().toUpperCase(),
      email: document.getElementById("email").value.trim(),
      phone: document.getElementById("phone").value.trim(),
      department: document.getElementById("department").value,
      year: document.getElementById("year").value,
      domain: document.getElementById("domain").value,
      linkedin_github: document.getElementById("linkedin_github").value.trim(),
      motivation: document.getElementById("motivation").value.trim()
    };

    if (!formData.name || !formData.roll_no || !formData.email || !formData.phone || !formData.department || !formData.year || !formData.domain) {
      showAlert("Please fill in all mandatory fields denoted with an asterisk (*).");
      return;
    }

    if (submitBtn) submitBtn.disabled = true;
    if (btnSpinner) btnSpinner.classList.remove("hidden");
    if (btnText) btnText.textContent = "Processing Application...";

    const newEntry = {
      id: Date.now(),
      ...formData,
      status: "Pending",
      created_at: new Date().toISOString().replace('T', ' ').substring(0, 19)
    };

    // Save to active submissions and localStorage immediately
    activeSubmissions.unshift(newEntry);
    saveLocalSubmissions(activeSubmissions);
    renderAdminBoard();

    // Try posting to backend API as well
    try {
      await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });
    } catch (e) {
      // Backend unavailable on static Vercel, client storage is active
    }

    form.reset();
    showAlert("Application submitted successfully! Your record has been logged in the Admin Board and Excel archive.", "success");

    // Open Success Modal
    const modal = document.getElementById("success-modal");
    if (modal) {
      setTimeout(() => {
        modal.classList.remove("hidden");
      }, 500);
    }

    if (submitBtn) submitBtn.disabled = false;
    if (btnSpinner) btnSpinner.classList.add("hidden");
    if (btnText) btnText.textContent = "Submit Application";
  });
}

// Download Excel (.xlsx) using SheetJS (works 100% on Vercel without server!)
function downloadExcelData() {
  const exportData = activeSubmissions.map((item, idx) => ({
    "Application ID": item.id || (idx + 1),
    "Full Name": item.name,
    "Roll Number": item.roll_no,
    "Email Address": item.email,
    "Phone Number": item.phone,
    "Department": item.department,
    "Year of Study": item.year,
    "Domain of Interest": item.domain,
    "Portfolio / GitHub / LinkedIn": item.linkedin_github || "",
    "Motivation / Statement": item.motivation || "",
    "Application Status": item.status || "Pending",
    "Submission Date & Time": item.created_at || new Date().toLocaleString()
  }));

  if (typeof XLSX !== "undefined") {
    const worksheet = XLSX.utils.json_to_sheet(exportData);
    // Format column widths
    worksheet["!cols"] = [
      { wch: 15 }, // ID
      { wch: 24 }, // Name
      { wch: 14 }, // Roll No
      { wch: 28 }, // Email
      { wch: 16 }, // Phone
      { wch: 26 }, // Department
      { wch: 12 }, // Year
      { wch: 32 }, // Domain
      { wch: 35 }, // Portfolio
      { wch: 45 }, // Motivation
      { wch: 16 }, // Status
      { wch: 22 }  // Date
    ];

    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "CCIC Submissions");
    XLSX.writeFile(workbook, "CCIC_AIML_Submissions.xlsx");
  } else {
    // Fallback: Direct server endpoint
    window.location.href = "/api/admin/export/excel";
  }
}

// Download CSV format
function downloadCSVData() {
  const headers = [
    "Application ID",
    "Full Name",
    "Roll Number",
    "Email Address",
    "Phone Number",
    "Department",
    "Year of Study",
    "Domain of Interest",
    "Portfolio / GitHub / LinkedIn",
    "Motivation / Statement",
    "Application Status",
    "Submission Date & Time"
  ];

  const rows = activeSubmissions.map((item, idx) => [
    item.id || (idx + 1),
    `"${(item.name || '').replace(/"/g, '""')}"`,
    `"${(item.roll_no || '').replace(/"/g, '""')}"`,
    `"${(item.email || '').replace(/"/g, '""')}"`,
    `"${(item.phone || '').replace(/"/g, '""')}"`,
    `"${(item.department || '').replace(/"/g, '""')}"`,
    `"${(item.year || '').replace(/"/g, '""')}"`,
    `"${(item.domain || '').replace(/"/g, '""')}"`,
    `"${(item.linkedin_github || '').replace(/"/g, '""')}"`,
    `"${(item.motivation || '').replace(/"/g, '""')}"`,
    `"${(item.status || 'Pending').replace(/"/g, '""')}"`,
    `"${(item.created_at || '').replace(/"/g, '""')}"`
  ]);

  const csvString = "\uFEFF" + [headers.join(","), ...rows.map(r => r.join(","))].join("\r\n");
  const blob = new Blob([csvString], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", "CCIC_AIML_Submissions.csv");
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

// Utility: escape HTML to prevent XSS
function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
