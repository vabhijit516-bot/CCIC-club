// Authentication Handler for CCIC AIML Club Portal
// Supports both live Firebase Authentication and Dev/Demo mode

(function () {
    let auth = null;
    let googleProvider = null;

    // Check if Firebase is loaded and configured
    function initFirebase() {
        if (window.firebase && window.CCIC_FIREBASE && window.CCIC_FIREBASE.isConfigured) {
            try {
                if (!firebase.apps.length) {
                    firebase.initializeApp(window.CCIC_FIREBASE.config);
                }
                auth = firebase.auth();
                googleProvider = new firebase.auth.GoogleAuthProvider();
                console.log("[CCIC Auth] Live Firebase initialized successfully.");
            } catch (err) {
                console.warn("[CCIC Auth] Firebase initialization warning:", err);
            }
        } else {
            console.log("[CCIC Auth] Running in Local/Dev Mode (Firebase credentials pending). Instant testing enabled!");
        }
    }

    // Helper: Determine if an email has admin privileges
    function isEmailAdmin(email) {
        if (!email) return false;
        const normalized = email.toLowerCase().trim();
        const list = (window.CCIC_FIREBASE && window.CCIC_FIREBASE.adminEmails) || [
            "admin@sairam.edu.in",
            "ccic.aiml@sairam.edu.in",
            "admin@ccic.org"
        ];
        return list.some(adminEmail => adminEmail.toLowerCase() === normalized) || normalized.includes("admin@");
    }

    // Get current stored session
    function getCurrentUser() {
        try {
            const raw = localStorage.getItem("ccic_user");
            return raw ? JSON.parse(raw) : null;
        } catch (e) {
            return null;
        }
    }

    // Save session to localStorage and sync with Flask backend
    async function saveSession(user) {
        localStorage.setItem("ccic_user", JSON.stringify(user));
        try {
            await fetch("/api/auth/session", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(user)
            });
        } catch (e) {
            console.warn("Backend session sync error:", e);
        }
    }

    // Clear session
    async function clearSession() {
        localStorage.removeItem("ccic_user");
        try {
            await fetch("/api/auth/logout", { method: "POST" });
        } catch (e) { }
    }

    // Login function
    async function loginWithEmailPassword(email, password, isAdminLogin = false) {
        const isAdminAccount = isEmailAdmin(email);

        if (isAdminLogin && !isAdminAccount) {
            throw new Error("Access Denied: This email does not have CCIC Administrator privileges.");
        }

        if (auth && window.CCIC_FIREBASE.isConfigured) {
            // Live Firebase Auth
            const userCredential = await auth.signInWithEmailAndPassword(email, password);
            const user = userCredential.user;
            const userData = {
                uid: user.uid,
                email: user.email,
                displayName: user.displayName || user.email.split("@")[0],
                role: isAdminAccount ? "admin" : "member",
                photoURL: user.photoURL || null
            };
            await saveSession(userData);
            return userData;
        } else {
            // Local Demo Mode
            await new Promise(r => setTimeout(r, 600)); // Simulate network latency
            const userData = {
                uid: "demo-" + Math.random().toString(36).substring(2, 9),
                email: email,
                displayName: email.split("@")[0].toUpperCase(),
                role: isAdminAccount ? "admin" : "member",
                photoURL: null
            };
            await saveSession(userData);
            return userData;
        }
    }

    // Sign up function
    async function signupWithEmailPassword(email, password, fullName) {
        const isAdminAccount = isEmailAdmin(email);

        if (auth && window.CCIC_FIREBASE.isConfigured) {
            const userCredential = await auth.createUserWithEmailAndPassword(email, password);
            const user = userCredential.user;
            if (fullName) {
                await user.updateProfile({ displayName: fullName });
            }
            const userData = {
                uid: user.uid,
                email: user.email,
                displayName: fullName || user.email.split("@")[0],
                role: isAdminAccount ? "admin" : "member",
                photoURL: null
            };
            await saveSession(userData);
            return userData;
        } else {
            // Local Demo Mode
            await new Promise(r => setTimeout(r, 600));
            const userData = {
                uid: "demo-" + Math.random().toString(36).substring(2, 9),
                email: email,
                displayName: fullName || email.split("@")[0],
                role: isAdminAccount ? "admin" : "member",
                photoURL: null
            };
            await saveSession(userData);
            return userData;
        }
    }

    // Google Sign-In
    async function loginWithGoogle() {
        if (auth && googleProvider && window.CCIC_FIREBASE.isConfigured) {
            const result = await auth.signInWithPopup(googleProvider);
            const user = result.user;
            const isAdminAccount = isEmailAdmin(user.email);
            const userData = {
                uid: user.uid,
                email: user.email,
                displayName: user.displayName || user.email.split("@")[0],
                role: isAdminAccount ? "admin" : "member",
                photoURL: user.photoURL
            };
            await saveSession(userData);
            return userData;
        } else {
            // Demo fallback for Google login
            const demoEmail = "sairam.student@sairam.edu.in";
            const userData = {
                uid: "demo-google-" + Date.now(),
                email: demoEmail,
                displayName: "Sairam AIML Scholar",
                role: "member",
                photoURL: null
            };
            await saveSession(userData);
            return userData;
        }
    }

    // Logout
    async function logout() {
        if (auth && window.CCIC_FIREBASE.isConfigured) {
            try { await auth.signOut(); } catch (e) { }
        }
        await clearSession();
        window.location.href = "/";
    }

    // Update Navigation Bars across all pages
    function updateNavbarAuth() {
        const user = getCurrentUser();
        const navAuthContainers = document.querySelectorAll(".ccic-nav-auth");

        navAuthContainers.forEach(container => {
            if (user) {
                const isAdmin = user.role === "admin";
                container.innerHTML = `
                    <div class="flex items-center gap-3">
                        ${isAdmin ? `
                            <a href="/admin" class="flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-secondary text-white text-xs font-semibold tracking-wide hover:bg-opacity-90 transition shadow-sm">
                                <span class="material-symbols-outlined text-[16px]">admin_panel_settings</span>
                                Admin Portal
                            </a>
                        ` : `
                            <span class="hidden md:inline-block text-xs font-semibold text-slate-700 bg-surface-container px-2.5 py-1 rounded-full border border-outline-variant/30">
                                <span class="text-secondary font-bold">●</span> ${user.displayName || user.email}
                            </span>
                        `}
                        <button onclick="CCIC_AUTH.logout()" class="px-3 py-1.5 text-xs font-semibold text-red-600 hover:text-red-700 hover:bg-red-50 rounded-md border border-red-200 transition">
                            Sign Out
                        </button>
                    </div>
                `;
            } else {
                container.innerHTML = `
                    <div class="flex items-center gap-2">
                        <a href="/login" class="px-3 py-1.5 text-xs font-semibold text-on-surface hover:text-secondary rounded-md border border-outline-variant/40 transition">
                            Sign In
                        </a>
                        <a href="/register" class="px-3 py-1.5 text-xs font-semibold text-white bg-secondary hover:bg-opacity-90 rounded-md transition shadow-sm">
                            Join Club
                        </a>
                    </div>
                `;
            }
        });
    }

    // Expose Global API
    window.CCIC_AUTH = {
        init: initFirebase,
        login: loginWithEmailPassword,
        signup: signupWithEmailPassword,
        loginWithGoogle: loginWithGoogle,
        logout: logout,
        getUser: getCurrentUser,
        isAdmin: isEmailAdmin,
        updateNavbarAuth: updateNavbarAuth
    };

    // Auto initialize on DOM ready
    document.addEventListener("DOMContentLoaded", () => {
        initFirebase();
        updateNavbarAuth();
    });
})();
