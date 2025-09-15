import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        # Fetch the image
        response = requests.get(url.strip(), timeout=10)
        response.raise_for_status()  # Raise exception for bad HTTP status codes

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Prevent overwriting duplicates by appending a number if file exists
        filepath = os.path.join("Fetched_Images", filename)
        base, ext = os.path.splitext(filepath)
        counter = 1
        while os.path.exists(filepath):
            filepath = f"{base}_{counter}{ext}"
            counter += 1

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {os.path.basename(filepath)}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An unexpected error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for multiple image URLs
    urls = input("Please enter image URLs (comma separated): ").split(",")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        if url.strip():  # Skip empty entries
            fetch_image(url.strip())

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
