import urllib.request
import os

images = {
    "placeholder-hero.jpg": "https://picsum.photos/seed/mfg-hero/1920/1080",
    "placeholder-engineering.jpg": "https://picsum.photos/seed/mfg-eng/800/600",
    "placeholder-fabrication.jpg": "https://picsum.photos/seed/mfg-fab/800/600",
    "placeholder-gal1.jpg": "https://picsum.photos/seed/mfg-g1/600/400",
    "placeholder-gal2.jpg": "https://picsum.photos/seed/mfg-g2/600/400",
    "placeholder-gal3.jpg": "https://picsum.photos/seed/mfg-g3/600/400",
    "placeholder-gal4.jpg": "https://picsum.photos/seed/mfg-g4/600/400",
    "placeholder-gal5.jpg": "https://picsum.photos/seed/mfg-g5/600/400",
    "placeholder-gal6.jpg": "https://picsum.photos/seed/mfg-g6/600/400"
}

for filename, url in images.items():
    print(f"Downloading real photo for {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("All real photo placeholders downloaded.")
