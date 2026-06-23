import re

# ==============================================================================
# 1. BUILD MANUFACTURING.CSS
# ==============================================================================

css_content = """
/* ====================================================================
   FINAL MASTER MANUFACTURING PAGE - PREMIUM INDUSTRIAL
   ==================================================================== */

/* Global Resets for Manufacturing Page */
body {
    background-color: #ffffff;
    color: #1A1A1A;
    font-family: 'Inter', sans-serif;
}

/* Background Utility Classes */
.m-bg-black { background-color: #000000; color: #ffffff; }
.m-bg-white { background-color: #ffffff; color: #1A1A1A; }
.m-bg-charcoal { background-color: #1A1A1A; color: #ffffff; }
.m-bg-light { background-color: #F5F5F5; color: #1A1A1A; }

/* Structural Padding */
.m-section {
    padding: 120px 0;
    position: relative;
    overflow: hidden;
}
.m-container {
    max-width: 1300px;
    margin: 0 auto;
    padding: 0 24px;
}

/* Typography - Stark Industrial */
.m-label {
    display: inline-block;
    font-family: 'Outfit', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.25em;
    color: #C8102E;
    margin-bottom: 24px;
    position: relative;
}
.m-label::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 100%;
    margin-left: 16px;
    width: 32px;
    height: 1px;
    background: #C8102E;
}
.m-h2 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2.5rem, 4vw, 3.8rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 24px;
}
.m-h2.center { text-align: center; margin-left: auto; margin-right: auto; }
.m-h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 12px;
}
.m-desc {
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 40px;
    max-width: 800px;
}
.m-desc.center { text-align: center; margin-left: auto; margin-right: auto; }

/* Split Screen Layouts */
.m-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 85vh;
}
.m-split-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 10% 12%;
}
.m-split-img {
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 500px;
    background-color: #000;
}
.m-split-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    inset: 0;
    /* Industrial graded filter */
    filter: grayscale(80%) contrast(1.15) brightness(0.85);
}
.m-split-reverse .m-split-content { grid-column: 1; grid-row: 1; }
.m-split-reverse .m-split-img { grid-column: 2; grid-row: 1; }
@media (max-width: 992px) {
    .m-split { grid-template-columns: 1fr; min-height: auto; }
    .m-split-reverse .m-split-content { grid-column: 1; grid-row: 2; }
    .m-split-reverse .m-split-img { grid-column: 1; grid-row: 1; }
    .m-split-content { padding: 80px 24px; }
}

/* Hero Section */
.m-hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    background-color: #000;
}
.m-hero-bg {
    position: absolute;
    inset: 0;
}
.m-hero-bg img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(80%) contrast(1.2) brightness(0.6); /* Darker for text readability */
}
.m-hero-content {
    position: relative;
    z-index: 10;
    max-width: 900px;
    padding-top: 60px; /* Offset for nav */
}
.m-hero-h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(3rem, 6vw, 5rem);
    font-weight: 900;
    line-height: 1.05;
    color: #fff;
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}
.m-hero-desc {
    font-size: 1.15rem;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.8);
    max-width: 700px;
    margin-bottom: 40px;
}
.m-hero-list {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-bottom: 48px;
}
.m-hero-list li {
    display: flex;
    align-items: center;
    gap: 12px;
    color: #fff;
    font-weight: 500;
}
.m-hero-list li::before {
    content: '';
    width: 6px;
    height: 6px;
    background-color: #C8102E;
}
@media (max-width: 600px) {
    .m-hero-list { grid-template-columns: 1fr; }
}

/* Buttons */
.m-btn-row { display: flex; gap: 16px; flex-wrap: wrap; }
.m-btn {
    display: inline-flex;
    align-items: center;
    padding: 16px 36px;
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-size: 0.9rem;
    text-decoration: none;
    transition: all 0.3s ease;
}
.m-btn-primary {
    background-color: #C8102E;
    color: #fff;
    border: 2px solid #C8102E;
}
.m-btn-primary:hover {
    background-color: #a30c25;
    border-color: #a30c25;
}
.m-btn-outline {
    background-color: transparent;
    color: #fff;
    border: 2px solid #fff;
}
.m-btn-outline:hover {
    background-color: #fff;
    color: #000;
}
.m-btn-dark {
    background-color: #000;
    color: #fff;
    border: 2px solid #000;
}
.m-btn-dark:hover {
    background-color: #C8102E;
    border-color: #C8102E;
}

/* 4-Card Grid (Capabilities) */
.m-grid-4 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
}
@media (max-width: 768px) {
    .m-grid-4 { grid-template-columns: 1fr; }
}
.m-card {
    padding: 48px;
    background-color: #F9F9F9;
    border-left: 3px solid transparent;
    transition: all 0.3s ease;
}
.m-card:hover {
    background-color: #fff;
    border-left-color: #C8102E;
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
}
.m-card-p {
    font-size: 1rem;
    line-height: 1.6;
    color: #555;
    margin: 0;
}

/* Process Timeline (Horizontal) */
.m-process-wrap {
    display: flex;
    justify-content: space-between;
    position: relative;
    max-width: 1100px;
    margin: 60px auto 0;
    overflow-x: auto;
    padding-bottom: 20px;
}
.m-pt-line {
    position: absolute;
    top: 24px;
    left: 20px;
    right: 20px;
    height: 2px;
    background-color: #ddd;
    z-index: 0;
}
.m-pt-node {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 120px;
    text-align: center;
}
.m-pt-dot {
    width: 16px;
    height: 16px;
    background-color: #C8102E;
    border-radius: 50%;
    margin-bottom: 16px;
    outline: 8px solid #F5F5F5;
}
.m-pt-text {
    font-family: 'Outfit', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #1A1A1A;
    line-height: 1.2;
}

/* Split Screen Lists (Innovation & Fabrication) */
.m-split-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}
.m-split-list li {
    font-family: 'Outfit', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    padding: 16px;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.03);
}
.m-bg-white .m-split-list li {
    border-color: rgba(0,0,0,0.1);
    background: #F9F9F9;
}

/* 6-Card Grid (Quality Assurance) */
.m-grid-6 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px; /* Creates the thin dividers via background color */
    background-color: #333; /* Divider color */
    border: 1px solid #333;
}
@media (max-width: 900px) {
    .m-grid-6 { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
    .m-grid-6 { grid-template-columns: 1fr; }
}
.m-test-card {
    background-color: #1A1A1A;
    padding: 40px;
    display: flex;
    align-items: center;
    gap: 16px;
    font-family: 'Outfit', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    transition: background-color 0.3s ease;
}
.m-test-card:hover {
    background-color: #222;
}
.m-test-card::before {
    content: '';
    display: block;
    width: 8px;
    height: 8px;
    background-color: #C8102E;
}

/* Image Gallery (Inside Aargee) */
.m-gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 60px;
}
@media (max-width: 900px) {
    .m-gallery { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
    .m-gallery { grid-template-columns: 1fr; }
}
.m-gal-item {
    aspect-ratio: 4/3;
    overflow: hidden;
    position: relative;
    background-color: #000;
}
.m-gal-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(80%) contrast(1.15) brightness(0.8);
    transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.6s;
}
.m-gal-item:hover img {
    transform: scale(1.05);
    filter: grayscale(0%) contrast(1.1) brightness(1); /* Reveal color on hover */
}

/* Animated Statistics */
.m-stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 40px;
    text-align: center;
}
@media (max-width: 900px) {
    .m-stats-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 480px) {
    .m-stats-grid { grid-template-columns: 1fr; }
}
.m-stat-item h4 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(2rem, 3vw, 2.8rem);
    font-weight: 900;
    color: #fff;
    margin-bottom: 8px;
    line-height: 1.1;
}
.m-stat-item p {
    font-family: 'Outfit', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #C8102E;
    margin: 0;
}

/* Final CTA */
.m-cta {
    padding: 140px 0;
    text-align: center;
}
.m-cta-inner {
    max-width: 800px;
    margin: 0 auto;
}

/* Animations (Sharp Fade) */
.ind-fade {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.ind-fade.visible {
    opacity: 1;
    transform: translateY(0);
}
"""

