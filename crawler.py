# Jonathan Young

import re
import bs4
from urllib.request import urlopen
import mechanicalsoup

        
def get_souped(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")
    print(soup.prettify())
    print(soup.findall("img"))
    print(soup.get_text())
    
    
def main():
    try:
        get_souped("http://olympus.realpython.org/profiles/dionysus")
    except:
        print("there has been an unexpected error, shutting down")


# for link in soup.find_all('a'):
#     print(link.get('href'))
# # http://example.com/elsie
# # http://example.com/lacie
# # http://example.com/tillie

# soup.title
# # <title>The Dormouse's story</title>

# soup.title.name
# # u'title'

# soup.title.string
# # u'The Dormouse's story'

# soup.title.parent.name
# # u'head'

# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# # u'title'

# soup.a
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# soup.find_all('a')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# soup.find(id="link3")
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

if __name__ == "__main__":
    main()
