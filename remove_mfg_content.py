import re

with open("manufacturing.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract everything before the first split-section (which includes head and navbar)
head_nav_match = re.search(r'(.*?)</nav>', html, re.DOTALL)
head_nav = head_nav_match.group(1) + "</nav>" if head_nav_match else ""

# Extract the footer and everything after
footer_match = re.search(r'(<!-- PREMIUM FOOTER -->.*)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

# Reconstruct the HTML
new_html = head_nav + "\n\n<!-- Content removed as requested -->\n<div style=\"min-height: 60vh; display:flex; align-items:center; justify-content:center;\">\n    <h1 style=\"font-family:'Outfit',sans-serif; color:#ccc;\">Manufacturing Page Content Cleared</h1>\n</div>\n\n" + footer

with open("manufacturing.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Manufacturing content removed.")