with open("manufacturing.css", "w", encoding="utf-8") as f:
    f.write(css_content)

# ==============================================================================
# 2. EXTRACT NAV & FOOTER FROM INDEX.HTML
# ==============================================================================
with open("index.html", "r", encoding="utf-8") as f:
    idx_html = f.read()

nav_match = re.search(r'(<!-- ======== NAVIGATION ======== -->.*?)</nav>', idx_html, re.DOTALL)
nav_html = nav_match.group(1) + "</nav>" if nav_match else ""
footer_match = re.search(r'(<!-- PREMIUM FOOTER -->.*?</footer>)', idx_html, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""

# Ensure Manufacturing is active
nav_html = nav_html.replace('class="nav-link active"', 'class="nav-link"')
nav_html = nav_html.replace('href="manufacturing.html" id="nav-manufacturing"', 'href="manufacturing.html" id="nav-manufacturing" class="nav-link active"')

# ==============================================================================
# 3. BUILD MANUFACTURING.HTML
# ==============================================================================
new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>Manufacturing Excellence | Aargee Equipment Pvt. Ltd.</title>
    <link href="https://fonts.googleapis.com" rel="preconnect" />
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Outfit:wght@400;600;700;800;900&amp;display=swap" rel="stylesheet" />
    <link href="index.css" rel="stylesheet" />
    <link href="manufacturing.css" rel="stylesheet" />
</head>
<body>

{nav_html}

<!-- =======================================================
     HERO SECTION
     ======================================================= -->
<header class="m-hero">
    <div class="m-hero-bg">
        <img src="placeholder-hero.jpg" alt="Aargee Manufacturing Facility">
    </div>
    <div class="m-container" style="width: 100%;">
        <div class="m-hero-content ind-fade">
            <span class="m-label">Manufacturing Excellence</span>
            <h1 class="m-hero-h1">Built With Precision.<br>Driven By Engineering.</h1>
            <p class="m-hero-desc">Advanced manufacturing infrastructure, skilled expertise, and systematic production processes delivering reliable transportation technologies with quality, consistency, and performance.</p>
            
            <ul class="m-hero-list">
                <li>Automated LED Manufacturing</li>
                <li>Mechanical Fabrication</li>
                <li>Assembly & Integration</li>
                <li>In-House Testing & Validation</li>
            </ul>
            
            <div class="m-btn-row">
                <a href="#capabilities" class="m-btn m-btn-primary">Explore Capabilities</a>
                <a href="#process" class="m-btn m-btn-outline">View Manufacturing Process</a>
            </div>
        </div>
    </div>
</header>

<!-- =======================================================
     SECTION 02 - MANUFACTURING CAPABILITIES
     ======================================================= -->
<section class="m-section m-bg-white" id="capabilities">
    <div class="m-container">
        <div class="ind-fade" style="margin-bottom: 60px;">
            <span class="m-label">What We Do</span>
            <h2 class="m-h2">Manufacturing Built For Reliability</h2>
            <p class="m-desc">Aargee combines engineering expertise, manufacturing infrastructure, and process-driven production systems to deliver dependable transportation technologies for demanding operating environments.</p>
        </div>
        
        <div class="m-grid-4">
            <div class="m-card ind-fade">
                <h3 class="m-h3">Automated LED Manufacturing</h3>
                <p class="m-card-p">Advanced production processes ensuring consistent quality, performance, and reliability for LED display technologies.</p>
            </div>
            <div class="m-card ind-fade">
                <h3 class="m-h3">Mechanical Fabrication</h3>
                <p class="m-card-p">Precision fabrication of metal frames, enclosures, mounting structures, and transportation-grade mechanical assemblies.</p>
            </div>
            <div class="m-card ind-fade">
                <h3 class="m-h3">Assembly & Integration</h3>
                <p class="m-card-p">Dedicated assembly operations supporting electronics integration, system assembly, and functional verification.</p>
            </div>
            <div class="m-card ind-fade">
                <h3 class="m-h3">Testing & Validation</h3>
                <p class="m-card-p">Comprehensive inspection, verification, and testing processes to ensure every product meets quality standards.</p>
            </div>
        </div>
    </div>
</section>

<!-- =======================================================
     SECTION 03 - HOW WE MANUFACTURE
     ======================================================= -->
<section class="m-section m-bg-light" id="process">
    <div class="m-container">
        <div class="ind-fade text-center">
            <div style="text-align: center;"><span class="m-label">Process</span></div>
            <h2 class="m-h2 center">From Engineering To Delivery</h2>
        </div>
        
        <div class="m-process-wrap ind-fade">
            <div class="m-pt-line"></div>
            
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Engineering<br>& Design</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Material<br>Preparation</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Fabrication</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Assembly</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Integration</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Testing</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Quality<br>Verification</div></div>
            <div class="m-pt-node"><div class="m-pt-dot"></div><div class="m-pt-text">Delivery</div></div>
        </div>
    </div>
</section>

<!-- =======================================================
     SECTION 04 - ENGINEERING & DEVELOPMENT
     ======================================================= -->
<section class="m-split m-bg-black" id="innovation">
    <div class="m-split-img ind-fade">
        <img src="placeholder-engineering.jpg" alt="Engineering and Development">
    </div>
    <div class="m-split-content ind-fade">
        <span class="m-label">Innovation</span>
        <h2 class="m-h2">Engineering Beyond Manufacturing</h2>
        <p class="m-desc">Our engineering teams continuously improve designs, optimize performance, and develop customized solutions that meet evolving transportation requirements.</p>
        
        <ul class="m-split-list">
            <li>Product Development</li>
            <li>Electronics Engineering</li>
            <li>Mechanical Design</li>
            <li>Prototype Validation</li>
            <li>System Optimization</li>
            <li>Customized Solutions</li>
        </ul>
    </div>
</section>

<!-- =======================================================
     SECTION 05 - MECHANICAL FABRICATION
     ======================================================= -->
<section class="m-split m-split-reverse m-bg-white" id="fabrication">
    <div class="m-split-content ind-fade">
        <span class="m-label">Fabrication</span>
        <h2 class="m-h2">Precision Mechanical Manufacturing</h2>
        <p class="m-desc">Supporting transportation technologies through precision fabrication of structural components, mounting systems, metal enclosures, and custom mechanical assemblies designed for long-term durability.</p>
        
        <ul class="m-split-list">
            <li>Metal Frame Fabrication</li>
            <li>Structural Assemblies</li>
            <li>Enclosure Manufacturing</li>
            <li>Mechanical Integration</li>
            <li>Transportation Components</li>
            <li>Custom Fabrication</li>
        </ul>
    </div>
    <div class="m-split-img ind-fade">
        <img src="placeholder-fabrication.jpg" alt="Workshop and Fabrication Imagery">
    </div>
</section>

<!-- =======================================================
     SECTION 06 - QUALITY & TESTING
     ======================================================= -->
<section class="m-section m-bg-charcoal" id="testing">
    <div class="m-container">
        <div class="ind-fade" style="margin-bottom: 60px;">
            <span class="m-label">Quality Assurance</span>
            <h2 class="m-h2">Quality Built Into Every Product</h2>
            <p class="m-desc">Every product undergoes systematic inspection, testing, and validation to ensure reliable performance, operational durability, and customer confidence.</p>
        </div>
        
        <div class="m-grid-6 ind-fade">
            <div class="m-test-card">Functional Testing</div>
            <div class="m-test-card">Electrical Verification</div>
            <div class="m-test-card">Performance Validation</div>
            <div class="m-test-card">Assembly Inspection</div>
            <div class="m-test-card">Reliability Checks</div>
            <div class="m-test-card">Final Quality Approval</div>
        </div>
    </div>
</section>

<!-- =======================================================
     SECTION 07 - MANUFACTURING GALLERY
     ======================================================= -->
<section class="m-section m-bg-white" id="gallery">
    <div class="m-container">
        <div class="ind-fade text-center">
            <div style="text-align: center;"><span class="m-label">Inside Aargee</span></div>
            <h2 class="m-h2 center">Manufacturing In Action</h2>
        </div>
        
        <div class="m-gallery">
            <div class="m-gal-item ind-fade"><img src="placeholder-gal1.jpg" alt="Production Floor"></div>
            <div class="m-gal-item ind-fade"><img src="placeholder-gal2.jpg" alt="Assembly Operations"></div>
            <div class="m-gal-item ind-fade"><img src="placeholder-gal3.jpg" alt="LED Manufacturing"></div>
            <div class="m-gal-item ind-fade"><img src="placeholder-gal4.jpg" alt="Mechanical Fabrication"></div>
            <div class="m-gal-item ind-fade"><img src="placeholder-gal5.jpg" alt="Quality Inspection"></div>
            <div class="m-gal-item ind-fade"><img src="placeholder-gal6.jpg" alt="Engineering Teams"></div>
        </div>
    </div>
</section>

<!-- =======================================================
     SECTION 08 - MANUFACTURING STRENGTH
     ======================================================= -->
<section class="m-section m-bg-black" id="strength">
    <div class="m-container">
        <div class="ind-fade text-center" style="margin-bottom: 60px;">
            <div style="text-align: center;"><span class="m-label">Our Strength</span></div>
            <h2 class="m-h2 center">Built On Capability</h2>
        </div>
        
        <div class="m-stats-grid">
            <div class="m-stat-item ind-fade">
                <h4>Automated</h4>
                <p>LED Manufacturing</p>
            </div>
            <div class="m-stat-item ind-fade">
                <h4>Dedicated</h4>
                <p>Engineering Team</p>
            </div>
            <div class="m-stat-item ind-fade">
                <h4>Advanced</h4>
                <p>Production Systems</p>
            </div>
            <div class="m-stat-item ind-fade">
                <h4>In-House</h4>
                <p>Testing & Validation</p>
            </div>
        </div>
    </div>
</section>

<!-- =======================================================
     FINAL CTA SECTION
     ======================================================= -->
<section class="m-cta m-bg-white">
    <div class="m-cta-inner ind-fade">
        <h2 class="m-h2 center">Engineering Quality Through Manufacturing Excellence</h2>
        <p class="m-desc center">Combining manufacturing expertise, engineering precision, and quality-driven processes to deliver technologies trusted across the transportation industry.</p>
        <div style="text-align: center; margin-top: 40px;">
            <a href="solutions.html" class="m-btn m-btn-dark">Explore Our Solutions</a>
        </div>
    </div>
</section>

{footer_html}

<script src="main.js"></script>
<script>
    (function () {{
        // Sticky Navbar logic
        var navbar = document.getElementById('navbar');
        if (navbar) {{
            window.addEventListener('scroll', function () {{
                navbar.classList.toggle('scrolled', window.scrollY > 45);
            }}, {{ passive: true }});
        }}

        // Elegant Industrial Fade-Up Observer
        const fadeElements = document.querySelectorAll('.ind-fade');
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }}
            }});
        }}, {{ threshold: 0.15 }});

        fadeElements.forEach((el, index) => {{
            // Add slight staggered delay to grid items automatically
            if (el.classList.contains('m-card') || el.classList.contains('m-gal-item') || el.classList.contains('m-stat-item')) {{
                el.style.transitionDelay = `${{ (index % 4) * 0.1 }}s`;
            }}
            observer.observe(el);
        }});
    }})();
</script>
</body>
</html>
"""

with open("manufacturing.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Master manufacturing page successfully created.")
