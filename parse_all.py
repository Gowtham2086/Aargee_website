import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

# Instead of looking at HTML comments, let's look at the <section class="sol-sol-section" ...> tags directly.
# Except, we don't want to match the "Why Choose" section or the footer.
# So we match sections that have an id matching sol\d+

sections_iter = re.finditer(r'(<!--.*?-->\s*)?<section class="sol-sol-section[^"]*" id="sol\d+">.*?</section>', html, re.DOTALL)

for match in sections_iter:
    s = match.group(0)
    title = re.search(r'<h[23] class="sol-sol-title[^>]*>(.*?)</h[23]>', s)
    title_str = title.group(1) if title else "Unknown"
    print(f"Title: {title_str}")
