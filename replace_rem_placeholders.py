import re

with open("solutions.html", "r", encoding="utf-8") as f:
    content = f.read()

# Solution 03: Passenger Safety Systems
content = re.sub(
    r'<div class="sol-img-placeholder">\s*<svg[\s\S]*?</svg>\s*<p>Passenger Safety Systems</p>\s*</div>',
    '<img src="placeholder-safety.jpg" alt="Passenger Safety Systems">',
    content
)

# Solution 04: Alcohol Interlock Systems
content = re.sub(
    r'<div class="sol-img-placeholder dark-bg">\s*<svg[\s\S]*?</svg>\s*<p>Alcohol Interlock Systems</p>\s*</div>',
    '<img src="placeholder-interlock.jpg" alt="Alcohol Interlock Systems">',
    content
)

# Solution 05: Comfort & Entertainment
content = re.sub(
    r'<div class="sol-img-placeholder">\s*<svg[\s\S]*?</svg>\s*<p>Comfort &amp; Entertainment</p>\s*</div>',
    '<img src="placeholder-comfort.jpg" alt="Passenger Comfort & Entertainment">',
    content
)

# Solution 06: Intelligent LED Lighting
content = re.sub(
    r'<div class="sol-img-placeholder">\s*<svg[\s\S]*?</svg>\s*<p>Intelligent LED Lighting</p>\s*</div>',
    '<img src="placeholder-lighting.jpg" alt="Intelligent Lighting Solutions">',
    content
)

with open("solutions.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Placeholders replaced.")
