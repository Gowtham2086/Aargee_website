import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

# The solutions are bounded between <!-- ============================================================
#          SOLUTION XX
#          ============================================================ -->
# and the next one.
# Let's use re.split to split the document by these headers.

pattern = re.compile(r'(<!-- ============================================================\s*SOLUTION \d+.*?============================================================ -->\s*<section.*?id="sol\d+".*?</section>)', re.DOTALL)

parts = re.split(r'(<!-- ============================================================\s*SOLUTION 01.*?)(?=<!-- ============================================================\s*SOLUTION 07-09 WHY CHOOSE)', html, flags=re.DOTALL)
if len(parts) >= 3:
    pre_content = parts[0]
    solutions_content = parts[1]
    post_content = html[len(pre_content) + len(solutions_content):]
else:
    print("Could not parse main structure.")
    exit(1)

# Now extract all the individual solution sections from solutions_content
sections = re.findall(pattern, solutions_content)

if not sections:
    print("No sections found!")
    exit(1)

print(f"Found {len(sections)} sections.")
for i, s in enumerate(sections):
    title = re.search(r'<h[23] class="sol-sol-title[^>]*>(.*?)</h[23]>', s)
    title_str = title.group(1) if title else "Unknown"
    print(f"Section {i+1}: {title_str}")
