import re

# Update HTML
with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

# Change the section class from bg-dark to bg-white
html = html.replace('<section class="sol-sol-section bg-dark" id="sol09">', '<section class="sol-sol-section bg-white" id="sol09">')

# Change h2 class to remove 'white' class
html = html.replace('<h2 class="sol-h2 white" style="text-align:center;">Intelligent Camera & Passenger Analytics Solutions</h2>', '<h2 class="sol-h2" style="text-align:center;">Intelligent Camera & Passenger Analytics Solutions</h2>')

# Change p class from sol-why-body to sol-sol-desc
html = html.replace('<p class="sol-why-body" style="text-align:center; max-width:800px; margin: 0 auto;">', '<p class="sol-sol-desc" style="text-align:center; max-width:800px; margin: 0 auto;">')

# Remove inline color:#fff from Why Choose Title
html = html.replace('<h3 class="sac-title" style="text-align:center; margin-bottom:32px; color:#fff;">', '<h3 class="sac-title" style="text-align:center; margin-bottom:32px;">')

with open("solutions.html", "w", encoding="utf-8") as f:
    f.write(html)


# Update CSS
with open("index.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS block for sol-analytics-card
css = css.replace('background: #111827; /* Dark luxury card background */', 'background: #ffffff; /* Light card background */')
css = css.replace('border: 1px solid rgba(255, 255, 255, 0.05);', 'border: 1px solid rgba(0, 0, 0, 0.08);')
css = css.replace('box-shadow: 0 24px 64px rgba(0, 0, 0, 0.4);', 'box-shadow: 0 24px 64px rgba(0, 0, 0, 0.08);')
css = css.replace('color: var(--white);', 'color: var(--dark);') # for sac-title
css = css.replace('color: var(--white-muted);', 'color: #4B5563;') # for sac-desc
css = css.replace('color: var(--white-soft);', 'color: #4B5563;') # for sol-feat-list and sw-item
css = css.replace('background: #111827;', 'background: #f9fafb;') # for sol-why-choose (assuming the previous replace was specific, let's be careful)

with open("index.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated Solution 07 to light theme successfully.")
