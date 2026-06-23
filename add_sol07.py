import re

css_code = """
/* ================================================
   SOLUTION ANALYTICS GRID (SOLUTION 07)
   ================================================ */
.sol-analytics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-bottom: 64px;
}

.sol-analytics-card {
    background: #111827; /* Dark luxury card background */
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 18px;
    padding: 32px;
    display: flex;
    flex-direction: column;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.sol-analytics-card:hover {
    transform: translateY(-8px);
    border-color: rgba(200, 16, 46, 0.3);
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.4);
}

.sac-icon {
    width: 56px;
    height: 56px;
    background: rgba(200, 16, 46, 0.1);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--red);
    margin-bottom: 24px;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.sol-analytics-card:hover .sac-icon {
    transform: scale(1.1) rotate(5deg);
    background: rgba(200, 16, 46, 0.15);
}

.sac-title {
    font-family: var(--font-display);
    font-size: 22px;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 16px;
    line-height: 1.2;
}

.sac-desc {
    font-size: 14.5px;
    color: var(--white-muted);
    line-height: 1.6;
    margin-bottom: 24px;
}

.sol-analytics-card .sol-feat-list {
    margin-bottom: auto; /* pushes the image down */
    color: var(--white-soft);
}

/* Why Choose Section */
.sol-why-choose {
    background: #111827;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 18px;
    padding: 40px;
}

.sol-why-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
}

.sw-item {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 15px;
    color: var(--white-soft);
    font-weight: 500;
}

@media (max-width: 1024px) {
    .sol-analytics-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .sol-analytics-grid {
        grid-template-columns: 1fr;
    }
}
"""

html_code = """
    <!-- ============================================================
         SOLUTION 07 — Intelligent Camera & Passenger Analytics
         ============================================================ -->
    <section class="sol-sol-section bg-dark" id="sol09">
        <div class="sol-container">
            <div class="sol-analytics-intro sol-fade" style="margin-bottom: 48px;">
                <div class="sol-lbl" style="justify-content:center;">Solution 07</div>
                <h2 class="sol-h2 white" style="text-align:center;">Intelligent Camera & Passenger Analytics Solutions</h2>
                <p class="sol-why-body" style="text-align:center; max-width:800px; margin: 0 auto;">Advanced vision-based monitoring and analytics technologies designed to enhance passenger safety, operational visibility, and fleet intelligence. These solutions provide real-time monitoring, AI-powered passenger analytics, and improved situational awareness for modern transportation systems.</p>
            </div>

            <!-- The 3 Cards -->
            <div class="sol-analytics-grid">
                <!-- Card 01 -->
                <div class="sol-analytics-card sol-fade d1">
                    <div class="sac-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                            <circle cx="9" cy="7" r="4" />
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                            <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                        </svg>
                    </div>
                    <h3 class="sac-title">AI Passenger Counting System</h3>
                    <p class="sac-desc">Accurately monitor passenger boarding and alighting activities using AI-powered vision analytics. The system provides real-time occupancy insights, passenger flow analysis, and operational data to improve transportation planning and fleet efficiency.</p>
                    <ul class="sol-feat-list" style="margin-bottom: 24px;">
                        <li>Real-time passenger counting</li>
                        <li>Boarding and alighting detection</li>
                        <li>AI-powered analytics</li>
                        <li>Occupancy monitoring</li>
                        <li>High counting accuracy</li>
                        <li>Fleet utilization insights</li>
                    </ul>
                    <div class="sol-image-container" style="margin-top:auto;">
                        <div class="sol-sol-img-wrap" style="aspect-ratio:16/9; margin-bottom: 0;">
                            <img src="placeholder-ai-count.jpg" alt="AI Passenger Counting System">
                        </div>
                    </div>
                </div>

                <!-- Card 02 -->
                <div class="sol-analytics-card sol-fade d2">
                    <div class="sac-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                            <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                            <circle cx="12" cy="13" r="4" />
                        </svg>
                    </div>
                    <h3 class="sac-title">Interior Monitoring Camera</h3>
                    <p class="sac-desc">Designed for continuous in-vehicle monitoring, the interior camera enhances passenger safety, security, and operational visibility by providing clear visual coverage of passenger and driver areas.</p>
                    <ul class="sol-feat-list" style="margin-bottom: 24px;">
                        <li>Full HD video monitoring</li>
                        <li>Wide-angle coverage</li>
                        <li>Driver behaviour monitoring</li>
                        <li>Passenger area surveillance</li>
                        <li>Low-light performance</li>
                        <li>Audio recording support</li>
                    </ul>
                    <div class="sol-image-container" style="margin-top:auto;">
                        <div class="sol-sol-img-wrap" style="aspect-ratio:16/9; margin-bottom: 0;">
                            <img src="placeholder-interior-cam.jpg" alt="Interior Monitoring Camera">
                        </div>
                    </div>
                </div>

                <!-- Card 03 -->
                <div class="sol-analytics-card sol-fade d3">
                    <div class="sac-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                            <circle cx="12" cy="12" r="3" />
                        </svg>
                    </div>
                    <h3 class="sac-title">Exterior Monitoring Camera</h3>
                    <p class="sac-desc">Provides high-quality external vehicle monitoring to improve driver awareness, operational safety, and incident recording in urban and intercity transportation environments.</p>
                    <ul class="sol-feat-list" style="margin-bottom: 24px;">
                        <li>Full HD imaging</li>
                        <li>Day and night operation</li>
                        <li>Wide viewing angle</li>
                        <li>Low-light visibility</li>
                        <li>Weather-resistant design</li>
                        <li>Transportation-grade reliability</li>
                    </ul>
                    <div class="sol-image-container" style="margin-top:auto;">
                        <div class="sol-sol-img-wrap" style="aspect-ratio:16/9; margin-bottom: 0;">
                            <img src="placeholder-exterior-cam.jpg" alt="Exterior Monitoring Camera">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Why Choose This Solution -->
            <div class="sol-why-choose sol-fade d4">
                <h3 class="sac-title" style="text-align:center; margin-bottom:32px; color:#fff;">Why Choose This Solution</h3>
                <div class="sol-why-grid">
                    <div class="sw-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                        Enhanced Passenger Safety
                    </div>
                    <div class="sw-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                        Real-Time Visibility
                    </div>
                    <div class="sw-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                        AI-Based Analytics
                    </div>
                    <div class="sw-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                        Operational Intelligence
                    </div>
                    <div class="sw-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                        Improved Fleet Management
                    </div>
                    <div class="sw-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
                        Transportation-Grade Reliability
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open("index.css", "a", encoding="utf-8") as f:
    f.write(css_code)

with open("solutions.html", "r", encoding="utf-8") as f:
    content = f.read()

# Insert before <!-- ============================================================
#         WHY AARGEE — dark
#         ============================================================ -->
target_marker = "<!-- ============================================================\n         WHY AARGEE — dark"
if target_marker in content:
    new_content = content.replace(target_marker, html_code + "\n    " + target_marker)
else:
    # try another way
    target_marker = "<!-- WHY AARGEE"
    new_content = re.sub(r'<!--\s*============[\s\S]*?WHY AARGEE', html_code + "\n    <!-- ============================================================\n         WHY AARGEE", content)

with open("solutions.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Added Solution 07 successfully.")
