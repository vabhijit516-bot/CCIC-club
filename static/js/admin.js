// Admin Dashboard Handler for CCIC AIML Club Portal

let allSubmissions = [];

document.addEventListener("DOMContentLoaded", () => {
    // Check client-side authentication
    const user = window.CCIC_AUTH ? window.CCIC_AUTH.getUser() : null;
    
    // If not logged in or not admin, check with backend or redirect
    if (!user || user.role !== "admin") {
        console.warn("Unauthenticated admin access detected.");
    }

    loadDashboard();

    // Event listeners
    const searchInput = document.getElementById("search-input");
    const domainSelect = document.getElementById("filter-domain");
    const statusSelect = document.getElementById("filter-status");

    if (searchInput) searchInput.addEventListener("input", filterAndRenderSubmissions);
    if (domainSelect) domainSelect.addEventListener("change", filterAndRenderSubmissions);
    if (statusSelect) statusSelect.addEventListener("change", filterAndRenderSubmissions);
});

async function loadDashboard() {
    try {
        const [subsRes, statsRes] = await Promise.all([
            fetch("/api/admin/submissions"),
            fetch("/api/stats")
        ]);

        if (subsRes.status === 401 || subsRes.status === 403) {
            window.location.href = "/login?redirect=admin&error=unauthorized";
            return;
        }

        const subsData = await subsRes.json();
        const statsData = await statsRes.json();

        if (subsData.success) {
            allSubmissions = subsData.submissions;
            renderStats(statsData);
            filterAndRenderSubmissions();
        }
    } catch (err) {
        console.error("Dashboard loading failed:", err);
    }
}

function renderStats(stats) {
    if (!stats) return;

    const totalEl = document.getElementById("stat-total");
    const pendingEl = document.getElementById("stat-pending");
    const approvedEl = document.getElementById("stat-approved");
    const domainsEl = document.getElementById("stat-domains");

    if (totalEl) totalEl.textContent = stats.total || 0;
    if (pendingEl) pendingEl.textContent = (stats.status && stats.status.Pending) || 0;
    if (approvedEl) approvedEl.textContent = (stats.status && stats.status.Approved) || 0;
    if (domainsEl) domainsEl.textContent = Object.keys(stats.domains || {}).length;
}

function filterAndRenderSubmissions() {
    const search = (document.getElementById("search-input")?.value || "").toLowerCase().trim();
    const domainFilter = document.getElementById("filter-domain")?.value || "All";
    const statusFilter = document.getElementById("filter-status")?.value || "All";

    const filtered = allSubmissions.filter(item => {
        const matchesSearch = !search ||
            (item.name && item.name.toLowerCase().includes(search)) ||
            (item.roll_no && item.roll_no.toLowerCase().includes(search)) ||
            (item.email && item.email.toLowerCase().includes(search)) ||
            (item.department && item.department.toLowerCase().includes(search));

        const matchesDomain = domainFilter === "All" || item.domain === domainFilter;
        const matchesStatus = statusFilter === "All" || item.status === statusFilter;

        return matchesSearch && matchesDomain && matchesStatus;
    });

    renderTable(filtered);
}

