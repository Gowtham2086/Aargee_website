import re

with open('manufacturing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace div placeholders with image tags
html = re.sub(
    r'<div style="[^"]*?">mfg-hero-bg\.jpg</div>',
    r'<img src="mfg-hero-bg.jpg" alt="Manufacturing Facility">',
    html
)

html = re.sub(
    r'<div style="[^"]*?">mfg-innovation-img\.jpg</div>',
    r'<img src="mfg-innovation-img.jpg" alt="Engineering and Development">',
    html
)

html = re.sub(
    r'<div style="[^"]*?">mfg-fabrication-img\.jpg</div>',
    r'<img src="mfg-fabrication-img.jpg" alt="Fabrication">',
    html
)

for i in range(1, 7):
    html = re.sub(
        r'<div style="[^"]*?">mfg-gallery-' + str(i) + r'\.jpg</div>',
        r'<img src="mfg-gallery-' + str(i) + r'.jpg" alt="Manufacturing Gallery ' + str(i) + r'">',
        html
    )

with open('manufacturing.html', 'w', encoding='utf-8') as f:
    f.write(html)
