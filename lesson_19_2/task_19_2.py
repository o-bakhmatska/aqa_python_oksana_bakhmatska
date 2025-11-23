import requests
import urllib.parse
from config import BASE_URL, IMAGES_DIR

def upload_image(path_to_file):
    url = f"{BASE_URL}/upload"
    with open(path_to_file, "rb") as f:
        files = {"image": f}
        response = requests.post(url, files=files)

    print("UPLOAD STATUS:", response.status_code)
    print("UPLOAD RESPONSE:", response.json())
    return response.json().get("image_url")


def get_image_info(file_name):
    encoded_name = urllib.parse.quote(file_name)
    url = f"{BASE_URL}/image/{encoded_name}"

    headers = {"Content-Type": "text"}
    response = requests.get(url, headers=headers)

    print("GET STATUS:", response.status_code)
    print("GET RESPONSE:", response.json())
    return response.json().get("image_url")


def delete_image(file_name):
    encoded_name = urllib.parse.quote(file_name)
    url = f"{BASE_URL}/delete/{encoded_name}"

    response = requests.delete(url)

    print("DELETE STATUS:", response.status_code)
    print("DELETE RESPONSE:", response.json())


if __name__ == "__main__":

    local_file = IMAGES_DIR / "IMG_20230218_114720.jpg"

    print("\n1. UPLOADING... ")
    uploaded_url = upload_image(local_file)

    filename = uploaded_url.split("/")[-1]

    print("\n2. GET INFO...")
    get_image_info(filename)

    print("\n3. DELETING...")
    delete_image(filename)
