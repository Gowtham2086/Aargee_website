import re

with open("solutions.html", "r", encoding="utf-8") as f:
    content = f.read()

# We want to change:
# <div class="sol-sol-img-wrap">
#   <img ...> (or <div class="sol-img-placeholder">...</div>)
#   <div class="sol-img-badge">...</div>
# </div>
#
# TO:
# <div class="sol-image-container">
#   <div class="sol-sol-img-wrap">
#     <img ...> (or <div class="sol-img-placeholder">...</div>)
#   </div>
#   <div class="sol-img-badge">...</div>
# </div>

# Let's use a regex that matches the div.sol-sol-img-wrap and its contents up to the start of sol-img-badge,
# then matches the sol-img-badge, and wraps them appropriately.

pattern = re.compile(
    r'(<div class="sol-sol-img-wrap">)\s*([\s\S]*?)\s*(<div class="sol-img-badge">[\s\S]*?</div>\s*</div>)',
    re.IGNORECASE
)

# Wait, the closing </div> of sol-img-badge is followed by another </div> for sol-sol-img-wrap.
# The inner content might contain nested divs (like sol-img-placeholder has a div inside it? No, sol-img-placeholder doesn't have nested divs other than itself).
# Actually, it's safer to just split by `<div class="sol-img-badge">`

def replacer(match):
    wrap_open = match.group(1)
    img_content = match.group(2)
    # The badge starts with <div class="sol-img-badge">
    # We need to extract the badge and the closing </div> of the wrap
    badge_and_close = match.group(3)
    
    # We remove the trailing </div> from badge_and_close which belonged to sol-sol-img-wrap
    badge_content = badge_and_close.rsplit('</div>', 1)[0]
    
    new_html = f'''<div class="sol-image-container">
                    {wrap_open}
                        {img_content}
                    </div>
                    {badge_content}
                </div>'''
    return new_html

new_content = pattern.sub(replacer, content)

# Now we need to modify the CSS for sol-img-badge in solutions.html
css_pattern = r'(\.sol-img-badge\s*\{[\s\S]*?)\n\s*position:\s*absolute;[\s\S]*?right:\s*24px;'
css_replacement = r'''\1
            position: relative;
            margin-top: 20px;
            width: fit-content;'''
new_content = re.sub(r'\.sol-img-badge\s*\{[\s\S]*?gap:\s*8px;\s*\}', r'''.sol-img-badge {
            position: relative;
            margin-top: 16px;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(200, 16, 46, 0.2);
            border-radius: 8px;
            padding: 10px 20px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        }''', new_content)

with open("solutions.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done")
