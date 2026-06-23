import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

titles = re.findall(r'<h2 class="sol-sol-title[^>]*>(.*?)</h2>', html)
for i, t in enumerate(titles):
    print(f"Solution {i+1}: {t}")
