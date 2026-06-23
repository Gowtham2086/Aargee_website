import glob
import re

css_addition = """
.nav-tagline {
    color: #FFFFFF;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.65rem;
    letter-spacing: 1.5px;
    margin-top: 5px;
    text-align: center;
    white-space: nowrap;
}
"""

with open('index.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.nav-tagline' not in css_content:
    with open('index.css', 'a', encoding='utf-8') as f:
        f.write(css_addition)

for html_file in glob.glob("*.html"):
    if html_file == "logo-section.html": continue
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<span class="nav-tagline">' not in content:
        content = re.sub(
            r'(<img[^>]*class="logo-img"[^>]*src="aargee-logo\.png\?v=3"[^>]*>)',
            r'\1\n                <span class="nav-tagline">Engineering Power. Enabling Progress.</span>',
            content
        )
    
    content = re.sub(
        r'<h3>AARGEE EQUIPMENT PVT\. LTD\.</h3>\s*<span class="pf-tagline">[^<]+</span>',
        '',
        content
    )
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Updated navbars and footers")
