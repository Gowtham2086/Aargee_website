import re

with open("solutions.html", "r", encoding="utf-8") as f:
    html = f.read()

# We will match the sections based on the `<section class="sol-sol-section...` tag directly.
# And we'll consume the preceding HTML comment if it exists so we can replace it.
pattern = re.compile(r'(?:<!--.*?-->\s*)*<section class="sol-sol-section[^"]*" id="sol\d+">.*?</section>', re.DOTALL)

sections = re.findall(pattern, html)

section_map = {}
for s in sections:
    title_match = re.search(r'<h[23] class="sol-sol-title[^>]*>(.*?)</h[23]>', s)
    if title_match:
        # Decode entities and remove newlines/spaces
        title_str = title_match.group(1).replace('&amp;', '&').strip()
        section_map[title_str] = s

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

backgrounds = ["bg-white", "bg-grey", "bg-dark"] * 3
new_sections_html = []

for i, title in enumerate(desired_order):
    if title not in section_map:
        print(f"Error: Could not find section '{title}'")
        print("Available titles:", section_map.keys())
        exit(1)
        
    s = section_map[title]
    
    # Strip any existing HTML comments at the top of the block
    s = re.sub(r'^(?:<!--.*?-->\s*)*', '', s, flags=re.DOTALL)
    
    # Add our unified comment
    comment = f"    <!-- ============================================================\n         SOLUTION {i+1:02d} — {title}\n         ============================================================ -->\n    "
    s = comment + s
    
    # Update ID
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
        s = re.sub(r'<h([23]) class="sol-sol-title">', r'<\1 class="sol-sol-title white">', s)
        s = re.sub(r'<p class="sol-sol-desc">', r'<p class="sol-sol-desc white">', s)
        s = re.sub(r'<ul class="sol-feat-list">', r'<ul class="sol-feat-list white">', s)
        s = re.sub(r'<div class="sol-lbl">', r'<div class="sol-lbl" style="color: rgba(255,255,255,0.7);">', s)
    else:
        s = re.sub(r'<h([23]) class="sol-sol-title white">', r'<\1 class="sol-sol-title">', s)
        s = re.sub(r'<p class="sol-sol-desc white">', r'<p class="sol-sol-desc">', s)
        s = re.sub(r'<ul class="sol-feat-list white">', r'<ul class="sol-feat-list">', s)
        s = re.sub(r'<div class="sol-lbl" style="color: rgba\(255,255,255,0.7\);">', r'<div class="sol-lbl">', s)
        
    new_sections_html.append(s)

# Replace everything from the first section to the end of the last section
split_pattern = r'((?:<!--.*?-->\s*)*<section class="sol-sol-section[^"]*" id="sol\d+">.*?</section>)'
parts = re.split(split_pattern, html, flags=re.DOTALL)

# parts contains alternating [non-match, match, non-match, match...]
# The first match is at parts[1], the last match is at parts[-2]
if len(parts) >= 3:
    pre_html = parts[0]
    post_html = parts[-1]
    
    new_html = pre_html + "\n".join(new_sections_html) + "\n" + post_html
    with open("solutions.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Reordered and reformatted successfully!")
else:
    print("Could not split HTML correctly.")
