from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://tj-sc.jusbrasil.com.br/jurisprudencia/6533938/recurso-criminal-rccr-797420-sc-2008079742-0?ref=serp"
html = urlopen(url)
bsObj = BeautifulSoup(html, "lxml")
regex = re.compile('.*JurisprudenceContent JurisprudencePage-content*')
result = [content.get_text() for content in bsObj.find_all("div", {"class" : regex})]
print(" ".join(result))


#myImgTag.attrs['src'] retrieves a python dictionary object with the source location for an image
