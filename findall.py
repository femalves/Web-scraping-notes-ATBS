from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/jobs"
def getContent(url):


    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:

        bsObj = BeautifulSoup(html, "lxml")
        nameList = bsObj.findAll(class_= "storylink")

        
        print(nameList[1].get_text())
    except AttributeError as e:
        return None


content = getContent(url)
