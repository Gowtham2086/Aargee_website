import re

# Read solutions.html
with open("solutions.html", "r", encoding="utf-8") as f:
    sol_content = f.read()

# Extract footer and scripts
footer_match = re.search(r'(<footer class="premium-footer">.*</html>)', sol_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

# Read industries.html
with open("industries.html", "r", encoding="utf-8") as f:
    ind_content = f.read()

# Append footer
if footer not in ind_content:
    with open("industries.html", "w", encoding="utf-8") as f:
        f.write(ind_content + "\n" + footer)
    print("Footer and scripts appended.")
else:
    print("Footer already exists.")