function renderTable(submissions) {
    const tbody = document.getElementById("submissions-tbody");
    const countEl = document.getElementById("results-count");
    if (!tbody) return;

    if (countEl) countEl.textContent = `${submissions.length} applicants found`;

    if (submissions.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="8" class="text-center py-10 text-slate-500 font-medium">
                    <span class="material-symbols-outlined text-4xl text-slate-400 block mb-2">folder_off</span>
                    No registration records match your filter criteria.
                </td>
            </tr>
        `;
        return;
    }

    tbody.innerHTML = submissions.map(item => {
        let statusBadge = "";
        if (item.status === "Approved") {
            statusBadge = `<span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-300">Approved</span>`;
        } else if (item.status === "Reviewed") {
            statusBadge = `<span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 border border-amber-300">Reviewed</span>`;
        } else {
            statusBadge = `<span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-blue-100 text-blue-800 border border-blue-300">Pending</span>`;
        }

        return `
            <tr class="hover:bg-slate-50/80 transition border-b border-outline-variant/30 text-sm">
                <td class="px-4 py-3.5 font-bold text-slate-900">#${item.id}</td>
                <td class="px-4 py-3.5">
                    <div class="font-bold text-slate-900">${escapeHtml(item.name)}</div>
                    <div class="text-xs text-slate-500">${escapeHtml(item.email)}</div>
                </td>
                <td class="px-4 py-3.5 font-mono text-xs font-semibold text-slate-700">${escapeHtml(item.roll_no)}</td>
                <td class="px-4 py-3.5">
                    <div class="text-xs font-medium text-slate-900">${escapeHtml(item.department)}</div>
                    <div class="text-[11px] text-slate-500">${escapeHtml(item.year)}</div>
                </td>
                <td class="px-4 py-3.5">
                    <span class="inline-block px-2 py-0.5 rounded text-xs font-medium bg-slate-100 text-slate-800 border border-slate-200">
                        ${escapeHtml(item.domain)}
                    </span>
                </td>
                <td class="px-4 py-3.5 text-xs text-slate-500">${item.created_at ? item.created_at.substring(0, 16) : "-"}</td>
                <td class="px-4 py-3.5">${statusBadge}</td>
                <td class="px-4 py-3.5 text-right">
                    <div class="flex items-center justify-end gap-1.5">
                        <button onclick="viewApplicantDetails(${item.id})" class="p-1.5 text-slate-600 hover:text-secondary rounded hover:bg-slate-100 transition" title="View Details">
                            <span class="material-symbols-outlined text-[18px]">visibility</span>
                        </button>
                        <select onchange="updateStatus(${item.id}, this.value)" class="text-xs py-1 px-1.5 rounded border border-outline-variant/40 bg-white font-medium">
                            <option value="Pending" ${item.status === "Pending" ? "selected" : ""}>Pending</option>
                            <option value="Reviewed" ${item.status === "Reviewed" ? "selected" : ""}>Reviewed</option>
                            <option value="Approved" ${item.status === "Approved" ? "selected" : ""}>Approve</option>
                        </select>
                    </div>
                </td>
            </tr>
        `;
    }).join("");
}

async function updateStatus(id, newStatus) {
    try {
        const res = await fetch("/api/admin/update-status", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id, status: newStatus })
        });
        const result = await res.json();
        if (result.success) {
            const item = allSubmissions.find(s => s.id === id);
            if (item) item.status = newStatus;
            filterAndRenderSubmissions();
        } else {
            alert(result.error || "Failed to update status.");
        }
    } catch (e) {
        console.error("Status update error:", e);
    }
}

function viewApplicantDetails(id) {
    const item = allSubmissions.find(s => s.id === id);
    if (!item) return;

    const modal = document.getElementById("details-modal");
    const content = document.getElementById("details-modal-content");
    if (!modal || !content) return;

    content.innerHTML = `
        <div class="space-y-4">
            <div class="flex justify-between items-start border-b pb-3">
                <div>
                    <h3 class="text-lg font-bold text-slate-900">${escapeHtml(item.name)}</h3>
                    <p class="text-xs text-slate-500 font-mono">${escapeHtml(item.roll_no)} • ${escapeHtml(item.department)} (${escapeHtml(item.year)})</p>
                </div>
                <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-800">${escapeHtml(item.status)}</span>
            </div>
            
            <div class="grid grid-cols-2 gap-3 text-xs">
                <div>
                    <span class="text-slate-500 block">Email Address:</span>
                    <a href="mailto:${escapeHtml(item.email)}" class="font-semibold text-secondary hover:underline">${escapeHtml(item.email)}</a>
                </div>
                <div>
                    <span class="text-slate-500 block">Contact Phone:</span>
                    <span class="font-semibold text-slate-800">${escapeHtml(item.phone)}</span>
                </div>
                <div>
                    <span class="text-slate-500 block">Primary AI Domain:</span>
                    <span class="font-semibold text-slate-800">${escapeHtml(item.domain)}</span>
                </div>
                <div>
                    <span class="text-slate-500 block">Portfolio / GitHub:</span>
                    <a href="${escapeHtml(item.linkedin_github)}" target="_blank" class="font-semibold text-secondary hover:underline truncate block">
                        ${escapeHtml(item.linkedin_github || "None provided")}
                    </a>
                </div>
            </div>

            <div>
                <span class="text-xs text-slate-500 block mb-1">Statement of Purpose / Motivation:</span>
                <div class="bg-surface-container/50 p-3 rounded text-xs text-slate-800 leading-relaxed border border-outline-variant/30">
                    ${escapeHtml(item.motivation || "No statement provided.")}
                </div>
            </div>
        </div>
    `;

    modal.classList.remove("hidden");
}

function closeDetailsModal() {
    const modal = document.getElementById("details-modal");
    if (modal) modal.classList.add("hidden");
}

function escapeHtml(text) {
    if (!text) return "";
    return String(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
