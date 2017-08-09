from bs4 import BeautifulSoup

import requests, os

headers = {
    'User-Agent': 'I\'m a vessel.',
    'From': 'bloopetybleep@domain.com'
}

i = 0
output = ""
curr = "https://www.reddit.com/r/Showerthoughts/top/"

while True:
    if i > 50:
        break

    r  = requests.get(curr, headers = headers)
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for link in soup.find_all("p", {"class": "title"}):
        output += link.find_all("a")[0].string + "\n"

    try:
        curr = soup.find_all("a", {"rel": "next"})[0].get("href")

    except IndexError:
        break

    else:
        i += 1




with open("text.txt", "w") as f:
    f.write(output)

os.system("python3 mark.py")
