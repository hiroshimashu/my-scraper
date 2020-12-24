import requests
from bs4 import BeautifulSoup

url = "https://www.patentlyapple.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

entries = soup.find(class_ = "left-container-inner")

filename = "titles.txt"
with open(filename, "w") as f: 
    for title_element in entries.find_all(class_ = "entry-title"):
        title = title_element.find("a").text
        link = title_element.find("a").get("href")
        f.write("title: " + title + "\n")
        f.write("link: " + link + "\n") 
        f.write("\n")

    