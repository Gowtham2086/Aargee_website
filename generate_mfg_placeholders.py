import urllib.request
import os

images = {
    "placeholder-hero.jpg": "https://placehold.co/1920x1080/08080a/ffffff.jpg?text=Manufacturing+Hero",
    "placeholder-engineering.jpg": "https://placehold.co/800x600/111827/ffffff.jpg?text=Engineering+and+Development",
    "placeholder-fabrication.jpg": "https://placehold.co/800x600/111827/ffffff.jpg?text=Workshop+and+Fabrication",
    "placeholder-gal1.jpg": "https://placehold.co/600x400/374151/ffffff.jpg?text=Production+Floor",
    "placeholder-gal2.jpg": "https://placehold.co/600x400/374151/ffffff.jpg?text=Assembly+Operations",
    "placeholder-gal3.jpg": "https://placehold.co/600x400/374151/ffffff.jpg?text=LED+Manufacturing",
    "placeholder-gal4.jpg": "https://placehold.co/600x400/374151/ffffff.jpg?text=Mechanical+Fabrication",
    "placeholder-gal5.jpg": "https://placehold.co/600x400/374151/ffffff.jpg?text=Quality+Inspection",
    "placeholder-gal6.jpg": "https://placehold.co/600x400/374151/ffffff.jpg?text=Engineering+Teams"
}

for filename, url in images.items():
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

print("All placeholders downloaded.")
