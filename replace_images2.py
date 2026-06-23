import re

def replace_images():
    with open('manufacturing.html', 'r', encoding='utf-8') as f:
        content = f.read()

    images = [
        "placeholder-industry-intro.jpg",
        "camera-ai.jpg",
        "placeholder-engineering.jpg",
        "camera-exterior.jpg",
        "placeholder-company-photo.jpg",
        "placeholder-lighting.jpg",
        "camera-interior.jpg",
        "placeholder-cctv.jpg",
        "placeholder-safety.jpg",
        "perfect-engineering.png"
    ]

    for img in images:
        content = content.replace(f'src="{img}"', 'src="pis-placeholder.png"')

    with open('manufacturing.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    replace_images()
