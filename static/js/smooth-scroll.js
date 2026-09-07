// Smooth Scroll-Up and Page Transition Handler for CCIC AIML Club Portal

document.addEventListener("DOMContentLoaded", () => {
    // 1. Smoothly glide to top on fresh page load/click
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // 2. Create Floating Smooth Scroll-to-Top Button
    let topBtn = document.getElementById("scroll-to-top-btn");
    if (!topBtn) {
        topBtn = document.createElement("button");
        topBtn.id = "scroll-to-top-btn";
        topBtn.setAttribute("aria-label", "Scroll to top");
        topBtn.setAttribute("title", "Scroll smoothly to top");
        topBtn.innerHTML = '<span class="material-symbols-outlined" style="font-size: 26px;">arrow_upward</span>';
        document.body.appendChild(topBtn);

        topBtn.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }

    // Toggle button visibility based on scroll depth
    let scrollTimeout;
    window.addEventListener("scroll", () => {
        if (!scrollTimeout) {
            scrollTimeout = setTimeout(() => {
                if (window.scrollY > 240) {
                    topBtn.classList.add("visible");
                } else {
                    topBtn.classList.remove("visible");
                }
                scrollTimeout = null;
            }, 50);
        }
    }, { passive: true });

    // 3. Smooth handling for intra-page anchors (#)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href");
            if (targetId && targetId !== "#") {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault();
                    targetElement.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });
                }
            }
        });
    });

    // 4. Smooth Page Transition upon clicking navigation links
    document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute("href");
        // Only apply to internal site links (exclude external, mailto, anchor only, and file downloads)
        if (href &&
            !href.startsWith("#") &&
            !href.startsWith("http") &&
            !href.startsWith("mailto") &&
            !href.startsWith("tel") &&
            !link.hasAttribute("target") &&
            !href.includes("/export/")) {
            
            link.addEventListener("click", function (e) {
                // If it's already the current page, scroll smoothly to top
                if (window.location.pathname === href) {
                    e.preventDefault();
                    window.scrollTo({ top: 0, behavior: "smooth" });
                    return;
                }

                // Smoothly fade out before navigating
                const main = document.querySelector("main");
                if (main) {
                    main.style.transition = "opacity 0.22s ease-out, transform 0.22s ease-out";
                    main.style.opacity = "0";
                    main.style.transform = "translateY(-10px)";
                }
            });
        }
    });
});
