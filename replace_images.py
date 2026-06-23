import re

def replace_images():
    with open('manufacturing.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all image src values with pis-placeholder.png except aargee-logo.png
    def replacer(match):
        if 'aargee-logo' in match.group(1):
            return match.group(0)
        return 'src="pis-placeholder.png"'

    content = re.sub(r'src="([^"]+?\.(jpg|png|jpeg))"', replacer, content)

    with open('manufacturing.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    replace_images()
