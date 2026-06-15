/* ================================================
   AARGEE — HERO INTERACTIONS
   Counters • Nav scroll • Mobile menu
   ================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ================================================
    // 1. NAVBAR — Stick on scroll (after top bar leaves)
    // ================================================
    const navbar = document.getElementById('navbar');
    const topBar = document.getElementById('top-bar');

    if (navbar && topBar) {
        const topBarHeight = topBar.offsetHeight;
        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    if (window.scrollY >= topBarHeight) {
                        navbar.classList.add('fixed');
                    } else {
                        navbar.classList.remove('fixed');
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // ================================================
    // 2. MOBILE TOGGLE
    // ================================================
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('open');
            document.body.style.overflow = navMenu.classList.contains('open') ? 'hidden' : '';
        });

        navMenu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('open');
                document.body.style.overflow = '';
            });
        });
    }

    // ================================================
    // 3. COUNTER ANIMATION
    // ================================================
    const counters = document.querySelectorAll('.stat-number[data-count]');

    const animateCounter = (el) => {
        const target = parseInt(el.dataset.count, 10);
        const duration = 2000;
        const start = performance.now();

        const tick = (now) => {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 4);
            el.textContent = Math.round(target * eased);
            if (progress < 1) requestAnimationFrame(tick);
        };

        requestAnimationFrame(tick);
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(el => counterObserver.observe(el));

    // ================================================
    // 4. SUBTLE PARALLAX ON HERO BACKGROUND
    // ================================================
    const heroBgImg = document.getElementById('hero-bg-img');

    if (heroBgImg) {
        let pTicking = false;

        window.addEventListener('scroll', () => {
            if (!pTicking) {
                requestAnimationFrame(() => {
                    const scrollY = window.scrollY;
                    const speed = 0.3;
                    heroBgImg.style.transform = `translateY(${scrollY * speed}px) scale(1.05)`;
                    pTicking = false;
                });
                pTicking = true;
            }
        }, { passive: true });

        // Initial scale to prevent edges showing
        heroBgImg.style.transform = 'translateY(0) scale(1.05)';
    }

    // ================================================
    // 5. SCROLL REVEAL — About section
    // ================================================
    const revealEls = document.querySelectorAll('.reveal-left, .reveal-right');

    if (revealEls.length) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15 });

        revealEls.forEach(el => revealObserver.observe(el));
    }

    // ================================================
    // 6. ABOUT STATS — Animate counter on scroll
    // ================================================
    const aboutCounters = document.querySelectorAll('.about-stat-num[data-count]');

    const animateAboutCounter = (el) => {
        const target = parseInt(el.dataset.count, 10);
        const duration = 1800;
        const start = performance.now();

        const tick = (now) => {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.round(target * eased);
            if (progress < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
    };

    const aboutCounterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateAboutCounter(entry.target);
                aboutCounterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    aboutCounters.forEach(el => aboutCounterObserver.observe(el));

    // ================================================
    // HOME-ABOUT — counter animation for ha-big-num
    // ================================================
    const haCounters = document.querySelectorAll('.ha-big-num[data-count]');
    const haCounterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.dataset.count, 10);
                const duration = 1800;
                const start = performance.now();
                const tick = (now) => {
                    const p = Math.min((now - start) / duration, 1);
                    const eased = 1 - Math.pow(1 - p, 3);
                    el.textContent = Math.round(target * eased);
                    if (p < 1) requestAnimationFrame(tick);
                };
                requestAnimationFrame(tick);
                haCounterObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });
    haCounters.forEach(el => haCounterObserver.observe(el));
});


document.addEventListener("DOMContentLoaded", function() {
// Premium Sections Animation Logic
            var reveals = document.querySelectorAll('.reveal-up, .zoom-in');
            if (reveals.length) {
                var ro = new IntersectionObserver(function(e) {
                    e.forEach(function(x) {
                        if (x.isIntersecting) {
                            x.target.classList.add('active');
                            ro.unobserve(x.target);
                        }
                    });
                }, { threshold: 0.15, rootMargin: "0px 0px -50px 0px" });
                reveals.forEach(function(el) { ro.observe(el); });
            }
});

