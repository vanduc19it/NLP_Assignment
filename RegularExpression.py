
import re
import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen


# get số điện thoại và email
myurl = "http://doan1nam2.herokuapp.com/"
html = urlopen(myurl).read()
soup = BeautifulSoup(html, "html.parser")
links  = soup.find_all('span')
array = [];

for link in links:
    phone = re.findall("[0-9]{9}", link.text)
    email = re.findall("[a-z0-9][a-z0-9-.]*@[a-z0-9-.]+",link.text)
    if phone != []:
        print(phone)
    if email != []:
        print(email)

#get link 
f = open("file003.txt", "r", encoding="utf-8")
text = str(f.read())

href_link = re.search('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', text).group()
print(href_link)

#delete các thẻ HTML
f = open("file004.txt", "r", encoding="utf-8")
tag = str(f.read())
pattern = '<[^<]+>'
repl = ''
print(re.sub(pattern,repl, tag))





