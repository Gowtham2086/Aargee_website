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



/* ================================================
   QUOTE MODAL LOGIC
   ================================================ */
// 1. Inject Modal HTML into the DOM
(function initQuoteModal() {
    const modalHTML = `
        <div class="modal-overlay" id="quoteModal">
            <div class="modal-container">
                <div class="modal-header">
                    <button class="modal-close-btn" id="closeModalBtn" aria-label="Close modal">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                    <h2 class="modal-title">Request a Quote</h2>
                    <p class="modal-subtitle">Tell us about your requirements and our team will get back to you with a customized solution.</p>
                </div>
                <div class="modal-body">
                    <form id="quoteForm" novalidate>
                        <div class="form-grid">
                            <div class="form-group">
                                <label class="form-label" for="quoteName">Full Name *</label>
                                <input type="text" id="quoteName" name="name" class="form-input" required>
                                <span class="error-msg">Name is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteCompany">Company Name *</label>
                                <input type="text" id="quoteCompany" name="company" class="form-input" required>
                                <span class="error-msg">Company is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteEmail">Email Address *</label>
                                <input type="email" id="quoteEmail" name="email" class="form-input" required>
                                <span class="error-msg">Valid email is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quotePhone">Phone Number *</label>
                                <input type="tel" id="quotePhone" name="phone" class="form-input" required>
                                <span class="error-msg">Phone is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteIndustry">Industry *</label>
                                <select id="quoteIndustry" name="industry" class="form-select" required>
                                    <option value="" disabled selected>Select Industry</option>
                                    <option value="Roadways">Roadways</option>
                                    <option value="Railways">Railways</option>
                                    <option value="Airways">Airways</option>
                                    <option value="Waterways">Waterways</option>
                                    <option value="Other">Other</option>
                                </select>
                                <span class="error-msg">Please select an industry</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteProduct">Product / Solution *</label>
                                <input type="text" id="quoteProduct" name="product" class="form-input" required>
                                <span class="error-msg">Product is required</span>
                            </div>
                            <div class="form-group full">
                                <label class="form-label" for="quoteRequirements">Project Requirements *</label>
                                <textarea id="quoteRequirements" name="requirements" class="form-textarea" required></textarea>
                                <span class="error-msg">Requirements are required</span>
                            </div>
                            <!-- Hidden honeypot for spam -->
                            <input type="text" name="_honey" style="display:none">
                            <input type="hidden" name="_subject" value="New Quote Request from AARGEE Website!">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn-modal-cancel" id="cancelModalBtn">Cancel</button>
                    <button type="button" class="btn-modal-submit" id="submitModalBtn">
                        <span class="submit-text">Submit Request</span>
                        <div class="spinner"></div>
                    </button>
                </div>
                
                <!-- Success State -->
                <div class="modal-success" id="modalSuccess">
                    <div class="success-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                    </div>
                    <div class="success-title">Thank You</div>
                    <div class="success-desc">Thank you for contacting AARGEE. Our team will review your requirements and get back to you shortly.</div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);

    // 2. Element References
    const modal = document.getElementById('quoteModal');
    const closeBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancelModalBtn');
    const submitBtn = document.getElementById('submitModalBtn');
    const form = document.getElementById('quoteForm');
    const successState = document.getElementById('modalSuccess');
    
    // Find all 'Get A Quote' buttons and the main nav button
    const quoteBtns = document.querySelectorAll('a');
    const targetBtns = Array.from(quoteBtns).filter(btn => 
        btn.id === 'nav-contact-btn' || btn.textContent.trim().toLowerCase() === 'get a quote'
    );

    // 3. Modal Interactions
    const openModal = (e) => {
        if(e) e.preventDefault();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    };

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        setTimeout(() => {
            form.reset();
            successState.classList.remove('active');
            document.querySelectorAll('.form-group').forEach(g => g.classList.remove('has-error'));
        }, 400); // Reset after animation completes
    };

    targetBtns.forEach(btn => btn.addEventListener('click', openModal));
    closeBtn.addEventListener('click', closeModal);
    cancelBtn.addEventListener('click', closeModal);
    
    // Close on overlay click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
    
    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
    });

    // 4. Validation & Submission Logic
    const validateEmail = (email) => {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    };

    const validateForm = () => {
        let isValid = true;
        const requiredInputs = form.querySelectorAll('[required]');
        
        requiredInputs.forEach(input => {
            const group = input.closest('.form-group');
            if (!input.value.trim() || (input.type === 'email' && !validateEmail(input.value))) {
                group.classList.add('has-error');
                input.classList.add('error');
                isValid = false;
            } else {
                group.classList.remove('has-error');
                input.classList.remove('error');
            }
            
            // Clear error on typing
            input.addEventListener('input', () => {
                group.classList.remove('has-error');
                input.classList.remove('error');
            }, { once: true });
        });
        
        return isValid;
    };

    submitBtn.addEventListener('click', () => {
        if (!validateForm()) return;
        
        // Disable button & show spinner
        submitBtn.disabled = true;
        submitBtn.classList.add('loading');
        
        // Collect Data
        const formData = new FormData(form);
        
        // AJAX Post to formsubmit
        fetch("https://formsubmit.co/ajax/gowtham2086@gmail.com", {
            method: "POST",
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            submitBtn.disabled = false;
            submitBtn.classList.remove('loading');
            
            if(data.success) {
                // Show success UI
                successState.classList.add('active');
                
                // Auto close after 4 seconds
                setTimeout(() => {
                    closeModal();
                }, 4000);
            } else {
                alert("Something went wrong. Please try again.");
            }
        })
        .catch(error => {
            submitBtn.disabled = false;
            submitBtn.classList.remove('loading');
            console.error('Error:', error);
            alert("Network error. Please try again later.");
        });
    });
})();


/* ================================================
   QUOTE MODAL LOGIC
   ================================================ */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Modal HTML into the DOM
    const modalHTML = `
        <div class="modal-overlay" id="quoteModal">
            <div class="modal-container">
                <div class="modal-header">
                    <button class="modal-close-btn" id="closeModalBtn" aria-label="Close modal">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                    <h2 class="modal-title">Request a Quote</h2>
                    <p class="modal-subtitle">Tell us about your requirements and our team will get back to you with a customized solution.</p>
                </div>
                <div class="modal-body">
                    <form id="quoteForm" novalidate>
                        <div class="form-grid">
                            <div class="form-group">
                                <label class="form-label" for="quoteName">Full Name *</label>
                                <input type="text" id="quoteName" name="name" class="form-input" required>
                                <span class="error-msg">Name is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteCompany">Company Name *</label>
                                <input type="text" id="quoteCompany" name="company" class="form-input" required>
                                <span class="error-msg">Company is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteEmail">Email Address *</label>
                                <input type="email" id="quoteEmail" name="email" class="form-input" required>
                                <span class="error-msg">Valid email is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quotePhone">Phone Number *</label>
                                <input type="tel" id="quotePhone" name="phone" class="form-input" required>
                                <span class="error-msg">Phone is required</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteIndustry">Industry *</label>
                                <select id="quoteIndustry" name="industry" class="form-select" required>
                                    <option value="" disabled selected>Select Industry</option>
                                    <option value="Roadways">Roadways</option>
                                    <option value="Railways">Railways</option>
                                    <option value="Airways">Airways</option>
                                    <option value="Waterways">Waterways</option>
                                    <option value="Other">Other</option>
                                </select>
                                <span class="error-msg">Please select an industry</span>
                            </div>
                            <div class="form-group">
                                <label class="form-label" for="quoteProduct">Product / Solution *</label>
                                <input type="text" id="quoteProduct" name="product" class="form-input" required>
                                <span class="error-msg">Product is required</span>
                            </div>
                            <div class="form-group full">
                                <label class="form-label" for="quoteRequirements">Project Requirements *</label>
                                <textarea id="quoteRequirements" name="requirements" class="form-textarea" required></textarea>
                                <span class="error-msg">Requirements are required</span>
                            </div>
                            <!-- Hidden honeypot for spam -->
                            <input type="text" name="_honey" style="display:none">
                            <input type="hidden" name="_subject" value="New Quote Request from AARGEE Website!">
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn-modal-cancel" id="cancelModalBtn">Cancel</button>
                    <button type="button" class="btn-modal-submit" id="submitModalBtn">
                        <span class="submit-text">Submit Request</span>
                        <div class="spinner"></div>
                    </button>
                </div>
                
                <!-- Success State -->
                <div class="modal-success" id="modalSuccess">
                    <div class="success-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                    </div>
                    <div class="success-title">Thank You</div>
                    <div class="success-desc">Thank you for contacting AARGEE. Our team will review your requirements and get back to you shortly.</div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);

    // 2. Element References
    const modal = document.getElementById('quoteModal');
    const closeBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancelModalBtn');
    const submitBtn = document.getElementById('submitModalBtn');
    const form = document.getElementById('quoteForm');
    const successState = document.getElementById('modalSuccess');
    
    // Find all 'Get A Quote' buttons (might be multiple)
    const quoteBtns = document.querySelectorAll('a[href="#"], #nav-contact-btn');
    const targetBtns = Array.from(quoteBtns).filter(btn => btn.textContent.trim().toLowerCase() === 'get a quote');

    // 3. Modal Interactions
    const openModal = (e) => {
        if(e) e.preventDefault();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    };

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
        setTimeout(() => {
            form.reset();
            successState.classList.remove('active');
            document.querySelectorAll('.form-group').forEach(g => g.classList.remove('has-error'));
        }, 400); // Reset after animation completes
    };

    targetBtns.forEach(btn => btn.addEventListener('click', openModal));
    closeBtn.addEventListener('click', closeModal);
    cancelBtn.addEventListener('click', closeModal);
    
    // Close on overlay click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
    
    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
    });

    // 4. Validation & Submission Logic
    const validateEmail = (email) => {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    };

    const validateForm = () => {
        let isValid = true;
        const requiredInputs = form.querySelectorAll('[required]');
        
        requiredInputs.forEach(input => {
            const group = input.closest('.form-group');
            if (!input.value.trim() || (input.type === 'email' && !validateEmail(input.value))) {
                group.classList.add('has-error');
                input.classList.add('error');
                isValid = false;
            } else {
                group.classList.remove('has-error');
                input.classList.remove('error');
            }
            
            // Clear error on typing
            input.addEventListener('input', () => {
                group.classList.remove('has-error');
                input.classList.remove('error');
            }, { once: true });
        });
        
        return isValid;
    };

    submitBtn.addEventListener('click', () => {
        if (!validateForm()) return;
        
        // Disable button & show spinner
        submitBtn.disabled = true;
        submitBtn.classList.add('loading');
        
        // Collect Data
        const formData = new FormData(form);
        
        // AJAX Post to formsubmit
        fetch("https://formsubmit.co/ajax/gowtham2086@gmail.com", {
            method: "POST",
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            submitBtn.disabled = false;
            submitBtn.classList.remove('loading');
            
            if(data.success) {
                // Show success UI
                successState.classList.add('active');
                
                // Auto close after 4 seconds
                setTimeout(() => {
                    closeModal();
                }, 4000);
            } else {
                alert("Something went wrong. Please try again.");
            }
        })
        .catch(error => {
            submitBtn.disabled = false;
            submitBtn.classList.remove('loading');
            console.error('Error:', error);
            alert("Network error. Please try again later.");
        });
    });
});
