js_code = """
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
"""

with open("main.js", "a", encoding="utf-8") as f:
    f.write("\n" + js_code)

print("JS appended to main.js")
