from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.ycombinator.com/jobs")
bsObj = BeautifulSoup(html, "lxml")

for child in bsObj.find("table", {"id": "hnmain"}).children:
    print("THIS IS A CHILD:")
    print(child)

for descendant in bsObj.find("table", {"id": "hnmain"}).descendants:
    print("THIS IS A DESCENDANT:")
    print(descendant)

for sibling in bsObj.find("table", {"id": "hnmain"}).tr.next_siblings:
    # Objects cannot be siblings with themselves.
    # Any time you get siblings of an object, the object itself will not be included.
    # This function calls next siblings only.
    # The is also a previous_siblings function.
    print("THIS IS A SIBLING:")
    print(sibling)

#Selects the img tag, goes back to its parent and then to the previous sibling of its parent.
#print(bsObj.find("img", {"src":"www.google.com/img"})).parent.previous_sibling.get_text()) 

#print(bsObj.body.h1) #selects the first h1 tag that is a descendant (child) of the body tag
#print(img for img in bsObj.div.findAll("img")) #selects all img tags that are descendant of the first div tag

#To make your scrapers more robust, it's best to be as specific as possible,
#when making tag selections.
