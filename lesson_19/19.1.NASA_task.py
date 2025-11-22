import requests
import random
import os

def get_data(url):
    response = requests.get(url)
    return response.json()

def extract_image_urls(data):
    images_urls = []

    items = data.get("collection", {}).get("items", [])
    for item in items:
        links = item.get("links", [])
        for link in links:
            href = link.get("href")
            if href and href.endswith((".jpg", ".jpeg", ".png")):
                images_urls.append(href)

    return images_urls

def choose_random_images(image_urls, count=3):
    return random.sample(image_urls, count)

def download_and_save_images(image_urls, folder="NASA_images"):
    os.makedirs(folder, exist_ok=True)

    for i, image_url in enumerate(image_urls, start=1):
        img_data = requests.get(image_url).content
        filename = os.path.join(folder, f"nasa_image_{i}.jpg")

        with open(filename, "wb") as f:
            f.write(img_data)

        print(f"Image saved: {filename} {image_url}")


def main():
    base_url = "https://images-api.nasa.gov/search?q=mars&media_type=image"

    data = get_data(base_url)

    images_urls = extract_image_urls(data)
    print(f"Found {len(images_urls)} images")

    selected = choose_random_images(images_urls, 3)

    download_and_save_images(selected)


if __name__ == "__main__":
    main()



