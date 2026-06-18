import re

file_path = "solutions.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Industries We Serve placeholders
content = re.sub(
    r'<div class="sol-ind-imgbox">[\s\S]*?</svg>\s*</div>',
    '<img src="placeholder-road.jpg" alt="Roadways Placeholder" class="sol-ind-imgbox" style="object-fit:cover; width:100%; height:200px; padding:0; border:none; background:#eee;">',
    content,
    count=1
)

content = re.sub(
    r'<div class="sol-ind-imgbox">[\s\S]*?</svg>\s*</div>',
    '<img src="placeholder-rail.jpg" alt="Railways Placeholder" class="sol-ind-imgbox" style="object-fit:cover; width:100%; height:200px; padding:0; border:none; background:#eee;">',
    content,
    count=1
)

content = re.sub(
    r'<div class="sol-ind-imgbox">[\s\S]*?</svg>\s*</div>',
    '<img src="placeholder-air.jpg" alt="Airways Placeholder" class="sol-ind-imgbox" style="object-fit:cover; width:100%; height:200px; padding:0; border:none; background:#eee;">',
    content,
    count=1
)

content = re.sub(
    r'<div class="sol-ind-imgbox">[\s\S]*?</svg>\s*</div>',
    '<img src="placeholder-water.jpg" alt="Waterways Placeholder" class="sol-ind-imgbox" style="object-fit:cover; width:100%; height:200px; padding:0; border:none; background:#eee;">',
    content,
    count=1
)

# Replace remaining Solutions placeholders
content = re.sub(
    r'<div class="sol-img-placeholder">[\s\S]*?</svg>\s*<p>Vehicle Tracking .*?</p>\s*</div>',
    '<img src="placeholder-tracking.jpg" alt="Vehicle Tracking System">',
    content
)

content = re.sub(
    r'<div class="sol-img-placeholder">[\s\S]*?</svg>\s*<p>Driver Monitoring .*?</p>\s*</div>',
    '<img src="placeholder-dms.jpg" alt="Driver Monitoring Systems">',
    content
)

content = re.sub(
    r'<div class="sol-img-placeholder">[\s\S]*?</svg>\s*<p>LED Destination .*?</p>\s*</div>',
    '<img src="placeholder-led.jpg" alt="LED Destination Boards">',
    content
)

content = re.sub(
    r'<div class="sol-img-placeholder">[\s\S]*?</svg>\s*<p>Video Surveillance .*?</p>\s*</div>',
    '<img src="placeholder-cctv.jpg" alt="Video Surveillance Systems">',
    content
)

content = re.sub(
    r'<div class="sol-img-placeholder">[\s\S]*?</svg>\s*<p>Intelligent Transport .*?</p>\s*</div>',
    '<img src="placeholder-itms.jpg" alt="Intelligent Transport Management Systems">',
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Placeholders replaced.")
