from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
def getContent(url):


    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:

        bsObj = BeautifulSoup(html, "lxml")
        nameList = bsObj.findAll("a", {"class": "storylink"})
        #get_text() strips all tags form the document and returns a string containing text only
        result = [name.get_text() for name in nameList]
    except AttributeError as e:
        return None
    return result

content = getContent(url)
if content == None:
    print("Content could not be found")
else:
    print(content)
