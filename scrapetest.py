from urllib.request import urlopen
html = urlopen("https://news.ycombinator.com/")
print(html.read())

#urllib documentation at https://docs.python.org/3/library/urllib.html
