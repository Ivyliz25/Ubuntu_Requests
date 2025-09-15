🟠 Ubuntu Image Fetcher

"I am because we are." – Ubuntu Philosophy

The Ubuntu Image Fetcher is a simple Python tool that allows you to mindfully collect images from the web, store them in an organized directory, and handle errors gracefully. Inspired by the spirit of Ubuntu, it emphasizes community, respect, sharing, and practicality.

✨ Features

✅ Download one or multiple images from given URLs (comma-separated input).

✅ Automatically creates a Fetched_Images/ directory if it doesn’t exist.

✅ Extracts filenames from URLs or generates a default one.

✅ Prevents overwriting duplicates by adding _1, _2, etc.

✅ Handles HTTP errors and unexpected issues gracefully.

✅ Saves files in binary mode for accuracy.

📂 Project Structure
Ubuntu_Requests/
│── fetcher.py        # Main Python script
│── Fetched_Images/   # Directory where images are stored (auto-created)
│── README.md         # Documentation

🚀 Usage
1️⃣ Install dependencies

Make sure you have Python 3 installed. Install the required library:

pip install requests

2️⃣ Run the program
python fetcher.py

3️⃣ Enter URLs

When prompted, enter one or more image URLs separated by commas:

Please enter image URLs (comma separated): 
https://example.com/ubuntu1.jpg, https://example.com/ubuntu2.png

✅ Example Output
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

✓ Successfully fetched: ubuntu1.jpg
✓ Image saved to Fetched_Images/ubuntu1.jpg

✓ Successfully fetched: ubuntu2.png
✓ Image saved to Fetched_Images/ubuntu2.png

Connection strengthened. Community enriched.

🔒 Error Handling & Precautions

If a connection fails → a clear error message is shown.

If the file already exists → a new unique filename is generated.

If the URL is invalid or not an image → the script fails gracefully without crashing.

🌍 Ubuntu Principles in Action

Community → Connects to the wider web community by fetching shared resources.

Respect → Handles errors gracefully, without breaking.

Sharing → Organizes images for later use.

Practicality → Creates a simple but useful tool.

🛠️ Future Enhancements

Check MIME type before saving (to ensure it’s an image).

Support for downloading images from text files with multiple URLs.

Option to rename images on download.

📜 License

This project is open-source and free to use, modify, and share.

"A person is a person through other persons." – Ubuntu Philosophy
