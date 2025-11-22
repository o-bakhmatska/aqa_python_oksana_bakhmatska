import requests
import random
import os


base_url = "https://images-api.nasa.gov/search?q=mars&media_type=image"
response = requests.get(base_url)
data = response.json()

images_urls = []

items = data.get("collection", {}).get("items", [])

for item in items:
    links = item.get("links", [])
    for link in links:
        href = link.get("href")
        if href and href.endswith((".jpg", ".jpeg", ".png")):
            images_urls.append(href)

print(f"Found {len(images_urls)} images")

images_quantity = 3
images_selected = random.sample(images_urls, images_quantity)

folder = "NASA_images"
os.makedirs(folder, exist_ok=True)

for i, image_url in enumerate(images_selected, start=1):
    img_data = requests.get(image_url).content
    filename = os.path.join(folder, f"nasa_image_{i}.jpg")
    with open(filename, "wb") as f:
        f.write(img_data)

    print(f"Image saved: {filename} {image_url}")



