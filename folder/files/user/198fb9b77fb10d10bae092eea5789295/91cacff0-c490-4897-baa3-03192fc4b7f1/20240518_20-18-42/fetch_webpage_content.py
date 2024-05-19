# filename: fetch_webpage_content.py
import requests

def fetch_and_save_webpage_content(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        return f"Content saved to {filename}"
    except requests.RequestException as e:
        return str(e)

# The URL of the webpage to fetch
url = "https://microsoft.github.io/autogen/docs/Examples/"

# The filename to save the content
filename = "webpage_content.txt"

# Fetch and save the content of the webpage
result_message = fetch_and_save_webpage_content(url, filename)
print(result_message)