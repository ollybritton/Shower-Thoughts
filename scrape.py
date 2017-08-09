from bs4 import BeautifulSoup

import requests, os

headers = {
    'User-Agent': 'I\'m a vessel.',
    'From': 'bloopetybleep@domain.com'
}

output = ""

for url in ["https://www.reddit.com/r/Showerthoughts/hot/", "https://www.reddit.com/r/Showerthoughts/new/", "https://www.reddit.com/r/Showerthoughts/rising/"]:
    r  = requests.get(url, headers = headers)
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for link in soup.find_all("p", {"class": "title"}):
        output += link.find_all("a")[0].string + "\n"


with open("text.txt", "w") as f:
    f.write(output)

os.system("python3 mark.py")
