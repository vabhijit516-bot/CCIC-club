// Form Submission Handler for CCIC AIML Club Portal
document.addEventListener("DOMContentLoaded", () => {
    const regForm = document.getElementById("ccic-registration-form");
    if (!regForm) return;

    const alertBox = document.getElementById("form-alert");
    const submitBtn = document.getElementById("submit-btn");
    const btnText = document.getElementById("btn-text");
    const btnSpinner = document.getElementById("btn-spinner");

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

    regForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Collect fields
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

        // Basic validation
        if (!formData.name || !formData.roll_no || !formData.email || !formData.phone || !formData.department || !formData.year || !formData.domain) {
            showAlert("Please fill in all required fields.");
            return;
        }

        // Set Loading State
        if (submitBtn) submitBtn.disabled = true;
        if (btnSpinner) btnSpinner.classList.remove("hidden");
        if (btnText) btnText.textContent = "Submitting Application...";

        try {
            const response = await fetch("/api/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok && result.success) {
                showAlert(result.message || "Application submitted successfully! Our coordinators will review your submission.", "success");
                regForm.reset();
                setTimeout(() => {
                    const modal = document.getElementById("success-modal");
                    if (modal) modal.classList.remove("hidden");
                }, 800);
            } else {
                showAlert(result.error || "Failed to submit application. Please check your inputs.");
            }
        } catch (err) {
            showAlert("Network error occurred while submitting. Please verify your connection.");
            console.error("Submission error:", err);
        } finally {
            if (submitBtn) submitBtn.disabled = false;
            if (btnSpinner) btnSpinner.classList.add("hidden");
            if (btnText) btnText.textContent = "Submit Application";
        }
    });
});
