from ast import pattern
from cgitb import text
import imp
from itertools import count
import  urllib.request as req
import ssl
import bs4

rawData = []
topMovie = []
goodMovie = []
badMovie = []
url = "https://www.ptt.cc/bbs/movie/index.html"

def getData(url):
    request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })

    context = ssl._create_unverified_context()

    with req.urlopen(request, context=context) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    # print(titles)
    for title in titles:
        if title.a != None:
            rawData.append(title.a.string)

    for element in rawData:
        if "好雷" in element:
            topMovie.append(element)
        
        elif "普雷" in element:
            goodMovie.append(element)
        
        elif "負雷" in element:
            badMovie.append(element)
    

    nextLink = root.find("a", string = "‹ 上頁")
    return (nextLink["href"])



count = 0
while count < 10:
    url = "https://www.ptt.cc" + getData(url)
    count += 1

topMovie = list(set(topMovie))
topMovie = "\n".join(topMovie)

goodMovie = list(set(goodMovie))
goodMovie = "\n".join(goodMovie)

badMovie = list(set(badMovie))
badMovie = "\n".join(badMovie)

with open("MovieQuery.txt", "w", encoding = "utf-8") as file:
    file.write(topMovie)
    file.write(goodMovie)
    file.write(badMovie)
