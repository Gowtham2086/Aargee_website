import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

sections_iter = re.finditer(r'<section class="sol-sol-section ([^"]*)" id="sol\d+">.*?</section>', html, re.DOTALL)

for match in sections_iter:
    s = match.group(0)
    bg = match.group(1)
    
    title = re.search(r'<h[23] class="sol-sol-title[^>]*>(.*?)</h[23]>', s)
    title_str = title.group(1) if title else "Unknown"
    
    is_reverse = "reverse" in s
    
    print(f"[{bg}] [Rev:{is_reverse}] {title_str}")
