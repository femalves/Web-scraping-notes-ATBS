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
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.title
        content = bsObj.table
    except AttributeError as e:
        return None
    result = {'title': title, 'content': content}
    return result

content = getContent(url)
if content == None:
    print("Content could not be found")
else:
    print(content)
