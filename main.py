from bs4 import BeautifulSoup
from urllib.request import urlopen

myurl = "https://www.gonaturalenglish.com/1000-most-common-words-in-the-english-language/"
html = urlopen(myurl).read()
soup = BeautifulSoup(html, "html.parser")

array = [];
links  = soup.find_all('li')
for link in links:
    print(link.text)
    array.append(link.text)

for i in range(1000):
    with open("file%03d.txt" % i, 'w', encoding='utf-8') as f:
        f.write(f"{array[i]}")