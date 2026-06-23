import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

# AI Passenger Counting
ai_placeholder = """<div class="sol-img-placeholder">
                            <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="1.2" opacity="0.4">
                                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
                                <circle cx="9" cy="7" r="4" />
                                <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
                                <path d="M16 3.13a4 4 0 0 1 0 7.75" />
                            </svg>
                            <p>AI Passenger Counting</p>
                        </div>"""
html = html.replace('<img src="placeholder-ai-count.jpg" alt="AI Passenger Counting System">', ai_placeholder)

# Interior Camera
interior_placeholder = """<div class="sol-img-placeholder">
                            <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="1.2" opacity="0.4">
                                <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
                                <circle cx="12" cy="13" r="4" />
                            </svg>
                            <p>Interior Monitoring</p>
                        </div>"""
html = html.replace('<img src="placeholder-interior-cam.jpg" alt="Interior Monitoring Camera">', interior_placeholder)

# Exterior Camera
exterior_placeholder = """<div class="sol-img-placeholder">
                            <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#C8102E" stroke-width="1.2" opacity="0.4">
                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                                <circle cx="12" cy="12" r="3" />
                            </svg>
                            <p>Exterior Monitoring</p>
                        </div>"""
html = html.replace('<img src="placeholder-exterior-cam.jpg" alt="Exterior Monitoring Camera">', exterior_placeholder)

with open("solutions.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added SVG placeholders successfully.")
