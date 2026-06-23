import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

new_html = """    <!-- ============================================================
         SOLUTION 07 — AI Passenger Counting
         ============================================================ -->
    <section class="sol-sol-section bg-white" id="sol09">
        <div class="sol-container">
            <div class="sol-sol-inner">
                <!-- Text side -->
                <div class="sol-sol-content sol-fade d1">
                    <div class="sol-sol-num">07</div>
                    <div class="sol-sol-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                            <circle cx="9" cy="7" r="4" />
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                            <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                        </svg>
                    </div>
                    <div class="sol-lbl">Solution 07</div>
                    <h2 class="sol-sol-title">AI Passenger Counting System</h2>
                    <p class="sol-sol-desc">Accurately monitor passenger boarding and alighting activities using AI-powered vision analytics. The system provides real-time occupancy insights, passenger flow analysis, and operational data to improve transportation planning and fleet efficiency.</p>
                    
                    <ul class="sol-feat-list">
                        <li>Real-time passenger counting</li>
                        <li>Boarding and alighting detection</li>
                        <li>AI-powered analytics</li>
                        <li>Occupancy monitoring</li>
                        <li>High counting accuracy</li>
                        <li>Fleet utilization insights</li>
                    </ul>
                </div>

                <!-- Image side -->
                <div class="sol-sol-image sol-fade d2">
                    <div class="sol-sol-img-wrap">
                        <img src="camera-ai.jpg" alt="AI Passenger Counting System">
                    </div>
                    <div class="sol-img-badge">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="12 6 12 12 16 14"/>
                        </svg>
                        <div>
                            <span>AI Analytics</span>
                            <strong>Real-Time Monitoring</strong>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SOLUTION 08 — Interior Monitoring Camera
         ============================================================ -->
    <section class="sol-sol-section bg-grey" id="sol10">
        <div class="sol-container">
            <div class="sol-sol-inner reverse">
                <!-- Text side -->
                <div class="sol-sol-content sol-fade d1">
                    <div class="sol-sol-num">08</div>
                    <div class="sol-sol-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                            <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                            <circle cx="12" cy="13" r="4" />
                        </svg>
                    </div>
                    <div class="sol-lbl">Solution 08</div>
                    <h2 class="sol-sol-title">Interior Monitoring Camera</h2>
                    <p class="sol-sol-desc">Designed for continuous in-vehicle monitoring, the interior camera enhances passenger safety, security, and operational visibility by providing clear visual coverage of passenger and driver areas.</p>
                    
                    <ul class="sol-feat-list">
                        <li>Full HD video monitoring</li>
                        <li>Wide-angle coverage</li>
                        <li>Driver behaviour monitoring</li>
                        <li>Passenger area surveillance</li>
                        <li>Low-light performance</li>
                        <li>Audio recording support</li>
                    </ul>
                </div>

                <!-- Image side -->
                <div class="sol-sol-image sol-fade d2">
                    <div class="sol-sol-img-wrap">
                        <img src="camera-interior.jpg" alt="Interior Monitoring Camera">
                    </div>
                    <div class="sol-img-badge">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="12 6 12 12 16 14"/>
                        </svg>
                        <div>
                            <span>Continuous</span>
                            <strong>HD Recording</strong>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SOLUTION 09 — Exterior Monitoring Camera
         ============================================================ -->
    <section class="sol-sol-section bg-dark" id="sol11">
        <div class="sol-container">
            <div class="sol-sol-inner">
                <!-- Text side -->
                <div class="sol-sol-content sol-fade d1">
                    <div class="sol-sol-num dark">09</div>
                    <div class="sol-sol-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                            <circle cx="12" cy="12" r="3" />
                        </svg>
                    </div>
                    <div class="sol-lbl">Solution 09</div>
                    <h2 class="sol-sol-title white">Exterior Monitoring Camera</h2>
                    <p class="sol-sol-desc white">Provides high-quality external vehicle monitoring to improve driver awareness, operational safety, and incident recording in urban and intercity transportation environments.</p>
                    
                    <ul class="sol-feat-list white">
                        <li>Full HD imaging</li>
                        <li>Day and night operation</li>
                        <li>Wide viewing angle</li>
                        <li>Low-light visibility</li>
                        <li>Weather-resistant design</li>
                        <li>Transportation-grade reliability</li>
                    </ul>
                </div>

                <!-- Image side -->
                <div class="sol-sol-image sol-fade d2">
                    <div class="sol-sol-img-wrap">
                        <img src="camera-exterior.jpg" alt="Exterior Monitoring Camera">
                    </div>
                    <div class="sol-img-badge">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="12 6 12 12 16 14"/>
                        </svg>
                        <div>
                            <span>All-Weather</span>
                            <strong>Operation</strong>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SOLUTION 07-09 WHY CHOOSE SECTION
         ============================================================ -->
    <section class="sol-sol-section bg-white" style="padding-top:0;">
        <div class="sol-container">
            <div class="sol-why-choose sol-fade">
                <h3 class="sac-title" style="text-align:center; margin-bottom:32px;">Why Choose This Solution</h3>
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

start_marker = "<!-- ============================================================\n         SOLUTION 07 —"
end_marker = "<!-- ============================================================\n         WHY AARGEE"

pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)

if pattern.search(html):
    html = pattern.sub(new_html + "\n    " + end_marker, html)
    with open("solutions.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Replaced old Solution 07 with new massive sections successfully.")
else:
    print("Could not find the target section to replace.")
