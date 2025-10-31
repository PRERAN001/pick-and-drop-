import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Samsung"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    blocks = soup.find_all('div')
    for block in blocks:
        span = block.find('span')
        small = block.find('small')
        links = block.find_all('a')
        text = span.get_text(strip=True) if span else None
        author = small.get_text(strip=True) if small else None
        tags = [tag.get_text(strip=True) for tag in links if tag.get_text(strip=True)]
        if text or author or tags:
            print(f"Text: {text}\nAuthor: {author}\nTags: {', '.join(tags)}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
