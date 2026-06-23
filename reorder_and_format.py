import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract all sections
# They are delimited by HTML comments <!-- ====== SOLUTION XX ====== -->
# We will match from one comment up to the next.

pattern = re.compile(r'(<!-- ============================================================\s*SOLUTION \d+.*?============================================================ -->\s*<section class="sol-sol-section[^"]*" id="sol\d+">.*?</section>)', re.DOTALL)

sections = re.findall(pattern, html)

# 2. Map titles to their section HTML
section_map = {}
for s in sections:
    title_match = re.search(r'<h[23] class="sol-sol-title[^>]*>(.*?)</h[23]>', s)
    if title_match:
        # decode html entities just in case for matching
        title_str = title_match.group(1).replace('&amp;', '&').strip()
        section_map[title_str] = s

# 3. Define the desired order of titles
desired_order = [
    "Passenger Information Systems",
    "Intelligent Lighting Solutions",
    "Driver Safety & Monitoring Systems",
    "Passenger Safety Systems",
    "Alcohol Interlock Systems",
    "Passenger Comfort & Entertainment",
    "AI Passenger Counting System",
    "Interior Monitoring Camera",
    "Exterior Monitoring Camera"
]

# 4. Generate the new HTML for each section with correct formatting
backgrounds = ["bg-white", "bg-grey", "bg-dark"] * 3
new_sections_html = []

for i, title in enumerate(desired_order):
    if title not in section_map:
        print(f"Error: Could not find section '{title}'")
        exit(1)
        
    s = section_map[title]
    
    # Update Section Header Comment
    s = re.sub(r'SOLUTION \d+.*?(?=\s*===)', f'SOLUTION {i+1:02d} — {title}', s)
    
    # Update ID
    # Since original IDs were sol01... but there might be gaps, let's just use sol01 to sol09
    s = re.sub(r'id="sol\d+"', f'id="sol{i+1:02d}"', s)
    
    # Update Background
    s = re.sub(r'<section class="sol-sol-section [^"]*"', f'<section class="sol-sol-section {backgrounds[i]}"', s)
    
    # Update sol-sol-num
    s = re.sub(r'<div class="sol-sol-num.*?">.*?</div>', f'<div class="sol-sol-num{" dark" if backgrounds[i]=="bg-dark" else ""}">{i+1:02d}</div>', s)
    
    # Update reverse
    if i % 2 == 1: # Reverse every alternating section
        if 'class="sol-sol-inner"' in s:
            s = s.replace('class="sol-sol-inner"', 'class="sol-sol-inner reverse"')
    else:
        if 'class="sol-sol-inner reverse"' in s:
            s = s.replace('class="sol-sol-inner reverse"', 'class="sol-sol-inner"')
            
    # Update White/Dark Text Classes
    if backgrounds[i] == "bg-dark":
        # Add white to h2/h3
        s = re.sub(r'<h([23]) class="sol-sol-title">', r'<\1 class="sol-sol-title white">', s)
        # Add white to desc
        s = re.sub(r'<p class="sol-sol-desc">', r'<p class="sol-sol-desc white">', s)
        # Add white to feat-list
        s = re.sub(r'<ul class="sol-feat-list">', r'<ul class="sol-feat-list white">', s)
        # Add sol-lbl white
        s = re.sub(r'<div class="sol-lbl">', r'<div class="sol-lbl" style="color: rgba(255,255,255,0.7);">', s)
    else:
        # Remove white from h2/h3
        s = re.sub(r'<h([23]) class="sol-sol-title white">', r'<\1 class="sol-sol-title">', s)
        # Remove white from desc
        s = re.sub(r'<p class="sol-sol-desc white">', r'<p class="sol-sol-desc">', s)
        # Remove white from feat-list
        s = re.sub(r'<ul class="sol-feat-list white">', r'<ul class="sol-feat-list">', s)
        # Remove sol-lbl inline style if it exists
        s = re.sub(r'<div class="sol-lbl" style="color: rgba\(255,255,255,0.7\);">', r'<div class="sol-lbl">', s)
        
    new_sections_html.append(s)

# 5. Replace the chunk in the original HTML
# Find where the first section starts and where the last section ends
first_section_match = re.search(pattern, html)
if not first_section_match:
    print("Could not find start of sections")
    exit(1)
    
# We want to replace everything from the start of the first section
# down to right before "SOLUTION 07-09 WHY CHOOSE SECTION" or "WHY AARGEE"
split_pattern = r'(<!-- ============================================================\s*SOLUTION 01.*?)(?=<!-- ============================================================\s*SOLUTION 07-09 WHY CHOOSE SECTION|<!-- ============================================================\s*WHY AARGEE)'

parts = re.split(split_pattern, html, flags=re.DOTALL)
if len(parts) >= 3:
    new_html = parts[0] + "\n".join(new_sections_html) + "\n    " + parts[2]
    with open("solutions.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Reordered and reformatted successfully!")
else:
    print("Could not split HTML correctly.")
